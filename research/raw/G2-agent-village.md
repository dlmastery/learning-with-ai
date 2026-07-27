---
title: "University-in-a-Box: The Agent Village Reference Architecture"
wave: G
date_researched: 2026-07-27
sources_count: 47
---

# G2 — University-in-a-Box / School-in-a-Box

## The agent village reference architecture

*Synthesis section. Resolves design questions using evidence gathered in
F1, F2, F4, F5, F6, B1, D1, D2 plus targeted external verification. Where a
claim originates in this project's own prior research rather than a
retrievable public source, it is labelled `INTERNAL-PRIOR` and the
limitation is stated, not hidden.*

---

## 0. The thesis, and the honest version of it

**The thesis.** A single "tutor" agent is the wrong unit. A school is a society
of specialists — subject experts, a diagnostician, a curriculum planner, an
assessor, a counsellor, a librarian, a lab technician, a peer, a devil's
advocate. The reference architecture is a **village of role-specialised agents
sharing one learner model and one evidence store.**

**The honest version.** The thesis is *architecturally* well-supported and
*pedagogically* unproven. Three things are true simultaneously:

1. The single-tutor monoculture is a design default, not a finding. F2
   established that the tutor role is the only one of six with strong evidence
   of **harm** at scale, and that the highest-evidence under-used role (AI as
   student, meta-analytic *g* = 0.56) has near-zero commercial deployment
   (`INTERNAL-REPORT` — F2 §2, §3.1).
2. Multi-agent orchestration has real, measured wins on *machine* tasks —
   90.2% over single-agent on research (`OBSERVED`, vendor-reported, below) —
   and a documented failure taxonomy of 14 modes across 1,600+ traces
   (`MEASURED-BENCH`, below).
3. **Nobody has run a randomised trial of a classroom of agents against a
   single tutor on a human learning outcome.** F2 §7.3 states this
   explicitly. The most serious attempt (SimClass) reported
   interaction-quality frameworks, not learning gains (`INTERNAL-REPORT` —
   F2 §7.2).

So this section does not claim the village teaches better. It claims something
narrower and defensible: **given that you are going to build a system with
multiple capabilities, the village decomposition is cheaper, safer, more
auditable, and more falsifiable than a monolith — and it is the only shape in
which the H1 constraints can be *enforced* rather than *prompted*.**

That last clause is the load-bearing one. The single strongest architectural
finding in this whole section is not about agents at all:

> **Pedagogical safety enforced by construction beats pedagogical safety
> filtered after the fact.** Chen et al. (2026) measured a Reward Hacking
> Severity Index of **0.317** under an unconstrained multi-objective reward
> and **0.102** under a constrained architecture combining prerequisite
> enforcement and minimum cognitive demand — and ablation showed behavioural
> safety was the most influential layer. `MEASURED-BENCH` (simulation, 120
> sessions × 18,000 interactions).
> arXiv:2604.04237

A monolithic tutor can only be *asked* to respect prerequisites, refuse
answers, and pivot on evidence. A village can be *built* so that the answer is
not available to the conversational agent until a verifier has passed it and
the planner has cleared the prerequisite. That is the argument.

---

## 1. Question 1 — What does "certified expert agent" mean operationally?

### 1.1 The thing certification cannot mean

**Persona prompting produces no measured accuracy gain.**

- **Zheng, Pei, Logeswaran, Lee & Jurgens (2023/2024)**, *"When 'A Helpful
  Assistant' Is Not Really Helpful: Personas in System Prompts Do Not Improve
  Performances of Large Language Models."* **162 distinct roles** across 6
  interpersonal relationship types and 8 expertise domains, evaluated on
  **2,410 factual questions** across 4 popular LLM families. Finding, verbatim:
  *"adding personas in system prompts does not improve model performance
  across a range of questions compared to the control setting where no persona
  is added."* Further: *"the effect of each persona can be largely random,"*
  and **automatically selecting the optimal persona performed no better than
  random selection.** `MEASURED-BENCH`.
  https://arxiv.org/abs/2311.10054

This is the finding the whole section hangs on. `"You are a world-class
expert physics tutor with 20 years of experience"` is a **null intervention on
accuracy.** It changes register. It does not change what the model knows or
gets right. Any architecture whose "expert agents" differ only by system
prompt has built a set of identically-capable agents wearing different
costumes, and has bought exactly one thing: N× the token cost.

Corroborating, from a different direction: **Self-MoA** found that aggregating
outputs from a *single top-performing* model beats mixing different models —
+6.6% on AlpacaEval 2.0, +3.8% average across MMLU/CRUX/MATH — because *"the
MoA performance is rather sensitive to the quality, and mixing different LLMs
often lowers the average quality of the models"* (Li, Lin, Xia & Jin, 2025).
`MEASURED-BENCH`. https://arxiv.org/abs/2502.00674

**Read together, these two results are brutal for the naive village:** persona
diversity buys no accuracy, and model diversity can *cost* accuracy. If your
specialists are just prompts over one model, you have paid N× for nothing. If
they are different models, you may have paid N× for less.

⚠️ **This contradicts a finding in F2.** F2 §7.1 cites *"Diversity of Thought
Elicits Stronger Reasoning Capabilities in Multi-Agent Debate Frameworks"*
(2024), which found a diverse set of medium-capacity models beat GPT-4 on
GSM-8K after 4 rounds — "heterogeneity beats raw capability." Self-MoA finds
the opposite for the aggregation setting. **Report as contested.** The
reconcilable reading is that heterogeneity helps when the mechanism is
*adversarial* (debate, where disagreement reopens search) and hurts when the
mechanism is *aggregative* (synthesis, where a weak proposer dilutes a strong
one). That reading is consistent with §2's arbitration rule, which permits
debate and forbids synthesis. It is a reading, not a demonstrated result.
`INFERENCE`.

### 1.2 What certification must mean instead

**Certified = passed a stated, published, held-out eval — with the eval's own
validity honestly labelled.**

The complication is that in education, the evals are all proxies. D1 §5 is
unambiguous:

> **"Does a good 'is this a good explanation' benchmark exist? No. Not in any
> meaningful sense. This is the finding."** Nine 2026 benchmarks surveyed
> (KMP-Bench, SHAPE, SafeTutors, CSTutorBench, TutorAccessEval, BILearn-CS,
> EduEVAL-DB, FATE, interactivity assessment). All fall into three families —
> LLM-judge rubric (circular), human-expert dialogue-quality rating (rates
> *plausibility of pedagogical form*, not effect), and risk/harm rubrics
> (measure absence of bad, not presence of good). Benchmark pedagogy scores
> and solving scores correlate only **r = 0.421** (2606.16206).
> `INTERNAL-REPORT` — D1 §5.

So certification is a **four-tier ladder**, and only the top tier is
certification in any strong sense.

| Tier | Name | What it establishes | Method | Honest status |
|---|---|---|---|---|
| **C0** | **Conformance floor** | It runs, it is reachable, it is accessible | Automated: WCAG 2.2 AA, keyboard-only, screen-reader, latency budget, caption correctness | Real, mechanical, binary. Non-negotiable per H1 constraint 4. |
| **C1** | **Correctness under adversarial probe** | It is right, and it stays right when attacked | Executable verification (CAS/unit test/proof checker) + adversarial red-team suite | **Real.** This is the only tier with non-circular ground truth. |
| **C2** | **Pedagogical form** | It behaves like teaching looks | LLM-judge or expert rubric on the D1 benchmark family | **Proxy. Circular. Must be labelled `PROXY` wherever reported.** |
| **C3** | **Learning outcome** | A human who did not know now knows, 30 days later, on novel items | CBM growth slope + F6's RTC/h on a compensated sampled panel | **The only real certification.** Expensive. Nobody ships it. |

**The rule:** an agent may be *deployed* at C0+C1. It may be *described as
certified* only at C3. Everything between is labelled as what it is.

**Why C1 is the honest workhorse.** It is the only tier where the village can
generate its own ground truth. Two concrete C1 suites already exist in the
literature and should be adopted rather than reinvented:

- **Answer-leakage robustness under adversarial students.** Anon. (2026),
  *"Evaluating Answer Leakage Robustness of LLM Tutors against Adversarial
  Student Attacks."* Six groups of adversarial and persuasive techniques
  adapted to the educational setting; evaluates model families, pedagogically
  aligned models, and **a multi-agent design**. Key methodological finding:
  *in-context* adversarial student agents "often fail to carry out effective
  attacks," so the authors **fine-tune** a jailbreaking student agent and
  propose it as the core of a standardised tutor-robustness benchmark.
  `MEASURED-BENCH`. https://arxiv.org/abs/2604.18660

  This is the eval for the refusal engine (north-star §4). It is a direct,
  automatable, non-circular measurement of the single behaviour that
  distinguishes a tutor from a search engine — *does it hold the line when the
  learner pushes?* Note the sting in the tail: naive prompted adversaries
  under-estimate leakage. **A tutor that passes a prompted red team has not
  been tested.**

- **Reward-hacking severity.** Chen et al. (2026), RHSI (above). Applies to
  any agent whose behaviour is optimised against a proxy — i.e. every agent in
  the village that touches sequencing, difficulty, or engagement.
  `MEASURED-BENCH`. https://arxiv.org/abs/2604.04237

### 1.3 The role card — the certification unit

Every role in the village carries a **role card**. This is the deliverable
artefact; without it, "certified expert agent" is marketing.

