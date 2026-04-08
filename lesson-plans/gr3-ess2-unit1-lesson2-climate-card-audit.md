# Grade 3 Earth Science Unit 1 Lesson 2 — Climate Card Audit

Last updated: 2026-04-08
Status: audit complete for climate-card inclusion revision
Target lesson: `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`

## Purpose

This audit maps every place Unit 1 Lesson 2 currently depends on external climate-region comparison materials so the next implementation chunk can replace that dependency with included, lesson-native climate cards without breaking the existing LLC lesson shell.

## Authoritative files in scope

### Primary implementation file
- `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`

### Directly related support asset
- `lesson-plans/gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html`

### Related navigation / publishing references checked for scope only
- `lesson-plans/index.html`
- `lesson-plans/_generated/lesson-index-data.json`
- `lesson-plans/gr3-shareable-manifest.md`
- `lesson-plans/gr3-earth-science-batch-review.md`

## Lesson structure inventory

The main Lesson 2 file currently contains these sections in order:
1. title / subtitle / metadata
2. hero image + caption
3. NGSS standard box
4. learning objective
5. big idea
6. science explanation
7. vocabulary chips
8. materials
9. procedure (`Let's Get Started`)
10. discussion questions
11. extension
12. parent/teacher notes
13. student worksheet page
14. parent answer key page
15. feedback-layer / document-id wiring
16. paywall script and footer

This confirms the lesson follows the established Grade 3 LLC shell and should be revised in-place rather than restructured.

## Current climate-card dependency map

### 1) Materials section — explicit external dependency
File: `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`

Current wording:
- `Picture cards or a simple map of four climate regions`

Why it matters:
- This is the clearest existing parent-supplied requirement.
- It tells the family to provide or source the comparison material outside the lesson.
- It does not specify that the lesson itself contains the climate-region visuals needed for the activity.

### 2) Procedure Step 2 — implied dependency on external visuals/cards
File: `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`

Current wording:
- `Compare a hot dry desert, a rainy rainforest, a cold tundra, and a temperate region.`

Why it matters:
- The step assumes the family has something visible to compare.
- Because no in-lesson comparison asset currently exists, this instruction implicitly depends on the materials-list item above.
- This step is the strongest candidate to anchor the new included climate cards.

### 3) Procedure Step 4 — implied dependency carried into worksheet use
File: `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`

Current wording:
- `Students record typical conditions and explain how regions are different.`

Why it matters:
- Students need a source of region-specific information to fill the worksheet accurately.
- Right now, that source is implicitly the parent-provided picture cards or map.
- Once climate cards are embedded, this step should explicitly direct students to use the included cards.

### 4) Student Worksheet section 1 — implied dependency on external comparison source
File: `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`

Current worksheet prompt:
- `Compare Climate Regions`
- rows: `Desert`, `Rainforest`, `Tundra`, `Temperate Region`
- columns: `Usual Conditions` / `What might you expect there?`

Why it matters:
- The worksheet assumes students already have access to accurate region details.
- There is no on-page instruction pointing students to an included asset.
- This is a required update surface even though it does not currently say `cards` explicitly.

### 5) Parent Answer Key section 1 — implicit dependence on outside activity source
File: `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`

Current wording:
- `Desert: usually hot and dry. Rainforest: usually warm and rainy. Tundra: usually very cold. Temperate: moderate conditions with seasons.`

Why it matters:
- The answer key gives sample content, but it does not orient the parent to an included lesson asset.
- If the lesson gains climate cards, the answer key should reinforce that students should use those included cards as evidence.

## Confirmed non-references / no current climate-card wording

The following sections do **not** currently mention cards directly, but may still need wording adjustments later for consistency once cards are embedded:
- discussion questions
- extension
- parent/teacher notes
- worksheet section 2 (`Weather or Climate?`)
- worksheet section 3 (`Explain the Difference`)
- answer-key sections 2 and 3
- reference card file content

## Related asset review

### Reference card
File: `lesson-plans/gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html`

Findings:
- The refcard is a compact study support asset.
- It includes definition-level support only: climate, region, usual, long-term, plus a short `Remember This` box.
- It does **not** provide the four activity-ready climate-region comparison items needed for the lesson procedure.
- It should not be treated as the activity replacement by itself.

Decision:
- Keep the refcard conceptually separate from the lesson-embedded climate cards.
- The next chunk may optionally update the refcard only if tighter alignment is useful, but the required replacement for the parent-supplied materials must live inside the lesson page itself.

### Adjacent lesson pattern used as the model
File reviewed: `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`

Relevant pattern:
- Lesson 3 includes a dedicated in-lesson data block: `Weather Chart for This Lesson`.
- The chart sits directly after `Materials` and before `Let's Get Started`.
- Materials, procedure, worksheet, and answer key all explicitly refer to `the included weather chart on this lesson page`.

Why this matters:
- This is the clearest nearby LLC precedent for embedding a lesson-critical printable asset directly in the lesson body.
- It preserves the normal lesson shell while making the activity self-contained.
- It provides the best model for where and how Lesson 2 climate cards should be added.

## Best implementation target for next chunk

### Recommended placement
Insert a dedicated climate-card section in the main lesson file:
- after `Materials`
- before `Let's Get Started`

### Recommended format
Use an in-lesson printable block analogous to Lesson 3’s chart section, but tailored for climate-region comparison:
- section heading such as `Climate Cards for This Lesson`
- four clearly separated cards: Desert, Rainforest, Tundra, Temperate Region
- each card should include at minimum:
  - region name
  - typical temperature / moisture language
  - short `usual conditions` summary
  - simple visual cues or icons
  - one or two `what you might expect there` clues that map directly to the worksheet

### Why this is the best fit
- matches an existing Grade 3 Earth Science pattern already used successfully in Lesson 3
- keeps the asset inside the lesson instead of pushing families to a separate printable or outside supply
- allows explicit wording updates in materials, procedure, worksheet, and answer key to point to `the included climate cards on this lesson page`
- preserves current page order and LLC style conventions

## Exact file-and-section edit targets for next chunk

### Must edit
#### `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`
Sections to update:
- `Materials`
- new in-lesson climate-card block inserted after `Materials`
- `Let's Get Started` steps 2 and 4 at minimum
- worksheet section 1 prompt/instructions
- answer key section 1 sample guidance
- any success criteria / troubleshooting wording that should point families back to the included cards

### Probably no edit needed for this chunk’s follow-on implementation
#### `lesson-plans/gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html`
Reason:
- the refcard is a separate support asset, not the activity material the lesson currently lacks
- the objective can be achieved without changing it

### Scope-only references; do not edit unless later verification shows breakage
- `lesson-plans/index.html`
- `lesson-plans/_generated/lesson-index-data.json`
- `lesson-plans/gr3-shareable-manifest.md`
- `lesson-plans/gr3-earth-science-batch-review.md`

## Audit conclusion

The climate-card problem is currently localized to the main Lesson 2 lesson page, not the navigation or refcard system.

The actual dependency chain is:
- explicit in `Materials`
- implied in procedure steps 2 and 4
- implied in worksheet section 1
- implicitly unsupported in answer key section 1

The cleanest LLC-consistent fix is to add a dedicated in-lesson printable `Climate Cards for This Lesson` block directly after `Materials`, then update all dependent wording to reference the included cards on the lesson page instead of parent-provided materials.
