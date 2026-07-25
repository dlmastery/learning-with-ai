---
name: antigravity-cli
description: "Delegate coding to Google Antigravity CLI (agy) — terminal agent with plan mode and sub-agents."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Coding-Agent, Antigravity, Google, Gemini, Planning, Sub-Agents]
    related_skills: [claude-code, codex, grok-cli, coding-agent-router]
---

# Antigravity CLI (`agy`)

Delegate coding tasks to Google's Antigravity CLI via the Hermes terminal.
`agy` is the terminal counterpart to the Antigravity IDE and shares its agent
harness — multi-step reasoning, tool calling, and sub-agents.

## When to use

- Tasks that benefit from an explicit plan-then-execute pass (`--mode plan`)
- Work that should be scoped to a persistent project/conversation
- A third independent opinion alongside Claude Code and Codex

## Prerequisites

- `agy` on PATH — installed at `~/.local/bin/agy`
  (verify: `terminal(command="which agy && agy --help | head -3")`)
- **Interactive sign-in required once.** Running `agy models` before sign-in
  fails with *"Please sign in to view available models."* The user must run
  bare `agy` in a real terminal to complete the browser login. Hermes cannot
  do this sign-in headlessly — surface the instruction to the user instead of
  retrying.
- Verify auth before delegating: `agy models` should list models, not error.

## One-Shot Tasks (headless)

`-p/--print` runs a single prompt non-interactively and prints the response:

```
terminal(command="agy -p 'Summarize the architecture of this repo'", workdir="~/project", pty=true)
```

For tasks that write files, auto-approve tool permissions or the run will block
on a prompt:

```
terminal(command="agy --dangerously-skip-permissions -p 'Add input validation to api/handlers.py'", workdir="~/project", pty=true)
```

Default print timeout is 5 minutes — raise it for longer work:

```
terminal(command="agy --print-timeout 20m --dangerously-skip-permissions -p 'Refactor the storage layer'", workdir="~/project", background=true, pty=true)
```

## Plan Mode

Get a plan without letting the agent edit anything:

```
terminal(command="agy --mode plan -p 'Plan the migration from SQLite to Postgres'", workdir="~/project", pty=true)
```

`--mode accept-edits` is the counterpart for execution runs.

## Key Flags

| Flag | Effect |
|------|--------|
| `-p, --print "..."` | Headless one-shot; prints the response and exits |
| `--print-timeout <dur>` | Wait limit for print mode (default `5m0s`) |
| `--dangerously-skip-permissions` | Auto-approve all tool permission requests |
| `--mode plan \| accept-edits` | Plan-only vs. execute-and-edit |
| `--model <model>` | Model for this session (see `agy models`) |
| `--effort low \| medium \| high` | Reasoning effort |
| `--agent <name>` | Pick a specific agent (see `agy agents`) |
| `--add-dir <path>` | Add another directory to the workspace (repeatable) |
| `--sandbox` | Run with terminal restrictions enabled |
| `-c, --continue` | Continue the most recent conversation |
| `--conversation <id>` | Resume a specific conversation |
| `--project <id>` / `--new-project` | Scope the session to a project |

## Subcommands

`agy models`, `agy agents`, `agy plugin`, `agy update`, `agy changelog`.

## Background Mode

```
terminal(command="agy --print-timeout 30m --dangerously-skip-permissions -p '<task>'", workdir="~/project", background=true, pty=true)
process(action="poll", session_id="<id>")
process(action="log", session_id="<id>")
```

## Rules

1. **Always use `pty=true`** — `agy` is an interactive TUI and hangs without a PTY.
2. **Always use `-p`** for delegation — bare `agy` opens the TUI and never returns.
3. **Check sign-in first** with `agy models`; if it errors, tell the user to run bare `agy` themselves. Do not loop on it.
4. **Raise `--print-timeout`** for anything beyond a quick edit — the 5m default silently cuts long runs short.
5. **`--dangerously-skip-permissions` only inside a git worktree** you can throw away, and review `git diff` before merging.
6. **Use `--mode plan` first** on unfamiliar codebases, then execute.
