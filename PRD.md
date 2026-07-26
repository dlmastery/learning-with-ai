# PRD — *Learning in the New Frontier AI World*

**A standard-setting survey of AI-native learning, plus the reference implementation.**

| | |
|---|---|
| Status | Active — July 2026 frontier reset landed; 26 raw documents + 21 synthesis sections |
| Target | ~100 pages, ~20 sections, 400+ cited sources |
| Repo | `dlmastery/learning-with-ai` (private) |
| Date | 2026-07-25 |

---

## 1. Thesis

Every existing treatment of AI in education asks *"how do we bolt AI onto school?"*
This survey asks the inverted question: **if learning were designed today, with
frontier AI assumed, what would it look like?**

The answer is not merely "a chatbot tutor." It is a multilingual, multimodal,
offline-capable **expert mentor mesh** that knows the learner, creates the right
learning object on demand, routes to specialists, and collaborates with teachers
and families.

The north star is **no child left behind**: a world-class AI mentor for every
learner, including rural and remote communities across Africa, China, India,
Latin America, and everywhere expert attention is scarce.

## 2. Non-goals

- **Not a vendor catalogue.** Product marketing is quoted only when labelled as such.
- **Not an incumbent-defense document.** Industry anxiety is not an evidence
  prior; current capability and measured learning gains are.
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
5. **Frontier-first.** July 2026 primary evidence supersedes inherited narratives
   built around older models or isolated studies.
6. **Constructive rigor.** Include limitations when they change a design,
   deployment, safety, or interpretation decision; do not manufacture a negative
   counterpoint for rhetorical balance.

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

**Retrieval note:** the initial session's WebSearch budget was exhausted.
Continuations check the current allowance, but systematic retrieval remains the
default: arXiv, Semantic Scholar, OpenAlex, Crossref, ERIC and PubMed APIs, plus
targeted primary-source fetches. Unreachable sources are flagged, never guessed.

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
| B2 | AI tutoring efficacy | Which designs now produce measured learning gains, for whom, and at what cost? |

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
| F2 | Beyond one tutor: the expert agent society | How should specialists collaborate around one learner? |
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

### Wave E — The market frontier
| § | Section | Core question |
|---|---|---|
| E1 | **Edtech startup landscape & novelties** | What is actually being built, funded, and shipped right now? |
| E2 | **LessonOrca as primary evidence** | Does Socratic-only tutoring work, measured on real users? |

#### E1 — Edtech landscape

A systematic sweep of what exists in 2026, not a vendor list. Organised by the
*primitive* each company bets on, so the section reads as a taxonomy of design
hypotheses rather than a directory: content generation · tutoring · assessment ·
teacher tooling · language · early literacy · STEM · credentialing · learning
infrastructure. Funding and traction data where available (Crunchbase/press),
labelled `VENDOR` throughout. Incumbent business-model concerns do not set the
research agenda; global learning gain, reach, and cost do.

#### E2 — LessonOrca *(primary evidence, not anchoring)*

Distinct from the portfolio quarantine (§4): the quarantine exists to stop
*design* anchoring. LessonOrca is a **deployed product with instrumented users**,
which makes it an evidence source rather than an inspiration source.

What makes it survey-relevant:

- **Socratic-oriented by construction** — "never gives answers directly." This
  is one production implementation of the teaching-mode router. Compare it with
  worked-example, verification-first, and mixed policies rather than treating
  one interaction style as universal.
- **Persistent learner profiles** across sessions — the F5 model, in the field.
- **Full parent/tutor transparency** into every AI interaction — a concrete answer
  to F8's oversight problem, and a pattern worth generalising.
- **Continuity between sessions** framed as *the* problem — matching F11's claim
  that retention, not comprehension, is where systems fail.

**Original-measurement opportunity.** A PostHog deployment on this product means
the survey can report *measured* behaviour rather than cited literature:
session completion, return rate, question-depth distributions, drop-off points,
and—if instrumented—which teaching modes work best by learner, subject, and
moment. Almost no published work has this product-level routing data.

Constraints: any use must be aggregate-only, no individual learner data, COPPA
posture preserved, and clearly labelled `OBSERVED` (single-product, non-randomised)
rather than `MEASURED-RCT`. Report it as one product's telemetry, not as proof.

