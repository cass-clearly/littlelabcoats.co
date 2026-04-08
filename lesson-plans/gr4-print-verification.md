# Grade 4 Life Science — Live Print and Content Readiness Verification

Last updated: 2026-04-08
Chunk: `verify-live-print-and-content-readiness`
Status: iteration 1 live QA completed; public lesson/quiz/refcard rendering and review/paywall behavior mostly pass on representative Grade 4 assets, but one public directory surface fix was required and one Remarq script-loading issue remains open

## Scope of this pass

This verification pass checked the live public Grade 4 Life Science package on `littlelabcoats.co` with real browser automation against representative assets from both units:

- Unit 1 lesson 1
- Unit 1 lesson 6
- Unit 1 refcard lesson 1
- Unit 1 quiz
- Unit 2 lesson 1
- Unit 2 lesson 6
- Unit 2 refcard lesson 1
- Unit 2 quiz

It also spot-checked the public discovery surfaces:

- `https://littlelabcoats.co/curriculum/`
- `https://littlelabcoats.co/curriculum.html`
- `https://littlelabcoats.co/`

## What was verified live

### 1. Public lesson preview behavior

Verified on these public lesson URLs:
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson1-roots-stems-and-plant-support-systems.html`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson6-construct-an-argument-plant-structures.html`

Confirmed on the live public pages:
- each lesson returned `200`
- each lesson exposed the expected real `data-document-id`
- the preview paywall displayed on public non-review URLs
- the lesson shell stayed visible before the lock point
- the printable worksheet section was hidden in public preview mode
- the lesson path / next-step navigation remained visible
- each sampled lesson still linked forward to the appropriate unit quiz

### 2. Review-mode lesson behavior

Verified on these live review URLs:
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson1-roots-stems-and-plant-support-systems.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-lesson6-construct-an-argument-plant-structures.html?review=1`

Confirmed on the live review pages:
- each review URL returned `200`
- the paywall overlay was not shown
- full procedure steps were visible
- the worksheet section was visible
- the parent answer key was visible
- the top-right print button existed on lesson pages
- clicking the print button invoked the print handler successfully in browser automation (`window.print()` fired once on each sampled lesson)

### 3. Print behavior on live pages

Confirmed by live browser emulation on representative Grade 4 assets:
- lesson print buttons are hidden in print media
- paywall overlays are hidden in print media
- the lesson body prints on a white background
- no obvious shell-level print regression appeared on the sampled review pages
- live PDFs generated successfully for all representative review targets in this pass

Temporary live verification artifacts generated during review:
- `/tmp/gr4-ls1-unit1-lesson1-external-structures-for-survival.html-review.pdf`
- `/tmp/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html-review.pdf`
- `/tmp/gr4-ls1-unit1-refcard-lesson1-external-structures-for-survival.html-review.pdf`
- `/tmp/gr4-ls1-unit1-quiz.html-review.pdf`
- `/tmp/gr4-ls1-unit2-lesson1-roots-stems-and-plant-support-systems.html-review.pdf`
- `/tmp/gr4-ls1-unit2-lesson6-construct-an-argument-plant-structures.html-review.pdf`
- `/tmp/gr4-ls1-unit2-refcard-lesson1-roots-stems-and-plant-support-systems.html-review.pdf`
- `/tmp/gr4-ls1-unit2-quiz.html-review.pdf`

### 4. Refcard / printable asset checks

Verified on these public URLs:
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-refcard-lesson1-external-structures-for-survival.html`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-refcard-lesson1-roots-stems-and-plant-support-systems.html`

Confirmed:
- both representative refcards returned `200`
- both exposed the expected real `data-document-id`
- both use a print-oriented single-page card layout
- both rendered successfully under print emulation and in generated PDFs
- no paywall overlay is present on the refcard pages

### 5. Quiz preview / review behavior

Verified on these public and review URLs:
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-quiz.html`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-quiz.html?review=1`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-quiz.html`
- `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit2-quiz.html?review=1`

Confirmed:
- both quiz pages returned `200`
- both public quiz pages showed the expected paywall preview state
- both public quiz pages exposed exactly 2 visible question cards in preview mode during clean-browser checks
- both public quiz pages hid the short-response section and answer key in preview mode
- both review quiz URLs exposed all 8 multiple-choice questions
- both review quiz URLs exposed the short-response section and answer key
- quiz print CSS hides the paywall overlay in print media
- both quizzes include live links back into the canonical Grade 4 lesson sequence

## Discovery-surface findings

### `curriculum.html`
Verified live:
- returns `200`
- Grade 4 links point at canonical `/lesson-plans/...` URLs
- representative Grade 4 package links resolve correctly from this page

### `index.html`
Verified live:
- returns `200`
- Grade 4 package links point at canonical `/lesson-plans/...` URLs
- representative Grade 4 package links resolve correctly from this page

### `curriculum/`
Problem found during this pass:
- the Grade 4 links on `https://littlelabcoats.co/curriculum/` were still using relative `lesson-plans/...` paths
- on the deployed `/curriculum/` route that produced broken URLs such as:
  - `https://littlelabcoats.co/curriculum/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`
- those broken `/curriculum/lesson-plans/...` URLs returned `404`

Action taken in this iteration:
- updated `curriculum/index.html` so the Grade 4 free sample, Unit 1 lesson/quiz links, and Unit 2 lesson/quiz links use root-relative `/lesson-plans/...` paths instead of route-relative `lesson-plans/...`

This fix still needs deploy verification after push.

## Known open issue from live browser QA

### Remarq feedback-layer script is not public-web safe yet on the sampled Grade 4 pages

On every representative Grade 4 lesson, refcard, and quiz checked in this pass, browser automation reported the same live script-load failure:
- page source still points the feedback layer at `http://192.168.5.204:3334/feedback-layer.js`
- the browser attempted to load it as `https://192.168.5.204:3334/feedback-layer.js`
- the request failed with `net::ERR_SSL_PROTOCOL_ERROR`

Meaning:
- the page-shell review bypass works (`?review=1` unlocks content correctly)
- print/readability checks mostly pass
- but the embedded Remarq feedback-layer script is still not loading cleanly from the published HTTPS pages in browser automation

This is the remaining issue most likely to block true public inline-comment behavior on the Grade 4 package.

## Iteration-1 disposition

### Passed in this pass
- live lesson URLs render on the public site
- live review URLs unlock correctly
- representative lesson print buttons work
- print CSS hides paywall overlays and print buttons where expected
- representative refcards render as printable assets
- representative quizzes enforce public preview mode and unlock in review mode
- canonical Grade 4 lesson-to-quiz links are present on the sampled live pages

### Fixed in this pass
- corrected the Grade 4 `/curriculum/` discovery links in `curriculum/index.html` so they will deploy as root-relative canonical lesson/quiz URLs instead of broken `/curriculum/lesson-plans/...` URLs

### Still open after this pass
- deploy + recheck the `/curriculum/` Grade 4 link fix
- resolve or explicitly waive the broken private-IP feedback-layer script loading on live Grade 4 pages before calling the package fully production-ready for public review/comments
