# Grade 4 LS1 Unit 1 Lesson 1 Animal Card Audit

Last updated: 2026-04-09
Status: chunk audit for embedding animal cards directly into the lesson page

## Scope of this audit

Target lesson:
- `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`

Objective for later implementation:
- remove all dependence on outside animal picture cards, book images, or parent-sourced animal visuals
- embed the needed animal cards directly into the lesson page itself
- update all lesson references so materials, procedure, worksheet, and answer key point to the included cards
- preserve LLC print readiness, preview behavior, and route wiring

This file is an audit only. It does not claim the lesson has been updated yet.

## File and route inventory

Primary content files involved right now:
- lesson page: `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`
- refcard: `lesson-plans/gr4-ls1-unit1-refcard-lesson1-external-structures-for-survival.html`
- unit quiz: `lesson-plans/gr4-ls1-unit1-quiz.html`
- Grade 4 scope source: `lesson-plans/gr4-life-science-audit-and-scope.md`
- Grade 4 document ID source: `lesson-plans/gr4-document-id-manifest.md`

Site/listing/discovery surfaces that expose this lesson:
- `lesson-plans/index.html`
- `curriculum.html`
- `curriculum/index.html`
- `index.html`
- `lesson-plans/_generated/lesson-index-data.json`

Canonical public lesson URL:
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`

Target review URL for later live verification:
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html?review=1`

Known document IDs:
- lesson page: `doc_1ls0NvQ4g-0`
- refcard: `doc_Q7eAJYTjhDQ`

## Current dependency audit: every place the lesson relies on external animal visuals

### Main lesson file

File:
- `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`

Direct or implied external-material dependencies:

1. Materials section
- line 285: `picture cards or book images of 4–6 animals`
- why it matters: this is the clearest current external dependency. The lesson currently assumes the adult must supply or locate animal visuals elsewhere.

2. Procedure step 1
- line 291: `Start with a quick picture walk. Ask students to notice one visible body part on several animals before naming its job.`
- why it matters: `picture walk` implies a separate image source. If cards are embedded later, this should explicitly point to the included animal cards.

3. Procedure step 3
- line 293: `Sort animal examples by the kind of job the structure does...`
- why it matters: this step assumes a manipulable/example set exists, but the lesson does not currently provide one. Later implementation should anchor this step to the included card set.

4. Procedure step 4
- line 294: `Have students choose two animals...`
- why it matters: the lesson asks students to choose from a set of animals that is not actually supplied on-page.

5. Extension section
- line 301: `Go on a “structure hunt” with pets, birds outside, or animal photos from a book.`
- why it matters: this is another explicit outside-image dependency. It is not the core activity, but it reinforces the expectation that visuals come from outside the lesson.

6. Worksheet: Structure Spotter
- line 308: `Write an animal and one external structure you noticed.`
- why it matters: the prompt does not name the evidence source. In practice it currently depends on whichever outside pictures/cards/books the adult found.

7. Worksheet: Match the Job
- line 309 table header: `Evidence from the picture or animal`
- why it matters: this is explicit worksheet-level dependence on an external picture or a live animal, rather than on lesson-included cards.

8. Answer key
- lines 315-317 onward do not mention the source set directly, but the acceptable examples list depends on the same unsupplied animal-example pool established earlier in the lesson.
- why it matters: answer-key copy is not itself broken, but it is indirectly coupled to the missing/on-external visual set.

### Refcard file

File:
- `lesson-plans/gr4-ls1-unit1-refcard-lesson1-external-structures-for-survival.html`

Direct or implied external-material dependencies:

1. Materials snapshot
- inline text includes: `picture cards or book images of 4–6 animals`
- why it matters: the refcard repeats the same external dependency as the main lesson.

2. What to notice
- inline text includes: `Start with a quick picture walk...`
- why it matters: same picture-source assumption as the main lesson.

3. Family extension
- inline text includes: `animal photos from a book`
- why it matters: repeats the outside-source expectation in family-facing guidance.

## Hidden dependency notes

