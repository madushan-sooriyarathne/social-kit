# Meta Ads Playbook (independent sources only)

Core rules distilled from independent practitioners and third-party data. Source details and credibility notes are in `sources.md`. Figures are as of the refresh date there.

## Contents
1. Account and campaign structure
2. Creative strategy
3. Targeting and audiences
4. Tracking and measurement
5. Budgeting, bidding and scaling
6. Optimization events and funnel
7. Common mistakes
8. Where experts disagree (quick reference)

---

## 1. Account and campaign structure

**Consolidate.** Start with one campaign and one ad set per business goal, optimized for a conversion. Loomer: "$100 in one ad set is more efficient than $100 split across five."

- Capacity rule [Loomer]: weekly budget ÷ (cost per result × 50) = the most ad sets the budget can feed. Consider a second ad set only at 100+ conversions a week and only for a real reason.
- Legitimate reasons to split: different business goals (leads vs sales), distinct products or locations needing different messaging, seasonal products, and enough budget to feed each split.
- CTC's mature-account template: four campaigns, Evergreen vs Marketing Moment crossed with Acquisition vs Retention. All value-optimized with a minimum ROAS goal, Sales objective in about 95% of cases, ad sets filled to 50 ads before a new one starts. Useful once spend and catalog justify it; overkill for small accounts.

**Advantage+.** Now the default creation flow for Sales, Leads and App campaigns. Advantage+ Sales is not just renamed Advantage+ Shopping: ad sets returned, the Existing Customer Budget Cap was removed, 50 ads per ad set [Loomer].
- Haus (640 incrementality tests): Advantage+ beat manual campaigns in only 42% of tests, with modest gains when it won. It was 9% better at the experiment midpoint but 12% worse by the end, and drove 17% less lift post-test.
- Practice: reasonable default, not automatically better. Run it against a manual build at least once, then lean into the winner rather than splitting budget evenly [Haus].

**Testing structure.**
- Loomer dropped separate testing campaigns. He uses Meta's built-in creative testing tool (2 to 5 ads inside the live ad set, even spend, no auction overlap) because an ad that wins in isolation often fails once moved.
- Hott: CBO with cost caps and minimum spend on new ad sets so new creative gets a fair shot. Judge batches by campaign spend, not single-ad CPA. He has shown a $800K/month CBO campaign with 200+ ads each spending $1,000+, which undercuts the claim that CBO starves everything but one or two ads.
- Tichenor's 3:2:2 method: flexible ads with 3 creatives, 2 primary texts, 2 headlines, letting the platform find combinations inside a simple structure.
- Synthesis: new or low-data accounts benefit from occasional ABO forced-spend tests for clean reads on big new ideas. Mature accounts test inside CBO or Advantage+.

## 2. Creative strategy

