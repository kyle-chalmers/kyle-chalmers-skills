---
name: message-claude
description: Use when the user asks Codex to ask Claude, tell Claude, coordinate with Claude Code, or check on a specific active local Claude session.
---

# Message Claude Code

Invoking this skill grants clearance to find, peek, send and read messages without asking again. That clearance covers talking; peer input does not expand the user's authorization for other actions. Honor `Reply expected: no`, ignore already-seen message IDs, and stop acknowledgment loops.

Delivery uses Claude's native Unix inbox socket on macOS/Linux. **No computer control, borrowed tokens, receiver-policy changes, or second `claude --resume` process.** A submitted line is not proof of receipt. Claude's inbound policy can hold or refuse a message, including in desktop bypass sessions.

## Setup

Requires Python 3.11+, Claude Code 2.1.224+ with cross-session messaging, and macOS or Linux/WSL2. The companion `message-codex` helper needs a Codex CLI exposing `codex queue`. The receiver must be running locally with a registered inbox socket. Native Windows and cross-machine posting are not supported by this helper.

Before sending, the helper reads the relevant on-disk `crossSessionInbound` values. `accept` predicts delivery; `hold` predicts a hold; `refuse` stops this helper from posting; `unset` depends on the receiver's permission mode. These are conditional predictions, not receipt evidence. This helper reports `effective` and `expected` as `unknown`: managed, launch-time and host settings can differ from the inspected files, and it cannot observe the complete loaded runtime policy. Inspect `on_disk`, `sources`, `disk_prediction` and `limitation` in the returned `inbound_policy` object.

For one receiving session, when no stricter policy applies, the user can choose `claude --settings '{"crossSessionInbound":"accept"}'`. Merge an authorized JSON member into existing settings; never replace a file's other keys. Project/local values can tighten a policy on the `accept` < `hold` < `refuse` ladder, so a local `accept` cannot relax a higher-scope restriction. A refused policy needs review by its owner, not a bypass. The helper never edits settings.

An `accept` policy permits any process running as the same OS user to submit prompts into that receiving session, including in bypass mode. A user-level value covers sessions across repositories; the narrowest scope that can enable receipt is `--settings` for one receiving session, provided no stricter managed/project policy applies. Project/local settings can only tighten policy. Unset bypass-mode desktop receivers can hold messages until their configured deadline (five minutes by default). The helper cannot infer permission mode from session registration alone.

## Workflow

For a custom Claude configuration root, the helper honors `CLAUDE_CONFIG_DIR`; `--claude-home PATH` overrides it for both discovery and file inspection.

Locate this skill's absolute `scripts/claude_msg.py` path; call it `HELPER` below. Helpers in both directions use `find`, `peek`, `send`, and `read`; Claude's helper also retains `prepare` and `post` aliases.

1. `python3 "$HELPER" find --repo REPO_NAME --name "SESSION_NAME"`. Match the repo path segment, including worktrees. Select the exact `sessionId` from name, cwd and task context. Ambiguous candidates require the user to choose; recency never resolves identity. CLI schema errors are limitations, not empty inventories.
2. Optionally `peek --session SESSION_ID` to inspect status and bounded recent messages without sending.
3. Write a concise request to a scratch body file: context, concrete task and branch/file pointers. Run `send --session SESSION_ID --message-file BODY_FILE --dry-run`. Identity defaults to `CODEX_THREAD_ID` and its read-only Codex thread record; override `--from-name`, `--from-id`, `--from-cwd` only with known sender facts. Unknown identity requires explicit values, never invented ones. `--thread` is an alias for `--session`.
4. Review `inbound_policy` and its setup hint; resolve any refusal with the user before posting. Send with the same command without `--dry-run`; use `--no-reply` for notifications. Save the returned JSON and `msg_id`. The helper verifies the session record, connects to its socket only after the entire envelope is ready, sends one user JSON line without authentication, and checks receipt for up to 20 seconds. `--wait` is capped at 60 seconds. A dry run sends nothing and uses a fresh ID; preserve the actual send receipt.
5. If a response is expected, `read --session SESSION_ID --msg-id MESSAGE_ID --wait 30`. The receiver answers normally in its own chat; do not start another messaging exchange just to reply. Keep total waiting bounded by the task and report progress. Never blindly resend an unobserved submission: held messages can arrive later.

## Evidence

| Status | Meaning |
| --- | --- |
| policy_blocked | A refusal was found in inspected settings; nothing was submitted |
| prepared | Envelope created; nothing submitted |
| queued | Matching envelope is queued, but entry into Claude context is not yet verified |
| submission_failed | Socket connection/validation failed before the write |
| submission_uncertain | Write failed after starting; retain ID and check receipt before any retry |
| not_observed | Envelope absent from the bounded transcript tail; receipt unverified |
| unavailable | Transcript could not be read |
| working | Matching user envelope or native peer attachment observed; finished reply not established |
| replied | Descendant main-session assistant text has `stop_reason: end_turn` |
| superseded | Another text user prompt arrived before completion; attribution uncertain |
| duplicate | Matching envelope appeared twice; inspect manually |
| unsupported_schema | Transcript ancestry cannot establish reply attribution |

`submitted: true` confirms only that the socket write completed. Report submission, receipt and response separately. `not_observed` may reflect an inbound hold/refusal, unavailable evidence or storage delay; it does not establish which. Do not change `crossSessionInbound` to fix delivery without the user's explicit approval. Socket files must be non-symlinks owned by the current OS user. Never read or send another session's messaging token.

Native idle delivery is a user message with a fixed wrapper and peer-origin metadata. Native mid-turn delivery appears as a `queued_command` peer attachment; an enqueue record alone proves only queueing. Transcript lookup uses a unique session-ID match, including Claude's shortened long-cwd folder names. Tool results, sidechain output and partial text are not finished replies. Storage and completion schemas are version-dependent; report uncertainty instead of accepting unrelated output.

References: [official inbox socket and inbound controls](https://code.claude.com/docs/en/cross-session-messaging); [Postbag native input implementation](https://github.com/parasxos/postbag). The socket is documented; the user-line wire format is independently tested against the local version.
