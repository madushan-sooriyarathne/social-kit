# Evidence Base for Landing Page Strategy (independent sources only, current to November 2026)

Every recommendation should trace back to something here or to a newer independent finding from the freshness check. Strength labels: **Strong** = controlled experiments, large-scale usability research or peer-reviewed studies with consistent replication; **Moderate** = large correlational data, consistent findings across several independent experts, or single well-run studies; **Weak** = small or dated samples, single case studies, vendor or agency tests without published methods.

## Contents
1. Experimentation reality
2. Page structure and attention
3. Forms and lead capture
4. Page speed
5. Tracking and data quality
6. Myths and wasted effort
7. Expert disagreements
8. Caveats
9. Sources

## 1. Experimentation reality

| Finding | Source | Strength |
|---|---|---|
| Across tens of thousands of tests at Airbnb, Booking, Amazon and Microsoft, the authors have never seen a change lift conversion anywhere near 300%. Large case-study lifts are usually underpowered noise | Kohavi, Deng, Vermeer, "A/B Testing Intuition Busters", KDD 2022 | Strong |
| A landing page case reporting a 337% lift came from 82 vs 75 visitors; pre-test power was about 3% | Kohavi, Deng, Vermeer, KDD 2022 | Strong |
| Published success rates: Microsoft 33%, Avinash Kaushik 20%, Bing 15%, Booking.com, Google Ads and Netflix about 10%, Airbnb Search 8%. At a 10% success rate and p < 0.05, about 22% of "significant" wins are false; assume 10% if you do not know your own rate | Kohavi, Deng, Vermeer, KDD 2022 | Strong |
| Meta-analysis of 1,001 tests: median lift 0.08%, mean 2.08%, median MDE 6%, about 33.5% had a significant winner, median test 60,342 users | Georgiev, Analytics-Toolkit, 2022 | Strong |
| About 70% of 115 public GoodUI tests had low power; median lift of the 85 kept tests was 3.92% | Georgiev, 2018 | Moderate |
| Significant results from tests with power below 50% must exaggerate the effect; below 10% power the sign is nearly a coin flip | Gelman and Carlin, cited by Kohavi | Strong |
| Checking significance repeatedly and stopping at the first significant reading pushes false positives to about 26% in a worked example, versus the nominal 5% | Evan Miller, "How Not to Run an A/B Test" | Strong |
| About 6% of Microsoft experiments showed sample ratio mismatch; LinkedIn reported about 10% of triggered experiments used to | Fabijan, Vermeer et al., KDD 2019 | Strong |
| Never set an MDE above 5% for mature products; larger true effects almost never happen unless something was broken | Kohavi, 2025 webinar (hosted by GrowthBook, a vendor) | Moderate |
| Sample size at 80% power and alpha 0.05: n = 16 p(1 - p) / delta squared per variant | Kohavi, Deng, Vermeer | Strong |

## 2. Page structure and attention

| Finding | Source | Strength |
|---|---|---|
| Users spent about 57% of viewing time above the fold, 74% in the first two screenfuls, 81% in the first three (2010 study: 80% above the fold). Attention is front-loaded but people scroll | NN/g eyetracking, 2018 | Strong |
| Full-width hero images or videos that look complete create an "illusion of completeness" and stop scrolling; let the next section show | NN/g | Moderate |
| Decorative imagery is ignored; product and real-people images are studied | NN/g eyetracking | Strong |
| ResearchXL: technical, heuristic, web analytics, mouse tracking, qualitative surveys, user testing. Heuristic findings are areas of interest, not truths. Fix technical issues first | Peep Laja, CXL | Moderate (framework) |
| LIFT model: value proposition, relevance, clarity, anxiety, distraction, urgency | Chris Goward, WiderFunnel (agency) | Weak as evidence, useful vocabulary |
| Message match and one conversion goal per campaign page (attention ratio 1:1) | Oli Gardner; Tim Ash; CXL | Moderate for message match, Weak to Moderate for attention ratio |
| Page length should follow awareness level: short for most-aware, longer objection handling for colder traffic | Eugene Schwartz, applied by Joanna Wiebe (Copyhackers) | Moderate (practitioner consensus) |
| Voice-of-customer phrasing from reviews, surveys and sales calls as copy source | Copyhackers | Moderate |
| Leading with the emotional outcome over feature lists | Talia Wolf | Weak (lift claims), plausible for hedonic categories |

## 3. Forms and lead capture

