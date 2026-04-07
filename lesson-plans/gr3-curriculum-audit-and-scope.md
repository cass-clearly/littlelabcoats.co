# Grade 3 Curriculum Audit and Scope

Last updated: 2026-04-07

## Purpose

This file is the single tracking artifact for Grade 3 repo inventory, curriculum crosswalk, status classification, and implementation backlog.

It began as the **audit + scope definition** tracker for the Grade 3 buildout pass and now also carries the final in-repo QA reconciliation snapshot for handoff.

Unless a later section explicitly says otherwise, early tables in this file should be read as historical audit snapshots rather than the final current-state status.

**Current-state shortcut:** for the final integrated status view, go directly to `Final Grade 3 QA pass snapshot (2026-04-07, iteration 1 of 2)` near the end of this file.

It does **not** claim that Rachel review, Margaret review, or Remarq inline review has happened unless a later batch-review section explicitly records those notes.

---

## Source inputs used for this audit

### Curriculum/navigation references
- `curriculum/index.html`
  - Grade 3 public curriculum currently shows only `3-LS4: Adaptation` with `Bird Beak Buffet`
  - Grade 3 section also says: `More Grade 3 Units Coming Soon`
- `index.html`
  - Grade 3 landing view shows only `Bird Beak Buffet` under Life Science and a cross-grade physical science entry (`Thermal Energy Ice Cream`)

### Style + implementation references
- `lesson-plans/style-guide.html`
  - Establishes canonical LLC terminology such as `Student Worksheet`, `Parent Answer Key`, `The Big Idea`, `Discussion Questions`, `Materials`, and `Parent / Teacher Notes` or `Teacher Notes` for grades 3–5
- `lesson-plans/gr3-ls1-unit1-lesson1-template-audit.md`
- `lesson-plans/gr3-ls1-unit1-lesson2-template-audit.md`
  - Both explicitly recommend using strong nearby LLC lessons for structure/behavior and preserving paywall/review behavior, `data-document-id`, feedback layer, and footer parity

### Existing Grade 3 lesson artifacts inspected
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html`
- `lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`
- `lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html`
- `lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`
- `lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`
- `lesson-plans/gr3-ps2-unit1-quiz.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html`
- `lesson-plans/gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- `lesson-plans/bird-beak-buffet.html`

---

## Audit summary

### What is clearly established now
1. **Grade 3 Life Science Unit 1 Lesson 1 and Lesson 2 are the current baseline Grade 3 LLC lesson templates.**
   - `gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
   - `gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`
2. These two files already reflect the newer LLC shell expected for later Grade 3 work:
   - stronger LLC section rhythm
   - `Student Worksheet`
   - `Parent Answer Key`
   - feedback layer script
   - preview/paywall behavior
   - pending `data-document-id` placeholders suitable for later review wiring
3. **Grade 3 Physical Science Unit 1 exists only partially.**
   - Lessons 1–2 have content
   - Lessons 3–6 are TODO placeholders
   - quiz is TODO placeholder
   - only refcard for lesson 1 has real content
4. **Public navigation does not yet represent the full Grade 3 scope.**
   - Public curriculum currently advertises only `Bird Beak Buffet` for Grade 3
   - the remaining Grade 3 files are repo artifacts, not yet fully surfaced as public curriculum entries

### Scope decision for this chunk
The canonical Grade 3 scope for the next implementation passes should be based on the **actual Grade 3 repo curriculum artifacts discovered in the repo**, not on current public navigation alone.

### Scope buckets used in this audit

#### 1. Canonical discovered-in-repo curriculum scope
These are the Grade 3 curriculum slots that are actively scaffolded or implemented in the repo and should drive the next build passes.
- `3-LS1` Life Science Unit 1 — Lessons 1–2 already present and canonical
- `3-PS2` Physical Science Unit 1 — Lessons 1–6 + per-lesson refcards + unit quiz scaffolded in filenames
- `3-LS4` standalone lesson — `Bird Beak Buffet` already public/live and tracked as a Grade 3 public artifact

#### 2. Publicly linked now
These are currently discoverable in Grade 3 navigation/public curriculum references.
- `lesson-plans/bird-beak-buffet.html`
- Grade 3 navigation references in `curriculum/index.html`
- Grade 3 landing references in `index.html`

#### 3. Adjacent but out of canonical unit scope
These are Grade 3-branded or Grade 3-adjacent artifacts that should be tracked, but should **not** be mistaken for the core canonical Grade 3 unit map.
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- cross-grade Grade 3 landing references such as `Thermal Energy Ice Cream`

#### 4. Unknown / not-yet-referenced Grade 3 curriculum
These items may exist in an external curriculum plan, but are **not discoverable as structured Grade 3 scope in this repo today**.
- additional Grade 3 Life Science units beyond `3-LS1` and `3-LS4`
- Grade 3 Earth/Space Science units
- Grade 3 Engineering/ETS units
- a full year-at-a-glance Grade 3 map comparable to the Kindergarten curriculum map

### Open scope caveat
This repo does **not** currently expose a complete full-year Grade 3 curriculum map in the way Kindergarten does. So this audit tracks the **discovered Grade 3 curriculum references and file scaffolds that actually exist now**. If Serena/Chris have an external full-year Grade 3 sequence, that can expand this file in a later planning pass.

---

## Baseline template decisions for later build work

See also: `lesson-plans/gr3-implementation-baseline.md` for the reusable Grade 3 shell, standards/terminology checklist, route/paywall expectations, and review-loop acceptance checklist used by later build batches.


### Primary Grade 3 baseline templates
These should be treated as the **canonical format references** for remaining Grade 3 lessons.

#### A. `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
Status: `live complete baseline template`

