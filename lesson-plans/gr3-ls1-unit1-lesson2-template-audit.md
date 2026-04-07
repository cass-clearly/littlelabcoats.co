# Grade 3 Life Science Unit 1 Lesson 2 — Template Audit

Target file: `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`

Purpose: lock the exact Little Lab Coats lesson shell, continuity decisions, and content blueprint before drafting Lesson 2.

## Primary template selection

### Immediate continuity anchor
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`

Why this is the continuity anchor:
- It is the newly standardized Grade 3 Lesson 1 that Lesson 2 must feel like it directly follows.
- It already uses the modern LLC lesson shell, print structure, worksheet/answer-key split, and paywall/review behavior expected for this unit.
- It establishes the Grade 3 Life Science tone: family-facing, printable, scientifically accurate, and centered on `3-LS1-1`.
- It already frames the core universal pattern students now need to apply: birth, growth, reproduction, and death.

### Primary structural model
- `lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html`

Why this is still the best shell to mirror:
- It is the strongest nearby Life Science lesson with the full modern LLC pattern intact.
- It preserves the exact reusable page architecture needed for Lesson 2: metadata, hero, standards box, Big Idea, The Science, vocabulary, Materials, procedure steps, discussion questions with hints, Extensions, Parent/Teacher Notes, Student Worksheet, Parent Answer Key, Remarq script, paywall overlay, and `review=1` bypass.
- Its worksheet and answer-key rhythm is especially strong for family use and can be adapted cleanly to a comparison lesson.

### Secondary topic references
- `lesson-plans/k-ls1-unit2-lesson6-plant-life-cycle.html`
  - Best topic-specific reference for life-cycle sequencing, stage naming, and student-facing life-cycle model ideas.
  - Use only for topic mechanics and worksheet inspiration, not for reading level or pacing.
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
  - Useful grade-band check for 3rd-grade pacing, answer-key density, and sentence complexity.
  - Not the structural template because it lacks the full modern review/paywall and section pattern.

## Non-negotiable LLC shell for Lesson 2

Lesson 2 should use this exact order.

1. `body[data-document-id="..."]`
2. Optional print button
3. `h1` title
4. Subtitle in italics
5. `.meta` bar
6. `.hero-image` with caption
7. `.standards-box`
8. `h2` `The Big Idea`
9. `h2` `The Science`
10. `.tip-box` for vocabulary
11. `h2` `Materials`
12. `.materials-box`
13. `h2` `Let's Get Started`
14. Multiple `.procedure-step` blocks
15. `h2` `Discussion Questions`
16. Multiple `.question-box` blocks with `.discussion-hint`
17. `h2` `Extensions`
18. `.extension-box`
19. `h2` `Parent/Teacher Notes`
20. `.teacher-note`
21. `.page-break` + Student Worksheet page
22. `.page-break` + Parent Answer Key page
23. feedback-layer script tag
24. paywall overlay markup/styles/scripts
25. footer / copyright block if present in the source shell used

## Terminology and metadata rules to preserve

### Required section names
Use the established LLC names exactly:
- `The Big Idea`
- `The Science`
- `Materials`
- `Let's Get Started`
- `Discussion Questions`
- `Extensions`
- `Parent/Teacher Notes`
- `Student Worksheet`
- `Parent Answer Key`

### Standards label
- Use singular `NGSS Standard:`
- Cite `3-LS1-1` in the same full-sentence format used by Lesson 1

### Metadata bar rules
- Keep order: Grade, Duration, Subject
- Do not add `Setting:`
- Match Grade 3 formatting used by Lesson 1
- Keep duration in established range style, e.g. `45–60 minutes` if the final lesson supports that timing

## Reusable LLC component classes and visual conventions

### Base lesson styling to reuse
Mirror the class system already used in Grade 3 Lesson 1 / the strongest Life Science shell:
- `.meta`
- `.hero-image`, `.emoji-hero`, `.caption`
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

