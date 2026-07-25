#!/usr/bin/env node
// The CLI surface. Same actions, no server required.
//   node cli.mjs actions
//   node cli.mjs action add-task --title="Ship it" --priority=1
//   node cli.mjs agent "clear everything I finished and add buy milk"
import { callAction, listActions } from './actions.mjs';
import { runAgent } from './agent.mjs';

const [, , cmd, ...rest] = process.argv;

const parseFlags = (argv) => {
  const out = {}; const positional = [];
  for (const a of argv) {
    const m = /^--([^=]+)(?:=(.*))?$/.exec(a);
    if (m) out[m[1]] = m[2] ?? true; else positional.push(a);
  }
  return { flags: out, positional };
};

const c = { dim: (s) => `\x1b[2m${s}\x1b[0m`, b: (s) => `\x1b[1m${s}\x1b[0m`, g: (s) => `\x1b[32m${s}\x1b[0m`, r: (s) => `\x1b[31m${s}\x1b[0m`, y: (s) => `\x1b[33m${s}\x1b[0m` };

try {
  switch (cmd) {
    case 'actions': {
      for (const a of listActions()) {
        const tags = [a.agentTool === false ? c.dim('ui-only') : null, a.needsApproval ? c.y('approval') : null].filter(Boolean).join(' ');
        console.log(`  ${c.b(a.name.padEnd(18))} ${a.description} ${tags}`);
      }
      break;
    }
    case 'action': {
      const [name, ...args] = rest;
      if (!name) throw new Error('usage: cli.mjs action <name> [--field=value]');
      const { flags } = parseFlags(args);
      console.log(JSON.stringify(await callAction(name, flags, { surface: 'cli', actor: 'human' }), null, 2));
      break;
    }
    case 'agent': {
      const message = rest.join(' ');
      if (!message) throw new Error('usage: cli.mjs agent "<what you want>"');
      const { flags } = parseFlags(rest);
      const r = await runAgent(message.replace(/--\S+/g, '').trim(), { autoApprove: !!flags.yes });
      console.log(`\n  ${c.b(r.reply)}\n`);
      for (const x of r.results) {
        const mark = x.status === 'ok' ? c.g('✓') : x.status === 'needs-approval' ? c.y('⚠') : c.r('✗');
        console.log(`  ${mark} ${x.action} ${c.dim(JSON.stringify(x.input))}${x.error ? c.r(' — ' + x.error) : ''}`);
      }
      console.log();
      break;
    }
    case 'ls': {
      const tasks = await callAction('list-tasks', { status: rest[0] ?? 'open' }, { surface: 'cli' });
      if (!tasks.length) { console.log(c.dim('\n  nothing here\n')); break; }
      console.log();
      for (const t of tasks) {
        const box = t.status === 'done' ? c.g('◉') : '○';
        const pri = t.priority === 1 ? c.r('!') : t.priority === 3 ? c.dim('·') : ' ';
        console.log(`  ${box} ${pri} ${t.status === 'done' ? c.dim(t.title) : t.title} ${c.dim(t.project)}${t.due ? c.dim(' · ' + t.due) : ''}`);
      }
      console.log();
      break;
    }
    default:
      console.log(`
  ${c.b('Ambient')} — agent-native todo

    ${c.b('actions')}                       list every action
    ${c.b('action')} <name> [--f=v]         run one action
    ${c.b('agent')} "<request>" [--yes]     talk to the agent
    ${c.b('ls')} [open|done|all]            quick list
`);
  }
} catch (e) {
  console.error(`\n  ${c.r('error')} ${e.message}\n`);
  process.exit(1);
}
