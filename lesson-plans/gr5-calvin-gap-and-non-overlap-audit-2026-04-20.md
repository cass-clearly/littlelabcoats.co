# Grade 5 Calvin Gap + Non-Overlap Audit — 2026-04-20

Purpose: audit the actual Grade 5 repo state for duplication, partial-unit traps, NGSS completeness, and the right fill / cleanup order so future work does not mistake one-offs and legacy pages for a finished fifth-grade catalog.

## Repo baseline audited

### Grade 5 domains currently present in repo
- Life Science
  - `gr5-ls1-unit1-*`
  - `gr5-ls1-unit2-*`
- Earth & Space Science
  - `gr5-ess1-unit1-*`
  - `gr5-ess3-unit1-l1-human-impact.html`
  - `5th-fossils-earth-history.html`
- Physical Science
  - `gr5-ps2-unit1-*`
  - `gr5-ps1-lesson1-reactants-products-mixtures.html`
  - `gr5-ps1-refcard.html`
  - `gr5-ps1-unit1-quiz.html`
  - `5th-forces-balanced-unbalanced.html`
- Engineering
  - `gr5-ets1-unit1-*`
- Related freebie / legacy files
  - `free-gr5-bread-mold-terrarium.html`
  - `free-gr5-bread-mold-terrarium-refcard.html`
  - `free-gr5-bread-mold-terrarium-quiz.html`

### Review / audit evidence checked
- `lesson-plans/gr5-life-science-batch-review.md`
- `lesson-plans/gr5-earth-science-batch-review.md`
- `lesson-plans/gr5-engineering-batch-review.md`
- `lesson-plans/gr5-life-science-gap-analysis-2026-04-11.md`
- `lesson-plans/gr5-ps1-mixed-age-atoms-calvin-review-2026-04-14.md`

## Calvin verdict on current Grade 5

Grade 5 has some genuinely strong finished lanes already:
- Life Science = strong 2-unit domain
- Engineering = real water-filter design package
- Forces / motion = real 6-lesson physical-science unit
- Water systems = real 6-lesson Earth-science unit

But Grade 5 is still not complete because the remaining weak spots are major, not cosmetic.

The big problem is **false completeness**.
At first glance the repo can make Grade 5 look broad, but several of those surfaces are actually:
- legacy standalones
- partial units
- orphan lessons
- alternative versions of content already handled better somewhere else

The main Grade 5 work left is not to sprinkle more freebies around. It is to finish the incomplete canonical lanes honestly.

## What is already solid enough to keep

### Keep: Grade 5 Life Science (`gr5-ls1-unit1-*`, `gr5-ls1-unit2-*`)
Why it earns its slot:
- ecosystems / matter movement lane is clearly older than lower-grade food-chain content
- plant matter / growth unit closes a real Grade 5 conceptual gap
- the domain now feels like real upper-elementary life science rather than scattered lessons

Calvin note:
- protect this lane from lower-grade ecology drift
- do not backslide into simpler “what is a habitat?” content here

### Keep: Grade 5 Engineering (`gr5-ets1-unit1-*`)
Why it earns its slot:
- criteria, constraints, testing, redesign, and evidence all feel appropriately older
- the water-filter challenge is coherent and commercially strong

### Keep: Grade 5 Forces / Motion (`gr5-ps2-unit1-*`)
Why it earns its slot:
- progression is clean and complete
- this is the canonical Grade 5 motion/forces lane, not the old standalone legacy page

### Keep: Grade 5 Water Systems (`gr5-ess1-unit1-*`)
Why it earns its slot:
- the unit is coherent and review-complete
- it gives Grade 5 a real Earth-systems story instead of one-off water-cycle pages

## Duplication / false-completeness flags

### Duplication flag 1: `5th-forces-balanced-unbalanced.html` is not the canonical Grade 5 forces lane
Why it is a problem:
- the real canonical package is `gr5-ps2-unit1-*`
- keeping the older standalone as if it is equal to the full unit creates discovery noise
- it can trick future audits into thinking there are two separate Grade 5 forces products when there is really one full lane plus one legacy artifact

Recommended cleanup disposition:
- keep the full `gr5-ps2-unit1-*` unit as canon
- treat `5th-forces-balanced-unbalanced.html` as legacy / non-canonical / marketing-only if needed

### Duplication flag 2: `gr5-ps1-lesson1-reactants-products-mixtures.html` plus refcard + quiz look like a unit start, but they do not close Grade 5 chemistry
Why it is a problem:
- there is one lesson, one refcard, and one quiz, but no real 6-lesson unit
- this can easily be mistaken for a finished matter lane when it is not
- Calvin’s 2026-04-14 review already confirmed the lane is still too thin and not the requested mixed-age atoms package

Recommended cleanup disposition:
- keep it as a precursor / starter asset
- do not describe Grade 5 physical science as complete because of this one-off
- do not build random adjacent chemistry freebies before the core matter lane exists

### Duplication flag 3: Earth-science content is fragmented across one real unit + one orphan lesson + one legacy fossil page
Files involved:
- `gr5-ess1-unit1-*`
- `gr5-ess3-unit1-l1-human-impact.html`
- `5th-fossils-earth-history.html`

