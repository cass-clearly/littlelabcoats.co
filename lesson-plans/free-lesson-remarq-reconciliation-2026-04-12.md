# Free Lesson Remarq Reconciliation — 2026-04-12

Last updated: 2026-04-12
Status: repair batch completed and pushed in commit `776aea0`
Scope: K–5 standalone free-lesson batch only; no active Grade 5 LS1 Unit 2 content files were touched

## Why this batch

This was selected directly from `lesson-plans/llc-remarq-review-audit-2026-04-12.md` as a high-leverage non-content repair target:
- the free-lesson batch already had repo-level Rachel + Margaret review proof in `lesson-plans/free-lesson-batch-review.md`
- Kindergarten through Grade 2 still pointed at placeholder-style document IDs that returned `404`
- the freebie pages were also still loading the review UI on normal public URLs instead of only on `?review=1`

## Files changed

### Source files
- all 18 free-batch artifacts:
  - `lesson-plans/k-milk-magic.html`
  - `lesson-plans/k-milk-magic-refcard.html`
  - `lesson-plans/k-milk-magic-quiz.html`
  - `lesson-plans/free-gr1-celery-rainbow.html`
  - `lesson-plans/free-gr1-celery-rainbow-refcard.html`
  - `lesson-plans/free-gr1-celery-rainbow-quiz.html`
  - `lesson-plans/free-gr2-salt-dough-fossil-factory.html`
  - `lesson-plans/free-gr2-salt-dough-fossil-factory-refcard.html`
  - `lesson-plans/free-gr2-salt-dough-fossil-factory-quiz.html`
  - `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
  - `lesson-plans/free-gr3-egg-drop-kitchen-challenge-refcard.html`
  - `lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html`
  - `lesson-plans/free-gr4-apple-oxidation.html`
  - `lesson-plans/free-gr4-apple-oxidation-refcard.html`
  - `lesson-plans/free-gr4-apple-oxidation-quiz.html`
  - `lesson-plans/free-gr5-bread-mold-terrarium.html`
  - `lesson-plans/free-gr5-bread-mold-terrarium-refcard.html`
  - `lesson-plans/free-gr5-bread-mold-terrarium-quiz.html`

### New durable artifacts
- `lesson-plans/free-lesson-document-id-manifest.md`
- `scripts/verify_remarq_batch.py`
- `lesson-plans/free-lesson-remarq-reconciliation-2026-04-12.md`

## Repair actions applied

1. Created or reconciled real backend documents for the canonical free-lesson URLs.
   - Kindergarten through Grade 2 got fresh real backend document IDs.
   - Grade 3 through Grade 5 already had resolving IDs; those were preserved.
2. Rewired each free-batch file’s `body[data-document-id]` to the real backend-backed ID recorded in `lesson-plans/free-lesson-document-id-manifest.md`.
3. Replaced the always-on static `feedback-layer.js` include with a `?review=1`-gated loader in all 18 free-batch files.
   - result: review controls stay off on the normal public freebie URLs
   - result: review controls still load on the canonical review URLs
4. Added `scripts/verify_remarq_batch.py` so later reconciliation passes can re-check:
   - local source gating state
   - backend document existence
   - public URL resolution
   - public/review HTML document-ID parity

## Verification evidence

### Backend + public HTML verification
After push, the first live pass still saw stale public HTML for the newly reconciled K–2 IDs.
A short wait/retry pass succeeded once propagation caught up.

Command used:
- `python3 scripts/verify_remarq_batch.py ...`

Verified result after propagation:
- all 18 free-batch artifacts returned `OK`
- each local source file had:
  - no always-on static feedback-layer include
  - a `?review=1`-gated review loader
  - a `body[data-document-id]` that resolves `200` from `http://192.168.5.204:3334/documents/:id`
- each public canonical URL returned `200`
- each public `?review=1` URL returned `200`
- public HTML and review HTML both exposed the expected reconciled `data-document-id`

### Browser-level review gating verification
Representative live browser checks were run with headless Chrome on one lesson, one refcard, and one quiz:
- lesson sample: `https://littlelabcoats.co/lesson-plans/k-milk-magic.html`
- refcard sample: `https://littlelabcoats.co/lesson-plans/free-gr1-celery-rainbow-refcard.html`
- quiz sample: `https://littlelabcoats.co/lesson-plans/free-gr2-salt-dough-fossil-factory-quiz.html`

Observed result on the live public site:
- normal URL: no Feedback tab / no review sidebar
- `?review=1` URL: Feedback tab + review sidebar present

That proves the repaired free-batch review controls are gated to review mode instead of leaking onto the default public routes.

## Batch disposition

Truthful current state after this repair batch:
- the free-lesson batch is now backend-reconciled at the document-ID level
- the free-lesson batch review UI is now gated to `?review=1`
- the repaired public and review routes resolve correctly on the live site
- this batch did not alter the active serial content-review lane
- broader non-free Grade 3 reviewed-batch reconciliation still remains for later passes
