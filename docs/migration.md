# Migration and retirement

This repository is the maintained source for six portable skills. The categories are session management, coding workflows, workflow design, and meetings. Larger suites appear in the same catalog and marketplace, with their source code maintained in their own repositories.

## Portable skill mapping

| Previous source | New maintained source |
|---|---|
| next-session-prompt / skills/next-session-prompt | skills/next-session-prompt |
| ai-friend-review / skills/ai-friend-review | skills/ai-friend-review |
| skill-chain / skills/skill-chain | skills/skill-chain |
| data-ai-reference / videos/ai_coding_agent_tips/git-ship | skills/git-ship |
| data-ai-reference / videos/ai_coding_agent_tips/encourage | skills/encourage |
| data-ai-reference / videos/meeting_transcript_to_jira/skill/meeting-to-tickets | skills/meeting-to-tickets |

The imported files were matched against the public GitHub blob hashes before copying. Original revisions and intentional changes are recorded in [provenance](../catalog/provenance.json). AI Friend Review includes both Python helpers, its agent metadata, and its research reference. Meeting to Tickets includes its editable template. The historical source repositories retain the original Git history.

## Retirement sequence

1. Publish and validate the new collection and installation paths.
2. Put a moved notice at the top of each standalone source repository's README, linking its new folder.
3. Keep old files and installer URLs readable. An archived repository remains a historical snapshot; existing users should reinstall from the new maintained source to receive future changes.
4. Archive the three standalone repositories: next-session-prompt, ai-friend-review, and skill-chain. Archiving is reversible; deleting them would break tutorial entry points.
5. Add migration pointers to the extracted skill sections in Data AI Reference. Keep that repository active because its broader examples still serve other tutorials.
6. Preserve the existing `claude-plugins` marketplace identifier and its suite entries. Add a pointer to this marketplace rather than changing the identity of users' installed marketplace.

Current source-repository changes and archive results are recorded below as they are verified. This sequence is a plan until a result is explicitly recorded.

## Validation

The offline catalog check verifies skill discovery, category coverage, bundled references, provenance, and marketplace entries. The installer is exercised in temporary directories, including refusal to overwrite existing or symlinked skills. The imported AI Friend Review tests use fake reviewer CLIs; they do not run paid reviewers. Its default-selection test isolates the user reviewer-ranking environment override. Generated review prompts and outputs are ignored and must remain untracked in adopter repositories.

Live reviewer authentication and live installations of the external suites are not part of the consolidation checks. Old installation endpoints keep serving the frozen historical files; archiving does not redirect raw file URLs to this repository.

## Status

- New public repository: created.
- Six portable skills: published with source provenance and validated.
- Source repository moved notices and archival: verified for next-session-prompt, ai-friend-review, and skill-chain on October 21, 2026.
- Data AI Reference migration pointers: published in the coding tips and Meeting Transcript to Jira READMEs; broader examples remain active.
- Legacy marketplace pointer: published. Its existing identifier and four suite entries are preserved; the consolidated collection and Healwright are now also available.
- Live YouTube descriptions: unchanged; exact replacements require a fresh live read and review.

All 43 offline tests pass. Both plugin manifests pass strict validation. [GitHub Actions validation](https://github.com/kyle-chalmers/kyle-chalmers-skills/actions/runs/39730198236) passed after the initial publication.

The standalone AI Friend Review repository had one open compatibility report. It remains readable at its original URL, and the outstanding items are tracked in [the consolidated repository issue](https://github.com/kyle-chalmers/kyle-chalmers-skills/issues/1). No claim is made that these inherited CLI compatibility reports were resolved by moving the files.
