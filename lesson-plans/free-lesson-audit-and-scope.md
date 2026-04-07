# Free Lesson Audit and Scope — Grades K–5

Date: 2026-04-07  
Status: chunk 1 audit artifact / source of truth for free-lesson mapping before implementation changes

This file is the authoritative in-repo audit for the current free-lesson set across grades K–5.

It answers four questions:
1. What free-lesson candidates exist in the repo today?
2. What does the public/catalog surface currently point to?
3. What is the intended free lesson per grade for this pass?
4. Which files/surfaces need create vs fix work before the free-lesson set can move into review/build loops?

## Ground rules for this audit

- Treat Serena's correction as authoritative for Kindergarten: **the intended Kindergarten free lesson is milk**, unless a stronger, explicit approved repo source proves otherwise.
- Do **not** guess mappings where the repo is silent.
- Distinguish between:
  - **repo candidate exists**
  - **public/catalog surface actually points to it**
  - **supporting assets exist** (reference card, quiz, route parity)
- This audit is limited to free-lesson mapping/scope. It does **not** claim Rachel or Margaret review happened.

## Primary evidence reviewed

### Repo free-lesson candidate files discovered
- `lesson-plans/free-k-fizzy-color-explosions.html`
- `lesson-plans/k-milk-magic.html`
- `lesson-plans/free-gr1-celery-rainbow.html`
- `lesson-plans/free-gr2-salt-dough-fossil-factory.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- `lesson-plans/free-gr4-apple-oxidation.html`
- `lesson-plans/free-gr5-bread-mold-terrarium.html`

### Public/catalog/navigation surfaces inspected
- `store.html`
- `index.html`
- `curriculum.html`
- `curriculum/index.html`
- `lesson-plans/gr3-curriculum-audit-and-scope.md`
- `memory/2026-04-02.md`

### Important context evidence
- `memory/2026-04-02.md` records the originally queued standalone freebies as:
  - K: Fizzy Color Explosions
  - Grade 1: Celery Rainbow
  - Grade 2: Salt Dough Fossil Factory
  - Grade 3: Egg Drop Kitchen Challenge
  - Grade 4: Apple Oxidation Experiment
  - Grade 5: Bread Mold Terrarium
- Current user instruction for this project pass says Serena later corrected Kindergarten from fizzy to milk. This audit therefore treats **milk** as the intended Kindergarten target and records any remaining fizzy references as mismatches.

## Executive summary

- There is a clear repo-side freebie candidate for every grade K–5.
- Kindergarten is the only grade with a direct target conflict in repo files: both `free-k-fizzy-color-explosions.html` and `k-milk-magic.html` exist.
- The only clear public/store free mapping currently found is **not aligned** with the intended K free lesson:
  - `store.html` currently advertises a Kindergarten free sample pointing to `lesson-plans/k-ls1-unit3-lesson1-what-do-animals-need.html`.
- No public/catalog surface inspected currently maps Grades 1–5 to their standalone freebie files.
- None of the standalone freebie files currently have matching standalone refcard or standalone quiz artifacts discoverable by filename pattern.
- All discovered freebie lesson pages currently still contain preview/paywall/review-shell code, so they are not yet obviously configured as true public free lessons.

## Authoritative grade-by-grade map

| Grade | Intended free lesson for this pass | Current repo free-lesson candidate(s) | Current public/catalog mapping source | Current public result | Status |
| --- | --- | --- | --- | --- | --- |
| K | `k-milk-magic.html` — **Milk Magic** | `lesson-plans/k-milk-magic.html`; conflicting older candidate `lesson-plans/free-k-fizzy-color-explosions.html` | `store.html` free sample card | `lesson-plans/k-ls1-unit3-lesson1-what-do-animals-need.html` (Animal Needs) | **mismapped** |
| 1 | `free-gr1-celery-rainbow.html` — **Celery Rainbow** | `lesson-plans/free-gr1-celery-rainbow.html` | no grade-1 free mapping found in `store.html`, `index.html`, `curriculum.html`, or `curriculum/index.html` | none found | **missing public mapping** |
| 2 | `free-gr2-salt-dough-fossil-factory.html` — **Salt Dough Fossil Factory** | `lesson-plans/free-gr2-salt-dough-fossil-factory.html` | no grade-2 free mapping found in inspected public/catalog files | none found | **missing public mapping** |
| 3 | `free-gr3-egg-drop-kitchen-challenge.html` — **Egg Drop Kitchen Challenge** | `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html` | no free mapping found in inspected public/catalog files; existing Grade 3 audit tracks this as a public-adjacent freebie, not canonical curriculum | none found | **missing public mapping** |
| 4 | `free-gr4-apple-oxidation.html` — **The Great Apple Browning Experiment** | `lesson-plans/free-gr4-apple-oxidation.html` | no grade-4 free mapping found in inspected public/catalog files; `curriculum.html` / `curriculum/index.html` still show Grade 4 coming soon | none found | **missing public mapping** |
| 5 | `free-gr5-bread-mold-terrarium.html` — **Bread Mold Terrarium** | `lesson-plans/free-gr5-bread-mold-terrarium.html` | no grade-5 free mapping found in inspected public/catalog files | none found | **missing public mapping** |

## Kindergarten conflict note (explicit)

### What Serena’s correction means for this audit
For this pass, Kindergarten is treated as:
- **intended target:** `lesson-plans/k-milk-magic.html`
- **not intended target:** `lesson-plans/free-k-fizzy-color-explosions.html` unless a later approved source reasserts fizzy

### What still exists in repo/public surfaces
- Repo still contains both:
  - `lesson-plans/k-milk-magic.html`
  - `lesson-plans/free-k-fizzy-color-explosions.html`
- Public store surface currently points to neither milk nor fizzy. It points to:
  - `lesson-plans/k-ls1-unit3-lesson1-what-do-animals-need.html`
- `memory/2026-04-02.md` preserves the older queued plan where Kindergarten was fizzy.

### Kindergarten conclusion
Kindergarten is currently **triple-misaligned**:
1. Serena-corrected intended lesson = **Milk Magic**
2. old queued standalone freebie in memory = **Fizzy Color Explosions**
3. current public store free sample = **Animal Needs**

That mismatch must be resolved explicitly in the next chunk. Do not infer that the public mapping is correct just because it exists.

## Repo asset inventory by grade

### Grade K
- Lesson-page candidates found:
  - `lesson-plans/k-milk-magic.html`
  - `lesson-plans/free-k-fizzy-color-explosions.html`
- Matching standalone refcard found by freebie stem: none
- Matching standalone quiz found by freebie stem: none
- Public/catalog mapping found:
  - `store.html` free sample card → `lesson-plans/k-ls1-unit3-lesson1-what-do-animals-need.html`
- Preview/paywall shell present in both lesson candidates: yes
- Route parity (directory route) for chosen target `k-milk-magic`: none found

### Grade 1
- Lesson-page candidate found:
  - `lesson-plans/free-gr1-celery-rainbow.html`
- Matching standalone refcard found by freebie stem: none
- Matching standalone quiz found by freebie stem: none
- Public/catalog mapping found: none in inspected public/catalog files
- Preview/paywall shell present: yes
- Route parity (directory route): none found

### Grade 2
- Lesson-page candidate found:
  - `lesson-plans/free-gr2-salt-dough-fossil-factory.html`
- Matching standalone refcard found by freebie stem: none
- Matching standalone quiz found by freebie stem: none
- Public/catalog mapping found: none in inspected public/catalog files
- Preview/paywall shell present: yes
- Route parity (directory route): none found

### Grade 3
- Lesson-page candidate found:
  - `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- Matching standalone refcard found by freebie stem: none
