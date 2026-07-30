# CLAUDE.md — project state, requirements ledger, and resume instructions

**Purpose:** this file exists so the project survives a crash, a context reset, or a
new session. Read this first. It is the authoritative record of what was asked.

**Project:** *Learning in the New Frontier AI World* — a ~100-page standard-setting
survey plus a reference implementation.
**Repo:** `dlmastery/learning-with-ai` (**public**) · **Owner:** eranti@gmail.com / `dlmastery`
**Started:** 2026-07-25

---

## 1. Requirements ledger — everything the user asked for, verbatim in intent

Numbered so nothing is silently dropped. `✅` planned/underway · `⏳` queued · `❓` blocked on user.

### The deliverable
| # | Requirement | Status |
|---|---|---|
| 1 | Create GitHub repo `learning-with-ai`, push to it | ✅ done |
| 2 | A **huge survey paper**: "Learning in the New Frontier AI World" | ✅ underway |
| 3 | Target ~**100 pages** | ✅ 27+ sections planned |
| 4 | Build it **INCREMENTALLY — not one-go generation** | ✅ enforced: section per agent, commit per section |
| 5 | **Then** dynamic mini-apps per chapter/section, full multimodal | ⏳ Phase 3 |
| 6 | Voice: elite teacher + elite deep researcher, Karpathy-tier | ✅ editorial standard |
| 7 | Leave no stone unturned | ✅ 27 sections |
| 8 | Appropriate examples + citations throughout | ✅ mandatory evidence labels |
| 9 | Generic across **all fields** | ✅ |
| 10 | Grounded in **learning science + edtech science** | ✅ B1 is the floor |
| 11 | Restate → detailed plan → execute | ✅ done in that order |
| 12 | Detailed **PRD of the research plan** | ✅ `PRD.md` |
| 13 | Update PRD + CLAUDE.md to survive crash | ✅ this file |

### Named entities to investigate
| # | Entity | Section | Status |
|---|---|---|---|
| 14 | paradigm.study | A1 | ✅ |
| 15 | vizuara.ai + their books | A1 | ✅ |
| 16 | Brilliant-style interactive animations | A2 | ✅ |
| 17 | "Morimo" interactive colabs → **marimo** (reactive notebooks) | A3/F3 | ✅ |
| 18 | GPT-Live / Gemini-Live capabilities | A4 | ✅ |
| 19 | World models | A5 | ✅ |
| 20 | **Kimi K3** interactive worlds — VERIFY, do not repeat claims | A5 | ✅ |
| 21 | Wan streamer → live avatar to talk to | A4 | ✅ |
| 22 | Manim animations | A2 | ✅ |
| 23 | Remotion studio | A2 | ✅ |
| 24 | **zemomemo.com** scientific remembering framework | F11 | ✅ **report delivered 2026-07-27** — FSRS-6 SvelteKit app, cites no efficacy datum |
| 25 | **lessonorca.com** — the user's own product | E2 | ✅ primary evidence |
| 26 | Latest **edtech startups, innovations, novelties** | E1 | ✅ |
| 27 | `xiaol/Harnessing-LLM-Skills-to-Master-Machine-Learning` as an example | G3 | ✅ analysed AFTER futures |

### Capabilities to survey
| # | Requirement | Section |
|---|---|---|
| 28 | Video-in / audio-in → video-out / audio-out (full duplex) | A4 |
| 29 | Agent-native / agent-first learning apps | G2 |
| 30 | On-the-fly personalized textbook creation, personalized taste | A1 |
| 31 | **Grilling** to find the learner's best mode of learning | F2 + F5 ⚠️ see §3 |
| 32 | Extreme grounding — formula derivations especially | F3 |
| 33 | Zero-to-hero, gradual progressive complexity | F10 + B1 |
| 34 | Modules → chapters → topics → exercises → quizzes → illustrations → interactive sessions | A1 + C2 |
| 35 | Kids + students learning complex topics, heavily illustrated | C1 + A2 |
| 36 | Next-gen AI that **motivates** learning | F6 |
| 37 | **ELI10 / ELI15 / ELI20 / ELI25** intuition laddering | **F10** |
| 38 | Scientific remembering framework | **F11** |

### Architecture vision (added late, governs G2)
| # | Requirement | Section |
|---|---|---|
| 39 | **University-in-a-box / school-in-a-box**, personalized per student | G2 |
| 40 | **Agent village** — instead of humans, agents | G2 |
| 41 | Each agent **expert, certified, amazing** | G2 ⚠️ "certified" must mean *passed a stated eval*, never *prompted to be an expert* |
| 42 | Works for **SELPA students AND regular students** | H1 |
| 43 | **Helping SELPA is a key goal** | **H1 — design for the margin FIRST** |

