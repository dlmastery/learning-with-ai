#!/usr/bin/env python3
"""
Vintage check — fails when a legacy number is used as a bound on a frontier system.

WHY THIS FILE EXISTS.

The survey's headline numbers measure a different class of machine than the one this
project exists to build. Bloom's 2 sigma is a 1984 claim about human tutors working
from two early-1980s Chicago dissertations. VanLehn's 0.79/0.76 is a 2011 review of
human tutoring and rule-based ITS. Nickow's 0.288 is 96 randomised trials of human
tutoring with zero AI arms. The "0.2-0.4 SD band" is a rounding of three LLM-era
field trials that the corpus then re-describes as a shared pre-LLM ceiling.

Using any of those as the bound on what a 2026 frontier model can do is a category
error. `evidence/VINTAGE.md` is the audit; this file is its enforcement.

WHAT COUNTS AS A VIOLATION.

A legacy number appearing anywhere an argument is made about what an AI tutor can or
cannot do.

THE FIX IS TO DELETE IT, and this file's guidance said the opposite until 30 Jul.

Labelling a 1984 measurement does not stop it framing the argument — the owner
rejected that compromise twice. A pre-LLM number may not appear as a ceiling, a
bound, a comparator, a benchmark to beat, a concession condition, or a row in a
chart against a frontier result. Cut the sentence. Where no frontier measurement
exists, say the trial has not been run and specify it: an honest gap is a better
argument than a borrowed number, because the gap is an opportunity and the borrowed
number is a false ceiling.

They may still appear in three places, because there they are the RECORD of retiring
a number rather than an argument using it: `survey/19-the-canon.md` (history is its
subject), `CORRECTIONS.md` and the backstage `process/` docs, and any passage whose
surrounding text marks it as superseded, retracted or corrected.

WHY IT HAS A SELF-TEST, AND WHY AN EMPTY SCAN FAILS.

C-30: this repo shipped a checker that printed "0 violations" and exited 0 while
every error it was built to catch was present in the tree. C-36: a later version
returned OK after every surface was deleted. So:

    python3 evidence/check-vintage.py --self-test

plants each rule's known-bad probe into a scratch copy and FAILS if the rule does
not fire, and a scan finding fewer than MIN_SURFACES files fails rather than passing.

Usage:
    python3 evidence/check-vintage.py              # report
    python3 evidence/check-vintage.py --strict     # exit 1 on violation
    python3 evidence/check-vintage.py --self-test  # prove the rules fire
"""
import pathlib, re, sys, tempfile, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Published surfaces. research/raw/ is an immutable record of what an agent found at a
# point in time and is deliberately NOT rewritten (see CORRECTIONS.md), so it is out of
# scope here exactly as it is in check-corrections.py.
#
# docs/thesis.html and docs/deck.html ARE in scope. They are absent from
# check-corrections.py's SURFACES, which is how the C-51 violation on thesis.html
# survived — see VINTAGE.md worklist V15.
SURFACES = ["README.md", "PAPER.md", "process/CLAUDE.md", "process/AUDIT.md",
            "docs/index.html", "docs/paper.html", "docs/thesis.html", "docs/deck.html",
            "survey/*.md", "docs/demos/*.html"]
# CORRECTIONS.md and evidence/VINTAGE.md are excluded: they are the ledger and the audit,
# and their job is to quote the wrong forms.

MIN_SURFACES = 20
WINDOW = 400   # chars either side that may carry the class attribution

# PAPER.md and docs/paper.html are ASSEMBLED from survey/*.md by build-paper.py. They are
# scanned (omitting them is the C-36 hole) but reported separately, because fixing the
# survey source and rebuilding clears them. Fixing them directly does not.
GENERATED = {"PAPER.md", "docs/paper.html"}

# Proximity must not cross a section boundary. Two numbers in adjacent sections are not
# "near" each other in any sense a reader would recognise, and treating them as adjacent
# is how a proximity checker turns into noise nobody reads.
BOUNDARY = re.compile(r"\n\s*#|\n\s*-{3,}|\n\s*\*{3,}|<h[1-6]\b|<hr\b")

