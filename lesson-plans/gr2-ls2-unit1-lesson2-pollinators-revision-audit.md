# Grade 2 LS2 Unit 1 Lesson 2 — Pollinators Revision Audit

Status: chunk audit for Serena feedback revision
Date: 2026-04-09
Source lesson: `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
Primary review URL: `/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`

## Purpose

This audit narrows the real implementation surface for Serena's requested revision pass before content edits begin.

It documents:
- which files matter
- where the current mismatches live
- which Remarq/review fields must stay stable
- where each requested fix should be implemented

## Source file inventory

### 1) Primary lesson file
- `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`

This single file currently contains all of the following:
- lesson shell and styling
- Activity 1 and Activity 2 content
- pollinator-card markup
- student worksheet
- answer key
- feedback-layer script
- paywall and review-bypass logic

### 2) Route/index metadata
- `lesson-plans/_generated/lesson-index-data.json`

Relevant entry confirms:
- `slug`: `gr2-ls2-unit1-lesson2-pollinators`
- `sourcePath`: `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
- `canonicalUrl`: `/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
- `reviewUrl`: `/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`

### 3) Existing Grade 2 Life Science reference-card surface
- `lesson-plans/gr2-ls2-refcard.html`
- matching directory variant also exists: `lesson-plans/gr2-ls2-refcard/index.html`

Current state:
- this is a unit/domain-level ecosystems reference card
- it includes a short pollinator tile
- it does **not** include flower anatomy support for `anther`, `stigma`, `sepal`, or dissection guidance
- the lesson file does **not** currently link to a lesson-specific anatomy reference card

## Current mismatch verification in source

## Activity 2 pollinator-card issues

Within `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html` under `🌼 Activity 2: Who Pollinates What?`:

### Hummingbird card
Current rendered card uses:
- emoji/image surrogate: `🦜`
- name: `Hummingbird`
- match text: red tubular flowers

Issue:
- the visible card asset is a parrot emoji, not a hummingbird representation

### Moth card
Current rendered card uses:
- emoji/image surrogate: `🌙`
- name: `Moth`
- match text: white flowers blooming at night

Issue:
- the visible card asset is a moon emoji, not a moth representation

## Worksheet duplicates of the same issue

The same visual mismatch is repeated in the worksheet matching table:
- `🦜 Hummingbird`
- `🌙 Moth`

The same mismatch is repeated again in the answer key correct-match list:
- `🦜 Hummingbird`
- `🌙 Moth`

## Worksheet confusion verification

Within the same lesson file, `Part 1 — Label the Pollen Transfer Diagram` currently:
- asks students to use a word bank containing `anther`, `pollen`, `stigma`, `petal`, `seed`
- provides two generic flower boxes with blank lines
- asks students to `Draw arrows showing how pollen travels from Flower 1 to Flower 2`
- includes a separate dashed rectangle labeled `(draw your arrows here)`

Observed problems in source relative to Serena's feedback:
- the student-facing diagram does not explicitly show the flower parts being labeled
- the lesson has not yet made flower anatomy a main supported activity before this worksheet demand
- the arrow task is spatially disconnected from the flower boxes, making the intended path less obvious
- anatomy language appears in the worksheet before the lesson has sufficiently scaffolded it

## Flower anatomy/dissection mismatch verification

Current lesson anatomy support is present, but weakly integrated:
- vocabulary box includes `stamen`, `pistil`, and `stigma`
- science section mentions `stigma`
- extension list includes `Real Flower Dissection`
- parent/teacher notes include a short instruction to find stamens and stigma on real flowers
- worksheet asks students to identify flower parts
- answer key includes flower-part explanations

Mismatch:
- flower anatomy is treated as a side note / extension, while the worksheet expects it as core understanding
- there is no lesson-specific flower anatomy reference card currently supporting the worksheet or family review flow

## Remarq and review wiring that must remain unchanged

Within `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`:

### Body document id
- `<body data-document-id="doc_8COJPE7TH7w">`

### Feedback-layer script
- `src="https://cassclearly.com/feedback-layer.js?v=20260408"`
- `data-api-url="https://cassclearly.com"`
- `data-document-id="doc_8COJPE7TH7w"`
- `data-content-selector="body"`

### Review-mode bypass behavior
The paywall script currently checks:
- `window.location.search.indexOf('review=1') !== -1`

Behavior that must be preserved:
- review mode sets access in local storage and returns early
- paywall should not block the public review URL when `?review=1` is present

### Routing metadata that must remain stable
In `lesson-plans/_generated/lesson-index-data.json`:
- canonical route remains `/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
- review route remains `/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`