### Research sources
| # | Requirement | Status |
|---|---|---|
| 44 | arXiv + industry papers | ✅ via API |
| 45 | Google DeepMind advances, last ~3 months | ✅ D1 (incl. LearnLM) |
| 46 | The user's **AI Studio apps** (35 projects) | ✅ D2, quarantined — see §3 |
| 47 | As many parallel subagents as possible, full agent team | ✅ capped at 20 concurrent |
| 48 | Take the time needed | ✅ |
| 49 | Dissect every piece, plan and attack each | ✅ this ledger |

---

## 2. Editorial standard (non-negotiable)

Evidence labels on every claim: `MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH` ·
`OBSERVED` · `VENDOR` · `DEMO` · `INFERENCE`.

1. A `VENDOR` claim may **never** be restated as a finding.
2. Every section must contain ≥1 documented **negative or null** result.
3. Unverifiable claims are reported as unverifiable, never laundered or omitted.
4. Effect sizes over adjectives.

---

## 3. Standing corrections — decisions that must not be re-litigated

**Anchoring quarantine.** The user's 35-project portfolio is a *late validation*
section (D2), never the foundation. Basis: research in this project measured **zero**
diversity gain from seeding a generator with examples (p = .95/.89/.49) and 57–77%
correct→wrong movement under anchoring. The user explicitly asked not to be limited
by their own "tunnel vision." **LessonOrca (E2) is exempt** — a deployed,
instrumented product is *evidence*, not *inspiration*.

**"Grilling" is redirected.** The user asked for grilling to find "the best mode of
learning for you." Learning-styles matching has **no** credible evidence (Pashler et
al.). Grilling therefore diagnoses **prior knowledge and misconceptions** — which do
predict learning and govern the expertise-reversal effect. Deliver the intent, not
the debunked mechanism.

**SELPA-first, not SELPA-also.** Build the SELPA-grade system; it serves everyone
(Universal Design for Learning / curb-cut effect). Hard limits: an AI may not author
an IEP (IDEA — legally binding, team-authored), may not diagnose or label a child,
must meet the accessibility standard ADA Title II actually incorporates — **WCAG 2.1 AA**, with compliance dates moved to 26 Apr 2027/2028 (91 FR 20902); see C-26, and must treat disability status as sensitive data.
Special education is the most replication-rich area in education — the AI's job there
is *fidelity and dosage of known-good intervention*, not invention.

**Certification means an eval, not a prompt.** Persona prompting shows no measured
accuracy gain (162 personas × 2,410 questions). Every "expert agent" needs a published
eval suite, a grounding tier, and a scope boundary.

---

## 4. Repo layout

```
PRD.md          research plan, editorial standard, 27-section outline
CLAUDE.md       this file — requirements ledger + resume instructions
survey/         the paper, one file per section (written as evidence lands)
evidence/       bibliography.json, claim ledger
research/raw/   verbatim agent reports, one per section — THE SOURCE OF TRUTH
apps/           dynamic per-concept mini-apps (Phase 3)
examples/       worked zero-to-hero artifacts
```

Agents write to `research/raw/<SECTION-ID>-<slug>.md` with YAML frontmatter
(`title`, `wave`, `date_researched`, `sources_count`). Survey sections are drafted
**from** those files; never delete a raw report.

---

## 5. Environment constraints

- **WebSearch budget EXHAUSTED (200/200)** for this session. Agents must use
  `curl` against arXiv / Semantic Scholar / OpenAlex / Crossref / ERIC / PubMed
  APIs, plus `WebFetch` on known URLs and `gh api` (authenticated, 5000/hr).
  Calling WebSearch fails. Unreachable sources are flagged, never guessed.
- **Concurrent subagent cap: 20.** Raise with
  `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS=40` to run remaining waves at full width.
- `gh` authenticated as `dlmastery`; git credential helper configured.

---

## 6. Resume instructions after a crash

1. Read `PRD.md` §6 for the section plan.
2. `ls research/raw/` — every file there is a **completed** section's research.
3. Any section in the PRD without a matching `research/raw/` file needs its agent
   re-launched. Agent prompts follow the pattern in §7 below.
4. Draft `survey/<section>.md` from each completed raw report; commit per section.
5. Never regenerate a raw report that already exists — append or supersede with a
   dated new file instead.

## 7. Agent prompt template

Every research agent gets: the section's core question · the WebSearch-exhausted
constraint and the API alternatives · a demand for evidence labels · a demand for
≥1 negative/null result · an instruction to state what *should* exist rather than
summarise what does (futures waves) · the exact `research/raw/` output path · a
request for a 400–500 word executive summary as the final message.