# A ledger row is ALLOWED to quote the bad form. Identified structurally, by a real id.
LEDGER_ROW = re.compile(r'^\s*(?:\|\s*(?:\*\*)?(C-\d+)|<tr><td>(C-\d+))', re.M)

def _real_ids():
    led = ROOT / "CORRECTIONS.md"
    if not led.exists():
        return set()
    return set(re.findall(r"^\| \*\*(C-\d+)\*\*", led.read_text(encoding="utf-8"), re.M))

REAL_IDS = _real_ids()

def in_ledger_row(text, pos):
    start = text.rfind("\n", 0, pos) + 1
    m = LEDGER_ROW.match(text, start)
    if not m:
        return False
    return (m.group(1) or m.group(2)) in REAL_IDS


# ── Fragments ────────────────────────────────────────────────────────────────
#
# FRONTIER_CLAIM: text asserting what an AI / LLM / frontier system does, can do,
# achieves, is bounded by, or is measured at. Deliberately narrow. A bare mention
# of "AI" is not a claim; "AI tutoring achieves", "the ceiling for", "what a model
# can" are.
#
# Note the [\s\S] proximity windows: `[^.]{0,N}` cannot cross the period in
# "Nickow et al.", which is the exact defect that produced C-30.

# A bare trial name is NOT a claim. "Sierra Leone" and "Kestin" appear in correction
# ledgers and source lists where no capability is being asserted; including them made the
# rule fire on process/AUDIT.md's list of self-corrections. A claim needs a system term
# joined to an achievement or bound.
FRONTIER_CLAIM = (
    r"(?:AI[- ]tutor(?:ing|s)?|LLM tutor(?:ing|s)?|frontier (?:model|system)|"
    r"the (?:real )?ceiling|best AI|"
    r"what (?:a |an |the )?(?:AI|LLM|model|system)s? (?:can|could|achieve)|"
    r"(?:AI|LLM|the model)s? (?:can|achieves?|reach(?:es)?|lands? at|is bounded))"
)

# Naming the class is the cure. These are the phrases that make the usage legitimate,
# and each one names WHAT the number measured or WHEN — never a generic hedge.
HUMAN_CLASS = r"human tutor|human tutoring|human one-to-one|in-person|human arm|human-delivered|human tutee|human learning-by-teaching"
ITS_CLASS   = r"pre-?LLM|rule-based|intelligent tutoring system|\bITS\b|Cognitive Tutor|ALEKS|before LLMs|Ma et al|Steenbergen-Hu|2011|2014"
FRONTIER_ERA = r"LLM-era|frontier-era|202[3-6]|Sierra Leone|Nigeria|Rori|three (?:field )?trials"


class Rule:
    """bad : what must not appear (the legacy number NEAR a frontier claim).
       cure: what makes it acceptable within WINDOW chars — always a class or a year.
       probe: a literal string, in the form it appears or appeared in this repo,
              used by --self-test to prove the rule fires."""
    def __init__(self, vid, bad, cure, note, probe):
        self.vid, self.note, self.probe = vid, note, probe
        self.bad = re.compile(bad, re.I)
        self.cure = re.compile(cure, re.I)


