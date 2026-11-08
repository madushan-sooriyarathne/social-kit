# Social Kit

A Claude plugin marketplace of digital marketing skills. Every skill is built from deep research that uses only independent third-party experts and data, and is refreshed monthly.

| Skill | Point it at a brand or URL and get |
|---|---|
| `meta-ads-strategy` | A launch-ready Meta ads strategy: tracking, structure, budget math, creative concepts, scaling rules, 90-day plan |
| `organic-growth-strategy` | An organic growth plan for Instagram, Facebook and Threads with pillars, format mix, calendar and KPIs |
| `seo-expert` | A prioritized SEO and AI-search growth strategy with a technical snapshot |
| `seo-copywriting` | A keyword map and publish-ready, keyword-optimized page copy with a placement checker |
| `art-direction` | A photo and video shoot guide with shot list, angles, light windows, video hooks and crops |

## Install in Claude Code

```
/plugin marketplace add madushan-sooriyarathne/social-kit
/plugin install social-kit@social-kit
```

Run `/plugin marketplace update social-kit` to pick up a new monthly version.

## How it stays current

- `SOURCE_POLICY.md` defines which sources qualify and which authors are excluded per skill.
- `research/<skill>/brief.md` holds the original research request and the questions each refresh keeps answered.
- A monthly scheduled task follows `REFRESH_PROCEDURE.md`, updates the evidence files, logs changes in `research/<skill>/CHANGELOG.md`, bumps the plugin version and opens a pull request for review.

## Layout

```
.claude-plugin/marketplace.json
plugins/social-kit/
  .claude-plugin/plugin.json
  skills/<skill>/SKILL.md, references/, scripts/
research/<skill>/brief.md, CHANGELOG.md
SOURCE_POLICY.md
REFRESH_PROCEDURE.md
```

To add a skill, see the last section of `REFRESH_PROCEDURE.md`.