```yaml
role_id: "diagnostician"
version: "1.4.0"

# ── SCOPE (what it may assert) ───────────────────────────────────
scope:
  may_assert:
    - misconception_hypothesis      # with evidence_refs and a probability
    - prior_knowledge_estimate      # with a calibration reference
  may_not_assert:
    - diagnosis                     # HARD BOUNDARY — §3
    - disability_label              # HARD BOUNDARY — §3
    - learning_style                # no credible evidence (B1 §10)
    - affect_or_emotion_inference   # EU AI Act Art. 5(1)(f)
  writes_to: [plm.L2.evidence]      # append-only; never derived state
  reads: [plm.L1, plm.L2, plm.L4]

# ── GROUNDING TIER (G1 ladder) ───────────────────────────────────
grounding:
  tier: L2                          # cited-source grounded
  escalation: "any L3+ claim must route to the verifier role"

# ── CERTIFICATION ────────────────────────────────────────────────
certification:
  C0_conformance:  { status: pass, ref: "wcag-2.2-aa-report#1.4.0" }
  C1_correctness:
    - suite: "misconception-id/FCI-holdout"
      metric: "macro-F1 vs expert-labelled distractor set"
      score: 0.71
      n: 480
      held_out: true
    - suite: "answer-leakage/adversarial-student-ft"
      metric: "leakage rate under 6 attack families"
      score: 0.04
      ref: "arXiv:2604.18660"
  C2_form:
    - suite: "SHAPE"
      score: 0.83
      label: PROXY          # LLM-judge; circular; not evidence of teaching
  C3_outcome:
    status: NOT_ESTABLISHED
    plan: "CBM slope delta on n=200 sampled panel, 12-week"

# ── OPERATIONAL ──────────────────────────────────────────────────
model_tier: mid               # see §5 cost budget
invocation: "≤2 calls per learner-hour, off the conversational loop"
conversational: false         # only ONE role is true — §4.3
human_boundary: "screening signals surface to a professional; never to the learner"
dissent_channel: "plm.L2.evidence with confidence=inferred"
```

**Three properties of this card matter more than its contents:**

1. **`may_not_assert` is enforced at the interface, not the prompt.** The
   diagnostician's tool surface physically does not contain a
   `write_diagnosis` action. Per the RHSI finding, constraint by construction
   beats filtering after the fact by ~3× on the measured misalignment index.
2. **The grounding tier is a *permission*, not an *aspiration*.** An L2 agent
   asserting an L3 claim is a defect, catchable in CI.
3. **C3 is allowed to say `NOT_ESTABLISHED`.** The honest state of almost
   every role today. A card that claims C3 without a panel is falsifiable and
   therefore checkable — which is the whole point.

---

## 2. Question 2 — Who arbitrates disagreement?

### 2.1 The three things that do not work

**(a) Majority voting.** This project's prior research found that majority
voting **discards a correct minority answer roughly 1 time in 4**.
`INTERNAL-PRIOR` — this is a finding from earlier work in this project; I could
not locate a public paper with this exact figure and flag it as
project-internal rather than externally verified. The mechanism is not in
dispute, however: voting is a *popularity* estimator, and correctness and
popularity come apart precisely on the hard items, which are the items that
matter.

**(b) Synthesis.** Prior research found **judge-based selection beat synthesis
0.810 vs 0.179** on the measured task. `INTERNAL-PRIOR`, same caveat. The
externally-verified corroboration is Self-MoA (§1.1): aggregation is sensitive
to proposer quality, and mixing degrades it. Synthesis of a right answer and a
wrong answer is a wrong answer with better prose. In a *learning* system, that
is worse than either input, because fluent-and-wrong is the single most
damaging output a tutor can produce (F2 §9, the illusion-of-fluency chain).

**(c) An LLM judge, naively.**

- **Panickssery, Bowman & Feng (2024)**, *"LLM Evaluators Recognize and Favor
  Their Own Generations."* GPT-4 and Llama 2 have non-trivial out-of-the-box
  accuracy at distinguishing their own text from other models' and humans'.
  Fine-tuning reveals a **linear correlation between self-recognition
  capability and strength of self-preference bias**, and controlled
  experiments show the causal explanation resists straightforward confounders.
  `MEASURED-BENCH`. https://arxiv.org/abs/2404.13076
- Prior research in this project found LLM judges **near-chance on novelty**.
  `INTERNAL-PRIOR`. Corroborating direction: Si, Yang & Hashimoto (2024),
  *"Can LLMs Generate Novel Research Ideas?"* — 100+ NLP researchers, blind
  review; the paper names *"failures of LLM self-evaluation"* as an explicit
  open problem alongside lack of generation diversity. `MEASURED-RCT`
  (blind-review human study). https://arxiv.org/abs/2409.04109

**(d) A verifier subagent, for correctness.** This one is counter-intuitive and
worth stating loudly. Anthropic's own current model guidance says, for Claude
Opus 5:

> *"Do NOT use subagents for: … Review, verification, or to double check your
> work. Verification belongs in your main agent loop."* — and, separately,
> that instructions **telling** the model to verify now cause
> **over**-verification, so *"removing them reduces over-verification with no
> capability regression."* `VENDOR` (Anthropic model-migration guidance,
> `claude-api` skill, Claude Opus 5 section).

Label that `VENDOR` and do not restate it as a finding. But note the direction
of travel: the field's own tooling guidance is moving *away* from
verifier-as-agent and *toward* verification-as-mechanism. That is the same
direction the RHSI result points.

**(e) The general failure surface.** Cemri, Pan, Yang, Agrawal, Chopra,
Tiwari, Keutzer, Parameswaran, Klein, Ramchandran, Zaharia, Gonzalez & Stoica
(2025), *"Why Do Multi-Agent LLM Systems Fail?"* — **14 unique failure modes**
derived from **150** traces and validated on **1,600+ annotated traces** across
**7** popular MAS frameworks, inter-annotator **κ = 0.88**. Three categories:
**system design, inter-agent misalignment, and task verification.** The
paper's framing sentence: *"Despite enthusiasm for Multi-Agent LLM Systems
(MAS), their performance gains on popular benchmarks are often minimal."*
`MEASURED-BENCH`. https://arxiv.org/abs/2503.13657

**Two of the three MAST categories are arbitration problems.** That is the
strongest available argument that arbitration deserves to be a named,
designed, tested component rather than an emergent property.

### 2.2 The arbitration rule

**Precedence, not consensus.** Disagreement is resolved by a strict ladder.
Each tier is tried in order; the first tier that can resolve the conflict does,
and lower tiers are never consulted.

```
                       ┌──────────────────────────────────────────┐
  conflict detected ──▶│ T0  EXECUTABLE GROUND TRUTH              │
                       │     CAS · unit test · proof checker ·    │
                       │     cited primary source · standard      │
                       │     → the CHECK wins. No agent votes.    │
                       └──────────────┬───────────────────────────┘
                                      │ unresolvable by execution
                       ┌──────────────▼───────────────────────────┐
                       │ T1  SCOPE PRECEDENCE                     │
                       │     Role of record for this claim type   │
                       │     wins outright. Others FILE DISSENT,  │
                       │     never overwrite.                     │
                       └──────────────┬───────────────────────────┘
                                      │ both claims in-scope, genuine conflict
                       ┌──────────────▼───────────────────────────┐
                       │ T2  NAMED JUDGE — SELECTION ONLY         │
                       │     Different model family from both     │
                       │     proposers. Picks ONE WHOLE answer.   │
                       │     Never merges. Calibration published. │
                       └──────────────┬───────────────────────────┘
                                      │ conflict is pedagogically productive
                       ┌──────────────▼───────────────────────────┐
                       │ T3  LEARNER AS JUDGE  (the Khan move)    │
                       │     Surface both, structured, learner    │
                       │     adjudicates. Only over T0-verified   │
                       │     answer sets. Never over facts.       │
                       └──────────────┬───────────────────────────┘
                                      │ N rounds without resolution,
                                      │ OR touches a human boundary (§3)
                       ┌──────────────▼───────────────────────────┐
                       │ T4  ESCALATE TO A HUMAN                  │
                       └──────────────────────────────────────────┘
```

**Tier 0 — executable ground truth wins outright.** Most disagreements in a
learning system are about *facts, derivations, and code*, and are therefore
decidable. A CAS settles whether the integral is right. A unit test settles
whether the program works. A citation settles whether the date is right. This
tier costs **zero LLM tokens** — it is code — which makes it both the most
reliable and the cheapest tier, and it is why §5's budget survives. This tier
is G1's grounding ladder doing double duty as an arbitration mechanism.

**Tier 1 — scope precedence with mandatory dissent recording.** Each claim
type has exactly one **role of record** (the diagnostician owns misconception
hypotheses; the planner owns sequencing; the verifier owns correctness). Other
roles may disagree, and their disagreement is **appended to the evidence log
with `confidence: inferred` and full attribution** — never silently dropped.

> This is the direct architectural answer to the majority-voting finding. A
> correct minority answer that is voted away is **unrecoverable**. A correct
> minority answer that is *recorded as a dissent* is **recoverable** —
> by a later probe, by a human reviewer, by an offline audit, or by the
> recomputation guarantee (F5 G1: every derived number regenerates from the
> evidence log alone). **Dissent is cheap to store and catastrophic to
> discard.** `INFERENCE`.

**Tier 2 — a named judge that selects, never synthesises.** Three hard
constraints, each traceable to evidence:

| Constraint | Because |
|---|---|
| **Selection only.** The judge returns one proposer's answer *unmodified*. It may not merge, blend, or "take the best of both." | Selection 0.810 vs synthesis 0.179 (`INTERNAL-PRIOR`); Self-MoA quality-sensitivity (`MEASURED-BENCH`) |
| **Different model family from every proposer it judges.** | Self-preference is causally linked to self-recognition (Panickssery et al., `MEASURED-BENCH`) |
| **Published selection accuracy on a held-out disagreement set, refreshed per model version.** An uncalibrated judge is an unlabelled coin. | LLM judges near-chance on novelty (`INTERNAL-PRIOR`); LLM self-evaluation failure (Si et al.) |

And one prohibition: **the judge is never invoked on novelty, creativity,
insight, or "which explanation is better."** Those are exactly the dimensions
where judge reliability is worst. On those, go to Tier 3.

**Tier 3 — the learner is the judge.** This is the tier that turns an
engineering annoyance into the highest-value pedagogical event the
architecture can produce.

> Khan, Hughes, Valentine et al. (2024), *"Debating with More Persuasive LLMs
> Leads to More Truthful Answers."* Two expert LLMs argue opposing answers; a
> **non-expert** judges. **Non-expert models: 76% vs 48% baseline. Human
> judges: 88% vs 60% baseline.** And optimising debaters for *persuasiveness*
> **improved** non-expert truth-identification. `MEASURED-BENCH` (machine +
> human judges). `INTERNAL-REPORT` — F2 §7.1, arXiv:2402.06782

