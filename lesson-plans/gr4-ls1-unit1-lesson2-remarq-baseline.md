# Grade 4 Life Science Unit 1 Lesson 2 — Remarq Baseline

Last updated: 2026-04-09
Status: revision follow-up checked after lesson updates and live review verification
Target: `Grade 4 Life Science → Animal Structures & Survival → Unit 1 Lesson 2`

## Canonical lesson + route confirmation

### Lesson page
- Repo file: `lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html`
- Public route: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html`
- Public review route: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html?review=1`
- Remarq document ID: `doc_tHdONv_mztI`

Confirmation sources:
- `lesson-plans/index.html` lists **Sensing the World** as `Unit 1 • Lesson 2` with both open and review-mode links.
- `lesson-plans/gr4-document-id-manifest.md` maps `gr4-ls1-unit1-lesson2-sensing-the-world.html` to `doc_tHdONv_mztI`.
- `lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html` exposes `data-document-id="doc_tHdONv_mztI"` and canonical URL `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html`.

### Coupled asset likely to matter in follow-on review
- Repo file: `lesson-plans/gr4-ls1-unit1-refcard-lesson2-sensing-the-world.html`
- Public review route: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson2-sensing-the-world.html?review=1`
- Remarq document ID: `doc_QUcUw6IL6uU`

Reason to watch it in later chunks:
- The refcard repeats the current materials wording (`animal photos or simple observation cards`, `paper tube or blindfold`) and the current extension wording (`touch only, then by sight only`), so lesson changes may require parity updates.

## Existing Remarq comment inventory for the lesson

All current comments on `doc_tHdONv_mztI` were reviewed from the live Remarq backend.

### Already-addressed batch feedback still visible in Remarq
1. `cmt_cmqjrg03Pgs` — Rachel — 2026-04-08
   - Comment: tighten the compare prompt so students must name the sensory structure, the information it detects, and the survival behavior it supports for each animal.
   - Baseline disposition: appears already applied in the live lesson worksheet prompt and answer-key language.

### Lesson-specific comment resolution status after the current revision pass

#### Resolved lesson comments
1. `cmt_IUsYk9D75g4` — Serena Salvato
   - Quote: `animal photos or simple observation cards`
   - Resolution now visible in lesson: materials now say `2–4 animal photos from a nature book, magazine, or device`, which removes the implication that missing observation cards are supplied with the lesson.

2. `cmt_5wTOgmamF8Q` — Serena Salvato
   - Quote: `paper tub`
   - Resolution now visible in lesson: materials and Step 1 now explicitly say `toilet paper roll or paper towel tube`.

3. `cmt_LaTi5_pzAzg` — Serena Salvato
   - Quote: `Have students record one structure, one type of information it detects, and one survival behavior it supports.`
   - Resolution now visible in lesson: Step 4 now explicitly tells students to complete a second `Sensory Detective` row and finish the `Claim Box` with one full sentence naming the structure, the information it detects, and how that helps survival or behavior.

4. `cmt_ICYW7DoUQsw` — Serena Salvato
   - Quote: `sight`
   - Resolution now visible in lesson: the smell challenge is now part of Step 4 in the main lesson flow, and the extension no longer carries the main sensory-activity move by itself.

5. `cmt_155TFGieedk` — Serena Salvato
   - Quote: `Sensory Detective`
   - Resolution now visible in lesson: the worksheet now says `Use during Step 2 and Step 4`, and Step 2 explicitly tells families when to begin the table.

6. `cmt_n2qIxYe2lyo` — Serena Salvato
   - Quote: `because`
   - Resolution now visible in lesson: the worksheet now says `Complete during Step 4`, and Step 4 explicitly tells families when to finish the `Claim Box`.

#### Remaining comment status
- No unaddressed actionable lesson-page comments remain from the current Remarq revision pass.
- `cmt_cmqjrg03Pgs` remains a non-regression item and is still reflected in the compare prompt / answer-key expectations.

## Post-revision checklist status

### Lesson-page comment fixes
- observation-card ambiguity removed on the lesson page
- concrete tube example added on the lesson page
- Step 4 rewritten to be explicit and worksheet-linked
- smell activity moved into the main lesson flow
- `Sensory Detective` timing cue added
- `Claim Box` timing cue added

### Parity watch item still worth a later follow-up
- the paired refcard still reflects older wording and should be reviewed separately for parity on materials / science summary / family follow-up language

## Live review-mode verification after current revisions

Live checks completed against:
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html?review=1`

### Availability and updated content
- HTTP status: `200`
- Live page exposes `data-document-id="doc_tHdONv_mztI"`
- Live page contains the updated lesson wording, including:
  - `Sensory structures help animals gather clues.`
  - Step 4 smell-challenge wording
  - worksheet cue `Use during Step 2 and Step 4`

### Remarq wiring confirmed live
- live page still loads `feedback-layer.js?v=20260408` from `https://cassclearly.com`
- live page still exposes the matching lesson document ID in both `<body>` and the feedback-layer script tag
- live page still contains the `?review=1` unlock logic for review mode
- `https://cassclearly.com/feedback-layer.js?v=20260408` returned HTTP `200`

### Live review/edit UI presence confirmed
A headless browser check against the public `?review=1` URL confirmed:
- `.fb-sidebar` present
- `.fb-sidebar-tab` present
- feedback-layer styles for annotation / comment UI loaded
- full review content visible in review mode, including the worksheet

Disposition:
- review mode loads on the correct live lesson page
- Remarq review/edit UI is present on the public review URL
- the updated lesson content is the content currently served on the live review page
- the lesson is structurally aligned, science-tightened, and ready for Serena review on the public review URL

### Final Serena review link
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html?review=1`

### Print-sensitive sections identified for preservation
- print button present in live page
- `@media print` rules exist and currently hide the print button and paywall overlay
- print-sensitive boxed sections currently used throughout the lesson:
  - `standards-box`
  - `materials-box`
  - `procedure-step`
  - `question-box`
  - `teacher-note`
  - `worksheet-card`
  - `answer-key`
  - `extension-box`
- page-break boundaries currently matter for:
  - worksheet section
  - answer-key section

### Coupled asset baseline spot-check
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson2-sensing-the-world.html?review=1` exposes `data-document-id="doc_QUcUw6IL6uU"`
- current refcard still mirrors the pre-revision sensory activity wording and material wording, so it should be checked after lesson edits for consistency

## Out of scope for this chunk
- no PDF generation
- no export work
- refcard parity cleanup remains for a later chunk
