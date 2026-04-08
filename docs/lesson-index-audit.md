# Lesson Index Audit

Date: 2026-04-08

This audit locks the source-of-truth and routing decisions for the auto-updating lesson index page.

## Decision summary

- **Authoritative discovery source:** root-level HTML files in `lesson-plans/`
- **Do not discover from:** nested `lesson-plans/**/index.html` mirrors, because they duplicate the root lesson files
- **Chosen stable public URL for the index page:** `/lesson-plans/`
- **Chosen implementation file:** `lesson-plans/index.html`
- **Primary grouping strategy:** parse grade + domain + unit from the lesson filename slug
- **Fallback grouping:** put anything that is clearly a lesson but does not match the standard curriculum pattern into a standalone bucket instead of dropping it

## What exists in the repo

The site is a static HTML repo. There is no existing app/router/build pipeline in the repo root that can discover files at request time in the browser.

Relevant existing URL patterns:

- root pages like `/index.html`, `/curriculum.html`, `/store.html`
- directory-style pages like `/curriculum/` backed by `curriculum/index.html`
- lesson pages under `/lesson-plans/`
- many lesson pages exist in **both** forms:
  - `lesson-plans/<slug>.html`
  - `lesson-plans/<slug>/index.html`

The duplicated directory `index.html` pages appear to be mirrors for directory-style serving, not the best discovery source.

## Authoritative lesson discovery source

Use the **root-level files in `lesson-plans/*.html`** as the canonical discovery source for the lesson index generator.

Why this is the safest source:

1. It is a single flat directory, so discovery is simple and deterministic.
2. The nested `lesson-plans/<slug>/index.html` files duplicate many of the same lessons and would create duplicate index entries if scanned directly.
3. Existing manual curriculum pages already point heavily at the root-level lesson paths, so indexing those files preserves current canonical links.
4. The root filenames carry most of the structured metadata needed for grouping.

## File selection rules

The index generator should scan `lesson-plans/*.html` and keep only **lesson pages**.

### Include

Keep files that are actual lesson pages, including:

- normal grade/unit lessons such as:
  - `k-ess2-unit1-lesson1-what-is-weather.html`
  - `gr1-ess1-unit1-lesson1-the-sun.html`
  - `gr2-ps1-unit1-l1-matter.html`
  - `gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html`
- free sample lessons such as:
  - `free-gr3-egg-drop-kitchen-challenge.html`
- legitimate standalone lesson pages that do not match the standard naming pattern, such as:
  - `bird-beak-buffet.html`
  - `5th-fossils-earth-history.html`
  - `5th-forces-balanced-unbalanced.html`

### Exclude

Do not index these as lessons:

- refcards: filenames containing `refcard`
- quizzes: filenames containing `quiz`
- duplicated nested mirrors: `lesson-plans/**/index.html`
- internal docs / planning / review artifacts in `lesson-plans/`, for example names containing:
  - `audit`
  - `review`
  - `manifest`
  - `worksheet`
  - `competitor-analysis`
  - `daario-`
  - `document-id-manifest`
  - `shareable-manifest`
  - `style-guide`

## Metadata that is reliably discoverable

There is no consistent frontmatter or centralized content manifest in the lesson files.

The generator should rely on this priority order:

1. **Filename slug** (most reliable for grade/domain/unit parsing)
2. **`<title>` tag** for display title fallback
3. **`<h1>` tag** if needed, but treat it as optional/noisy because many pages include emoji or style markup

Observed metadata behavior:

- modern lessons often include both `<title>` and `<h1>`
- some pages place the `<h1>` later in the file, so shallow reads are not reliable
- some free/sample lessons support `?review=1`, some may not yet; the index should still append `?review=1` consistently because the requirement is to expose the review URL shape
- newer lesson files often include `data-document-id` and review-mode scripting, but those are not universal enough to make them the discovery source

## Filename parsing strategy

Parse metadata from the root lesson slug.

### Standard structured patterns

Support these curriculum-style patterns first:

- `k-<domain>-unit<unit>-lesson<lesson>-<title>`
- `gr<grade>-<domain>-unit<unit>-lesson<lesson>-<title>`
- `gr<grade>-<domain>-unit<unit>-l<lesson>-<title>`

Examples:

- `k-ps3-unit2-lesson4-melting-race`
- `gr1-ess1-unit1-lesson6-patterns-in-the-sky`
- `gr2-ps1-unit1-l4-mixing`
- `gr3-ets1-unit1-lesson2-researching-constraints-and-materials`

### Known legacy / irregular patterns

Also tolerate these without failing:

- `gr1-ls1-lesson1-animal-structures-biomimicry` (missing explicit `unit`)
- `unit1-lesson1-push-pull-sort` (kindergarten legacy pattern with no explicit grade/domain in filename)
- `5th-fossils-earth-history`
- `bird-beak-buffet`
- `free-gr4-apple-oxidation`

## Grouping strategy for the future index

Use a graceful parser, not a strict validator.

### Primary group levels

1. **Grade**
   - map `k` to `Kindergarten`
   - map `gr1`..`gr5` to `Grade 1`..`Grade 5`
   - map `5th` and similar legacy forms into the matching grade bucket when possible
2. **Domain**
   - `ps` => Physical Science
   - `ls` => Life Science
   - `ess` => Earth & Space Science
   - `ets` => Engineering / Design
3. **Unit**
   - derive from `unit<nr>` when present
4. **Lesson order**
   - derive from `lesson<nr>` or `l<nr>` when present

### Fallback buckets

If any dimension is missing, degrade gracefully:

- unknown grade => `Other Lessons`
- known grade but unknown domain => `Other Lessons` within that grade
- missing unit => sort directly under the grade/domain bucket as standalone items
- free samples => keep visible in the best matching grade bucket, optionally marked as free/sample in a later implementation chunk

This avoids dropping legitimate lesson pages just because older files do not fully match the newer naming pattern.

## Chosen stable route

Create the index page at:

- repo path: `lesson-plans/index.html`
- public URL: `/lesson-plans/`

Why this route is the best fit:

1. It is stable and memorable.
2. It sits next to the content it indexes.
3. It matches the repo’s existing directory-style URL pattern already used by `curriculum/index.html`.
4. It does not require changing any existing lesson URLs.
5. It leaves `/curriculum.html` alone as the parent library/marketing page while giving Chris and Serena a direct operational index URL.

## Implementation guidance for the next chunk

The next implementation chunk should:

1. add a small generator script that reads `lesson-plans/*.html`
2. normalize lesson entries into:
   - `title`
   - `slug`
   - `canonicalUrl`
   - `reviewUrl` (`canonicalUrl + '?review=1'`)
   - `grade`
   - `domain`
   - `unit`
   - `lessonNumber`
   - `bucket/fallbackGroup`
3. render those normalized entries into `lesson-plans/index.html`
4. avoid hand-maintained lesson arrays entirely

## Final locked choices for this chunk

- **Source of truth:** `lesson-plans/*.html`
- **Canonical lesson URL base:** `/lesson-plans/<slug>.html`
- **Review URL format:** `/lesson-plans/<slug>.html?review=1`
- **Index page URL:** `/lesson-plans/`
- **Grouping basis:** filename parsing first, HTML title second, fallback buckets for irregular lessons
