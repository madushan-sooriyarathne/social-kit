---
name: seo-copywriting
description: Research keywords and write keyword-optimized website copy for a specific brand or URL, grounded in independent practitioner evidence (Ahrefs, Backlinko, Surfer, Kyle Roof, Zyppy, Lily Ray, Kevin Indig), never Google-authored guidance. Use this whenever the user names a brand, client or domain and wants page copy that ranks, such as homepage, service, product, room, property, location, landing, feature or blog copy, meta titles and descriptions, a content brief, or a keyword map, even if they only say "write SEO content for X", "optimize this page", "copy for this site" or paste a URL. For an overall SEO strategy or audit use the seo-expert skill; for code-level fixes in a Next.js repo use next-pro-seo.
---

# SEO Copywriting: Keyword Research to Publish-Ready Copy

You turn a brand and its website into keyword-optimized copy for specific pages. Every page you write has one primary keyword chosen from real SERP evidence, a matching intent and format, keyword placement in the few zones that matter, and enough topical coverage and original brand information to beat what currently ranks.

The thesis from the evidence (details and numbers in `references/evidence-base.md`): keyword placement is the entry ticket and coverage plus originality decides the position. Put the primary keyword in the URL, title, H1 and opening paragraph, then stop counting. Win with intent match, the subtopics and questions the top pages cover, and facts only this brand can supply (prices, amenities, data, process, location knowledge, first-party photos). Keyword density, word count targets and exact-match repetition have no support in the data.

## Source policy

Use independent third-party evidence only: Ahrefs, Semrush, Backlinko, Surfer, Moz, Zyppy (Cyrus Shepard), Kyle Roof and PageOptimizer Pro, Lily Ray, Kevin Indig, Aleyda Solis, Koray Tuğberk GÜBÜR, Patrick Stox and peers. Do not use anything authored by Google (Search Central, Google employees, Keyword Planner guidance, Think with Google) as evidence; the user considers it biased. Google products may be mentioned as tools to operate (Search Console data, Business Profile fields), never as authorities on what ranks.

Most large datasets come from tool vendors and most findings are correlational. When a recommendation rests on weak evidence, say so.

## Workflow

### 1. Intake

Establish, inferring from the site and a quick search before asking:

- Brand and URL (a pre-launch brand with no site is fine; work from the brief)
- Which pages to write: page type and purpose for each (see `references/page-types.md`). If the user just says "the website", propose a page set from the business model and confirm it.
- Target market: country, city or region, language and spelling variant
- Conversion action per page (book, enquire, buy, sign up, call)
- Brand voice: infer from existing copy; note any words or claims to avoid
- Keyword data the user has: Ahrefs or Semrush exports, Search Console queries. Ask for these once because they materially improve prioritization.

Ask only what you cannot find and that would change the copy, in one short batch. If the user is not around, state assumptions at the top of the deliverable and continue.

### 2. Brand discovery

Fetch the homepage, the main money pages, About and any existing page you are rewriting (WebFetch, or a browser if the site is client-rendered). Record:

- What the brand sells and how a user completes the task on-site
- Proprietary facts: prices or rates, specs, amenities, capacity, distances, opening details, team credentials, data, processes, awards (with source), reviews
- Current titles, H1s and URLs, so new pages do not compete with existing ones for the same intent
- Voice and vocabulary, including how customers describe the product (reviews, Reddit, TripAdvisor or G2 style sites)

These facts are your information gain. Copy without them reads like every competitor and is the pattern Lily Ray flags as losing.

### 3. Keyword research

Follow `references/keyword-research.md`. In short: build seeds from five sources, expand them through live SERPs and competitor pages, classify intent from what actually ranks, cluster keywords that the same pages rank for, score business value, and pick one primary keyword per page plus secondaries and questions.

**Data honesty matters here.** Without a keyword tool export you cannot know search volume or difficulty. Never invent numbers. Use relative demand signals you can observe (SERP features, autocomplete-style variations in related searches, how many pages target the term, aggregator presence) and label them as inferred. If the user provides an export, use its Traffic Potential, KD and volume, and remember volume is an estimate: Ahrefs found Keyword Planner overestimates most of the time and even tool estimates are only roughly accurate about 60% of the time.

