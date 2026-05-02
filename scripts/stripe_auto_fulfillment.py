#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / 'ops' / 'product-fulfillment-map.json'
LOG_PATH = ROOT / 'data' / 'stripe-fulfillment-log.json'
ENV_PATH = Path('/home/cass/.openclaw/.env')
STRIPE_ITEM = 'Stripe - Little Lab Coats'
STRIPE_VAULT = 'Assistant'
SEND_ACCOUNT = 'clearlycass10@gmail.com'


def run(cmd, env=None):
    return subprocess.run(cmd, check=True, text=True, capture_output=True, env=env)


def load_env_file(path: Path):
    env = {}
    if not path.exists():
        return env
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def get_stripe_secret():
    if os.environ.get('STRIPE_SECRET_KEY'):
        return os.environ['STRIPE_SECRET_KEY']
    env = os.environ.copy()
    file_env = load_env_file(ENV_PATH)
    token = file_env.get('OP_SERVICE_ACCOUNT_TOKEN')
    if not token:
        raise RuntimeError('OP_SERVICE_ACCOUNT_TOKEN missing from ~/.openclaw/.env')
    env['OP_SERVICE_ACCOUNT_TOKEN'] = token
    proc = run([
        'op', 'item', 'get', STRIPE_ITEM,
        '--vault', STRIPE_VAULT,
        '--fields', 'credential',
        '--reveal',
    ], env=env)
    secret = proc.stdout.strip()
    if not secret:
        raise RuntimeError('Stripe secret not found in 1Password item')
    return secret


def stripe_request(secret, path, params=None):
    url = 'https://api.stripe.com' + path
    if params:
        url += '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url)
    auth = ('%s:' % secret).encode('utf-8')
    import base64
    req.add_header('Authorization', 'Basic ' + base64.b64encode(auth).decode('ascii'))
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode('utf-8'))


def load_map():
    data = json.loads(MAP_PATH.read_text())
    products = {}
    for entry in data['products']:
        payment_link_id = entry.get('paymentLinkId')
        if payment_link_id:
            products[payment_link_id] = entry
    return products


def load_log():
    if LOG_PATH.exists():
        return json.loads(LOG_PATH.read_text())
    return {'processedSessions': {}, 'lastRunAt': None}


def save_log(log):
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text(json.dumps(log, indent=2, sort_keys=True) + '\n')


def render_email(template_path: Path, customer_name: str):
    body = template_path.read_text()
    return body.replace('{{customer_name}}', customer_name or 'there')


def send_email(to_email: str, subject: str, body: str, dry_run=False):
    if dry_run:
        return {'dryRun': True}
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.txt') as tmp:
        tmp.write(body)
        tmp_path = tmp.name
    try:
        run([
            'gog', 'gmail', 'send',
            '--account', SEND_ACCOUNT,
            '--to', to_email,
            '--subject', subject,
            '--body-file', tmp_path,
        ])
    finally:
        try:
            os.unlink(tmp_path)
        except FileNotFoundError:
            pass
    return {'sent': True}


def process_events(secret, product_map, log, dry_run=False, limit=20, replay_session_ids=None):
    events = stripe_request(secret, '/v1/events', {
        'type': 'checkout.session.completed',
        'limit': limit,
    }).get('data', [])
    sent = []
    skipped = []
    replay_session_ids = set(replay_session_ids or [])
    for event in reversed(events):
        session = event.get('data', {}).get('object', {})
        session_id = session.get('id')
        if not session_id:
            continue
        if session_id in log['processedSessions'] and session_id not in replay_session_ids:
            continue
        if not session.get('livemode'):
            skipped.append({'sessionId': session_id, 'reason': 'not_live'})
            continue
        if session.get('payment_status') != 'paid':
            skipped.append({'sessionId': session_id, 'reason': 'not_paid'})
            continue
        payment_link_id = session.get('payment_link')
        if not payment_link_id:
            skipped.append({'sessionId': session_id, 'reason': 'missing_payment_link'})
            continue
        product = product_map.get(payment_link_id)
        if not product:
            skipped.append({'sessionId': session_id, 'reason': 'unmapped_payment_link', 'paymentLinkId': payment_link_id})
            continue
        customer = session.get('customer_details') or {}
        to_email = customer.get('email')
        if not to_email:
            skipped.append({'sessionId': session_id, 'reason': 'missing_customer_email'})
            continue
        template_path = ROOT / product['emailTemplatePath']
        body = render_email(template_path, customer.get('name') or '')
        send_email(to_email, product['draftSubject'], body, dry_run=dry_run)
        record = {
            'sessionId': session_id,
            'eventId': event.get('id'),
            'paymentLinkId': payment_link_id,
            'slug': product['slug'],
            'customerEmail': to_email,
            'customerName': customer.get('name'),
            'subject': product['draftSubject'],
            'downloadUrl': product.get('downloadUrl'),
            'sentAt': int(time.time()),
            'dryRun': dry_run,
        }
        log['processedSessions'][session_id] = record
        sent.append(record)
    log['lastRunAt'] = int(time.time())
    return sent, skipped


def main():
    parser = argparse.ArgumentParser(description='Send Little Lab Coats fulfillment emails for paid Stripe sessions.')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--limit', type=int, default=20)
    parser.add_argument('--replay-session', action='append', default=[])
    args = parser.parse_args()

    product_map = load_map()
    if not product_map:
        raise RuntimeError('No paymentLinkId mappings found in product-fulfillment-map.json')
    secret = get_stripe_secret()
    log = load_log()
    sent, skipped = process_events(
        secret,
        product_map,
        log,
        dry_run=args.dry_run,
        limit=args.limit,
        replay_session_ids=args.replay_session,
    )
    save_log(log)
    result = {
        'sentCount': len(sent),
        'sent': sent,
        'skippedCount': len(skipped),
        'skipped': skipped,
        'dryRun': args.dry_run,
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if sent:
            for item in sent:
                print(f"sent {item['slug']} -> {item['customerEmail']} ({item['sessionId']})")
        else:
            print('no new fulfillment emails to send')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        raise
