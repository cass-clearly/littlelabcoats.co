# Kindergarten + Grade 1 Standalone Free Sample Replacement Review

Last updated: 2026-04-27
Scope: replace the previously shipped K/G1 free-sample lane that incorrectly mapped existing paid-unit Lesson 1 pages as freebies.

## Replacement disposition

The previous interpretation has been replaced. The free-sample lane no longer uses canonical paid-unit Lesson 1 pages as the K/G1 freebies.

Removed/replaced incorrect public mappings:

- K-PS2 previously mapped to `lesson-plans/unit1-lesson1-push-pull-sort.html` → replaced with `lesson-plans/free-k-ps2-ramp-roll-rescue.html`
- K-PS3 previously mapped to `lesson-plans/k-ps3-unit2-lesson1-sun-warms-everything.html` → replaced with `lesson-plans/free-k-ps3-sunshine-color-watch.html`
- K-LS1 Unit 2 previously mapped to `lesson-plans/k-ls1-unit2-lesson1-whats-inside-a-seed.html` → replaced with `lesson-plans/free-k-ls1-unit2-sprout-needs-detective.html`
- K-LS1 Unit 3 previously mapped to `lesson-plans/k-ls1-unit3-lesson1-what-do-animals-need.html` → replaced with `lesson-plans/free-k-ls1-unit3-animal-home-checkup.html`
- K-ESS2 previously mapped to `lesson-plans/k-ess2-unit1-lesson1-what-is-weather.html` → replaced with `lesson-plans/free-k-ess2-weather-window-station.html`
- K-ESS3 previously mapped to `lesson-plans/k-ess3-unit2-lesson1-what-earth-gives-us.html` → replaced with `lesson-plans/free-k-ess3-earth-treasure-sort.html`
- K-ETS1 previously mapped to `lesson-plans/k-ets1-unit1-lesson1-what-is-a-problem.html` → replaced with `lesson-plans/free-k-ets1-paper-bridge-rescue.html`
- 1-PS4 previously mapped to `lesson-plans/gr1-ps4-unit1-lesson1-sound-is-vibration.html` → replaced with `lesson-plans/free-gr1-ps4-cup-string-sound-sender.html`
- 1-LS1 previously promoted `lesson-plans/free-gr1-celery-rainbow.html` as the unit sample → replaced with `lesson-plans/free-gr1-ls1-bird-beak-tool-test.html`
- 1-LS3 previously mapped to `lesson-plans/gr1-ls3-unit2-lesson1-you-look-like-your-parents.html` → replaced with `lesson-plans/free-gr1-ls3-family-trait-detectives.html`
- 1-ESS1 previously mapped to `lesson-plans/gr1-ess1-unit1-lesson1-the-sun.html` → replaced with `lesson-plans/free-gr1-ess1-shadow-clock-mini-lab.html`
- 1-ETS1 previously mapped to `lesson-plans/gr1-ets1-unit1-lesson1-what-problem-can-we-solve.html` → replaced with `lesson-plans/free-gr1-ets1-pencil-holder-redesign.html`

## New standalone unit sample inventory

Each row has a new lesson, matching reference card, and matching quiz. None of the lesson pages below are reused canonical paid-unit lesson pages.

