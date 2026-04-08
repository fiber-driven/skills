# Phase Details

Each phase states its intent, the skill to invoke, and its gate (what must be true before advancing).

---

## Phase -1: Classify

**Intent:** Scale the flow to match task complexity. Avoid max ceremony on small changes without losing rigor on complex ones.

**How:** Ask what we're building and assess against three signals:
1. **Scope** — How many modules/files are affected?
2. **Domain familiarity** — Is this a well-understood codebase or new territory?
3. **Stakes** — What breaks if this is wrong?

| Class | Criteria | Active Phases |
|---|---|---|
| **Quick Fix** | Single file, clear bug, obvious solution | 0 (lightweight) → 2 (design: 2-3 sentences) → 6 → 8 → 9 |
| **Standard** | 1-3 modules, understood domain | 0 → 2 → 3 (Design Review) → 4 → 6 → 8 → 9 |
| **Complex** | Multi-module, unfamiliar domain, high stakes | All phases (0–9) |

Design (Phase 2) is always present — what scales is its depth and how many review checkpoints surround it. User can override any classification.

**On resume:** Before continuing a flow, run these entropy checks:
1. Verify all referenced spec files in FLOW-STATUS.md still exist
2. Compare file modification timestamps against last phase transition timestamp
3. Flag any files modified outside the flow since last session
4. Check for orphaned test files or half-implemented modules
5. Verify CHANGELOG.md has an `[Unreleased]` section

Report findings before continuing. If specs have drifted, resolve before advancing.

**Gate:** User confirms complexity class. FLOW-STATUS.md created with class recorded. Telemetry `flow_start` event logged.

---

## Phase 0: Research

**Intent:** Understand what exists before designing anything. Research quality is the ceiling for everything downstream.

**How:** Ask what we're building. Dispatch Explore subagents to map existing code, data sources, schemas, and external constraints. Produce a research summary at `docs/specs/RESEARCH.md`.

**Skill:** None (direct exploration)

**Gate:** User confirms research looks directionally correct.

---

## Phase 1: Research Review

**Intent:** Cross-AI critique of the research before it becomes the foundation for everything downstream. This is the highest-leverage review point.

**Skill (default):** `/codex:adversarial-review` — challenges research assumptions, data sourcing, and completeness. Run with focus text targeting the research doc.

**Skill (fallback):** `/codex-review` file-based handoff, when the user explicitly wants to run the review in VS Code.

**After review completes:** Apply `/receiving-code-review` protocol to process findings. Then:
1. Write findings to `docs/specs/codex-review-research-{YYYYMMDD}.md`
2. Register the artifact path in FLOW-STATUS.md
3. Only then mark phase complete

**When to skip:** Quick Fix or Standard class (per Phase -1). Always offer the option but recommend it for: external data projects, unfamiliar codebases, high-stakes features.

**Gate:** All Critical findings resolved. Research doc updated. Findings artifact written and registered.

---

## Phase 2: Design

**Intent:** Explore approaches, pick a direction, formalize into a buildable design spec. This phase replaces the old Brainstorm → Spec → Spec Review pipeline — one pass, no redundant ceremony.

**Skill:** `/brainstorming` (superpowers skill). Feed the research summary as context.

The brainstorm skill already produces a spec-quality DESIGN.md with architecture, module structure, data flow, and error handling. To close the gap with what a separate spec phase used to add, **require these three sections in the output DESIGN.md:**

1. **Non-Goals** — Explicit list of what's out of scope and why. Prevents scope creep during build. (Can be labeled "Future" or "Out of Scope" if that fits the doc better.)
2. **Acceptance Criteria** — Given/When/Then examples for key behaviors. These feed directly into TDD during the build phase. Push for concrete "given X input, expect Y output" examples.
3. **Open Questions** — Unresolved items tagged with who should answer them. All blocking questions must be resolved before advancing.

**Frontend projects:** After design direction is approved:
- If no design context exists, run `/teach-impeccable` first
- Build a high-fidelity mockup using Impeccable skills (`/critique`, `/arrange`, `/typeset`, `/colorize`, `/polish`)
- Iterate with user — use `/bolder` or `/quieter` to dial intensity, `/distill` to simplify

**Gate:** User approves DESIGN.md. All blocking Open Questions resolved. Non-Goals and Acceptance Criteria sections present.

---

## Phase 3: Design Review

**Intent:** Cross-AI critique of the design before investing in implementation planning. The design is the highest-leverage artifact after research — errors here multiply into hundreds of bad lines.

**Skill (default):** `/codex:adversarial-review` — challenges design choices, tradeoffs, and assumptions. Run with focus text targeting DESIGN.md.

**Skill (fallback):** `/codex-review` file-based handoff, when the user explicitly wants to run the review in VS Code.

**After review completes:** Apply `/receiving-code-review` protocol to process findings. Then:
1. Write findings to `docs/specs/codex-review-design-{YYYYMMDD}.md`
2. Register the artifact path in FLOW-STATUS.md
3. Only then mark phase complete

