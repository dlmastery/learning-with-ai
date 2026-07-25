// The agent surface. It has NO privileged path to the database — it calls the
// exact same actions the UI buttons call. That is the parity invariant.
//
// Backend is pluggable: an authenticated local CLI agent (claude / codex) or a
// local Ollama model. No API keys required either way.
import { spawn } from 'node:child_process';
import { callAction, listActions } from './actions.mjs';
import { db, nowISO } from './db.mjs';

const BACKEND = process.env.TODO_AGENT_BACKEND ?? 'claude'; // claude | codex | ollama
const OLLAMA_MODEL = process.env.TODO_OLLAMA_MODEL ?? 'hermes3';

function agentTools() {
  return listActions()
    .filter((a) => a.agentTool !== false)
    .map((a) => ({
      name: a.name,
      description: a.description,
      needsApproval: !!a.needsApproval,
      fields: Object.fromEntries(
        Object.entries(a.schema ?? {}).map(([k, s]) => [
          k,
          [s.type ?? 'string', s.required ? 'required' : 'optional', s.enum ? `one of ${s.enum.join('|')}` : '', s.description ?? '']
            .filter(Boolean).join(' · '),
        ]),
      ),
    }));
}

function buildPrompt(userMessage, screen) {
  return `You are the agent inside a todo application. You act by emitting action calls.

AVAILABLE ACTIONS (this is your complete capability set):
${JSON.stringify(agentTools(), null, 2)}

WHAT THE USER IS CURRENTLY LOOKING AT:
${JSON.stringify(screen, null, 2)}

USER MESSAGE:
${userMessage}

Respond with ONLY a JSON object, no prose and no code fences:
{"calls":[{"action":"add-task","input":{"title":"..."}}],"reply":"one short friendly sentence"}

Rules:
- Emit as many calls as the request needs. Emit none if the user only asked a question.
- To answer a question about their tasks, call list-tasks or stats first — never guess.
- Titles must be short and imperative. Infer priority and due date when the user implies them.
- Never invent a task id. If you need one, call list-tasks first in the same response.
- "reply" is what the user reads. Be warm and brief.`;
}

function runCLI(cmd, args, input, timeoutMs = 120000) {
  return new Promise((resolve, reject) => {
    const p = spawn(cmd, args, { stdio: ['pipe', 'pipe', 'pipe'] });
    let out = '', err = '';
    const timer = setTimeout(() => { p.kill('SIGTERM'); reject(new Error(`${cmd} timed out`)); }, timeoutMs);
    p.stdout.on('data', (d) => (out += d));
    p.stderr.on('data', (d) => (err += d));
    p.on('error', (e) => { clearTimeout(timer); reject(e); });
    p.on('close', () => { clearTimeout(timer); out.trim() ? resolve(out) : reject(new Error(err.slice(0, 300) || 'empty response')); });
    if (input) { p.stdin.write(input); p.stdin.end(); }
  });
}

async function think(prompt) {
  if (BACKEND === 'ollama') {
    const r = await fetch('http://localhost:11434/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model: OLLAMA_MODEL, prompt, stream: false, format: 'json' }),
    });
    if (!r.ok) throw new Error(`ollama ${r.status}`);
    return (await r.json()).response;
  }
  if (BACKEND === 'codex') return runCLI('codex', ['exec', '--skip-git-repo-check', prompt]);
  return runCLI('claude', ['-p', prompt, '--permission-mode', 'bypassPermissions']);
}

function extractJSON(text) {
  const cleaned = text.replace(/```json\s*|```/g, '').trim();
  const start = cleaned.indexOf('{');
  if (start === -1) throw new Error('no JSON in model output');
  // Walk to the matching brace so trailing prose can't break parsing.
  let depth = 0, inStr = false, esc = false;
  for (let i = start; i < cleaned.length; i++) {
    const c = cleaned[i];
    if (esc) { esc = false; continue; }
    if (c === '\\') { esc = true; continue; }
    if (c === '"') inStr = !inStr;
    if (inStr) continue;
    if (c === '{') depth++;
    else if (c === '}' && --depth === 0) return JSON.parse(cleaned.slice(start, i + 1));
  }
  throw new Error('unbalanced JSON in model output');
}

/** Run one agent turn. Returns { reply, calls, results }. */
export async function runAgent(userMessage, { autoApprove = false } = {}) {
  db.prepare('INSERT INTO messages (role, content, created_at) VALUES (?,?,?)')
    .run('user', userMessage, nowISO());

  const screen = await callAction('view-screen', {}, { surface: 'agent' });
  const raw = await think(buildPrompt(userMessage, screen));

  let plan;
  try { plan = extractJSON(raw); }
  catch (e) { throw new Error(`Could not parse the model's response (${e.message}). Raw: ${raw.slice(0, 200)}`); }

  const results = [];
  for (const call of plan.calls ?? []) {
    const { action, input = {} } = call;
    try {
      const def = listActions().find((a) => a.name === action);
      if (def?.needsApproval && !autoApprove) {
        results.push({ action, input, status: 'needs-approval' });
        continue;
      }
      const value = await callAction(action, input, { surface: 'agent', actor: 'agent' });
      results.push({ action, input, status: 'ok', value });
    } catch (e) {
      results.push({ action, input, status: 'error', error: e.message });
    }
  }

  const reply = plan.reply ?? 'Done.';
  db.prepare('INSERT INTO messages (role, content, created_at) VALUES (?,?,?)')
    .run('assistant', reply, nowISO());

  return { reply, calls: plan.calls ?? [], results };
}
