#!/usr/bin/env python3
"""Raw-HTML landing page and form audit. Stdlib only.

Fetches the page as served (no JavaScript execution) and reports what a strategist checks
first: headline and CTAs, contact links, every form field and how it is labelled, input
types and autocomplete, spam protection, third-party scripts, tag managers and analytics,
client-side testing tools and anti-flicker snippets, consent tools, hero image and font
loading, video and iframes.

Content that only appears after client-side rendering will not show here; that is itself
a finding for crawlers and slow phones. Pair this with a field-data speed check and a
look at the page on a phone-width viewport.

Usage:
    python3 landing_audit.py https://example.com/offer
    python3 landing_audit.py https://example.com/offer --json > audit.json
    python3 landing_audit.py --file saved_page.html --base https://example.com/
"""

import argparse
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

UA = "Mozilla/5.0 (compatible; landing-audit/1.0)"

TOOLS = {
    "Google Tag Manager": [r"googletagmanager\.com/gtm\.js", r"GTM-[A-Z0-9]{4,}"],
    "GA4 / gtag": [r"googletagmanager\.com/gtag/js", r"\bG-[A-Z0-9]{6,}\b"],
    "Meta Pixel": [r"connect\.facebook\.net/.+/fbevents\.js", r"fbq\("],
    "Hotjar": [r"static\.hotjar\.com", r"hotjar"],
    "Microsoft Clarity": [r"clarity\.ms"],
    "TikTok Pixel": [r"analytics\.tiktok\.com"],
    "LinkedIn Insight": [r"snap\.licdn\.com"],
}
CHAT = {
    "Intercom": r"widget\.intercom\.io|intercomcdn",
    "Tawk.to": r"embed\.tawk\.to",
    "Crisp": r"client\.crisp\.chat",
    "Drift": r"js\.driftt\.com|drift\.com",
    "Zendesk": r"static\.zdassets\.com",
    "HubSpot chat": r"js\.hs-scripts\.com|js\.usemessages\.com",
    "Elfsight / WhatsApp widget": r"elfsight|getbutton\.io|whatsapp-widget",
}
TESTING = {
    "Optimizely": r"cdn\.optimizely\.com",
    "VWO": r"dev\.visualwebsiteoptimizer\.com|_vwo_code",
    "AB Tasty": r"try\.abtasty\.com",
    "Convert": r"cdn-\d+\.convertexperiments\.com",
    "Google Optimize (retired)": r"optimize\.google\.com|googleoptimize\.com",
    "Kameleoon": r"kameleoon",
}
ANTI_FLICKER = [r"async-hide", r"anti-?flicker", r"_vis_opt_path_hides", r"opacity\s*:\s*0\s*!important",
                r"\.async-hide\s*\{", r"abtasty.*hide"]
CONSENT = {
    "Cookiebot": r"consent\.cookiebot\.com",
    "OneTrust": r"cdn\.cookielaw\.org|onetrust",
    "CookieYes": r"cookieyes",
    "Usercentrics": r"usercentrics",
    "iubenda": r"iubenda",
    "Complianz": r"complianz",
    "Termly": r"termly\.io",
}
CAPTCHA = {
    "reCAPTCHA": r"google\.com/recaptcha|grecaptcha|g-recaptcha",
    "hCaptcha": r"hcaptcha",
    "Cloudflare Turnstile": r"challenges\.cloudflare\.com/turnstile|cf-turnstile",
}
CTA_WORDS = re.compile(r"\b(book|check|enquire|inquire|contact|get|start|request|reserve|schedule|download|sign ?up|"
                       r"try|join|call|message|whatsapp|send|apply|claim|view|see availability|demo|quote)\b", re.I)
