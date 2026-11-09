# Foundation: Voice of Customer, Awareness, Positioning and the Message Hierarchy

Goal: one message hierarchy, built from customer language, that every ad, page and email draws on. Scale it to the request: a full version for a copy pack or positioning brief, a half-page version for a single email or ad set. If the user already has positioning or a messaging doc, start from it and only fill the gaps.

## Contents
1. Voice-of-customer research
2. Awareness level
3. Market sophistication
4. Jobs to be done
5. Positioning
6. Message hierarchy
7. Validating the value proposition

## 1. Voice-of-customer research

Collect raw customer language before writing anything. Sources, best first:
1. Customer interviews, sales call recordings, enquiry emails and WhatsApp threads the user shares
2. Post-purchase or thank-you page survey answers
3. Support tickets and FAQs
4. Public reviews of the brand and of what the audience already buys instead: TripAdvisor, Booking, Airbnb (hospitality); agent and development reviews, portal comments (real estate); G2, Capterra, Trustpilot, Reddit (SaaS); Amazon and Trustpilot (ecommerce)

Method (Wiebe and Klettke, Consensus):
- Read the descriptive middle (2 to 4 stars) more than the extremes; extremes are short and emotional, the middle explains.
- Copy exact phrases. Paste them into a text file, one review or answer per line, and run `python3 scripts/voc_phrases.py reviews.txt` to surface recurring phrases and candidate sentences.
- Sort phrases into:
  - **Before state:** pains, anxieties, failed alternatives, what they were doing before
  - **Dream state:** outcomes, feelings, what changed
  - **Objections:** what almost stopped them (price, trust, fit, effort, risk, timing)
  - **Decision triggers:** what made them act now
- Keep a "steal sheet" of the 20 to 40 strongest phrases with their source. Headlines and subject lines often come straight from it.

If the user can add a question to their thank-you page or post-booking email, suggest one: "What almost stopped you from booking with us today?" It gives objections from real converters (Wiebe, Single).

## 2. Awareness level (Schwartz)

Diagnose per audience and per traffic source, because the same brand meets readers at different stages.

| Stage | Reader knows | Opening that fits | Typical traffic |
|---|---|---|---|
| Unaware | Not even the problem | Story, identity, a surprising fact; earn attention before any pitch | Cold social, display |
| Problem Aware | The pain, not the solutions | Name the problem in their words, agitate, introduce the solution category | Cold social, informational search |
| Solution Aware | Solutions exist, not this one | Lead with the outcome and why this approach is better than the alternatives | Category search, comparison content |
| Product Aware | This product, not convinced | Proof, objection handling, the offer | Retargeting, branded search, email list |
| Most Aware | Ready, needs a reason now | The offer and the CTA, fast | Branded search, cart and booking abandonment, loyal list |

Rule: the less aware the reader, the more indirect the opening and the longer the copy. The more aware, the faster you reach the offer.

## 3. Market sophistication (Schwartz)

| Stage | Market state | What works |
|---|---|---|
| 1 | First to make the claim | State the claim plainly |
| 2 | Competitors copy the claim | Enlarge it: numbers, proof, specifics |
| 3 | Claims exhausted | Introduce a new mechanism: how it works differently |
| 4 | Mechanisms copied | Make the mechanism bigger, easier, faster or surer |
| 5 | Market believes nothing | Identification and story: who this is for, a world the reader belongs to |

Diagnose by listing the claims competitors already make (from discovery). If everyone says "luxury", "seamless" or "all-in-one", the market is at stage 3 or beyond, and a bare claim headline will not work. Luxury hospitality usually sits at 4 to 5 (identity and specific sensory proof win); SaaS at 3 to 4 (mechanism and category framing); real estate at 3 to 5 depending on the segment.

## 4. Jobs to be done

Write 3 to 5 job statements from VoC: "When [situation], I want to [motivation], so I can [outcome]." Example shape: "When we're planning our first trip without the kids, we want somewhere private and quiet, so we can actually reconnect." Use them to pick angles and to keep copy about the buyer's progress, not the product's features.

## 5. Positioning (Dunford)

Work in this order; each step depends on the one before.
1. **Competitive alternatives:** what best-fit customers would do if this brand didn't exist ("book a beach hotel in Bentota", "use spreadsheets", "rent through a portal", "do nothing").
2. **Unique attributes:** what the brand has that those alternatives lack. Facts only, with `[VERIFY]` where unconfirmed.
3. **Value and proof:** what each attribute enables, in customer terms, with the proof that backs it.
4. **Best-fit customers:** who cares most about that value (characteristics, not demographics alone).
5. **Market category:** the frame that makes the value obvious ("private jungle villa" vs "boutique hotel"; "direct booking engine for small villas" vs "property management software").
6. **Relevant trends** (optional): only if they make the value more urgent and are real.

## 6. Message hierarchy (the output every asset draws on)

```
Primary value proposition (one sentence):
  [Outcome] for [best-fit customer], [unlike/without the competitive alternative].

Pillar 1: [benefit in customer language]
  Attribute: ...   Proof: ...   VoC phrase: "..."
Pillar 2: ...
Pillar 3: ...

Top objections (in the order buyers raise them):
  1. [Objection in their words] → [Answer] → [Proof]
  ...

Proof inventory: numbers, reviews (with source and date), awards (with source), client names, guarantees, policies.
Awareness map: audience × traffic source → stage → opening approach.
Sophistication stage and what it implies for headlines.
Voice: 3 to 5 adjectives turned into rules ("warm: second person, sensory detail, no exclamation marks").
Words to use (from VoC) and words to avoid (competitor clichés, banned claims).
```

Keep claims honest. Every pillar needs proof the brand can show; a pillar without proof becomes a `[VERIFY]` item or gets dropped.

## 7. Validating the value proposition

Test before spending real budget, in order of cost:
1. **5-second or first-click test:** show the hero section briefly, ask what the company does and who it's for. If most people can't say, fix clarity first. (Consensus)
2. **Message test:** for B2B and SaaS, a panel test on Clarity, Relevance, Value, Differentiation and Friction (Wynter's framework, Single [Vendor]); or 5 to 10 interviews with best-fit customers reacting to two or three hierarchy versions.
3. **Angle test with ads:** run 2 or 3 value propositions as ads with identical creative, audience and landing page, and compare CTR as a clarity signal and downstream conversion as the real judge.

Record which version won and why; it becomes the control for every later test.
