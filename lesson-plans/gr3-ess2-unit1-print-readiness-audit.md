# Grade 3 Earth Science Unit 1 — Weather & Climate Print-Readiness Audit

Last updated: 2026-04-08
Status: audit + shared-shell implementation + local runtime verification complete for the Grade 3 Weather & Climate print pass
Primary priority: `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html` and `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`

## Purpose

This audit is the implementation handoff for the print-readiness fixes requested after the recent embedded-artifact work.

It identifies:
- the concrete files currently responsible for Grade 3 Weather & Climate print behavior
- what is lesson-specific vs duplicated shell-level behavior
- the likely root causes for Lesson 2 and Lesson 3 print problems
- the minimal file set for the next implementation chunk

## Files currently responsible for print behavior

### Highest-priority lesson files
- `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`
- `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`

### Same-shell comparison files used to separate local vs repeated behavior
- `lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html`
- `lesson-plans/gr3-ess2-unit1-lesson5-designing-for-local-weather.html`
- `lesson-plans/gr3-ess2-unit1-lesson6-reducing-weather-related-hazards.html`

### Directly related support assets reviewed for scope
- `lesson-plans/gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html`
- `lesson-plans/gr3-ess2-unit1-refcard-lesson3-reading-weather-data.html`
- `lesson-plans/gr3-ess2-unit1-lesson2-climate-card-audit.md`
- `lesson-plans/gr3-ess2-unit1-lesson3-chart-audit.md`
- `lesson-plans/gr3-earth-science-batch-review.md`

### Reference-only print guidance / pattern files
- `lesson-plans/style-guide.html`
- `lesson-plans/template.html`
- `lesson-plans/template-preview.html`

## Current-state findings

### Lesson 2 current content state
`lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html` already includes:
- a dedicated `Climate Cards for This Lesson` section
- explicit references to `the included climate cards on this lesson page`
- no obvious remaining parent-supplied climate-card instruction in the main lesson file

Conclusion:
- the core content dependency appears already fixed in the lesson itself
- the remaining Lesson 2 work is primarily print/layout/readability work, not basic content sourcing

### Lesson 3 current content state
`lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html` already includes:
- a dedicated `Weather Chart for This Lesson` section
- explicit references to `the included weather chart on this lesson page`
- worksheet and answer-key language tied to the included chart

Conclusion:
- the current issue is not absence of the chart
- the current issue is whether the embedded chart and surrounding worksheet/table flow remain truly printable after the embed change

## Structural pattern comparison: what is shared vs local

### Repeated shell-level pattern found across nearby Grade 3 lessons
Lessons 1, 2, 3, 5, and 6 all repeat the same general structure inline inside each lesson HTML file:
- fixed top-right `.print-btn`
- inline print-button wiring in the lesson shell
- page-level inline CSS including `@media print`
- paywall overlay markup (`.llc-paywall-overlay`)
- paywall lock script that hides content after `Materials` unless unlocked or `?review=1`
- feedback-layer script

Important implication:
- there is no obvious centralized shared print component in this part of the repo
- the `shared` print behavior is functionally duplicated shell code, not a single imported stylesheet/component
- any shell-level fix may need to be repeated in each affected lesson file unless an upstream generator exists elsewhere

### Lesson-specific artifact pattern
Lesson 2 adds print-critical climate-card structures:
- `.climate-card-section`
- `.climate-card-grid`
- `.climate-card`
- `.climate-card-note`

Lesson 3 adds print-critical weather-data structures:
- `.weather-chart-section`
- `.weather-chart`
- `.chart-key`
- worksheet `compare-table` blocks tied to the chart

Important implication:
- some fixes will belong only to Lesson 2 and Lesson 3 because the embedded artifacts are different
- some fixes may still belong to the duplicated shell pattern shared by nearby lessons

## Regression map

## 1) Lesson 2 — climate-card print/layout issues

### Confirmed current state
The lesson now supplies its own climate cards.
That part should be preserved.

### Root-cause candidates from code inspection
1. **Climate cards are embedded inside a 2-column CSS grid with no print-specific grid fallback.**
   - `.climate-card-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }`
   - There is no print-specific rule that forces one column, fixed card sizing, or controlled card stacking.
   - Likely risk: cards may shrink too much, produce uneven card heights, or create awkward white gaps in print.

2. **Climate-card blocks are protected individually from splitting, but the grid/container is not print-tuned for page flow.**
   - `.climate-card-section` and `.climate-card` are covered by `break-inside: avoid` / `page-break-inside: avoid`.
   - That avoids card splitting, but it can also create large blank areas if a card or section gets pushed as a unit.
   - Likely risk: awkward gaps and uneven page fill.

