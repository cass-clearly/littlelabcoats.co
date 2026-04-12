# Remarq infrastructure repair batch — 2026-04-12

## Scope
Repaired the non-owned missing-backend batches outside the active `gr5-ls1-unit2*` serial lane:

- `gr2-ets1-unit1*` (13 files)
- `gr4-ets1-unit1*` (13 files)
- `gr4-ess2-unit1*` (13 files)
- `gr4-ess1-unit1*` (8 files)
- `gr4-ps3-unit1*` (7 files)
- `gr5-ets1-unit1*` (13 files)

Total targeted files: **67**

## What changed
- Added `scripts/remarq_batch_tools.py`
  - `gate` mode: replaces static Remarq bootstrap with review-only inline bootstrap
  - `reconcile` mode: inserts missing production `documents` rows while preserving existing configured `data-document-id` values
  - `verify` mode: audits local wiring and backend document resolution, with optional live/public checks
- Kept `scripts/verify_remarq_batch.py` as a thin entrypoint wrapper around the shared tool
- Applied review-gated bootstrap wiring to all 67 targeted files so the feedback layer is only appended when `?review=1` is present in the local source
- Reconciled all 67 configured document IDs into production Remarq Postgres on `localhost:5434`

## Verification run
Local/backend verification command:

```bash
python3 scripts/remarq_batch_tools.py verify --json --skip-live \
  lesson-plans/gr2-ets1-unit1* \
  lesson-plans/gr4-ets1-unit1* \
  lesson-plans/gr4-ess2-unit1* \
  lesson-plans/gr4-ess1-unit1* \
  lesson-plans/gr4-ps3-unit1* \
  lesson-plans/gr5-ets1-unit1*
```

Result:

- **67/67 files passed** local wiring + backend checks
- **0 failures**
- All targeted `GET /documents/:id` checks now return **200** for the configured IDs

## Live spot check
Spot-checked these representative files with full live/public + live/review fetches:

- `lesson-plans/gr2-ets1-unit1-lesson1-define-the-bridge-problem.html`
- `lesson-plans/gr2-ets1-unit1-refcard-lesson1-define-the-bridge-problem.html`
- `lesson-plans/gr4-ess1-unit1-refcard.html`
- `lesson-plans/gr4-ps3-unit1-l2-collisions-transfer-energy.html`

Observed state during this pass:

- production backend lookup already returns **200** for each checked configured document ID
- public and review URLs return **200**
- public HTML still shows the old always-loaded feedback script, which means the site is still serving pre-push HTML at the time of the spot check

Status: **repo repair complete; live site still awaiting propagation at verification time**

## Notes
- No files matching `gr5-ls1-unit2*` were modified.
- This pass was wiring/infrastructure only; educational content was not rewritten.
