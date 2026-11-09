# KPIs: Definitions, Formulas and Caveats

Three headline KPIs judge every page. Report them against a recorded baseline, segmented by source and device, never as a single blended number without context. Supporting metrics explain why the headline moved and tie it to revenue.

## 1. Page load speed

| Metric | Formula | Source |
|---|---|---|
| LCP p75 | 75th percentile of per-page-view LCP over 28 days, by landing page and device | Own RUM via `web-vitals`, or public field data where the page has enough traffic |
| INP p75, CLS p75 | Same method | Same |
| TTFB p75 | Same method; isolates server and CDN | Same |

Report against the budget in page-speed.md. Caveat: low-traffic pages often lack public field data; collect your own. Lab scores diagnose, they do not replace field data.

## 2. Lead capture rate

**Formula:** confirmed leads / landing page sessions x 100.
- State the denominator every time. Sessions inflate the base when visitors return; users can be undercounted under consent restrictions.
- Count only server-confirmed, deduplicated leads (`generate_lead` with unique `lead_id`).
- Decide up front whether contact clicks (`click_whatsapp`, `click_phone`) count as leads. Default: report them as a separate contact rate, because a click is not a conversation, then add reconciled WhatsApp conversations to leads where the business logs them.
- Report by source and device; blended rates hide traffic mix shifts.
- Under Basic Consent Mode GA4 undercounts numerator and denominator unevenly. Cross-check with CRM leads divided by server-logged sessions.

## 3. Form submissions

| Metric | Formula |
|---|---|
| Form submissions | Count of server-confirmed, deduplicated `generate_lead` per form |
| View-to-start rate | `form_start` / sessions where the form was visible |
| Completion rate | `generate_lead` / `form_start` |
| Abandonment rate | 1 minus completion rate |
| Field drop-off | Share of `form_abandon` events by `last_field` |
| Error rate by field | `form_error` count by `field_name` / `form_start` |
| Spam rate | `form_spam_blocked` / (`generate_lead` + `form_spam_blocked`) |

## 4. Supporting metrics

- Lead quality: qualified rate (CRM-qualified / leads), lead-to-booking, lead-to-viewing or lead-to-paid, cost per qualified lead, revenue per lead
- Contact rate: contact clicks / sessions, by channel
- GA4 vs CRM lead variance (tracking health)
- Consent acceptance rate
- `(not set)` and Unassigned share of sessions

## 5. Benchmarks

Independent, current, lead-gen benchmarks are scarce. Most published "average landing page conversion rates" come from tool vendors' customer bases (for example Unbounce) and mix industries, sources and definitions. Use them only as rough context, labelled as vendor data. The client's own baseline and trend matter more. For luxury hospitality and Sri Lankan real estate, no reliable independent benchmark exists; build one per client.

## 6. Monthly dashboard

1. Headline: qualified leads, cost per qualified lead, lead-to-revenue vs last month and the same month last year
2. Funnel: sessions, form views, form starts, leads, qualified leads, bookings or viewings or paid, by source and device
3. Form health: completion rate, top abandoned fields, errors by field, spam blocked
4. Speed: LCP, INP, CLS at p75 by page, against budget
5. Tracking health: consent acceptance, GA4 vs CRM variance, `(not set)` share
6. Changes and experiments log: what changed, status, outcome and confidence
7. Next actions from the backlog

Looker Studio over GA4 plus a CRM export works; a spreadsheet works too. Annotate releases, campaign launches and seasonal peaks.
