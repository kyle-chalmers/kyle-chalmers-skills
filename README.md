# Kyle Chalmers Skills

Reusable AI agent skills by [Kyle Chalmers](https://kclabs.ai), with public tutorials on [Kyle Chalmers Data Plus AI](https://www.youtube.com/@kylechalmersdataai).

Pick the task you want help with. Each skill is a folder containing `SKILL.md` and any scripts or references it needs.

## Choose a skill

| Category | Skill | What it helps you do |
|---|---|---|
| Session management | [Next Session Prompt](skills/next-session-prompt/) | Capture unfinished work in a prompt for the next session. |
| Coding workflows | [AI Friend Review](skills/ai-friend-review/) | Ask other locally available AI coding agents to review work. |
| Coding workflows | [Git Ship](skills/git-ship/) | Commit and open a pull request, with merging only when requested. |
| Coding workflows | [Encourage](skills/encourage/) | Reset a stalled agent around a concrete next experiment. |
| Workflow design | [Skill Chain](skills/skill-chain/) | Design a repeatable workflow and scaffold the skills for its steps. |
| Meetings | [Meeting to Tickets](skills/meeting-to-tickets/) | Draft scoped tickets from a transcript using an editable template. |

The folders stay directly under `skills/` so agents can discover them consistently. Categories are browsing metadata in [the catalog](catalog/skills.json). Each skill keeps one maintained source.

## Install

With the [Skills CLI](https://github.com/vercel-labs/skills), choose the skills and agents interactively:

```bash
npx skills add kyle-chalmers/kyle-chalmers-skills
```

To select one skill:

```bash
npx skills add kyle-chalmers/kyle-chalmers-skills --skill next-session-prompt
```

Or clone this repository and use the included Python 3.10+ installer:

```bash
git clone https://github.com/kyle-chalmers/kyle-chalmers-skills.git
cd kyle-chalmers-skills
python3 scripts/install.py --skill next-session-prompt --agent codex
```

Use `--agent claude` for Claude Code. `--all` selects all six portable skills. `--dest /path/to/skills` supports other folder-based loaders. The installer copies each complete skill and refuses to overwrite an existing file, folder, or symlink. Back up and remove an older installation deliberately before replacing it.

For Claude Code's plugin loader:

```text
/plugin marketplace add kyle-chalmers/kyle-chalmers-skills
/plugin install kyle-chalmers-skills@kyle-chalmers-skills
```

Start a new agent session after installation. Claude Code exposes plugin skills under the plugin namespace; a copied skill uses its own name. For example, invoke a copied skill with `/next-session-prompt` in Claude Code or `$next-session-prompt` in Codex. Agents without a skill loader can read the selected `SKILL.md` directly.

## Larger suites

These are maintained with their implementation, tests, and release process in their own repositories. The same marketplace lists them, so you can discover and install them from one entry point.

| Category | Suite | Purpose |
|---|---|---|
| Data engineering | [Ticketwright](https://github.com/kyle-chalmers/ticketwright) | Ticket-driven analysis and quality checks. |
| Data engineering | [Jobwright](https://github.com/kyle-chalmers/jobwright) | Govern and safely deploy orchestration jobs. |
| Data engineering | [Healwright](https://github.com/kyle-chalmers/healwright) | Build and audit self-healing data jobs. |
| Analytics | [StreamSnow](https://github.com/kyle-chalmers/streamsnow) | Build and ship governed Streamlit apps in Snowflake. |
| Security | [AI Data Security](https://github.com/kyle-chalmers/ai-data-security) | Audit secrets, AI configuration, and data access. |

For example, install `/plugin install streamsnow@kyle-chalmers-skills` after adding this marketplace. Refer to each suite's README for its runtime and setup requirements. AI Friend Review also needs configured reviewer CLIs; installing its skill does not install those programs. Meeting to Tickets drafts for human review and does not write to a tracker.

AI Friend Review has an [inherited CLI compatibility report](https://github.com/kyle-chalmers/kyle-chalmers-skills/issues/1) to verify. Offline tests exercise fake CLIs and do not establish compatibility with every installed reviewer version.

## Tutorials and migration

- [Related videos and the links affected by consolidation](docs/videos.md)
- [Inventory of all 36 public repositories inspected](docs/inventory.md)
- [Migration and retirement status](docs/migration.md)
- [Original sources and revisions](catalog/provenance.json)

Existing repository URLs remain useful for historical material. This repository is the maintained home for the six portable skills above.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). MIT licensed; see [LICENSE](LICENSE).

