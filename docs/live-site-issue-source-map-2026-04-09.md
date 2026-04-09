# Little Lab Coats live-site issue source map — 2026-04-09

## Purpose
Locate the production-rendered files, components, and public URLs that control the newly reported live-site issues so the implementation pass edits the real surfaces.

## Production route map

### Homepage / landing page
- Public URL: `https://littlelabcoats.co/`
- Primary source file: `index.html`
- Notes:
  - Live fetch confirmed homepage HTML contains the current navigation, curriculum tabs, featured sample block, popup markup, and popup JS.
  - `lesson-plans/landing-page.html` is a draft/older variant and should **not** be treated as the primary live homepage source for this fix batch.

### Curriculum page
- Public URLs:
  - `https://littlelabcoats.co/curriculum.html`
  - `https://littlelabcoats.co/curriculum/`
- Source files:
  - `curriculum.html`
  - `curriculum/index.html`
- Notes:
  - Both public curriculum routes should be treated as live-facing and kept aligned where the same issue appears.

### Store page
- Public URL: `https://littlelabcoats.co/store.html`
- Source file: `store.html`
- Notes:
  - This page contains the grade-by-grade free sample cards and is part of the public sample surfacing that should stay grade-correct.

### Lesson index
- Public URL: `https://littlelabcoats.co/lesson-plans/index.html`
- Source files:
  - Rendered page: `lesson-plans/index.html`
  - Data source: `lesson-plans/_generated/lesson-index-data.json`
  - Generators: `scripts/generate-lesson-index-data.py`, `scripts/render-lesson-index-page.py`
- Notes:
  - The rendered lesson index currently shows the correct per-grade free samples.
  - Because this page is generated, any issue discovered there later should be fixed at the data/generator level rather than only patching rendered HTML.

## Issue-to-source map

### 1) Kindergarten Unit 3 incorrectly shows a free sample at the end / inside the unit listing
#### Production code locations
- `index.html`
  - K grade panel, Unit 3 block around the `K-LS1 Unit 3: Animal Needs` section
  - Currently includes `Free Sample — Milk Magic` inline inside the unit lesson list
- `curriculum.html`
  - K-LS1 Unit 3 card body under `Animal Needs: The Survival Checklist`
  - Currently includes `Free Sample — Milk Magic` as the starred first row inside the unit card
- `curriculum/index.html`
  - Duplicate public curriculum route with the same K-LS1 Unit 3 free-sample insertion

#### Why this is the right fix target
- These are the live curriculum surfaces where the incorrect placement is publicly rendered.
- `lesson-plans/index.html` is not the source of this specific reported placement issue; it lists Kindergarten Unit 3 lessons separately and shows `Milk Magic` elsewhere.

### 2) Every grade shows the kindergarten free sample instead of a grade-appropriate free sample
#### Production code locations
- `index.html`
  - Grade tabs markup: `.grade-tab` buttons and `.grade-panel` sections
  - Featured sample area: `.featured-preview`, `.featured-title`, `.featured-box`, `.featured-step`, `.featured-question`, `.featured-open-btn`
  - Grade tab JS: the script that toggles `.grade-panel.active`
- `store.html`
  - Grade-specific free sample cards are already explicitly mapped per grade and should be used as reference/ground truth during implementation
- `curriculum.html` and `curriculum/index.html`
  - Grade-specific free sample rows are already explicitly mapped per grade and should also be used as reference
- `lesson-plans/_generated/lesson-index-data.json`
  - Contains the canonical per-grade free sample entries (`k-milk-magic`, `free-gr1-celery-rainbow`, `free-gr2-salt-dough-fossil-factory`, `free-gr3-egg-drop-kitchen-challenge`, `free-gr4-apple-oxidation`, `free-gr5-bread-mold-terrarium`)

#### Root-cause note
- On the homepage, the grade tabs only swap the curriculum panels.
- The featured sample preview block below the tabs is hard-coded to Kindergarten (`Milk Magic`) and does not change when the selected grade tab changes.
- If the report is about “every grade showing the kindergarten sample,” `index.html` featured sample behavior is the primary production target.

### 3) Mobile subscribe popup/modal X does not close the modal
#### Production code locations
- `index.html`
  - Mobile-visible popup markup:
    - `#llcEmailPopup`
    - `#llcPopupClose`
    - `#llcSignupForm`
  - Popup CSS:
    - `.llc-popup-overlay`
    - `.llc-popup`
    - `.llc-popup-close`
    - mobile responsive popup rules under `@media (max-width: 480px)`
  - Popup JS:
    - `var overlay = document.getElementById('llcEmailPopup');`
    - `var closeBtn = document.getElementById('llcPopupClose');`
    - `function dismiss()`
    - `closeBtn.addEventListener('click', dismiss);`
    - overlay click handler

#### Root-cause note
- Handler wiring exists in the live homepage source, so the likely implementation area is interaction correctness on mobile: hit target, stacking, event flow, or scroll-lock/dismiss behavior, not missing popup wiring altogether.

### 4) Mobile navigation does not clearly expose pricing/about
#### Production code locations
- `index.html`
  - Desktop nav markup under `<nav>` with `.nav-links`
  - Mobile behavior under `@media (max-width: 768px)` where `.nav-links { display: none; }`
  - No replacement hamburger/menu/drawer/tabbed nav is currently provided on the homepage
- Adjacent public pages with the same pattern:
  - `store.html`
  - `terms.html`
  - `thank-you.html`
- `curriculum.html` keeps visible nav links in the current source, so the immediate reported homepage/mobile problem centers on `index.html`

