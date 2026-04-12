# Grade 5 Earth Science Batch Review

Last updated: 2026-04-12
Chunk: `gr5-ess1-unit1-review-batch-1`
Status: round-1 Rachel + Margaret review recorded; round-1 revisions applied in repo; review index + main lesson directory updated with reviewed-status exposure; Remarq document IDs reconciled; commit `9a0c8c4` pushed to `origin/main`; representative public review HTML reverified

## Scope

This batch is the first real execution chunk of the full-library reviewer program.
It covers the complete Grade 5 Earth & Space Science Unit 1 package:

### Canonical lesson pages
- `lesson-plans/gr5-ess1-unit1-l1-where-is-earth-s-water.html`
- `lesson-plans/gr5-ess1-unit1-l2-evaporation-and-condensation.html`
- `lesson-plans/gr5-ess1-unit1-l3-precipitation-and-collection.html`
- `lesson-plans/gr5-ess1-unit1-l4-runoff-infiltration-and-groundwater.html`
- `lesson-plans/gr5-ess1-unit1-l5-earth-systems-working-together.html`
- `lesson-plans/gr5-ess1-unit1-l6-modeling-a-local-water-system.html`

### Matching support artifacts
- `lesson-plans/gr5-ess1-unit1-refcard.html`
- `lesson-plans/gr5-ess1-unit1-quiz.html`

### Directory / status surfaces updated in this batch
- `lesson-plans/index.html`
- `lesson-plans/review/index.html`
- `lesson-plans/_generated/lesson-index-data.json`
- `lesson-plans/llc-review-program-tracker.md`

## Starting inventory basis

This batch was selected directly from the 2026-04-12 library audit:
- `lesson-plans/llc-remarq-review-audit-2026-04-12.md`

Why this batch first:
- it is a coherent 6-lesson domain unit
- all lesson, quiz, and refcard URLs already exist publicly
- review-mode URLs already return `200`
- the package had no prior proven Rachel+Margaret review artifact in repo
- the package still exposed cleanup opportunities that could be fixed literally in one pass

## Live review-path verification before review

Verified on 2026-04-12:
- each of the 6 lesson review URLs returned `200`
- the unit quiz review URL returned `200`
- the unit refcard review URL returned `200`

Representative verified URLs:
- `https://littlelabcoats.co/lesson-plans/gr5-ess1-unit1-l1-where-is-earth-s-water.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr5-ess1-unit1-l2-evaporation-and-condensation.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr5-ess1-unit1-l3-precipitation-and-collection.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr5-ess1-unit1-l4-runoff-infiltration-and-groundwater.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr5-ess1-unit1-l5-earth-systems-working-together.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr5-ess1-unit1-l6-modeling-a-local-water-system.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr5-ess1-unit1-quiz.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr5-ess1-unit1-refcard.html?review=1`

Important honesty note:
- at the start of this batch, the configured Grade 5 ESS1 Unit 1 document IDs were returning `404` from the reachable Remarq backend at `http://192.168.5.204:3334/documents/:id`
- on 2026-04-12, real backend documents were created/reconciled for all 6 lessons plus the unit quiz and refcard, the source files were updated to those real IDs, and representative public review HTML now serves the reconciled IDs
- this removes the earlier ESS1 Remarq-blocker for this batch, but it does **not** imply the wider library has been reconciled yet

## Rachel review artifact

Status: `round 1 commented — revisions applied`
Round: `1`
Scope label: `Grade 5 ESS1 Unit 1 — Water on Earth Systems`

### Rachel round-1 review notes

1. **Target:** `gr5-ess1-unit1-l1-where-is-earth-s-water.html` through `gr5-ess1-unit1-l6-modeling-a-local-water-system.html`
   **Observation:** The subtitle line is rendering as literal `undefined` on every lesson page, which looks unfinished on the live/public lesson shell.
   **Expected revision action:** Replace the broken subtitle with a real unit/lesson subtitle on all six lessons.

2. **Target:** `gr5-ess1-unit1-l1-where-is-earth-s-water.html`
   **Observation:** The worksheet asks for reservoirs and share size, but it would coach families better if the answer key restated the difference between “most water” and “easy-to-use fresh water” more explicitly.
   **Expected revision action:** Strengthen the answer-key language so the misconception is addressed directly.

