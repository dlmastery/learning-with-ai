#!/usr/bin/env python3
"""
Voice check — is the prose written, or is it generated?

The adversarial slop reviews found that this survey has a small number of
sentence shapes and reuses them until they stop carrying meaning: 578 em-dashes,
147 `X, not Y` antitheses, 1,013 bold spans (one every 48 words), fourteen
sections closing with an identical checklist header, six carrying a seven-word
header verbatim, and eleven of nineteen ending on the same rhetorical move.

None of those is wrong once. Each is wallpaper at the observed rate, and none
was visible while writing because nothing counted them.

Two kinds of check:

  PER-FILE RATE   a tic per 1,000 words, over a budget
  CORPUS SHAPE    the same header, or the same closing move, across too many files

Thresholds are set at roughly half the rate the reviews measured — high enough
that a deliberate use passes, low enough that a habit fails.

Usage:  python3 evidence/check-voice.py [--strict] [--verbose]
"""
import pathlib, re, sys, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = sorted(ROOT.glob("survey/*.md"))

# The four surfaces a reader meets before the survey. They were reviewed
# separately and have their own tics — see evidence/slop-front-matter.md.
FRONT = ["README.md", "docs/index.html", "docs/deck.html", "docs/thesis.html"]

# ── per-file rates, per 1,000 words ───────────────────────────────────────────
RATE = {
    "em-dash":            (re.compile(r"—"),                                    6.0),
    "bold span":          (re.compile(r"\*\*[^*\n]+\*\*"),                      12.0),
    "`X, not Y`":         (re.compile(r",\s+not\s+\w"),                         1.6),
    "`rather than`":      (re.compile(r"\brather than\b"),                      1.0),
    "enumerative lead":   (re.compile(r"(?m)^(Two|Three|Four|Five)\s+\w+[^.\n]{0,40}\s+follow"), 0.6),
    "`, and it is` appos":(re.compile(r",\s+and it is\s+\w"),                   0.6),
    "`exactly`":          (re.compile(r"\bexactly\b"),                          0.6),
    "`precisely`":        (re.compile(r"\bprecisely\b"),                        0.3),
    "honesty talk":       (re.compile(r"\bhonest(?:y|ly)?\b"),                  0.5),
    "self-ranking":       (re.compile(r"the (?:most|single most|least|cheapest|strongest|clearest)"
                                      r"\s+[\w\- ]{0,30}\s+in this (?:survey|document|section)"), 0.3),
    "pull-quote aphorism":(re.compile(r"(?m)^>\s*\*\*"),                        0.5),
}

FLOOR = 3   # minimum occurrences before a rate overrun is a habit

# ── front-matter tics, per 1,000 words ────────────────────────────────────────
# The negation beat — state a negation, supply the correction as a second clause —
# runs 12 times across these four files and 60+ times in the paper. It earns its
# keep when the reader genuinely holds the belief being negated, which is once or
# twice per document, not once per screen.
FRONT_RATE = {
    "negation beat":      (re.compile(r"\bis not\b[^.\n]{0,70}\.\s+(?:It|They|That|This)\s+is\b"), 1.2),
    "`Which …` fragment": (re.compile(r"(?m)^\s*(?:<[^>]+>\s*)*Which\b"),                             0.8),
    "`the whole X`":      (re.compile(r"\bthe whole (?:problem|strategy|effect|landscape|frame|"
                                     r"corpus|time|point|argument|thing)\b"),                          1.0),
    "`nobody has X`":     (re.compile(r"\bnobody has\b"),                                             1.5),
    "`worth X-ing`":      (re.compile(r"\bworth (?:stating|doing|having|running|taking|being)\b"),     0.8),
    "`the honest X`":     (re.compile(r"\bthe honest \w+"),                                            0.5),
    "em-dash":            (re.compile(r"—"),                                                           8.0),
    "bold span":          (re.compile(r"\*\*[^*\n]+\*\*|<(?:b|strong)\b[^>]*>"),                     16.0),
}

# A run of identical words repeated inside one file, or across README and the
# dashboard, is a paragraph that was pasted rather than written twice.
DUP_RUN = 14

# ── corpus-wide shapes: how many distinct files may share one ─────────────────
SHAPE_CAP = 4

HEADER = re.compile(r"(?m)^#{2,3}\s+(?:\d+\.\s*)?(.+?)\s*$")
CLOSING_ANTITHESIS = re.compile(
    r"(?:is|was|are|were)\s+not\s+[^.\n]{2,70}\.\s+(?:It|They|That|This)\s+(?:is|was|are|were)\s")


def words(t):
    return max(1, len(re.findall(r"\b[\w'-]+\b", t)))


