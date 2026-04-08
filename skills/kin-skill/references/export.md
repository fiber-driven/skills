# Export — Package Skills for claude.ai

Export skill(s) as `.skill` files (zip archives with folder structure) that can be uploaded directly to claude.ai projects.

## Usage

- `/kin-skill export lights-on-brand-voice` → export one skill
- `/kin-skill export all` → export all LOD skills

## Output Directory

`~/Developer/lights-on/playground/claude-ai-skills/`

## How It Works

A `.skill` file is a zip archive containing the skill's folder structure:

```
skill-name/
  SKILL.md
  references/
    gotchas.md
    ...
```

Claude.ai recognizes this format and imports the full folder structure as a project skill.

## Export Steps

1. Resolve the skill path — check `~/.claude/skill-repos/lightson-digital-skills/skills/{name}/` first, then `~/.claude/skills/{name}/` (follow symlinks to real path)
2. Create the zip archive:
   ```bash
   cd {parent-of-skill-dir}
   zip -r "{output-dir}/{skill-name}.skill" "{skill-name}/" -x "*.DS_Store"
   ```
3. Report: file path, size, contents listing

## Export All

When `all` is specified, export these LOD skills (the ones used on claude.ai):

- lights-on-interview-builder
- lights-on-brand-guidelines
- lights-on-brand-voice
- prompt-optimizer
- lights-on-guest-research
- humanizer

Skip internal-only skills (kin-skill, codex-review, kin-vibe-coding, install-skill) — these use Claude Code features that don't exist on claude.ai.

## Gotchas

- Always export from the repo path, not the symlink — symlinks inside zip files don't work.
- The humanizer skill lives at `~/.claude/skills/humanizer/` (not in the LOD repo). Follow the symlink to the real path before zipping.
- Exclude `.DS_Store`, `.git/`, `README.md`, `WARP.md` and other non-skill files from the zip.
- After exporting, tell the user to upload the `.skill` files to their claude.ai project to replace the current versions.
