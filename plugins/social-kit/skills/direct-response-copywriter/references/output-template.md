# Output Template

Deliver one copy pack per brand or campaign. Drop sections the request didn't cover rather than padding them.

```
# [Brand]: Direct Response Copy Pack ([campaign or asset set], [date])

## Summary
Two to four sentences: the core message, the angle logic, the recommended first test,
and what needs verifying before launch.

## Assumptions and inputs
- Brief as understood: offer, audience, markets, channels, conversion action
- Data used: VoC sources (with counts), past results, user exports
- Anything assumed because the user wasn't available

## Message hierarchy
- Awareness map (audience × traffic source → stage → opening)
- Sophistication stage and its implication
- Positioning: alternatives, unique attributes, value and proof, best-fit customers, category
- Primary value proposition
- Pillars with proof and VoC phrases
- Objections with answers
- Proof inventory
- Voice rules, words to use, words to avoid
- Validation plan

## Ads
Variation matrix (table from ad-copy.md section 9), round 1 then round 2 plan.
Full copy per variant where it doesn't fit the table.

## Landing page: [name]
- Traffic source and awareness stage
- Message match line (the ad or email promise it continues)
- Copy in page order, headings as they will appear
  - Mark CTAs as **[CTA: label → destination]**
  - Mark proof slots as *[Proof: what, source]*
  - Mark image slots as *[Image: what it shows]*
- Conversion event for tracking

## Email: [flow name]
Sequence map (table from email-sequences.md section 9), then each email in full:
sender, subject options, preview text, body, CTA.

## Test and measurement plan
Test plan table (metrics-and-testing.md section 7), tracking events needed, baseline
or labelled vendor benchmark per metric.

## Checker results
One line per asset from copy_lint.py (reading grade, flags kept and why).

## Evidence notes
The findings the pack leans on, with strength labels, kept short.

## [VERIFY] list
Every fact, policy, price, claim or permission that needs the brand's confirmation.
```

Notes:
- If the environment offers a doc artifact, use it; otherwise write a markdown file and send it.
- Export the ad variation matrix and the email sequence map as CSV (or a spreadsheet artifact) when the user will load them into tools.
- Keep evidence out of the copy itself; it belongs in the notes.
- Character counts for subject lines, headlines and ad fields are real counts from the checker, not estimates.
