/**
 * Link check — every internal link and anchor resolves.
 *
 * Two failures made this necessary. All 29 contents links on the paper page were
 * dead at once, because the rail and the headings were slugged by two hand-matched
 * rules and nothing compared them. Separately, 83 of 87 cross-references pointed at
 * real but wrong sections after a regex renumbering. A reference that resolves to
 * the wrong place is worse than a dead one, because nothing flags it — this catches
 * only the dead kind, which is why numbering is generated rather than patched.
 *
 * Covers docs/**.html (href targets, same-page anchors, cross-page fragments) and
 * the Markdown surfaces (README, CORRECTIONS, survey/, process/) for relative
 * links to files that must exist.
 *
 *   node evidence/check-links.mjs        # exits non-zero on a dead link
 */
import { readdirSync, readFileSync, existsSync, statSync } from 'fs';
import { join, dirname, resolve, relative } from 'path';
import { fileURLToPath } from 'url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const rel = p => relative(ROOT, p);

function walk(dir, ext, out = []) {
  if (!existsSync(dir)) return out;
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) walk(p, ext, out);
    else if (e.name.endsWith(ext)) out.push(p);
  }
  return out;
}

const ids = f => new Set([...readFileSync(f, 'utf8').matchAll(/\sid="([^"]+)"/g)].map(m => m[1]));

const dead = [];
let checked = 0;

// ── the built site ───────────────────────────────────────────────────────────
const pages = walk(join(ROOT, 'docs'), '.html');
for (const f of pages) {
  const html = readFileSync(f, 'utf8');
  const own = ids(f);
  for (const [, href] of html.matchAll(/href="([^"]+)"/g)) {
    if (/^(https?:|mailto:|#$)/.test(href)) continue;
    checked++;
    if (href.startsWith('#')) {
      if (!own.has(href.slice(1))) dead.push([rel(f), href, 'anchor not on this page']);
      continue;
    }
    const [path, frag] = href.split('#');
    const target = resolve(dirname(f), path || '.');
    if (!existsSync(target)) { dead.push([rel(f), href, 'file does not exist']); continue; }
    if (frag && target.endsWith('.html') && !ids(target).has(frag))
      dead.push([rel(f), href, 'fragment not in target']);
  }
}

// ── the Markdown surfaces ────────────────────────────────────────────────────
const docs = [
  join(ROOT, 'README.md'), join(ROOT, 'CORRECTIONS.md'),
  ...walk(join(ROOT, 'survey'), '.md'), ...walk(join(ROOT, 'process'), '.md'),
].filter(existsSync);

for (const f of docs) {
  for (const [, href] of readFileSync(f, 'utf8').matchAll(/\]\(([^)\s]+)\)/g)) {
    if (/^(https?:|mailto:|#)/.test(href)) continue;
    checked++;
    const target = resolve(dirname(f), href.split('#')[0]);
    if (!existsSync(target)) dead.push([rel(f), href, 'file does not exist']);
  }
}

if (!pages.length || !docs.length) {
  console.error('scanned nothing — refusing to pass');
  process.exit(2);
}

if (!dead.length) {
  console.log(`links: OK — ${pages.length} pages + ${docs.length} documents, `
            + `${checked} internal links, all resolve`);
  process.exit(0);
}

console.log(`links: ${dead.length} dead of ${checked}\n`);
for (const [f, href, why] of dead) console.log(`  ${f}\n    ${href}  — ${why}\n`);
process.exit(1);
