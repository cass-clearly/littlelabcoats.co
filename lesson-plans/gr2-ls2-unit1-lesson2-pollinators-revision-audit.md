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
- `lesson-plans/remarq-review-repair-final-report.md`

### Git history reviewed for claimed implementation state
- commit `1d600ec` — `feat: scaffold flower anatomy in grade 2 pollinators lesson`
- commit `a2764dd` — `docs: record grade 2 pollinators review readiness`
- commit `7fbbb92` — `docs: clarify render-check limitations for pollinators review`
- commit `a40b2a8` — `Document Grade 2 pollinators review validation`

## Normalized reviewer checklist (source-of-truth for the next live audit)

### Serena
1. **Pollinator visuals must be correct**
   - reported concern: the moth still reads like a butterfly and the hummingbird still does not read as an actual hummingbird
   - verification surfaces:
     - `🌼 Activity 3: Who Pollinates What?`
     - worksheet `Part 3 — Who Pollinates What? Match It!`
     - answer key `Part 3 — Who Pollinates What? (Correct Matches)`
   - dependent visual/source surface:
     - current lesson uses inline emoji/icon-style visuals, not external raster image files, so the live audit must verify what those visuals actually look like in the public page render

2. **Worksheet / anatomy flow must be coherent**
   - requested change: stop asking students to label unsupported anatomy and make the worksheet make sense with the lesson setup
   - verification surfaces:
     - `🌸 Activity 2: Flower Anatomy Mini-Lab`
     - worksheet `Part 1 — Show the Path of Pollen`
     - worksheet `Part 2 — Label the Flower Parts`
     - parent/teacher notes
     - answer key Parts 1 and 2

3. **Pollen-transfer task must clearly show the intended path**
   - requested change: make the goal explicit instead of leaving students to infer it
   - verification surfaces:
     - Activity 2 Step 3 (`Connect Anatomy to Pollination`)
     - worksheet Part 1 directions / task callout
     - answer key Part 1
     - teacher note reinforcing `anther → bee → stigma`

4. **Flower dissection must be a main lesson component**
   - requested change: move flower anatomy/dissection into the actual lesson flow, not a disconnected side note
   - verification surfaces:
     - `📦 Materials` mini-lab subsection
     - `🌸 Activity 2: Flower Anatomy Mini-Lab`
     - extensions / family-support references
     - parent/teacher notes

5. **Provide a flower anatomy reference card**
   - requested change: add a dedicated support artifact families can use during worksheet time
   - verification surfaces:
     - `lesson-plans/gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination.html`
     - lesson links to that refcard from Activity 2 and the family-support callout

### Rachel
- **No lesson-specific Rachel review artifact has been located yet for this lesson package in repo docs.**
- For the next audit pass, Rachel-specific work must be sourced from one of:
  - real Remarq comments on the live lesson/refcard pages
  - a later review artifact not yet located in repo search
  - explicit human-provided checklist outside the repo
- Until such evidence is found, Rachel items for this lesson should be tracked as `unrecovered / needs-source` rather than assumed complete.

### Margaret
- **No lesson-specific Margaret review artifact has been located yet for this lesson package in repo docs.**
- For the next audit pass, Margaret-specific work must be sourced from one of:
  - real Remarq comments on the live lesson/refcard pages
  - a later review artifact not yet located in repo search
  - explicit human-provided checklist outside the repo
- Until such evidence is found, Margaret items for this lesson should be tracked as `unrecovered / needs-source` rather than assumed complete.

## Current source and asset inventory

### Direct implementation files
1. `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
   - primary lesson file
   - contains the lesson shell, worksheet, answer key, pollinator-card visuals, review bypass logic, and lesson Remarq wiring

2. `lesson-plans/gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination.html`
   - lesson-linked support artifact for flower anatomy and pollination vocabulary / mini-lab support

### Review / discovery surfaces to verify against the live lesson
1. `lesson-plans/_generated/lesson-index-data.json`
   - canonical/review routing manifest for this lesson
2. `lesson-plans/index.html`
   - public lesson directory entry with open + review links
3. `lesson-plans/review/index.html`
   - public review directory entry with direct `?review=1` link

### Live URLs that define the shipped public surface
- lesson canonical: `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
- lesson review: `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`
- refcard canonical: `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination.html`
- refcard review: `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination.html?review=1`

