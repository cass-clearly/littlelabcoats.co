# Grade 4 Engineering Batch Review

Last updated: 2026-04-12
Chunk: `gr4-ets1-unit1-review-batch-1`
Status: round-1 Rachel + Margaret review recorded from direct source/live inspection; round-1 revisions applied in repo; reviewed-status exposure added to the directory surfaces; commit/push and representative public verification completed for this batch

## Scope

This batch covers the complete Grade 4 Engineering Unit 1 storm-shelter package:

### Canonical lesson pages
- `lesson-plans/gr4-ets1-unit1-lesson1-define-the-storm-shelter-problem.html`
- `lesson-plans/gr4-ets1-unit1-lesson2-compare-shelter-materials-and-shapes.html`
- `lesson-plans/gr4-ets1-unit1-lesson3-plan-a-testable-storm-shelter.html`
- `lesson-plans/gr4-ets1-unit1-lesson4-build-and-run-the-first-shelter-test.html`
- `lesson-plans/gr4-ets1-unit1-lesson5-redesign-using-test-evidence.html`
- `lesson-plans/gr4-ets1-unit1-lesson6-present-and-defend-your-shelter-solution.html`

### Support assets
- `lesson-plans/gr4-ets1-unit1-refcard-lesson1-define-the-storm-shelter-problem.html`
- `lesson-plans/gr4-ets1-unit1-refcard-lesson2-compare-shelter-materials-and-shapes.html`
- `lesson-plans/gr4-ets1-unit1-refcard-lesson3-plan-a-testable-storm-shelter.html`
- `lesson-plans/gr4-ets1-unit1-refcard-lesson4-build-and-run-the-first-shelter-test.html`
- `lesson-plans/gr4-ets1-unit1-refcard-lesson5-redesign-using-test-evidence.html`
- `lesson-plans/gr4-ets1-unit1-refcard-lesson6-present-and-defend-your-shelter-solution.html`
- `lesson-plans/gr4-ets1-unit1-quiz.html`

### Status surfaces updated in this batch
- `lesson-plans/lesson-index-statuses.json`
- `lesson-plans/index.html`
- `lesson-plans/review/index.html`
- `lesson-plans/_generated/lesson-index-data.json`
- `lesson-plans/llc-review-program-tracker.md`

## Starting basis

Why this batch was selected next:
- it is the next coherent unfinished Grade 4 review lane after the completed Grade 4 Life Science domain and the Grade 5 Engineering closeout
- all 6 lesson review URLs, all 6 refcard review URLs, and the quiz review URL already resolve publicly
- the current repo had no durable Grade 4 engineering Rachel + Margaret review artifact yet
- the support assets exposed a literal rendering defect that could be fixed cleanly in one batch

## Live review-path verification before revision

Verified on 2026-04-12 before final closeout:
- representative lesson review URL returned `200`
- representative refcard review URL returned `200`
- representative quiz review URL returned `200`
- representative live pages exposed the same explicit `data-document-id` values as the repo source
- representative checked document IDs resolve at the reachable backend `http://192.168.5.204:3334/documents/:id`

Representative checked URLs:
- `https://littlelabcoats.co/lesson-plans/gr4-ets1-unit1-lesson1-define-the-storm-shelter-problem.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr4-ets1-unit1-refcard-lesson1-define-the-storm-shelter-problem.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr4-ets1-unit1-quiz.html?review=1`

## Rachel review artifact

Status: `round 1 commented — revisions applied`
Round: `1`
Scope label: `Grade 4 ETS1 Unit 1 — Storm Shelter Design`

### Rachel round-1 review notes

1. **Target:** all six Grade 4 Engineering refcards  
   **Observation:** The `Key vocabulary` line is rendering as character-by-character chips instead of real vocabulary words, and the `Materials snapshot` list is carrying vocabulary terms instead of materials.  
   **Expected revision action:** Replace the broken chip rows with the actual lesson vocabulary and restore materials snapshots that match each lesson.

2. **Target:** `gr4-ets1-unit1-lesson2-compare-shelter-materials-and-shapes.html`  
   **Observation:** The worksheet can still let a student pick a favorite option without tying observations to shelter criteria.  
   **Expected revision action:** Strengthen the worksheet coaching and answer key so students cite an observed property and connect it to a criterion or constraint.

3. **Target:** `gr4-ets1-unit1-quiz.html`  
   **Observation:** The short response is close, but the parent grading cues should explicitly keep version 1 and version 2 under the same fair-test setup.  
   **Expected revision action:** Tighten the prompt and grading notes so families look for same-test evidence, not just a generic redesign story.