These are the places where the lesson does not explicitly say `animal cards`, but still relies on an external animal set:
- `picture walk`
- `sort animal examples`
- `choose two animals`
- worksheet evidence language: `from the picture or animal`
- refcard materials snapshot and family extension

If later edits only replace the materials bullet and do not update these indirect references, the parent-supplied dependency will survive.

## What does not currently need route-level change for this chunk

These are inventory items, not edit targets for the eventual embedded-card change unless something breaks:
- `lesson-plans/index.html` already links the lesson and review mode correctly
- `curriculum.html` already links the lesson and unit quiz
- `curriculum/index.html` already links the lesson and unit quiz
- `index.html` already links the lesson and unit quiz
- `lesson-plans/_generated/lesson-index-data.json` already records the canonical URL and review URL correctly
- `lesson-plans/gr4-document-id-manifest.md` already records the lesson and refcard document IDs
- `lesson-plans/gr4-life-science-audit-and-scope.md` already records canonical and review URLs for later verification

## LLC embedded-card pattern notes to preserve

Reference pattern pages inspected:
- `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html`
- `lesson-plans/k-ls1-unit3-lesson2-whats-for-dinner.html`
- `lesson-plans/gr1-ls1-unit1-lesson2-plant-parts-functions.html`

Patterns worth preserving for the future implementation:

1. Put the cards directly in the lesson page before or near the procedure section
- the Grade 3 climate lesson uses a named section (`Climate Cards for This Lesson`) before `Let's Get Started`
- materials and worksheet text explicitly point to `the included ... cards on this lesson page`
- this is the cleanest existing LLC precedent for replacing external sourcing with embedded lesson-owned assets

2. Keep the cards printable on letter-sized pages
- existing embedded-card pages use bounded card grids and page breaks
- print CSS protects content blocks with `break-inside: avoid` / `page-break-inside: avoid`
- future animal cards should be grouped so printing does not split a single card awkwardly across pages

3. Keep the lesson preview/paywall behavior intact
- the current lesson locks content starting from the `Materials` heading
- any new animal-card section inserted after `Materials` will sit behind the paywall in normal mode and remain visible in `?review=1`
- if the card section is placed before `Materials`, preview exposure changes; that should be a deliberate choice, not an accident

4. Preserve LLC lesson structure and voice
- current Grade 4 lesson structure is: header → standards → lesson path → big idea → science → vocabulary/tip → materials → procedure → discussion → extension → teacher notes → worksheet → answer key
- embedded cards should fit this structure, not replace it with a different page format

5. Point worksheet and answer-key language to the included source explicitly
- strongest existing pattern language is: `Use the included ... cards from this lesson page`
- later edits should use this wording in materials, procedure, worksheet directions, and answer-key notes for consistency

6. Preserve print-ready worksheet and detachable answer-key flow
- the worksheet and answer key are already separated by page breaks
- if animal cards become part of the printable packet, placement must not break the worksheet/answer-key separation or make the answer key start mid-card set

## Minimum future edit surface so no stale dependency survives

When the implementation chunk happens, review and likely update all of these locations together:
- main lesson CSS if a new card grid/card component is added
- main lesson Materials section
- main lesson Procedure steps 1, 3, and 4
- main lesson Extension section if the family-facing language should now prefer the included cards first
- main lesson worksheet prompt text, especially `Structure Spotter` and `Match the Job`
- main lesson answer-key phrasing if it should cite the included cards as the student evidence source
- main lesson page-break placement to keep cards printable
- paired refcard materials snapshot
- paired refcard `What to notice` bullets
- paired refcard family extension language

## Audit conclusion

Current state:
- the lesson is routed correctly and has a known live review URL
- the lesson and refcard both still depend on outside animal visuals
- the dependency appears in both explicit materials language and indirect activity wording

Conclusion for next chunk:
- embedding an on-page animal card section in the main lesson is required
- simply changing one materials bullet is not sufficient
- the main lesson and its paired refcard both need wording updates to fully remove the parent-supplied-card expectation
