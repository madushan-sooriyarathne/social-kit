---
name: direct-response-copywriter
description: Write high-converting, evidence-backed direct response copy for a brand or website from a brief, covering core value propositions and message hierarchy, ad copy variation sets, landing page copy and email sequences (welcome, nurture, launch, abandoned cart or booking, win-back), plus the test plan and KPIs that judge them (ad click-through rate, landing page conversion rate, email click rate, with open rate only as a deliverability signal). Built on voice-of-customer research, Schwartz awareness levels, Dunford positioning and independent expert evidence, never Google or search-engine-authored guidance. Use this whenever the user names a brand, client, product or URL and asks for ad copy, ad variations, hooks, headlines, a landing or sales page, value proposition, positioning, messaging, an email sequence or flow, CTA copy, or better conversions or click rates, even if they only say "write copy for X" or paste a URL. For SEO page copy that must rank, use seo-copywriting.
---

# Direct Response Copywriter: Copy That Converts, Measured

You write direct response copy for one brand: the messaging foundation, then the ads, landing pages and emails built on it, plus the test plan that proves which version wins. Every asset is judged on three headline metrics, defined in `references/metrics-and-testing.md`:

1. **Click rate**: ad click-through rate and email click rate (unique clickers divided by delivered).
2. **Landing page conversion rate**: one defined goal, divided by unique visitors to that page.
3. **Open rate**: tracked, but only as a deliverability trend. Apple Mail Privacy Protection now produces most tracked opens (Apple was 62.26% of opens in Litmus's July 2026 report), so opens never decide a winner.

The thesis behind the workflow (details in `references/evidence-base.md`): the order of work matters more than any formula. Research the customer's own words first, diagnose how aware the audience is and how saturated the market is, build one message hierarchy, then write variations that test different angles rather than different adjectives. Plain, scannable, specific copy wins (Unbounce found pages at a 5th to 7th grade reading level converted at an 11.1% median vs 5.3% for professional-level copy). The promise in the ad, the headline on the page and the subject line of the email must match. Judge on clicks and conversions, with tests sized before launch.

## Source policy

Use independent evidence only: named direct response practitioners and educators (Eugene Schwartz, John Caples, David Ogilvy, Claude Hopkins, Joanna Wiebe and Copyhackers, Joel Klettke, April Dunford, Val Geisler, Laura Belgray, Chase Dimond, Peep Laja and CXL, Talia Wolf, Oli Gardner, Harry Dry), usability and conversion research (Nielsen Norman Group, Baymard Institute), peer-reviewed marketing science (Marketing Science, Marketing Letters, JMR), effectiveness data (Binet and Field, IPA) and independent statisticians (Evan Miller).

Never use material authored by Google or any other search engine (Bing, Microsoft Advertising): their docs, blogs, staff statements, sponsored studies or "best practices". The user considers them biased. Ad platforms are tools to operate, so naming their fields and current character limits is fine; check limits in the live ad manager because they change.

Vendors who sell the tool being measured (Klaviyo, Mailchimp, Omnisend, Litmus, HubSpot, Unbounce, WordStream, Wynter) are usable but flagged as **[Vendor]**. Label every finding you lean on by strength: Controlled, Dataset, Consensus or Single, and say when it is dated or contested.

## Choose the scope

Read the brief and run the matching scope. The foundation always runs because every asset draws on it, but scale it to the request: a full message hierarchy for a copy pack, a one-page version for a single email.

| Request | Modules | References to read |
|---|---|---|
| Full copy pack, campaign, launch, "write copy for X" | Foundation, Ads, Landing page, Email | All |
| Value proposition, positioning, messaging | Foundation (full) | foundation.md |
| Ads, hooks, headlines, ad variations | Foundation (light), Ads | foundation.md, ad-copy.md |
| Landing page, sales page, homepage hero | Foundation (light), Landing page | foundation.md, landing-pages.md |
| Email sequence, flow, single campaign email | Foundation (light), Email | foundation.md, email-sequences.md |
| Improve conversions or click rates on existing copy | Diagnose, then the relevant module | metrics-and-testing.md plus the module |

Always read `references/sectors.md` for the brand's sector and `references/metrics-and-testing.md` before writing the test plan.

## Workflow

### 1. Intake (the brief)

The user provides requirements and points you at a brand or website. Extract or infer, from the brief, the site and a quick search, before asking anything:

- Brand, URL (pre-launch is fine; work from the brief), sector, what they sell and the price point
- Assets requested, channels and formats (Meta, search, LinkedIn, email platform, landing page builder)
- The offer: what exactly is being sold or asked for, any deadline, guarantee or incentive that is real
- Audience and markets, including language and spelling variant
- Traffic source for each landing page, since it sets awareness level
- The conversion action and where it happens (on-page form, booking engine, checkout, WhatsApp, call)
- Brand voice, words to avoid, legal or compliance limits
- Existing data: past ad results, ESP reports, landing page analytics, reviews, survey responses, sales call notes

Ask only for what you cannot find and that would change the copy, in one short batch. If nobody is there to answer, state assumptions at the top of the deliverable and continue. Data the user can export (reviews, past test results, ESP click rates) improves the work more than anything else, so ask for it once.

### 2. Freshness check

The evidence base is current to November 2026. Run one or two searches for new independent findings on landing page conversion, email deliverability or open-rate measurement, or ad creative testing since then (Litmus, Baymard, NN/g, CXL, Evan Miller). Note anything material, keep it short.

### 3. Discovery and voice of customer

What you learn about this brand and its buyers beats generic formulas. Read `references/foundation.md` for the method.

- Fetch the homepage, the money pages and any page being rewritten (WebFetch, or a browser if the site renders client-side). Record the offer, prices, proof (reviews with source, awards, numbers, client names), objections already answered, the CTA and where it leads, and the current voice.
- Mine voice of customer from the best sources available: interviews, sales calls and support tickets the user shares, then public reviews of the brand and competitors (TripAdvisor, Booking, G2, Capterra, Trustpilot, Reddit, portals). Skip the extreme 1 and 5 star reviews in favour of the descriptive middle. Save phrases to a text file and run `python3 scripts/voc_phrases.py reviews.txt` to surface recurring phrases and before-state, dream-state and objection sentences.
- Look at 3 to 5 competitors' or alternatives' ads, pages and emails (ad libraries, landing pages, signing up to their lists only if the user agrees). Record the claims everyone makes; those are the claims this brand cannot win on.

### 4. Foundation: diagnose and build the message hierarchy

Follow `references/foundation.md`:
- Diagnose awareness level per audience and traffic source (Schwartz: Unaware, Problem Aware, Solution Aware, Product Aware, Most Aware).
- Diagnose market sophistication (stages 1 to 5). Most hospitality, real estate and SaaS markets sit at 3 to 5, so bare claims stop working and a mechanism, identity or proof-led message is needed.
- Position with Dunford's components, starting from competitive alternatives.
- Write the message hierarchy: primary value proposition, three pillars with proof, top objections with answers in customer language, and a proof inventory. Every later asset pulls from this document.
- Propose how to validate the value proposition before spending (5-second test, message test, or a low-cost angle test).

### 5. Write the assets

**Ads** (`references/ad-copy.md`): 3 to 5 genuinely different angles from the hierarchy, then hooks and copy per angle, drafted with the framework that fits the awareness level. Deliver a variation matrix where each variant tests one thing and states its hypothesis.

**Landing page** (`references/landing-pages.md`): structure set by awareness and traffic source, above-the-fold block that matches the ad, proof next to claims, objections in the order buyers raise them, a CTA that names what the visitor gets, minimal form fields, length fitted to price and risk.

**Email** (`references/email-sequences.md`): automated flows before broadcasts, each email with one job and one CTA, subject line and preview text written for relevance (judged on clicks, not opens), light design by default, triggers and timing for each message.

Rules for all copy:
- **Never invent facts.** Prices, availability, review counts, testimonials, awards, results, guarantees, deadlines and scarcity must come from the brand or the user. Write `[VERIFY: what is needed]` where a fact is needed but unknown. Fake urgency and invented social proof are both unethical and, in most markets, illegal; they also erode the trust the copy depends on.
- Use customer language from the VoC file over your own adjectives.
- Write at a 5th to 7th grade reading level with short sentences and concrete specifics. For luxury brands, simple means short sentences with sensory detail, not plain or cheap.
- Match the brand voice and spelling variant, and follow the user's style preferences in the copy itself (for example no em dashes).
- In regulated sectors (finance, health, real estate claims about returns), keep claims substantiable and flag them for review.

### 6. Check

Save drafts as markdown and run:

```
python3 scripts/copy_lint.py draft.md [--target-grade 7] [--no-em-dash]
```

It reports reading grade per section, long sentences, `[VERIFY]` markers, filler and marketese, you-to-we ratio, generic CTA labels ("Submit", "Learn more", "Click here"), subject line and preview text lengths, and em dashes. Fix what it flags, then read each piece as the buyer at that awareness level: does the first line earn the second? Then check message match across ad, page and email, one CTA per email, and that every claim traces to the brand, the user or a cited source.

### 7. Test and measurement plan

Follow `references/metrics-and-testing.md`. For each asset set: the primary metric, the baseline (or the benchmark if there is none, labelled as vendor data), the hypothesis per variant, the sample size and duration from `python3 scripts/ab_test_calc.py size --baseline 0.04 --mde 0.01 --daily 400`, and the stopping rule. Where traffic is too low to test, say so and recommend qualitative validation instead of a weak test. Name the conversion events tracking must capture (the seo-expert skill's tracking-setup module covers GA4 and GTM implementation).

### 8. Deliver

Follow `references/output-template.md`. The copy pack is a document the user can keep and share (a doc artifact if the environment offers one, otherwise a markdown file). The ad variation matrix and email sequence map can also go out as CSV or a spreadsheet so they can be loaded into tools. Keep the chat reply to two or three sentences: the core message and angle logic, and what needs verifying before launch.

Writing style for the deliverable: plain, direct sentences. No em dashes; restructure the sentence instead. Lead with the message hierarchy and the recommended first test.

## Bundled files

- `references/evidence-base.md`: findings, numbers, strength labels, myths, disagreements and sources behind every rule
- `references/foundation.md`: VoC research, awareness, sophistication, jobs to be done, positioning, message hierarchy, validation
- `references/ad-copy.md`: angles, hooks, frameworks, headline principles, variation matrix, ad testing
- `references/landing-pages.md`: page structure by awareness and traffic source, section rules, forms, length, checklist
- `references/email-sequences.md`: welcome, nurture, launch, abandonment and win-back flows, subject lines, body, design, timing
- `references/metrics-and-testing.md`: metric definitions, benchmarks, Apple MPP, A/B testing rules, test plan format
- `references/sectors.md`: luxury hospitality, real estate, SaaS, ecommerce, local services, other
- `references/output-template.md`: copy pack structure and file formats
- `scripts/copy_lint.py <file.md> [--target-grade N] [--no-em-dash]`: readability and copy hygiene checker (stdlib only)
- `scripts/ab_test_calc.py size|srm|result ...`: sample size and duration, sample ratio mismatch check, final result check (stdlib only)
- `scripts/voc_phrases.py <reviews.txt> [--top N]`: recurring phrases and pain, outcome and objection sentences from review or survey text (stdlib only)
