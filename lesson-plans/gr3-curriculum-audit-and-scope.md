# Grade 3 Curriculum Audit and Scope

Last updated: 2026-04-07
Status: authoritative chunk-1 audit for the Grade 3 completion run

## Purpose

This file is the source of truth for the current Grade 3 implementation run.

For this run, the user-provided scope is authoritative even if older repo notes or missing year-map docs say less.
This audit exists to answer four things before implementation starts:
- what Grade 3 artifacts already exist in the repo
- which existing files are the required continuity anchors
- which new lesson/support files must be created for this run
- which wiring surfaces will need updates later so the finished Grade 3 set appears publicly where expected

## Authoritative scope for this run

Treat the following as the required Grade 3 build scope for this run:
- each unit contains **6 NGSS-aligned lessons**
- use the existing Grade 3 lessons already built as anchors, not as blockers
- complete the remaining Grade 3 Life Science lessons in the current life science track beyond Lessons 1 and 2
- build **at least one complete 6-lesson Grade 3 Earth Science unit**
- build **one complete 6-lesson Grade 3 Engineering unit**
- for every new or unfinished lesson in this run, keep/copy preview behavior so the preview reaches the conceptual top matter and locks from `Materials` rather than showing only a tiny top section
- run the full LLC process on the new lesson set later: build -> Rachel review -> Margaret review -> revise -> repeat up to 3 total rounds max -> ready-for-live files -> public URL manifest
- update site/catalog mappings later so the finished Grade 3 set appears publicly where expected
- do **not** push or publish in this pass

Important consequence:
- missing Grade 3 year-map docs are **not** a blocker for this run
- this explicit scope overrides older notes that treated Earth Science / Engineering work as blocked by year-map ambiguity

---

## Current repo inventory re-audit

### Existing Grade 3 lesson and support artifacts confirmed in repo

#### Grade 3 Life Science
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`

#### Grade 3 Physical Science anchors already built
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html`
- `lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`
- `lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html`
- `lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`
- `lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`
- `lesson-plans/gr3-ps2-unit1-quiz.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html`

#### Grade 3 standalone / adjacent anchors
- `lesson-plans/bird-beak-buffet.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-refcard.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html`

### Current Grade 3 navigation/catalog surfaces already touching Grade 3
- `index.html`
- `curriculum.html`
- `curriculum/index.html`

### What currently exists vs what this run still requires

#### Already existing in repo and usable as anchors
- Grade 3 Life Science Unit 1 Lessons 1–6 now exist in repo
- Grade 3 Physical Science Unit 1 Lessons 1–6 exist in repo
- Grade 3 Physical Science Unit 1 quiz exists in repo
- Grade 3 Physical Science per-lesson refcards for Lessons 1–6 exist in repo
- Bird Beak Buffet exists as a Grade 3 standalone anchor
- Egg Drop Kitchen Challenge + refcard + quiz exist as Grade 3 engineering-adjacent anchors

#### Still missing or incomplete for this run
- Grade 3 Life Science Unit 1 refcards for Lessons 3–6 are now present in repo and live-verified
- Grade 3 Life Science Unit 1 quiz is now present in repo and live-verified
- a complete 6-lesson Grade 3 Earth Science unit
- a complete 6-lesson Grade 3 Engineering unit
- Earth Science and Engineering companion support artifacts where the LLC workflow expects them
- Earth Science and Engineering batch review artifacts
- real Remarq wiring / document IDs for newly created assets in this run
- updated Grade 3 catalog/navigation wiring for the finished set
- final clean public URL manifest for the finished set after live verification

### Life Science gap-map conclusion

For this completion run, **no Grade 3 LS1 lesson pages remain to be written**.
The remaining Grade 3 Life Science scope is exactly:
- wire real Remarq document IDs for LS1 lessons, refcards, and quiz
- carry the verified LS1 live state forward in later Grade 3 manifest/audit updates as Earth Science and Engineering are shipped

---

## Existing anchor files to reuse