### Wave H — Access-first design *(reordered to the front of the design argument)*
| § | Section | Core question |
|---|---|---|
| H1 | **Special education, SELPA, and accessibility-first design** | What if we design for the margin first? |

#### H1 — The inversion

Standard practice builds for the median learner and bolts on accommodations.
This survey argues the opposite order: **build the SELPA-grade system; it serves
everyone.** The formal name is **Universal Design for Learning** (CAST); the
popular name is the curb-cut effect.

The argument is not moral, it is technical. Every core SELPA accommodation is
*also* an established mainstream learning principle:

| SELPA accommodation | Same thing, mainstream literature |
|---|---|
| Multiple representations | Mayer multimedia principles; Ainsworth DeFT |
| Extended time / self-pacing | Self-paced mastery learning |
| Reduced distraction | Coherence principle; extraneous cognitive load |
| Text-to-speech / speech-to-text | Modality principle; decoding-load removal |
| Explicit, systematic instruction | Worked examples; direct instruction evidence |
| Chunking & scaffolds that fade | Segmenting principle; scaffolding + fading |
| Frequent low-stakes checks | Retrieval practice; formative assessment |

Designing for the margin first produces a better system for the centre. That is
the section's thesis and it should govern the reference architecture in G2.

**Evidence spine.** This is the most replication-rich area in education and must
be treated as such: National Reading Panel; structured literacy and
Orton-Gillingham for dyslexia; explicit/direct instruction (Project Follow
Through, Stockard et al. meta-analysis); Response to Intervention / MTSS;
mathematics interventions for dyscalculia; AAC and assistive technology
evidence; executive-function supports for ADHD; autism-spectrum instructional
research. Report effect sizes, and report where the evidence is weak.

**Hard constraints — non-negotiable, stated in the paper:**

1. **An IEP is a legally binding document authored by a team including the
   parent.** Under IDEA an AI may draft, summarise, surface progress data, and
   prepare materials. It may not author, decide eligibility, or replace the team
   process. Any system claiming otherwise is a legal and ethical failure.
2. **This is not a domain for novel unvalidated pedagogy.** Where decades of
   replicated intervention research exist, the AI's job is *fidelity and dosage*
   — delivering known-good intervention at an intensity no staffing ratio can
   afford — not invention.
3. **Diagnosis is out of scope.** Screening signals may be surfaced to
   professionals; the system must never label a child.
4. **Accessibility is a floor, not a feature.** WCAG 2.2 AA minimum, keyboard-
   only operation, screen-reader correctness, captions, no
   colour-only encoding, adjustable motion. A learning system that fails
   accessibility has failed its hardest users first.
5. **Data protection is elevated.** Disability status is sensitive data under
   FERPA/IDEA and GDPR special-category rules. Default to on-device, minimise,
   and never train on it.

**Open question the section must answer honestly:** does AI tutoring actually
help students with disabilities, or has it only been measured on typical
learners? Find the evidence; if it is thin, say so — that gap is itself a
finding, and arguably the most important one in the survey.

#### H1.1 — Learner archetypes the system must actually serve

Not personas for flavour. Each archetype names a **mechanism**, the **design
consequence**, and the **failure mode** if ignored. The system is only credible
if it works for these, not for a median abstraction.

| Archetype | Load-bearing mechanism | Design consequence | Failure mode if ignored |
|---|---|---|---|
| **Attention / ADHD** | Executive function + inhibition (Barkley), not "not trying". Sustained attention collapses long before comprehension does. | Short segments; one idea per screen; ruthless removal of decorative content; immediate feedback; movement and break scheduling; novelty used deliberately. | Long unbroken explanation. The child disengages, and the system reads disengagement as inability. |
| **Working-memory limitation** | WM capacity is the bottleneck; instructions with 3+ held steps fail before reasoning starts. | Externalise memory — visible steps, persistent scaffolds, worked examples, no "remember what we said earlier". Never make the child hold state. | Multi-step verbal instruction. Looks like a reasoning failure; is actually a storage failure. |
| **Long-term retention difficulty** | Encoding and consolidation, not comprehension. The child *understood* it and it decayed. | Scheduled retrieval (F11) is mandatory, not optional; overlearning; re-teach cycles planned from day one. | Teaching once and moving on. The curriculum advances; the child does not. |
| **Reasoning / abstraction gaps** | Abstraction without a concrete anchor has nothing to attach to. | **Explicit instruction over discovery.** Concreteness fading (F10). Never start at the formal level. | Discovery learning. Actively harmful here — this is well replicated. |
| **Processing speed** | Slower does not mean less able; timed tasks measure speed, not knowledge. | Untimed by default; measure mastery, never rate. | Timed drills. Measures the disability, not the learning. |
| **Language / reading access** | Decoding load consumes the capacity needed for meaning. | Text-to-speech, speech-to-text, dual-coded content; decouple *reading* difficulty from *concept* difficulty. | Assessing physics through a reading test. |
| **Anxiety / learned helplessness** | Prior failure history is itself a barrier; errors are threatening. | Low-stakes everything; visible personal growth curve; error framed as information; no public comparison. | High-frequency graded testing. Demoralises exactly the child it was meant to help. |