Why it matters:
- explicitly rebuilt into the established LLC lesson shell
- includes `data-document-id`
- includes `feedback-layer.js`
- includes preview/paywall/review behavior
- includes `Student Worksheet`
- includes `Parent Answer Key`
- includes stronger print/layout parity

#### B. `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`
Status: `live complete baseline template`

Why it matters:
- explicitly intended to feel like direct continuity from Grade 3 Lesson 1
- preserves the same modern LLC shell and public/review behavior
- confirms the current Grade 3 lesson rhythm, tone, and review/publish parity expectations

### Strong nearby LLC exemplar noted by the audits
- `lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html`
  - structural shell and behavior reference
- `lesson-plans/k-ls1-unit2-lesson6-plant-life-cycle.html`
  - topic-specific life-cycle framing reference only

### Brand/style constraints to carry forward
From `lesson-plans/style-guide.html` and the template audits:
- use `Student Worksheet` exactly
- use `Parent Answer Key` exactly
- use `The Big Idea`, `Discussion Questions`, `Materials`
- for Grade 3+, use `Parent / Teacher Notes` or `Teacher Notes` rather than kindergarten-specific wording
- preserve preview/paywall/review structure when making modern LLC lesson pages
- do not invent a new visual/content format

---

## Repo inventory: all discovered Grade 3 artifacts

### A. Canonical Grade 3 lesson pages

| Artifact | Type | Route candidate | Current status | Notes |
|---|---|---|---|---|
| `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | lesson page | `/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | live complete baseline | modern LLC shell; worksheet + answer key + feedback/paywall |
| `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | lesson page | `/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | live complete baseline | modern LLC shell; worksheet + answer key + feedback/paywall |
| `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | lesson page | `/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | draft incomplete | content-bearing; older/simpler shell; has worksheet + answer key; lacks modern paywall/review parity |
| `lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | lesson page | `/lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | draft incomplete | content-bearing; older/simpler shell; has worksheet + answer key; lacks modern paywall/review parity |
| `lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | lesson page | `/lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | placeholder | file is TODO only |
| `lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html` | lesson page | `/lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html` | placeholder | file is TODO only |
| `lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | lesson page | `/lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | placeholder | file is TODO only |
| `lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | lesson page | `/lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | placeholder | file is TODO only |

### B. Grade 3 refcards and quiz artifacts

| Artifact | Type | Route candidate | Current status | Notes |
|---|---|---|---|---|
| `lesson-plans/gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html` | refcard | `/lesson-plans/gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html` | draft incomplete | content exists; needs consistency review against final Grade 3 pattern |
| `lesson-plans/gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html` | refcard | `/lesson-plans/gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html` | placeholder | TODO only |
| `lesson-plans/gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html` | refcard | `/lesson-plans/gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html` | placeholder | TODO only |
| `lesson-plans/gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html` | refcard | `/lesson-plans/gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html` | placeholder | TODO only |
| `lesson-plans/gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html` | refcard | `/lesson-plans/gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html` | placeholder | TODO only |
| `lesson-plans/gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html` | refcard | `/lesson-plans/gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html` | placeholder | TODO only |
| `lesson-plans/gr3-ps2-unit1-quiz.html` | unit quiz | `/lesson-plans/gr3-ps2-unit1-quiz.html` | placeholder | TODO only |

### C. Grade 3 planning/reference artifacts

| Artifact | Type | Current status | Notes |
|---|---|---|---|
| `lesson-plans/gr3-ls1-unit1-lesson1-template-audit.md` | audit/reference | reference-only | implementation guidance for the modern Grade 3 shell |
| `lesson-plans/gr3-ls1-unit1-lesson2-template-audit.md` | audit/reference | reference-only | implementation guidance for continuity and review/paywall parity |

### D. Other Grade 3 public/adjacent artifacts

