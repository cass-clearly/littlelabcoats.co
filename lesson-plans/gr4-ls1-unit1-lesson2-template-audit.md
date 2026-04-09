# Grade 4 Life Science Unit 1 Lesson 2 — Template Audit

Last updated: 2026-04-09
Target file: `lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html`
Purpose: lock the exact Little Lab Coats structure, style/substance requirements, and open Remarq-driven revision targets before editing the lesson content.

## Scope of this audit

This audit is for the lesson page only:
- `lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html`

Coupled follow-up to watch after lesson edits:
- `lesson-plans/gr4-ls1-unit1-refcard-lesson2-sensing-the-world.html`

Why the refcard is coupled:
- it repeats the current materials wording
- it repeats the current science summary
- it repeats the current family extension wording
- if the lesson is tightened and clarified, the refcard will likely need parity edits in a later chunk

## Source files inspected

Primary source under revision:
- `lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html`

Remarq/open-comment reference:
- `lesson-plans/gr4-ls1-unit1-lesson2-remarq-baseline.md`

Style/substance handbook reference:
- `lesson-plans/style-guide.html`

Established Grade 4 Life Science reference lessons used for pattern matching:
- `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`
- `lesson-plans/gr4-ls1-unit1-lesson3-mouths-beaks-teeth-and-getting-food.html`
- `lesson-plans/gr4-ls1-unit2-lesson2-leaves-and-making-food.html`

Document ID / Remarq wiring reference:
- `lesson-plans/gr4-document-id-manifest.md`

## Current lesson audit — what exists now

### Current section order in the file
The current lesson already follows the broad LLC shell in this order:
1. `body[data-document-id="doc_tHdONv_mztI"]`
2. print button
3. `h1` lesson title
4. subtitle
5. metadata bar
6. hero image / caption
7. NGSS standards box
8. `The Big Idea`
9. `The Science`
10. vocabulary tip box
11. `Materials`
12. `Let's Get Started`
13. `Discussion Questions`
14. `Extensions`
15. `Parent/Teacher Notes`
16. Student Worksheet page break and worksheet section
17. Parent Answer Key page break and answer key
18. feedback-layer script
19. paywall overlay + preview lock script
20. footer

### Current strengths already present
- canonical URL is present
- correct public route naming is already in place
- `data-document-id="doc_tHdONv_mztI"` is present on `<body>`
- feedback-layer script is present and uses the same document ID
- review/paywall pattern matches other Grade 4 lessons
- page breaks exist for worksheet and answer key
- section naming mostly matches LLC terminology
- green Life Science color family is already in use

### Current structural/content mismatches vs the stronger LLC pattern
Compared with the stronger nearby Grade 4 lessons and the style guide, Lesson 2 still reads thinner and less deliberately structured.

Observed mismatches:
- the lesson uses only a single compact materials subsection (`Gather Before You Start`) instead of a more explicit, specific materials presentation
- the science paragraph is still too dense in one block and does not feel as child-friendly as the best neighboring lessons
- the lesson flow cues are not explicit enough about when students complete each worksheet section
- the main activity sequence is functional, but less polished and less concrete than the stronger neighboring lessons
- the discussion-question count is only 3; handbook guidance says 5–8 is the normal target
- the answer key has useful guidance, but it does not yet include the stronger detach instruction wording expected by the handbook
- the lesson is structurally valid, but still feels more like a minimal pass than a fully normalized LLC lesson

## Primary target structure for this lesson

Use Grade 4 Unit 1 Lesson 1 and Lesson 3 as the main structural shell, with Unit 2 Lesson 2 as a secondary rhythm check.

### Expected LLC section order to preserve
1. `body[data-document-id="..."]`
2. optional print button
3. `h1` title with moderate emoji use
4. subtitle
5. `.meta` bar in order: Grade, Duration, Subject
6. `.hero-image` with caption
7. `.standards-box`
8. `h2` `The Big Idea`
9. `h2` `The Science`
10. `.tip-box` for key vocabulary
11. `h2` `Materials`
12. `.materials-box`
13. `h2` `Let's Get Started`
14. multiple `.procedure-step` blocks
15. `h2` `Discussion Questions`
16. multiple `.question-box` blocks, each with `.discussion-hint`
17. `h2` `Extensions`
18. `.extension-box`
19. `h2` `Parent/Teacher Notes`
20. `.teacher-note`
21. `.page-break` + Student Worksheet page
22. `.page-break` + Parent Answer Key page
23. feedback-layer script tag
24. paywall overlay markup / scripts
25. footer / copyright block

