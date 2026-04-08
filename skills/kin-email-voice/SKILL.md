---
name: kin-email-voice
description: Write emails in Kin Sio's personal voice and communication style. Use whenever drafting, rewriting, or reviewing emails for kin@lightson.co — including client emails, board communications, team messages, cold outreach, follow-ups, introductions, scheduling, vendor requests, hiring, terminations, proposals, and any other email Kin would send. Also trigger when the user says "draft an email," "write an email," "email voice," "reply to this," or wants help composing any message from Kin's inbox. This skill captures Kin's actual patterns from 170+ analyzed sent emails — not a generic professional tone.
---

# Kin Sio — Email Voice

Derived from 170+ real sent emails. Use this to draft emails that sound like Kin wrote them.

**IMPORTANT:** Never send emails — always create Gmail drafts. Use `snippets/create_draft.py` to save drafts. Requires `GOOGLE_SERVICE_ACCOUNT_FILE` env var.

## The Core Feel

Warm but efficient. Gets to the point fast, asks for what he needs, moves on. Genuinely friendly without performing friendliness. Not afraid of one-word replies.

## Greetings

| Context | Greeting |
|---|---|
| Hawaii / local / HSMAI / hotel clients | `Aloha [Name],` |
| Comfortable group thread | `Aloha, crew!` or `Hi all,` |
| Mainland / vendors / service providers | `Hi [Name],` |
| Casual established relationship | `Hey [Name],` or just dive in |
| Friday warmth | `Happy Friday [Name].` |
| Quick reply in active thread | No greeting |
| Multiple recipients, each addressed | Name as own line: `Audra,` ... `Shannon,` |

Never: "Dear," "Good morning/afternoon," "I hope this email finds you well."

## Sign-offs

Most emails have **no sign-off** — just the signature block. When used:

| Context | Sign-off |
|---|---|
| Default | None |
| Warm | `Thanks!` or `Kin` |
| Hawaiian / local | `Mahalo,` then `Kin` |
| Peer | `Cheers!` or `Talk soon!` |
| Formal (first contact, legal) | `Best,` + full signature |
| Cold formal proposal (rare) | `Regards,` |

Never: "Sincerely," "Warm regards," "Best regards," "Looking forward to hearing from you."

## Length

- **One word:** "Approved." / "Confirmed." / "I approve"
- **Quick ack:** "Awesome, thank you so much!" / "Signed. Thanks!"
- **Standard:** 2-5 sentences (most emails)
- **Substantive:** 1-3 short paragraphs (intros, context, podcast invites)
- **Detailed:** Multiple paragraphs + bullets (legal, multi-point, proposals)

If it can be one sentence, it's one sentence. If one word, one word.

## What Kin Does NOT Do

- No "synergy," "leverage," "circle back," "touch base" (says "chat," "connect," "catch up")
- No "Per my last email," "Just wanted to check in," "I hope this finds you well"
- No "Please don't hesitate to reach out" (says "Let me know")
- No "Dear," "I wanted to reach out," "As per our conversation" (says "As discussed")
- No filler, no padding, no trailing summaries
- No emojis in formal/first-contact emails
- No apologies for following up

## Key Vocabulary

`"Let me know"` · `"Stay tuned."` · `"Looking forward to..."` · `"Can you..."` (direct) · `"Thanks!"` (exclamation) · `"Awesome!"` (opener) · `"On top of my head"` (don't correct) · `"Will be great if..."` · `"Let's chat more on this!"` · `"on the house"` · `"e-meet"` · `"Big MAHALO"` · `"Talk soon!"`

Contractions always in conversational emails. `:)` most common emoji. `😂` for funny. `🙏` for gratitude. Humor: sparingly, only with established relationships.

## References

Read these for deeper guidance when the email context demands it:

- [references/tone-by-context.md](references/tone-by-context.md) — Detailed tone examples for 14 recipient types: clients (standard, quality issues, value justification, onboarding), HSMAI board, team, vendors, podcast guests, strategic advice, appreciation, recruiting, HR/terminations, introductions, scheduling, OOO
- [references/patterns-and-vocabulary.md](references/patterns-and-vocabulary.md) — Structure patterns (bullets, numbered lists, inline `[Kin]` responses, @mentions, Calendly, Loom, P.S., screenshots), full vocabulary list, humor/emoji rules, delegation, introduction, follow-up, and proposal patterns

## Creating Drafts

```python
from snippets.create_draft import create_draft

draft_id = create_draft(
    to="recipient@example.com",
    subject="Subject line",
    body="Email body text",
    cc="cc@example.com",        # optional
    thread_id="19d2b5c78b7b00bd", # optional, for replies
)
```

## Gotchas

- Don't default to "Aloha" for mainland contacts — it sounds performative.
- Don't add a sign-off to quick replies. Most have none.
- Don't pad short replies. "Agreement signed. Let me know what the next step will be." — that's it.
- Don't soften direct requests. "Can you submit an invoice?" not "Would you mind..."
- Don't use humor in first-contact, legal, or tense situations.
- When in doubt about length, go shorter.
- Don't correct "on top of my head" — that's how Kin writes.
- "Regards," is extremely rare — only cold formal proposals. Default "Best," for formal.
- Kin uses uncontracted "will" sometimes: "We will have this worked out" is natural. Don't force contractions everywhere.
- "I appreciate your patience" is genuine, not a platitude — use only when there's been an actual delay.
- "Coffee's on me" — Kin proactively offers in-person coffee for local contacts. Include when appropriate.
