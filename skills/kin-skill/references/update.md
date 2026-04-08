# Update — Edit, Commit, Push

Update a skill in its GitHub repo and keep the local environment in sync.

## Repo Routing

Skills live in two repos based on naming convention:

| Prefix | Repo | Local Path | Remote |
|---|---|---|---|
| `kin-*` | fiber-driven/skills | `~/.claude/skill-repos/fiber-driven-skills/skills/` | `github.com/fiber-driven/skills` |
| `lights-on-*` | lightson-digital/skills | `~/.claude/skill-repos/lightson-digital-skills/skills/` | `github.com/lightson-digital/skills` |
| other (codex-review, ksh-invoice-recon, prompt-optimizer) | lightson-digital/skills | `~/.claude/skill-repos/lightson-digital-skills/skills/` | `github.com/lightson-digital/skills` |

Determine the correct repo from the skill name before any operation.

## Constants

- **Symlinks:** `~/.claude/skills/` (all skills, regardless of repo)
- **Sources:** `~/.claude/skill-sources.json` (sync script config)

## Workflow

Pull latest from remote before making changes. If pull fails (diverged history), stop and tell the user.

Edit files directly in the repo path — never in `~/.claude/skills/`. The repo is the source of truth; symlinks make edits immediately live locally.

After editing: verify the symlink points to the correct repo (not a standalone directory), commit with conventional message `feat({skill-name}): {description}`, and push.

Report: what changed, commit hash, remote status, symlink status.

## Creating a New Skill

1. Determine repo from the skill name prefix
2. Create the directory in the correct repo
3. Write SKILL.md with proper frontmatter
4. Run `bash ~/.claude/scripts/sync-skills.sh` to create the symlink
5. Commit and push

## Sync Check

If the user says "check sync" or "are my skills in sync":

```bash
for repo_dir in fiber-driven-skills lightson-digital-skills; do
  echo "=== $repo_dir ==="
  for skill in $(ls ~/.claude/skill-repos/$repo_dir/skills/ 2>/dev/null); do
    link=~/.claude/skills/$skill
    target=$(readlink "$link" 2>/dev/null)
    if [ -d "$link" ] && [ ! -L "$link" ]; then
      echo "OUT OF SYNC: $skill is a standalone dir, not a symlink"
    elif [ -L "$link" ]; then
      echo "OK: $skill -> $target"
    else
      echo "MISSING: $skill has no symlink"
    fi
  done
done
```

## Gotchas

- Always pull before editing. Editing without pulling creates merge conflicts.
- The symlink check matters — skills occasionally get duplicated as standalone directories (e.g., after reinstalling via `npx skills add`). Remove and recreate the symlink.
- When updating multiple skills in one session, one commit per skill keeps git history useful.
- Reference files in `references/` subdirectories need `git add skills/{name}/` (not just `skills/{name}/SKILL.md`).
- `data/` directories are gitignored — they hold local telemetry/state, not skill definitions.
- Hardlinks break when `git rm` removes files. Always use symlinks via the sync script, never hardlinks.
