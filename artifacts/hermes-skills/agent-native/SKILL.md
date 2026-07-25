---
name: agent-native
description: "Drive Agent-Native apps from Hermes over MCP — link, inspect, and run actions."
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [Agent-Native, MCP, Actions, App-Framework, Builder-io, Orchestration]
    related_skills: [claude-code, codex, coding-agent-router]
---

# Agent-Native ↔ Hermes

Agent-Native (BuilderIO) is a framework where **one action definition powers six
surfaces**: UI, agent, HTTP, MCP, A2A, and CLI. Because every action is
automatically an MCP tool, Hermes can drive an entire Agent-Native app without
any per-app integration work.

## The core idea

```ts
// One definition. Every surface.
export default defineAction({
  schema: z.object({ emailId: z.string(), body: z.string() }),
  run: async ({ emailId, body }) => { await db.insert(replies).values({ emailId, body }); },
});
```

The consequence for Hermes: **you do not write tools for the app.** You attach to
its MCP endpoint and every action the app's UI can perform becomes a Hermes tool.

## Linking an app to Hermes

Any running Agent-Native app serves MCP at `/mcp` on its own URL.

```
# 1. Start the app (from the app's repo)
terminal(command="pnpm dev", workdir="~/myapp", background=true, notify_on_complete=true)

# 2. Confirm the port it bound (read the dev server output)
process(action="log", session_id="<id>")

# 3. Attach Hermes to it
terminal(command="hermes mcp add myapp --url http://localhost:<PORT>/mcp")

# 4. Verify the connection and see the tools it exposes
terminal(command="hermes mcp test myapp")
terminal(command="hermes mcp list")
```

After this, the app's actions appear as `myapp:<action-name>` tools. Narrow the
exposed set with `hermes mcp configure myapp` if the app has many actions — every
MCP tool consumes context window, and Agent-Native's own docs warn that a long
overlapping tool list degrades tool-selection quality.

## The reverse link (optional)

`hermes mcp serve` exposes Hermes itself over MCP, so an Agent-Native app's agent
can call *into* Hermes and use its installed skills:

```
terminal(command="hermes mcp serve", background=true)
```

Point the app's MCP client at that endpoint. Use this when the app needs a
capability Hermes already has a skill for, rather than reimplementing it as an
action.

## Driving an app without MCP

Every action is also reachable over HTTP and CLI. Useful for scripting, or when
the app is not running under an MCP-capable session.

```
# HTTP — actions are auto-mounted
terminal(command="curl -sX POST http://localhost:<PORT>/_agent-native/actions/<action-name> \
  -H 'Content-Type: application/json' -d '{\"field\":\"value\"}'")

# CLI — from the app repo
terminal(command="pnpm action <action-name> --field=value", workdir="~/myapp")

# Talk to the app's own agent
terminal(command="pnpm agent 'do the thing'", workdir="~/myapp", pty=true)
```

## The `agent-native` CLI

`@agent-native/core` ships a binary with (among others) `action`, `agent`,
`agents`, `add-app`, `api`, `app-skill`, `build`, `check`, and a `claude-code`
participant mode. Run `npx agent-native --help` inside an app repo to see the set
for that version — the command list changes between releases, so check rather
than assume.

## Rules

1. **Do not write Hermes tools that duplicate app actions.** Attach over MCP instead. Duplicated tool definitions are the clearest sign an integration is cosmetic rather than real.
2. **Prune the tool surface.** `hermes mcp configure <name>` to disable actions Hermes will never call. Every exposed tool costs context.
3. **Respect approval gates.** Actions marked `needsApproval` pause for human confirmation, and approval is bound to the specific arguments. Never try to route around this — it exists for outward-facing, hard-to-undo operations.
4. **Check the app is actually running** before adding the MCP server; `hermes mcp add` against a dead endpoint gives a confusing failure. `curl -sf <url>/mcp` first.
5. **The app owns its data.** Agent-Native keeps all state in SQL and the UI is a projection of it. Mutate through actions, never by touching the database directly — direct writes bypass validation, authorization, audit, and live-sync.
6. **One app per MCP entry.** Register each Agent-Native app under its own name so tools stay namespaced and you can disable one without affecting the others.
