# Grade 3 Curriculum Audit and Scope

Last updated: 2026-04-07

## Purpose

This file is the single tracking artifact for Grade 3 repo inventory, curriculum crosswalk, status classification, and implementation backlog.

It began as the **audit + scope definition** tracker for the Grade 3 buildout pass and now also carries the final in-repo QA reconciliation snapshot for handoff.

Unless a later section explicitly says otherwise, early tables in this file should be read as historical audit snapshots rather than the final current-state status.

**Current-state shortcut:** start with `Repo re-audit snapshot for current thread (2026-04-07, iteration 1 of 2)` below. The later `Stricter rerun inventory + correction snapshot (2026-04-07, iteration 1 of 2)` and `Final Grade 3 QA pass snapshot (2026-04-07, iteration 1 of 2)` sections should now be read as historical earlier-pass snapshots unless they are explicitly reaffirmed by the newer repo re-audit section.

It does **not** claim that Rachel review, Margaret review, or Remarq inline review has happened unless a later batch-review section explicitly records those notes.

---

## Repo re-audit snapshot for current thread (2026-04-07, iteration 1 of 2)

This section is the current chunk-level source of truth for the repository re-audit requested in this thread.
It is intentionally narrower and stricter than earlier Grade 3 writeups: it records only what is verifiable from the repo right now, separates repo state from unverified live-site state, and names preview-depth behavior by exact file/path rather than by assumption.

### Exact repo evidence re-checked for this refresh

#### Grade 3 lesson and support files inventoried
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
- `lesson-plans/bird-beak-buffet.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-refcard.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html`

#### Grade 3 repo navigation/catalog surfaces re-checked
- `index.html`
- `curriculum.html`
- `curriculum/index.html`

#### Stronger-scope source search re-checked
- `lesson-plans/science-curriculum-business-plan.html`
- `lesson-plans/free-lesson-audit-and-scope.md`
- `lesson-plans/gr3-life-science-batch-review.md`
- `lesson-plans/gr3-physical-science-batch-review.md`
- repo-wide filename/content search for Grade 3 curriculum-map / scope / manifest terms

#### Exact preview-depth code paths re-checked
- inline paywall logic inside:
  - `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
  - `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`
  - `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
  - `lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html`
  - `lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`
  - `lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html`
  - `lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`
  - `lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`
- quiz paywall logic inside:
  - `lesson-plans/gr3-ps2-unit1-quiz.html`

### Current repo-state findings

#### 1. Grade 3 curriculum currently discoverable in the repo
The currently discoverable Grade 3 curriculum and Grade 3-adjacent inventory in this repo is:
- canonical lesson scope:
  - `3-LS1 Unit 1` — Lessons 1–2
  - `3-PS2 Unit 1` — Lessons 1–6 plus unit quiz
  - `3-LS4` standalone — `Bird Beak Buffet`
- canonical support-asset scope:
  - `3-PS2` refcards for Lessons 1–6
- Grade 3-adjacent but out-of-canonical-map scope:
  - `free-gr3-egg-drop-kitchen-challenge.html`
  - `free-gr3-egg-drop-kitchen-challenge-refcard.html`
  - `free-gr3-egg-drop-kitchen-challenge-quiz.html`

No additional Grade 3 `3-ESS*`, `3-ETS*`, other `3-LS*`, or other `3-PS*` lesson/unit files were discoverable by repo inventory during this refresh.

#### 1a. Result of the stronger-scope source search
No stronger in-repo Grade 3 year map was found during this refresh.

What was found:
- `lesson-plans/science-curriculum-business-plan.html` contains a detailed Kindergarten year map, but this refresh did not find a comparable Grade 3 year map section in that file
- `lesson-plans/gr3-life-science-batch-review.md` explicitly says additional Grade 3 Life Science expansion would require an external Grade 3 curriculum map if one exists
- `lesson-plans/gr3-physical-science-batch-review.md` confirms completion inside the currently discovered PS2 scope, not a broader full-year Grade 3 map
- `lesson-plans/free-lesson-audit-and-scope.md` tracks the Grade 3 freebie, but does not redefine the canonical Grade 3 curriculum map

Current audit consequence:
- this chunk can be exact about the **discoverable repo scope**
- it cannot honestly claim a complete intended full-year Grade 3 domain map beyond that discoverable repo scope
- external-scope confirmation remains the blocker for any claim that more Grade 3 domains/units are definitively intended right now

#### 2. Current repo navigation/catalog state
The repo-side Grade 3 discovery surfaces already contain more than the earlier historical audit text said.

Verified current repo links:
- `index.html`
  - links `3-LS1` Lessons 1–2
  - links `3-PS2` Lessons 1–6 + quiz
  - links `3-LS4 Bird Beak Buffet`
  - also links the Grade 3 freebie `free-gr3-egg-drop-kitchen-challenge.html`
- `curriculum.html`
  - links `3-LS1` Lessons 1–2
  - links `3-PS2` Lessons 1–6 + quiz
  - links `3-LS4 Bird Beak Buffet`
  - also links the Grade 3 freebie `free-gr3-egg-drop-kitchen-challenge.html`
