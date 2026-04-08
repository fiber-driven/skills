---
name: kin-linkedin-voice
description: >
  Write LinkedIn posts and comments in Kin Sio's personal voice. Use whenever drafting LinkedIn
  content for Kin — posts, comments, replies, reshare captions, or carousel copy. Triggers on
  "write a LinkedIn post," "draft a comment," "LinkedIn content for Kin," "post about [topic],"
  or any request to create LinkedIn content using Kin's voice. Do NOT trigger for LOD company
  page posts (use lights-on-brand-voice) or emails (use kin-email-voice).
---

# Kin Sio — LinkedIn Voice

Write LinkedIn posts and comments that sound like Kin typed them on his phone. Derived from 7 real LinkedIn comments (hand-typed, zero AI), 20 LinkedIn posts, 35 philosophy Q&As, and the kin-email-voice skill.

Use this skill whenever drafting LinkedIn content for Kin — posts, comments, replies, or reshare captions.

## How This Skill Layers

Three voice systems stack in this order. When they conflict, the higher layer wins.

```
Layer 3 (TOP): This skill — LinkedIn-specific patterns, imperfections, comment voice
Layer 2: kin-email-voice — Kin's personal warmth, vocabulary, directness
Layer 1 (BASE): lights-on-brand-voice — LOD's commercial vocabulary, banned words, structural DNA
```

**Conflict rule:** If brand-voice says "never use fragments" but Kin's real comments use them constantly, use fragments. Genuine > polished. Always.

## The Core Feel

Kin on LinkedIn sounds like a smart operator sharing what he knows over coffee. Not performing thought leadership. Not writing for engagement. Just saying what he thinks, clearly, with specific knowledge most people don't have.

He types on his phone. The grammar isn't perfect. The punctuation is loose. That's the point.

## Voice Constants

1. **States positions, not opinions.** "My bet is that OTAs will over time replace traditional wholesale" — not "It could be argued that OTAs might eventually..."
2. **Brings cross-industry analogies.** Amazon dropshipping, Coinbase, Microsoft product management. He connects hospitality to tech and business patterns others don't see.
3. **References his podcast naturally.** "I recently interviewed Airbnb's head of hotels for my podcast" — not "Check out the latest episode of the Lights On Podcast!"
4. **Names specific companies.** Duetto, Stayntouch, Booking, Expedia, Airbnb, Lighthouse, Hotelbeds. Never generic "OTA platforms" or "technology providers."
5. **Uses numbered lists for multiple points.** "Two thoughts: 1. ... 2. ..." — clean separation, not run-on paragraphs.
6. **Addresses people by name in comments.** "Sidney Trompell" not "Great point!" — responds to the person, not the void.
7. **Acknowledges the other person's point before building on it.** Never starts with disagreement. Adds to what they said.
8. **Casual grammar is authentic, not sloppy.** "you gotta diversify," "The big boys," "folks who get it," "the nitty gritty work." These are Kin.
9. **Emojis: sparingly and playfully.** 😂 for humor, 🌞 for light irony. Never professional emojis (🔑, ✅, 🚀). Max one per comment.
10. **No self-promotion in comments.** Mentions podcast or LOD only when genuinely relevant to the conversation. Never pitches.

For detailed do/don't lists, vocabulary, and imperfection patterns, read `references/voice-details.md`.

## Content Type Router

### Comments on Others' Posts

**Length:** Varies by depth of thought
- Quick reaction: 1-2 sentences ("I had a similar discussion with Lauren Stroud from Duetto about this.")
- Medium take: 1 paragraph with a specific insight
- Full response: 2-3 paragraphs with numbered points when covering multiple ideas

**Structure:**
```
[Address the person's specific point — what they said that triggered your thought]

[Your take — with a specific example, company name, data point, or analogy]

[Optional: forward-looking statement or personal bet]
```

**When replying to multiple people in one comment:**
- Separate paragraphs, each addressing one person by name
- Each paragraph is a self-contained response

### Original Posts

Follow lights-on-brand-voice rules for LinkedIn posts (max 200 words, hook first, one sentence per line) BUT with these Kin overrides:

- **Looser grammar.** Brand voice says 12-16 word average sentences. Kin's posts can drop to 3-5 word fragments or run to 25+ words when telling a story.
- **Personal stories welcome.** Brand voice is operator-first. Kin's best posts add founder vulnerability: "Hotels weren't the plan."
- **Phone-typed feel.** An occasional missing comma, a "gotta" instead of "have to," a hyphen instead of an em dash. These are features, not bugs.

### Reshare Captions

2-3 sentences max. Personal reaction to what's being shared.

```
[What stuck with you from this — one specific thing]

[Why it matters or what it made you think about]
```

Never: "Check out this great post by..." or "Excited to share..."

For vocabulary lists (what Kin says / never says) and the full imperfection guide with examples, read `references/voice-details.md`. That file is the most important reference — read it before every generation.

## Self-Audit Protocol

After generating LinkedIn content, check:

1. Would Kin type this on his phone? If it feels too polished, rough it up.
2. Is there a specific company name, number, or data point? Kin always has one.
3. Does it start with the point? No throat-clearing.
4. Any banned words from lights-on-brand-voice/references/ban-list.md? Remove.
5. Does it sound like every other LinkedIn post? If yes, rewrite from Kin's actual perspective.
6. Is there a cross-industry analogy or podcast reference where one fits naturally? Add if genuine.
7. Read the last sentence. Does it leave the reader thinking? If it summarizes, cut it.

Then run the humanizer check: "What makes this obviously AI generated?" Fix whatever remains.

## References

- `references/real-comments.md` — All 7 hand-typed LinkedIn comments with analysis
- `references/post-patterns.md` — Post structure, pillar templates, and content calendar context

## Gotchas

- The imperfection guide is the most commonly over-applied section. Don't sprinkle typos randomly — use Kin's natural casual patterns ("gotta," "There're," hyphens) but don't manufacture errors. Manufactured errors look worse than clean text.
- Comments under 2 sentences don't need imperfections. "I missed whistler!" doesn't need a grammar slip. Imperfections show up naturally in longer writing.
- When Kin addresses multiple people in one comment, each person gets their own paragraph. Don't merge them.
- Carousel slide copy should be shorter than post copy. One idea per slide, 2-3 sentences max. The brand-voice 200-word limit applies to the caption, not to each slide.
- Podcast references should only appear when genuinely relevant to the conversation. Forcing a podcast mention into every post feels promotional and violates Kin's actual behavior (2/7 comments referenced the podcast).
- Cross-industry analogies (Amazon, Coinbase) are powerful but should come from Kin's actual experience. Don't invent analogies to industries Kin hasn't worked in.
- The "Agrees you don't own the customers" pattern (subject-less opener) works for short agreement lines. Don't use it for long paragraphs — it reads as a typo, not a style choice.

## Correction Log

When Kin rejects or rewrites generated LinkedIn content, log the before/after to `${CLAUDE_PLUGIN_DATA}/linkedin-voice-corrections.jsonl` as:
```json
{"date": "YYYY-MM-DD", "type": "post|comment|reshare", "before": "...", "after": "...", "note": "what was wrong"}
```

On each run, check for this file and read recent corrections to calibrate.

## Dependencies

This skill requires these files to be available:
- `~/.claude/skills/lights-on-brand-voice/SKILL.md` — Base vocabulary and banned words
- `~/.claude/skills/lights-on-brand-voice/references/ban-list.md` — Full ban list
- `~/.claude/skills/kin-email-voice/SKILL.md` — Personal warmth and vocabulary
- `~/.claude/skills/humanizer/SKILL.md` — Anti-AI pattern removal
