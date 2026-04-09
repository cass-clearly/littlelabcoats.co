# Learning Objective Standards Fix — Reusable Implementation Plan

Date: 2026-04-09

This document translates the audit into a repeatable implementation recipe for the library-wide Learning Objective standards fix.

Primary audit reference:
- `docs/learning-objective-library-audit.md`

## Locked goal

Every lesson page must include a standalone `Learning Objective` or `Learning Objectives` section as the **first top-level lesson section** after the title/meta/hero/standards top matter and **before** `The Big Idea`, `The Science`, `Materials`, and the rest of the lesson flow.

This plan is for **lesson pages only**. It does not modify quizzes, refcards, or PDFs.

## Non-negotiable preservation rules

When updating lesson files, preserve all of the following unless a specific issue requires a targeted fix:

- `body[data-document-id]`
- feedback-layer script tags and their `data-document-id`, `data-api-url`, and `data-content-selector`
- Remarq/review script placement and IDs
- preview/paywall containers such as `#llcPaywall` and `llc-paywall-overlay`
- preview lock logic, especially pages that intentionally lock from `Materials`
- `page-break` wrappers and worksheet/answer-key page ordering
- worksheet tables, response lines, and answer-key blocks
- print button behavior and print CSS
- existing visual theme colors, typography, and domain-specific styling

## Canonical insertion rule

Insert or normalize the Learning Objective section in this exact zone:

1. `h1` title
2. subtitle
3. meta bar
4. hero image / emoji hero (if present)
5. standards box
6. `h2` = `🎯 Learning Objective` or `🎯 Learning Objectives`
7. objective content block
8. existing concept section (`The Big Idea`, `The Big Science Idea`, `The Science`, `Background`, etc.)
9. existing remaining lesson flow unchanged

## Labeling rules

Use the label already native to the closest compliant template in that family whenever possible:

- Use **`🎯 Learning Objective`** when the page is written as a single summary sentence or paragraph.
- Use **`🎯 Learning Objectives`** when the page clearly uses a short bulleted set of 2–3 outcome statements and that style already matches nearby earlier lessons.
- Do **not** leave `Learning Goals` as the primary heading once updated.
- If a page currently has an inline tip-box objective, promote that content into the standalone first `h2` section and remove the redundant inline objective callout.

## Template-family mapping

The auditable non-compliant pages fall into a small set of implementation families. The next chunk should execute by family, not page-by-page improvisation.

### Family A — `Learning Goals` heading templates

**What they look like**
- A top-level `h2` such as `🎯 Learning Goals` or HTML-entity variants of the same
- Usually followed by bullets or short outcome text
- Common in legacy Grade 1 LS3, Grade 2 ESS/LS/PS, legacy Kindergarten `unit1-*`, free samples, and some standalone lessons

**Representative files**
- `lesson-plans/gr1-ls3-unit2-lesson1-you-look-like-your-parents.html`
- `lesson-plans/gr2-ps1-unit1-l1-matter.html`
- `lesson-plans/free-gr1-celery-rainbow.html`
- `lesson-plans/unit1-lesson1-push-pull-sort.html`

**Implementation recipe**
1. Find the existing `Learning Goals` section.
2. Move it so it becomes the first top-level `h2` section after the standards box if it is not already there.
3. Rename the heading to `🎯 Learning Objective` or `🎯 Learning Objectives`.
4. Reuse the existing goal content whenever it is already concise and lesson-specific.
5. If the current content is a long bullet list, tighten to the closest earlier-lesson pattern for that family rather than adding a second redundant objective block.
6. Leave all later sections in their existing order unless one of them must shift down by exactly one slot to accommodate the moved objective block.

**Preservation notes**
- Some of these pages have paywall copy that literally says `You're seeing the Learning Goals.` Update that text when touching the page in the implementation chunk so preview copy matches the new section name.
- Do not change worksheet page-break locations.

### Family B — `Big Idea`-first modern templates with no objective section

