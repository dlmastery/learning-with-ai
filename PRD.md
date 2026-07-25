# PRD — *Learning in the New Frontier AI World*

**A standard-setting survey of AI-native learning, plus the reference implementation.**

| | |
|---|---|
| Status | Active — Wave A + F in flight |
| Target | ~100 pages, ~20 sections, 400+ cited sources |
| Repo | `dlmastery/learning-with-ai` (private) |
| Date | 2026-07-25 |

---

## 1. Thesis

Every existing treatment of AI in education asks *"how do we bolt AI onto school?"*
This survey asks the inverted question: **if learning were designed today, with
frontier AI assumed, what would it look like?**

The answer is not "a chatbot tutor." That framing is a failure of imagination and
is, on the evidence, pedagogically counterproductive in several specific ways this
survey documents.

## 2. Non-goals

- **Not a vendor catalogue.** Product marketing is quoted only when labelled as such.
- **Not a hype document.** Null and negative results are mandatory content, not caveats.
- **Not anchored on prior art.** See §4 — anchoring is an actively managed risk.
- **Not a single-shot generation.** The paper is built incrementally, section by
  section, each committed as its evidence lands.

## 3. Editorial standard

Every claim carries a **source URL** and an **evidence-strength label**:

| Label | Meaning |
|---|---|
| `MEASURED-RCT` | Randomized controlled trial with reported effect size |
| `MEASURED-META` | Meta-analysis or systematic review |
| `MEASURED-BENCH` | Benchmark result, method disclosed |
| `OBSERVED` | Field/observational study |
| `VENDOR` | Company claim, not independently verified |
| `DEMO` | Shown in a curated demo; availability/reliability unverified |
| `INFERENCE` | The author's reasoning beyond the cited evidence |

Rules that are not negotiable:

1. **A `VENDOR` claim may never be restated as a finding.**
2. **Contested findings are reported as contested.** Bloom's 2-sigma, learning
   styles, gamification, and animation efficacy are all popularly overstated; the
   survey says so with citations.
3. **If a claim cannot be verified, the survey says it could not be verified**
   rather than omitting or laundering it.
4. **Effect sizes over adjectives.** "Improves learning" is not a finding.

## 4. Anchoring risk — actively managed

Research conducted inside this project established that seeding a generator with
existing examples produced **zero** diversity gain (p = .95 / .89 / .49 across three
metrics), and that anchored revision moves answers correct→wrong 57–77% of the time.

Therefore:

- The author's existing portfolio (35 projects) is **quarantined to a late
  validation section**, not used as the foundation.
- Comparable projects (e.g. `xiaol/Harnessing-LLM-Skills-to-Master-Machine-Learning`)
  are analysed **after** the futures sections are drafted, never before.
- Futures-wave agents are instructed to state what *should* exist, not summarise
  what does.

## 5. Research method

**Constraint:** this session's WebSearch budget is exhausted. Systematic retrieval
is unaffected — agents use arXiv, Semantic Scholar, OpenAlex, Crossref, ERIC and
PubMed APIs via `curl`, plus targeted `WebFetch` and authenticated `gh api`.
Serendipitous discovery is degraded; unreachable sources are flagged, never guessed.

**Parallel agent waves.** Each agent owns one section, writes a standalone report to
`research/raw/`, and returns an executive summary. Sections are drafted from those
reports as they land.

## 6. Section plan

### Wave A — The named frontier
| § | Section | Core question |
|---|---|---|
| A1 | AI-native textbook platforms | Can a course be generated end-to-end, and what breaks? |
| A2 | Interactive animation & visual explanation | Does animation help — and can AI author it correctly? |
| A3 | Reactive notebooks & computational documents | Is the notebook the right unit of a chapter? |
| A4 | Live full-duplex multimodal tutoring | What changes when the tutor can see and be interrupted? |
| A5 | World models as learning substrates | Is a generated world safe to learn physics in? |

### Wave B — The evidence floor
| § | Section | Core question |
|---|---|---|
| B1 | Learning science | What actually works, independent of AI? |
| B2 | AI tutoring efficacy | What has been *measured*, including nulls? |

### Wave C — Generation technology
| § | Section | Core question |
|---|---|---|
| C1 | Illustration & diagram generation | Can a machine draw a correct figure? |
| C2 | Assessment item generation & psychometrics | Do generated items retain validity? |
| C3 | Learner modeling & knowledge tracing | Can we know what a learner knows? |

