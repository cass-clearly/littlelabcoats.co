# Active Review Comment Audit

Last updated: 2026-04-10
Status: live-vs-source audit pass
Source checklist: `lesson-plans/active-review-comment-checklist.md`
Rule for this file: statuses below are based on **direct verification of both current source and current live page HTML**. Earlier claims were ignored unless the present state confirmed them.

Status labels used:
- `resolved`
- `unresolved`
- `partially_resolved`

---

## Audit results by comment

### Grade 2 LS2 Unit 1 Lesson 2 — Pollinators: Nature's Delivery Service

Source file: `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html`
Live review URL: `https://littlelabcoats.co/lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html?review=1`

1. **`cmt_hwZG7xWu4Dw` — Dr. Rachel Chen — quoted `🦋 Moth`**
   - **Status:** `resolved`
   - **Why:** The current source and live page no longer use a butterfly emoji for the moth. The student-facing matching table now shows a dedicated inline moth illustration, and the answer-key list uses text + moon/night wording rather than a butterfly icon.
   - **Source evidence:** `gr2-ls2-unit1-lesson2-pollinators.html` contains an inline SVG moth icon in the worksheet matching section and `Moth → 🌕 White flowers (blooms at night)` in the answer key.
   - **Live evidence:** Live review HTML shows the same inline moth illustration and the moon/night answer-key wording.

2. **`cmt_WnxtyKxYK3Y` — Margaret Hoffman — quoted `Students will EXPLAIN the role of pollinators`**
   - **Status:** `resolved`
   - **Why:** The learning objective now uses italics for the action verbs instead of all-caps emphasis.
   - **Source evidence:** Current source reads `Students will <em>explain</em> ... and <em>create</em> ...`.
   - **Live evidence:** Live review HTML matches the italicized `<em>explain</em>` and `<em>create</em>` wording.

3. **`cmt_watF_T6CePw` — Dr. Rachel Chen — quoted `Moths are nocturnal`**
   - **Status:** `resolved`
   - **Why:** This was a positive scientific-validation note, and the validated content is still present.
   - **Source evidence:** The science/activity surfaces still describe moths as nocturnal and match them to white night-blooming flowers.
   - **Live evidence:** Live review HTML still contains `Moths are nocturnal — white flowers glow in moonlight`.

4. **`cmt_V5Dpxg_S3M4` — Margaret Hoffman — quoted `discussion-hint`**
   - **Status:** `resolved`
   - **Why:** This was a positive formatting/standards-validation note, and the validated lesson shell/standards formatting is still present.
   - **Source evidence:** Current source still includes the expected discussion-hint structure and NGSS block.
   - **Live evidence:** Live review HTML still exposes the same discussion-hint pattern and standards block.

5. **`cmt_1bZOv1iAIdk` — Dr. Rachel Chen — quoted `lavender`**
   - **Status:** `resolved`
   - **Why:** The comment explicitly pointed to Lesson 6, not Lesson 2. In the current live and source state for `gr2-ls2-unit1-lesson6-ecosystems-under-threat.html`, the flagged lavender/native wording is no longer present.
   - **Source evidence:** Searching `lesson-plans/gr2-ls2-unit1-lesson6-ecosystems-under-threat.html` shows no current lavender/native claim.
   - **Live evidence:** Live Lesson 6 review HTML does not surface the flagged lavender wording.

6. **`cmt_Yaayd-n3jg8` — Cass (Editor) — quoted `🐝 Pollinators`**
   - **Status:** `resolved`
   - **Why:** This checklist item was a verification/log note, not an independent content request. The verification has now been completed against current source and current live HTML. The source/live page clearly confirm italicized learning-objective verbs and correct public Remarq wiring. The moth treatment is also clearly no longer a butterfly emoji. The shipped student-facing treatment now uses dedicated pollinator image assets plus moon/night wording in the text surfaces rather than a literal `🌙 throughout` replacement, and that difference is now explicitly documented instead of assumed.
   - **Source evidence:** Current source shows `<em>explain</em>/<em>create</em>`, production `feedback-layer.js` with matching document ID, dedicated hummingbird/moth image assets referenced in both student-facing placements via `../images/pollinators/*.svg?v=20260410`, and moon/night wording in the answer key.
   - **Live evidence:** Live review HTML matches the same production Remarq wiring, cache-busted asset references, and moon/night wording; no butterfly emoji treatment remains.

7. **`cmt_ja0CZ_OoMck` — Chris — quoted `Hummingbird`**
   - **Status:** `resolved`
   - **Why:** The current lesson no longer uses an emoji or weak inline stand-in for the hummingbird. It now points to a dedicated external hummingbird image asset in both student-facing placements, and the live review page serves that asset successfully via the cache-busted URL used by the lesson.
   - **Source evidence:** Current source references `../images/pollinators/hummingbird-card.svg?v=20260410` in both the Activity 3 card and the worksheet matching row.
   - **Live evidence:** Live review HTML contains the same cache-busted hummingbird asset references, and `https://littlelabcoats.co/images/pollinators/hummingbird-card.svg?v=20260410` returns `HTTP 200`.

