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
| gr5-ess1-unit1-review-batch-1 | Grade 5 ESS1 Unit 1 lessons 1-6 + refcard + quiz | in progress | yes | yes | yes | yes | no | pre-edit review URLs verified; post-push pending | First concrete execution batch started 2026-04-12. Remarq backend IDs still unresolved at checked backend. |
| gr4-ls1-remarq-review-revise-loop | Grade 4 LS1 Units 1-2 lessons/refcards/quizzes | previously completed | yes | yes | yes | yes | yes | yes | Proven prior batch, see `lesson-plans/gr4-life-science-batch-review.md`. |

## Current next action

Next required ship step:
- finish the Grade 5 ESS1 Unit 1 repo edits already identified in `lesson-plans/gr5-earth-science-batch-review.md`
- commit and push that batch
- verify public production HTML after push
- then move to the next coherent batch

## Candidate next batches after current one

Priority candidates:
- Grade 5 LS1 Unit 2 plant matter & growth
- Kindergarten PS3 Unit 2 sun/heat set
- Grade 2 LS2 Unit 1 plant/pollinator/ecosystem set (after Remarq-path reconciliation planning)

## Notes for future continuation

- treat this file as the durable handoff artifact for the multi-batch program
- do not mark a batch complete just because a review note file exists
- keep each batch small enough to review, revise, push, and verify in one chunk
- prefer unit-shaped batches over random lesson-by-lesson hopping unless a blocker forces a surgical pass
