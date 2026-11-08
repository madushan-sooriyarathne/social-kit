#!/usr/bin/env python3
"""Check a page draft for keyword placement and on-page basics.

Stdlib only. Usage:
    python3 copy_check.py page.md [--range 600-1200] [--no-em-dash]

Draft format: a header block of "Field: value" lines, a line containing only
"---", then the page copy in markdown (one "# " H1, "## " and "### " headings).

    URL: /private-pool-villa-hikkaduwa
    Title: Private Pool Villa in Hikkaduwa (Sleeps 6) | Tropical House
    Meta: Book a private pool villa in Hikkaduwa, eight minutes from the beach...
    Primary: private pool villa hikkaduwa
    Secondary: villa with pool hikkaduwa, hikkaduwa villa rental, family villa hikkaduwa
    Questions: how far is the villa from the beach? | is breakfast included?
    ---
    # Private Pool Villa in Hikkaduwa
    Body copy...

Secondary is comma separated; Questions is separated by "|".
Matching is case and punctuation insensitive. "exact" means the phrase appears
as written; "variant" means every meaningful word appears in the zone (simple
plural folding). Exit code 1 when any check FAILs.
"""
import argparse
import re
import sys

STOP = {
    "a", "an", "the", "in", "on", "at", "for", "of", "to", "and", "or", "with",
    "near", "by", "from", "is", "are", "your", "my", "our", "best", "vs",
}


def norm(text):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", text.lower())).strip()


def fold(word):
    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def tokens(text):
    return [fold(w) for w in norm(text).split()]


def key_tokens(phrase):
    toks = [t for t in tokens(phrase) if t not in STOP]
    return toks or tokens(phrase)


def match(phrase, text):
    """Return 'exact', 'variant' or 'missing'."""
    if not phrase or not text:
        return "missing"
    if re.search(r"\b" + re.escape(norm(phrase)) + r"\b", norm(text)):
        return "exact"
    have = set(tokens(text))
    if all(t in have for t in key_tokens(phrase)):
        return "variant"
    return "missing"


def count_exact(phrase, text):
    return len(re.findall(r"\b" + re.escape(norm(phrase)) + r"\b", norm(text)))


def parse(path):
    raw = open(path, encoding="utf-8").read()
    if "\n---\n" not in raw:
        sys.exit("Draft needs a header block, then a line with only ---, then the copy.")
    head, body = raw.split("\n---\n", 1)
    meta = {}
    for line in head.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip().lower()] = v.strip()
    return meta, body