Archetypes **co-occur** — ADHD with working-memory limits and a history of failure
is the common case, not the edge case. The system must compose accommodations, not
select one.

#### H1.2 — The bidirectional loop *(the core mechanism of this project)*

The system learns the student while the student learns the topic. Both models
update. This is the architectural centre of H1 and G2.

```
  pre-test / grill  →  hypothesis about THIS learner
        ↓
  teach with method M
        ↓
  frequent low-stakes probe   ← CBM: brief, graphed, non-punitive
        ↓
  decision rule fires?  ──no──→  continue M
        │ yes
        ↓
  PIVOT: change method, not volume
        ↓
  update learner model → repeat
```

**1. Grill / pre-test.** Diagnose **prior knowledge and misconceptions**, never
"learning style" (no credible evidence — see §3 of CLAUDE.md). Also establish
*channel* constraints: reading load, WM span, sustained-attention window.

**2. Frequent probing.** Curriculum-Based Measurement: brief, frequent, graphed.
Low-stakes by construction. The growth curve is shown to the **student** as their
own progress (open learner model), never as a verdict.

**3. The pivot rule — the hard part.** Most AI tutors re-explain the same way with
more words. This system must detect non-response and **change approach**:
representation (verbal → visual → manipulative → worked example), granularity,
modality, pacing, or prerequisite level. Formal basis: Data-Based
Individualization decision rules (e.g. four consecutive points below the goal
line ⇒ change instruction). The survey must specify:
- what signal triggers a pivot (accuracy, latency, error *type*, disengagement, self-report);
- how long before pivoting — **too fast is as harmful as too slow**, because method-thrash prevents any method from consolidating;
- what to pivot *to*, and in what order;
- when to stop pivoting and escalate to a human.

**4. Bidirectional model.** The learner model (F5) is a live hypothesis, not a
record. It must be **inspectable and correctable by the student and parent** —
they know things the telemetry cannot see.

#### H1.3 — Where this survey's own advice inverts

Stated explicitly so the paper does not contradict itself:

| General claim (elsewhere in survey) | For this population |
|---|---|
| Productive failure; desirable difficulties | **Explicit instruction wins.** Struggle that is productive for a typical learner is often just failure here. |
| Discovery and exploration | **Guided, worked, faded.** Discovery learning is among the clearest harms. |
| Frequent assessment is good | Only **low-stakes, brief, private, growth-framed**. Frequent high-stakes assessment harms. |
| Reduce scaffolds as expertise grows | Fade **on evidence**, never on schedule; be willing to restore them without treating it as regression. |

A survey that gives one universal answer here is wrong. The correct claim is that
the *mode* must be selected per learner and per moment — which is precisely what
the bidirectional loop is for.

### Wave G — Synthesis
| § | Section |
|---|---|
| G1 | The grounding ladder (L0–L4 correctness standard) |
| G2 | **Reference architecture: the agent village** |
| G3 | Comparative analysis of AI-native book projects |
| G4 | Research agenda |

#### G2 — University-in-a-box / school-in-a-box: the agent village

A single "tutor" agent is the wrong unit. A school is a *society of specialists*:
subject experts, a diagnostician, a curriculum planner, an assessor, a
counsellor, a librarian, a lab technician, a peer, a devil's advocate. The
reference architecture is a **village of role-specialised agents** sharing one
learner model and one evidence store.

Design questions the section must resolve rather than assert:

1. **What does "certified expert agent" mean operationally?** A claim of expertise
   is worthless without a test. Proposal: every agent role carries a published
   eval suite, a grounding tier from G1, and a scope boundary — an agent may only
   assert what its tier permits. "Certified" must mean *passed a stated eval*,
   never *prompted to be an expert* (see B1: persona prompting shows **no**
   measured accuracy gain).
