# Grade 3 Implementation Baseline

Last updated: 2026-04-07
Status: authoritative implementation baseline for the Grade 3 completion run

## Purpose

This file defines the implementation baseline for all remaining Grade 3 Little Lab Coats work in this run.

Use it together with `lesson-plans/gr3-curriculum-audit-and-scope.md`.
The audit file defines **what must be built**.
This baseline file defines **how it must be built**.

---

## Non-negotiable rules

- Do **not** invent a new Grade 3 lesson shell.
- Do **not** block on missing Grade 3 year-map docs.
- Do **use** the explicit scope in `gr3-curriculum-audit-and-scope.md` as the authoritative build list for this run.
- Do **reuse** the existing Grade 3 LS1 lessons as continuity anchors.
- Do **reuse** existing LLC live patterns for lesson pages, refcards, quizzes, preview behavior, and catalog wiring.
- Do **build support artifacts with the lessons** where the unit workflow expects them.
- Do **preserve the deeper preview boundary** used by the current Grade 3 lesson anchors.

---

## Source-of-truth precedence

### 1. What to build
Use:
- `lesson-plans/gr3-curriculum-audit-and-scope.md`

This is the authoritative scope file for:
- remaining Grade 3 LS1 lessons beyond Lessons 1 and 2
- the locked `3-ESS2 Unit 1` Earth Science build set
- the locked `3-ETS1 Unit 1` Engineering build set
- the concrete lesson/refcard/quiz path plan for each unit
- support-asset expectations
- route/catalog touchpoints

### 2. Primary Grade 3 continuity anchors
Use these first for shell, pacing, print behavior, and family-facing tone:
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`

Use them for:
- Grade 3 visual rhythm
- section order
- lesson pacing
- worksheet + answer-key split
- review/paywall pattern
- grade-band tone

### 3. Strongest adjacent structural shell
Use this when a modern LLC shell detail needs a stronger nearby implementation reference:
- `lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html`

Use it for:
- exact modern lesson architecture
- colored box system
- print layout rules
- reusable class/component patterns
- paywall/review implementation details

### 4. Terminology and brand authority
Use:
- `lesson-plans/style-guide.html`

Use it for:
- exact section names
- metadata conventions
- standards wording
- worksheet/answer-key naming
- grade-band wording rules

### 5. Refcard pattern anchors
Use the Grade 3 PS2 refcards as the current refcard pattern source:
- `lesson-plans/gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html`

Use them for:
- per-lesson refcard naming rhythm
- unit-consistent support asset styling
- compact support-page structure

### 6. Quiz pattern anchors
Use:
- `lesson-plans/gr3-ps2-unit1-quiz.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html`

Use them for:
- Grade 3 quiz structure
- support-asset packaging expectations
- review/paywall compatibility on quiz artifacts

### 7. Engineering content anchor
Use:
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-refcard.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html`

Use them for:
- engineering challenge tone
- family-facing build/test framing
- support-asset packaging

Do **not** treat them as proof the canonical 6-lesson Grade 3 engineering unit already exists.

### 8. Catalog/navigation wiring anchors
Use:
- `index.html`
- `curriculum.html`
- `curriculum/index.html`

Use them for:
- Grade 3 unit card structure
- lesson listing patterns
- quiz-link placement
- public discovery surface parity

---

## Grade 3 lesson shell: required structure

Unless a tiny science-specific adjustment is needed internally, new Grade 3 lesson pages should follow this order:

1. `body[data-document-id="..."]`
2. optional print button
3. `h1` title
4. italic subtitle
5. metadata bar
6. hero image or emoji + caption
7. standards box
8. `The Big Idea`
9. `The Science`
10. vocabulary tip box
11. `Materials`
12. `Let's Get Started`
13. `Discussion Questions`
14. `Extensions`
15. `Parent/Teacher Notes` or `Parent / Teacher Notes`
16. `.page-break` + `Student Worksheet`
17. `.page-break` + `Parent Answer Key`
18. `feedback-layer.js`
19. paywall overlay and scripts
20. footer/copyright block