3. **Worksheet tables use the generic `.compare-table` pattern without print-specific table rules.**
   - No explicit print treatment for table row splitting, column widths, or header repetition.
   - Likely risk: region-comparison tables break awkwardly or crowd cells when printed.

4. **The lesson shell does not include broader print handling for embedded artifact sections beyond generic `break-inside` rules.**
   - Good enough for simple boxes, likely insufficient for card grids and worksheet tables.

### Fix-scope decision for Lesson 2
- **Lesson-specific fixes:** climate-card layout, climate-card print stacking/sizing, any Lesson 2 worksheet/table tuning
- **Duplicated shell-level fixes:** only if print-button or generic page-break/overlay behavior is also broken in runtime

## 2) Lesson 3 — weather-chart and worksheet print/layout issues

### Confirmed current state
The lesson now supplies its own weather chart.
That part should be preserved.

### Root-cause candidates from code inspection
1. **The weather chart section is not included in the `@media print` break-protection list.**
   - Current print rules protect `.procedure-step, .question-box, .teacher-note, .materials-box, .tip-box, .extension-box, .answer-key, .standards-box, .objective-box`
   - They do **not** include `.weather-chart-section`, `.weather-chart`, or `.chart-key`
   - Likely risk: the embedded chart can split awkwardly across pages or separate from its heading/key.

2. **Worksheet tables also use the generic `.compare-table` pattern without print-specific treatment.**
   - Same risk as Lesson 2, but more acute here because the worksheet is chart-dependent and comparison-heavy.
   - Likely risk: broken row grouping, cramped columns, awkward table splits.

3. **The embedded weather table has no print-specific sizing or proportional rules.**
   - No explicit print font-size adjustments, column width constraints, or table-layout guidance.
   - Likely risk: the chart can crowd, compress, or leave strange spacing depending on browser print behavior.

4. **Artifact heading/grouping is vulnerable.**
   - `h1, h2, h3 { break-after: avoid; }` helps headings, but there is no artifact-group print rule that keeps the section intro, table, and chart key together sensibly.
   - Likely risk: the heading stays with a tiny fragment while the actual chart or key jumps.

### Fix-scope decision for Lesson 3
- **Lesson-specific fixes:** weather-chart section grouping, chart table sizing, worksheet table print behavior, chart key placement
- **Duplicated shell-level fixes:** only if runtime confirms print-button or generic shell behavior is also contributing

## 3) Shared duplicated shell-level print behavior

### Print button wiring
Observed in both priority lessons and nearby comparison lessons:
- top-right button exists in markup as a fixed `.print-btn` in each duplicated lesson shell
- the repaired shared-shell version now uses `type="button"` plus `window.focus(); window.print()`

Code-path conclusion:
- the current button wiring itself is simple and not obviously broken in source
- if the button fails in practice, the likely causes are runtime state issues, overlay interactions, or browser behavior rather than missing JS

### Paywall / review interaction
Observed in both priority lessons:
- paywall hides content from `Materials` onward unless local storage is unlocked or `?review=1` is present
- print CSS hides `.llc-paywall-overlay`

Risk profile:
- in review mode (`?review=1`) the paywall script should not intentionally hide the lesson
- in locked mode, print could still be misleading if content is hidden before the user clicks print
- this is a shell-level runtime concern, not specific to the embedded artifact sections

### Shared print CSS limits
The repeated shell-level `@media print` block does these things well:
- hides `.print-btn`
- hides `.llc-paywall-overlay`
- preserves background colors
- protects common content boxes from splitting

But the repeated block does **not** yet handle:
- embedded artifact tables/charts/cards as a first-class print concern
- generic worksheet table pagination
- artifact-specific spacing cleanup after the embed work
- print-friendly fallback layout for multi-column card grids

### Fix-scope decision for duplicated shell-level behavior
- **Shell-level / repeated lesson-shell fix bucket:**
  - shared print-button runtime verification
  - any generic print CSS additions for repeated lesson shell classes if those additions are safe beyond Lessons 2 and 3
- **Do not over-generalize yet:**
  - climate-card grid rules are Lesson 2 specific
  - weather-chart rules are Lesson 3 specific

## Relevant comparison against established LLC lesson patterns

