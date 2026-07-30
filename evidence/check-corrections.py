#!/usr/bin/env python3
"""
Propagation check for superseded values.

WHY THIS FILE EXISTS, AND WHY IT HAS A SELF-TEST.

The failure mode: a correction is recorded in CORRECTIONS.md and applied in one
file, while the superseded value survives elsewhere. That happened six times on
2026-07-28 and an external reviewer found all six.

The first version of this checker DID NOT WORK. A reviewer copied the tree, planted
the five superseded values in the exact form they had originally appeared, and the
checker printed "0 violations" and exited 0. Two defects:

  1. Patterns used `[^.]{0,80}` as a proximity window, which cannot cross the period
     in "Nickow et al." — the literal string that produced the original error.
  2. Cure words were generic ("corrected", "superseded"), so an unrelated occurrence
     within the window cleared a live violation.

A checker without a test is exactly the failure it claims to prevent. So:

    python3 evidence/check-corrections.py --self-test

plants each rule's known-bad string into a scratch copy and FAILS if the rule does
not fire. Run it before trusting a green result. `--strict` exits non-zero on any
violation; CI should run `--self-test` and `--strict` together.

Usage:
    python3 evidence/check-corrections.py              # report
    python3 evidence/check-corrections.py --strict     # exit 1 on violation
    python3 evidence/check-corrections.py --self-test  # prove the rules fire
"""
import pathlib, re, sys, tempfile, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Published surfaces only. research/raw/ is an immutable record of what an agent
# found at a point in time and is deliberately NOT rewritten (see CORRECTIONS.md).
SURFACES = ["README.md", "PAPER.md", "process/CLAUDE.md", "process/AUDIT.md",
            "docs/index.html", "docs/paper.html", "survey/*.md", "docs/demos/*.html"]
# CORRECTIONS.md is excluded: it is the ledger and must quote superseded values.

WINDOW = 400   # chars either side that may carry the cure

# A ledger row is ALLOWED to quote the superseded value — that is its job. A row is
# identified structurally (a table row whose first cell is a C-nn id), not by any
# keyword, so this cannot be used to launder prose. C-17 is exactly this case: a
# process correction that must quote the sentence it is about.
LEDGER_ROW = re.compile(r'^\s*(?:\|\s*(?:\*\*)?(C-\d+)|<tr><td>(C-\d+))', re.M)

def _real_ids():
    """Only ids that actually exist in CORRECTIONS.md may claim the exemption.
    Previously any '| C-99 |' prefix was trusted, so an invented id laundered
    four retired values at once."""
    led = ROOT / "CORRECTIONS.md"
    if not led.exists(): return set()
    return set(re.findall(r"^\| \*\*(C-\d+)\*\*", led.read_text(), re.M))

REAL_IDS = _real_ids()

def in_ledger_row(text, pos):
    start = text.rfind("\n", 0, pos) + 1
    m = LEDGER_ROW.match(text, start)
    if not m: return False
    cid = m.group(1) or m.group(2)
    return cid in REAL_IDS

class Rule:
    """bad: what must not appear.  cure: what makes it acceptable nearby.
    probe: a literal string, known to have appeared in the repo, used by --self-test."""
    def __init__(self, cid, bad, cure, note, probe):
        self.cid, self.note, self.probe = cid, note, probe
        self.bad = re.compile(bad, re.I)
        self.cure = re.compile(cure, re.I)