---

## 8. Status — 2026-07-27

**Read `AUDIT.md` first.** It is the requirements audit and it supersedes the
priority list that used to live here.

### The rule this project now runs on
> **Progress is reported in survey words, never in report count.** Research is the
> input; prose is the deliverable. At least one survey section per session, before
> any other work.

### Current state
- **`survey/` — 9 sections, ~15,000 words** (target ~45,000). This is the deliverable.
- **`research/raw/` — 31 reports, ~280k words.** Input, complete for every planned
  section except the demo-driven ones.
- `docs/` — dashboard (stale; needs 31-report refresh + demo links + charts moved
  off hand-written SVG, which C1 rates Tier D) and `docs/demos/` (gallery shell +
  shared `demo.css`; 13 demo pages unbuilt).

### Sections still to write from reports already in hand
A1 textbooks · A2 animation · A4 live-multimodal · A5 world-models · B1 learning
science · B2 efficacy scoreboard · C1 illustration · C2 psychometrics · D1 frontier
quarter · D2 portfolio · D3 LearnLM · E1/E2 edtech landscape · F1 assessment ·
F2 beyond-the-tutor · F5 learner model · F6 motivation · F8 safety · F9 open
problems · G1 grounding · G2 agent village · G3 comparable artifacts · I1
pedagogical systems · I2 global traditions

### Corrections on the record (never silently re-edit; add to this list)
Sierra Leone unadjusted +0.216 n.s. · "restraint removes harm, does not add
benefit" · Orton-Gillingham g=0.22 n.s. · `d=0.971` unverifiable → ≈0.93 ·
Fyfe 2014 is a systematic review with no pooled ES · Bloom's 2σ retired
(VanLehn 0.79 / **Nickow 0.288** — 0.37 was the superseded 2020 working paper /
**Kestin d≈0.63**, developer-evaluated; "0.63–0.73" spliced two estimands) · **g=0.56 is human
learning-by-teaching, not teachable agents; g=0.43 is peer tutoring's tutor gain** ·
**gap-widening is a property of untargeted delivery, not of technology** · deixis
substrate exists (arXiv:2604.02893) · pāṭha protocol benchmarked and falsified ·
PNAS "correction" to Bastani is an affiliation erratum only — the −17% stands.

### Open decision for the user
`research/raw/E1-E2-*.md` is public and contains LessonOrca operating figures
(churn cost, pricing). Scrub from history or leave — user's call.

---

## 9. Writing rules — earned the hard way, each from a shipped defect

Every rule below exists because the failure happened, was found by an adversarial
reviewer, and is in `CORRECTIONS.md`. They are not style preferences.

### 9.1 Never open with a volume metric

**"38 sections, 88,078 words, built on ~2,100 sources"** was the first line of the
README. It tells a reader nothing except that we would like to be found impressive.
A word count is not a finding.

- No document opens with its own size. Not the README, not the paper masthead, not
  slide one, not a page footer.
- **Never let a generator write counts into a prose surface.** That line was
  *injected* by `build-paper.py` on every rebuild, and it was stale as well as vain
  ("thirteen demos" when there were fourteen). Counts belong on the dashboard, where
  somebody has come looking for status.
- The same applies to correction counts. *"51 corrections, 20 external"* is the same
  flex in a different costume. Say what it means — *a substantial minority were found
  by adversarial reviewers* — and let the ledger carry the number.

### 9.2 A closing line may be used once

Four sections ended on a variant of *"what teaches is not the richness of what the
learner is given…"*. Five demos closed on the identical paragraph. **Reusing an
ending retroactively cheapens every claim of independent convergence in the
document** — which this survey makes often.

Before writing a closing paragraph, grep for its distinctive phrase across `survey/`
and `docs/`. If it exists, write a different one or delete the section's ending.

### 9.3 Rationed constructions

Frequency analysis across the corpus, not a checklist. Counted at the time of writing:

| Construction | Count | Rule |
|---|---|---|
| `X is not Y. It is Z.` | 147 in the first half alone | Once per section, maximum |
| `Two things follow.` / enumerative preamble | 69, of which 38 begin "Two" | Say the things; drop the announcement |
| `the honest ___` | 133 across 39 of 40 reports | Once per document |
| `which is precisely` | 23 | Delete; it announces precision instead of being precise |
| `, and it is [appositive]` | 47 | Halve it |
| Em-dash | 578, ~1.8 per 100 words | 3.5–9× literate non-fiction. Halve it |
| Bold | one span per 48 words | **Cut 60%.** Emphasis every 40 words signals nothing |