| Artifact | Type | Current status | Notes |
|---|---|---|---|
| `lesson-plans/bird-beak-buffet.html` | standalone Grade 3 lesson | live complete | linked in `curriculum/index.html` and `index.html`; tagged to Grade 3 adaptation |
| `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html` | freebie/marketing lesson | live complete / out-of-scope for canonical map | Grade 3-branded public asset, but not part of current discovered LS1/PS2 unit structure |

### E. Route consistency findings

- Discovered Grade 3 lesson files are currently plain `.html` files in `lesson-plans/`
- No matching Grade 3 per-lesson directory routes (`lesson-plans/.../index.html`) were found for these Grade 3 files
- Public navigation currently points only to `bird-beak-buffet.html` for Grade 3
- Route consistency and public linking remain follow-up work for later chunks

### F. Per-artifact supporting-assets inventory

This table is the compact asset/supporting-material audit for discovered Grade 3 lesson artifacts.

| Artifact | Worksheet present | Parent Answer Key present | Feedback layer / review hooks | Preview / paywall hooks | Supporting asset status | Notes |
|---|---|---|---|---|---|---|
| `gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | yes | yes | yes | yes | strong baseline | current best-in-class Grade 3 shell |
| `gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | yes | yes | yes | yes | strong baseline | current best-in-class Grade 3 shell |
| `gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | yes | yes | no modern parity found | no modern parity found | partial | has worksheet + answer key but not the modern LLC review/paywall shell |
| `gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | yes | yes | no modern parity found | no modern parity found | partial | has worksheet + answer key but not the modern LLC review/paywall shell |
| `gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | no | no | no | no | placeholder | TODO-only file |
| `gr3-ps2-unit1-lesson4-magnetic-patterns.html` | no | no | no | no | placeholder | TODO-only file |
| `gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | no | no | no | no | placeholder | TODO-only file |
| `gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | no | no | no | no | placeholder | TODO-only file |
| `gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html` | n/a | n/a | n/a | n/a | partial | content-bearing refcard |
| `gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html` | n/a | n/a | n/a | n/a | placeholder | TODO-only refcard |
| `gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html` | n/a | n/a | n/a | n/a | placeholder | TODO-only refcard |
| `gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html` | n/a | n/a | n/a | n/a | placeholder | TODO-only refcard |
| `gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html` | n/a | n/a | n/a | n/a | placeholder | TODO-only refcard |
| `gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html` | n/a | n/a | n/a | n/a | placeholder | TODO-only refcard |
| `gr3-ps2-unit1-quiz.html` | n/a | n/a | n/a | n/a | placeholder | TODO-only quiz |
| `bird-beak-buffet.html` | not audited in this chunk | not audited in this chunk | not audited in this chunk | not audited in this chunk | public-adjacent baseline | tracked as existing public Grade 3 artifact, not part of LS1/PS2 modernization scope |
| `free-gr3-egg-drop-kitchen-challenge.html` | not audited in this chunk | not audited in this chunk | not audited in this chunk | not audited in this chunk | public-adjacent freebie | tracked for scope hygiene only |

### G. Current public URLs vs intended discovered Grade 3 routes

| Grade 3 artifact | Currently linked publicly from Grade 3 navigation? | Current known public URL candidate | Intended/discovered route field | Notes |
|---|---|---|---|---|
| `Bird Beak Buffet` | yes | `/lesson-plans/bird-beak-buffet.html` | `/lesson-plans/bird-beak-buffet.html` | only clearly linked Grade 3 lesson now |
| `3-LS1 Unit 1 L1` | no | none currently linked from Grade 3 navigation | `/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | repo artifact exists; not exposed in Grade 3 navigation |
| `3-LS1 Unit 1 L2` | no | none currently linked from Grade 3 navigation | `/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | repo artifact exists; not exposed in Grade 3 navigation |
| `3-PS2 Unit 1 L1` | no | none currently linked from Grade 3 navigation | `/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | repo artifact exists |
| `3-PS2 Unit 1 L2` | no | none currently linked from Grade 3 navigation | `/lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | repo artifact exists |
| `3-PS2 Unit 1 L3` | no | none currently linked from Grade 3 navigation | `/lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | TODO placeholder file exists |
| `3-PS2 Unit 1 L4` | no | none currently linked from Grade 3 navigation | `/lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html` | TODO placeholder file exists |
| `3-PS2 Unit 1 L5` | no | none currently linked from Grade 3 navigation | `/lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | TODO placeholder file exists |
| `3-PS2 Unit 1 L6` | no | none currently linked from Grade 3 navigation | `/lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | TODO placeholder file exists |
| `3-PS2 Unit 1 Quiz` | no | none currently linked from Grade 3 navigation | `/lesson-plans/gr3-ps2-unit1-quiz.html` | TODO placeholder file exists |

