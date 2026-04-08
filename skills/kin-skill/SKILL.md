---
name: kin-skill
description: >
  Manage skills — create, audit, install, update, export, and track usage. Use when the user says "kin-skill,"
  "/kin-skill create," "/kin-skill audit," "/kin-skill install," "/kin-skill update," "/kin-skill export,"
  "/kin-skill usage," "create a skill," "audit this skill," "install skill," "update skill," "export skill,"
  "export for claude.ai," "skill usage," "skill analytics," or any skill management task.
user-invocable: true
argument-hint: "create | audit [skill] | install [url] | update [skill] | export [skill|all] | usage [args]"
---

# Kin Skill — Skill Management Hub

Unified interface for creating, auditing, updating, and tracking skills.

Parse the first argument to determine the subcommand. If no argument, show this menu:

```
/kin-skill create            Create a new skill (wraps /skill-creator + quality audit)
/kin-skill audit [name]      Audit an existing skill against quality principles
/kin-skill install [url]     Install a skill from URL, vet it with skill-vetter
/kin-skill update [name]     Edit, commit, push a skill in the LOD repo
/kin-skill export [name|all] Export skill(s) as .skill files for claude.ai
/kin-skill usage [args]      Show skill usage analytics
```

## Subcommand Routing

| Subcommand | Reference File | What It Does |
|---|---|---|
| `create` | `references/create.md` | Invoke `/skill-creator`, then auto-audit against quality principles |
| `audit` | `references/quality-checklist.md` | Score a skill against the 9 quality principles, suggest fixes |
| `install` | `references/install.md` | Vet with `/skill-vetter` first, then install via `/install-skill` only if LOW risk |
| `update` | `references/update.md` | Edit → commit → push → verify symlink |
| `export` | `references/export.md` | Package skill(s) as .skill zip files for claude.ai upload |
| `usage` | `references/usage.md` | Analyze skill usage log |

Read the matching reference file before proceeding. The quality checklist is also read during `create` (post-creation audit).
