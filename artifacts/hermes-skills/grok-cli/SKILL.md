---
name: grok-cli
description: "Delegate coding to the Grok CLI (xAI) — fast one-shot edits, git-aware tasks."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Coding-Agent, Grok, xAI, Refactoring, Fast-Edits]
    related_skills: [claude-code, codex, antigravity-cli, coding-agent-router]
---

# Grok CLI

Delegate coding tasks to the `grok` CLI via the Hermes terminal. Grok is xAI's
conversational coding agent with text-editor capabilities.

## When to use

- Fast, well-scoped edits where latency matters more than deep reasoning
- Quick explanations of a file or diff
- Git-assisted operations (`grok git`)
- A cheap second opinion to compare against Claude Code or Codex output

Prefer `claude-code` or `codex` for large multi-file refactors and long
autonomous runs.

## Prerequisites

- `grok` on PATH (verify: `terminal(command="which grok")`)
- Auth via `GROK_API_KEY` env var, `-k/--api-key`, or the settings file at
  `~/.grok/user-settings.json`. A missing `GROK_API_KEY` alone does **not**
  mean Grok is unauthenticated — check the settings file first.
- Not restricted to git repos (unlike Codex), but `--directory` should still be
  set explicitly so edits land where you expect.

## One-Shot Tasks (headless)

`-p/--prompt` runs a single prompt and exits — this is the mode to use for
delegation:

```
terminal(command="grok -p 'Explain what src/auth.py does and list its exports'", workdir="~/project", pty=true)
```

Pin the working directory explicitly when the task edits files:

```
terminal(command="grok --directory ~/project -p 'Add a --verbose flag to cli.py'", pty=true)
```

## Model Selection

```
terminal(command="grok -m grok-code-fast-1 -p 'Fix the off-by-one in paginate()'", workdir="~/project", pty=true)
terminal(command="grok -m grok-4-latest -p 'Review this module for race conditions'", workdir="~/project", pty=true)
```

Use `grok-code-fast-1` for mechanical edits, `grok-4-latest` for reasoning.

## Background Mode (Long Tasks)

```
terminal(command="grok --directory ~/project -p 'Migrate the test suite to pytest'", background=true, pty=true)
# Returns session_id

process(action="poll", session_id="<id>")
process(action="log", session_id="<id>")
process(action="kill", session_id="<id>")
```

## Key Flags

| Flag | Effect |
|------|--------|
| `-p, --prompt "..."` | Headless one-shot; runs and exits |
| `-d, --directory <dir>` | Working directory for the session |
| `-m, --model <model>` | e.g. `grok-code-fast-1`, `grok-4-latest` |
| `-k, --api-key <key>` | Override the stored key |
| `-u, --base-url <url>` | Alternate endpoint |
| `--max-tool-rounds <n>` | Cap tool iterations (default 400) — lower it to bound cost |

## Subcommands

- `grok git` — git operations with AI assistance
- `grok mcp` — manage MCP servers available to Grok

## Rules

1. **Always use `pty=true`** — Grok is an interactive terminal app and will hang without a PTY.
2. **Always use `-p`** for delegation — without it Grok opens an interactive session that never returns.
3. **Always set `--directory` or `workdir`** — Grok defaults to its own launch directory, not yours.
4. **Bound runaway loops** with `--max-tool-rounds` (the default of 400 is very high) on open-ended tasks.
5. **Review the diff** — `git diff` after the run before committing anything.
6. **Parallel is fine** — multiple `grok -p` processes can run concurrently in separate worktrees.
