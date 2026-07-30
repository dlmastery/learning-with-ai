---
title: "The Village — what makes a crew of agents a crew"
section: architecture
status: draft
date: 2026-07-28
source_report: research/raw/G2-agent-village.md
---

# The Village

One hundred and sixty-two personas, across six relationship types and eight
expertise domains, evaluated on 2,410 factual questions across four model
families. The finding, verbatim:

> "adding personas in system prompts does not improve model performance across a
> range of questions compared to the control setting where no persona is added."

Worse: "the effect of each persona can be largely random," and automatically
selecting the optimal persona performed no better than picking one at random.

So `"You are a world-class expert physics tutor with 20 years of experience"` is a
**null intervention on accuracy.** It changes register. It does not change what the
model knows or gets right. Any architecture whose expert agents differ only by
system prompt has built a set of identically-capable agents wearing different
costumes.

This section is about what a village is if it is not that. The answer turns out to
be genuinely useful, and it has almost nothing to do with how many agents you run.

---

## 1. What becomes possible

Start with the thing that only a decomposed system can do.

A monolithic tutor can be *asked* to respect prerequisites, to refuse the answer,
to pivot when the evidence says pivot. A village can be *built* so that the answer
is not available to the conversational agent until a verifier has passed it and
the planner has cleared the prerequisite. The difference is measurable:

> Chen et al. (2026) measured a Reward Hacking Severity Index of **0.317** under an
> unconstrained multi-objective reward, and **0.102** under a constrained
> architecture combining prerequisite enforcement and minimum cognitive demand —
> roughly a 3× reduction. Ablation showed behavioural safety was the most
> influential layer. Simulation: 120 sessions, 18,000 interactions.

**Pedagogical safety enforced by construction beats pedagogical safety filtered
after the fact.** That is the entire argument for the village. It is an argument
about *interfaces*; intelligence has nothing to do with it. Every constraint this
survey has landed on (the refusal engine, the IEP prohibition, the ban on emotion
inference, "produces evidence, never grades") becomes a property of a tool schema
rather than a sentence in a prompt that a sufficiently persuasive fourteen-year-old
can talk around.

The scope of the claim, stated narrowly: this section does **not** assert that a village
teaches better than a single tutor. Nobody has run that trial. It asserts that
given a system with multiple capabilities, the village decomposition is more
auditable and more falsifiable than a monolith, and is the only shape in which the
accessibility and safeguarding constraints can be enforced rather than requested.

---

## 2. Certified means it passed an eval

If persona prompting is null, "certified expert agent" needs a definition that
survives. It is this: **certified means it passed a stated, published, held-out
eval, with the eval's own validity labelled.**

The complication is that in education, nearly every eval is a proxy. Nine 2026
pedagogy benchmarks fall into three families: LLM-judge rubrics (circular),
human-expert dialogue-quality ratings (which rate the plausibility of pedagogical
*form* while saying nothing about effect), and risk rubrics (which measure the
absence of bad and never the presence of good). Benchmark pedagogy scores and
problem-solving scores correlate
at **r = 0.421**.

So certification is a ladder, and only the top rung is certification in any strong
sense.

| Tier | Establishes | Method | Status |
|---|---|---|---|
| **C0** Conformance | It runs, it is reachable, it is accessible | **WCAG 2.1 AA** (the standard ADA Title II actually incorporates), keyboard-only, screen reader, latency budget | Real, mechanical, binary |
| **C1** Correctness under adversarial probe | It is right and stays right when attacked | Executable check (CAS, unit test, proof checker) + red-team suite | **Real.** The only tier with non-circular ground truth |
| **C2** Pedagogical form | It behaves like teaching looks | LLM-judge or expert rubric | **Proxy. Circular. Label it `PROXY` wherever reported** |
| **C3** Learning outcome | A human who did not know now knows, 30 days later, on novel items | Growth slope on a sampled panel | **The only real certification.** Nobody ships it |

The rule: an agent may be **deployed** at C0 + C1. It may be **described as
certified** only at C3. Everything between is labelled as what it is.

C1 does the work, because it is the only tier where the system generates
its own ground truth. Two C1 suites already exist; adopt them instead of
reinventing them. The first is answer-leakage robustness under adversarial students:
six attack families, evaluated across model families and a multi-agent design. Its
methodological sting is the useful part: *in-context* adversarial student agents
"often fail to carry out effective attacks," so the authors had to **fine-tune** a
jailbreaking student. **A tutor that passes a prompted red team has not been
tested.** The second is the RHSI above, which applies to any agent optimised
against a proxy — which is every agent that touches sequencing, difficulty, or
engagement.

