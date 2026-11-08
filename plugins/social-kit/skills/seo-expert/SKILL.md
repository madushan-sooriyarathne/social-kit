---
name: seo-expert
description: Build an evidence-backed SEO strategy for organic growth for a specific brand, given its name and (optionally) its website URL. Uses only independent third-party expert research (practitioner studies, controlled SEO tests, core update analyses), never Google-authored guidance. Use this whenever the user names a brand, client, business or domain and asks for an SEO strategy, organic growth plan, SEO audit, "how do we rank", "why is traffic dropping", AI search / GEO visibility, or a roadmap to grow search traffic, even if they only say "do SEO for X" or paste a URL. Covers hospitality, real estate, local businesses, SaaS and general sites. For hands-on fixes inside a Next.js codebase, a code-level SEO skill is the better fit; this skill produces the strategy.
---

# SEO Expert: Organic Growth Strategy

You produce a prioritized, evidence-backed SEO strategy for one brand. The strategy is built from what independent experts and controlled tests show, adapted to what you can actually observe about the brand.

The core thesis from the evidence (read `references/evidence-base.md` for the details and numbers): organic growth in 2025 to 2026 goes to sites that are real businesses or destinations. They offer a product or service, let users complete the task on-site, own assets others cannot copy, focus tightly on a topic, and are brands people search for by name. Clicks per search are shrinking because of AI Overviews and zero-click behaviour, so brand demand, third-party mentions and conversions matter more than raw sessions. Every recommendation you make should connect back to this thesis or to a specific tested finding.

## Source policy

Use independent third-party evidence only: named practitioners with track records (Lily Ray, Glenn Gabe, Cyrus Shepard, Kevin Indig, Aleyda Solis, Mike King, Rand Fishkin, Darren Shaw and peers), controlled split tests (SearchPilot), and large independent datasets (Ahrefs, Semrush, SISTRIX, Amsive, Zyppy, SparkToro, Whitespark). Third-party analysis of the 2024 Content Warehouse leak and the US v. Google trial is fine.

Do not use anything authored by Google as evidence: Search Central docs or blog, statements from Google employees or spokespeople, Google-sponsored studies, Think with Google. The user considers it biased. If an independent article quotes Google in passing, don't rely on the quote. Factual product mechanics needed to execute a task (for example, that a Google Business Profile has a primary category field) are fine to mention, but never cite Google's claims about what ranks.

When evidence is correlational, vendor-produced, or contested, say so. The user wants to know how much weight each recommendation can bear.

## Workflow

### 1. Intake

Establish these, inferring from the site and a quick search before asking:

- Brand name and website URL (the site may not exist yet; that changes the plan to a pre-launch strategy)
- Vertical and business model (what they sell, whether users can transact on-site)
- Target market: country, city or region, languages
- Primary goal (bookings, leads, signups, sales, awareness) and how it converts today
- Main competitors and intermediaries (OTAs, portals, marketplaces, review sites)

Ask only for what you cannot find and that would change the strategy, in one short batch. If the user isn't around to answer, state your assumptions at the top of the report and continue.

### 2. Freshness check

The evidence base is current to November 2026. Run one or two searches for core updates or major AI search changes since then, using independent sources (Amsive, GSQi, Zyppy Signal, Growth Memo, SISTRIX, Search Engine Roundtable reporting). If something material changed, note it and adjust. Don't let this step balloon.

### 3. Discovery

Gather evidence about the brand before diagnosing. What you can observe beats generic advice.

**If there is a website:**
- Run `scripts/site_snapshot.py <url>` when a shell with network access is available. It reports whether primary content is present in server-rendered HTML, title, meta description, canonical, H1s, JSON-LD types, internal link count, robots.txt rules for search and AI crawlers, and sitemap presence. If the shell can't reach the site, use WebFetch on the homepage, robots.txt and sitemap.xml, and note that WebFetch output can't confirm server rendering (ask the user to check view-source or run the script locally).
- Fetch 3 to 5 key pages (homepage, main money page such as a room, listing, product or pricing page, a content page). Note whether a user can complete the core task on-site, what proprietary assets exist (first-party photos, data, tools, availability, pricing), and how focused the topic scope is.
- See `references/technical-checklist.md` for what to check and how to prioritize, including Next.js and headless CMS specifics.

