# Hypotheses, A/B Testing and Low-Traffic Validation

A test only answers a question when it has enough traffic to detect a realistic effect. Typical true effects are small (Georgiev: median lift 0.08% across 1,001 tests) and underpowered "wins" exaggerate or reverse the truth (Kohavi, Deng, Vermeer). So the first decision is not what to test but whether this page can test at all.

## Contents
1. Hypothesis format
2. Prioritization with PXL
3. Sample size and traffic tiers
4. Test plan template
5. Running a test: duration, peeking, sequential stopping
6. Reading a result: SRM, Twyman's law, guardrails
7. Client-side vs server-side
8. Low-traffic playbook
9. Learning log

## 1. Hypothesis format

"Because we observed [evidence from discovery], we believe [change] for [audience or source] will cause [primary metric] to [increase or decrease], measured by [event]. Guardrails: [metrics]."

Every hypothesis cites its research input. An idea with no evidence behind it goes to the bottom of the backlog.

## 2. Prioritization with PXL

CXL's PXL uses binary questions to reduce opinion. `scripts/pxl_score.py` applies these weights:

| Criterion | Score |
|---|---|
| Above the fold | 1 |
| Noticeable within 5 seconds | 2 |
| Adds or removes an element | 1 |
| Designed to increase motivation | 1 |
| Runs on a high-traffic page | 1 |
| Addresses an issue found in user testing | 2 |
| Addresses an issue found in qualitative feedback (surveys, reviews, sales notes) | 1 |
| Supported by analytics data | 1 |
| Supported by mouse tracking or recordings | 1 |
| Ease: under 1 hour = 3, 1 to 4 hours = 2, 4 to 8 hours = 1, over 8 hours = 0 | 0 to 3 |

Known critique: PXL rewards qualitatively sourced ideas whether or not they win more often in your data. After 20 to 30 tests, recalibrate the weights against the learning log (`--weights` option). On Tier 3 pages, use the score to order implementation, not tests.

## 3. Sample size and traffic tiers

Per-variant sample at 80% power and alpha 0.05 (Kohavi, Deng, Vermeer): n = 16 p(1 - p) / delta squared, where p is the baseline rate and delta the absolute effect. `scripts/sample_size.py` uses the exact two-proportion formula, which gives slightly larger numbers than the rule of thumb, and converts them to weeks of traffic.

Worked example at a 2% enquiry rate and 3,000 sessions a month, 50/50 split (script output):

| Relative lift to detect | Per variant | Duration |
|---|---|---|
| 10% | about 80,700 | about 4.5 years |
| 20% | about 21,100 | about 14 months |
| 50% | about 3,800 | about 11 weeks |

Tiers used in the strategy:
- **Tier 1, test-ready:** a 20% relative MDE is reachable in 6 weeks or less. Run server-side A/B tests with pre-registered sample sizes. Kohavi advises MDEs of 5% or less for mature products; most agency client pages will not reach that, so be explicit about what the test can and cannot see.
- **Tier 2, big swings only:** a 50% relative MDE is reachable in about 8 weeks or less. Test whole-page concepts, offer changes or channel-first layouts, with a sequential stopping rule.
- **Tier 3, no valid A/B:** use the low-traffic playbook.

## 4. Test plan template

| Field | Content |
|---|---|
| Hypothesis | In the standard format |
| Evidence | The discovery finding behind it |
| Variants | Screenshots or blueprint diffs |
| Primary metric | One, defined by event and denominator |
| Guardrails | Qualified lead rate, LCP per variant, form error rate, secondary conversions |
| Audience and split | Sources, devices, 50/50 unless justified |
| Baseline and MDE | With source of the baseline |
| Sample size and duration | From sample_size.py, whole weeks, at least 2 weeks |
| Stopping rule | Fixed horizon, or sequential threshold stated in advance |
| SRM check | Chi-squared on assignment counts before analysis |
| Decision rule | What result ships, what result is inconclusive |

## 5. Running a test: duration, peeking, sequential stopping

- Fix the sample size in advance and run whole weekly cycles, at least 2 weeks, so weekday and weekend behaviour are both covered.
- Do not stop the first time a dashboard shows significance. Repeated peeking inflated false positives to about 26% in Evan Miller's worked example. Bayesian dashboards are not immune.
- If early stopping is needed, pre-register a sequential design. Evan Miller's simple sequential test: fix a total conversion count N; declare the treatment the winner when its conversions exceed control's by 2 times the square root of N; stop with no winner when the two together reach N. `sample_size.py` estimates N for a given lift (an approximation; check against Miller's calculator).
- Note traffic mix changes during the test (a new campaign launching, a seasonal shift) and segment by source.

## 6. Reading a result: SRM, Twyman's law, guardrails

1. **SRM first.** Run `scripts/srm_check.py <control count> <variant count>`. About 6% of Microsoft experiments had a mismatched split (Fabijan, Vermeer et al.). If p < 0.001, do not trust the result; look for bots, redirects, consent-dependent tracking or a variant that errors.
2. **Twyman's law.** Any figure that looks interesting or different is usually wrong. A large lift on a small sample needs replication or a stricter threshold.
3. **Winner's curse.** With power under 50%, a significant effect is exaggerated; report the confidence interval, not only the point estimate.
4. **Guardrails.** A variant that raises submissions but lowers qualified rate or slows LCP is not a win.
5. **Novelty effect.** Check the effect over time and for new vs returning visitors.
6. **Multiple comparisons.** One primary metric, declared in advance; extra variants and metrics need correction.

Frequentist or Bayesian: Georgiev defends frequentist sequential designs; Bayesian advocates prefer probability-of-better wording. Pre-registration, power and honest reporting matter more than the school. If reporting Bayesian results, state the prior. Never present "95% confidence" as the chance the variant is better.

## 7. Client-side vs server-side

Client-side tools change the page in the browser, which causes flicker or, with anti-flicker snippets, blank time and slower LCP (Andy Davies). Server-side assignment (Next.js middleware, an edge function, or an open-source framework such as GrowthBook self-hosted, a vendor) renders the variant before the page reaches the browser, costs almost no speed, and logs assignment for SRM checks. Default to server-side.

## 8. Low-traffic playbook (Tier 2 and 3)

1. **Fix before testing.** Bugs, broken tracking, slow mobile loads and confusing form fields do not need a test.
2. **Qualitative validation.** Five-user tests catch large usability problems; message testing panels (for example Wynter, a vendor) show target-audience reactions to copy without live traffic, useful for B2B SaaS; first-click and preference tests check layouts.
3. **Bold changes.** Only changes that could plausibly move conversion 30 to 50% or more are detectable: new offer framing, a new page structure, WhatsApp-first vs form-first.
4. **Proxy metrics with caution.** `form_start` and CTA clicks have more volume than leads, but can mislead; confirm against leads and qualified leads over time.
5. **Sequential tests** for clear winners or losers on Tier 2.
6. **Season-matched pre/post.** Compare equal-length periods against the same period last year (Sri Lankan high season runs roughly December to April), track traffic mix, and present the result as directional, not causal. Where possible keep a holdout (one source or market on the old page).
7. **Pool learnings across clients.** A pattern that wins on several similar sites is stronger evidence than one underpowered test (the GoodUI approach).

## 9. Learning log

One record per test or major change: hypothesis, evidence, screenshots, primary and guardrail metrics, MDE and sample size, dates, SRM result, outcome with confidence interval, decision, follow-ups. Keep it searchable (a sheet, Notion, Airtable or a CMS dataset) and use it to recalibrate PXL weights.
