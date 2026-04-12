# Little Lab Coats UI / shell lane note — 2026-04-12

## Scope resumed in this pass
- verify the curriculum-library search fix on the real live site first
- only extend search if a real failing case remained
- spend the rest of the batch on visible grade 3–5 shell/presentation issues outside the active reviewer-content files

## Search verification result
Live verification on both public curriculum routes (`/curriculum.html` and `/curriculum/`) still showed a real failing case:
- searching `Grade 1` or `first grade` returned no results on the live site
- searching generic terms like `engineering` was still constrained by the default Kindergarten grade tab instead of searching across the full catalog

## Search implementation decision
Non-obvious choice logged here:
- **while a search query is active, the curriculum search now behaves as a cross-grade search surface instead of respecting the currently selected grade tab**
- the UI temporarily shows `All Grades` as the active chip during search, then returns to the previously selected grade tab when the query is cleared
- explicit grade phrases in the query (for example `Grade 1`, `first grade`, `kindergarten`, `grade 5 ecosystems`) are parsed as a grade filter instead of being treated like raw tokens, which avoids false positives from unit tags like `5-PS2-1`

## Shell consistency decision
Non-obvious choice logged here:
- for the public Grade 5 Life Science and Physical Science slash routes (`/lesson-plans/<slug>/`), the directory `index.html` files are now kept in lockstep with the canonical `.html` lesson/refcard/quiz files
- this avoids maintaining two visible shells for the same public route family and removes the stale slash-route variants that were still showing broken `undefined` subtitles

## Files expected in this batch
- `curriculum.html`
- `curriculum/index.html`
- Grade 5 LS1 slash-route `index.html` mirrors
- Grade 5 PS2 slash-route `index.html` mirrors
