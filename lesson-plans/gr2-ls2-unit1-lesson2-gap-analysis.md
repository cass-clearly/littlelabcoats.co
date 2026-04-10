# Grade 2 LS2 Unit 1 Lesson 2 — Pollinators Gap Analysis Against Source and Live

Last verified: 2026-04-10
Target review URL: `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`
Canonical URL: `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
Source file: `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
Authoritative comment inventory: `lesson-plans/gr2-ls2-unit1-lesson2-live-comment-inventory.md`
Verified document ID in source and live page: `doc_8COJPE7TH7w`

## Scope for this chunk

This file evaluates only the **actionable** comments from the authoritative live inventory:
- `cmt_hwZG7xWu4Dw`
- `cmt_WnxtyKxYK3Y`
- `cmt_ja0CZ_OoMck`
- `cmt_owSIHIW_p7w`

Non-actionable, duplicate, and blocked/ambiguous comments remain accounted for in the inventory file and are not implementation drivers here.

## Verification method used

### Local source inspection
- searched `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html` for learning-objective wording, `Hummingbird`, `Moth`, pollinator image references, and Remarq wiring
- inspected the Activity 3 pollinator grid block, worksheet matching block, answer key text, and feedback-layer script block
- inspected current asset files:
  - `images/pollinators/hummingbird-card.svg`
  - `images/pollinators/moth-card.svg`

### Live-page inspection
- fetched `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`
- verified live learning-objective markup against the literal all-caps/italics comment
- verified live pollinator image references for the hummingbird and moth assets
- verified live page still exposes `data-document-id="doc_8COJPE7TH7w"` and `feedback-layer.js`

## Comment-by-comment compliance audit

### 1) `cmt_WnxtyKxYK3Y`
- **Literal comment text:**
  > Learning objective uses ALL CAPS on 'EXPLAIN' and 'CREATE'. Must change to italics per curriculum style guide. Inconsistent with L3, L5 which use italics for action verbs.
- **Exact implementation surface:** `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
- **Local source evidence:**
  - learning objective currently reads:
    - `Students will <em>explain</em> the role of pollinators in plant reproduction and <em>create</em> a model demonstrating how pollen transfers from flower to flower.`
  - this is present in the local source and no `EXPLAIN`/`CREATE` all-caps wording remains in the learning objective.
- **Live review page evidence:**
  - fetched live review HTML contains:
    - `Students will <em>explain</em> the role of pollinators in plant reproduction and <em>create</em> a model demonstrating how pollen transfers from flower to flower.`
  - fetched live review HTML does **not** contain:
    - `Students will EXPLAIN the role of pollinators`
    - `Students will <strong>EXPLAIN</strong> the role of pollinators`
- **Compliance status:** `satisfied in both source and live`
- **Next-chunk implication:** no implementation change required for this comment unless a fresh live pull shows regression.

### 2) `cmt_hwZG7xWu4Dw`
- **Literal comment text:**
  > Moth is shown with a butterfly emoji 🦋. Moths and butterflies are different insects — a moth emoji 🪲 doesn't exist but using 🦋 is misleading for learners. Consider replacing with 🌕 (the nocturnal/moon symbol already used in the description) or simply spelling it out without a representative emoji to avoid confusion.
- **Exact implementation surfaces:**
  - `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
  - specifically:
    - Activity 3 pollinator grid moth card
    - worksheet Part 3 moth row
    - answer key Part 3 moth line
- **Current local source evidence:**
  - Activity 3 moth card uses:
    - `<img src="../images/pollinators/moth-card.svg?v=20260410" alt="Illustration of a moth pollinator near a moonlit night sky">`
    - plus text: `→ White flowers (night blooming) 🌕`
  - worksheet Part 3 moth row uses:
    - `<img src="../images/pollinators/moth-card.svg?v=20260410" alt="">`
  - answer key moth line is text-only:
    - `<li><strong>Moth</strong> → 🌕 <strong>White flowers (blooms at night)</strong> — moths are nocturnal; white flowers are visible in moonlight</li>`
  - no `🦋` butterfly emoji occurrence was found in the current lesson source for the moth treatment.
- **Live review page evidence:**
  - fetched live review HTML includes the moth image reference:
    - `../images/pollinators/moth-card.svg?v=20260410`
  - fetched live review HTML includes `Moth` plus `🌕` in the flower-match text.
  - fetched live review HTML does not show evidence of `🦋` in the inspected snippets for the moth treatment.
- **Compliance status:** `satisfied in both source and live for the specific anti-butterfly-emoji requirement`
- **Important boundary note:** this comment is satisfied only with respect to its literal requirement to stop showing the moth as a butterfly emoji / misleading butterfly treatment. It does **not** satisfy Chris's separate Gemini-image requirement.
- **Next-chunk implication:** no further implementation is required for this Rachel comment if the current source/live state remains intact.

### 3) `cmt_ja0CZ_OoMck`
- **Literal comment text:**
  > Use gemini to make an image for this hummingbird.