- Matching standalone quiz found by freebie stem: none
- Public/catalog mapping found: none in inspected public/catalog files
- Related audit context:
  - `lesson-plans/gr3-curriculum-audit-and-scope.md` explicitly treats this file as a Grade 3 public-adjacent freebie, not part of the canonical Grade 3 curriculum map
- Preview/paywall shell present: yes
- Route parity (directory route): none found

### Grade 4
- Lesson-page candidate found:
  - `lesson-plans/free-gr4-apple-oxidation.html`
- Matching standalone refcard found by freebie stem: none
- Matching standalone quiz found by freebie stem: none
- Public/catalog mapping found: none in inspected public/catalog files
- Public curriculum state found:
  - `curriculum.html` and `curriculum/index.html` still show Grade 4 as coming soon, with no free lesson surfaced
- Preview/paywall shell present: yes
- Route parity (directory route): none found

### Grade 5
- Lesson-page candidate found:
  - `lesson-plans/free-gr5-bread-mold-terrarium.html`
- Matching standalone refcard found by freebie stem: none
- Matching standalone quiz found by freebie stem: none
- Public/catalog mapping found: none in inspected public/catalog files
- Preview/paywall shell present: yes
- Route parity (directory route): none found

## Public/catalog mapping audit by surface

### `store.html`
Current observed free sample block:
- badge: Kindergarten + Free
- title: `Free Sample — Animal Needs`
- CTA target: `/lesson-plans/k-ls1-unit3-lesson1-what-do-animals-need.html`

