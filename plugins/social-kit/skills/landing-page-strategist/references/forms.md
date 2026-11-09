# Forms and Lead Capture

The form is where intent becomes a lead. Every field costs effort, but the right fields, well labelled, can beat fewer fields badly chosen (Aagaard). Decide each field by what the next step needs and what downstream lead quality shows, not by habit or by what sales would like to know someday.

## Contents
1. Field decisions
2. Labels, types and marking
3. Validation and errors
4. Single-step vs multi-step
5. Privacy microcopy and the success state
6. Spam protection
7. Alternative capture channels
8. Lead quality trade-off
9. Form spec template

## 1. Field decisions

For each candidate field ask: does the next step (reply, quote, viewing, trial) fail without it? If not, cut it, make it optional, or move it after submission.

- Every field adds effort (NN/g, Baymard: field count drives effort more than step count). Baymard's checkout research found most sites need about 8 fields against an average of 11.3; lead forms usually need far fewer.
- Cutting the wrong fields can lower conversion. Aagaard's test lost 14% when it cut 9 fields to 6 and gained 19.21% by keeping 9 with clearer labels and order (single test, Weak to Moderate). Rewrite confusing fields before deleting useful ones.
- Confusing optional fields cause errors (Expedia's "Company" field anecdote). Remove or relabel anything users misread.
- **Phone:** valuable where agents call back (villas, real estate) but adds friction (agency test: about 48% drop on an ebook form, Weak). Make it optional with a reason ("for a faster reply on WhatsApp"), or ask on the thank-you step.
- **Progressive profiling:** ask the minimum now, the rest in the reply, on the thank-you page or at the next touchpoint.

## 2. Labels, types and marking

- Persistent visible labels above each field. Placeholders are hints only, never labels (NN/g, Strong).
- Mark both required and optional fields explicitly (Baymard: 32% missed a required field when only optional ones were marked).
- Input types and attributes: `type="email"`, `type="tel"`, `inputmode="numeric"` for numbers, `autocomplete="name"`, `"email"`, `"tel"`, `"country"`, native date pickers or a tested date range picker for stays.
- Group related fields; order from easy to personal (dates and guests before name and phone).
- Single-column layout on mobile.

## 3. Validation and errors

- Validate on blur, not on every keystroke; never flag an empty field the user has not touched. Wroblewski and Etre (2009, 22 participants): inline validation improved success, errors and completion time; trust the direction, not the exact percentages.
- Error messages next to the field, saying how to fix it ("Enter an email like name@example.com"), announced to screen readers.
- Preserve everything entered on error; never clear the form.
- Guideline-compliant forms produced far more error-free first submissions (Seckler et al., CHI 2014; NN/g summary 78% vs 42%).
- Server errors get a clear fallback: "Something went wrong. Message us on WhatsApp" with the link, so the lead is not lost.

## 4. Single-step vs multi-step

- Multi-step suits longer or complex forms (NN/g on staged disclosure). Claims like "multi-step converts 86% higher" come from vendors without methods; do not present them as fact.
- If multi-step, open with a low-commitment, high-relevance step that also qualifies: dates and guests for a villa, budget and area for real estate, work email for SaaS. Ask for contact details last. Show progress ("Step 1 of 2").
- Track each step (`form_step`) so drop-off is visible.
- For 3 fields or fewer, a single step is usually right.

## 5. Privacy microcopy and the success state

- A short line near the submit button about how the data is used ("We only use this to reply to your enquiry"). Avoid wording that primes the fear ("We will never spam you"). Weak to Moderate evidence; test where traffic allows.
- Submit button label states the outcome ("Send my enquiry", "Check availability").
- The success state confirms receipt, sets expectations ("We reply within 2 hours, 8am to 10pm Sri Lanka time" `[VERIFY]`), and offers a next step (WhatsApp link, calendar link, brochure). Fire `generate_lead` only on server-confirmed success.

## 6. Spam protection

Visible CAPTCHAs cost conversions (Baymard 2018: 8.66% failed first try, 29.45% when case-sensitive; Moz 2009: about 3.2% of conversions lost). Use invisible layers first:
1. Honeypot field hidden from users and screen readers
2. Minimum time-to-submit check
3. Server-side validation and rate limiting per IP and per email
4. An invisible challenge only for traffic that fails the checks above

Track blocked submissions (`form_spam_blocked`) so spam rate is reportable and false positives are noticed.

## 7. Alternative capture channels

| Channel | Best for | Track as | Notes |
|---|---|---|---|
| WhatsApp click-to-chat | Sri Lankan and South Asian hospitality and real estate; often the main enquiry channel | `click_whatsapp` | A click is not a conversation; reconcile weekly with WhatsApp Business conversation counts. Prefill the message with the page and dates so enquiries are attributable |
| Phone | High-value, older or urgent buyers | `click_phone` | Use a tracking number only if it does not break NAP consistency |
| Calendar booking | Real estate viewings, SaaS demos | `generate_lead` with `lead_type: viewing` or `demo` | Embeds in iframes need postMessage listeners |
| Booking engine | Hotels and villas with direct booking | `check_availability`, `begin_checkout`, `purchase` | Often cross-domain; see tracking.md |
| Chat widget | SaaS, complex products | `chat_start` | Load behind a facade; widgets are heavy (page-speed.md) |

Evidence for which channel converts best is practitioner experience (Weak). Test channel-first layouts only where traffic allows; otherwise compare with season-matched pre/post.

## 8. Lead quality trade-off

More fields usually mean fewer but better-qualified leads. Settle it with CRM data: qualified rate, lead-to-booking, lead-to-viewing or lead-to-paid, cost per qualified lead. Never call a form change a win on submission rate alone; make qualified rate a guardrail.

## 9. Form spec template

| Field | Label (exact) | Type and attributes | Required | Why needed | Validation and error text | Step |
|---|---|---|---|---|---|---|

Then list: submit label, privacy line, success state copy, spam layers, alternative channels with prefilled messages, events fired at each point, and CRM fields written (including hidden fields for click IDs, UTMs and `lead_id`).
