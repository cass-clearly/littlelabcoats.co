# Learning Objective Library Audit

Date: 2026-04-09

This audit locks the source-of-truth lesson set and identifies which lesson pages already follow the established Learning Objective pattern versus which pages need updates in the implementation chunk.

## Scope and source of truth

- **Authoritative lesson source:** `lesson-plans/_generated/lesson-index-data.json`, backed by canonical root lesson files in `lesson-plans/*.html`
- **Why this source:** it already encodes the approved root-level lesson discovery rules and avoids duplicate nested mirror pages
- **Excluded from scope:** quizzes, refcards, worksheets, audit/review/planning docs, and nested mirror pages like `lesson-plans/<slug>/index.html`
- **Lesson pages in scope:** 151

This matches the current operational lesson-library convention already documented for discovery/indexing: root-level lesson HTML files are the canonical source, not nested directory mirrors.

## Locked canonical pattern

**Source-of-truth rule:** the lesson must include a standalone `Learning Objective` or `Learning Objectives` section as the **first top-level lesson section** after the standards/top matter and **before** `The Big Idea`, `The Science`, `Materials`, and the rest of the lesson flow.

Accepted canonical shape:

1. title / subtitle / meta / hero / standards top matter
2. `h2` = `🎯 Learning Objective` or `🎯 Learning Objectives`
3. objective content as paragraph, bullet list, or boxed objective block
4. next top-level section is the concept section (`The Big Idea`, `The Big Science Idea`, `The Science`, etc.)
5. `Materials` remains after conceptual top matter so preview/paywall behavior can still lock from `Materials` where implemented

### Canonical example lessons

- `lesson-plans/gr1-ess1-unit1-lesson1-the-sun.html`
  - First sections: `🎯 Learning Objectives` → `🔬 The Big Science Idea` → `📦 Materials` → `🔬 Let's Investigate — Shadow Tracking!` → `💬 Discussion Questions`
  - Pattern variant: plural `Learning Objectives` followed by bullet-list outcomes, then `The Big Science Idea`.
- `lesson-plans/gr1-ets1-unit1-lesson1-what-problem-can-we-solve.html`
  - First sections: `🎯 Learning Objective` → `💡 The Big Idea` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Pattern variant: singular `Learning Objective` followed by a paragraph, then `The Big Idea`.
- `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html`
  - First sections: `🎯 Learning Objective` → `💡 The Big Idea` → `🔬 The Science` → `Materials` → `Let's Get Started`
  - Pattern variant: singular `Learning Objective` followed by an `.objective-box`, then `The Big Idea`; this is also the modern preview/paywall-safe pattern that keeps the objective visible before `Materials`.

## Audit method

- `compliant` = page contains `Learning Objective`/`Learning Objectives` and that heading is the first top-level `h2` in the lesson body
- `missing` = page has no standalone Learning Objective section at all
- `misplaced` = page mentions Learning Objective somewhere, but not as the first top-level section
- edge cases are called out separately when a page uses `Learning Goals` or an inline tip-box objective instead of the canonical first section

## Summary

- **Compliant:** 68
- **Missing:** 82
- **Misplaced:** 1

### By lesson bucket

- `1-ess`: compliant 6
- `1-ets`: compliant 6
- `1-free-samples`: missing 1
- `1-ls`: compliant 6, missing 6
- `1-ps`: compliant 6
- `2-ess`: missing 6
- `2-free-samples`: missing 1
- `2-ls`: compliant 6, missing 6
- `2-ps`: compliant 1, missing 6
- `3-ess`: compliant 6
- `3-ets`: compliant 6
- `3-free-samples`: missing 1
- `3-ls`: compliant 6
- `3-ps`: missing 6
- `4-free-samples`: missing 1
- `4-ls`: missing 12
- `5-ess`: missing 1
- `5-free-samples`: missing 1
- `5-other`: missing 2
- `5-ps`: compliant 1
- `k-ess`: compliant 6, missing 6
- `k-ets`: compliant 6
- `k-free-samples`: missing 1
- `k-ls`: compliant 6, missing 5, misplaced 1
- `k-other`: missing 6
- `k-ps`: missing 6
- `other-lessons`: missing 8

