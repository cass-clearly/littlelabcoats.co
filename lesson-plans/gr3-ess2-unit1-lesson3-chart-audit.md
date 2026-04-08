# Grade 3 Earth Science Unit 1 Lesson 3 — Weather Chart Audit

Date: 2026-04-08
Target lesson file: `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`
Live lesson route: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`
Review route: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html?review=1`

## Purpose

This audit identifies every place Lesson 3 currently depends on an external parent-supplied weather chart or bar graph, confirms the in-repo file that drives the live lesson page, and selects the established LLC replacement pattern to use in the next implementation chunk.

## Current external-chart dependency map

### 1. Materials section
Location: `Materials` → `🏠 Household Items to Gather`

Current dependency:
- `A simple weather chart or bar graph`

Why it matters:
- This is the clearest direct parent-supplied requirement.
- The lesson currently asks the family to obtain the core instructional artifact from outside the lesson.

### 2. Procedure / lesson flow
Location: `Let's Get Started`

Current dependency points:
- Step 1: `Show students how a chart title and labels tell what kind of data they are reading.`
- Step 2: `Ask which day was warmest, wettest, windiest, or cloudiest based on the display.`
- Step 3: `Students use the data to say how one day was different from another.`
- Step 4: `Students explain a trend using numbers, bars, or symbols from the chart.`
- Step 5: `Students practice saying “I know this because the chart shows…”`

Why it matters:
- The full procedure assumes a chart/display already exists, but Lesson 3 does not actually provide one.
- The instructional sequence is already chart-centered, so the right fix is to supply the missing chart rather than redesign the lesson.

### 3. Student worksheet
Location: `Student Worksheet`

Current dependency points:
- Section title: `1️⃣ Read the Weather Chart`
- Prompt table asks for answers `from the chart`
- Trend prompt asks: `What pattern or trend do you notice in the chart or graph?`
- Claim frame asks students to complete: `because the chart shows ...`

Why it matters:
- The worksheet is structurally ready for a supplied chart.
- No worksheet redesign is required if the lesson page provides a concrete weather display students can reference.

### 4. Parent answer key
Location: `🔑 PARENT ANSWER KEY`

Current dependency points:
- `Answers will vary with the display used`
- Sample answer references a generic rainfall bar on Thursday rather than a lesson-specific display
- Troubleshooting language assumes a chart exists but does not identify a provided one

Why it matters:
- The answer key currently confirms that the lesson was written to depend on an outside display.
- Once a built-in chart is added, this section should become lesson-specific instead of variable-by-family.

### 5. Discussion + teacher note language
Location: `Discussion Questions` and `Parent/Teacher Notes`

Current dependency points:
- Repeated references to `the chart`, `the data`, and `the display`
- Teacher note: `point to the exact part of the chart`

Why it matters:
- These sections do not create the dependency by themselves, but they reinforce that a supplied in-lesson chart is the intended center of the activity.

## Pattern comparison: what LLC already does

### Adjacent Grade 3 Earth Science pattern
Reference files:
- `lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html`
- `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`

Observed pattern:
- The lesson shell stays self-contained in a single HTML file.
- Core learning artifacts are usually embedded directly in the lesson page as tables, worksheet sections, or other inline instructional markup.
- Adjacent lessons already rely on structured, printable in-page content rather than separate asset pipelines.

Implication for Lesson 3:
- The fix should happen in the lesson HTML itself, not by telling families to find a chart elsewhere.

### Established inline chart pattern elsewhere in LLC
Reference files:
- `lesson-plans/k-ess3-unit2-lesson2-water-resource.html`
- `lesson-plans/gr1-ess1-unit1-lesson6-patterns-in-the-sky.html`

Observed pattern:
- LLC commonly embeds instructional charts directly in the lesson page using local CSS classes and HTML tables.
- Example patterns include:
  - `water-chart` table embedded in the body of the lesson
  - `sky-patterns-chart` table embedded in the lesson content
- These charts are printable, styled consistently with the lesson color system, and usable as the actual student-facing interpretation artifact.

Implication for Lesson 3:
- The established house pattern is an inline chart/table inside the lesson page, not an external download requirement and not a parent-created substitute.

## Correct file(s) to edit

Primary lesson file to update:
- `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`

Potentially affected support file only if needed later:
- `lesson-plans/gr3-ess2-unit1-refcard-lesson3-reading-weather-data.html`

Current chunk conclusion:
- The objective can be satisfied by editing the lesson page in place.
- The refcard does not currently create the parent-supplied dependency and does not need to change for this audit chunk.

## Concrete implementation target for next chunk

Chosen target:
- Add an inline, lesson-embedded weather chart/data display directly inside `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`.

Recommended shape:
- A self-contained, printable weather chart/table styled with lesson-local CSS in the same pattern as other LLC embedded charts.
- Place it before or at the start of the interpretive activity so students can immediately use it for Steps 1–5 and the worksheet.
- Update nearby text so it explicitly points to the included chart rather than any parent-supplied material.

Why this is the right pattern:
- It preserves the existing lesson shell and flow.
- It matches established LLC inline chart/table conventions.
- It keeps the lesson family-friendly and print-ready.
- It lets the worksheet and answer key become specific to one high-quality provided chart rather than a variable outside artifact.

## Out of scope for this audit chunk

Not implemented yet:
- No chart added yet
- No lesson text changed yet
- No refcard changes yet
- No build/review-link verification yet
- No git commit/push yet