### Exact required section names
Use these names exactly:
- `The Big Idea`
- `The Science`
- `Materials`
- `Let's Get Started`
- `Discussion Questions`
- `Extensions`
- `Parent/Teacher Notes` or `Parent / Teacher Notes`
- `Student Worksheet`
- `Parent Answer Key`
- `NGSS Standard:`

### Forbidden substitutions
Do not swap in alternatives like:
- `Procedure`
- `Instructions`
- `Overview`
- `Concept`
- `Reflection Questions`
- `Handout`
- `Data Sheet`
- `Teacher Guide`

---

## Approved reusable patterns

### Core classes/patterns to preserve
- `.meta`
- `.hero-image`
- `.emoji-hero`
- `.caption`
- `.standards-box`
- `.tip-box`
- `.materials-box`
- `.procedure-step`
- `.question-box`
- `.discussion-hint`
- `.extension-box`
- `.teacher-note`
- `.worksheet-section`
- `.name-date`
- `.answer-key`
- `.page-break`
- `.print-btn`

### Color logic to preserve
Keep the functional LLC box-color system recognizable across Grade 3 lessons:
- standards box: lavender/purple
- vocabulary box: cyan
- materials box: gold/orange
- discussion/procedure boxes: LLC instructional colors
- extensions box: indigo/light purple
- parent/teacher notes: gray dashed

Do not invent a different box-color language for every Grade 3 domain.
The lessons should feel like one product family.

---

## Metadata, terminology, and print rules

### Metadata order
Use:
1. Grade
2. Duration
3. Subject
4. optional kit badge only if justified

Never add `Setting:`.

### Standards box rules
- label must be singular `NGSS Standard:`
- include full code and full performance expectation text
- place standards box immediately after hero/caption

### Materials rules
- use specific quantities where possible
- use bullet lists rather than vague one-word lists
- use subheads only when helpful

### Worksheet rules
Every full lesson should include a dedicated worksheet page when the unit pattern expects it.
Minimum expectations:
- starts on a new page
- clear `Student Worksheet` title
- `Name / Date` line
- usable writing/drawing space
- prompts that match the lesson task

### Parent answer key rules
Every full lesson should include a dedicated answer-key page when the unit pattern expects it.
Minimum expectations:
- starts on a new page
- uses `Parent Answer Key` exactly
- includes sample acceptable answers
- includes success criteria / what success looks like
- includes parent-facing notes where helpful

### Print rules
Preserve:
- page breaks for worksheet and answer key
- print color preservation
- `break-inside: avoid` / `page-break-inside: avoid` for major boxes
- printable family-friendly layout

---

## Preview / paywall / review baseline

### Mandatory implementation pieces
Modern Grade 3 lessons should preserve:
- `body[data-document-id="..."]`
- `feedback-layer.js` with matching document ID
- `llcPaywall`
- `llc_access` localStorage pattern
- `?review=1` bypass behavior
- consistent `/store.html` CTA pattern

### Verified preview-depth pattern to copy forward
The current Grade 3 lesson anchors use a deeper preview rule that locks from the first `h2` matching:
- `materials`
- `gather before you start`
- `what you need`