---

## Detailed completion-gap classification for `gr3-ps2-unit1-*`

### Lesson pages

#### `gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
Current classification: `draft incomplete`

What exists now:
- title, metadata, NGSS standard, learning objective, big idea
- materials
- investigation steps
- discussion questions
- parent/teacher notes
- student worksheet
- parent/teacher answer key content
- pending `data-document-id`

Specific completion needs:
- rebuild into the **modern Grade 3 LLC shell** used by Life Science Lessons 1–2
- standardize section names and visual rhythm to the newer template
- add full preview/paywall/review behavior parity
- add feedback layer script/footer parity if missing from final shell
- review wording/terminology against style guide (`Parent Answer Key`, exact section naming, etc.)
- verify route/public-link assumptions later

#### `gr3-ps2-unit1-lesson2-motion-changes-with-force.html`
Current classification: `draft incomplete`

What exists now:
- same broad structure as lesson 1
- content-bearing lesson body
- worksheet and answer key sections
- pending `data-document-id`

Specific completion needs:
- same modernization/parity work required for lesson 1
- align fully to the established Grade 3 lesson shell
- verify consistent answer-key naming/wording against style guide
- add review/paywall/footer/feedback parity if missing from final shell

#### `gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`
Current classification: `placeholder`

Specific completion needs:
- full lesson page must be created from TODO stub
- include worksheet and parent answer key if pattern remains applicable
- include modern review/paywall shell
- likely use existing magnet-related nearby LLC lessons as topic reference while preserving Grade 3 shell

#### `gr3-ps2-unit1-lesson4-magnetic-patterns.html`
Current classification: `placeholder`

Specific completion needs:
- full lesson page from TODO stub
- worksheet + parent answer key where appropriate
- modern shell + review/paywall parity

#### `gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`
Current classification: `placeholder`

Specific completion needs:
- full engineering/design lesson from TODO stub
- worksheet + parent answer key where appropriate
- modern shell + review/paywall parity
- likely needs especially clear build/test/revise workflow in the lesson itself

#### `gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`
Current classification: `placeholder`

Specific completion needs:
- full capstone/improvement lesson from TODO stub
- worksheet + parent answer key where appropriate
- modern shell + review/paywall parity
- likely depends on lesson 5 design challenge structure

### Supporting artifacts

#### `gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html`
Current classification: `draft incomplete`

What exists now:
- compact reference card content exists

Specific completion needs:
- verify final terminology and visual parity with approved Grade 3 reference-card pattern
- verify whether per-lesson refcards remain the intended pattern for the whole unit

#### Refcards for Lessons 2–6
Current classification: `placeholder`

Specific completion needs:
- full content creation from TODO stubs
- ensure one consistent reference-card pattern across the full unit

#### `gr3-ps2-unit1-quiz.html`
Current classification: `placeholder`

Specific completion needs:
- create full interactive/printable unit quiz pattern consistent with LLC practice
- align question coverage to the actual completed lesson sequence after lesson buildout

---

## Canonical Grade 3 curriculum crosswalk

This crosswalk tracks **all currently discoverable Grade 3 curriculum slots** in the repo and classifies expected outputs.

### Status legend
- `live complete` = appears ready and already functioning as a current public/baseline artifact
- `draft incomplete` = real content exists but does not yet meet the target LLC standard for this pass
- `placeholder` = TODO-only stub or equivalent
- `missing` = no discovered artifact exists yet for a scoped slot
- `reference-only` = planning/template guidance, not student-facing curriculum

### Review workflow legend
For every lesson/refcard/quiz build item below, the intended workflow is:
- Build
- Rachel review
- Margaret review
- Revise
- Repeat up to **3 total review rounds max**
- If still unresolved, mark `needs human review`

No review columns below imply work already happened.

