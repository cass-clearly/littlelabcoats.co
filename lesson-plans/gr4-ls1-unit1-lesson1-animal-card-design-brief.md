# Grade 4 LS1 Unit 1 Lesson 1 Embedded Animal Card Design Brief

Last updated: 2026-04-09
Status: design brief for embedding animal cards directly into the lesson page

## Purpose

This brief defines the in-lesson animal card solution for:
- `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`

It is the bridge between the dependency audit and the implementation pass.
The goal is to make the lesson self-contained, instructionally strong, print-ready, and stylistically aligned with Little Lab Coats.

## Design decision summary

Use an embedded card section inside the lesson page called:
- `Animal Cards for This Lesson`

The section should:
- appear after `Materials` and before `Let's Get Started`
- provide the full example set needed for the lesson activity
- be explicitly referenced by materials, procedure, worksheet, and answer-key wording
- be printable as part of the lesson packet without requiring a separate download or parent-supplied book/image set
- remain behind the existing lesson paywall in normal mode because it will appear after `Materials`

## Selected card content set

Use **6 animal cards**.

This is the best fit because it:
- gives enough variety for compare/sort/choose-two tasks
- covers the lesson’s named structure/function categories without overcrowding the page
- can fit in a clean 2-column by 3-row printable grid on letter-sized paper
- stays manageable for a 45–60 minute Grade 4 family lesson

### Required structure/function coverage

The set must collectively cover:
- body covering / staying warm or dry
- movement
- protection / defense
- getting food

### Selected animal set

1. **Duck**
- primary visible structure: waterproof feathers / webbed feet
- strongest job(s): staying dry and moving through water
- reason to include: already used in the lesson text, easy anchor example, supports body covering + movement

2. **Polar Bear**
- primary visible structure: thick fur / large paws
- strongest job(s): staying warm, walking on snow/ice, swimming support
- reason to include: strong body covering example and easy contrast with duck

3. **Turtle**
- primary visible structure: shell
- strongest job(s): protection
- reason to include: clear defense/protection example that is instantly readable for children

4. **Hawk**
- primary visible structure: hooked beak / sharp talons
- strongest job(s): catching and tearing food
- reason to include: strong getting-food example and a future bridge to Unit 1 argument writing

5. **Deer**
- primary visible structure: long legs / hooves
- strongest job(s): fast movement and safer travel on land
- reason to include: simple movement structure with a different habitat/body plan than duck

6. **Porcupine**
- primary visible structure: quills
- strongest job(s): protection / defense
- reason to include: makes it easy to compare two different protection structures with turtle

## Why these six are instructionally sufficient

This set supports all intended lesson moves:
- **picture walk / noticing:** every card has a clear visible structure to notice quickly
- **sorting by job:** cards can be sorted into movement, protection, getting food, or body covering / staying warm-dry
- **choose two animals:** six cards provide enough choice without overwhelming the worksheet
- **claim writing:** students can cite one visible structure and explain a survival function using concrete evidence

The set also avoids overloading the first lesson with more advanced or less visible examples that would require extra background explanation.

## Card content format

Each card should use a consistent LLC-friendly structure:
- animal name
- large visual/icon area
- one highlighted structure label
- one short survival-job tag
- 2 short evidence bullets

### Proposed card anatomy

Header:
- emoji or simple visual cue
- animal name
- mini tag such as `stays dry`, `moves fast`, `stays protected`, or `gets food`

Body:
- `Notice this structure:` one named external structure
- `How it helps:` one concise sentence connecting structure to survival
- `Look for evidence:` 1–2 concrete child-friendly observation bullets

### Example content pattern

**Duck**
- Notice this structure: waterproof feathers and webbed feet
- How it helps: These structures help a duck stay dry and move through water.
- Look for evidence:
  - feathers shed water instead of soaking it up
  - webbed feet push against the water like paddles

This content pattern is strong because it supports both observation and worksheet evidence language.

## Placement plan inside the lesson page

### Final placement

Insert the new section:
- after the existing `Materials` box
- before `Let's Get Started`

### Why this placement is correct

1. It matches the best in-repo precedent
- the Grade 3 climate lesson places included cards between `Materials` and the procedure

2. It preserves lesson flow
- families gather materials first
- then immediately see the included animal cards they will use
- then the procedure can refer back to them naturally

3. It preserves current preview/paywall behavior
- the page currently locks from `Materials`
- placing the card section after `Materials` keeps the embedded cards inside the paid lesson body in normal mode
- in `?review=1`, the full section remains visible for review and QA

## Section naming and intro copy plan

### Section title
- `Animal Cards for This Lesson`

### Intro copy pattern
Use wording like:
- `Use the included animal cards on this lesson page for the observation, sorting, and worksheet activities. Each card highlights one visible external structure and the job it helps the animal do.`

Optional supporting note:
- `You can point to the cards on screen or print this page and cut them apart for easier sorting.`

This wording is important because it fully replaces the old expectation that families bring their own picture cards or book images.

