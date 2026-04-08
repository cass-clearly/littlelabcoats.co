# Grade 4 Life Science Audit and Scope

Last updated: 2026-04-08
Status: authoritative chunk-1 audit for the Grade 4 Life Science live-publish recovery

## Purpose

This file is the source of truth for the blocked Grade 4 Life Science rollout.
It answers four concrete questions before any publish/review/deploy work continues:
- which Grade 4 Life Science assets already exist in the repo
- which exact public URLs are intended to exist for those assets
- which live/discovery surfaces should expose the domain
- which gaps still prevent the package from being truly finished on the public site

This file is intentionally an audit, not a completion claim.
It reflects the current repo state plus spot checks against the live site.

---

## Executive summary

Grade 4 Life Science is no longer a hypothetical scope-only build.
The repo already contains the full core package expected for the domain:
- 12 canonical lesson pages
- 12 matching refcards
- 2 unit quizzes
- a Grade 4 batch review tracker
- a Grade 4 document ID manifest
- a Grade 4 shareable manifest
- Grade 4 entries in the generated lesson directory

However, the public rollout is still blocked.
Current live checks show the canonical Grade 4 lesson and quiz URLs are still returning `404`, while the live curriculum page still shows Grade 4 as "coming soon."
That means the main remaining problem is no longer content creation; it is publish/deploy/listing completion.

---

## Authoritative scope for this run

Treat the following as the required finished-state scope for Grade 4 Life Science:
- domain code: `4-LS1`
- total units: `2`
- lessons per unit: `6`
- total lesson pages: `12`
- total refcards: `12`
- total unit quizzes: `2`
- live public canonical URLs for all lesson/refcard/quiz assets
- explicit real Remarq document IDs wired into the actual files
- Rachel + Margaret review completed on the real public pages
- print-ready public pages
- Grade 4 Life Science exposed on curriculum/discovery/listing surfaces

Primary NGSS anchor for the domain:
- `4-LS1-1` — Construct an argument that plants and animals have internal and external structures that function to support survival, growth, behavior, and reproduction.

---

## Existing repo audit relevant to Grade 4 Life Science

### Current authoritative pattern sources
Use these as the current LLC completion-standard anchors:
- `lesson-plans/gr3-curriculum-audit-and-scope.md`
- `lesson-plans/gr3-implementation-baseline.md`
- `lesson-plans/gr3-life-science-batch-review.md`
- `lesson-plans/gr3-document-id-manifest.md`
- `lesson-plans/gr3-shareable-manifest.md`

These remain the best continuity sources for:
- lesson + refcard + quiz packaging
- review/revision tracking
- document ID manifesting
- live URL verification
- directory/catalog expectations

### Grade 4 implementation support docs already present
Confirmed Grade 4 support docs now exist in repo:
- `lesson-plans/gr4-life-science-audit-and-scope.md`
- `lesson-plans/gr4-implementation-baseline.md`
- `lesson-plans/gr4-life-science-batch-review.md`
- `lesson-plans/gr4-document-id-manifest.md`
- `lesson-plans/gr4-shareable-manifest.md`

### Important interpretation of existing Grade 4-adjacent files
These files are Grade 4-adjacent but not part of the canonical Grade 4 Life Science domain package:
- `lesson-plans/free-gr4-apple-oxidation.html`
- `lesson-plans/free-gr4-apple-oxidation-refcard.html`
- `lesson-plans/free-gr4-apple-oxidation-quiz.html`
- `lesson-plans/gr4-ls1-unit1-l1-food-webs.html`

Interpretation:
- the free apple oxidation trio is a useful Grade 4 quality/pattern anchor, but it is not the Grade 4 Life Science domain package
- `gr4-ls1-unit1-l1-food-webs.html` is a legacy/exploratory Grade 4 artifact and should not be treated as a canonical page in the blocked rollout

---

## Locked Grade 4 Life Science unit map

## Unit 1 — Animal Structures & Survival

Unit code:
- `4-LS1 Unit 1`

Locked lesson list:
1. External Structures for Survival
2. Sensing the World
3. Mouths, Beaks, Teeth, and Getting Food
4. Movement Structures and Finding Safety
5. Structures for Protection and Defense
6. Construct an Argument: How Animal Structures Help Them Live

## Unit 2 — Plant Structures & Reproduction

Unit code:
- `4-LS1 Unit 2`

Locked lesson list:
1. Roots, Stems, and Plant Support Systems
2. Leaves and Making Food
3. Water Transport Inside Plants
4. Flowers, Pollination, and Reproduction
5. Seeds, Fruits, and New Plants
6. Construct an Argument: How Plant Structures Help Plants Live and Reproduce

