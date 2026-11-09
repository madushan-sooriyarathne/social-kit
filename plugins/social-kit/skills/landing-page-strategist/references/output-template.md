# Output Template

Deliver one strategy document per page (or page set). It is used by the client, designer, copywriter and developer, so keep each section scannable. Drop a section rather than pad it; for single-module requests, deliver that module plus the KPI baseline it affects.

```
# [Brand]: Landing Page Strategy ([page name or campaign])
[Date] · Prepared for [user or agency]

## Summary
Three to five sentences: the diagnosis, the core page idea, the traffic tier and what it
means for testing, the top three moves, and what needs verifying.

## Assumptions and inputs
- Materials received (brief, guidelines, photos, reviews, exports) and what was missing
- Anything assumed because the user was not available

## Brief
Goal and primary conversion, offer specifics, audience and awareness level, traffic
sources, constraints, launch date.

## KPI baseline and targets
| KPI | Baseline (period, source) | Target | Notes |
| LCP p75 mobile | | | |
| Lead capture rate (leads / sessions) | | | Denominator stated |
| Form submissions and completion rate | | | |
| Qualified lead rate (guardrail) | | | |
If data is missing, list the exact exports needed instead.

## Diagnosis
- Current page or starting point (audit findings by ResearchXL category, LIFT labels)
- Message match inventory (source, promise, current hero, gap)
- Voice of customer: top questions, objections and phrases
- Competitive convention and the gap this brand can own

## Traffic tier and test strategy
Sample size numbers from sample_size.py, the tier, and what can and cannot be tested.

## Page blueprint
Section table (page-blueprint.md section 10), then the hero copy in full.
Visual direction from brand materials and any brand-rule conflicts.

## Lead capture and form spec
Form spec table (forms.md section 9), submit label, privacy line, success state, spam
layers, alternative channels.

## Speed plan
Budget table, LCP element, third-party inventory with load strategy, build notes for
the stack.

## Tracking plan
Measurement plan, event dictionary, dataLayer examples, dedup, consent decision,
cross-domain, CRM fields and offline conversion loop.

## Hypothesis backlog and test plans
PXL-scored backlog (from pxl_score.py), then a full test plan for each test the tier
allows, or the low-traffic validation plan.

## QA matrix
Before launch: devices, browsers, consent states, form paths, events.

## Reporting
Monthly dashboard contents, owners, cadence.

## What we are not recommending
Tactics the evidence shows waste effort, one line each.

## Evidence notes
The findings the plan leans on, with strength labels and conflicts.

## [VERIFY] list
Every brand fact, number, permission or access item that needs confirming.
```

Notes:
- Tables for specs, logs and plans; prose for reasoning.
- Name the brand's real sources, offers, competitors and assets; no generic filler.
- No invented ratings, prices, traffic or conversion rates.
- Plain, direct sentences. No em dashes; restructure the sentence instead.
- If the environment offers a doc artifact, use it; otherwise write a markdown file and send it. Offer CSV or a sheet for the form spec, event dictionary, backlog and QA matrix.
