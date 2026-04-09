# Grade 3 Shareable Manifest

Last updated: 2026-04-09
Status: Grade 3 LS1, PS2 baseline, ESS2, and ETS1 public URLs in this handoff were spot-checked successfully on 2026-04-07; representative live publish/discoverability checks for ESS2 and ETS1 lessons, quizzes, refcards, and curriculum surfaces returned HTTP 200 on 2026-04-07; stable self-generated document IDs are now wired for the newly shipped LS1 / ESS2 / ETS1 packages; Grade 3 review-entry routing and live production Remarq wiring were re-verified on 2026-04-09
Audience: Serena

This file is the concise Grade 3 URL handoff for the current live state.
It should be treated as the Grade 3 source-of-truth URL list for what is publicly reachable right now, plus the exact unresolved blockers that still need external workflow access.

Scope note for audit alignment:
- this manifest reflects the **currently discoverable Grade 3 repo state** audited in `lesson-plans/gr3-curriculum-audit-and-scope.md`
- that repo state currently includes `3-LS1` lesson pages 1–6, `3-PS2`, `3-ESS2 Unit 1`, `3-ETS1 Unit 1`, and the standalone `3-LS4` lesson `Bird Beak Buffet`
- it should not be read as proof that a larger full-year Grade 3 domain map has been confirmed in-repo

## 2026-04-09 urgent Grade 3 review-flow verification

This addendum captures the urgent review-usability fix verification after the Grade 3 directory review-routing and Remarq wiring update was committed and pushed on `main`.

### Live directory-entry verification

The live public directory surfaces now expose representative Grade 3 lesson links with explicit `?review=1` review URLs:
- `https://littlelabcoats.co/`
- `https://littlelabcoats.co/curriculum.html`
- `https://littlelabcoats.co/curriculum/`
- `https://littlelabcoats.co/lesson-plans/`

Representative live matches confirmed in fetched page source:
- `gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html?review=1`
- `gr3-ess2-unit1-lesson1-weather-patterns-over-time.html?review=1`
- `gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html?review=1`
- `gr3-ets1-unit1-lesson1-defining-the-problem.html?review=1`

### Representative live lesson verification

The following live review URLs were re-checked on 2026-04-09 and returned `HTTP 200`:
- `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html?review=1`

For each sampled live lesson page, fetched page source confirmed:
- explicit `data-document-id` is present on the deployed page
- the deployed page loads `https://cassclearly.com/feedback-layer.js?v=20260408`
- the deployed page uses `data-api-url="https://cassclearly.com"`
- the deployed page still contains `?review=1` bypass logic so the review URL opens the full lesson instead of the preview lock

### Deploy/cache status

Deployment lag was explicitly checked and ruled out for the sampled directory and lesson pages:
- live homepage response showed fresh `last-modified` and cache-miss headers during verification
- live fetched HTML already reflected the new `?review=1` Grade 3 directory links
- live fetched Grade 3 lesson HTML already reflected the production feedback-layer wiring

### Review-usability conclusion

For the verified sample, the urgent user-facing problem is no longer reproducible:
- the live public Grade 3 directory paths now point reviewers into review URLs
- representative Grade 3 lesson pages on the live domain now expose production Remarq wiring plus explicit document IDs
- the review path is available from the directory entrypoint, not only from a manually typed direct lesson URL

## Already public / linked in Grade 3 navigation

- `Bird Beak Buffet`  
  `https://littlelabcoats.co/lesson-plans/bird-beak-buffet.html`

## Existing Grade 3 baseline lesson URLs

These are the baseline Grade 3 lesson files already present in the repo and treated as the format anchors for later Grade 3 work.
They remain the live baseline anchors for the LS1 unit.

