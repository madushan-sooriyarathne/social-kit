#!/usr/bin/env python3
"""Budget and learning-phase math for a Meta ads strategy.

Rules come from references/playbook.md:
- Max ad sets = weekly budget / (cost per result x 50)   [Loomer]
- Second ad set only at 100+ conversions a week           [Loomer]
- Fallback: an event reachable 25-50 times a week         [Loomer]
- Creative cadence by spend tier                          [Foxwell, Motion]

Usage:
  python budget_math.py --monthly-budget 3000 --cpa 60
  python budget_math.py --daily-budget 40 --cpa 25 --currency LKR --usd-rate 300
"""
import argparse
import math

LEARNING_EVENTS = 50
FALLBACK_EVENTS = 25
SECOND_AD_SET_EVENTS = 100
WEEKS_PER_MONTH = 30.4 / 7


def creative_cadence(monthly_usd):
    if monthly_usd < 10_000:
        return ("Under $10K/month: about 4-5 distinct assets a month [Foxwell]; "
                "Motion's tier average is ~2.8 launches a week, top quartile 2-3x that.")
    if monthly_usd < 100_000:
        return ("$10K-$100K/month: scale between 4-5 assets and 8-10 concepts a month "
                "with spend; count distinct concepts, not variations [Foxwell, Motion].")
    if monthly_usd < 1_000_000:
        return ("$100K+/month: about 8-10 new concepts a month, 40-50 assets [Foxwell].")
    return "$1M+/month: Motion's tier average is ~18.85 creative launches a week."


def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--monthly-budget", type=float)
    g.add_argument("--weekly-budget", type=float)
    g.add_argument("--daily-budget", type=float)
    p.add_argument("--cpa", type=float, required=True,
                   help="Expected cost per optimized result, same currency as budget")
    p.add_argument("--currency", default="USD")
    p.add_argument("--usd-rate", type=float, default=1.0,
                   help="Units of currency per 1 USD (for spend-tier lookup)")
    a = p.parse_args()

    if a.monthly_budget is not None:
        weekly = a.monthly_budget / WEEKS_PER_MONTH
    elif a.weekly_budget is not None:
        weekly = a.weekly_budget
    else:
        weekly = a.daily_budget * 7
    monthly = weekly * WEEKS_PER_MONTH
    daily = weekly / 7
    cur = a.currency

    conv_week = weekly / a.cpa
    max_ad_sets = math.floor(weekly / (a.cpa * LEARNING_EVENTS))
    min_daily_one = a.cpa * LEARNING_EVENTS / 7
    max_cpa_learning = weekly / LEARNING_EVENTS
    max_cpa_fallback = weekly / FALLBACK_EVENTS

    print(f"Budget: {cur} {daily:,.0f}/day, {cur} {weekly:,.0f}/week, {cur} {monthly:,.0f}/month")
    print(f"Expected optimized results: {conv_week:,.1f}/week at {cur} {a.cpa:,.2f} each")
    print(f"Ad sets the budget can feed at {LEARNING_EVENTS}/week: {max_ad_sets}")
    print(f"Daily budget needed for ONE ad set to reach {LEARNING_EVENTS}/week: {cur} {min_daily_one:,.0f}")

    if conv_week >= SECOND_AD_SET_EVENTS:
        verdict = "Volume supports a second ad set if there is a real reason to split."
    elif conv_week >= LEARNING_EVENTS:
        verdict = "One ad set can exit learning. Keep to one ad set."
    elif conv_week >= FALLBACK_EVENTS:
        verdict = ("Below 50/week but within the 25-50 fallback range. One ad set; "
                   "acceptable, expect slower learning.")
    else:
        verdict = (f"Below {FALLBACK_EVENTS}/week. Either optimize for a shallower event costing "
                   f"under {cur} {max_cpa_fallback:,.2f}, or keep the deep event, use one ad set, "
                   "judge over 4+ week windows and accept it may never exit learning.")
    print(f"Verdict: {verdict}")
    print(f"CPA ceiling for 50/week: {cur} {max_cpa_learning:,.2f}; for 25/week: {cur} {max_cpa_fallback:,.2f}")
    print(f"Creative cadence: {creative_cadence(monthly / a.usd_rate)}")


if __name__ == "__main__":
    main()