**What they look like**
- First top-level `h2` is `💡 The Big Idea`, `🎯 The Big Idea`, `The Big Idea`, or `🔬 The Big Science Idea`
- Often followed by `The Science`, `Materials`, `Let's Get Started`, etc.
- Common in Grade 3 PS, Grade 4 LS, Kindergarten ESS3, Kindergarten LS Unit 2, and some standalone upper-grade lessons

**Representative files**
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`
- `lesson-plans/k-ess3-unit2-lesson1-what-earth-gives-us.html`
- `lesson-plans/k-ls1-unit2-lesson1-whats-inside-a-seed.html`

**Implementation recipe**
1. Insert a new standalone Learning Objective section immediately after the standards box.
2. Use the nearby compliant family style to decide objective format:
   - paragraph form for engineering / modern lesson templates
   - boxed paragraph form if the family already uses `.objective-box` or a similar visual treatment
   - bullet list form only when the earlier sibling lessons in that family use `Learning Objectives`
3. Keep the existing `Big Idea` / `Science` / `Materials` sections in the exact same relative order after the new objective block.
4. Do not rewrite conceptual sections unless needed for grammar flow after insertion.

**Preservation notes**
- For pages with preview locking from `Materials`, the new objective must remain above `Materials` so preview depth improves without changing the lock boundary.
- For pages whose first `h2` currently anchors print flow, insert the new block before it without moving page-break containers.

### Family C — inline tip-box objective that must be promoted

**What they look like**
- No standalone Learning Objective `h2`
- Objective text exists inside a `tip-box` or similar inline callout after `The Big Idea`

**Representative file**
- `lesson-plans/k-ls1-unit2-lesson4-sunlight-or-no-sunlight.html`

**Implementation recipe**
1. Extract the existing inline objective sentence.
2. Add a standalone `🎯 Learning Objective` section immediately after the standards box.
3. Place the extracted sentence into that new objective block.
4. Remove the redundant inline objective tip-box, but keep neighboring vocabulary tip-boxes and science text unchanged.
5. Leave the existing `The Big Idea` section as the next top-level section after the new objective.

**Preservation notes**
- This is a normalization move, not a content rewrite.
- Keep the lesson’s experiment pacing, worksheet pages, and preview wiring untouched.

### Family D — science-first / free-sample templates with `Learning Goals` after science

**What they look like**
- The page begins with `The Science`
- `Learning Goals` appears later as a separate top-level section
- Often used in free lessons and some promotional/standalone pages

**Representative files**
- `lesson-plans/free-gr1-celery-rainbow.html`
- `lesson-plans/free-gr2-salt-dough-fossil-factory.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- `lesson-plans/free-gr4-apple-oxidation.html`
- `lesson-plans/free-gr5-bread-mold-terrarium.html`
- `lesson-plans/free-k-fizzy-color-explosions.html`

**Implementation recipe**
1. Do not leave `The Science` as the first section.
2. Promote the existing `Learning Goals` content into a new first section after standards.
3. Rename the heading to `🎯 Learning Objective` or `🎯 Learning Objectives`.
4. Keep `The Science` immediately after the objective unless the page already has a stronger compliant family ordering to match.
5. Update any paywall/preview copy that mentions `Learning Goals` so the UI language stays consistent.

**Preservation notes**
- Free samples may have slightly different paywall/review behavior; preserve feedback-layer wiring and any free-sample-specific unlock flow.
- Do not convert these into a totally different full-library layout; normalize only the top-of-lesson sequence.

### Family E — outlier standalone lessons using `Learning Goals` plus custom section names

**What they look like**
- Standalone or legacy lesson with custom concept section names like `Lesson Flow`, `Engineering Challenge`, or custom setup blocks
- May have custom `Materials` labels like `What You'll Need`

**Representative files**
- `lesson-plans/5th-fossils-earth-history.html`
- `lesson-plans/forces-motion-acceleration.html`
- `lesson-plans/bird-beak-buffet.html`
- `lesson-plans/5th-forces-balanced-unbalanced.html`

