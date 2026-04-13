# Grade 4 Physical Science Batch Review

Last updated: 2026-04-13
Chunk: `gr4-ps3-unit1-review-batch-1`
Status: round-1 Rachel + Margaret review recorded from direct source inspection; round-1 revisions applied in repo; reviewed-status rollout is live; representative public verification completed

## Scope

This batch covers the complete Grade 4 Physical Science Unit 1 `Energy & Motion` package:

### Canonical lesson pages
- `lesson-plans/gr4-ps3-unit1-l1-stored-energy-starts-motion.html`
- `lesson-plans/gr4-ps3-unit1-l2-collisions-transfer-energy.html`
- `lesson-plans/gr4-ps3-unit1-l3-faster-motion-bigger-changes.html`
- `lesson-plans/gr4-ps3-unit1-l4-surfaces-and-friction-change-motion.html`
- `lesson-plans/gr4-ps3-unit1-l5-testing-one-change-at-a-time.html`
- `lesson-plans/gr4-ps3-unit1-l6-explain-how-energy-moves-and-causes-motion.html`

### Support assets
- `lesson-plans/gr4-ps3-unit1-refcard.html`
- `lesson-plans/gr4-ps3-unit1-quiz.html`

### Additional asset created in this pass
- `images/lesson-heroes/gr4-ps3-unit1-l1-energy-starts-motion-v2.jpg`

## Starting basis

Why this batch was the highest-value next move:
- the full-library coverage audit showed that Grade 4 Physical Science was the last clean minimum-shape gap in the canonical K–5 inventory
- `gr4-ps3-unit1` already had Lessons 2–6 plus the unit refcard and unit quiz
- creating the missing Lesson 1 was enough to finish the 6-lesson package cleanly
- the unit already had stable explicit document IDs on the existing files, so the cleanest next action was to add the missing lesson, reconcile the new document ID, and close the full batch honestly

## Wiring / backend verification before public closeout

Verified in repo + backend during this pass:
- the new Lesson 1 file contains explicit `data-document-id="doc_gr4ps3u1l1"`
- the full Grade 4 Physical Science package now passes local markup + backend verification together
- the checked backend at `http://192.168.5.204:3334/documents/:id` returns `200` for:
  - `doc_gr4ps3u1l1`
  - `doc_gr4ps3u1l2`
  - `doc_gr4ps3u1l3`
  - `doc_gr4ps3u1l4`
  - `doc_gr4ps3u1l5`
  - `doc_gr4ps3u1l6`
  - `doc_gr4ps3u1ref`
  - `doc_gr4ps3u1quiz`

Representative command used:

```bash
python3 scripts/remarq_batch_tools.py verify --json --skip-live \
  lesson-plans/gr4-ps3-unit1-l1-stored-energy-starts-motion.html \
  lesson-plans/gr4-ps3-unit1-l2-collisions-transfer-energy.html \
  lesson-plans/gr4-ps3-unit1-l3-faster-motion-bigger-changes.html \
  lesson-plans/gr4-ps3-unit1-l4-surfaces-and-friction-change-motion.html \
  lesson-plans/gr4-ps3-unit1-l5-testing-one-change-at-a-time.html \
  lesson-plans/gr4-ps3-unit1-l6-explain-how-energy-moves-and-causes-motion.html \
  lesson-plans/gr4-ps3-unit1-refcard.html \
  lesson-plans/gr4-ps3-unit1-quiz.html
```

## Rachel review artifact

Status: `round 1 commented — revisions applied`
Round: `1`
Scope label: `Grade 4 PS3 Unit 1 — Energy & Motion`

### Rachel round-1 review notes

1. **Target:** `gr4-ps3-unit1-l1-stored-energy-starts-motion.html`  
   **Observation:** The new worksheet explanation frame is strong overall, but the prompt should force families to name which start was faster and one thing that stayed the same in the fair test.  
   **Expected revision action:** Tighten the worksheet coaching and answer key so the comparison stays evidence-based.

2. **Target:** `gr4-ps3-unit1-refcard.html`  
   **Observation:** The unit refcard jumps quickly into collisions and friction, but the newly restored Lesson 1 idea should also appear on the unit card so the package starts with a clear “higher start → more speed” throughline.  
   **Expected revision action:** Add explicit higher-start / more-energy language to the refcard.

