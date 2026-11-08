#!/usr/bin/env python3
"""Scan a website's imagery and visual identity for an art direction audit.

Stdlib only. Usage:
    python3 brand_visual_scan.py https://example.com [--pages /rooms /about] [--measure 40]

Reports per page and overall:
- images found in server HTML (img, picture/srcset, og:image, inline background images)
- alt text coverage
- stock-library hints in image URLs (unsplash, pexels, shutterstock, istock, getty, adobe stock)
- video presence (video tags, YouTube, Vimeo, Wistia embeds)
- social profile links
- theme colour, most frequent CSS hex colours, Google Fonts families
- a hint when the page looks client-rendered (few images or text in raw HTML)
With --measure N, fetches the first bytes of up to N images and reports pixel sizes and
the landscape / portrait / square split, which shows whether vertical assets exist.
"""

import argparse
import collections
import re
import ssl
import struct
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser

UA = "Mozilla/5.0 (compatible; art-direction-scan/1.0)"
STOCK_HINTS = ["unsplash", "pexels", "shutterstock", "istockphoto", "istock", "gettyimages",
               "stock.adobe", "adobestock", "depositphotos", "dreamstime", "freepik", "123rf", "pixabay"]
SOCIAL = {"instagram.com": "Instagram", "tiktok.com": "TikTok", "youtube.com": "YouTube",
          "youtu.be": "YouTube", "facebook.com": "Facebook", "linkedin.com": "LinkedIn",
          "pinterest.": "Pinterest", "vimeo.com": "Vimeo", "x.com": "X", "twitter.com": "X"}
VIDEO_HOSTS = ["youtube.com/embed", "youtube-nocookie.com", "player.vimeo.com", "wistia", "vidyard"]


def fetch(url, max_bytes=3_000_000, range_bytes=None):
    headers = {"User-Agent": UA}
    if range_bytes:
        headers["Range"] = f"bytes=0-{range_bytes - 1}"
    req = urllib.request.Request(url, headers=headers)
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=20, context=ctx) as resp:
        data = resp.read(range_bytes or max_bytes)
        ctype = resp.headers.get("Content-Type", "")
    return data, ctype


class PageParser(HTMLParser):
    def __init__(self, base):
        super().__init__(convert_charrefs=True)
        self.base = base
        self.images = []  # dicts: src, alt, kind
        self.links = []
        self.videos = []
        self.stylesheets = []
        self.inline_css = []
        self.meta = {}
        self.text_chars = 0
        self.script_count = 0
        self._in_style = False
        self._in_script = False

    def abs(self, u):
        return urllib.parse.urljoin(self.base, u.strip()) if u else ""

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        style = a.get("style", "")
        for m in re.findall(r"url\(['\"]?([^'\")]+)['\"]?\)", style):
            if not m.startswith(("data:", "#")):
                self.images.append({"src": self.abs(m), "alt": None, "kind": "css-bg"})
        if tag == "img":
            src = a.get("src") or a.get("data-src") or ""
            if not src or src.startswith("data:"):
                srcset = a.get("srcset") or a.get("data-srcset") or ""
                src = srcset.split(",")[-1].strip().split(" ")[0] if srcset else src
            if src and not src.startswith("data:"):
                self.images.append({"src": self.abs(src), "alt": a.get("alt"), "kind": "img",
                                    "w": a.get("width"), "h": a.get("height")})
        elif tag == "source" and a.get("srcset") and a.get("type", "").startswith("image"):
            pass  # picture sources duplicate the img fallback
        elif tag == "meta":
            key = (a.get("property") or a.get("name") or "").lower()
            if key in ("og:image", "twitter:image", "theme-color", "og:video", "description"):
                self.meta.setdefault(key, a.get("content", ""))
                if key in ("og:image", "twitter:image") and a.get("content"):
                    self.images.append({"src": self.abs(a["content"]), "alt": None, "kind": key})
        elif tag == "a" and a.get("href"):
            self.links.append(self.abs(a["href"]))
        elif tag in ("video", "iframe"):
            src = a.get("src") or a.get("data-src") or ""
            if tag == "video" or any(h in src for h in VIDEO_HOSTS):
                self.videos.append(tag + ": " + (self.abs(src) if src else "(source child)"))
        elif tag == "link":
            rel = a.get("rel", "").lower()
            if "stylesheet" in rel and a.get("href"):
                self.stylesheets.append(self.abs(a["href"]))
        elif tag == "style":
            self._in_style = True
        elif tag == "script":
            self._in_script = True
            self.script_count += 1

    def handle_endtag(self, tag):
        if tag == "style":
            self._in_style = False
        elif tag == "script":
            self._in_script = False

    def handle_data(self, data):
        if self._in_style:
            self.inline_css.append(data)
        elif not self._in_script:
            self.text_chars += len(data.strip())


