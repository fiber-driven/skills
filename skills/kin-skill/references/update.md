# Update — Edit, Commit, Push

Update a skill in the `lightson-digital-skills` GitHub repo and keep the local environment in sync.

## Constants

- **Repo:** `~/.claude/skill-repos/lightson-digital-skills`
- **Skills dir:** `~/.claude/skill-repos/lightson-digital-skills/skills/`
- **Symlinks:** `~/.claude/skills/`
- **Remote:** `github.com/lightson-digital/skills`

## Workflow

Pull latest from remote before making changes. If pull fails (diverged history), stop and tell the user.

Edit files directly in the repo path — never in `~/.claude/skills/`. The repo is the source of truth; symlinks make edits immediately live locally.

After editing: verify the symlink points to the repo (not a standalone directory), commit with conventional message `feat({skill-name}): {description}`, and push.

Report: what changed, commit hash, remote status, symlink status.

## Creating a New Skill

Create the directory in the repo, write SKILL.md with proper frontmatter, create the symlink, commit and push.

## Sync Check

If the user says "check sync" or "are my skills in sync":

```bash
for skill in $(ls ~/.claude/skill-repos/lightson-digital-skills/skills/); do
  link=~/.claude/skills/$skill
  if [ -d "$link" ] && [ ! -L "$link" ]; then
    echo "OUT OF SYNC: $skill is a standalone dir, not a symlink"
  elif [ -L "$link" ]; then
    echo "OK: $skill"
  else
    echo "MISSING: $skill has no symlink"
  fi
done
```

## Gotchas

- Always pull before editing. Editing without pulling creates merge conflicts.
- The symlink check matters — skills occasionally get duplicated as standalone directories (e.g., after reinstalling via `npx skills add`). Remove and recreate the symlink.
- When updating multiple skills in one session, one commit per skill keeps git history useful.
- Reference files in `references/` subdirectories need `git add skills/{name}/` (not just `skills/{name}/SKILL.md`).
