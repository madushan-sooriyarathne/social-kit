#!/usr/bin/env python3
"""Sample size, test duration and traffic tier for a conversion-rate A/B test.

Stdlib only.

Fixed-horizon sample size per variant (two-sided, two-proportion z-test):
    n = (z_{1-a/2} * sqrt(2 p_bar (1 - p_bar)) + z_{1-b} * sqrt(p1(1-p1) + p2(1-p2)))^2 / (p2 - p1)^2
This is the exact form of the 16 p(1-p)/delta^2 rule of thumb (Kohavi, Deng, Vermeer)
at 80% power and alpha 0.05.

Sequential estimate: Evan Miller's simple sequential test (winner when treatment
conversions exceed control by 2*sqrt(N); stop with no winner when total conversions
reach N). N is estimated with a Brownian-motion approximation; confirm with Miller's
online calculator before relying on it.

Usage:
    python3 sample_size.py --baseline 0.02 --mde 0.2 --monthly-sessions 3000
    python3 sample_size.py --baseline 0.035 --monthly-sessions 12000 --traffic-share 0.5
    python3 sample_size.py --baseline 0.02 --mde 0.3 --monthly-sessions 3000 --json

--baseline         current conversion rate as a fraction (0.02 = 2%)
--mde              relative minimum detectable effect (0.2 = 20% lift); if omitted, a table
                   for 5%, 10%, 20%, 30% and 50% is printed
--monthly-sessions sessions per month reaching the tested page
--traffic-share    share of those sessions entering the test (default 1.0)
--power            default 0.8
--alpha            two-sided, default 0.05
"""

import argparse
import json
import math
from statistics import NormalDist

N01 = NormalDist()
WEEKS_PER_MONTH = 52 / 12


def per_variant_n(p1, rel_mde, alpha=0.05, power=0.8):
    p2 = p1 * (1 + rel_mde)
    if not 0 < p1 < 1 or not 0 < p2 < 1:
        raise ValueError("baseline and baseline*(1+mde) must be between 0 and 1")
    za = N01.inv_cdf(1 - alpha / 2)
    zb = N01.inv_cdf(power)
    p_bar = (p1 + p2) / 2
    num = (za * math.sqrt(2 * p_bar * (1 - p_bar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (p2 - p1) ** 2)


def miller_power(n_total, lift):
    """Approximate power of Miller's sequential test with total conversions n_total."""
    q = (1 + lift) / (2 + lift)  # probability a conversion lands in treatment
    mu = 2 * q - 1
    sigma = math.sqrt(1 - mu * mu)
    b = 2 * math.sqrt(n_total)
    s = sigma * math.sqrt(n_total)
    return N01.cdf((mu * n_total - b) / s) + math.exp(2 * mu * b / sigma ** 2) * N01.cdf((-mu * n_total - b) / s)


def miller_n(lift, power=0.8):
    if lift <= 0:
        return None
    lo, hi = 10, 10
    while miller_power(hi, lift) < power:
        hi *= 2
        if hi > 10 ** 9:
            return None
    while lo < hi:
        mid = (lo + hi) // 2
        if miller_power(mid, lift) >= power:
            hi = mid
        else:
            lo = mid + 1
    return lo


def weeks_needed(n_per_variant, monthly_sessions, share, variants=2):
    weekly = monthly_sessions * share / WEEKS_PER_MONTH
    if weekly <= 0:
        return math.inf
    return n_per_variant * variants / weekly


def tier(baseline, monthly_sessions, share, alpha, power):
    w20 = weeks_needed(per_variant_n(baseline, 0.2, alpha, power), monthly_sessions, share)
    w50 = weeks_needed(per_variant_n(baseline, 0.5, alpha, power), monthly_sessions, share)
    if w20 <= 6:
        return 1, "Test-ready: a 20% relative lift is detectable within 6 weeks. Run server-side A/B tests."
    if w50 <= 8:
        return 2, "Big swings only: only lifts of about 50% are detectable in about 8 weeks. Test whole-page concepts with a sequential stopping rule."
    return 3, "No valid A/B test: use research, fixes, qualitative validation and season-matched pre/post with a holdout."


def row(baseline, mde, monthly, share, alpha, power):
    n = per_variant_n(baseline, mde, alpha, power)
    w = weeks_needed(n, monthly, share)
    seq_n = miller_n(mde, power)
    seq_sessions = math.ceil(seq_n / (baseline * (2 + mde))) if seq_n else None
    return {
        "relative_mde": mde,
        "absolute_effect": round(baseline * mde, 6),
        "per_variant": n,
        "total": n * 2,
        "weeks": round(w, 1) if math.isfinite(w) else None,
        "weeks_rounded_up_to_full_weeks": max(2, math.ceil(w)) if math.isfinite(w) else None,
        "sequential_total_conversions_N": seq_n,
        "sequential_win_margin": round(2 * math.sqrt(seq_n), 1) if seq_n else None,
        "sequential_max_sessions_per_variant": seq_sessions,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--baseline", type=float, required=True)
    ap.add_argument("--mde", type=float)
    ap.add_argument("--monthly-sessions", type=float, required=True)
    ap.add_argument("--traffic-share", type=float, default=1.0)
    ap.add_argument("--power", type=float, default=0.8)
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    mdes = [a.mde] if a.mde else [0.05, 0.10, 0.20, 0.30, 0.50]
    rows = [row(a.baseline, m, a.monthly_sessions, a.traffic_share, a.alpha, a.power) for m in mdes]
    t, note = tier(a.baseline, a.monthly_sessions, a.traffic_share, a.alpha, a.power)
    out = {
        "baseline": a.baseline,
        "monthly_sessions": a.monthly_sessions,
        "traffic_share": a.traffic_share,
        "power": a.power,
        "alpha": a.alpha,
        "tier": t,
        "tier_note": note,
        "rows": rows,
    }
    if a.json:
        print(json.dumps(out, indent=2))
        return

    print(f"Baseline {a.baseline:.2%}, {a.monthly_sessions:,.0f} sessions/month, {a.traffic_share:.0%} in test, "
          f"power {a.power:.0%}, alpha {a.alpha} (two-sided), 2 variants\n")
    print(f"{'Rel. MDE':>9} {'Per variant':>12} {'Weeks':>8}   {'Seq. N conv':>11} {'Win margin':>10}")
    for r in rows:
        weeks = f"{r['weeks']:.1f}" if r["weeks"] is not None else "inf"
        seqn = f"{r['sequential_total_conversions_N']:,}" if r["sequential_total_conversions_N"] else "n/a"
        margin = f"{r['sequential_win_margin']}" if r["sequential_win_margin"] else "n/a"
        print(f"{r['relative_mde']:>9.0%} {r['per_variant']:>12,} {weeks:>8}   {seqn:>11} {margin:>10}")
    print(f"\nTier {t}. {note}")
    print("Run whole weeks and at least 2 weeks. Sequential N is an approximation of Evan Miller's method.")


if __name__ == "__main__":
    main()