| Finding | Source | Strength |
|---|---|---|
| Placeholder text used as labels harms memory, error checking and accessibility; use persistent visible labels | NN/g, "Placeholders in Form Fields Are Harmful" | Strong |
| 32% of participants missed at least one required field when only optional fields were marked; 75% hit severe issues on mobile when both were not marked | Baymard | Strong |
| Checkout averages 5.1 steps and 11.3 fields; most sites need about 8; 17% abandoned for complexity; field count affects usability more than step count | Baymard 2024 (ecommerce checkout, mechanics transfer to lead forms) | Strong |
| Cutting one of NN/g's forms from 6 to 2 fields; each field cut tends to raise completion | NN/g | Moderate |
| Cutting a lead form from 9 to 6 fields dropped conversions 14%; keeping 9 with rewritten labels and order lifted 19.21% | Michael Aagaard, reported by CXL (single test, author then at Unbounce, sample not published) | Weak to Moderate, important caution |
| Removing a confusing optional "Company" field reportedly added about $12M a year | Expedia (Joe Megibow), 2010 anecdote | Weak; a label clarity lesson |
| Adding company size and industry fields dropped conversion; cost per lead rose from $34.94 to $41.90 | MarketingExperiments / Marketo (vendor) | Weak |
| Adding a phone field cut ebook form conversion about 48% | Vital Design (agency test) | Weak |
| Inline validation on blur: 22% higher success, 22% fewer errors, 31% higher satisfaction, 42% faster completion | Wroblewski and Etre, 2009, 22 participants | Direction Moderate, numbers Weak |
| Forms following 20 usability guidelines were completed faster with fewer attempts; NN/g summary: 78% vs 42% error-free first submissions | Seckler et al., CHI 2014 (one co-author Google-affiliated) | Strong for direction |
| Staged disclosure (wizards) suits complex or occasional tasks | NN/g | Moderate |
| Multi-step "converts 86% higher" style claims | Form-tool vendor blogs, no methods | Weak; do not cite as fact |
| 8.66% of users failed a CAPTCHA first try, 29.45% when case-sensitive | Baymard, 2018 | Moderate, dated |
| About 3.2% of conversions lost with CAPTCHA on across about 50 sites | Moz, 2009 | Weak, dated |
| Developer-pushed dataLayer events are the most robust form tracking; DOM triggers break easily | Analytics Mania (Julius Fedorovicius) | Strong (practitioner consensus) |

## 4. Page speed

| Finding | Source | Strength |
|---|---|---|
| A 1 second increase in load time associated with 2.7% fewer downloads; the analyst flagged omitted-variable bias and ran a follow-up experiment | Mozilla, 2010 | Moderate |
| Correlation charts between speed and conversion are not cause and effect; test on your own site | Tammy Everts | Moderate |
| No consistent link between INP "good/poor" thresholds and conversion; one site lost conversions at 100ms INP | SpeedCurve (Cliff Crocker), vendor | Weak to Moderate; supports site-specific budgets |
| After dozens of performance A/B tests, no single metric consistently correlated with conversion, though most tests showed positive effects | Fasterize, Web Performance Calendar 2024, vendor | Weak |
| Average load time directly affected conversion in one Magento store | Stadnik and Nowak, 2017, peer-reviewed, observational | Moderate |
| 90% of pages include at least one third party; median 16 third-party domains; 41% of mobile home pages could use third-party facades | HTTP Archive Web Almanac 2025 (community-authored) | Strong (descriptive) |
| Anti-flicker snippets hide the whole page until the testing tool loads; 1.7 seconds of blank screen measured in one example; default timeouts are far too long | Andy Davies, 2020 | Strong (mechanism) |
| "0.1s = 8% more conversions" | Deloitte/55, Google-commissioned | Excluded under source policy |

Interpretation: speed is a hygiene factor with a real but site-specific effect. It matters most on mobile paid traffic, where a slow LCP wastes spend before the visitor sees the offer.

## 5. Tracking and data quality

- Basic Consent Mode: Google tags collect nothing until consent; GA4 behavioural modelling effectively off. Advanced: cookieless pings when denied, enabling modelling; discuss with legal counsel (Simo Ahava). **Moderate to Strong.**
- Server-side tagging reduces client load and gives data control; using it mainly to evade ad blockers erodes user agency (Ahava). Adds cost and maintenance. **Moderate.**
- GA4 Enhanced Measurement form interactions often conflict with custom form tracking and miscount conversions (Analytics Mania). **Moderate.**
- Dirty data sources: GTM plus hard-coded gtag, missing cross-domain linker, unfiltered internal traffic, duplicate submits on reload (Analytics Mania, Simo Ahava). **Strong (practitioner consensus).**

## 6. Myths and wasted effort

- **Button colour tests.** Contrast and visibility matter; hue rarely does. Big colour wins are Twyman's law candidates.
- **"Everything must be above the fold."** About 43% of attention lands below the first screen (NN/g).
- **Copying case-study lifts.** Usually underpowered noise (Kohavi et al.).
- **"Shorter forms always win."** Wording and relevance can beat cutting (Aagaard).
- **"Multi-step always converts better."** Vendor claims without methods.
- **"0.1 seconds = 8%."** Google-sponsored, observational, not transferable.
- **Reading a vendor dashboard's "95% confidence" as the chance the variant is better.** It is not.
- **Judging a form change on submissions alone.** Lead quality can move the other way.
- **Running A/B tests on a few thousand sessions a month.** The test cannot detect realistic effects.