def prose(p):
    """Front-matter surfaces: strip markup so the counts run over words only."""
    t = p.read_text(encoding="utf-8")
    if p.suffix == ".html":
        t = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", t)
    return t


def dupes(texts, n=DUP_RUN):
    """Longest repeated word-runs of length >= n, reported once each."""
    seen, hits = {}, []
    for label, t in texts:
        w = re.findall(r"[A-Za-z][\w'-]*", re.sub(r"<[^>]+>", " ", t))
        for i in range(len(w) - n + 1):
            key = " ".join(w[i:i + n]).lower()
            if key in seen and seen[key] != (label, i - 1):
                hits.append((seen[key][0], label, " ".join(w[i:i + n])))
            seen.setdefault(key, (label, i))
    out, used = [], set()
    for a, b, s in hits:
        head = " ".join(s.split()[:6]).lower()
        if head not in used:
            used.add(head); out.append((a, b, s))
    return out


def body(p):
    """Prose only: no front matter, no fenced code, no tables."""
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S)
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"(?m)^\|.*$", " ", t)
    return t


def main():
    verbose = "--verbose" in sys.argv
    issues, headers, closers = [], collections.defaultdict(list), []

    for p in FILES:
        t = body(p)
        w = words(t)
        for name, (pat, budget) in RATE.items():
            n = len(pat.findall(t))
            rate = n * 1000 / w
            # A rate alone punishes short sections: one `precisely` in 1,200 words
            # is 0.8/1k and is not a habit. A tic must recur before it counts.
            if rate > budget and n >= FLOOR:
                issues.append((p.name, name, n, round(rate, 1), budget))

        for h in HEADER.findall(t):
            key = re.sub(r"[^a-z ]", "", h.lower()).strip()
            if len(key.split()) >= 3:
                headers[key].append(p.name)

        tail = "\n".join(t.rstrip().splitlines()[-14:])
        if CLOSING_ANTITHESIS.search(tail):
            closers.append(p.name)

    front_texts = []
    for rel in FRONT:
        f = ROOT / rel
        if not f.exists():
            continue
        t = prose(f)
        w = words(re.sub(r"<[^>]+>", " ", t))
        front_texts.append((rel, t))
        for name, (pat, budget) in FRONT_RATE.items():
            n = len(pat.findall(t))
            if n * 1000 / w > budget and n >= FLOOR:
                issues.append((rel, name, n, round(n * 1000 / w, 1), budget))

    duplicated = dupes(front_texts)

    shapes = [(h, f) for h, f in headers.items() if len(f) > SHAPE_CAP]
    over_closers = len(closers) > SHAPE_CAP

    if not issues and not shapes and not over_closers and not duplicated:
        print(f"voice: OK — {len(FILES)} sections + {len(front_texts)} front-matter "
              f"surfaces, every tic within budget, no header shared by more than "
              f"{SHAPE_CAP} files, no duplicated passages")
        return 0

    print(f"voice: {len(issues)} rate overrun(s), {len(shapes)} over-shared header(s)"
          f"{', closing move over-used' if over_closers else ''}\n")

    if issues:
        by_file = collections.defaultdict(list)
        for f, name, n, rate, budget in issues:
            by_file[f].append((name, n, rate, budget))
        print(f"  {'section':34}{'tic':22}{'n':>4}{'/1k':>7}{'budget':>8}")
        for f in sorted(by_file, key=lambda k: -len(by_file[k])):
            for i, (name, n, rate, budget) in enumerate(sorted(by_file[f], key=lambda r: -r[2] / r[3])):
                print(f"  {(f if i == 0 else ''):34}{name:22}{n:>4}{rate:>7}{budget:>8}")
                if not verbose and i == 2 and len(by_file[f]) > 3:
                    print(f"  {'':34}… {len(by_file[f]) - 3} more (--verbose)")
                    break
        print()

    for h, f in sorted(shapes, key=lambda s: -len(s[1])):
        print(f"  [SHARED HEADER ×{len(f)}] \"{h[:64]}\"")
        print(f"    {', '.join(sorted(f))}\n")

    for a, b, s in duplicated:
        where = f"twice in {a}" if a == b else f"{a} and {b}"
        print(f"  [DUPLICATED ≥{DUP_RUN} WORDS] {where}")
        print(f"    \"{s[:96]}…\"\n")

    if over_closers:
        print(f"  [CLOSING MOVE ×{len(closers)}] the `not X. It is Y.` antithesis ends "
              f"{len(closers)} sections; cap is {SHAPE_CAP}")
        print(f"    {', '.join(sorted(closers))}\n")

    return 1


if __name__ == "__main__":
    rc = main()
    sys.exit(rc if "--strict" in sys.argv else 0)
