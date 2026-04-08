# Grade 4 Life Science — Live Print and Content Readiness Verification

Last updated: 2026-04-08
Chunk: `verify-live-print-and-content-readiness`
Status: iteration 3 live QA completed; representative Grade 4 public lesson/quiz/refcard rendering, review/paywall behavior, printable assets, discovery surfaces, and live Remarq comment loading now pass on the public site

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
Iteration-1 problem:
- the Grade 4 links on `https://littlelabcoats.co/curriculum/` were using relative `lesson-plans/...` paths
- on the deployed `/curriculum/` route that produced broken URLs such as:
  - `https://littlelabcoats.co/curriculum/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`
- those broken `/curriculum/lesson-plans/...` URLs returned `404`

Iteration-2 live verification:
- `https://littlelabcoats.co/curriculum/` now exposes root-relative Grade 4 links such as:
  - `/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`
- browser automation confirmed the rendered link now resolves to:
  - `https://littlelabcoats.co/lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`
- the representative Grade 4 curriculum-directory link no longer routes through the broken `/curriculum/lesson-plans/...` path

Disposition:
- the Grade 4 `/curriculum/` discovery-surface 404 issue is fixed live

## Remarq infrastructure resolution in this chunk

### What was wrong before iteration 3

Iteration-1 issue:
- the Grade 4 pages were pointing directly at the private LAN host `http://192.168.5.204:3334/feedback-layer.js`
- on live HTTPS pages that produced `ERR_SSL_PROTOCOL_ERROR`

Iteration-2 issue:
- the Grade 4 pages were moved to HTTPS-safe wiring, but the chosen hostname `https://remarq.littlelabcoats.co` was not actually usable from the public web
- direct checks against that hostname returned Cloudflare error `1014` (`CNAME Cross-User Banned`)
- because of that host-level failure, representative public Grade 4 pages could not fetch comments successfully from the browser

### What changed in iteration 3

Infrastructure-side fix applied on the live proxy path:
- updated the live `cassclearly.com` nginx config to proxy these Remarq routes to the production Remarq server on `127.0.0.1:3334`
  - `/comments`
  - `/documents`
  - `/health`
  - `/openapi.json`
  - `/ws`
- verified with an `Origin: https://littlelabcoats.co` request that the proxied Remarq API now returns:
  - `Access-Control-Allow-Origin: https://littlelabcoats.co`
  - `Access-Control-Allow-Credentials: true`
- rewired the canonical 26-file Grade 4 package to use:
  - script source: `https://cassclearly.com/feedback-layer.js?v=20260408`
  - API base: `https://cassclearly.com`

### Final live browser result

Representative live browser QA now shows:
- no more private-IP feedback-layer bootstrap on sampled Grade 4 pages
- no more `remarq.littlelabcoats.co` browser failures on sampled Grade 4 pages
- no more Remarq CORS failures on sampled Grade 4 pages
- representative reviewed lesson/quiz pages now load live comments/highlights successfully on the real public URLs
- sampled review pages with known recorded comments show visible highlights/comment presence in the browser

Disposition:
- public Remarq comment loading is now functioning on the sampled Grade 4 package pages used in this verification pass

## Final disposition for this chunk

### Passed in the final live pass
- live lesson URLs render on the public site
- live review URLs unlock correctly
- representative lesson print buttons work
- print CSS hides paywall overlays and print buttons where expected
- representative refcards render as printable assets
- representative quizzes enforce public preview mode and unlock in review mode
- canonical Grade 4 lesson-to-quiz links are present on the sampled live pages
- the Grade 4 `/curriculum/` discovery links resolve to canonical `/lesson-plans/...` URLs on the real public site
- representative reviewed Grade 4 pages now load live Remarq comments/highlights successfully from the public browser context

### Final package conclusion
- the Grade 4 Life Science package now passes the representative live print/readiness/content-completeness checks for this chunk
- public preview behavior, review-mode behavior, printable assets, and companion quiz/refcard access match the expected LLC public pattern on the sampled live pages
- the Grade 4 Life Science package is now functionally complete for real public user access for the scope verified in this chunk
