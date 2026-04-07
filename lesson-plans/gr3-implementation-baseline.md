# Grade 3 Implementation Baseline

Last updated: 2026-04-07

## Purpose

This file is the implementation standard for all remaining Grade 3 Little Lab Coats work.

Use it when building or modernizing any Grade 3 lesson, refcard, or quiz batch.

This guide is intentionally derived from:
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`
- `lesson-plans/gr3-ls1-unit1-lesson1-template-audit.md`
- `lesson-plans/gr3-ls1-unit1-lesson2-template-audit.md`
- `lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html`
- `lesson-plans/style-guide.html`

It should be treated as the reusable baseline for every remaining Grade 3 batch.

---

## Non-negotiable rule

**Do not invent a new visual format, page architecture, naming convention, route style, or review/paywall behavior for Grade 3.**

All remaining Grade 3 work should:
- reuse the modern LLC lesson shell already established in Grade 3 LS1 Lesson 1 and Lesson 2
- follow the terminology rules in `lesson-plans/style-guide.html`
- use `lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html` as the strongest adjacent structural shell where needed
- use existing live Grade 3 pages as continuity anchors, not as loose inspiration

If a new lesson needs a structure decision, the answer is almost always:
1. follow Grade 3 LS1 Lesson 1 and Lesson 2 first
2. if a shell detail is ambiguous, mirror `gr2-ls2-unit1-lesson1-what-do-plants-need.html`
3. only borrow topic mechanics from other lessons; do not borrow an entirely different format

---

## Source-of-truth precedence

### Primary Grade 3 continuity anchors
1. `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
2. `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`

Use these for:
- Grade 3 visual rhythm
- page architecture
- worksheet + answer-key split
- preview/paywall/review behavior
- family-facing tone
- print layout and section pacing

### Primary shell reference when a reusable pattern is needed
3. `lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html`

Use this for:
- exact modern LLC shell behavior
- class/component patterns
- colored-box system
- print rules
- paywall/review implementation pattern

### Terminology authority
4. `lesson-plans/style-guide.html`

Use this for:
- exact section names
- metadata conventions
- standards-box wording
- worksheet/answer-key naming
- grade-band wording rules

### Topic-only references
5. Grade/topic-specific lessons outside the baseline set

Use only for:
- science sequencing
- content examples
- worksheet prompt ideas

Do **not** use topic-only references to justify a new shell or visual pattern.

---

## Grade 3 lesson shell: exact required structure

All remaining Grade 3 lesson pages should follow this order unless a very small topic-specific reason requires an internal variation.

1. `body[data-document-id="..."]`
2. optional print button
3. `h1` title
4. italic subtitle
5. metadata bar
6. hero image or emoji + caption
7. standards box
8. `The Big Idea`
9. `The Science`
10. key vocabulary tip box
11. `Materials`
12. `Let's Get Started`
13. `Discussion Questions`
14. `Extensions`
15. `Parent/Teacher Notes` or `Parent / Teacher Notes`
16. `.page-break` + `Student Worksheet`
17. `.page-break` + `Parent Answer Key`
18. feedback-layer script
19. paywall overlay markup and scripts
20. footer/copyright block

### Explicitly required section names
Use these exact names:
- `The Big Idea`
- `The Science`
- `Materials`
- `Let's Get Started`
- `Discussion Questions`
- `Extensions`
- `Parent/Teacher Notes` or `Parent / Teacher Notes`
- `Student Worksheet`
- `Parent Answer Key`
- `NGSS Standard:` (singular)

### Explicitly forbidden substitutions
Do not replace the standard labels with alternatives like:
- `Procedure`
- `Instructions`
- `Overview`
- `Concept`
- `Reflection Questions`
- `Handout`
- `Data Sheet`
- `Teacher Guide`
- `Notes to Instructors`

---

## Template reference matrix