### Normal Grade 4 lesson conventions to mirror from nearby lessons
- family-facing, printable tone
- moderate emoji use, not kindergarten-level density
- green Life Science headers and accents
- one clear Big Idea section, one clearer and shorter Science section, then vocabulary
- more explicit materials phrasing with concrete examples
- procedure steps that tell the parent exactly what to do and tell the student exactly what to record
- worksheet prompts that point back to specific steps
- answer key written as support for parents, not rigid grading

## Lesson-specific handbook checklist

The following are the style/substance rules from `lesson-plans/style-guide.html` that directly apply to this revision.

### Section naming and order
- use the exact section names:
  - `The Big Idea`
  - `The Science`
  - `Materials`
  - `Let's Get Started`
  - `Discussion Questions`
  - `Extensions`
  - `Parent/Teacher Notes`
  - `Student Worksheet`
  - `Parent Answer Key`
- keep the standard section order used across LLC lessons
- keep worksheet and answer key on separate new pages

### Metadata / standards
- metadata order must remain Grade, Duration, Subject
- do not add a `Setting:` field
- keep singular label `NGSS Standard:`
- keep `4-LS1-1` citation format with full standard text

### Materials requirements
- materials wording should be specific, not vague
- include concrete examples where a household item could be interpreted multiple ways
- if an asset is implied to be provided, the lesson should clearly state whether it is included on the page / in printables / or should be supplied by the parent

### Science/tone requirements
- science should be accurate without being condescending
- science should be kid-friendly, clear, and not textbook-dense
- `The Science` should introduce the why behind the activity and ease students into the practical work
- Grade 3–5 emoji use should stay moderate
- structure/function language must stay central for `4-LS1-1`

### Discussion question requirements
- every discussion question should include a suggested answer hint using `.discussion-hint`
- the standard pattern is 5–8 discussion questions
- hints should be open-ended but scientifically accurate

### Worksheet / answer key requirements
- use the exact phrase `Student Worksheet`
- use the exact phrase `Parent Answer Key`
- answer key should include detach wording in the standard style
- answer key should include supportive guidance, sample acceptable responses, and success criteria
- worksheet directions should be concise and clearly tied to lesson flow

### Print / layout / review requirements
- print colors must be preserved
- worksheet and answer key must start on new pages
- major instructional boxes should avoid splitting in print
- Remarq script must remain present at the bottom with the correct document ID
- feedback-layer script document ID must match the body document ID
- paywall + `?review=1` bypass behavior must remain intact

## Open Remarq comments that still need implementation

Source: `lesson-plans/gr4-ls1-unit1-lesson2-remarq-baseline.md`

### Already-addressed comment still visible in Remarq
- `cmt_cmqjrg03Pgs` — Rachel
  - Status in baseline: already reflected in current worksheet/answer-key wording
  - Action for next chunk: preserve the tighter compare-prompt expectation; do not regress it

### Open Serena comments to actively implement

#### 1) Provide or clarify lesson-support assets
- `cmt_IUsYk9D75g4`
- Quote: `animal photos or simple observation cards`
- Comment: `supply these with the lessons`
- Required revision implication:
  - either explicitly provide/include the observation assets in the lesson package
  - or rewrite the materials and activity wording so the lesson does not falsely imply included materials that are missing

#### 2) Make the tube example concrete
- `cmt_5wTOgmamF8Q`
- Quote: `paper tub`
- Comment: `give examples are we talking straw or toilet roll tube`
- Required revision implication:
  - replace vague tube wording with a concrete example such as toilet paper roll or paper towel tube
  - make the same clarification wherever that prop appears in the lesson/refcard

#### 3) Rewrite Step 4 for clarity
- `cmt_LaTi5_pzAzg`
- Quote: `Have students record one structure, one type of information it detects, and one survival behavior it supports.`
- Comment: `This is unclear what the step is asking 4. Make it more explicit`
- Required revision implication:
  - rewrite Step 4 so the action is unmistakable
  - explicitly name the worksheet section to complete
  - explicitly say what the student should write after the smell activity

#### 4) Move smell into the main lesson
- `cmt_ICYW7DoUQsw`
- Quote: `sight`
- Comment: `change this to smell. It's more fun. And encorporate it into the main lesson. It's more dynamic and interesting. Integrate into step 4`
- Required revision implication:
  - keep smell in the core procedure, not only in Extensions
  - make Step 4 the main smell-based activity moment
  - ensure the extension is no longer carrying the main fun sensory move by itself

#### 5) Make worksheet timing clearer for Sensory Detective
- `cmt_155TFGieedk`
- Quote: `Sensory Detective`
- Comment: `is this step 2? Can we make this clearer?`
- Required revision implication:
  - add explicit timing language to the worksheet section and/or procedure step
  - tell families when students should begin the table