RULES = [
    Rule("C-58",
         r"(?:four|Four)[\s\S]{0,40}?(?:seven|those seven)?[\s\S]{0,20}?second[- ]language",
         r"three of (?:them|those seven)|EJ1415077|chemistry course",
         "Three of the seven ChatGPT RCTs are second-language learning, not four; "
         "EJ1415077 is a foundational chemistry course",
         "seven randomised trials, four of them second-language learning"),
    Rule("C-6/C-12",
         r"Nickow[\s\S]{0,120}?\b0\.37\b|\b0\.37\b[\s\S]{0,120}?Nickow|v:\s*0\.37\b",
         r"\b0\.288\b",
         "Nickow pooled tutoring is 0.288 (AERJ 2024); 0.37 is the superseded 2020 working paper",
         'note:"Nickow et al. — the honest field-wide number", v:0.37'),
    Rule("C-13", r"0\.63\s*[–—-]\s*0\.73", r"ceiling[- ]correct|two (different )?estimands|spliced",
         "'0.63-0.73' splices a regression estimate to a ceiling-corrected floor",
         "Kestin RCT 0.63–0.73 inside the human-tutoring range"),
    Rule("C-4", r"\b0\.971\b", r"unverifiab|≈\s*0\.93|\b0\.93\b",
         "d=0.971 is not verifiable; reported components imply ~0.93",
         "Expertise reversal interaction d = 0.971"),
    Rule("C-1", r"strongest evidence in the history of educational technology",
         r"was our error|\+?0\.216|not significant",
         "Sierra Leone's unadjusted estimate is +0.216, SE 0.137, not significant",
         "is the strongest evidence in the history of educational technology."),
    Rule("C-7", r"0\.56[\s\S]{0,160}?teachable|teachable[\s\S]{0,160}?0\.56",
         r"human\s+learning-by-teaching|Kobayashi|untested",
         "g=0.56 is human learning-by-teaching, not the teachable-agent version",
         "g = 0.56 is the teachable-agent effect"),
    Rule("C-18", r"Annex III[\s\S]{0,200}?2 August 2026|2 August 2026[\s\S]{0,200}?Annex III",
         r"2 December 2027|2026/1744",
         "Annex III deferred to 2 Dec 2027; only Article 50 applies from 2 Aug 2026",
         "On 2 August 2026 the EU AI Act's Annex III obligations begin to apply."),
    Rule("C-19", r"crew of seven|seven roles(?![\s\S]{0,300}?registry)",
         r"registry of ten|active set|3\s*[–—-]\s*5",
         "The roster is a registry of ten with an active set of 3-5",
         "Not one tutor. A crew of seven, each narrow"),
    Rule("C-2", r"no retention penalty|\+127%[\s\S]{0,120}?no penalty",
         r"−0\.004|-0\.004|removes? (a )?harm",
         "Guardrails remove harm; the guardrailed unassisted coefficient is -0.004, n.s.",
         "+127% with no retention penalty"),
    Rule("C-16", r"(?:\b0\.(?:50|499)\b|g\s*=\s*0\.5)[\s\S]{0,140}?222 (classroom )?studies|222 (classroom )?studies[\s\S]{0,140}?48,478",
         r"I²\s*=\s*88|I2\s*=\s*88",
         "Retrieval practice g=0.50 must carry its heterogeneity, I² = 88%",
         "g = 0.50 | 222 classroom studies · 48,478 students"),
    Rule("C-15", r"Cepeda['’]?s? meta-analytic tradition", r"2025|classroom meta-analysis",
         "d=0.54 is from a 2025 classroom meta-analysis, not 'the Cepeda tradition'",
         "Spacing / distributed practice | d = 0.54 | Cepeda meta-analytic tradition"),
    Rule("C-22", r"Sierra Leone[\s\S]{0,120}?school year", r"eight weeks|8 weeks",
         "The Sierra Leone trial ran eight weeks",
         "The Sierra Leone trial, the largest deployment we examine, ran across a school year"),
    Rule("C-20", r"[Uu]nbounded item generation", r"14,929,920|finite",
         "The adversary item space is finite and measured at 14,929,920",
         "Unbounded item generation"),
    Rule("C-21", r"99\.1%\s*@\s*0\.61\s*ms|99\.1%[\s\S]{0,60}?0\.61\s*ms",
         r"0\.38\s*[–—-]\s*0\.61|both (are )?reported|two harnesses",
         "Two harnesses measured 0.38 ms and 0.61 ms; report both, not the flattering one",
         "99.1% @ 0.61 ms"),
    Rule("C-3", r"Orton-Gillingham(?![\s\S]{0,300}?(0\.22|p\s*=\s*\.40|non-?significant|\bnulls?\b))",
         r"0\.22|non-?significant|p\s*=\s*\.40|\bnulls?\b|active ingredient",
         "Orton-Gillingham is g = 0.22, p = .40 against active comparison",
         "Orton-Gillingham, the most-requested intervention, is decades-replicated"),
    Rule("C-37", r"loop\s+equals\s+the\s+value|equals the value of the external check",
         r"bounded by",
         "The agentic rule is a BOUND, not an equality — SciCode has weak tests and still lands at 4.6%",
         "The value of an agentic loop equals the value of the external check it closes on."),
    Rule("C-26", r"WCAG\s*2\.2",
         r"WCAG\s*2\.1|incorporates|enforceable",
         "ADA Title II incorporates WCAG 2.1, not 2.2; deadlines moved to 26 Apr 2027/2028",
         "WCAG 2.2 AA is a floor, not a target."),
    Rule("C-27", r"accommodations[\s\S]{0,120}?known-good|known-good[\s\S]{0,120}?accommodations",
         r"0\.034|mandated|legally required",
         "Accommodations are legally mandated and evidentially weak (g = .034, p = .180)",
         "accommodations are part of the known-good intervention base"),
    Rule("C-29", r"Doroudi(?![\s\S]{0,400}?(21 of 41|over half|51%))",
         r"21 of 41|over half|51%",
         "Doroudi's overall finding is POSITIVE — 21 of 41 (51%) beat all baselines",
         "Doroudi et al. is a negative review of instructional sequencing."),
    Rule("C-25", r"[Ee]xactly one interaction survived",
         r"assistance|guidance|Noetel|how much help",
         "The survivor is narrower: prior knowledge moderates HOW MUCH HELP, not instruction broadly",
         "Exactly one interaction survived the fifty-year search."),
]