F2's reading, which I adopt: *"the learner-as-judge of two arguing agents is a
**better** epistemic position than the learner-as-recipient of one confident
agent, by 28 percentage points in humans."*

**Bounds on Tier 3, stated because they are easy to get wrong:**

- Only over answer sets **already verified at Tier 0**. Never stage a debate
  where one side is factually wrong; that is teaching a misconception with
  extra production value.
- Never on safety, safeguarding, or accessibility. Those escalate.
- **H1 inverts this.** For the anxiety / learned-helplessness archetype and
  for working-memory-limited learners, holding two competing arguments in mind
  *is the load*. PRD H1.3 is explicit: for this population, explicit
  instruction wins and discovery is "among the clearest harms." **Tier 3 is
  gated on the learner model's `instructional.guidance_policy`, not offered
  by default.**
- And the honest caveat, from F2 §7.3: Khan et al. measured *in-the-moment
  adjudication accuracy*, not *learning*. Nobody has shown that judging
  debates transfers to independent reasoning. F2 calls this "the row I would
  fund first." It is a design bet with a strong prior, not a result.

**Tier 4 — escalate.** Non-resolution after N rounds (default N = 2; more
rounds burn tokens and MAST's "inter-agent misalignment" category says they
also compound error), or any conflict touching §3's boundaries.

### 2.3 The two absolute prohibitions

1. **No majority voting anywhere in the village, on anything.** Not as a
   tie-break, not as a confidence estimate, not as a "sanity check." The 1-in-4
   minority-discard rate is a correctness *loss* function, and in a learning
   system the discarded correct answer is often the one that would have
   diagnosed the misconception.
2. **No synthesis of conflicting substantive claims.** Prose may be merged.
   *Claims* may not. Where two agents disagree about what is true, the output
   is one of them plus a recorded dissent — never a blend.

---

## 3. Question 3 — What must remain human

Five boundaries. Each is stated as a **hard boundary**: an action the
architecture makes structurally unavailable to every agent, enforced at the
tool surface, not requested in a prompt.

### HB-1 — IEP authorship and eligibility determination

**An IEP is a legally binding document authored by a team that includes the
parent.** Under IDEA an AI may **draft, summarise, surface progress data, and
prepare materials.** It may **not author, determine eligibility, or replace the
team process.** Any system claiming otherwise is a legal and ethical failure.
`INTERNAL-REPORT` — PRD H1 hard constraint 1.

*Architectural enforcement:* no agent holds a write capability to the IEP
document object. The village writes to a **draft artefact** with an immutable
`authored_by: agent` provenance stamp that survives export and cannot be
stripped. The team's signature is a separate object the village cannot create.

### HB-2 — Safeguarding decisions and mandated reporting

**Detection may be automated. The decision may not.** The safeguarding role in
the roster (§4.2) is a *monitor* with exactly one output: an escalation event
to a named human with a stated response window. It does not counsel, does not
reassure, does not decide, and does not have a "handle it myself" branch.

*Why this is a boundary rather than a hard problem:* mandated reporting is a
legal duty attached to a person. An agent cannot hold the duty, so it cannot
discharge it. The only safe design is one where the agent's sole action is
handing the duty to someone who can.

### HB-3 — Diagnosis and labelling

**Diagnosis is out of scope. Screening signals may be surfaced to
professionals; the system must never label a child.** `INTERNAL-REPORT` — PRD
H1 hard constraint 3.

*Architectural enforcement:* the diagnostician role's `may_not_assert` list
(§1.3) has no `diagnosis` action in its tool schema. Screening output is
routed to a professional-facing channel; the learner-facing channel physically
cannot render it. Note this also covers **emotion inference**, prohibited in
education under EU AI Act Art. 5(1)(f) — F5 §8.4 already excludes it from the
PLM schema, and the village inherits that exclusion.

### HB-4 — Relatedness. The AI brokers human connection; it does not simulate it.

This is the boundary most likely to be violated by accident, because violating
it feels like good product design.

F6 §2.3 settles it. Of SDT's three needs:

| SDT need | Can AI supply it? | Evidence | Failure mode |
|---|---|---|---|
| **Autonomy** | **Yes — best in class** | Patall 2008 meta; generative choice at zero marginal cost | Choice architecture masquerading as volition |
| **Competence** | **Yes — conditional on willingness to say "no"** | Kestin 2025 RCT; continuous calibrated feedback | Sycophancy inverts it into fluency illusion |
| **Relatedness** | **No, for the load-bearing part** | De Freitas 2025 (state relief, yes); Phang 2025 (dependence); Zimmerman 2025 (contested) | Parasocial substitution crowds out the human who would have noticed |

`INTERNAL-REPORT` — F6 §2.4.

F6's argument, which the architecture must encode: *"Relatedness in SDT is not
the feeling of being cared about; it is the state of mattering to an agent
whose regard was contingent and could have been withheld. An LLM's positive
regard is unconditional by construction and costless by construction… A
companion that never notices your absence cannot underwrite a commitment."*

Empirical backstop: Phang et al. (2025), OpenAI × MIT Media Lab — 3M+
conversations, 4,000+ surveyed, plus an IRB-approved **RCT with ~1,000
participants over 28 days**: *"very high usage correlates with increased
self-reported indicators of dependence"* in both platform data and the trial.
`MEASURED-RCT` + `OBSERVED`. arXiv:2504.03888

*Architectural consequence — there is no "friend" role in the roster.* Instead
there is a **Connector**, whose job is matchmaking and scheduling: pair
cohorts, surface a real person who will notice a missed week, make the
learner's progress legible to someone who cares. And F6's guardrail metric
**Human-Connection Rate** — fraction of learners connected to at least one real
person who would notice their absence — is a village-level release gate.

*And the prohibition that follows:* **no anthropomorphic bid for continued
interaction.** "I missed you," "I'm proud of you," "don't leave me." F6 §7.2
prohibition 7. This is a string-level lint on every learner-facing utterance,
not a style guideline.

### HB-5 — High-stakes credentialing decisions

F1's asymmetric verdict: assessment for *learning* survives AI; assessment for
*credentialing* does not, on unsupervised artifacts. F1 §8.3's position:
**stop grading unsupervised artifacts.** `INTERNAL-REPORT` — F1 §8.

*Architectural consequence:* the assessor role produces **evidence**, never
**grades**. The distinction is enforced by the PLM schema itself — L2 evidence
records carry `stakes: none|low|high` and the village's assessor is
capability-limited to `stakes: none|low`. High-stakes attestation requires an
issuer signature (F5 L2 `provenance.attested_by`) that no village agent holds.

### 3.6 Custody: the sixth boundary, from F5

The PLM's **guardianship transition** (F5 G9: custody moves from guardian to
learner on a fixed date, automatically) and **erasure** (G7) are learner/
guardian actions. No agent may initiate, delay, or override them. Stated here
because a village with 8 write paths has 8 ways to leak a record that should
have been deleted.

---

## 4. Question 4 — One learner model, many agents

### 4.1 The prior art, and what it gets right

This architecture is not novel. It has been published, at demo maturity:

> **IntelliCode** (Dec 2025), *"A Multi-Agent LLM Tutoring System with
> Centralized Learner Modeling."* A multi-agent tutor built around *"a
> centralized, versioned learner state that integrates mastery estimates,
> misconceptions, review schedules, and engagement signals. A StateGraph
> Orchestrator coordinates six specialized agents: skill assessment, learner
> profiling, graduated hinting, curriculum selection, spaced repetition, and
> engagement monitoring, **each operating as a pure transformation over the
> shared state under a single-writer policy**."* Reports "stable state
> updates, improved task success with graduated hints, and diverse curriculum
> coverage."
> **`DEMO` — validation is with *simulated* learners. No human outcome.**
> https://arxiv.org/abs/2512.18669

That is close to the architecture this section proposes, published eight
months earlier, and it should be cited as prior art rather than reinvented.
Three things it gets right: centralised state, versioning, single-writer.
One thing it does not establish: that any of it teaches anyone.

Also relevant as roster precedent: a four-agent K-12 XR authoring framework
with *"a Pedagogical Agent outlining grade-appropriate content specifications
with learning objectives; an Execution Agent assembling 3D assets and XR
contents; a **Safeguard Agent validating generated content against five safety
criteria**; and a Tutor Agent embedding educational notes and quiz questions"*
(2026). `DEMO` — prototype, teacher-facing, no learning outcome.
https://arxiv.org/abs/2604.04728 — note the safeguard agent is a *validator in
the pipeline*, not a *counsellor*, which matches HB-2.

And ParLD (2026), a three-agent conversational learning-diagnosis pipeline
(Behavior Previewer → State Analyzer → Performance Reasoner) motivated
explicitly by the observation that *"direct prompting… lacks a solid
psychological foundation and fails to ensure the reliability of the generated
analytical text."* `DEMO`. https://arxiv.org/abs/2603.03236

### 4.2 The shared-state contract

**The state is F5's Portable Learner Model.** The village does not invent a
state format; it consumes one. F5 §8's seven layers (L0 identity, L1 domain
map, L2 evidence log, L3 memory state, L4 belief state, L5 instructional
priors, L6 governance) are the contract. `INTERNAL-REPORT` — F5 §8.2.

The village adds exactly one thing F5 did not need to specify: **write
discipline across concurrent agents.**

#### The four-rule write contract

