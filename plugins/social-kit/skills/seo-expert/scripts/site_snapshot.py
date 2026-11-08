#!/usr/bin/env python3
"""Quick SEO snapshot of a website using only the Python standard library.

Fetches raw HTML (no JavaScript execution, which is what AI crawlers see) and
reports: visible text length, title, meta description, canonical, robots meta,
H1s, JSON-LD types, internal/external link counts, robots.txt rules for search
and AI crawlers, and sitemap presence.

Usage:
    python3 site_snapshot.py https://example.com [--pages /rooms /about] [--json]
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

UA = "Mozilla/5.0 (compatible; seo-snapshot/1.0)"
CRAWLERS = [
    "Googlebot", "Bingbot",
    "OAI-SearchBot", "ChatGPT-User", "GPTBot",
    "PerplexityBot", "Claude-SearchBot", "Claude-User", "ClaudeBot",
    "Google-Extended", "CCBot",
]
SHELL_TEXT_THRESHOLD = 500  # visible chars below this suggests a client-rendered shell


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read(5_000_000).decode(r.headers.get_content_charset() or "utf-8", "replace")
            return r.status, r.geturl(), body
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception as e:  # network refused, DNS, TLS
        return None, url, f"ERROR: {e}"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.meta = {}
        self.canonical = None
        self.h1 = []
        self.links = []
        self.jsonld = []
        self.text_parts = []
        self._stack = []
        self._skip = 0
        self._in_title = self._in_h1 = self._in_jsonld = False
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "noscript", "template"):
            self._skip += 1
            if tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
                self._in_jsonld, self._buf = True, ""
        elif tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1, self._buf = True, ""
        elif tag == "meta":
            key = (a.get("name") or a.get("property") or "").lower()
            if key:
                self.meta[key] = a.get("content", "")
        elif tag == "link" and "canonical" in (a.get("rel") or "").lower():
            self.canonical = a.get("href")
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "template"):
            self._skip = max(0, self._skip - 1)
            if tag == "script" and self._in_jsonld:
                self.jsonld.append(self._buf)
                self._in_jsonld = False
        elif tag == "title":
            self._in_title = False
        elif tag == "h1" and self._in_h1:
            self.h1.append(" ".join(self._buf.split()))
            self._in_h1 = False

    def handle_data(self, data):
        if self._in_jsonld:
            self._buf += data
            return
        if self._skip:
            return
        if self._in_title:
            self.title += data
        if self._in_h1:
            self._buf += data
        self.text_parts.append(data)


def jsonld_types(blocks):
    types = []

    def walk(node):
        if isinstance(node, dict):
            t = node.get("@type")
            if t:
                types.extend(t if isinstance(t, list) else [t])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    for b in blocks:
        try:
            walk(json.loads(b))
        except json.JSONDecodeError:
            types.append("(invalid JSON-LD)")
    return sorted(set(types))


def analyze_page(url):
    status, final_url, html = fetch(url)
    if status is None:
        return {"url": url, "error": html}
    p = PageParser()
    p.feed(html)
    text = " ".join(" ".join(p.text_parts).split())
    host = urllib.parse.urlparse(final_url).netloc
    internal = external = 0
    for href in p.links:
        if href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        h = urllib.parse.urlparse(urllib.parse.urljoin(final_url, href)).netloc
        internal += h == host
        external += h != host
    flags = []
    if len(text) < SHELL_TEXT_THRESHOLD:
        flags.append("Very little visible text in raw HTML: likely client-side rendered, invisible to AI crawlers")
    if not p.title.strip():
        flags.append("Missing <title>")
    if not p.meta.get("description"):
        flags.append("Missing meta description")
    if not p.canonical:
        flags.append("Missing canonical tag")
    if len(p.h1) != 1:
        flags.append(f"{len(p.h1)} H1 tags (expected 1)")
    if "noindex" in p.meta.get("robots", "").lower():
        flags.append("Page is noindex")
    if not p.jsonld:
        flags.append("No JSON-LD structured data")
    return {
        "url": url,
        "final_url": final_url,
        "status": status,
        "html_bytes": len(html),
        "visible_text_chars": len(text),
        "text_sample": text[:200],
        "title": " ".join(p.title.split()),
        "meta_description": p.meta.get("description", ""),
        "meta_robots": p.meta.get("robots", ""),
        "canonical": p.canonical,
        "h1": p.h1,
        "jsonld_types": jsonld_types(p.jsonld),
        "og_title": p.meta.get("og:title", ""),
        "internal_links": internal,
        "external_links": external,
        "flags": flags,
    }


def parse_robots(txt):
    groups, current, seen_rule = {}, [], False
    sitemaps = []
    for raw in txt.splitlines():
        line = raw.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        k, v = (s.strip() for s in line.split(":", 1))
        k = k.lower()
        if k == "user-agent":
            if seen_rule:
                current, seen_rule = [], False
            current.append(v.lower())
            groups.setdefault(v.lower(), [])
        elif k in ("allow", "disallow"):
            seen_rule = True
            for ua in current:
                groups[ua].append((k, v))
        elif k == "sitemap":
            sitemaps.append(v)
    return groups, sitemaps


def crawler_access(groups, bot):
    rules = groups.get(bot.lower())
    source = bot
    if rules is None:
        rules, source = groups.get("*", []), "*"
    if any(k == "disallow" and v == "/" for k, v in rules) and not any(
        k == "allow" and v in ("/", "/*") for k, v in rules
    ):
        return f"BLOCKED (via {source})"
    partial = [v for k, v in rules if k == "disallow" and v]
    if partial:
        return f"allowed, {len(partial)} disallowed paths (via {source})"
    return f"allowed (via {source})" if source != "*" or rules else "allowed (no rules)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--pages", nargs="*", default=[], help="extra paths or URLs to check")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    base = args.url if "://" in args.url else "https://" + args.url
    origin = "{0.scheme}://{0.netloc}".format(urllib.parse.urlparse(base))

    report = {"origin": origin, "pages": [], "robots": {}, "sitemaps": []}
    for u in [base] + [urllib.parse.urljoin(origin, p) for p in args.pages]:
        report["pages"].append(analyze_page(u))

    status, _, robots = fetch(origin + "/robots.txt")
    if status == 200:
        groups, sitemaps = parse_robots(robots)
        report["robots"] = {bot: crawler_access(groups, bot) for bot in CRAWLERS}
        report["sitemaps"] = sitemaps
    else:
        report["robots_error"] = f"robots.txt status {status}: {robots[:120] if status is None else ''}"
    if not report["sitemaps"]:
        s, _, body = fetch(origin + "/sitemap.xml")
        if s == 200 and ("<urlset" in body or "<sitemapindex" in body):
            report["sitemaps"] = [origin + "/sitemap.xml (not referenced in robots.txt)"]

    if args.json:
        print(json.dumps(report, indent=2))
        return

    print(f"# SEO snapshot: {origin}\n")
    for pg in report["pages"]:
        print(f"## {pg['url']}")
        if "error" in pg:
            print(f"  Could not fetch: {pg['error']}\n")
            continue
        for k in ("status", "final_url", "visible_text_chars", "title", "meta_description",
                  "canonical", "meta_robots", "h1", "jsonld_types", "internal_links", "external_links"):
            print(f"  {k}: {pg[k]}")
        print(f"  text_sample: {pg['text_sample']!r}")
        for f in pg["flags"]:
            print(f"  ! {f}")
        print()
    print("## Crawler access (robots.txt)")
    if report["robots"]:
        for bot, v in report["robots"].items():
            print(f"  {bot}: {v}")
    else:
        print(f"  {report.get('robots_error')}")
    print("\n## Sitemaps")
    print("  " + ("\n  ".join(report["sitemaps"]) if report["sitemaps"] else "none found"))


if __name__ == "__main__":
    sys.exit(main())
