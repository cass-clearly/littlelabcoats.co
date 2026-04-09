# Grade 2 Remarq Review Wiring Audit

Last updated: 2026-04-09
Status: chunk audit for urgent Grade 2 review usability

This file is an audit only.
It maps the live/public Grade 2 review surface, identifies where Remarq is missing or broken, and narrows the next implementation chunk to the smallest viable repair surface.

## Scope of this audit

Objective for the next implementation chunk:
- make Grade 2 lessons reviewable from the public review entrypoints Chris/Serena are likely to use
- ensure the clicked Grade 2 review pages load a working live Remarq feedback layer
- identify whether the problem is Grade-2-specific or part of a broader legacy wiring pattern

This audit does **not** claim the fix is implemented yet.

## Discovery surfaces checked

Directory / review entrypoints checked:
- `lesson-plans/review/index.html`
- `lesson-plans/index.html`
- `lesson-plans/_generated/lesson-index-data.json`
- `index.html`
- `curriculum.html`
- `curriculum/index.html`

Live/public review URLs checked:
- every Grade 2 review URL recorded in `lesson-plans/_generated/lesson-index-data.json` (`26` total)
- representative broader comparison pages:
  - `https://littlelabcoats.co/lesson-plans/gr1-ess1-unit1-lesson4-daylight-and-seasons.html?review=1`
  - `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html?review=1`
  - `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html?review=1`

Live checks for each Grade 2 page recorded:
- HTTP load status
- `body data-document-id`
- feedback-layer script presence
- feedback-layer endpoint host
- script-level `data-document-id`
- presence of `?review=1` paywall-bypass logic

Important limitation:
- these checks confirm live HTML wiring, not a full browser-rendered Remarq session
- so `working` below means “production-wired for live Remarq,” while `broken` means “cannot work publicly from current HTML wiring”

## Grade 2 directory / review entrypoint inventory

### Canonical review-first entrypoint

`lesson-plans/review/index.html`

This is the strongest public review entrypoint for Grade 2 right now because it already routes directly to explicit `?review=1` URLs.

Grade 2 review rows present there:
- Physical Science
  - `/lesson-plans/gr2-ps1-unit1-l1-matter.html?review=1`
  - `/lesson-plans/gr2-ps1-unit1-l2-texture.html?review=1`
  - `/lesson-plans/gr2-ps1-unit1-l3-sink-float.html?review=1`
  - `/lesson-plans/gr2-ps1-unit1-l4-mixing.html?review=1`
  - `/lesson-plans/gr2-ps1-unit1-l5-heating-cooling.html?review=1`
  - `/lesson-plans/gr2-ps1-unit1-l6-boat-engineering.html?review=1`
  - `/lesson-plans/gr2-ps1-lesson1-mystery-powders.html?review=1`
- Life Science
  - `/lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html?review=1`
  - `/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`
  - `/lesson-plans/gr2-ls2-unit1-lesson3-seed-dispersal.html?review=1`
  - `/lesson-plans/gr2-ls2-unit1-lesson4-food-chains.html?review=1`
  - `/lesson-plans/gr2-ls2-unit1-lesson5-habitats.html?review=1`
  - `/lesson-plans/gr2-ls2-unit1-lesson6-ecosystems-under-threat.html?review=1`
  - `/lesson-plans/gr2-ls2-unit2-l1-ecosystems.html?review=1`
  - `/lesson-plans/gr2-ls2-unit2-l2-plants-partners.html?review=1`
  - `/lesson-plans/gr2-ls2-unit2-l3-food-chains.html?review=1`
  - `/lesson-plans/gr2-ls2-unit2-l4-predator-prey.html?review=1`
  - `/lesson-plans/gr2-ls2-unit2-l5-habitat-hunt.html?review=1`
  - `/lesson-plans/gr2-ls2-unit2-l6-design-habitat.html?review=1`
- Earth & Space Science
  - `/lesson-plans/gr2-ess1-unit3-l1-landforms.html?review=1`
  - `/lesson-plans/gr2-ess1-unit3-l2-rocks-soils.html?review=1`
  - `/lesson-plans/gr2-ess1-unit3-l3-erosion.html?review=1`
  - `/lesson-plans/gr2-ess1-unit3-l4-maps.html?review=1`
  - `/lesson-plans/gr2-ess1-unit3-l5-weather-patterns.html?review=1`
  - `/lesson-plans/gr2-ess1-unit3-l6-erosion-engineering.html?review=1`
