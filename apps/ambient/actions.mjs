// ONE definition per operation. Every surface — UI, agent, HTTP, MCP, CLI —
// calls the same `run`. This is the Agent-Native parity invariant: there is no
// second implementation anywhere, so the UI and the agent cannot drift.
import { db, nowISO, newId, audit, setAppState, getAppState } from './db.mjs';

const registry = new Map();

/**
 * @param {object} def
 * @param {string} def.name
 * @param {string} def.description   shown to the model as the tool description
 * @param {object} def.schema        JSON-Schema-ish: { field: {type, required, enum, description} }
 * @param {boolean} [def.agentTool]  false hides it from the agent (UI-only affordances)
 * @param {boolean} [def.needsApproval] pause before running (outward-facing / hard to undo)
 * @param {boolean} [def.mutates]    whether it writes (drives audit + live-sync broadcast)
 * @param {Function} def.run
 */
export function defineAction(def) {
  if (registry.has(def.name)) throw new Error(`Duplicate action: ${def.name}`);
  registry.set(def.name, { agentTool: true, needsApproval: false, mutates: false, ...def });
  return def;
}

export const listActions = () => [...registry.values()];
export const getAction = (name) => registry.get(name);

/** Validate input against the action's declared schema. One validator, all surfaces. */
function validate(action, input = {}) {
  const out = {};
  for (const [field, spec] of Object.entries(action.schema ?? {})) {
    let v = input[field];
    if (v === undefined || v === null || v === '') {
      if (spec.required) throw new Error(`Missing required field: ${field}`);
      if (spec.default !== undefined) v = spec.default;
      else continue;
    }
    if (spec.type === 'number') {
      v = Number(v);
      if (Number.isNaN(v)) throw new Error(`${field} must be a number`);
    }
    if (spec.type === 'boolean') v = v === true || v === 'true' || v === 1;
    if (spec.enum && !spec.enum.includes(v)) {
      throw new Error(`${field} must be one of: ${spec.enum.join(', ')}`);
    }
    out[field] = v;
  }
  return out;
}

const listeners = new Set();
export const onChange = (fn) => { listeners.add(fn); return () => listeners.delete(fn); };
const broadcast = (payload) => { for (const fn of listeners) { try { fn(payload); } catch {} } };

/**
 * The single entry point every surface funnels through. Validate → authorize →
 * apply → audit → broadcast. Agent writes reach the UI without a manual refresh,
 * which the framework calls its #1 promise.
 */
export async function callAction(name, input = {}, ctx = {}) {
  const action = registry.get(name);
  if (!action) throw new Error(`Unknown action: ${name}`);
  const surface = ctx.surface ?? 'http';
  const actor = ctx.actor ?? (surface === 'agent' ? 'agent' : 'human');

  if (action.agentTool === false && surface === 'agent') {
    throw new Error(`Action '${name}' is not available to the agent`);
  }

  const args = validate(action, input);
  const result = await action.run(args, { surface, actor });

  if (action.mutates) {
    audit(name, surface, actor, args);
    broadcast({ action: name, surface, actor });
  }
  return result;
}

// ─────────────────────────────────────────────────────────────────────────────
// Actions
// ─────────────────────────────────────────────────────────────────────────────

const PRIORITIES = [1, 2, 3];

defineAction({
  name: 'list-tasks',
  description: 'List tasks. Filter by status (open/done/all) or project. Returns the full task objects.',
  schema: {
    status: { type: 'string', enum: ['open', 'done', 'all'], default: 'all', description: 'Which tasks to return' },
    project: { type: 'string', description: 'Restrict to one project' },
  },
  run: ({ status = 'all', project }) => {
    let sql = 'SELECT * FROM tasks';
    const where = [], params = [];
    if (status !== 'all') { where.push('status = ?'); params.push(status); }
    if (project) { where.push('project = ?'); params.push(project); }
    if (where.length) sql += ' WHERE ' + where.join(' AND ');
    sql += ' ORDER BY status ASC, priority ASC, position ASC, created_at DESC';
    return db.prepare(sql).all(...params);
  },
});

defineAction({
  name: 'add-task',
  description: 'Create a task. Use this whenever the user wants something added to their list.',
  mutates: true,
  schema: {
    title: { type: 'string', required: true, description: 'Short imperative title' },
    notes: { type: 'string', default: '', description: 'Optional detail' },
    priority: { type: 'number', enum: PRIORITIES, default: 2, description: '1 urgent, 2 normal, 3 someday' },
    due: { type: 'string', description: 'ISO date (YYYY-MM-DD)' },
    project: { type: 'string', default: 'Inbox', description: 'Project/bucket name' },
  },
  run: ({ title, notes = '', priority = 2, due, project = 'Inbox' }) => {
    const id = newId(), ts = nowISO();
    const min = db.prepare('SELECT MIN(position) AS m FROM tasks').get()?.m ?? 0;
    db.prepare(
      `INSERT INTO tasks (id,title,notes,status,priority,due,project,position,created_at,updated_at)
       VALUES (?,?,?,'open',?,?,?,?,?,?)`,
    ).run(id, title.trim(), notes, priority, due ?? null, project, min - 1, ts, ts);
    return db.prepare('SELECT * FROM tasks WHERE id = ?').get(id);
  },
});

