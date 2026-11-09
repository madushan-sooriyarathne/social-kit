# Tracking Integration

Goal: a lead count the business can trust and connect to revenue. Most lead-gen programs fail quietly here, through duplicate events, DOM triggers that broke on a redesign, consent gaps and no link to CRM outcomes. Event names match the seo-expert skill so one brand keeps one tracking system. Confirm GA4 and GTM menu paths in the live product; they change.

## Contents
1. Measurement plan
2. Event dictionary
3. dataLayer spec
4. Deduplication
5. Consent
6. Cross-domain and booking engines
7. Click IDs, UTMs and the CRM loop
8. Server-side tagging
9. QA matrix
10. Tracking and speed

## 1. Measurement plan

Write it before building:

| Business goal | User action | Event | Key event? | Parameters | Fired from | Owner |
|---|---|---|---|---|---|---|

Also record: conversion definitions per platform (GA4 key events, Google Ads, Meta), consent behaviour, and the CRM fields that receive attribution data. Keep the event list small; track only what someone will act on.

## 2. Event dictionary

| Event | When | Parameters |
|---|---|---|
| `form_start` | First interaction with any field | `form_id`, `form_name`, `lead_type` |
| `form_step` | Each completed step of a multi-step form | `form_id`, `step_number`, `step_name` |
| `form_error` | Validation failure shown to the user | `form_id`, `field_name`, `error_type` |
| `form_abandon` | Page exit after `form_start` without success | `form_id`, `last_field` |
| `form_spam_blocked` | Submission rejected by spam layers | `form_id`, `reason` |
| `generate_lead` | Server confirmed the lead was stored (key event) | `form_id`, `lead_type`, `lead_id`, `value`, `currency` |
| `click_whatsapp`, `click_phone`, `click_email` | Contact link tapped | `placement` (hero, sticky, footer) |
| `check_availability`, `begin_checkout`, `purchase` | Booking flow (hospitality) | `purchase` needs `transaction_id`, `value`, `currency` |
| `book_viewing`, `book_demo`, `start_trial`, `sign_up` | Vertical macro conversions | `lead_id` or user id |

Turn off GA4 Enhanced Measurement form interactions when using these custom form events; the automatic ones often conflict and miscount (Analytics Mania). Never send names, emails or phone numbers in parameters or URLs.

## 3. dataLayer spec

Developer-pushed dataLayer events are the most robust method; DOM triggers (thank-you element visibility, submit-button clicks) break easily (Analytics Mania, Strong). Push after the server responds:

```js
// after POST /api/leads returns 200 with { leadId }
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
  event: 'generate_lead',
  form_id: 'villa_enquiry',
  lead_type: 'enquiry',
  lead_id: leadId,
  value: 150,
  currency: 'USD'
});
```

In GTM: a Custom Event trigger per event, dataLayer variables per parameter, one GA4 Event tag per event or a generic tag reading `{{Event}}`. Use DOM click triggers only for simple `tel:`, `wa.me` and `mailto:` links. Name assets consistently (`GA4 - Event - generate_lead`, `CE - generate_lead`, `DLV - lead_id`).

## 4. Deduplication

- Generate `lead_id` (UUID) on the server, store it in the database, return it to the page, push it with `generate_lead`.
- Fire `generate_lead` once per `lead_id`; guard against double clicks and reloads of the success state.
- Pass `lead_id` as the event or transaction ID to ad platforms so browser and server-side conversions deduplicate and offline imports can match.

## 5. Consent

Simo Ahava's distinction:
- **Basic Consent Mode:** Google tags load nothing until consent. GA4 behavioural modelling is effectively off; some Ads conversion modelling remains.
- **Advanced Consent Mode:** tags load with consent denied by default and send cookieless pings, enabling modelling. Collecting pings from non-consenting users needs legal review.

Implications: expect lower reported conversions from EU and UK visitors (common for luxury villa guests) under Basic. Treat CRM lead counts as the source of truth and report the GA4 vs CRM variance. Set consent defaults before any tag fires and wire the CMP through GTM templates rather than late gtag calls. The mode choice is a legal and business decision; record it. Flag local law too (for Sri Lankan brands, the Personal Data Protection Act) without giving legal advice.

## 6. Cross-domain and booking engines

- Booking engine or app on another domain you can tag: add both to the cross-domain configuration, install the same container, verify the `_gl` parameter survives, add the domain to unwanted referrals.
- Third-party engine you cannot tag: track `begin_checkout` on the click-out, request the vendor's analytics integration or postback, and reconcile confirmed bookings from the engine's reports.
- Iframe widgets (calendars, booking widgets): listen for the vendor's `postMessage` events in GTM.
- Payment gateways go in unwanted referrals.

## 7. Click IDs, UTMs and the CRM loop

- Capture `gclid`, `gbraid`, `wbraid`, `fbclid`, all UTMs and the landing page URL into hidden fields; store them with the lead and `lead_id`.
- When a lead becomes a confirmed booking, viewing or paying customer, upload that outcome to the ad platforms (offline conversion import, server-side conversion APIs) with the click ID, so bidding optimises for qualified leads rather than form fills.
- UTM governance: lower-case, one controlled vocabulary in a shared sheet, no UTMs on internal links. Check the share of `(not set)` and Unassigned monthly.
- Report lead-to-qualified and lead-to-revenue by landing page and source each month.

## 8. Server-side tagging

Ahava's case: lighter pages (one event stream replaces several vendor scripts), control to validate or strip data, better security policies. He warns that using it mainly to dodge ad blockers erodes user agency. It adds hosting cost and maintenance. Worth it for SaaS and hotel groups with meaningful paid media; usually overkill for a single villa or a small agency site.

## 9. QA matrix

Test in GTM Preview, GA4 DebugView and the network tab, plus ad platform test tools.

| Event | Form path (success, validation error, server error, spam-blocked) | Consent state (accepted, rejected, no choice) | Device | Expected hits | Params present | Pass | Notes |
|---|---|---|---|---|---|---|---|

Pass conditions: exactly one `generate_lead` per real lead, none on errors or spam, correct parameters, consent respected, cross-domain session preserved, lead and click IDs written to the CRM.

## 10. Tracking and speed

Every tag costs main-thread time. Audit GTM quarterly: remove dead pixels, fire non-essential tags after load or on interaction, and consider server-side forwarding for ad pixels where volume justifies it.
