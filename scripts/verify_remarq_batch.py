#!/usr/bin/env python3
import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlencode

import requests

BACKEND_BASE = "http://192.168.5.204:3334"
PUBLIC_BASE = "https://littlelabcoats.co/lesson-plans"
FEEDBACK_SRC = "https://cassclearly.com/feedback-layer.js?v=20260408"

BODY_ID_RE = re.compile(r'<body[^>]*data-document-id="([^"]+)"', re.IGNORECASE)
STATIC_FEEDBACK_RE = re.compile(r'<script[^>]+src="https://cassclearly\.com/feedback-layer\.js\?v=20260408"', re.IGNORECASE)
GATED_REVIEW_RE = re.compile(r"window\.location\.search\.indexOf\('review=1'\)\s*===\s*-1", re.IGNORECASE)


def extract_doc_id(text: str) -> str:
    match = BODY_ID_RE.search(text)
    if not match:
        raise ValueError("missing body data-document-id")
    return match.group(1)


def extract_live_doc_id(text: str) -> str:
    match = BODY_ID_RE.search(text)
    if not match:
        raise ValueError("live HTML missing body data-document-id")
    return match.group(1)


def fetch_text(url: str, session: requests.Session):
    response = session.get(url, timeout=20)
    return response.status_code, response.text


def verify_file(path: Path, session: requests.Session):
    text = path.read_text()
    doc_id = extract_doc_id(text)
    issues = []

    if STATIC_FEEDBACK_RE.search(text):
        issues.append("static feedback-layer.js include still present")
    if not GATED_REVIEW_RE.search(text):
        issues.append("missing ?review=1-gated review loader")

    backend = session.get(f"{BACKEND_BASE}/documents/{doc_id}", timeout=20)
    if backend.status_code != 200:
        issues.append(f"backend GET /documents/{doc_id} returned {backend.status_code}")

    slug = path.name
    cache_bust = urlencode({"cb": str(int(time.time()))})
    public_url = f"{PUBLIC_BASE}/{slug}?{cache_bust}"
    review_url = f"{PUBLIC_BASE}/{slug}?review=1&{cache_bust}"

    public_status, public_html = fetch_text(public_url, session)
    if public_status != 200:
        issues.append(f"public URL returned {public_status}")
    else:
        live_doc_id = extract_live_doc_id(public_html)
        if live_doc_id != doc_id:
            issues.append(f"public HTML doc id mismatch: {live_doc_id} != {doc_id}")

    review_status, review_html = fetch_text(review_url, session)
    if review_status != 200:
        issues.append(f"review URL returned {review_status}")
    else:
        live_review_doc_id = extract_live_doc_id(review_html)
        if live_review_doc_id != doc_id:
            issues.append(f"review HTML doc id mismatch: {live_review_doc_id} != {doc_id}")

    return {
        "path": str(path),
        "doc_id": doc_id,
        "backend_status": backend.status_code,
        "public_url": public_url,
        "public_status": public_status,
        "review_url": review_url,
        "review_status": review_status,
        "issues": issues,
    }



def main():
    parser = argparse.ArgumentParser(description="Verify Remarq document wiring for Little Lab Coats batch files.")
    parser.add_argument("paths", nargs="+", help="Repo-relative lesson-plans HTML paths to verify")
    parser.add_argument("--json", action="store_true", help="Emit JSON summary")
    args = parser.parse_args()

    session = requests.Session()
    results = []
    for raw_path in args.paths:
        path = Path(raw_path)
        if not path.exists():
            results.append({"path": raw_path, "issues": ["file does not exist"]})
            continue
        try:
            results.append(verify_file(path, session))
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
                print(f"  public: {result['public_status']}  {result['public_url']}")
                print(f"  review: {result['review_status']}  {result['review_url']}")
            for issue in result.get("issues", []):
                print(f"  issue: {issue}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