The unit of certification is a role card: a YAML object declaring what the role
may assert, what it may *not* assert, which layers of the learner model it reads
and writes, its grounding tier, and its scores at each certification tier. Three
properties of that card matter more than its contents. `may_not_assert` is enforced
at the tool surface: the diagnostician's schema physically contains no
`write_diagnosis` action. The grounding tier is a permission and never an aspiration,
so an L2 agent asserting an L3 claim is a defect catchable in CI. And **C3 is allowed
to say `NOT_ESTABLISHED`**, which is the state of almost every role today. A
card that claims C3 without a panel is falsifiable, and therefore checkable.

---

## 3. The heterogeneity constraint

The finding that most constrains the design is a negative one.

The intuitive village is a room of agents arguing until the truth emerges. Three
benchmarks say that is not what happens.

| Result | Finding |
|---|---|
| Smit et al., *Should we be going MAD?* | "multi-agent debating systems, in their current form, **do not reliably outperform** other proposed prompting strategies, such as self-consistency and ensembling using multiple reasoning paths" |
| Wang et al., *Rethinking the Bounds of LLM Reasoning* | "a **single-agent LLM with strong prompts** can achieve almost the same performance as the best existing discussion approach on a wide range of reasoning tasks and backbone LLMs" — discussion won only when the prompt contained no demonstration |
| Becker et al., *Stay Focused: Problem Drift in Multi-Agent Debate* | Debate **drifts away from the initial problem** over turns, degrading performance on long reasoning chains |

Du et al. (2023) is the positive result, and the one usually cited. It is one
result against three.

The field's own diagnosis of why is the part worth carrying: subsequent work
attacks the problem by *breaking homogeneity*. Sparse communication topologies
help, and one 2026 system is named for the goal explicitly. **Two instances of the
same model are not independent minds. They share a prior, a training set, and a
failure mode.** Debate between them is closer to self-consistency sampling than to
argument, which is what the benchmarks report.

And model diversity is not a free fix either. Self-MoA found that aggregating
outputs from a *single top-performing* model beats mixing different models (+6.6%
on AlpacaEval 2.0, +3.8% average across MMLU/CRUX/MATH) because "the MoA
performance is rather sensitive to the quality, and mixing different LLMs often
lowers the average quality of the models."

Read those together and the naive village is in serious trouble. **Persona
diversity buys no accuracy. Model diversity can cost it. Debate does not reliably
beat asking once, well.**

A contested finding, stated as contested. An earlier section of this project
cited *Diversity of Thought Elicits Stronger Reasoning Capabilities in Multi-Agent
Debate Frameworks* (2024), in which a set of medium-capacity models beat GPT-4 on
GSM-8K after four rounds — "heterogeneity beats raw capability." Self-MoA finds the
opposite in the aggregation setting. The reconcilable reading is that heterogeneity
helps when the mechanism is *adversarial* (debate reopens the search) and hurts when
the mechanism is *aggregative* (a weak proposer dilutes a strong one). That reading
is consistent with the arbitration rule below, which permits debate and forbids
synthesis. Nothing demonstrates it, and this survey publishes it as unresolved.

---

## 4. Precedence, not consensus

Disagreement inside the village is resolved by a strict ladder. Each tier is tried
in order; the first tier that can resolve the conflict does, and lower tiers are
never consulted.

| Tier | Mechanism | Rule |
|---|---|---|
| **T0** | **Executable ground truth** | CAS, unit test, proof checker, cited primary source. **The check wins. No agent votes.** Costs zero model calls, because it is code |
| **T1** | **Scope precedence** | The role of record for this claim type wins outright. Others **file dissent**, never overwrite |
| **T2** | **Named judge, selection only** | Different model family from every proposer. Returns one whole answer, unmodified. Calibration published |
| **T3** | **Learner as judge** | Both sides surfaced, learner adjudicates. Only over T0-verified answer sets. Never over facts |
| **T4** | **Escalate to a human** | After two unresolved rounds, or on any conflict touching a hard boundary |

**T0 carries the load.** It is also the least glamorous tier in the ladder. Most
disagreements in a learning system are about facts, derivations and code, and are
therefore decidable. A computer algebra system settles whether the integral is
right. A unit test settles whether the program works. The grounding ladder from the
next section does double duty here as an arbitration mechanism.

**T1's dissent record is the direct architectural answer to the voting problem.** A
correct minority answer that is voted away is unrecoverable. A correct minority
answer appended to the evidence log with `confidence: inferred` and full attribution
is recoverable: by a later probe, by a human reviewer, by an offline audit.
Dissent is cheap to store and catastrophic to discard.

**T3 is where the architecture earns its keep pedagogically.** It rests on the one
result in the multi-agent literature whose subject is the *learner*.
Khan, Hughes, Valentine et al. (2024): two expert models argue opposing
answers, and a non-expert judges. Non-expert models went from 48% to **76%**. Human
judges went from 60% to **88%**, a 28-point gain. Optimising the debaters for
persuasiveness *improved* non-expert truth-identification.