| Area | Required baseline | Approved source pattern | Required / optional | Notes |
|---|---|---|---|---|
| Overall shell | Grade 3 LS1 modern shell | `gr3-ls1-unit1-lesson1`, `gr3-ls1-unit1-lesson2`, `gr2-ls2-unit1-lesson1` | required | no new shell invention |
| Title + subtitle | centered, print-friendly, unit framing | Grade 3 LS1 L1/L2 | required | moderate emoji use is okay for Grade 3 |
| Metadata bar | Grade, Duration, Subject, optional kit badge | style guide + LS1 L1/L2 | required | do not add `Setting:` |
| Hero block | emoji or visual anchor + caption | LS1 L1/L2 | required | should feel like same family as existing Grade 3 pages |
| Standards box | purple/lavender box after hero | style guide + LS1 L1/L2 + gr2 plants | required | use singular `NGSS Standard:` |
| `The Big Idea` | concise conceptual anchor | LS1 L1/L2 | required | section appears before `The Science` |
| `The Science` | clear family-facing science explanation | LS1 L1/L2 + gr2 plants | required | do not skip for remaining Grade 3 lessons |
| Vocabulary tip box | cyan tip box | LS1 L1/L2 + gr2 plants | required | may use chips plus sentence-based vocab box |
| `Materials` | gold box, specific quantities | style guide + gr2 plants | required | use bullet lists, not vague material names |
| `Let's Get Started` | procedure-step blocks with times | LS1 L1/L2 + gr2 plants | required | not `Procedure` |
| `Discussion Questions` | question boxes + italic hints | LS1 L1/L2 + gr2 plants | required | every question needs a hint |
| `Extensions` | extension box | LS1 L1/L2 | required | concise, useful, family-facing |
| `Parent/Teacher Notes` | dashed gray note box | LS1 L1/L2 + style guide | required | Grade 3 should not regress to kindergarten-only note naming |
| Student worksheet | own page with page break | LS1 L1/L2 + gr2 plants | required | worksheet starts on new page |
| Parent answer key | own page with page break | LS1 L1/L2 + gr2 plants | required | include detach-style heading and sample acceptable answers |
| Print rules | print-color-adjust + avoid split boxes | LS1 L1/L2 + gr2 plants | required | preserve printable family use |
| Feedback layer | `feedback-layer.js` with matching document ID | LS1 L1/L2 + gr2 plants | required | do not omit in modern shell |
| Preview/paywall | `llcPaywall`, access key, review bypass | LS1 L1/L2 + gr2 plants | required | keep store CTA pattern consistent |
| Route consistency | route field tracked even if page is flat `.html` now | Grade 3 audit + current repo state | required | document intended route in planning artifacts |
| Refcards | compact support artifact, terminology consistent | existing Grade 3 refcard pattern | required when unit pattern calls for it | keep visually simpler than lessons |
| Unit quiz | unit-level supporting artifact after lessons stabilize | Grade 3 audit expectations | required when unit pattern calls for it | should follow established LLC quiz behavior for that content type |

---

## Approved component and styling baseline

### Core reusable classes/patterns to preserve
Use the modern LLC class system already visible in the baseline lessons where applicable:
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

### Color system to preserve
For Grade 3 Life Science and Grade 3 modernization work, preserve the existing LLC functional color system:
- Life Science primary green headings/steps: `#2e7d32`
- green accent/borders: `#00B894`
- pale green section backgrounds: `#e8f5e9`, `#f1f8e9`
- standards box lavender/purple: `#f3e5f5` + `#ce93d8`
- vocabulary cyan: `#e0f7fa`
- materials gold/orange: `#fff8e1` + `#ffcc80`
- extensions indigo/light purple: `#e8eaf6` + `#9fa8da`
- notes gray dashed: `#f5f5f5` + dashed gray border

### Important styling rule
Preserve the **functional box color system** even when the lesson topic changes.

That means:
- do not create a brand-new color logic for Grade 3 Physical Science
- keep the LLC role-based boxes recognizable across lessons
- subject identity can shift in heading/accent tone, but the lesson should still feel like the same product family

---

## Metadata, standards, and terminology rules

### Metadata order
Use:
1. Grade
2. Duration
3. Subject
4. optional `🎒 Kit Lesson` only if justified

### Standards box rules
- label must be `NGSS Standard:` singular
- use the full code and full performance expectation text
- use an em dash between standard code and text
- place standards box immediately after the hero block