def structure(body):
    h1, subs, paras = [], [], []
    current_heading = None
    first_para_after = {}
    buf = []

    def flush():
        if buf:
            para = " ".join(buf).strip()
            paras.append(para)
            if current_heading is not None and current_heading not in first_para_after:
                first_para_after[current_heading] = para
            buf.clear()

    for line in body.splitlines():
        s = line.strip()
        if s.startswith("# "):
            flush()
            h1.append(s[2:].strip())
            current_heading = None
        elif re.match(r"#{2,6} ", s):
            flush()
            text = s.lstrip("#").strip()
            subs.append(text)
            current_heading = len(subs) - 1
        elif not s:
            flush()
        else:
            buf.append(re.sub(r"^[-*+]\s+|^\d+\.\s+", "", s))
    flush()
    return h1, subs, paras, first_para_after


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--range", help="target word range from the SERP, e.g. 600-1200")
    ap.add_argument("--no-em-dash", action="store_true", help="flag em and en dashes")
    args = ap.parse_args()

    meta, body = parse(args.draft)
    primary = meta.get("primary", "")
    title = meta.get("title", "")
    desc = meta.get("meta", "")
    url = meta.get("url", "")
    secondaries = [s.strip() for s in meta.get("secondary", "").split(",") if s.strip()]
    questions = [q.strip() for q in meta.get("questions", "").split("|") if q.strip()]

    h1, subs, paras, first_after = structure(body)
    body_text = " ".join(paras)
    all_text = " ".join(h1 + subs + paras)
    words = norm(body_text).split()
    results = []

    def add(level, msg):
        results.append((level, msg))

    if not primary:
        add("FAIL", "No Primary keyword in the header block")

    # Zones
    slug_toks = set(fold(t) for t in re.split(r"[-/_.]+", url.lower()) if t)
    if url and primary:
        missing = [t for t in key_tokens(primary) if t not in slug_toks]
        add("PASS" if not missing else "WARN",
            f"URL slug {'contains' if not missing else 'is missing'} primary words"
            + (f": {', '.join(missing)}" if missing else ""))
    elif not url:
        add("WARN", "No URL in header")

    for zone, text in (("Title", title), ("H1", h1[0] if h1 else "")):
        m = match(primary, text)
        add({"exact": "PASS", "variant": "PASS", "missing": "FAIL"}[m],
            f"{zone}: primary keyword {m}")

    opening = " ".join(words[:150])
    m = match(primary, opening)
    add("PASS" if m != "missing" else "FAIL", f"First 150 words: primary keyword {m}")

    # Title, meta, H1
    tl = len(title)
    if not title:
        add("FAIL", "No Title in header")
    elif tl > 60 or tl < 30:
        add("WARN", f"Title is {tl} chars (aim for about 50 to 60; too long or short gets rewritten)")
    else:
        add("PASS", f"Title is {tl} chars")
    if "[" in title or "]" in title:
        add("WARN", "Title uses brackets; parentheses are removed less often")
    if primary and title and norm(primary) in norm(title):
        pos = norm(title).find(norm(primary))
        if pos > len(norm(title)) / 2:
            add("INFO", "Primary sits in the second half of the title; front-load it if it reads naturally")

    dl = len(desc)
    if not desc:
        add("WARN", "No Meta description")
    elif dl > 160 or dl < 100:
        add("WARN", f"Meta description is {dl} chars (aim for about 120 to 155)")
    else:
        add("PASS", f"Meta description is {dl} chars")

    if len(h1) != 1:
        add("FAIL", f"Found {len(h1)} H1 headings; use exactly one")
    if h1 and title:
        a, b = set(key_tokens(title)), set(key_tokens(h1[0]))
        overlap = len(a & b) / max(1, len(a | b))
        if overlap < 0.3:
            add("INFO", "Title and H1 differ a lot; closer matching reduces title rewrites")

    # Headings
    if subs and primary:
        exact_heads = sum(1 for s in subs if count_exact(primary, s))
        if exact_heads >= 3 or (len(subs) >= 2 and exact_heads / len(subs) > 0.5):
            add("WARN", f"Primary repeated exactly in {exact_heads} of {len(subs)} subheadings; use variations")
        else:
            add("PASS", f"Subheadings vary the keyword ({exact_heads} of {len(subs)} exact)")
    elif not subs:
        add("WARN", "No H2 or H3 subheadings")

    # Density (stuffing guard only, not a target)
    if primary and words:
        n = count_exact(primary, body_text)
        density = n * len(norm(primary).split()) / len(words) * 100
        if n == 0:
            add("INFO", "Primary phrase never appears verbatim; fine when natural variants cover it")
        else:
            level = "WARN" if density > 2.5 else "INFO"
            add(level, f"Primary used verbatim {n} times ({density:.1f}% of words)"
                + ("; read for stuffing" if level == "WARN" else "; no target exists, this is a stuffing check"))

    # Secondaries and questions
    for s in secondaries:
        m = match(s, all_text)
        add("PASS" if m != "missing" else "WARN", f"Secondary '{s}': {m}")
    for q in questions:
        qt = set(key_tokens(q))
        best = max((len(qt & set(key_tokens(h))) / max(1, len(qt)) for h in subs), default=0)
        add("PASS" if best >= 0.6 else "WARN",
            f"Question '{q}': {'covered by a heading' if best >= 0.6 else 'no matching heading'}")

    # Snippet-ready answers under question headings
    for i, s in enumerate(subs):
        if s.endswith("?"):
            para = first_after.get(i, "")
            n = len(para.split())
            if n == 0:
                add("WARN", f"'{s}' has no answer paragraph")
            elif n < 25 or n > 70:
                add("INFO", f"'{s}' opens with {n} words; about 40 to 50 suits snippets and AI answers")

    # Length
    wc = len(words)
    if args.range:
        lo, hi = (int(x) for x in args.range.split("-"))
        add("PASS" if lo <= wc <= hi else "WARN", f"Word count {wc} (SERP range {lo} to {hi})")
    else:
        add("INFO", f"Word count {wc}")

    # Hygiene
    verify = len(re.findall(r"\[VERIFY", body + title + desc))
    if verify:
        add("WARN", f"{verify} [VERIFY] markers to resolve before publishing")
    if args.no_em_dash:
        dashes = len(re.findall(r"\u2014|\s\u2013\s", body + title + desc))
        add("PASS" if not dashes else "FAIL", f"Em or spaced en dashes: {dashes}")

    order = {"FAIL": 0, "WARN": 1, "INFO": 2, "PASS": 3}
    for level, msg in sorted(results, key=lambda r: order[r[0]]):
        print(f"{level:5} {msg}")
    fails = sum(1 for l, _ in results if l == "FAIL")
    warns = sum(1 for l, _ in results if l == "WARN")
    print(f"\n{fails} fail, {warns} warn")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
