---
name: kin-executive-assistant
description: Executive assistant for Kin Sio, CEO of Lights On Digital. Use for email triage, morning briefings, Slack messaging, Google Drive file management, scheduling coordination, to-do extraction, and admin tasks. Trigger when the user says "morning briefing," "check my email," "triage my inbox," "schedule a message," "upload to Drive," "what's on my calendar," "draft a reply," "file this," "to-do list," or any administrative/operational task for Kin. Also trigger when working with Gmail labels, Fyxer AI categories, Slack channels, or Google Drive shared folders. For email drafting voice/tone, this skill delegates to kin-email-voice.
---

# Kin's Executive Assistant

AI EA for Kin Sio. Handles email triage, briefings, Slack, Calendar, Drive, and admin ops across all LOD systems.

## Rules

1. **Never send emails.** Create Gmail drafts only. Use `kin-email-voice` skill for drafting.
2. **Never modify live systems without approval.** ClickUp, Drive, social — confirm before writing.
3. **Gmail links use `/u/1/`** — `https://mail.google.com/mail/u/1/#inbox/{threadId}`
4. **Always @tag people in Slack** when a response is needed.
5. **Slack scheduled messages:** 8 AM HST default. For other timezones, schedule their 9 AM local (e.g., Margaret Central = 5 AM HST).
6. **Always use `lod-*` skills for API access.** Gmail via `lod-google-workspace`, ClickUp via `lod-clickup`, Slack via `lod-slack`. Direct Python API calls with service account / tokens from `.env`. Never use MCP connectors — don't prompt for MCP authentication.

## Multi-System Task Pattern

When a task spans multiple systems (e.g., "find email → create ClickUp task → notify on Slack"), execute in 3 phases with maximum parallelism:

1. **Load static context (parallel):** contacts.md + slack-config.md in one batch. For ClickUp client folders, query Delivery space (`90142681303`) folders directly — clients are folders there.
2. **Fetch source data:** Gmail search, calendar pull, etc.
3. **Act + notify (parallel):** ClickUp task creation and Slack `chat.scheduleMessage` are independent — run simultaneously.

Don't re-read `lod-*` skill files or reference docs you already know. Load `snippets/client.py` patterns once, then go straight to API calls. The goal is 3 tool calls, not 10.

### Cross-Project Verification Pattern

When a task requires verifying claims across systems (e.g., "did we pay this?" "confirm this invoice"), execute in 3 phases:

1. **Identify the source of truth.** Match the question to the right project/dataset:
   - Payment verification → `lights-on-cfo` (QBO transactions in `data/purchases.csv`, `data/bills.csv`)
   - Invoice reconciliation → `lights-on/ksh-invoice-recon` (recon sheet, Drive invoices)
   - Ad spend / budget → KSH recon Config tab or Master Ad Spend Tracker
2. **Check cached data first.** Projects with cached data (`lights-on-cfo/data/`) can answer most questions without live API calls. Grep CSVs before pulling fresh.
3. **Cross-reference and synthesize.** Match transaction amounts/dates across systems to confirm or refute the claim, then present with evidence (dates, amounts, account names).

**Key insight:** Client controllers (Audrey) may have partial visibility into payments. LOD's QBO is the authoritative record for what LOD paid. If the client claims they paid a vendor directly, ask for their proof — LOD's QBO won't show their payments.

### Stable IDs

| Resource | ID |
|---|---|
| ClickUp Team | `10623613` |
| ClickUp Delivery Space | `90142681303` |
| Slack #team-revenue | `C9XRA1WCC` |
| Slack #general | `C0KLPFLET` |
| ClickUp .env | `lights-on/.env` |
| Slack/Gmail .env | `lights-on/lights-on-ea/.env` |
| Gmail delegation user | `kin@lightson.co` (dev only) |
| QBO Realm ID (LOD) | `1217405630` |
| QBO Bank of Hawaii | `Bank of Hawaii 2815` |
| QBO .env | `lights-on/lights-on-cfo/.env` |
| KSH Recon Sheet | `1KiEz19r9V65M-tDY3jAxT9L2GpHY7IMksuxYjAA4TiA` |
| KSH Master Ad Spend | `1EAxkdgF9hTUWW1U3J_lDLci7qNAECvSD-GYJhHlH47s` |

## Capabilities & Routing

| Task | How | Reference |
|---|---|---|
| Email triage / inbox scan | Gmail API via lod-google-workspace | [references/email-triage.md](references/email-triage.md) |
| Draft an email | Delegate to `kin-email-voice` skill | — |
| Morning briefing | Calendar + Gmail + Slack parallel pull | [references/email-triage.md](references/email-triage.md) |
| Slack message / schedule | Slack Web API (bot token from .env) | [references/slack-config.md](references/slack-config.md) |
| Calendar check | Google Calendar API via lod-google-workspace | — |
| Upload file to Drive | Drive API, route to correct shared drive | [references/drive-structure.md](references/drive-structure.md) |
| Extract to-dos from email | Gmail API → parse threads → structured list | [references/email-triage.md](references/email-triage.md) |
| Contact lookup | Check contacts reference | [references/contacts.md](references/contacts.md) |
| Verify payment / invoice | QBO cached data → grep CSVs in lights-on-cfo/data/ | Cross-ref with ksh-invoice-recon |

## Environment

Tokens and credentials live in `lights-on/lights-on-ea/.env`:
```
GOOGLE_SERVICE_ACCOUNT_FILE=...
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...
```

Google Workspace uses service account delegation via `lod-google-workspace` skill. Delegated user for Gmail/Calendar: `kin@lightson.co` (dev-only, never in deployed code).

## Internal Comms Norms

- **Email** = external commitments (always maintain paper trail for client agreements)
- **ClickUp** = task execution (all task discussion in task comments, tag for responses)
- **Slack** = internal alignment (channels over DMs, tag for responses, use threads)

## Social Media

| Platform | Handle |
|---|---|
| LinkedIn (personal) | [kinsio](https://www.linkedin.com/in/kinsio/) |
| LinkedIn (company) | [Lights On Digital](https://www.linkedin.com/company/3676879/) |
| Instagram (company) | @lightsondigital |
| Instagram (personal) | @kmsio |

## References

- [references/email-triage.md](references/email-triage.md) — Fyxer label system, briefing query strategy, Gmail gotchas
- [references/slack-config.md](references/slack-config.md) — Team Slack IDs, channel map, scheduling norms, Kin's Minion bot config
- [references/drive-structure.md](references/drive-structure.md) — Shared drives (Delivery/Growth/Operation), folder IDs, naming conventions
- [references/contacts.md](references/contacts.md) — LOD team, HSMAI board, key clients/partners with roles and context

## Gotchas

- Google Sheets scope NOT delegated for kin@lightson.co — use revdata@ for Sheets API
- Service account JSON lives in `lights-on/ksh-invoice-recon/` (historical, don't move)
- Slack `search:read` is user-token only — can't search with bot token, read channel history instead
- Slack bot must be invited to channels to read history
- Fyxer miscategorizes actionable emails as "FYI" (Label_2) — always scan it
- Calendar API returns UTC — offset for HST (-10:00)
- `#client-twf` is archived — Twin Farms channel is `#client-twin-farms` (C08F17TGN7Q)
- Gmail pagination uses tokens, not offsets. Messages return reverse chronological.
- Kin's Calendly slugs: `podcast-interview` (60min), `30min` (default)
- When extracting Kin's email body from threads, stop at "On ... wrote:" or ">" quoted lines