## Spot-check notes

- `lesson-plans/k-ls1-unit2-lesson4-sunlight-or-no-sunlight.html` — **misplaced**
  - First sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: objective exists only as inline tip-box content, not first section
- `lesson-plans/free-gr1-celery-rainbow.html` — **missing**
  - First sections: `🔬 The Science` → `📚 Learning Goals` → `📦 Materials` → `🔬 Let's Get Started` → `❓ Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/5th-forces-balanced-unbalanced.html` — **missing**
  - First sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr1-ess1-unit1-lesson1-the-sun.html` — **compliant**
  - First sections: `🎯 Learning Objectives` → `🔬 The Big Science Idea` → `📦 Materials` → `🔬 Let's Investigate — Shadow Tracking!` → `💬 Discussion Questions`
- `lesson-plans/gr1-ets1-unit1-lesson1-what-problem-can-we-solve.html` — **compliant**
  - First sections: `🎯 Learning Objective` → `💡 The Big Idea` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
- `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html` — **compliant**
  - First sections: `🎯 Learning Objective` → `💡 The Big Idea` → `🔬 The Science` → `Materials` → `Let's Get Started`

## Concrete target list for the implementation chunk

These pages need updates to meet the library-wide standard.

### Misplaced Learning Objective

- `lesson-plans/k-ls1-unit2-lesson4-sunlight-or-no-sunlight.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: objective exists only as inline tip-box content, not first section

### Missing Learning Objective

- `lesson-plans/5th-forces-balanced-unbalanced.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/5th-fossils-earth-history.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 Background Science (for Parent/Teacher)` → `🚀 Lesson Flow` → `📦 What You'll Need` → `🔬 Hands-On Activity: Cast & Mold Fossil Investigation (20–25 min)`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/bird-beak-buffet.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔧 Setup (5 minutes)` → `🔬 Let's Get Started`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/forces-motion-acceleration.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `🛠️ The Engineering Challenge` → `📦 Materials` → `🔬 Let's Get Started`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/free-gr1-celery-rainbow.html`
  - Current first sections: `🔬 The Science` → `📚 Learning Goals` → `📦 Materials` → `🔬 Let's Get Started` → `❓ Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/free-gr2-salt-dough-fossil-factory.html`
  - Current first sections: `🔬 The Science` → `📚 Learning Goals` → `📦 Materials` → `🔬 Let's Get Started` → `❓ Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html`
  - Current first sections: `🔬 The Science` → `📚 Learning Goals` → `📦 Materials` → `🔬 Let's Get Started` → `❓ Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/free-gr4-apple-oxidation.html`
  - Current first sections: `🔬 The Science` → `📚 Learning Goals` → `📦 Materials` → `🔬 Let's Get Started` → `❓ Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/free-gr5-bread-mold-terrarium.html`
  - Current first sections: `🔬 The Science` → `📚 Learning Goals` → `📦 Materials` → `🔬 Let's Get Started` → `❓ Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/free-k-fizzy-color-explosions.html`
  - Current first sections: `🔬 The Science` → `📚 Learning Goals` → `📦 Materials` → `🔬 Let's Get Started` → `❓ Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr1-ls3-unit2-lesson1-you-look-like-your-parents.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `📚 Background (Read Aloud to Student)` → `🔬 Procedure`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr1-ls3-unit2-lesson2-baby-animals-and-needs.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `📚 Background (Read Aloud to Student)` → `🔬 Procedure`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr1-ls3-unit2-lesson3-parents-protect-offspring.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `📚 Background (Read Aloud to Student)` → `🔬 Procedure`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr1-ls3-unit2-lesson4-parents-teach-offspring.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `📚 Background (Read Aloud to Student)` → `🔬 Procedure`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr1-ls3-unit2-lesson5-plant-parenting.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `📚 Background (Read Aloud to Student)` → `🔬 Procedure`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr1-ls3-unit2-lesson6-patterns-parent-offspring.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `📚 Background (Read Aloud to Student)` → `🔬 Procedure`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ess1-unit3-l1-landforms.html`
  - Current first sections: `&#x1F3AF; Learning Goals` → `&#x1F4E6; Materials` → `&#x1F4D6; Vocabulary` → `&#x1F52C; Background` → `&#x1F9EA; Activity: Landform Builder`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ess1-unit3-l2-rocks-soils.html`
  - Current first sections: `&#x1F3AF; Learning Goals` → `&#x1F4E6; Materials` → `&#x1F4D6; Vocabulary` → `&#x1F52C; Background` → `&#x1F9EA; Activity: Rock Properties Chart & Soil Shake`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ess1-unit3-l3-erosion.html`
  - Current first sections: `&#x1F3AF; Learning Goals` → `&#x1F4E6; Materials` → `&#x1F4D6; Vocabulary` → `&#x1F52C; Background` → `&#x1F9EA; Activity: Erosion Experiment`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ess1-unit3-l4-maps.html`
  - Current first sections: `&#x1F3AF; Learning Goals` → `&#x1F4E6; Materials` → `&#x1F4D6; Vocabulary` → `&#x1F52C; Background` → `&#x1F9EA; Activity: Room Map`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ess1-unit3-l5-weather-patterns.html`
  - Current first sections: `&#x1F3AF; Learning Goals` → `&#x1F4E6; Materials` → `&#x1F4D6; Vocabulary` → `&#x1F52C; Background` → `&#x1F9EA; Activity: 5-Day Weather Journal`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ess1-unit3-l6-erosion-engineering.html`
  - Current first sections: `&#x1F3AF; Learning Goals` → `&#x1F4E6; Materials` → `&#x1F4D6; Vocabulary` → `&#x1F52C; Background` → `&#x1F9EA; Activity: Erosion Barrier Challenge`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ls2-unit2-l1-ecosystems.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `🌍 Background` → `🔬 Activity: Ecosystem Map`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ls2-unit2-l2-plants-partners.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `🌍 Background` → `🔬 Activity: Pollinator Simulation`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ls2-unit2-l3-food-chains.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `🌍 Background` → `🔬 Activity: Food Chain Mobile`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ls2-unit2-l4-predator-prey.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `🌍 Background` → `🔬 Activity: Population Tag`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ls2-unit2-l5-habitat-hunt.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `🌍 Background` → `🔬 Activity: 20-Minute Habitat Hunt`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ls2-unit2-l6-design-habitat.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `🌍 Background` → `🐾 Know Your Animal`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ps1-unit1-l1-matter.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `🌍 Background` → `🔬 Procedure: The Matter Sort`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ps1-unit1-l2-texture.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `🌍 Background` → `🔬 Procedure: The Materials Properties Investigation`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ps1-unit1-l3-sink-float.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `🌍 Background` → `🔬 Procedure: The Sink or Float Investigation`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ps1-unit1-l4-mixing.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `🌍 Background` → `🔬 Procedure: Two Mixing Experiments`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ps1-unit1-l5-heating-cooling.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `🌍 Background` → `🔬 Procedure: Three Heating and Cooling Experiments`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr2-ps1-unit1-l6-boat-engineering.html`
  - Current first sections: `🎯 Learning Goals` → `📦 Materials` → `📖 Vocabulary` → `🌍 Background` → `🔬 Procedure: Design, Build, Test, Improve!`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html`
  - Current first sections: `💡 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
