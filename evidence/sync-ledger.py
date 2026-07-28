#!/usr/bin/env python3
"""Regenerate CORRECTIONS.md's scoreboard from its own rows.

The scoreboard was hand-maintained and drifted: the table said 7 external, the
prose said eight, the rows said 8, and the columns did not sum to the total.
A hand-kept count inside the document about not hand-keeping counts.
"""
import pathlib, re, sys, collections

P = pathlib.Path(__file__).resolve().parent.parent / "CORRECTIONS.md"
t = P.read_text()

rows = re.findall(r'^\| \*\*(C-\d+)\*\* \|(?:[^|]*\|){3}\s*([^|]+?)\s*\|$', t, re.M)
if not rows:
    print("no ledger rows parsed — refusing to write"); sys.exit(1)

def bucket(prov):
    p = prov.upper()
    if "EXTERNAL" in p:               return "external"
    if "DEMO BUILDER" in p or "BUILDER" in p or "SURVEY WRITER" in p: return "builders"
    if "SELF-VERIFY" in p:            return "verify"
    return "research"

counts = collections.Counter(bucket(p) for _, p in rows)
total, ext = len(rows), counts["external"]
NUM = {7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve"}

board = f"""## Scoreboard

*Generated from the rows above by `evidence/sync-ledger.py`. It drifted twice while
hand-maintained, which is the whole argument for generating it.*

| Source | Count |
|---|---|
| Caught by our own research | {counts['research']} |
| Caught by our own verification — including of our own warnings | {counts['verify']} |
| Caught by our own builders, working against their own briefs | {counts['builders']} |
| **Caught by an adversarial external reviewer** | **{ext}** |
| **Total** | **{total}** |

{NUM.get(ext, ext)} of {total} were found by someone whose job was to fail us — including
the two most damaging (C-12, C-13), the one about this ledger itself (C-23), and the one
that proved the propagation checker did not work (C-30). That ratio is the honest measure
of what an internal review process is worth, and it is the argument for commissioning the
hostile read rather than trusting the self-audit.
"""
t = re.sub(r'## Scoreboard\n.*$', board, t, flags=re.S)
P.write_text(t)
print(f"ledger scoreboard regenerated: {total} total — "
      + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
