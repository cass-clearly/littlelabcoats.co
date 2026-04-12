# Free Lesson Document ID Manifest

Last updated: 2026-04-12
Status: canonical free-lesson batch document IDs reconciled to real backend records; review controls source-gated to `?review=1` across the free lesson set

## Scope

This manifest covers the full K–5 standalone free-lesson batch tracked in `lesson-plans/free-lesson-batch-review.md`:
- Kindergarten milk trio
- Grade 1 celery rainbow trio
- Grade 2 salt dough fossil trio
- Grade 3 egg-drop trio
- Grade 4 apple oxidation trio
- Grade 5 bread mold trio

## Reconciliation note

- Kindergarten through Grade 2 were still wired to placeholder-style document IDs that returned `404` in the reachable Remarq backend before this pass.
- On 2026-04-12, real backend documents were created/reconciled for those canonical URLs and the source files were updated to the returned document IDs.
- Grade 3 through Grade 5 already resolved in the backend; those real IDs were preserved.
- All free-batch files now gate the feedback-layer bootstrap behind `?review=1`, so review controls no longer appear on the normal public freebie URLs by default.

## Asset → document ID mapping

- `lesson-plans/k-milk-magic.html` → `doc_zr0YeciOdzA` (`200` at `http://192.168.5.204:3334/documents/doc_zr0YeciOdzA`; canonical URI `https://littlelabcoats.co/lesson-plans/k-milk-magic.html`)
- `lesson-plans/k-milk-magic-refcard.html` → `doc_950mBWx1p04` (`200` at `http://192.168.5.204:3334/documents/doc_950mBWx1p04`; canonical URI `https://littlelabcoats.co/lesson-plans/k-milk-magic-refcard.html`)
- `lesson-plans/k-milk-magic-quiz.html` → `doc_bFVKBy5kOlM` (`200` at `http://192.168.5.204:3334/documents/doc_bFVKBy5kOlM`; canonical URI `https://littlelabcoats.co/lesson-plans/k-milk-magic-quiz.html`)
- `lesson-plans/free-gr1-celery-rainbow.html` → `doc_zyxmw7ZXZrI` (`200` at `http://192.168.5.204:3334/documents/doc_zyxmw7ZXZrI`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr1-celery-rainbow.html`)
- `lesson-plans/free-gr1-celery-rainbow-refcard.html` → `doc_9Y5rGc0bDdw` (`200` at `http://192.168.5.204:3334/documents/doc_9Y5rGc0bDdw`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr1-celery-rainbow-refcard.html`)
- `lesson-plans/free-gr1-celery-rainbow-quiz.html` → `doc_nfdF17gM19M` (`200` at `http://192.168.5.204:3334/documents/doc_nfdF17gM19M`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr1-celery-rainbow-quiz.html`)
- `lesson-plans/free-gr2-salt-dough-fossil-factory.html` → `doc_wdFzxdor-UE` (`200` at `http://192.168.5.204:3334/documents/doc_wdFzxdor-UE`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr2-salt-dough-fossil-factory.html`)
- `lesson-plans/free-gr2-salt-dough-fossil-factory-refcard.html` → `doc_c5Poc8AFlho` (`200` at `http://192.168.5.204:3334/documents/doc_c5Poc8AFlho`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr2-salt-dough-fossil-factory-refcard.html`)
- `lesson-plans/free-gr2-salt-dough-fossil-factory-quiz.html` → `doc_OOCOTy8Y8P4` (`200` at `http://192.168.5.204:3334/documents/doc_OOCOTy8Y8P4`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr2-salt-dough-fossil-factory-quiz.html`)
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html` → `doc_fmUnpkK9XPU` (`200` at `http://192.168.5.204:3334/documents/doc_fmUnpkK9XPU`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`)
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-refcard.html` → `doc_G3wDDjtBlsQ` (`200` at `http://192.168.5.204:3334/documents/doc_G3wDDjtBlsQ`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr3-egg-drop-kitchen-challenge-refcard.html`)
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html` → `doc_PsyNYnXSGTI` (`200` at `http://192.168.5.204:3334/documents/doc_PsyNYnXSGTI`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html`)
- `lesson-plans/free-gr4-apple-oxidation.html` → `doc_OK2BbngJCv8` (`200` at `http://192.168.5.204:3334/documents/doc_OK2BbngJCv8`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr4-apple-oxidation.html`)
- `lesson-plans/free-gr4-apple-oxidation-refcard.html` → `doc_IQp2Dkx2jnk` (`200` at `http://192.168.5.204:3334/documents/doc_IQp2Dkx2jnk`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr4-apple-oxidation-refcard.html`)
- `lesson-plans/free-gr4-apple-oxidation-quiz.html` → `doc_8Vx3eQUNvrw` (`200` at `http://192.168.5.204:3334/documents/doc_8Vx3eQUNvrw`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr4-apple-oxidation-quiz.html`)
- `lesson-plans/free-gr5-bread-mold-terrarium.html` → `doc_BPKTdiZOxVo` (`200` at `http://192.168.5.204:3334/documents/doc_BPKTdiZOxVo`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr5-bread-mold-terrarium.html`)
- `lesson-plans/free-gr5-bread-mold-terrarium-refcard.html` → `doc_E8G3kFcZBTg` (`200` at `http://192.168.5.204:3334/documents/doc_E8G3kFcZBTg`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr5-bread-mold-terrarium-refcard.html`)
- `lesson-plans/free-gr5-bread-mold-terrarium-quiz.html` → `doc_XufM9iMwdfY` (`200` at `http://192.168.5.204:3334/documents/doc_XufM9iMwdfY`; canonical URI `https://littlelabcoats.co/lesson-plans/free-gr5-bread-mold-terrarium-quiz.html`)