| Domain | Unit / Standard | Lesson slot | Lesson title / artifact | Expected outputs | Current repo artifact(s) | Status | Route/public URL field | Rachel review | Margaret review | Rev 1 | Rev 2 | Rev 3 | Ready for human review | Dependencies / notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Life Science | `3-LS1` Unit 1 | L1 | What Is a Life Cycle? | lesson page + student worksheet + parent answer key + review/paywall hooks | `gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | live complete | `/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | planned | planned | planned | planned | planned | not yet recorded | baseline template |
| Life Science | `3-LS1` Unit 1 | L2 | Different Life Cycles, Same Big Pattern | lesson page + student worksheet + parent answer key + review/paywall hooks | `gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | live complete | `/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | planned | planned | planned | planned | planned | not yet recorded | baseline template |
| Physical Science | `3-PS2` Unit 1 | L1 | Balanced and Unbalanced Forces | lesson page + student worksheet + parent answer key + route + review/paywall hooks + refcard coverage | `gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`, `gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html` | draft incomplete | `/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | planned | planned | planned | planned | planned | not yet recorded | modernize to Life Science shell |
| Physical Science | `3-PS2` Unit 1 | L2 | Motion Changes with Force | lesson page + student worksheet + parent answer key + route + review/paywall hooks + refcard coverage | `gr3-ps2-unit1-lesson2-motion-changes-with-force.html`, `gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html` | draft incomplete | `/lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | planned | planned | planned | planned | planned | not yet recorded | lesson exists; refcard placeholder |
| Physical Science | `3-PS2` Unit 1 | L3 | Magnets Pull Without Touching | lesson page + student worksheet + parent answer key + route + review/paywall hooks + refcard coverage | `gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`, `gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html` | placeholder | `/lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | planned | planned | planned | planned | planned | not yet recorded | full creation required |
| Physical Science | `3-PS2` Unit 1 | L4 | Magnetic Patterns | lesson page + student worksheet + parent answer key + route + review/paywall hooks + refcard coverage | `gr3-ps2-unit1-lesson4-magnetic-patterns.html`, `gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html` | placeholder | `/lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html` | planned | planned | planned | planned | planned | not yet recorded | full creation required |
| Physical Science | `3-PS2` Unit 1 | L5 | Design a Magnetic Game or Tool | lesson page + student worksheet + parent answer key + route + review/paywall hooks + refcard coverage | `gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`, `gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html` | placeholder | `/lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | planned | planned | planned | planned | planned | not yet recorded | likely depends on L3/L4 content grounding |
| Physical Science | `3-PS2` Unit 1 | L6 | Test and Improve Your Force Design | lesson page + student worksheet + parent answer key + route + review/paywall hooks + refcard coverage | `gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`, `gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html` | placeholder | `/lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | planned | planned | planned | planned | planned | not yet recorded | likely depends on L5 |
| Physical Science | `3-PS2` Unit 1 | Quiz | Unit 1 Quiz | unit quiz | `gr3-ps2-unit1-quiz.html` | placeholder | `/lesson-plans/gr3-ps2-unit1-quiz.html` | planned | planned | planned | planned | planned | not yet recorded | should follow after lesson sequence is stable |
| Life Science | `3-LS4` standalone | L1 | Bird Beak Buffet | standalone lesson page | `bird-beak-buffet.html` | live complete | `/lesson-plans/bird-beak-buffet.html` | tracked separately | tracked separately | tracked separately | tracked separately | tracked separately | already public artifact | already linked publicly; not part of LS1/PS2 build backlog |

---

## Missing-items matrix

These are scoped items implied by the discovered Grade 3 unit scaffolds but not yet present as real curriculum deliverables.

| Scoped item | Expected because | Status |
|---|---|---|
| Full content for `3-PS2` Unit 1 Lessons 3–6 | lesson filenames already exist | missing from lesson content; TODO placeholders only |
| Full content for `3-PS2` Unit 1 refcards Lessons 2–6 | refcard filenames already exist | missing from content; TODO placeholders only |
| Full content for `3-PS2` Unit 1 quiz | quiz filename already exists | missing from content; TODO placeholder only |
| Modern review/paywall/feedback parity for `3-PS2` Unit 1 Lessons 1–2 | lesson pages exist, but weaker/older shell than LS1 baseline | missing from current lesson implementation |
| Explicit worksheet + parent-answer-key support files for placeholder PS2 lessons | expected by established Grade 3 lesson pattern where appropriate | missing because lesson bodies are still TODOs |
| Public curriculum links/routes for Grade 3 LS1 and PS2 sequence | needed for final public curriculum manifest and route consistency | missing from current public navigation |
| Grade 3 per-lesson directory route parity (`.../index.html`) if desired by site pattern | many stronger LLC lessons use directory routes | missing for current Grade 3 discovered files |
| Additional Grade 3 year-map references beyond discovered LS1 / PS2 / LS4 scope | needed only if an external full Grade 3 map exists | unknown / not discoverable in repo today |

---

## Status matrix by lesson slot

### Current lesson-level status

| Grade 3 slot | Status | Reason |
|---|---|---|
| `3-LS1 Unit 1 L1` | live complete | modern LLC shell, worksheet, answer key, review/paywall hooks |
| `3-LS1 Unit 1 L2` | live complete | modern LLC shell, worksheet, answer key, review/paywall hooks |
| `3-PS2 Unit 1 L1` | draft incomplete | has lesson content but needs modern LLC shell parity |
| `3-PS2 Unit 1 L2` | draft incomplete | has lesson content but needs modern LLC shell parity |
| `3-PS2 Unit 1 L3` | placeholder | TODO stub only |
| `3-PS2 Unit 1 L4` | placeholder | TODO stub only |
| `3-PS2 Unit 1 L5` | placeholder | TODO stub only |
| `3-PS2 Unit 1 L6` | placeholder | TODO stub only |
| `3-PS2 Unit 1 Quiz` | placeholder | TODO stub only |
| `3-LS4 standalone Bird Beak Buffet` | live complete | existing public lesson |

### Supporting-asset status

| Supporting asset | Status | Reason |
|---|---|---|
| `3-PS2 L1 refcard` | draft incomplete | content exists; needs consistency check after lesson modernization |
| `3-PS2 L2 refcard` | placeholder | TODO stub only |
| `3-PS2 L3 refcard` | placeholder | TODO stub only |
| `3-PS2 L4 refcard` | placeholder | TODO stub only |
| `3-PS2 L5 refcard` | placeholder | TODO stub only |
| `3-PS2 L6 refcard` | placeholder | TODO stub only |
| `LS1 L1 template audit` | reference-only | planning artifact |
| `LS1 L2 template audit` | reference-only | planning artifact |

---

## Recommended implementation backlog

Prefer fewer, larger coherent batches.

### Batch 0 — Template baseline and audit lock
Goal:
- use this audit file as the single source of truth for Grade 3 scope
- treat Grade 3 LS1 Lessons 1–2 as the approved target shell

Dependencies:
- none

Outputs:
- this audit file
- no review claims yet

### Batch 1 — Modernize the existing Physical Science foundation
Scope:
- `3-PS2 Unit 1 L1`
- `3-PS2 Unit 1 L2`
- review/refine `3-PS2 L1 refcard`
- build `3-PS2 L2 refcard`

Why this batch first:
- converts existing content-bearing files to the approved Grade 3 standard
- creates the stable shell/content pattern for the rest of the physical science unit

Review workflow for each item in this batch:
- build/update
- Rachel review
- Margaret review
- revise
- repeat up to 3 total review rounds max
- mark ready for human review if unresolved after round 3

### Batch 2 — Build the core magnet lessons together
Scope:
- `3-PS2 Unit 1 L3`
- `3-PS2 Unit 1 L4`
- `3-PS2 L3 refcard`
- `3-PS2 L4 refcard`

Why this batch together:
- shared concept domain
- shared materials and vocabulary base
- avoids one-file thrash and keeps magnetic-force sequencing coherent

Dependencies:
- Batch 1 should establish the final physical-science shell and terminology

Review workflow:
- build both lessons and both refcards together
- Rachel review
- Margaret review
- revise as one coherent batch
- repeat up to 3 total review rounds max
- if still unresolved, hand to human review

### Batch 3 — Build the engineering capstone pair together
Scope:
- `3-PS2 Unit 1 L5`
- `3-PS2 Unit 1 L6`
- `3-PS2 L5 refcard`
- `3-PS2 L6 refcard`

Why this batch together:
- L6 logically depends on the design work in L5
- build/test/improve sequence should be written and reviewed together

Dependencies:
- Batches 1 and 2 complete enough to stabilize force/magnet concepts and unit vocabulary

Review workflow:
- build both lessons + support cards
- Rachel review
- Margaret review
- revise
- repeat up to 3 total review rounds max
- if still unresolved, hand to human review

### Batch 4 — Finish the unit assessment + route/public-manifest prep
Scope:
- `3-PS2 Unit 1 Quiz`
- route/public URL consistency pass for all discovered Grade 3 lessons
- final Grade 3 public URL manifest draft for Serena handoff

Dependencies:
- lesson sequence should be stable first

Review workflow:
- build quiz / route manifest prep
- Rachel review
- Margaret review
- revise
- repeat up to 3 total review rounds max
- if still unresolved, hand to human review

---

## Known issues / caveats to carry into the next iteration

1. **Public navigation lag**
   - `curriculum/index.html` and `index.html` do not yet expose the discovered Grade 3 LS1/PS2 scope.
2. **Route inconsistency**
   - Many stronger LLC lessons use directory-based routes; discovered Grade 3 files currently do not.
3. **Physical Science shell mismatch**
   - Lessons 1–2 have real content but are not yet aligned with the modern Grade 3 shell used by LS1 Lessons 1–2.
4. **Review status is intentionally blank/planned**
   - No Rachel/Margaret review is claimed here because no review artifacts/comments were created in this audit chunk.
5. **Grade 3 full-year completeness is still unknown**
   - This audit captures the full Grade 3 scope that is discoverable in this repo today, not necessarily an external full-year map.

---

## Life Science batch outcome (2026-04-07)

See also: `lesson-plans/gr3-life-science-batch-review.md`

### Outcome
- Re-checked the in-repo Grade 3 Life Science scope during the `grade3-life-science-batch` chunk.
- Confirmed that no additional non-live Grade 3 Life Science lesson pages were discoverable beyond:
  - `gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
  - `gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`
  - the already-public standalone `bird-beak-buffet.html`