### Color/box system to preserve
Lesson 2 should stay in the Life Science green family established by Lesson 1:
- main heading / section green: `#2e7d32`
- accent green / border emphasis: `#00B894`
- pale green backgrounds: `#e8f5e9`, `#f1f8e9`, `#f9fff9`

Keep cross-functional box colors consistent with LLC:
- NGSS box: purple/lavender (`.standards-box`)
- Vocabulary tip box: cyan (`.tip-box`)
- Materials box: warm gold/orange (`.materials-box`)
- Procedure steps: green-backed Life Science instructional boxes (`.procedure-step`)
- Discussion boxes: pale green with green left border (`.question-box`)
- Extensions: indigo/light purple (`.extension-box`)
- Parent notes: gray dashed (`.teacher-note`)
- Answer key: gray dashed with centered darker heading (`.answer-key`)

### Typography and tone
- Keep the print-friendly serif body styling already used in Lesson 1 and the plant-needs template.
- Keep headings, spacing, and box rhythm visually parallel to Grade 3 Lesson 1.
- Maintain family-facing voice: clear, warm, practical, scientifically sound, not textbook-dense.
- Use Grade 3 language that assumes students can compare patterns and explain evidence, without drifting into middle-school vocabulary overload.

## Print, worksheet, and answer-key rules

### Print behavior to preserve
- Student Worksheet must start on a new page with `.page-break`
- Parent Answer Key must start on its own new page with `.page-break`
- Preserve print colors with:
  - `-webkit-print-color-adjust: exact;`
  - `print-color-adjust: exact;`
- Keep major boxes from splitting in print using `break-inside: avoid` / `page-break-inside: avoid`
- Keep printable widths and spacing aligned to the existing 8.5in page layout

### Worksheet conventions to preserve
- Include a centered `Name / Date` line
- Use multiple worksheet sections with strong subheads and ample writing/drawing space
- Keep worksheet tasks student-facing and concise
- Favor comparison tables, sorting/order boxes, labeled drawing spaces, and short science-sentence completions over dense paragraph prompts

### Answer-key conventions to preserve
- Use detach instruction in the heading
- Include sample acceptable answers, not just one rigid answer
- Add `What Success Looks Like`
- Add practical parent-facing notes or troubleshooting if misconceptions are likely
- Accept student-friendly wording where scientifically appropriate

## Review, preview, and paywall behavior to preserve

Lesson 2 should copy the live behavior pattern already present in Grade 3 Lesson 1.

Required behaviors:
- `<body>` must include `data-document-id`
- Include the feedback-layer script tag with matching document ID
- Include the standard LLC paywall overlay markup and styles
- Keep the `llc_access` localStorage unlock pattern
- Preserve `?review=1` bypass so full lesson + comments show in review mode
- Lock the lesson from the first substantive content section after the preview threshold, using the same script structure already established in Lesson 1
- Preserve the same subscription CTA styling and store link pattern

### Exact preview/paywall pattern confirmed from the inspected lesson shell
- The feedback layer currently uses `data-content-selector="body"` and a matching `data-document-id` on both `<body>` and the script tag.
- The paywall overlay is injected near the end of the file with `id="llcPaywall"` and starts as `style="display:none;"`.
- The paywall script uses `ACCESS_KEY = 'llc_access'` and grants access when localStorage equals `granted`.
- Review mode is implemented with `window.location.search.indexOf('review=1') !== -1`, which sets localStorage access and skips locking.
- The lock script scans `h2` headings and hides content beginning at the first substantive section after the preview threshold; in the current Grade 3 Lesson 1 shell this effectively hides from the early lesson body onward and leaves only the preview-visible top matter.
- The paywall CTA points to `/store.html` and uses the existing LLC title/subtitle/button styling already present in Lesson 1 and the strongest nearby live lesson shell.

Implementation note:
- Until a real Remarq document ID exists, use a pending-style document ID placeholder consistent with Lesson 1 naming patterns