- `3-LS1 Unit 1 Lesson 1 — What Is a Life Cycle?`  
  `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- `3-LS1 Unit 1 Lesson 2 — Different Life Cycles, Same Big Pattern`  
  `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html`

## Grade 3 LS1 Batch 1 lesson URLs staged for handoff

These lesson files now exist in LLC format, have recorded Rachel + Margaret round-1 comments, and have round-1 revisions applied in repo.
They are wired into the Grade 3 navigation surfaces and were verified live on the public domain on 2026-04-07.

- `3-LS1 Unit 1 Lesson 3 — Plant Life Cycles and Seeds`  
  `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson3-plant-life-cycles-and-seeds.html`  
  Status: `live verified 2026-04-07`
- `3-LS1 Unit 1 Lesson 4 — Animal Life Cycles and Metamorphosis`  
  `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson4-animal-life-cycles-and-metamorphosis.html`  
  Status: `live verified 2026-04-07`
- `3-LS1 Unit 1 Lesson 5 — Comparing Life Cycle Patterns`  
  `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson5-comparing-life-cycle-patterns.html`  
  Status: `live verified 2026-04-07`
- `3-LS1 Unit 1 Lesson 6 — Model and Explain a Life Cycle`  
  `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson6-model-and-explain-a-life-cycle.html`  
  Status: `live verified 2026-04-07`

## Grade 3 LS1 support URLs staged for handoff

- `3-LS1 Refcard — Lesson 3 Plant Life Cycles and Seeds`  
  `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-refcard-lesson3-plant-life-cycles-and-seeds.html`  
  Status: `live verified 2026-04-07`
- `3-LS1 Refcard — Lesson 4 Animal Life Cycles and Metamorphosis`  
  `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-refcard-lesson4-animal-life-cycles-and-metamorphosis.html`  
  Status: `live verified 2026-04-07`
- `3-LS1 Refcard — Lesson 5 Comparing Life Cycle Patterns`  
  `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-refcard-lesson5-comparing-life-cycle-patterns.html`  
  Status: `live verified 2026-04-07`
- `3-LS1 Refcard — Lesson 6 Model and Explain a Life Cycle`  
  `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-refcard-lesson6-model-and-explain-a-life-cycle.html`  
  Status: `live verified 2026-04-07`
- `3-LS1 Unit 1 Quiz — Life Cycles`  
  `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-quiz.html`  
  Status: `live verified 2026-04-07`

## Grade 3 PS2 current public baseline URLs

These Physical Science lesson and quiz URLs are already publicly reachable on the live site.
Current HTTP spot checks returned `200` on 2026-04-07.
They are included here as existing Grade 3 baseline inventory, not as part of the newly shipped LS1 / ESS2 / ETS1 completion run.

- `3-PS2 Unit 1 Lesson 1 — Balanced and Unbalanced Forces`  
  `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`  
  Status: `HTTP 200 spot-checked 2026-04-07`
- `3-PS2 Unit 1 Lesson 2 — Motion Changes with Force`  
  `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html`  
  Status: `HTTP 200 spot-checked 2026-04-07`
- `3-PS2 Unit 1 Lesson 3 — Magnets Pull Without Touching`  
  `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`  
  Status: `HTTP 200 spot-checked 2026-04-07`
- `3-PS2 Unit 1 Lesson 4 — Magnetic Patterns`  
  `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html`  
  Status: `HTTP 200 spot-checked 2026-04-07`
- `3-PS2 Unit 1 Lesson 5 — Design a Magnetic Game or Tool`  
  `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`  
  Status: `HTTP 200 spot-checked 2026-04-07`
- `3-PS2 Unit 1 Lesson 6 — Test and Improve Your Force Design`  
  `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`  
  Status: `HTTP 200 spot-checked 2026-04-07`
- `3-PS2 Unit 1 Quiz — Forces & Motion`  
  `https://littlelabcoats.co/lesson-plans/gr3-ps2-unit1-quiz.html`  
  Status: `HTTP 200 spot-checked 2026-04-07`

## Supporting artifacts completed in repo

- `3-LS1` refcards for Lessons 3–6 are present in repo.
- `3-LS1 Unit 1 Quiz` is present in repo.
- `3-PS2` refcards for lessons 1–6 are present and no longer placeholder-quality.
- Current review-tracking artifacts live in:
  - `lesson-plans/gr3-life-science-batch-review.md`
  - `lesson-plans/gr3-physical-science-batch-review.md`

## Grade 3 Earth Science URLs

These Earth Science files are now live on the public domain and were verified on 2026-04-07.

