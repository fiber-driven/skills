# Skill Quality Checklist

9 principles distilled from Anthropic's "Lessons from Building Claude Code: How We Use Skills."
Score each principle Pass/Fail/NA. A quality skill passes at least 7 of the applicable principles.

---

## 1. Skip the Obvious

Claude already knows how to git commit, run tests, read files. The skill should focus on
what's non-obvious — domain-specific knowledge, project conventions, gotchas, and judgment calls.

**Audit:** Scan for instructions that restate default Claude behavior (e.g., "run `git add`",
"use `ls` to list files"). Flag each one. If >30% of the skill is obvious instructions, fail.

---

## 2. Build a Gotchas Section

The highest-signal content in any skill. Gotchas accumulate over time as the skill encounters
edge cases. A new skill should seed 2-3 gotchas from known failure modes. A mature skill
should have 5-10+.

**Audit:** Does the skill have a `## Gotchas` section? Does it contain specific, actionable
items (not generic advice)? Score: present with 3+ items = pass, present but thin = partial,
missing = fail.

---

## 3. Progressive Disclosure

A skill is a folder, not a file. The SKILL.md hub should be short (~30-80 lines) and dispatch
to reference files for details. Claude loads SKILL.md every time the skill triggers — everything
in the hub consumes context on every invocation.

**Audit:** Check SKILL.md line count. Over 150 lines = likely fail. Check for `references/`
subdirectory. Is detail pushed to reference files that are read on-demand? Hub should contain
intent and routing, not implementation details.

| Lines | Verdict |
|-------|---------|
| <80 | Good hub size |
| 80-150 | Acceptable if no natural splits |
| 150+ | Needs progressive disclosure |

---

## 4. Don't Railroad

State intent and constraints, not step-by-step commands. The article's example:

**Too prescriptive:** "Step 1: Run git log. Step 2: Run git cherry-pick. Step 3: If conflicts..."

**Better:** "Cherry-pick the commit onto a clean branch. Resolve conflicts preserving intent."

**Audit:** Count numbered step-by-step sequences. If the skill has >2 multi-step command
sequences where Claude already knows the mechanics, flag as railroading. Steps are fine for
genuinely non-obvious workflows (like the skill-sources.json schema).

---

## 5. Description = Trigger

The description field is for the model, not the user. It should include natural language
phrases that users actually say, not just a technical summary.

**Audit:** Does the description include trigger phrases? ("Use when the user says X, Y, Z.")
Does it mention what NOT to trigger on? (Helps avoid false positives.) Is it under 300 chars
for scanning efficiency?

---

## 6. Think Through Setup

For skills that need configuration (API keys, channel names, preferences), cache first-run
answers using `${CLAUDE_SKILL_DIR}/config.json`. The skill should check for config on load
and only ask setup questions when NOT_CONFIGURED.

**Audit:** Does this skill need per-user or per-project configuration? If yes, does it use
`${CLAUDE_SKILL_DIR}/config.json` (or equivalent) to cache answers? If the skill asks setup
questions every time it runs, fail.

---

## 7. Store Data

For skills that produce or consume persistent state across sessions, use
`${CLAUDE_PLUGIN_DATA}` for logs, correction histories, or accumulated knowledge.

**Audit:** Does this skill benefit from remembering things across sessions? (Correction logs,
past outputs, usage patterns.) If yes, does it use `${CLAUDE_PLUGIN_DATA}`? If the skill
would clearly benefit from persistence but doesn't implement it, flag as an opportunity.

---

## 8. Give It Code

Store reusable scripts, helper functions, or code snippets in the skill folder. Claude
composes from these rather than reconstructing from prose descriptions every time.

**Audit:** Does this skill involve generating or working with code? If yes, are there stored
code snippets, templates, or helper functions in the skill folder? The article's example:
`lib/signups.py` with gotcha-laden docstrings that Claude imports and uses.

---

## 9. On-Demand Hooks

For skills that need session-scoped guardrails (e.g., "warn me before pushing to main"),
create hooks that activate when the skill runs and deactivate when the session ends.

**Audit:** Does this skill have behaviors that should persist for the rest of a session?
("Always check X before Y during this workflow.") If yes, does it set up hooks? Most skills
don't need this — score NA if not applicable.

---

## Scoring

After auditing all 9 principles, produce a scorecard:

```
Skill: {name}
Lines: {SKILL.md line count} | References: {count} | Gotchas: {count}

| # | Principle              | Score | Notes |
|---|------------------------|-------|-------|
| 1 | Skip the obvious       | ✓/✗/— |       |
| 2 | Gotchas section         | ✓/✗/— |       |
| 3 | Progressive disclosure  | ✓/✗/— |       |
| 4 | Don't railroad          | ✓/✗/— |       |
| 5 | Description = trigger   | ✓/✗/— |       |
| 6 | Think through setup     | ✓/✗/— |       |
| 7 | Store data              | ✓/✗/— |       |
| 8 | Give it code            | ✓/✗/— |       |
| 9 | On-demand hooks         | ✓/✗/— |       |

Pass: {n}/9 applicable | Verdict: {PASS/NEEDS WORK}
```

For each failing principle, include a specific recommendation with what to change and where.
