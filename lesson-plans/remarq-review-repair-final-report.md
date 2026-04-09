# Remarq Review Repair — Final Report

Last updated: 2026-04-09
Status: business-ready summary

## Executive summary

Grade 2 review pages are now live and production-wired for Remarq on the public site.

The highest-impact non-Grade-2 follow-up that was in reachable scope is also live:
- Grade 3 support assets (quizzes + refcards)
- Grade 3 free sample trio

The core root cause was consistent across the broken sets:
- pages existed and often already had document IDs
- review URLs often already existed
- but the live feedback layer was still pointing at the private dev host `192.168.5.204:3334` instead of the public production host `https://cassclearly.com`

## Commit / push status

Relevant shipped commits on `main`:
- `5094470` — `Wire Grade 2 review lessons to production Remarq`
- `e4f416c` — `Wire Grade 3 support assets to production Remarq`

Remote status:
- `origin/main` is up to date with `e4f416c`

## What is fixed and live now

### Grade 2 review lessons — fixed and live

The full Grade 2 review lesson set is now production-wired for Remarq on the live/public site.

This includes:
- **Grade 2 Physical Science**
  - `gr2-ps1-unit1-l1-matter`
  - `gr2-ps1-unit1-l2-texture`
  - `gr2-ps1-unit1-l3-sink-float`
  - `gr2-ps1-unit1-l4-mixing`
  - `gr2-ps1-unit1-l5-heating-cooling`
  - `gr2-ps1-unit1-l6-boat-engineering`
  - `gr2-ps1-lesson1-mystery-powders`
- **Grade 2 Life Science**
  - `gr2-ls2-unit1-lesson1-what-do-plants-need`
  - `gr2-ls2-unit1-lesson2-pollinators`
  - `gr2-ls2-unit1-lesson3-seed-dispersal`
  - `gr2-ls2-unit1-lesson4-food-chains`
  - `gr2-ls2-unit1-lesson5-habitats`
  - `gr2-ls2-unit1-lesson6-ecosystems-under-threat`
  - `gr2-ls2-unit2-l1-ecosystems`
  - `gr2-ls2-unit2-l2-plants-partners`
  - `gr2-ls2-unit2-l3-food-chains`
  - `gr2-ls2-unit2-l4-predator-prey`
  - `gr2-ls2-unit2-l5-habitat-hunt`
  - `gr2-ls2-unit2-l6-design-habitat`
- **Grade 2 Earth & Space Science**
  - `gr2-ess1-unit3-l1-landforms`
  - `gr2-ess1-unit3-l2-rocks-soils`
  - `gr2-ess1-unit3-l3-erosion`
  - `gr2-ess1-unit3-l4-maps`
  - `gr2-ess1-unit3-l5-weather-patterns`
  - `gr2-ess1-unit3-l6-erosion-engineering`
- **Grade 2 free sample**
  - `free-gr2-salt-dough-fossil-factory`

What “live-good” means in this report:
- public URL returned `200`
- page serves `https://cassclearly.com/feedback-layer.js?v=20260408`
- page serves `data-api-url="https://cassclearly.com"`
- `body data-document-id` matches script `data-document-id`
- non-free lessons expose review-mode unlock logic for `?review=1`

### Grade 3 shared/support follow-up — fixed and live

The following adjacent high-impact non-Grade-2 assets were also repaired and verified live:

**Grade 3 support assets**
- `gr3-ess2-unit1-quiz.html`
- `gr3-ess2-unit1-refcard-lesson1-weather-patterns-over-time.html`
- `gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html`
- `gr3-ess2-unit1-refcard-lesson3-reading-weather-data.html`
- `gr3-ess2-unit1-refcard-lesson4-weather-hazards-and-impacts.html`
- `gr3-ess2-unit1-refcard-lesson5-designing-for-local-weather.html`
- `gr3-ess2-unit1-refcard-lesson6-reducing-weather-related-hazards.html`
- `gr3-ets1-unit1-quiz.html`
- `gr3-ets1-unit1-refcard-lesson1-defining-the-problem.html`
- `gr3-ets1-unit1-refcard-lesson2-researching-constraints-and-materials.html`
- `gr3-ets1-unit1-refcard-lesson3-planning-a-solution.html`
- `gr3-ets1-unit1-refcard-lesson4-building-and-testing-a-prototype.html`
- `gr3-ets1-unit1-refcard-lesson5-improving-the-design.html`
- `gr3-ets1-unit1-refcard-lesson6-share-and-defend-your-solution.html`
- `gr3-ls1-unit1-quiz.html`
- `gr3-ls1-unit1-refcard-lesson3-plant-life-cycles-and-seeds.html`
- `gr3-ls1-unit1-refcard-lesson4-animal-life-cycles-and-metamorphosis.html`
- `gr3-ls1-unit1-refcard-lesson5-comparing-life-cycle-patterns.html`
- `gr3-ls1-unit1-refcard-lesson6-model-and-explain-a-life-cycle.html`
- `gr3-ps2-unit1-quiz.html`