- `3-ESS2 Unit 1 Lesson 1 — Weather Patterns Over Time`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Lesson 2 — Climate Regions and Conditions`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Lesson 3 — Reading Weather Data`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Lesson 4 — Weather Hazards and Impacts`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson4-weather-hazards-and-impacts.html`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Lesson 5 — Designing for Local Weather`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson5-designing-for-local-weather.html`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Lesson 6 — Reducing Weather-Related Hazards`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson6-reducing-weather-related-hazards.html`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Quiz — Weather & Climate`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-quiz.html`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Refcard 1 — Weather Patterns Over Time`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson1-weather-patterns-over-time.html`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Refcard 2 — Climate Regions and Conditions`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Refcard 3 — Reading Weather Data`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson3-reading-weather-data.html`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Refcard 4 — Weather Hazards and Impacts`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson4-weather-hazards-and-impacts.html`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Refcard 5 — Designing for Local Weather`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson5-designing-for-local-weather.html`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Refcard 6 — Reducing Weather-Related Hazards`  
  `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson6-reducing-weather-related-hazards.html`  
  Status: `live verified 2026-04-07`

## Grade 3 Engineering URLs

These Engineering files are now live on the public domain and were verified on 2026-04-07.

- `3-ETS1 Unit 1 Lesson 1 — Defining the Problem`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Lesson 2 — Researching Constraints and Materials`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson2-researching-constraints-and-materials.html`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Lesson 3 — Planning a Solution`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson3-planning-a-solution.html`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Lesson 4 — Building and Testing a Prototype`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson4-building-and-testing-a-prototype.html`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Lesson 5 — Improving the Design`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson5-improving-the-design.html`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Lesson 6 — Share and Defend Your Solution`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson6-share-and-defend-your-solution.html`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Quiz — Engineering Design`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-quiz.html`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Refcard 1 — Defining the Problem`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-refcard-lesson1-defining-the-problem.html`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Refcard 2 — Researching Constraints and Materials`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-refcard-lesson2-researching-constraints-and-materials.html`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Refcard 3 — Planning a Solution`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-refcard-lesson3-planning-a-solution.html`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Refcard 4 — Building and Testing a Prototype`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-refcard-lesson4-building-and-testing-a-prototype.html`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Refcard 5 — Improving the Design`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-refcard-lesson5-improving-the-design.html`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Refcard 6 — Share and Defend Your Solution`  
  `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-refcard-lesson6-share-and-defend-your-solution.html`  
  Status: `live verified 2026-04-07`

## Live verification sweep addendum

Full public re-check completed on 2026-04-07 for the newly shipped Grade 3 Earth Science and Engineering sets.
All in-scope URLs below returned `HTTP 200`, and the fetched page titles matched the expected lesson / refcard / quiz names.

### Earth Science full public sweep
- `gr3-ess2-unit1-lesson1-weather-patterns-over-time.html` → `200` / title matched
- `gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html` → `200` / title matched
- `gr3-ess2-unit1-lesson3-reading-weather-data.html` → `200` / title matched
- `gr3-ess2-unit1-lesson4-weather-hazards-and-impacts.html` → `200` / title matched
- `gr3-ess2-unit1-lesson5-designing-for-local-weather.html` → `200` / title matched
- `gr3-ess2-unit1-lesson6-reducing-weather-related-hazards.html` → `200` / title matched
- `gr3-ess2-unit1-quiz.html` → `200` / title matched
- `gr3-ess2-unit1-refcard-lesson1-weather-patterns-over-time.html` → `200` / title matched
- `gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html` → `200` / title matched
- `gr3-ess2-unit1-refcard-lesson3-reading-weather-data.html` → `200` / title matched
- `gr3-ess2-unit1-refcard-lesson4-weather-hazards-and-impacts.html` → `200` / title matched
- `gr3-ess2-unit1-refcard-lesson5-designing-for-local-weather.html` → `200` / title matched
- `gr3-ess2-unit1-refcard-lesson6-reducing-weather-related-hazards.html` → `200` / title matched

### Engineering full public sweep
- `gr3-ets1-unit1-lesson1-defining-the-problem.html` → `200` / title matched
- `gr3-ets1-unit1-lesson2-researching-constraints-and-materials.html` → `200` / title matched
- `gr3-ets1-unit1-lesson3-planning-a-solution.html` → `200` / title matched
- `gr3-ets1-unit1-lesson4-building-and-testing-a-prototype.html` → `200` / title matched
- `gr3-ets1-unit1-lesson5-improving-the-design.html` → `200` / title matched
- `gr3-ets1-unit1-lesson6-share-and-defend-your-solution.html` → `200` / title matched
- `gr3-ets1-unit1-quiz.html` → `200` / title matched
- `gr3-ets1-unit1-refcard-lesson1-defining-the-problem.html` → `200` / title matched
- `gr3-ets1-unit1-refcard-lesson2-researching-constraints-and-materials.html` → `200` / title matched
- `gr3-ets1-unit1-refcard-lesson3-planning-a-solution.html` → `200` / title matched
- `gr3-ets1-unit1-refcard-lesson4-building-and-testing-a-prototype.html` → `200` / title matched
- `gr3-ets1-unit1-refcard-lesson5-improving-the-design.html` → `200` / title matched
- `gr3-ets1-unit1-refcard-lesson6-share-and-defend-your-solution.html` → `200` / title matched

### Live discoverability spot checks
- `/` exposes Grade 3 Earth Science and Grade 3 Engineering lesson + quiz links in the Grade 3 section.
- `/curriculum.html` exposes Grade 3 Earth Science and Grade 3 Engineering lesson + quiz links in the Grade 3 curriculum view.
- `/curriculum/` exposes the same Grade 3 Earth Science and Grade 3 Engineering lesson + quiz links in the live curriculum route.
- No routing, visibility, or grade-placement fix was required during this verification pass.

## Integration checklist snapshot

- Preview/paywall lesson scripts for LS1, Earth Science, and Engineering use the deeper `lock-from-Materials` behavior in repo.
- `index.html`, `curriculum.html`, and `curriculum/index.html` now include Grade 3 LS1, Earth Science, and Engineering unit discoverability links in repo.
- Store CTA pattern remains `/store.html` on the newly built Grade 3 lessons and quizzes.
- Grade 3 lesson and quiz routes are now represented in repo-side catalog surfaces for LS1, Earth Science, and Engineering.
- Stable self-generated document IDs are now wired in-repo for the in-scope LS1 / ESS2 / ETS1 lessons, refcards, and quizzes.
- The authoritative mapping lives in `lesson-plans/gr3-document-id-manifest.md`.
- Representative live re-checks on 2026-04-07 returned HTTP 200 for: `gr3-ess2-unit1-lesson1-weather-patterns-over-time.html`, `gr3-ess2-unit1-quiz.html`, `gr3-ess2-unit1-refcard-lesson1-weather-patterns-over-time.html`, `gr3-ets1-unit1-lesson1-defining-the-problem.html`, `gr3-ets1-unit1-quiz.html`, `gr3-ets1-unit1-refcard-lesson1-defining-the-problem.html`, `curriculum.html`, `curriculum/`, and `/`.

## Deployment notes for the newly shipped Grade 3 work

- LS1 publish: `df77a88` — `Publish Grade 3 LS1 unit completion assets and navigation`
- LS1 verification record: `8ed1028` — `Record live verification for Grade 3 LS1 rollout`
- Earth publish: `df78991` — `Publish Grade 3 Earth Science weather unit and navigation`
- Earth verification record: `07a2eb7` — `Record live verification for Grade 3 Earth Science rollout`
- Earth support-asset verification note: `b7bfff6` — `Document Earth Science support asset verification`
- Engineering publish: `461ca34` — `Publish Grade 3 Engineering unit and navigation`
- Engineering verification record: `481728c` — `Record live verification for Grade 3 Engineering rollout`

## Final rollout manifest for newly completed Grade 3 assets

This section is the final handoff view for the newly completed Grade 3 rollout in this run.
Each listed asset is live, tied to its stable generated document ID, and backed by the review / publish / verification records referenced elsewhere in this file.

### Completion summary

- `3-LS1` completion assets in scope for this run: Rachel + Margaret review recorded, revisions applied, published live, and live verified on 2026-04-07.
- `3-ESS2 Unit 1`: Rachel + Margaret review recorded, revisions applied, published live, and live verified on 2026-04-07.
- `3-ETS1 Unit 1`: Rachel + Margaret review recorded, revisions applied, published live, and live verified on 2026-04-07.
- Stable self-generated document IDs are the implementation truth for this run and are wired in the published LS1 / ESS2 / ETS1 assets.
- Final live verification for ESS2 / ETS1 includes full public sweep results plus live navigation/discoverability checks recorded above.

### `3-LS1 Unit 1` newly completed assets

- `3-LS1 Unit 1 Lesson 3 — Plant Life Cycles and Seeds`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson3-plant-life-cycles-and-seeds.html`  
  Document ID: `doc_gr3_ls1_u1_l3`  
  Status: `live verified 2026-04-07`