- **Exact implementation surfaces:**
  - `images/pollinators/hummingbird-card.svg`
  - `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
    - Activity 3 hummingbird card image reference
    - worksheet Part 3 hummingbird row image reference
- **Current local source evidence:**
  - Activity 3 hummingbird card uses:
    - `<img src="../images/pollinators/hummingbird-card.svg?v=20260410" alt="Illustration of a hummingbird pollinator hovering by a red tubular flower">`
  - worksheet Part 3 hummingbird row uses:
    - `<img src="../images/pollinators/hummingbird-card.svg?v=20260410" alt="">`
  - asset file exists: `images/pollinators/hummingbird-card.svg`
  - inspected asset content shows a hand-authored/static SVG illustration, but the current repo evidence does **not** prove Gemini was used to make this image.
- **Live review page evidence:**
  - fetched live review HTML includes:
    - `../images/pollinators/hummingbird-card.svg?v=20260410`
  - this proves the live page currently uses the same hummingbird asset reference as local source.
  - it does **not** prove the live asset is Gemini-generated.
- **Compliance status:** `unmet / not provably satisfied in source or live`
- **Reason:** the literal comment requires Gemini specifically. Current evidence only proves that a hummingbird image exists, not that Gemini was used to make it.
- **Required implementation target for next chunk:**
  - generate or source a hummingbird image with Gemini
  - save the resulting asset in the repo (likely replacing or superseding `images/pollinators/hummingbird-card.svg` or swapping to a new Gemini-derived asset path)
  - update `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html` references if the asset filename/path changes
- **Asset-generation requirement identified before implementation begins:** `yes — Gemini required explicitly by comment text`

### 4) `cmt_owSIHIW_p7w`
- **Literal comment text:**
  > Use gemini to make an image for this moth.
- **Exact implementation surfaces:**
  - `images/pollinators/moth-card.svg`
  - `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
    - Activity 3 moth card image reference
    - worksheet Part 3 moth row image reference
- **Current local source evidence:**
  - Activity 3 moth card uses:
    - `<img src="../images/pollinators/moth-card.svg?v=20260410" alt="Illustration of a moth pollinator near a moonlit night sky">`
  - worksheet Part 3 moth row uses:
    - `<img src="../images/pollinators/moth-card.svg?v=20260410" alt="">`
  - asset file exists: `images/pollinators/moth-card.svg`
  - inspected source/asset state shows a current moth image exists, but the current repo evidence does **not** prove Gemini was used to make this image.
- **Live review page evidence:**
  - fetched live review HTML includes:
    - `../images/pollinators/moth-card.svg?v=20260410`
  - this proves the live page currently uses the same moth asset reference as local source.
  - it does **not** prove the live asset is Gemini-generated.
- **Compliance status:** `unmet / not provably satisfied in source or live`
- **Reason:** the literal comment requires Gemini specifically. Current evidence only proves that a moth image exists, not that Gemini was used to make it.
- **Required implementation target for next chunk:**
  - generate or source a moth image with Gemini
  - save the resulting asset in the repo (likely replacing or superseding `images/pollinators/moth-card.svg` or swapping to a new Gemini-derived asset path)
  - update `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html` references if the asset filename/path changes
- **Asset-generation requirement identified before implementation begins:** `yes — Gemini required explicitly by comment text`

## Source vs live difference summary

### No source/live drift found for these checked surfaces
- learning objective italics state matches between source and live
- hummingbird image reference matches between source and live
- moth image reference matches between source and live
- live review page still carries the expected Remarq document ID and feedback-layer script

### Actual unmet work identified
- unmet work is **not** currently a source/live mismatch on the checked HTML surfaces
- unmet work is the lack of provable Gemini-generated hummingbird and moth images required by Chris's literal comments

## Exact files/assets/routes needing changes in the next implementation chunk

### Must change
1. `images/pollinators/hummingbird-card.svg`
   - or a new Gemini-generated hummingbird asset path if not replacing in place
2. `images/pollinators/moth-card.svg`
   - or a new Gemini-generated moth asset path if not replacing in place
3. `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
   - only if asset filenames/paths or alt text need updating after Gemini asset creation

### Verify-only; no change currently indicated
1. `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
   - learning objective italics already compliant
2. Remarq/review wiring on live page
   - `data-document-id="doc_8COJPE7TH7w"`
   - `feedback-layer.js`
3. review route
   - `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`

## Actionable-comment status table

| Comment ID | Short label | Source status | Live status | Final status for this chunk | Concrete implementation target / reason |
| --- | --- | --- | --- | --- | --- |
| `cmt_WnxtyKxYK3Y` | Italicize EXPLAIN/CREATE | satisfied | satisfied | satisfied in both source and live | no change required |
| `cmt_hwZG7xWu4Dw` | Remove misleading butterfly treatment for moth | satisfied | satisfied | satisfied in both source and live | no change required for this literal requirement |
| `cmt_ja0CZ_OoMck` | Use Gemini for hummingbird image | not provably satisfied | not provably satisfied | unmet | Gemini-generated hummingbird asset plus lesson reference verification |
| `cmt_owSIHIW_p7w` | Use Gemini for moth image | not provably satisfied | not provably satisfied | unmet | Gemini-generated moth asset plus lesson reference verification |

## Chunk conclusion

Every actionable comment now has an explicit status against both local source and the live review page:
- two comments are already satisfied in both source and live
- two comments remain unmet because the literal text requires Gemini-generated imagery and current evidence does not prove Gemini provenance

This gap analysis is the execution map for the next implementation chunk.
