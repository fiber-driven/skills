# Gotchas

Accumulated edge cases and failure patterns. Add a line each time something surprising happens.

## Research Phase
- Research on Excel/PMS file formats is unreliable from code exploration alone — always request sample files and read them directly
- For data pipeline projects, schema understanding matters more than code exploration. Spend 80% of research time on the data, not the code.

## Design Phase
- Designs that describe what the system should do without concrete test cases tend to be ambiguous. The Acceptance Criteria section (given/when/then) is required — push for it if the brainstorm output omits it.
- Long design docs (>500 lines) cause downstream drift. If the doc is long, add an explicit "Requirements Summary" section at the top with numbered items the plan can reference.
- The old flow had separate Brainstorm → Spec → Spec Review phases. These were collapsed because brainstorm already produces spec-quality output. If a design feels underspecified, the fix is to deepen the brainstorm — not to bolt on a second formalization pass.

## Review Phases
- Codex reviews tend to be most valuable for research and spec phases. Plan reviews often produce lower-signal findings because the plan is derivative of the spec.
- If the user skips all review phases, note that — the risk accumulates silently.

## Build Phase
- Subagents working in parallel can create merge conflicts if they touch the same files. Check the plan for file overlap before dispatching parallel agents.
- TDD discipline tends to slip on infrastructure/config code (GitHub Actions, Supabase migrations). Remind: even config changes need verification.
- `verification-before-completion` catches ~30% of issues that "all tests pass" misses. Never skip it.

## Documentation Phase
- Users often want to skip this phase. Gently push back — context drift between sessions is the #1 source of wasted time in future conversations.

## Review Phases (Native Codex)
- Native `/codex:review` and `/codex:adversarial-review` return findings to chat only. Always write findings to a file and register in FLOW-STATUS.md — otherwise the review trail is lost on context reset or session end.
- Apply `/receiving-code-review` protocol when processing Codex findings. Without it, the default response is to rubber-stamp everything ("You're absolutely right!") or implement suggestions without verifying they're correct.

## Debugging
- The instinct to "try a quick fix" before investigating is the #1 source of thrash in the build phase. `/systematic-debugging` must trigger at the first failure, not after failed attempts. The skill's contract is explicit: investigate before proposing any fix.

## Complexity Classification
- Quick Fix class still requires a design step (even if 2-3 sentences). Skipping design entirely contradicts the superpowers `brainstorming` baseline and leads to scope creep during build.
- When in doubt about classification, classify higher. Downgrading mid-flow is easy; upgrading after skipping phases is expensive.

## Flow Resumption
- FLOW-STATUS.md can get stale if the user makes changes outside the flow. On resume, always verify the current state of artifacts (do the files exist? have they been modified since last phase?).
- Run entropy checks: compare file mtimes against FLOW-STATUS timestamps, check for orphaned test files, verify CHANGELOG has `[Unreleased]` section.