3. **Target:** directory / status surfaces  
   **Observation:** Once the full Grade 4 Physical Science package is closed, later passes should be able to see that this batch is reviewed / revised without rediscovering it from scratch.  
   **Expected revision action:** Update the durable tracker and lesson-index status surfaces during final closeout.

## Margaret review artifact

Status: `round 1 commented — revisions applied`
Round: `1`
Scope label: `Grade 4 PS3 Unit 1 — Energy & Motion`

### Margaret round-1 review notes

1. **Target:** `gr4-ps3-unit1-l1-stored-energy-starts-motion.html`  
   **Observation:** The new lesson is a strong entry point, but the parent answer key should more explicitly remind families that the car and ramp stayed the same while only the starting height changed.  
   **Expected revision action:** Strengthen the sample explanation so the fair-test logic is explicit.

2. **Target:** full unit arc  
   **Observation:** The added Lesson 1 now gives the unit a much cleaner progression into the later collision, friction, and explanation lessons.  
   **Expected revision action:** No additional lesson-content change required beyond the Lesson 1 / refcard clarifications above.

3. **Target:** public closeout honesty  
   **Observation:** Do not mark this batch complete until the new Lesson 1 route and the revised support assets are visibly live on the public review URLs.  
   **Expected revision action:** Finish public verification after push before upgrading status to completed.

## Revision tracking

### Revision round 1
Status: `revised after round 1`

Applied revisions:
- strengthened Lesson 1 worksheet coaching so students must name which start was faster and one thing that stayed the same in the fair test
- strengthened the Lesson 1 parent answer key so the fair-test logic is explicit: same car, same ramp, changed starting height
- updated the unit refcard so the package now explicitly includes the Lesson 1 higher-start / more-energy / more-speed idea

### Revision round 2
Status: `not started`
Reserved only if live verification or later reviewer follow-up surfaces additional issues.

### Revision round 3
Status: `not started`
Reserved only if another review loop is genuinely required later.

## Public verification log

Verified live on 2026-04-13 after push and cache-busting:
- `https://littlelabcoats.co/lesson-plans/gr4-ps3-unit1-l1-stored-energy-starts-motion.html?cb=verify2`
  - confirmed the public lesson returns `200`
  - confirmed the public lesson serves `data-document-id="doc_gr4ps3u1l1"`
  - confirmed the Gemini-generated hero image is live on the public lesson route
  - confirmed the public lesson does **not** append the feedback-layer script outside review mode
- `https://littlelabcoats.co/lesson-plans/gr4-ps3-unit1-l1-stored-energy-starts-motion.html?review=1&cb=verify2`
  - confirmed the live review route returns `200`
  - confirmed the review route appends the feedback-layer script with `data-document-id="doc_gr4ps3u1l1"`
- `https://littlelabcoats.co/lesson-plans/gr4-ps3-unit1-refcard.html?review=1&cb=verify3`
  - confirmed the live review route returns `200`
  - confirmed the revised higher-start / more-energy / more-speed language is live on the refcard
  - confirmed the review route appends the feedback-layer script with `data-document-id="doc_gr4ps3u1ref"`
- `https://littlelabcoats.co/lesson-plans/gr4-ps3-unit1-quiz.html?review=1&cb=verify2`
  - confirmed the live review route returns `200`
  - confirmed the review route appends the feedback-layer script with `data-document-id="doc_gr4ps3u1quiz"`
- `https://littlelabcoats.co/lesson-plans/?cb=verify3`
  - confirmed the public lesson index contains `Stored Energy Starts Motion`
  - confirmed the public lesson index exposes the Grade 4 Physical Science `Reviewed / revised` badge and status summary note
- `https://littlelabcoats.co/lesson-plans/review/?cb=verify3`
  - confirmed the public review index contains `Stored Energy Starts Motion`
  - confirmed the public review index exposes the Grade 4 Physical Science `Reviewed / revised` badge and status summary note

## Honest batch disposition

What this file proves already:
- the missing Lesson 1 was created in canonical repo form
- the full Grade 4 Physical Science package now exists as a 6-lesson unit with support assets
- Rachel and Margaret round-1 notes are recorded for the package
- literal revisions from those notes are already applied in repo
- backend document wiring is reconciled for the full package

What this file does not claim:
- it does not claim that every other Grade 4 or Grade 5 domain has already completed the same end-to-end review lane
- it does not claim that the overlapping Grade 4 Earth scaffold ambiguity is resolved beyond the canonical counting decision recorded in the library audit