- `curriculum/index.html`
  - links `3-LS1` Lessons 1–2
  - links `3-PS2` Lessons 1–6 + quiz
  - links `3-LS4 Bird Beak Buffet`
  - also links the Grade 3 freebie `free-gr3-egg-drop-kitchen-challenge.html`

Important boundary:
- this refresh confirms **repo-side wiring only**
- it does **not** claim the public domain currently reflects those repo links
- live publish verification remains a later chunk

#### 3. Categorized gap list for the current discovered repo scope

##### Existing-complete in repo
- `3-LS1 Unit 1 Lesson 1` — complete lesson shell present
- `3-LS1 Unit 1 Lesson 2` — complete lesson shell present
- `3-PS2 Unit 1 Lessons 1–6` — complete lesson shells present
- `3-PS2 Unit 1 Quiz` — present with review/paywall shell
- `3-PS2` refcards for Lessons 1–6 — present in repo
- repo navigation references for LS1, PS2, LS4, and the Grade 3 freebie — present in `index.html`, `curriculum.html`, and `curriculum/index.html`

##### Existing-partial or still needing later work
- live publish verification for the repo-wired Grade 3 navigation/catalog state — not yet verified on the public domain
- final canonical public-URL manifest for the Grade 3 curriculum set — tracked separately and still publish-state-sensitive
- `Bird Beak Buffet` parity with the newer Grade 3 lesson shell — not treated as broken in this chunk, but still a separate modernization decision if strict shell parity is required later
- Grade 3 preview-depth acceptance confirmation is now evidence-backed for the audited lesson set, but the code remains duplicated inline per lesson file rather than centralized in one reusable component

##### Missing from the discoverable repo map
- additional Grade 3 Life Science units beyond `3-LS1` and `3-LS4`
- Grade 3 Earth / Space Science units
- Grade 3 Engineering / ETS unit pages
- a full year-at-a-glance Grade 3 curriculum map comparable to stronger lower-grade curriculum maps

##### Blocked / unknown rather than honestly missing-in-repo files
- any claim that Grade 3 should include more domains/units than the discovered `LS1`, `LS4`, and `PS2` set is currently blocked by lack of an in-repo Grade 3 year map or other authoritative scope source
- any claim that the repo-wired Grade 3 navigation is already live is blocked until later publish verification happens against the public domain
- any claim that specific `3-ESS*` or `3-ETS*` lesson slots are missing files rather than simply absent-from-known-scope is blocked until an authoritative Grade 3 map names those slots

### Preview-depth audit for the Grade 3 lesson set

#### Current lesson-preview behavior verified from exact files
The following Grade 3 lesson pages all contain inline paywall logic that locks from the first `h2` matching one of these keywords:
- `materials`
- `gather before you start`
- `what you need`

Verified lesson files using that lock boundary:
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html`
- `lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`
- `lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html`
- `lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`
- `lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`

Practical implication:
- these lesson pages preview through the top conceptual sections before `Materials`
- this is deeper than the older LLC pattern that locked at the first non-goal section after `Learning Objective` / `Learning Goal`
- for the audited Grade 3 lesson set, the current preview boundary is **not** the tiny top-section behavior; it is already the deeper `lock-from-Materials` behavior

#### Grade 3 quiz preview behavior
- `lesson-plans/gr3-ps2-unit1-quiz.html` has quiz preview/paywall behavior present
- during this refresh, no matching `lockKeywords` block was found in the same lesson-style form as the lesson pages
- that is a separate quiz-preview implementation detail, not evidence that the lesson pages themselves are still shallow

#### Grade 3-adjacent freebie preview behavior
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html` is a free-access artifact with the feedback layer present and the paywall lock intentionally removed
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html` is a free-access companion artifact with the feedback layer present and no lesson-style paywall-lock block found
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-refcard.html` is a free companion artifact and no lesson-style paywall-lock block was found in this refresh
- because these are free-access artifacts, they are **not** part of the shallow-preview problem class for this Grade 3 chunk

#### Preview-depth conclusion for this chunk
- no currently discovered canonical Grade 3 lesson page was found using the older shallow `learning objective / learning goal / big idea` lock boundary
- the exact current Grade 3 lesson files named above are already using the deeper `materials / gather before you start / what you need` boundary
- the Grade 3-adjacent freebie trio is free-access rather than shallow-preview locked
- if preview-depth fixes are still required later, they should target:
  - new Grade 3 lesson files created after this audit
  - any non-Grade-3 legacy/template pages elsewhere in the repo still using the older shallow boundary
  - the Grade 3 quiz only if later product requirements require lesson-style depth semantics there too

### Implementation queue from this refreshed audit

Use coherent batches; do not re-open already complete lesson shells without a concrete reason.

#### Batch A — Grade 3 scope-expansion audit before new curriculum creation
Goal:
- determine whether there is an authoritative Grade 3 year map outside the currently discoverable repo scope

Why this is first:
- the repo currently proves `LS1`, `LS4`, and `PS2`
- it does **not** prove the full intended year across all domains
- before creating additional Grade 3 units, the next iteration should search for or request an authoritative source that says what else Grade 3 is supposed to include