| Unit | New standalone lesson | Support assets |
| --- | --- | --- |
| K-PS2 Forces & Motion | `free-k-ps2-ramp-roll-rescue.html` | `free-k-ps2-ramp-roll-rescue-refcard.html`, `free-k-ps2-ramp-roll-rescue-quiz.html` |
| K-PS3 Sunshine & Warmth | `free-k-ps3-sunshine-color-watch.html` | `free-k-ps3-sunshine-color-watch-refcard.html`, `free-k-ps3-sunshine-color-watch-quiz.html` |
| K-LS1 Unit 2 Plants | `free-k-ls1-unit2-sprout-needs-detective.html` | `free-k-ls1-unit2-sprout-needs-detective-refcard.html`, `free-k-ls1-unit2-sprout-needs-detective-quiz.html` |
| K-LS1 Unit 3 Animal Needs | `free-k-ls1-unit3-animal-home-checkup.html` | `free-k-ls1-unit3-animal-home-checkup-refcard.html`, `free-k-ls1-unit3-animal-home-checkup-quiz.html` |
| K-ESS2 Weather & Seasons | `free-k-ess2-weather-window-station.html` | `free-k-ess2-weather-window-station-refcard.html`, `free-k-ess2-weather-window-station-quiz.html` |
| K-ESS3 Earth & Human Activity | `free-k-ess3-earth-treasure-sort.html` | `free-k-ess3-earth-treasure-sort-refcard.html`, `free-k-ess3-earth-treasure-sort-quiz.html` |
| K-ETS1 Engineering | `free-k-ets1-paper-bridge-rescue.html` | `free-k-ets1-paper-bridge-rescue-refcard.html`, `free-k-ets1-paper-bridge-rescue-quiz.html` |
| 1-PS4 Sound & Light | `free-gr1-ps4-cup-string-sound-sender.html` | `free-gr1-ps4-cup-string-sound-sender-refcard.html`, `free-gr1-ps4-cup-string-sound-sender-quiz.html` |
| 1-LS1 Plant & Animal Structures | `free-gr1-ls1-bird-beak-tool-test.html` | `free-gr1-ls1-bird-beak-tool-test-refcard.html`, `free-gr1-ls1-bird-beak-tool-test-quiz.html` |
| 1-LS3 Parents & Offspring | `free-gr1-ls3-family-trait-detectives.html` | `free-gr1-ls3-family-trait-detectives-refcard.html`, `free-gr1-ls3-family-trait-detectives-quiz.html` |
| 1-ESS1 Sun, Moon & Stars | `free-gr1-ess1-shadow-clock-mini-lab.html` | `free-gr1-ess1-shadow-clock-mini-lab-refcard.html`, `free-gr1-ess1-shadow-clock-mini-lab-quiz.html` |
| 1-ETS1 Engineering | `free-gr1-ets1-pencil-holder-redesign.html` | `free-gr1-ets1-pencil-holder-redesign-refcard.html`, `free-gr1-ets1-pencil-holder-redesign-quiz.html` |

## Discovery surfaces updated

- `free-lessons.html` now presents only the 12 new standalone K/G1 unit samples in the unit-sample lane, with lesson, refcard, quiz, and review links.
- `store.html#free-lessons` now renders the 12 new K/G1 standalone unit samples instead of the rejected canonical Lesson 1 mappings; higher-grade standalone freebies remain below them.
- `index.html#sample-units` now uses the new K-PS2 Ramp Roll Rescue and Grade 1 Cup-String Sound Sender samples for the K/G1 featured sample tabs and links to the new unit-sample directory.
- `curriculum.html` and `curriculum/index.html` now include prominent K and Grade 1 cards linking to the new standalone unit-sample directories and no longer promote Celery Rainbow as the Grade 1 unit sample.

## Remarq / review-mode wiring

All 36 new files use explicit document IDs and a review-gated feedback bootstrap:

- public URL: no review controls should be created by runtime script unless `?review=1` is present
- review URL: inline `loadFeedbackLayer()` appends `/feedback-layer.js?v=20260421`
- backend: document IDs reconciled to real Remarq backend records
- normal pages carry `data-free-sample="standalone-k-gr1-2026-04-27"`

Verification command used:

```bash
xargs python3 scripts/remarq_batch_tools.py verify --skip-live < /tmp/new_free_paths.txt
```

Result: all 36 new lesson/refcard/quiz files returned `OK` with backend status `200`.

## Reviewer artifacts and fix log

### Rachel review — curriculum/age fit

Status: comments captured and fixes applied.

1. **Comment:** “The replacement cannot just rename Lesson 1. Each unit needs a genuinely new experience that still previews the unit’s core science.”
   **Fix applied:** Created 12 new standalone lesson concepts: ramp rescue, sunshine color watch, sprout-needs detective, animal-home checkup, weather-window station, Earth-treasure sort, paper bridge rescue, cup-string sound sender, bird-beak tool test, family-trait detectives, shadow-clock mini lab, and pencil-holder redesign.