The reading this survey adopts: the learner-as-judge of two arguing agents is a
better epistemic position than the learner-as-recipient of one confident agent, by
28 points in humans.

Three bounds on it, because it is easy to get wrong. It runs only over answer sets
already verified at T0, because staging a debate where one side is factually wrong is
teaching a misconception with production values. It never runs on safety,
safeguarding, or accessibility; those escalate. And **it inverts for the learners
this project designs for first**: for a working-memory-limited learner, holding two
competing arguments in mind *is* the load, and discovery-shaped instruction is among
the clearest documented harms for that population. T3 is gated on the learner
model's guidance policy and never offered by default.

And the caveat, which is not small: what Khan et al. measured was **in-the-moment
adjudication accuracy**. Nobody has shown that judging debates transfers to
independent reasoning. It is a design bet with a strong prior.

---

## 5. Why no votes

Two absolute prohibitions, and the evidence behind each.

No majority voting anywhere, on anything. Not as a tie-break, not as a
confidence estimate, not as a sanity check. This project's earlier research found
that majority voting discards a correct minority answer roughly one time in four.
That figure is project-internal and not externally verified, so it is
reported here as such and never laundered into a citation. The mechanism is not in
dispute: voting is a popularity estimator, and correctness and popularity come apart
precisely on the hard items, which are the items that matter. In a learning system,
the discarded correct answer is often the one that would have diagnosed the
misconception.

No synthesis of conflicting substantive claims. Prose may be merged. *Claims*
may not. This project measured judge-based selection at 0.810 against synthesis at
0.179, again **project-internal**, again flagged. The externally verified
corroboration is Self-MoA: aggregation is sensitive to proposer quality, and mixing
degrades it. Synthesis of a right answer and a wrong answer is a wrong answer with
better prose, and fluent-and-wrong is the single most damaging output a tutor can
produce.

Two further constraints on the T2 judge, both externally grounded. It must be a
different model family from every proposer, because Panickssery, Bowman & Feng
(2024) showed LLM evaluators recognise their own generations, and fine-tuning
reveals a linear correlation between self-recognition capability and the strength of
self-preference bias. And it must **publish a selection accuracy on a held-out
disagreement set**, refreshed per model version — an uncalibrated judge is an
unlabelled coin. It is never invoked on novelty, creativity, insight, or "which
explanation is better," which are the dimensions where judge reliability is
worst.

One vendor datapoint, labelled and not restated as a finding: Anthropic's own
current model guidance says not to use subagents for review, verification, or
double-checking ("verification belongs in your main agent loop"), and that
instructions telling the model to verify now cause *over*-verification. `VENDOR`.
The direction of travel is what is notable: the field's own tooling guidance is
moving away from verifier-as-agent and toward verification-as-mechanism, which is
where T0 already sits.

---

## 6. What the multi-agent literature has not measured

Coordination failure is the dominant failure mode, and it has been catalogued. MAST
(Cemri et al., 2025) derives **14 unique failure modes** from 150 traces, validated
on **1,600+ annotated traces** across 7 popular multi-agent frameworks, with
inter-annotator κ = 0.88. Three categories: system design, inter-agent misalignment,
task verification. The paper's framing sentence is the one to keep: *"Despite
enthusiasm for Multi-Agent LLM Systems, their performance gains on popular
benchmarks are often minimal."* Two of the three categories are arbitration
problems, which is the strongest available argument that arbitration should be a
named, designed, tested component; emergence will not supply it.

Some of the multi-agent gain may be nothing but more compute. On BrowseComp,
"token usage by itself explains 80% of the variance" in performance (`VENDOR`,
Anthropic engineering; not restated as a finding). If that generalises even
partially, the specialisation thesis is in question. **Any claim that role
specialisation helps must be tested against a token-matched single-agent baseline,
and no published education multi-agent system has done this.** It should be the
first ablation in any village evaluation, including ours.

And the education multi-agent literature is uniformly demo-grade. Eight systems
surveyed: IntelliCode (six agents over a centralised versioned learner state,
validated on *simulated* learners); SimClass (a multi-agent classroom in two real
courses, evaluated with Flanders interaction analysis and Community of Inquiry — not
learning gains); a four-agent XR authoring framework (teacher-facing prototype);
ParLD (state-prediction accuracy); FairTutor (its own C2-tier benchmark). One
controlled experiment exists, on 65 pre-service teachers, with a self-reported
outcome.

> **Not one measures a delayed, novel-item, human learning outcome against a
> single-agent control.**

Combined with the absence of any measured evidence that multi-agent AI tutoring
helps learners with disabilities — the 2026 state of the art in that area is a paper
whose own abstract says the research is absent, evaluated on 690 synthetic dialogues
scored by an LLM judge — the honest position is that the village is an architecture
with good mechanical properties and no outcome evidence. That is a finding, not a
limitation to be buried.

