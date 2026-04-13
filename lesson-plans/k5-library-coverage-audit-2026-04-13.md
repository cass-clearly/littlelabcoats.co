# K–5 Library Coverage Audit — 2026-04-13

Purpose: honest full-library coverage scan for the minimum K–5 target shape.

Target shape used for this audit:
- each grade has **4 broad domains**: Physical Science, Life Science, Earth & Space Science, and Engineering
- each broad domain has **at least 1 useful unit**
- a second unit is counted only if it is materially non-repetitive and a useful addition
- each counted unit must have **exactly 6 lesson pages**
- support assets are tracked separately from the lesson-count scan, but missing support assets still block protocol-complete release work

## Audit method

Canonical source scanned:
- top-level `lesson-plans/*.html`

Counting rules used:
- counted only canonical lesson pages, not refcards, quizzes, review docs, audits, or nested `index.html` mirrors
- grouped lessons by grade + discipline family in the filename slug
- mapped `ps*` to Physical Science, `ls*` to Life Science, `ess*` to Earth & Space Science, and `ets*` to Engineering
- treated overlapping duplicate families as a canonical-choice problem instead of double-counting them

## Canonical-choice decisions made in this pass

### Grade 4 Earth & Space Science
There are two overlapping Grade 4 Earth families in the repo:
- `gr4-ess1-unit1-*`
- `gr4-ess2-unit1-*`

Canonical choice for target-shape counting:
- **count `gr4-ess2-unit1-*` as the Grade 4 Earth & Space Science unit**

Why:
- its lesson naming aligns more directly with the Grade 4 weathering / erosion / deposition / landform-change scope
- the `ESS2` family is the cleaner NGSS-family fit for the actual content
- the `ESS1` family is retained in repo as overlapping historical scaffold content, but it should not force a fake “extra unit” count for this audit

### Grade 5 Earth & Space Science
- count `gr5-ess1-unit1-*` as the canonical broad-domain Earth unit
- keep `gr5-ess3` fossils standalone material as an extra artifact, not the minimum-shape unit

## Highest-value gap found at audit start

Only one minimum-shape coverage gap was still open in the canonical lesson inventory at the start of this pass:
- **Grade 4 Physical Science (`gr4-ps3-unit1`) was missing Lesson 1**
- Lessons 2–6, the unit refcard, and the unit quiz already existed
- that made Grade 4 Physical Science the cleanest and highest-value coverage gap to close immediately

## Gap closure completed in this pass

Shipped in this pass:
- `lesson-plans/gr4-ps3-unit1-l1-stored-energy-starts-motion.html`
- `images/lesson-heroes/gr4-ps3-unit1-l1-energy-starts-motion-v2.jpg` (Gemini-generated lesson visual embedded directly in the new lesson)
- supporting unit refinement in `lesson-plans/gr4-ps3-unit1-refcard.html`

Result:
- `gr4-ps3-unit1` now has a full **6 / 6** lesson set in the canonical repo inventory

## Grade-by-grade coverage matrix

### Kindergarten
- **Physical Science:** `k-ps3-unit2` — 6 / 6 lessons
- **Life Science:** `k-ls1-unit2` — 6 / 6 lessons
  - extra useful addition present: `k-ls1-unit3` — 6 / 6 lessons
- **Earth & Space Science:** canonical count uses `k-ess2-unit1` — 6 / 6 lessons
  - extra useful addition present: `k-ess3-unit2` — 6 / 6 lessons
- **Engineering:** `k-ets1-unit1` — 6 / 6 lessons
- **Minimum-shape status:** met

### Grade 1
- **Physical Science:** `gr1-ps4-unit1` — 6 / 6 lessons
- **Life Science:** `gr1-ls1` canonical unit — 6 / 6 lessons
  - extra useful addition present: `gr1-ls3-unit2` — 6 / 6 lessons
- **Earth & Space Science:** `gr1-ess1-unit1` — 6 / 6 lessons
- **Engineering:** `gr1-ets1-unit1` — 6 / 6 lessons
- **Minimum-shape status:** met

### Grade 2
- **Physical Science:** `gr2-ps1-unit1` — 6 / 6 lessons
- **Life Science:** `gr2-ls2-unit1` — 6 / 6 lessons
  - extra useful addition present: `gr2-ls2-unit2` — 6 / 6 lessons
- **Earth & Space Science:** `gr2-ess1-unit3` — 6 / 6 lessons
- **Engineering:** `gr2-ets1-unit1` — 6 / 6 lessons
- **Minimum-shape status:** met

### Grade 3
- **Physical Science:** `gr3-ps2-unit1` — 6 / 6 lessons
- **Life Science:** canonical count uses `gr3-ls1-unit1` — 6 / 6 lessons
  - extra useful additions present: `gr3-ls3-unit2` and `gr3-ls4-unit3`, both 6 / 6 lessons
- **Earth & Space Science:** `gr3-ess2-unit1` — 6 / 6 lessons
- **Engineering:** `gr3-ets1-unit1` — 6 / 6 lessons
- **Minimum-shape status:** met

### Grade 4
- **Physical Science:** `gr4-ps3-unit1` — 6 / 6 lessons after this pass
- **Life Science:** canonical count uses `gr4-ls1-unit1` — 6 / 6 lessons
  - extra useful addition present: `gr4-ls1-unit2` — 6 / 6 lessons
- **Earth & Space Science:** canonical choice `gr4-ess2-unit1` — 6 / 6 lessons
  - overlapping non-canonical scaffold still present: `gr4-ess1-unit1` — 6 / 6 lessons
- **Engineering:** `gr4-ets1-unit1` — 6 / 6 lessons
- **Minimum-shape status:** met

### Grade 5
- **Physical Science:** `gr5-ps2-unit1` — 6 / 6 lessons
- **Life Science:** canonical count uses `gr5-ls1-unit1` — 6 / 6 lessons
  - extra useful addition present: `gr5-ls1-unit2` — 6 / 6 lessons
- **Earth & Space Science:** canonical choice `gr5-ess1-unit1` — 6 / 6 lessons
  - extra standalone artifact present: `gr5-ess3` fossils material, not counted as the minimum-shape unit
- **Engineering:** `gr5-ets1-unit1` — 6 / 6 lessons
- **Minimum-shape status:** met

## Bottom line

After the Grade 4 Physical Science Lesson 1 creation in this pass, the canonical repo inventory now supports the minimum K–5 shape honestly:
- every grade has all 4 broad domains represented
- every counted broad-domain unit has a complete 6-lesson lesson set
- remaining work is now mainly **review-program completion, live verification, and canonical cleanup**, not missing whole-domain unit creation for the minimum shape

## Remaining non-coverage work that still matters

This audit is only about the minimum curriculum-shape inventory. It does **not** by itself prove that every counted unit has already completed the full Little Lab Coats review protocol.

Important follow-up lanes still remain:
- continue reviewer-program closeout for other unreviewed units now that Grade 4 Physical Science has been restored, reviewed, pushed, and live-verified in this pass
- move next into Grade 4 Earth & Space Science using `gr4-ess2-unit1` as the canonical Grade 4 Earth review lane
- eventually retire or clearly deprecate the overlapping `gr4-ess1-unit1` scaffold so later audits do not double-count Grade 4 Earth content
