#!/usr/bin/env python3
"""A/B test helper for copy tests (stdlib only).

Subcommands:
  size    Sample size per variant and duration, before launch.
          python3 ab_test_calc.py size --baseline 0.048 --mde 0.012 [--daily 300] [--variants 2] [--alpha 0.05] [--power 0.8]
          --baseline  current conversion or click rate as a decimal (0.048 = 4.8%)
          --mde       smallest absolute difference worth detecting (0.012 = 1.2 points)
          --relative  treat --mde as a relative lift instead (0.25 = +25%)
          --daily     visitors (or recipients, impressions) per variant per day, for duration

  srm     Sample ratio mismatch check on the traffic split, during or after the test.
          python3 ab_test_calc.py srm 5012 4890 [--expected 50 50]

  result  Evaluate once, at the planned sample size (no peeking).
          python3 ab_test_calc.py result <conv_A> <n_A> <conv_B> <n_B> [--alpha 0.05]

Notes:
- Evan Miller's rule of thumb (n = 16 p(1-p) / d^2, alpha 0.05, power 0.8) is printed
  alongside the normal-approximation formula.
- Duration is rounded up to whole weeks so weekday and weekend behaviour both count.
- Checking a running test repeatedly and stopping at the first significant reading
  inflates false positives (Miller: 10 peeks turn an apparent 1% into a real 5%).
"""
import argparse
import math
import sys
from statistics import NormalDist

Z = NormalDist()


def cmd_size(a):
    p1 = a.baseline
    if not 0 < p1 < 1:
        sys.exit("--baseline must be between 0 and 1 (e.g. 0.048)")
    d = p1 * a.mde if a.relative else a.mde
    p2 = p1 + d
    if not 0 < p2 < 1 or d == 0:
        sys.exit("baseline plus mde must stay between 0 and 1, and mde must be non-zero")
    # Bonferroni for multiple variants vs control
    comparisons = max(1, a.variants - 1)
    alpha = a.alpha / comparisons
    za = Z.inv_cdf(1 - alpha / 2)
    zb = Z.inv_cdf(a.power)
    pbar = (p1 + p2) / 2
    n = ((za * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2) / d ** 2
    n = math.ceil(n)
    miller = math.ceil(16 * p1 * (1 - p1) / d ** 2)

    print(f"Baseline {p1:.2%}, target {p2:.2%} (absolute difference {d:+.2%}, relative {d / p1:+.1%})")
    print(f"Alpha {a.alpha} two-sided" + (f", Bonferroni-adjusted to {alpha:.4f} for {a.variants} variants" if comparisons > 1 else "") + f", power {a.power}")
    print(f"Sample per variant: {n:,}  (Miller rule of thumb: {miller:,})")
    print(f"Total across {a.variants} variants: {n * a.variants:,}")
    print(f"Expected conversions per variant at baseline: {round(n * p1):,}")
    if a.daily:
        days = math.ceil(n / a.daily)
        weeks = max(1, math.ceil(days / 7))
        print(f"At {a.daily:,} per variant per day: {days} days, run {weeks} full week(s) ({weeks * 7} days)")
        if weeks > 8:
            print("Warning: longer than about 8 weeks. Consider a bigger change (angle or offer), a higher-traffic page,"
                  " or qualitative validation instead of a weak test.")
    print("Decide the stop date now and evaluate once at that sample.")


def chi2_sf_df(x, df):
    # survival function for chi-square, df small: use regularized gamma via series
    if df == 1:
        return math.erfc(math.sqrt(x / 2))
    k = df / 2.0
    xx = x / 2.0
    # lower regularized gamma by series
    term = 1.0 / k
    s = term
    for i in range(1, 500):
        term *= xx / (k + i)
        s += term
        if term < 1e-15 * s:
            break
    lower = s * math.exp(-xx + k * math.log(xx) - math.lgamma(k))
    return max(0.0, 1.0 - lower)


def cmd_srm(a):
    counts = a.counts
    if len(counts) < 2:
        sys.exit("give at least two counts")
    exp_w = a.expected or [1] * len(counts)
    if len(exp_w) != len(counts):
        sys.exit("--expected needs one weight per count")
    total = sum(counts)
    wsum = sum(exp_w)
    expected = [total * w / wsum for w in exp_w]
    x = sum((o - e) ** 2 / e for o, e in zip(counts, expected))
    p = chi2_sf_df(x, len(counts) - 1)
    for i, (o, e) in enumerate(zip(counts, expected)):
        print(f"Variant {chr(65 + i)}: observed {o:,}, expected {e:,.0f} ({o / total:.2%} of traffic)")
    print(f"Chi-square {x:.3f}, p = {p:.5f}")
    if p < 0.001:
        print("Sample ratio mismatch (p < 0.001): the split is broken. Find the cause (redirects, bot filtering,"
              " tracking firing differently per variant) and discard this test's result.")
    else:
        print("No sample ratio mismatch detected.")


def cmd_result(a):
    ca, na, cb, nb = a.conv_a, a.n_a, a.conv_b, a.n_b
    if min(na, nb) <= 0 or ca > na or cb > nb:
        sys.exit("check inputs: conversions must not exceed visitors")
    pa, pb = ca / na, cb / nb
    pool = (ca + cb) / (na + nb)
    se0 = math.sqrt(pool * (1 - pool) * (1 / na + 1 / nb))
    z = (pb - pa) / se0 if se0 else 0
    p = 2 * (1 - Z.cdf(abs(z)))
    se = math.sqrt(pa * (1 - pa) / na + pb * (1 - pb) / nb)
    zc = Z.inv_cdf(1 - a.alpha / 2)
    lo, hi = (pb - pa) - zc * se, (pb - pa) + zc * se
    print(f"A: {ca:,}/{na:,} = {pa:.2%}")
    print(f"B: {cb:,}/{nb:,} = {pb:.2%}")
    rel = (pb - pa) / pa if pa else float('nan')
    print(f"Difference B - A: {pb - pa:+.2%} absolute, {rel:+.1%} relative")
    print(f"{int((1 - a.alpha) * 100)}% CI for the difference: {lo:+.2%} to {hi:+.2%}")
    print(f"z = {z:.2f}, p = {p:.4f}")
    if p < a.alpha:
        print(f"Significant at alpha {a.alpha}. Valid only if this is the pre-planned sample and stop date.")
    else:
        print("Not significant. Treat as no detectable difference at this sample; keep the control or test a bigger change.")
    if min(ca, cb) < 30:
        print("Caution: fewer than 30 conversions in a variant; the result is fragile.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("size")
    s.add_argument("--baseline", type=float, required=True)
    s.add_argument("--mde", type=float, required=True)
    s.add_argument("--relative", action="store_true")
    s.add_argument("--daily", type=int)
    s.add_argument("--variants", type=int, default=2)
    s.add_argument("--alpha", type=float, default=0.05)
    s.add_argument("--power", type=float, default=0.8)

    r = sub.add_parser("srm")
    r.add_argument("counts", type=int, nargs="+")
    r.add_argument("--expected", type=float, nargs="+")

    t = sub.add_parser("result")
    t.add_argument("conv_a", type=int)
    t.add_argument("n_a", type=int)
    t.add_argument("conv_b", type=int)
    t.add_argument("n_b", type=int)
    t.add_argument("--alpha", type=float, default=0.05)

    a = ap.parse_args()
    {"size": cmd_size, "srm": cmd_srm, "result": cmd_result}[a.cmd](a)


if __name__ == "__main__":
    main()