Why it is a problem:
- the water-systems unit is real canon
- the human-impact page is only lesson 1 of something larger and currently stands alone
- the fossil/history page sits outside a clean canonical unit structure
- together they create the illusion of broader Earth coverage than the repo actually supports

Recommended cleanup disposition:
- keep the water-systems unit as canon
- either complete the human-impact/resources lane or clearly mark it unfinished
- decide whether the fossil page becomes the seed of a real Earth-history unit or gets de-emphasized until such a unit exists

### Duplication flag 4: freebies should not be counted as canonical lane coverage
Files involved:
- `free-gr5-bread-mold-terrarium.html`
- `free-gr5-bread-mold-terrarium-refcard.html`
- `free-gr5-bread-mold-terrarium-quiz.html`

Calvin note:
- useful promo/sample assets
- not a substitute for a full decomposers or microbiology unit
- should not drive Grade 5 scope decisions by themselves

## Grade 5 real gaps

### Gap 1: Grade 5 matter / atoms / chemical-change lane is still incomplete
Evidence:
- only one chemistry lesson exists in the `gr5-ps1` lane
- the companion refcard and quiz exist, but the unit itself does not
- Calvin’s 2026-04-14 review already says the lane is too thin and not yet the requested mixed-age atoms package

Why this is the highest-value gap:
- it is one of the clearest missing upper-elementary science lanes in the whole catalog
- it supports strong parent-impressive lessons if done well
- it should feel meaningfully older than Grade 2 matter by using invisible-particle models, rearrangement reasoning, and evidence about new substances

Non-overlap guardrail:
- do not rebuild Grade 2 “sort properties / sink-float / simple mixing” at a slightly older reading level
- Grade 5 must feel like matter-conservation and model-based chemistry reasoning

### Gap 2: Grade 5 human-impact / resource-protection lane is incomplete
Current repo state:
- `gr5-ess3-unit1-l1-human-impact.html` exists
- the rest of the unit does not appear in the audited repo inventory

Why this matters:
- the existing lesson is promising, but one lesson does not make a real Earth-systems / stewardship lane
- Grade 5 should have a coherent community-solutions unit, not one isolated concern page

Non-overlap guardrail:
- do not make it a recycled Grade 2 “save the Earth” feelings unit
- Grade 5 should use information from communities, systems, tradeoffs, and evidence-backed solutions

### Gap 3: Earth-history / fossils content is unresolved
Current repo state:
- `5th-fossils-earth-history.html` exists as a standalone legacy page
- there is no clear 6-lesson Earth-history unit visible around it

Why this matters:
- fossils and Earth history are a natural strong Grade 5 offering if treated as a real lane
- right now the repo does not clearly decide whether this is canonical curriculum or legacy residue

### Gap 4: directory truthfulness still depends on cleanup discipline
Because Grade 5 has multiple strong units plus several standalones, it is easy for future work to overclaim completeness unless discovery surfaces distinguish:
- canonical unit
- unfinished lane seed
- legacy standalone
- free sample

## Cross-grade guardrails for future Grade 5 work

Do **not** spend future Grade 5 build time on these weak repeats:
- simple food-chain / habitat intro content already owned by Grade 2 and early Grade 5 life science lessons
- generic push/pull force pages that repeat lower-grade motion ideas
- simple water-cycle diagram pages without systems reasoning
- broad “pollution is bad” lessons without community-solution or systems depth

Grade 5 should feel older by emphasizing:
- models of unseen matter
- conservation / rearrangement reasoning
- argument from evidence
- Earth systems interactions
- real community or engineering solutions

## Recommended fill / cleanup order

### 1) Highest-value build: full Grade 5 PS1 matter / atoms / chemical-change unit
Why first:
- biggest unfinished canonical science lane in Grade 5
- already has a starter asset, which means the fastest path is to convert the thin chemistry one-off into a real 6-lesson sequence
- Calvin review already identified the direction: shared model work, atom counts, rearrangement, and conservation

### 2) Next fill: complete the Grade 5 human-impact / resource-protection unit
Why second:
- there is already a strong Lesson 1 seed
- the grade needs a real `5-ESS3` lane, not an orphan page
- this has strong business value for homeschool families because it connects science to meaningful action

### 3) Cleanup decision: fossils / Earth history
Options:
- promote `5th-fossils-earth-history.html` into a real Earth-history unit seed and finish the lane
- or clearly de-emphasize it until the full unit exists

But do not leave it floating in an ambiguous half-canonical state.

### 4) Cleanup decision: legacy forces standalone
After the bigger gaps above:
- keep `gr5-ps2-unit1-*` as the canonical force/motion package
- de-list or clearly subordinate `5th-forces-balanced-unbalanced.html`

## Bottom-line Calvin judgment

Grade 5 already has enough strong work to feel promising, but it is still missing one major physical-science lane and one major Earth-science lane.

The real Grade 5 problems are:
- matter/atoms lane still incomplete
- human-impact/resources lane still incomplete
- fossils/Earth-history lane still unresolved
- legacy standalones can make the catalog look broader than it really is

So the right next move is:
1. finish Grade 5 PS1 honestly
2. finish Grade 5 ESS3 honestly
3. decide whether fossils becomes a real unit or stays non-canonical
4. clean discovery surfaces so canonical work is obvious and legacy work does not masquerade as completeness