#### Root-cause note
- This is a structural discoverability issue: mobile hides the navigation links with no alternate menu, leaving `Pricing` and `About` inaccessible from visible header nav.

## Observed live behavior snapshot (mobile viewport)

Viewport used for spot check: approximately iPhone 12 / 390×844.

### Homepage (`/`)
- Header nav links are hidden on mobile (`.nav-links` not visible), leaving only the logo and `Subscribe` CTA visible.
- Grade tabs are visible and switch the active grade panel correctly.
- The featured sample block below the tabs remains hard-coded to Kindergarten (`Milk Magic`) even after switching to Grade 3, confirming the likely root cause of the “every grade shows the kindergarten sample” report on the homepage.
- Kindergarten Unit 3 on the homepage visibly includes `Free Sample — Milk Magic` inline in the unit list.
- The popup `X` click handler does dismiss the overlay in browser automation, but the close target is very small and body scroll remained locked (`overflow: hidden`) after dismissal in the observed run. That means the live mobile complaint is consistent with a real interaction/usability bug even though the click listener exists.

### Curriculum routes (`/curriculum.html` and `/curriculum/`)
- The Animal Needs unit card shows `Free Sample — Milk Magic` inline once expanded on mobile.
- Current mobile nav remains visible on the curriculum page; the headline mobile-nav discoverability problem is therefore centered on the homepage, not the curriculum page.

### Store (`/store.html`)
- Free-sample cards are correctly grade-specific on mobile:
  - K → Milk Magic
  - 1 → Celery Rainbow
  - 2 → Salt Dough Fossil Factory
  - 3 → Egg Drop Kitchen Challenge
  - 4 → Apple Browning Experiment
  - 5 → Bread Mold Terrarium
- Store mobile nav also hides `.nav-links`, so it is an adjacent shared-pattern page. For this bug batch, it should be treated as reference-only unless the later implementation intentionally broadens the mobile-nav fix beyond the homepage.

## Verification checklist for the implementation/deploy pass

### Core pages
- `https://littlelabcoats.co/`
- `https://littlelabcoats.co/curriculum.html`
- `https://littlelabcoats.co/curriculum/`
- `https://littlelabcoats.co/store.html`
- `https://littlelabcoats.co/lesson-plans/index.html`

### Grade-specific free sample pages
- `https://littlelabcoats.co/lesson-plans/k-milk-magic.html`
- `https://littlelabcoats.co/lesson-plans/free-gr1-celery-rainbow.html`
- `https://littlelabcoats.co/lesson-plans/free-gr2-salt-dough-fossil-factory.html`
- `https://littlelabcoats.co/lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
- `https://littlelabcoats.co/lesson-plans/free-gr4-apple-oxidation.html`
- `https://littlelabcoats.co/lesson-plans/free-gr5-bread-mold-terrarium.html`

### Specific post-push checks to run
1. Homepage mobile viewport:
   - visible nav affordance exists
   - pricing is reachable
   - about/founder is reachable
2. Homepage sample-units section:
   - changing grade tabs updates the displayed free sample correctly, if the featured sample is intended to track grade selection
3. Homepage popup:
   - open subscribe popup
   - tap `X`
   - confirm popup closes and body scroll state returns to normal
4. Curriculum routes (`/curriculum.html` and `/curriculum/`):
   - Kindergarten Unit 3 no longer shows the misplaced free sample inside the unit list
5. Store page:
   - all grade sample cards still point to the correct grade-level free lesson
6. Lesson index:
   - per-grade free sample entries still match the canonical grade mapping

## Implementation guardrails for the next chunk
- Do **not** change the landing-page logo/header branding concept yet.
- Serena requested branding/logo options before any concept-level header change goes live.
- Allowed scope for this fix batch:
  - navigation visibility/usability improvements on mobile
  - behavior fixes for the popup close action
  - content/mapping corrections for free sample surfacing
- Preferred edit order:
  1. `index.html` for homepage/mobile nav/popup/featured sample behavior
  2. `curriculum.html` and `curriculum/index.html` for K Unit 3 sample-placement parity
  3. only touch generated lesson-index data/rendering files if the later implementation proves the lesson index itself is part of the bug
- Mobile-nav scope for the later implementation pass:
  - **In scope by default:** homepage `index.html`
  - **Only update if needed for consistency after homepage fix:** `store.html`, `terms.html`, `thank-you.html`
  - **Reference-only for this batch unless a mirrored defect is confirmed:** draft/legacy files such as `lesson-plans/landing-page.html`

## Checks completed during this audit chunk
- Repository source inspection with ripgrep/read across homepage, curriculum, store, and lesson-index files
- Live homepage fetch confirmed production HTML contains:
  - hidden mobile nav links under the mobile breakpoint
  - K Unit 3 free-sample markup
  - featured sample block
  - popup close markup and JS
- Browser automation spot check at mobile viewport on homepage, curriculum, and store confirmed:
  - homepage mobile nav links are hidden
  - homepage grade tabs switch panels but not the featured sample block
  - homepage popup `X` dismisses in automation, but the close target is tiny and body scroll stayed locked after close
  - curriculum routes show the misplaced Milk Magic row inside K Unit 3 when expanded
  - store free-sample cards are correctly grade-specific
- Public HTTP 200 verification for:
  - `/`
  - `/curriculum.html`
  - `/curriculum/`
  - `/store.html`
  - `/lesson-plans/index.html`
  - all six grade-specific free sample pages

## Current conclusion
The production fix path is centered on `index.html`, with parity cleanup required in `curriculum.html` and `curriculum/index.html`. `store.html` and the generated lesson index currently serve as grade-mapping references and live verification surfaces, not the primary root cause for the homepage-specific sample-switching bug.