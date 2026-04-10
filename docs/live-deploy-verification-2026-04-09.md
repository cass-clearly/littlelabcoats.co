# Live deploy verification — 2026-04-09

Commit deployed: `959735f` — `Fix homepage mobile nav, popup close, and free sample mappings`

## Deployment
- Pushed to `origin/main`
- Remote: `https://github.com/cass-clearly/littlelabcoats.co.git`
- Verification used cache-busting query parameters after push to avoid stale CDN/browser responses.

## Live URLs checked
- `https://littlelabcoats.co/`
- `https://littlelabcoats.co/curriculum.html`
- `https://littlelabcoats.co/curriculum/`
- `https://littlelabcoats.co/store.html`
- `https://littlelabcoats.co/lesson-plans/index.html`
- `https://littlelabcoats.co/lesson-plans/k-milk-magic.html`
- `https://littlelabcoats.co/lesson-plans/free-gr1-celery-rainbow.html`
- `https://littlelabcoats.co/lesson-plans/free-gr2-salt-dough-fossil-factory.html`
- `https://littlelabcoats.co/lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- `https://littlelabcoats.co/lesson-plans/free-gr4-apple-oxidation.html`
- `https://littlelabcoats.co/lesson-plans/free-gr5-bread-mold-terrarium.html`

## Observed outcomes

### Homepage (`/`) — mobile viewport
- Mobile header now shows a visible `Menu` toggle.
- Opening the mobile menu exposes:
  - `Curriculum`
  - `Pricing`
  - `About`
  - `FAQ`
  - `Subscribe`
- Tapping `Pricing` closes the menu and navigates to `#pricing`.
- Tapping `About` closes the menu and navigates to `#founder`.
- Tapping mobile `Subscribe` closes the menu and opens the subscribe popup.
- Tapping the popup `X` closes the popup and restores page scrolling (`document.body.style.overflow` returns to empty).
- Kindergarten Unit 3 no longer shows `Milk Magic` inline.
- Homepage Kindergarten Unit 3 now reads:
  - `K-LS1 Unit 3: Animal Needs`
  - `Lessons 2–6 shown here`
  - followed by the lesson links only.
- Grade tab / featured sample mapping now updates correctly on the live site:
  - `grade-k` → `Milk Magic` → `/lesson-plans/k-milk-magic.html`
  - `grade-1` → `Celery Rainbow` → `/lesson-plans/free-gr1-celery-rainbow.html`
  - `grade-2` → `Salt Dough Fossil Factory` → `/lesson-plans/free-gr2-salt-dough-fossil-factory.html`
  - `grade-3` → `Egg Drop Kitchen Challenge` → `/lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
  - `grade-4` → `Apple Browning Experiment` → `/lesson-plans/free-gr4-apple-oxidation.html`
  - `grade-5` → `Bread Mold Terrarium` → `/lesson-plans/free-gr5-bread-mold-terrarium.html`

### Curriculum routes (`/curriculum.html` and `/curriculum/`) — mobile viewport
- Expanding `Animal Needs: The Survival Checklist` no longer shows `Free Sample — Milk Magic` inside the unit card.
- Lessons `L2` through `L6` remain present.
- Unit quiz link remains present.
- Reference card link remains present.

### Store (`/store.html`)
- Grade-specific free sample links remain correct:
  - K → `/lesson-plans/k-milk-magic.html`
  - 1 → `/lesson-plans/free-gr1-celery-rainbow.html`
  - 2 → `/lesson-plans/free-gr2-salt-dough-fossil-factory.html`
  - 3 → `/lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
  - 4 → `/lesson-plans/free-gr4-apple-oxidation.html`
  - 5 → `/lesson-plans/free-gr5-bread-mold-terrarium.html`

### Lesson index (`/lesson-plans/index.html`)
- Grade 1 through Grade 4 free-sample surfaces matched the expected grade-specific sample links in the verification pass.
- Canonical direct grade-specific sample URLs for K–5 all remained reachable and were included in the checked URL set above.

## Result summary
- Live mobile navigation issue: resolved on homepage.
- Live mobile subscribe popup close issue: resolved on homepage.
- Live homepage per-grade featured free-sample issue: resolved.
- Live Kindergarten Unit 3 misplaced free-sample issue: resolved on homepage and both curriculum routes.

## Notes
- Verification used mobile-relevant browser automation on the public site after push.
- One early homepage grade-tab check gave a false negative because the test did not first scroll into the sample-units area before tab interaction; the corrected live verification confirmed the feature is working as expected.

## Deploy verification rule update — 2026-04-10
- `littlelabcoats.co` live deploy path is push to `origin/main`.
- Production is served from GitHub Pages behind Cloudflare/Fastly.
- After push, canonical public pages can lag briefly before they reflect the new commit.
- During that window, stale public HTML alone should not be treated as an immediate hard blocker.
- Correct verification behavior is: push → check live URLs with cache-busting query params → allow a short wait/retry window → recheck before declaring a deploy problem.
- Status reports should explicitly distinguish:
  - `repo pushed, waiting on propagation`
  - `deploy pipeline unknown/broken`
- This note reflects the behavior observed on 2026-04-10: push to `origin/main`, then wait for public propagation before judging live verification.