#### Batch B — If authoritative scope exists, build the missing Grade 3 domains/units in coherent domain batches
Potential follow-on batches only after scope expansion is real:
- additional Life Science units together
- Earth / Space together
- Engineering / ETS together

#### Batch C — Preview-depth parity guardrail for future/new Grade 3 pages
Goal:
- when creating any new Grade 3 lesson pages, copy the current deeper `lock-from-Materials` preview boundary rather than the older shallow goal-based lock pattern

Concrete rule:
- new Grade 3 lesson pages should match the exact deeper-preview behavior verified in the eight canonical lesson files above

#### Batch D — Review-loop execution for any genuinely new or newly expanded Grade 3 scope
Goal:
- only after new curriculum scope is proven and files exist, run the full Rachel → Margaret → revise loop for those items, up to three total rounds max

#### Batch E — Publish/readiness verification and manifest reconciliation
Goal:
- verify live/public parity for repo-wired Grade 3 navigation
- finalize the Grade 3 public-URL manifest against actual publish state rather than repo-only assumptions

### Current chunk decision
For the repo-discoverable Grade 3 scope audited in this refresh:
- canonical Grade 3 lesson files are **not** currently partial in the repo
- every remaining item inside the **discoverable repo scope** is now assigned to a coherent later batch: scope-expansion audit, potential new-domain build batches, preview-depth guardrail, review loops for newly created scope, and publish/manifest verification
- the biggest unresolved item is not lesson incompleteness inside discovered files; it is **scope ambiguity beyond the discovered repo map**
- the main preview-depth risk for the next chunk is regression on newly created Grade 3 pages, not the currently audited canonical Grade 3 lesson files
- therefore this chunk should be read as complete for the discoverable repo scope, with external-scope confirmation recorded as the blocker to any stronger full-year Grade 3 completeness claim

---

## Stricter rerun inventory + correction snapshot (2026-04-07, iteration 1 of 2)

This section is the current source of truth for the stricter Grade 3 reviewer-rerun planning pass.
It supersedes any weaker earlier wording elsewhere in this file that could be read as if the current stricter reviewer requirement were already complete.

### Verified Grade 3 review set for the stricter rerun

