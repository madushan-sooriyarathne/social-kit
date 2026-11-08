# Evidence Base (independent sources only, current to November 2026)

Every recommendation in a strategy should trace back to something here or to a newer independent finding you found in the freshness check. Strength labels: **Strong** = controlled tests or court testimony; **Moderate** = large correlational datasets or consistent findings across several independent analysts; **Weak** = small samples, surveys, vendor marketing data, or secondhand reports.

## Contents
1. What predicts organic winners
2. Ranking factors table
3. Core updates 2023 to 2026
4. Content strategy findings
5. Technical findings
6. Links, digital PR and brand mentions
7. AI search and zero-click
8. Measurement
9. Myths and wasted effort
10. Expert disagreements and caveats
11. Source list

## 1. What predicts organic winners

Cyrus Shepard, Zyppy Signal, April 9, 2026 (400+ winning and losing sites, hand-classified, Spearman correlation). **Moderate.**

| Trait | Correlation with winning |
|---|---|
| Offers a product or service | 0.391 |
| Allows task completion on-site | 0.381 |
| Owns proprietary assets | 0.357 |
| Tight topical focus | 0.250 |
| Strong brand (branded navigational demand) | 0.206 |

- Sites with none of the traits won 13.5% of the time; four traits 68.1%; all five 69.7%.
- 92.9% of winners had proprietary assets vs 57.1% of losers.
- 32.6% of winners had strong branded demand vs 16.1% of losers.
- Tight focus predicted winning (75.9% vs 61.3%); broad "topical focus" did not.
- "First-hand experience" and "uniqueness" did not separate winners from losers; Shepard thinks they're baseline requirements.
- Shepard's advice: "own the next step of the user journey" with tools, calculators, booking, searchable databases.

## 2. Ranking factors table

| Factor | Evidence | Strength |
|---|---|---|
| Business model, proprietary assets, task completion | Shepard 2026 (above); consistent with core update winner/loser patterns | Moderate |
| Brand demand | Shepard 2026; leaked Content Warehouse docs reference site-level authority (analysis: Mike King/iPullRank, Rand Fishkin/SparkToro) | Moderate |
| Click and engagement signals | US v. Google testimony confirmed NavBoost, a click-based re-ranking system. King reports the leak names NavBoost 84 times across five modules; analyses describe goodClicks, badClicks, lastLongestClicks | Strong that clicks are used; weak on how to "optimise" them |
| Titles and snippets | SearchPilot split tests: capitalising parts of title tags positive in half of tests, never negative (one +17.5%); moving location to the start of the title helped a local healthcare site | Strong but site-specific |
| Links | Still in the system (PageRank-type attributes in the leak). For AI visibility backlinks correlate only 0.218 (Ahrefs, 75,000 brands) | Moderate |
| Topical depth | Shepard (tight focus wins). Indig/Semrush, 50,000+ brands in ChatGPT, Jan to Jun 2026: clear topic owners kept their position about 90% of the time month to month; only about 15% of categories had a clear owner | Moderate |
| Core Web Vitals | Backlinko (208K pages): weak or no correlation with engagement. 88% of 42M URLs Ahrefs analysed lacked enough field data to get a ranking signal at all | Weak as a ranking lever; matters for conversions |

Implication: on-page optimisation works at the margin; the big swings are decided at the site and brand level.

## 3. Core updates 2023 to 2026

- **September 2023 Helpful Content Update:** Lily Ray found 129 of 130 heavily hit sites had only declined further a year later. Glenn Gabe tracked 380+ affected sites; only 47 surged in the August 2024 update. The first broad rebound came in the June 2025 core update, nearly two years later, and many recovering sites hadn't made meaningful changes. HouseFresh's full recovery (October 2025) is the exception people cite.
- **June 2025:** Ray's SISTRIX analysis of 1,000 winners and losers: hobbyist and reference sites, YouTube and Wikipedia up; big marketplaces down (Amazon the biggest loser).
- **December 2025 (Dec 11 to 29):** Ray: ecommerce and retail brands won (Apparel +19%, Retailers +14%, Finance +15%); UGC, Q&A, news and major health publishers lost. Hotel and travel showed a split. Gabe documented heavy YMYL volatility.
- **March 2026 (Mar 27 to Apr 8, after a short spam update):** Ray called it a first-party, official-source correction. Losers included YouTube, Reddit, Tripadvisor, Yelp, Expedia, Travelocity, Realtor.com. Her travel headline: brand sites win. Aleyda Solis described a shift from intermediaries and aggregators toward destination brands and institutional sources.
- **May 2026:** Gabe reported it was heavier than March across verticals (secondhand). **Weak.**

