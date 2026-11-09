#!/usr/bin/env python3
"""Sample ratio mismatch (SRM) check for an A/B test. Stdlib only.

Runs a chi-squared goodness-of-fit test of observed assignment counts against the
designed split. Check this before reading any test result: about 6% of Microsoft
experiments had SRM (Fabijan, Vermeer et al., KDD 2019). A p-value below 0.001 is the
common threshold for "do not trust this test".

Usage:
    python3 srm_check.py 10230 9870                 # 50/50 by default
    python3 srm_check.py 10230 9870 --ratio 50 50
    python3 srm_check.py 5100 5020 4880 --ratio 1 1 1
"""

import argparse
import math


def gammaincc(s, x):
    """Regularized upper incomplete gamma Q(s, x)."""
    if x < 0 or s <= 0:
        raise ValueError("invalid arguments")
    if x == 0:
        return 1.0
    gln = math.lgamma(s)
    if x < s + 1:
        # series for P, return 1 - P
        term = total = 1.0 / s
        a = s
        for _ in range(10000):
            a += 1
            term *= x / a
            total += term
            if abs(term) < abs(total) * 1e-15:
                break
        return max(0.0, 1.0 - total * math.exp(-x + s * math.log(x) - gln))
    # continued fraction for Q (Lentz)
    tiny = 1e-300
    b = x + 1 - s
    c = 1 / tiny
    d = 1 / b
    h = d
    for i in range(1, 10000):
        an = -i * (i - s)
        b += 2
        d = an * d + b
        d = tiny if abs(d) < tiny else d
        c = b + an / c
        c = tiny if abs(c) < tiny else c
        d = 1 / d
        delta = d * c
        h *= delta
        if abs(delta - 1) < 1e-15:
            break
    return math.exp(-x + s * math.log(x) - gln) * h


def srm(counts, ratio):
    total = sum(counts)
    rsum = sum(ratio)
    expected = [total * r / rsum for r in ratio]
    chi2 = sum((o - e) ** 2 / e for o, e in zip(counts, expected))
    df = len(counts) - 1
    p = gammaincc(df / 2, chi2 / 2)
    return chi2, df, p, expected


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("counts", nargs="+", type=int, help="observed users or sessions per variant")
    ap.add_argument("--ratio", nargs="+", type=float, help="designed split, e.g. 50 50 (default equal)")
    ap.add_argument("--threshold", type=float, default=0.001)
    a = ap.parse_args()

    if len(a.counts) < 2:
        ap.error("need at least two variants")
    ratio = a.ratio or [1] * len(a.counts)
    if len(ratio) != len(a.counts):
        ap.error("--ratio needs one value per variant")

    chi2, df, p, expected = srm(a.counts, ratio)
    total = sum(a.counts)
    print(f"Total assigned: {total:,}")
    for i, (o, e) in enumerate(zip(a.counts, expected)):
        print(f"  Variant {i}: observed {o:,} ({o / total:.2%}), expected {e:,.0f} ({e / total:.2%})")
    print(f"Chi-squared {chi2:.3f}, df {df}, p = {p:.6g}")
    if p < a.threshold:
        print(f"SRM DETECTED (p < {a.threshold}). Do not trust the result. Check bots, redirects, "
              "consent-dependent tracking, variant errors and assignment logging.")
    else:
        print(f"No SRM at p < {a.threshold}. Proceed to analysis.")


if __name__ == "__main__":
    main()