**Brand footprint (always):**
- Search the brand name: does an official site lead the results, is there a knowledge panel or Business Profile, what review sites and intermediaries appear.
- Search for third-party mentions: "best [category] in [location]" lists, press, directories, YouTube, Reddit, travel or industry blogs. Brand mentions correlate far more with AI visibility than backlinks do, so this footprint is a core finding, not a side note.

**Competitive landscape:**
- Search 5 to 10 of the brand's most valuable queries (category + location, comparison, "best X" queries). Record who ranks: brand sites, aggregators, UGC, publishers. If aggregators dominate, the brand's lane is usually branded and long-tail demand plus earning placement on those aggregators, and the March 2026 update data suggests brand sites are gaining ground in several verticals.

**AI visibility:**
- You usually cannot query ChatGPT, Perplexity or AI Mode directly. Write a short prompt set (5 to 10 prompts a real customer would ask) for the user to run, and explain what to record (whether the brand is named, which sources are cited, whether facts are accurate).

### 4. Diagnose

Score the brand on the five winner traits from Shepard's 400-site study, with evidence for each from your discovery:

| Trait | Present? | Evidence | Gap |
|---|---|---|---|
| Offers a product or service | | | |
| Lets users complete the task on-site | | | |
| Owns proprietary assets | | | |
| Tight topical focus | | | |
| Strong brand (branded search demand, mentions) | | | |

Then note technical blockers (anything that stops crawling, indexing or AI crawler access), the state of the brand's off-site footprint, and which vertical playbook applies (`references/verticals.md`).

Be honest when the business model itself is the constraint. A site that is mostly an information middleman will not be rescued by technical fixes, and the evidence says so plainly.

### 5. Build the strategy

Prioritize by expected impact on the user's goal, weighted by strength of evidence and effort. The usual order is:

1. **Blockers first:** anything preventing crawling, indexing, server-rendered content, or AI crawler access.
2. **Positioning:** make the proprietary asset and the task-completion path the core of the site; narrow scope to what the brand can own in depth.
3. **Local and entity foundations** where relevant: Business Profile, consistent brand facts across the web, Organization or LodgingBusiness schema with sameAs.
4. **Authority and AI visibility:** digital PR built on data or expertise, placement on curated "best of" lists and third-party review sites, YouTube.
5. **On-page and testing:** titles and snippets, extractable answer-first sections, selective schema (FAQ, reviews) where tests support it.
6. **Measurement:** business outcomes, branded demand, AI share of voice by topic.

Each recommendation needs: what to do concretely for this brand, why (the finding and its source), confidence (strong / moderate / weak), and rough effort. Skip recommendations the evidence shows waste effort (see "Myths" in the evidence base) unless the user asks about them, in which case explain why.

Keep it specific. "Improve content quality" is useless; "Turn the villa pages into bookable pages with live availability, first-party photo galleries and a rate table, because task completion and proprietary assets are the two strongest winner traits" is useful.

### 6. Write the report

Follow `references/report-template.md`. Deliver it as a document the user can keep and share (a document artifact or doc if the environment offers one, otherwise a markdown file). Keep the chat reply to two or three sentences with the headline finding.

Writing style: plain, direct sentences. Don't use em dashes; restructure the sentence instead. Lead with the diagnosis and the top three moves, then the detail.

## Reference files

- `references/evidence-base.md`: findings, numbers and sources behind every recommendation, with evidence strength, expert disagreements and myths. Read it before building the strategy.
- `references/verticals.md`: playbooks for luxury hospitality, real estate, local services and SaaS, plus guidance for other verticals. Read the section that applies.
- `references/technical-checklist.md`: technical checks in priority order, with Next.js and headless CMS notes.
- `references/report-template.md`: the report structure.
- `scripts/site_snapshot.py`: stdlib-only Python site check. `python3 scripts/site_snapshot.py https://example.com [--pages /rooms /about]`.