## Continuity brief — how Lesson 2 should feel like a sequel to Lesson 1

Lesson 1 introduced the idea that a life cycle is a pattern of stages and named the four universal parts: birth, growth, reproduction, and death. Lesson 2 should feel like the natural next move:
- Lesson 1 asked, `What is a life cycle?`
- Lesson 2 answers, `How can life cycles look different but still follow the same big pattern?`

### Sequel moves to carry forward
- Keep the same green Life Science visual system so the pages clearly belong to the same unit
- Reuse the same section rhythm and worksheet/answer-key structure so families recognize the flow immediately
- Open by briefly reminding students of the universal pattern from Lesson 1, then shift to comparison
- Keep the same core NGSS framing: organisms have unique and diverse life cycles, but all share common features
- Preserve a model-based mindset from Lesson 1 by having students compare and represent patterns, not just memorize stage names
- Use the same family-facing balance of kid language plus correct scientific vocabulary

### What should be new in Lesson 2
- More organisms in one lesson, not just a single example
- Stronger compare/contrast emphasis
- Explicit attention to diversity in life cycles:
  - metamorphosis vs gradual growth
  - eggs vs live birth
  - seed/seedling/plant pattern vs animal development
- Clear statement that the stages may look different or have different names, but the big pattern still holds

## Lesson 2 content blueprint

### Recommended title direction
- `Different Life Cycles, Same Big Pattern`

Reason:
- It sounds like a direct sequel to Lesson 1 rather than a brand-new topic
- It foregrounds compare/contrast and the unit’s core conceptual takeaway

### Subtitle direction
Use the same unit/lesson framing style as Grade 3 Lesson 1, for example:
- `Life Science — Life Cycles | Unit 1, Lesson 2 of 6`

### NGSS/content throughline
- Focus tightly on `3-LS1-1`
- Core claim: different organisms can have very different-looking life cycles, but they all share the same overall pattern of beginning life, growing, reproducing, and dying

### Organism set to compare
Use a small, familiar set that shows meaningful contrast without overwhelming the page:
- butterfly
- frog
- bean plant
- bird
- human

Why this set works:
- butterfly shows metamorphosis
- frog shows dramatic body-form change from tadpole to adult
- bean plant ensures plants are fully represented, not treated as secondary to animals
- bird provides egg-laying animal development without metamorphosis
- human provides live birth and gradual growth

### Big Idea direction
- Life cycles can look very different from one organism to another, but every organism follows the same big pattern of birth, growth, reproduction, and death.

### The Science direction
This section should explain:
- a life cycle is the sequence of stages in an organism’s life
- the stages have different names depending on the organism
- some organisms hatch from eggs, some begin as seeds, some are born live
- some change dramatically in form, while others grow more gradually
- the reason it is called a cycle is that adults reproduce and a new young organism begins the pattern again

### Vocabulary focus
Likely vocabulary list:
- life cycle
- stage
- organism
- offspring
- reproduce / reproduction
- metamorphosis
- seedling
- tadpole
- adult

### Materials direction
Keep materials simple and printable-friendly:
- printed lesson pages and worksheet
- pencils / crayons / colored pencils
- optional scissors or cards only if the worksheet design truly requires cut-and-sort interaction

### `Let's Get Started` lesson flow direction
Recommended flow:
1. Quick review of the universal pattern from Lesson 1
2. Compare two familiar life cycles aloud and notice obvious differences
3. Introduce a multi-organism comparison display or cards
4. Guide students to sort stages or match organisms to life-cycle descriptions
5. Close by naming the common pattern shared by all examples
6. Transition into worksheet tasks that ask students to order, compare, and explain

### Discussion Questions direction
Questions should probe:
- why a butterfly and a bean plant can both have life cycles even though they look so different
- how frogs and humans differ in early stages
- why the word `cycle` still fits all organisms
- what all organisms have in common across life cycles
- how models help us compare different organisms

