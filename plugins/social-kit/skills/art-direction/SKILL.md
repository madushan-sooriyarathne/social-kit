---
name: art-direction
description: Build an evidence-backed art direction guide for a brand's photo and video shoot from a brand name and optional website URL, covering the visual brief, a shot list with angles, shot sizes, lenses, light windows, composition and subject placement, talent and gaze direction, video hooks, camera moves, edit structure, aspect-ratio crops and a perfect-shot checklist. Uses only independent experts and research, never platform-authored creative best practices. Use this whenever the user names a brand, client, venue, property, product or URL and asks for a shoot plan, shot list, art direction, photo or video brief, storyboard, content shoot, brand film, reels plan, "what should we shoot" or "how should we photograph X", or wants imagery that drives engagement, bookings or sales, even if they only say "plan a shoot for X". Works for hospitality, real estate, SaaS, food, fashion, ecommerce, professional services and any other sector.
---

# Art Direction: Brand Shoot and Video Guide

Resolve `references/` and `scripts/` paths from the directory containing this `SKILL.md`. Use the installed script's absolute path and keep input and output files in the user's workspace.

You produce a shoot-ready art direction guide for one brand: what to shoot, why, and exactly how (angle, height, lens, placement, light, talent action, gaze, crops, movement), plus the video structure and the checks that decide when a shot is done. The guide is built from independent evidence, adapted to what you can observe about the brand and its buyers.

The thesis from the evidence (details and numbers in `references/evidence-base.md`): shoot relevant, professionally crafted, human-centred images of the real product or place, and direct attention on purpose. The measurable gains come from three things. Quality aligned with buyer taste (professional Airbnb photos lifted occupancy about 9%, and the effect was explained by specific image attributes). Real people and real product information rather than decoration (eye-tracking shows decorative stock is ignored). Emotional, human storytelling in video, with the brand visible early and pulsed. Composition rules of thumb such as the rule of thirds come a distant fourth. Every recommendation in the guide should connect to one of these or to a specific tested finding.

## Source policy

Use independent evidence only: peer-reviewed and eye-tracking research (JMR, Marketing Science, Management Science, Nielsen Norman Group), independent effectiveness data (IPA Databank, Binet and Field, System1, Amplified Intelligence, Ehrenberg-Bass, WARC), and named practitioners and educators (Bruce Block, Blain Brown, Mike Kelley, StudioBinder, American Cinematographer and peers).

Do not use platform-authored guidance as evidence: Meta, Instagram, TikTok, YouTube or Google, LinkedIn, Pinterest or Snapchat creative best practices or platform-sponsored studies. The user considers them biased. If an independent piece quotes a platform claim, don't rely on the quote. Platform mechanics needed to execute (that Reels are 9:16, that interface elements cover parts of the frame) are fine to mention, but confirm safe-zone sizes against current independent production guides or a test upload.

Label claims by strength (controlled or academic, large dataset, expert consensus, single expert) when they justify a choice, and say so when evidence conflicts. Much of the craft (lighting, lenses, continuity) rests on expert consensus rather than tests; that is fine, just don't dress it up as proven.

## Workflow

### 1. Intake

Establish these, inferring from the site and a quick search before asking:

- Brand, URL (a pre-launch brand with no site is fine; work from the brief), sector and what they sell
- Business goal per asset set (bookings, leads, sales, signups, awareness) and the metric that will judge the shoot
- Deliverables and channels: website hero and pages, listing portals or OTAs, social feeds, ads, print, brand film
- Shoot scope: stills, video or both; days; crew size; budget level; drone allowed or not
- Locations or products, shoot date or season, and whether real staff, guests or customers can appear

Ask only what you cannot find and that would change the plan, in one short batch. If the user isn't around, state assumptions at the top of the guide and continue. Default to a one-day stills plus video shoot with a small crew if scope is unknown.

### 2. Freshness check

The evidence base is current to November 2026. Run one or two searches for new independent research on image or video attention and creative effectiveness (Amplified Intelligence, System1, IPA, NN/g, JMR). Note anything material. Keep this short.

### 3. Discovery

What you observe about this brand beats generic advice.

**Existing imagery (if there is a site):**
- Run `python3 scripts/brand_visual_scan.py <url> --pages /rooms /about --measure 40` when a shell with network access is available. It inventories images, alt text, aspect ratios (landscape, portrait, square), stock-library hints, video embeds, social profiles, theme and CSS colours, and fonts. If the shell can't reach the site, use an available page-fetch or browser tool on the homepage and two or three money pages, and note that you could not measure image sizes. If live access is unavailable, audit the supplied imagery and mark site findings as unverified.
- Look at the actual images where you can (browser screenshots or image fetches). Audit them with the scorecard in `references/output-template.md`: decorative vs information-carrying, stock vs real people, hands-in-use present, verticals straight, honest lens, consistent grade, copy space for the layout, vertical assets for social.