## Margaret review artifact

Status: `round 1 commented — revisions applied`
Round: `1`
Scope label: `Grade 4 ETS1 Unit 1 — Storm Shelter Design`

### Margaret round-1 review notes

1. **Target:** `gr4-ets1-unit1-lesson5-redesign-using-test-evidence.html`  
   **Observation:** The redesign worksheet should force students to name the exact failure point before proposing a change. Right now families could accept a vague redesign answer.  
   **Expected revision action:** Add explicit worksheet coaching and stronger answer-key language tying the redesign to the failure point and evidence.

2. **Target:** Grade 4 Engineering support package  
   **Observation:** The refcard rendering bug makes the public support assets feel unfinished even though the lesson sequence itself is coherent.  
   **Expected revision action:** Fix the refcard vocabulary/materials sections literally on the canonical files.

3. **Target:** directory/review status surfaces  
   **Observation:** Once this batch is reviewed and revised, later passes should be able to see that status without rediscovering it from scratch.  
   **Expected revision action:** Mark the Grade 4 Engineering lesson set as reviewed / revised in the generated lesson-index metadata and both directory pages.

## Revision tracking

### Revision round 1
Status: `revised after round 1`

Applied revisions:
- replaced the broken character-by-character `Key vocabulary` chip rows on all 6 Grade 4 Engineering refcards with the actual lesson vocabulary
- restored real `Materials snapshot` lists on all 6 Grade 4 Engineering refcards so the cards no longer show vocabulary in the materials section
- strengthened Lesson 2 worksheet coaching and answer-key language so students must cite an observed property and connect it to a shelter criterion or constraint
- strengthened Lesson 5 worksheet coaching and answer-key language so students must name the failure point before proposing a redesign and explain how version 2 should improve the same test
- tightened the Grade 4 Engineering quiz short response and grading cues so families look for same-fair-test evidence plus criteria-based improvement
- added reviewed / revised status exposure for Grade 4 Engineering in the durable tracker, generated lesson-index metadata, main lesson directory, and review directory

### Revision round 2
Status: `not started`
Reserved only if a later live/Remarq follow-up pass surfaces additional issues.

### Revision round 3
Status: `not started`
Reserved only if a later live/Remarq follow-up pass surfaces additional issues.

## Public/status verification log

Verified live on 2026-04-12 after push and cache-busting:
- `https://littlelabcoats.co/lesson-plans/?cb=gr4etscloseout4`
  - confirmed public lesson index contains `Grade 4 Engineering Unit 1 completed review and revision.`
  - confirmed the representative lesson `Define the Storm Shelter Problem` now shows the `Reviewed / revised` badge in the public lesson directory
- `https://littlelabcoats.co/lesson-plans/review/?cb=gr4etscloseout4`
  - confirmed public review index contains `Grade 4 Engineering Unit 1 completed review and revision.`
  - confirmed the representative lesson `Define the Storm Shelter Problem` now shows the `Reviewed / revised` badge in the public review directory
- `https://littlelabcoats.co/lesson-plans/gr4-ets1-unit1-lesson2-compare-shelter-materials-and-shapes.html?review=1&cb=gr4etscloseout4`
  - confirmed the strengthened worksheet coaching is live on the public review URL
- `https://littlelabcoats.co/lesson-plans/gr4-ets1-unit1-refcard-lesson4-build-and-run-the-first-shelter-test.html?review=1&cb=gr4etscloseout4`
  - confirmed the refcard `Key vocabulary` row now shows real vocabulary chips (`fair test`, `variable`, `prototype`, `failure point`, `evidence`, `observation`) instead of character-by-character chips
  - confirmed the refcard still exposes `data-document-id="doc_gr4ets1u1l4r"`
- `https://littlelabcoats.co/lesson-plans/gr4-ets1-unit1-quiz.html?review=1&cb=gr4etscloseout4`
  - confirmed the strengthened same-fair-test short-response language is live and the quiz still exposes `data-document-id="doc_gr4ets1u1quiz"`

## Honest batch disposition

What this file proves now:
- Rachel and Margaret review notes exist in repo for the full Grade 4 Engineering unit package
- literal batch revisions are applied in the canonical lesson/refcard/quiz files
- reviewed / revised status has been wired into the repo-side listing surfaces
- commit/push and representative public verification are complete for this batch

What this file does not claim:
- it does not claim the broader Grade 4 Earth & Space Science queue is already resolved
- it does not claim any later Grade 4/5 batch has already gone through the same end-to-end cycle