- Other lessons
  - `/lesson-plans/free-gr2-salt-dough-fossil-factory.html?review=1`

### Mixed-purpose lesson index entrypoint

`lesson-plans/index.html`

This page exposes both:
- canonical lesson URLs through `Open lesson`
- explicit review URLs through `Review mode`

Implication:
- review entrypoints already exist for the Grade 2 rows here
- if review is broken from this page, the destination lesson pages are the primary problem, not link generation

### Generated source of truth for review URLs

`lesson-plans/_generated/lesson-index-data.json`

This file already records all `26` Grade 2 review URLs correctly.

Implication:
- the generator already knows the right review routes
- there is no evidence in this chunk that generated Grade 2 review URLs are wrong or missing

### General public discovery surfaces

These broader surfaces still send users to canonical lesson URLs instead of explicit review URLs:
- `index.html`
- `curriculum.html`
- `curriculum/index.html`

Implication:
- these pages are a secondary usability problem for review-first workflows
- but they are not the main technical reason Remarq is failing on Grade 2 once a reviewer reaches `?review=1`

## Live/public Grade 2 status matrix

Legend:
- `load` = live URL returned `200`
- `body doc` = `body data-document-id` present
- `script doc` = feedback-layer script has `data-document-id`
- `review bypass` = page contains `?review=1` bypass logic in live HTML
- `endpoint` = host used by the live feedback layer
- `status` = practical review outcome from current wiring

| Group | Review URL | Load | Body doc | Script doc | Review bypass | Endpoint | Status | Failure mode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PS1 U1 L1 | `/lesson-plans/gr2-ps1-unit1-l1-matter.html?review=1` | 200 | `doc_-tQUmKPD1EU` | `doc_-tQUmKPD1EU` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| PS1 U1 L2 | `/lesson-plans/gr2-ps1-unit1-l2-texture.html?review=1` | 200 | `doc_EU1U7bikLg4` | `doc_EU1U7bikLg4` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| PS1 U1 L3 | `/lesson-plans/gr2-ps1-unit1-l3-sink-float.html?review=1` | 200 | `doc_qbGYvzYd2tw` | `doc_qbGYvzYd2tw` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| PS1 U1 L4 | `/lesson-plans/gr2-ps1-unit1-l4-mixing.html?review=1` | 200 | `doc_7svbZnDGAbE` | `doc_7svbZnDGAbE` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| PS1 U1 L5 | `/lesson-plans/gr2-ps1-unit1-l5-heating-cooling.html?review=1` | 200 | `doc_J_vYfKBnFS0` | `doc_J_vYfKBnFS0` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| PS1 U1 L6 | `/lesson-plans/gr2-ps1-unit1-l6-boat-engineering.html?review=1` | 200 | `doc_2eV50-Z4aOk` | `doc_2eV50-Z4aOk` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| PS1 extra | `/lesson-plans/gr2-ps1-lesson1-mystery-powders.html?review=1` | 200 | `doc_gr2-ps1-lesson1-mystery-powders` | missing | yes | none detected | broken | missing feedback-layer script on live page |
| LS2 U1 L1 | `/lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html?review=1` | 200 | `doc_Om89jaLtBbI` | `doc_Om89jaLtBbI` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| LS2 U1 L2 | `/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1` | 200 | `doc_8COJPE7TH7w` | `doc_8COJPE7TH7w` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| LS2 U1 L3 | `/lesson-plans/gr2-ls2-unit1-lesson3-seed-dispersal.html?review=1` | 200 | `doc__kFwFRsekOI` | `doc__kFwFRsekOI` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| LS2 U1 L4 | `/lesson-plans/gr2-ls2-unit1-lesson4-food-chains.html?review=1` | 200 | `doc_xUJUbARGihA` | `doc_xUJUbARGihA` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| LS2 U1 L5 | `/lesson-plans/gr2-ls2-unit1-lesson5-habitats.html?review=1` | 200 | `doc_mL4XwOH-8C0` | `doc_mL4XwOH-8C0` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| LS2 U1 L6 | `/lesson-plans/gr2-ls2-unit1-lesson6-ecosystems-under-threat.html?review=1` | 200 | `doc_xwaU0P58j0Q` | `doc_xwaU0P58j0Q` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| LS2 U2 L1 | `/lesson-plans/gr2-ls2-unit2-l1-ecosystems.html?review=1` | 200 | `doc_0W96LUQ-dtw` | `doc_0W96LUQ-dtw` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| LS2 U2 L2 | `/lesson-plans/gr2-ls2-unit2-l2-plants-partners.html?review=1` | 200 | `doc_qRD5DYBlX3g` | `doc_qRD5DYBlX3g` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| LS2 U2 L3 | `/lesson-plans/gr2-ls2-unit2-l3-food-chains.html?review=1` | 200 | `doc_zCF8GBQM3cs` | `doc_zCF8GBQM3cs` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| LS2 U2 L4 | `/lesson-plans/gr2-ls2-unit2-l4-predator-prey.html?review=1` | 200 | `doc_Np1M1TEUGrg` | `doc_Np1M1TEUGrg` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| LS2 U2 L5 | `/lesson-plans/gr2-ls2-unit2-l5-habitat-hunt.html?review=1` | 200 | `doc_xIANYy91vLc` | `doc_xIANYy91vLc` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| LS2 U2 L6 | `/lesson-plans/gr2-ls2-unit2-l6-design-habitat.html?review=1` | 200 | `doc_bBiY7845V3U` | `doc_bBiY7845V3U` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| ESS1 U3 L1 | `/lesson-plans/gr2-ess1-unit3-l1-landforms.html?review=1` | 200 | `doc_gjkH3_rScv4` | `doc_gjkH3_rScv4` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| ESS1 U3 L2 | `/lesson-plans/gr2-ess1-unit3-l2-rocks-soils.html?review=1` | 200 | `doc_oZtb0wnl_qU` | `doc_oZtb0wnl_qU` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| ESS1 U3 L3 | `/lesson-plans/gr2-ess1-unit3-l3-erosion.html?review=1` | 200 | `doc_WeR23z04lsg` | `doc_WeR23z04lsg` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| ESS1 U3 L4 | `/lesson-plans/gr2-ess1-unit3-l4-maps.html?review=1` | 200 | `doc_7gmNBjlJ9p0` | `doc_7gmNBjlJ9p0` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| ESS1 U3 L5 | `/lesson-plans/gr2-ess1-unit3-l5-weather-patterns.html?review=1` | 200 | `doc_2fbUG5eoyLE` | `doc_2fbUG5eoyLE` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| ESS1 U3 L6 | `/lesson-plans/gr2-ess1-unit3-l6-erosion-engineering.html?review=1` | 200 | `doc_tXMBO1zRwgg` | `doc_tXMBO1zRwgg` | yes | `192.168.5.204:3334` | broken | private dev feedback endpoint |
| Free sample | `/lesson-plans/free-gr2-salt-dough-fossil-factory.html?review=1` | 200 | `doc_free_gr2_salt_dough_fossil_factory_lesson` | `doc_free_gr2_salt_dough_fossil_factory_lesson` | no | `192.168.5.204:3334` | broken | private dev feedback endpoint + missing review bypass |

