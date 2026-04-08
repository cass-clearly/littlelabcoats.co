# Grade 4 Shareable Manifest

Last updated: 2026-04-08
Status: final closeout URL manifest for the canonical Grade 4 Life Science domain; live verification on 2026-04-08 confirms the lesson, review, quiz, and listing URLs below resolve publicly with no canonical Grade 4 404s remaining
Audience: Serena

This file is the concise Grade 4 Life Science URL handoff for the current repo state.
It should be treated as the source-of-truth URL list for the canonical `4-LS1` package now present in repo.

## Grade 4 Life Science lesson URLs

- `External Structures for Survival`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html?review=1`
- `Sensing the World`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html?review=1`
- `Mouths, Beaks, Teeth, and Getting Food`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson3-mouths-beaks-teeth-and-getting-food.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson3-mouths-beaks-teeth-and-getting-food.html?review=1`
- `Movement Structures and Finding Safety`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson4-movement-structures-and-finding-safety.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson4-movement-structures-and-finding-safety.html?review=1`
- `Structures for Protection and Defense`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson5-structures-for-protection-and-defense.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson5-structures-for-protection-and-defense.html?review=1`
- `Construct an Argument: How Animal Structures Help Them Live`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html?review=1`
- `Roots, Stems, and Plant Support Systems`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson1-roots-stems-and-plant-support-systems.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson1-roots-stems-and-plant-support-systems.html?review=1`
- `Leaves and Making Food`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson2-leaves-and-making-food.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson2-leaves-and-making-food.html?review=1`
- `Water Transport Inside Plants`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson3-water-transport-inside-plants.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson3-water-transport-inside-plants.html?review=1`
- `Flowers, Pollination, and Reproduction`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson4-flowers-pollination-and-reproduction.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson4-flowers-pollination-and-reproduction.html?review=1`
- `Seeds, Fruits, and New Plants`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson5-seeds-fruits-and-new-plants.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson5-seeds-fruits-and-new-plants.html?review=1`
- `Construct an Argument: How Plant Structures Help Plants Live and Reproduce`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson6-construct-an-argument-plant-structures.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson6-construct-an-argument-plant-structures.html?review=1`

## Grade 4 Life Science support URLs

- `Unit 1 Quiz`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-quiz.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-quiz.html?review=1`
- `Unit 2 Quiz`  
  `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-quiz.html`  
  Review: `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-quiz.html?review=1`
- `Document ID mapping` lives in `lesson-plans/gr4-document-id-manifest.md`
- `Batch review tracking` lives in `lesson-plans/gr4-life-science-batch-review.md`

## Live listing / discovery URLs

These are the public surfaces that should expose Grade 4 Life Science live:

- `Homepage`  
  `https://littlelabcoats.co/`
- `Curriculum library`  
  `https://littlelabcoats.co/curriculum/`
- `Curriculum library (html route)`  
  `https://littlelabcoats.co/curriculum.html`

## Scope note

This manifest intentionally reflects the canonical 12-lesson Grade 4 Life Science package and does **not** treat `gr4-ls1-unit1-l1-food-webs.html` as authoritative for the Grade 4 LS1 scope.

## Final live verification note

Final live closeout verification on 2026-04-08 confirmed:
- all 12 canonical lesson URLs return `200`
- all 12 canonical lesson review URLs return `200`
- both canonical quiz URLs return `200`
- both canonical quiz review URLs return `200`
- the live listing/discovery surfaces return `200`:
  - `https://littlelabcoats.co/`
  - `https://littlelabcoats.co/curriculum/`
  - `https://littlelabcoats.co/curriculum.html`
- representative live page checks confirmed explicit `data-document-id` values on deployed Grade 4 pages match `lesson-plans/gr4-document-id-manifest.md`
- representative live review checks confirmed public Remarq comment/highlight loading works on sampled reviewed Grade 4 pages
- `lesson-plans/gr4-life-science-batch-review.md` records the Rachel + Margaret review evidence, comment IDs, document matches, and revision status
- `lesson-plans/gr4-print-verification.md` records the final live print/readiness verification evidence

Disposition:
- this manifest is the final exact public URL handoff for the canonical Grade 4 Life Science domain
- no canonical Grade 4 public 404s remain in the verified lesson, review, quiz, or listing surfaces
