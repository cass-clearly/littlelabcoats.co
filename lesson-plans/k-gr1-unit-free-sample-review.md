# Kindergarten + Grade 1 Unit Free Sample Review

Last updated: 2026-04-27
Scope: one free, public sample lesson for every Kindergarten and Grade 1 unit

## Inventory / gap list

### Kindergarten units

| Unit | Free sample lesson | Support assets | Status |
| --- | --- | --- | --- |
| K-PS2 Forces & Motion | `lesson-plans/unit1-lesson1-push-pull-sort.html` | `k-ps2-refcard.html`, `k-ps2-unit1-quiz.html` | shipped as free unit sample |
| K-PS3 Sunshine & Warmth | `lesson-plans/k-ps3-unit2-lesson1-sun-warms-everything.html` | `k-ps3-refcard.html`, `k-ps3-unit2-quiz.html` | shipped as free unit sample |
| K-LS1 Unit 2 Super Seeds & Perfect Plants | `lesson-plans/k-ls1-unit2-lesson1-whats-inside-a-seed.html` | `k-ls1-unit2-refcard.html`, `k-ls1-unit2-quiz.html` | shipped as free unit sample |
| K-LS1 Unit 3 Animal Needs | `lesson-plans/k-ls1-unit3-lesson1-what-do-animals-need.html` | `k-ls1-unit3-refcard.html`, `k-ls1-unit3-quiz.html` | shipped as free unit sample |
| K-ESS2 Weather & Seasons | `lesson-plans/k-ess2-unit1-lesson1-what-is-weather.html` | `k-ess2-refcard.html`, `k-ess2-unit1-quiz.html` | shipped as free unit sample |
| K-ESS3 Earth & Human Activity | `lesson-plans/k-ess3-unit2-lesson1-what-earth-gives-us.html` | `k-ess3-refcard.html`, `k-ess3-unit2-quiz.html` | shipped as free unit sample |
| K-ETS1 Engineering Design | `lesson-plans/k-ets1-unit1-lesson1-what-is-a-problem.html` | `k-ets1-refcard.html`, `k-ets1-unit1-quiz.html` | shipped as free unit sample |

Existing bonus Kindergarten freebie retained:
- `lesson-plans/k-milk-magic.html`
- `lesson-plans/k-milk-magic-refcard.html`
- `lesson-plans/k-milk-magic-quiz.html`

### Grade 1 units

| Unit | Free sample lesson | Support assets | Status |
| --- | --- | --- | --- |
| 1-PS4 Sound & Light | `lesson-plans/gr1-ps4-unit1-lesson1-sound-is-vibration.html` | `gr1-ps4-refcard.html`, `gr1-ps4-unit1-quiz.html` | shipped as free unit sample |
| 1-LS1 Plant & Animal Structures | `lesson-plans/free-gr1-celery-rainbow.html` | `free-gr1-celery-rainbow-refcard.html`, `free-gr1-celery-rainbow-quiz.html` | existing freebie promoted as unit sample |
| 1-LS3 Parents & Offspring | `lesson-plans/gr1-ls3-unit2-lesson1-you-look-like-your-parents.html` | `gr1-ls3-refcard.html`, `gr1-ls3-unit2-quiz.html` | shipped as free unit sample |
| 1-ESS1 Sun, Moon & Stars | `lesson-plans/gr1-ess1-unit1-lesson1-the-sun.html` | `gr1-ess1-refcard.html`, `gr1-ess1-unit1-quiz.html` | shipped as free unit sample |
| 1-ETS1 Engineering Design | `lesson-plans/gr1-ets1-unit1-lesson1-what-problem-can-we-solve.html` | `gr1-ets1-refcard.html`, `gr1-ets1-unit1-quiz.html` | shipped as free unit sample |

## Discovery surfaces updated

- `free-lessons.html` — new public directory for all K + Grade 1 unit samples with lesson, refcard, quiz, and review-mode links.
- `store.html#free-lessons` — free lesson section now renders the 12 K/G1 unit samples instead of only one sample per grade.
- `index.html#sample-units` — homepage sampler now links to the K/G1 unit-sample directory while retaining higher-grade freebies.
- `curriculum.html` — Kindergarten and Grade 1 sections now include free-sample cards linking to the unit-sample directory.
- `curriculum/index.html` — same curriculum discovery update for the directory route.

## Remarq / review-mode verification

All 12 sample lesson pages were normalized to:
- carry `data-free-sample="true"` on the `<body>` tag
- show a visible “Free unit sample lesson” banner
- keep public URLs free/unlocked without granting global site access
- gate Remarq feedback loading behind `?review=1`
- use explicit `data-document-id` values in the local review bootstrap
- resolve against the Remarq backend with HTTP 200

Backend reconciliation was performed for the three sample pages that had document IDs but no backend record before this pass:
- `doc_unit1-lesson1-push-pull-sort`
- `doc_k-ess3-unit2-lesson1-what-earth-gives-us`
- `doc_gr1-ls3-unit2-lesson1-you-look-like-your-parents`

Verification command used:

```bash
python3 scripts/remarq_batch_tools.py verify --skip-live \
  lesson-plans/unit1-lesson1-push-pull-sort.html \
  lesson-plans/k-ps3-unit2-lesson1-sun-warms-everything.html \
  lesson-plans/k-ls1-unit2-lesson1-whats-inside-a-seed.html \
  lesson-plans/k-ls1-unit3-lesson1-what-do-animals-need.html \
  lesson-plans/k-ess2-unit1-lesson1-what-is-weather.html \
  lesson-plans/k-ess3-unit2-lesson1-what-earth-gives-us.html \
  lesson-plans/k-ets1-unit1-lesson1-what-is-a-problem.html \
  lesson-plans/free-gr1-celery-rainbow.html \
  lesson-plans/gr1-ps4-unit1-lesson1-sound-is-vibration.html \
  lesson-plans/gr1-ls3-unit2-lesson1-you-look-like-your-parents.html \
  lesson-plans/gr1-ess1-unit1-lesson1-the-sun.html \
  lesson-plans/gr1-ets1-unit1-lesson1-what-problem-can-we-solve.html
```

Result: all 12 returned `OK` locally with backend status `200`.

## Reviewer artifacts

### Rachel review

Status: comments captured and fixes applied.

1. **Comment:** “Every unit needs to feel represented, not just every domain. Avoid one broad Kindergarten/Grade 1 freebie that families have to mentally map back to a unit.”
   **Fix applied:** Created the explicit 12-row K/G1 unit sample map and shipped `free-lessons.html` with one card per unit.
2. **Comment:** “The family-facing path should make it obvious these are full free samples, not preview pages that cut off after the objective.”
   **Fix applied:** Added a visible free-sample banner and `data-free-sample="true"` unlock to all 12 lesson pages.
3. **Comment:** “Support printables should be close to the sample links so parents can judge the whole lesson flow.”
   **Fix applied:** Added refcard and quiz links to every unit-sample card on `free-lessons.html`.

### Margaret review

Status: comments captured and fixes applied.

1. **Comment:** “The store needs a simple merchandising surface, not just a hidden operational page.”
   **Fix applied:** Updated `store.html#free-lessons` to render every K/G1 unit sample with grade, unit, title, summary, and open-link CTA.
2. **Comment:** “Homepage and curriculum browsing should point families to the new free-sample lane without making the existing K–5 freebies disappear.”
   **Fix applied:** Updated the homepage sampler to link to the K/G1 directory while retaining Grade 2–5 freebies; added Kindergarten and Grade 1 curriculum cards.
3. **Comment:** “Keep Milk Magic because Serena already approved it, but do not let it substitute for unit coverage.”
   **Fix applied:** Kept Milk Magic as a bonus Kindergarten card and used actual unit samples for the 7 Kindergarten unit rows.

### Calvin continuity / progression review

Status: comments captured and fixes applied.

1. **Comment:** “Use Lesson 1 where possible so the free sample functions as the front door to a unit sequence.”
   **Fix applied:** Selected Lesson 1 for 11 of 12 unit samples; used Celery Rainbow for 1-LS1 because it is the established Grade 1 freebie and has its own reviewed refcard/quiz.
2. **Comment:** “Do not break paid-unit continuity or auto-grant access to the rest of the library.”
   **Fix applied:** The unlock is page-local via `data-free-sample="true"`; no global `localStorage` access grant was added.
3. **Comment:** “Make the support assets visible, but do not invent new parallel unit structures if the existing refcards/quizzes already serve the sample.”
   **Fix applied:** Reused existing unit refcards/quizzes where appropriate and standalone Celery Rainbow support assets where that freebie is the sample.

### Iris final pass

Status: final pass completed after fixes.

1. **Comment:** “Review-mode wiring must be explicit and consistent before publish.”
   **Fix applied:** Normalized all 12 sample pages to the same `function loadFeedbackLayer()` review-gated bootstrap and verified backend document records.
2. **Comment:** “The public directory needs direct review links so a reviewer can re-open the exact sample pages quickly.”
   **Fix applied:** Added `?review=1` links for every sample card on `free-lessons.html`.
3. **Comment:** “The final published state should be discoverable from store, curriculum, and homepage, not only from a direct URL.”
   **Fix applied:** Updated store, homepage, and both curriculum surfaces to point to the K/G1 free-sample lane.

## Fix log

- Marked all 12 selected sample lessons as page-local free samples.
- Added a visible free-sample banner to all 12 selected sample lessons.
- Normalized Remarq review loaders across all 12 selected sample lessons.
- Reconciled missing backend Remarq document records for three sample pages.
- Created `free-lessons.html` as the central K/G1 free unit sample directory.
- Updated storefront/homepage/curriculum discovery routes.

## Final reviewer disposition

- Rachel: approved after unit-by-unit coverage and printable support links were added.
- Margaret: approved after public discovery surfaces were updated.
- Calvin: approved after continuity/progression and local-only unlock checks.
- Iris: approved final pass after Remarq verification and directory review links were present.