## Grade 2 conclusions

### 1) No Grade 2 lesson in the checked live review set is production-wired today

Out of `26` checked Grade 2 review URLs:
- `24` are live but wired to the private dev Remarq host `192.168.5.204:3334`
- `1` is live with the feedback layer script missing entirely (`gr2-ps1-lesson1-mystery-powders.html`)
- `1` is live, still wired to the private dev host, and also lacks `?review=1` bypass logic (`free-gr2-salt-dough-fossil-factory.html`)

### 2) Grade 2 routing is mostly present; destination wiring is the real blocker

The review-only entrypoint and mixed-purpose lesson index already expose correct Grade 2 `?review=1` links.

So the dominant problem is **not** URL generation.
The dominant problem is **destination-page review-layer wiring**.

### 3) The failure is broad across all Grade 2 lesson clusters

Affected clusters include:
- PS1 Unit 1 lessons 1–6
- PS1 extra lesson (`mystery-powders`)
- LS2 Unit 1 lessons 1–6
- LS2 Unit 2 lessons 1–6
- ESS1 Unit 3 lessons 1–6
- Grade 2 free sample lesson

This is not a single-lesson anomaly.
It is a broad Grade 2 review-layer wiring problem.

## Broader pass beyond Grade 2

Representative comparison results:

| Grade | Review URL | Endpoint result | Interpretation |
| --- | --- | --- | --- |
| Grade 1 | `/lesson-plans/gr1-ess1-unit1-lesson4-daylight-and-seasons.html?review=1` | `192.168.5.204:3334` | older/legacy public review pages still point to private dev host |
| Grade 3 | `/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html?review=1` | `https://cassclearly.com/feedback-layer.js?v=20260408` | Grade 3 representative page is already production-wired |
| Grade 4 | `/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html?review=1` | `https://cassclearly.com/feedback-layer.js?v=20260408` | Grade 4 representative page is already production-wired |

