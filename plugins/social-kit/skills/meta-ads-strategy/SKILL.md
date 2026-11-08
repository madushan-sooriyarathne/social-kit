---
name: meta-ads-strategy
description: Build a complete, launch-ready Meta (Facebook and Instagram) ads strategy for a specific brand, grounded in independent practitioner research rather than Meta's own guidance. Use this whenever the user names a brand, client, product or website and wants a Meta ads plan, campaign structure, creative plan, budget split, testing roadmap or a review of how they run paid social, even if they only say "how should we run Facebook ads for X", "plan Instagram ads for this client", or paste a URL and ask about paid social.
---

# Meta Ads Strategy

Turn one brand into a Meta ads strategy that a media buyer could launch from on Monday. The knowledge base in `references/` is a synthesis of independent experts and third-party datasets (Jon Loomer, Andrew Foxwell, Barry Hott, Charley Tichenor, Ben Heath, Common Thread Collective, Motion, Haus). Material published by Meta is deliberately excluded because it is written to encourage more spend and more automation. Apply the same rule if you research anything during a run: use independent practitioners and third-party data, not Meta's blog, Blueprint, help center or case studies.

## Bundled files

- `references/playbook.md`: the core rules by topic (structure, creative, targeting, measurement, bidding, funnel, mistakes). Read it every time.
- `references/verticals.md`: notes for hospitality, real estate, SaaS, ecommerce, local services and small or low-budget markets. Read only the sections that match the brand.
- `references/sources.md`: who each source is, why it is credible, the refresh date and the refresh procedure. Read it when you need to cite, when the user asks "says who?", or when refreshing the skill.
- `scripts/budget_math.py`: computes how many ad sets the budget can feed, whether the learning phase is reachable and the creative cadence for the spend tier. Run it rather than doing the arithmetic in your head.

## Workflow

### 1. Build the brand picture

If the user gave a URL, fetch the homepage plus the pages that matter for conversion (product or pricing, booking engine or checkout, contact or enquiry form). Extract what is sold, price or average order value, the conversion path and how many steps it has, the offer, the proof (reviews, awards, press), target markets and languages, and whether a Meta pixel is visible in the page source (`connect.facebook.net` or `fbq(`). A visible pixel says nothing about the Conversions API, so treat CAPI as unknown until confirmed.

Some facts only the user knows. The ones that change the strategy most are:

1. Monthly ad budget and currency
2. The business outcome that matters (bookings, qualified leads, trials, sales) and roughly what one is worth
3. Target markets (where the buyers live, which can differ from where the brand is)
4. Current tracking (pixel, CAPI, CRM) and how many conversions a month the site produces today

Ask for whichever of these you cannot infer, in one short message. If the user is not around to answer or tells you to go ahead, make the most plausible assumption, label it clearly in the strategy, and note only the assumptions that would flip a decision if wrong. Do not produce parallel plans for every possible budget; one focused plan with a stated assumption is more useful.

### 2. Classify the situation

Pin down these five things before recommending anything, because almost every later choice follows from them:

- **Vertical**, which selects the section of `references/verticals.md` to read.
- **Conversion economics**: expected cost per result for the deepest worthwhile event. If the brand has no history, estimate from price point and source-market CPMs and say it is an estimate.
- **Budget math**: run `python scripts/budget_math.py --monthly-budget <amount> --cpa <expected cost per result>` and use its output for ad set count, learning feasibility and creative cadence.
- **Special Ad Category**: housing, employment, credit/financial products and social or political issues carry targeting restrictions, and they apply based on the audience's location, not the advertiser's.
- **Source market**: CPMs follow the audience. A Sri Lankan villa selling to UK travellers pays UK prices.

### 3. Choose the optimization event

Pick the deepest event the account can realistically feed at roughly 25 to 50 a week per ad set: purchase or booking with value, then qualified lead or CRM stage, then lead, then add to cart or initiate checkout as a last resort. Meta optimizes literally for whatever you pick, so a cheap proxy event buys cheap, low-quality people. If the deep event can never reach volume (high-ticket villas, B2B), keep it anyway when results are judgeable over a longer window, consolidate to one ad set, and say plainly that the campaign may never exit learning.

### 4. Write the strategy

Use the template below. Every recommendation should be specific to this brand (its offer, its buyer, its numbers) and carry a one-line reason. Tag a claim with its source in brackets, such as [Loomer] or [Motion 2026], only where the source adds weight or where experts disagree; do not footnote every sentence.

Where experts genuinely disagree (CBO vs ABO, excluding past customers, bid caps, creative volume, the Incremental Attribution setting), state which side you recommend for this brand and why, in one or two sentences.

## Strategy template

```
# Meta Ads Strategy: [Brand]
Prepared [date] · Knowledge base refreshed [date from sources.md]

## Summary
Three to five sentences: the goal, the structure, the creative bet, the budget, and the single biggest risk.

## Assumptions and inputs
What was given, what was inferred from the site, what was assumed. Mark assumptions that would change the plan if wrong.

## Readiness checklist (fix before spending)
Tracking (pixel, CAPI, deduplication, Event Match Quality target 7+), conversion event with value, landing page and offer match, response time for leads or enquiries. Mark each as ready, missing or unknown, and list blockers first.

## Optimization event and measurement
The event to optimize for and why. Attribution setting and how to read results (break down click vs view). The incrementality check planned for this account.

## Account structure
Campaigns and ad sets as a small table: name, objective, optimization event, targeting, budget, purpose. Include the budget_math output (conversions per week, ad sets supportable) in one or two lines.

## Targeting and exclusions
Hard settings only (location, minimum age if justified, custom audience exclusions). Any value rules. Your position on excluding past customers.

## Creative plan
Monthly cadence from budget_math. Then the first batch of distinct concepts (usually 4 to 6): for each, the angle, the persona or motivation it targets, the format, and a sample hook written for this brand. Concepts must differ in angle, format or persona, not just in copy.

## Bidding, budget and scaling rules
Starting bid strategy, when to add cost caps or a minimum ROAS, and the rule for scaling.

## First 90 days
Weeks 1-2, 3-6, 7-12: what launches, what gets tested, what decision is made at each checkpoint and on what metric.

## KPIs and decision rules
Primary KPI and target, guardrail metrics, and explicit kill/keep/scale rules judged on weekly data.

## Risks and open questions
```

## Output style

Write concisely and directly, with no em dashes. Use numbers wherever possible (budgets, thresholds, timelines). Prefer one clear recommendation over a menu of options. Keep the strategy under about 1,500 words unless the user asks for more depth; the creative concepts are where extra words earn their keep.

Deliver it as a document the user can keep and share: the environment's document type if one exists, otherwise a markdown file.

## Freshness

Meta changes features often. Check the refresh date in `references/sources.md`. If it is more than 60 days old and web search is available, do a quick check for major platform changes reported by independent sources (jonloomer.com is the most reliable single source) before finalizing, and mention anything that changes the plan. If you cannot check, say in one line that platform details may have moved since the refresh date.