### Materials rules
- use specific quantities
- prefer bullet lists
- if helpful, use subheads such as:
  - `From Your Science Kit`
  - `Household Items to Gather`
  - `Optional / Nice to Have`
  - `Printables`
- do not use vague one-word materials lists

### Grade 3 wording rules
- family-facing, warm, practical, scientifically accurate
- Grade 3 readable, not kindergarten phrasing
- avoid middle-school jargon overload

---

## Worksheet and Parent Answer Key baseline

### Student Worksheet requirements
Every full Grade 3 lesson page should include a dedicated worksheet page when the pattern calls for one.

Minimum worksheet expectations:
- starts on a new page with `.page-break`
- has a clear `Student Worksheet` title
- includes a `Name` / `Date` line
- uses structured sections with room to write/draw
- uses concise student-facing prompts
- matches the science task of the lesson

### Parent Answer Key requirements
Every full Grade 3 lesson page should include a dedicated answer-key page when the pattern calls for one.

Minimum answer-key expectations:
- starts on a new page with `.page-break`
- uses `Parent Answer Key` exactly
- includes sample acceptable answers, not just one rigid answer
- includes parent-facing tone
- includes `What Success Looks Like`
- includes troubleshooting/misconception notes where relevant

### Explicit naming rule
Always say:
- `Student Worksheet`
- `Parent Answer Key`

Never substitute:
- `Data Sheet`
- `Observation Sheet`
- `Teacher Guide`
- `Answer Key for Parents`

---

## Print baseline

The baseline lessons preserve strong print behavior. Future Grade 3 lessons should keep that intact.

### Required print behavior
- worksheet starts on a new page
- answer key starts on a new page
- preserve colors in print using:
  - `-webkit-print-color-adjust: exact;`
  - `print-color-adjust: exact;`
- avoid splitting major boxes across pages using:
  - `break-inside: avoid;`
  - `page-break-inside: avoid;`
- keep the 8.5 inch printable layout and print-friendly serif body style

### Print quality rule
If a new Grade 3 lesson looks fine in browser but would print poorly, it does **not** meet the baseline.

---

## Preview / paywall / review baseline

This is mandatory for modern Grade 3 lessons.

### Required implementation pattern
Future modernized Grade 3 lesson pages should preserve:
- `body[data-document-id="..."]`
- feedback-layer script with matching `data-document-id`
- paywall overlay with `id="llcPaywall"`
- localStorage access pattern using `llc_access`
- `?review=1` bypass behavior
- `/store.html` CTA pattern already used by current LLC lessons
- copyright/footer parity

### Preview/paywall acceptance rules
A lesson is not baseline-compliant if it is missing any of these without a documented exception:
- review mode bypass
- feedback-layer script
- paywall overlay logic
- pending or final document ID on body and script

### Review-mode caution
Do not claim browser-level verification happened unless an actual verification pass happened. In planning/build docs, record the pattern requirement without pretending it was tested live.

---

## Route and navigation baseline

### Current repo reality
The current Grade 3 pages discovered in the repo are mostly flat `.html` files in `lesson-plans/`.

### Baseline rule for future work
Every Grade 3 lesson build batch should record:
- the current file path
- the intended route/public URL field
- whether route parity with stronger LLC directory patterns is still pending

### Route consistency checklist
For each lesson batch, track:
- file path created/updated
- intended public route
- whether it is currently linked from Grade 3 navigation
- whether it still needs navigation wiring later

### Important boundary
This chunk defines the route expectations; it does not require route migration or publish wiring yet.

---

## Grade 3 refcard and quiz baseline

### Refcards
Refcards should be treated as compact support artifacts, not mini-lessons.

Refcard rules:
- terminology must match the lesson
- keep visual structure consistent across the unit
- do not invent a different branding system for each refcard
- if one refcard pattern is chosen for the unit, the remaining refcards should follow it

### Unit quizzes
Unit quiz creation should wait until the lesson sequence is stable enough to reflect the actual built content.

Quiz rules:
- align coverage to completed lesson sequence
- use established LLC quiz conventions for that content type
- do not build the quiz from placeholder assumptions if lessons are still changing substantially

---

## Reusable build checklist for every Grade 3 lesson batch

Use this checklist for every lesson in every later chunk.