2. **Who arbitrates disagreement?** Multi-agent research in this project found
   majority voting discards correct minority answers ~1 in 4 times, and that
   selection beats synthesis by a wide margin. The village needs an explicit
   arbitration rule, not a consensus vibe.
3. **What must remain human?** Legal authorship (IEPs), safeguarding decisions,
   diagnosis, and relatedness. Name these explicitly.
4. **Single learner model, many agents** — every agent reads and writes one
   learner state (F5), or the village fragments into contradictory tutors.
5. **Cost discipline** — a village is N× the tokens of a tutor. F4's arithmetic
   governs how many agents a learner-hour can afford.

The architecture must satisfy H1 first: if the village does not work for a SELPA
student, it is not the architecture.

## 7. The reference implementation

The survey's conclusions are testable, so they get built: **dynamic per-concept
learning mini-apps** under `apps/`, on agent-native norms — one action definition
driving UI, agent, HTTP, MCP and CLI surfaces, all state in SQL, agent/UI parity.

Each app targets one concept and must demonstrate at least one survey claim
(e.g. verification-first derivation, adversarial grilling, productive failure).

## 8. Acceptance criteria

1. Every section cites ≥15 sources with evidence labels.
2. Every section uses current primary evidence and states decision-relevant
   scope or uncertainty.
3. No `VENDOR` claim appears as a finding.
4. The grounding ladder is concrete enough to implement.
5. At least three working mini-apps demonstrate survey claims.
6. A reader who disagrees can find the evidence and check it.

## 9. Risks

| Risk | Mitigation |
|---|---|
| Anchoring on existing work | Quarantine (§4) |
| Vendor-claim laundering | Mandatory evidence labels |
| Capability hype | Separate vendor claims from measured outcomes; require direct sources |
| Incumbent or historical pessimism | July 2026 frontier-first review and explicit universal-mentor north star |
| Breadth without depth | One agent per section, ≥15 sources each |
| Search budget exhaustion | API-based retrieval; flag unreachable |
| Survey obsolescence | D1 designed as a rolling quarterly section |

---

### F11 reference implementation — ZemoMemo (zemomemo.com)

`VENDOR` unless noted. Flashcard platform built on **FSRS-6**, the current
research-grade spaced-repetition scheduler (`MEASURED-BENCH` — FSRS itself is
validated on Anki-scale review data; ZemoMemo's own outcomes are not published).

Loop: deck creation (manual · import · PDF · AI prompt) → Learn Mode with
confidence rating → **"stickiness score"** (days a card survives in memory) →
sub-5-minute refresh sessions timed just before predicted forgetting → successful
refresh extends the interval.

**Three choices that match the H1 archetypes:**

| Feature | Archetype it serves | Mechanism |
|---|---|---|
| FSRS-6 scheduling | Long-term retention difficulty | Spaced retrieval — best-evidenced retention intervention available |
| Sub-5-minute sessions | Attention / ADHD | Fits inside the attention window rather than fighting it |
| Visible "stickiness score" | Anxiety / learned helplessness | An **open learner model**: growth number owned by the learner, not a verdict |

**The limit, stated in the survey:** flashcards train *recall of discrete items*.
They do not train **transfer or reasoning**. A system leaning only on SRS produces
a learner who remembers everything and cannot apply it. F11 therefore owns the
**retention** half only; the **reasoning** half belongs to F10 (depth laddering)
plus worked examples with faded scaffolds — a different mechanism, different
evidence base.

Also inherits F6's caution: gamified engagement is the least stable cell in the
gamification meta-analyses, with measured novelty decay. Any streak-like
mechanic must pass the **Null-Learner Test** before shipping.

**⚠️ Correction to the F11 note above (added after B1 landed).** Latimier (2020)
finds **expanding intervals confer no advantage: g = 0.034, n.s.** The expansion
curve marketed by SM-2/FSRS/ZemoMemo is *not* the active ingredient. What is
supported: scheduling retrieval at all (classroom d = 0.54; only 12 of 271
massed-vs-spaced comparisons failed) with gaps ≈10–20% of the target retention
interval, falling to 5–10% for year-long retention (Cepeda 2008). Endorse the
practice; do not endorse the schedule shape. `MEASURED-META`
