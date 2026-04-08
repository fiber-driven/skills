# Usage — Skill Analytics

Analyze the skill usage log at `~/.claude/logs/skill-usage.jsonl` and present a summary.

## Default View (no args)

Show a complete overview:
- **Total invocations** and date range covered
- **Frequency table**: skill name, count, last used — sorted by count descending
- **Recent activity**: last 10 invocations with timestamp, skill, and context (truncated)
- **Per-project breakdown**: group by working directory to show which skills are used where

## With Args

The user can pass arguments to filter:
- A skill name (e.g., `/kin-skill usage frontend-design`) → show all invocations with full context
- `recent` or `recent N` → show last N entries (default 20)
- `projects` → show per-project breakdown only
- A date like `2026-03` → filter to that month

## Formatting

- Use markdown tables for frequency data
- Keep context strings trimmed to ~80 chars in tables
- Show timestamps in local-friendly format (date + time, no seconds)

## If No Data

If `~/.claude/logs/skill-usage.jsonl` doesn't exist or is empty, tell the user no skill usage has been logged yet.
