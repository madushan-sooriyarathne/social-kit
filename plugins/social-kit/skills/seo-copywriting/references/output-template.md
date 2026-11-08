# Output Template

Deliver one document for the brand. Use this structure.

```
# [Brand]: SEO Copy

## Summary
Two or three sentences: pages written, the keyword logic, and what needs verifying before publishing.

## Assumptions and data
- Market, language and spelling variant used
- Keyword data source: user export (tool and date) or SERP-inferred
- Anything assumed because the user was not available

## Keyword map
| Page | URL | Primary | Secondaries | Intent | Demand signal | Confidence |

## Page: [Page name]

### Target
- Primary keyword:
- Secondaries:
- Questions answered:
- Intent and SERP format:
- Information gain angle: what this page offers that the ranking pages do not

### Metadata
- URL: /slug
- Title tag (NN chars):
- Meta description (NN chars):
- H1:

### Copy
[Full page copy in markdown, headings as they will appear on the page.
Mark CTAs as **[CTA: label → destination]**.
Mark image slots as *[Image: description | alt: alt text]*.]

### Supporting elements
- Schema suggestion (type and the fields to fill, only types with test support or clear fit)
- Internal links: in (from which pages, anchor text) and out
- [VERIFY] list: every fact that needs the brand's confirmation

(repeat per page)

## Checker results
One line per page from copy_check.py, with any warnings you chose to keep and why.

## Next steps
At most three: for example, verify flagged facts, publish order, which pages to link from existing content.
```

Notes:
- Character counts for title and meta are real counts, not estimates.
- Keep the evidence explanation out of the page copy; cite it briefly in Target or Summary only where a choice needs justifying.
- If the environment offers a doc artifact, use it; otherwise write a markdown file and send it.