Each question must include a `.discussion-hint` under it.

### Extensions direction
Good extension fits:
- choose one more organism and add it to the comparison
- create a mini poster showing the same big pattern across three organisms
- discuss where sharks, chickens, oak trees, or flowers would fit

### Parent/Teacher Notes direction
Include notes to support likely misconceptions:
- students may think plants do not have life cycles
- students may think `different stages` means only `different sizes`
- students may think `death` makes a cycle stop, so the note should reconnect them to reproduction and a new generation beginning
- encourage acceptance of equivalent stage labels if the pattern and science are correct

## Worksheet blueprint for the next chunk

Lesson 2 should keep lesson + worksheet + answer key all on one page file.

### Student Worksheet recommended structure
1. `Put One Life Cycle in Order`
   - 4-stage or 5-stage boxes for one chosen organism
2. `Compare Two Organisms`
   - table with columns for same / different
3. `Show the Big Pattern`
   - fill-in-the-blank science sentence using birth, growth, reproduction, death
4. `Explain Why It Is a Cycle`
   - short written response lines
5. Optional labeled drawing/model space if room allows

### Parent Answer Key recommended structure
- Sample sequence answers for butterfly, frog, bean plant, bird, and human
- Sample same/different comparison statements
- Accepted words for the big-pattern sentence
- Short model explanation for why it is called a cycle
- `What Success Looks Like`
- `Troubleshooting / Teaching Notes`

## Non-negotiable parity checklist before touching the final lesson HTML

### Continuity and structure
- Follow `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` for unit continuity, section rhythm, and family-facing tone.
- Follow `lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html` for the modern LLC shell, worksheet/answer-key split, and live preview/paywall behavior.
- Use `lesson-plans/k-ls1-unit2-lesson6-plant-life-cycle.html` only for life-cycle-specific modeling ideas, not for kindergarten pacing or phrasing.
- Do not invent a new section order, wrapper structure, or custom preview system.

### Visual parity
- Keep the Grade 3 Life Science green heading/border system used in Lesson 1.
- Keep LLC box colors functionally consistent: purple NGSS, cyan vocabulary, gold materials, green procedure/discussion, indigo extension, gray notes/answer key.
- Keep serif body typography, printable spacing, and 8.5in page width aligned with the existing lesson shell.
- Reuse established wrapper classes where possible instead of introducing redundant one-off variants.

### Content parity
- Make Lesson 2 explicitly feel like the sequel to Lesson 1 by opening from the universal pattern and then shifting to compare/contrast.
- Include the full five-organism comparison set: butterfly, frog, bean plant, bird, and human.
- Reinforce the shared pattern of birth, growth, reproduction, and death while highlighting stage-name and stage-shape differences.
- Keep all wording family-facing, Grade 3 appropriate, and scientifically sound.

### Worksheet and answer-key parity
- Include a dedicated Student Worksheet page and a separate Parent Answer Key page, each on a new printed page.
- Use concise student tasks: ordering, comparing, science-sentence completion, and brief explanation/modeling.
- Include detachable answer-key wording, sample acceptable answers, success criteria, and troubleshooting notes.

### Review and preview parity
- Keep `data-document-id`, feedback-layer script, paywall overlay, `llc_access` localStorage behavior, `?review=1` bypass, and the existing `/store.html` CTA pattern.
- Preserve the footer/copyright block.
- Do not publish or wire a final Remarq ID yet; a pending placeholder is acceptable for review-ready repo work.

## Final implementation recommendation

For Lesson 2, use `gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` as the immediate continuity anchor and mirror `gr2-ls2-unit1-lesson1-what-do-plants-need.html` for the structural shell and behavior. Borrow only topic-specific sequencing/model ideas from `k-ls1-unit2-lesson6-plant-life-cycle.html`.

That combination gives Lesson 2 the right unit continuity, the strongest modern LLC structure, and the right science focus without inventing a new format.