EMAILISH = re.compile(r"e-?mail", re.I)
PHONEISH = re.compile(r"phone|mobile|tel|whatsapp|contact.?number", re.I)


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.meta = {}
        self.lang = None
        self.headings = []
        self.links = []
        self.buttons = []
        self.forms = []
        self.labels_for = {}
        self.scripts = []
        self.inline_js = []
        self.styles_inline = []
        self.preloads = []
        self.stylesheets = []
        self.images = []
        self.videos = []
        self.iframes = []
        self.text = []
        self._stack = []
        self._in = {"title": False, "script": False, "style": False}
        self._heading = None
        self._link = None
        self._button = None
        self._label = None
        self._form = None

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in["title"] = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "")
        elif tag in ("h1", "h2"):
            self._heading = [tag, ""]
        elif tag == "a":
            self._link = {"href": a.get("href", ""), "text": ""}
        elif tag == "button":
            self._button = {"type": a.get("type", "submit"), "text": "", "in_form": self._form is not None}
        elif tag == "label":
            self._label = {"for": a.get("for"), "text": "", "wraps": []}
            if a.get("for"):
                self.labels_for[a["for"]] = ""
        elif tag == "form":
            self._form = {"action": a.get("action", ""), "method": (a.get("method") or "get").lower(),
                          "id": a.get("id", ""), "fields": [], "submit": [], "html": []}
        elif tag in ("input", "select", "textarea"):
            f = {
                "tag": tag, "type": (a.get("type") or ("text" if tag == "input" else tag)).lower(),
                "name": a.get("name", ""), "id": a.get("id", ""), "placeholder": a.get("placeholder", ""),
                "required": "required" in a or a.get("aria-required") == "true",
                "autocomplete": a.get("autocomplete", ""), "inputmode": a.get("inputmode", ""),
                "aria_label": a.get("aria-label", "") or a.get("aria-labelledby", ""),
                "hidden_style": bool(re.search(r"display\s*:\s*none|visibility\s*:\s*hidden|left\s*:\s*-\d{3,}",
                                               a.get("style", ""))) or "aria-hidden" in a,
                "tabindex": a.get("tabindex", ""), "wrapped_label": self._label is not None, "value": a.get("value", ""),
            }
            if self._label is not None:
                self._label["wraps"].append(f)
            if f["type"] == "submit":
                if self._form is not None:
                    self._form["submit"].append(f["value"] or "Submit")
            elif self._form is not None:
                self._form["fields"].append(f)
            else:
                self.forms_orphan = getattr(self, "forms_orphan", []) + [f]
        elif tag == "script":
            self._in["script"] = True
            if a.get("src"):
                self.scripts.append({"src": a["src"], "async": "async" in a, "defer": "defer" in a,
                                     "type": a.get("type", ""), "in_head": "head" in self._stack})
        elif tag == "style":
            self._in["style"] = True
        elif tag == "link":
            rel = a.get("rel", "").lower()
            if "preload" in rel:
                self.preloads.append({"href": a.get("href", ""), "as": a.get("as", ""),
                                      "fetchpriority": a.get("fetchpriority", "")})
            if "stylesheet" in rel:
                self.stylesheets.append(a.get("href", ""))
        elif tag == "img":
            self.images.append({"src": a.get("src", "") or a.get("data-src", ""), "alt": a.get("alt"),
                                "loading": a.get("loading", ""), "fetchpriority": a.get("fetchpriority", ""),
                                "width": a.get("width", ""), "height": a.get("height", ""),
                                "srcset": bool(a.get("srcset"))})
        elif tag == "video":
            self.videos.append({"autoplay": "autoplay" in a, "poster": a.get("poster", ""), "src": a.get("src", "")})
        elif tag == "source" and self._stack and self._stack[-1] == "video" and self.videos and not self.videos[-1]["src"]:
            self.videos[-1]["src"] = a.get("src", "")
        elif tag == "iframe":
            self.iframes.append(a.get("src", "") or a.get("data-src", ""))
        if tag not in ("meta", "link", "img", "input", "br", "hr", "source"):
            self._stack.append(tag)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in["title"] = False
        elif tag == "script":
            self._in["script"] = False
        elif tag == "style":
            self._in["style"] = False
        elif tag in ("h1", "h2") and self._heading:
            self.headings.append((self._heading[0], " ".join(self._heading[1].split())))
            self._heading = None
        elif tag == "a" and self._link is not None:
            self._link["text"] = " ".join(self._link["text"].split())
            self.links.append(self._link)
            self._link = None
        elif tag == "button" and self._button is not None:
            self._button["text"] = " ".join(self._button["text"].split())
            self.buttons.append(self._button)
            if self._form is not None and self._button["type"] == "submit":
                self._form["submit"].append(self._button["text"] or "(no text)")
            self._button = None
        elif tag == "label" and self._label is not None:
            text = " ".join(self._label["text"].split())
            if self._label["for"]:
                self.labels_for[self._label["for"]] = text
            for f in self._label["wraps"]:
                f["label_text"] = text
            self._label = None
        elif tag == "form" and self._form is not None:
            self.forms.append(self._form)
            self._form = None
        if tag in self._stack:
            while self._stack and self._stack.pop() != tag:
                pass

    def handle_data(self, data):
        if self._in["title"]:
            self.title += data
        if self._in["script"]:
            self.inline_js.append(data)
            return
        if self._in["style"]:
            self.styles_inline.append(data)
            return
        if self._heading:
            self._heading[1] += data
        if self._link is not None:
            self._link["text"] += data
        if self._button is not None:
            self._button["text"] += data
        if self._label is not None:
            self._label["text"] += data
        if data.strip():
            self.text.append(data.strip())


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
        charset = r.headers.get_content_charset() or "utf-8"
        return r.geturl(), r.status, raw.decode(charset, errors="replace"), len(raw)


