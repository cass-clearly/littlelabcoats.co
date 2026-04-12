#!/usr/bin/env python3
import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Iterable
from urllib.parse import urlencode

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
BACKEND_BASE = os.environ.get("REMARQ_BACKEND_BASE", "http://192.168.5.204:3334")
PUBLIC_BASE = os.environ.get("LLC_PUBLIC_BASE", "https://littlelabcoats.co/lesson-plans")
FEEDBACK_SRC = os.environ.get("REMARQ_FEEDBACK_SRC", "https://cassclearly.com/feedback-layer.js?v=20260408")
API_URL = os.environ.get("REMARQ_API_URL", "https://cassclearly.com")
DEFAULT_CONTENT_SELECTOR = "body"

BODY_ID_RE = re.compile(r'<body[^>]*data-document-id="([^"]+)"', re.IGNORECASE)
BODY_TAG_RE = re.compile(r'<body[^>]*>', re.IGNORECASE)
STATIC_FEEDBACK_RE = re.compile(r'<script[^>]+src="https://cassclearly\.com/feedback-layer\.js\?v=20260408"[^>]*></script>', re.IGNORECASE)
REVIEW_GATED_RE = re.compile(r"window\.location\.search\.indexOf\('review=1'\)\s*!==\s*-1")
LOCAL_REVIEW_BOOTSTRAP_RE = re.compile(r"function\s+loadFeedbackLayer\s*\(")
SCRIPT_DOC_ID_RE = re.compile(r'<script[^>]+data-document-id="([^"]+)"[^>]*>', re.IGNORECASE)
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.IGNORECASE | re.DOTALL)
CANONICAL_RE = re.compile(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', re.IGNORECASE)

REVIEW_BOOTSTRAP = """<script>(function () {\n  function loadFeedbackLayer() {\n    var script = document.createElement('script');\n    script.src = '__FEEDBACK_SRC__';\n    script.dataset.apiUrl = '__API_URL__';\n    script.dataset.documentId = '__DOC_ID__';\n    script.dataset.contentSelector = '__CONTENT_SELECTOR__';\n    document.body.appendChild(script);\n  }\n\n  if (window.location.search.indexOf('review=1') !== -1) {\n    if (document.readyState === 'loading') {\n      document.addEventListener('DOMContentLoaded', loadFeedbackLayer, { once: true });\n    } else {\n      loadFeedbackLayer();\n    }\n  }\n})();</script>"""


def repo_path(raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve()


def extract_doc_id(text: str) -> str:
    match = BODY_ID_RE.search(text)
    if not match:
        raise ValueError("missing body data-document-id")
    return match.group(1)


def extract_script_doc_id(text: str) -> str | None:
    match = SCRIPT_DOC_ID_RE.search(text)
    if not match:
        return None
    return match.group(1)


def extract_title(text: str) -> str:
    match = TITLE_RE.search(text)
    if not match:
        return "Little Lab Coats lesson"
    return re.sub(r"\s+", " ", match.group(1)).strip()


def build_uri(path: Path, text: str) -> str:
    canonical_match = CANONICAL_RE.search(text)
    if canonical_match:
        return canonical_match.group(1)
    return f"{PUBLIC_BASE}/{path.name}"


def make_bootstrap(doc_id: str) -> str:
    return (
        REVIEW_BOOTSTRAP
        .replace("__FEEDBACK_SRC__", FEEDBACK_SRC)
        .replace("__API_URL__", API_URL)
        .replace("__DOC_ID__", doc_id)
        .replace("__CONTENT_SELECTOR__", DEFAULT_CONTENT_SELECTOR)
    )


def needs_gated_repair(text: str) -> bool:
    if LOCAL_REVIEW_BOOTSTRAP_RE.search(text):
        return False
    return bool(STATIC_FEEDBACK_RE.search(text))


def gate_feedback_loader(path: Path) -> bool:
    text = path.read_text()
    doc_id = extract_doc_id(text)
    if not needs_gated_repair(text):
        return False
    updated = STATIC_FEEDBACK_RE.sub(make_bootstrap(doc_id), text, count=1)
    if updated == text:
        raise RuntimeError(f"failed to gate feedback bootstrap in {path}")
    path.write_text(updated)
    return True


def fetch_text(url: str, session: requests.Session):
    response = session.get(url, timeout=20)
    return response.status_code, response.text


def verify_file(path: Path, session: requests.Session, skip_live: bool = False):
    text = path.read_text()
    doc_id = extract_doc_id(text)
    issues: list[str] = []
    script_doc_id = extract_script_doc_id(text)

    if script_doc_id and script_doc_id != doc_id:
        issues.append(f"script data-document-id mismatch: {script_doc_id} != {doc_id}")
    if STATIC_FEEDBACK_RE.search(text):
        issues.append("static feedback-layer.js include still present")
    if not REVIEW_GATED_RE.search(text):
        issues.append("missing ?review=1 gated review loader")
    if not LOCAL_REVIEW_BOOTSTRAP_RE.search(text):
        issues.append("missing inline review bootstrap function")

    backend = session.get(f"{BACKEND_BASE}/documents/{doc_id}", timeout=20)
    backend_status = backend.status_code
    if backend_status != 200:
        issues.append(f"backend GET /documents/{doc_id} returned {backend_status}")

    result = {
        "path": str(path.relative_to(REPO_ROOT)),
        "doc_id": doc_id,
        "backend_status": backend_status,
        "public_url": None,
        "public_status": None,
        "public_has_feedback_script": None,
        "review_url": None,
        "review_status": None,
        "review_has_feedback_script": None,
        "issues": issues,
    }

    if skip_live:
        return result

    slug = path.name
    cache_bust = urlencode({"cb": str(int(time.time()))})
    public_url = f"{PUBLIC_BASE}/{slug}?{cache_bust}"
    review_url = f"{PUBLIC_BASE}/{slug}?review=1&{cache_bust}"
    result["public_url"] = public_url
    result["review_url"] = review_url

    public_status, public_html = fetch_text(public_url, session)
    result["public_status"] = public_status
    if public_status != 200:
        issues.append(f"public URL returned {public_status}")
    else:
        live_doc_id = extract_doc_id(public_html)
        if live_doc_id != doc_id:
            issues.append(f"public HTML doc id mismatch: {live_doc_id} != {doc_id}")
        has_feedback = FEEDBACK_SRC in public_html
        result["public_has_feedback_script"] = has_feedback
        if has_feedback:
            issues.append("public HTML still contains feedback-layer script without review=1")

    review_status, review_html = fetch_text(review_url, session)
    result["review_status"] = review_status
    if review_status != 200:
        issues.append(f"review URL returned {review_status}")
    else:
        live_review_doc_id = extract_doc_id(review_html)
        if live_review_doc_id != doc_id:
            issues.append(f"review HTML doc id mismatch: {live_review_doc_id} != {doc_id}")
        has_review_feedback = FEEDBACK_SRC in review_html
        result["review_has_feedback_script"] = has_review_feedback
        if not has_review_feedback:
            issues.append("review HTML missing feedback-layer script")

    return result


def load_env(env_path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in env_path.read_text().splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        values[key] = value.strip().strip('"').strip("'")
    alias_map = {
        "POSTGRES_HOST": ["DB_HOST", "DATABASE_HOST"],
        "POSTGRES_PORT": ["DB_PORT", "DATABASE_PORT"],
        "POSTGRES_DB": ["DB_NAME", "DATABASE_NAME"],
        "POSTGRES_USER": ["DB_USER", "DATABASE_USER"],
        "POSTGRES_PASSWORD": ["DB_PASSWORD", "DATABASE_PASSWORD"],
    }
    for canonical, aliases in alias_map.items():
        if canonical in values:
            continue
        for alias in aliases:
            if alias in values:
                values[canonical] = values[alias]
                break
    return values


def sql_literal(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def build_insert_sql(rows: Iterable[dict[str, str]]) -> str:
    values = []
    for row in rows:
        values.append(
            "(" + ", ".join([
                sql_literal(row["doc_id"]),
                sql_literal(row["uri"]),
            ]) + ")"
        )
    values_sql = ",\n    ".join(values)
    return f"""
WITH input(id, uri) AS (
    VALUES
    {values_sql}
)
INSERT INTO documents (id, uri)
SELECT input.id,
       input.uri
FROM input
WHERE NOT EXISTS (
  SELECT 1 FROM documents d WHERE d.id = input.id
);
""".strip()


def run_psql(sql: str, env: dict[str, str]):
    command = [
        "psql",
        "-h",
        env.get("POSTGRES_HOST", "localhost"),
        "-p",
        env.get("POSTGRES_PORT", "5434"),
        "-U",
        env.get("POSTGRES_USER", "remarq"),
        "-d",
        env.get("POSTGRES_DB", "remarq"),
        "-v",
        "ON_ERROR_STOP=1",
        "-c",
        sql,
    ]
    child_env = os.environ.copy()
    child_env["PGPASSWORD"] = env["POSTGRES_PASSWORD"]
    return subprocess.run(command, env=child_env, check=True, capture_output=True, text=True)


def collect_rows(paths: list[Path]):
    rows = []
    for path in paths:
        text = path.read_text()
        doc_id = extract_doc_id(text)
        rows.append(
            {
                "path": path,
                "doc_id": doc_id,
                "uri": build_uri(path, text),
                "title": extract_title(text),
            }
        )
    return rows


def cmd_gate(args):
    changed = []
    for raw_path in args.paths:
        path = repo_path(raw_path)
        if gate_feedback_loader(path):
            changed.append(str(path.relative_to(REPO_ROOT)))
    for item in changed:
        print(item)
    return 0


def cmd_reconcile(args):
    env = load_env(repo_path(args.env_file))
    paths = [repo_path(raw_path) for raw_path in args.paths]
    rows = collect_rows(paths)
    sql = build_insert_sql(rows)
    if args.print_sql:
        print(sql)
        return 0
    try:
        result = run_psql(sql, env)
    except subprocess.CalledProcessError as exc:
        if exc.stdout:
            print(exc.stdout.strip())
        if exc.stderr:
            print(exc.stderr.strip(), file=sys.stderr)
        raise
    print(result.stdout.strip())
    return 0


def cmd_verify(args):
    session = requests.Session()
    results = []
    for raw_path in args.paths:
        path = repo_path(raw_path)
        try:
            results.append(verify_file(path, session, skip_live=args.skip_live))
        except Exception as exc:  # noqa: BLE001
            results.append({"path": raw_path, "issues": [f"verification error: {exc}"]})
    failures = [result for result in results if result.get("issues")]
    if args.json:
        print(json.dumps({"results": results, "ok": not failures}, indent=2))
    else:
        for result in results:
            print(f"{result['path']}: {'OK' if not result.get('issues') else 'FAIL'}")
            if result.get("doc_id"):
                print(f"  doc_id: {result['doc_id']}")
                print(f"  backend: {result['backend_status']}")
                if result.get("public_url"):
                    print(f"  public: {result['public_status']}  feedback={result['public_has_feedback_script']}  {result['public_url']}")
                if result.get("review_url"):
                    print(f"  review: {result['review_status']}  feedback={result['review_has_feedback_script']}  {result['review_url']}")
            for issue in result.get("issues", []):
                print(f"  issue: {issue}")
    return 1 if failures else 0


def build_parser():
    parser = argparse.ArgumentParser(description="Little Lab Coats Remarq batch verification and reconciliation tools.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    gate_parser = subparsers.add_parser("gate", help="Replace static feedback-layer includes with review-only bootstrap")
    gate_parser.add_argument("paths", nargs="+", help="HTML files to repair")
    gate_parser.set_defaults(func=cmd_gate)

    reconcile_parser = subparsers.add_parser("reconcile", help="Insert missing backend documents while preserving configured ids")
    reconcile_parser.add_argument("paths", nargs="+", help="HTML files to reconcile")
    reconcile_parser.add_argument("--env-file", default="/home/cass/.openclaw/workspace/remarq-production/.env")
    reconcile_parser.add_argument("--print-sql", action="store_true")
    reconcile_parser.set_defaults(func=cmd_reconcile)

    verify_parser = subparsers.add_parser("verify", help="Verify local/live/backend wiring for a batch")
    verify_parser.add_argument("paths", nargs="+", help="HTML files to verify")
    verify_parser.add_argument("--json", action="store_true")
    verify_parser.add_argument("--skip-live", action="store_true")
    verify_parser.set_defaults(func=cmd_verify)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