### 1. Primary continuity anchors for all new Grade 3 lessons
Use these first when cloning shell, tone, pacing, worksheet split, and family-facing presentation:
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`

These are the strongest direct Grade 3 continuity anchors for:
- title/subtitle/meta rhythm
- section order
- worksheet + answer-key split
- print behavior
- family-facing grade-band tone
- feedback/paywall/review structure

### 2. Strongest adjacent modern LLC shell
Use this as the strongest shell reference whenever a new Grade 3 lesson needs a reliable structure source:
- `lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html`

Use it for:
- overall modern lesson architecture
- colored box system
- print rules
- component/class reuse
- review/paywall implementation pattern

### 3. Style/brand authority
Use this for terminology and section naming:
- `lesson-plans/style-guide.html`

Use it for:
- exact section names
- metadata conventions
- standards wording
- worksheet naming
- answer-key naming
- grade-band wording guardrails

### 4. Refcard pattern source
Use the existing Grade 3 PS2 refcards as the current in-repo refcard pattern source:
- `lesson-plans/gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html`

Use these for:
- per-lesson support asset naming
- grade-band visual simplicity for refcards
- unit-consistent refcard rhythm across a 6-lesson unit

### 5. Quiz pattern sources
Use these as the strongest Grade 3-adjacent quiz anchors:
- `lesson-plans/gr3-ps2-unit1-quiz.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html`

Use them for:
- Grade 3 quiz shell expectations
- review/paywall compatibility for quizzes
- parent-facing support tone where applicable

### 6. Engineering content anchor
Use this as the current Grade 3 engineering-adjacent topic anchor, but not as proof that the full engineering unit already exists:
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-refcard.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html`

Use these for:
- challenge-style engineering activity framing
- engineering vocabulary and family-facing tone
- support-asset packaging expectations

### 7. Navigation/catalog wiring sources
Use these exact files when later wiring the new Grade 3 units publicly:
- `index.html`
- `curriculum.html`
- `curriculum/index.html`

---

## Preview-depth baseline for this run

### Verified current Grade 3 lesson behavior
The current canonical Grade 3 lesson anchors use the deeper preview boundary that locks from the first `h2` matching:
- `materials`
- `gather before you start`
- `what you need`