def field_label(f, labels_for):
    if f.get("label_text"):
        return f["label_text"]
    if f["id"] and labels_for.get(f["id"]):
        return labels_for[f["id"]]
    if f["aria_label"]:
        return f"[aria] {f['aria_label']}"
    return ""


def audit(html, url, status=None, size=None):
    p = Page()
    p.feed(html)
    host = urlparse(url).hostname or ""
    root = ".".join(host.split(".")[-2:]) if host else ""
    blob = html

    def domain(src):
        return urlparse(urljoin(url, src)).hostname or ""

    scripts = []
    third = set()
    for s in p.scripts:
        d = domain(s["src"])
        is_third = bool(d) and root not in d
        if is_third:
            third.add(d)
        scripts.append({**s, "domain": d, "third_party": is_third})
    for src in p.iframes:
        d = domain(src)
        if d and root not in d:
            third.add(d)

    found = lambda table: [k for k, pats in table.items()
                           if any(re.search(x, blob, re.I) for x in (pats if isinstance(pats, list) else [pats]))]
    gtm_ids = sorted(set(re.findall(r"GTM-[A-Z0-9]{4,}", blob)))
    ga_ids = sorted(set(re.findall(r"\bG-[A-Z0-9]{6,}\b", blob)))
    direct_gtag = bool(re.search(r"googletagmanager\.com/gtag/js", blob))

    contact = {
        "whatsapp": [l["href"] for l in p.links if re.search(r"wa\.me|api\.whatsapp\.com|whatsapp://", l["href"], re.I)],
        "tel": [l["href"] for l in p.links if l["href"].lower().startswith("tel:")],
        "mailto": [l["href"] for l in p.links if l["href"].lower().startswith("mailto:")],
    }
    ctas = []
    for l in p.links:
        if l["text"] and CTA_WORDS.search(l["text"]) and len(l["text"]) <= 40:
            ctas.append({"text": l["text"], "href": l["href"]})
    for b in p.buttons:
        if b["text"] and len(b["text"]) <= 40:
            ctas.append({"text": b["text"], "href": "(button)"})

    forms = []
    issues = []
    for i, f in enumerate(p.forms):
        visible = [x for x in f["fields"] if x["type"] not in ("hidden",) and not x["hidden_style"]]
        honeypot = [x for x in f["fields"] if x["type"] != "hidden" and (x["hidden_style"] or x["tabindex"] == "-1")]
        rows = []
        for x in visible:
            lab = field_label(x, p.labels_for)
            r = {"name": x["name"] or x["id"], "type": x["type"], "label": lab, "placeholder": x["placeholder"],
                 "required": x["required"], "autocomplete": x["autocomplete"]}
            rows.append(r)
            ident = f"{x['name']} {x['id']} {lab} {x['placeholder']}"
            if not lab and x["placeholder"]:
                issues.append(f"Form {i + 1}: '{r['name']}' uses placeholder as its only label")
            elif not lab and x["type"] not in ("checkbox", "radio", "submit", "button"):
                issues.append(f"Form {i + 1}: '{r['name']}' has no accessible label")
            if EMAILISH.search(ident) and x["type"] != "email":
                issues.append(f"Form {i + 1}: '{r['name']}' looks like email but type is '{x['type']}'")
            if PHONEISH.search(ident) and x["type"] not in ("tel",) and x["tag"] == "input":
                issues.append(f"Form {i + 1}: '{r['name']}' looks like phone but type is '{x['type']}'")
            if x["tag"] == "input" and x["type"] in ("text", "email", "tel") and not x["autocomplete"]:
                issues.append(f"Form {i + 1}: '{r['name']}' has no autocomplete attribute")
        req = sum(1 for r in rows if r["required"])
        if rows and 0 < req < len(rows):
            labels = " ".join(r["label"] for r in rows).lower()
            if "optional" not in labels:
                issues.append(f"Form {i + 1}: optional fields are not marked as optional")
        for s in f["submit"]:
            if s.strip().lower() in ("submit", "send", "(no text)"):
                issues.append(f"Form {i + 1}: generic submit label '{s}'")
        forms.append({"action": f["action"], "method": f["method"], "visible_fields": len(rows),
                      "required_fields": req, "fields": rows, "submit_labels": f["submit"],
                      "honeypot_like_fields": len(honeypot)})

    hero = p.images[0] if p.images else None
    speed = []
    if hero:
        if hero["loading"] == "lazy":
            speed.append("First image is loading=lazy; if it is the hero/LCP element this delays LCP")
        if not hero["width"] or not hero["height"]:
            speed.append("First image has no width/height attributes (layout shift risk)")
        if not hero["srcset"] and "/_next/image" not in hero["src"]:
            speed.append("First image has no srcset (may ship desktop size to phones)")
    if not any(pl["as"] == "image" for pl in p.preloads) and not (hero and hero["fetchpriority"] == "high"):
        speed.append("No image preload or fetchpriority=high on the hero")
    blocking = [s for s in scripts if s["in_head"] and not s["async"] and not s["defer"] and s["type"] != "module"]
    if blocking:
        speed.append(f"{len(blocking)} render-blocking script(s) in <head>")
    if any(v["autoplay"] for v in p.videos):
        speed.append("Autoplay video present; ensure a poster image is the LCP element on mobile")
    fonts = [s for s in p.stylesheets if "fonts.googleapis.com" in s or "typekit" in s or "fonts." in s]
    if fonts:
        speed.append(f"{len(fonts)} external font stylesheet(s); consider self-hosting and subsetting")
    anti = [x for x in ANTI_FLICKER if re.search(x, blob, re.I)]
    testing = found(TESTING)
    if anti:
        speed.append("Anti-flicker / page-hiding snippet detected: blanks the page until the test tool loads")
    if gtm_ids and direct_gtag and len(set(ga_ids)) > 0:
        issues.append("Both GTM and a direct gtag.js load found: check for double-counted GA4 events")

    visible_text = " ".join(p.text)
    return {
        "url": url, "status": status, "html_bytes": size or len(html.encode()),
        "visible_text_chars": len(visible_text),
        "likely_client_rendered": len(visible_text) < 400,
        "title": " ".join(p.title.split()), "meta_description": p.meta.get("description", ""),
        "viewport_meta": "viewport" in p.meta, "lang": p.lang,
        "h1": [t for h, t in p.headings if h == "h1"], "h2": [t for h, t in p.headings if h == "h2"][:12],
        "cta_candidates": ctas[:25], "contact_links": contact,
        "forms": forms, "form_issues": issues,
        "captcha": found(CAPTCHA),
        "analytics": found(TOOLS), "gtm_ids": gtm_ids, "ga4_ids": ga_ids,
        "chat_widgets": found(CHAT), "testing_tools": testing, "anti_flicker_patterns": anti,
        "consent_tools": found(CONSENT),
        "third_party_domains": sorted(third), "script_count": len(scripts),
        "images": len(p.images), "hero_image": hero, "videos": p.videos, "iframes": p.iframes,
        "preloads": p.preloads, "speed_flags": speed,
    }