The rerun scope is the currently live/discovered Grade 3 lesson set requested for review:
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html`
- `lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`
- `lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html`
- `lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`
- `lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`
- `lesson-plans/gr3-ps2-unit1-quiz.html`

### Quiz inclusion decision

`lesson-plans/gr3-ps2-unit1-quiz.html` is **included** in the stricter review set.

Rationale:
- the file exists in the repo as a real Grade 3 PS2 unit artifact
- the requested user scope explicitly includes it if it is part of the review set
- earlier Grade 3 tracking artifacts already group it with the PS2 lesson sequence
- it affects curriculum completeness and should be reviewed alongside PS2 Lessons 1–6 rather than treated as a separate later-only artifact

### Existing Grade 3 review/status artifacts that must be treated carefully

#### Core tracking artifacts
- `lesson-plans/gr3-curriculum-audit-and-scope.md`
- `lesson-plans/gr3-life-science-batch-review.md`
- `lesson-plans/gr3-physical-science-batch-review.md`
- `lesson-plans/gr3-shareable-manifest.md`

#### Historical-but-weaker claims that must not be treated as final stricter-review completion
- `lesson-plans/gr3-physical-science-batch-review.md`
  - contains historical statuses like `Status: commented`, `Revision round 1: done`, and `Ready-for-human-review`
  - these are now treated as earlier-pass PS2 build/review markers, **not** proof that the stricter full Grade 3 rerun is complete
- `lesson-plans/gr3-curriculum-audit-and-scope.md`
  - the older `Final Grade 3 QA pass snapshot` section contains wording such as `draft ready for human review` and cites the earlier PS2 review artifact as the basis
  - for the stricter rerun, that wording must be read as historical only until new rerun comments + revisions are recorded
- `lesson-plans/gr3-shareable-manifest.md`
  - tracks URLs and earlier review-readiness language for PS2
  - should not be used as proof that the stricter reviewer pass has been completed
- `lesson-plans/gr3-life-science-batch-review.md`
  - honestly remains pending, but still needs explicit LS1 Rachel + Margaret review comments in the stricter rerun

### Public navigation/catalog file map for later wiring

These are the exact repo files that govern Grade 3 discovery and now contain the staged repo-side navigation updates for the Grade 3 LS1 + PS2 set:
- `index.html`
  - Grade 3 landing content now stages LS1 Lessons 1–2, PS2 Lessons 1–6 + quiz, and the existing `Bird Beak Buffet` standalone lesson
- `curriculum.html`
  - Grade 3 curriculum library section now stages LS1, PS2, and `Bird Beak Buffet` in the unit-card pattern
- `curriculum/index.html`
  - mirrors the curriculum-library Grade 3 section and now stages the same LS1 + PS2 + LS4 discovery set

Current staged-not-live summary:
- Grade 3 LS1 Lessons 1–2 are now wired in repo navigation/catalog files
- Grade 3 PS2 Lessons 1–6 are now wired in repo navigation/catalog files
- Grade 3 PS2 Unit 1 Quiz is now wired in repo navigation/catalog files
- these changes are prepared for the next push/publish step, but they are **not yet claimed as live on the public domain**

### Review-plan note for the stricter rerun

Use two review batches for execution, while preserving explicit comment targets inside each artifact:
1. `Grade 3 LS1 batch`
   - covers LS1 Lesson 1 and LS1 Lesson 2
   - reviewer comments may be recorded per lesson or as a batch only if each comment clearly names the affected lesson
2. `Grade 3 PS2 batch`
   - covers PS2 Lessons 1–6 plus `gr3-ps2-unit1-quiz.html`
   - reviewer comments may be grouped by sub-batch (`L1–L2`, `L3–L4`, `L5–L6`, `Quiz`) or by lesson, but every comment must still map to a concrete file target

Minimum acceptance for the next chunk:
- both Rachel and Margaret must have explicit round-1 comments recorded for both LS1 and PS2 scope
- resulting file revisions must be logged as round-1 actions
- no artifact should claim stricter-review completion until those comments and revisions are actually present

### Stricter rerun review-artifact status update

Current state after round-1 review + revision work:
- `lesson-plans/gr3-life-science-batch-review.md`
  - Rachel round-1 comments: `recorded`
  - Margaret round-1 comments: `recorded`
  - revision round 1: `revised after round 1 — no round 2 required right now`
- `lesson-plans/gr3-physical-science-batch-review.md`
  - Rachel stricter round-1 comments: `recorded`
  - Margaret stricter round-1 comments: `recorded`
  - stricter rerun revision round 1: `revised after round 1 — no round 2 required right now`

This means the stricter Grade 3 rerun now has explicit round-1 review comments captured for both LS1 and PS2 scope, and the lesson files have been revised in response. Historical earlier-pass sections elsewhere in the repo should still be read as historical only.

### Navigation/readiness staging snapshot

Current pre-publish readiness state:
- reviewer round 1: complete for both Rachel and Margaret across LS1 + PS2 scope
- round-1 revisions: applied in lesson/quiz files and recorded in the review artifacts
- round 2: not required right now; reopen only if a human reviewer wants additional polish
- repo navigation/catalog wiring: staged in `index.html`, `curriculum.html`, and `curriculum/index.html`
- public/live publish state: **not yet claimed** in this repo pass

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
3. **Grade 3 Physical Science Unit 1 now has a full stricter-round-1-reviewed lesson + quiz set in repo.**
   - Lessons 1–6 have concrete content
   - the quiz has concrete content
   - refcards for lessons 1–6 are present in repo
   - stricter Rachel + Margaret round-1 comments and revisions are recorded in the review artifacts
4. **Repo navigation now stages the full Grade 3 LS1 + PS2 scope, but publish is still pending.**
   - `index.html`, `curriculum.html`, and `curriculum/index.html` now stage the Grade 3 LS1 + PS2 listings alongside `Bird Beak Buffet`
   - this repo pass does **not** claim that the public domain has already been updated

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
| `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | lesson page | `/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | round-1 reviewed + revised baseline | modern LLC shell; worksheet + answer key + feedback/paywall |
| `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | lesson page | `/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | round-1 reviewed + revised baseline | modern LLC shell; worksheet + answer key + feedback/paywall |
| `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | lesson page | `/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | round-1 reviewed + revised | modern LLC shell parity improved; evidence prompts strengthened |
| `lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | lesson page | `/lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | round-1 reviewed + revised | modern LLC shell parity improved; trial-comparison structure strengthened |
| `lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | lesson page | `/lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | round-1 reviewed + revised | mixed-object guidance added; no longer a placeholder |
| `lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html` | lesson page | `/lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html` | round-1 reviewed + revised | mixed-results framing added; no longer a placeholder |
| `lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | lesson page | `/lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | round-1 reviewed + revised | success-criteria and constraint language added |
| `lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | lesson page | `/lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | round-1 reviewed + revised | version-comparison and proof prompts added |

### B. Grade 3 refcards and quiz artifacts

| Artifact | Type | Route candidate | Current status | Notes |
|---|---|---|---|---|
| `lesson-plans/gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html` | refcard | `/lesson-plans/gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html` | present in repo | supporting refcard exists |
| `lesson-plans/gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html` | refcard | `/lesson-plans/gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html` | present in repo | supporting refcard exists |
| `lesson-plans/gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html` | refcard | `/lesson-plans/gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html` | present in repo | supporting refcard exists |
| `lesson-plans/gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html` | refcard | `/lesson-plans/gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html` | present in repo | supporting refcard exists |
| `lesson-plans/gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html` | refcard | `/lesson-plans/gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html` | present in repo | supporting refcard exists |
| `lesson-plans/gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html` | refcard | `/lesson-plans/gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html` | present in repo | supporting refcard exists |
| `lesson-plans/gr3-ps2-unit1-quiz.html` | unit quiz | `/lesson-plans/gr3-ps2-unit1-quiz.html` | round-1 reviewed + revised | quiz shell updated with short response, parent notes, and answer key |

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
| `gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | yes | yes | yes | yes | revised | worksheet + answer key + evidence prompts + review/paywall parity present |
| `gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | yes | yes | yes | yes | revised | worksheet + answer key + structured trial comparison + review/paywall parity present |
| `gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | yes | yes | yes | yes | revised | no longer placeholder; mixed-object guidance present |
| `gr3-ps2-unit1-lesson4-magnetic-patterns.html` | yes | yes | yes | yes | revised | no longer placeholder; magnetic-pattern evidence framing present |
| `gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | yes | yes | yes | yes | revised | no longer placeholder; success criterion + constraint present |
| `gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | yes | yes | yes | yes | revised | no longer placeholder; version-comparison prompt present |
| `gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html` | n/a | n/a | n/a | n/a | present | content-bearing refcard |
| `gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html` | n/a | n/a | n/a | n/a | present | supporting refcard exists |
| `gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html` | n/a | n/a | n/a | n/a | present | supporting refcard exists |
| `gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html` | n/a | n/a | n/a | n/a | present | supporting refcard exists |
| `gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html` | n/a | n/a | n/a | n/a | present | supporting refcard exists |
| `gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html` | n/a | n/a | n/a | n/a | present | supporting refcard exists |
| `gr3-ps2-unit1-quiz.html` | n/a | n/a | yes | yes | revised | quiz shell now includes review/paywall support and parent-facing answer guidance |
| `bird-beak-buffet.html` | not audited in this chunk | not audited in this chunk | not audited in this chunk | not audited in this chunk | public-adjacent baseline | tracked as existing public Grade 3 artifact, not part of LS1/PS2 modernization scope |
| `free-gr3-egg-drop-kitchen-challenge.html` | not audited in this chunk | not audited in this chunk | not audited in this chunk | not audited in this chunk | public-adjacent freebie | tracked for scope hygiene only |

