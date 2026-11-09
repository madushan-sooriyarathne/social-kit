# Page Speed

Speed is a hygiene factor with a real but site-specific effect on conversion (Mozilla 2010, Everts, Stadnik and Nowak; Moderate). It matters most for mobile paid traffic, where a slow LCP wastes spend before the visitor sees the offer. Fix poor mobile loads fully, set a budget, then spend effort on offer, proof and forms.

## Contents
1. Metrics
2. Field vs lab data
3. Performance budget
4. Common landing page speed killers
5. Fixes for Next.js and headless CMS builds
6. Fixes for other stacks
7. Speed plan format

## 1. Metrics

| Metric | Measures | Why it matters on a landing page |
|---|---|---|
| LCP (Largest Contentful Paint) | When the hero image or headline renders | The visitor sees the offer; the main landing page metric |
| INP (Interaction to Next Paint) | Responsiveness to taps and typing | CTA taps, form typing, date pickers |
| CLS (Cumulative Layout Shift) | Unexpected layout movement | Late banners, fonts and consent dialogs moving the CTA or form |
| TTFB (Time to First Byte) | Server and CDN response | Caps how fast LCP can be |

Commonly used tooling thresholds (LCP 2.5 s, INP 200 ms, CLS 0.1) are a default starting point, not evidence of a conversion cliff; SpeedCurve (vendor) found no consistent conversion link to INP thresholds. Set each client's budget from their own data once it exists.

## 2. Field vs lab data

- **Lab** (Lighthouse, WebPageTest, browser devtools): diagnosis and regression checks in CI.
- **Field / RUM**: what real visitors experience. Low-traffic sites often lack public field data, so collect your own with the open-source `web-vitals` library, sending values to GA4 as events or to a RUM tool.
- Report the 75th percentile over 28 days, segmented by device and traffic source. Paid social mobile traffic on slower networks is the segment to watch.

## 3. Performance budget

Practitioner targets for a landing page (not research thresholds):

| Item | Budget |
|---|---|
| LCP, mobile p75 | 2.0 s or less |
| INP p75 | 200 ms or less |
| CLS p75 | 0.05 or less |
| JavaScript, compressed | 150 KB or less |
| Third-party requests | 10 or fewer |
| Hero image | 150 KB or less, correctly sized |
| Web fonts | 2 families, 4 files or fewer |

Enforce with Lighthouse CI or bundle-size checks on every deploy.

## 4. Common landing page speed killers

- **Third-party scripts.** 90% of pages load at least one third party; the median page uses 16 third-party domains; 41% of mobile home pages could benefit from facades (Web Almanac 2025). Chat widgets, heatmap tools, review widgets and pixel stacks are the usual culprits.
- **Client-side A/B testing and anti-flicker snippets.** The snippet hides the whole page until the testing script loads; Andy Davies measured 1.7 s of blank screen in one example and called common default timeouts far too high. This directly delays LCP for every visitor in the test.
- **Video and oversized hero images.** Background video delays LCP and often does not autoplay on mobile. Use a poster image as the LCP element.
- **Web fonts.** Many weights, render blocking, and layout shift on fallback swap.
- **GTM bloat.** Every Custom HTML tag runs on the main thread. Dead pixels accumulate.
- **Consent banners** injected late cause CLS; reserve their space or overlay without shifting content.
- **Client-rendered content.** Pages that fetch content in the browser render late and are invisible to crawlers that do not run JavaScript.

## 5. Fixes for Next.js and headless CMS builds

Implementation guidance for a Next.js (App Router) and Sanity stack; adapt names for other headless setups.
- Render landing pages as static or ISR Server Components so HTML comes from the CDN edge. Keep client components out of the first screen except the form.
- Hero: `next/image` with `priority` (or `fetchPriority="high"`), explicit `sizes`, modern formats. From Sanity's image CDN request exact widths with `auto=format`; use LQIP placeholders that do not block LCP.
- Fonts: `next/font` to self-host and subset, `display: swap`, size-adjusted fallbacks to avoid CLS.
- Third parties: `next/script` with `afterInteractive` or `lazyOnload`; facades for chat, maps and YouTube that load on interaction.
- A/B assignment in middleware: set a cookie, render the variant on the server, log the assignment. No anti-flicker snippet is needed.
- Load GTM once in the root layout; audit its tags quarterly.
- Tailwind v4: keep output small; avoid shipping unused component libraries.
- Form API (Hono on Bun or similar): validate and respond fast, then push CRM sync, email and ad-platform uploads to a background queue so the success state appears immediately.

## 6. Fixes for other stacks

- WordPress and page builders: remove unused plugins, disable builder animations above the fold, preload the hero, defer non-critical scripts, use a caching and image CDN plugin.
- Hosted landing page builders: limit embedded widgets, compress images before upload, check whether the builder's own testing feature injects an anti-flicker snippet.

## 7. Speed plan format

| Item | Current (field p75 or lab) | Budget | Cause | Fix | Owner |
|---|---|---|---|---|---|

Followed by the third-party inventory:

| Script | Purpose | Needed on this page? | Load strategy (remove, defer, facade, server-side) | Size |
|---|---|---|---|---|
