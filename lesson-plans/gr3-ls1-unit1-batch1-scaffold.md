# Grade 3 LS1 Unit 1 Batch 1 Scaffold

Last updated: 2026-04-07
Status: implementation baseline for Grade 3 Life Science Unit 1 Lessons 3–6
Scope: Batch 1 recovery for the remaining lessons in `3-LS1 Unit 1`

2026-04-14 superseding note:
- The historical Lesson 2 anchor named in this scaffold is no longer a live sequencing anchor.
- Use the Calvin audit (`lesson-plans/gr3-ls1-unit1-calvin-audit-and-overhaul-plan-2026-04-14.md`) when making future continuity decisions for this unit.

## Purpose

This file is the chunk-level implementation brief for the Grade 3 Life Science Batch 1 recovery pass.
It converts the repo audit, style guide, and current Grade 3 lesson anchors into a direct build scaffold for Lessons 3–6.

Use this file together with:
- `lesson-plans/gr3-curriculum-audit-and-scope.md`
- `lesson-plans/gr3-implementation-baseline.md`
- `lesson-plans/gr3-ls1-unit1-lesson1-template-audit.md`
- `lesson-plans/gr3-ls1-unit1-lesson2-template-audit.md`

If there is any ambiguity, the precedence for this batch is:
1. explicit user scope for Grade 3 LS1 Lessons 3–6
2. `gr3-curriculum-audit-and-scope.md`
3. Grade 3 LS1 Lessons 1 and 2 as direct continuity anchors
4. `style-guide.html`
5. the strongest adjacent shell in `gr2-ls2-unit1-lesson1-what-do-plants-need.html`

---

## Batch scope locked for this pass

This batch is the remainder of the current Grade 3 Life Science unit.
Create or complete:
- `lesson-plans/gr3-ls1-unit1-lesson3-plant-life-cycles-and-seeds.html`
- `lesson-plans/gr3-ls1-unit1-lesson4-animal-life-cycles-and-metamorphosis.html`
- `lesson-plans/gr3-ls1-unit1-lesson5-comparing-life-cycle-patterns.html`
- `lesson-plans/gr3-ls1-unit1-lesson6-model-and-explain-a-life-cycle.html`

Matching support artifacts expected in the same batch workflow:
- `lesson-plans/gr3-ls1-unit1-refcard-lesson3-plant-life-cycles-and-seeds.html`
- `lesson-plans/gr3-ls1-unit1-refcard-lesson4-animal-life-cycles-and-metamorphosis.html`
- `lesson-plans/gr3-ls1-unit1-refcard-lesson5-comparing-life-cycle-patterns.html`
- `lesson-plans/gr3-ls1-unit1-refcard-lesson6-model-and-explain-a-life-cycle.html`
- `lesson-plans/gr3-ls1-unit1-quiz.html`

Batch review + handoff artifacts expected in this pass:
- `lesson-plans/gr3-life-science-batch-review.md`
- `lesson-plans/gr3-shareable-manifest.md`

Do not push or publish in this pass.

---

## Direct continuity anchors to mirror

### Immediate anchors
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`

These establish the exact Grade 3 LS1 continuity for:
- title/subtitle rhythm
- Life Science green palette
- family-facing Grade 3 tone
- section order
- worksheet and answer-key split
- review/paywall behavior
- deeper preview boundary

### Structural shell backup
- `lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html`

Use this only when Lessons 1–2 do not make a shell detail obvious enough.
Do not invent a new LS1 shell for Lessons 3–6.

---

## Required lesson shell for Lessons 3–6

Every new LS1 lesson in this batch should follow this order:

1. `body[data-document-id="..."]`
2. optional print button
3. `h1` title
4. italic subtitle
5. `.meta` bar
6. `.hero-image` with moderate Grade 3 emoji use and caption
7. `.standards-box`
8. `The Big Idea`
9. `The Science`
10. `.tip-box` key vocabulary
11. `Materials`
12. `.materials-box`
13. `Let's Get Started`
14. multiple `.procedure-step` blocks
15. `Discussion Questions`
16. multiple `.question-box` blocks with `.discussion-hint`
17. `Extensions`
18. `.extension-box`
19. `Parent/Teacher Notes`
20. `.teacher-note`
21. `.page-break` + `Student Worksheet`
22. `.page-break` + `Parent Answer Key`
23. feedback-layer script tag
24. paywall overlay + access script
25. footer / copyright block

