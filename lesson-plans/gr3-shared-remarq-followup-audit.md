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

## Subsequent full migration note

After this follow-up audit was written, the remaining live lesson/support HTML files that still pointed at the private dev Remarq host were migrated to the production `cassclearly.com` host as a final cleanup pass.

Current state for the HTML review surfaces in `lesson-plans/`:
- no remaining lesson/support HTML file is expected to point at `192.168.5.204:3334`
- the original “remaining private-host cases” list in this file is now historical context, not current live-state truth

If future Remarq issues appear, treat them as route-specific regressions to audit directly rather than assuming the earlier legacy backlog still exists unchanged.

## Recommended next follow-up if needed

If more Remarq cleanup is requested later, the next work should be:
1. route-specific live verification if a page is reported broken
2. browser-interactive confirmation of visible comment/highlight UI on a few representative pages
3. cleanup of any historical audit docs whose pre-fix wording is no longer useful