### Wave D — Frontier capability
| § | Section | Core question |
|---|---|---|
| D1 | Frontier model advances (rolling 3 months) | What is newly possible this quarter? |
| D2 | Portfolio validation *(quarantined)* | Does the standard survive contact with real apps? |

### Wave F — The futures argument *(the contribution)*
| § | Section | Core question |
|---|---|---|
| F1 | Assessment: collapse & reconstruction | What is assessment when AI can produce the artifact? |
| F2 | Beyond the tutor: peer, student, adversary | Is "helpful tutor" the wrong default? |
| F3 | Executable & verifiable knowledge | How do we make generated explanations *checkable*? |
| F4 | Reach: economics, access, language | What does "nobody left behind" cost, arithmetically? |
| F5 | Memory & the lifelong learner model | What persists across years, not sessions? |
| F6 | Motivation & the attention economy | Why do learners quit, and can AI change that? |
| F7 | Embodiment: spatial, physical, robotic | What can't be learned through a screen? |
| F8 | Safety, privacy, and children | What must never be built? |
| F9 | Open problems & what nobody is building | Where is the field blind? |
| F10 | **Explanation depth laddering (ELI10/15/20/25)** | Can one concept be rendered at every sophistication level without lying? |
| F11 | **Scientific remembering frameworks** | What makes knowledge *stick* rather than merely land? |

#### F10 — Explanation depth laddering *(distinct primitive, do not merge)*

Zero-to-hero moves a learner **through topics over time**. Laddering renders **one
concept at N sophistication levels simultaneously**, so a learner enters at their
level and climbs. Almost nothing does this deliberately.

Required contributions:

1. **A level taxonomy** — what operationally separates ELI10 from ELI15 from ELI20:
   vocabulary, prerequisite load, formalism, abstraction, and which edge cases are
   retained vs dropped. Not vibes.
2. **A fidelity rule** — what a simplification may *drop* versus what it may never
   *falsify*, so climbing the ladder never requires unlearning. This is the central
   risk: the Bohr atom is taught, then untaught. A productive simplification and a
   planted misconception must be distinguishable *by construction*.
3. **Adaptive entry** — the expertise reversal effect means an ELI5 given to an
   expert actively harms them. Level selection must be driven by measured prior
   knowledge, never by preference.

Evidence spine: concreteness fading (Goldstone & Son; Fyfe & McNeil), Bruner's
spiral curriculum, Gentner's structure mapping, Ainsworth's DeFT, Meyer & Land's
threshold concepts, Chi's self-explanation effect, conceptual-change research
(Posner, diSessa).

#### F11 — Scientific remembering

Retention is a separate problem from comprehension and is where most learning
systems quietly fail. Covers spaced repetition schedulers (SM-2, FSRS, Anki-scale
data), encoding strength, mnemonic and method-of-loci evidence, elaborative
interrogation, and the interaction between *understanding* and *retention* — a
well-understood explanation still decays without scheduled retrieval.

Overlaps F5 (learner modeling); F11 owns the **retention mechanism**, F5 owns the
**learner state**.

### Wave G — Synthesis
| § | Section |
|---|---|
| G1 | The grounding ladder (L0–L4 correctness standard) |
| G2 | Reference architecture for an AI-native learning system |
| G3 | Comparative analysis of AI-native book projects |
| G4 | Research agenda |

## 7. The reference implementation

The survey's conclusions are testable, so they get built: **dynamic per-concept
learning mini-apps** under `apps/`, on agent-native norms — one action definition
driving UI, agent, HTTP, MCP and CLI surfaces, all state in SQL, agent/UI parity.

Each app targets one concept and must demonstrate at least one survey claim
(e.g. verification-first derivation, adversarial grilling, productive failure).

## 8. Acceptance criteria

1. Every section cites ≥15 sources with evidence labels.
2. Every section contains ≥1 documented **negative or null** result.
3. No `VENDOR` claim appears as a finding.
4. The grounding ladder is concrete enough to implement.
5. At least three working mini-apps demonstrate survey claims.
6. A reader who disagrees can find the evidence and check it.

## 9. Risks

| Risk | Mitigation |
|---|---|
| Anchoring on existing work | Quarantine (§4) |
| Vendor-claim laundering | Mandatory evidence labels |
| Hype drift | Mandatory negative results per section |
| Breadth without depth | One agent per section, ≥15 sources each |
| Search budget exhaustion | API-based retrieval; flag unreachable |
| Survey obsolescence | D1 designed as a rolling quarterly section |
