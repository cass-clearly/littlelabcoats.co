# Grade 4 LS1 Unit 1 Lesson 1 QA Notes

Last updated: 2026-04-09
Status: review-and-quality-check pass completed for embedded animal-card update

## Scope reviewed

Primary lesson:
- `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`

Directly coupled support asset:
- `lesson-plans/gr4-ls1-unit1-refcard-lesson1-external-structures-for-survival.html`

Reference parity anchor checked:
- `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`

Live review target checked:
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html?review=1`

## QA result summary

This pass confirms that the lesson now behaves like a self-contained LLC embedded-card lesson.
No stale requirement remains telling families to locate or supply animal cards externally.
The embedded card section is present in the lesson, the paired refcard is aligned, and print verification confirms letter-sized output.

## Content QA findings

Confirmed in the lesson and refcard:
- no remaining `picture cards` dependency
- no remaining `book images` dependency
- no remaining `animal photos from a book` requirement
- no remaining `picture or animal` worksheet evidence wording
- no remaining parent-supplied animal-card requirement

Confirmed replacement wording is consistent:
- `the included animal cards on this lesson page`
- `Animal Cards for This Lesson`
- `Name an animal`
- `This chart goes with Step 3`
- `Evidence from the included card`

## Layout and print QA findings

Confirmed in source and live review HTML:
- `Materials` is followed by `Animal Cards for This Lesson`
- the card section appears before `Let's Get Started`
- worksheet and parent answer key remain separated by page breaks
- print CSS includes `@page { size: letter portrait; margin: 0.4in; }`

Confirmed by local print render:
- WeasyPrint output reports `612 x 792 pts (letter)`
- extracted PDF text shows the expected order:
  - embedded card section
  - `Let's Get Started`
  - `Student Worksheet`
  - `Parent Answer Key`

## LLC parity check

Compared against the embedded-card pattern in:
- `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`

Parity confirmed on the points that matter here:
- embedded card section lives between `Materials` and the procedure
- materials and worksheet text explicitly point to included on-page cards
- card grid is printable and self-contained
- lesson structure remains standard LLC flow instead of becoming a separate printable format

## Issues found during QA

No additional blocking content issues found.
No further content/layout edits were required in this QA pass.

## Final QA conclusion for this chunk

The lesson is review-ready for the next shipping/reporting phase.
The embedded animal cards are present, internally consistent, and usable in both lesson-view and print-view contexts based on the checks run in this pass.