**When to skip:** Quick Fix class (per Phase -1). Always offer the option but recommend it for: complex architectures, multi-system integrations, unfamiliar domains.

**Gate:** All Critical findings resolved. DESIGN.md updated. Findings artifact written and registered.

---

## Phase 4: Plan

**Intent:** Convert the reviewed design into a granular, TDD-based implementation plan.

**Skill:** `/writing-plans` (superpowers skill). Feed the DESIGN.md (updated after Phase 3 review).

**Gate:** User reviews the plan. Plan reviewed by subagent reviewer.

---

## Phase 5: Plan Review

**Intent:** Cross-AI critique of the plan against the design before building.

**Skill (default):** `/codex:review` — standard review (plans are derivative of specs, so lighter review fits). Run targeting the plan file.

**Skill (fallback):** `/codex-review` file-based handoff, when the user explicitly wants to run the review in VS Code.

**After review completes:** Apply `/receiving-code-review` protocol to process findings. Then:
1. Write findings to `docs/specs/codex-review-plan-{YYYYMMDD}.md`
2. Register the artifact path in FLOW-STATUS.md
3. Only then mark phase complete

**When to skip:** Quick Fix or Standard class (per Phase -1). Plan reviews tend to produce lower-signal findings because the plan is derivative of the spec (see gotchas).

**Gate:** All Critical findings resolved. Plan updated. Findings artifact written and registered.

---

## Phase 6: Build

**Intent:** Execute the plan with subagents and TDD discipline.

**Skills (in order of preference):**
1. Suggest `/using-git-worktrees` for workspace isolation
2. `/subagent-driven-development` — one fresh subagent per task, each follows TDD
3. `/dispatching-parallel-agents` for independent tasks
4. Fall back to `/executing-plans` if subagents aren't practical

**Build state management:** On Phase 6 entry, create the build state file:
```bash
echo '{"phase":"build","test_failed":false,"debug_invoked":false,"fix_attempts":0}' > /tmp/vibe-build-state.json
```
On Phase 6 exit, remove it: `rm -f /tmp/vibe-build-state.json`. Update state on test failures, debug invocations, and fix attempts (see `references/build-hooks.md` for transitions).

**On any test failure or unexpected behavior:** Set `test_failed: true` in build state, then invoke `/systematic-debugging` immediately, before proposing any fix. Set `debug_invoked: true` after invoking. Root cause first, always. Do not attempt speculative fixes — the debugging skill's contract requires investigation before action.

**After 3 failed fix attempts on the same issue:** Stop and ask the user. Do not keep retrying. The build-guard hook will also remind about this.

**Scope discipline:** Implement DESIGN.md as specified. If you notice something missing or improvable, add it to Open Questions in the design doc — do not fix it inline during build.

**Frontend projects (after implementation):**
- `/polish` for alignment, spacing, consistency
- `/audit` for a11y, performance, theming, responsive
- `/web-design-guidelines` for semantic HTML, keyboard nav, contrast
- Fix all Critical and Important findings

**Before any "done" claim:** `/verification-before-completion`

**Gate:** All tasks complete. All tests pass. Frontend a11y audit passed (if applicable). Verification command run fresh with passing output.

---

## Phase 7: Simplify (Optional)

**Intent:** Review the full project for code reuse, quality, and efficiency before documentation locks things in.

**Skill:** `/simplify`

**After simplify:** Re-run full test suite and `/verification-before-completion`.

**Gate:** All tests still pass after changes.

---

## Phase 8: Documentation

**Intent:** Ensure all project docs accurately represent the current state.

**What to update:**
- `README.md` — project overview, setup, usage, architecture
- `CLAUDE.md` — project-level instructions for future AI sessions
- `CHANGELOG.md` — entry under `[Unreleased]` (Keep a Changelog format)
- Local specs — mark as implemented, note deviations
- ADRs in `docs/adr/` for significant technical decisions
- Archive superseded docs to `docs/archive/`
- Clean up folder structure, flag `.gitignore` candidates

**Hard gate:** README.md, CLAUDE.md, and CHANGELOG.md must be updated in the same commit as code changes. Do not advance to Phase 9 without this. This is non-negotiable — context drift between sessions is the #1 source of wasted time.

**Gate:** User confirms docs are complete and reflect current state. Doc updates committed alongside code.

---

## Phase 9: Finish

**Intent:** Integrate the work and clean up.

**Skill:** `/finishing-a-development-branch` — presents options: merge locally, create PR, keep as-is, discard. Handles worktree cleanup.

**Checklist:**
- README.md is on the default branch (visible on the GitHub repo page). If the PR hasn't been merged yet and the repo page is blank, either merge or push the README to main separately.
- CHANGELOG.md has an `[Unreleased]` entry covering all changes.
- FLOW-STATUS.md is updated with Phase 9 complete.

**Gate:** Work integrated or explicitly parked. Repo README visible on GitHub. Flow status marked finished. Telemetry `flow_end` event logged with outcome and phase counts.
