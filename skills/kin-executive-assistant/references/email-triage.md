# Email Triage — Fyxer AI Label System

kin@lightson.co uses Fyxer AI to auto-categorize every email. Nothing stays in raw inbox.

## Fyxer Labels (numbered by priority, not label ID)

| Label | Gmail ID | Purpose | Briefing Priority |
|---|---|---|---|
| **1: to respond** | Label_1 | Emails requiring Kin's direct reply — questions, requests, proposals | **HIGH** — always surface |
| **2: FYI** | Label_2 | Important threads Kin should know about — partner updates, team threads, vendor status. **Often contains actionable items.** | **HIGH** — scan for hidden actions |
| **3: comment** | Label_8 | Google Docs comments, ClickUp comments, collaborative doc @mentions | MEDIUM — scan for @mentions |
| **4: notification** | Label_7 | System notifications — Ignition proposal acceptances, DocuSign completions, ClickUp tasks, Rise25 podcast status. **Business-critical events land here.** | **HIGH** — filter for business events |
| **5: meeting update** | Label_6 | Calendar invites, meeting changes | LOW — calendar handles this |
| **6: awaiting reply** | Label_5 | Threads where Kin sent last message — waiting on others | MEDIUM — check for stale (>3 days) |
| **7: actioned** | Label_4 | Already handled — Kin's sent replies and thread context | SKIP |
| **8: marketing** | Label_3 | Newsletters, promos, vendor spam (5,900+ unread) | SKIP |

## Morning Briefing Query Strategy

1. **Label_1 (to respond)** — ALL unread. Action items.
2. **Label_2 (FYI)** — Unread, scan for items that actually need action
3. **Label_7 (notification)** — Unread, filter for business events (proposal accepted, document signed, episode published). Skip ClickUp noise.
4. **Label_5 (awaiting reply)** — Threads older than 3 days (stale follow-ups)
5. **Skip:** Label_3 (marketing), Label_4 (actioned), Label_6 (meeting update)

## Additional Gmail Labels (non-Fyxer)

Topic routing labels (not priority): `Revenue`, `Creative`, `Reports`, `Sales`, `Billing`, `Facebook Ads`, `Web`

## Gmail API Notes

- Always include thread links: `https://mail.google.com/mail/u/1/#inbox/{threadId}`
- Group output by actionability, not chronology
- Pagination uses `nextPageToken`, not offsets
- Messages return reverse chronological
- To extract Kin's email body, stop at "On ... wrote:" or ">" quoted lines
- Use `format="metadata"` with `metadataHeaders` for triage (faster than `format="full"`)
- Use `format="full"` only when you need the body text
