# Grade 3 + Shared Remarq Follow-up Audit

Last updated: 2026-04-09
Status: post-Grade-2 shared/non-Grade-2 follow-up

This note records what was repaired in the shared/non-Grade-2 follow-up chunk and what still remains outside the tightly scoped repair surface.

## What this follow-up repaired

### Grade 3 support assets moved to production Remarq wiring

Repaired from private dev host to production host:
- `lesson-plans/gr3-ess2-unit1-quiz.html`
- `lesson-plans/gr3-ess2-unit1-refcard-lesson1-weather-patterns-over-time.html`
- `lesson-plans/gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html`
- `lesson-plans/gr3-ess2-unit1-refcard-lesson3-reading-weather-data.html`
- `lesson-plans/gr3-ess2-unit1-refcard-lesson4-weather-hazards-and-impacts.html`
- `lesson-plans/gr3-ess2-unit1-refcard-lesson5-designing-for-local-weather.html`
- `lesson-plans/gr3-ess2-unit1-refcard-lesson6-reducing-weather-related-hazards.html`
- `lesson-plans/gr3-ets1-unit1-quiz.html`
- `lesson-plans/gr3-ets1-unit1-refcard-lesson1-defining-the-problem.html`
- `lesson-plans/gr3-ets1-unit1-refcard-lesson2-researching-constraints-and-materials.html`
- `lesson-plans/gr3-ets1-unit1-refcard-lesson3-planning-a-solution.html`
- `lesson-plans/gr3-ets1-unit1-refcard-lesson4-building-and-testing-a-prototype.html`
- `lesson-plans/gr3-ets1-unit1-refcard-lesson5-improving-the-design.html`
- `lesson-plans/gr3-ets1-unit1-refcard-lesson6-share-and-defend-your-solution.html`
- `lesson-plans/gr3-ls1-unit1-quiz.html`
- `lesson-plans/gr3-ls1-unit1-refcard-lesson3-plant-life-cycles-and-seeds.html`
- `lesson-plans/gr3-ls1-unit1-refcard-lesson4-animal-life-cycles-and-metamorphosis.html`
- `lesson-plans/gr3-ls1-unit1-refcard-lesson5-comparing-life-cycle-patterns.html`
- `lesson-plans/gr3-ls1-unit1-refcard-lesson6-model-and-explain-a-life-cycle.html`
- `lesson-plans/gr3-ps2-unit1-quiz.html`

### Grade 3 free sample trio moved to production Remarq wiring

Repaired from private dev host to production host:
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-quiz.html`
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge-refcard.html`

## High-impact public review surfaces now expected to be good

After the Grade 2 chunk plus this follow-up, the highest-impact public review surfaces in reachable scope are:
- Grade 2 review lessons
- Grade 3 lesson pages
- Grade 3 support assets (quiz/refcards)
- Grade 3 free sample trio
- Grade 3 review-only and lesson-index entrypoints
- main public Grade 3 discovery links in `index.html`, `curriculum.html`, and `curriculum/index.html`

## Remaining known private-host cases outside this chunk

A repo-wide scan still finds private-host Remarq wiring outside the repaired Grade 2 + Grade 3 scope.

Current bounded categories still showing `192.168.5.204:3334` references:
- Kindergarten / early: `115` files
- Grade 1: `75` files
- Grade 2 support assets: `12` files
- Grade 5: `9` files
- Free lessons / support (outside repaired Grade 3 sample): `15` files total category before subtracting repaired subset
- Other / misc legacy pages: `27` files

Representative still-broken live public examples outside current scope:
- Grade 1 lesson page:
  - `https://littlelabcoats.co/lesson-plans/gr1-ess1-unit1-lesson4-daylight-and-seasons.html?review=1`
- Kindergarten lesson page:
  - `https://littlelabcoats.co/lesson-plans/k-ps3-unit2-lesson4-melting-race.html?review=1`
- Grade 4 free sample lesson:
  - `https://littlelabcoats.co/lesson-plans/free-gr4-apple-oxidation.html?review=1`

These are not silently ignored.
They remain known follow-up migration work, but repairing them all is larger than this chunk’s bounded scope.

## Why the remaining cases were not fixed here

This chunk was intentionally limited to:
- shared/high-impact public review surfaces tied to the already-audited Grade 3 gap
- the Grade 3 support assets and free sample that logically sit next to the repaired Grade 3 lesson pages
- documenting the broader remaining migration rather than reopening the entire historical archive in one pass

## Recommended next follow-up if needed

If more Remarq migration work is requested, the next bounded passes should likely be:
1. Grade 1 lesson pages + linked support assets
2. Kindergarten lesson pages + linked support assets
3. remaining free sample/support pages across grades
4. miscellaneous legacy/sandbox pages only if they are still publicly important
