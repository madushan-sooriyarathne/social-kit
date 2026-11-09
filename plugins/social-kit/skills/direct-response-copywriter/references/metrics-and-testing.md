# Metrics and Testing

Three headline metrics judge the work: click rate (ads and email), landing page conversion rate, and open rate as a deliverability signal only. Report each against a recorded baseline, and tie it to a business outcome (bookings, qualified leads, trials, revenue).

## Contents
1. Ad click-through rate
2. Email click rate and CTOR
3. Email open rate and Apple MPP
4. Landing page conversion rate
5. A/B testing rules
6. When traffic is too low
7. Test plan format
8. Response vs brand

## 1. Ad click-through rate

- **Definition:** link clicks ÷ impressions. Use link clicks, not all clicks (profile taps, reactions).
- **Benchmarks** [Vendor, WordStream/LocaliQ]: search ads 6.64% all industries (travel 9.32%, real estate 7.61%); Facebook traffic campaigns 1.71% (travel 2.76%, real estate 1.68%).
- **Levers:** angle relevance to the audience, specificity, offer clarity, awareness match, a hook in the first line or second.
- **Caveat:** a diagnostic, not a goal. CTR can rise while conversion quality falls. Judge ads on cost per qualified conversion. Likes and engagement are weaker signals still.

## 2. Email click rate and CTOR

- **Click rate:** unique clickers ÷ delivered. The primary email metric.
- **CTOR:** unique clickers ÷ unique opens. Deflated by MPP's inflated opens; use for trend only within one list.
- **Benchmarks** [Vendor]: Mailchimp 2.62% all users; Klaviyo 2026 campaigns 1.69%, flows 5.58%; Omnisend 2026 abandoned cart 4.13% click, 1.72% conversion.
- **Levers with evidence:** triggered flows over broadcasts (Dataset), simpler design (Controlled, vendor, dated), one clear CTA (Consensus), relevance personalization (Controlled, mixed).
- **Caveat:** security scanners auto-click links on many B2B lists. Filter machine clicks where the ESP allows.

## 3. Email open rate and Apple MPP

- **Definition:** unique opens ÷ delivered.
- **Why it is broken:** Apple Mail Privacy Protection (September 2021) pre-fetches the tracking pixel, recording an open whether or not anyone reads the email, and hides time and location. Apple was 62.26% of tracked opens in Litmus's July 2026 report (1B+ opens), Gmail 27.03%.
- **Use it only for:** deliverability trend. A sudden drop suggests spam-folder placement or a blocklist issue. Segment Apple vs non-Apple opens if the ESP allows, for a cleaner read.
- **Never use it for:** picking subject line winners, defining inactive subscribers, or send-time optimization.
- **Benchmarks** [Vendor, inflated]: Mailchimp 35.63%, Klaviyo campaigns 31%, flows 32.2%, Omnisend abandoned cart 37.12%.

## 4. Landing page conversion rate

- **Definition:** conversions ÷ unique visitors to that page, for one defined goal. Keep micro-conversions (click to booking engine, form start) separate from macro-conversions (booking, qualified lead, trial).
- **Benchmarks** [Vendor, Unbounce 2024 medians]: all 6.6%; travel and hospitality 4.8% (top quartile 15.6%); SaaS 3.8% (11.6%); ecommerce 4.2% (11.4%); financial services 8.3% (26.1%).
- **Levers with evidence:** reading level (Dataset), scannability and concision (Controlled, dated), message match (Consensus), cost transparency and form friction (Dataset, Baymard), proof beside claims (Consensus).
- **Caveat:** traffic source moves conversion rate more than copy in many datasets, so compare like with like. A lower rate with better-qualified leads can be the better page.

## 5. A/B testing rules

1. Write the hypothesis and the single primary metric before launch.
2. Size the test in advance and run whole weeks: `python3 scripts/ab_test_calc.py size --baseline 0.048 --mde 0.012 --daily 300`. Evan Miller's rule of thumb: n per variant = 16 × p × (1 − p) ÷ δ².
3. Don't stop on early significance. Peeking 10 times turns an apparent 1% significance level into a real 5% (Miller). Bayesian dashboards are not immune (Molas 2025).
4. Check the traffic split: `python3 scripts/ab_test_calc.py srm 5012 4890`. A significant mismatch means the test is broken; discard it.
5. Evaluate once, at the planned sample: `python3 scripts/ab_test_calc.py result 120 2500 151 2510`.
6. One change per test where the traffic allows; when testing whole pages, say that the result can't attribute the lift to a single element.
7. Keep a test log: hypothesis, dates, sample, result, decision, what it teaches about the audience.

## 6. When traffic is too low

If the calculator says the test needs months, don't lower the confidence threshold. Use qualitative validation instead: 5-second tests, message testing, customer interviews, session recordings, and an angle test with ads where impressions are cheap. Ship the best-reasoned version and track the trend against the baseline.

## 7. Test plan format

| Asset | Primary metric | Baseline (source) | Variant and hypothesis | MDE | Sample per variant | Duration | Stop rule | Decision if win / lose |
|---|---|---|---|---|---|---|---|---|

Also list the tracking events required (for example `generate_lead`, `begin_checkout`, `purchase`, `click_whatsapp`) and who implements them. The seo-expert skill's tracking-setup module covers GA4 and GTM implementation.

## 8. Response vs brand

Response metrics capture short-term activation only. Binet and Field's IPA analysis found the best long-term profit with about 60% brand and 40% activation for B2C, about 46/54 for B2B (Dataset). Keep the brand voice fixed in the message hierarchy and test angles and offers within it, so CTR-optimized copy doesn't cheapen a premium brand.