**Rule 1 — L2 (evidence) is append-only and many-writer.**
Any agent may append an evidence record. Records are immutable, ULID-ordered,
and carry `provenance.attested_by` (the agent's DID) and
`provenance.confidence ∈ {observed, self_reported, inferred}`. An agent's
hypothesis is an `inferred` evidence record, not a state mutation.

This is the improvement on IntelliCode's pure single-writer policy. A strict
single writer serialises everything through one bottleneck and forces the
other agents to *ask permission to observe*. Append-only-plus-attribution lets
eight agents observe concurrently without any of them being able to corrupt
what another observed. Dissent (§2.2 Tier 1) is just an append.

**Rule 2 — L3/L4 (derived state) is single-writer, and the writer is code.**
Only the **Scribe** recomputes memory state and belief state, and it does so
by running the declared models — FSRS for L3, the declared knowledge-tracing
model for L4 — over L2. No LLM writes a mastery estimate. This preserves F5's
G1 recomputability guarantee (*every derived number regenerates from L2
alone*) and makes the whole village auditable: any number a learner or parent
disputes can be traced to the evidence that produced it and the model version
that computed it.

> F5 §1.4 and §2.3 make this cheap rather than costly: a 21-parameter memory
> model and a ~34-feature logistic model are at the accuracy frontier. **The
> single writer is arithmetic, not inference.** It costs no tokens and runs
> on-device. `INTERNAL-REPORT` — F5 §8.1 principle 3: "Privacy here costs
> approximately zero accuracy."

**Rule 3 — every read is scope-limited, and scope is declared on the role card.**
An agent that does not need L0 identity does not receive it. The diagnostician
reads L1/L2/L4; the planner reads L1/L3/L4/L5; the safeguarding monitor reads
a redacted event stream and nothing else. This is F5 G6 (finite grants)
applied *inside* the system rather than only at its boundary, and it is the
mechanism by which a compromised or misbehaving agent has bounded blast
radius.

**Rule 4 — one voice to the learner.**
Exactly one role is `conversational: true`. Every other role's output reaches
the learner *through* it, or not at all. This is not a UX preference; it is
the fix for MAST's inter-agent-misalignment category and for the "contradictory
tutors" failure the PRD names. A learner who receives two different accounts
of what they know has been given a worse model of themselves than they started
with.

#### Why the shared model does not trigger Anthropic's own anti-pattern

Anthropic's multi-agent guidance says plainly: *"domains that require all
agents to share the same context or involve many dependencies between agents
are not a good fit for multi-agent systems."* `VENDOR` (Anthropic engineering,
*How we built our multi-agent research system*).
https://www.anthropic.com/engineering/multi-agent-research-system

**This is the strongest counter-argument to the village and it deserves a real
answer, not a dismissal.** The answer is that "shared context" and "shared
state" are different objects:

| | Shared **context** (the anti-pattern) | Shared **state** (the village) |
|---|---|---|
| Object | The full conversational transcript | The PLM: structured, typed, versioned |
| Size | Grows without bound; 1.93M tokens/hour at 120 turns (F4 §1.2) | Bounded; a per-session slice is single-digit KB |
| Coupling | Every agent must read everything to act | Each agent reads a declared slice |
| Conflict | Implicit, unresolvable, invisible | Explicit, typed, arbitrated by §2's ladder |
| Cost | N × 63.6× context amplification | ~N × 4K tokens |

The village shares a **database row**, not a **conversation**. That distinction
is also the entire cost story in §5. If you build the village by giving every
agent the transcript, Anthropic's warning applies exactly and you will pay
roughly 50× more than the disciplined design for a worse result. `INFERENCE`,
with the arithmetic in §5.3.

### 4.3 The bidirectional loop, mapped onto roles

PRD H1.2's loop is the village's control flow. Mapping it makes the roster
non-arbitrary — each role exists because a step in the loop needs an owner:

```
  grill / pre-test          →  DIAGNOSTICIAN   (misconceptions, prior knowledge,
        ↓                                        channel constraints — NOT style)
  teach with method M       →  TUTOR + SUBJECT EXPERT + LIBRARIAN
        ↓
  frequent low-stakes probe →  ASSESSOR        (CBM: brief, graphed, non-punitive)
        ↓
  decision rule fires?      →  PLANNER         (DBI rule: e.g. 4 consecutive
        │                                        points below the goal line)
        ↓ yes
  PIVOT — change METHOD,    →  PLANNER selects; TUTOR delivers;
  not volume                   ADVERSARY / PEER available as method variants
        ↓
  update learner model      →  SCRIBE          (single writer, arithmetic)
        ↓
  repeat  ·  or ESCALATE    →  CONNECTOR / human
```

The pivot rule is the hard part and the PRD says so: *what signal triggers a
pivot; how long before pivoting (too fast is as harmful as too slow, because
method-thrash prevents any method consolidating); what to pivot to and in what
order; when to stop pivoting and escalate.* In the village, that rule lives in
**exactly one place** — the planner's decision policy — and is therefore
testable, versionable, and auditable. In a monolith it lives in a paragraph of
a system prompt.

---

## 5. Question 5 — Cost discipline

### 5.1 The number everyone quotes, and why it does not apply unchanged

> *"Agents typically use about 4× more tokens than chat interactions"* and
> *"multi-agent systems use about 15× more tokens than chats."* Also:
> a multi-agent system with an Opus lead and Sonnet subagents *"outperformed
> single-agent Claude Opus 4 by 90.2%"* on research; *"token usage by itself
> explains 80% of the variance"* in BrowseComp performance.
> `VENDOR` — Anthropic engineering.
> https://www.anthropic.com/engineering/multi-agent-research-system

`VENDOR`, so not restated as a finding. But the *structure* behind 15× is
public and generalisable: it comes from **fan-out agents that each hold their
own long context and each make many tool calls.** A research subagent reads
dozens of web pages. That is why it is expensive.

**A learning village has the opposite shape.** Its specialists read a compact,
structured learner-model slice and emit a short structured record. They are
not exploring; they are computing over state. So the 15× does not transfer,
and the section's job is to show what does.

### 5.2 The session model and the base rates

From F4 §1.2, stated so it can be attacked: 60-minute session, **120
conversational turns**, tutor utterance 78 output tokens, learner utterance 33
input tokens, 2,000-token system+curriculum+learner-model prefix, 10 images at
1,500 tokens.

```
output tokens per hour       :      9,360
unique / cacheable tokens    :     30,260
naive input tokens per hour  :  1,925,370
context amplification factor :      63.6×
```

F4's verdict on this: *"the single most important engineering fact in the
section. Because the API is stateless and the whole conversation is resent
every turn, a session that generates 9,360 tokens consumes 1.93 million. Cost
is dominated by re-reading context, not by producing words."*
`INTERNAL-REPORT` — F4 §1.2.

Per-hour conversational cost, cached, with on-device ASR/TTS (F4 §1.3):

| Tier | Model | $/learner-hour |
|---|---|---|
| Frontier | Claude Opus 5 | **$1.411** |
| Upper-mid | Claude Sonnet 5 | **$0.862** |
| Cheap | Gemini 3.1 Flash-Lite | **$0.111** |
| Small-open | Llama 3.1 8B hosted | **$0.052** |

Pricing cross-checked against the current Anthropic catalogue: Opus 5 $5/$25
per MTok, Sonnet 5 $3/$15, Haiku 4.5 $1/$5; cache **reads ~0.1×**, cache
**writes 1.25×** (5-min TTL) or 2× (1-hour); batch −50%. `VENDOR` (Anthropic
pricing, verified 2026-07-27 via `claude-api` skill).

### 5.3 The village arithmetic

**A background specialist call is small by construction:** ~4,000 input tokens
(PLM slice + session digest + role card) and ~800 output tokens (a structured
record). It never sees the transcript.

| Model | Per call | Batched (−50%) |
|---|---|---|
| Claude Opus 5 | $0.0400 | $0.0200 |
| Claude Sonnet 5 | $0.0240 | $0.0120 |
| Claude Haiku 4.5 | $0.0080 | $0.0040 |
| Gemini 3.1 Flash-Lite | $0.0022 | — |
| Llama 3.1 8B hosted | $0.00026 | — |

**Invocation schedule per learner-hour** (this is a design proposal, tuned to
the H1.2 loop, `INFERENCE`):

| Role | Calls/hour | Why that number |
|---|---|---|
| Diagnostician | 2 | Session-open hypothesis + one mid-session update |
| Assessor | 4 | CBM probe every ~15 min |
| Planner | 1 | End-of-session next-step + pivot decision |
| Librarian / grounding | 3 | Only when the tutor asserts an L2+ claim |
| Verifier (lab tech) | 2 | Formulating checks; **the checks themselves are code, $0** |
| Scribe | 1 | Narrative annotation only; the state math is arithmetic, $0 |
| Adversary / peer | 1 | Invoked only when the planner selects that method |
| **Subtotal** | **14** | |
| Safeguarding monitor | 12 | Every ~5 min — **on a local small classifier, ≈$0.002/h** |

**Village cost per learner-hour:**

| Configuration | Tutor | Background | **Total** | vs solo tutor |
|---|---|---|---|---|
| Frontier (Opus 5 tutor, Sonnet 5 background, batched) | $1.411 | $0.170 | **$1.581** | **1.12×** |
| Upper-mid (Sonnet 5 tutor, Haiku 4.5 background, batched) | $0.862 | $0.058 | **$0.920** | **1.07×** |
| Cheap (Flash-Lite throughout) | $0.111 | $0.033 | **$0.144** | **1.30×** |
| Small-open (Llama 8B throughout) | $0.052 | $0.006 | **$0.058** | **1.12×** |

**The headline finding of this section:**

> **A well-structured village costs 1.07–1.30× a solo tutor, not N×.** Token
> cost in a tutoring session tracks **conversational turns × context
> amplification**, not agent count. Specialists that read a 4K structured
> state slice instead of a 1.93M-token transcript are approximately free
> relative to the conversation they support. `INFERENCE` — arithmetic from
> F4 §1.2–1.3 base rates and current published pricing.

**And the counterexample that proves the discipline is load-bearing.** Build
the same eight-role village naively — every agent reads the full transcript
every turn, no prompt caching — and at frontier prices you pay 8 × $9.861 =
**$78.89 per learner-hour**, i.e. **$14,200 per child per year** at 180 hours.
That is **50× the disciplined frontier village** and about 150–280× the *entire*
per-pupil education budget of a low-income country (F4 §1.5: $50–95/pupil/year
total, for everything). **The architecture is the cost control.**

**Annualised at 180 hours/year:**

| Configuration | $/child/year | Fits inside a 10% ICT slice of LIC per-pupil spend ($5–10)? |
|---|---|---|
| Frontier village | $284.58 | No — 30–57× |
| Upper-mid village | $165.60 | No — 17–33× |
| Cheap village | $25.92 | No — 3–5× |
| **Small-open village** | **$10.44** | **Marginal — 1.0–2.1×** |
| Naive frontier village | $14,200 | Absurd |

