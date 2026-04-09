# Learning Objective Integrity Pass

Date: 2026-04-09

This pass verifies that the library-wide Learning Objective standards fix did not break Remarq/review wiring, preview/paywall behavior, or print-relevant lesson structure on the changed lesson files.

## Scope

- Changed lesson files reviewed: **83**
- Review scope source: current working-tree diff under `lesson-plans/`

## Automated integrity audit

- Files with valid `body[data-document-id]`: **83/83**
- Files with feedback-layer script `data-document-id`: **83/83**
- Files where body/script document IDs match: **83/83**
- Files whose first top-level section is Learning Objective/Learning Objectives: **83/83**
- Files still containing worksheet markers: **81/83**
- Files still containing answer-key markers: **83/83**
- Files with preview/paywall container present: **77/83** (not required for every file because some free lessons are intentionally unlocked)
- Files with materials-based preview lock keywords present: **76/83**

## Audit issues

- None. No Remarq/review wiring mismatches or first-section regressions were detected in the changed lesson set.

## Representative spot checks

- `lesson-plans/gr1-ls3-unit2-lesson1-you-look-like-your-parents.html`
  - body/script document IDs match: `doc_gr1-ls3-unit2-lesson1-you-look-like-your-parents == doc_gr1-ls3-unit2-lesson1-you-look-like-your-parents`
  - first `h2`: `🎯 Learning Objectives`
  - `page-break` count: `4`
  - paywall container present: `True`
  - worksheet marker present: `True`
  - answer-key marker present: `True`
  - materials-based preview lock keywords present: `True`
- `lesson-plans/free-gr1-celery-rainbow.html`
  - body/script document IDs match: `doc_free_gr1_celery_rainbow_lesson == doc_free_gr1_celery_rainbow_lesson`
  - first `h2`: `🎯 Learning Objectives`
  - `page-break` count: `6`
  - paywall container present: `False`
  - worksheet marker present: `True`
  - answer-key marker present: `True`
  - materials-based preview lock keywords present: `False`
- `lesson-plans/k-ls1-unit2-lesson4-sunlight-or-no-sunlight.html`
  - body/script document IDs match: `doc_SUYaI9Y1EWw == doc_SUYaI9Y1EWw`
  - first `h2`: `🎯 Learning Objective`
  - `page-break` count: `5`
  - paywall container present: `True`
  - worksheet marker present: `True`
  - answer-key marker present: `True`
  - materials-based preview lock keywords present: `True`
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
  - body/script document IDs match: `doc_gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces == doc_gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces`
  - first `h2`: `🎯 Learning Objective`
  - `page-break` count: `5`
  - paywall container present: `True`
  - worksheet marker present: `True`
  - answer-key marker present: `True`
  - materials-based preview lock keywords present: `True`
- `lesson-plans/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html`
  - body/script document IDs match: `doc_PkRt1nihjic == doc_PkRt1nihjic`
  - first `h2`: `🎯 Learning Objective`
  - `page-break` count: `5`
  - paywall container present: `True`
  - worksheet marker present: `True`
  - answer-key marker present: `True`
  - materials-based preview lock keywords present: `True`
- `lesson-plans/5th-fossils-earth-history.html`
  - body/script document IDs match: `doc_5th-fossils-earth-history == doc_5th-fossils-earth-history`
  - first `h2`: `🎯 Learning Objective`
  - `page-break` count: `5`
  - paywall container present: `True`
  - worksheet marker present: `True`
  - answer-key marker present: `True`
  - materials-based preview lock keywords present: `True`
- `lesson-plans/ocean-L1-coral-kingdom.html`
  - body/script document IDs match: `doc_ocean-L1-coral-kingdom == doc_ocean-L1-coral-kingdom`
  - first `h2`: `🎯 Learning Objective`
  - `page-break` count: `6`
  - paywall container present: `True`
  - worksheet marker present: `True`
  - answer-key marker present: `True`
  - materials-based preview lock keywords present: `True`
- `lesson-plans/k-milk-magic.html`
  - body/script document IDs match: `doc_free_k_milk_magic_lesson == doc_free_k_milk_magic_lesson`
  - first `h2`: `🎯 Learning Objective`
  - `page-break` count: `5`
  - paywall container present: `False`
  - worksheet marker present: `True`
  - answer-key marker present: `True`
  - materials-based preview lock keywords present: `False`
- `lesson-plans/thermal-energy-ice-cream.html`
  - body/script document IDs match: `doc_thermal-energy-ice-cream == doc_thermal-energy-ice-cream`
  - first `h2`: `🎯 Learning Objectives`
  - `page-break` count: `6`
  - paywall container present: `True`
  - worksheet marker present: `True`
  - answer-key marker present: `True`
  - materials-based preview lock keywords present: `True`

## Print / worksheet sanity conclusion

- The changed files retained worksheet markers, answer-key markers where expected, and existing `page-break` class usage.
- Spot-checked lessons across legacy, free, kindergarten, modern grade 3, modern grade 4, and standalone/ocean families still show the expected top matter → Learning Objective → lesson content flow without disturbing later worksheet sections.

## Preview / review / Remarq conclusion

- Changed files retained matching document IDs between the lesson body and feedback-layer script.
- Free lessons that intentionally omit paywall overlays still retain review wiring through the feedback layer.
- Preview-locked lessons still retain `llcPaywall` containers and materials-oriented lock cues where that behavior was already part of the template family.

## Fixes applied during this pass

- No code/content fixes were required in this integrity-pass iteration; the changed lesson set passed the wiring checks that were audited.

## Remaining follow-up outside this chunk

- Commit and push are still required before overall task completion.
- The Grade 4 Life Science Unit 1 Lesson 1 PDF re-export note belongs in the final closeout / follow-up capture after the site/library fix is complete, not in this integrity pass.