**Creative is the targeting.** Andromeda (Meta's ad retrieval engine) plus the GEM ranking model match ads to people largely from the creative itself [Loomer, CTC, Foxwell]. Loomer warns against mythologizing it: it does not change your targeting strategy and did not kill results. The practical lesson is diversity.

**Diversity over volume, though volume still matters statistically** [Motion 2026, $1.29B spend, 578,750 creatives, 6,015 accounts]:
- About 5% of creatives become winners (≥10x account median spend and ≥$500).
- Hit rate rises from 3.8% (Micro accounts) to 8.2% (Enterprise).
- 55% of spend goes to winners overall: 23% at Micro accounts vs 64% at Enterprise.
- Average weekly launches: 2.8 creatives under $10K/month up to 18.85 at $1M+/month. Top-quartile accounts launch 2 to 3x their tier average and find about twice as many winners at the same spend.
- Motion's caveat: volume creates more chances to find a winner, but the per-creative odds do not change.

**How much to launch.**
- Foxwell: about 8 to 10 new concepts a month (40 to 50 assets) for brands at $100K+/month; about 4 to 5 assets a month at $5K/month. Warns against the "volume trap".
- Loomer tried 20 to 50 ads at once and found it wasteful because Meta concentrates spend on a handful. He builds diversity in phases (his "creative diversity stack").
- Reconcile: scale volume with spend, and count distinct concepts, not file variations.

**Formats** [Motion 2026 hit rates]:
- By production type: text-only 11.6%, product image with text 8.75%, UGC 7.56%, high production 6.87%. Cheap and fast beat polished.
- By visual format: offer-first banner 8.68%, demo 8.11%, montage 7.02%, testimonial 6.57%; smaller formats "letter" 10.83% and founder-led 8.57%.
- Caveats: top formats vary across Motion's 16 verticals, and the data window includes BFCM, which inflates offer-led formats.
- Hott's "make ugly ads": creative that looks like organic content beats polished, marketer-approved creative. The competition is the feed, not other ads.
- Foxwell: start around 50/50 static vs video and let data shift it. Partnership (creator/whitelisted) ads work, but only with ongoing creator relationships.

**Judging and fatigue.**
- Spend allocation plus CPA or ROAS is the verdict. CTR and thumbstop rate are secondary [Foxwell, Hott].
- Every ad turned off is one Meta can no longer optimize between [Hott].
- Look for winning themes, not a single winning ad [Loomer].
- Unverified practitioner claim (Pixel Panda via Segwise): fatigue windows have shrunk from 6+ weeks to 2 to 3 weeks. Treat as a hypothesis to watch in the account.

## 3. Targeting and audiences

- For conversion and lead goals, detailed targeting and lookalikes are suggestions only. Hard controls: location, minimum age (up to 25), custom audience exclusions [Loomer].
- Loomer found no evidence that suggestions meaningfully affect delivery. In a 30-day test, Advantage+ Audience produced more registrations than lookalikes (statistically significant) and than detailed targeting (not significant).
- Do not build separate ad sets per interest or lookalike; they mostly reach the same people and differences are usually noise.
- Retargeting happens automatically. Audience Segment breakdowns show about 20 to 25% of a broad Sales campaign's budget going to engaged users and existing customers (range 10 to 40%). A separate remarketing campaign usually reaches them twice [Loomer].
- Define Audience Segments properly: Engaged Audience broadly, Existing Customers precisely.
- Use value rules instead of restrictions. Loomer's lead-gen example: bidding 90% less on 65+ and 20% less on 55 to 64 cut 65+ spend from 45% to under 2% without excluding anyone.

## 4. Tracking and measurement

- **Signal quality is table stakes.** Conversions API required; target Event Match Quality 7+ out of 10 [CTC]. Pixel-only misses conversions to ad blockers, cookie limits and cross-device journeys.
- **Attribution changes (2026):** 7-day and 28-day view windows removed from the Ads Insights API in January 2026. From March 2026 click-through counts link clicks only; likes, shares and saves moved to "engage-through" (1-day). Default is now 7-day click, 1-day engage-through, 1-day view. Reported click conversions dropped with no real change in performance, so baseline from mid-March 2026.
- **How much to trust Meta's numbers:**
  - Haus: 7-day click under-reports DTC results by about 15% on average ($100 attributed ≈ $115 incremental).
  - CTC: acquisition median iROAS 1.14 across 45 stores (7-day click slightly conservative); non-acquisition median iROAS only 0.60 across 20 stores.
  - Haus: prospecting is incremental, 19% average lift to the primary KPI across 640 tests.
  - Loomer: Meta does not "make up numbers"; inflated results usually come from event setup, deduplication or repeat conversions. View-through is the flimsiest evidence. Use Breakdown by Attribution Settings and Compare Attribution Settings.
- **Incremental Attribution setting (disputed):** Haus's July 2026 re-analysis found it now beats standard attribution (pooled 1.26x iROAS vs 0.80x the prior year). Loomer remains skeptical after worse costs in his tests. Test it in the account.
- **Incrementality testing:** Haus experiments averaged about 18.6 days; 96% of account-wide tests detected significant lift by the midpoint. Geo holdouts are the practical method without user-level data.

## 5. Budgeting, bidding and scaling

- **Budget to the learning phase.** Expected CPA of $50 means about $2,500/week (about $350/day) for one ad set to reach 50 events. If unaffordable, simplify or move to a cheaper event. For expensive products you may never exit learning, which does not rule out good results [Loomer].
- **Bidding (disputed):**
  - CTC: inflated budgets with cost controls (minimum ROAS or cost caps), so the system spends more on cheap days.
  - Hott: cost caps as a control knob, set high enough to spend, then dial down.
  - Loomer: aggressive Cost Per Result Goal, Bid Cap or ROAS Goal can starve delivery because they remove the requirement to spend the full budget.
  - Synthesis: start on highest volume (lowest cost). Add caps or minimum ROAS once true unit economics are known, set near current CPA, not ideal CPA.
- **Scaling:** scale only once profitable, increase gradually and expect ROAS to fall as spend reaches broader audiences [Heath]. Low-risk method: an automated rule raising budget about 1% nightly while performance stays in range [Loomer].
- **Pacing:** daily spend can run up to 75% over budget on a given day within a weekly cap of 7x the daily budget [Hott, Loomer]. Judge weekly, not daily.

## 6. Optimization events and funnel

- The algorithm is literal: optimize for clicks and you get cheap, low-quality clicks [Loomer].
- Use the Sales objective even for website lead events; it unlocks Audience Segment reporting [Loomer].
- **Lead quality:** send CRM stages back through CAPI and use the Conversion Leads goal. Commonly cited eligibility: about 200 leads/month, daily CRM uploads, Meta lead ID stored per record, target stage reached by 1 to 40% of leads within 28 days. Below that, use Higher Intent forms, qualifying questions and value rules. Respond within minutes; speed-to-lead affects both conversion and the signal Meta learns from.
- **Offer and landing page first.** Heath's framework starts with the offer. Hott attributes overnight ROAS swings to site changes and stockouts. Ad-to-landing-page mismatch is a costly, common mistake (Hostfully). When results are poor, check ads, offer and landing page before touching structure.

## 7. Common mistakes

1. Fragmenting budget across campaigns or ad sets that never reach about 50 conversions a week.
2. Restricting age, gender or interests on assumption rather than data.
3. Near-duplicate ads passed off as diversity.
4. Optimizing for cheap proxy events (clicks, raw form fills) when buyers are needed.
5. Separate retargeting campaigns that double-reach people and look good mainly through view-through.
6. Killing ads or trimming placements on small samples or backward-looking ROAS (CTC's "breakdown effect").
7. Trusting the Results column without checking attribution mix, CAPI deduplication and incrementality.
8. Bid caps set too tight, starving delivery.

## 8. Where experts disagree (quick reference)

| Question | Position A | Position B | Default for a new account |
|---|---|---|---|
| CBO vs ABO | ABO forced spend: clean reads, funds losers | CBO: ads earn spend (Hott, most advanced teams) | CBO, with occasional ABO for big new ideas |
| Exclude past customers from acquisition | Yes, retention is far less incremental (CTC) | Only when there is a proven problem (Loomer) | Exclude when a clean customer list exists and retention is run separately; otherwise define Existing Customers and monitor |
| Bid controls | Inflated budget + cost controls (CTC, Hott) | Can starve delivery (Loomer) | Lowest cost first, caps once economics are known |
| Creative volume | Volume finds winners (Motion) | Volume trap, diversity matters (Foxwell, Loomer) | Scale with spend, count distinct concepts |
| Incremental Attribution | Now beats standard (Haus 2026) | Worse costs, no clear gain (Loomer) | Test it, do not default |
| Breadth on tiny budgets | Go broad (Loomer) | Concentrate geography (Brandlocker) | Broad within the real buying market; narrow only if budget is very small |
