# Little Lab Coats Remarq + Reviewer Audit

Date: 2026-04-12
Scope: canonical lesson library under `lesson-plans/`
Method: repo-wide HTML audit + review-artifact scan + backend spot/full ID existence checks where reachable

## What this audit checked

For each canonical lesson artifact in `lesson-plans/`:
- whether explicit Remarq wiring is present and internally consistent
  - `body data-document-id`
  - feedback-layer script presence
  - feedback-layer `data-document-id`
  - `?review=1` review-bypass presence when present in file
- whether the configured document ID resolves in the reachable Remarq backend at `http://192.168.5.204:3334/documents/:id`
- whether there is repo evidence that the file went through **both** required reviewers: Rachel and Margaret

## Important honesty limits

This audit is factual but not magical:
- reviewer coverage is counted as **proved** only where repo artifacts explicitly tie the file or batch to both Rachel and Margaret
- if the repo does not contain proof, the file is marked **unknown**, not assumed reviewed
- backend existence checks only prove that a document record currently resolves in the reachable Remarq backend
- backend existence does **not** by itself prove Rachel/Margaret review happened
- review-artifact mentions do **not** by themselves prove the current configured ID is the same backend record unless the artifact explicitly says so

## Canonical artifact counts

Canonical artifact set used for summary (deduped to prefer the top-level `.html` over duplicate directory `index.html` wrappers when both exist):
- total canonical artifacts: **322**
- canonical lesson pages: **205**
- canonical refcards: **83**
- canonical quizzes: **34**

## Remarq wiring summary

Canonical artifact wiring state:
- valid explicit ID wiring (`body` + script IDs present and matching): **314 / 322**
- missing wiring: **8 / 322**
- mismatch-only cases after canonical dedupe: **0**

Canonical **lesson-page** wiring state:
- valid explicit ID wiring: **203 / 205**
- missing wiring: **2 / 205**

Artifacts with missing canonical wiring:
- `lesson-plans/gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html`
- `lesson-plans/gr4-ls1-unit1-l1-food-webs.html`
- `lesson-plans/review/index.html`

Notes:
- of those 8, only **1** is a real lesson page (`gr4-ls1-unit1-l1-food-webs.html`), and it appears to be a stale/non-canonical page rather than a mainline curriculum lesson
- the other lesson-page exception is `lesson-plans/review/index.html`, which is a review directory page rather than a teachable lesson
- the six Grade 3 PS2 misses are support assets (refcards), not lesson pages

## Backend document existence summary

For every canonical artifact with a valid matching explicit ID, the audit queried the reachable backend:
- backend document exists (`200`): **112**
- backend document not found (`404`): **202**

That means a large share of files have syntactically sane IDs in markup but **no currently resolvable backend document** at the checked backend.

## Reviewer-proof summary

Canonical artifact reviewer-proof state from repo evidence:
- proof of **both Rachel and Margaret**: **85 / 322**
- proof for only one reviewer: **0 / 322**
- **unknown / no proof found in repo artifacts**: **237 / 322**

Canonical **lesson-page** reviewer-proof state:
- proof of both Rachel and Margaret: **42 / 205**
- one reviewer only: **0 / 205**
- unknown / no proof found: **163 / 205**

## Combined risk matrix — lesson pages only

Lesson pages grouped by reviewer proof + backend document state:

- both reviewers proved + backend document exists: **11**
- both reviewers proved + backend document missing (`404`): **30**
- both reviewers proved + no valid ID wiring: **1**
- reviewer proof unknown + backend document exists: **83**
- reviewer proof unknown + backend document missing (`404`): **79**
- reviewer proof unknown + no valid ID wiring: **1**

## What is actually well-supported right now

### Strongest verified batch: Grade 4 Life Science

`lesson-plans/gr4-life-science-batch-review.md` contains the strongest concrete review proof in the repo.
It explicitly records:
- Rachel round-1 inline comments on real lesson/quiz documents
- Margaret round-1 inline comments on real lesson/quiz documents
- comment IDs
- comment-to-live-document mapping
- explicit backend confirmation for reviewed document IDs

From this audit, the following canonical lesson pages have both-reviewer proof **and** resolvable backend-backed IDs:
- `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`
- `lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html`
- `lesson-plans/gr4-ls1-unit1-lesson3-mouths-beaks-teeth-and-getting-food.html`
- `lesson-plans/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html`
- `lesson-plans/gr4-ls1-unit2-lesson1-roots-stems-and-plant-support-systems.html`
- `lesson-plans/gr4-ls1-unit2-lesson3-water-transport-inside-plants.html`
- `lesson-plans/gr4-ls1-unit2-lesson4-flowers-pollination-and-reproduction.html`
- `lesson-plans/gr4-ls1-unit2-lesson5-seeds-fruits-and-new-plants.html`
- `lesson-plans/gr4-ls1-unit2-lesson6-construct-an-argument-plant-structures.html`

