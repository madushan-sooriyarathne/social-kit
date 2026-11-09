#!/usr/bin/env python3
"""Readability and copy hygiene checker for direct response drafts (stdlib only).

Usage:
    python3 copy_lint.py draft.md [--target-grade 7] [--no-em-dash] [--max-sentence 25]

Input: a markdown file. Sections are split on markdown headings (#, ##, ###).
Lines starting with these labels are treated as email fields and length-checked:
    Subject: ...      (also "Subject A:", "Subject option 1:")
    Preview: ...      (also "Preview text:")
Lines starting with "Headline:" are length-checked as ad or page headlines.

Reports per section: Flesch-Kincaid grade, average sentence length, words.
Flags: long sentences, [VERIFY] markers, filler and marketese, generic CTA labels,
we-vs-you balance, exclamation marks, all-caps words, em dashes (with --no-em-dash).

Heuristic syllable counting, so treat grades as approximate (about +/- 1 grade).
Exit code 0 always; this is a reviewing aid, not a gate.
"""
import argparse
import re
import sys

FILLER = [
    "nestled", "unparalleled", "world-class", "world class", "state-of-the-art",
    "cutting-edge", "cutting edge", "seamless", "seamlessly", "leverage", "synergy",
    "best-in-class", "game-changer", "game changing", "revolutionary", "look no further",
    "in today's world", "in today's fast-paced", "elevate your", "unlock the power",
    "take it to the next level", "one-stop shop", "second to none", "like never before",
    "boasts", "a myriad of", "plethora", "unique experience", "hidden gem",
    "luxurious experience", "breathtaking", "tranquil oasis", "paradise awaits",
    "robust", "innovative solution", "all-in-one solution", "empower",
]
GENERIC_CTA = ["submit", "click here", "learn more", "read more", "find out more",
               "send", "go", "continue", "more info", "enter"]
WE_WORDS = {"we", "our", "us", "we're", "we've", "ours"}
YOU_WORDS = {"you", "your", "you're", "you'll", "yours", "you've"}

FIELD_RE = re.compile(r"^\s*[-*]?\s*\**(subject(?: (?:line|option))?(?: ?[a-z0-9]+)?|preview(?: text)?|headline)\**\s*:\s*(.+)$", re.I)
CTA_RE = re.compile(r"\[CTA:\s*([^\]>→]+?)\s*(?:→|->|\])", re.I)


def syllables(word):
    w = word.lower()
    w = re.sub(r"[^a-z]", "", w)
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    groups = re.findall(r"[aeiouy]{1,2}", w)
    return max(1, len(groups))


def strip_markdown(text):
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\*\[[^\]]*\]\*", " ", text)  # image and proof slots
    text = re.sub(r"\[(CTA|Image|Proof|VERIFY)[^\]]*\]", " ", text, flags=re.I)
    text = re.sub(r"[*_#>|]", " ", text)
    return text


def sentences(text):
    text = strip_markdown(text)
    # treat list items and line breaks as sentence boundaries
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    out = []
    for p in parts:
        p = p.strip(" -\t")
        if len(re.findall(r"[A-Za-z']+", p)) >= 3:
            out.append(p)
    return out


def grade(sents):
    words = [w for s in sents for w in re.findall(r"[A-Za-z']+", s)]
    if not sents or not words:
        return None, 0, 0
    syl = sum(syllables(w) for w in words)
    asl = len(words) / len(sents)
    asw = syl / len(words)
    fk = 0.39 * asl + 11.8 * asw - 15.59
    return round(fk, 1), round(asl, 1), len(words)