Recovery lessons (Gabe, Ray, Shepard): wait for rollout to finish before diagnosing; recovery usually needs another broad core update, so months not weeks; "quality" includes UX and ads (Shepard's 2023 50-site study linked fixed footer and video ads with losers; no winners used push notifications); rebuilding the business model beats rewriting articles.

## 4. Content strategy findings

- Pick topics where the brand can complete the task or offer proprietary information (availability, pricing, floor plans, first-party photos, local knowledge, product data).
- Depth beats breadth. Indig's ChatGPT data: breadth isn't penalised when each topic has real depth, and in finance and real estate breadth was rewarded. Shallow presence is what fails.
- Proprietary data is the most reusable asset: it feeds rankings, digital PR links and AI citations at once.
- E-E-A-T in practice (Ray, Shepard): an outcome of being a real, known entity, not author boxes.
- AI-assisted content is not the problem; unedited, mass-produced pages with no added value are. Ray predicted 2026 enforcement against scaled AI content and the March 2026 spam update followed.
- Ray (2026): AI Overviews cut citations of self-ranking listicles by 38%. Self-serving "best X" lists on your own site are fading.

## 5. Technical findings

- **AI crawlers don't execute JavaScript** (Vercel/MERJ, December 2024). GPTBot made 569M fetches in a month, ClaudeBot 370M; they downloaded JS files (11.5% and 23.84% of requests) but never ran them. Client-side-only content is invisible to them. **Strong.**
- **Schema (SearchPilot controlled tests):** FAQ schema positive in 67% of tests (+4 to 15%, one +25%). Review schema +20% on product pages; adding price schema to it was inconclusive. Article schema inconclusive twice. `dateModified` alone inconclusive. Ratings schema on local pages inconclusive. Microdata to JSON-LD migration: no measurable impact. **Strong, site-specific.**
- **AI Overview citations and rankings:** Ahrefs (March 2026) found only 38% of AI Overview citations come from the top 10 for the exact query (down from 76% in July 2025), so ranking across a whole topic cluster matters. Contested; see caveats.
- **Core Web Vitals:** a floor. Fix "Poor" scores, then stop.
- Solis's AI search criteria: Accessible (audit crawl blocks for search and AI crawlers), Useful (clusters with strong internal linking), Consistent/Recognizable (same brand facts everywhere), retrieval happens at passage or chunk level.

## 6. Links, digital PR and brand mentions

- Ahrefs (75,000 brands, Spearman): branded web mentions correlate 0.664 with AI Overview visibility; YouTube mentions about 0.737 across ChatGPT, AI Mode and AI Overviews; backlink count 0.218. Top-quartile brands for mentions averaged 169 AI Overview mentions vs 14 for the next tier. **Moderate (correlational, vendor).**
- BuzzStream State of Digital PR 2026 (Vince Nero, Feb 9, 2026): 95.9% pitch data-led content; 85.8% say backlinks are digital PR's most effective outcome; 68.2% say it's more effective than a year earlier; about 80% never buy links (down from 87.3% in 2025). Editorial.link survey of 518 SEOs: 48.6% rate digital PR the most effective link tactic. **Weak (self-reported surveys by vendors).**
- Whitespark 2026: "In AI SEO, mentions (citations) are the new link."
- Paid links and PBNs: consistently associated with spam update hits in Gabe and Ray's analyses; recovery possible but slow.

## 7. AI search and zero-click

- Ahrefs (Ryan Law, Xibeijia Guan, 300,000 keywords): AI Overviews cut position-1 CTR by 34.5% (March 2025 data) and 58% (December 2025 data). Position 2 lost about half its clicks; position 10 nearly 20%. **Moderate.**
- SparkToro: 58.5% of US searches zero-click in 2024 (360 open-web clicks per 1,000 searches); 2026 Similarweb-based follow-up found 68.01% and about 276 per 1,000. Different panels, so not a perfect comparison.
- Bain: B2B software CTR down by as much as 30% in some categories; 85% of B2B buyers purchase from their "day one" list.
- Kevin Indig (70-user think-aloud study, May 2025; 846K-session clickstream, 2026): AI Overviews create a comparison environment where users still click to verify; in AI Mode users accepted product recommendations 88% of the time; brand and authority are the first filter users apply; 91% of citations appear in only one of ChatGPT, Perplexity or AI Overviews.
- Freshness: AirOps/Indig report pages not updated in 3+ months are 3x more likely to lose AI citations. **Weak (secondhand).**
- YouTube is 5.6% of all AI Overview citations (Ahrefs, March 2026).
- Lily Ray published a fabricated article as a test and AI Overviews repeated it as fact within 24 hours. AI answers are volatile and manipulable; don't over-invest in "prompt ranking" hacks.

## 8. Measurement

From Solis (three layers: AI presence, readiness, business impact), Fishkin (zero-click content) and Indig:
- Business outcomes: organic and AI-referred conversions, revenue per visit, assisted conversions, pipeline (SaaS), direct-booking share vs OTA (hospitality), qualified leads (real estate).
- Brand demand: branded search volume and branded clicks as a leading indicator.
- Visibility: impressions and CTR split by branded vs non-branded and by AI Overview presence; third-party visibility indices; AI share of voice and mention accuracy by topic rather than single prompts.
- Topic ownership: share of category prompts that name the brand.
- Report AI impact without overclaiming (Solis). AI referrals often land in "Direct" and are polluted by bots (Indig).

## 9. Myths and wasted effort

- "Technical fixes will recover a core update hit." Shepard (2026): business model, UX or content production is usually what's killing the site.
- "Author boxes and E-E-A-T badges fix quality." Shepard's 2023 study found they don't.
- "Every schema type boosts rankings." SearchPilot's inconclusive results say otherwise.
- "Perfect Core Web Vitals win rankings." Weak evidence.
- Refreshing dates without real updates and over-varying anchor text were linked with losers in Shepard's second 50-site study.
- Self-promotional "best X" listicles and scaled AI pages are being demoted (Ray, 2026).
- Buying clicks to game NavBoost has never been shown to work; King describes a site being de-indexed after a click experiment.
- "Answer-first formatting guarantees AI citations." Indig argues it doesn't work on its own because trust and brand decide.

## 10. Expert disagreements and caveats

- Most evidence is correlational. Only SearchPilot's tests are causal, and they're site-specific (5% A/A false-positive rate).
- Datasets disagree on the same update: SISTRIX UK showed Reddit and Instagram as March 2026 winners while Amsive US showed them as losers. Visibility indices measure rankings, not traffic.
- AI Overview citation overlap with top-10 results is contested: Ahrefs 76% (July 2025) to 38% (March 2026); BrightEdge about 17%; Conductor 43%. One analyst argues an Ahrefs parser change partly explains the trend.
- Niche vs breadth: Shepard favours tight focus for Google; Indig's ChatGPT data says depth matters more than narrowness.
- Size of traffic loss: Shepard notes some studies find overall organic declines probably modest; Indig says organic is down but not all due to AI. Pain concentrates in informational publishers.
- The leak shows which attributes exist, not their weights or production use. King and Fishkin treat it as strong directional evidence; skeptics urge caution.
- Vendor bias: Ahrefs, Semrush, BuzzStream, Cloudbeds, HotelRank and Local Falcon sell tools related to their findings.

## 11. Source list

- Shepard, winning sites study: https://signal.zyppy.com/p/winning-google
- iPullRank leak analysis: https://ipullrank.com/google-algo-leak
- SearchPilot case studies: https://www.searchpilot.com/resources/case-studies/seo-split-test-lessons-adding-faq-schema and https://www.searchpilot.com/resources/case-studies/a-look-back-at-the-most-surprising-tests-of-2025
- Backlinko CWV study: https://backlinko.com/core-web-vitals-study
- Gabe, June 2025 core update: https://www.gsqi.com/marketing-blog/june-2025-google-core-update/
- Amsive (Ray) update analyses: https://www.amsive.com/insights/seo/google-march-2026-core-update-winners-losers-analysis/ and https://www.amsive.com/insights/seo/googles-december-2025-core-update-winners-losers-analysis/
- Solis, AI search winning brands: https://www.aleydasolis.com/en/ai-search/ai-search-winning-brands-characteristics/
- Ahrefs, AI Overviews reduce clicks: https://ahrefs.com/blog/ai-overviews-reduce-clicks/
- Ahrefs, rankings vs AI citations: https://ahrefs.com/blog/search-rankings-ai-citations
- SparkToro zero-click 2024: https://sparktoro.com/blog/2024-zero-click-search-study-for-every-1000-us-google-searches-only-374-clicks-go-to-the-open-web-in-the-eu-its-360/
- Bain, zero-click B2B: https://www.bain.com/insights/losing-control-how-zero-click-search-affects-b2b-marketers-snap-chart/
- Indig, Growth Memo: https://www.growth-memo.com/p/ai-halftime-report-h1-2026 and https://www.growth-memo.com/p/users-behave-differently-in-ai-overviews
- Whitespark Local Search Ranking Factors: https://whitespark.ca/local-search-ranking-factors/
- Local Falcon realtor AI index: https://www.localfalcon.com/research/the-realtor-ai-visibility-index
- HotelRank OTA bias: https://hotelrank.ai/case-studies/ota-bias-gpt5-models
