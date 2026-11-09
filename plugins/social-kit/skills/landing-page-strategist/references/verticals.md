# Vertical Playbooks

Defaults only. Discovery decides: the buyer questions in reviews and enquiries and the competitive gap override anything here. Vertical-specific evidence is mostly practitioner experience (Weak); the general evidence in evidence-base.md still applies.

## Luxury hospitality (villas, boutique hotels, resorts)

**Goal:** direct enquiries and bookings that would otherwise go through OTAs.

**Traffic and awareness:** branded search and returning guests (most aware), Meta and Instagram prospecting (problem aware, emotional), destination searches (solution aware). Usually Tier 2 or 3 traffic.

**Page sections, typical order:**
1. Hero: the property and its defining feature (pool, view, privacy) with location and travel time; CTA "Check availability" plus WhatsApp
2. Rates from, inclusions, minimum stay, seasonality as text
3. Rooms or layout with capacity and bed types
4. Real photography that answers "what will my stay feel like" (route gaps to art-direction)
5. Location with minutes to beach, town, airport
6. Reviews with platform and count
7. Direct-booking benefits stated honestly (rate, flexibility, a perk) `[VERIFY]`
8. Policies: check-in, children, cancellation
9. FAQ and closing CTA

**Form:** dates and guests first (qualifies and feels low-commitment), then name, email, optional phone with a WhatsApp reason, optional message. Prefill WhatsApp with the page and dates.

**Key events:** `check_availability`, `generate_lead` (enquiry), `click_whatsapp`, `begin_checkout`, `purchase` with `transaction_id` when a booking engine exists. The booking engine is often cross-domain or an iframe; tracking.md section 6 decides whether bookings are attributed at all.

**North star:** direct booking share vs OTA, enquiry-to-booking rate.

## Real estate (agencies, developers, agents)

**Goal:** qualified enquiries and viewing requests.

**Page sections:**
1. Hero: property or project type, location, price or price band, one standout feature; CTA "Book a viewing" or "Get the price list"
2. Key facts block: price, size, bedrooms, bathrooms, tenure, completion date
3. Floor plans and honest photography
4. Location: transport, schools, amenities with distances
5. Developer or agent credibility: completed projects, licences `[VERIFY]`
6. Payment plans, fees and taxes with `[VERIFY]` where unknown
7. FAQ and closing CTA

**Form:** budget and preferred area or unit type first, then contact details. Phone is usually justified here; explain why. Calendar booking for viewings where an agent's diary allows.

**Key events:** `generate_lead` with `lead_type` (enquiry, viewing, brochure), `book_viewing`, `download_brochure`, `click_whatsapp`, `click_phone`.

**North star:** viewing-booked rate and lead-to-viewing rate; cost per qualified lead.

## SaaS

**Goal:** trials, signups or demo requests that become paying customers.

**Traffic and awareness:** category and comparison search (solution and product aware), paid social (problem aware), integration and use-case searches. More likely Tier 1 or 2 on paid traffic.

**Page sections:**
1. Hero: the job done and for whom, in customer language; CTA "Start free trial" or "Book a demo"; product screenshot that shows the outcome
2. Problem in the customer's words (voice of customer)
3. How it works in 3 steps
4. Outcomes with numbers and named customers `[VERIFY]`
5. Integrations, security, pricing pointer
6. Objection FAQ (migration, contract, data)
7. Closing CTA

**Form:** work email only for trial signup where possible; enrich later. Demo forms can justify company size if sales routes by it; test the cost. Message testing panels help when traffic is low (vendor tools, label as such).

**Key events:** `sign_up`, `start_trial`, `book_demo`, `generate_lead`, `view_pricing`. Cross-domain to the app or a separate auth domain is common.

**North star:** trial-to-paid and demo-to-opportunity, measured through the CRM loop.

## Local services and professional services

- Hero states the service, the area served and the fastest contact route.
- Phone and WhatsApp are first-class conversions; calendar booking where appointments exist.
- Proof is local: reviews from the area, named staff, credentials.
- Key events: `generate_lead`, `book_appointment`, `click_phone`, `click_whatsapp`, `click_directions`.

## Ecommerce product or campaign pages

- The goal is usually `add_to_cart` or `purchase`; Baymard's checkout research applies directly.
- Product facts, real photos, reviews with counts, delivery and returns terms near the CTA.
- Higher traffic often makes Tier 1 testing realistic.