- Therefore, iteration 1 of the Life Science batch completed as a **scoped no-op batch** with explicit review artifacts created rather than silent skipping.

### Life Science status update

| Life Science item | Status after batch check | Notes |
|---|---|---|
| `3-LS1 Unit 1 L1` | already live complete baseline | unchanged in this batch |
| `3-LS1 Unit 1 L2` | already live complete baseline | unchanged in this batch |
| `3-LS4 Bird Beak Buffet` | already live complete standalone | tracked separately from LS1 batch |
| additional remaining Grade 3 Life Science lesson pages | none found in repo scope | no new lesson files created in this batch |

### Review-artifact status
- Rachel review artifact: created, status `pending`
- Margaret review artifact: created, status `pending`
- revision rounds 1–3: scaffolded, none started
- human-review escalation: not needed yet for nonexistent remaining in-repo Life Science lesson slots

## Physical Science batch outcome (2026-04-07, iterations 1–2)

See also: `lesson-plans/gr3-physical-science-batch-review.md`

### Batch outcomes
- `gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` was modernized into the approved Grade 3 LLC shell.
- `gr3-ps2-unit1-lesson2-motion-changes-with-force.html` was modernized into the approved Grade 3 LLC shell.
- `gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` was created from placeholder state.
- `gr3-ps2-unit1-lesson4-magnetic-patterns.html` was created from placeholder state.
- `gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` was created from placeholder state.
- `gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` was created from placeholder state.
- `gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html` was standardized to the current PS2 refcard pattern.
- `gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html` was created from placeholder state.
- `gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html` was created from placeholder state.
- `gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html` was created from placeholder state.
- `gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html` was created from placeholder state.
- `gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html` was created from placeholder state.
- `gr3-ps2-unit1-quiz.html` was created from placeholder state.
- Rachel and Margaret review notes now exist in the batch review artifact, and revision round 1 is recorded as complete.

