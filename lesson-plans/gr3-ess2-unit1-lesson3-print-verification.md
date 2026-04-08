# Grade 3 Earth Science Unit 1 Lesson 3 — Print Verification Note

Last updated: 2026-04-08
Target file: `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`
Live review URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html?review=1`

## What changed for Lesson 3 print readiness

The lesson page now includes Lesson 3–specific print safeguards for the embedded weather-data artifact and worksheet:

- print sizing for the embedded weather chart and worksheet table
- explicit chart and worksheet column widths via `colgroup`
- `thead` / `tbody` structure for better print table behavior
- repeated table-header support in print
- print margin control with `@page`
- stronger break handling for:
  - `.weather-chart-section`
  - `.chart-key`
  - `.worksheet-section`
  - `.compare-table`
- print-safe chart wrapper behavior (`overflow: visible` in print)
- safer text wrapping in printed table cells
- top-right print button is now wired as `type="button"` plus `onclick="window.focus(); window.print();"`

## What is verified by code inspection

Confirmed in `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`:
- the embedded weather chart is still present and lesson-native
- the worksheet comparison table is still present and lesson-native
- print CSS now explicitly targets the chart section and worksheet table behavior
- table structure now supports more reliable print layout than the previous markup
- the top-right print button is present and wired to `window.focus(); window.print()`

## Runtime verification completed

A working local HTTP preview path was used together with headless Chrome DevTools Protocol checks against the current repo state.

Verified locally on the updated Lesson 3 file:
- clicking the top-right print button invoked the print handler successfully (`window.__printCalled = 1` after clicking `.print-btn`)
- print media hides the print button and paywall overlay
- the embedded weather chart remains present in print mode
- the weather chart and worksheet comparison table both render with `table-layout: fixed`
- the weather chart, chart key, and worksheet table all stayed visually readable in print emulation
- a print PDF was generated successfully for the lesson
- a print screenshot was captured successfully for visual review

Local verification artifacts generated during review:
- `/tmp/gr3-ess2-unit1-lesson3-reading-weather-data.pdf`
- `/tmp/gr3-ess2-unit1-lesson3-reading-weather-data-print.png`

## Manual spot-check checklist after publish

Open:
- `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html?review=1`

After deploy, confirm:
1. The top-right print button still opens print from the live page
2. The weather chart fits on page at readable size
3. The chart header row remains readable and proportioned correctly
4. The chart key stays near the chart without creating a large blank gap
5. The worksheet table columns remain readable and do not overflow page width
6. There are no awkward page splits through the chart or first worksheet table
7. Screen layout still matches the normal LLC lesson structure

## Current status

This note now records successful local runtime print verification for the updated Lesson 3 file, plus a remaining live-site spot-check to perform after publish.