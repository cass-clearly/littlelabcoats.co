# Grade 2 LS2 Unit 1 Lesson 2 — Pollinators Revision Audit

Status: current-state audit for Serena revision completion
Date: 2026-04-09
Lesson source: `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
Reference-card source: `lesson-plans/gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination.html`
Primary live review URL: `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`
Reference-card review URL: `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination.html?review=1`

## Purpose

This audit establishes the exact current delta for Serena's requested Grade 2 pollinators revision work without relying on the previously failing screenshot/headless-render path.

It answers:
- what files are in scope
- where each requested change lives in source
- whether the requested changes are already present locally
- what review wiring must remain stable
- what non-headless validation path should be used for the next implementation/review loop

## Files inspected

### Primary lesson package
- `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
- `lesson-plans/gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination.html`

### Routing / entry surfaces
- `lesson-plans/_generated/lesson-index-data.json`
- `lesson-plans/index.html`
- `lesson-plans/review/index.html`

### Prior audit / status notes reviewed
- `lesson-plans/gr2-ls2-unit1-lesson2-review-readiness.md`
- `lesson-plans/gr2-remarq-review-wiring-audit.md`

## Coupled files for this lesson revision

### Required implementation surface
1. `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
   - contains lesson content, worksheet, answer key, paywall/review bypass, and lesson Remarq wiring

2. `lesson-plans/gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination.html`
   - lesson-linked support artifact for anatomy/dissection and worksheet coherence

### Stable metadata / route surfaces to verify, not necessarily edit
1. `lesson-plans/_generated/lesson-index-data.json`
   - confirms canonical and review URLs for the lesson

2. `lesson-plans/index.html`
   - contains both canonical lesson link and explicit review-mode link

3. `lesson-plans/review/index.html`
   - contains direct review-mode entrypoint

## Route audit

Confirmed in `lesson-plans/_generated/lesson-index-data.json`:
- `slug`: `gr2-ls2-unit1-lesson2-pollinators`
- `sourcePath`: `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
- `canonicalUrl`: `/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
- `reviewUrl`: `/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`

Confirmed review entry surfaces:
- `lesson-plans/index.html` includes:
  - `/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
  - `/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`
- `lesson-plans/review/index.html` includes:
  - `/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`

Audit conclusion on routing:
- lesson routing is already stable and correctly exposes review mode
- this chunk does **not** require slug or route changes

## Requested-change map to exact source areas

All requested Serena revisions are already present in the local lesson package.

### 1) Correct the hummingbird and moth cards
Primary lesson locations:
- lesson pollinator grid under `🌼 Activity 3: Who Pollinates What?`
- worksheet `Part 3 — Who Pollinates What? Match It!`
- answer key `Part 3 — Who Pollinates What? (Correct Matches)`

Current source state:
- Hummingbird uses `🐦`
- Moth uses `🦋`
- explanatory text matches the intended pollinator/flower relationships

Implementation delta from this audit:
- none currently identified in local source
- next chunk should only verify these remain intact after any further lesson edits

### 2) Fix the confusing worksheet / anatomy flow
Primary lesson locations:
- `🌸 Activity 2: Flower Anatomy Mini-Lab`
- worksheet `Part 1 — Show the Path of Pollen`
- worksheet `Part 2 — Label the Flower Parts`
- parent/teacher notes section
- answer key Parts 1 and 2

Current source state:
- flower anatomy appears as a full main activity before worksheet use
- worksheet Part 1 now explicitly instructs students to write `anther` on Flower 1 and `stigma` on Flower 2
- Part 1 uses a reduced word bank focused on `anther`, `pollen`, and `stigma`
- parent/teacher notes explicitly instruct adults to teach flower parts before starting the worksheet

Implementation delta from this audit:
- none currently identified in local source
- if future content edits touch worksheet wording, Part 1 / Part 2 / answer key / teacher notes must remain synchronized

### 3) Clarify the pollen-transfer question aim
Primary lesson locations:
- worksheet `Part 1 — Show the Path of Pollen`
- Activity 2 Step 3 (`Connect Anatomy to Pollination`)
- parent/teacher note about `anther → bee → stigma`
- answer key Part 1

Current source state:
- pollen path is explicitly named: pollen starts on the anther, pollinator carries it, pollen lands on the stigma
- worksheet directions specify arrow 1 from anther to bee and arrow 2 from bee to stigma
- answer key mirrors the same path

Implementation delta from this audit:
- none currently identified in local source
- this path wording is now a coupling point and should stay identical across lesson, worksheet, and answer key

### 4) Make flower dissection a main lesson part
Primary lesson locations:
- `📦 Materials` (`🌸 For the Flower Anatomy Mini-Lab`)
- `🌸 Activity 2: Flower Anatomy Mini-Lab`
- extensions section
- parent/teacher notes

Current source state:
- real-flower inspection and gentle dissection are in the main lesson body, not only in extensions
- materials explicitly prepare for the mini-lab
- family support callout points learners to the anatomy reference card during mini-lab and worksheet time

Implementation delta from this audit:
- none currently identified in local source

### 5) Include a flowering plant anatomy reference card so the worksheet becomes coherent
Primary support-file location:
- `lesson-plans/gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination.html`

Lesson link locations:
- Activity 2 Step 1 link to the reference card
- family support tip box link to the reference card
- materials section references the printable card

Current source state:
- lesson-specific anatomy reference card exists
- card covers `anther`, `stigma`, `pollen`, `sepal`, `petal`, mini-lab steps, and pollination path support
- card has its own feedback-layer / Remarq wiring

Implementation delta from this audit:
- none currently identified in local source

## Exact lesson sections governing the requested areas

