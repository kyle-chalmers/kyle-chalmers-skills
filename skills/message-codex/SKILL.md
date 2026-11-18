---
name: message-codex
description: "Use when the user asks Claude Code to message, ping, ask, hand work to, coordinate with, or read a reply from a running OpenAI Codex session (Codex Desktop app or Codex CLI) on the same machine."
---

# Message a Codex session

Claude Code reaches a live Codex thread through the supported `codex queue` command and reads the answer from that thread's local rollout file. No computer control is involved. The helper `scripts/codex_msg.py` (stdlib Python, read-only against Codex state) does discovery, sending and reply matching. Run it as `python3 <this skill dir>/scripts/codex_msg.py <command>`; every command prints JSON.

## Setup

- A Codex CLI that has `codex queue` (check with `codex queue --help`), signed in, on macOS or Linux. The Codex Desktop app's threads are reachable through the same command.
- Python 3.11 or later.
- This direction needs no Claude Code setting: Codex answers in its own thread and the helper reads it. The reverse direction (Codex messaging Claude, the `message-claude` skill) depends on the receiving Claude session's `crossSessionInbound` setting. A Claude session in bypass-permissions mode holds messages from outside Claude Code unless that setting is `accept`, and the desktop app drops a held message after the `dialogExpiry` deadline (five minutes by default). Project and local settings can only make this key stricter (`accept` < `hold` < `refuse`), so an `accept` there is ignored. `accept` takes effect from `--settings '{"crossSessionInbound":"accept"}'` when launching one receiving session, or from `~/.claude/settings.json` for every session, unless managed settings or a stricter project value override it. Prefer the single-session flag, state the trade-off (any process running as the user can then push prompts into the sessions it covers), and let `message-claude`'s inspected policy report what actually applies. Never change the setting yourself. See the [cross-session messaging docs](https://code.claude.com/docs/en/cross-session-messaging).

## Rules

- Invoking this skill is the user's clearance to talk with the Codex session: find, send, peek and read without asking first.
- Talking is all that clearance covers. A message is peer input to Codex, not the user's authorization for destructive or outbound actions (deletes, pushes, PRs, sending anything external). Codex is told so in the envelope and may ask the user before acting; relay that instead of arguing it with Codex.
- Pick the thread deliberately. Use a thread id or exact name the user gave you. Otherwise a thread qualifies only when its name or first message matches the work the user described; if zero or several qualify, show the user up to three candidates (name, cwd, local `updated_at`, first message) and let them choose. Recency alone never picks a thread.
- To learn what a Codex session is doing, `peek` it instead of messaging it.
- Never reply to a message marked `Reply expected: no`, ignore a msg-id you have already handled, and stop any exchange that is only acknowledgements.

## Steps

1. **Find.** `find --repo <repo-dir-name>`, narrowed with `--name "<words from its title>"`. Desktop sessions run in `~/.codex/worktrees/<hash>/<repo>`, so match on the repo directory name, not the path of the user's own checkout. `state` is `busy` while a turn is running. Times are local.
2. **Send.** Write the body to a file in the scratchpad, saying who asked for what ("The user asked me to find out whether..."), then `send --thread <id> --message-file <path>` (add `--no-reply` when no answer is needed, `--dry-run` to preview). The helper wraps the body in the shared envelope: sender name and session id (from `CLAUDE_CODE_SESSION_ID`), cwd, a unique `msg-id`, `Reply via`, and `Reply expected`. Keep the returned `msg_id` and `queued_item`. A dry run queues nothing, so there is nothing to `read` after it. A subagent sending on your behalf names the parent session as sender, which is where replies belong.
3. **Read.** `read --thread <id> --msg-id <msg_id> --queued-item <queued_item> --wait 60`. Each call waits at most 60 seconds; call it again to keep waiting, or loop it under the Monitor tool for long turns. Status values:

| status | meaning |
|---|---|
| `queued` | still in Codex's queue, usually because a turn is running |
| `not_observed` | not in the rollout tail and not queued; delivery is unverified, not lost. Check with `peek` before resending |
| `working` | delivered; the turn that received it is still running |
| `replied` | `reply` holds Codex's final message for that turn |
| `aborted` | the turn was interrupted; tell the user |
| `duplicate` | the envelope arrived twice; inspect the thread by hand |
| `unavailable` | the rollout file could not be read |
| `unsupported_schema` | the envelope arrived but its turn start is outside the readable tail, so no reply can be attributed; use `peek` |

Report delivery and reply separately to the user, in your own words, with the status.

## When no Codex session is running

If `find` shows no suitable thread, `start --cd <dir> --message-file <path>` starts a new headless Codex session in `<dir>` and waits for its reply (up to `--timeout`, 600 seconds by default; run it in the background for long tasks). It returns `thread`, `status` and `reply`. Continue that same session with `resume --thread <id> --message-file <path>`.

- Started sessions always run in Codex's **read-only** sandbox: they can read, answer and review, but cannot edit files. Tell the user that, and if they want Codex to make changes, they should do it in a session they run themselves.
- `resume` only accepts eligible headless threads (originator `codex_exec`, which marks a headless origin, not that this skill created it) whose log shows the last turn finished. It refuses Desktop-app or terminal threads, busy threads, and threads whose state it cannot read, because a second process writing the same thread would fork it; use `send` for live sessions. The check runs once before resuming, so it reduces but cannot rule out a race with another process.
- A message `send` queues to a headless thread waits until something resumes it, and is then folded into that turn. Use `resume`, not `send`, for headless threads.
- Whether a headless thread also appears in the Codex app's sidebar has not been verified.

## Common mistakes

- Calling `codex queue` directly without closing stdin hangs forever on an attached terminal. The helper passes `stdin=DEVNULL`; do the same (`< /dev/null`) if you ever call it by hand.
- Taking the first `task_complete` after sending. The user's own turns land in the same thread, so only the turn whose user message *starts* with your envelope header ending in `msg-id <id>]` is your reply. A msg-id quoted elsewhere does not count.
- Writing to `~/.codex/*.sqlite`. Codex owns those files; delivery goes only through `codex queue`.
- Using Claude Code's `SendMessage` or `ListAgents`: they reach Claude sessions only.

Codex's side of the protocol is the `message-claude` skill.
