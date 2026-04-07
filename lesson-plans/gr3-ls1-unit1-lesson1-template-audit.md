# Grade 3 Life Science Unit 1 Lesson 1 — Template Audit

Target file: `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`

Purpose: identify the exact established Little Lab Coats lesson pattern this page should follow before rebuilding it.

## Primary template selection

### Primary structural model
- `lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html`

Why this is the best base:
- Same subject family: Life Science
- Strongest alignment to the style guide among the nearby lesson files reviewed
- Includes the full modern LLC lesson shell: metadata, hero, NGSS box, Big Idea, The Science, vocabulary, materials, lesson steps, discussion questions, extensions, parent/teacher notes, Student Worksheet, Parent/Teacher Answer Key, Remarq script, paywall overlay, and `review=1` bypass logic
- Already uses Life Science green styling and parent-facing polish expected for the target lesson

### Secondary references
- `lesson-plans/k-ls1-unit2-lesson6-plant-life-cycle.html`
  - Best topic-specific reference for life-cycle framing, sequencing language, and worksheet/diagram ideas
  - Useful for life-cycle-specific explanations, but not the grade-level depth target
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
  - Useful grade-band reference for 3rd grade reading level, pacing, and worksheet/answer-key density
  - Not a complete modern template because it lacks The Science, Extensions, Remarq, and paywall/review behavior

## Non-negotiable LLC requirements pulled from `lesson-plans/style-guide.html`

### Required lesson order
The style guide requires this exact sequence:
1. Title
2. Subtitle
3. Metadata bar
4. Hero image or emoji with caption
5. NGSS Standards box
6. The Big Idea
7. The Science
8. Key Vocabulary (tip box)
9. Materials
10. Let's Get Started
11. Discussion Questions
12. Extensions
13. Parent / Teacher Notes
14. Student Worksheet(s) on a new page
15. Parent Answer Key on a final page
16. Remarq script tag in the footer

### Terminology to use exactly
- `The Big Idea`
- `The Science`
- `Materials`
- `Let's Get Started`
- `Discussion Questions`
- `Extensions`
- `Parent / Teacher Notes` or `Parent/Teacher Notes`
- `Student Worksheet`
- `Parent Answer Key`
- `NGSS Standard:` label should be singular

### Metadata conventions
Per style guide:
- Required order: Grade, Duration, Subject, optional Kit designation
- Never include `Setting:`
- Grade should be written out as grade level formatting, not shorthand metadata inventions
- Duration should use en dash where a range appears

### Visual/brand conventions relevant to this lesson
- Life Science pages should use the green theme family
  - dark: `#00B894` / `#2e7d32` family in existing lessons
  - light/background: pale green boxes and accents
- Functional boxes should stay consistent across subjects:
  - NGSS box: purple/lavender
  - Materials: gold/orange
  - Discussion: green
  - Tip/vocabulary: cyan
  - Extensions: indigo/light purple
  - Parent notes: gray dashed
- Body text should be print-friendly and family-friendly, using the repo’s established lesson styling rather than standalone custom layout experiments

### Discussion question rule
- Each discussion question should include an italic suggested answer/hint directly underneath using `.discussion-hint`

### Print rules to preserve
- Student worksheet and answer key must each start on a new page with `.page-break`
- Use `break-inside: avoid` / `page-break-inside: avoid` on major blocks
- Preserve print colors with:
  - `-webkit-print-color-adjust: exact;`
  - `print-color-adjust: exact;`
- Avoid headings separating from their content in print

### Answer-key rules to preserve
The answer key should include:
- clear detach instruction
- expected/sample answers
- supportive parent-facing tone
- success criteria
- troubleshooting or practical notes where relevant

### Review/paywall behavior to preserve
From the strongest live lesson pattern:
- Include the feedback layer script tag
- Include paywall overlay markup/styles/scripts
- Support `?review=1` bypass so review mode shows the full lesson and comments
- Keep the copyright/footer block

## Structural map for the target lesson

This is the structure the Grade 3 life cycle lesson should adopt.

1. `body[data-document-id="..."]`
2. optional print button used by modern lesson pages
3. `h1` title with moderate emoji use suitable for Grade 3
4. subtitle line in italics
5. `.meta` bar with Grade, Duration, Subject, and only optional kit badge if truly needed
6. `.hero-image` with emoji hero or visual anchor plus caption
7. `.standards-box` with singular `NGSS Standard:` label and full `3-LS1-1` wording
8. `h2` `The Big Idea`
9. `h2` `The Science`
10. `.tip-box` for key vocabulary
11. `h2` `Materials`
12. `.materials-box` with LLC-style subheads if useful
13. `h2` `Let's Get Started`
14. multiple `.procedure-step` blocks with step headers and times
15. `h2` `Discussion Questions`
16. multiple `.question-box` blocks, each with `.discussion-hint`
17. `h2` `Extensions`
18. `.extension-box`
19. `h2` `Parent/Teacher Notes`
20. `.teacher-note`
21. `.page-break` + Student Worksheet page(s)
22. `.page-break` + Parent Answer Key page
23. feedback layer script
24. paywall overlay + script with `review=1` bypass
25. footer/copyright block

