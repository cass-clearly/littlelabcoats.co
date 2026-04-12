# Little Lab Coats Full-Library Review Program Tracker

Last updated: 2026-04-12
Purpose: durable batch tracker for running the whole lesson library through the required Rachel + Margaret review -> literal fixes -> republish -> directory/status-update workflow.

## Program rules

A lesson batch is only counted as reviewed in this tracker when all of these are true for that batch:
1. Rachel review artifact exists
2. Margaret review artifact exists
3. literal fixes are applied in repo
4. review/status surfaces are updated
5. batch commit and push are completed
6. post-publish public verification is recorded

If any item above is still missing, the batch stays in `in progress` or `needs republish`.

## Starting inventory source

Primary audit baseline:
- `lesson-plans/llc-remarq-review-audit-2026-04-12.md`

Key top-line audit facts from that baseline:
- canonical lesson pages: **205**
- lesson pages with repo proof of both Rachel + Margaret: **42**
- lesson pages with reviewer status unknown: **163**
- strongest already-proved reviewed area before this program pass: Grade 4 Life Science

## Batch queue strategy

Practical execution order:
1. coherent whole units with live review URLs already working
2. batches that still lack proved Rachel+Margaret review artifacts
3. batches where directory/review status visibility is weak
4. backend/Remarq reconciliation after content/review truth is recorded

## Batch ledger

| Batch ID | Scope | Status | Rachel | Margaret | Revisions | Directory/status updated | Commit+push | Public verify | Notes |
|---|---|---|---|---|---|---|---|---|---|
| gr5-ess1-unit1-review-batch-1 | Grade 5 ESS1 Unit 1 lessons 1-6 + refcard + quiz | completed | yes | yes | yes | yes | yes | yes | First concrete execution batch completed 2026-04-12. Commit `9a0c8c4` pushed to `origin/main`; backend document IDs were created/reconciled and representative live review HTML now serves the new ESS1 document IDs. |
| gr5-ls1-unit2-review-batch-1 | Grade 5 LS1 Unit 2 lessons 1-6 + lesson refcards + quiz | completed | yes | yes | yes | yes | yes | yes | Reviewer-first continuation resumed 2026-04-12 from direct source/live inspection because live comment feed was empty; see `lesson-plans/gr5-life-science-batch-review.md`. |
| gr2-ets1-unit1-review-batch-1 | Grade 2 ETS1 Unit 1 lessons 1-6 + lesson refcards + quiz | completed | yes | yes | no literal content changes needed | yes | yes | yes | Review notes are recorded in `lesson-plans/gr2-engineering-batch-review.md`; commit `aa52f75` fixed the generator/parser omission, and public lesson-index plus review-index verification now shows Grade 2 Engineering on the live status surfaces. |
| gr5-ets1-unit1-review-batch-1 | Grade 5 ETS1 Unit 1 lessons 1-6 + lesson refcards + quiz | completed | yes | yes | no literal lesson-content changes needed | yes | yes | yes | Review notes are recorded in `lesson-plans/gr5-engineering-batch-review.md`; this closeout pass added reviewed / revised status exposure to the generated directory surfaces and reran representative live lesson/refcard/quiz verification. |
| gr4-ets1-unit1-review-batch-1 | Grade 4 ETS1 Unit 1 lessons 1-6 + lesson refcards + quiz | completed | yes | yes | yes | yes | yes | yes | Review notes are recorded in `lesson-plans/gr4-engineering-batch-review.md`; this batch fixed the broken refcard vocabulary/materials rendering, tightened lesson/quiz evidence prompts, and reran representative live verification after push. |
| gr4-ls1-remarq-review-revise-loop | Grade 4 LS1 Units 1-2 lessons/refcards/quizzes | previously completed | yes | yes | yes | yes | yes | yes | Proven prior batch, see `lesson-plans/gr4-life-science-batch-review.md`. |

## Current next action

Next required ship step:
- resolve the next Grade 4 Earth & Space Science batch selection before continuing, because the current repo/index surface exposes both `gr4-ess1-*` and `gr4-ess2-*` lesson families for overlapping landform/weathering scope
- keep release gating strict: Rachel + Margaret review first, literal fixes second, public verification before counting anything as released
- if the next Grade 4/5 lane has duplicate or conflicting scaffolds, keep that ambiguity explicit before claiming a finished batch

## Candidate next batches after current one

Priority candidates:
- Grade 4 Earth & Space Science after the Grade 4 engineering lane, if the canonical ESS1/ESS2 scaffold choice is explicit enough to keep the tracker honest
- Grade 5 Physical Science or another Grade 5 domain with an existing durable review tracker, if one is added before the next pass
- Kindergarten PS3 Unit 2 sun/heat set after the Grade 4/5 engineering lane is cleared

## Notes for future continuation

- treat this file as the durable handoff artifact for the multi-batch program
- do not mark a batch complete just because a review note file exists
- keep each batch small enough to review, revise, push, and verify in one chunk
- prefer unit-shaped batches over random lesson-by-lesson hopping unless a blocker forces a surgical pass
- 2026-04-12 closeout note: the previously active Pollinators + Grade 4 LS1 open-comment set was rechecked and then closed in Remarq after live/source verification; those tracked documents now show `0` open top-level comments across that active set
- 2026-04-12 continuation note: Grade 5 LS1 Unit 2 had live review-mode coverage and stable document IDs but no current comment-feed artifact, so the batch resumed via direct source/live Rachel + Margaret review notes recorded in `lesson-plans/gr5-life-science-batch-review.md` before literal fixes were applied