3. **Target:** `gr5-ess1-unit1-l2-evaporation-and-condensation.html`
   **Observation:** The model is solid, but the worksheet prompt can still let students say droplets “came through” the cover. The written task should force source-and-process language.
   **Expected revision action:** Make the worksheet and answer key explicitly name evaporation first, then condensation.

4. **Target:** `gr5-ess1-unit1-quiz.html`
   **Observation:** The short response is okay, but the answer-key success criteria should explicitly check whether students connect multiple water movements instead of just dropping vocabulary words.
   **Expected revision action:** Tighten the success criteria to require connected system reasoning.

5. **Target:** Grade 5 ESS1 batch packaging
   **Observation:** The directory surfaces do not currently signal that this package has entered the reviewer program.
   **Expected revision action:** Add reviewed/in-program status exposure to the batch tracker and both lesson directory surfaces.

## Margaret review artifact

Status: `round 1 commented — revisions applied`
Round: `1`
Scope label: `Grade 5 ESS1 Unit 1 — Water on Earth Systems`

### Margaret round-1 review notes

1. **Target:** `gr5-ess1-unit1-l1-where-is-earth-s-water.html` through `gr5-ess1-unit1-l6-modeling-a-local-water-system.html`
   **Observation:** The live pages look polished overall, but the `undefined` subtitle makes the set feel not-yet-finished for homeschool families.
   **Expected revision action:** Add consistent subtitle lines that tell parents exactly where each lesson sits in the unit.

2. **Target:** `gr5-ess1-unit1-l2-evaporation-and-condensation.html`
   **Observation:** The parent note already warns against the “through the plastic” misconception, but the student worksheet should do more coaching work too.
   **Expected revision action:** Update the worksheet wording so students explain where the droplets came from and which process happened first.

3. **Target:** `gr5-ess1-unit1-quiz.html`
   **Observation:** The quiz answer key is usable, but the short-response grading notes should help a parent distinguish a connected explanation from a vocabulary list.
   **Expected revision action:** Add language that checks for sequence / relationship, not just term usage.

4. **Target:** review/index + lesson directory
   **Observation:** Once a batch has been reviewed and revised, it helps to show that status in the directory instead of making future passes rediscover it from scratch.
   **Expected revision action:** Update the status surfaces and durable tracker so later batches can continue cleanly.

## Revision tracking

### Revision round 1
Status: `revised after round 1`

Applied revisions:
- replaced the broken `undefined` subtitle on all 6 Grade 5 ESS1 Unit 1 lesson pages with real unit/lesson subtitles
- strengthened Lesson 1 answer-key language to directly contrast “most Earth water” vs “easy-to-use fresh water`
- strengthened Lesson 2 worksheet prompt and answer key so students explicitly describe evaporation first and condensation second
- strengthened the unit quiz short-response success criteria so parents look for connected system reasoning, not just vocabulary mentions
- created a durable multi-batch review tracker for the whole library
- recorded this batch as completed in-program in the tracker
- updated the public lesson directory and review index to expose reviewed/in-program status for this batch
- updated generated lesson-index metadata to mark this batch as reviewed round 1 and revised

### Revision round 2
Status: `not started`
Reserved only if a later live/Remarq follow-up pass surfaces additional issues.

### Revision round 3
Status: `not started`
Reserved only if a later live/Remarq follow-up pass surfaces additional issues.

## Directory / reviewed-status rollout completed in this batch

The following surfaces now expose this batch as actively reviewed / revised:
- `lesson-plans/index.html`
- `lesson-plans/review/index.html`
- `lesson-plans/_generated/lesson-index-data.json`
- `lesson-plans/llc-review-program-tracker.md`

## Remaining follow-up for this batch

Batch-complete status:
- commit `9a0c8c4` is pushed to `origin/main`
- representative public review verification has been rerun on the live ESS1 lesson/refcard/quiz routes after the push
- the ESS1 lesson/refcard/quiz source files now point at real backend document IDs that resolve at the checked Remarq backend

No open follow-up remains for this batch itself beyond normal future regression monitoring.

## Honest batch disposition

What this file truthfully proves now:
- a concrete first batch was selected from the audit and run through a real review/revision pass
- Rachel and Margaret review notes are recorded at the batch level
- literal fixes from those notes were applied in repo
- the directory/status surfaces were updated so later batches can continue systematically

What this file does not claim:
- it does not claim the entire library is complete
- it does not claim the wider Little Lab Coats Remarq backlog is reconciled outside this specific ESS1 batch
- it does not claim later Grade 5 batches already went through the same end-to-end cycle