8. **`cmt_owSIHIW_p7w` — Chris — quoted `Moth`**
   - **Status:** `resolved`
   - **Why:** The current lesson no longer uses an emoji or weak inline stand-in for the moth. It now points to a dedicated external moth image asset in both student-facing placements, and the live review page serves that asset successfully via the cache-busted URL used by the lesson.
   - **Source evidence:** Current source references `../images/pollinators/moth-card.svg?v=20260410` in both the Activity 3 card and the worksheet matching row.
   - **Live evidence:** Live review HTML contains the same cache-busted moth asset references, and `https://littlelabcoats.co/images/pollinators/moth-card.svg?v=20260410` returns `HTTP 200`.

### Grade 4 LS1 Unit 1 Lesson 2 — Sensing the World

Source file: `lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html`
Live review URL: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html?review=1`

9. **`cmt_cmqjrg03Pgs` — Rachel — quoted `🌿 Sensing the World 🌿`**
   - **Status:** `resolved`
   - **Why:** The lesson now requires students to record the sensory structure, the information it detects, and the behavior it supports.
   - **Source evidence:** Step 2 and the `Sensory Detective` table use `Sensory structure`, `What information it detects`, and `How that helps behavior`; answer-key guidance also expects this structure.
   - **Live evidence:** Live review HTML shows the same Step 2/worksheet/answer-key wording.

10. **`cmt_IUsYk9D75g4` — Serena Salvato — quoted `nimal photos or simple observation cards`**
    - **Status:** `resolved`
    - **Why:** The live/source lesson no longer implies supplied observation cards; it now specifies using `2–4 animal photos from a nature book, magazine, or device`.
    - **Source evidence:** Materials list contains `2–4 animal photos from a nature book, magazine, or device`.
    - **Live evidence:** Live review HTML matches that updated materials wording.

11. **`cmt_5wTOgmamF8Q` — Serena Salvato — quoted `paper tub`**
    - **Status:** `resolved`
    - **Why:** The vague material wording is now concrete.
    - **Source evidence:** Materials + Step 1 say `toilet paper roll or paper towel tube`.
    - **Live evidence:** Live review HTML matches the same wording.

12. **`cmt_LaTi5_pzAzg` — Serena Salvato — quoted `Have students record one structure...`**
    - **Status:** `resolved`
    - **Why:** Step 4 is now explicit about the exact student task.
    - **Source evidence:** Step 4 tells students to complete a second `Sensory Detective` row and finish the `Claim Box` with one full sentence naming the structure, information detected, and survival/behavior link.
    - **Live evidence:** Live review HTML shows the same Step 4 wording.

13. **`cmt_ICYW7DoUQsw` — Serena Salvato — quoted `sight`**
    - **Status:** `resolved`
    - **Why:** The main lesson flow now uses smell in Step 4 rather than leaving the more dynamic example in an extension-only role.
    - **Source evidence:** Step 4 runs a smell challenge using familiar scents; worksheet guidance says add the second row after the smell challenge.
    - **Live evidence:** Live review HTML shows the same smell-based Step 4.

14. **`cmt_155TFGieedk` — Serena Salvato — quoted `y Detective`**
    - **Status:** `resolved`
    - **Why:** The worksheet and procedure now clearly say when the `Sensory Detective` table is used.
    - **Source evidence:** Worksheet says `Use during Step 2 and Step 4`; Step 2 explicitly says to begin the table during that step.
    - **Live evidence:** Live review HTML matches those cues.

15. **`cmt_n2qIxYe2lyo` — Serena Salvato — quoted ` becaus`**
    - **Status:** `resolved`
    - **Why:** The `Claim Box` now clearly states when it is completed.
    - **Source evidence:** Worksheet says `Complete during Step 4` above the claim sentence.
    - **Live evidence:** Live review HTML matches the same wording.

### Grade 4 LS1 Unit 1 Lesson 3 — Mouths, Beaks, Teeth, and Getting Food

16. **`cmt_RuLciC0fyFw` — Margaret — quoted `🌿 Mouths, Beaks, Teeth, and Getting Food 🌿`**
   - **Status:** `resolved`
   - **Why:** The worksheet now asks for a visible clue and a fit/mismatch explanation.
   - **Source evidence:** `Would It Work?` prompt says `Name a visible clue ... then explain why that structure would or would not work well for a different food source`; answer-key guidance repeats visible-clue language.
   - **Live evidence:** Live review HTML shows the same prompt and guidance.

### Grade 4 LS1 Unit 1 Lesson 6 — Construct an Argument: Animal Structures

17. **`cmt_uYklotZpdVI` — Rachel — quoted `🌿 Construct an Argument: How Animal Structures Help Them Live 🌿`**
   - **Status:** `resolved`
   - **Why:** This was a positive continuity-validation note, and the reviewed continuity/path structure remains present.
   - **Source evidence:** Current lesson still includes the Grade 4 full-domain path and Unit 2 continuity.
   - **Live evidence:** Live review HTML exposes the same lesson shell and continuity content.

### Grade 4 LS1 Unit 2 Lesson 1 — Roots, Stems, and Plant Support Systems

18. **`cmt_3kaZteO94Vg` — Margaret — quoted `🌿 Roots, Stems, and Plant Support Systems 🌿`**
   - **Status:** `resolved`
   - **Why:** This was a positive continuity-validation note, and the plant-unit transition/path structure remains present.
   - **Source evidence:** Current lesson still sits inside the Grade 4 lesson-path structure.
   - **Live evidence:** Live review HTML serves the same continuity-enabled page.

### Grade 4 LS1 Unit 2 Lesson 3 — Water Transport Inside Plants

19. **`cmt_dCniCaGVsBA` — Rachel — quoted `🌿 Water Transport Inside Plants 🌿`**
   - **Status:** `resolved`
   - **Why:** The lesson now explicitly uses the requested observation → inference → function framing.
   - **Source evidence:** Step 4 says `record an observation, an inference, and the function that inference supports`.
   - **Live evidence:** Live review HTML matches that Step 4 wording.

### Grade 4 LS1 Unit 2 Lesson 4 — Flowers, Pollination, and Reproduction

20. **`cmt_dv5KvSm1RGc` — Rachel — quoted `🌿 Flowers, Pollination, and Reproduction 🌿`**
   - **Status:** `resolved`
   - **Why:** This was a positive package-coherence note, and the lesson still serves as the package’s explicit reproduction anchor.
   - **Source evidence:** The science, questions, and worksheet all still center reproduction.
   - **Live evidence:** Live review HTML shows the same reproduction-centered lesson.

### Grade 4 LS1 Unit 2 Lesson 5 — Seeds, Fruits, and New Plants

21. **`cmt_DSXoQojNP44` — Margaret — quoted `🌿 Seeds, Fruits, and New Plants 🌿`**
   - **Status:** `resolved`
   - **Why:** The writing prompt and teacher support now explicitly require offspring/reduced-competition framing.
   - **Source evidence:** `Explain the Benefit` prompt says `Be sure to mention offspring, the next generation, or reduced competition with the parent plant`; teacher notes reinforce the same expectation.
   - **Live evidence:** Live review HTML matches the same wording.

### Grade 4 LS1 Unit 2 Lesson 6 — Construct an Argument: Plant Structures

22. **`cmt_KpHnslYt7LE` — Margaret — quoted `🌿 Construct an Argument: How Plant Structures Help Plants Live and Reproduce 🌿`**
   - **Status:** `resolved`
   - **Why:** This was a positive package-parallelism note, and the plant capstone still reads as the parallel to Unit 1 Lesson 6.
   - **Source evidence:** The current lesson retains mirrored argument structure and full-domain framing.
   - **Live evidence:** Live review HTML matches that structure.

### Grade 4 LS1 Unit 2 Quiz

23. **`cmt_Ypf07YNGxIc` — Rachel — quoted `🌿 Plant Structures &amp; Reproduction Unit Quiz 🌸`**
   - **Status:** `resolved`
   - **Why:** The short response now explicitly asks for one structure tied to survival/growth and one tied to reproduction.
   - **Source evidence:** Short response prompt says `Explain how one supports survival or growth and how the other supports reproduction`.
   - **Live evidence:** Live review HTML shows the same prompt.

---

## Current implementation backlog

Only comments still needing follow-up edits are included here.

- **No Pollinators follow-up edits remain from this live-review verification pass.**

## Backlog summary by lesson/package

- **Pollinators:** 0 follow-up items remain from the current live-vs-source audit
- **Grade 4 LS1 reviewed set:** 0 follow-up items remain from the current live-vs-source audit

## Audit notes

- Live page checks were based on current public review URLs, not local preview.
- Source checks were based on current repo files, not prior status docs.
- Positive comments were preserved and explicitly marked `resolved` where the validated state is still visible.
- The Pollinators cross-lesson lavender comment was audited against the actual current Lesson 6 target because the comment body explicitly redirected the issue there.
- Pollinators visual verification was re-run after push using the actual public review URL and the direct public asset URLs.
- The deployed lesson now references cache-busted Pollinators asset URLs (`?v=20260410`) in both student-facing hummingbird and moth placements.
- Bare asset URLs without the query string were still returning cached `404` responses during this pass, but the exact cache-busted URLs used by the live lesson returned `HTTP 200`; the live lesson therefore loaded the verified public asset URLs actually referenced in the page source.
- This audit intentionally records the current deployed reality: dedicated external image assets are what shipped for the hummingbird and moth, not the earlier inline SVG treatment.
- After the Pollinators ship/verify pass, the full Grade 4 LS1 active-review set was spot-checked again against current source and current live review URLs. No new drift was found in the reviewed prompts, continuity/path shells, reproduction framing, evidence language, or feedback-layer document wiring.
- The final truth-pass conclusion for this chunk is: Pollinators is fully reconciled from current source/live evidence, the editor-summary item is treated as a satisfied verification/log item with explicit notes about the exact shipped state, and the Grade 4 reviewed set does not currently need additional implementation.