**Implementation recipe**
1. Preserve all custom section names after the objective block.
2. Reuse and rename the existing `Learning Goals` content rather than inventing a new objective paragraph if a usable goal section already exists.
3. Insert/move the objective block to immediately after the standards/top matter.
4. Leave later custom instructional sections untouched unless a heading must shift down to maintain the required first-section ordering.

**Preservation notes**
- These pages are most likely to have bespoke layout choices; keep changes extremely local to the top-of-lesson content stack.

## Family-to-scope mapping

Use these mappings during implementation so the next chunk does not have to re-classify pages manually.

### Learning Goals heading families
- Grade 1 LS3 parent/offspring unit lessons
- Grade 2 ESS unit pages using `gr2-ess1-unit3-l*`
- Grade 2 LS2 unit 2 pages using `gr2-ls2-unit2-l*`
- Grade 2 PS1 unit 1 pages using `gr2-ps1-unit1-l*`
- Legacy Kindergarten `unit1-lesson*` pages
- free sample lessons `free-*`
- standalone legacy/custom lessons that explicitly use `Learning Goals`

### Big Idea-first insertion families
- Grade 3 PS2 unit pages
- Grade 4 LS unit 1 and unit 2 pages in scope
- Kindergarten ESS3 unit 2 pages
- Kindergarten LS1 unit 2 pages except the inline-objective outlier
- any custom standalone lesson where first section is `The Big Idea` / `The Science` and there is no existing objective block

### Inline-objective normalization family
- `lesson-plans/k-ls1-unit2-lesson4-sunlight-or-no-sunlight.html`

## Template-update guidance

`lesson-plans/template.html` still documents `The Big Idea` before `The Science`, but it does not yet encode the locked library-wide Learning Objective-first rule.

For this standards-fix implementation:
- use the **audit + this implementation plan** as the operative source of truth
- do **not** let the template comments override the locked objective-first standard
- if the template itself is updated later, it should be a separate, deliberate follow-up change rather than accidental drift during the library fix

## Validation checklist for each edited lesson

### Section-order validation
- `Learning Objective` / `Learning Objectives` is the first lesson `h2`
- standards/top matter still appears above it
- `Big Idea` / `The Science` / `Materials` remain in the intended order after insertion
- worksheet section still starts only at the original worksheet page-break location
- answer key remains after worksheet pages

### Print-readiness smoke check
- no `page-break` wrapper moved or deleted
- no worksheet table, response line, draw box, or answer-key block shifted into the wrong page section
- no print CSS selector removed or renamed
- inserted objective block does not create obvious malformed HTML or swallow later content

### Remarq / review / preview preservation check
- `body[data-document-id]` unchanged
- feedback-layer script still present with the same `data-document-id`
- `#llcPaywall` and related preview overlay still exist when present before the edit
- preview lock logic still keys off `Materials` / `What You'll Need` / similar materials heading when that was the original behavior
- any user-facing paywall copy that says `Learning Goals` is updated if the page now says `Learning Objective`

## Fast execution order for the next chunk

1. Fix Family C first (`k-ls1-unit2-lesson4-sunlight-or-no-sunlight.html`) because it is the only misplaced case and provides the cleanest normalization pattern.
2. Fix Family A / D batches next by reusing existing `Learning Goals` content instead of writing brand-new objectives from scratch.
3. Fix Family B pages by inserting objective blocks into Big-Idea-first templates.
4. Finish Family E standalone custom pages with extra caution due to bespoke structure.
5. Run the validation checklist after each batch, not just at the end.

## Ready-for-implementation conclusion

The library now has a repeatable, family-based implementation strategy:
- rename-and-promote existing `Learning Goals` blocks where possible
- insert a new objective block only when the page truly has none
- promote inline objective content into a standalone first section when needed
- preserve worksheet structure, print layout, preview depth, and Remarq wiring in every case
