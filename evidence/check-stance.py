#!/usr/bin/env python3
"""
Stance check — does an artifact argue FOR the mission or against it?

This project's mission is that everyone becomes a polymath: the end of rationed
attention. Its research discipline is adversarial. Those two are compatible, but
only if the discipline is the *warrant* and the mission is the *message*.

Repeatedly it inverted. The dashboard opened on three disqualifying findings. The
deck's identity became "we build the examiner." Section titles read *"what it
cannot buy"*, *"what that is worth"*, *"what has actually been measured"*. Each was
fixed when pointed at, and reappeared somewhere else, because nothing was measuring
the pattern.

This does. Three checks:

  1. DEFENSIVE HEADINGS — headings whose shape is an audit rather than a claim.
  2. OPENING STANCE      — does the first screen of an artifact say what becomes
                           possible, or what fails?
  3. VANITY METRICS      — volume as an opening argument.

Usage:  python3 evidence/check-stance.py [--strict]
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Reader-facing surfaces. research/raw/ is deliberately exempt: those are audits by
# design and are not what a reader meets first.
FRONT = ["README.md", "docs/index.html", "docs/deck.html", "docs/thesis.html"]
PROSE = ["survey/*.md"]

# Heading shapes that announce an audit. Each was found in this repo.
DEFENSIVE = re.compile(
    r"what (it|they|that) cannot"
    r"|what that is worth"
    r"|what has actually been"
    r"|how honest"
    r"|what .{0,24}actually (means|is worth|consists of)"
    r"|and what it (does not|cannot)"
    r"|one claim that holds"
    r"|read as evidence and not", re.I)

# Words that assert a limit, and words that assert a possibility.
LIMIT = re.compile(r"\b(not|never|no|nothing|nobody|cannot|fails?|failed|null|"
                   r"wrong|error|absent|missing|unmeasured|unverifiable|"
                   r"disqualif\w+|harm|worse|inert|zero)\b", re.I)
POSSIBLE = re.compile(r"\b(can|could|becomes?|possible|unlocks?|enables?|builds?|"
                      r"buildable|now|new|first|works?|gains?|reaches?|"
                      r"achieves?|opportunity)\b", re.I)

VANITY = re.compile(r"\b[\d,]{4,}\s*(words|sources|citations)"
                    r"|\b\d+\s+sections\s*[·,]"
                    r"|\b\d+\s+research reports\b"
                    r"|[\d,]+-word\b", re.I)

def text_of(p):
    t = p.read_text(encoding="utf-8", errors="ignore")
    if p.suffix == ".html":
        t = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", t)
        t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)

def headings(p):
    raw = p.read_text(encoding="utf-8", errors="ignore")
    if p.suffix == ".html":
        return [re.sub(r"<[^>]+>", "", h) for h in re.findall(r"<h[12][^>]*>(.*?)</h[12]>", raw, re.S)]
    return [l.lstrip("# ").strip() for l in raw.splitlines() if l.startswith("#")]

def main():
    issues = []

    # 1 — defensive headings, everywhere
    for pat in FRONT + PROSE:
        for f in sorted(ROOT.glob(pat)):
            for h in headings(f):
                if DEFENSIVE.search(h):
                    issues.append(("DEFENSIVE HEADING", f.relative_to(ROOT), h[:78],
                                   "reads as an audit; state the claim instead"))

    # 2 — opening stance on the front-facing artifacts only
    for pat in FRONT:
        for f in sorted(ROOT.glob(pat)):
            head = text_of(f)[:1600]
            lim, pos = len(LIMIT.findall(head)), len(POSSIBLE.findall(head))
            if lim > pos * 1.3 and lim >= 8:
                issues.append(("OPENING STANCE", f.relative_to(ROOT),
                               f"{lim} limit words vs {pos} possibility words in the first screen",
                               "the first screen argues what fails; lead with what becomes possible"))

    # 3 — vanity metrics on any reader-facing surface
    for pat in FRONT:
        for f in sorted(ROOT.glob(pat)):
            for m in VANITY.finditer(text_of(f)[:2500]):
                issues.append(("VANITY METRIC", f.relative_to(ROOT), m.group(0).strip(),
                               "volume is not an argument; counts belong on the status page"))

    if not issues:
        n = len(list(ROOT.glob("survey/*.md"))) + len(FRONT)
        print(f"stance: OK — {n} surfaces, no defensive headings, "
              f"no limit-led openings, no vanity metrics")
        return 0

    print(f"stance: {len(issues)} issue(s)\n")
    for kind, path, found, fix in issues:
        print(f"  [{kind}] {path}")
        print(f"    found : {found}")
        print(f"    fix   : {fix}\n")
    return 1

if __name__ == "__main__":
    rc = main()
    sys.exit(rc if "--strict" in sys.argv else 0)