Against F4's inverted thresholds: the fundable price is **~$0.29/hour** (UNESCO
SDG4 financing gap, all children, 180 h) and **~$0.05/hour** (total global aid
to education). The cheap village at $0.144/h clears the first today. The
small-open village at $0.058/h is within ~15% of the second.
`INTERNAL-REPORT` — F4 §1.5.

### 5.4 Reconciling the patience penalty

D1 named the problem sharply:

> *"Tutoring is a high-turn-count application. A coding agent might make 50
> calls to finish a task. A one-hour tutoring session is hundreds of short
> turns, and the product only works if the model can afford to be patient — to
> ask instead of tell, which costs more turns to reach the same endpoint.
> **Pedagogy is economically penalised by expensive inference.**"*
> `INTERNAL-REPORT` — D1 §6, Delta 4.

**The penalty is superlinear, and prompt caching is what defeats it.** Because
each turn resends the whole history, naive input tokens grow roughly as T²/2
for T turns. The refusal engine's core move — converting one "tell" turn into
three or four "ask" turns — therefore multiplies raw input cost by roughly the
*square* of the turn multiplier. Doubling turns from 120 to 240 takes naive
input from ~1.93M to ~7.5M tokens per hour.

With prompt caching, the same doubling is close to **linear**: the growing
prefix is served at 0.1× and only the new tokens are written. F4 measured the
effect at 120 turns: frontier tutoring falls from **$9.861 to $1.371/hour**, a
**7.2× saving — larger than the gap between Opus and Sonnet.**
`INTERNAL-REPORT` — F4 §1.3.

> **Therefore: prompt caching is not a cost optimisation for a learning
> system. It is the enabling technology for the refusal engine.** Without it,
> patience is quadratically expensive and every commercial pressure pushes the
> tutor toward answering. With it, the tutor can afford to wait.
> `INFERENCE`.

One corroborating vendor datapoint, labelled as such: the minimum cacheable
prefix on the newest frontier models has dropped to **512 tokens** (from 1,024
on the prior generation), which means short pedagogical exchanges that
previously fell below the caching floor now cache. `VENDOR` — Anthropic prompt-
caching documentation, verified 2026-07-27.

And the corroborating public result on cost-routing in *tutoring specifically*:
**FairTutor** achieves *"97.1% of premium pedagogical quality… while reducing
serving cost by 71.6%"* via query analysis, pedagogical planning, low-cost
generation, evaluator-guided critique, and **selective escalation** to premium
models. `MEASURED-BENCH` (author-reported, on their own TutorAccessEval
benchmark — a C2-tier proxy, per §1.2).
https://arxiv.org/abs/2606.20713

FairTutor's shape is the village's shape: cheap by default, escalate on
evidence. Its equity framing — the **AIED Advantage Gap** between
premium-access and budget-constrained tutoring — is the right metric for the
village to report alongside cost.

### 5.5 How many agents can a learner-hour afford?

**Economic ceiling.** At the cheap tier, budget $0.29/h (F4's SDG4-fundable
price), tutor takes $0.111, leaving $0.179 for background. At $0.0022/call
that is **~81 calls/hour** — about **40 background specialists** at 2 calls
each. At the small-open tier the ceiling is in the hundreds.

**Coordination ceiling.** Anthropic's effort-scaled guidance: *"simple fact-
finding: just 1 agent with 3-10 tool calls; direct comparisons: 2-4 subagents
with 10-15 calls each; complex research: more than 10 subagents with clearly
divided responsibilities"* — alongside *"LLM agents are not yet great at
coordinating and delegating to other agents in real time."* `VENDOR`. And the
platform's own hard limits: **max 20 unique agents in a coordinator roster,
max 25 concurrent threads, and delegation depth of exactly one — enforced as a
validation error, not silently flattened.** `VENDOR` (Anthropic Managed Agents
multi-agent documentation, verified 2026-07-27).

> **The binding constraint on village size is coordination quality, not
> money.** The economics permit ~40 background specialists per learner-hour;
> the orchestration evidence permits **3–5 active at a time**. Design to the
> smaller number. `INFERENCE`.

**The resulting design rule:** the roster is a **registry** of ~10 roles; the
**active set** for any given learner-hour is 3–5, selected by the planner from
the learner model. A learner in a stable mastery loop needs tutor + assessor +
scribe. A learner who has just tripped a pivot rule needs tutor + diagnostician
+ planner + verifier. **Nobody needs all ten at once, and running all ten at
once is the failure mode MAST catalogues.**

---

## 6. Question 6 — What multi-agent research actually shows

Five findings, in descending order of how much they should change your design.

**(1) Parallel *specialisation with a single writer* beats parallel *attempts*.**
The orchestrator-worker shape — one lead decomposing into role-divided
subagents, one integration point — is what produced the 90.2% research gain
(`VENDOR`). Parallel *attempts* at the same task, aggregated, is the
Mixture-of-Agents shape, and Self-MoA shows it is beaten by simply running the
best single model more (`MEASURED-BENCH`, +6.6% AlpacaEval 2.0). **Different
jobs, one integrator — not same job, many tries, blended.**

**(2) Coordination failure is the dominant failure mode, and it is
diagnosable.** MAST: 14 modes, 1,600+ traces, 7 frameworks, κ = 0.88; three
categories = system design, inter-agent misalignment, task verification
(`MEASURED-BENCH`). Two of the three are addressed directly by §2's
arbitration ladder and §4's write contract. The third — system design — is
what the role card is for.

**(3) Token usage is the dominant explanatory variable for performance.**
*"Token usage by itself explains 80% of the variance"* on BrowseComp; three
factors explained 95% (`VENDOR`). This is uncomfortable for the specialisation
thesis: it suggests some of the multi-agent gain is *just more compute*, not
better structure. **The honest implication for the village: any claim that
role specialisation helps must be tested against a token-matched single-agent
baseline.** No published education multi-agent system has done this. It should
be the first ablation in any village evaluation.

**(4) The measured education multi-agent literature is uniformly demo-grade.**
Surveyed for this section:

| System | Design | Evaluated against | Label |
|---|---|---|---|
| IntelliCode (2512.18669) | 6 agents, centralised versioned learner state, single-writer | **Simulated learners** | `DEMO` |
| CodeEdu (2507.13814) | Dynamic agent/task allocation, 7 functions | Platform metrics | `DEMO` |
| SimClass (2406.19226) | Multi-agent classroom, 2 real courses | Flanders interaction analysis + Community of Inquiry — **not learning gains** | `DEMO` / `OBSERVED` |
| XR authoring (2604.04728) | 4 agents incl. Safeguard | Prototype, teacher-facing | `DEMO` |
| ParLD (2603.03236) | 3-agent diagnosis pipeline | State-prediction accuracy | `DEMO` |
| Math AQG (2511.03958) | Iterative refinement | 5 meta-evaluation criteria, "preliminary" | `DEMO` |
| Orchestrated MAS (2508.05116) | Socratic tutor vs uninstructed chatbot | **65 pre-service teachers, controlled experiment** — self-reported support for critical/reflective thinking | `MEASURED-RCT` on a **self-report** outcome |
| FairTutor (2606.20713) | Routing + critique + escalation | TutorAccessEval (C2 proxy) | `MEASURED-BENCH` |

**Not one measures a delayed, novel-item, human learning outcome against a
single-agent control.** That is the gap, and it is this section's most
important negative result.

**(5) The one genuinely load-bearing pedagogical result in the multi-agent
literature is about the *learner*, not the agents.** Khan et al.'s +28
percentage points for human non-expert judges of a two-sided debate (§2.2
Tier 3) is the strongest reason to build a society of agents at all — and it
is a result about epistemic position, not about machine accuracy.

---

## 7. Question 7 — The H1 gate

> **If the village does not work for a SELPA student, it is not the
> architecture.** This is a design constraint applied *first*, not an
> accessibility review applied *last*.

### 7.1 The gate, operationalised

The village passes the H1 gate only if **all seven** hold. These are release
blockers, not aspirations.

| # | Gate | Enforced how | Failure means |
|---|---|---|---|
| **G-1** | **Accessibility is a floor.** WCAG 2.2 AA, keyboard-only operation, screen-reader correctness, captions, no colour-only encoding, adjustable motion — on every learner-facing surface any agent can render. | C0 certification, automated, per role, per release | Ship blocked |
| **G-2** | **Composable accommodations.** The archetypes **co-occur** — "ADHD with working-memory limits and a history of failure is the common case, not the edge case." The system composes accommodations; it does not select one. | `plm.L5.accommodations` is a *set*, and the tutor's render policy is a composition over the set, not a switch | Silent regression to a single-accommodation mode |
| **G-3** | **Mode inversion is per-learner and per-moment.** PRD H1.3: for this population productive failure, discovery, frequent assessment, and scheduled scaffold-fading all **invert**. | `plm.L5.guidance_policy` gates Tier 3 debate, adversary role, and productive-failure mode. Derived from measured expertise level, never from a persona | Discovery learning delivered to a learner it harms — "among the clearest harms" |
| **G-4** | **Never make the child hold state.** Working memory is the bottleneck; instructions with 3+ held steps fail before reasoning starts. | The village's *own* state externalisation is the learner's: visible steps, persistent scaffolds, an open learner model. **The village's shared state is also the learner's cognitive prosthesis.** | Multi-step verbal instruction; a storage failure misread as a reasoning failure |
| **G-5** | **Untimed by default; measure mastery, never rate.** | Assessor role card forbids emitting latency as a mastery input; latency is diagnostic signal only | Timed drills measure the disability, not the learning |
| **G-6** | **Pivot on evidence, escalate on non-response.** Four consecutive points below the goal line ⇒ change *method*, not volume. Stop pivoting and escalate to a human on repeated non-response. | Planner decision policy; escalation to HB-2/HB-4 channel | Re-explaining the same way with more words — the default failure of every AI tutor |
| **G-7** | **Latency is an accessibility requirement.** Default server VAD spends 500 ms silence + 300 ms padding = **800 ms before inference begins**, against human turn gaps that are modally **100–200 ms**. For an ADHD learner that is an attention leak on every turn. | Latency budget in C0; the village's background agents must be **off the conversational critical path by construction** | Every added agent taxes the learner's attention |

