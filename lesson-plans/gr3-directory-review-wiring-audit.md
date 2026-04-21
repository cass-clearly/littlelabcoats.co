# Grade 3 Directory Review Wiring Audit

Last updated: 2026-04-09
Status: chunk audit for urgent Grade 3 directory → live review usability

This file is an audit only.
It identifies the current Grade 3 review-routing failure and narrows the next implementation chunk to the smallest viable fix surface.

## Scope of this audit

Objective for the next implementation chunk:
- make Grade 3 lessons reviewable from the public directory path Serena is using
- ensure the clicked Grade 3 lesson pages load a working live Remarq feedback layer
- keep changes tightly scoped to Grade 3 review usability

This audit does **not** claim the fix is implemented yet.

## In-scope discovery surfaces checked

Public discovery/index surfaces checked for Grade 3 lesson access:
- `curriculum.html`
- `curriculum/index.html`
- `index.html`
- `lesson-plans/index.html`
- `lesson-plans/review/index.html`
- `lesson-plans/_generated/lesson-index-data.json`

Representative Grade 3 lesson pages checked:
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html`
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html`

Known-good comparison page checked:
- `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`

## File and route inventory

### 1) Public curriculum/home directory entrypoints

These Grade 3 surfaces currently send users to the canonical lesson URL, **not** directly to `?review=1`:

- `curriculum.html`
- `curriculum/index.html`
- `index.html`

Example current link shape from these surfaces:
- `/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `/lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html`
- `/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
- `/lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html`

Implication:
- if Serena enters through the general public directory/curriculum/home surfaces, she lands on the normal preview page first, not an explicit review path

### 2) Lesson index entrypoint

`lesson-plans/index.html` is mixed-purpose and currently exposes both:
- canonical lesson links via `Open lesson`
- explicit review links via `Review mode`

Example current review link shape:
- `/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html?review=1`

Implication:
- the lesson index already has a review entrypoint available
- but usability still depends on the destination lesson page being wired to live Remarq correctly

### 3) Review-only index entrypoint

`lesson-plans/review/index.html` is already routing Grade 3 links directly to review URLs.

Example current link shape:
- `/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html?review=1`
- `/lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html?review=1`
- `/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html?review=1`
- `/lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html?review=1`

Implication:
- the review-only index itself is **not** the primary routing failure
- if review is still broken from this page, the problem is on the destination lesson pages

### 4) Generated review-link source

`lesson-plans/_generated/lesson-index-data.json` already records correct Grade 3 `reviewUrl` values.

Example values present now:
- `/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html?review=1`
- `/lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html?review=1`
- `/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html?review=1`
- `/lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html?review=1`

Implication:
- generated review URL data is already correct for Grade 3
- no evidence yet that the index data generator is producing the wrong review route

## Representative lesson-page wiring audit

### What Grade 3 lesson pages have right

Representative Grade 3 lessons already contain:
- a `body data-document-id="..."`
- a `data-document-id="..."` on the feedback-layer script tag
- review unlock logic that bypasses the paywall when `?review=1` is present

Examples:
- `gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `gr3-ess2-unit1-lesson1-weather-patterns-over-time.html`
- `gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
- `gr3-ets1-unit1-lesson1-defining-the-problem.html`

So the issue is **not** missing document IDs and **not** missing `?review=1` paywall bypass logic.

### What Grade 3 lesson pages have wrong

Representative Grade 3 lessons currently load the feedback layer from a local LAN/dev endpoint:
- `http://192.168.5.204:3334/feedback-layer.js`
- `data-api-url="http://192.168.5.204:3334"`

Examples confirmed in:
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html`
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
- `lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html`

This is the critical mismatch with live/public review behavior.

### Known-good Grade 4 comparison

The checked Grade 4 lesson uses the live production feedback layer instead:
- `/feedback-layer.js?v=20260421`
- `data-api-url="https://cassclearly.com"`

Confirmed in:
- `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`

Implication:
- Grade 4 is wired for public/live Remarq
- Grade 3 representative lessons are still wired to a private local endpoint that Serena cannot use from the public site

## Root-cause conclusion

### Primary failure point

The clearest failure is **lesson-page Remarq wiring**, not review URL generation.

Specifically:
- Grade 3 review URLs exist
- Grade 3 review-only index links exist
- Grade 3 pages contain document IDs
- Grade 3 pages bypass the paywall in `?review=1`
- **but the Grade 3 lesson pages point their feedback layer at a local private host, not the live Remarq endpoint**

That means a Grade 3 page can open, but Serena will not get a working public review/comment/edit experience from the live site.

### Secondary usability issue

There is also a smaller directory-entry problem:
- `curriculum.html`
- `curriculum/index.html`
- `index.html`

all currently route Grade 3 clicks to canonical lesson URLs instead of explicit `?review=1` URLs.

This is not the main technical blocker, but it does reduce review usability from the general public directory surfaces.

## Smallest viable fix surface for the next chunk

### Required fix surface

The smallest viable next implementation should focus on:

1. Grade 3 lesson pages themselves
- switch Grade 3 lesson feedback-layer script source from local dev host to the production feedback-layer host
- switch Grade 3 lesson `data-api-url` from local dev host to production
- keep existing Grade 3 document IDs unchanged unless a live document mismatch is discovered later

2. Grade 3 public discovery surfaces that Serena is likely using
- update Grade 3 links on `curriculum.html`
- update Grade 3 links on `curriculum/index.html`
- update Grade 3 links on `index.html`
- target explicit `?review=1` URLs for Grade 3 lesson rows if the goal is review-first usability from the directory

### Surfaces that do not appear to need logic changes right now

These already look structurally correct for review routing:
- `lesson-plans/review/index.html`
- `lesson-plans/index.html` review-mode links
- `lesson-plans/_generated/lesson-index-data.json`

They may still be regenerated later for consistency, but they are not the current root cause.

## Representative live verification targets for the next chunk

Use these after the implementation chunk is pushed live:

- `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html?review=1`

Suggested directory-entry verification pages:
- `https://littlelabcoats.co/curriculum.html`
- `https://littlelabcoats.co/curriculum/`
- `https://littlelabcoats.co/`
- `https://littlelabcoats.co/lesson-plans/`
- `https://littlelabcoats.co/lesson-plans/review/`

## Audit conclusion

Current state:
- Grade 3 review URLs are present in the dedicated lesson index and review index
- Grade 3 generated index data already contains correct `reviewUrl` values
- Grade 3 lesson pages contain document IDs and review-mode unlock logic
- Grade 3 representative lesson pages are still wired to a private local feedback-layer host
- broad public directory surfaces still send Grade 3 users to canonical lesson URLs instead of explicit review URLs

Conclusion for next chunk:
- treat the Grade 3 lesson-page feedback-layer endpoint as the primary fix
- treat review-first directory links on public Grade 3 discovery surfaces as the adjacent usability fix
- keep the change set limited to Grade 3 lessons plus the few Grade 3 directory surfaces Serena is actually using
