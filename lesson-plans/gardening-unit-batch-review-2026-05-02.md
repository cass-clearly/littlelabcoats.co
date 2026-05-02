# Garden Detectives Gardening Unit — Batch Review

Last updated: 2026-05-02
Scope: mixed-age gardening buyer unit anchored by `lesson-plans/free-garden-detectives-soil-seed-sun.html`
Status: Round 1 reviewer notes captured; fixes applied; local verification completed.

## Source-of-truth package

- `lesson-plans/free-garden-detectives-soil-seed-sun.html` — Lesson 1 free sample anchor
- `lesson-plans/gardening-unit-lesson2-leaf-detective-lab.html`
- `lesson-plans/gardening-unit-lesson3-plant-parts-on-the-job.html`
- `lesson-plans/gardening-unit-lesson4-weed-wildflower-wanted-guest.html`
- `lesson-plans/gardening-unit-lesson5-perennials-annuals-garden-planning.html`
- `lesson-plans/gardening-unit-lesson6-pollinator-party-wildflower-garden-design.html`
- `lesson-plans/gardening-unit-refcard.html`
- `lesson-plans/gardening-unit-quiz.html`
- `lesson-plans/gardening-unit-observation-pages.html`
- `lesson-plans/gardening-unit-vocabulary-cards.html`
- `lesson-plans/gardening-unit-mini-posters.html`
- `lesson-plans/gardening-unit-garden-journal-cover.html`
- `lesson-plans/review/gardening-unit-review.html`
- `gardening-unit-download.html`
- `ops/gardening-unit-welcome-email.txt`

## Round 1 — Rachel style/content review

Status: `commented — revision pass applied`

1. **Target:** Lesson 2 Leaf Detective Lab
   **Observation:** Strong hook, but the activity must not become plant-ID trivia.
   **Required fix:** Keep the page centered on observable leaf evidence before naming plants.
   **Resolution:** Lesson 2 now says “No guessing yet — only clues,” uses shape/edge/vein/texture evidence, and treats app/ID lookup only as an extension after student observations.

2. **Target:** Lesson 3 Plant Parts on the Job
   **Observation:** The celery/flower dye demo needs a clear visible-evidence moment for parents.
   **Required fix:** Add explicit colored-tube inspection and parent coaching.
   **Resolution:** Lesson 3 includes a cross-section inspection step, “tiny tubes” answer-key language, and a structure/function worksheet.

3. **Target:** Bonus content
   **Observation:** Buyer value should feel useful, not bloated.
   **Required fix:** Keep extras printable and reusable across the unit.
   **Resolution:** Added observation pages, vocabulary cards, mini posters, and garden journal cover; no heavy extra activities beyond the promised pack.

## Round 1 — Margaret family-execution review

Status: `commented — revision pass applied`

1. **Target:** Whole unit
   **Observation:** The lane must stay practical for a parent at home with ordinary materials.
   **Required fix:** Avoid specialty supplies and make each lesson executable indoors or outdoors.
   **Resolution:** Each lesson uses household materials, outdoor samples/photos as alternatives, and explicit parent notes for safety and substitutions.

2. **Target:** Lesson 4 Weed/Wildflower/Wanted Guest
   **Observation:** “Weed” can easily become moralizing or inaccurate.
   **Required fix:** Frame weeds as goal/context decisions and include safety language.
   **Resolution:** Lesson 4 now defines weeds as plants growing where they conflict with the current goal, includes pull/protect/move reasoning, and warns against handling unknown/pesticide-treated plants.

3. **Target:** Review/download usability
   **Observation:** A buyer pack needs one clear hub, not a pile of filenames.
   **Required fix:** Add a review/download hub and hosted redirect.
   **Resolution:** Added `lesson-plans/review/gardening-unit-review.html` and `gardening-unit-download.html`.

## Round 1 — Calvin continuity/progression review

Status: `approved after revision`

Verdict: The six-lesson lane now has real progression: site evidence → leaf evidence → structure/function mechanism → garden belonging decisions → seasonal/constraint planning → pollinator design capstone. Each lesson has a distinct job and would leave a real gap if removed.

### Lesson-by-lesson findings