### Updated Physical Science status

| Physical Science item | Status after full chunk | Notes |
|---|---|---|
| `3-PS2 Unit 1 L1` | ready for human review | modern LLC shell + worksheet + parent answer key + review/paywall hooks |
| `3-PS2 Unit 1 L2` | ready for human review | modern LLC shell + worksheet + parent answer key + review/paywall hooks |
| `3-PS2 Unit 1 L3` | ready for human review | created from placeholder |
| `3-PS2 Unit 1 L4` | ready for human review | created from placeholder |
| `3-PS2 Unit 1 L5` | ready for human review | created from placeholder |
| `3-PS2 Unit 1 L6` | ready for human review | created from placeholder |
| `3-PS2 L1 refcard` | ready for human review | standardized |
| `3-PS2 L2 refcard` | ready for human review | created from placeholder |
| `3-PS2 L3 refcard` | ready for human review | created from placeholder |
| `3-PS2 L4 refcard` | ready for human review | created from placeholder |
| `3-PS2 L5 refcard` | ready for human review | created from placeholder |
| `3-PS2 L6 refcard` | ready for human review | created from placeholder |
| `3-PS2 Unit 1 Quiz` | ready for human review | created from placeholder |

### Review-artifact status
- Rachel review artifact: created, status `commented`
- Margaret review artifact: created, status `commented`
- revision round 1: `done`
- revision rounds 2–3: available if future review comments require more changes
- human-review readiness: yes for the completed in-repo PS2 scope

## Decision for next chunk

Use this file as the source of truth and move to the final QA / route / shareable-manifest chunk to verify consistency and prepare Serena-facing Grade 3 URLs.

---

## Final Grade 3 QA pass snapshot (2026-04-07, iteration 1 of 2)

This section reconciles the discovered Grade 3 lesson scope into final working statuses for the next live/publish step.

### QA checks used in this pass
- Re-read this audit file together with:
  - `lesson-plans/gr3-implementation-baseline.md`
  - `lesson-plans/gr3-life-science-batch-review.md`
  - `lesson-plans/gr3-physical-science-batch-review.md`
- Re-checked modern lesson-shell markers on Grade 3 lesson pages:
  - `Student Worksheet`
  - `Parent Answer Key`
  - `feedback-layer.js`
  - `llcPaywall`
  - `review=1`
  - `data-document-id`
- Re-checked PS2 refcards for absence of `TODO`
- Re-checked Grade 3 navigation references in:
  - `curriculum/index.html`
  - `index.html`

### Final tracked lesson statuses for the next live step

