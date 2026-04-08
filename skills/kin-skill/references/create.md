# Create — New Skill Workflow

Two phases: create the skill, then audit it.

## Phase 1 — Create

Invoke `/skill-creator` to handle the actual skill creation. It covers: intent capture,
SKILL.md drafting, test case creation, evaluation, and iteration.

Let skill-creator do its job fully. Don't interfere with its workflow.

## Phase 2 — Quality Audit (automatic)

After skill-creator finishes and the SKILL.md exists, immediately run the quality audit.

Read `references/quality-checklist.md` and score the new skill against all 9 principles.

**For a brand-new skill, these are the most common failures:**
- Missing gotchas section (seed 2-3 from known failure modes)
- SKILL.md too long (split into hub + references)
- Railroading (numbered steps for things Claude already knows)
- No trigger phrases in description

**After scoring:** Present the scorecard. For each failing principle, make the fix directly —
don't just report it. Then show the user what changed.

## Phase 3 — Repo Integration

After the quality audit passes, integrate into the lightson-digital-skills repo:

1. Move the skill into `~/.claude/skill-repos/lightson-digital-skills/skills/{skill-name}/`
2. Create symlink from `~/.claude/skills/{skill-name}`
3. Commit and push (use the update subcommand's workflow)

If the user wants the skill to stay local (not in the repo), skip this phase.

## Platform Compatibility

Skills should work on both Claude Code and claude.ai. During the audit, check for
platform-specific instructions (e.g., "launch 3 Agent subagents") and flag them.
Intent-based instructions ("research with maximum depth and parallelism") work everywhere.
