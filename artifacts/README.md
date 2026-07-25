# Session artifacts

Everything built during the 2026-07-25 session, preserved here so it survives.

## `../apps/ambient/` — agent-native reference implementation

A working todo app where **one action definition powers five surfaces**: UI,
agent, HTTP, MCP, and CLI. Built to the Agent-Native norms the survey advocates
and verified end-to-end — Hermes drove it over MCP, and the audit table shows two
different surfaces writing through the same `add-task` action.

Demonstrates concretely: actions as single source of truth · all state in SQL
(including ephemeral UI state, so the agent can see what the learner is looking
at) · live sync so agent writes reach the UI without refresh · approval gates on
irreversible actions.

Run: `node server.mjs` → http://localhost:4173 · MCP at `/mcp`.
Zero dependencies (Node 24 `node:sqlite`), which matters on aarch64.

## `hermes-skills/` — skills authored this session

| Skill | What |
|---|---|
| `agent-native` | Drive Agent-Native apps from Hermes over MCP |
| `coding-agent-router` | Route/race claude · codex · grok · agy, with `race.sh` |
| `grok-cli` | Grok CLI delegation |
| `antigravity-cli` | Google Antigravity (`agy`) delegation |

`coding-agent-router` carries an evidence-based racing gate: race **only** when
tests decide the winner. Measured — public tests +8.14pp, generated tests
+2.70pp, **LLM judge alone −3.20pp / −1.68pp**.

## `dgx-sunshine/` — hardened headless-streaming installer

Derived from `eelbaz/dgx-spark-headless-sunshine` with three changes: every
touched file backed up unconditionally, passwordless autologin **off** by default
(upstream enables it silently), and a generated `rollback.sh`. Not run.
