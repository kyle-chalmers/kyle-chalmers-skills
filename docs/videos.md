# Tutorials and public entry points

The release map and final-video transcripts were checked locally on October 21, 2026. Transcript text establishes the recommendations below. This does not claim a fresh read of every live YouTube description. Caption retrieval uses a transcript downloader, with existing final-video transcripts reused where available. Full transcripts and production materials are not distributed here.

| Public tutorial | Evidence in the transcript | Maintained resource | Link treatment |
|---|---|---|---|
| [5 Small Claude Code Tips](https://youtu.be/SDEtP1msjos?t=672) | At 11:12, Git Ship is introduced as the reusable shipping skill. | [git-ship](../skills/git-ship/) and [encourage](../skills/encourage/) from the companion collection. | Keep Data AI Reference as the tutorial archive; point its skill sections here. |
| [Next Session Prompt](https://youtu.be/V0BkDqHZUcA?t=58) | At 00:58, the session handoff skill is invoked; the GitHub repository is recommended for installation. | [next-session-prompt](../skills/next-session-prompt/) | Preserve the old repository and installer URLs; add a moved notice. |
| [AI Friend Reviewer](https://youtu.be/2nBUItHz96c?t=72) | At 01:12, AI Friend Review is named and offered as an installable skill. | [ai-friend-review](../skills/ai-friend-review/) | Preserve the old repository and supporting-file links; add a moved notice. |
| [Claude Code Insights](https://youtu.be/Ey8x2DZHEq4?t=157) | At 02:37, review is combined with Git Ship; later discussion distinguishes failed reviewers from completed reviews. | [ai-friend-review](../skills/ai-friend-review/) and [git-ship](../skills/git-ship/) | The older public Git Ship file had fallen behind this discussion. Its migration removes unsafe cleanup and documents review limitations; it does not claim to implement a mechanically enforced gate. |
| [Meeting Transcript to Jira](https://youtu.be/9FlqHryv22o?t=1287) | At 21:27, the customizable Meeting to Tickets skill is introduced. | [meeting-to-tickets](../skills/meeting-to-tickets/), including [TEMPLATE.md](../skills/meeting-to-tickets/TEMPLATE.md) | Keep the setup guides and sample transcript in Data AI Reference. Update skill and template entry points together. |
| [Context Engineering: 4 Layers](https://youtu.be/euj9jLBM140?t=1551) | At 25:51, write-notion-report is described in the channel analyzer application. | [Channel Patterns Analyzer](https://github.com/kyle-chalmers/channel-patterns-analyzer) | Keep this application-specific skill with its application. |
| [StreamSnow](https://youtu.be/73jOT3-TW8Y?t=142) | At 02:22, the skills are described alongside an integration pipeline and package. | [StreamSnow](https://github.com/kyle-chalmers/streamsnow) | Catalog the suite; retain its package and existing tutorial links. |
| [dbt and AI](https://youtu.be/34RkoSPfpV4) | The recording explicitly installs dbt Labs' upstream agent skills. | [dbt Labs agent skills](https://github.com/dbt-labs/dbt-agent-skills) | Keep attribution and upstream installation instructions. |
| [Claude Code DuckDB](https://youtu.be/QGe4c_AMqGk) | The recording installs an external DuckDB skills marketplace. | [DuckDB companion project](https://github.com/kyle-chalmers/claude-code-duckdb) | Keep the companion project and upstream links. |
| [Claude Code Storage Problem](https://youtu.be/o7tKO4qN_uc) | Related repository contains a cleanup command, rather than a portable SKILL.md. | [Cleanup logs](https://github.com/kyle-chalmers/clean-claude-code-debug-logs) | Keep as a legacy command pending a separate conversion. |

Skill Chain is included because it is an existing public, portable skill. No matching published tutorial was established in the inspected release map, so none is invented here.

## YouTube description updates

The old GitHub URLs remain readable after archiving. Updating descriptions is a separate publication step: read each current live description, change only the affected skill links, and review the exact replacements before saving. The checked local description for Meeting Transcript to Jira has separate links to the skill, template, sample transcript, and setup guide; only the first two move.
