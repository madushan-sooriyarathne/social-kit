# Ad Copy Variations

Goal: a structured variation set that finds the winning angle first, then improves hooks and formats within it, with every variant tied to a hypothesis and a matching landing page.

## Contents
1. Angles
2. Hooks
3. Frameworks by awareness level
4. Headline principles
5. Structuring the variation matrix
6. Channel notes
7. Sizing and judging the test
8. Message match handoff
9. Output

## 1. Angles (test these first)

An angle is the core reason to buy. Pull 3 to 5 from the message hierarchy that are genuinely different, not synonyms of one idea. Angle types:

| Angle type | Built from | Example shape (villa) |
|---|---|---|
| Pain | Before-state VoC | "Tired of resorts where you never get a quiet pool?" |
| Desire or outcome | Dream-state VoC | Waking to birdsong with the whole pool to yourselves |
| Mechanism | Unique attribute | Only six guests at a time, so the staff know your name |
| Identity | Best-fit customer traits | For couples who'd rather read by a pool than queue for a buffet |
| Proof | Proof inventory | What 200 guests say about breakfast on the terrace `[VERIFY]` |
| Offer | Real incentive or deadline | Book direct for free airport transfer `[VERIFY]` |
| Objection flip | Top objection | "Far from the beach" reframed as "five minutes from the beach, a world from the crowds" `[VERIFY distance]` |

Match angles to awareness: pain and identity for cold audiences, mechanism and proof for solution and product aware, offer and objection flips for retargeting and most aware.

## 2. Hooks

The hook is the first line, first second of video or the headline that stops the scroll. Write 2 or 3 per winning angle:
- A question in the reader's words
- A specific number or fact
- A surprising contrast (outside vs inside, crowd vs calm)
- A direct call-out of who it's for
- A short scene in present tense

A hook that earns the click by curiosity alone can lift CTR while lowering conversion quality. Every hook must point honestly at what the landing page delivers.

## 3. Frameworks by awareness level

Drafting scaffolds only (Consensus; no evidence one outperforms another).
- **PAS** (Problem, Agitate, Solution): problem-aware audiences.
- **BAB** (Before, After, Bridge): solution-aware audiences who need a vivid outcome.
- **AIDA** (Attention, Interest, Desire, Action): longer formats and cold audiences.
- **4 U's** (Useful, Urgent, Unique, Ultra-specific): a checklist to grade each headline. Urgent only when the urgency is real.

## 4. Headline principles (Caples, tested in split runs)

- Appeal to self-interest or give news. Say what the reader gets.
- A longer headline that says something beats a short one that says nothing.
- Specifics beat generalities and are more believable: "4 bedrooms, 12-metre pool, 6 minutes to Hikkaduwa beach" over "spacious luxury villa near the beach" (facts `[VERIFY]`).
- Use the customer's words from the steal sheet.

## 5. Structuring the variation matrix

Test in this order, changing one layer at a time:
1. **Angle** (biggest effect, test first)
2. **Hook or headline** within the winning angle
3. **Format** (static, video, carousel, creator style)
4. **Body length and CTA wording**

Changing angle and format in the same variant makes the result uninterpretable. A first round is usually 3 to 5 angles × 1 hook each, same creative and audience; a second round is the winning angle × 3 hooks.

For each variant record: ID, angle, awareness stage, hook, primary text, headline, description, CTA button, creative note, landing page and match line, hypothesis ("Identity angle will beat pain angle on cost per enquiry for UK couples because reviews stress privacy over price").

## 6. Channel notes

Check current character limits and fields in the live ad manager; they change. General patterns:
- **Paid social (Meta, TikTok, LinkedIn):** mostly cold or lukewarm audiences, so lead with the angle, not the brand. Front-load the first line because the rest is truncated. For video, put the hook and the brand in the first one or two seconds (see the art-direction skill's video module for attention evidence).
- **Search ads:** the searcher already stated the problem or product, so mirror the query, state the offer and a proof point, and qualify (price band, location, minimum stay) to protect conversion rate.
- **LinkedIn and B2B:** specific outcome for a named role; mechanism or proof angles over emotional hooks for SaaS, while keeping the brand voice consistent.
- **Retargeting:** product aware; lead with proof, objection answers or the real offer.

## 7. Sizing and judging the test

- Before launch, size it: `python3 scripts/ab_test_calc.py size --baseline <rate> --mde <absolute difference> --daily <visitors per variant per day>`. Small differences on low base rates need large samples, which is why angle tests (big expected effects) suit small budgets and word-level tests usually don't.
- Judge on cost per qualified conversion, then on conversion quality (lead quality, booking value), not on CTR. CTR is a diagnostic: high CTR with low conversion means the promise and the page don't match, or the hook is curiosity bait.
- Benchmarks for orientation only [Vendor, WordStream/LocaliQ]: search CTR 6.64% all industries (travel 9.32%, real estate 7.61%); Facebook traffic campaigns 1.71% (travel 2.76%, real estate 1.68%). Compare against the account's own history first.
- Note platform delivery: ad platforms optimize delivery toward early winners, so splits are rarely clean. Use the platform's own split test feature where it exists, or treat results as directional.

## 8. Message match handoff

For each winning angle, write the matching landing page headline and subhead in the same words as the ad, with the same offer. If one page serves several angles, give each angle its own headline variant or its own page. Message match is strong practitioner consensus (Gardner, Wiebe, CXL).

## 9. Output

Variation matrix table (also exportable as CSV):

| ID | Round | Angle | Awareness | Hook | Primary text | Headline | Description | CTA | Creative note | Landing page and match line | Hypothesis | Primary metric |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