2. **Comment:** “Kindergarten samples need concrete noticing, short explanations, and low-writing worksheets.”
   **Fix applied:** Kindergarten worksheets use simple comparison tables, drawing boxes, and parent-guided evidence prompts; long-form writing is limited to short evidence lines.
3. **Comment:** “Grade 1 should feel a step more evidence-rich than K without becoming dense.”
   **Fix applied:** Grade 1 samples add explicit vocabulary and claim/evidence prompts while keeping the investigations short and household-material based.

### Margaret review — merchandising/discovery

Status: comments captured and fixes applied.

1. **Comment:** “The free lesson hub must plainly say the old interpretation was replaced, otherwise families and internal reviewers will still see the old Lesson 1 lane.”
   **Fix applied:** Updated `free-lessons.html` hero and summary to say these are brand-new standalone samples and that the previous canonical-Lesson-1 mapping was replaced.
2. **Comment:** “The store should show all new K/G1 freebies, not just one generic free lesson per grade.”
   **Fix applied:** Updated `store.html#free-lessons` to render all 12 corrected K/G1 unit samples before the higher-grade freebies.
3. **Comment:** “Homepage and curriculum surfaces need to point to the corrected lane and stop promoting Celery as the Grade 1 unit sample.”
   **Fix applied:** Updated `index.html`, `curriculum.html`, and `curriculum/index.html`; Celery Rainbow remains as an older standalone file but is not used as the Grade 1 unit sample.

### Calvin continuity/progression review

Status: comments captured and fixes applied.

1. **Comment:** “Do not break paid-unit continuity by making the actual paid Lesson 1 pages free.”
   **Fix applied:** New sample filenames are all `free-k-*` / `free-gr1-*`; canonical paid-unit Lesson 1 URLs remain paid preview/unit URLs and are no longer mapped as freebies.
2. **Comment:** “Each sample should tease the unit theme without duplicating the unit sequence’s opener.”
   **Fix applied:** Each sample uses a related but distinct task: for example K-PS2 uses a ramp rescue rather than Push & Pull Sort, 1-ESS1 uses shadow tracing rather than The Sun, and 1-LS3 uses family trait cards rather than the paid parent/offspring opener.
3. **Comment:** “Support assets should not be afterthoughts.”
   **Fix applied:** Every new lesson has a matching one-page reference card and a quiz with short-response guidance.

### Iris final QA/review-mode pass

Status: comments captured and fixes applied.

1. **Comment:** “Every reviewable file needs an explicit real document ID and consistent review-mode loader.”
   **Fix applied:** Added deterministic `doc_free_*` IDs to all 36 files, reconciled backend records, and verified all 36 with `scripts/remarq_batch_tools.py verify --skip-live`.
2. **Comment:** “The review links should resolve from the public discovery hub.”
   **Fix applied:** Added `?review=1` links for all 12 lesson pages on `free-lessons.html`; review index was regenerated.
3. **Comment:** “Do not claim Gemini/image work if no image generation was needed.”
   **Fix applied:** Used only clear, common emoji/print CSS visuals where the object/concept was obvious; no Gemini dependency was required and no generated-image claim is made.

## Final reviewer disposition

- Rachel: approved after K/G1 age-fit and original-lesson checks.
- Margaret: approved after free hub, store, homepage, and curriculum discovery surfaces were corrected.
- Calvin: approved after paid-unit continuity and non-duplication checks.
- Iris: approved after Remarq backend/review-mode verification passed for all 36 new files.

## Current handoff state

- New standalone K/G1 free sample lane is ready to publish from the corrected free hub, store free section, homepage sampler, and curriculum free-sample cards.
- Previous canonical-Lesson-1 freebie mappings have been replaced on those public free-sample discovery surfaces.
- Remaining deployment step: commit, push to `origin/main`, and verify public URLs after GitHub Pages/edge propagation.