Also verified in that review artifact:
- `lesson-plans/gr4-ls1-unit2-quiz.html`
- representative Grade 4 refcard/quiz live IDs were verified in `lesson-plans/gr4-document-id-manifest.md`

### Other both-reviewer proof exists, but backend reality is weak or absent

The repo contains both-reviewer claims for these broader areas:
- free lesson batch (`lesson-plans/free-lesson-batch-review.md`)
- Grade 3 LS1 batch (`lesson-plans/gr3-life-science-batch-review.md`)
- Grade 3 ESS2 batch (`lesson-plans/gr3-earth-science-batch-review.md`)
- Grade 3 ETS1 batch (`lesson-plans/gr3-engineering-batch-review.md`)
- several Grade 1 / Grade 2 routing and repair audit files mention review coverage for directory/index variants

But many of those files currently point at IDs that return `404` in the checked backend, so the repo proof and backend reality are not consistently aligned.

## Urgent failures / high-risk gaps

### 1) Most lesson pages do **not** have provable Rachel+Margaret coverage in the repo

This is the biggest truth from the audit.
Out of **205 canonical lesson pages**, only **42** have repo proof that both required reviewers touched them.
That leaves **163 lesson pages** with reviewer status **unknown**.

### 2) Many syntactically valid Remarq IDs do not resolve to a backend document

Across canonical artifacts with valid matching IDs:
- **202** return `404`
- only **112** resolve

On lesson pages specifically:
- **79** lesson pages have unknown reviewer proof and backend `404`
- **30** lesson pages have both-reviewer proof in repo artifacts but backend `404`

That is a serious integrity gap between page wiring and live backend-backed Remarq records.

### 3) Some review artifacts explicitly admit IDs were still pending or not yet real

Example:
- `lesson-plans/gr3-life-science-batch-review.md` explicitly says the package was published and review-tracked, but also states: **"Remarq IDs still pending"**

So for those batches, reviewer-process evidence may exist at the batch-document level, but it is not safe to claim the current file wiring is fully backed by confirmed live Remarq documents.

### 4) Legacy/stale duplicate page variants muddy the picture

Many lessons exist in both:
- `lesson-plans/foo.html`
- `lesson-plans/foo/index.html`

The duplicate `index.html` wrappers often have older or partial wiring states. This audit deduped to the top-level `.html` canonical file where both existed, but the duplicates are still a maintenance hazard and can confuse future audits.

## Clear-state summary by category

### A. Valid Remarq ID wiring + both reviewers proved + backend document exists
This is the safest bucket.
Count for lesson pages: **11**
This bucket is dominated by the Grade 4 LS1 review-confirmed set.

### B. Valid Remarq ID wiring + both reviewers proved + backend document missing
Count for lesson pages: **30**
These files have repo review proof but the current configured ID does not resolve in the checked backend.
Treat these as **high-risk** until the backend/document mapping is reconciled.
Representative examples:
- all reviewed free sample lesson pages (`free-gr1` through `free-gr5`)
- multiple Grade 3 reviewed lesson pages

### C. Valid Remarq ID wiring + reviewer proof unknown + backend document exists
Count for lesson pages: **83**
These are technically in better shape on the Remarq-ID side, but there is no repo proof that both Rachel and Margaret reviewed them.
Do **not** mark these as review-complete.

### D. Valid Remarq ID wiring + reviewer proof unknown + backend document missing
Count for lesson pages: **79**
These are the riskiest operationally among mainline lesson pages: no reviewer proof and no resolvable backend document.

### E. Missing/invalid wiring
Count for lesson pages: **2**
Neither appears to be a canonical curriculum lesson needing immediate live customer use, but they remain audit failures.

## Recommended follow-up order

1. **Treat reviewer coverage as unverified by default** for any lesson not explicitly named in a Rachel+Margaret artifact.
2. **Reconcile backend documents for reviewed batches next**, especially:
   - free lesson set
   - Grade 3 LS1 / ESS2 / ETS1 reviewed batches
3. **Create or refresh a canonical manifest** mapping each lesson file to:
   - current configured document ID
   - backend existence status
   - Rachel proof source
   - Margaret proof source
   - confidence level
4. **Decide a single canonical page shape** (`.html` vs `/index.html`) and retire or clearly mark legacy duplicates.

## Bottom line

Truthful current state:
- most canonical lesson pages have sane explicit Remarq wiring in markup
- many of those IDs do **not** resolve to a real backend document at the checked backend
- only a minority of lessons have repo proof that **both Rachel and Margaret** reviewed them
- the strongest end-to-end verified area is the Grade 4 LS1 batch
- the overall library does **not** currently support a truthful claim that every lesson has valid Remarq backing and both required reviewers completed review
