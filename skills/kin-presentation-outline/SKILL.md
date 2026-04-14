---
name: kin-presentation-outline
description: Build or audit presentation outlines using Patrick Winston's "How to Speak" framework. Use when the user says "presentation outline," "help me prepare a talk," "audit my presentation," "score my outline," "build a presentation," or wants to structure a talk. Also triggers on "Winston framework" or "how to speak."
---

# Presentation Outline — Winston's "How to Speak" Framework

Two modes: **Build** (interactive outline creation) and **Audit** (score an existing outline).

## Mode Detection

- **Build:** User wants to create, prepare, or outline a presentation. No existing content provided.
- **Audit:** User provides existing content (pasted text or file path) AND wants it reviewed, scored, or improved.
- **"Improve" / "review" without content** → route to Build (they want to create, not audit).
- **Ambiguous** → ask which mode.

## Build Mode

Read `references/build-flow.md` for the full question sequence and outline template. Read `references/winston-framework.md` for the framework source of truth. Read `references/talk-types.md` for talk-type modifiers.

Flow: ask talk type → teaching branch (if lecture/workshop) → 8 content questions one at a time → generate outline with logistics checklist → auto-audit with cold-reader constraint.

## Audit Mode

Read `references/audit-rubric.md` for the 8 scored dimensions, framework coverage checklist, and scorecard format. Read `references/talk-types.md` for weighting modifiers.

Flow: ingest outline → detect talk type → score 8 dimensions with evidence quotes → framework coverage checklist → present scorecard with top 3 fixes and delivery reminders → offer to fix.

## Key Rules

- One question at a time during Build. Don't batch questions.
- Every audit score requires a quoted evidence phrase from the outline. No quote = max 2/5.
- Auto-audit after Build uses **cold-reader constraint**: score only what's visible in the text, as if you didn't participate in the interview.
- If slides are selected as a tool, enforce the "one language processor" rule — flag any section that implies reading text from slides.

## Gotchas

Read `gotchas.md` for accumulated failure patterns.
