---
name: kin-vibe-coding
description: Orchestrate the full vibe coding workflow — from research through spec, review, plan, review, and TDD-driven implementation. Use when starting a new feature, project, or significant piece of work. Also trigger when the user says "vibe code", "start the flow", "new feature", "let's build", or wants to resume an in-progress flow. This skill is a wrapper — it stays decoupled from underlying skills and calls them at the right phase.
---

# Kin's Vibe Coding Flow — Orchestrator

You conduct a multi-phase development workflow. Invoke the right skill at each phase, enforce gates, and maintain visible progress. You are the conductor, not the orchestra.

**Read before starting:**
- `references/phase-details.md` — Intent, skills, and gates for each phase
- `references/gotchas.md` — Accumulated edge cases and failure patterns
- `references/telemetry.md` — Flow telemetry schema (log on phase transitions)
- `references/build-hooks.md` — Phase 6 mechanical enforcement (read on first use to check hook is registered)

## Phase Map

Display at the top of EVERY response. Update markers as phases complete.

```
VIBE CODING FLOW
================
[ ] Phase -1: Classify
[ ] Phase 0: Research
[ ] Phase 1: Research Review
[ ] Phase 2: Design
[ ] Phase 3: Design Review
[ ] Phase 4: Plan
[ ] Phase 5: Plan Review
[ ] Phase 6: Build
[ ] Phase 7: Simplify (optional)
[ ] Phase 8: Documentation
[ ] Phase 9: Finish

Legend: [x] done  [~] active  [ ] pending  [!] blocked  [—] skipped
```

After Phase -1 classification, grey out skipped phases in the map based on complexity class:
- **Quick Fix:** Show phases 0, 2, 6, 8, 9 only
- **Standard:** Show phases 0–2, 3, 4, 6, 8, 9 (compress reviews to Design Review only)
- **Complex:** Show all phases

## Flow State

Persist state in `docs/specs/FLOW-STATUS.md` so flows survive across conversations. On first invocation, create it with the feature name, date, complexity class, phase log table, and artifact paths. Update on every phase transition.

On resume: read FLOW-STATUS.md, run entropy checks (see Phase -1 resume rules in phase-details.md), display the phase map, summarize position, and continue.

## Telemetry

Log flow events to `~/.claude/skills/kin-vibe-coding/data/flow-history.jsonl`. See `references/telemetry.md` for schema. Log at: flow start, each phase transition, review findings, and flow end.

## Build Phase Hooks

Phase 6 uses a state file (`/tmp/vibe-build-state.json`) to track debug discipline. The orchestrator creates it on Phase 6 entry and deletes it on exit. A PreToolUse hook on Edit/Write reads it to remind about debug-before-fix and 3-attempts rules. See `references/build-hooks.md` for setup.

## Core Rules

- **Specs are the real source code.** Treat them as first-class, version-controlled artifacts.
- **Design is always present.** The superpowers `brainstorming` skill hard-gates every task through design/approval. Complexity scaling adjusts design *depth* (2-3 sentences vs. full DESIGN.md), never removes it.
- **Review at the highest leverage point.** Research errors → thousands of bad lines. Spec errors → hundreds. Code errors → just code errors.
- **Debug before fixing.** On any test failure or unexpected behavior in Phase 6, invoke `/systematic-debugging` before proposing a fix. Root cause first, always.
- **Review artifacts are durable.** Every review phase must produce a findings file in `docs/specs/` and register it in FLOW-STATUS.md. Chat-only findings are not acceptable.
- **Phase gates are non-negotiable.** Each phase has explicit completion criteria in the phase details. Don't advance without them.
- **Users can skip phases.** Mark skipped phases `[—]`, note what context might be missing, and proceed.
- **Users can jump to a phase** if prior phases are complete. Verify, then start.
