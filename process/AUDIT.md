# Requirements audit — 2026-07-27

> **⚠️ SUPERSEDED 2026-07-28.** This audit was accurate when written and is now the most
> out-of-date file in the repository — several of its findings have been fixed and it
> understates the survey by ~42,000 words. It is kept unedited as a **record of what was
> true on 27 July**, not as a current status page. For current status see the
> [dashboard](https://dlmastery.github.io/learning-with-ai/); for an adversarial
> assessment see [`evidence/review-2026-07-28.md`](evidence/review-2026-07-28.md).
>
> Resolved since: F11 (zemomemo), C3 (slides + presentations), G1, F9, F7, A3, F4 all
> delivered; survey at 22 sections / ~56,500 words; dashboard rebuilt on a declarative
> chart spec; README rewritten. Still open: the E1-E2 redaction decision, and the demo
> pages still marked *Building*.

Audited against every instruction given since the project began, not against the
plan. The plan is not the requirement; the request is.

**Verdict: the research is in excellent shape and the deliverable is not.**

---

## 0. The finding that matters more than the rest combined

The thing that was asked for is a **~100-page survey**. Here is what exists:

| Artifact | Words | Status |
|---|---|---|
| **`survey/` — the deliverable** | **5,694** | **≈12% of a 100-page target** |
| `research/raw/` — the *input* | 264,786 | 25 reports, excellent |

Ratio: **46 words of research consumed per word of survey produced.**

I have been optimising the input and reporting on the input. Every session has
ended with "N reports landed" — which is a measure of *raw material*, not of the
thing requested. A reader arriving at this repo today finds four essays and a
research library, when they were promised a survey.

**This is the single largest miss and it is a process failure, not a resourcing
one.** Research is easy to parallelise and feels productive; synthesis is neither.
The correction is structural: from here, *no new research agent launches until the
sections that already have reports are written.*

Requirement #4 said build it **incrementally, section by section**. That was
followed for research and abandoned for prose.

---

## 1. Explicitly requested, never delivered

| # | What was asked | Evidence it was asked | State |
|---|---|---|---|
| **1** | **Scientific remembering framework (zemomemo)** | Asked twice; the user corrected my spelling — *"it is zemomemo"* | **F11 never launched.** No report, no section. Requirements #24 and #38 both point here. |
| **2** | **On-the-fly slide generation** | *"on the fly slide generation…"* | **No section owns it.** 7 reports mention slides incidentally; none treats generative slide-making as a technique. |
| **3** | **Students explain / give presentations** | *"having students explain topic to gain deeper understanding, giving presentation"* | **Zero coverage.** F2 covers teaching *the tutor*; presenting *to an audience* is a different mechanism with its own literature and was not researched. |
| **4** | **Dynamic multimodal mini-apps per chapter** | Requirement #5, stated in the original brief | Not started until today. Demo gallery scaffolded this session; 13 demo pages still unbuilt. |
| **5** | **Demos of every technique** | *"you will provide mock realistic demos of each and every technique"* | Gallery shell only. |

---

## 2. Sections with no report at all

| § | Topic | Why it matters |
|---|---|---|
| **G1** | The grounding ladder, synthesised | **Cited by name in already-published prose** — `survey/00-north-star-jarvis.md` says "grounded by verifiable code (G1 ladder)". A dangling reference, public since the repo went open. |
| **F11** | Scientific remembering | See §1. Twice-requested. |
| **A3** | Reactive notebooks (marimo) | Requirement #17, named entity. Partially absorbed into F3 by accident, never owned. |
| **F7** | Embodiment / manipulatives | Bears directly on SELPA — physical materials are one of the three costs AI does *not* collapse (I1). |
| **F9** | Open problems | A standard-setting survey without an open-problems section is not standard-setting. |
| **F4** | Reach economics | **Still partial.** Killed by the session limit; §1–3 only, flagged since. |

---

## 3. Quality and hygiene defects

**3.1 — Unredacted commercial data in a public repo.** `research/raw/E1-E2-*.md`
contains LessonOrca operating figures, including a churn-cost line
(*"$1,600 lost per churned student — ~$200/mo × 8 months avg"*). The repo was made
public on request; this was flagged at the time, git commands were supplied, and
**nothing was done**. It is the user's own company's data, so this is their call —
but it should be a decision, not an oversight.

**3.2 — The dashboard is stale and under-built.** It does not link the demo
gallery, does not reflect 25 reports, and predates roughly ten findings including
five corrections. Its charts are **hand-written SVG, which our own C1 report rates
Tier D** — the correct target is a declarative spec with a deterministic renderer.
We are shipping, on the front page, the thing our research says not to do.

**3.3 — `CLAUDE.md` has drifted from reality.** It states the repo is private (it
is public), lists 11 completed reports (there are 25), and its "priority order for
the next session" is entirely complete. The file exists specifically to survive a
crash; a stale ledger is worse than none.

**3.4 — Tone against the standing instruction.** The user said: *"there are a lot
of AI doomers in edtech. Ignore them. Be bias free. Be positive."* The survey opens
on the felt-learning trap, and the running report style leads with corrections and
nulls. Rigour is not doom — but **structure signals stance**, and leading five
consecutive updates with "here is what we got wrong" reads as a posture even when
each item is individually correct. Findings stay; *ordering* changes. Lead with
what is now possible; carry the guardrail in the same breath.

---

## 4. Delivered and verified

Recorded so the audit is not one-sided. 25 research reports, ~265k words, every
claim evidence-labelled, ≥1 null per section. All 27 named entities investigated
except zemomemo. PRD complete at 30 sections. Repo public, Pages building. Five
substantive self-corrections caught by the research and recorded rather than
silently edited — Sierra Leone's unadjusted estimate, "restraint teaches",
Orton-Gillingham, `d=0.971` (unverifiable; components imply ≈0.93), Bloom's 2σ.
One subagent claim (the Bastani
"correction") independently verified and **rejected**. The evidence discipline is
working; it is the only reason this audit has anything solid to stand on.

---

## 5. The plan

Ordered by what unblocks what. Wave 2 runs in parallel in the background because
research parallelises; **Wave 3 is the priority and does not wait for it.**

### Wave 1 — public correctness *(this session, by hand)*
1. Refresh `CLAUDE.md` to actual state.
2. Rebuild the dashboard: 25 reports, all new findings, link the demo gallery,
   move charts off hand-written SVG.
3. Put the redaction decision in front of the user as a decision.

### Wave 2 — close the research gaps *(parallel agents, background)*
`F11` scientific remembering · `G1` grounding-ladder synthesis · `A3` reactive
notebooks · `F7` embodiment · `F9` open problems · `F4` completion ·
**`C3` generative slides & learner-authored presentations** *(new section — covers
the two requests in §1.2 and §1.3)*

### Wave 3 — **write the survey** *(the deliverable; starts immediately)*
25 reports are already sitting there unwritten. Target ~20 sections at
2,000–2,500 words. **Rule: at least one survey section written per session, every
session, before any other work.** Progress is reported in *survey words*, never in
report count.

### Wave 4 — the demo gallery
13 pages against the shared design system already in `docs/demos/demo.css`.
Computed where computable, honestly labelled where scripted.

---

## 6. The rule this audit adds

> **Report progress in the units of the thing that was asked for.**
>
> Twenty-five reports is not twelve percent of a survey; it is a hundred percent
> of something nobody requested. Research is the input. Prose is the deliverable.
