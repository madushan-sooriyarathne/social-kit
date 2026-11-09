#!/usr/bin/env python3
"""Score and rank a hypothesis backlog with the PXL framework (CXL). Stdlib only.

Input CSV columns (header row required; yes/no columns accept 1/0, y/n, yes/no, true/false):
    id, hypothesis, evidence,
    above_fold, noticeable_5s, adds_removes, motivation, high_traffic,
    user_testing, qualitative, analytics, mouse_tracking,
    ease_hours

ease_hours is the estimated build time in hours: under 1 = 3 points, 1 to 4 = 2,
4 to 8 = 1, over 8 = 0.

Weights default to the PXL weights in references/testing.md. Recalibrate after 20 to 30
tests by passing a JSON file of weights, e.g. {"user_testing": 1, "analytics": 2}.

Usage:
    python3 pxl_score.py backlog.csv
    python3 pxl_score.py backlog.csv --weights weights.json --out ranked.csv
    python3 pxl_score.py --template > backlog.csv
"""

import argparse
import csv
import json
import sys

WEIGHTS = {
    "above_fold": 1,
    "noticeable_5s": 2,
    "adds_removes": 1,
    "motivation": 1,
    "high_traffic": 1,
    "user_testing": 2,
    "qualitative": 1,
    "analytics": 1,
    "mouse_tracking": 1,
}
TRUE = {"1", "y", "yes", "true", "x"}


def ease_points(hours):
    try:
        h = float(hours)
    except (TypeError, ValueError):
        return 0
    if h < 1:
        return 3
    if h <= 4:
        return 2
    if h <= 8:
        return 1
    return 0


def score(row, weights):
    pts = sum(w for k, w in weights.items() if str(row.get(k, "")).strip().lower() in TRUE)
    return pts + ease_points(row.get("ease_hours")), bool(
        any(str(row.get(k, "")).strip().lower() in TRUE for k in ("user_testing", "qualitative", "analytics", "mouse_tracking"))
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--weights")
    ap.add_argument("--out")
    ap.add_argument("--template", action="store_true", help="print an empty CSV header and one example row")
    a = ap.parse_args()

    cols = ["id", "hypothesis", "evidence", *WEIGHTS.keys(), "ease_hours"]
    if a.template:
        w = csv.writer(sys.stdout)
        w.writerow(cols)
        w.writerow(["H1", "Restate the ad promise in the hero headline", "Meta ads promise private pool; hero says 'Luxury redefined'",
                    1, 1, 0, 1, 1, 0, 1, 1, 0, 1])
        return
    if not a.csv:
        ap.error("pass a backlog CSV or --template")

    weights = dict(WEIGHTS)
    if a.weights:
        with open(a.weights) as f:
            weights.update(json.load(f))

    with open(a.csv, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["pxl_score"], r["has_evidence"] = score(r, weights)
    rows.sort(key=lambda r: (-r["pxl_score"], r.get("id", "")))

    max_score = sum(weights.values()) + 3
    print(f"PXL ranking (max {max_score})\n")
    for i, r in enumerate(rows, 1):
        flag = "" if r["has_evidence"] else "  [no research evidence: move down or gather data]"
        print(f"{i:>2}. {r['pxl_score']:>2}  {r.get('id', ''):<6} {r.get('hypothesis', '')[:80]}{flag}")

    if a.out:
        with open(a.out, "w", newline="") as f:
            fields = list(rows[0].keys()) if rows else cols + ["pxl_score", "has_evidence"]
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
        print(f"\nWrote {a.out}")


if __name__ == "__main__":
    main()