- `lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html`
  - Current first sections: `💡 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
- `lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html`
  - Current first sections: `💡 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
- `lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html`
  - Current first sections: `💡 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
- `lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html`
  - Current first sections: `💡 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
- `lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html`
  - Current first sections: `💡 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
- `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html`
  - Current first sections: `The Big Idea` → `The Science` → `Materials` → `Let's Get Started` → `Discussion Questions`
- `lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html`
  - Current first sections: `The Big Idea` → `The Science` → `Materials` → `Let's Get Started` → `Discussion Questions`
- `lesson-plans/gr4-ls1-unit1-lesson3-mouths-beaks-teeth-and-getting-food.html`
  - Current first sections: `The Big Idea` → `The Science` → `Materials` → `Let's Get Started` → `Discussion Questions`
- `lesson-plans/gr4-ls1-unit1-lesson4-movement-structures-and-finding-safety.html`
  - Current first sections: `The Big Idea` → `The Science` → `Materials` → `Let's Get Started` → `Discussion Questions`
- `lesson-plans/gr4-ls1-unit1-lesson5-structures-for-protection-and-defense.html`
  - Current first sections: `The Big Idea` → `The Science` → `Materials` → `Let's Get Started` → `Discussion Questions`
- `lesson-plans/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html`
  - Current first sections: `The Big Idea` → `The Science` → `Materials` → `Let's Get Started` → `Discussion Questions`