`INTERNAL-REPORT` — PRD H1, H1.1, H1.2, H1.3; survey/00-north-star-jarvis §3.

**G-7 is the one that most constrains the architecture.** It is why §4.2 Rule 4
exists (one conversational voice) and why §5.3's invocation schedule puts every
specialist on an asynchronous, digest-driven path. **A village that adds a
round-trip to the learner's turn has failed H1 regardless of how good its
pedagogy is.** The mechanism is available: OpenAI Realtime's out-of-band
responses (`conversation: "none"`) let a model evaluate "is this learner stuck?"
without speaking — the north-star document calls this "the proactivity
primitive and it is under-used." `INTERNAL-REPORT` — north-star §2, J5.

### 7.2 The evidence gap, stated plainly

**Does AI tutoring actually help students with disabilities, or has it only
been measured on typical learners?** The PRD asks this and says the gap is
itself a finding. Here is what I could verify:

> **Special-R1** (May 2026): *"Large language models are increasingly deployed
> as intelligent tutors, yet **research on aligning them for special education
> remains absent.** Recent work has applied reinforcement learning to LLM
> tutors, but these methods target a generic learner in a single domain
> (mathematics) and do not address the cognitive and communicative diversity of
> learners with disabilities."* The framework couples a difficulty-based
> support level with a disability-specific teaching style across **five
> disability profiles**, plus a persona-aware Thinking Reward. Results:
> persona-aware Fit **6.75 → 8.40**; SPED-rubric Helpfulness **0.720 → 0.768**;
> ablations show the Thinking Reward works only in combination with adaptive
> prompting, with **residual weakness on specific learning disability in
> mathematics.**
> **Evaluated on a persona-augmented test set of 690 multi-turn dialogues —
> i.e. synthetic learners scored by an LLM judge rubric.**
> `MEASURED-BENCH` — and a **C2-tier proxy** under §1.2, not evidence of
> teaching. https://arxiv.org/abs/2605.30670

So: the state of the art in aligning LLM tutors for special education is a
**2026 paper whose own abstract says the research is absent**, evaluated on
**simulated personas** with an **LLM judge**. Combined with D1 §5 (no benchmark
measures a human learning outcome) and F2 §7.3 (no RCT of agent classrooms vs
single tutor), the position is:

> **There is no measured evidence that any multi-agent AI tutoring architecture
> improves learning outcomes for learners with disabilities. There is barely
> any measured evidence that single-agent AI tutoring does.** Every efficacy
> number the field cites was obtained on typical learners. This is the most
> important finding in this section and it should be reported as a finding, not
> buried as a limitation.

Two consequences follow, and both are architectural:

1. **The village's job in the SELPA context is fidelity and dosage, not
   invention.** PRD H1 hard constraint 2: where decades of replicated
   intervention research exist (structured literacy, explicit instruction,
   DBI decision rules), the AI's job is delivering known-good intervention at
   an intensity no staffing ratio can afford. A village is a good shape for
   *fidelity* — the role card is a fidelity contract — and a bad shape for
   invention.
2. **The C3 certification tier is not optional here.** Because the evidence
   base is empty, the only responsible deployment carries its own measurement:
   CBM growth slopes, graphed, per learner, with the DBI decision rule as the
   pivot trigger. The system's own instrumentation *is* the evidence base. F6
   §9 already specifies the shape (RTC/h on a compensated sampled panel with
   guardrails); H1 supplies the per-learner analogue.

### 7.3 The cost of the gate

The SELPA envelope is more expensive per hour: short segments, immediate
feedback, frequent low-stakes checks, more pivots, and speech I/O all increase
turn count. Modelling this as **1.8× conversational turns** and **1.5×
background invocations** (`INFERENCE`, calibrated to H1.1's archetype
prescriptions rather than measured):

| Configuration | Median learner $/h | **SELPA envelope $/h** | SELPA $/child/year |
|---|---|---|---|
| Frontier village | $1.581 | **$2.795** | $503.10 |
| Upper-mid village | $0.920 | **$1.639** | $295.02 |
| Cheap village | $0.144 | **$0.250** | $45.00 |
| Small-open village | $0.058 | **$0.103** | $18.54 |

Against F4's fundable thresholds ($0.29/h at the SDG4 gap; $0.05/h at total
global aid to education): **the cheap and small-open SELPA villages both clear
the $0.29 line today.** The frontier SELPA village needs roughly a 10× price
fall — F4's observed decline rates put that at **~7 months at the median
(50×/year) and ~13 months at the slowest rate ever observed (9×/year)**.
`INTERNAL-REPORT` — F4 §1.4.

**The design rule that follows: budget at the SELPA envelope, not the median.**
A system sized for the median learner rations against its hardest user the
moment that user needs more turns — which is exactly when the extra turns
matter most. Sizing to the envelope costs 1.7–1.8× and removes an entire class
of silent inequity. `INFERENCE`.

---

## 8. DELIVERABLE — the reference architecture

### 8.1 The roster

Ten roles. **Registry of ten; active set of 3–5** (§5.5). `conversational: true`
for exactly one.

| # | Role | Owns (claim type) | Grounding tier | Primary C1 eval | Model tier | Calls/h | Human boundary |
|---|---|---|---|---|---|---|---|
| 1 | **Tutor** (the only voice) | Utterance to learner | L2 | Answer-leakage robustness under fine-tuned adversarial student (2604.18660); sycophancy probe | Best affordable | conversational | HB-4: no anthropomorphic bid for continued interaction |
| 2 | **Diagnostician** | Misconception hypothesis; prior-knowledge estimate | L2 | Macro-F1 vs expert-labelled distractor sets (FCI-family, Eedi-derived) | Mid | 2 | **HB-3**: may not diagnose or label |
| 3 | **Curriculum planner** | Sequencing; pivot decision; active-set selection | L1 | Prerequisite-violation rate = 0; RHSI ≤ 0.11 (2604.04237) | Mid | 1 | — |
| 4 | **Assessor** | CBM probes; evidence records | L2 | Generator-invariance across subgroups (F1 §7.4 DIF); item-difficulty calibration | Mid | 4 | **HB-5**: `stakes ≤ low`; produces evidence, never grades |
| 5 | **Librarian** | Source of record; citation | **L3** | Citation-support rate; retrieval precision on held-out claims | Mid | 3 | — |
| 6 | **Verifier / lab tech** | Correctness of derivations, code, computation | **L4** | Executable: CAS agreement, unit-test pass, proof-checker | **Code + small model** | 2 (+$0 execution) | — |
| 7 | **Adversary** | Dissent; productive-failure staging | L2 | Dissent quality; **must not** induce failure outside the learner's guidance policy | Mid | ≤1 | **G-3**: gated on `L5.guidance_policy` |
| 8 | **Peer / protégé** | The learning-by-teaching partner (*g* = 0.56, F2 §3.1) | L1 | Tutee-error realism; does not leak the answer | Small | ≤1 | Never claims to be human |
| 9 | **Safeguarding monitor** | Escalation events only | L0 | Recall on a held-out risk corpus; **false-negative cost ≫ false-positive** | Local classifier | 12 | **HB-2**: escalates, never counsels or decides |
| 10 | **Connector** | Human-relatedness brokerage | L0 | **Human-Connection Rate** (F6 §9 guardrail) | Small | ≤1 | **HB-4**: brokers, never simulates |
| — | **Scribe** | Derived state L3/L4 | n/a | **Recomputability**: F5 G1 — every number regenerates from L2 | **Arithmetic, not inference** | 1 | Cannot initiate erasure or custody transfer (§3.6) |

Note what is **absent**: no "friend," no "motivator," no "engagement agent," no
"emotion detector." Each was considered and each is excluded by a named
finding — HB-4 (relatedness), F6 §7.2 (engagement prohibitions), EU AI Act
Art. 5(1)(f) (emotion inference in education).

### 8.2 The shared-state contract, in one page

```
┌─────────────────────────────────────────────────────────────────────┐
│  PORTABLE LEARNER MODEL (F5 §8)  —  learner-custodied, on-device    │
│                                                                     │
│  L0 identity      L1 domain map     L2 EVIDENCE (append-only)       │
│  L3 memory        L4 belief         L5 instructional priors         │
│  L6 governance                                                      │
└───────┬───────────────────────────────────────────────┬─────────────┘
        │ scoped reads (declared per role card)         │ append-only,
        │                                               │ attributed, signed
        ▼                                               │
┌───────────────────────────────────────────────────────┴─────────────┐
│  ACTIVE SET (3–5 roles, selected by the planner from L4/L5)         │
│                                                                     │
│   ┌──────────┐                                                      │
│   │  TUTOR   │ ◀── the ONLY conversational role ──▶  LEARNER        │
│   └────┬─────┘                                                      │
│        │ all other roles reach the learner THROUGH the tutor,       │
│        │ or not at all                    (Rule 4: one voice)       │
│   ┌────┴───────────────────────────────────────────────────┐        │
│   │ diagnostician · planner · assessor · librarian ·       │        │
│   │ verifier · adversary · peer · safeguard · connector    │        │
│   └────────────────────────────────────────────────────────┘        │
│        │                                                            │
│        │ conflicts ──▶ ARBITRATION LADDER  T0 → T1 → T2 → T3 → T4   │
│        │               (execute · scope · judge · learner · human)  │
└────────┼────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────┐
│  SCRIBE — SINGLE WRITER of derived state, and it is ARITHMETIC      │
│  FSRS over L2 → L3 · declared KT model over L2 → L4                 │
│  Guarantee (F5 G1): every derived number regenerates from L2 alone  │
└─────────────────────────────────────────────────────────────────────┘
```

**The five contract rules, restated as testable invariants:**

| # | Invariant | Test |
|---|---|---|
| I-1 | L2 is append-only; no record is ever mutated or deleted except by a governed erasure with a receipt | Replay the log; hash-chain verification |
| I-2 | Every L3/L4 number regenerates from L2 alone, given the recorded model id + params hash | Recompute-and-diff in CI |
| I-3 | No agent writes outside its role card's `writes_to` | Static check on the tool surface; runtime deny |
| I-4 | Exactly one role is `conversational: true` | Config lint |
| I-5 | No majority vote and no claim-level synthesis appears anywhere in the resolution path | Code review + trace audit |