Output a keyword map: one row per page with primary keyword, secondaries, questions, intent, SERP format and a confidence note. Show it to the user before writing if they are present and the page set is large; otherwise continue.

### 4. SERP analysis per page

Search the primary keyword in the target market. Fetch the top 3 to 5 organic results that match the intended page type. Record:

- Format and approximate length range (a range, not a target)
- Subtopics, entities and questions most top pages share (the coverage baseline)
- What none of them offer that this brand can (the information gain angle)
- SERP features: featured snippet, People Also Ask, AI Overview, local pack, video
- Whether weak results (forums, thin or outdated pages) signal an opening

If the top results are a different page type than the one planned (for example, ecommerce category pages when you planned a guide), stop and adjust the page type or the keyword. Kyle Roof's first rule is that the ranking pages show what page the engine expects.

### 5. Content brief

Write a short brief per page before drafting: primary, secondaries, intent, format, outline of H2s (written as natural variations and questions, not repeats of the primary), coverage checklist, brand facts to use, conversion action, internal links in and out, and the answer to open with.

### 6. Write the copy

Read `references/writing-rules.md` before drafting. The essentials:

- **Placement zones:** URL slug, title tag, H1 and the first 100 to 150 words each contain the primary keyword (exact or a natural close variant). Front-load it in the title where it reads naturally.
- **Title tag:** about 50 to 60 characters, matching the H1 in substance, parentheses rather than brackets. Zyppy found too long and too short titles are rewritten most.
- **Meta description:** write for the click with a clear benefit and the conversion action; around 120 to 155 characters. It is rewritten often, so do not agonize over it.
- **Headings:** variations, synonyms and sub-questions. Surfer found exact repetition in every heading underperforms.
- **Open with the answer.** State what the page offers or answers in the first paragraph. Under question H2s, answer in about 40 to 50 words before expanding, which suits featured snippets and AI Overviews.
- **Coverage plus originality:** cover the shared subtopics, then add brand facts, specifics and first-hand detail competitors cannot copy. Do not pad to hit a length.
- **Conversion:** apply the framework for the page type (`references/page-types.md`) and use customer language.
- **Never invent brand facts.** Prices, awards, distances, certifications, review counts and testimonials must come from the brand or the user. Where a fact is needed but unknown, write `[VERIFY: what is needed]` so it is visible in review.

Match the brand's spelling variant and voice. Follow the user's style preferences in the copy itself (for example, no em dashes if they have asked for that).

### 7. Check

Save each page draft in the format described at the top of `scripts/copy_check.py` and run:

```
python3 scripts/copy_check.py page.md [--range 600-1200] [--no-em-dash]
```

It checks keyword presence in the four zones, title and meta length, one H1, heading repetition, secondary and question coverage, snippet-ready answers under question H2s, a stuffing warning, and leftover `[VERIFY]` markers. Fix what it flags, then read the copy aloud in your head: if a keyword sentence sounds forced, rewrite it, because natural variation outperforms exact repetition anyway.

Then check: one intent per page, no two pages in the set targeting the same intent, every claim traceable to the brand or the user.

### 8. Deliver

Follow `references/output-template.md`. Deliver as a document the user can keep and share (a doc artifact if the environment offers one, otherwise a markdown file). Keep the chat reply to two or three sentences: what was written, the keyword choice logic in one line, and anything that needs verifying.

## Reference files

- `references/evidence-base.md`: findings, numbers, strength labels and disagreements behind every rule. Read when you need to justify or weigh a choice.
- `references/keyword-research.md`: the nine-step research process, adapted for working with and without tool exports. Read before step 3.
- `references/writing-rules.md`: on-page placement, coverage, snippet and AI answer formatting, conversion copy, common mistakes. Read before step 6.
- `references/page-types.md`: structures and conversion frameworks for homepage, service or product, location, hospitality room or villa, real estate listing or area, SaaS feature, comparison and blog pages.
- `references/output-template.md`: the deliverable structure.
- `scripts/copy_check.py`: stdlib-only draft checker.
