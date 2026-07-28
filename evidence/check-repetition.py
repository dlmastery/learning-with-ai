#!/usr/bin/env python3
"""
Flag recurring claims that are restated without pointing at where they are established.

A survey reuses a small set of load-bearing results. That is correct — each one is
doing different work in a different argument. What is not correct is restating a
finding as though it were new, because it inflates apparent breadth and makes 33
sections read as 33 essays rather than one paper.

The rule: a recurring claim may appear anywhere. Outside its HOME section it must
carry a cross-reference (a section number) within a short window, so a reader can
tell they are meeting an old friend rather than a new fact.

Usage:  python3 evidence/check-repetition.py [--strict]
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SURVEY = ROOT / "survey"
WINDOW = 700          # chars either side that may carry the cross-reference
XREF = re.compile(r'§\s?\d{1,2}|section\s+\d{1,2}', re.I)

# claim -> (pattern, home section prefix)
CLAIMS = [
 ("Bastani −17% unassisted",  r"−17%|17% worse",                        "01"),
 ("Sierra Leone estimate",    r"Sierra Leone",                          "09"),
 ("retrieval practice g≈0.50",r"g = 0\.499|g ≈ 0\.50|g = 0\.50",        "24"),
 ("felt/real d≈0.48",         r"d ≈ 0\.48|d≈0\.48",                     "01"),
 ("expertise reversal",       r"\+?0\.505|−0\.428|-0\.428",             "22"),
 ("Fuchs 1991 decision rule", r"only the arm|CBM-ExS",                  "04"),
 ("Null-Learner Test",        r"Null-Learner",                          "14"),
 ("zero RCTs on disability",  r"zero.{0,40}disabilit|0\*?\*? mention disabilit", "04"),
]

def main():
    bare = []
    for f in sorted(SURVEY.glob("*.md")):
        sec = f.stem[:2]
        t = f.read_text(encoding="utf-8")
        for name, pat, home in CLAIMS:
            if sec == home:
                continue                       # the home section establishes it
            for m in re.finditer(pat, t, re.I):
                lo, hi = max(0, m.start()-WINDOW), min(len(t), m.end()+WINDOW)
                if not XREF.search(t[lo:hi]):
                    bare.append((f.stem, t.count("\n",0,m.start())+1, name, home))
                    break                      # one flag per claim per section
    if not bare:
        print(f"repetition: OK — {len(CLAIMS)} recurring claims, "
              f"{len(list(SURVEY.glob('*.md')))} sections, every restatement cross-referenced")
        return 0
    print(f"repetition: {len(bare)} restatement(s) with no cross-reference\n")
    for stem, line, name, home in bare:
        print(f"  survey/{stem}.md:{line}")
        print(f"    restates : {name}   (established in §{home})")
        print(f"    fix      : add a §{home} reference within a paragraph, or cut the restatement\n")
    return 1

if __name__ == "__main__":
    rc = main()
    sys.exit(rc if "--strict" in sys.argv else 0)