### Exact section names
Use these names exactly:
- `The Big Idea`
- `The Science`
- `Materials`
- `Let's Get Started`
- `Discussion Questions`
- `Extensions`
- `Parent/Teacher Notes`
- `Student Worksheet`
- `Parent Answer Key`
- `NGSS Standard:`

Forbidden substitutions for this batch include:
- `Procedure`
- `Overview`
- `Reflection Questions`
- `Handout`
- `Teacher Guide`
- `Learning Goal` as the gating section name for preview

---

## Required styling and reusable component conventions

### Reuse these classes and visual patterns
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
Keep the Grade 3 Life Science green family used by LS1 Lessons 1 and 2:
- main green heading system: `#2e7d32`
- Life Science accent green: `#00B894`
- light green lesson backgrounds: `#e8f5e9`, `#f1f8e9`, `#f9fff9`

Keep functional LLC box colors consistent:
- standards box: purple/lavender
- vocabulary tip box: cyan
- materials box: gold/orange
- discussion/procedure boxes: Life Science greens
- extensions box: indigo/light purple
- parent notes + answer key: gray dashed

### Tone rules to preserve
- family-facing, warm, and practical
- scientifically accurate without sounding textbook-heavy
- Grade 3 appropriate sentence complexity
- feels like a sequel to Lessons 1 and 2, not a reset into a new format
- assumes kids can compare patterns, use models, and explain evidence

---

## Worksheet, refcard, and answer-key conventions

### Worksheet rules for every lesson page
Every lesson page in this batch should include:
- a dedicated worksheet page on a new printed page
- a centered `Name / Date` line
- student-facing prompts with room to write or draw
- tasks that match the lesson’s science work instead of generic filler
- print-safe layout that does not break core boxes awkwardly

### Parent Answer Key rules for every lesson page
Every lesson page in this batch should include:
- `✂️ PARENT ANSWER KEY — Detach before giving worksheet to students`
- sample acceptable answers, not one rigid answer only
- `What Success Looks Like`
- parent-facing notes or troubleshooting guidance where misconceptions are likely
- clear support for evidence/model language when students compare life cycles

### Refcard conventions for the batch
Refcards for Lessons 3–6 should follow the Grade 3 PS2 naming rhythm and remain visually consistent across the full LS1 set.
For this chunk, the key locked convention is:
- one per-lesson refcard file
- same lesson numbering as the lesson page
- no drift into a different support-asset format mid-unit

### Quiz convention for the batch
The LS1 unit quiz path is locked to:
- `lesson-plans/gr3-ls1-unit1-quiz.html`

The quiz should be treated as the shared unit companion for Lessons 1–6, but it is not built in this chunk.

---

## Preview / paywall / review behavior to mirror exactly

### Required implementation pieces on Lessons 3–6
Each new lesson page should preserve:
- `body[data-document-id="..."]`
- feedback-layer script tag with matching document ID
- `llcPaywall`
- `ACCESS_KEY = 'llc_access'`
- localStorage unlock pattern
- `?review=1` bypass logic
- `/store.html` CTA pattern

### Deeper preview rule locked for this batch
The current Grade 3 LS1 anchors lock from the first `h2` matching:
- `materials`
- `gather before you start`
- `what you need`

This is the preview behavior to preserve for Lessons 3–6.

### Interpretation rule for this batch
The preview should still let families reach the conceptual top matter before the paywall appears.
That means the visible preview should include:
- title
- subtitle
- metadata bar
- hero/caption
- standards box
- `The Big Idea`
- `The Science`
- vocabulary

Then lock from `Materials` onward.
Do not regress to an older shallow lock that hides most of the concept setup.