- `3-LS1 Unit 1 Lesson 4 — Animal Life Cycles and Metamorphosis`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson4-animal-life-cycles-and-metamorphosis.html`  
  Document ID: `doc_gr3_ls1_u1_l4`  
  Status: `live verified 2026-04-07`
- `3-LS1 Unit 1 Lesson 5 — Comparing Life Cycle Patterns`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson5-comparing-life-cycle-patterns.html`  
  Document ID: `doc_gr3_ls1_u1_l5`  
  Status: `live verified 2026-04-07`
- `3-LS1 Unit 1 Lesson 6 — Model and Explain a Life Cycle`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-lesson6-model-and-explain-a-life-cycle.html`  
  Document ID: `doc_gr3_ls1_u1_l6`  
  Status: `live verified 2026-04-07`
- `3-LS1 Refcard — Lesson 3 Plant Life Cycles and Seeds`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-refcard-lesson3-plant-life-cycles-and-seeds.html`  
  Document ID: `doc_gr3_ls1_u1_ref_l3`  
  Status: `live verified 2026-04-07`
- `3-LS1 Refcard — Lesson 4 Animal Life Cycles and Metamorphosis`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-refcard-lesson4-animal-life-cycles-and-metamorphosis.html`  
  Document ID: `doc_gr3_ls1_u1_ref_l4`  
  Status: `live verified 2026-04-07`
- `3-LS1 Refcard — Lesson 5 Comparing Life Cycle Patterns`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-refcard-lesson5-comparing-life-cycle-patterns.html`  
  Document ID: `doc_gr3_ls1_u1_ref_l5`  
  Status: `live verified 2026-04-07`