- `lesson-plans/gr4-ls1-unit2-lesson1-roots-stems-and-plant-support-systems.html`
  - Current first sections: `The Big Idea` → `The Science` → `Materials` → `Let's Get Started` → `Discussion Questions`
- `lesson-plans/gr4-ls1-unit2-lesson2-leaves-and-making-food.html`
  - Current first sections: `The Big Idea` → `The Science` → `Materials` → `Let's Get Started` → `Discussion Questions`
- `lesson-plans/gr4-ls1-unit2-lesson3-water-transport-inside-plants.html`
  - Current first sections: `The Big Idea` → `The Science` → `Materials` → `Let's Get Started` → `Discussion Questions`
- `lesson-plans/gr4-ls1-unit2-lesson4-flowers-pollination-and-reproduction.html`
  - Current first sections: `The Big Idea` → `The Science` → `Materials` → `Let's Get Started` → `Discussion Questions`
- `lesson-plans/gr4-ls1-unit2-lesson5-seeds-fruits-and-new-plants.html`
  - Current first sections: `The Big Idea` → `The Science` → `Materials` → `Let's Get Started` → `Discussion Questions`
- `lesson-plans/gr4-ls1-unit2-lesson6-construct-an-argument-plant-structures.html`
  - Current first sections: `The Big Idea` → `The Science` → `Materials` → `Let's Get Started` → `Discussion Questions`
- `lesson-plans/gr5-ess3-unit1-l1-human-impact.html`
  - Current first sections: `🎯 Learning Goals` → `💡 The Big Idea` → `📦 Materials` → `🔬 Part 1 -- Pollution Simulation (15 min)` → `📋 Part 2 -- Impact Audit (20 min)`
  - Note: uses Learning Goals label instead of Learning Objective
  - Note: objective exists only as inline tip-box content, not first section
- `lesson-plans/k-ess3-unit2-lesson1-what-earth-gives-us.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ess3-unit2-lesson2-water-resource.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ess3-unit2-lesson3-soil.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ess3-unit2-lesson4-humans-change-earth.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 The Three Scenarios — Before & After` → `🔬 Let's Get Started`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ess3-unit2-lesson5-weather-hazards.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `🌪️ The Four Major Weather Hazards` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ess3-unit2-lesson6-being-earths-helper.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🌍 The Four Earth Problems — Pick ONE!` → `💚 Example Earth Helper Actions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ls1-unit2-lesson1-whats-inside-a-seed.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🌿 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ls1-unit2-lesson2-planting-day.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ls1-unit2-lesson3-parts-of-a-plant.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Question`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ls1-unit2-lesson5-seed-travelers.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ls1-unit2-lesson6-plant-life-cycle.html`
  - Current first sections: `🎓 Unit 2 Wrap-Up — Super Seeds & Perfect Plants` → `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-milk-magic.html`
  - Current first sections: `💡 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let’s Get Started` → `💬 Discussion Questions`
- `lesson-plans/k-ps3-unit2-lesson1-sun-warms-everything.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Question`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ps3-unit2-lesson2-shadow-science.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Question`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ps3-unit2-lesson3-dark-vs-light-surfaces.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Question`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ps3-unit2-lesson4-melting-race.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Question`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ps3-unit2-lesson5-design-sun-shelter-plan.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science Behind Good Design` → `📦 Materials for Planning Today` → `🔬 Let's Get Started` → `💬 Discussion Question`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/k-ps3-unit2-lesson6-design-sun-shelter-build.html`
  - Current first sections: `🎯 The Big Idea` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Question (Unit Wrap-Up)` → `🚀 Extensions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/ocean-L1-coral-kingdom.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/ocean-L2-sharks-built-to-hunt.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/ocean-L3-into-the-abyss.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/ocean-L4-ocean-in-motion.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/thermal-energy-ice-cream.html`
  - Current first sections: `🔬 The Science` → `📚 Learning Goals` → `📦 Materials` → `🔬 Procedure` → `❓ Discussion Questions & Answers`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/unit1-lesson1-push-pull-sort.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/unit1-lesson2-ramp-racers.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/unit1-lesson3-strong-push-gentle-push.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/unit1-lesson4-magnet-magic.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/unit1-lesson5-wind-wagon.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective
