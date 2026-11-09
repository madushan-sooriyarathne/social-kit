# Email Sequences

Goal: automated sequences that earn clicks and conversions, plus campaigns that keep the list warm. Judge every email on click rate and conversions; opens are only a deliverability trend because of Apple Mail Privacy Protection.

## Contents
1. Priorities
2. Sequence designs
3. Subject lines and preview text
4. Body copy and CTA
5. Design
6. Personalization
7. Timing and triggers
8. Compliance basics
9. Output

## 1. Priorities

Build triggered flows before broadcast campaigns. Klaviyo 2026 [Vendor]: flows averaged 5.58% click rate and 2.11% placed order rate vs 1.69% and 0.16% for campaigns. Flows win partly because they fire on intent, so the trigger matters as much as the copy. Order of build for most brands: abandonment (cart, booking, browse), welcome, post-purchase or pre-arrival, nurture, win-back.

## 2. Sequence designs

### Welcome or onboarding (Val Geisler's Dinner Party Strategy, Single)
1. **Welcome:** a personal note, ideally from a founder or host, setting expectations. Avoid "Welcome to [brand]" as a subject line.
2. **Appetizer:** quick value or a story that shows what the brand believes.
3. **Main course:** the core product or experience and the one action that matters.
4. **Sides:** supporting features, social proof.
5. **Dessert:** a real bonus or offer.
6. **Invite back:** next step, or ask them to self-segment by clicking (dates, interests, plan type).
Widen the gaps as the sequence goes on. Klaviyo 2026 [Vendor]: welcome series 6.5% average click rate (top 10%: 13.3%).

### Abandoned cart, booking or browse
- Klaviyo 2026 [Vendor]: abandoned cart is the highest revenue per recipient of any flow ($6.77 average, $13.70 top 10%), 6% average click; browse abandonment 5.6% click.
- Common shape (vendor guidance, not test results): reminder after 2 to 4 hours, follow-ups at about 24 and 48 hours.
  1. Reminder: the exact item, dates or listing, one CTA back to it
  2. Objection answer: the most likely reason they left (cost, delivery or arrival details, cancellation, trust), with proof
  3. Last nudge: a real reason to act (actual availability, a genuine deadline or incentive if one exists)
- Write to the real abandonment causes Baymard documents (unexpected costs, slow delivery, trust), not just "you forgot something". Remember 42% were just browsing (Baymard), so keep the tone helpful.
- Hospitality: booking abandonment (dates searched, no booking) needs the dates, room or villa, current availability only if true, and the cancellation policy. Real estate: saved-search and viewed-listing triggers. SaaS: trial milestones and activation steps.

### Nurture
Alternate value and soft offers; each email has one job and one CTA. Draw topics from the VoC objections and dream states. Cadence the list can sustain, consistent over time.

### Launch or sales
Announce, explain the mechanism, proof, objection handling, deadline. Real deadlines are legitimate urgency; invented ones erode trust (Belgray, Dimond, Copyhackers: Consensus).

### Post-purchase or pre-arrival
Confirm, reduce anxiety (what happens next, what to bring, how to get there), invite a review at the right moment, and set up the next purchase or referral.

### Win-back
Lowest earner (Klaviyo 2026: $0.82 average revenue per recipient). Keep it short: remind them of the value, ask for an explicit click to stay subscribed, then suppress non-clickers. Define inactivity by clicks, site visits or purchases, never by opens alone, because MPP generates false opens.

## 3. Subject lines and preview text

- Write for relevance: the specific thing this reader cares about (their dates, their saved listing, their trial step) beats clever wordplay.
- Name personalization is contested: one large field experiment lifted opens 9.05% to 10.80% and leads 31% (Sahni et al. 2018, Controlled); a later study found no first-name effect (Defau and Zauner 2023, Controlled). Personalize on behaviour and context first.
- No reliable length rule (published tests conflict). Keep the key words early because clients truncate.
- Preview text completes or extends the subject line; never leave it to default to "View in browser".
- Write 2 or 3 subject options per important email and judge the test on clicks or conversions, not opens.

## 4. Body copy and CTA

- One job and one primary CTA per email (Consensus).
- Front-load the value; short paragraphs. NN/g reports newsletters are read even more abruptly than web pages.
- CTA as a button and as a text link, labelled with the outcome.
- Sender name a real person where the brand voice allows.
- Reading level at or near grade 7 (run `scripts/copy_lint.py`).

## 5. Design

Default to light design. HubSpot's tests (about 2014, B2B list, [Vendor]) found the simpler email won every time: plain text 42% more clicks than a GIF version, an image-heavy template 51% fewer clicks, simple HTML 30% more clicks than heavy HTML, with equal deliverability. For visual products (villas, fashion, food), test a light template with one strong image against a heavier one rather than assuming either.

## 6. Personalization

Use behaviour and context: what they viewed, dates searched, plan, stage, location, past purchases. Insert names only where it reads naturally. Never imply knowledge the reader didn't knowingly share.

## 7. Timing and triggers

- No universal best send time (vendor studies conflict and MPP hides real open times). Test on the list using clicks.
- For each flow email specify: trigger, delay, exit condition (purchased, booked, replied), and what happens to people who click but don't convert.
- Corporate security scanners can auto-click links; filter clicks that occur seconds after delivery where the ESP allows, especially for B2B lists.

## 8. Compliance basics

Consent for marketing email, a working unsubscribe in every message, a physical address where the law requires it, and honest subject lines. Flag the rules for the brand's markets (for example GDPR and PECR for UK and EU recipients, CAN-SPAM for the US, Sri Lanka's Personal Data Protection Act) for the user to confirm; this is not legal advice.

## 9. Output

Sequence map (also exportable as CSV):

| Flow | # | Trigger and delay | Exit condition | Job of this email | Subject options | Preview text | CTA and destination | Primary metric |
|---|---|---|---|---|---|---|---|---|

Then the full copy of each email: sender name, subject options, preview text, body, CTA, and a `[VERIFY]` list.
