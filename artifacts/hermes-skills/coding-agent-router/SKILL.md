---
name: coding-agent-router
description: "Pick the right CLI coding agent for a task, or race several in parallel git worktrees and merge the winner."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [Orchestration, Coding-Agent, Routing, Worktrees, Arbitration, Parallel]
    related_skills: [claude-code, codex, grok-cli, antigravity-cli, hermes-agent]
---

# Coding Agent Router

Arbitrate between the CLI coding agents installed on this machine: choose one
for a task, or run several in parallel on isolated git worktrees and merge the
best result. This is the local, cross-platform equivalent of worktree IDEs like
Superset (macOS/x64-only) — same model, driven from Hermes instead of a GUI.

## Available agents on this machine

| Agent | Command | Headless invocation | Auth |
|-------|---------|---------------------|------|
| Claude Code | `claude` | `claude -p "<task>"` | `~/.claude/.credentials.json` |
| Codex | `codex` | `codex exec "<task>"` | `~/.codex/auth.json` |
| Grok | `grok` | `grok -p "<task>"` | `~/.grok/user-settings.json` |
| Antigravity | `agy` | `agy -p "<task>"` | interactive sign-in required (bare `agy`) |

Before routing, confirm the agent exists and is authenticated. Skip any agent
that fails its check rather than retrying it — and say which ones you skipped.

## Routing heuristics

| Task shape | Route to |
|-----------|----------|
| Large multi-file refactor, long autonomous run | `claude` |
| Feature build inside a git repo, PR review, batch issue fixing | `codex` |
| Fast scoped edit, quick explanation, cheap second opinion | `grok` |
| Plan-first work on an unfamiliar codebase | `agy --mode plan` |
| High-stakes change, **and the repo has a real test suite** | race (see gate below) |
| High-stakes change, **no tests** | do NOT race — use parallel specialization |

Route to a single agent by default.

### The racing gate — read before using race.sh

Racing only pays under specific conditions. Measured evidence (2026):

- With **tests** as the verifier, best-of-N gains ~+8pp.
- With **model-generated tests**, ~+2.7pp.
- With an **LLM judge alone**, it measured **negative** on two of three
  benchmarks (−3.2pp, −1.7pp). A judge with no execution signal picks wrong
  often enough to lose the oracle gain.

So: **race only when a passing/failing test suite decides the winner.** If the
only available judge is "an agent reads the diffs," you are in the configuration
that measured net-negative. Pick one agent instead.

Two more findings that shape how to race:

- **Same prompt ≠ independent samples.** Identical prompts produce near-identical
  opening moves and correlated errors. Heterogeneous agents (different vendors)
  are the diversity that actually helps — which is what `race.sh` does. Never
  race the same agent N times and expect N independent attempts.
- **Racing plans beats racing patches.** Selecting among *proposals* before
  implementation is cheaper and scores better than selecting among finished
  diffs. Prefer `--mode plan` / a planning prompt for the race, then implement
  the winner once.

### Prefer parallel specialization to racing

The pattern with the strongest evidence is **N agents contributing intelligence,
one agent contributing actions** — multiple reviewers with distinct lenses,
single writer. A three-lens review beat a single strong agent by ~2 findings per
PR *at lower total cost* than the single agent. Racing writers, by contrast,
multiplies cost and creates merge conflicts in code nobody on your team wrote.

Use racing for: bake-offs where you genuinely want to compare agents, or a
high-stakes change with a decisive test suite. Use specialization for
everything else.

## Single-agent delegation

Load the agent's own skill (`claude-code`, `codex`, `grok-cli`,
`antigravity-cli`) for its flags and caveats, then run it with `pty=true`.

## Racing agents in parallel worktrees

`scripts/race.sh` creates one git worktree per agent, runs each agent headless
and in parallel against the same prompt, and writes each result to its own
branch plus a diff file for comparison.

```
terminal(command="bash ~/.hermes/skills/autonomous-ai-agents/coding-agent-router/scripts/race.sh -r ~/project -a claude,codex,grok -t 'Fix the memory leak in the websocket handler'", pty=true, background=true)
```

Output lands in `/tmp/agent-race-<timestamp>/`:

```
/tmp/agent-race-<ts>/
  claude/  worktree + branch race/<ts>/claude
  codex/   worktree + branch race/<ts>/codex
  grok/    worktree + branch race/<ts>/grok
  claude.diff  codex.diff  grok.diff    ← the candidate patches
  claude.log   codex.log   grok.log     ← agent transcripts
  SUMMARY.txt                           ← per-agent exit status, diffstat, duration
```

### Arbitrating the results

After the race completes, judge the candidates rather than picking the first
that finished:

1. Read `SUMMARY.txt` — discard agents that errored or produced an empty diff.
2. Read each `*.diff`. Compare on: does it actually address the task, blast
   radius, whether tests/types still pass, and whether it invents dependencies.
3. Run the project's tests inside the winning worktree before merging.
4. Merge the winner:
   ```
   terminal(command="git merge --squash race/<ts>/codex && git commit", workdir="~/project")
   ```
5. Clean up:
   ```
   terminal(command="bash ~/.hermes/skills/autonomous-ai-agents/coding-agent-router/scripts/race.sh --cleanup /tmp/agent-race-<ts> -r ~/project", pty=true)
   ```

State the trade-off you saw between candidates when you report back — the point
of racing is the comparison, not just the winner.

## Rules

1. **Never race outside a git repo** — worktrees are the isolation boundary. No repo, no race.
2. **Commit or stash first** — `race.sh` refuses to run on a dirty tree.
3. **One agent by default.** Race only when tests decide the winner (see the racing gate), or for an explicit bake-off.
4. **Copy gitignored config into each worktree.** `.env`, local settings, and credentials do not come along with `git worktree add` — the single most common first-run failure. Check what the project needs before launching, and allocate distinct ports/databases per worktree if the task runs a server or migrations.
5. **Skip unauthenticated agents**, report them, and continue with the rest — do not block the whole race on one login.
6. **Never auto-merge.** A human or Hermes must read the diff and run tests before merging.
7. **Always clean up worktrees** — orphaned worktrees corrupt later `git worktree` operations.