### Pollinator-visual asset inventory
- no separate local image files are currently referenced by `gr2-ls2-unit1-lesson2-pollinators.html` for the hummingbird / moth pollinator cards
- the current lesson no longer uses the earlier plain emoji placeholders for the two disputed animal pollinators; it now uses inline SVG illustrations in both major student-facing placements:
  - `🌼 Activity 3: Who Pollinates What?`
    - Hummingbird card → inline blue/green bird SVG with long beak
    - Moth card → inline tan/brown moth SVG with four wings
  - worksheet `Part 3 — Who Pollinates What? Match It!`
    - Hummingbird row → same inline bird SVG reused as a compact icon
    - Moth row → same inline moth SVG reused as a compact icon
- the answer key `Part 3 — Who Pollinates What? (Correct Matches)` names `Hummingbird` and `Moth` in text only and does **not** contain a matching visual/icon for either animal
- because the disputed surfaces are custom inline illustrations rather than audited source-linked image files, the next implementation chunk must explicitly replace the hummingbird and moth SVG markup in both student-facing placements, not merely preserve the current state

## Baseline mapping of prior claimed fixes / commits

### Commit-backed implementation change
- `1d600ec` — `feat: scaffold flower anatomy in grade 2 pollinators lesson`
  - changed `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
  - created/changed `lesson-plans/gr2-ls2-unit1-refcard-lesson2-flower-anatomy-and-pollination.html`
  - baseline claim supported by file diff scope: anatomy mini-lab + support-card work landed here

### Documentation-backed claims only
- `a2764dd` / `7fbbb92` / `a40b2a8`
  - these later commits update audit/readiness documentation, not the lesson/refcard implementation files themselves
  - they should be treated as **claims about shipped state**, not proof that the visible public lesson matches reviewer intent

### Prior claimed-done map from repo docs
- Serena item: incorrect pollinator cards → claimed resolved in:
  - `lesson-plans/gr2-ls2-unit1-lesson2-review-readiness.md`
  - `lesson-plans/gr2-ls2-unit1-lesson2-pollinators-revision-audit.md`
  - source locations cited: Activity 3, worksheet Part 3, answer key Part 3
- Serena item: confusing worksheet/anatomy flow → claimed resolved in the same two docs
  - source locations cited: Activity 2, worksheet Parts 1–2, teacher notes, answer key
- Serena item: unclear pollen-transfer task → claimed resolved in the same two docs
  - source locations cited: Activity 2 Step 3, worksheet Part 1, answer key Part 1
- Serena item: make flower dissection a main lesson part → claimed resolved in the same two docs
  - source locations cited: Materials mini-lab block, Activity 2, family-support callout, teacher notes
- Serena item: add/use a flower anatomy reference card → claimed resolved in the same two docs
  - source locations cited: refcard file plus lesson links to it
- Rachel/Margaret broader review set for this lesson:
  - no repo artifact with explicit itemized comments has been located yet
  - current status for this chunk: `not yet sourced; must be recovered from live comments or another artifact before done/not-done claims can be trusted`

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

Most Serena-requested lesson revisions are already present in the local lesson package, but the hummingbird and moth visuals remain the active unresolved gap.

### 1) Correct the hummingbird and moth cards
Primary lesson locations:
- lesson pollinator grid under `🌼 Activity 3: Who Pollinates What?`
  - Hummingbird card block around lines `436–449`
  - Moth card block around lines `456–470`
- worksheet `Part 3 — Who Pollinates What? Match It!`
  - Hummingbird row icon around line `596`
  - Moth row icon around line `614`
- answer key `Part 3 — Who Pollinates What? (Correct Matches)`
  - text-only confirmation rows around lines `690` and `692`

Current source state:
- Hummingbird now uses a custom inline SVG rather than the earlier plain bird emoji
- Moth now uses a custom inline SVG rather than the earlier plain butterfly emoji
- explanatory text still matches the intended pollinator/flower relationships

Why these are still the active implementation gap:
- Serena's explicit complaint for this lesson remains that the hummingbird still does not read as an actual hummingbird and the moth still does not read clearly enough as the intended moth
- the current hummingbird drawing is generic and stylized enough that it can still read as a broad cartoon bird instead of a clearly recognizable hummingbird
- the current moth drawing is better than the old butterfly emoji, but it is still a simplified generic insect illustration rather than a carefully selected, clearly identifiable moth visual
- these two visuals appear twice each in the student-facing lesson package, so the next implementation chunk must update both placements for each animal to avoid mixed old/new visuals

Implementation delta from this audit:
- replace the hummingbird SVG in both the Activity 3 card and the worksheet Part 3 row
- replace the moth SVG in both the Activity 3 card and the worksheet Part 3 row
- keep the answer-key text relationship lines unless the visual rewrite requires tiny wording cleanup for consistency

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

The previously open hummingbird/moth visual gap has now been corrected in local source, and the lesson is in **pre-push local review** state rather than still waiting on the visual implementation itself.

### Serena items that are already supported in current source
- anatomy/dissection is promoted into the main lesson flow
- pollen-transfer path wording is explicit and synchronized across lesson, worksheet, and answer key
- worksheet setup is clearer and aligned with the answer key
- the dedicated flower anatomy reference card exists and is linked from the lesson
- production Remarq script + stable document IDs are present on both lesson and support card
- hummingbird visual replaced in both student-facing placements
- moth visual replaced in both student-facing placements

### This-pass local review result
- Activity 3 and worksheet Part 3 were manually rechecked after the SVG swap
- the updated hummingbird and moth visuals remain aligned with the existing captions and lesson flow
- the answer key remains correctly text-only for these pollinator entries
- no local source-level regression was found in the adjacent worksheet sections, answer-key structure, paywall logic, review bypass logic, or Remarq wiring
- live/public review-page verification is still pending for the later ship/verify chunk and is not claimed complete here

### Rachel / Margaret status
- no lesson-specific Rachel review artifact has been recovered in repo docs for this lesson package
- no lesson-specific Margaret review artifact has been recovered in repo docs for this lesson package
- therefore any Rachel/Margaret completion claim for this lesson remains `unsourced / pending recovery`, not done

So the next implementation chunk should treat this lesson as **ready for commit/push and live verification**, not as needing more local visual redesign unless live review reveals a new issue.

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

Next chunk should focus on shipping and live verification:

### Commit, push, and verify the public review page
- commit the lesson visual update plus this audit/status documentation
- push to GitHub
- fetch and inspect the public review URL after push
- confirm the shipped page exposes the updated hummingbird and moth visuals on the live review surface
- then prepare the final honest status summary that separates Serena-done items, this-pass fixes, and Rachel/Margaret unsourced/pending status

## Local review and regression-check notes

Status: local review pass completed; ready for commit/push pending live verification

Checks completed in local source:
- reviewed `🌼 Activity 3: Who Pollinates What?` in context and confirmed the new hummingbird and moth visuals fit the existing pollinator-card layout
- reviewed worksheet `Part 3 — Who Pollinates What? Match It!` and confirmed the compact icon versions stay paired with the correct labels and flower matches
- reviewed answer key `Part 3 — Who Pollinates What? (Correct Matches)` and confirmed no visual/icon dependency was introduced there
- rechecked adjacent lesson sections before and after the touched area so the swap did not disturb surrounding LLC structure or instructional flow
- rechecked `data-document-id`, feedback-layer script, and `?review=1` bypass logic in the lesson file so the visual edit did not disturb review-mode behavior
- rechecked the paywall overlay block and lock script so no accidental regression was introduced outside the pollinator swap

Local regression judgment:
- no obvious source-level structural regression remains
- no caption mismatch was found around the updated pollinator visuals
- no extra cleanup edit was required in the lesson HTML after this local review pass
- live/public verification still remains outstanding and must happen after push

## Audit conclusion

This lesson is locally review-clean for the hummingbird/moth fix and ready for the commit/push + live-verification chunk.

Findings:
- the updated hummingbird and moth visuals are present in both student-facing placements
- the answer key remains correctly text-only for these pollinator entries
- Serena-complete anatomy/worksheet/reference-card items remain intact alongside the new visual fix
- Rachel and Margaret review status for this lesson remains unsourced/pending rather than complete
- the dependent files, review/public URLs, and Remarq-sensitive wiring remain documented for the ship/verify chunk