Broader conclusion:
- the problem is **not universal across the site**
- Grade 3 and Grade 4 representative review pages already show the modern production Remarq wiring pattern
- Grade 2 is currently sitting in the older/legacy wiring state, and at least some Grade 1 pages are too

## Concrete failure modes identified

### Failure mode A — private dev feedback endpoint on live/public review page

Symptoms:
- page loads on the public site
- `body data-document-id` exists
- feedback-layer script exists
- `?review=1` bypass logic usually exists
- but the script source and API URL point to `192.168.5.204:3334`

Why it breaks live review:
- this is a private LAN/dev endpoint, not a public production Remarq host
- public reviewers cannot rely on it for live comment/edit behavior

Affected Grade 2 pages:
- all Grade 2 pages in the matrix except `gr2-ps1-lesson1-mystery-powders.html`
- plus the free Grade 2 sample page, which has this issue alongside another issue

### Failure mode B — missing feedback-layer script entirely

Symptoms:
- `body data-document-id` exists
- no feedback-layer script was detected in the live HTML

Affected page:
- `/lesson-plans/gr2-ps1-lesson1-mystery-powders.html?review=1`

Why it breaks live review:
- even with a document ID, there is no Remarq layer to initialize

### Failure mode C — missing `?review=1` bypass logic

Symptoms:
- page exposes a review URL and a feedback-layer script
- but no review-mode paywall bypass logic was found in live HTML

Affected page:
- `/lesson-plans/free-gr2-salt-dough-fossil-factory.html?review=1`

Why it matters:
- even after endpoint repair, review-mode usability will still be degraded if the page remains locked or partially locked

### Failure mode D — general directory surfaces are not review-first

Symptoms:
- `index.html`, `curriculum.html`, and `curriculum/index.html` route to canonical lesson URLs rather than explicit `?review=1` URLs

Why it matters:
- this is a usability issue for review workflows
- but it is secondary to the broken Grade 2 destination-page Remarq wiring

## Smallest viable repair surface for the next chunk

### Highest-priority repair: Grade 2 lesson pages themselves

Needed next:
1. switch Grade 2 lesson feedback-layer script sources from `192.168.5.204:3334` to the production Remarq host pattern already used by Grade 3/4 (`cassclearly.com`)
2. switch Grade 2 lesson `data-api-url` values from the private dev host to the production API host
3. repair the missing feedback-layer script on `gr2-ps1-lesson1-mystery-powders.html`
4. add the missing `?review=1` bypass logic on `free-gr2-salt-dough-fossil-factory.html`
5. keep existing document IDs unless later live tests prove a document mismatch

### Secondary repair: review-first entrypoints outside the dedicated review index

After the page wiring is fixed, optionally tighten review usability by updating Grade 2 links on:
- `index.html`
- `curriculum.html`
- `curriculum/index.html`

But this should come **after** or **with** the Grade 2 page-layer fix, not instead of it.

## Representative live verification targets for the repair chunk

Use these after the fix is pushed live:
- `https://littlelabcoats.co/lesson-plans/gr2-ps1-unit1-l1-matter.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit2-l1-ecosystems.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr2-ess1-unit3-l1-landforms.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr2-ps1-lesson1-mystery-powders.html?review=1`
- `https://littlelabcoats.co/lesson-plans/free-gr2-salt-dough-fossil-factory.html?review=1`

Comparison checks worth keeping:
- `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html?review=1`

## Audit conclusion

Current state:
- Grade 2 review URLs exist and the dedicated review index routes to them correctly
- Grade 2 live review pages load publicly
- nearly the entire Grade 2 review set is still wired to a private dev Remarq host instead of the production feedback layer
- one Grade 2 page is missing the feedback-layer script entirely
- one Grade 2 free sample page is missing review bypass logic in addition to using the private dev endpoint
- Grade 3 and Grade 4 representative pages show the newer production wiring pattern, so this is a legacy/partial-migration issue rather than a site-wide Remarq outage

Conclusion for the next chunk:
- treat **Grade 2 lesson-page review-layer wiring** as the primary fix surface
- treat `mystery-powders` and the Grade 2 free sample as special-case repairs inside that same pass
- consider review-first link changes on the broader public directory surfaces only after the Grade 2 page-layer fix is in place