RULES = [
    # ── V-BLOOM ────────────────────────────────────────────────────────────────
    Rule("V-BLOOM",
         r"(?:2\s?σ|two[- ]sigma|2[- ]sigma|Bloom'?s? (?:2|two))"
         r"[\s\S]{0,220}?" + FRONTIER_CLAIM
         + r"|" + FRONTIER_CLAIM + r"[\s\S]{0,220}?(?:2\s?σ|two[- ]sigma|2[- ]sigma|Bloom'?s? (?:2|two))",
         HUMAN_CLASS + r"|1984|does not replicate|did not replicate|retired|Anania|Burke|dissertation",
         "Bloom's 2 sigma is a 1984 claim about a HUMAN tutoring + mastery bundle, from two "
         "early-1980s Chicago dissertations. Naming it near an AI capability claim requires "
         "saying so, or saying it does not replicate.",
         "Two sigma is the target an AI tutor should be measured against."),

    # ── V-BAND ────────────────────────────────────────────────────────────────
    Rule("V-BAND",
         r"0\.2\s*[–—-]\s*0\.4(?:\s*SD)?",
         # Any phrasing that establishes the band's frontier provenance clears it.
         # The first four were the cure list; the rest are the phrasings the
         # rewrite actually reached for.
         FRONTIER_ERA + r"|answer freely|three trials|Sierra Leone|LLM tutoring|"
         r"immediate post-test|teacher-supervised|three field (?:trials|studies)|"
         r"rounding of|no pooling|no pooled estimate|did not exist in 20|"
         r"four countries|deployment trials cluster",
         "The 0.2-0.4 SD band is FRONTIER by construction: a rounding of three LLM-era field "
         "trials (Sierra Leone +0.258 adjusted / +0.216 n.s. unadjusted; Nigeria +0.23-0.31 with "
         "~43% attrition; Rori 0.37 across 11 clusters, developer-authored). It is not a pooled "
         "pre-LLM estimate and has no confidence interval. Say what it is a band OF.",
         "The measured 0.2–0.4 SD band is the ceiling every system lands in."),

    # ── V-BAND-SAMEBAND ───────────────────────────────────────────────────────
    Rule("V-BAND-SAMEBAND",
         r"same band as[\s\S]{0,60}?(?:ITS|intelligent tutoring|human tutor)"
         r"|(?:ITS|intelligent tutoring|human tutoring)[\s\S]{0,40}?the same band",
         r"2014|2011|Ma et al|Steenbergen-Hu|Nickow|96 (?:randomi[sz]ed|RCT)|constituent|unestablished",
         "'The same band as ITS and human tutoring' merges three classes measured decades apart. "
         "The ITS comparator is two 2014 meta-analyses; the human comparator is Nickow's 96 RCTs. "
         "Name the sources and their years, or the sentence asserts an equivalence it has not shown.",
         "Quote the band, not the ceiling. 0.2 SD, the same band as ITS and human tutoring."),

    # ── V-ITS-SPLICE ──────────────────────────────────────────────────────────
    Rule("V-ITS-SPLICE",
         r"0\.32\s*[–—-]\s*0\.(?:42|57)",
         r"Ma et al|Steenbergen-Hu|2014|two meta|spliced|separate meta",
         "'0.32-0.42' (and '0.32-0.57') appear in NO single source. They are spliced from "
         "Steenbergen-Hu & Cooper 2014 (g = 0.32-0.37, 39 studies, college) and Ma et al. 2014 "
         "(g = 0.42 vs teacher-led; 0.57 vs other CBI). Two 2014 metas, constituent years "
         "unestablished. Attribute both, or do not print a range.",
         "the same band as pre-LLM ITS (0.32–0.42) and in-person human tutoring"),

    # ── V-NICKOW ──────────────────────────────────────────────────────────────
    Rule("V-NICKOW",
         r"(?:Nickow|\b0\.288\b)[\s\S]{0,220}?" + FRONTIER_CLAIM
         + r"|" + FRONTIER_CLAIM + r"[\s\S]{0,220}?(?:Nickow|\b0\.288\b)",
         HUMAN_CLASS + r"|96 (?:randomi[sz]ed|RCT)|preK-12|pre-K|J-PAL|tutoring (?:RCT|trial|studies)",
         "Nickow, Oreopoulos & Quan 2024 (AERJ) pooled 0.288 SD (SE 0.029) across 96 randomised "
         "trials of HUMAN preK-12 tutoring. Zero AI arms. The constituent study years are "
         "unestablished in this corpus. It is not a field-wide number for AI tutoring.",
         "Nickow — the honest field-wide number for what an AI tutor achieves"),

    # ── V-VANLEHN ─────────────────────────────────────────────────────────────
    Rule("V-VANLEHN",
         r"(?:VanLehn|\b0\.79\b|\b0\.76\b)[\s\S]{0,220}?" + FRONTIER_CLAIM
         + r"|" + FRONTIER_CLAIM + r"[\s\S]{0,220}?(?:VanLehn|\b0\.79\b|\b0\.76\b)",
         HUMAN_CLASS + r"|" + ITS_CLASS,
         "VanLehn 2011 reports TWO classes: human tutoring d = 0.79 and rule-based ITS d = 0.76. "
         "The review is 2011; the years of the trials it reviews are unestablished here. Neither "
         "number measured an LLM, and neither is a ceiling for one. Say which arm and which era.",
         "VanLehn measured 0.79, and that is the bar an AI tutor has to clear."),

    # ── V-CEILING ─────────────────────────────────────────────────────────────
    Rule("V-CEILING",
         r"the (?:real )?ceiling[\s\S]{0,120}?(?:VanLehn|Nickow|\b0\.79\b|\b0\.288\b|2\s?σ|two[- ]sigma)"
         r"|(?:VanLehn|Nickow|\b0\.79\b|\b0\.288\b)[\s\S]{0,120}?the (?:real )?ceiling",
         # The cure is that THE CEILING is attributed, not that a class word floats nearby.
         # A chart row reading `label:"Human tutoring", note:"the real ceiling"` contains the
         # words "human tutoring" and still asserts an unqualified ceiling.
         r"ceiling for (?:a |an |the )?(?:human|person|pre-?LLM|rule-based|ITS|adult)|"
         r"(?:human|pre-?LLM|ITS)[- ]tutoring ceiling|ceiling (?:of|on) (?:a )?human|"
         r"not (?:a|the) ceiling for (?:a )?(?:AI|LLM|frontier)|ceiling for what (?:a )?human",
         "Calling a HUMAN or ITS measurement 'the ceiling' on a surface about AI tutoring asserts "
         "that a 2011/2024 measurement of another class of system bounds a frontier one. If it is "
         "a ceiling, say a ceiling for what.",
         "VanLehn's 0.79 is the real ceiling and the best AI tutor sits below it."),

    # ── V-TUTORGYM ────────────────────────────────────────────────────────────
    Rule("V-TUTORGYM",
         r"223[\s\S]{0,160}?(?:chance|tutoring domains)",
         # "the models tested" scopes the claim but does not date it, and the error here is
         # temporal: a 2024 snapshot bounding a 2026 system. The cure must carry the vintage.
         r"four models|initial evaluation|claude-3-5|gpt-4o-2024|deepseek-v2\.5|snapshot|"
         r"(?:August|Aug|October|Oct)[^.]{0,24}2024|2024 (?:vintage|model|snapshot)",
         "TutorGym's 223-domain result is four model snapshots from August-October 2024 "
         "(claude-3-5-sonnet-20241022, claude-3-5-haiku-20241022, gpt-4o-2024-08-06, "
         "deepseek-v2.5), zero-shot, no tool use, in what the authors call an initial evaluation. "
         "A 2024 capability measurement is not a 2026 capability bound. See C-51.",
         "Across 223 real tutoring domains, no model beat chance at labelling an incorrect action."),

    # ── V-PREFERENCE ──────────────────────────────────────────────────────────
    Rule("V-PREFERENCE",
         r"(?:d\s*[≈=]\s*\.?0?\.48|d\s*≈\s*0\.48)[\s\S]{0,160}?knowledge"
         r"|preference[\s\S]{0,120}?(?:d\s*[≈=]\s*0?\.48)",
         r"Buljan|infographic|n\s*=\s*334|three RCTs|Cochrane|adults|immediate quiz",
         "d = 0.48 preference-vs-knowledge is Buljan et al. 2018: three RCTs, n = 334, infographic "
         "vs plain-language Cochrane summary, adults, immediate quiz. Published here as a general "
         "law about learner preference with the scope stripped. See C-52.",
         "Preference moves at d ≈ 0.48 while knowledge does not move at all."),

    # ── V-UNDATED-META ────────────────────────────────────────────────────────
    Rule("V-UNDATED-META",
         r"(?:machine tutoring already matched|already at 0\.76 before|"
         r"ITS (?:already )?(?:matched|equalled|equaled) human)",
         ITS_CLASS + r"|" + HUMAN_CLASS,
         "'Machine tutoring already matched human tutoring' is VanLehn 2011 comparing rule-based "
         "ITS to human tutors. Stated without its class and year it reads as a claim about "
         "current systems.",
         "machine tutoring already matched it, so the AI ceiling is known"),
]