## Implementation map for Serena's four requested fixes

## 1) Replace incorrect hummingbird and moth card visuals/content
Primary edit surface:
- `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`

Exact components to revise:
- Activity 2 pollinator-card grid
- worksheet Part 3 matching table
- answer key Part 3 correct-match list

Likely scope:
- replace `🦜` with a hummingbird representation
- replace `🌙` with a moth representation
- verify surrounding explanatory text still matches the chosen visual

## 2) Fix confusing worksheet Part 1
Primary edit surface:
- `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`

Exact components to revise:
- worksheet `Part 1 — Label the Pollen Transfer Diagram`
- possibly worksheet `Part 2 — Label the Flower Parts`
- parent/teacher notes if scaffold language changes
- answer key Part 1 and Part 2 to match the new student task

Likely direction:
- either add an actual anatomy diagram students can use directly
- or simplify Part 1 so it no longer asks for unsupported labeling before anatomy has been taught

## 3) Clarify the pollen-transfer-with-arrows task
Primary edit surface:
- `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`

Exact components to revise:
- worksheet Part 1 instructions
- worksheet arrow-drawing area / visual layout
- answer key Part 1 arrow expectations

Likely direction:
- make the target path explicit: pollen starts on Flower 1, sticks to the bee, then lands on Flower 2
- reduce ambiguity by integrating arrows into the actual diagram instead of a disconnected blank box

## 4) Resolve the disconnected flower-anatomy section
Primary edit surfaces:
- `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
- possible new lesson-specific reference card file if created during implementation

Exact components to revise in the lesson:
- science/setup sequence before worksheet
- extension section, especially `Real Flower Dissection`
- parent/teacher notes
- worksheet sections using anatomy terms
- answer key expectations

Recommended implementation direction from audit:
- promote flower dissection from optional extension to core lesson flow
- add a flower-anatomy reference support artifact for student/parent use
- do **not** force this into the existing broad `gr2-ls2-refcard.html` unless there is a strong product reason to keep all LS2 support on one poster

Reason:
- `gr2-ls2-refcard.html` is a broad ecosystems summary card, not a lesson-specific anatomy support sheet
- Serena's request is lesson-specific and tied to worksheet usability
- a dedicated lesson-level anatomy reference card is the cleaner implementation surface if a new support asset is needed

## File-touch expectation for the next implementation chunk

Definitely expected:
- `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`

Possibly expected, only if a new support artifact is introduced:
- a new lesson-specific reference card file under `lesson-plans/` for flower anatomy / flower dissection support
- route/index metadata only if that new support artifact needs explicit linking elsewhere

Not currently required just for the revision itself:
- changing the lesson slug
- changing the review URL
- changing the Remarq document id
- changing the feedback-layer host or API host

## Audit conclusion

This revision is centered on one live lesson file with three tightly coupled areas inside it:
1. visible pollinator-card representations
2. worksheet/task clarity
3. lesson-flow scaffolding for flower anatomy

The current review surface is already identified and routed correctly. The Remarq-sensitive fields to preserve are:
- body `data-document-id`
- feedback-layer `data-document-id`
- feedback-layer `data-api-url`
- `?review=1` bypass logic

The main open implementation decision for the next chunk is whether Serena's requested anatomy support should be:
- embedded entirely into the lesson file, or
- supported by a new lesson-specific flower anatomy reference card

Based on current repo structure, a lesson-specific support card is the cleaner fit than expanding the broad Grade 2 LS2 refcard.
