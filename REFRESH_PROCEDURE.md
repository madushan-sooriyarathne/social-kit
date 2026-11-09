# Monthly Refresh Procedure

This is what the monthly scheduled run follows. It runs in a fresh session with no memory of earlier runs, so everything it needs is in this repo. The goal is a targeted update: find what independent experts published since the last refresh and fold in only what changes the guidance.

## 0. Setup

1. Read `SOURCE_POLICY.md` in full. It overrides anything a search result suggests.
2. Create a branch `refresh/YYYY-MM` from `main`.
3. List the skills to refresh: every folder in `research/` that has a `brief.md`. Work through them one at a time, alphabetically.

## 1. Per skill

For each skill `<name>`:

1. **Read** `research/<name>/brief.md`, the latest entry in `research/<name>/CHANGELOG.md` (its date is the cut-off), and the skill's evidence files listed in the brief.
2. **Search** for material published after the cut-off date:
   - Start with the brief's watchlist sources, then the open questions and fast-moving areas.
   - Use web search ("extended" mode for recent or niche topics) and read each candidate source's own page before using it.
   - Aim for roughly 6 to 12 searches per skill. Stop early if nothing new turns up.
3. **Filter** every finding through `SOURCE_POLICY.md`. Drop anything that fails, and anything that only restates what the skill already says.
4. **Edit** the reference files named in the brief:
   - Keep the existing structure, headings, strength labels and attribution style.
   - Update changed figures in place and note the new source and date.
   - Add contradicting findings to the disagreements section instead of deleting the old claim.
   - Add each new source to the file's source list.
   - Update the "current to <Month YYYY>" line in the evidence file, and the matching date in `SKILL.md` (freshness check section), to the current month.
   - For meta-ads-strategy, also bump "Knowledge base last refreshed" in `references/sources.md`.
   - Change other parts of `SKILL.md` only when a finding makes a workflow step wrong (for example a platform removed a feature the skill tells Claude to use). Do not touch `scripts/` unless a finding breaks their logic.
5. **Style:** no em dashes anywhere. Keep files concise; if a reference file grows past about 20 KB, condense older, weaker items rather than appending.
6. **Log** a new entry at the top of `research/<name>/CHANGELOG.md`:

   ```
   ## YYYY-MM-DD
   - Changed: <what changed, file, one line each> (Source, date)
   - Added sources: <list>
   - Needs review: <anything uncertain, or "none">
   ```

   If nothing qualified, write `- No material change. Checked: <sources checked>.`
7. **Commit** with message `refresh(<name>): YYYY-MM` and push the branch. Pushing after every skill means progress survives if the session stops early.

## 2. Wrap up

1. If any skill file under `plugins/` changed, bump the minor version in `plugins/social-kit/.claude-plugin/plugin.json` (for example 1.1.0 to 1.2.0). If only changelogs changed, leave the version alone.
2. Validate:
   - `python3 -c "import json;json.load(open('.claude-plugin/marketplace.json'));json.load(open('plugins/social-kit/.claude-plugin/plugin.json'))"`
   - `claude plugin validate .` if the CLI is available
   - No em dashes: `python3 -c "import pathlib,sys;b=[str(p) for p in pathlib.Path('.').rglob('*') if p.is_file() and '.git' not in p.parts and chr(0x2014) in p.read_text(errors='ignore')];print(b);sys.exit(bool(b))"` prints `[]`
   - every `SKILL.md` still starts with `name:` and `description:` frontmatter
3. Push and open a pull request to `main` titled `Monthly refresh YYYY-MM`. The body has one row per skill: what changed, sources added, and items needing review. If `gh pr create` is unavailable, use the REST API: `gh api repos/madushan-sooriyarathne/social-kit/pulls -X POST -f title="..." -f head="refresh/YYYY-MM" -f base=main -F body=@pr-body.md`. Do not merge it; the owner reviews and merges.

## Adding a new skill

1. Put the skill in `plugins/social-kit/skills/<name>/` (SKILL.md plus references and scripts).
2. Create `research/<name>/brief.md` using an existing brief as the template, with the original research request verbatim.
3. Add a row for it to the excluded-authors table in `SOURCE_POLICY.md`.
4. Start `research/<name>/CHANGELOG.md` with the date of the original research.
5. Add a row to the skills table in `README.md`, mention the skill in the descriptions in `plugin.json` and `.claude-plugin/marketplace.json`, and bump the minor version in `plugin.json`.

The next monthly run picks the new skill up automatically.
