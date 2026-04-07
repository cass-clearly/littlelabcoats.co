# Free Lesson Public Mapping and Publish Prep

Last updated: 2026-04-07  
Chunk: `update-public-mappings-and-publish-prep`

This artifact records the repo-side public mapping updates for the K–5 free-lesson set.
It documents what the public-facing site files now point to in the repo.
It does **not** claim anything has been pushed or published live.

## Authoritative intended free-lesson map

| Grade | Intended free lesson | Lesson path |
| --- | --- | --- |
| K | Milk Magic | `lesson-plans/k-milk-magic.html` |
| 1 | Celery Rainbow | `lesson-plans/free-gr1-celery-rainbow.html` |
| 2 | Salt Dough Fossil Factory | `lesson-plans/free-gr2-salt-dough-fossil-factory.html` |
| 3 | Egg Drop Kitchen Challenge | `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html` |
| 4 | Apple Browning Experiment | `lesson-plans/free-gr4-apple-oxidation.html` |
| 5 | Bread Mold Terrarium | `lesson-plans/free-gr5-bread-mold-terrarium.html` |

## Post-change public mapping matrix

| Grade | Intended lesson | `store.html` | `index.html` | `curriculum.html` | `curriculum/index.html` | Status |
| --- | --- | --- | --- | --- | --- | --- |
| K | `k-milk-magic.html` | mapped via free sample card | mapped via featured sample block and K curriculum preview list | mapped via Free Lesson Spotlights and K unit list entry | mapped via Free Lesson Spotlights and K unit list entry | aligned |
| 1 | `free-gr1-celery-rainbow.html` | mapped via free sample card | mapped via free lesson sampler list | mapped via Free Lesson Spotlights | mapped via Free Lesson Spotlights | aligned |
| 2 | `free-gr2-salt-dough-fossil-factory.html` | mapped via free sample card | mapped via free lesson sampler list | mapped via Free Lesson Spotlights | mapped via Free Lesson Spotlights | aligned |
| 3 | `free-gr3-egg-drop-kitchen-challenge.html` | mapped via free sample card | mapped via free lesson sampler list | mapped via Free Lesson Spotlights | mapped via Free Lesson Spotlights | aligned |
| 4 | `free-gr4-apple-oxidation.html` | mapped via free sample card | mapped via free lesson sampler list | mapped via Free Lesson Spotlights | mapped via Free Lesson Spotlights | aligned |
| 5 | `free-gr5-bread-mold-terrarium.html` | mapped via free sample card | mapped via free lesson sampler list | mapped via Free Lesson Spotlights | mapped via Free Lesson Spotlights | aligned |

## Kindergarten discrepancy handling

Resolved for repo-side public mappings in this chunk:
- Active Kindergarten freebie mapping now uses `lesson-plans/k-milk-magic.html`
- The older archival file `lesson-plans/free-k-fizzy-color-explosions.html` remains in the repo for history only
- The prior public free-sample target `lesson-plans/k-ls1-unit3-lesson1-what-do-animals-need.html` was replaced on the edited public sample/navigation surfaces updated in this chunk

## Files changed for mapping alignment

- `store.html`
- `index.html`
- `curriculum.html`
- `curriculum/index.html`
- `lesson-plans/free-lesson-public-mapping-and-publish-prep.md`

## Remaining manual publish steps

1. Review the changed public/catalog files in a browser or staging preview
2. Confirm visual layout still works across desktop and mobile for:
   - store free sample cards
   - homepage featured sample block
   - curriculum Free Lesson Spotlights sections
3. Push the repo changes through the normal publish/deploy workflow
4. Verify the live site reflects the updated free mappings after deployment
5. Spot-check all six public lesson URLs on the live site

## Unresolved questions for human review

- None identified in repo mapping logic after this pass
- The canonical Animal Needs unit still exists in the repo, but edited public surfacing now leads Kindergarten free-sample discovery with `k-milk-magic.html`
- If the team wants a different merchandising strategy than a K–5 free sampler on store/homepage/curriculum, that would be a product decision rather than a mapping-correction issue

## Final human-ready handoff review

### Repo readiness checklist

- Audit source of truth exists: `lesson-plans/free-lesson-audit-and-scope.md`
- Review history exists with Rachel + Margaret comments: `lesson-plans/free-lesson-batch-review.md`
- Review-driven revisions are logged and verified in repo files
- K–5 free packages each contain lesson + refcard + quiz
- Edited public/catalog surfaces point to the intended K–5 free lessons in repo state
- Kindergarten freebie authority remains `k-milk-magic.html`
- No live/publish claim is made in this repo pass

### Human review focus before publish

- Visual QA on the new store free-sample cards
- Visual QA on the homepage featured sample and K–5 sampler list
- Visual QA on the curriculum Free Lesson Spotlights sections
- Sanity-check that the canonical Animal Needs unit still makes sense as curriculum while Milk Magic leads free-sample discovery

## Handoff summary

Repo-side public free-lesson mappings are now aligned to the audited K–5 intended targets and the artifact set is ready for human review/publish preparation.
Nothing in this file should be read as a claim that the site is already live with these changes.