## Print-readiness plan

### Grid and density
- use a **2-column x 3-row grid** on desktop/print
- stack to **1 column** on narrow screens/mobile
- keep each card self-contained with `break-inside: avoid` and `page-break-inside: avoid`

### Pagination
- the card section should stay before the worksheet page break
- if space is tight, the entire card section may continue onto a second printed page, but a single card should never split across pages
- if needed, place a controlled page break before the worksheet rather than forcing the card section into cramped space

### Card sizing
- large enough to read when printed in color or grayscale
- compact enough that all 6 cards can fit across 1–2 lesson pages without crowding
- target content length: roughly 35–60 words per card, plus 2 short bullets

### Visual treatment
Use the existing Grade 4 Life Science palette:
- green heading family already used in the lesson
- soft green/cream card fills consistent with LLC print materials
- rounded card corners, bordered edges, subtle icon badges

### Labels and usability
- cards should be useful **without cutting** by simply pointing and comparing on the page
- cards should be **optionally cut apart** after printing even if they are not styled like kindergarten cut cards
- include enough spacing/gutters that cutting with scissors is practical if a family chooses to do that
- do **not** require cutting for the lesson to work

### Print CSS requirements
Future implementation should include:
- `break-inside: avoid` on the overall card section and each card
- print color adjustment preservation
- slightly reduced internal spacing/font size in print only if needed
- no fixed-height card body that risks clipping text in print

## On-page reference language to standardize later

Use this exact wording pattern everywhere possible:
- `the included animal cards on this lesson page`

### Materials wording target
Replace outside sourcing with language like:
- `the included animal cards on this lesson page`
- `printed lesson pages and Student Worksheet`
- `pencil or colored pencils`

Optional printables sublist if desired:
- `Student Worksheet page from this lesson`
- `Animal Cards for This Lesson section on this page`

### Procedure wording target
Future procedure references should explicitly point to the included cards, for example:
- `Start with a quick picture walk using the included animal cards on this lesson page.`
- `Sort the included animal cards by the job the structure does...`
- `Choose two animals from the included animal cards...`

### Worksheet wording target
The worksheet should reference the same source clearly, for example:
- `Use the included animal cards from this lesson page.`
- replace `Evidence from the picture or animal` with wording tied to the included cards, such as `Evidence from the included card`

### Answer-key wording target
The answer key should also name the source set, for example:
- `Students may use any of the included animal cards from this lesson page as evidence if they correctly connect structure to function.`

### Refcard wording target
The paired refcard should mirror the same design assumptions:
- materials snapshot should name `the included animal cards on this lesson page`
- observation guidance should mention the included cards rather than outside pictures/books
- family extension should prefer the included cards first, with outside observation as an optional extension rather than a requirement

## Card-to-activity mapping

### Step 1: quick picture walk
Use all 6 cards.
Goal:
- notice visible structures before naming their jobs

### Step 2: model structure-function thinking
Use Duck as the teacher model.
Reason:
- the lesson already contains a duck example, so this keeps continuity

### Step 3: sort by job
Suggested sort buckets:
- movement
- protection
- getting food
- staying warm or dry

Cards can support multiple buckets, but each should have one primary tag for clarity.

### Step 4: choose two animals
Any two of the 6 cards work.
This supports differentiation:
- simpler pair: turtle + deer
- more advanced pair: duck + hawk or polar bear + porcupine

### Worksheet evidence use
The worksheet should push students to cite something visible from the card:
- shell
- quills
- feathers
- beak
- talons
- paws
- long legs
- hooves
- webbed feet

## Tone and quality bar

The card copy should feel:
- science-accurate at Grade 4 level
- family-friendly and easy to scan
- stronger than generic animal flashcards
- consistent with LLC’s warm, visual, parent-usable style

Avoid:
- overly technical zoology language
- long paragraphs inside cards
- vague phrases like `it helps the animal survive` without naming how

## Non-goals for this lesson

Do not turn this into:
- a separate downloadable PDF requirement
- a full animal adaptation unit overview
- a cut-and-paste craft that requires extra prep to function
- a hidden dependency on outside books, web searches, or parent-made cards

## Implementation-ready decisions

The next implementation chunk should proceed with these locked decisions:
- number of cards: **6**
- animals: **duck, polar bear, turtle, hawk, deer, porcupine**
- placement: **after Materials, before Let’s Get Started**
- section title: **Animal Cards for This Lesson**
- wording standard: **the included animal cards on this lesson page**
- primary print layout: **2-column x 3-row grid**
- usage mode: **works on-screen, printable as-is, optional cut-apart support**
- instructional role: **observation + sorting + worksheet evidence source**

## Definition of success for implementation

The design will be correctly implemented when:
- the lesson page itself contains a polished embedded animal-card section
- a family can complete the lesson without searching for outside pictures or making their own cards
- materials, procedure, worksheet, and answer key all clearly point to the included card section
- the page still looks like a normal LLC lesson and prints cleanly
