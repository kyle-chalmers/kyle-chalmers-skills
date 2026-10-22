---
name: git-ship
description: "Stage, commit, push, PR, and squash merge the current branch to main"
---

# Git Ship

You are executing the full git shipping workflow. Ship the current feature branch by staging changes, committing, pushing, creating a PR, and squash merging to main.

## Input

The user provides a single argument indicating merge preference:

- **Affirmative** (yes, y, yeah, sure, yep, yes merge, etc.) → run the full flow including squash merge
- **Negative** (no, n, nope, nah, no merge, skip merge, etc.) → stop after PR is created, skip merge and cleanup
- **No argument provided** → default to no merge (stop after PR is created)

Always auto-generate both the commit message and PR description — never ask the user for these.

## Message Guidelines

**Commit message:**
- Conventional commit format: `type: subject` (e.g., `feat: add login page`)
- Subject line: 100 characters max
- Optional body: max 3 bullet points, each under 72 characters
- No fluff — describe what changed and why only if non-obvious

**PR description:**
- `## Summary` section: 3–5 bullet points max, plain English, no technical jargon
- `## Test plan` section: 1–3 lines on how to verify
- Total body: 100 words max
- Footer: `Generated with AI`

## Pre-flight Checks

1. **If on main, auto-create a feature branch.** Analyze the staged/unstaged/untracked changes (run `git diff` and `git status`) to understand what changed, then create an appropriately named branch using conventional naming (e.g., `docs/update-readme`, `feat/add-auth`, `fix/api-timeout`). Run `git checkout -b <branch-name>` to switch to it before continuing.
2. **Verify there are changes to commit.** Run `git status` to check for staged, unstaged, or untracked changes. If there are no changes AND no unpushed commits, abort.
3. **Required checks.** Run the checks specified by the repository. If a build script exists (`pnpm build`, `npm run build`, `make`, etc.), run it. If no build system is detected, skip the build.
4. **Review proportionate to the change.** For behavior changes or changes spanning several components, use the installed `ai-friend-review` skill when available and validate its findings before shipping. If it is unavailable or fails, report that limitation. A failed reviewer is not a passing review. Do not invent an enforced review gate; follow the actual repository checks.

## Shipping Flow

### Step 1: Stage & Commit (if there are uncommitted changes)

- Run `git status` and `git diff --stat` to understand all changes
- Stage all relevant files (prefer naming files explicitly over `git add .`)
- Do NOT stage files that likely contain secrets (`.env`, credentials, etc.)
- Commit with the auto-generated message in conventional commit format
- Follow the actual agent runtime and repository attribution convention. Do not invent a model identity or co-author.

### Step 2: Push

- Push the branch to origin with `-u` flag: `git push -u origin <branch-name>`

### Step 3: Create PR

- Create a PR using `gh pr create` with:
  - A conventional commit title (use the commit message subject line)
  - A body following the Message Guidelines above
  - Include the `Generated with AI` footer

### Step 4: Squash Merge

- Run this step only when the user requested merging. Otherwise stop with the pull request URL.
- Wait for required checks and reviews to pass.
- Merge using `gh pr merge --squash`

### Step 5: Cleanup

- Switch back to main: `git checkout main`
- Pull latest: `git pull`
- Delete the local feature branch: `git branch -d <branch-name>`
- Delete the remote branch: `git push origin --delete <branch-name>`
- **Sanity check:** Run `git status --porcelain`. Preserve any unexpected changes and report their paths. Do not restore, reset, or discard user work automatically.
- Confirm success by showing the merge commit

## Rules

- Use feature branch + PR workflow, never push directly to main. If a `CLAUDE.md` or `AGENTS.md` exists in the repo root, read it first and follow any git workflow conventions defined there
- Use squash merge only
- Use conventional commit format for all messages
- If any step fails, stop and report the error clearly — do not continue the flow
