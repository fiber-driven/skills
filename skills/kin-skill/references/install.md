# Install Subcommand

Vet a skill for security first, then install only if it passes.

## Workflow

1. **Parse the URL** — supports GitHub URLs, ClawHub URLs, `owner/repo@skill` shorthand, or `owner/repo` (all skills)
2. **Fetch the skill content without installing** — clone to a temp location or fetch the SKILL.md content, but do NOT symlink into `~/.claude/skills/` yet
   - **GitHub URL:** shallow clone to `/tmp/{owner}-{repo}`, locate the SKILL.md
   - **ClawHub / other URL:** fetch the page content to extract the SKILL.md
3. **Invoke `/skill-vetter`** on the fetched skill files to produce a vetting report
4. **Act on the verdict:**
   - **LOW risk** → proceed with full installation (register in skill-sources.json, symlink, etc.)
   - **MEDIUM risk or higher** → show the vetting report, do NOT install, ask the user to explicitly confirm before proceeding
   - **DO NOT INSTALL** → clean up temp files, warn the user

## Fetching Without Installing

For GitHub repos, clone to temp:
```bash
git clone --depth 1 https://github.com/{owner}/{repo}.git /tmp/{owner}-{repo}
```

Then read all files in the skill directory for vetting. Only after the user approves (or risk is LOW) do you run the actual `/install-skill` flow to register and symlink.

## Cleanup (if vetting fails or user declines)

```bash
# Remove temp clone
rm -rf /tmp/{owner}-{repo}
```

## Non-GitHub URLs (e.g., ClawHub)

If the URL is not a GitHub URL:
1. Fetch the page content to find the SKILL.md
2. Write to a temp location (`/tmp/{skill-name}/SKILL.md`) for vetting
3. Only create the real skill directory at `~/.claude/skills/{skill-name}/` after vetting passes