1. **Lesson 1 — Soil, Seeds & Sun:** anchor / initial evidence; keep as the free sample.
2. **Lesson 2 — Leaf Detective Lab:** observe and classify evidence; distinct from soil because the evidence source is leaf structure.
3. **Lesson 3 — Plant Parts on the Job:** explain mechanism and structure/function; adds dye transport evidence.
4. **Lesson 4 — Weed, Wildflower, or Wanted Guest?:** apply evidence to garden goals and ecological tradeoffs; adds human decision-making.
5. **Lesson 5 — Perennials, Annuals & Garden Planning:** compare life-cycle/season choices and plan with constraints; raises design demand.
6. **Lesson 6 — Pollinator Party & Wildflower Garden Design:** synthesize unit evidence into a design capstone; highest reasoning demand.

### Calvin urgent actions now

- Keep the mixed-age differentiation visible in each lesson.
- Preserve Lesson 6 as a true synthesis, not just a poster craft.

### Resolution

- Every lesson includes age 4 / age 9 / age 12 roles.
- Lesson 6 requires explicit design criteria, constraints, and evidence from earlier lessons.

## Round 1 — Iris final QA / render / review-mode pass

Status: `passed locally`

### QA checklist

- Lesson 1 remains the free anchor and its roadmap topics are preserved.
- Lessons 2–6 exist with semantic document IDs and review-mode bootstrap.
- Bonus observation pages, vocabulary cards, mini posters, and garden journal cover exist.
- Review hub links to all buyer artifacts using `?review=1`.
- Hosted download redirect points to the review/download hub.
- Local HTTP checks returned 200 for every new HTML file and review URL.
- Review-mode marker check found the expected document ID and feedback-layer bootstrap in every new buyer artifact.

## Comment-to-change resolution log

| Reviewer | Exact requirement | File evidence | Status |
| --- | --- | --- | --- |
| Rachel | Do not make Lesson 2 plant-ID trivia; use observable leaf evidence first. | `gardening-unit-lesson2-leaf-detective-lab.html` evidence-first flow and answer key. | adopted |
| Rachel | Make Lesson 3 dye-demo evidence visible and parent-coachable. | `gardening-unit-lesson3-plant-parts-on-the-job.html` colored-tube inspection + answer key. | adopted |
| Rachel | Bonus content should add buyer value without bloat. | Four promised reusable bonus printables only. | adopted |
| Margaret | Keep materials ordinary and parent-executable. | Materials lists and parent notes in Lessons 2–6. | adopted |
| Margaret | Frame weeds accurately as goal/context decisions. | Lesson 4 pull/protect/move evidence workflow. | adopted |
| Margaret | Add one clear buyer hub. | `lesson-plans/review/gardening-unit-review.html` and `gardening-unit-download.html`. | adopted |
| Calvin | Distinct progression and lesson jobs. | Lesson sequence from evidence gathering to capstone design. | adopted |
| Iris | Review/download links render locally and use review mode. | Verification log below. | adopted |

## Verification log

Commands run in this pass:

```bash
python3 tmp/build_gardening_unit.py
python3 scripts/remarq_batch_tools.py reconcile [new buyer artifact paths]
python3 scripts/remarq_batch_tools.py verify --json --skip-live [new buyer artifact paths]
python3 scripts/generate-lesson-index-data.py
python3 -m http.server 8765
curl -I http://127.0.0.1:8765/[new paths]
curl -I http://127.0.0.1:8765/[new paths]?review=1
python3 tmp/verify_gardening_unit.py
```

Observed results in this pass:

- Remarq reconcile inserted 11 backend documents for the new buyer artifacts.
- Remarq verify with `--skip-live` returned `ok: true`; backend status `200` for all 11 new buyer artifact document IDs.
- Local HTTP verification returned `200` for 24 routes: each new lesson/bonus artifact with and without `?review=1`, plus `lesson-plans/review/gardening-unit-review.html` and `gardening-unit-download.html`.
- Review-mode marker verification found the expected `feedback-layer.js?v=20260421` bootstrap in every new buyer artifact.
- Headless Chrome render checks wrote screenshots for Lesson 2 review mode and the review hub to `tmp/gardening-unit-checks/lesson2-review.png` and `tmp/gardening-unit-checks/review-hub.png` during the verification run.

Public deploy verification is not claimed in this artifact.