### G. Current public URLs vs intended discovered Grade 3 routes

| Grade 3 artifact | Currently linked publicly from Grade 3 navigation? | Current known public URL candidate | Intended/discovered route field | Notes |
|---|---|---|---|---|
| `Bird Beak Buffet` | yes | `/lesson-plans/bird-beak-buffet.html` | `/lesson-plans/bird-beak-buffet.html` | existing Grade 3 standalone lesson remains staged in navigation |
| `3-LS1 Unit 1 L1` | staged in repo | `/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | `/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | wired in repo navigation; not yet claimed live on public domain |
| `3-LS1 Unit 1 L2` | staged in repo | `/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | `/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | wired in repo navigation; not yet claimed live on public domain |
| `3-PS2 Unit 1 L1` | staged in repo | `/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | `/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | wired in repo navigation; round-1 revisions applied |
| `3-PS2 Unit 1 L2` | staged in repo | `/lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | `/lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | wired in repo navigation; round-1 revisions applied |
| `3-PS2 Unit 1 L3` | staged in repo | `/lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | `/lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | wired in repo navigation; no longer placeholder |
| `3-PS2 Unit 1 L4` | staged in repo | `/lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html` | `/lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html` | wired in repo navigation; no longer placeholder |
| `3-PS2 Unit 1 L5` | staged in repo | `/lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | `/lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | wired in repo navigation; no longer placeholder |
| `3-PS2 Unit 1 L6` | staged in repo | `/lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | `/lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | wired in repo navigation; round-1 revisions applied |
| `3-PS2 Unit 1 Quiz` | staged in repo | `/lesson-plans/gr3-ps2-unit1-quiz.html` | `/lesson-plans/gr3-ps2-unit1-quiz.html` | wired in repo navigation; quiz shell revised from round-1 feedback |

---

## Detailed completion snapshot for `gr3-ps2-unit1-*`

### Lesson pages

#### `gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
Current classification: `round-1 reviewed + revised`

Current tracked state:
- modernized into the current Grade 3 LLC shell
- includes worksheet, parent answer key, review hooks, and paywall support
- strengthened with clearer trial-comparison evidence prompts during stricter round 1

#### `gr3-ps2-unit1-lesson2-motion-changes-with-force.html`
Current classification: `round-1 reviewed + revised`

Current tracked state:
- aligned to the established Grade 3 shell
- includes worksheet, parent answer key, review hooks, and paywall support
- strengthened with clearer trial-selection and evidence prompts during stricter round 1

#### `gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`
Current classification: `round-1 reviewed + revised`

Current tracked state:
- no longer a placeholder
- includes worksheet, parent answer key, review hooks, and paywall support
- strengthened with mixed-object guidance during stricter round 1

#### `gr3-ps2-unit1-lesson4-magnetic-patterns.html`
Current classification: `round-1 reviewed + revised`

Current tracked state:
- no longer a placeholder
- includes worksheet, parent answer key, review hooks, and paywall support
- strengthened with mixed-results interpretation guidance during stricter round 1

#### `gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`
Current classification: `round-1 reviewed + revised`

Current tracked state:
- no longer a placeholder
- includes worksheet, parent answer key, review hooks, and paywall support
- strengthened with explicit success-criterion and constraint language during stricter round 1

#### `gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`
Current classification: `round-1 reviewed + revised`

Current tracked state:
- no longer a placeholder
- includes worksheet, parent answer key, review hooks, and paywall support
- strengthened with version-comparison and proof prompts during stricter round 1

### Supporting artifacts

#### `gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html`
Current classification: `present in repo`