Compared against nearby Grade 3 lessons, Lessons 2 and 3 still follow the normal LLC shell order:
1. title / subtitle / meta
2. standards
3. learning objective
4. big idea / science
5. materials
6. artifact block (new embedded section)
7. procedure
8. discussion
9. extension
10. notes
11. worksheet
12. answer key
13. feedback layer / paywall / footer

Conclusion:
- no major structural rewrite is needed
- the embedded artifact work belongs in the lesson pages
- the regressions are about print tuning of that structure, not about replacing the structure

## Runtime / print-preview check status

### What was checked
- static code-path review of the duplicated print-button wiring
- static inspection of `@media print` blocks
- static inspection of page-break coverage, card/chart/table classes, and paywall script flow
- attempted headless Chrome PDF print runs against Lesson 2 and Lesson 3 local review routes
- attempted headless Firefox screenshot runs against Lesson 2 and Lesson 3 local review routes using temporary profiles

### Runtime result
A working local HTTP preview path plus headless Chrome DevTools Protocol checks completed successfully against the updated local repo state.

Successful local runtime checks included:
- click-test verification of the top-right print button on Lessons 2, 3, and 5
- print-media emulation checks confirming the print button and paywall overlay are hidden in print
- successful print-PDF generation for Lessons 2, 3, and 5
- successful print screenshots for Lessons 2, 3, and 5
- visual print-emulation spot-checks confirming the embedded climate cards, embedded weather chart, and nearby shared-shell worksheet tables remain proportioned and readable

### What is confirmed vs not yet confirmed

#### Confirmed by code inspection and local runtime verification
- the top-right print button is present in the lesson markup and now uses `window.focus(); window.print()`
- Lessons 1, 2, 3, 5, and 6 share the duplicated lesson-shell print behavior and now use the updated print-button wiring
- Lesson 2 contains its own embedded climate-card section
- Lesson 3 contains its own embedded weather-chart section
- the local print pass now verifies the embedded artifact classes and nearby shared worksheet tables render with materially improved print handling

#### Still best to confirm after deploy on the live site
- final production pagination on the published pages
- final live click behavior in the deployed environment

Audit consequence:
- the shared-shell print implementation is now locally runtime-verified
- remaining follow-up is a live-site spot-check after commit/push/deploy
- for human/manual follow-up, the intended review targets are:
  - `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html?review=1`
  - `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html?review=1`

## Minimal implementation file set for the next chunk

### Must edit
- `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`
- `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`

### May need edits if runtime confirms duplicated shell-level issues beyond these two lessons
- `lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html`
- `lesson-plans/gr3-ess2-unit1-lesson5-designing-for-local-weather.html`
- `lesson-plans/gr3-ess2-unit1-lesson6-reducing-weather-related-hazards.html`

Reason:
- these lessons appear to share the same inline print-button/paywall/print CSS shell
- only touch them if a shell-level fix is truly needed and safe to repeat

### No change required for this next chunk unless later alignment is desired
- `lesson-plans/gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html`
- `lesson-plans/gr3-ess2-unit1-refcard-lesson3-reading-weather-data.html`
- `lesson-plans/gr3-earth-science-batch-review.md`

Reason:
- the main lesson pages are the print-critical artifact surface
- the refcards are separate support assets, not the source of the current print regressions

## Implementation decision summary

### Fixes that belong in lesson-specific markup/CSS
- Lesson 2 climate-card print layout
- Lesson 2 climate-card grid fallback / card sizing / spacing
- Lesson 2 worksheet table print tuning if needed
- Lesson 3 weather-chart section grouping
- Lesson 3 chart sizing / table print behavior / chart-key flow
- Lesson 3 worksheet table print tuning if needed

### Fixes that belong in duplicated shared shell code only if runtime confirms the problem
- print-button behavior that still fails despite the repaired shared-shell `window.focus(); window.print()` wiring
- generic print CSS additions that are safe for all nearby Grade 3 lessons
- paywall/print interaction problems that are not unique to Lessons 2 and 3

### Best next implementation posture
Use a **mix**:
- lesson-specific artifact layout fixes first
- duplicated shell-level print fixes only where the behavior is clearly shared and not just local to one artifact type

## Done-state for this audit chunk

This audit now provides:
- a concrete affected-file list
- a regression map for Lesson 2, Lesson 3, and duplicated shell-level behavior
- a clear split between lesson-specific and repeated-shell fix scope
- a minimal implementation file set for the next chunk
- an explicit boundary between findings confirmed by code inspection and findings that still need browser print verification

## Known remaining limitation

Local runtime verification is now complete, but the final production proof still requires a live-site spot-check after commit/push/deploy so the published pages can be confirmed on their real review URLs.