| Grade 3 lesson in scope | Final status bucket | Public URL / route field | Review artifact basis | QA notes |
|---|---|---|---|---|
| `3-LS1 Unit 1 L1` — What Is a Life Cycle? | live baseline | `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | existing baseline lesson; tracked in Life Science audit notes | modern Grade 3 shell present; not currently linked from Grade 3 navigation |
| `3-LS1 Unit 1 L2` — Different Life Cycles, Same Big Pattern | live baseline | `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | existing baseline lesson; tracked in Life Science audit notes | modern Grade 3 shell present; not currently linked from Grade 3 navigation |
| `3-PS2 Unit 1 L1` — Balanced and Unbalanced Forces | draft ready for human review | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | `lesson-plans/gr3-physical-science-batch-review.md` with Rachel + Margaret notes and revision round 1 complete | worksheet, answer key, feedback layer, paywall, review bypass, and route field all present |
| `3-PS2 Unit 1 L2` — Motion Changes with Force | draft ready for human review | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | `lesson-plans/gr3-physical-science-batch-review.md` with Rachel + Margaret notes and revision round 1 complete | worksheet, answer key, feedback layer, paywall, review bypass, and route field all present |
| `3-PS2 Unit 1 L3` — Magnets Pull Without Touching | draft ready for human review | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | `lesson-plans/gr3-physical-science-batch-review.md` with Rachel + Margaret notes and revision round 1 complete | created from placeholder; modern shell markers present |
| `3-PS2 Unit 1 L4` — Magnetic Patterns | draft ready for human review | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html` | `lesson-plans/gr3-physical-science-batch-review.md` with Rachel + Margaret notes and revision round 1 complete | created from placeholder; modern shell markers present |
| `3-PS2 Unit 1 L5` — Design a Magnetic Game or Tool | draft ready for human review | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | `lesson-plans/gr3-physical-science-batch-review.md` with Rachel + Margaret notes and revision round 1 complete | created from placeholder; modern shell markers present |
| `3-PS2 Unit 1 L6` — Test and Improve Your Force Design | draft ready for human review | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | `lesson-plans/gr3-physical-science-batch-review.md` with Rachel + Margaret notes and revision round 1 complete | created from placeholder; modern shell markers present |
| `3-PS2 Unit 1 Quiz` — Forces & Motion Quiz | draft ready for human review | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-quiz.html` | `lesson-plans/gr3-physical-science-batch-review.md` with Rachel + Margaret notes and revision round 1 complete | real quiz exists with `data-document-id`, feedback layer, lesson-style `llcPaywall`, and `review=1` bypass |
| `3-LS4` standalone — Bird Beak Buffet | live baseline | `https://littlelabcoats.co/lesson-plans/bird-beak-buffet.html` | existing public Grade 3 artifact | currently the only Grade 3 lesson clearly linked from public Grade 3 navigation |

### Supporting-artifact and review completeness summary

| Artifact group | Status | Notes |
|---|---|---|
| `3-PS2` refcards lessons 1–6 | draft ready for human review | all refcard files exist and no `TODO` placeholders remain |
| Life Science review artifact | scoped no-op / honest pending | `lesson-plans/gr3-life-science-batch-review.md` intentionally stays pending because no new LS lesson files were built in that batch |
| Physical Science review artifact | reviewed and revised | Rachel + Margaret notes exist and revision round 1 is recorded in `lesson-plans/gr3-physical-science-batch-review.md` |

### Route and navigation reconciliation
- `curriculum/index.html` and `index.html` still expose only `Bird Beak Buffet` for Grade 3.
- Grade 3 LS1 and PS2 lesson file URLs are now tracked and ready for the next live/publish step, but they are **not** yet wired into Grade 3 public navigation in this pass.
- This pass records intended public URLs only; it does **not** claim that additional Grade 3 lessons were published or surfaced live in navigation.

### Next-step navigation wiring pointers
Use these tracked routes when the publish/navigation step happens later:
- add `3-LS1 Unit 1 Lesson 1` → `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- add `3-LS1 Unit 1 Lesson 2` → `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`
- add `3-PS2 Unit 1 Lessons 1–6` → their corresponding `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson*.html` routes
- add `3-PS2 Unit 1 Quiz` → `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-quiz.html`

### Serena handoff note
- **Already public / baseline:** `Bird Beak Buffet`
- **Existing Grade 3 lesson baselines with stable URLs:** `3-LS1 Unit 1 Lessons 1–2`
- **Built and reviewed in-repo, ready for human review before live wiring:** `3-PS2 Unit 1 Lessons 1–6`, refcards 1–6, and the unit quiz
- **Still remaining for the next live step:** public navigation wiring and final publish/live verification

### Current blocked items
- No blocked Grade 3 lesson files in the currently discovered canonical scope.
- Remaining gaps are publish/navigation tasks, not missing lesson content.