Current tracked state:
- supporting refcard exists

#### Refcards for Lessons 2–6
Current classification: `present in repo`

Current tracked state:
- supporting refcards exist for each lesson in the unit

#### `gr3-ps2-unit1-quiz.html`
Current classification: `round-1 reviewed + revised`

Current tracked state:
- quiz shell is present and no longer placeholder-only
- includes short response, parent notes, answer key support, and review/paywall compatibility

---

## Canonical Grade 3 curriculum crosswalk

This crosswalk tracks **all currently discoverable Grade 3 curriculum slots** in the repo and their current post-round-1 state.

### Status legend
- `round-1 reviewed + revised baseline` = baseline lesson with stricter round-1 review captured and revisions applied
- `round-1 reviewed + revised` = stricter round-1 review captured and revisions applied
- `live complete` = existing public/baseline artifact outside the stricter LS1/PS2 rerun scope
- `present in repo` = supporting artifact exists in the repo and is not being represented here as a separate live/public readiness claim
- `reference-only` = planning/template guidance, not student-facing curriculum

### Review workflow legend
For Grade 3 LS1 + PS2 scope in this pass, the tracked state is:
- Rachel review: recorded
- Margaret review: recorded
- Rev 1: applied
- Rev 2 / Rev 3: not needed right now unless a human requests another pass

