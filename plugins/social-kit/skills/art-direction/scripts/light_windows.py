#!/usr/bin/env python3
"""Sunrise, sunset, golden hour and blue hour for a location and date.

Stdlib only. Usage:
    python3 light_windows.py <lat> <lon> <YYYY-MM-DD> [--tz 5.5] [--days 3]

--tz is the UTC offset in hours for the shoot location (5.5 for Sri Lanka, -5 for New York
in winter). Uses the NOAA solar position equations, sampled every minute.

Definitions (sun elevation): blue hour -6 to -4 degrees, golden hour -4 to +6 degrees,
sunrise and sunset at -0.833 degrees. Times are approximate (within a few minutes); terrain,
buildings and cloud change the usable light, so scout on site.
"""

import argparse
import datetime as dt
import math


def sun_elevation(lat, lon, when_utc):
    jd = when_utc.timestamp() / 86400.0 + 2440587.5
    t = (jd - 2451545.0) / 36525.0
    l0 = (280.46646 + t * (36000.76983 + 0.0003032 * t)) % 360
    m = 357.52911 + t * (35999.05029 - 0.0001537 * t)
    e = 0.016708634 - t * (0.000042037 + 0.0000001267 * t)
    mr = math.radians(m)
    c = (math.sin(mr) * (1.914602 - t * (0.004817 + 0.000014 * t))
         + math.sin(2 * mr) * (0.019993 - 0.000101 * t) + math.sin(3 * mr) * 0.000289)
    true_long = l0 + c
    omega = 125.04 - 1934.136 * t
    app_long = true_long - 0.00569 - 0.00478 * math.sin(math.radians(omega))
    seconds = 21.448 - t * (46.815 + t * (0.00059 - t * 0.001813))
    eps0 = 23 + (26 + seconds / 60) / 60
    eps = eps0 + 0.00256 * math.cos(math.radians(omega))
    decl = math.degrees(math.asin(math.sin(math.radians(eps)) * math.sin(math.radians(app_long))))
    y = math.tan(math.radians(eps / 2)) ** 2
    l0r = math.radians(l0)
    eq_time = 4 * math.degrees(y * math.sin(2 * l0r) - 2 * e * math.sin(mr)
                               + 4 * e * y * math.sin(mr) * math.cos(2 * l0r)
                               - 0.5 * y * y * math.sin(4 * l0r) - 1.25 * e * e * math.sin(2 * mr))
    minutes = when_utc.hour * 60 + when_utc.minute + when_utc.second / 60
    true_solar = (minutes + eq_time + 4 * lon) % 1440
    hour_angle = true_solar / 4 - 180
    lat_r, decl_r, ha_r = map(math.radians, (lat, decl, hour_angle))
    cos_zen = (math.sin(lat_r) * math.sin(decl_r) + math.cos(lat_r) * math.cos(decl_r) * math.cos(ha_r))
    return 90 - math.degrees(math.acos(max(-1.0, min(1.0, cos_zen))))


def crossings(samples, threshold):
    out = []
    for (t1, e1), (t2, e2) in zip(samples, samples[1:]):
        if (e1 - threshold) * (e2 - threshold) <= 0 and e1 != e2:
            frac = (threshold - e1) / (e2 - e1)
            out.append((t1 + (t2 - t1) * frac, "rising" if e2 > e1 else "setting"))
    return out


def day_report(lat, lon, day, tz):
    tzinfo = dt.timezone(dt.timedelta(hours=tz))
    start_local = dt.datetime(day.year, day.month, day.day, tzinfo=tzinfo)
    samples = []
    for minute in range(0, 24 * 60 + 1):
        local = start_local + dt.timedelta(minutes=minute)
        samples.append((local, sun_elevation(lat, lon, local.astimezone(dt.timezone.utc))))

    def find(th, direction):
        for when, d in crossings(samples, th):
            if d == direction:
                return when.strftime("%H:%M")
        return "n/a"

    noon = max(samples, key=lambda s: s[1])
    print(f"\n{day.isoformat()}  (UTC{tz:+g})")
    print(f"  morning blue hour:   {find(-6, 'rising')} to {find(-4, 'rising')}")
    print(f"  morning golden hour: {find(-4, 'rising')} to {find(6, 'rising')}")
    print(f"  sunrise:             {find(-0.833, 'rising')}")
    print(f"  solar noon:          {noon[0].strftime('%H:%M')} (sun elevation {noon[1]:.0f} deg, hardest overhead light)")
    print(f"  sunset:              {find(-0.833, 'setting')}")
    print(f"  evening golden hour: {find(6, 'setting')} to {find(-4, 'setting')}")
    print(f"  evening blue hour:   {find(-4, 'setting')} to {find(-6, 'setting')} (twilight exteriors, lights on)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lat", type=float)
    ap.add_argument("lon", type=float)
    ap.add_argument("date", help="YYYY-MM-DD")
    ap.add_argument("--tz", type=float, default=0.0, help="UTC offset in hours, e.g. 5.5")
    ap.add_argument("--days", type=int, default=1)
    args = ap.parse_args()
    day = dt.date.fromisoformat(args.date)
    print(f"Light windows for {args.lat}, {args.lon}")
    for i in range(args.days):
        day_report(args.lat, args.lon, day + dt.timedelta(days=i), args.tz)


if __name__ == "__main__":
    main()