- `3-LS1 Refcard — Lesson 6 Model and Explain a Life Cycle`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-refcard-lesson6-model-and-explain-a-life-cycle.html`  
  Document ID: `doc_gr3_ls1_u1_ref_l6`  
  Status: `live verified 2026-04-07`
- `3-LS1 Unit 1 Quiz — Life Cycles`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ls1-unit1-quiz.html`  
  Document ID: `doc_gr3_ls1_u1_quiz`  
  Status: `live verified 2026-04-07`

### `3-ESS2 Unit 1` final live assets

- `3-ESS2 Unit 1 Lesson 1 — Weather Patterns Over Time`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html`  
  Document ID: `doc_gr3_ess2_u1_l1`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Lesson 2 — Climate Regions and Conditions`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`  
  Document ID: `doc_gr3_ess2_u1_l2`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Lesson 3 — Reading Weather Data`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`  
  Document ID: `doc_gr3_ess2_u1_l3`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Lesson 4 — Weather Hazards and Impacts`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson4-weather-hazards-and-impacts.html`  
  Document ID: `doc_gr3_ess2_u1_l4`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Lesson 5 — Designing for Local Weather`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson5-designing-for-local-weather.html`  
  Document ID: `doc_gr3_ess2_u1_l5`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Lesson 6 — Reducing Weather-Related Hazards`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-lesson6-reducing-weather-related-hazards.html`  
  Document ID: `doc_gr3_ess2_u1_l6`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Quiz — Weather & Climate`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-quiz.html`  
  Document ID: `doc_gr3_ess2_u1_quiz`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Refcard 1 — Weather Patterns Over Time`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson1-weather-patterns-over-time.html`  
  Document ID: `doc_gr3_ess2_u1_ref_l1`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Refcard 2 — Climate Regions and Conditions`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson2-climate-regions-and-conditions.html`  
  Document ID: `doc_gr3_ess2_u1_ref_l2`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Refcard 3 — Reading Weather Data`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson3-reading-weather-data.html`  
  Document ID: `doc_gr3_ess2_u1_ref_l3`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Refcard 4 — Weather Hazards and Impacts`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson4-weather-hazards-and-impacts.html`  
  Document ID: `doc_gr3_ess2_u1_ref_l4`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Refcard 5 — Designing for Local Weather`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson5-designing-for-local-weather.html`  
  Document ID: `doc_gr3_ess2_u1_ref_l5`  
  Status: `live verified 2026-04-07`
- `3-ESS2 Unit 1 Refcard 6 — Reducing Weather-Related Hazards`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ess2-unit1-refcard-lesson6-reducing-weather-related-hazards.html`  
  Document ID: `doc_gr3_ess2_u1_ref_l6`  
  Status: `live verified 2026-04-07`

