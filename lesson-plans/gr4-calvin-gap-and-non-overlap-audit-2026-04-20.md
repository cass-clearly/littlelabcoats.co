# Grade 4 Calvin Gap + Non-Overlap Audit — 2026-04-20

Purpose: audit the actual Grade 4 repo state for duplication, false breadth, NGSS-shape gaps, and cleanup order so later work does not keep adding content in the wrong places.

## Repo baseline audited

### Grade 4 domains currently present in repo
- Life Science
  - `gr4-ls1-unit1-*`
  - `gr4-ls1-unit2-*`
- Physical Science
  - `gr4-ps3-unit1-*`
- Earth & Space Science
  - `gr4-ess1-unit1-*`
  - `gr4-ess2-unit1-*`
- Engineering
  - `gr4-ets1-unit1-*`
- Related non-canonical / freebie / legacy files
  - `free-gr4-apple-oxidation.html`
  - `free-gr4-apple-oxidation-refcard.html`
  - `free-gr4-apple-oxidation-quiz.html`
  - `gr4-ls1-unit1-l1-food-webs.html`

### Review/packaging evidence checked
- `lesson-plans/gr4-life-science-batch-review.md`
- `lesson-plans/gr4-physical-science-batch-review.md`
- `lesson-plans/gr4-engineering-batch-review.md`
- `lesson-plans/gr4-life-science-audit-and-scope.md`
- `lesson-plans/gr4-life-science-gap-analysis-2026-04-11.md`

## Calvin verdict on current Grade 4

Grade 4 is stronger than Grades 2 and 5 in one important way: three lanes already feel like real sellable packages.
- Life Science = real 2-unit domain
- Physical Science = real 6-lesson energy/motion unit
- Engineering = real 6-lesson storm-shelter unit

The weak point is not lack of content everywhere. The weak point is **Earth & Space Science confusion plus one major missing physical-science lane**.

Right now Grade 4 can look more complete than it really is because:
- Earth processes appear twice under two near-duplicate unit families
- one legacy life-science page (`food-webs`) creates false cross-grade noise
- there is still no real Grade 4 waves / information-transfer lane
- there is still no convincing Grade 4 sky/space lane visible in the repo

So the correct Grade 4 move is **cleanup first, then build the missing high-value lanes**.

## What is already solid enough to keep

### Keep: Grade 4 Life Science (`gr4-ls1-unit1-*`, `gr4-ls1-unit2-*`)
Why it earns its slot:
- clear Grade 4 lift into structure-function reasoning
- distinct from Grade 3 life cycles / traits and Grade 5 ecosystems
- argumentation capstones make it feel older and more rigorous

Calvin note:
- do not dilute this lane by adding off-theme ecology pages inside Grade 4 life science
- protect the structure-function identity

### Keep: Grade 4 Physical Science (`gr4-ps3-unit1-*`)
Why it earns its slot:
- progression is clean: stored energy → collisions → motion changes → friction → testing variables → explanation
- stronger than lower-grade “push/pull” work
- commercially coherent as a single Energy & Motion unit

Calvin note:
- this is good canon
- it does **not** mean Grade 4 physical science is complete overall

### Keep: Grade 4 Engineering (`gr4-ets1-unit1-*`)
Why it earns its slot:
- strong criteria/constraints/testing sequence
- good transfer from Earth/weather knowledge into design work
- clearer than generic “build something” engineering

Calvin note:
- keep it as the engineering anchor
- do not add another engineering lane before fixing Grade 4 Earth duplication and the missing waves lane

## Duplication / false-completeness flags

### Duplication flag 1: Grade 4 Earth processes exist in two near-parallel unit families
Files involved:
- `gr4-ess1-unit1-lesson1-weathering-starts-landform-change.html`
- `gr4-ess1-unit1-lesson2-erosion-moves-sediment.html`
- `gr4-ess1-unit1-lesson3-deposition-builds-new-landforms.html`
- `gr4-ess1-unit1-lesson4-maps-and-models-show-earth-surface-change.html`
- `gr4-ess1-unit1-lesson5-patterns-of-water-wind-ice-and-vegetation.html`
- `gr4-ess1-unit1-lesson6-explain-and-protect-a-changing-streambank.html`

and

- `gr4-ess2-unit1-lesson1-weathering-breaks-rocks.html`
- `gr4-ess2-unit1-lesson2-erosion-moves-earth-materials.html`
- `gr4-ess2-unit1-lesson3-deposition-builds-new-landforms.html`
- `gr4-ess2-unit1-lesson4-reading-landform-maps-and-models.html`
- `gr4-ess2-unit1-lesson5-fast-and-slow-surface-changes.html`
- `gr4-ess2-unit1-lesson6-explain-how-earth-processes-shape-landforms.html`

