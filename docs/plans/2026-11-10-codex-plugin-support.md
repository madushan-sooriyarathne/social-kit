# Codex Plugin Support Implementation Plan

Ship Social Kit through the same Git repository to Claude Code, Codex CLI, and Codex in the ChatGPT desktop app. Both platforms use the seven existing skills, references, and Python helpers under `plugins/social-kit/skills/`.

Codex CLI 0.167.0 installed the current Claude-format plugin after explicit marketplace registration in an isolated checkout. This plan adds a native Codex marketplace and the current portable manifest format for an explicit, documented distribution path. Scope covers installation from this repo and maintenance of the shared skills.

## 1. Add the plugin manifest and marketplace

Create `plugins/social-kit/plugin.json`. Use the same identity, version, and repository metadata as the existing `plugins/social-kit/.claude-plugin/plugin.json`. The example uses the current version, 1.1.0. If the compatibility edits in step 2 ship in the same release, apply the repo's minor bump rule to both manifests.

```json
{
  "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
  "name": "social-kit",
  "version": "1.1.0",
  "description": "Digital marketing skills backed only by independent third-party expert research: Meta ads strategy, Meta organic growth, SEO strategy, SEO copywriting, brand shoot art direction, landing page and conversion strategy, and direct response copywriting.",
  "author": {
    "name": "Madushan Sooriyarathne"
  },
  "repository": "https://github.com/madushan-sooriyarathne/social-kit",
  "keywords": ["marketing", "meta-ads", "instagram", "seo", "copywriting", "art-direction", "landing-pages", "cro", "email-marketing"],
  "extensions": {
    "com.openai": {
      "interface": {
        "displayName": "Social Kit",
        "shortDescription": "Research-backed digital marketing skills"
      }
    }
  }
}
```

Create `.agents/plugins/marketplace.json`. Resolve the entry from the repository root.

```json
{
  "name": "social-kit",
  "interface": {
    "displayName": "Social Kit"
  },
  "plugins": [
    {
      "name": "social-kit",
      "source": {
        "source": "local",
        "path": "./plugins/social-kit"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Marketing"
    }
  ]
}
```

Keep the existing Claude manifest and marketplace in place. Codex discovers the shared `skills/` directory from the portable manifest. The marketplace lets users opt in through installation. [OpenAI plugin packaging and marketplace documentation](https://developers.openai.com/plugins/build/plugins)

## 2. Make the shared workflows portable

- In `art-direction`, `direct-response-copywriter`, `landing-page-strategist`, `seo-copywriting`, and `seo-expert`, replace references to `WebFetch` with instructions to use the host's page-fetch or browser tools. Keep each skill's existing limits on what can be verified and add a concise fallback where missing for when live access is unavailable.
- In `meta-ads-strategy`, use `python3` consistently with the other workflows. Where a skill runs a bundled script, make clear that the script path is relative to that skill's installed directory. Inputs and outputs can still use the user's workspace paths. Keep the existing research and sourcing rules.

## 3. Document installation and maintenance

Update `README.md` to describe both platforms. Keep the existing Claude Code commands and add the Codex CLI commands below. Document that a fresh Codex session exposes the installed skills. In Codex desktop, open the Plugins Directory, choose **Social Kit** from the configured marketplace, and install it.

```sh
codex plugin marketplace add madushan-sooriyarathne/social-kit
codex plugin add social-kit@social-kit
codex plugin marketplace upgrade social-kit
```

The first two commands install the plugin after the new files reach the Git ref being installed. The last command refreshes a Git-backed marketplace. In the CLI, select the plugin skill from the skill picker, for example `$social-kit:meta-ads-strategy`. [Codex CLI reference](https://learn.chatgpt.com/docs/cli/reference#codex-plugin) · [Plugin installation](https://learn.chatgpt.com/docs/plugins)

Add a root `AGENTS.md` for contributors working in Codex. Point it to `REFRESH_PROCEDURE.md` and `SOURCE_POLICY.md`, record where skills and research live, and carry over the existing style and pull request rules from `CLAUDE.md`. [Codex repository instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

Update the wrap-up and new-skill sections of `REFRESH_PROCEDURE.md` to keep both manifest versions in sync, update both manifest descriptions when skills change, and retain the existing condition for when to bump the version. Extend the existing JSON validation to parse the four packaging files, compare the plugin names and versions, and resolve each marketplace entry to the same plugin folder.

## 4. Validate both installation paths

1. In a temporary checkout and an isolated Codex profile, run the local install below. Confirm the marketplace lists one Social Kit entry and the installed plugin is enabled at the same version as the Claude manifest.

   ```sh
   codex plugin marketplace add .
   codex plugin list --marketplace social-kit --available --json
   codex plugin add social-kit@social-kit --json
   codex plugin list --marketplace social-kit --json
   ```

2. From a fresh session, verify that Codex lists all seven skills under the `social-kit` namespace. Explicitly invoke the Meta ads strategy skill with a USD 3,000 monthly budget and USD 25 CPA. Confirm Codex finds the installed reference files and runs the bundled helper. The helper should report about 27.6 expected results per week. Give the SEO expert skill a public URL to verify its page-fetch fallback and how it reports checks the environment cannot perform.
3. Test the Git-backed install and upgrade from a separate directory. Install from the implementation ref, publish a second fixture version, run `codex plugin marketplace upgrade social-kit`, and confirm the installed version and cached skill files advance. Smoke-test installation in the desktop Plugins Directory.
4. Run `claude plugin validate .` and `claude plugin validate plugins/social-kit`. Smoke-test the existing Claude installation flow and confirm it exposes the same seven skill names. Run the repository's existing style and frontmatter checks.

## Evidence from planning

In temporary checkouts, Codex CLI 0.167.0 installed the existing Claude package and also installed the proposed portable package. Codex's app server discovered all seven skills in the portable installation with zero skill loading errors. The bundled budget script ran from the installed cache. A local Git fixture exercised the Git-backed marketplace path and upgraded the installed plugin from 1.1.0 to 1.2.0. Claude's marketplace and plugin validation both passed with the proposed files present. The final GitHub installation and interactive skill runs on both clients remain implementation checks.
