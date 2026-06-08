#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/cass/.openclaw/workspace/littlelabcoats.co"
LOCK_FILE="$ROOT/data/stripe_auto_fulfillment.lock"
LOG_FILE="$ROOT/data/stripe-fulfillment-poller.log"
TMP_OUTPUT="$(mktemp)"

cleanup() {
  rm -f "$TMP_OUTPUT"
}
trap cleanup EXIT

export PATH="/usr/local/bin:/usr/bin:/bin"
cd "$ROOT"

if ! /usr/bin/flock -n "$LOCK_FILE" /usr/bin/python3 scripts/stripe_auto_fulfillment.py --json >"$TMP_OUTPUT" 2>&1; then
  {
    printf '[%s] ERROR\n' "$(date -Is)"
    cat "$TMP_OUTPUT"
    printf '\n'
  } >> "$LOG_FILE"
  exit 1
fi

if grep -q '"sentCount": 0' "$TMP_OUTPUT" && grep -q '"skippedCount": 0' "$TMP_OUTPUT"; then
  exit 0
fi

{
  printf '[%s]\n' "$(date -Is)"
  cat "$TMP_OUTPUT"
  printf '\n'
} >> "$LOG_FILE"