The standard slop lexicon (`delve`, `tapestry`, `realm`, `myriad`, `crucial`,
metaphorical `navigate`) scores **zero** across the corpus. The tics are one layer
down, which is why frequency analysis is the tool and a banned-word list is not.

### 9.4 A template becomes visible at about ten uses

`## What this section commits us to` closes 14 of 19 sections. Fourteen demo
orientation panels run the identical *imperative → "Then" → "watch"* rhythm; 14 of 14
"What this is" panels are verbless noun phrases.

When generating N instances from one brief, **vary the shape deliberately** or expect
a reviewer to count it. The generator that produced them is in the repo, so the brief
is not merely visible — it is committed.

### 9.5 Verify the sentence a correction lands in

An in-place correction to §15 deleted the subject of a live sentence and left an
unmatched `**`, producing unread text — **in the section whose argument is that we
correct in public within a day.** After any in-place edit, read the whole paragraph
back, not the diff.

### 9.6 Never claim independence between two of our own workstreams

The thesis said *"when a gap is visible independently from both directions, it is
usually real."* Both directions were workstreams of this project. That is the same
team reaching one conclusion twice, which is weaker evidence, and a document selling
its corrections ledger cannot afford the elision.

### 9.7 Renumbering is a build step, never a regex

Repeated `sed`-style bumps left the thesis with two sections numbered 9, no section 8,
and three cross-references pointing at unrelated content. **A reference that resolves
to a real but wrong section is worse than a dead one, because nothing flags it.**
Numbering and cross-references are generated from one declarative outline, and the
builder reports orphans.

### 9.8 Cite an effect size with its estimand

`d ≈ 0.48` (preference) and `g = 0.48` (teaching expectancy) appeared on one page,
undisambiguated. Two unrelated results, one number. Always name what the effect is
*of*.

### 9.9 If nothing counts a mannerism, it is invisible

Every rule from 9.1 to 9.4 was written after a reviewer counted something: 578
em-dashes, 147 `X, not Y` antitheses, 1,013 bold spans (one every 48 words), 35
sections closing on one header, 14 ending on one rhetorical move. **None of it was
visible while writing.** Prose habits are not caught by reading, because reading is
what installed them.

`evidence/check-voice.py` counts them now: a per-file rate per 1,000 words against a
budget, plus corpus shapes (one header, or one closing move, across more than four
files), plus maximal verbatim runs of 14+ words repeated between reader-facing
surfaces. Budgets sit at half the measured rate with a floor of three occurrences, so
a deliberate use passes and a habit fails.

The general form: **any editorial rule that is not executable will be violated, and
the violation will be invisible to the person who wrote the rule.**

### 9.10 A check advertised as runnable must be run

`README.md` listed `node evidence/test-demos.mjs` as one of three checks that "guard
the repository." It could not run at all — it imported playwright with no fallback,
hard-coded an absolute path from one machine, tested a single colour scheme, and
**exited zero on failure**, so nothing downstream would have noticed either.

Meanwhile three published demo pages scrolled horizontally on a phone and one emitted
`<rect x="NaN">`. The check that would have caught all four was in the repository, in
the README, and broken.

Before citing a check as evidence of rigour, run it, break it on purpose, and confirm
it fails. A check that cannot fail is decoration, and it is worse than no check
because it is load-bearing in the argument.

### 9.11 A shared component encodes an assumption about its content

`.chip` was specified for single tokens (`MEASURED-RCT`) and carried `white-space:
nowrap`, which was right for those. Later pages put a sentence of provenance in one,
and three of them overflowed the viewport at 390px. `table` carried `min-width:520px`
for tables inside a scroll box, and a table outside one widened the whole page.

Both were correct rules whose precondition stopped holding when new content arrived.
**When a component is reused by generated pages, the constraint has to live with the
box that owns the overflow**, not with the assumption that the content stays small.

### 9.12 A generator whose output has been hand-edited is a landmine

`evidence/gen-demo-orientation.py` wrote the orientation block on every demo page
and was safely re-runnable, because it replaced its own block rather than stacking.
Then the blocks were rewritten by hand — twice — to break a shared rhythm and to
meet the voice budgets.

Re-running it would have reverted all of that on every page at once, **and no test
would have failed**, because the output is valid HTML that renders, passes every
render check, and links correctly. The only signal would have been prose quietly
getting worse.

Either the generator is the source of truth and nobody edits its output, or the
output is the source of truth and the generator is retired. Holding both is the
failure. This one is retired behind a guard that refuses to run and says why.

The same test applies to `.gen-gallery.py` and `evidence/build-paper.py`: both are
live generators, and their outputs — the gallery cards, `PAPER.md`, `docs/paper.html`
— must never be hand-edited. Edit the data list or the section file instead.