def image_size(data):
    """Return (w, h) from the first bytes of PNG, GIF, JPEG or WebP data, else None."""
    try:
        if data[:8] == b"\x89PNG\r\n\x1a\n":
            return struct.unpack(">II", data[16:24])
        if data[:6] in (b"GIF87a", b"GIF89a"):
            return struct.unpack("<HH", data[6:10])
        if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
            chunk = data[12:16]
            if chunk == b"VP8 ":
                w, h = struct.unpack("<HH", data[26:30])
                return w & 0x3FFF, h & 0x3FFF
            if chunk == b"VP8L":
                b = data[21:25]
                w = 1 + (((b[1] & 0x3F) << 8) | b[0])
                h = 1 + (((b[3] & 0xF) << 10) | (b[2] << 2) | ((b[1] & 0xC0) >> 6))
                return w, h
            if chunk == b"VP8X":
                w = 1 + int.from_bytes(data[24:27], "little")
                h = 1 + int.from_bytes(data[27:30], "little")
                return w, h
        if data[:2] == b"\xff\xd8":
            i = 2
            while i < len(data) - 9:
                if data[i] != 0xFF:
                    i += 1
                    continue
                marker = data[i + 1]
                if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                    h, w = struct.unpack(">HH", data[i + 5:i + 9])
                    return w, h
                seg = struct.unpack(">H", data[i + 2:i + 4])[0]
                i += 2 + seg
    except (struct.error, IndexError):
        return None
    return None