Audit result:
- currently the only explicit free lesson surfaced in the store
- does not match intended Kindergarten free lesson for this pass
- does not expose any Grades 1–5 standalone freebies

### `index.html`
Audit result:
- no explicit K–5 standalone free-lesson mapping found for the discovered freebie files
- homepage sample/browse sections do not currently act as the free-lesson map for the standalone freebie set

### `curriculum.html`
Audit result:
- no explicit mapping to the standalone freebies found
- Grade 4 remains “coming soon” in the current library structure
- Grade 5 shows regular curriculum lessons, not the free standalone set

### `curriculum/index.html`
Audit result:
- mirrors the same problem: no explicit standalone freebie mapping found for K–5
- Grade 4 remains “coming soon”
- Grade 5 shows curriculum lessons, not the free standalone set

## Gap / mismatch inventory

| Area | Grade(s) affected | Exact files/surfaces | Problem type | Notes |
| --- | --- | --- | --- | --- |
| Intended target conflict | K | `lesson-plans/k-milk-magic.html`; `lesson-plans/free-k-fizzy-color-explosions.html`; `memory/2026-04-02.md` | outdated/mismapped target | Serena-corrected milk target conflicts with older fizzy planning artifact and leftover fizzy file |
| Public free-sample mismatch | K | `store.html` | stale public mapping | Store still advertises Animal Needs instead of the intended K standalone free lesson |
| Missing public free mapping | 1, 2, 3, 4, 5 | `store.html`, `index.html`, `curriculum.html`, `curriculum/index.html` | missing mapping | Freebie lesson pages exist in repo but are not discoverable through inspected public/catalog surfaces |
| Missing standalone refcards | K, 1, 2, 3, 4, 5 | no discovered `lesson-plans/*refcard*` files matching freebie stems | incomplete asset set | Need decision whether freebies get dedicated refcards or grade-linked refcards; currently none match the freebie pages |
| Missing standalone quizzes | K, 1, 2, 3, 4, 5 | no discovered `lesson-plans/*quiz*` files matching freebie stems | incomplete asset set | Need explicit quiz plan per freebie |
| Preview/paywall still present | K, 1, 2, 3, 4, 5 | all discovered standalone freebie lesson pages | free-flag / access mismatch | Existing freebie pages still include paywall shell / access-lock JS markers |
| Missing route parity | K, 1, 2, 3, 4, 5 | all discovered standalone freebie lesson pages | route inconsistency | Freebie pages currently appear as flat `.html` files only; no matching directory-style routes were found |
| Grade 4 catalog visibility | 4 | `curriculum.html`; `curriculum/index.html` | missing grade exposure | Grade 4 still says coming soon, so even a completed freebie will remain undiscoverable until mapped |

## Implementation target list for the next chunk

### Kindergarten
- **Fix** `store.html`
  - replace current free sample target from `k-ls1-unit3-lesson1-what-do-animals-need.html` to the approved Kindergarten free lesson target once wired
- **Fix** free-lesson authority in repo mapping surfaces
  - treat `lesson-plans/k-milk-magic.html` as intended K free lesson
- **Fix** stale competing candidate handling
  - decide whether `lesson-plans/free-k-fizzy-color-explosions.html` is retired, redirected, or preserved as a non-primary artifact
- **Create or fix** supporting standalone refcard and quiz if the free-lesson SOP requires them for the freebie set
- **Fix** free-access behavior on `lesson-plans/k-milk-magic.html`

### Grade 1
- **Fix** public/catalog mapping surfaces to expose `lesson-plans/free-gr1-celery-rainbow.html`
- **Create** matching standalone refcard if required
- **Create** matching standalone quiz if required
- **Fix** free-access behavior on `lesson-plans/free-gr1-celery-rainbow.html`

### Grade 2
- **Fix** public/catalog mapping surfaces to expose `lesson-plans/free-gr2-salt-dough-fossil-factory.html`
- **Create** matching standalone refcard if required
- **Create** matching standalone quiz if required
- **Fix** free-access behavior on `lesson-plans/free-gr2-salt-dough-fossil-factory.html`

### Grade 3
- **Fix** public/catalog mapping surfaces to expose `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- **Create** matching standalone refcard if required
- **Create** matching standalone quiz if required
- **Fix** free-access behavior on `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- **Fix** scope hygiene in Grade 3 references as needed so this freebie is clearly tracked as the Grade 3 free lesson without confusing the canonical curriculum map

### Grade 4
- **Fix** public/catalog mapping surfaces to expose `lesson-plans/free-gr4-apple-oxidation.html`
- **Fix** Grade 4 “coming soon” catalog state in `curriculum.html` and `curriculum/index.html` if those surfaces are part of the public free-lesson route plan
- **Create** matching standalone refcard if required
- **Create** matching standalone quiz if required
- **Fix** free-access behavior on `lesson-plans/free-gr4-apple-oxidation.html`

