# Landing Page Copy

Goal: one page, one audience, one action, with copy that matches the traffic's awareness level and the promise that brought the visitor there.

## Contents
1. Map traffic to awareness
2. Page structures by awareness
3. Above the fold
4. Writing for scanners and reading level
5. Proof and objections
6. CTA and forms
7. Length
8. Checklist
9. Benchmarks

## 1. Map traffic to awareness

| Traffic source | Usual awareness | Lead with |
|---|---|---|
| Branded search, email to own list, abandonment emails | Product or Most Aware | The offer, proof, CTA fast |
| Category or comparison search | Solution Aware | Outcome and why this approach beats the alternatives |
| Retargeting | Product Aware | Proof and objection answers |
| Cold paid social | Problem Aware or Unaware | The problem, a story or identity, then earn the pitch |

Own-list email traffic converts best (Unbounce: 28.6% median for email-sourced ecommerce traffic, secondhand, [Vendor]). Expect cold traffic to convert lower and judge each page against its own source.

## 2. Page structures by awareness

Section names are functions, not literal headings.

**Most Aware or Product Aware (short)**
1. Headline that restates the offer from the ad or email
2. Subhead: what it is, for whom, the key specific
3. CTA plus one proof element
4. Key facts block (price or rate, inclusions, capacity, terms)
5. Proof (reviews with source)
6. Top 3 to 5 objections as FAQ
7. CTA repeated

**Solution Aware (medium)**
1. Outcome headline matching the ad
2. Subhead naming the alternative and why this is different
3. CTA plus proof
4. How it works or what you get (numbered or bulleted)
5. Proof next to each claim
6. Comparison with the alternative, honest
7. Objections, CTA

**Problem Aware or Unaware (long)**
1. Hook headline in the reader's words (the problem or the identity)
2. Short story or scene that names the before state
3. The bridge: the solution category, then this product's mechanism
4. Outcome and specifics
5. Proof stack
6. Offer, objections in order, risk reversal if real (guarantee, cancellation policy)
7. CTA after each major section, not only at the end

## 3. Above the fold

- **Headline:** matches the ad's promise in the same words and states the primary outcome. Clarity beats cleverness.
- **Subhead:** what it is and who it's for, with one specific.
- **One primary CTA** naming what the visitor gets.
- **One proof element:** rating with source, review count, award, client logo.

A visitor should be able to say what the brand offers within five seconds (test it; see foundation.md section 7).

## 4. Writing for scanners and reading level

- 79% of users scan and 16% read word by word (NN/g, Controlled, 1997). Concise, scannable and objective writing combined improved usability 124%.
- Meaningful subheads that carry the argument on their own, bullets for lists, one idea per paragraph, no marketese.
- Aim for a 5th to 7th grade reading level (Unbounce: 11.1% median vs 5.3% at professional level; SaaS 12.9% vs 2.1%; Dataset [Vendor], correlational). Run `scripts/copy_lint.py`.
- For luxury, low reading level means short sentences carrying sensory specifics ("The pool is yours from 7 am. The only sound is the jungle."), not plain or cheap language.

## 5. Proof and objections

- Put proof next to the claim it supports, not in a separate testimonials block nobody reaches.
- Specific numbers and named, dated testimonials beat generic praise (Caples: specifics are more believable).
- Answer objections from the VoC file in the order buyers raise them, usually price, trust, fit, effort, risk.
- Risk reversal only if real: free cancellation window, guarantee, trial terms. Quote the actual policy.
- Never invent reviews, counts, awards or scarcity. Use `[VERIFY]`.

## 6. CTA and forms

- CTA labels name the outcome: "Check availability", "Get my valuation", "Start my free trial", not "Submit" or "Learn more" (Consensus).
- One primary action per page; secondary actions (WhatsApp, call) only where that's how leads actually arrive.
- Ask only for fields you'll use. Show cost and terms early; unexpected costs are the most common fixable abandonment cause (Baymard: 40% of US shoppers abandoned over extra costs; Dataset).
- Microcopy under the CTA answers the last worry ("Free cancellation until 14 days before arrival" `[VERIFY]`; "No credit card required").
- If the CTA leads to a third-party booking engine or checkout, the page copy should prepare the visitor for it (what they'll see, what it costs) so the hand-off doesn't lose them.

## 7. Length

Fit length to awareness, price and risk. Long copy suits low awareness, high price and high risk; short copy suits Most Aware visitors and low-commitment offers (Consensus: Caples, Ogilvy, modern CRO). Unbounce found SaaS pages at 250 to 725 words and finance pages at 195 to 715 words converted best in its data ([Vendor]). Stop when every objection for that awareness level is answered.

## 8. Checklist

1. Headline matches the ad or email that sends traffic
2. Visitor can say what it is and who it's for in five seconds
3. One primary CTA, labelled with the outcome, visible on mobile without scrolling
4. Proof beside each major claim, with source
5. Objections answered in buyer order
6. Costs, terms and policies stated before the hand-off
7. Reading grade at or near 7, short sentences, subheads that carry the argument
8. No invented facts; `[VERIFY]` list complete
9. Conversion event defined for tracking
10. A test hypothesis for the page's first iteration

## 9. Benchmarks

Unbounce 2024 medians [Vendor]: all industries 6.6%; travel and hospitality 4.8% (top quartile 15.6%); SaaS 3.8% (top quartile 11.6%); ecommerce 4.2%; financial services 8.3%. Real estate not verified in primary data. Compare against the page's own baseline and traffic source first.
