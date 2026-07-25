// Mounts every surface off the SAME action registry:
//   UI    → GET  /
//   HTTP  → POST /_actions/:name
//   MCP   → POST /mcp            (JSON-RPC 2.0)
//   Agent → POST /_agent
//   Sync  → GET  /_events        (SSE, with polling fallback via /_actions/list-tasks)
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { join, dirname, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { callAction, listActions, onChange } from './actions.mjs';
import { runAgent } from './agent.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const PORT = Number(process.env.PORT ?? 4173);
const HOST = process.env.HOST ?? '0.0.0.0';

const MIME = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.svg': 'image/svg+xml', '.webmanifest': 'application/manifest+json' };

const json = (res, code, body) => {
  const s = JSON.stringify(body);
  res.writeHead(code, { 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': Buffer.byteLength(s), 'Access-Control-Allow-Origin': '*' });
  res.end(s);
};

const readBody = (req) => new Promise((resolve) => {
  let b = ''; req.on('data', (c) => (b += c));
  req.on('end', () => { try { resolve(b ? JSON.parse(b) : {}); } catch { resolve({}); } });
});

// ── live sync ────────────────────────────────────────────────────────────────
const clients = new Set();
onChange((payload) => {
  const frame = `data: ${JSON.stringify(payload)}\n\n`;
  for (const res of clients) { try { res.write(frame); } catch {} }
});

// ── MCP: actions become tools with zero extra code ───────────────────────────
const toJSONSchema = (schema = {}) => ({
  type: 'object',
  properties: Object.fromEntries(Object.entries(schema).map(([k, s]) => [k, {
    type: s.type === 'number' ? 'number' : s.type === 'boolean' ? 'boolean' : 'string',
    description: s.description ?? '',
    ...(s.enum ? { enum: s.enum } : {}),
  }])),
  required: Object.entries(schema).filter(([, s]) => s.required).map(([k]) => k),
});

async function handleMCP(req, res) {
  const msg = await readBody(req);
  const reply = (result) => json(res, 200, { jsonrpc: '2.0', id: msg.id ?? null, result });
  const fail = (code, message) => json(res, 200, { jsonrpc: '2.0', id: msg.id ?? null, error: { code, message } });

  switch (msg.method) {
    case 'initialize':
      return reply({ protocolVersion: '2024-11-05', capabilities: { tools: {} }, serverInfo: { name: 'todo-agent', version: '1.0.0' } });
    case 'notifications/initialized':
      return res.writeHead(202).end();
    case 'tools/list':
      return reply({
        tools: listActions().filter((a) => a.agentTool !== false).map((a) => ({
          name: a.name, description: a.description, inputSchema: toJSONSchema(a.schema),
        })),
      });
    case 'tools/call': {
      const { name, arguments: args = {} } = msg.params ?? {};
      try {
        const value = await callAction(name, args, { surface: 'mcp', actor: 'agent' });
        return reply({ content: [{ type: 'text', text: JSON.stringify(value, null, 2) }] });
      } catch (e) {
        return reply({ content: [{ type: 'text', text: `Error: ${e.message}` }], isError: true });
      }
    }
    default:
      return fail(-32601, `Method not found: ${msg.method}`);
  }
}

// ── server ───────────────────────────────────────────────────────────────────
const server = createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);
  const path = url.pathname;

  if (req.method === 'OPTIONS') {
    return res.writeHead(204, { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET,POST,OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type' }).end();
  }

  if (path === '/mcp' && req.method === 'POST') return handleMCP(req, res);

  if (path === '/_events') {
    res.writeHead(200, { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache', Connection: 'keep-alive', 'Access-Control-Allow-Origin': '*' });
    res.write('retry: 3000\n\n');
    clients.add(res);
    const ping = setInterval(() => { try { res.write(': ping\n\n'); } catch {} }, 25000);
    req.on('close', () => { clearInterval(ping); clients.delete(res); });
    return;
  }

  if (path === '/_actions' && req.method === 'GET') {
    return json(res, 200, listActions().map(({ name, description, schema, agentTool, needsApproval, mutates }) =>
      ({ name, description, schema, agentTool, needsApproval, mutates })));
  }

  if (path.startsWith('/_actions/') && req.method === 'POST') {
    const name = path.slice('/_actions/'.length);
    try {
      const input = await readBody(req);
      const surface = req.headers['x-surface'] ?? 'http';
      return json(res, 200, { ok: true, value: await callAction(name, input, { surface, actor: 'human' }) });
    } catch (e) {
      return json(res, 400, { ok: false, error: e.message });
    }
  }

  if (path === '/_agent' && req.method === 'POST') {
    try {
      const { message, autoApprove } = await readBody(req);
      if (!message?.trim()) return json(res, 400, { ok: false, error: 'message is required' });
      return json(res, 200, { ok: true, ...(await runAgent(message, { autoApprove })) });
    } catch (e) {
      return json(res, 500, { ok: false, error: e.message });
    }
  }

  // static
  const file = path === '/' ? 'index.html' : path.replace(/^\/+/, '');
  try {
    const buf = await readFile(join(here, 'public', file));
    return res.writeHead(200, { 'Content-Type': MIME[extname(file)] ?? 'application/octet-stream' }).end(buf);
  } catch {
    return res.writeHead(404, { 'Content-Type': 'text/plain' }).end('Not found');
  }
});

server.listen(PORT, HOST, () => {
  console.log(`\n  ✦ Ambient — agent-native todo\n`);
  console.log(`    UI     http://localhost:${PORT}`);
  console.log(`    MCP    http://localhost:${PORT}/mcp`);
  console.log(`    HTTP   POST http://localhost:${PORT}/_actions/<name>`);
  console.log(`    Agent  POST http://localhost:${PORT}/_agent`);
  console.log(`\n    ${listActions().length} actions · ${listActions().filter(a => a.agentTool !== false).length} exposed to agents\n`);
});
