# Grade 3 Earth Science Unit 1 Lesson 2 — Print Verification Note

Last updated: 2026-04-08
Target file: `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`
Live review URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html?review=1`

## What changed for Lesson 2 print readiness

The lesson page now includes Lesson 2–specific print safeguards for the embedded climate-card activity and worksheet tables:

- the lesson itself supplies the climate cards on the page
- print sizing for climate cards and worksheet tables
- explicit worksheet table column widths via `colgroup`
- `thead` / `tbody` structure for better print table behavior
- repeated table-header support in print
- print margin control with `@page`
- stronger break handling for:
  - `.climate-card-section`
  - `.climate-card`
  - `.climate-card-note`
  - `.worksheet-section`
  - `.compare-table`
- smaller print-safe card icon, title, tag, and clue sizing
- top-right print button is now wired as `type="button"` plus `onclick="window.focus(); window.print();"`

## What is verified by code inspection

Confirmed in `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`:
- the lesson contains `Climate Cards for This Lesson`
- no remaining main-lesson wording asks the parent to provide climate cards
- materials, procedure, worksheet, and answer key all point to the included climate cards on the lesson page
- print CSS now explicitly targets the climate-card section and worksheet tables
- the top-right print button is present and wired to `window.focus(); window.print()`

## Runtime verification completed

A working local HTTP preview path was used together with headless Chrome DevTools Protocol checks against the current repo state.

Verified locally on the updated Lesson 2 file:
- clicking the top-right print button invoked the print handler successfully (`window.__printCalled = 1` after clicking `.print-btn`)
- print media hides the print button and paywall overlay
- the lesson still includes all 4 embedded climate cards in print mode
- both worksheet tables render with `table-layout: fixed`
- both worksheet tables keep full page-width proportions in print emulation
- a print PDF was generated successfully for the lesson
- a print screenshot was captured successfully for visual review

Local verification artifacts generated during review:
- `/tmp/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.pdf`
- `/tmp/gr3-ess2-unit1-lesson2-climate-regions-and-conditions-print.png`

## Manual spot-check checklist after publish

Review target:
- `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html?review=1`

After deploy, confirm:
1. The top-right print button still opens print from the live page
2. All four climate cards remain readable without awkward splits or giant blank gaps
3. The climate-card note stays visually attached to the card block
4. The worksheet tables fit cleanly on the page
5. There is still no parent-facing instruction telling the family to supply climate cards
6. Screen layout still matches the normal LLC lesson structure

## Current status

This note now records successful local runtime print verification for the updated Lesson 2 file, plus a remaining live-site spot-check to perform after publish.