#### 6) Make worksheet timing clearer for Claim Box
- `cmt_n2qIxYe2lyo`
- Quote: `because`
- Comment: `Which step is this? Make it clear when this is to be completed by the student`
- Required revision implication:
  - explicitly tie Claim Box completion to the relevant lesson step
  - mirror this cue in both procedure wording and worksheet wording

## Comparison findings from established Grade 4 lessons

### Reference lesson: Unit 1 Lesson 1
`lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`

What to copy from it:
- stronger materials specificity
- more concrete procedure wording
- clearer worksheet prompts that point back to exact steps
- stronger parent note about what the lesson is really trying to teach
- more fully realized “lesson package” feeling

What not to over-copy:
- the included animal-card block is lesson-specific enrichment, not a universal requirement for every lesson

### Reference lesson: Unit 1 Lesson 3
`lesson-plans/gr4-ls1-unit1-lesson3-mouths-beaks-teeth-and-getting-food.html`

What to copy from it:
- concise, focused science section rhythm
- cleaner structure-function wording
- worksheet prompts that ask for visible evidence plus function
- answer-key tone that supports good science reasoning

### Reference lesson: Unit 2 Lesson 2
`lesson-plans/gr4-ls1-unit2-lesson2-leaves-and-making-food.html`

What to copy from it:
- same shell and print/review behavior
- one-paragraph science section that is short and digestible
- direct connection between lesson steps and worksheet usage

Caution:
- Unit 2 Lesson 2 is useful as a shell/rhythm check, but it is itself somewhat minimal; Unit 1 Lessons 1 and 3 are the stronger pattern anchors

## Before/after revision checklist for the next implementation chunk

### Structure normalization
- keep the existing shell order intact
- preserve title / subtitle / meta / hero / standards / paywall / review wiring
- make the lesson feel like a normal Grade 4 LLC lesson rather than a lighter one-off
- consider adding one or two more discussion questions to align better with handbook expectations if space permits
- strengthen answer-key detach wording toward handbook standard

### Science section tightening
- substantially shorten and simplify `The Science`
- keep only the essential ideas needed for Grade 4:
  - sensory structures collect information
  - different structures detect different kinds of information
  - that information supports behavior and survival
- remove any wording that feels textbook-dense or over-explanatory
- keep NGSS structure-function alignment explicit

### Materials clarity
- resolve the ambiguity around `animal photos or simple observation cards`
- explicitly say whether assets are included or parent-supplied
- replace vague `paper tube` wording with a concrete example

### Procedure clarity
- rewrite Step 4 around the smell activity as the main engaging move
- make Step 2 / Step 4 worksheet timing clearer
- tell the parent what the student records in `Sensory Detective`
- tell the parent when the student completes the `Claim Box`

### Worksheet clarity
- add step-linked directions to `Sensory Detective`
- add step-linked directions to `Claim Box`
- preserve Rachel’s tighter expectation that students connect:
  - structure
  - information detected
  - behavior supported

### Parent-facing polish
- keep the teacher note focused on Grade 4-level limits
- keep the extension as a true optional follow-on, not the place where the best activity lives
- ensure the lesson reads as fun and child-friendly, not dry

### Remarq / live-review preservation
- preserve `data-document-id="doc_tHdONv_mztI"`
- preserve matching feedback-layer script document ID
- preserve `?review=1` unlock behavior
- verify after later implementation/push that live review mode still exposes Remarq editing

### Coupled parity follow-up after lesson revision
Later chunk should check:
- `lesson-plans/gr4-ls1-unit1-refcard-lesson2-sensing-the-world.html`

Parity items to inspect later:
- materials wording
- science-summary wording
- smell/touch follow-up wording
- overall consistency with the revised lesson

## Definition of done for this audit chunk

This chunk is complete when:
- the expected section order and formatting conventions are explicitly documented
- the applicable handbook rules are converted into a lesson-specific checklist
- all open Serena/Remarq comments are accounted for with concrete implementation implications
- the next implementation chunk can revise the lesson without re-discovering the target pattern

## Recommended implementation starting point for the next chunk

When editing begins, start with these in order:
1. rewrite `The Science` first so the lesson tone is normalized early
2. fix materials wording and explicitly resolve the missing-assets ambiguity
3. rewrite Step 4 around the smell activity and add worksheet timing cues
4. update worksheet labels/prompts so `Sensory Detective` and `Claim Box` map clearly to lesson steps
5. then do a final parity pass on discussion count, answer-key wording, and refcard follow-up needs