Verified in:
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html`
- `lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`
- `lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html`
- `lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`
- `lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`

### Rule for all new or unfinished lessons in this run
All newly built Grade 3 Life Science, Earth Science, and Engineering lessons in this run must preserve/copy the deeper `lock-from-Materials` behavior.

Do **not** regress to the older shallow lock boundary that stops at `Learning Objective`, `Learning Goal`, `Big Idea`, or `The Big Idea`.

---

## Authoritative lesson matrix for this run

This matrix is the concrete build list for the remaining Grade 3 completion work.
For this chunk, filename and unit-code ambiguity is now intentionally closed.
These paths are the canonical path plan for implementation unless a later human explicitly renames them.

### Locked path conventions for this run
- Remaining Life Science work continues the existing `gr3-ls1-unit1-*` naming sequence.
- The Earth Science unit for this run is locked to **`3-ESS2 Unit 1`** using the `gr3-ess2-unit1-*` path prefix.
- The Engineering unit for this run is locked to **`3-ETS1 Unit 1`** using the `gr3-ets1-unit1-*` path prefix.
- Each complete 6-lesson unit in this run gets:
  - one lesson page per lesson
  - one per-lesson refcard using the PS2 naming rhythm
  - one unit quiz
- Review artifacts for the newly built scope will be tracked at the batch level in:
  - `lesson-plans/gr3-life-science-batch-review.md`
  - `lesson-plans/gr3-earth-science-batch-review.md`
  - `lesson-plans/gr3-engineering-batch-review.md`
- Final URL/readiness handoff for this run will be tracked in:
  - `lesson-plans/gr3-shareable-manifest.md`

| Domain | Unit | Slot | Repo status now | Required artifact(s) for this run | Locked lesson path | Locked refcard path | Locked quiz path | Remarq doc ID status | Preview-depth check | Review status | Intended live URL | Navigation status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Life Science | `3-LS1 Unit 1` | L1 | exists in repo | keep as anchor | `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | n/a | n/a | unknown / verify existing | already deeper preview | baseline anchor; no new review needed for this chunk | `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | linked in `index.html`, `curriculum.html`, `curriculum/index.html`; live status still requires public verification |
| Life Science | `3-LS1 Unit 1` | L2 | exists in repo | keep as anchor | `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | n/a | n/a | unknown / verify existing | already deeper preview | baseline anchor; no new review needed for this chunk | `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | linked in `index.html`, `curriculum.html`, `curriculum/index.html`; live status still requires public verification |
| Life Science | `3-LS1 Unit 1` | L3 | lesson + support live | keep live lesson/refcard pair | `lesson-plans/gr3-ls1-unit1-lesson3-plant-life-cycles-and-seeds.html` | `lesson-plans/gr3-ls1-unit1-refcard-lesson3-plant-life-cycles-and-seeds.html` | `lesson-plans/gr3-ls1-unit1-quiz.html` | placeholder/pending real ID | preview behavior verified in repo before publish | Rachel+Margaret round 1 recorded for lesson; support-asset review addendum recorded | `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson3-plant-life-cycles-and-seeds.html` | repo navigation updated and public URL verified |
| Life Science | `3-LS1 Unit 1` | L4 | lesson + support live | keep live lesson/refcard pair | `lesson-plans/gr3-ls1-unit1-lesson4-animal-life-cycles-and-metamorphosis.html` | `lesson-plans/gr3-ls1-unit1-refcard-lesson4-animal-life-cycles-and-metamorphosis.html` | `lesson-plans/gr3-ls1-unit1-quiz.html` | placeholder/pending real ID | preview behavior verified in repo before publish | Rachel+Margaret round 1 recorded for lesson; support-asset review addendum recorded | `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson4-animal-life-cycles-and-metamorphosis.html` | repo navigation updated and public URL verified |
| Life Science | `3-LS1 Unit 1` | L5 | lesson + support live | keep live lesson/refcard pair | `lesson-plans/gr3-ls1-unit1-lesson5-comparing-life-cycle-patterns.html` | `lesson-plans/gr3-ls1-unit1-refcard-lesson5-comparing-life-cycle-patterns.html` | `lesson-plans/gr3-ls1-unit1-quiz.html` | placeholder/pending real ID | preview behavior verified in repo before publish | Rachel+Margaret round 1 recorded for lesson; support-asset review addendum recorded | `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson5-comparing-life-cycle-patterns.html` | repo navigation updated and public URL verified |
| Life Science | `3-LS1 Unit 1` | L6 | lesson + support live | keep live lesson/refcard pair | `lesson-plans/gr3-ls1-unit1-lesson6-model-and-explain-a-life-cycle.html` | `lesson-plans/gr3-ls1-unit1-refcard-lesson6-model-and-explain-a-life-cycle.html` | `lesson-plans/gr3-ls1-unit1-quiz.html` | placeholder/pending real ID | preview behavior verified in repo before publish | Rachel+Margaret round 1 recorded for lesson; support-asset review addendum recorded | `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson6-model-and-explain-a-life-cycle.html` | repo navigation updated and public URL verified |
| Life Science | `3-LS1 Unit 1` | Unit support | live-verified | keep companion set and carry forward | n/a | `lesson-plans/gr3-ls1-unit1-refcard-lesson3-plant-life-cycles-and-seeds.html`; `lesson-plans/gr3-ls1-unit1-refcard-lesson4-animal-life-cycles-and-metamorphosis.html`; `lesson-plans/gr3-ls1-unit1-refcard-lesson5-comparing-life-cycle-patterns.html`; `lesson-plans/gr3-ls1-unit1-refcard-lesson6-model-and-explain-a-life-cycle.html` | `lesson-plans/gr3-ls1-unit1-quiz.html` | all pending real IDs | quiz behavior aligned to Grade 3 quiz pattern | batch review includes support-asset review addendum and public verification log | `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-quiz.html` | repo navigation updated and public URL verified |
| Earth Science | `3-ESS2 Unit 1` | L1 | missing | create lesson + refcard | `lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html` | `lesson-plans/gr3-ess2-unit1-refcard-lesson1-weather-patterns-over-time.html` | `lesson-plans/gr3-ess2-unit1-quiz.html` | pending new ID | must lock from `Materials` | review not started; later track in `lesson-plans/gr3-earth-science-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html` | not in current navigation |
| Earth Science | `3-ESS2 Unit 1` | L2 | missing | create lesson + refcard | `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html` | `lesson-plans/gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html` | `lesson-plans/gr3-ess2-unit1-quiz.html` | pending new ID | must lock from `Materials` | review not started; later track in `lesson-plans/gr3-earth-science-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html` | not in current navigation |
| Earth Science | `3-ESS2 Unit 1` | L3 | missing | create lesson + refcard | `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html` | `lesson-plans/gr3-ess2-unit1-refcard-lesson3-reading-weather-data.html` | `lesson-plans/gr3-ess2-unit1-quiz.html` | pending new ID | must lock from `Materials` | review not started; later track in `lesson-plans/gr3-earth-science-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html` | not in current navigation |
| Earth Science | `3-ESS2 Unit 1` | L4 | missing | create lesson + refcard | `lesson-plans/gr3-ess2-unit1-lesson4-weather-hazards-and-impacts.html` | `lesson-plans/gr3-ess2-unit1-refcard-lesson4-weather-hazards-and-impacts.html` | `lesson-plans/gr3-ess2-unit1-quiz.html` | pending new ID | must lock from `Materials` | review not started; later track in `lesson-plans/gr3-earth-science-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson4-weather-hazards-and-impacts.html` | not in current navigation |
| Earth Science | `3-ESS2 Unit 1` | L5 | missing | create lesson + refcard | `lesson-plans/gr3-ess2-unit1-lesson5-designing-for-local-weather.html` | `lesson-plans/gr3-ess2-unit1-refcard-lesson5-designing-for-local-weather.html` | `lesson-plans/gr3-ess2-unit1-quiz.html` | pending new ID | must lock from `Materials` | review not started; later track in `lesson-plans/gr3-earth-science-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson5-designing-for-local-weather.html` | not in current navigation |
| Earth Science | `3-ESS2 Unit 1` | L6 | missing | create lesson + refcard | `lesson-plans/gr3-ess2-unit1-lesson6-reducing-weather-related-hazards.html` | `lesson-plans/gr3-ess2-unit1-refcard-lesson6-reducing-weather-related-hazards.html` | `lesson-plans/gr3-ess2-unit1-quiz.html` | pending new ID | must lock from `Materials` | review not started; later track in `lesson-plans/gr3-earth-science-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson6-reducing-weather-related-hazards.html` | not in current navigation |
| Earth Science | `3-ESS2 Unit 1` | Unit support | missing | create full companion set | n/a | `lesson-plans/gr3-ess2-unit1-refcard-lesson1-weather-patterns-over-time.html`; `lesson-plans/gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html`; `lesson-plans/gr3-ess2-unit1-refcard-lesson3-reading-weather-data.html`; `lesson-plans/gr3-ess2-unit1-refcard-lesson4-weather-hazards-and-impacts.html`; `lesson-plans/gr3-ess2-unit1-refcard-lesson5-designing-for-local-weather.html`; `lesson-plans/gr3-ess2-unit1-refcard-lesson6-reducing-weather-related-hazards.html` | `lesson-plans/gr3-ess2-unit1-quiz.html` | all pending real IDs | quiz behavior aligned to Grade 3 quiz pattern | review not started; later track in `lesson-plans/gr3-earth-science-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-quiz.html` | add unit and support links to navigation after build |
| Engineering | `3-ETS1 Unit 1` | L1 | missing canonical unit lesson | create lesson + refcard | `lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html` | `lesson-plans/gr3-ets1-unit1-refcard-lesson1-defining-the-problem.html` | `lesson-plans/gr3-ets1-unit1-quiz.html` | pending new ID | must lock from `Materials` | review not started; later track in `lesson-plans/gr3-engineering-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html` | not in current navigation |
| Engineering | `3-ETS1 Unit 1` | L2 | missing canonical unit lesson | create lesson + refcard | `lesson-plans/gr3-ets1-unit1-lesson2-researching-constraints-and-materials.html` | `lesson-plans/gr3-ets1-unit1-refcard-lesson2-researching-constraints-and-materials.html` | `lesson-plans/gr3-ets1-unit1-quiz.html` | pending new ID | must lock from `Materials` | review not started; later track in `lesson-plans/gr3-engineering-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson2-researching-constraints-and-materials.html` | not in current navigation |
| Engineering | `3-ETS1 Unit 1` | L3 | missing canonical unit lesson | create lesson + refcard | `lesson-plans/gr3-ets1-unit1-lesson3-planning-a-solution.html` | `lesson-plans/gr3-ets1-unit1-refcard-lesson3-planning-a-solution.html` | `lesson-plans/gr3-ets1-unit1-quiz.html` | pending new ID | must lock from `Materials` | review not started; later track in `lesson-plans/gr3-engineering-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson3-planning-a-solution.html` | not in current navigation |
| Engineering | `3-ETS1 Unit 1` | L4 | missing canonical unit lesson | create lesson + refcard | `lesson-plans/gr3-ets1-unit1-lesson4-building-and-testing-a-prototype.html` | `lesson-plans/gr3-ets1-unit1-refcard-lesson4-building-and-testing-a-prototype.html` | `lesson-plans/gr3-ets1-unit1-quiz.html` | pending new ID | must lock from `Materials` | review not started; later track in `lesson-plans/gr3-engineering-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson4-building-and-testing-a-prototype.html` | not in current navigation |
| Engineering | `3-ETS1 Unit 1` | L5 | missing canonical unit lesson | create lesson + refcard | `lesson-plans/gr3-ets1-unit1-lesson5-improving-the-design.html` | `lesson-plans/gr3-ets1-unit1-refcard-lesson5-improving-the-design.html` | `lesson-plans/gr3-ets1-unit1-quiz.html` | pending new ID | must lock from `Materials` | review not started; later track in `lesson-plans/gr3-engineering-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson5-improving-the-design.html` | not in current navigation |
| Engineering | `3-ETS1 Unit 1` | L6 | missing canonical unit lesson | create lesson + refcard | `lesson-plans/gr3-ets1-unit1-lesson6-share-and-defend-your-solution.html` | `lesson-plans/gr3-ets1-unit1-refcard-lesson6-share-and-defend-your-solution.html` | `lesson-plans/gr3-ets1-unit1-quiz.html` | pending new ID | must lock from `Materials` | review not started; later track in `lesson-plans/gr3-engineering-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson6-share-and-defend-your-solution.html` | not in current navigation |
| Engineering | `3-ETS1 Unit 1` | Unit support | missing canonical unit support | create full companion set | n/a | `lesson-plans/gr3-ets1-unit1-refcard-lesson1-defining-the-problem.html`; `lesson-plans/gr3-ets1-unit1-refcard-lesson2-researching-constraints-and-materials.html`; `lesson-plans/gr3-ets1-unit1-refcard-lesson3-planning-a-solution.html`; `lesson-plans/gr3-ets1-unit1-refcard-lesson4-building-and-testing-a-prototype.html`; `lesson-plans/gr3-ets1-unit1-refcard-lesson5-improving-the-design.html`; `lesson-plans/gr3-ets1-unit1-refcard-lesson6-share-and-defend-your-solution.html` | `lesson-plans/gr3-ets1-unit1-quiz.html` | all pending real IDs | quiz behavior aligned to Grade 3 quiz pattern | review not started; later track in `lesson-plans/gr3-engineering-batch-review.md` | `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-quiz.html` | add unit and support links to navigation after build |
---

## Path-by-path execution checklist for later implementation chunks

Use this as the concrete execution tracker for every missing artifact in scope.

| Artifact group | Exact paths to create/update | Pattern source to clone | Later review artifact | Later catalog surfaces | Later manifest target |
|---|---|---|---|---|---|
| LS1 lesson-page verification only | `lesson-plans/gr3-ls1-unit1-lesson3-plant-life-cycles-and-seeds.html`; `lesson-plans/gr3-ls1-unit1-lesson4-animal-life-cycles-and-metamorphosis.html`; `lesson-plans/gr3-ls1-unit1-lesson5-comparing-life-cycle-patterns.html`; `lesson-plans/gr3-ls1-unit1-lesson6-model-and-explain-a-life-cycle.html` | Grade 3 LS1 lessons 1–2 + `gr2-ls2-unit1-lesson1-what-do-plants-need.html` | `lesson-plans/gr3-life-science-batch-review.md` | `index.html`; `curriculum.html`; `curriculum/index.html` | `lesson-plans/gr3-shareable-manifest.md` |
| LS1 support assets to create | `lesson-plans/gr3-ls1-unit1-refcard-lesson3-plant-life-cycles-and-seeds.html`; `lesson-plans/gr3-ls1-unit1-refcard-lesson4-animal-life-cycles-and-metamorphosis.html`; `lesson-plans/gr3-ls1-unit1-refcard-lesson5-comparing-life-cycle-patterns.html`; `lesson-plans/gr3-ls1-unit1-refcard-lesson6-model-and-explain-a-life-cycle.html`; `lesson-plans/gr3-ls1-unit1-quiz.html` | Grade 3 PS2 refcards + `gr3-ps2-unit1-quiz.html` | `lesson-plans/gr3-life-science-batch-review.md` | `index.html`; `curriculum.html`; `curriculum/index.html` when support links are exposed | `lesson-plans/gr3-shareable-manifest.md` |
| Earth Science lessons | `lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html`; `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`; `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`; `lesson-plans/gr3-ess2-unit1-lesson4-weather-hazards-and-impacts.html`; `lesson-plans/gr3-ess2-unit1-lesson5-designing-for-local-weather.html`; `lesson-plans/gr3-ess2-unit1-lesson6-reducing-weather-related-hazards.html` | Grade 3 LS1 lessons 1–2 + `gr2-ls2-unit1-lesson1-what-do-plants-need.html` + `style-guide.html` | `lesson-plans/gr3-earth-science-batch-review.md` | `index.html`; `curriculum.html`; `curriculum/index.html` | `lesson-plans/gr3-shareable-manifest.md` |
| Earth Science support assets | `lesson-plans/gr3-ess2-unit1-refcard-lesson1-weather-patterns-over-time.html`; `lesson-plans/gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html`; `lesson-plans/gr3-ess2-unit1-refcard-lesson3-reading-weather-data.html`; `lesson-plans/gr3-ess2-unit1-refcard-lesson4-weather-hazards-and-impacts.html`; `lesson-plans/gr3-ess2-unit1-refcard-lesson5-designing-for-local-weather.html`; `lesson-plans/gr3-ess2-unit1-refcard-lesson6-reducing-weather-related-hazards.html`; `lesson-plans/gr3-ess2-unit1-quiz.html` | Grade 3 PS2 refcards + `gr3-ps2-unit1-quiz.html` | `lesson-plans/gr3-earth-science-batch-review.md` | `index.html`; `curriculum.html`; `curriculum/index.html` when support links are exposed | `lesson-plans/gr3-shareable-manifest.md` |
| Engineering lessons | `lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html`; `lesson-plans/gr3-ets1-unit1-lesson2-researching-constraints-and-materials.html`; `lesson-plans/gr3-ets1-unit1-lesson3-planning-a-solution.html`; `lesson-plans/gr3-ets1-unit1-lesson4-building-and-testing-a-prototype.html`; `lesson-plans/gr3-ets1-unit1-lesson5-improving-the-design.html`; `lesson-plans/gr3-ets1-unit1-lesson6-share-and-defend-your-solution.html` | Grade 3 LS1 lessons 1–2 + `gr2-ls2-unit1-lesson1-what-do-plants-need.html` + `free-gr3-egg-drop-kitchen-challenge.html` | `lesson-plans/gr3-engineering-batch-review.md` | `index.html`; `curriculum.html`; `curriculum/index.html` | `lesson-plans/gr3-shareable-manifest.md` |
| Engineering support assets | `lesson-plans/gr3-ets1-unit1-refcard-lesson1-defining-the-problem.html`; `lesson-plans/gr3-ets1-unit1-refcard-lesson2-researching-constraints-and-materials.html`; `lesson-plans/gr3-ets1-unit1-refcard-lesson3-planning-a-solution.html`; `lesson-plans/gr3-ets1-unit1-refcard-lesson4-building-and-testing-a-prototype.html`; `lesson-plans/gr3-ets1-unit1-refcard-lesson5-improving-the-design.html`; `lesson-plans/gr3-ets1-unit1-refcard-lesson6-share-and-defend-your-solution.html`; `lesson-plans/gr3-ets1-unit1-quiz.html` | Grade 3 PS2 refcards + `gr3-ps2-unit1-quiz.html` + `free-gr3-egg-drop-kitchen-challenge-refcard.html` + `free-gr3-egg-drop-kitchen-challenge-quiz.html` | `lesson-plans/gr3-engineering-batch-review.md` | `index.html`; `curriculum.html`; `curriculum/index.html` when support links are exposed | `lesson-plans/gr3-shareable-manifest.md` |

### Build-loop requirements for every path above
- create/update the file in `lesson-plans/`
- use LLC style-guide terminology and the existing live lesson shell
- include `data-document-id`, `feedback-layer.js`, `llcPaywall`, and `?review=1` bypass where the artifact type expects them
- keep the deeper `lock-from-Materials` preview rule on lesson pages
- ensure the visible preview reaches the Learning Objective / conceptual top matter before locking at `Materials`
- include `Student Worksheet` + `Parent Answer Key` on lesson pages
- create the real review artifact updates for Rachel and Margaret when those later chunks run
- assign/verify real Remarq document IDs before publish and record whether each asset is still placeholder vs wired
- record final intended URL in `lesson-plans/gr3-shareable-manifest.md`

### Navigation/catalog checklist
When content creation is complete, later chunks must update:
- `index.html`
- `curriculum.html`
- `curriculum/index.html`

For each new unit/lesson, later wiring must define:
- which Grade 3 unit card it appears under
- lesson ordering inside that unit
- whether the unit quiz is listed publicly
- whether any standalone freebie remains separate from the canonical curriculum list

### Execution checklist by lesson set

#### LS1 support completion loop
1. Build missing LS1 refcards + LS1 unit quiz.
2. Verify LS1 lesson pages still preserve the deeper preview boundary through `Materials`.
3. Run Rachel review on LS1 support assets and any lesson-page regressions discovered during packaging.
4. Run Margaret review on LS1 support assets and any lesson-page regressions discovered during packaging.
5. Revise from review feedback; repeat up to 3 total rounds if needed.
6. Wire/verify real Remarq document IDs for LS1 lessons, refcards, and quiz.
7. Update `index.html`, `curriculum.html`, and `curriculum/index.html` so LS1 Lessons 3–6 and the quiz are publicly discoverable.
8. Publish LS1 updates.
9. Verify the public LS1 URLs and navigation on the live site.

#### Earth Science unit completion loop
1. Build all 6 Earth Science lessons plus 6 refcards plus the unit quiz.
2. Verify each lesson preserves the deeper preview boundary through `Materials`.
3. Run Rachel review on the Earth Science lesson set.
4. Run Margaret review on the Earth Science lesson set.
5. Revise from review feedback; repeat up to 3 total rounds if needed.
6. Wire/verify real Remarq document IDs for Earth Science lessons, refcards, and quiz.
7. Update `index.html`, `curriculum.html`, and `curriculum/index.html` with the Earth Science unit.
8. Publish the Earth Science unit.
9. Verify the public Earth Science URLs and navigation on the live site.

#### Engineering unit completion loop
1. Build all 6 Engineering lessons plus 6 refcards plus the unit quiz.
2. Verify each lesson preserves the deeper preview boundary through `Materials`.
3. Run Rachel review on the Engineering lesson set.
4. Run Margaret review on the Engineering lesson set.
5. Revise from review feedback; repeat up to 3 total rounds if needed.
6. Wire/verify real Remarq document IDs for Engineering lessons, refcards, and quiz.
7. Update `index.html`, `curriculum.html`, and `curriculum/index.html` with the Engineering unit.
8. Publish the Engineering unit.
9. Verify the public Engineering URLs and navigation on the live site.

### Final manifest checklist
Later chunks must produce a clean Grade 3 public URL manifest that includes:
- all Life Science URLs for Lessons 1–6 plus unit support assets
- all Earth Science URLs for Lessons 1–6 plus unit support assets
- all Engineering URLs for Lessons 1–6 plus unit support assets
- any Grade 3 standalone/freebie URLs that remain intentionally separate
- a clear distinction between repo-ready and live/published state

---

## Chunk-1 implementation decision

This audit chunk is complete when future implementation can proceed without year-map ambiguity.

That means the authoritative answer for the next chunks is now:
- use the existing Grade 3 LS1 lessons as the continuity anchors
- use the existing Grade 3 PS2/refcard/quiz set as support-pattern anchors
- use the explicit user-provided scope as the source of truth for missing work
- finish LS1 through Lesson 6
- build one full 6-lesson Grade 3 Earth Science unit
- build one full 6-lesson Grade 3 Engineering unit
- carry the deeper preview behavior forward on every new lesson
- later update navigation/catalog and produce a public URL manifest, but do not publish in this pass