| Domain | Unit / Standard | Lesson slot | Lesson title / artifact | Expected outputs | Current repo artifact(s) | Status | Route/public URL field | Rachel review | Margaret review | Rev 1 | Rev 2 | Rev 3 | Ready for human review | Dependencies / notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Life Science | `3-LS1` Unit 1 | L1 | What Is a Life Cycle? | lesson page + student worksheet + parent answer key + review/paywall hooks | `gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | round-1 reviewed + revised baseline | `/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | recorded | recorded | applied | not needed right now | not needed right now | yes | baseline template with clearer evidence/model prompts |
| Life Science | `3-LS1` Unit 1 | L2 | Different Life Cycles, Same Big Pattern | lesson page + student worksheet + parent answer key + review/paywall hooks | `gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | round-1 reviewed + revised baseline | `/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | recorded | recorded | applied | not needed right now | not needed right now | yes | baseline template with comparison/application tightening |
| Physical Science | `3-PS2` Unit 1 | L1 | Balanced and Unbalanced Forces | lesson page + student worksheet + parent answer key + route + review/paywall hooks + refcard coverage | `gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`, `gr3-ps2-unit1-refcard-lesson1-balanced-and-unbalanced-forces.html` | round-1 reviewed + revised | `/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | recorded | recorded | applied | not needed right now | not needed right now | yes | trial-comparison evidence prompts added |
| Physical Science | `3-PS2` Unit 1 | L2 | Motion Changes with Force | lesson page + student worksheet + parent answer key + route + review/paywall hooks + refcard coverage | `gr3-ps2-unit1-lesson2-motion-changes-with-force.html`, `gr3-ps2-unit1-refcard-lesson2-motion-changes-with-force.html` | round-1 reviewed + revised | `/lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | recorded | recorded | applied | not needed right now | not needed right now | yes | trial-selection and evidence prompts added |
| Physical Science | `3-PS2` Unit 1 | L3 | Magnets Pull Without Touching | lesson page + student worksheet + parent answer key + route + review/paywall hooks + refcard coverage | `gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`, `gr3-ps2-unit1-refcard-lesson3-magnets-pull-without-touching.html` | round-1 reviewed + revised | `/lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | recorded | recorded | applied | not needed right now | not needed right now | yes | mixed-object guidance clarified |
| Physical Science | `3-PS2` Unit 1 | L4 | Magnetic Patterns | lesson page + student worksheet + parent answer key + route + review/paywall hooks + refcard coverage | `gr3-ps2-unit1-lesson4-magnetic-patterns.html`, `gr3-ps2-unit1-refcard-lesson4-magnetic-patterns.html` | round-1 reviewed + revised | `/lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html` | recorded | recorded | applied | not needed right now | not needed right now | yes | mixed-results interpretation clarified |
| Physical Science | `3-PS2` Unit 1 | L5 | Design a Magnetic Game or Tool | lesson page + student worksheet + parent answer key + route + review/paywall hooks + refcard coverage | `gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`, `gr3-ps2-unit1-refcard-lesson5-design-a-magnetic-game-or-tool.html` | round-1 reviewed + revised | `/lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | recorded | recorded | applied | not needed right now | not needed right now | yes | success criterion + constraint language added |
| Physical Science | `3-PS2` Unit 1 | L6 | Test and Improve Your Force Design | lesson page + student worksheet + parent answer key + route + review/paywall hooks + refcard coverage | `gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`, `gr3-ps2-unit1-refcard-lesson6-test-and-improve-your-force-design.html` | round-1 reviewed + revised | `/lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | recorded | recorded | applied | not needed right now | not needed right now | yes | version-1 vs version-2 proof prompt added |
| Physical Science | `3-PS2` Unit 1 | Quiz | Unit 1 Quiz | unit quiz | `gr3-ps2-unit1-quiz.html` | round-1 reviewed + revised | `/lesson-plans/gr3-ps2-unit1-quiz.html` | recorded | recorded | applied | not needed right now | not needed right now | yes | quiz shell updated with short response + parent notes |
| Life Science | `3-LS4` standalone | L1 | Bird Beak Buffet | standalone lesson page | `bird-beak-buffet.html` | live complete | `/lesson-plans/bird-beak-buffet.html` | tracked separately | tracked separately | tracked separately | tracked separately | tracked separately | already public artifact | already linked publicly; not part of LS1/PS2 build backlog |

---

## Remaining pre-publish items matrix

These are the scoped next-step items that still remain after the stricter round-1 rerun and repo-side navigation staging.

| Scoped item | Expected because | Status |
|---|---|---|
| Push staged Grade 3 navigation/catalog changes | repo navigation is ready but this pass does not publish | pending later publish step |
| Verify public domain shows the staged Grade 3 LS1 + PS2 listings after publish | required to confirm repo-to-live parity | pending later publish verification |
| Grade 3 per-lesson directory route parity (`.../index.html`) if desired by site pattern | some LLC lessons use directory routes | optional follow-up; not required for this chunk |
| Additional Grade 3 year-map references beyond discovered LS1 / PS2 / LS4 scope | needed only if an external full Grade 3 map exists | unknown / not discoverable in repo today |

---

## Status matrix by lesson slot

### Current lesson-level status

| Grade 3 slot | Status | Reason |
|---|---|---|
| `3-LS1 Unit 1 L1` | round-1 reviewed + revised baseline | modern LLC shell, worksheet, answer key, review/paywall hooks, and review revisions present |
| `3-LS1 Unit 1 L2` | round-1 reviewed + revised baseline | modern LLC shell, worksheet, answer key, review/paywall hooks, and review revisions present |
| `3-PS2 Unit 1 L1` | round-1 reviewed + revised | evidence prompts and LLC shell parity improved |
| `3-PS2 Unit 1 L2` | round-1 reviewed + revised | trial-selection prompts and LLC shell parity improved |
| `3-PS2 Unit 1 L3` | round-1 reviewed + revised | lesson exists with mixed-object guidance and full shell |
| `3-PS2 Unit 1 L4` | round-1 reviewed + revised | lesson exists with mixed-results guidance and full shell |
| `3-PS2 Unit 1 L5` | round-1 reviewed + revised | lesson exists with success-criterion and constraint guidance |
| `3-PS2 Unit 1 L6` | round-1 reviewed + revised | lesson exists with version-comparison/proof guidance |
| `3-PS2 Unit 1 Quiz` | round-1 reviewed + revised | quiz exists with updated shell and parent-facing support |
| `3-LS4 standalone Bird Beak Buffet` | live complete | existing public lesson |

### Supporting-asset status

| Supporting asset | Status | Reason |
|---|---|---|
| `3-PS2` refcards lessons 1–6 | present in repo | all supporting refcards exist |
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
- Rachel and Margaret review notes now exist in the batch review artifact, and revision round 1 is recorded as complete for that earlier PS2 pass.

### Updated Physical Science status

| Physical Science item | Current stricter-rerun status | Notes |
|---|---|---|
| `3-PS2 Unit 1 L1` | round-1 reviewed + revised | modern LLC shell + worksheet + parent answer key + review/paywall hooks |
| `3-PS2 Unit 1 L2` | round-1 reviewed + revised | modern LLC shell + worksheet + parent answer key + review/paywall hooks |
| `3-PS2 Unit 1 L3` | round-1 reviewed + revised | created from placeholder earlier, then revised in stricter round 1 |
| `3-PS2 Unit 1 L4` | round-1 reviewed + revised | created from placeholder earlier, then revised in stricter round 1 |
| `3-PS2 Unit 1 L5` | round-1 reviewed + revised | created from placeholder earlier, then revised in stricter round 1 |
| `3-PS2 Unit 1 L6` | round-1 reviewed + revised | created from placeholder earlier, then revised in stricter round 1 |
| `3-PS2 L1 refcard` | present in repo | standardized |
| `3-PS2 L2 refcard` | present in repo | supporting refcard exists |
| `3-PS2 L3 refcard` | present in repo | supporting refcard exists |
| `3-PS2 L4 refcard` | present in repo | supporting refcard exists |
| `3-PS2 L5 refcard` | present in repo | supporting refcard exists |
| `3-PS2 L6 refcard` | present in repo | supporting refcard exists |
| `3-PS2 Unit 1 Quiz` | round-1 reviewed + revised | updated quiz shell with short response + parent notes |

### Review-artifact status
- Rachel review artifact: recorded in `lesson-plans/gr3-physical-science-batch-review.md`
- Margaret review artifact: recorded in `lesson-plans/gr3-physical-science-batch-review.md`
- revision round 1: applied and logged in the PS2 review artifact
- revision rounds 2–3: not required right now; reopen only if a human reviewer wants another pass
- stricter-rerun readiness: complete for round 1 across the full requested PS2 scope

## Decision for next chunk

Use this file as the source of truth for the staged pre-publish Grade 3 state: stricter round 1 is complete, revisions are applied, and navigation is staged in repo for a later publish/verification step.

---

## Final Grade 3 QA pass snapshot (2026-04-07, iteration 1 of 2)

Historical note: this section reflects the earlier in-repo QA/review-readiness snapshot before the stricter reviewer-rerun requirement was imposed. Read it together with `Stricter rerun inventory + correction snapshot (2026-04-07, iteration 1 of 2)` above.

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
| `3-LS1 Unit 1 L1` — What Is a Life Cycle? | round-1 reviewed + revised baseline | `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` | stricter LS1 batch review artifact now records Rachel + Margaret comments and round-1 revisions | staged in repo Grade 3 navigation; not yet claimed live |
| `3-LS1 Unit 1 L2` — Different Life Cycles, Same Big Pattern | round-1 reviewed + revised baseline | `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` | stricter LS1 batch review artifact now records Rachel + Margaret comments and round-1 revisions | staged in repo Grade 3 navigation; not yet claimed live |
| `3-PS2 Unit 1 L1` — Balanced and Unbalanced Forces | round-1 reviewed + revised | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` | stricter PS2 batch review artifact now records Rachel + Margaret comments and round-1 revisions | worksheet, answer key, feedback layer, paywall, review bypass, and route field all present |
| `3-PS2 Unit 1 L2` — Motion Changes with Force | round-1 reviewed + revised | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html` | stricter PS2 batch review artifact now records Rachel + Margaret comments and round-1 revisions | worksheet, answer key, feedback layer, paywall, review bypass, and route field all present |
| `3-PS2 Unit 1 L3` — Magnets Pull Without Touching | round-1 reviewed + revised | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` | stricter PS2 batch review artifact now records Rachel + Margaret comments and round-1 revisions | created from placeholder earlier, then revised during stricter round 1 |
| `3-PS2 Unit 1 L4` — Magnetic Patterns | round-1 reviewed + revised | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html` | stricter PS2 batch review artifact now records Rachel + Margaret comments and round-1 revisions | created from placeholder earlier, then revised during stricter round 1 |
| `3-PS2 Unit 1 L5` — Design a Magnetic Game or Tool | round-1 reviewed + revised | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` | stricter PS2 batch review artifact now records Rachel + Margaret comments and round-1 revisions | created from placeholder earlier, then revised during stricter round 1 |
| `3-PS2 Unit 1 L6` — Test and Improve Your Force Design | round-1 reviewed + revised | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` | stricter PS2 batch review artifact now records Rachel + Margaret comments and round-1 revisions | created from placeholder earlier, then revised during stricter round 1 |
| `3-PS2 Unit 1 Quiz` — Forces & Motion Quiz | round-1 reviewed + revised | `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-quiz.html` | stricter PS2 batch review artifact now records Rachel + Margaret comments and round-1 revisions | real quiz exists with `data-document-id`, feedback layer, lesson-style `llcPaywall`, and `review=1` bypass |
| `3-LS4` standalone — Bird Beak Buffet | live baseline | `https://littlelabcoats.co/lesson-plans/bird-beak-buffet.html` | existing public Grade 3 artifact | preserved alongside the newly staged Grade 3 repo navigation set |