def surfaces():
    seen = []
    for pat in SURFACES:
        seen += sorted(ROOT.glob(pat))
    return seen

def scan(root):
    out = []
    for pat in SURFACES:
        for f in sorted(root.glob(pat)):
            try: text = f.read_text(encoding="utf-8")
            except Exception: continue
            for r in RULES:
                for m in r.bad.finditer(text):
                    if in_ledger_row(text, m.start()):
                        continue
                    lo, hi = max(0, m.start()-WINDOW), min(len(text), m.end()+WINDOW)
                    if not r.cure.search(text[lo:hi]):
                        out.append((f.relative_to(root), text.count("\n",0,m.start())+1,
                                    r.cid, m.group(0)[:70].replace("\n"," "), r.note))
    return out

def self_test():
    """Plant each rule's known-bad probe in a scratch copy; the rule must fire."""
    failures = []
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)/"repo"
        shutil.copytree(ROOT, tmp, ignore=shutil.ignore_patterns(".git","node_modules"))
        target = tmp/"survey"/"_selftest.md"
        for r in RULES:
            target.write_text("# self-test fixture\n\n" + r.probe + "\n")
            hits = [v for v in scan(tmp) if v[2] == r.cid and "_selftest" in str(v[0])]
            if not hits:
                failures.append((r.cid, r.probe[:60]))
        target.unlink(missing_ok=True)
    if failures:
        print(f"SELF-TEST FAILED — {len(failures)} rule(s) did not fire on their own probe:\n")
        for cid, probe in failures:
            print(f"  [{cid}] did not detect: {probe!r}")
        return 1
    print(f"self-test: OK — all {len(RULES)} rules fire on their planted probe")
    return 0

def main():
    argv = sys.argv[1:]
    rc = 0
    if "--self-test" in argv:
        rc |= self_test()
        if "--strict" not in argv:
            return rc
    n_surfaces = len(surfaces())
    if n_surfaces < 20:
        print(f"corrections propagation: FAILED — only {n_surfaces} surfaces found. "
              f"An empty or truncated scan is not a pass.")
        return 1
    v = scan(ROOT)
    if not v:
        print(f"corrections propagation: OK — {len(RULES)} rules, "
              f"{n_surfaces} published surfaces, {len(REAL_IDS)} ledger ids, 0 violations")
        return rc
    print(f"corrections propagation: {len(v)} VIOLATION(S)\n")
    for path, line, cid, snippet, note in v:
        print(f"  {path}:{line}  [{cid}]\n    found : {snippet!r}\n    rule  : {note}\n")
    return 1

if __name__ == "__main__":
    code = main()
    sys.exit(code if ("--strict" in sys.argv or "--self-test" in sys.argv) else 0)
