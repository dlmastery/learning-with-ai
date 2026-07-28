#!/usr/bin/env python3
"""
Propagation check for superseded values.

The failure mode this exists to catch: a correction is recorded in CORRECTIONS.md
and applied in one file, while the superseded value survives somewhere else. That
happened six times on 2026-07-28 and an external reviewer found all six.

Every rule below is derived from a row in CORRECTIONS.md. A rule fires when a
superseded value appears in a published surface WITHOUT its correction nearby.
"Nearby" means within the same paragraph-sized window, because a correction that
does not reach the sentence it corrects is not a correction (C-17).

Usage:  python3 evidence/check-corrections.py            # report
        python3 evidence/check-corrections.py --strict   # exit 1 on any violation
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Published surfaces only. research/raw/ is an immutable record of what an agent
# found at a point in time and is deliberately NOT rewritten — see CORRECTIONS.md.
SURFACES = ["README.md", "CORRECTIONS.md", "CLAUDE.md", "AUDIT.md",
            "docs/index.html", "survey/*.md", "docs/demos/*.html"]

WINDOW = 600   # characters either side that may carry the correction

# (id, regex for the superseded value, regex that must appear nearby, human note)
RULES = [
    ("C-6/C-12", r"\bNickow[^.]{0,80}?0\.37\b|0\.37[^.]{0,60}?Nickow",
     r"0\.288|working[- ]paper|superseded",
     "Nickow pooled tutoring is 0.288 (AERJ 2024); 0.37 is the 2020 working paper"),
    ("C-13", r"0\.63\s*[–-]\s*0\.73",
     r"ceiling|estimand|spliced|superseded",
     "'0.63–0.73' splices a regression estimate to a ceiling-corrected floor"),
    ("C-4", r"\bd\s*=\s*0\.971\b|\b0\.971\b",
     r"unverifiab|≈\s*0\.93|0\.93",
     "d=0.971 is not verifiable; components imply ~0.93"),
    ("C-1", r"strongest evidence in the history of educational technology",
     r"was our error|corrected|not significant|\+0\.216",
     "Sierra Leone's unadjusted estimate is +0.216, not significant"),
    ("C-7", r"g\s*=\s*0\.56[^.]{0,120}?teachable|teachable[^.]{0,120}?g\s*=\s*0\.56",
     r"human|Kobayashi|untested",
     "g=0.56 is human learning-by-teaching, not the teachable-agent version"),
    ("C-18", r"Annex III[^.]{0,160}?2 August 2026|2 August 2026[^.]{0,160}?Annex III",
     r"2 December 2027|2026/1744|deferred|superseded",
     "Annex III deferred to 2 Dec 2027; only Article 50 bites 2 Aug 2026"),
    ("C-19", r"crew of seven|[Ss]even roles(?![^.]{0,200}registry)",
     r"registry of ten|active set|3[–-]5",
     "The roster is a registry of ten with an active set of 3-5"),
    ("C-2", r"no retention penalty|\+127%[^.]{0,80}?no penalty",
     r"−0\.004|-0\.004|n\.s\.|removes? (a )?harm",
     "Guardrails remove harm; the unassisted coefficient is -0.004, n.s."),
    ("C-16", r"g\s*=\s*0\.4?99?\b[^.]{0,100}?222 (classroom )?studies",
     r"I²\s*=\s*88|I2\s*=\s*88",
     "Retrieval practice g=0.50 must carry I²=88%"),
    ("C-15", r"Cepeda['’]?s? meta-analytic tradition",
     r"2025|classroom meta-analysis|superseded",
     "d=0.54 is from a 2025 classroom meta-analysis, not 'the Cepeda tradition'"),
    ("C-22", r"Sierra Leone[^.]{0,80}?school year",
     r"eight weeks|8 weeks|corrected",
     "The Sierra Leone trial ran eight weeks"),
    ("C-20", r"[Uu]nbounded item generation",
     r"14,929,920|finite|measured",
     "The adversary item space is finite and measured at 14,929,920"),
]

def files():
    for pat in SURFACES:
        yield from sorted(ROOT.glob(pat))

def main():
    violations = []
    for f in files():
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, IsADirectoryError):
            continue
        for cid, bad, cure, note in RULES:
            for m in re.finditer(bad, text, re.I):
                lo = max(0, m.start() - WINDOW)
                hi = min(len(text), m.end() + WINDOW)
                if not re.search(cure, text[lo:hi], re.I):
                    line = text.count("\n", 0, m.start()) + 1
                    violations.append((f.relative_to(ROOT), line, cid,
                                       m.group(0)[:60].replace("\n", " "), note))

    if not violations:
        print(f"corrections propagation: OK — {len(RULES)} rules, "
              f"{len(list(files()))} published surfaces, 0 violations")
        return 0

    print(f"corrections propagation: {len(violations)} VIOLATION(S)\n")
    for path, line, cid, snippet, note in violations:
        print(f"  {path}:{line}  [{cid}]")
        print(f"    found : {snippet!r}")
        print(f"    rule  : {note}\n")
    return 1

if __name__ == "__main__":
    rc = main()
    sys.exit(rc if "--strict" in sys.argv else 0)