---

## Canonical public asset inventory

Public URL root:
- `https://littlelabcoats.co/lesson-plans/`

Review URL pattern:
- append `?review=1` to the canonical public asset URL

### Unit 1 lesson pages

| Repo file | Canonical public URL | Review URL |
|---|---|---|
| `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html?review=1` |
| `lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html?review=1` |
| `lesson-plans/gr4-ls1-unit1-lesson3-mouths-beaks-teeth-and-getting-food.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson3-mouths-beaks-teeth-and-getting-food.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson3-mouths-beaks-teeth-and-getting-food.html?review=1` |
| `lesson-plans/gr4-ls1-unit1-lesson4-movement-structures-and-finding-safety.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson4-movement-structures-and-finding-safety.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson4-movement-structures-and-finding-safety.html?review=1` |
| `lesson-plans/gr4-ls1-unit1-lesson5-structures-for-protection-and-defense.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson5-structures-for-protection-and-defense.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson5-structures-for-protection-and-defense.html?review=1` |
| `lesson-plans/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html?review=1` |

### Unit 1 refcards

| Repo file | Canonical public URL | Review URL |
|---|---|---|
| `lesson-plans/gr4-ls1-unit1-refcard-lesson1-external-structures-for-survival.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson1-external-structures-for-survival.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson1-external-structures-for-survival.html?review=1` |
| `lesson-plans/gr4-ls1-unit1-refcard-lesson2-sensing-the-world.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson2-sensing-the-world.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson2-sensing-the-world.html?review=1` |
| `lesson-plans/gr4-ls1-unit1-refcard-lesson3-mouths-beaks-teeth-and-getting-food.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson3-mouths-beaks-teeth-and-getting-food.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson3-mouths-beaks-teeth-and-getting-food.html?review=1` |
| `lesson-plans/gr4-ls1-unit1-refcard-lesson4-movement-structures-and-finding-safety.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson4-movement-structures-and-finding-safety.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson4-movement-structures-and-finding-safety.html?review=1` |
| `lesson-plans/gr4-ls1-unit1-refcard-lesson5-structures-for-protection-and-defense.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson5-structures-for-protection-and-defense.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson5-structures-for-protection-and-defense.html?review=1` |
| `lesson-plans/gr4-ls1-unit1-refcard-lesson6-construct-an-argument-animal-structures.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson6-construct-an-argument-animal-structures.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson6-construct-an-argument-animal-structures.html?review=1` |

### Unit 1 quiz

| Repo file | Canonical public URL | Review URL |
|---|---|---|
| `lesson-plans/gr4-ls1-unit1-quiz.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-quiz.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-quiz.html?review=1` |

### Unit 2 lesson pages

| Repo file | Canonical public URL | Review URL |
|---|---|---|
| `lesson-plans/gr4-ls1-unit2-lesson1-roots-stems-and-plant-support-systems.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson1-roots-stems-and-plant-support-systems.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson1-roots-stems-and-plant-support-systems.html?review=1` |
| `lesson-plans/gr4-ls1-unit2-lesson2-leaves-and-making-food.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson2-leaves-and-making-food.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson2-leaves-and-making-food.html?review=1` |
| `lesson-plans/gr4-ls1-unit2-lesson3-water-transport-inside-plants.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson3-water-transport-inside-plants.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson3-water-transport-inside-plants.html?review=1` |
| `lesson-plans/gr4-ls1-unit2-lesson4-flowers-pollination-and-reproduction.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson4-flowers-pollination-and-reproduction.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson4-flowers-pollination-and-reproduction.html?review=1` |
| `lesson-plans/gr4-ls1-unit2-lesson5-seeds-fruits-and-new-plants.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson5-seeds-fruits-and-new-plants.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson5-seeds-fruits-and-new-plants.html?review=1` |
| `lesson-plans/gr4-ls1-unit2-lesson6-construct-an-argument-plant-structures.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson6-construct-an-argument-plant-structures.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson6-construct-an-argument-plant-structures.html?review=1` |

### Unit 2 refcards

