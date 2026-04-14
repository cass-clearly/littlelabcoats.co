# Calvin review worklist

Updated: 2026-04-14

## Active asks from Serena

### 1) Grade 3 Life Science Unit 1 overhaul
- Issue: Unit is repetitive, weak on novelty/value, and Lesson 2 is almost identical to Lesson 1.
- Required outcome:
  - Calvin audits the whole unit for repetition, continuity, and progression.
  - Duplicate/repetitive live lesson handling is decided and implemented.
  - Replacement lessons should not just be "look at the picture cards."
- Status: audit completed and urgent fix shipped on 2026-04-14.
- Durable artifacts:
  - `lesson-plans/gr3-ls1-unit1-calvin-audit-and-overhaul-plan-2026-04-14.md`
  - `lesson-plans/calvin-continuity-progression-rubric.md`
- Live sequencing action already taken:
  - `gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` retired from live sequencing pending rebuild.

### 2) Grade 3 Life Science Unit 2 overhaul
- Issue: same domain, unit 2 is also a mess and needs a complete overhaul.
- Required outcome:
  - Calvin weighs in on Unit 2 as well.
  - New lessons should have real progression, novelty, and engagement.
- Status: requested, not yet fully audited.

### 3) Durable tracking so jobs do not get lost
- Required outcome:
  - Keep an explicit list of Serena asks and job status.
  - Keep Calvin's reusable review standard in repo, not only in session memory.
- Status: active; this file tracks asks and `lesson-plans/calvin-continuity-progression-rubric.md` now holds the reusable rubric.

### 4) Explain the Grade 5 fossils fix clearly
- Serena asked what was actually fixed after an aborted message/run.
- Actual fix from commit `2c6e3f5`:
  - fossils lesson existed already: `lesson-plans/5th-fossils-earth-history.html`
  - problem was indexing/classification, not missing content
  - changed files:
    - `lesson-plans/_generated/lesson-index-data.json`
    - `lesson-plans/index.html`
    - `lesson-plans/review/index.html`
    - `scripts/generate-lesson-index-data.py`
- Status: fixed in repo, explanation delivered in chat.

### 5) Cross-grade/domain missing-content scan
- Required outcome:
  - Scan all grades/domains/units for missing content and progression gaps.
  - Keep a durable list of missing/planned content over time.
- Serena specifically flagged Grade 5 as incomplete and expects progression on:
  - inheritance and traits (life science)
  - space content (earth science)
  - atoms work (physical science)
  - fossils
  - weather
- Status: requested, should become part of Calvin's audit scope.

## Calvin mandate
Calvin is the reviewer for:
- continuity across a whole unit
- repetition and weak novelty
- knowledge progression across grades
- repeated experiments that should be differentiated
- checking that higher grades are meaningfully more advanced, not reworded duplicates

## Current Calvin job
- Session/job: `calvin-reviewer`
- Job id: `838f1678-2126-4659-b09e-f181282cc1a2`
- Current focus: start with Grade 3 Life Science Unit 1, then expand to Unit 2 and broader gap scan