def css_colours(css_texts):
    counter = collections.Counter()
    for css in css_texts:
        for m in re.findall(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", css):
            h = m.lower()
            if len(h) == 3:
                h = "".join(c * 2 for c in h)
            counter["#" + h] += 1
    return counter


def fonts(css_texts, links):
    fams = set()
    for u in links:
        if "fonts.googleapis.com" in u:
            for fam in re.findall(r"family=([^&:]+)", urllib.parse.unquote(u)):
                fams.add(fam.replace("+", " "))
    for css in css_texts:
        for fam in re.findall(r"font-family\s*:\s*([^;}{]+)", css):
            first = fam.split(",")[0].strip().strip("'\"")
            if first and not first.startswith("var("):
                fams.add(first)
    return sorted(fams)[:12]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("--pages", nargs="*", default=[], help="extra paths or URLs to scan")
    ap.add_argument("--measure", type=int, default=0, help="fetch headers of up to N images to read pixel sizes")
    args = ap.parse_args()

    base = args.url if args.url.startswith("http") else "https://" + args.url
    targets = [base] + [urllib.parse.urljoin(base, p) for p in args.pages]
    all_images, all_links, all_videos, css_texts, sheet_urls = [], [], [], [], []
    meta_home = {}

    for url in targets:
        print(f"\n=== {url}")
        try:
            data, ctype = fetch(url)
        except Exception as e:  # noqa: BLE001
            print(f"  ERROR fetching: {e}")
            continue
        html = data.decode("utf-8", errors="replace")
        p = PageParser(url)
        p.feed(html)
        if url == base:
            meta_home = p.meta
        imgs = p.images
        with_alt = [i for i in imgs if i["kind"] == "img" and i.get("alt")]
        img_tags = [i for i in imgs if i["kind"] == "img"]
        print(f"  images in server HTML: {len(imgs)} (img tags {len(img_tags)}, "
              f"css backgrounds {sum(1 for i in imgs if i['kind'] == 'css-bg')})")
        if img_tags:
            print(f"  alt text present: {len(with_alt)}/{len(img_tags)}")
        print(f"  videos/embeds: {len(p.videos)}")
        print(f"  visible text chars: {p.text_chars}, scripts: {p.script_count}")
        if len(img_tags) < 3 and p.script_count > 5:
            print("  NOTE: few images in raw HTML with many scripts; page may be client-rendered. "
                  "Check visually in a browser.")
        all_images += imgs
        all_links += p.links
        all_videos += p.videos
        css_texts += p.inline_css
        sheet_urls += p.stylesheets

    for s in list(dict.fromkeys(sheet_urls))[:4]:
        try:
            d, _ = fetch(s, max_bytes=1_500_000)
            css_texts.append(d.decode("utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            pass

    uniq = list({i["src"]: i for i in all_images}.values())
    print("\n=== Overall")
    print(f"unique images: {len(uniq)}")
    stock = [i["src"] for i in uniq if any(h in i["src"].lower() for h in STOCK_HINTS)]
    print(f"stock-library hints in URLs: {len(stock)}")
    for s in stock[:8]:
        print(f"  {s}")
    print(f"videos/embeds: {len(set(all_videos))}")
    for v in list(dict.fromkeys(all_videos))[:8]:
        print(f"  {v}")
    socials = collections.OrderedDict()
    for l in all_links:
        for host, name in SOCIAL.items():
            if host in l and "share" not in l and "intent" not in l:
                socials.setdefault(name, l)
    print("social profiles:", "none found" if not socials else "")
    for name, l in socials.items():
        print(f"  {name}: {l}")
    for k in ("theme-color", "og:image", "description"):
        if meta_home.get(k):
            print(f"{k}: {meta_home[k][:160]}")
    cols = css_colours(css_texts)
    print("top CSS colours:", ", ".join(f"{c} ({n})" for c, n in cols.most_common(10)) or "none found")
    fams = fonts(css_texts, sheet_urls)
    print("fonts:", ", ".join(fams) or "none found")

    print("\n=== Image list (first 40)")
    for i in uniq[:40]:
        alt = i.get("alt")
        alt_s = "(no alt)" if not alt else alt[:70]
        print(f"  [{i['kind']}] {i['src'][:120]} | {alt_s}")

    if args.measure:
        print(f"\n=== Pixel sizes (up to {args.measure})")
        shapes = collections.Counter()
        small = 0
        for i in uniq[:args.measure]:
            src = i["src"]
            if src.lower().split("?")[0].endswith(".svg"):
                continue
            try:
                d, _ = fetch(src, range_bytes=65536)
                size = image_size(d)
            except Exception as e:  # noqa: BLE001
                print(f"  ? {src[:100]} ({e.__class__.__name__})")
                continue
            if not size:
                print(f"  ? {src[:100]} (unknown format)")
                continue
            w, h = size
            r = w / h if h else 0
            shape = "square" if 0.9 <= r <= 1.1 else ("landscape" if r > 1.1 else "portrait")
            shapes[shape] += 1
            if max(w, h) < 1200:
                small += 1
            print(f"  {w}x{h} {shape} ratio {r:.2f} | {src[:100]}")
        print(f"shape split: {dict(shapes)}; images under 1200 px on the long edge: {small}")
        if shapes and shapes.get("portrait", 0) == 0:
            print("NOTE: no portrait images found; vertical assets for social may be missing.")


if __name__ == "__main__":
    sys.exit(main())