def split_sections(lines):
    sections = []
    title, buf = "(top)", []
    for line in lines:
        m = re.match(r"^(#{1,4})\s+(.*)", line)
        if m:
            if buf:
                sections.append((title, buf))
            title, buf = m.group(2).strip(), []
        else:
            buf.append(line)
    if buf:
        sections.append((title, buf))
    return sections


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--target-grade", type=float, default=7.0)
    ap.add_argument("--max-sentence", type=int, default=25, help="flag sentences longer than this many words")
    ap.add_argument("--no-em-dash", action="store_true", help="flag em dashes")
    args = ap.parse_args()

    try:
        raw = open(args.file, encoding="utf-8").read()
    except OSError as e:
        sys.exit(f"Cannot read {args.file}: {e}")
    lines = raw.splitlines()

    print(f"# copy_lint report: {args.file}\n")

    # Section readability
    print(f"## Readability (target grade {args.target_grade:g} or lower)")
    print("| Section | Grade | Avg sentence | Words | Flag |")
    print("|---|---|---|---|---|")
    all_sents = []
    for title, buf in split_sections(lines):
        body = "\n".join(l for l in buf if not FIELD_RE.match(l))
        s = sentences(body)
        g, asl, n = grade(s)
        all_sents.extend(s)
        if g is None:
            continue
        flag = "above target" if g > args.target_grade + 0.5 else ""
        print(f"| {title[:50]} | {g} | {asl} | {n} | {flag} |")
    g, asl, n = grade(all_sents)
    if g is not None:
        print(f"| **Whole draft** | **{g}** | {asl} | {n} | {'above target' if g > args.target_grade + 0.5 else ''} |")
    print()

    # Long sentences
    longs = [s for s in all_sents if len(re.findall(r"[A-Za-z']+", s)) > args.max_sentence]
    print(f"## Long sentences (> {args.max_sentence} words): {len(longs)}")
    for s in longs[:10]:
        print(f"- ({len(re.findall(r'[A-Za-z]+', s))} words) {s[:160]}")
    print()

    # Fields
    fields = []
    for i, line in enumerate(lines, 1):
        m = FIELD_RE.match(line)
        if m:
            kind = m.group(1).lower()
            val = m.group(2).strip().strip('"*')
            fields.append((i, kind, val))
    if fields:
        print("## Subject lines, preview text and headlines")
        print("| Line | Field | Chars | Words | Note | Text |")
        print("|---|---|---|---|---|---|")
        for i, kind, val in fields:
            chars, words = len(val), len(val.split())
            note = ""
            if kind.startswith("subject"):
                if chars > 60:
                    note = "long: key words may truncate on mobile"
                if re.search(r"welcome to", val, re.I):
                    note = (note + "; " if note else "") + "generic welcome (Geisler)"
            elif kind.startswith("preview"):
                if chars < 30:
                    note = "short: client may fill with body text"
                elif chars > 110:
                    note = "long: will truncate"
            elif kind == "headline" and words < 3:
                note = "very short: does it say something specific?"
            print(f"| {i} | {kind} | {chars} | {words} | {note} | {val[:70]} |")
        print()

    # Flags
    text_lower = raw.lower()
    print("## Flags")
    verify = re.findall(r"\[VERIFY[^\]]*\]", raw, re.I)
    print(f"- [VERIFY] markers: {len(verify)}" + (" (resolve before launch)" if verify else ""))
    for v in verify[:15]:
        print(f"  - {v}")

    hits = []
    for f in FILLER:
        c = len(re.findall(r"\b" + re.escape(f) + r"\b", text_lower))
        if c:
            hits.append(f"{f} ×{c}")
    print(f"- Filler and marketese: {', '.join(hits) if hits else 'none found'}")

    ctas = CTA_RE.findall(raw)
    generic = [c for c in ctas if c.strip().lower().rstrip('.!') in GENERIC_CTA]
    print(f"- CTAs found: {len(ctas)}" + (f"; generic labels: {', '.join(generic)} (name the outcome instead)" if generic else ""))

    words = re.findall(r"[a-z']+", text_lower)
    we = sum(1 for w in words if w in WE_WORDS)
    you = sum(1 for w in words if w in YOU_WORDS)
    ratio = f"{you}:{we}"
    note = " (more about the brand than the reader)" if we > you else ""
    print(f"- You-to-we ratio: {ratio}{note}")

    excl = raw.count("!")
    print(f"- Exclamation marks: {excl}" + (" (use sparingly)" if excl > 3 else ""))

    caps = [w for w in re.findall(r"\b[A-Z]{4,}\b", raw) if w not in {"VERIFY", "CTA", "FAQ", "HTML", "WHATSAPP", "SAAS", "URL", "GDPR", "PECR"}]
    if caps:
        print(f"- All-caps words: {', '.join(sorted(set(caps))[:10])}")

    if args.no_em_dash:
        em = raw.count("\u2014")
        en = raw.count("\u2013")
        print(f"- Em dashes: {em}" + (" (restructure these sentences)" if em else ""))
        if en:
            print(f"- En dashes: {en} (check none are used as em dashes)")


if __name__ == "__main__":
    main()
