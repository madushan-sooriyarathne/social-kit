#!/usr/bin/env python3
"""Voice-of-customer phrase miner (stdlib only).

Usage:
    python3 voc_phrases.py reviews.txt [--top 30] [--min-count 2]

Input: plain text with one review, survey answer or call note per line
(blank-line separated paragraphs also work). Paste from review sites, CSV
exports or transcripts; source labels in square brackets at the start of a
line, like "[TripAdvisor 4*]", are kept with the sentence.

Output (markdown):
  1. Recurring 2 to 4 word phrases, ranked by how many separate entries use them
  2. Candidate sentences sorted into before state (pain), dream state (outcome),
     objections and decision triggers, using cue words

The buckets are a first pass for a human to read, not an analysis. Copy the
strongest exact phrases into the steal sheet with their source.
"""
import argparse
import re
from collections import Counter, defaultdict

STOP = set("""a an the and or but if then so to of in on at for with from by as is are was were be been being it its
this that these those i me my we our us you your he she they them their his her there here
very really just also too not no do does did done have has had will would can could should
about into over after before up down out off than more most some any all each one two get got
""".split())

CUES = {
    "Before state (pain)": [
        "tired of", "frustrat", "struggl", "worried", "stress", "hated", "annoy", "difficult",
        "hard to", "couldn't", "could not", "problem", "disappoint", "fed up", "nightmare",
        "waste", "crowded", "noisy", "confus", "overwhelm", "previous", "before we", "used to",
    ],
    "Dream state (outcome)": [
        "finally", "loved", "love it", "love the", "felt like", "feel like", "made us", "made me", "perfect",
        "exactly what", "so easy", "peace", "relax", "best", "never want", "can't wait", "dream",
        "worth every", "saved", "changed", "highlight", "like home", "came back",
    ],
    "Objections": [
        "almost didn't", "almost did not", "hesitant", "unsure", "not sure", "worried that",
        "expensive", "price", "pricey", "cost", "far from", "too far", "skeptic", "sceptic",
        "doubt", "risk", "afraid", "concern", "wasn't sure", "was not sure",
        "however", "only downside", "the only",
    ],
    "Decision triggers": [
        "decided", "chose", "booked because", "because of", "the reason", "sold me", "convinced",
        "what made", "recommended", "after seeing", "photos", "responded", "quick reply",
        "flexible", "cancellation", "direct",
    ],
}


def entries(text):
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    if len(blocks) <= 1:
        blocks = [l.strip() for l in text.splitlines() if l.strip()]
    return blocks


def ngrams(tokens, n):
    return [" ".join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--min-count", type=int, default=2, help="minimum number of entries a phrase must appear in")
    ap.add_argument("--per-bucket", type=int, default=12)
    a = ap.parse_args()

    text = open(a.file, encoding="utf-8", errors="replace").read()
    items = entries(text)
    print(f"# VoC phrase report: {a.file}\n\nEntries read: {len(items)}\n")

    doc_freq = Counter()
    for it in items:
        body = re.sub(r"^\[[^\]]*\]\s*", "", it)
        toks = re.findall(r"[a-z0-9']+", body.lower())
        seen = set()
        for n in (2, 3, 4):
            for g in ngrams(toks, n):
                parts = g.split()
                if parts[0] in STOP or parts[-1] in STOP:
                    continue
                if all(p in STOP for p in parts):
                    continue
                seen.add(g)
        doc_freq.update(seen)

    # drop phrases fully contained in a longer phrase with the same count
    ranked = [(g, c) for g, c in doc_freq.items() if c >= a.min_count]
    ranked.sort(key=lambda x: (-x[1], -len(x[0])))
    kept = []
    for g, c in ranked:
        if any(g in k and c == kc for k, kc in kept):
            continue
        kept.append((g, c))
        if len(kept) >= a.top:
            break

    print(f"## Recurring phrases (in {a.min_count}+ entries)")
    if kept:
        print("| Phrase | Entries |\n|---|---|")
        for g, c in kept:
            print(f"| {g} | {c} |")
    else:
        print("None at this threshold. Add more entries or lower --min-count.")
    print()

    buckets = defaultdict(list)
    for it in items:
        label = ""
        m = re.match(r"^(\[[^\]]*\])\s*", it)
        if m:
            label = m.group(1) + " "
            it = it[m.end():]
        for sent in re.split(r"(?<=[.!?])\s+", it):
            s = sent.strip()
            if len(s.split()) < 4:
                continue
            low = s.lower()
            for bucket, cues in CUES.items():
                if any(re.search(r"\b" + re.escape(c), low) for c in cues):
                    buckets[bucket].append(label + s)
    for bucket in CUES:
        rows = buckets.get(bucket, [])
        print(f"## {bucket}: {len(rows)} candidate sentences")
        for s in rows[:a.per_bucket]:
            print(f"- {s[:220]}")
        print()
    print("Read the candidates, keep exact wording, and note the source for each phrase you use.")


if __name__ == "__main__":
    main()