| Repo file | Canonical public URL | Review URL |
|---|---|---|
| `lesson-plans/gr4-ls1-unit2-refcard-lesson1-roots-stems-and-plant-support-systems.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson1-roots-stems-and-plant-support-systems.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson1-roots-stems-and-plant-support-systems.html?review=1` |
| `lesson-plans/gr4-ls1-unit2-refcard-lesson2-leaves-and-making-food.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson2-leaves-and-making-food.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson2-leaves-and-making-food.html?review=1` |
| `lesson-plans/gr4-ls1-unit2-refcard-lesson3-water-transport-inside-plants.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson3-water-transport-inside-plants.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson3-water-transport-inside-plants.html?review=1` |
| `lesson-plans/gr4-ls1-unit2-refcard-lesson4-flowers-pollination-and-reproduction.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson4-flowers-pollination-and-reproduction.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson4-flowers-pollination-and-reproduction.html?review=1` |
| `lesson-plans/gr4-ls1-unit2-refcard-lesson5-seeds-fruits-and-new-plants.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson5-seeds-fruits-and-new-plants.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson5-seeds-fruits-and-new-plants.html?review=1` |
| `lesson-plans/gr4-ls1-unit2-refcard-lesson6-construct-an-argument-plant-structures.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson6-construct-an-argument-plant-structures.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson6-construct-an-argument-plant-structures.html?review=1` |

### Unit 2 quiz

| Repo file | Canonical public URL | Review URL |
|---|---|---|
| `lesson-plans/gr4-ls1-unit2-quiz.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-quiz.html` | `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-quiz.html?review=1` |

---

## Required live directory and discovery surfaces

These surfaces should expose Grade 4 Life Science publicly:
- `https://littlelabcoats.co/curriculum/`
- `https://littlelabcoats.co/curriculum.html`
- `https://littlelabcoats.co/lesson-plans/`
- `https://littlelabcoats.co/`

Current in-repo touchpoints for those surfaces:
- `curriculum.html`
- `curriculum/index.html`
- `lesson-plans/index.html`
- `index.html`
- `lesson-plans/_generated/lesson-index-data.json`
- `scripts/generate-lesson-index-data.py`
- `scripts/render-lesson-index-page.py`

Expected role of each surface:
- `curriculum.html` / `curriculum/index.html`: grade/domain curriculum library exposure for Grade 4 Life Science
- `lesson-plans/index.html`: operational directory with canonical open/review links for lessons
- `index.html`: homepage-level discoverability or summary exposure for Grade 4 availability

---

## Current repo-side listing state

### `lesson-plans/index.html`
Repo state confirms:
- a full `Grade 4 · Life Science` section exists
- all 12 canonical lesson pages are listed there
- both canonical open links and review-mode links are present
- Grade 4 is also represented in the page stats/navigation

### `curriculum.html` and `curriculum/index.html`
Repo state confirms:
- Grade 4 still shows a free apple oxidation sample card
- Grade 4 still shows a `Grade 4 Units Coming Soon` placeholder
- Grade 4 Life Science unit/domain cards are not yet exposed there

### `index.html`
Repo audit confirms:
- this surface still needs explicit inspection/update in later chunks for Grade 4 Life Science discoverability
- no chunk-1 claim is made that homepage Grade 4 Life Science exposure is already finished

---

## Remarq/backend state

### Current repo evidence
`lesson-plans/gr4-document-id-manifest.md` now records explicit real document IDs for:
- all 12 lesson pages
- all 12 refcards
- both quizzes

That means the repo is no longer in a placeholder-ID state.
The current repo evidence supports the conclusion that real backend document IDs have already been created and wired into the files.

### Spot-check result
A repo-wide check of the Grade 4 Life Science asset files shows:
- `body[data-document-id]` is present
- the feedback-layer script `data-document-id` matches the body-level document ID in each checked asset file

### Remaining Remarq work
Still required later:
- verify those IDs work on the actual public URLs after publish
- complete Rachel + Margaret review on the real public pages, not only repo/local files
- record final live review/revision status in the batch review/shareable artifacts

---

## Live-site verification snapshot

Checks run against the public site on 2026-04-08:

### Canonical Grade 4 lesson/package URLs
Observed live results:
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html` → `404`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html` → `404`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-quiz.html` → `404`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson1-roots-stems-and-plant-support-systems.html` → `404`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson6-construct-an-argument-plant-structures.html` → `404`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-quiz.html` → `404`

These representative failures strongly indicate the full canonical Grade 4 package is not yet deployed or otherwise not reachable on the production host.

### Live listing/discovery surfaces
Observed live results:
- `https://littlelabcoats.co/curriculum/` → `200`, but still shows `Grade 4 Units Coming Soon`
- `https://littlelabcoats.co/lesson-plans/` → `200`, and currently exposes the Grade 4 Life Science lesson directory entries

Important repo-vs-live conclusion:
- the lesson directory page is live with Grade 4 entries
- the canonical Grade 4 lesson pages themselves are still 404
- the curriculum library still presents Grade 4 as unfinished

