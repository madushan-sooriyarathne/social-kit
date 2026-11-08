# Technical Checklist (priority order)

Technical work is a floor, not a growth engine. Fix blockers fully, fix "Poor" scores, then move effort to positioning and authority. Order reflects independent evidence of impact.

## 1. Server-rendered content (highest priority)

AI crawlers (GPTBot, ClaudeBot, PerplexityBot) fetch JavaScript but never run it (Vercel/MERJ). Anything that only appears after client-side rendering is invisible to them.

Check: raw HTML response (curl or view-source, not the browser's DOM) contains the main body text, title, meta description, internal navigation links and JSON-LD. `scripts/site_snapshot.py` reports the visible-text length of the raw HTML and flags pages that look like empty app shells.

Next.js notes: use Server Components, SSG, ISR or SSR for content, metadata (`generateMetadata`) and schema. Avoid fetching CMS content in `useEffect` or client-only data hooks for indexable pages. Hydrating interactive parts on top is fine. With a headless CMS (Sanity, Contentful, Strapi), fetch on the server and render HTML; verify draft/preview mode isn't leaking into production.

Other frameworks: client-rendered SPAs (plain React, Vue, Angular builds) usually fail this check and need SSR or prerendering. WordPress and most classic CMSs pass by default; check that page builders don't lazy-load main text.

## 2. Crawlability and indexation

- robots.txt: not blocking important sections; a deliberate policy for AI search crawlers (OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot, Claude-User) and training crawlers (GPTBot, ClaudeBot, Google-Extended, CCBot). Blocking search crawlers removes the brand from those AI answers; blocking training crawlers is a business choice. Solis's "Accessible" criterion covers this audit.
- XML sitemap present, referenced in robots.txt, listing only canonical, indexable URLs. For headless CMS builds, generate it from the CMS.
- Canonical tags on every page pointing at the preferred URL; no conflicting canonicals across language or parameter variants.
- No orphan pages; no large sets of thin or near-duplicate pages (tag archives, empty filters, auto-generated location pages).
- Correct status codes: real 404s, 301s for moved pages, no soft 404s.
- hreflang if the site targets multiple languages or countries.

## 3. Internal linking and architecture

- Clusters around the topics the brand can own, with links between related pages and from hubs to every money page.
- Important pages within a few clicks of the homepage.
- Descriptive anchor text; Shepard's data linked over-varied anchors with losers, so keep it natural rather than engineered.
- AI fan-out retrieval draws on pages beyond the exact-query top 10, so covering a cluster well matters.

## 4. Structured data, selectively

Prioritise schema that earns a visible feature or clarifies the entity:
- Organization with `sameAs` links to official profiles (all sites)
- LodgingBusiness / Hotel with Offer (hospitality), RealEstateListing or Product/Offer where fitting, LocalBusiness (local), SoftwareApplication (SaaS)
- FAQPage on pages with genuine FAQs (SearchPilot: positive in 67% of tests)
- Review / AggregateRating on product pages with real reviews (SearchPilot: +20%)

Don't expect lifts from Article schema, `dateModified` alone, ratings on local pages, or migrating microdata to JSON-LD (all inconclusive or null in SearchPilot tests).

## 5. Titles, snippets and extractable content

- Titles: brand, primary topic, and location where relevant. Title changes are among the few things with causal test evidence (SearchPilot), so test them where page volume allows.
- Answer-first sections, comparison tables and self-contained passages make content easier for AI retrieval (Solis), but they help only alongside brand trust (Indig).
- Keep key facts (prices, capacity, hours, policies) as text, not inside images.

## 6. Core Web Vitals and UX

- Fix "Poor" LCP and INP, common on heavy client-JS builds and image-heavy hospitality sites (use responsive images, proper sizing, defer non-critical scripts).
- Don't chase perfect scores; 88% of URLs in Ahrefs' analysis lacked enough field data to get a signal at all.
- Avoid intrusive UX linked with losers in Shepard's 2023 study: fixed footer ads, autoplay video ads, push notification prompts, aggressive popups.

## 7. Consistency of brand facts

Name, address, phone, descriptions, prices and policies should match across the site, Business Profile, directories, OTAs or portals, and social profiles. Inconsistency confuses entity understanding in search and AI answers (Solis's "Consistent/Recognizable").