Verified in:
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html`
- `lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`
- `lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html`
- `lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`
- `lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`

### Preview-depth rule for every new lesson in this run
When creating the remaining Grade 3 Life Science, Earth Science, and Engineering lessons:
- copy the deeper `lock-from-Materials` behavior
- do not regress to the older shallow goal-based lock boundary
- confirm the actual keywords in the file, not just the overlay copy

### Quiz note
`lesson-plans/gr3-ps2-unit1-quiz.html` is a useful quiz-pattern anchor for review/paywall packaging, but lesson-style preview-depth logic is anchored first by the lesson files above.

---

## Unit-support baseline

### Refcards
When a Grade 3 unit uses per-lesson refcards:
- keep naming consistent across the full unit
- keep visual structure consistent across the full unit
- use the PS2 refcards as the anchor pattern
- do not let one refcard drift into a different design language

### Unit quizzes
When a full 6-lesson unit is completed:
- create the quiz in the same implementation pass or batch where the workflow expects it
- align coverage to the actual six completed lessons
- use Grade 3 quiz anchors already in repo

### Unit packaging rule for this run
For each newly completed unit in this run:
- lesson pages + support artifacts should be planned together
- use the concrete path plan locked in `gr3-curriculum-audit-and-scope.md`
- default support convention is **per-lesson refcards + one unit quiz**
- route and catalog touchpoints should be tracked alongside content creation
- review artifacts should cover the unit content and its support assets honestly

---

## Route and catalog baseline

### Current repo touchpoints to update later
The main Grade 3 discovery surfaces currently relevant are:
- `index.html`
- `curriculum.html`
- `curriculum/index.html`

### Tracking rule for each new artifact
For each new lesson/support file later created, track:
- current file path
- intended public URL
- unit/domain placement
- whether it needs a catalog entry
- whether a quiz/support asset also needs a catalog link

### Important boundary for this chunk
This baseline identifies the wiring points.
It does **not** require catalog edits yet.

---

## Reusable build checklist for future chunks

### A. Source-pattern check
- [ ] I am using `gr3-curriculum-audit-and-scope.md` for what to build
- [ ] I am using Grade 3 LS1 Lessons 1–2 as the primary continuity anchors
- [ ] I am using `gr2-ls2-unit1-lesson1-what-do-plants-need.html` when I need the strongest structural shell reference
- [ ] I am following `style-guide.html` terminology exactly
- [ ] I am not inventing a new format

### B. Shell check
- [ ] `body[data-document-id]` exists
- [ ] title + subtitle + metadata exist
- [ ] hero + caption exist
- [ ] standards box exists
- [ ] `The Big Idea` exists
- [ ] `The Science` exists
- [ ] vocabulary box exists
- [ ] `Materials` exists
- [ ] `Let's Get Started` exists
- [ ] `Discussion Questions` exists
- [ ] `Extensions` exists
- [ ] `Parent/Teacher Notes` exists
- [ ] `Student Worksheet` starts on a new page
- [ ] `Parent Answer Key` starts on a new page

### C. Preview/review check
- [ ] feedback layer exists with matching document ID
- [ ] paywall overlay exists
- [ ] `llc_access` logic exists
- [ ] `?review=1` bypass exists
- [ ] preview locks from `Materials` rather than a shallow goal section

### D. Support-asset check
- [ ] refcard pattern matches the chosen unit-wide pattern
- [ ] quiz pattern matches Grade 3 quiz anchors
- [ ] unit support assets are named consistently

### E. Tracking check
- [ ] file path is recorded
- [ ] intended URL is recorded
- [ ] later navigation/catalog touchpoint is recorded
- [ ] review-artifact target is recorded

---

## Review-loop honesty rule

For future chunks:
- do not mark Rachel review complete unless real comments exist
- do not mark Margaret review complete unless real comments exist
- do not mark revision rounds done unless the file changes were actually made
- do not mark anything live unless it was actually pushed/published later

---

## Recommendation for the next implementation chunks

Use this baseline exactly for:
- Grade 3 LS1 Lessons 3–6
- the new Grade 3 Earth Science unit
- the new Grade 3 Engineering unit

Default pattern decision order:
1. follow `gr3-curriculum-audit-and-scope.md` for scope
2. follow Grade 3 LS1 Lessons 1–2 for continuity
3. follow `gr2-ls2-unit1-lesson1-what-do-plants-need.html` for shell details
4. follow `style-guide.html` for terminology
5. follow PS2 refcards/quizzes and current Grade 3 catalog surfaces for support-asset and wiring patterns