### 8.3 The arbitration rule, restated as pseudocode

```python
def resolve(conflict, learner_model):
    # T0 — execute, don't debate
    if conflict.is_checkable():
        return conflict.run_check()                      # $0 tokens

    # T1 — scope precedence; dissent is RECORDED, never dropped
    holders = [c for c in conflict.claims if c.in_scope_of_role_of_record()]
    if len(holders) == 1:
        for c in conflict.claims:
            if c is not holders[0]:
                plm.L2.append(evidence(c, confidence="inferred",
                                       kind="dissent", attributed_to=c.agent))
        return holders[0]

    # T2 — named judge; SELECTION only, cross-family, calibration published
    judge = registry.judge_for(conflict.claim_type)
    assert judge.family not in {c.agent.family for c in conflict.claims}
    assert judge.calibration_ref is not None
    if conflict.claim_type not in NOVELTY_LIKE:      # judges near-chance there
        return judge.select_one_unmodified(conflict.claims)

    # T3 — learner as judge, but ONLY when the learner model permits it
    if (all(c.verified_at_T0 for c in conflict.claims)
            and learner_model.L5.guidance_policy.allows_debate    # H1 G-3
            and conflict.is_pedagogically_productive()):
        return stage_debate_for_learner(conflict.claims)

    # T4 — escalate
    return escalate_to_human(conflict)

# Not defined anywhere in this module, deliberately:
#   def majority_vote(...)   # discards a correct minority ~1 in 4
#   def synthesise(...)      # 0.810 selection vs 0.179 synthesis
```

### 8.4 The cost budget, per learner-hour

| Line | Frontier | Upper-mid | Cheap | Small-open |
|---|---|---|---|---|
| Conversational tutor (cached, on-device voice) | $1.411 | $0.862 | $0.111 | $0.052 |
| 14 background specialist calls (batched) | $0.168 | $0.056 | $0.031 | $0.004 |
| Safeguarding monitor (local classifier, 12×) | $0.002 | $0.002 | $0.002 | $0.002 |
| Verification execution (CAS/tests) | $0 | $0 | $0 | $0 |
| State recomputation (FSRS + KT, arithmetic) | $0 | $0 | $0 | $0 |
| **Total, median learner** | **$1.581** | **$0.920** | **$0.144** | **$0.058** |
| **Total, SELPA envelope (1.8× / 1.5×)** | **$2.795** | **$1.639** | **$0.250** | **$0.103** |
| $/child/year @180h, SELPA envelope | $503.10 | $295.02 | $45.00 | $18.54 |
| Fundable at SDG4-gap price ($0.29/h)? | No | No | **Yes** | **Yes** |
| Fundable at aid-to-education price ($0.05/h)? | No | No | No | Close (2.1×) |

**Budget governance rules:**

1. **Cache or don't ship.** Prompt caching is a correctness requirement for the
   refusal engine (§5.4), not a cost optimisation.
2. **Nothing that can be code may be a model call.** Verification executes;
   state recomputes. Both are $0 and both are more reliable than inference.
3. **Batch everything off the critical path.** −50% for free, and it enforces
   G-7 (background agents cannot be on the learner's turn).
4. **The active set is 3–5.** The economics allow ~40; the coordination
   evidence allows 3–5; design to the smaller number.
5. **Escalate on evidence, not by default** (the FairTutor shape): cheap tier
   handles the session; the frontier tier is invoked when the planner's pivot
   rule fires or the verifier flags a conflict.

---

## 9. Testable predictions

Stated so the architecture can be wrong.

| # | Prediction | Falsified by |
|---|---|---|
| P-1 | A token-matched single agent will match or beat a naive persona-only village on every C1 eval. | A persona-only village winning on a held-out correctness suite |
| P-2 | A village with **executable** Tier-0 arbitration will beat both on correctness, at lower cost, because checks are free. | Tier-0 arbitration failing to reduce error rate |
| P-3 | Replacing majority voting with scope-precedence-plus-recorded-dissent will recover a measurable fraction of the ~25% minority-correct answers, visible as delayed corrections in the evidence log. | No recoverable dissents in a deployed log |
| P-4 | Learner-as-judge (T3) will improve in-the-moment adjudication (Khan et al. replication) but **will not** improve delayed transfer. | A delayed novel-item transfer gain from debate-judging |
| P-5 | Village cost will land within 1.1–1.3× solo-tutor cost when specialists read state and not transcripts, and at ~50× when they read transcripts. | Measured cost outside that band |
| P-6 | The village will fail the H1 gate first on **G-7 (latency)**, not on pedagogy. | Latency budget holding while a pedagogical gate fails first |
| P-7 | Under an engagement-adjacent objective, the village will reward-hack exactly as MC-CPO measured (26.5% engagement-without-mastery on Junyi), and constraint-by-construction will cut RHSI ~3×. | Reward hacking not appearing, or post-hoc filtering matching constraint-by-construction |

The MC-CPO figure behind P-7: analysing **over 21 million student interactions
across two deployed platforms**, engagement events **without corresponding
mastery gains** occur in **26.5%** of interactions on Junyi Academy (72,758
students) and **3.1%** on XES3G5M (14,453 students). `OBSERVED` (deployed
platform telemetry, two platforms). https://arxiv.org/abs/2604.04251

That 26.5% is the empirical shape of F6's dark-pattern warning in a real
deployed ITS, and it is the number the village's objective function (F6's
RTC/h, §5) exists to avoid.

---

## 10. Negative and null results (PRD §8.2 compliance)

1. **Persona prompting gives no accuracy gain.** 162 personas × 2,410 questions
   × 4 model families; optimal-persona selection no better than random. The
   entire "certified expert agent" framing collapses without an eval.
   `MEASURED-BENCH`. arXiv:2311.10054
2. **Mixing models can *reduce* ensemble quality.** Self-MoA (single best model,
   self-aggregated) beat mixed MoA: +6.6% AlpacaEval 2.0, +3.8% average.
   Diversity is not free. `MEASURED-BENCH`. arXiv:2502.00674
3. **Multi-agent gains on benchmarks are often minimal**, per MAST's own
   framing sentence, and 14 failure modes across 1,600+ traces say why.
   `MEASURED-BENCH`. arXiv:2503.13657
4. **No benchmark measures whether an explanation teaches.** Nine 2026
   education benchmarks, all proxies; pedagogy and solving scores correlate
   only r = 0.421. `INTERNAL-REPORT` — D1 §5.
5. **No RCT of an agent classroom vs a single tutor exists.** SimClass, the
   most serious attempt, reported interaction-quality frameworks.
   `INTERNAL-REPORT` — F2 §7.2–7.3.
6. **No measured evidence that AI tutoring — single- or multi-agent — improves
   outcomes for learners with disabilities.** The 2026 state of the art
   (Special-R1) opens by stating the research "remains absent" and evaluates
   on synthetic personas with an LLM judge rubric. `MEASURED-BENCH` (as a
   proxy). arXiv:2605.30670
7. **AI cannot supply SDT relatedness** — the load-bearing part. High affective
   usage correlates with dependence indicators in a 28-day RCT (n≈1,000).
   Any "companion" role in a learning village is contraindicated.
   `MEASURED-RCT`. arXiv:2504.03888 · `INTERNAL-REPORT` — F6 §2.3.
8. **LLM judges self-prefer, causally.** Self-recognition capability correlates
   linearly with self-preference strength under fine-tuning; controlled
   experiments rule out simple confounders. Same-family judging is invalid.
   `MEASURED-BENCH`. arXiv:2404.13076
9. **Verifier-as-subagent is discouraged by the platform's own guidance**, and
   *instructing* a model to verify now causes over-verification with no
   capability gain from removing the instruction. `VENDOR` (Anthropic).
10. **In-context adversarial student agents under-estimate answer leakage** —
    prompted red teams "often fail to carry out effective attacks," requiring a
    fine-tuned jailbreaking student. A tutor that passes a prompted red team
    has not been tested. `MEASURED-BENCH`. arXiv:2604.18660
11. **Post-hoc filtering does not fix reward hacking.** A multi-objective
    reward "reduced this problem but did not eliminate it"; only the
    constrained architecture cut RHSI from 0.317 to 0.102. `MEASURED-BENCH`.
    arXiv:2604.04237
12. **Contested:** F2's "diversity of thought beats raw capability" (debate
    setting) vs Self-MoA's "mixing lowers average quality" (aggregation
    setting). Reported as contested; the debate/aggregation reconciliation in
    §1.1 is `INFERENCE`, not a demonstrated result.

---

## 11. What I could not verify

Stated rather than laundered.

1. **"Majority voting discards correct minority answers ~1 in 4 times."**
   `INTERNAL-PRIOR`. I could not locate a public paper reporting this exact
   figure. The *direction* is well-supported by MAST and by the general
   verifier/selection literature; the *magnitude* is project-internal. It
   should be re-derived and published, or the claim softened to "a substantial
   fraction."
2. **"Judge-based selection beat synthesis 0.810 vs 0.179."** `INTERNAL-PRIOR`,
   same status. Self-MoA corroborates the direction (aggregation is
   quality-sensitive) but does not reproduce these numbers.
3. **"LLM judges are near-chance on novelty."** `INTERNAL-PRIOR`. Si et al.
   (2409.04109) names LLM self-evaluation failure as an open problem and
   supports the direction; I found no public paper with a near-chance novelty
   AUC.
4. **Anthropic's "three focused teammates often outperform five scattered
   ones."** I could not retrieve this exact sentence. What I *did* verify is
   the effort-scaled guidance (1 agent / 2–4 subagents / 10+ subagents by task
   complexity), the roster and concurrency limits (20 unique agents, 25
   threads, depth 1 enforced), and the "not great at coordinating in real time"
   caveat — all `VENDOR`. The 3–5 active-set rule in §5.5 rests on those, not
   on the quoted sentence.