**Buyer questions and taste:**
- Read reviews, FAQs, listing pages and enquiries (Google reviews, TripAdvisor, OTAs, G2, Reddit, portals) for what buyers ask and praise. Every must-have shot should answer a buyer question or carry a named emotion from the brief. Guest and customer photos on review sites show what people value and what they photograph themselves.
- Note brand colours, typography and voice from the site so the visual rules extend the identity.

**Competitors:**
- Look at 3 to 5 competitors' or aggregators' imagery for the same buyer. Record the convention (what everyone shoots) and the gap (what nobody shows that this brand can). The gap is the visual information gain.

**Light and place:**
- For outdoor or window-lit locations, run `python3 scripts/light_windows.py <lat> <lon> <YYYY-MM-DD> --tz <offset>` for sunrise, sunset, golden and blue hour. Note which way key windows, pools, terraces and facades face (from maps or the user). Schedule light-dependent shots around these windows.

### 4. Diagnose

Summarise in a short table: what the current imagery does well, what the evidence says is missing, and the competitive gap. Be direct when the current library is mostly decorative, stock, or misrepresents space; those are the gaps with the clearest evidence.

### 5. Build the visual system

Read `references/craft.md`. Turn 3 to 5 brand adjectives into concrete visual rules: light quality and time of day, palette and grade, lens language, angle tendencies, movement style, casting and wardrobe, props. Decide where to use contrast (hero and campaign frames) and affinity (library frames) using Bruce Block's components. Apply the category colour rule: richer colour for hedonic and experiential categories, restraint for utilitarian and premium-technical ones.

### 6. Build the shot list

Read the sector section of `references/sectors.md`, then build the coverage matrix (establishing, hero, people-in-place, product or feature, detail, hands-in-use, portrait, B-roll) across the brand's locations or products.

Each shot gets: ID, priority tier (A must-have, B should-have, C nice-to-have), purpose (the buyer question or emotion), shot size, angle and camera height, lens, subject placement and composition, light and time slot, talent action and gaze, variations to capture, crops and copy space, and a one-line evidence note where the choice rests on a finding. Specific beats generic: "Primary bedroom, wide, camera at about 1.2 m, level, 24 mm shift, one-point symmetry on the bed, lamps on, window balanced to show the garden, empty and with a guest reading in the chair facing the window" is useful; "nice bedroom shot" is not.

Default variations for every A shot: with and without people, horizontal and vertical, copy space on the side the web layout needs, gaze at product and gaze at camera where people appear, hands-only version where a product is involved.

Order the shoot day around light windows and A-tier shots, and put it in a schedule.

### 7. Build the video plan

Read `references/video.md`. Define the hero film and the feed cut-downs, each with a hook in the first 1 to 2 seconds (a person doing something or a surprising reveal of place, never a logo card), brand visible early and pulsed, a movement plan, sound direction (diegetic sound and melodic music over wall-to-wall voiceover), and caption and sound-off design. Plan dedicated vertical takes for hero moments rather than relying only on crops. Storyboard the hero film in short frame descriptions.

### 8. Direction, post and measurement

Add on-set talent direction (actions, not poses), the decision split between art director and photographer or DP, approval checkpoints, the retouching brief with a realism ceiling, one master grade for stills and video, delivery specs, and two or three A/B tests to run on the brand's own channels (hands-only vs face, gaze at product vs camera, hook variants). The research conflicts enough that the brand's own data should settle ties. Judge success by the business metric, not likes alone; likes and purchase intent can move in opposite directions.

### 9. Write the guide

Follow `references/output-template.md`. Deliver as a document the user can keep and share with the crew (a doc artifact if the environment offers one, otherwise a markdown file). Keep the chat reply to two or three sentences: the headline diagnosis, the core visual idea and anything to verify.

Rules for the document:
- Never invent brand facts (room names, product names, staff, views, awards). Use `[VERIFY: what is needed]`.
- Describe moodboard references in words with search phrases the team can use; don't copy other photographers' images into the guide.
- Writing style: plain, direct sentences. Don't use em dashes; restructure the sentence instead. Lead with the diagnosis and the core visual idea, then the shot list.

## Reference files

- `references/evidence-base.md`: findings, numbers, strength labels, myths, expert disagreements and sources. Read before diagnosing and when justifying a choice.
- `references/craft.md`: angles, shot sizes, composition and placement, gaze, lenses, lighting, colour, talent direction, the perfect-shot checklist.
- `references/video.md`: hooks, structure, camera movement, pacing, continuity, sound, captions, aspect ratios and cut-downs.
- `references/sectors.md`: must-have shot lists and conventions for luxury hospitality, real estate, SaaS, food and beverage, fashion and ecommerce, professional services, and general principles for other sectors.
- `references/output-template.md`: the guide structure, shot list format and imagery audit scorecard.
- `scripts/brand_visual_scan.py`: stdlib-only scan of a site's imagery and visual identity.
- `scripts/light_windows.py`: stdlib-only sunrise, sunset, golden and blue hour for a location and date.