Calvin judgment:
- this is too much overlap for one grade-level catalog lane
- both sets are clearly about the same core Earth-surface-process story
- keeping both live as if they are separate Grade 4 units creates false breadth and discovery confusion

Recommended cleanup disposition:
- treat `gr4-ess2-unit1-*` as the canonical Grade 4 Earth-processes sequence
- treat `gr4-ess1-unit1-*` as legacy / replacement / consolidation material unless a human explicitly wants both preserved for a separate business reason
- do not build a second Earth-processes unit before this is resolved

### Duplication flag 2: `gr4-ls1-unit1-l1-food-webs.html` should not be treated as Grade 4 canon
Why it is a problem:
- it drifts away from the actual Grade 4 LS1 structure-function package
- food webs belong much more naturally to the Grade 5 ecosystems lane already in repo
- leaving it floating near canonical Grade 4 life science muddies the grade identity

Recommended cleanup disposition:
- keep it clearly de-listed / non-canonical
- do not let discovery surfaces imply that Grade 4 life science is partly about food webs

### Duplication flag 3: the free apple oxidation trio is not a domain-completeness signal
Files involved:
- `free-gr4-apple-oxidation.html`
- `free-gr4-apple-oxidation-refcard.html`
- `free-gr4-apple-oxidation-quiz.html`

Calvin note:
- these are good freebie / promo assets
- they do **not** close a Grade 4 chemistry gap by themselves
- do not mistake “there is a nice free lesson” for “Grade 4 matter coverage is solved”

## Grade 4 real gaps

### Gap 1: no clean Grade 4 waves / information-transfer unit
Why this matters:
- Grade 4 physical science should not stop at motion/energy only
- the repo currently has no real `4-PS4` lane for waves, patterns, light/sound signal thinking, or information transfer
- this is one of the clearest missing upper-elementary paid units in the current Grade 4 catalog

Non-overlap guardrail:
- do **not** rebuild Grade 1 light/sound as a watered-down repeat
- Grade 4 should feel older by using models, pattern transfer, and communication-system reasoning

### Gap 2: no convincing Grade 4 sky/space lane
Current repo problem:
- Grade 4 Earth inventory is overloaded on landform change and underbuilt on the broader Earth/space identity families expect from a full grade catalog
- there is no clean sky/space observation unit visible in the actual repo inventory

Non-overlap guardrail:
- do not repeat Grade 1 “sun/moon/stars basics” in simpler words
- Grade 4 should lean into patterns, models, and explanatory reasoning

### Gap 3: Earth cleanup is required before more Earth drafting
Why this matters:
- until `gr4-ess1-unit1-*` vs `gr4-ess2-unit1-*` is resolved, any new Earth drafting risks making the catalog even harder to understand
- discovery surfaces should not suggest two different canonical landform-process units for the same grade unless a human explicitly wants that duplication

## Cross-grade guardrails for future Grade 4 work

Do **not** spend future Grade 4 build time on these watered-down repeats:
- generic food chains / ecosystem intros that belong to Grade 5
- basic weather observation and water-cycle talk from K–2
- generic animal life cycle comparison from Grade 3
- another earth-surface-process unit before the duplicate Earth lane is cleaned up

Grade 4 should feel like a real lift into:
- structure-function argumentation
- clearer mechanism talk
- stronger testing and variable control
- models that explain, not just label

## Recommended fill / cleanup order

### 1) Highest-priority cleanup: canonicalize Grade 4 Earth science
Do this first:
- choose one canonical Earth-processes family
- de-list or clearly archive the duplicate family
- make the curriculum/discovery story say one honest thing

Calvin default:
- keep `gr4-ess2-unit1-*`
- archive or clearly subordinate `gr4-ess1-unit1-*`

### 2) Highest-value new build: Grade 4 Physical Science Unit 2 — Waves, Light & Information
Why next:
- biggest obvious NGSS-shape gap in Grade 4
- clearly distinct from existing motion unit
- easy to market because it supports mirrors, signals, vibrations, and communication design

### 3) Next Earth build: Grade 4 sky/space observations unit
Why after waves:
- fills the other obvious missing Grade 4 content identity
- gives Grade 4 Earth & Space Science broader credibility than “landforms twice”

### 4) Only after those: optional chemistry / engineering expansion
Possible later lane:
- a fuller Grade 4 chemistry or materials-change lane
- but only after the duplicate Earth lane and missing waves lane are handled

## Bottom-line Calvin judgment

Grade 4 is not a disaster. It already has several strong canonical units. But it is not honestly “finished” either.

The real Grade 4 problem is:
- one duplicated Earth lane creating false breadth
- one missing major waves lane
- one missing sky/space lane
- one legacy food-webs artifact that should stay non-canonical

So the right next move is not random new drafting. It is:
1. clean the Earth duplication
2. build waves/info transfer
3. build sky/space
4. then decide whether Grade 4 needs anything else
