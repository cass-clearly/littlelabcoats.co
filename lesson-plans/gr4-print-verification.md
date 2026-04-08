# Grade 4 Life Science — Live Print and Content Readiness Verification

Last updated: 2026-04-08
Chunk: `verify-live-print-and-content-readiness`
Status: iteration 2 live QA completed; representative Grade 4 public lesson/quiz/refcard rendering and review/paywall behavior pass, the `/curriculum/` Grade 4 discovery links are now fixed live, and the former private-IP feedback-layer script reference has been replaced with CDN + HTTPS wiring — but public Remarq comment loading still fails because the HTTPS Remarq host does not allow cross-origin browser access from `littlelabcoats.co`

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

## Known open issue from live browser QA

### Remarq comment loading is still blocked at the HTTPS API layer

Iteration-1 issue:
- the Grade 4 pages were pointing directly at the private LAN host `http://192.168.5.204:3334/feedback-layer.js`
- on live HTTPS pages that produced `ERR_SSL_PROTOCOL_ERROR`

Iteration-2 change applied across the canonical Grade 4 package:
- script source updated from the private LAN host to the hosted package URL:
  - `https://unpkg.com/@csalvato/remarq@1.6.0/dist/feedback-layer.js`
- API base updated from the private LAN host to the HTTPS Remarq hostname:
  - `https://remarq.littlelabcoats.co`

What live browser QA now shows on representative Grade 4 pages:
- the feedback-layer script itself now loads from `unpkg.com`
- the old private-IP SSL failure is gone from the sampled Grade 4 pages
- the page still fails to load comments because browser requests to:
  - `https://remarq.littlelabcoats.co/comments?document=<doc-id>`
  are blocked by cross-origin browser policy
- the representative browser error is now:
  - `No 'Access-Control-Allow-Origin' header is present on the requested resource`
- request failure is now `net::ERR_FAILED` against the HTTPS host rather than the earlier private-IP SSL error

Meaning:
- the Grade 4 package no longer depends on a private-IP script URL for its feedback-layer bootstrap
- public page rendering, preview/review behavior, and print readiness are in good shape on the sampled assets
- but true public inline-comment loading still requires infrastructure-side CORS / access-policy work on `remarq.littlelabcoats.co`

This remaining issue appears to be outside the Grade 4 lesson-file package itself.

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
- corrected the Grade 4 `/curriculum/` discovery links in `curriculum/index.html` and verified the fix live after deploy
- replaced the Grade 4 package's private-IP feedback-layer script wiring with CDN + HTTPS Remarq wiring across all 26 canonical Grade 4 lesson/refcard/quiz pages

### Still open after this pass
- infrastructure-side CORS / access-policy work is still required before `remarq.littlelabcoats.co` can serve comments to `https://littlelabcoats.co` in a public browser session
- until that host allows cross-origin comment loading, public inline Remarq comments remain blocked even though the Grade 4 page package itself now uses HTTPS-safe script wiring