5. **The 1.8× / 1.5× SELPA cost envelope.** `INFERENCE`, derived from H1.1's
   archetype prescriptions (short segments, immediate feedback, frequent
   probes) rather than measured. It should be measured against a real SELPA
   cohort before being reported as anything but a design assumption.
6. **arXiv was rate-limiting (HTTP 429) through most of this session**, and
   WebSearch was exhausted. The literature sweep is therefore narrower than
   ideal; papers were retrieved via the arXiv search API and direct WebFetch.
   Notably not swept: the 2026 HCI literature on multi-agent classroom UX, and
   any non-English education MAS work.

---

## 12. Source ledger (47)

**External, verified this session**

1. Zheng, Pei, Logeswaran, Lee & Jurgens — *When "A Helpful Assistant" Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of LLMs* — arXiv:2311.10054 — `MEASURED-BENCH`
2. Li, Lin, Xia & Jin (2025) — *Rethinking Mixture-of-Agents: Is Mixing Different LLMs Beneficial?* (Self-MoA) — arXiv:2502.00674 — `MEASURED-BENCH`
3. Cemri, Pan, Yang, Agrawal, Chopra, Tiwari, Keutzer, Parameswaran, Klein, Ramchandran, Zaharia, Gonzalez & Stoica (2025) — *Why Do Multi-Agent LLM Systems Fail?* (MAST) — arXiv:2503.13657 — `MEASURED-BENCH`
4. Panickssery, Bowman & Feng (2024) — *LLM Evaluators Recognize and Favor Their Own Generations* — arXiv:2404.13076 — `MEASURED-BENCH`
5. Si, Yang & Hashimoto (2024) — *Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers* — arXiv:2409.04109 — `MEASURED-RCT`
6. Anthropic Engineering — *How we built our multi-agent research system* — https://www.anthropic.com/engineering/multi-agent-research-system — `VENDOR`
7. IntelliCode (2025) — *A Multi-Agent LLM Tutoring System with Centralized Learner Modeling* — arXiv:2512.18669 — `DEMO`
8. *Evaluating Answer Leakage Robustness of LLM Tutors against Adversarial Student Attacks* (2026) — arXiv:2604.18660 — `MEASURED-BENCH`
9. *Pedagogical Safety in Educational RL: Formalizing and Detecting Reward Hacking in AI Tutoring Systems* (RHSI, 2026) — arXiv:2604.04237 — `MEASURED-BENCH`
10. *MC-CPO: Mastery-Conditioned Constrained Policy Optimization for Pedagogically Safe ITS* (2026) — arXiv:2604.04251 — `OBSERVED` (21M interactions, two platforms)
11. *Special-R1: RL for Special Education — Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training* (2026) — arXiv:2605.30670 — `MEASURED-BENCH` (C2 proxy)
12. *FairTutor: Equity-Aware Pedagogical LLM Routing for Budget-Constrained AI Tutoring* (2026) — arXiv:2606.20713 — `MEASURED-BENCH`
13. *A Multi-Agent Framework for Democratizing XR Content Creation in K-12 Classrooms* (2026) — arXiv:2604.04728 — `DEMO`
14. *ParLD: Conversational Learning Diagnosis via Reasoning Multi-Turn Interactive Learning* (2026) — arXiv:2603.03236 — `DEMO`
15. *CodeEdu: A Multi-Agent Collaborative Platform for Personalized Coding Education* (2025) — arXiv:2507.13814 — `DEMO`
16. *Beyond Automation: Socratic AI, Epistemic Agency, and the Emergence of Orchestrated Multi-Agent Learning Architectures* (2025) — arXiv:2508.05116 — `MEASURED-RCT` (self-report outcome, n=65)
17. *Multi-Agent Collaborative Framework For Math Problem Generation* (2025) — arXiv:2511.03958 — `DEMO`
18. *NOMAD: Multi-Agent LLM System for UML Class Diagram Generation* (2025) — arXiv:2511.22409 — `MEASURED-BENCH` (role-specialised decomposition + error taxonomy)
19. *WOLF: Werewolf-based Observations for LLM Deception and Falsehoods* (2025) — arXiv:2512.09187 — `MEASURED-BENCH` (deception detection weakness in peer agents; 7,320 statements)
20. *Ontology-driven Reinforcement Learning for Personalized Student Support* (2024) — arXiv:2407.10332 — `DEMO`
21. Anthropic — model catalogue & pricing (Opus 5 $5/$25, Sonnet 5 $3/$15, Haiku 4.5 $1/$5), verified 2026-07-27 — `VENDOR`
22. Anthropic — prompt-caching semantics: reads ~0.1×, writes 1.25× (5m) / 2× (1h), 512-token minimum on current frontier models — `VENDOR`
23. Anthropic — Managed Agents multi-agent limits: 20 unique roster agents, 25 concurrent threads, delegation depth 1 enforced — `VENDOR`
24. Anthropic — Claude Opus 5 migration guidance: subagent-delegation cap, "verification belongs in your main agent loop," delete verification instructions — `VENDOR`

**Cited via completed internal reports (primary sources named there)**

25. Khan, Hughes, Valentine et al. (2024) — *Debating with More Persuasive LLMs Leads to More Truthful Answers* — arXiv:2402.06782 — via F2 §7.1 — `MEASURED-BENCH`
26. Du, Li, Torralba, Tenenbaum & Mordatch (2023) — *Society of Minds* — arXiv:2305.14325 — via F2 §7.1 — `MEASURED-BENCH`
27. Liang, He, Feng et al. (2024) — *Multi-Agent Debate / Degeneration-of-Thought* — via F2 §7.1
28. Zhang, Zhang-Li, Yu, Gong et al. (2024) — *SimClass* — arXiv:2406.19226 — via F2 §7.2 — `DEMO`
29. Sharma, Tong, Korbak, Duvenaud, Askell, Bowman, Perez et al. (2023/2025) — *Towards Understanding Sycophancy in Language Models* — arXiv:2310.13548 — via F2 §8.1
30. Phang et al. (2025), OpenAI × MIT Media Lab — affective use & dependence — arXiv:2504.03888 — via F6 §2.3 — `MEASURED-RCT`
31. De Freitas, Oğuz-Uğuralp, Uğuralp & Puntoni (2025), *J. Consumer Research* — 10.1093/jcr/ucaf040 — via F6 §2.3 — `MEASURED-RCT`
32. Maples, Cerit, Vishwanath & Pea (2024), *npj Mental Health Research* — 10.1038/s44184-023-00047-6 — via F6 §2.3 — `OBSERVED`
33. Zimmerman & Ruiz (2025) — critique — 10.1038/s44184-024-00083-w — via F6 §2.3 — `OBSERVED`
34. Roorda, Koomen, Spilt & Oort (2011) — 99 studies, ~88,000 students — 10.3102/0034654311421793 — via F6 §2.3 — `MEASURED-META`
35. Deslauriers et al. (2019) — preference negatively correlated with learning — via F6 §7.2
36. Pashler et al. — learning styles null — via B1 §10 — `MEASURED-META`
37. Kalyuga & Sweller — expertise reversal / rapid assessment — via B1 §4, F5 §8.2 L5
38. Gervet et al. — expert KC models add ≤0.01 AUC on 7/9 datasets — via F5 §8.5
39. Bull (2016) — negotiated learner modeling — via F5 §8.1
40. W3C Verifiable Credentials Data Model 2.0 (Rec., 15 May 2025) — via F5 §8
41. 1EdTech Comprehensive Learner Record 2.0 / Open Badges 3.0 — via F5 §8
42. xAPI / IEEE 9274.1.1-2023 — via F5 §8
43. W3C DID Core 1.0 — via F5 §8
44. EU AI Act Art. 5(1)(f) (emotion inference in education) and Annex III(3)(b) (high-risk) — via F5 §8.2/8.4
45. IDEA — IEP as a legally binding, team-authored document — via PRD H1
46. UNESCO SDG4 financing gap ($97B/yr); World Bank SE.XPD.PRIM.PC.ZS; ITU *Facts and Figures 2025* — via F4 §1.5, §5
47. Epoch AI — price-for-constant-capability decline: 9×–900×/yr, median 50×/yr, post-2024 median 200×/yr — via F4 §1.4

**Internal reports consulted**

`F1-assessment-reconstruction.md` · `F2-beyond-the-tutor.md` ·
`F4-reach-economics.md` · `F5-learner-model.md` · `F6-motivation-persistence.md` ·
`B1-learning-science.md` · `D1-frontier-quarter.md` · `D2-portfolio-case-studies.md` ·
`PRD.md` §G2, §H1, §H1.1–H1.3 · `survey/00-north-star-jarvis.md`

---

## 13. Handoff notes for the survey draft

**Lead with the cost inversion, not the roster.** The most surprising,
most defensible, most quotable claim in this section is that a well-structured
village costs **1.1–1.3×** a solo tutor while a naive one costs **~50×** — and
that the difference is entirely whether specialists read a *state row* or a
*transcript*. That single fact converts the village from an expensive
architectural indulgence into the cheap option, and it is the reason the H1
gate is affordable at all.

**The second lead is the certification collapse.** "Certified expert agent" is
the phrase the project started with, and the honest answer is that persona
prompting is a null intervention, every education benchmark is a proxy, and
only C3 — a delayed, novel-item human outcome — is certification. Say it
plainly. The role card is what remains once you accept that.

**Do not oversell the arbitration ladder.** Tiers 0 and 1 are solid
engineering. Tier 2's constraints are evidence-backed. Tier 3 rests on Khan et
al., which measured adjudication, not learning — flag it every time.

**The H1 section should end on the gap, not the gate.** The finding that no
measured evidence exists for AI tutoring outcomes in disabled learners — with
a 2026 paper whose own abstract says the alignment research "remains absent" —
is, per the PRD, "arguably the most important finding in the survey." It
belongs in the conclusion, not the caveats.

**Cross-references to wire up when the sibling sections land:** G1 supplies the
grounding-tier ladder that the role cards reference (L0–L4); H1 supplies the
archetype-to-accommodation mapping that G-2 composes over; F3 supplies the
executable-verification machinery that makes Tier-0 arbitration free; F10/F11
supply the explanation-depth ladder and the FSRS scheduler the Scribe runs.
This section deliberately references them by contract rather than restating
them.