### A. Source-pattern check
- [ ] I am using Grade 3 LS1 Lesson 1 and/or Lesson 2 as the primary continuity anchor
- [ ] I am using `gr2-ls2-unit1-lesson1-what-do-plants-need.html` if I need the strongest nearby shell reference
- [ ] I am following `lesson-plans/style-guide.html` terminology exactly
- [ ] I am **not inventing a new format**

### B. Shell and section check
- [ ] `body[data-document-id]` exists
- [ ] title + subtitle + metadata bar are present
- [ ] hero + caption are present
- [ ] standards box is present after hero
- [ ] `The Big Idea` section is present
- [ ] `The Science` section is present
- [ ] vocabulary tip box is present
- [ ] `Materials` section is present
- [ ] `Let's Get Started` section is present using procedure-step blocks
- [ ] `Discussion Questions` section is present using question boxes and hints
- [ ] `Extensions` section is present
- [ ] `Parent/Teacher Notes` section is present
- [ ] `Student Worksheet` starts on a new page
- [ ] `Parent Answer Key` starts on a new page

### C. Terminology and metadata check
- [ ] section names match the style guide exactly
- [ ] standards label uses singular `NGSS Standard:`
- [ ] metadata order is Grade, Duration, Subject, optional kit badge
- [ ] no forbidden terminology like `Procedure`, `Data Sheet`, or `Teacher Guide`

### D. Print and family-use check
- [ ] print colors are preserved
- [ ] major boxes avoid splitting in print
- [ ] worksheet is actually usable by a family printing at home
- [ ] answer key includes sample answers and success criteria

### E. Preview/paywall/review check
- [ ] feedback-layer script exists with matching document ID
- [ ] paywall overlay exists
- [ ] `llc_access` pattern is preserved
- [ ] `?review=1` bypass logic is preserved
- [ ] footer/store CTA pattern remains consistent

### F. Route and tracking check
- [ ] current file path is recorded
- [ ] intended public route is recorded
- [ ] route/navigation wiring status is recorded
- [ ] if route parity is pending, that is explicitly noted

---

## Per-lesson acceptance checklist for build and review loops

Use this checklist during every build batch and after each revision pass.

| Check area | Accept if... | Status field |
|---|---|---|
| Source-pattern compliance | lesson clearly matches approved Grade 3 LLC shell | pending |
| Style-guide terminology | all required labels are exact | pending |
| Section order | lesson follows approved order | pending |
| Worksheet quality | dedicated printable worksheet is usable | pending |
| Parent answer key quality | sample answers + success criteria + parent-facing notes exist | pending |
| Preview/paywall parity | document ID, feedback layer, paywall, and review bypass exist | pending |
| Print readiness | page breaks and print behavior are intact | pending |
| Route tracking | intended route/public URL is documented | pending |
| Unit continuity | lesson feels like part of the same Grade 3 product family | pending |

### Review-loop tracking block
For each lesson/refcard/quiz item in a build batch, carry these fields:
- Rachel review: `pending / commented / revised`
- Margaret review: `pending / commented / revised`
- Revision round 1: `pending / done`
- Revision round 2: `pending / done`
- Revision round 3: `pending / done`
- Ready for human review: `yes / no`
- Notes / unresolved issues

### Review-loop rule
The required workflow is:
1. build
2. Rachel review
3. Margaret review
4. revise
5. repeat as needed
6. stop after **3 total revision rounds max**
7. if still unresolved, mark ready for human review = `no` and escalate to human review

### Important honesty rule
Do not mark Rachel review or Margaret review complete unless review artifacts/comments/notes actually exist.

---

## Batch-level usage rule

When working a coherent Grade 3 batch:
- apply this baseline to all lessons in the batch
- keep the same shell and terminology across the whole batch
- do not let one lesson drift into a custom pattern because it is a different topic
- if the batch includes refcards or quiz work, ensure those support artifacts remain visually and terminologically aligned with the lessons

---

## Recommendation for the next chunk

Use this file together with `lesson-plans/gr3-curriculum-audit-and-scope.md`.

Recommended next implementation step:
- modernize `3-PS2 Unit 1 Lessons 1–2` to match this baseline exactly before creating brand-new Grade 3 PS2 lessons.