This means the current public state is inconsistent across surfaces.

---

## Concrete gap list blocking full done state

### Gap 1 — canonical lesson/refcard/quiz URLs are not live
Symptoms:
- representative canonical lesson and quiz URLs return `404`

Concrete fix path:
- inspect the production publish/deploy path for `lesson-plans/gr4-ls1-*` assets
- determine why files present in repo and in the generated lesson directory are absent from the deployed static/site output
- redeploy and verify all canonical Grade 4 lesson/refcard/quiz URLs return `200`

### Gap 2 — curriculum library still hides Grade 4 behind coming-soon state
Symptoms:
- both `curriculum.html` and `curriculum/index.html` still show `Grade 4 Units Coming Soon`
- live `https://littlelabcoats.co/curriculum/` still reflects that state

Concrete fix path:
- replace the Grade 4 placeholder block in `curriculum.html` and `curriculum/index.html` with real Grade 4 Life Science unit cards
- deploy those listing updates
- verify the live curriculum page links into the correct canonical lesson/unit pages without 404s

### Gap 3 — homepage/discovery exposure is not yet confirmed complete
Symptoms:
- Grade 4 Life Science homepage discoverability has not yet been confirmed as finished in repo or live state

Concrete fix path:
- inspect `index.html` for Grade 4 curriculum coverage summaries, sample-lesson sections, or grade availability messaging
- add/update Grade 4 Life Science discoverability where needed
- verify the live homepage reflects the shipped Grade 4 state rather than an effectively hidden launch

### Gap 4 — public review workflow is not yet complete on the real pages
Symptoms:
- real document IDs exist in repo, but the live lesson URLs still 404
- Rachel + Margaret live-page review cannot be treated as complete until the actual public pages resolve

Concrete fix path:
- publish the canonical pages first
- verify `?review=1` works on the real public URLs
- run Rachel + Margaret review on the real pages
- revise and republish as needed
- record outcomes in `lesson-plans/gr4-life-science-batch-review.md`

### Gap 5 — final live print-readiness is not yet verified on public URLs
Symptoms:
- print styling may be present in repo files, but live print-readiness has not been verified on the actual public pages

Concrete fix path:
- after deploy, test live lesson pages, refcards, and quizzes in print mode
- confirm worksheet/page-break/paywall/review behavior on production URLs
- capture final proof in the shareable/final verification artifacts

### Gap 6 — deploy wiring/root cause still needs explicit identification
Current evidence suggests one of these is true:
- Grade 4 files are not included in the deployed artifact
- the deploy source is not using the current working tree/branch content
- a publish script, static export filter, or host sync step is excluding the new Grade 4 assets
- only the lesson-directory surface was regenerated/published while canonical lesson assets were not

Concrete fix path:
- inspect the actual deploy pipeline and artifact source
- verify whether `lesson-plans/gr4-ls1-*.html` is present in the deployment output
- fix the missing deployment step or route inclusion issue before re-running live verification

---

## Bounded handoff to later chunks

### Later chunk: publish and route recovery
Responsible for:
- tracing the deploy path
- ensuring Grade 4 canonical assets are included in the live site build/artifact
- eliminating public `404`s for all canonical Grade 4 lesson/refcard/quiz URLs

### Later chunk: directory and curriculum exposure
Responsible for:
- replacing Grade 4 coming-soon state in `curriculum.html` and `curriculum/index.html`
- verifying Grade 4 on the live curriculum library
- confirming homepage/discovery exposure where needed

### Later chunk: Remarq live review loop
Responsible for:
- verifying real review mode on live pages
- running Rachel + Margaret review on those public pages
- capturing revisions and final review status honestly

### Later chunk: final QA and proof
Responsible for:
- print-readiness on public URLs
- final exact public URL verification set
- commit/push/deploy proof that repo, deployment, and public site are aligned

---

## Chunk-1 completion decision

This audit chunk is complete when later implementation no longer has to guess.
That condition is now met.

The authoritative answer for the next chunks is:
- the canonical Grade 4 Life Science package already exists in repo
- the exact public URL pattern for every lesson/refcard/quiz asset is known
- real Remarq document IDs are already wired in repo for the package
- `lesson-plans/index.html` already exposes Grade 4 locally and live
- `curriculum.html` / `curriculum/index.html` still hide Grade 4 behind a coming-soon state
- representative canonical Grade 4 lesson/quiz URLs still 404 publicly
- the remaining work is publish/deploy/listing/review/verification work, not first-pass content drafting