**Grade 3 free sample trio**
- `free-gr3-egg-drop-kitchen-challenge.html`
- `free-gr3-egg-drop-kitchen-challenge-quiz.html`
- `free-gr3-egg-drop-kitchen-challenge-refcard.html`

### Grade 3 lesson discovery / review entrypoints — live-good

These public surfaces now lead users into active Grade 3 review tooling with explicit `?review=1` links on the checked entries:
- `https://littlelabcoats.co/lesson-plans/review/`
- `https://littlelabcoats.co/lesson-plans/`
- `https://littlelabcoats.co/`
- `https://littlelabcoats.co/curriculum.html`
- `https://littlelabcoats.co/curriculum/`

## Specific live/public URLs used for post-push verification

### Grade 2 verification URLs
- `https://littlelabcoats.co/lesson-plans/gr2-ps1-unit1-l1-matter.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit2-l1-ecosystems.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr2-ess1-unit3-l1-landforms.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr2-ps1-lesson1-mystery-powders.html?review=1`
- `https://littlelabcoats.co/lesson-plans/free-gr2-salt-dough-fossil-factory.html?review=1`

### Non-Grade-2 / shared-fix verification URLs
- `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-quiz.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson1-weather-patterns-over-time.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-quiz.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-quiz.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-quiz.html?review=1`
- `https://littlelabcoats.co/lesson-plans/free-gr3-egg-drop-kitchen-challenge.html?review=1`
- `https://littlelabcoats.co/lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html?review=1`
- `https://littlelabcoats.co/lesson-plans/free-gr3-egg-drop-kitchen-challenge-refcard.html?review=1`

### Entrypoint verification URLs
- `https://littlelabcoats.co/lesson-plans/review/`
- `https://littlelabcoats.co/lesson-plans/`
- `https://littlelabcoats.co/`
- `https://littlelabcoats.co/curriculum.html`
- `https://littlelabcoats.co/curriculum/`

## Root-cause summary

Primary root cause:
- the broken pages were still loading Remarq from the private dev endpoint `192.168.5.204:3334`
- public reviewers could reach the pages, but not a dependable public review/comment experience

Secondary issues found during audit:
- one earlier parser read made `gr2-ps1-lesson1-mystery-powders` look like it lacked a feedback-layer script; on closer inspection it had a script but was wired to the wrong host
- some public discovery surfaces previously needed review-first confirmation, but the highest-impact checked Grade 3 entrypoints are now verified live with explicit `?review=1` links

## Remaining known gaps outside this completed scope

No remaining private-host Remarq wiring gap is currently expected across the `lesson-plans/` HTML review surfaces after the final cleanup pass.

What still remains outside the scope of this report:
- browser-interactive confirmation of visible inline comments/highlights on more than the representative sampled pages
- ongoing regression monitoring in case a future page or generated artifact reintroduces non-production wiring
- cleanup of historical audit notes that still describe earlier broken states for context

## Follow-up recommendation

Recommended next bounded follow-up if more certainty is wanted:
1. run browser-level live spot checks on representative pages from Grade 1, Grade 2, Grade 3, Kindergarten, and free/sample surfaces
2. remove or clearly label historical audit files whose pre-fix wording could confuse future readers
3. treat any newly reported issue as a route-specific regression audit rather than an assumed broad migration backlog

## Verification scope note

This report confirms **live/public HTML wiring and review-route behavior**.
It does **not** claim a browser-interactive proof of visible inline comments/highlights on every verified page.

What is confirmed live:
- public URL loads
- production Remarq bootstrap URL is present
- production API URL is present
- body/script document IDs match
- `?review=1` unlock behavior is present on non-free lesson pages

For business decision-making here, the key conclusion is still straightforward:
- **Grade 2 is now reviewable on the live site**
- **the highest-impact adjacent Grade 3 support surfaces are also live-good**
- **the legacy private-host Remarq wiring backlog for the `lesson-plans/` HTML review surfaces has now been cleaned up in the repo**