def surfaces(root=ROOT):
    seen = []
    for pat in SURFACES:
        seen += sorted(root.glob(pat))
    return seen


def scan(root):
    out = []
    for f in surfaces(root):
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        for r in RULES:
            for m in r.bad.finditer(text):
                if in_ledger_row(text, m.start()):
                    continue
                if BOUNDARY.search(m.group(0)):
                    continue          # the two halves sit in different sections
                lo, hi = max(0, m.start() - WINDOW), min(len(text), m.end() + WINDOW)
                if not r.cure.search(text[lo:hi]):
                    out.append((str(f.relative_to(root)),
                                text.count("\n", 0, m.start()) + 1,
                                r.vid,
                                re.sub(r"\s+", " ", m.group(0))[:90],
                                r.note))
    return out


def self_test():
    """Plant each rule's known-bad probe in a scratch copy; the rule must fire.
    Also proves the empty-scan guard: a tree with no surfaces must not report OK."""
    failures = []
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td) / "repo"
        shutil.copytree(ROOT, tmp, ignore=shutil.ignore_patterns(".git", "node_modules"))
        target = tmp / "survey" / "_vintage_selftest.md"
        for r in RULES:
            target.write_text("# self-test fixture\n\n" + r.probe + "\n", encoding="utf-8")
            hits = [v for v in scan(tmp) if v[2] == r.vid and "_vintage_selftest" in str(v[0])]
            if not hits:
                failures.append((r.vid, r.probe[:70]))
        target.unlink(missing_ok=True)

        # Empty-scan guard, proven rather than asserted: strip the tree of surfaces
        # and confirm main() over it would fail. C-36 is this exact hole.
        empty = pathlib.Path(td) / "empty"
        empty.mkdir()
        if len(surfaces(empty)) >= MIN_SURFACES:
            failures.append(("EMPTY-GUARD", "an empty tree yielded enough surfaces to pass"))

    if failures:
        print(f"SELF-TEST FAILED — {len(failures)} rule(s) did not fire on their own probe:\n")
        for vid, probe in failures:
            print(f"  [{vid}] did not detect: {probe!r}")
        return 1
    print(f"self-test: OK — all {len(RULES)} rules fire on their planted probe; "
          f"empty-scan guard holds")
    return 0