### Pollinator cards
In `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`:
- `🌼 Activity 3: Who Pollinates What?`
- worksheet `Part 3 — Who Pollinates What? Match It!`
- answer key `Part 3 — Who Pollinates What? (Correct Matches)`

### Worksheet / anatomy flow
In the same lesson file:
- `🌸 Activity 2: Flower Anatomy Mini-Lab`
- worksheet `Part 1 — Show the Path of Pollen`
- worksheet `Part 2 — Label the Flower Parts`
- parent/teacher notes bullets about teaching flower parts before worksheet
- answer key Parts 1 and 2

### Pollen-transfer prompt / aim
In the same lesson file:
- Activity 2 Step 3 (`Connect Anatomy to Pollination`)
- worksheet Part 1 instructions and task callout
- answer key Part 1
- teacher note reinforcing `anther → bee → stigma`

### Flower dissection activity
In the same lesson file:
- materials subsection `🌸 For the Flower Anatomy Mini-Lab`
- Activity 2 Step 2 (`Try a Gentle Dissection`)
- family support tip box

### Print behavior
Lesson file:
- `@media print` block preserves print color and avoids breaking boxed lesson/worksheet elements apart
- `.page-break` is used to separate worksheet and answer key sections for printing

Reference-card file:
- `@media print` block with `@page` sizing/margins and simplified print styling

### Remarq document wiring
Lesson file:
- `<body data-document-id="doc_8COJPE7TH7w">`
- feedback-layer script:
  - `src="https://cassclearly.com/feedback-layer.js?v=20260408"`
  - `data-api-url="https://cassclearly.com"`
  - `data-document-id="doc_8COJPE7TH7w"`
  - `data-content-selector="body"`
- paywall review bypass checks `window.location.search.indexOf('review=1') !== -1`

Reference-card file:
- `<body data-document-id="doc_gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination">`
- feedback-layer script:
  - `src="https://cassclearly.com/feedback-layer.js?v=20260408"`
  - `data-api-url="https://cassclearly.com"`
  - `data-document-id="doc_gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination"`
  - `data-content-selector="body"`

## Live HTML verification findings

### Lesson review URL
Checked:
- `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`

Confirmed via direct HTML fetch:
- HTTP `200`
- live HTML contains `data-document-id="doc_8COJPE7TH7w"`
- live HTML contains the production feedback-layer script on `cassclearly.com`
- live HTML contains `🌸 Activity 2: Flower Anatomy Mini-Lab`
- live HTML contains `🌼 Activity 3: Who Pollinates What?`
- live HTML contains `Part 1 — Show the Path of Pollen`
- live HTML contains `Part 2 — Label the Flower Parts`

### Reference-card review URL
Checked:
- `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination.html?review=1`

Confirmed via direct HTML fetch:
- HTTP `200`
- live HTML contains `data-document-id="doc_gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination"`
- live HTML contains the production feedback-layer script on `cassclearly.com`
- live HTML contains the expected `Flower Anatomy &amp; Pollination` title/content

## Current delta conclusion

For the specific Serena-requested revision items, this audit found **no remaining source-level implementation gap** in the local lesson package.

What is already present locally and on the live review path:
- corrected hummingbird and moth cards
- anatomy/dissection promoted into the main lesson flow
- explicit pollen-transfer path wording
- clearer worksheet setup and aligned answer key
- dedicated flower anatomy reference card linked from the lesson
- production Remarq script + stable document IDs on both lesson and support card

So the next implementation chunk should treat this lesson as a **verify-and-preserve surface**, not a from-scratch content rewrite, unless a human review comment identifies a new change request.

## Non-headless verification plan for the remaining work

Do **not** reuse the failing screenshot/browser-render path as a gate.

Use this verification sequence instead:

1. **Source validation**
   - inspect local lesson and support-card HTML directly
   - confirm required section headings, card copy, worksheet wording, answer-key wording, print CSS hooks, and Remarq fields

2. **Route/link validation**
   - confirm canonical and review URLs in `lesson-plans/_generated/lesson-index-data.json`
   - confirm public review entrypoints in `lesson-plans/index.html` and `lesson-plans/review/index.html`
   - confirm lesson links to the anatomy reference card remain correct

3. **Live HTML validation**
   - fetch live review URLs with `curl`
   - verify HTTP `200`
   - grep for key strings proving deployment success:
     - lesson headings
     - worksheet section names
     - feedback-layer script
     - expected `data-document-id` values

4. **Remarq wiring validation**
   - verify body `data-document-id`
   - verify feedback-layer `data-document-id`
   - verify `data-api-url` remains `https://cassclearly.com`
   - verify lesson still contains `?review=1` bypass logic

5. **Browser-capable fallback available in this environment**
   - if an alternate browser-capable text or HTTP inspection tool is available, use it only as a secondary confirmation
   - do not block completion on screenshot capture or full headless rendering

Acceptance standard for this task:
- local source contains the requested revisions
- live review HTML matches the intended revised structure/content
- Remarq wiring remains intact on the deployed review page
- no dependency on screenshot/headless render success

## Next chunk recommendation

Next chunk should focus on one of two paths only:

### Path A — if no new human feedback appears
- run final implementation verification against current source and live HTML
- review diff / git state
- commit and push if working tree changes are required
- re-fetch live review URLs after push
- hand back ready-for-review links

### Path B — if a new human review comment identifies a fresh issue
- edit the lesson and the anatomy reference card together as needed
- keep worksheet / answer key / teacher notes synchronized
- preserve the document IDs, review bypass behavior, and `cassclearly.com` feedback-layer wiring

## Audit conclusion

This chunk is complete when treated as a current-state inspection task.

Findings:
- all required Serena changes are mapped to exact source areas
- the dependent files that move together are identified
- the review/public URLs are confirmed
- the Remarq-sensitive wiring is documented
- a non-headless validation path is defined and proven viable via live HTML checks
