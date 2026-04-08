# Grade 4 Shareable Manifest

Last updated: 2026-04-08
Status: canonical URL manifest for the Grade 4 Life Science domain; live refresh on 2026-04-08 confirms the lesson directory, curriculum surfaces, homepage links, and canonical Grade 4 lesson/quiz URLs all resolve publicly and point to the intended package
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
- `Lesson directory`  
  `https://littlelabcoats.co/lesson-plans/`

## Scope note

This manifest intentionally reflects the canonical 12-lesson Grade 4 Life Science package and does **not** treat `gr4-ls1-unit1-l1-food-webs.html` as authoritative for the Grade 4 LS1 scope.

## Live verification note

Live refresh on 2026-04-08 confirmed:
- all 12 canonical Grade 4 lesson URLs listed above return `200`
- both canonical Grade 4 quiz URLs listed above return `200`
- the live HTML for each canonical Grade 4 lesson and quiz page contains the expected exact `<link rel="canonical">` tag
- the following discovery/listing surfaces return `200` and point at canonical Grade 4 package URLs:
  - `https://littlelabcoats.co/`
  - `https://littlelabcoats.co/curriculum/`
  - `https://littlelabcoats.co/curriculum.html`
  - `https://littlelabcoats.co/lesson-plans/`
- the public lesson directory now shows the corrected Grade 4 package listing with `12 lessons` in `Grade 4 · Life Science`
- the public lesson directory no longer promotes `gr4-ls1-unit1-l1-food-webs.html` inside the Grade 4 Life Science listing
- the stale exploratory URL remains intentionally non-canonical and redirects toward the canonical Grade 4 entry page
- representative live page checks confirmed explicit `data-document-id` values on deployed Grade 4 pages match `lesson-plans/gr4-document-id-manifest.md`
- representative live review checks confirmed public Remarq comment/highlight loading works on sampled reviewed Grade 4 pages
- `lesson-plans/gr4-life-science-batch-review.md` records the Rachel + Margaret review evidence, comment IDs, document matches, and revision status
- `lesson-plans/gr4-print-verification.md` records the final live print/readiness verification evidence

Disposition:
- this manifest remains the source-of-truth URL list for the canonical Grade 4 Life Science package
- direct canonical Grade 4 lesson/review/quiz URLs are live
- public discovery-surface alignment for Grade 4 is now live on the public site