## 7. Expert disagreements

| Topic | One side | Other side | Working rule |
|---|---|---|---|
| Form length | NN/g, Baymard: cut fields | Aagaard: cutting the wrong fields hurts | Remove fields that add effort without value to the user or sales; rewrite before deleting |
| MDE realism | Kohavi: never above 5% for mature products | Small-site practitioners: only big changes are testable | Test big changes, treat big wins sceptically, replicate |
| Statistics | Georgiev: frequentist, sequential, pre-registered | Bayesian advocates: easier for clients to read | Discipline (power, no unplanned peeking, honest reporting) matters more than the school; state priors if Bayesian |
| Speed causality | Performance vendors: near-universal gains | Everts and others: correlation, site-specific | Fix poor mobile LCP, set budgets, measure your own effect |
| Consent Mode | Advanced recovers modelled data | Basic respects non-consent more fully | Legal and ethical choice; record it |

## 8. Caveats

- Several form statistics are small or old (Wroblewski 2009, Moz 2009, Expedia 2010). Trust the direction, not the percentages.
- Baymard benchmarks are ecommerce checkout; the effort mechanics transfer, the benchmark numbers do not.
- Kohavi's distributions come from large tech firms; Georgiev's practitioner data suggests small effects are typical elsewhere too.
- Vendors with commercial interests: SpeedCurve, Fasterize, Unbounce, GrowthBook, VWO, Optimizely, Wynter, form tools, MarketingExperiments.
- Independent lead-gen conversion benchmarks for luxury hospitality and Sri Lankan real estate effectively do not exist. Build baselines per client.
- GA4 and Consent Mode behaviour changes often; verify settings in the live product.

## 9. Sources

- Kohavi, Deng, Vermeer, A/B Testing Intuition Busters: https://airbnb.tech/wp-content/uploads/sites/19/2025/10/ABTestingIntuitionBusters.pdf
- Georgiev, 1,001 A/B tests: https://blog.analytics-toolkit.com/2022/what-can-be-learned-from-1001-a-b-tests/
- Evan Miller, How Not to Run an A/B Test: https://www.evanmiller.org/how-not-to-run-an-ab-test.html
- Fabijan et al., SRM: https://dl.acm.org/doi/10.1145/3097983.3097992
- Kohavi webinar notes: https://www.growthbook.io/blog/lessons-learned-from-ronny-kohavi-and-luke-sonnet-running-trustworthy-experiments
- CXL ResearchXL: https://cxl.com/conversion-optimization/conversion-research/
- CXL, reducing form fields (Aagaard): https://cxl.com/blog/reduce-form-fields/
- CXL, web form optimization: https://cxl.com/blog/web-form-optimization/
- NN/g, scrolling and attention: https://www.nngroup.com/articles/scrolling-and-attention/
- NN/g, placeholders: https://www.nngroup.com/articles/form-design-placeholders/
- NN/g, web form design: https://www.nngroup.com/articles/web-form-design/
- NN/g, wizards: https://www.nngroup.com/articles/wizards/
- Baymard, required and optional fields: https://baymard.com/research-articles/required-optional-form-fields
- Baymard, checkout form fields: https://baymard.com/research-articles/checkout-flow-average-form-fields
- Wroblewski, inline validation: https://www.lukew.com/ff/entry.asp?883=
- Seckler et al., web form guidelines: https://www.researchgate.net/publication/263350416_Designing_Usable_Web_Forms_-_Empirical_Evaluation_of_Web_Form_Improvement_Guidelines_Web
- Mozilla page load speed: https://blog.mozilla.org/metrics/2010/03/31/firefox-page-load-speed-part-i/
- Fasterize, correlation or causation: https://calendar.perfplanet.com/2024/correlation-or-causation-how-web-performance-proves-its-value/
- Stadnik and Nowak: https://link.springer.com/chapter/10.1007/978-3-319-67220-5_31
- Web Almanac 2025, page weight: https://almanac.httparchive.org/en/2025/page-weight
- Andy Davies, anti-flicker snippets: https://andydavies.me/blog/2020/11/16/the-case-against-anti-flicker-snippets/
- Analytics Mania, form tracking: https://www.analyticsmania.com/post/google-tag-manager-form-tracking/
- Analytics Mania, form abandonment: https://www.analyticsmania.com/post/form-abandonment-tracking-google-tag-manager/
- Simo Ahava, Consent Mode v2: https://www.simoahava.com/analytics/consent-mode-v2-google-tags/
- Simo Ahava, Basic Consent Mode: https://www.simoahava.com/analytics/basic-consent-mode-the-guide/
- Simo Ahava, server-side tagging: https://www.simoahava.com/analytics/agency-transparency-control-unsolved-problems-server-side-tagging/
