// All application state lives in SQL. This is Agent-Native rule #1.
// The UI is a projection of these tables; the agent reads and writes the same rows.
import { DatabaseSync } from 'node:sqlite';
import { mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const dbPath = process.env.TODO_DB ?? join(here, 'data', 'todo.db');
mkdirSync(dirname(dbPath), { recursive: true });

export const db = new DatabaseSync(dbPath);

db.exec(`
PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS tasks (
  id          TEXT PRIMARY KEY,
  title       TEXT NOT NULL,
  notes       TEXT NOT NULL DEFAULT '',
  status      TEXT NOT NULL DEFAULT 'open',      -- open | done
  priority    INTEGER NOT NULL DEFAULT 2,        -- 1 urgent, 2 normal, 3 someday
  due         TEXT,                              -- ISO date, nullable
  project     TEXT NOT NULL DEFAULT 'Inbox',
  position    REAL NOT NULL DEFAULT 0,
  created_at  TEXT NOT NULL,
  updated_at  TEXT NOT NULL,
  completed_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_tasks_status  ON tasks(status);
CREATE INDEX IF NOT EXISTS idx_tasks_project ON tasks(project);

-- Ephemeral UI state also lives in SQL, so the agent can see what the user
-- is looking at. This is the rule most implementations skip.
CREATE TABLE IF NOT EXISTS application_state (
  key        TEXT PRIMARY KEY,
  value      TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

-- Every mutating action is audited: who did it, from which surface.
CREATE TABLE IF NOT EXISTS audit (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  action     TEXT NOT NULL,
  surface    TEXT NOT NULL,                      -- ui | agent | http | mcp | cli
  actor      TEXT NOT NULL,                      -- human | agent
  input      TEXT NOT NULL,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS messages (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  role       TEXT NOT NULL,                      -- user | assistant | tool
  content    TEXT NOT NULL,
  created_at TEXT NOT NULL
);
`);

export const nowISO = () => new Date().toISOString();
export const newId = () => 't_' + Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4);

export function setAppState(key, value) {
  db.prepare(
    `INSERT INTO application_state (key, value, updated_at) VALUES (?, ?, ?)
     ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at`,
  ).run(key, JSON.stringify(value), nowISO());
}

export function getAppState(key) {
  const row = db.prepare('SELECT value FROM application_state WHERE key = ?').get(key);
  if (!row) return null;
  try { return JSON.parse(row.value); } catch { return null; }
}

export function audit(action, surface, actor, input) {
  db.prepare('INSERT INTO audit (action, surface, actor, input, created_at) VALUES (?,?,?,?,?)')
    .run(action, surface, actor, JSON.stringify(input ?? {}), nowISO());
}