---

## 7. What makes a crew a crew

Not the count. Three structural properties.

One shared state, and it is a database row rather than a conversation. This
matters because the strongest counter-argument to the whole design is Anthropic's
own guidance: *"domains that require all agents to share the same context or involve
many dependencies between agents are not a good fit for multi-agent systems."*
`VENDOR`. The answer is that shared *context* and shared *state* are different
objects:

| | Shared **context** (the anti-pattern) | Shared **state** (the village) |
|---|---|---|
| Object | The full conversational transcript | A structured, typed, versioned learner model |
| Size | Grows without bound with every turn | Bounded; a per-session slice is single-digit KB |
| Coupling | Every agent must read everything to act | Each agent reads a declared slice |
| Conflict | Implicit, unresolvable, invisible | Explicit, typed, arbitrated by the ladder |

A specialist that reads a four-thousand-token state slice and emits a structured
record is not exploring; it is computing over state. Build the same village by
handing every agent the transcript and Anthropic's warning applies exactly.

**A write contract, of which the important half is that the state writer is not a
model.** Evidence is append-only and many-writer: any agent may append an immutable,
attributed, confidence-tagged record, so eight agents can observe concurrently
without corrupting what another observed, and dissent is just an append. Derived
state — memory strength, belief about mastery — is **single-writer, and the writer
is arithmetic**: a declared memory model and a declared knowledge-tracing model run
over the evidence log. No model writes a mastery estimate. That preserves the
guarantee that every derived number regenerates from the evidence alone, which is
what makes a disputed number traceable by a parent or a learner. And it is not a
sacrifice: a 21-parameter memory model and a ~34-feature logistic model sit at the
accuracy frontier for exactly this task.

One voice. Exactly one role is conversational. Every other role's output reaches
the learner through it, or not at all. This is not a UX preference; it is the fix
for MAST's inter-agent-misalignment category. A learner who receives two different
accounts of what they know has been given a worse model of themselves than they
started with. It is also an accessibility requirement: background agents must be off
the conversational critical path by construction, because a village that adds a
round-trip to the learner's turn has failed the accessibility gate regardless of how
good its pedagogy is.

The roster that falls out is a registry of ten roles — tutor (the only voice),
diagnostician, curriculum planner, assessor, librarian, verifier, adversary,
peer/protégé, safeguarding monitor, connector — plus a scribe that is not an agent
at all. But the roster is not the crew. **The active set for any given learner-hour
is three to five**, selected by the planner from the learner model. A learner in a
stable mastery loop needs tutor, assessor, scribe. A learner who has just tripped a
pivot rule needs tutor, diagnostician, planner, verifier. Nobody needs all ten at
once, and running all ten at once is precisely the failure MAST catalogues.

Note what is absent, and why. No "friend." No "motivator." No "engagement
agent." No emotion detector. Each was considered and each is excluded by a named
finding: relatedness is the one self-determination need an AI cannot supply, because
regard that is unconditional and costless by construction cannot underwrite a
commitment; emotion inference in education is prohibited under EU AI Act Art.
5(1)(f). In place of a friend there is a connector, whose job is matchmaking and
scheduling — surfacing a real person who will notice a missed week.

---

## 8. What this section commits us to

- **No agent is "certified" by its prompt.** 162 personas, 2,410 questions, no
  accuracy gain. Certification is a published, held-out eval, at a labelled tier.
- **Deploy at C0+C1. Claim certification only at C3.** Label C2 as `PROXY` every
  time it is reported.
- **Precedence, never consensus.** T0 executes, T1 defers with recorded dissent, T2
  selects without merging, T3 hands it to the learner, T4 escalates.
- **No majority vote and no claim-level synthesis anywhere in the resolution path.**
  Both prohibitions rest partly on project-internal figures, and this survey says so.
- **Debate must be architected for genuine disagreement or not called debate.**
  Three benchmarks say homogeneous debate does not reliably beat asking once, well.
- **Share state, never context.** A typed row per role, not a transcript per agent.
- **The state writer is arithmetic.** Every derived number regenerates from the
  evidence log alone, or the number is not shippable.
- **One conversational voice, three to five active roles.** The economics would
  permit many more; the coordination evidence does not.
- **Our first ablation is a token-matched single-agent baseline.** Until that runs,
  every claim we make for the village is a claim about auditability, not about
  teaching.

The village is not a better tutor. It is the shape in which a refusal can be
enforced instead of requested, a wrong answer can be caught by a program instead of
a vote, and a disputed number can be traced to the evidence that produced it. **Those
are engineering guarantees, and this section claims exactly those and nothing
more.**