def print_report(r):
    out = []
    w = out.append
    w(f"URL: {r['url']}  (status {r['status']}, {r['html_bytes']:,} bytes HTML)")
    w(f"Visible text in raw HTML: {r['visible_text_chars']:,} chars"
      + ("  ** very little text in raw HTML: the page may be client-rendered, so content appears only after JS runs **"
         if r["likely_client_rendered"] else ""))
    w(f"Title: {r['title'] or '(none)'}")
    w(f"Meta description: {r['meta_description'] or '(none)'}")
    w(f"Viewport meta: {'yes' if r['viewport_meta'] else 'MISSING'}   lang: {r['lang'] or '(none)'}")
    w(f"H1: {r['h1'] or '(none)'}")
    if len(r["h1"]) > 1:
        w("  ** more than one H1 **")
    w(f"H2 (first 12): {r['h2']}")
    w("\nCTA candidates:")
    for c in r["cta_candidates"] or [{"text": "(none found)", "href": ""}]:
        w(f"  - {c['text']}  -> {c['href']}")
    cl = r["contact_links"]
    w(f"Contact links: WhatsApp {len(cl['whatsapp'])}, tel {len(cl['tel'])}, mailto {len(cl['mailto'])}")
    w(f"\nForms: {len(r['forms'])}")
    for i, f in enumerate(r["forms"], 1):
        w(f"  Form {i}: {f['visible_fields']} visible fields, {f['required_fields']} required, method {f['method']}, "
          f"submit {f['submit_labels']}, honeypot-like {f['honeypot_like_fields']}")
        for x in f["fields"]:
            w(f"    - {x['name'] or '(unnamed)'} [{x['type']}] label='{x['label']}' placeholder='{x['placeholder']}' "
              f"{'required' if x['required'] else 'optional'} autocomplete='{x['autocomplete']}'")
    w(f"Visible CAPTCHA tech: {r['captcha'] or 'none detected'}")
    if r["form_issues"]:
        w("Form and tracking issues:")
        for i in r["form_issues"]:
            w(f"  ! {i}")
    w(f"\nAnalytics: {r['analytics'] or 'none detected'}  GTM {r['gtm_ids']}  GA4 {r['ga4_ids']}")
    w(f"Consent tools: {r['consent_tools'] or 'none detected'}")
    w(f"Chat widgets: {r['chat_widgets'] or 'none'}   Testing tools: {r['testing_tools'] or 'none'}")
    w(f"Third-party domains ({len(r['third_party_domains'])}): {', '.join(r['third_party_domains']) or 'none'}")
    w(f"Scripts: {r['script_count']}  Images: {r['images']}  Videos: {len(r['videos'])}  Iframes: {len(r['iframes'])}")
    if r["iframes"]:
        for s in r["iframes"][:10]:
            w(f"  iframe: {s}")
    w("\nSpeed flags:")
    for s in r["speed_flags"] or ["none from raw HTML (still check field LCP/INP/CLS)"]:
        w(f"  - {s}")
    print("\n".join(out))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", nargs="?")
    ap.add_argument("--file", help="audit a saved HTML file instead of fetching")
    ap.add_argument("--base", help="base URL for --file (to classify third parties)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.file:
        with open(a.file, encoding="utf-8", errors="replace") as f:
            html = f.read()
        r = audit(html, a.base or a.url or "https://example.invalid/")
    elif a.url:
        try:
            final, status, html, size = fetch(a.url)
        except Exception as e:  # network or HTTP failure
            sys.exit(f"Could not fetch {a.url}: {e}. Try WebFetch or a browser, or save the HTML and use --file.")
        r = audit(html, final, status, size)
    else:
        ap.error("pass a URL or --file")
    if a.json:
        print(json.dumps(r, indent=2))
    else:
        print_report(r)


if __name__ == "__main__":
    main()
