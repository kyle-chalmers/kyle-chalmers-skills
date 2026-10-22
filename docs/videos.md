# Tutorials and public entry points

The release map and final-video transcripts were checked locally on October 21, 2026. Transcript text establishes the recommendations below. The nine descriptions affected by this migration were checked in YouTube Studio on October 22, 2026; the publication status is recorded below. Caption retrieval uses a transcript downloader, with existing final-video transcripts reused where available. Full transcripts and production materials are not distributed here.

| Public tutorial | Evidence in the transcript | Maintained resource | Link treatment |
|---|---|---|---|
| [5 Small Claude Code Tips](https://youtu.be/SDEtP1msjos?t=672) | At 11:12, Git Ship is introduced as the reusable shipping skill. | [git-ship](../skills/git-ship/) and [encourage](../skills/encourage/) from the companion collection. | Description links to both maintained skills. The companion materials link uses Data AI Reference's current repository name. |
| [Next Session Prompt](https://youtu.be/V0BkDqHZUcA?t=58) | At 00:58, the session handoff skill is invoked; the GitHub repository is recommended for installation. | [next-session-prompt](../skills/next-session-prompt/) | Description links to the maintained skill, installation instructions, and SKILL.md. The archived original keeps its historical files and moved notice. |
| [AI Friend Reviewer](https://youtu.be/2nBUItHz96c?t=72) | At 01:12, AI Friend Review is named and offered as an installable skill. | [ai-friend-review](../skills/ai-friend-review/) | Description links to the collection's installation instructions. Three related Shorts are verified; the Codex Short awaits verification. The archived original retains its moved notice. |
| [Claude Code Insights](https://youtu.be/Ey8x2DZHEq4?t=157) | At 02:37, review is combined with Git Ship; later discussion distinguishes failed reviewers from completed reviews. | [ai-friend-review](../skills/ai-friend-review/) and [git-ship](../skills/git-ship/) | The older public Git Ship file had fallen behind this discussion. Its migration removes unsafe cleanup and documents review limitations; it does not claim to implement a mechanically enforced gate. |
| [Meeting Transcript to Jira](https://youtu.be/9FlqHryv22o?t=1287) | At 21:27, the customizable Meeting to Tickets skill is introduced. | [meeting-to-tickets](../skills/meeting-to-tickets/), including [TEMPLATE.md](../skills/meeting-to-tickets/TEMPLATE.md) | Keep the setup guides and sample transcript in Data AI Reference. Update skill and template entry points together. |
| [Context Engineering: 4 Layers](https://youtu.be/euj9jLBM140?t=1551) | At 25:51, write-notion-report is described in the channel analyzer application. | [Channel Patterns Analyzer](https://github.com/kyle-chalmers/channel-patterns-analyzer) | Keep this application-specific skill with its application. |
| [StreamSnow](https://youtu.be/73jOT3-TW8Y?t=142) | At 02:22, the skills are described alongside an integration pipeline and package. | [StreamSnow](https://github.com/kyle-chalmers/streamsnow) | Catalog the suite; retain its package and existing tutorial links. |
| [dbt and AI](https://youtu.be/34RkoSPfpV4) | The recording explicitly installs dbt Labs' upstream agent skills. | [dbt Labs agent skills](https://github.com/dbt-labs/dbt-agent-skills) | Keep attribution and upstream installation instructions. |
| [Claude Code DuckDB](https://youtu.be/QGe4c_AMqGk) | The recording installs an external DuckDB skills marketplace. | [DuckDB companion project](https://github.com/kyle-chalmers/claude-code-duckdb) | Keep the companion project and upstream links. |
| [Claude Code Storage Problem](https://youtu.be/o7tKO4qN_uc) | Related repository contains a cleanup command, rather than a portable SKILL.md. | [Cleanup logs](https://github.com/kyle-chalmers/clean-claude-code-debug-logs) | Keep as a legacy command pending a separate conversion. |

Skill Chain is included because it is an existing public, portable skill. No matching published tutorial was established in the inspected release map, so none is invented here.

## YouTube description updates

The approved update replaces thirteen old repository URLs across five full-length videos and four Shorts. The five-tips tutorial also gains direct links to Git Ship and Encourage. All nine revised descriptions are saved in the private content repository. Six live updates were verified after reloading YouTube Studio on October 22, 2026; the remaining work is listed explicitly below.

| Affected video | Maintained destination | Live status |
|---|---|---|
| [5 Quick AI Coding Agent Changes, Major Productivity Gains](https://youtu.be/SDEtP1msjos) | [Git Ship](../skills/git-ship/), [Encourage](../skills/encourage/), and the [companion tutorial archive](https://github.com/kyle-chalmers/data-ai-reference/tree/main/videos/ai_coding_agent_tips) | Verified |
| [Save and Resume Any Claude Code Session](https://youtu.be/V0BkDqHZUcA) | [Next Session Prompt](../skills/next-session-prompt/), [installation](../README.md#install), and [SKILL.md](../skills/next-session-prompt/SKILL.md) | Verified |
| [Stack Multiple AI Reviewers Against Each Other](https://youtu.be/2nBUItHz96c) | [Installation instructions](../README.md#install) | Verified |
| [Make Your AI Agents Check Each Other](https://youtu.be/F4Kk8a_NvCg) | [AI Friend Review](../skills/ai-friend-review/) | Verified |
| [My AI Friend Review Skill Does Code Review For Me](https://youtu.be/RfoL2COrNg8) | [AI Friend Review](../skills/ai-friend-review/) | Verified |
| [Claude Code Runs My Review Skill](https://youtu.be/GlTm4_VCOqs) | [AI Friend Review](../skills/ai-friend-review/) | Verified |
| [Codex Ran 3 AI Reviewers For Me](https://youtu.be/Jc8-KeVFxHw) | [Next Session Prompt](../skills/next-session-prompt/) and [AI Friend Review](../skills/ai-friend-review/) | Save submitted; verification pending |
| [This Built-In Claude Code Command Finds What's Broken in Your Workflow](https://youtu.be/Ey8x2DZHEq4) | [AI Friend Review](../skills/ai-friend-review/) | Update pending |
| [Turn Meetings Into Jira Tickets With Claude Code](https://youtu.be/9FlqHryv22o) | [Meeting to Tickets](../skills/meeting-to-tickets/SKILL.md) and [TEMPLATE.md](../skills/meeting-to-tickets/TEMPLATE.md) | Update pending |

Titles, tags, chapter timestamps, and other description text were preserved. Meeting to Tickets still links to its setup guide, sample transcript, and meeting script in Data AI Reference. The original repositories remain readable as historical entry points. Production descriptions and verification records are maintained in the private content repository.