- `lesson-plans/unit1-lesson6-marble-run.html`
  - Current first sections: `🎯 The Big Idea` → `🔬 The Science` → `📦 Materials` → `🔬 Let's Get Started` → `💬 Discussion Questions`
  - Note: uses Learning Goals label instead of Learning Objective

## Full lesson inventory in scope

- `lesson-plans/k-ps3-unit2-lesson1-sun-warms-everything.html` — **missing**
- `lesson-plans/k-ps3-unit2-lesson2-shadow-science.html` — **missing**
- `lesson-plans/k-ps3-unit2-lesson3-dark-vs-light-surfaces.html` — **missing**
- `lesson-plans/k-ps3-unit2-lesson4-melting-race.html` — **missing**
- `lesson-plans/k-ps3-unit2-lesson5-design-sun-shelter-plan.html` — **missing**
- `lesson-plans/k-ps3-unit2-lesson6-design-sun-shelter-build.html` — **missing**
- `lesson-plans/k-ls1-unit2-lesson1-whats-inside-a-seed.html` — **missing**
- `lesson-plans/k-ls1-unit2-lesson2-planting-day.html` — **missing**
- `lesson-plans/k-ls1-unit2-lesson3-parts-of-a-plant.html` — **missing**
- `lesson-plans/k-ls1-unit2-lesson4-sunlight-or-no-sunlight.html` — **misplaced**
- `lesson-plans/k-ls1-unit2-lesson5-seed-travelers.html` — **missing**
- `lesson-plans/k-ls1-unit2-lesson6-plant-life-cycle.html` — **missing**
- `lesson-plans/k-ls1-unit3-lesson1-what-do-animals-need.html` — **compliant**
- `lesson-plans/k-ls1-unit3-lesson2-whats-for-dinner.html` — **compliant**
- `lesson-plans/k-ls1-unit3-lesson3-breathing.html` — **compliant**
- `lesson-plans/k-ls1-unit3-lesson4-how-animals-drink.html` — **compliant**
- `lesson-plans/k-ls1-unit3-lesson5-building-a-shelter.html` — **compliant**
- `lesson-plans/k-ls1-unit3-lesson6-when-needs-arent-met.html` — **compliant**
- `lesson-plans/k-ess2-unit1-lesson1-what-is-weather.html` — **compliant**
- `lesson-plans/k-ess2-unit1-lesson2-wind.html` — **compliant**
- `lesson-plans/k-ess2-unit1-lesson3-water-cycle.html` — **compliant**
- `lesson-plans/k-ess2-unit1-lesson4-four-seasons.html` — **compliant**
- `lesson-plans/k-ess2-unit1-lesson5-animals-and-weather.html` — **compliant**
- `lesson-plans/k-ess2-unit1-lesson6-weather-patterns.html` — **compliant**
- `lesson-plans/k-ess3-unit2-lesson1-what-earth-gives-us.html` — **missing**
- `lesson-plans/k-ess3-unit2-lesson2-water-resource.html` — **missing**
- `lesson-plans/k-ess3-unit2-lesson3-soil.html` — **missing**
- `lesson-plans/k-ess3-unit2-lesson4-humans-change-earth.html` — **missing**
- `lesson-plans/k-ess3-unit2-lesson5-weather-hazards.html` — **missing**
- `lesson-plans/k-ess3-unit2-lesson6-being-earths-helper.html` — **missing**
- `lesson-plans/k-ets1-unit1-lesson1-what-is-a-problem.html` — **compliant**
- `lesson-plans/k-ets1-unit1-lesson2-ask-questions.html` — **compliant**
- `lesson-plans/k-ets1-unit1-lesson3-draw-your-idea.html` — **compliant**
- `lesson-plans/k-ets1-unit1-lesson4-build-it.html` — **compliant**
- `lesson-plans/k-ets1-unit1-lesson5-test-and-improve.html` — **compliant**
- `lesson-plans/k-ets1-unit1-lesson6-share-your-solution.html` — **compliant**
- `lesson-plans/unit1-lesson1-push-pull-sort.html` — **missing**
- `lesson-plans/unit1-lesson2-ramp-racers.html` — **missing**
- `lesson-plans/unit1-lesson3-strong-push-gentle-push.html` — **missing**
- `lesson-plans/unit1-lesson4-magnet-magic.html` — **missing**
- `lesson-plans/unit1-lesson5-wind-wagon.html` — **missing**
- `lesson-plans/unit1-lesson6-marble-run.html` — **missing**
- `lesson-plans/free-k-fizzy-color-explosions.html` — **missing**
- `lesson-plans/gr1-ps4-unit1-lesson1-sound-is-vibration.html` — **compliant**
- `lesson-plans/gr1-ps4-unit1-lesson2-light-travels.html` — **compliant**
- `lesson-plans/gr1-ps4-unit1-lesson3-mirrors-and-communication.html` — **compliant**
- `lesson-plans/gr1-ps4-unit1-lesson4-vibrating-strings-and-sound.html` — **compliant**
- `lesson-plans/gr1-ps4-unit1-lesson5-sound-through-solids-liquids-gases.html` — **compliant**
- `lesson-plans/gr1-ps4-unit1-lesson6-design-a-sound-sender.html` — **compliant**
- `lesson-plans/gr1-ls1-unit1-lesson2-plant-parts-functions.html` — **compliant**
- `lesson-plans/gr1-ls1-unit1-lesson3-animal-protection.html` — **compliant**
- `lesson-plans/gr1-ls1-unit1-lesson4-plants-attract-pollinators.html` — **compliant**
- `lesson-plans/gr1-ls1-unit1-lesson5-structures-for-getting-food.html` — **compliant**
- `lesson-plans/gr1-ls1-unit1-lesson6-structures-for-moving.html` — **compliant**
- `lesson-plans/gr1-ls3-unit2-lesson1-you-look-like-your-parents.html` — **missing**
- `lesson-plans/gr1-ls3-unit2-lesson2-baby-animals-and-needs.html` — **missing**
- `lesson-plans/gr1-ls3-unit2-lesson3-parents-protect-offspring.html` — **missing**
- `lesson-plans/gr1-ls3-unit2-lesson4-parents-teach-offspring.html` — **missing**
- `lesson-plans/gr1-ls3-unit2-lesson5-plant-parenting.html` — **missing**
- `lesson-plans/gr1-ls3-unit2-lesson6-patterns-parent-offspring.html` — **missing**
- `lesson-plans/gr1-ls1-lesson1-animal-structures-biomimicry.html` — **compliant**
- `lesson-plans/gr1-ess1-unit1-lesson1-the-sun.html` — **compliant**
- `lesson-plans/gr1-ess1-unit1-lesson2-the-moon.html` — **compliant**
- `lesson-plans/gr1-ess1-unit1-lesson3-stars.html` — **compliant**
- `lesson-plans/gr1-ess1-unit1-lesson4-daylight-and-seasons.html` — **compliant**
- `lesson-plans/gr1-ess1-unit1-lesson5-sky-changes.html` — **compliant**
- `lesson-plans/gr1-ess1-unit1-lesson6-patterns-in-the-sky.html` — **compliant**
- `lesson-plans/gr1-ets1-unit1-lesson1-what-problem-can-we-solve.html` — **compliant**
- `lesson-plans/gr1-ets1-unit1-lesson2-look-at-animal-solutions.html` — **compliant**
- `lesson-plans/gr1-ets1-unit1-lesson3-plan-a-nature-inspired-tool.html` — **compliant**
- `lesson-plans/gr1-ets1-unit1-lesson4-build-your-first-model.html` — **compliant**
- `lesson-plans/gr1-ets1-unit1-lesson5-test-and-improve-your-design.html` — **compliant**
- `lesson-plans/gr1-ets1-unit1-lesson6-share-your-final-design.html` — **compliant**
- `lesson-plans/free-gr1-celery-rainbow.html` — **missing**
- `lesson-plans/gr2-ps1-unit1-l1-matter.html` — **missing**
- `lesson-plans/gr2-ps1-unit1-l2-texture.html` — **missing**
- `lesson-plans/gr2-ps1-unit1-l3-sink-float.html` — **missing**
- `lesson-plans/gr2-ps1-unit1-l4-mixing.html` — **missing**
- `lesson-plans/gr2-ps1-unit1-l5-heating-cooling.html` — **missing**
- `lesson-plans/gr2-ps1-unit1-l6-boat-engineering.html` — **missing**
- `lesson-plans/gr2-ps1-lesson1-mystery-powders.html` — **compliant**
- `lesson-plans/gr2-ls2-unit1-lesson1-what-do-plants-need.html` — **compliant**
- `lesson-plans/gr2-ls2-unit1-lesson2-pollinators.html` — **compliant**
- `lesson-plans/gr2-ls2-unit1-lesson3-seed-dispersal.html` — **compliant**
- `lesson-plans/gr2-ls2-unit1-lesson4-food-chains.html` — **compliant**
- `lesson-plans/gr2-ls2-unit1-lesson5-habitats.html` — **compliant**
- `lesson-plans/gr2-ls2-unit1-lesson6-ecosystems-under-threat.html` — **compliant**
- `lesson-plans/gr2-ls2-unit2-l1-ecosystems.html` — **missing**
- `lesson-plans/gr2-ls2-unit2-l2-plants-partners.html` — **missing**
- `lesson-plans/gr2-ls2-unit2-l3-food-chains.html` — **missing**
- `lesson-plans/gr2-ls2-unit2-l4-predator-prey.html` — **missing**
- `lesson-plans/gr2-ls2-unit2-l5-habitat-hunt.html` — **missing**
- `lesson-plans/gr2-ls2-unit2-l6-design-habitat.html` — **missing**
- `lesson-plans/gr2-ess1-unit3-l1-landforms.html` — **missing**
- `lesson-plans/gr2-ess1-unit3-l2-rocks-soils.html` — **missing**
- `lesson-plans/gr2-ess1-unit3-l3-erosion.html` — **missing**
- `lesson-plans/gr2-ess1-unit3-l4-maps.html` — **missing**
- `lesson-plans/gr2-ess1-unit3-l5-weather-patterns.html` — **missing**
- `lesson-plans/gr2-ess1-unit3-l6-erosion-engineering.html` — **missing**
- `lesson-plans/free-gr2-salt-dough-fossil-factory.html` — **missing**
- `lesson-plans/gr3-ps2-unit1-lesson1-balanced-and-unbalanced-forces.html` — **missing**
- `lesson-plans/gr3-ps2-unit1-lesson2-motion-changes-with-force.html` — **missing**
- `lesson-plans/gr3-ps2-unit1-lesson3-magnets-pull-without-touching.html` — **missing**
- `lesson-plans/gr3-ps2-unit1-lesson4-magnetic-patterns.html` — **missing**
- `lesson-plans/gr3-ps2-unit1-lesson5-design-a-magnetic-game-or-tool.html` — **missing**
- `lesson-plans/gr3-ps2-unit1-lesson6-test-and-improve-your-force-design.html` — **missing**
- `lesson-plans/gr3-ls1-unit1-lesson1-what-is-a-life-cycle.html` — **compliant**
- `lesson-plans/gr3-ls1-unit1-lesson2-different-life-cycles-same-big-pattern.html` — **compliant**
- `lesson-plans/gr3-ls1-unit1-lesson3-plant-life-cycles-and-seeds.html` — **compliant**
- `lesson-plans/gr3-ls1-unit1-lesson4-animal-life-cycles-and-metamorphosis.html` — **compliant**
- `lesson-plans/gr3-ls1-unit1-lesson5-comparing-life-cycle-patterns.html` — **compliant**
- `lesson-plans/gr3-ls1-unit1-lesson6-model-and-explain-a-life-cycle.html` — **compliant**
- `lesson-plans/gr3-ess2-unit1-lesson1-weather-patterns-over-time.html` — **compliant**
- `lesson-plans/gr3-ess2-unit1-lesson2-climate-regions-and-conditions.html` — **compliant**
- `lesson-plans/gr3-ess2-unit1-lesson3-reading-weather-data.html` — **compliant**
- `lesson-plans/gr3-ess2-unit1-lesson4-weather-hazards-and-impacts.html` — **compliant**
- `lesson-plans/gr3-ess2-unit1-lesson5-designing-for-local-weather.html` — **compliant**
- `lesson-plans/gr3-ess2-unit1-lesson6-reducing-weather-related-hazards.html` — **compliant**
- `lesson-plans/gr3-ets1-unit1-lesson1-defining-the-problem.html` — **compliant**
- `lesson-plans/gr3-ets1-unit1-lesson2-researching-constraints-and-materials.html` — **compliant**
- `lesson-plans/gr3-ets1-unit1-lesson3-planning-a-solution.html` — **compliant**
- `lesson-plans/gr3-ets1-unit1-lesson4-building-and-testing-a-prototype.html` — **compliant**
- `lesson-plans/gr3-ets1-unit1-lesson5-improving-the-design.html` — **compliant**
- `lesson-plans/gr3-ets1-unit1-lesson6-share-and-defend-your-solution.html` — **compliant**
- `lesson-plans/free-gr3-egg-drop-kitchen-challenge.html` — **missing**
- `lesson-plans/gr4-ls1-unit1-lesson1-external-structures-for-survival.html` — **missing**
- `lesson-plans/gr4-ls1-unit1-lesson2-sensing-the-world.html` — **missing**
- `lesson-plans/gr4-ls1-unit1-lesson3-mouths-beaks-teeth-and-getting-food.html` — **missing**
- `lesson-plans/gr4-ls1-unit1-lesson4-movement-structures-and-finding-safety.html` — **missing**
- `lesson-plans/gr4-ls1-unit1-lesson5-structures-for-protection-and-defense.html` — **missing**
- `lesson-plans/gr4-ls1-unit1-lesson6-construct-an-argument-animal-structures.html` — **missing**
- `lesson-plans/gr4-ls1-unit2-lesson1-roots-stems-and-plant-support-systems.html` — **missing**
- `lesson-plans/gr4-ls1-unit2-lesson2-leaves-and-making-food.html` — **missing**
- `lesson-plans/gr4-ls1-unit2-lesson3-water-transport-inside-plants.html` — **missing**
- `lesson-plans/gr4-ls1-unit2-lesson4-flowers-pollination-and-reproduction.html` — **missing**
- `lesson-plans/gr4-ls1-unit2-lesson5-seeds-fruits-and-new-plants.html` — **missing**
- `lesson-plans/gr4-ls1-unit2-lesson6-construct-an-argument-plant-structures.html` — **missing**
- `lesson-plans/free-gr4-apple-oxidation.html` — **missing**
- `lesson-plans/gr5-ps1-lesson1-reactants-products-mixtures.html` — **compliant**
- `lesson-plans/gr5-ess3-unit1-l1-human-impact.html` — **missing**
- `lesson-plans/5th-forces-balanced-unbalanced.html` — **missing**
- `lesson-plans/5th-fossils-earth-history.html` — **missing**
- `lesson-plans/free-gr5-bread-mold-terrarium.html` — **missing**
- `lesson-plans/bird-beak-buffet.html` — **missing**
- `lesson-plans/forces-motion-acceleration.html` — **missing**
- `lesson-plans/ocean-L3-into-the-abyss.html` — **missing**
- `lesson-plans/k-milk-magic.html` — **missing**
- `lesson-plans/ocean-L4-ocean-in-motion.html` — **missing**
- `lesson-plans/ocean-L2-sharks-built-to-hunt.html` — **missing**
- `lesson-plans/ocean-L1-coral-kingdom.html` — **missing**
- `lesson-plans/thermal-energy-ice-cream.html` — **missing**

## Ready-for-next-chunk conclusion

- Canonical pattern is locked.
- The full lesson library in scope has been enumerated.
- A concrete list of non-compliant lesson pages now exists for the implementation pass.