### `3-ETS1 Unit 1` final live assets

- `3-ETS1 Unit 1 Lesson 1 — Defining the Problem`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html`  
  Document ID: `doc_gr3_ets1_u1_l1`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Lesson 2 — Researching Constraints and Materials`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson2-researching-constraints-and-materials.html`  
  Document ID: `doc_gr3_ets1_u1_l2`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Lesson 3 — Planning a Solution`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson3-planning-a-solution.html`  
  Document ID: `doc_gr3_ets1_u1_l3`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Lesson 4 — Building and Testing a Prototype`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson4-building-and-testing-a-prototype.html`  
  Document ID: `doc_gr3_ets1_u1_l4`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Lesson 5 — Improving the Design`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson5-improving-the-design.html`  
  Document ID: `doc_gr3_ets1_u1_l5`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Lesson 6 — Share and Defend Your Solution`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-lesson6-share-and-defend-your-solution.html`  
  Document ID: `doc_gr3_ets1_u1_l6`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Quiz — Engineering Design`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-quiz.html`  
  Document ID: `doc_gr3_ets1_u1_quiz`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Refcard 1 — Defining the Problem`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-refcard-lesson1-defining-the-problem.html`  
  Document ID: `doc_gr3_ets1_u1_ref_l1`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Refcard 2 — Researching Constraints and Materials`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-refcard-lesson2-researching-constraints-and-materials.html`  
  Document ID: `doc_gr3_ets1_u1_ref_l2`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Refcard 3 — Planning a Solution`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-refcard-lesson3-planning-a-solution.html`  
  Document ID: `doc_gr3_ets1_u1_ref_l3`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Refcard 4 — Building and Testing a Prototype`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-refcard-lesson4-building-and-testing-a-prototype.html`  
  Document ID: `doc_gr3_ets1_u1_ref_l4`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Refcard 5 — Improving the Design`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-refcard-lesson5-improving-the-design.html`  
  Document ID: `doc_gr3_ets1_u1_ref_l5`  
  Status: `live verified 2026-04-07`
- `3-ETS1 Unit 1 Refcard 6 — Share and Defend Your Solution`  
  URL: `https://littlelabcoats.co/lesson-plans/gr3-ets1-unit1-refcard-lesson6-share-and-defend-your-solution.html`  
  Document ID: `doc_gr3_ets1_u1_ref_l6`  
  Status: `live verified 2026-04-07`

## What remains after this final handoff

- keep the new self-generated LS1 / ESS2 / ETS1 document IDs as the implementation truth for this run
- if future Remarq workflow changes ever require migration, use `lesson-plans/gr3-document-id-manifest.md` as the source mapping rather than re-inventing IDs ad hoc

## Scope note

- `free-gr3-egg-drop-kitchen-challenge.html` is a public Grade 3-adjacent freebie, but it is not part of the canonical LS1 / PS2 Grade 3 curriculum manifest for this handoff.