// A single patch-style update rather than one action per field. The framework
// warns that a long, overlapping tool list degrades the model's tool selection.
defineAction({
  name: 'update-task',
  description: 'Update any field of a task: title, notes, priority, due date, project, or status.',
  mutates: true,
  schema: {
    id: { type: 'string', required: true },
    title: { type: 'string' },
    notes: { type: 'string' },
    priority: { type: 'number', enum: PRIORITIES },
    due: { type: 'string', description: 'ISO date, or empty string to clear' },
    project: { type: 'string' },
    status: { type: 'string', enum: ['open', 'done'] },
  },
  run: (args) => {
    const { id, ...patch } = args;
    const existing = db.prepare('SELECT * FROM tasks WHERE id = ?').get(id);
    if (!existing) throw new Error(`No task with id ${id}`);

    const fields = [], params = [];
    for (const [k, v] of Object.entries(patch)) {
      fields.push(`${k} = ?`);
      params.push(k === 'due' && v === '' ? null : v);
    }
    if (patch.status === 'done') { fields.push('completed_at = ?'); params.push(nowISO()); }
    if (patch.status === 'open') { fields.push('completed_at = NULL'); }
    if (!fields.length) return existing;

    fields.push('updated_at = ?'); params.push(nowISO());
    db.prepare(`UPDATE tasks SET ${fields.join(', ')} WHERE id = ?`).run(...params, id);
    return db.prepare('SELECT * FROM tasks WHERE id = ?').get(id);
  },
});

defineAction({
  name: 'toggle-task',
  description: 'Flip a task between open and done.',
  mutates: true,
  schema: { id: { type: 'string', required: true } },
  run: ({ id }) => {
    const t = db.prepare('SELECT * FROM tasks WHERE id = ?').get(id);
    if (!t) throw new Error(`No task with id ${id}`);
    const next = t.status === 'done' ? 'open' : 'done';
    db.prepare('UPDATE tasks SET status=?, completed_at=?, updated_at=? WHERE id=?')
      .run(next, next === 'done' ? nowISO() : null, nowISO(), id);
    return db.prepare('SELECT * FROM tasks WHERE id = ?').get(id);
  },
});

defineAction({
  name: 'delete-task',
  description: 'Permanently delete a task.',
  mutates: true,
  needsApproval: true, // irreversible
  schema: { id: { type: 'string', required: true } },
  run: ({ id }) => {
    const t = db.prepare('SELECT * FROM tasks WHERE id = ?').get(id);
    if (!t) throw new Error(`No task with id ${id}`);
    db.prepare('DELETE FROM tasks WHERE id = ?').run(id);
    return { deleted: id, title: t.title };
  },
});

defineAction({
  name: 'clear-completed',
  description: 'Delete every completed task at once.',
  mutates: true,
  needsApproval: true,
  schema: {},
  run: () => {
    const n = db.prepare("SELECT COUNT(*) AS c FROM tasks WHERE status='done'").get().c;
    db.prepare("DELETE FROM tasks WHERE status='done'").run();
    return { cleared: n };
  },
});

defineAction({
  name: 'view-screen',
  description: "Read what the user is currently looking at — active filter, project, and selected task.",
  schema: {},
  run: () => ({
    navigation: getAppState('navigation') ?? { filter: 'open', project: null, selectedId: null },
    counts: db.prepare(
      `SELECT COUNT(*) AS total,
              SUM(CASE WHEN status='open' THEN 1 ELSE 0 END) AS open,
              SUM(CASE WHEN status='done' THEN 1 ELSE 0 END) AS done
       FROM tasks`).get(),
  }),
});

// UI-only: the browser reports its view so the agent isn't blind to it.
defineAction({
  name: 'set-navigation',
  description: 'Record the current UI view.',
  agentTool: false,
  schema: {
    filter: { type: 'string', enum: ['open', 'done', 'all'], default: 'open' },
    project: { type: 'string' },
    selectedId: { type: 'string' },
  },
  run: (nav) => { setAppState('navigation', nav); return nav; },
});

defineAction({
  name: 'list-projects',
  description: 'List every project with open/done counts.',
  schema: {},
  run: () => db.prepare(
    `SELECT project,
            COUNT(*) AS total,
            SUM(CASE WHEN status='open' THEN 1 ELSE 0 END) AS open
     FROM tasks GROUP BY project ORDER BY open DESC, project ASC`).all(),
});

defineAction({
  name: 'stats',
  description: 'Completion statistics: totals, completion rate, overdue count, and recent throughput.',
  schema: {},
  run: () => {
    const base = db.prepare(
      `SELECT COUNT(*) AS total,
              SUM(CASE WHEN status='open' THEN 1 ELSE 0 END) AS open,
              SUM(CASE WHEN status='done' THEN 1 ELSE 0 END) AS done
       FROM tasks`).get();
    const today = new Date().toISOString().slice(0, 10);
    const overdue = db.prepare(
      "SELECT COUNT(*) AS c FROM tasks WHERE status='open' AND due IS NOT NULL AND due < ?").get(today).c;
    const week = db.prepare(
      "SELECT COUNT(*) AS c FROM tasks WHERE status='done' AND completed_at >= ?")
      .get(new Date(Date.now() - 7 * 864e5).toISOString()).c;
    const total = base.total || 0;
    return {
      ...base,
      overdue,
      completedThisWeek: week,
      completionRate: total ? Math.round((base.done / total) * 100) : 0,
    };
  },
});
