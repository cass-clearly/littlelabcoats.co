# Grade 4 Life Science Unit 1 Lesson 2 — Remarq Baseline

Last updated: 2026-04-09
Status: baseline captured before revision edits
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

### Open lesson-specific comments to use as revision input

#### A. Materials and lesson-support asset clarity
1. `cmt_IUsYk9D75g4` — Serena Salvato
   - Quote: `animal photos or simple observation cards`
   - Comment: `supply these with the lessons`
   - Revision implication: clarify whether lesson-native observation cards/images are included, or reword the materials list so it does not imply missing provided assets.

2. `cmt_5wTOgmamF8Q` — Serena Salvato
   - Quote: `paper tub`
   - Comment: `give examples are we talking straw or toilet roll tube`
   - Revision implication: make the materials list and activity wording concrete by naming an age-appropriate tube example.

#### B. Procedure-step clarity and activity flow
3. `cmt_LaTi5_pzAzg` — Serena Salvato
   - Quote: `Have students record one structure, one type of information it detects, and one survival behavior it supports.`
   - Comment: `This is unclear what the step is asking 4. Make it more explicit`
   - Revision implication: rewrite Step 4 so the student task is explicit and connected to the worksheet.

4. `cmt_ICYW7DoUQsw` — Serena Salvato
   - Quote: `sight`
   - Comment: `change this to smell. It's more fun. And encorporate it into the main lesson. It's more dynamic and interesting. Integrate into step 4`
   - Revision implication: replace the current sight-only extension comparison with a smell-based activity and pull that idea into the main lesson flow rather than leaving it only in Extensions.

#### C. Worksheet sequencing / student-direction clarity
5. `cmt_155TFGieedk` — Serena Salvato
   - Quote: `Sensory Detective`
   - Comment: `is this step 2? Can we make this clearer?`
   - Revision implication: label or cue when students should complete the `Sensory Detective` worksheet section.

6. `cmt_n2qIxYe2lyo` — Serena Salvato
   - Quote: `because`
   - Comment: `Which step is this? Make it clear when this is to be completed by the student`
   - Revision implication: label or cue when students should complete the `Claim Box` section.

## Revision checklist for the next implementation chunk

### Content / materials updates
- Clarify whether the lesson includes observation cards or otherwise remove ambiguity around supplied animal visuals.
- Replace vague `paper tube` wording with a concrete example.

### Lesson-flow updates
- Make Step 4 explicit about what students do, what they record, and which worksheet section they use.
- Integrate a smell-based sensory activity into the main procedure, per Serena’s comment, instead of keeping the alternate-sense idea only in the extension.

### Worksheet / direction updates
- Add explicit worksheet timing/cues for `Sensory Detective`.
- Add explicit worksheet timing/cues for `Claim Box`.

### Parity check item
- After lesson edits, review the paired refcard for wording parity on materials and the `Try this next` sensory activity.

## Baseline public review-mode check

Live check completed against:
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html?review=1`

### Availability
- HTTP status: `200`
- Live page exposes `data-document-id="doc_tHdONv_mztI"`
- Live page still contains the current wording that Serena commented on, including:
  - `paper tube or blindfold for a quick limited-senses demo`
  - Step 4 wording about recording structure / information / behavior
  - worksheet headings `Sensory Detective` and `Claim Box`

### Current LLC structure confirmed on the live lesson page
- canonical link tag present
- lesson shell present: title, subtitle, grade/duration/subject meta, hero, NGSS box, lesson path, Big Idea, Science, Materials, procedure steps, discussion questions, extension, teacher notes, worksheet, answer key
- review/paywall wiring present via `feedback-layer.js` with API base `https://cassclearly.com`
- review-mode URL is available for later post-push verification

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
- no lesson-content edits yet