## Gap analysis: current target file vs LLC standard

### What the target already has that can be preserved conceptually
- Topic is correct: Grade 3 Life Science Unit 1 Lesson 1, life cycles
- Includes NGSS `3-LS1-1`
- Includes a Big Idea concept
- Includes key vocabulary, materials, steps, discussion questions, and a worksheet concept
- Core scientific direction is broadly right for the standard

### What is currently nonstandard or missing
- Uses an ad-hoc standalone page layout instead of the LLC lesson shell
- No LLC `.meta` bar
- No hero image/emoji wrapper with caption
- No `The Science` section
- Uses `Learning Objectives` grid instead of the standard section flow used by stronger LLC lessons
- Uses `Let’s Get Started` content, but not the standard `Let's Get Started` section naming/presentation with LLC procedure-step styling
- Discussion questions do not include suggested answer hints beneath each question
- Uses `Teacher Notes` instead of the stronger established `Parent/Teacher Notes` pattern
- Student worksheet is just a boxed section inside the lesson body, not a dedicated printable worksheet page
- No Parent Answer Key page
- No `.page-break` worksheet/answer-key print behavior
- No feedback-layer / Remarq script
- No paywall overlay
- No `review=1` bypass behavior
- No modern footer/copyright block
- Visual design does not follow the established LLC lesson palette and component system
- Body font/layout does not match the repo’s dominant print-friendly lesson format
- No obvious reusable wrapper classes from established LLC lessons
- Missing the family-facing polish present in the stronger templates

## Concrete rebuild checklist for the next chunk

### Use this exact template strategy
- Start from `gr2-ls2-unit1-lesson1-what-do-plants-need.html` as the base structural shell
- Borrow only topic-specific life-cycle ideas from `k-ls1-unit2-lesson6-plant-life-cycle.html`
- Keep Grade 3 reading level, not kindergarten phrasing

### Section/content checklist
- Replace the current custom top layout with the standard LLC title/subtitle/meta/hero/standards flow
- Keep the lesson focused on `3-LS1-1`: organisms have unique and diverse life cycles, but all share birth, growth, reproduction, and death
- Add `The Science` section before vocabulary
- Convert the lesson body into standard `Let's Get Started` procedure steps
- Keep discussion questions, but add suggested answer hints under every question
- Add an `Extensions` section in LLC format
- Rename/use `Parent/Teacher Notes`
- Move student-facing work onto a dedicated worksheet page
- Add a dedicated Parent Answer Key page with detach-style heading and sample responses

### Styling/component checklist
- Use Life Science green styling from the established lessons
- Keep NGSS box purple, materials gold, vocabulary cyan, discussion green, extensions indigo, notes gray dashed
- Use print-friendly body styles from the established lessons rather than the current custom card grid layout
- Ensure worksheet and answer key start on new pages
- Ensure major boxes avoid splitting in print

### Review/publish-behavior checklist
- Include `data-document-id` on `<body>`
- Include the feedback-layer script footer
- Include the standard LLC paywall overlay
- Include `review=1` bypass behavior exactly like the stronger live lesson pattern
- Preserve copyright footer

## Recommendation for implementation

For the rebuild, mirror `gr2-ls2-unit1-lesson1-what-do-plants-need.html` most closely for structure and behavior, while swapping in Grade 3 life-cycle content and selectively borrowing life-cycle-specific framing from `k-ls1-unit2-lesson6-plant-life-cycle.html`.

That gives the target lesson the strongest existing LLC format without inventing a new pattern.

## Implementation note — review-and-polish pass

### What changed
- Rebuilt `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` into the established LLC lesson shell used by nearby Life Science lessons.
- Added the full review-ready lesson structure: metadata, hero, NGSS box, Learning Objective, The Big Idea, The Science, vocabulary, Materials, Let's Get Started, Discussion Questions with hints, Extensions, Parent/Teacher Notes, Student Worksheet, Parent Answer Key, feedback layer, paywall/review logic, and footer.
- Polished wording for family-facing clarity and consistency with LLC terminology, including `Parent Answer Key`, preview/paywall copy, and clearer human life-cycle phrasing.
- Tightened worksheet/print presentation with dedicated page breaks for the Student Worksheet and Parent Answer Key.

### Final parity check notes
- Section rhythm, box styling, and print behavior now closely follow `gr2-ls2-unit1-lesson1-what-do-plants-need.html`.
- Preview/review/paywall behavior uses the same structural pattern as the modern LLC lesson template, including `feedback-layer.js`, `llcPaywall`, and `review=1` bypass handling.
- The file still uses a pending-style `data-document-id` (`doc_pending_gr3_ls1_u1_l1`), so Remarq wiring is not final yet, but the lesson file itself is review-ready for human content review.

### Follow-up review points
- When a real Remarq document ID is available, replace the pending document ID in both the `<body>` tag and feedback-layer script.
- Optional browser-level verification could confirm the exact preview cutoff and print layout visually, though the structure matches the existing repo pattern.