def main():
    argv = sys.argv[1:]
    rc = 0
    if "--self-test" in argv:
        rc |= self_test()
        if "--strict" not in argv:
            return rc

    n = len(surfaces())
    if n < MIN_SURFACES:
        print(f"vintage check: FAILED — only {n} surfaces found (need {MIN_SURFACES}). "
              f"An empty or truncated scan is not a pass.")
        return 1

    v = scan(ROOT)
    if not v:
        print(f"vintage check: OK — {len(RULES)} rules, {n} published surfaces, "
              f"{len(REAL_IDS)} ledger ids, 0 violations")
        return rc

    src = [x for x in v if x[0] not in GENERATED]
    gen = [x for x in v if x[0] in GENERATED]
    print(f"vintage check: {len(v)} VIOLATION(S) — a legacy number is bounding a frontier "
          f"system\n  {len(src)} in source surfaces, {len(gen)} in the assembled paper "
          f"(which clears on rebuild)\n")

    by_rule = {}
    for path, line, vid, snippet, note in src:
        by_rule.setdefault(vid, {"note": note, "hits": []})["hits"].append((path, line, snippet))

    for r in RULES:                       # stable, declared order
        if r.vid not in by_rule:
            continue
        blk = by_rule[r.vid]
        print(f"  [{r.vid}] {len(blk['hits'])} hit(s)")
        print(f"    rule : {blk['note']}")
        for path, line, snippet in blk["hits"]:
            print(f"      {path}:{line}  {snippet!r}")
        print()

    if gen:
        counts = {}
        for path, _, vid, _, _ in gen:
            counts[(path, vid)] = counts.get((path, vid), 0) + 1
        print("  assembled paper (rebuild after fixing survey/):")
        for (path, vid), n in sorted(counts.items()):
            print(f"      {path}  [{vid}] ×{n}")
        print()

    print("The fix is to DELETE the sentence, not to label the number. Where the claim\n"
          "  needs evidence, use a frontier-era measurement or state that the trial has\n"
          "  not been run.\n  See evidence/VINTAGE.md for the per-claim worklist.")
    return 1


if __name__ == "__main__":
    code = main()
    sys.exit(code if ("--strict" in sys.argv or "--self-test" in sys.argv) else 0)