### Supporting-artifact and review completeness summary

| Artifact group | Status | Notes |
|---|---|---|
| `3-PS2` refcards lessons 1–6 | present in repo and aligned to the current lesson set | all refcard files exist and no `TODO` placeholders remain |
| Life Science review artifact | stricter round 1 complete | `lesson-plans/gr3-life-science-batch-review.md` records Rachel + Margaret comments and round-1 revision dispositions |
| Physical Science review artifact | stricter round 1 complete | `lesson-plans/gr3-physical-science-batch-review.md` records Rachel + Margaret comments and round-1 revision dispositions |

### Route and navigation reconciliation
- `index.html`, `curriculum.html`, and `curriculum/index.html` now stage the Grade 3 LS1 and PS2 lesson set in repo navigation/catalog surfaces.
- These staged links are prepared for the next live/publish step, but this pass does **not** claim that the public domain has already been updated.
- Repo state now reflects: review round 1 complete, revisions applied, navigation staged, publish still pending.

### Next-step navigation wiring pointers
Use these tracked routes when the publish/navigation step happens later:
- add `3-LS1 Unit 1 Lesson 1` → `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- add `3-LS1 Unit 1 Lesson 2` → `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`
- add `3-PS2 Unit 1 Lessons 1–6` → their corresponding `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson*.html` routes
- add `3-PS2 Unit 1 Quiz` → `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-quiz.html`

### Serena handoff note
- **Already public / baseline:** `Bird Beak Buffet`
- **Existing Grade 3 lesson baselines with stable URLs and stricter round-1 review applied:** `3-LS1 Unit 1 Lessons 1–2`
- **Grade 3 PS2 lesson set with stricter round-1 review applied in repo:** `3-PS2 Unit 1 Lessons 1–6`, refcards 1–6, and the unit quiz
- **Still remaining for the next live step:** push/publish the staged navigation and verify the public domain reflects it

### Current blocked items
- No blocked Grade 3 lesson files in the currently discovered canonical scope.
- Remaining gaps are publish/navigation verification tasks only; stricter round-1 review and revision work are already recorded in repo artifacts.
