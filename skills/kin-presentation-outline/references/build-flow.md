# Build Mode — Question Sequence & Outline Template

## Question Sequence

Ask one question at a time. Wait for the answer before proceeding.

### Question 1: Talk Type
> What type of talk is this?
> - Lecture / workshop (50+ min, teaching audience)
> - Investor pitch (5-15 min, persuading to action)
> - Panel discussion (shared stage, limited control)
> - Virtual / Zoom presentation
> - Lightning talk (5 min or less)
> - Job talk / thesis defense
> - Other (describe)

Load talk-type modifiers from `talk-types.md`.

**For hybrid types** (e.g., "virtual investor pitch"): pick the primary type for structural guidance. Note the secondary as a constraint.

### Teaching Branch (lecture/workshop only)
> Are you teaching (audience learns a new skill or framework) or informing (audience learns about a topic)?

If teaching, weave these into questions 5-7:
- What stories should the audience know?
- What questions should they learn to ask?
- What methods or approaches do you want to demonstrate?

### Question 2: Audience
> Who's your audience? What do they already know, and what do they care about?

### Question 3: Empowerment Promise
> What will the audience know or be able to do after your talk that they can't now? (This becomes your opening line.)

### Question 4: Core Thesis
> What's the ONE thing they must remember if they forget everything else?

### Question 5: Fence / Near Miss
> What will people confuse your idea with? What is it NOT? What's the closest "wrong" version?

### Question 6: Story
> What's the story? Walk me through: problem → what you tried → the insight or turning point → the result.

### Question 7: Surprise
> What's surprising or counterintuitive about this? What will make people say "I didn't know that"?

### Question 8: Tools
> What tools will you have? (board/whiteboard, slides, props, screen share, demo, nothing)

If **slides** selected: note the "one language processor" constraint. The generated outline will flag any section implying text-heavy slides or reading from slides.

### Question 9: Closing
> How do you want to end?
> - Joke (humor that lands better at the end when audience knows you)
> - Salute (compliment the audience/occasion without thanking)
> - Benediction (formal, ceremonial close)
> - Type-appropriate close (e.g., call-to-action for pitches, contributions statement for job talks)

## Compression Rules

If the user provides context upfront (e.g., "15-min Zoom pitch to VCs about our AI product"), skip questions that are already answered.

**Inferable from a one-liner:** talk type, duration, audience, tools (often implied by format).

**Always ask explicitly:** empowerment promise (Q3), core thesis (Q4), fence (Q5), story (Q6), surprise (Q7), closing strategy (Q9).

## Outline Template

After all questions are answered, generate a structured outline in this format:

```markdown
# [Talk Title] — Outline

**Type:** [talk type] | **Duration:** [X min] | **Audience:** [who]

---

## Opening (first 1-2 minutes)

**Empowerment Promise:** [from Q3]
**Roadmap:** [3-5 section preview — verbal punctuation]

---

## Body

### Section 1: [Topic from story/thesis]
**Key point:** [what this section establishes]
**Cycling angle:** [how this presents the core thesis — angle 1]
[If teaching: story/question/method for this section]
**Engagement point:** [calibrated question to ask here, if duration allows]

### Section 2: [Next topic]
**Key point:** [...]
**Cycling angle:** [angle 2 on core thesis]
**Near miss:** [fence point from Q5 — "this is NOT..."]

### Section 3: [Next topic]
**Key point:** [...]
**Cycling angle:** [angle 3 on core thesis, if duration allows]
**Surprise:** [from Q7]

[Add/remove sections based on duration. Lectures get 4-6 sections. Lightning talks get 1-2.]

---

## Closing (final 1-2 minutes)

**Deliver on promise:** [restate what they now know/can do]
**Contributions / Key takeaway:** [1-3 bullet contributions statement]
**End technique:** [from Q9 — the actual joke, salute line, or CTA]

---

## Logistics Checklist (Winston's recommendations)

- [ ] Time slot: 11 AM ideal, avoid post-lunch
- [ ] Room: well-lit, case the venue, match room to crowd size
- [ ] Rules of engagement: phones away, laptops closed (in-person)
- [ ] Slides: no bullets, no reading text aloud, images > text, no laser pointer
- [ ] Props: any physical object that makes the concept tangible?

## Slide/Tool Notes

[If slides selected: specific "one language processor" warnings for sections that imply text-heavy slides]
[If board available: which sections benefit from live drawing/writing]
[If props: where to introduce them for maximum impact]
```

**Cycling depth by duration:**
- Lightning (5 min): 0-1 cycles. One clear through-line.
- Short (10-15 min): 1-2 cycles. Return to thesis once from a different angle.
- Standard (20-30 min): 2-3 cycles. Each body section revisits from a new angle.
- Lecture (45-60+ min): 3-5 cycles. Full cycling with engagement points every ~5 minutes.

## After Generation: Auto-Audit

After generating the outline, immediately run the Audit rubric (from `audit-rubric.md`) with the **cold-reader constraint**:

- Score ONLY what a reader who did NOT participate in the interview would see in the outline text
- Every score requires a quoted phrase from the outline as evidence
- If you cannot find evidence for a dimension, score 2/5 maximum
- Present the outline FIRST, then the scorecard with 2-3 targeted improvement suggestions
- Expect your scores to be 0.5-1.0 points lower than they "feel" — this is the cold-reader correction