### Grade 5
- **Fix** public/catalog mapping surfaces to expose `lesson-plans/free-gr5-bread-mold-terrarium.html`
- **Create** matching standalone refcard if required
- **Create** matching standalone quiz if required
- **Fix** free-access behavior on `lesson-plans/free-gr5-bread-mold-terrarium.html`

## Working conclusion

The authoritative intended free-lesson set for this pass is:
- K — `lesson-plans/k-milk-magic.html`
- 1 — `lesson-plans/free-gr1-celery-rainbow.html`
- 2 — `lesson-plans/free-gr2-salt-dough-fossil-factory.html`
- 3 — `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- 4 — `lesson-plans/free-gr4-apple-oxidation.html`
- 5 — `lesson-plans/free-gr5-bread-mold-terrarium.html`

Current public/catalog state does **not** match that set.

The next chunk should therefore focus on:
1. building/fixing any missing support assets for this set,
2. removing or superseding stale mappings (especially Kindergarten), and
3. wiring the public/store/catalog surfaces so the intended free lesson per grade is what the site actually shows.


## Review artifact linkage

Primary review tracker for the free-lesson set:
- `lesson-plans/free-lesson-batch-review.md`

Current review state recorded in repo:
- Rachel round 1: comments captured in `free-lesson-batch-review.md`
- Margaret round 1: comments captured in `free-lesson-batch-review.md`
- Round-1 revision pass: applied to targeted free-lesson artifacts and logged in `free-lesson-batch-review.md`
- Final package verification for the revision chunk: logged in `free-lesson-batch-review.md`
- Revision chunk handoff state: review-ready for human publish preparation, pending any future real round-2 comments
- Public mapping / publish-prep handoff: logged in `free-lesson-public-mapping-and-publish-prep.md`
- Final human-ready handoff review: logged in `free-lesson-public-mapping-and-publish-prep.md`
- Round 2: not started
- Round 3: not started

## Round-0 implementation notes

This section tracks the first artifact-build pass after the audit. It does not claim review completion; it only records that the intended K–5 freebie artifact trio now exists in repo files.

### Artifact sets created / normalized
- Kindergarten primary target kept as `lesson-plans/k-milk-magic.html`
  - modernized into the newer LLC lesson shell with updated section order, worksheet, answer key, and review metadata
  - created `lesson-plans/k-milk-magic-refcard.html`
  - created `lesson-plans/k-milk-magic-quiz.html`
  - normalized lesson shell metadata for free-access/review use
- Grade 1 primary target `lesson-plans/free-gr1-celery-rainbow.html`
  - created `lesson-plans/free-gr1-celery-rainbow-refcard.html`
  - created `lesson-plans/free-gr1-celery-rainbow-quiz.html`
  - normalized lesson shell metadata for free-access/review use
- Grade 2 primary target `lesson-plans/free-gr2-salt-dough-fossil-factory.html`
  - created `lesson-plans/free-gr2-salt-dough-fossil-factory-refcard.html`
  - created `lesson-plans/free-gr2-salt-dough-fossil-factory-quiz.html`
  - normalized lesson shell metadata for free-access/review use
- Grade 3 primary target `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
  - created `lesson-plans/free-gr3-egg-drop-kitchen-challenge-refcard.html`
  - created `lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html`
  - normalized lesson shell metadata for free-access/review use
- Grade 4 primary target `lesson-plans/free-gr4-apple-oxidation.html`
  - created `lesson-plans/free-gr4-apple-oxidation-refcard.html`
  - created `lesson-plans/free-gr4-apple-oxidation-quiz.html`
  - normalized lesson shell metadata for free-access/review use
- Grade 5 primary target `lesson-plans/free-gr5-bread-mold-terrarium.html`
  - created `lesson-plans/free-gr5-bread-mold-terrarium-refcard.html`
  - created `lesson-plans/free-gr5-bread-mold-terrarium-quiz.html`
  - normalized lesson shell metadata for free-access/review use

### Non-primary artifact note
- `lesson-plans/free-k-fizzy-color-explosions.html` remains in repo as a non-primary Kindergarten artifact. It was not promoted during this chunk because the audited intended Kindergarten free lesson is milk.
- The fizzy file now carries an explicit archive note in-page so it is no longer visually ambiguous as the active Kindergarten free-lesson target.

### Still intentionally out of scope for this chunk
- public/store/catalog rewiring
- Rachel review
- Margaret review
- review-round revisions
- publish/live verification