### Pending document IDs
Until real Remarq IDs are assigned, use pending-style placeholders consistent with the existing LS1 naming pattern, for example:
- `doc_pending_gr3_ls1_u1_l3`
- `doc_pending_gr3_ls1_u1_l4`
- `doc_pending_gr3_ls1_u1_l5`
- `doc_pending_gr3_ls1_u1_l6`

---

## Batch lesson-by-lesson scaffold

### Lesson 3
- File: `lesson-plans/gr3-ls1-unit1-lesson3-plant-life-cycles-and-seeds.html`
- Refcard: `lesson-plans/gr3-ls1-unit1-refcard-lesson3-plant-life-cycles-and-seeds.html`
- Continuity role: move from general life-cycle pattern into plant-specific life-cycle stages and seed-based beginnings
- Must still feel directly downstream of Lesson 2’s compare-the-pattern work

### Lesson 4
- File: `lesson-plans/gr3-ls1-unit1-lesson4-animal-life-cycles-and-metamorphosis.html`
- Refcard: `lesson-plans/gr3-ls1-unit1-refcard-lesson4-animal-life-cycles-and-metamorphosis.html`
- Continuity role: deepen the animal side with explicit metamorphosis and stage-change language
- Keep the same four-part big pattern visible while showing that some animals change dramatically in form

### Lesson 5
- File: `lesson-plans/gr3-ls1-unit1-lesson5-comparing-life-cycle-patterns.html`
- Refcard: `lesson-plans/gr3-ls1-unit1-refcard-lesson5-comparing-life-cycle-patterns.html`
- Continuity role: comparison-heavy application lesson across plants and animals
- Should build evidence/model language in preparation for the culminating Lesson 6 task

### Lesson 6
- File: `lesson-plans/gr3-ls1-unit1-lesson6-model-and-explain-a-life-cycle.html`
- Refcard: `lesson-plans/gr3-ls1-unit1-refcard-lesson6-model-and-explain-a-life-cycle.html`
- Continuity role: culmination lesson where students model and explain a life cycle using the unit’s shared pattern language
- Should feel like the capstone of the six-lesson LS1 sequence, not an isolated project page

### Shared unit support path
- Quiz: `lesson-plans/gr3-ls1-unit1-quiz.html`

---

## Batch-level review artifact format for this pass

Use `lesson-plans/gr3-life-science-batch-review.md` as the single batch review tracker for Lessons 3–6.
For this batch, it should track:
- scope confirmation for Lessons 3–6
- exact lesson + refcard + quiz paths in scope
- Rachel review section with concrete comments
- Margaret review section with concrete comments
- revision round log
- open issues / escalation notes
- honesty check stating what is not yet built, reviewed, or published

### Required review-round structure
- Round 1: Rachel comments
- Round 1: Margaret comments
- Revise lesson/support files from that feedback
- Repeat only if needed
- Cap total rounds at 3
- Do not claim review completion without real comments

---

## URL manifest convention for this batch

When this batch reaches publish-ready status later, `lesson-plans/gr3-shareable-manifest.md` should gain a dedicated LS1 Batch 1 section that lists:
- lesson title
- exact public URL
- whether the file is repo-ready only or live

Expected URL pattern:
- `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson3-plant-life-cycles-and-seeds.html`
- `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson4-animal-life-cycles-and-metamorphosis.html`
- `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson5-comparing-life-cycle-patterns.html`
- `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson6-model-and-explain-a-life-cycle.html`
- `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-quiz.html`

Manifest honesty rule:
- do not mark these URLs as live in this chunk
- this chunk only locks the future URL pattern and handoff format

---

## Done state for this scaffold chunk

This chunk is correctly established when:
- Lessons 1 and 2 are explicitly captured as the continuity anchors for Lessons 3–6
- the exact LLC section order and terminology are documented for the batch
- deeper preview behavior is locked to the `Materials` boundary for new LS1 lessons
- all lesson/refcard/quiz/review/manifest paths needed for the batch are identified
- the batch review artifact no longer claims there are no remaining Grade 3 LS1 lessons in scope

## Not done in this chunk

This chunk does not:
- draft the new lesson HTML files
- draft the refcards
- build the quiz
- run Rachel or Margaret review
- revise from actual comments
- push or publish anything
