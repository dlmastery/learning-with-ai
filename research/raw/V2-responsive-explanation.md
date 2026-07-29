---
title: "The Responsive Explanation — an engineering specification for an artifact generated against one learner's wrong belief and revised while they watch"
wave: V
date_researched: 2026-07-29
sources_count: 41
---

# V2 — The Responsive Explanation

> **The thesis being specified:** the explanation is generated for the one misconception
> the learner actually has, and it changes while they are watching it.

This is not "AI makes good explainer videos." That claim is small, already commoditised,
and measured to be worth roughly nothing on the axis that matters — the whole of §N4
establishes that the world's best pre-rendered explanations have never been evaluated
against delayed transfer, and §29 establishes *why* a clear explanation does not help:
it sits alongside the wrong model and raises confidence.

The frontier claim is different and it is an engineering claim: **the explanation is a
live artifact under continuous revision against a model of this specific learner's
current wrong belief.**

Every component this requires is already measured and sitting in this repository.
Nobody has assembled them. This document is the assembly.

**A note on labels.** Measured claims carry the repository's evidence labels. Anything
designed here and measured nowhere carries **`SPEC`** — a new label meaning *designed in
this document, not observed in any literature*. Roughly two-thirds of this document is
`SPEC`. That is the point of it. Sibling section V1 owns the human technique inventory;
this document owns the machine and does not restate V1.

---

## §0 — What has to exist, in one page

Seven components. Six of them do not exist anywhere. The seventh — the rendering
architecture — is settled and the field has stopped arguing about it.

| # | Component | Status | Section |
|---|---|---|---|
| 1 | **Belief Object** — a learner's wrong model represented so that an explanation can be *generated against it*, and so that it can be *run* | Nothing like it ships. F5 §8's `misconceptions` block is a label plus a scalar | §1 |
| 2 | **Discriminating probe** — 15–40 s, behavioural, surfaces the belief before the explanation begins | Distractor design exists (FCI, Eedi); the *generator* does not | §2 |
| 3 | **XIR** — the explanation intermediate representation: multi-surface, checkable pre-render, patchable mid-stream | The Tier-A pattern exists for *figures* (C1); no IR exists for *explanations* | §3 |
| 4 | **Fidelity compiler passes** — the four invariants as lint rules that block a render | Named in §25/§29 as a rule for humans; never mechanised | §3.4 |
| 5 | **Patch algebra + overlay path** — revision at 200 ms without a language model in the loop | Unbuilt | §4 |
| 6 | **`break()` sandbox** — instantiate the learner's own wrong rule and run it until it visibly fails | Unbuilt. Closest measured relative is Muller's Dialogue condition, d = 0.83 | §5 |
| 7 | **Scene graph with compile-time object IDs** — deixis in a moving artifact | Unbuilt for tutoring (F9 OP-8); the pixel-grounding substrate exists at 49% IoU and is the *wrong* solution | §6 |

**The single architectural commitment that makes the rest coherent:**

> The generative model authors **semantics**. A deterministic renderer owns **geometry**.
> A symbolic engine owns **dynamics**. A precompiled table owns the **200 ms path**.
> No language model sits anywhere on the real-time loop.

C1 measured the first split: decoupling algorithm simulation from rendering moved
success from **82.5% → 99.8%** (ALGOGEN, arXiv:2605.12159, `MEASURED-BENCH`). A5
measured the second: generated worlds satisfy prompt-and-physics in **39.6%** of cases
at best, **22%** on the hard subset (VideoPhy arXiv:2406.03520, VideoPhy-2), and
photorealism makes a physics error *more* persuasive rather than less. The third split
— keeping the LM off the real-time path — is this document's own and is `SPEC`.

---

## §1 — The misconception model

### 1.1 The problem with every existing representation

F5 §6.1 states the indictment better than this section can:

> BUGGY/DEBUGGY (Brown & Burton 1978, `doi:10.1207/s15516709cog0202_4`) synthesised a
> deep-structure model that could **explain *why* a student is making a mistake as
> opposed to simply identifying the mistake.** Forty-eight years later, the
> state-of-the-art model outputs a scalar probability of a correct answer. **We replaced
> a theory of error with a number between 0 and 1.**

F5's own Portable Learner Model (§8.2, `INFERENCE`) is the best schema in the repo and
it does not solve this either. Its `misconceptions` block is:

```yaml
misconceptions:
  - misconception_id: "fci:impetus-force-in-motion"
    status: active | dormant | refuted
    strength: 0.7
```

That is a **classifier output**. You cannot generate an explanation against a
classifier output. You can retrieve a canned refutation keyed to the label, which is a
lookup table with extra steps, and it is what every existing system does.

What is needed is a **generative** representation: a belief you can *execute* to predict
what this learner will say, and *run forward* until it breaks.

### 1.2 The Belief Object, and the interface that is the keystone

The keystone of this entire document is not a data structure. It is three functions that
every belief must implement. `SPEC`.

```
predict(item)            -> Distribution over responses
                            "what would a learner holding this belief answer?"

discriminate(rival)      -> Item
                            "give me an item on which this belief and `rival`
                             (usually the correct model) disagree maximally"

break(case_space)        -> Trace | SCOPE_LIMITED | EQUIVALENT | ⊥
                            "find an input on which running this belief produces a
                             visibly wrong result"
```

Everything else in this document falls out of these three:

- `discriminate()` **is** the probe generator (§2).
- `predict()` **is** the verifier, and it is why the verifier gap does not block us.
- `predict()` **is** what the explanation is compiled against (§3) and what mid-stream
  revision re-evaluates (§4).
- `break()` **is** the strongest move in the system (§5).
- Divergence between `predict()` and observed responses **is** the retirement criterion
  (§1.6).

**`predict()` makes verification unnecessary, and this is the most important consequence
in the document.** K2 measured the blocker: across **223 real tutoring domains, no LLM
performed better than chance at labelling an incorrect student action** (TutorGym,
arXiv:2505.01563, verified 2026-07-29, `MEASURED-BENCH`). Every architecture that asks a
model *"is this student action wrong, and why"* is building on a chance-level primitive.

The Belief Object never asks that question. It asks: **which of my k enumerated beliefs
predicted this response?** That is an argmax over precomputed distributions, not a
judgement. The chance-level labelling problem is converted into a table lookup. The
belief library *is* the verifier. `SPEC`, and it is the design's load-bearing move.

The cost is that the library must be enumerated per domain. F5 §6.6 argues this is
tractable and the evidence supports it: the FCI needs ~30 items to cover Newtonian
mechanics; the Eedi/NeurIPS-2020 corpus has **>20 million student answers** where the
label is *which wrong belief*, not *wrong* (arXiv:2007.12061, `MEASURED-BENCH`).
Misconceptions are a small, discrete, reusable vocabulary per domain. Mastery
probabilities are not.

### 1.3 The schema

```jsonc
// BeliefObject — the unit of the misconception model. SPEC.
// Extends and replaces PLM L4 `misconceptions` (F5 §8.2); PLM L2 evidence log
// remains the sole primary data, per PLM guarantee G1 (recomputability).
{
  "belief_id":   "belief:v1/mech/impetus-force-in-motion",
  "learner_ref": "<pairwise pseudonym, PLM L0>",
  "kc_ids":      ["wikidata:Q11402"],

  // ── WHAT KIND OF WRONG THIS IS ──────────────────────────────────────
  // The form determines the payload, the probe type, the repair, the decay
  // model, and whether break() is even applicable. It is not a tag.
  "form": "CAUSAL_SIGN",
  //  ONTOLOGICAL_CATEGORY | CAUSAL_SIGN | QUANTIFIER_ORDER |
  //  PROCEDURAL_BUG | SCOPE_OVERGENERALISATION | DETERMINED_AS_TUNABLE |
  //  RELATIONAL_ORDER_COLLAPSE

  "invariant_at_risk": "CAUSAL_SIGN",   // §29's four; ONTOLOGY | CAUSAL_SIGN |
                                        // QUANTIFIER_STRENGTH | UNIQUENESS_OF_MECHANISM

  "content": { /* form-specific — see §1.4 */ },

  // ── THE EXECUTABLE FORM ─────────────────────────────────────────────
  // This is the field that does not exist in any shipping learner model.
  "executable": {
    "tier": 1,                          // 1 = total DSL (§5.2); 2 = sandboxed real code
    "lang": "beliefdsl-0.1",
    "source": "<the learner's rule, as code>",
    "source_hash": "sha256:...",
    "domain": { "vars": {"v":"R+","m":"R+"}, "bounds": {...} },
    "authored_by": "template",          // template | model | human
    "termination": "total",             // total | fuel_metered
    "fit": { "predicted": 7, "of": 8, "last_fit_ts": "..." }   // predict() accuracy
                                        // ON THIS LEARNER. A belief that does not
                                        // predict this learner is not their belief.
  },

  // ── EVIDENCE AND CONFIDENCE ─────────────────────────────────────────
  "posterior": {
    "p": 0.78,
    "ci": [0.61, 0.89],                 // uncertainty mandatory (PLM G3)
    "prior_source": "population:mech-9-11:v3",
    "model": {"name":"belief-bayes","version":"0.1","params_ref":"sha256:..."}
  },
  "evidence":       [{"ulid":"...","probe_id":"...","option_id":"B","weight":+1.4}],
  "contra_evidence":[{"ulid":"...","probe_id":"...","option_id":"A","weight":-0.9}],

  // ── VALIDITY: WHERE THE LEARNER'S MODEL IS ACTUALLY RIGHT ───────────
  // Required. Without it the system will try to break a model inside its
  // domain of validity, which teaches the learner that the tutor argues.
  "validity_envelope": {
    "holds_on":  "v << c, no friction, single body",
    "fails_on":  "any case with a normal force doing no work",
    "checked_by": "z3:mech-ref-v2"
  },

  // ── TIME ────────────────────────────────────────────────────────────
  // Two clocks. See §1.5 — this is where every existing model gets it wrong.
  "temporal": {
    "first_observed": "2026-03-02T...",
    "last_confirmed": "2026-07-14T...",
    "belief_half_life_days": null,      // null = does not decay (see §1.5)
    "confidence_half_life_days": 21     // the ESTIMATE decays; the BELIEF may not
  },

  // ── REPAIR ──────────────────────────────────────────────────────────
  "status": "CONFIRMED",
  //  HYPOTHESISED | CONFIRMED | ADDRESSED | SCOPE_LIMITED |
  //  DORMANT | RETIRED | NOT_A_MISCONCEPTION
  "repair": {
    "attempts": [
      {"ts":"...","mode":"NAMED","xir_ref":"...","outcome":"no_change"},
      {"ts":"...","mode":"RUN_FORWARD","xir_ref":"...","outcome":"partial"}
    ],
    "retirement_criterion": {
      "k_consecutive": 3,
      "items_from": "discriminate()",
      "min_delay_days": 7,
      "assistance": "none",
      "unseen_only": true
    }
  },
  "provenance": {"library":"mech-v3","curated_by":"...","fp_reviewed":true}
}
```

### 1.4 The form-specific payloads

The brief is right that these need different representations. They need different
*everything* — different probes, different repairs, different decay, different
applicability of `break()`. Seven forms. `SPEC` throughout, grounded where noted.

**`ONTOLOGICAL_CATEGORY`** — Chi's crossing. The most robust class in the literature:
the Bohr-model hybrid population was **unchanged across a full semester** of university
chemistry (§25). Mathematics' canonical case is **process vs object** — a limit as
*something you do* versus *a number that exists*; a function as *a rule you apply*
versus *a point in a space*. A learner holding "limit" in the process category computes
limits indefinitely and cannot understand uniform convergence, because uniform
convergence quantifies over a **space of functions**, which requires functions to be
objects first (§29, `INFERENCE`).

```jsonc
"content": {
  "entity": "concept:limit",
  "learner_category": "PROCESS",
  "correct_category": "OBJECT",
  "licensed_predicates_learner": ["takes_time","is_fast","has_steps","is_performed"],
  "licensed_predicates_correct": ["is_element_of","is_equal_to","is_a_point_in"],
  "crossing": true          // true ⇒ repair is a category change, not a correction
}
```
`predict()` here is a **sort-check**, not a computation: it predicts which predicates the
learner will accept as *well-formed*, and it predicts they will reject object-predicates
as nonsense. `break()` **does not apply** — there is no dynamics to run. This is the
honest limit of the system's strongest move, stated in §5.4.

**`CAUSAL_SIGN`** — the biology/medicine killer per §29: correlational mechanism narrated
as causal, direction unmarked.

```jsonc
"content": {
  "graph": [{"from":"var:motion","to":"var:force","sign":"+","kind":"CAUSAL"}],
  "correct": [{"from":"var:motion","to":"var:force","sign":"0","kind":"NONCAUSAL"}],
  "intervention_predictions": [{"do":"motion↑","learner_says":"force↑","truth":"force unchanged"}]
}
```
`predict()` runs the signed graph forward under an intervention and returns a direction.
`discriminate()` is trivially cheap: one three-option item, ~8 seconds. `break()` runs
the intervention in the reference engine and shows the sign.

**`QUANTIFIER_ORDER`** — the mathematics and statistics killer. "For every ε there is a
δ" versus "there is a δ that works for every ε" is the difference between continuity and
uniform continuity, and the entire second half of a real-analysis course (§29). In
statistics the canonical instance is "the probability the hypothesis is true", which
reverses the conditional.

```jsonc
"content": {
  "learner_prefix": "∃δ ∀ε ∀x",
  "correct_prefix": "∀ε ∀x ∃δ",
  "statement_ref":  "def:continuity",
  "witness_dependence_dropped": ["x"]     // δ's dependence on x is what got lost
}
```
`predict()` predicts the learner will accept a uniform witness where none exists, and
will fail to distinguish a pointwise case from a uniform one. `break()` is not
execution but **search**: hand the reordered prefix to Z3 (`Z3Prover/z3`, 12,499★,
pushed 2026-07-29, `OBSERVED` GitHub API) and it returns UNSAT on a
pointwise-but-not-uniform case. **The counterexample is the explanation.**

Note the scope fact that makes this form uniquely tractable here: §29 implemented the
quantifier-prefix check and ran it against **1,524 sentences of lecture transcript,
where it fired zero times** — speech *elides* quantifiers rather than reordering them,
so there is no prefix to compare (C-50). It is a check for **authored technical prose
and generated output**. XIR *is* generated output and is *required* to emit a prefix
(§3.3). This is the one place where the machine is better positioned than the human
transcript: there is always something to check.

**`PROCEDURAL_BUG`** — Brown & VanLehn's repair theory: bugs are not random, they are the
outputs of *repairs* a learner applies when a procedure hits an impasse
(`doi:10.1016/B978-1-4832-1446-7.50031-5`).

```jsonc
"content": {
  "procedure_ref": "proc:multidigit-subtraction",
  "mutation": {"step":"borrow","from":"smaller_digit","to":"larger_digit"},
  "impasse": "top digit < bottom digit",
  "repair_applied": "swap-operands"
}
```
Directly executable and directly runnable. This is the easiest form and the one to build
first.

**`SCOPE_OVERGENERALISATION`** — a rule with a missing guard.
```jsonc
"content": { "rule_ref":"rule:distribute-exponent", "guard_dropped":"base is a product",
             "learner_rule":"apply(R) if true", "correct_rule":"apply(R) if P" }
```
`break()` searches the complement of the guard. Nearly always succeeds.

**`DETERMINED_AS_TUNABLE`** — §29 §3.2's engineering endemic, falsifying uniqueness of
mechanism. A quantity determined by a conservation law, a stationarity condition, or a
dimensional constraint, presented as a knob someone chose. The reader concludes the
design is taste, tunes it, and is confused when it breaks.
```jsonc
"content": { "symbol":"Z","learner_status":"ARBITRARY",
             "correct_status":"DETERMINED_BY","by_claim":"claim:normalisation" }
```
This form has the most dramatic `break()`: let the learner **set the knob**. The system
is over-determined, so the solver returns UNSAT. Showing UNSAT is showing that the
choice was never available. `SPEC`.

**`RELATIONAL_ORDER_COLLAPSE`** — Gentner: the attributional→relational shift is not
complete at 10 (F10 §10.3). A three-deep causal chain given to a ten-year-old is
*received* as a set of attributes. This is a belief about the learner's representational
capacity rather than about the domain; it constrains rung selection rather than
triggering a refutation.

### 1.5 Decay — the part everyone gets wrong

Existing models decay a misconception the way they decay a memory. That is backwards.
The literature says the opposite: **cross-category misconceptions are the ones that
survive instruction**, unchanged across a full semester (§25). A misconception is not a
fading trace; it is a stable structure.

What decays is **your confidence that it is still there**. Two clocks. `SPEC`.

| Form | `belief_half_life_days` | `confidence_half_life_days` | Rationale |
|---|---|---|---|
| `ONTOLOGICAL_CATEGORY` | `null` (does not decay) | 90 | Chi: unchanged over a semester |
| `CAUSAL_SIGN` | `null` | 21 | Structural; survives exposition |
| `QUANTIFIER_ORDER` | `null` | 30 | Structural |
| `DETERMINED_AS_TUNABLE` | `null` | 30 | Structural |
| `SCOPE_OVERGENERALISATION` | 180 | 21 | Erodes with counterexample exposure |
| `PROCEDURAL_BUG` | 60 | 14 | Overwritten by practice |
| `RELATIONAL_ORDER_COLLAPSE` | developmental | 180 | Ages out; do not model as repair |

The update rule that follows: **`posterior.p` must not decay toward zero. The credible
interval widens toward the population prior.** A belief unobserved for six months is not
*less likely present*; it is *less well known*. Decaying `p` toward zero produces a
system that quietly forgets the learner's hardest error and then re-teaches the same
lesson every semester, which is what schools do. `SPEC`.

### 1.6 Status transitions — and the one that is illegal

```
                 probe evidence
   HYPOTHESISED ────────────────► CONFIRMED
        │                            │
        │ contra-evidence            │ any repair attempt delivered
        ▼                            ▼
   NOT_A_MISCONCEPTION           ADDRESSED ──── k unassisted correct on
        ▲                            │          unseen discriminating items,
        │ break() = EQUIVALENT       │          delay ≥ 7d
        │                            │              │
   ┌────┴──────────┐                 │              ▼
   │ SCOPE_LIMITED │◄── break() = SCOPE_LIMITED  RETIRED
   └───────────────┘                 │
                                     └──► DORMANT (confidence interval too wide to act)
```

**The illegal transition is `ADDRESSED → RETIRED` on exposure.** This is where every
product will cheat, and the measurement that forbids it is the strongest single result
on explanation in the repository (§29 §3.3, Muller, N = 364, F(3,461) = 13.625,
p < .001, `MEASURED-RCT`):

| Condition | Content | Gain |
|---|---|---|
| Exposition | Clear, correct, 7:02 | 1.77 |
| Extended | Same, longer, 11:22 | 2.41 |
| **Refutation** | Exposition **verbatim + the misconception named**, 9:33 | **4.41** (d = 0.79) |
| **Dialogue** | Two speakers, one holding the misconception, 11:22 | **4.77** (d = 0.83) |

And in the same thesis: *"I learned something from the video"* scored **5.7 for Dialogue
against 5.6 for Exposition — flat**, while actual learning differed by d = 0.71.
Students found the better format **more dull** (p < .01) and said they would rather see
the worse one in lectures (p < .05).

> *"They believed they learned the same amount as students with double their learning
> gains. Thus the expositions actually strengthened misconceptions."*

**Therefore: delivering an explanation may never advance belief status.** Only unassisted
performance on unseen discriminating items at delay may. Self-report may never enter the
posterior at all — stated preference moves **d ≈ 0.48 while knowledge moves zero**
(Buljan et al. 2018, `10.1016/j.jclinepi.2017.12.003`, `MEASURED-RCT`), and simplification
*raises* confidence independent of competence with the bias **surviving explicit
debiasing** (Scharrer 2017; Salzmann 2025). A learner who has just watched a good
explanation is *more confident and therefore less likely to ask for the next rung*.
Preference-driven adaptation has a built-in downward ratchet.

---

## §2 — The elicitation loop

You cannot address a misconception you have not surfaced, and you have 15–40 seconds of
a learner's attention to surface it. `SPEC` throughout; grounding noted per rule.

### 2.1 The five rules

**E1 — Measure, never ask.** No self-report field may enter a posterior update. Stated
expertise, declared goal, "how well do you know this", and confidence sliders are all
inadmissible as evidence (F10 §12.1 R1, warrant above). They are admissible only as UI
navigation controls, and even then the system must be able to override them upward.

**E2 — The probe is `discriminate()`, not a quiz.** A probe item is generated by asking
for the item on which the candidate beliefs disagree most, and **every option is tagged
with the belief that predicts it**. This is exactly the FCI's design — "the instrument's
diagnostic power is entirely in its distractors", built from student interviews so each
wrong option corresponds to an identifiable Aristotelian or impetus-style belief
(Hestenes et al. 1992, `doi:10.1119/1.2343497`, `MEASURED-BENCH`) — and exactly the Eedi
corpus's shape. The generator is new; the item form is fifty years old.

**E3 — Commitment is mandatory.** The learner must submit an answer before anything is
revealed. The number: prequestion effect **g = 0.65 when participants guess** versus
**g = 0.22 when they do not**, *"amongst all of the moderator variables, prequestion
guessing had the strongest influence"* (N2 §3.2, `MEASURED-META`, 97 effect sizes). And
Muller again: *"students who witness demonstrations without being asked to make a
prediction perform as well on follow-up tests as those who don't see the demonstration
at all."* A demonstration without a preceding commitment is worth zero. This is a hard
gate in the sequence (§7 step 4), not a nudge.

**E4 — Probe for beliefs by *sign* and by *sort*, not by *value*.** A skill probe asks
for an answer. A belief probe asks for a direction or a category, which is where the
information is and which is an order of magnitude cheaper in seconds.

**E5 — Discriminability gate.** Reject any probe where two live beliefs induce the same
response distribution. A probe that costs 20 seconds of attention and moves no posterior
is worse than no probe, because attention is the scarcest input in the system. The
objective function is **expected information gain per second of learner attention** —
`bits/attention-second` — and it is what the probe selector maximises. `SPEC`.

### 2.2 Probe forms, by belief form

| Belief form | Probe form | Shape | Budget |
|---|---|---|---|
| `CAUSAL_SIGN` | `FORCED_CHOICE_SIGN` | "X increases. Y goes: up / down / unchanged." One item. | **8–12 s** |
| `ONTOLOGICAL_CATEGORY` | `SORT_CHECK` | "Which of these are sensible things to say? *A limit is fast. A limit is between 2 and 3. A limit takes four steps.*" Accepting rate-predicates on an object reveals the crossing. | **15–25 s** |
| `QUANTIFIER_ORDER` | `WITNESS_SELECT` | Give three candidate δ's; one works everywhere, one depends on x, one is wrong. The ∃δ∀ε holder picks the uniform one and rejects "it depends on x". | **25–40 s** |
| `PROCEDURAL_BUG` | `FIRST_STEP` | Kalyuga & Sweller rapid dynamic assessment: ask only for the **first step**, not the answer. Validated: higher knowledge *and* cognitive-efficiency gains under a yoked control (`10.1007/BF02504800`, `MEASURED-RCT`). | **10–20 s** |
| `SCOPE_OVERGENERALISATION` | `APPLICABILITY` | "Does the rule apply here? yes / no / not sure" across three cases, one outside the guard. | **20–30 s** |
| `DETERMINED_AS_TUNABLE` | `PREDICT_THEN_RUN` | "If we set Z to 3 instead, what changes?" The tunable-holder predicts a smooth change; the truth is inconsistency. Feeds directly into §5. | **15–25 s** |

The `SORT_CHECK` is the section's one genuinely new instrument and it matters
disproportionately: it is the only sub-30-second probe for the most robust error class
in the literature. `SPEC`.

### 2.3 The probe schema

```jsonc
{
  "probe_id": "probe:mech/impetus-01",
  "targets": ["belief:v1/mech/impetus-force-in-motion",
              "belief:v1/mech/force-proportional-to-velocity"],
  "form": "FORCED_CHOICE_SIGN",
  "budget_ms": 12000,
  "commit_required": true,               // E3. hard gate.
  "reveal_policy": "AFTER_COMMIT_ONLY",

  "stem": {"claim_ref":"claim:puck-on-ice","nl":"...","scene_ref":"scene:puck"},
  "options": [
    {"option_id":"A","nl":"...","predicted_by":["correct"]},
    {"option_id":"B","nl":"...","predicted_by":["belief:.../impetus-force-in-motion"]},
    {"option_id":"C","nl":"...","predicted_by":["belief:.../force-prop-to-velocity"]},
    {"option_id":"D","nl":"...","predicted_by":[]}    // untagged; must be < 25% of options
  ],

  "discriminability": {
    "expected_bits": 1.31,
    "min_pairwise_kl": 0.44,             // E5 gate: reject below 0.3
    "bits_per_attention_second": 0.109
  },
  "scoring": {"update":"bayes-multinomial","slip":0.08,"guess":0.25}
}
```

### 2.4 Cold start

Not a 30-item inventory. Three probes, ~90 seconds, selected greedily by
`bits_per_attention_second` from the domain library seeded with population priors. The
warrant for stopping at three: F10 §12.1 R4 — Tetzlaff et al., novices + assistance
**d = 0.505**, experts + assistance **d = −0.428**, and *"providing novices with
assistance has a stronger effect than withholding assistance from experts."* The cost of
under-shooting the entry rung is smaller than the cost of over-shooting, so under
uncertainty **enter one rung low and climb fast** rather than spending more attention on
diagnosis.

And per F10 R3: rung selection is **per prerequisite, not per learner** — compute the
mastery vector over the concept's prerequisite closure and set entry at the **weakest
link**, then ladder that prerequisite independently rather than dragging the whole
explanation down. The same person is ELI25 on linear algebra and ELI10 on measure theory.

---

## §3 — XIR, the explanation intermediate representation

This is the hardest and most valuable part of the document.

### 3.1 The requirement, and why a script fails it

XIR must be simultaneously:
1. **renderable to five surfaces** — animation, static figure, prose, interactive widget,
   spoken narration;
2. **checkable against the fidelity invariants before rendering**, without a learner and
   without an LLM judge;
3. **patchable mid-stream**, at three different latency budgets.

A script satisfies none of these. A scene graph satisfies (1) and neither of the others.
The settled answer from C1 — the LLM emits a small verifiable declarative IR, a
deterministic renderer draws — is correct and insufficient, because it is an IR for
*figures*. An explanation has discourse structure, a target belief, and a rung. The
figure IR is one layer of three.

### 3.2 Three layers, separated on the ALGOGEN line

ALGOGEN's causal claim is the design warrant, verbatim: end-to-end generation *"requires
the system to simultaneously simulate algorithm flow and satisfy video rendering
constraints, such as element layout and color schemes. **This complex task induces LLM
hallucinations**"* (arXiv:2605.12159, `MEASURED-BENCH`). The failure is **capacity
contention**. Splitting it moved 82.5% → 99.8%. XIR applies the same split twice.

```
  L_sem   — the claim graph.       WHAT IS TRUE.        Checked. Tens of nodes. No coordinates. No time.
    │
  L_plan  — the discourse plan.    WHAT IS SAID, IN WHAT ORDER, AGAINST WHICH BELIEF.
    │                              Beats, rungs, referential status, commitment slots.
  L_surf  — surface bindings.      WHICH RENDERER DRAWS WHICH CLAIM.
                                   Names claim_ids and object_ids only. NEVER coordinates.
```

C1 §4.3 states the non-negotiable: *"The model MUST NOT compute layout coordinates for
any figure that ships to a learner."* Nine independent groups, five domains, one
architecture, with the only clean ablation pointing the same way. XIR inherits this
as a schema-level prohibition: `L_surf` has no numeric position fields.

### 3.3 `L_sem` — the claim

```jsonc
{
  "claim_id": "claim:normalisation-is-intractable",
  "proposition": {
    "nl": "You can write the probability of any image up to a constant you cannot compute.",
    "formal": "p(x) = exp(-E(x)) / Z,  Z = ∫ exp(-E(x)) dx over all x"
  },

  // ── THE FOUR INVARIANTS, AS REQUIRED FIELDS ─────────────────────────
  // §25 / §29's fidelity rule. A rung may drop precision, formalism, or
  // mechanism-depth. It may NEVER falsify these four.
  "ontology": {
    "entity": "concept:partition-function",
    "category": "OBJECT",              // OBJECT|PROCESS|CONSTRAINT|SUBSTANCE|EMERGENT
    "predicates_used": ["is_equal_to","is_intractable"]
  },
  "causal": {
    "edges": [{"from":"var:dimension","to":"var:tractability","sign":"-",
               "kind":"CAUSAL","mechanism_unique": true}]
  },
  "quantifiers": {                     // null iff the claim is not quantified
    "prefix": "∀x ∃Z",
    "scope": "over the image space R^784",
    "entailed_by_formal": true         // set by V4, not by the author
  },
  "determinacy": {
    "constants": [{"sym":"Z","status":"DETERMINED_BY","by":"claim:normalisation"},
                  {"sym":"784","status":"ARBITRARY","note":"28x28 MNIST convention"}]
  },                                   // status ∈ DETERMINED_BY | FITTED | ARBITRARY
                                       // All three are fine. Not saying which is the violation.

  // ── LADDER POSITION ─────────────────────────────────────────────────
  "rung": 2,                           // 0=ELI10 ... 4=Research (F10 §10.3)
  "entailed_by": ["claim:normalisation@r3"],   // monotone refinement chain
  "drops_declared": ["ignores the continuous/discrete distinction — rung 3"],
  // Undeclared drops are illegal. F10 §11.4.

  // ── WHY THIS CLAIM IS IN THIS EXPLANATION ───────────────────────────
  "addresses": ["belief:v1/ebm/Z-is-a-hyperparameter"],
  "role": "OBSTACLE",
  //  OBSTACLE | NAMING | MACHINERY | CONSEQUENCE | SCOPE | CONTRAST
  //  NAMING is the beat that states the wrong idea aloud. See V6.

  "provenance": {"source_ref":"...","verified_by":"sympy:ebm-ref-v1"}
}
```

**`role: OBSTACLE` and the ordering it implies.** §29 §3.1 was corrected on this and the
correction is load-bearing: Muller's Refutation condition kept the definitions-first
order *verbatim* and simply stated the misconception aloud, scoring d = 0.79. **The
naming is the mechanism; the position is a preference.** So XIR *requires* a NAMING beat
(V6 below) and merely *prefers* obstacle-first ordering. Getting this backwards would
have made ordering a compile error, which the evidence does not support.

### 3.4 The verifier — five semantic passes and two structural

All seven run on `L_sem`/`L_plan` alone. **No learner. No LLM judge.** K2's numbers
forbid the LLM judge: selection *by test* **+8.14pp** versus LLM-judge **−3.20pp**
(`INTERNAL-PRIOR`), and step-level verification at chance (TutorGym). C1 adds the
false-positive direction: automated deception detectors *"frequently misclassify
non-misleading visualizations as deceptive"* — the error direction that makes a gate
unusable. So every pass below is **decidable**, not judged.

| Pass | Predicate | Decided by | Blocks render? |
|---|---|---|---|
| **V1 Monotone refinement** | Every claim at rung *n* is entailed by the rung *n+1* set under declared scope. Any sentence requiring the word "actually" at *n+1* is a violation | entailment check over the refinement chain (F10 §11.4) | **Yes** |
| **V2 Ontology sort-check** | Every predicate applied to an entity is well-formed for that entity's declared category | per-domain predicate×category table | **Yes** |
| **V3 Causal sign** | Every causal edge's sign matches the domain graph, or `kind` is `NONCAUSAL`. Unmarked direction fails | domain causal graph | **Yes** |
| **V4 Quantifier prefix** | The emitted prefix is entailed by the formal statement's prefix under declared scope | prefix comparison / Z3 | **Yes** |
| **V5 Determinacy labelling** | Every numeric constant carries `DETERMINED_BY`, `FITTED`, or `ARBITRARY`. **Missing label is the violation**, not any particular value | schema | **Yes** |
| **V6 Naming** | ≥1 beat with `role: NAMING` that states the targeted belief's content explicitly before it is refuted | structural | **Yes** |
| **V7 Referential status** | Every element declares a referent. `COMPETING_REFERENT` count must be 0; `NO_REFERENT` budgeted | structural | **Yes** for competing; warn for budget |

**V6 is the Muller result turned into a lint rule.** d = 0.79 for naming the
misconception, d = 0.83 for embodying it in a second speaker — the largest measured
effect on explanation in the corpus, and it is currently a matter of authorial taste
everywhere in the world. Here it is a compile error.

**V7 is N2's referential-status finding turned into a lint rule.** The measured ordering
(`MEASURED-META` throughout, N2 §1.3):

| The element's relation to the target | Effect | XIR enum |
|---|---|---|
| **Points at** the target (arrow, highlight, gesture) | **g = +0.43** [0.35, 0.50], k = 209 | `POINTS_AT_TARGET` |
| **Is** the target, dressed | **d+ = +0.33 to +0.39** | `IS_TARGET` |
| **Speaks about** it in second person ("your blood vessels") | **g = +0.33** [0.23, 0.44], k = 55 | `SECOND_PERSON` |
| **Moves but represents nothing** | **g = −0.05** [−0.17, 0.07] — *inert* | `NO_REFERENT` |
| **Carries a competing referent** | **g = −0.16 to −0.43** | `COMPETING_REFERENT` ⛔ |

The ordering is monotone in one variable only: *does the element have a referent, and is
that referent inside or outside the target schema?* A decorative border is maximally
extraneous, maximally persistent, and costs nothing — which is why "extraneousness" is
the wrong gate and referential status is the right one. XIR enforces the right one.

### 3.5 `L_plan` — the beat

```jsonc
{
  "beat_id": "beat:07",
  "role": "NAMING",
  "rung": 2,
  "targets_belief": "belief:v1/ebm/Z-is-a-hyperparameter",
  "claims": ["claim:normalisation-is-intractable"],
  "duration_ms_est": 14000,            // beats are 8-20s. See §4.3.
  "segmented_by": "SYSTEM",            // NEVER "LEARNER". Rey et al. 2019:
                                       // instructor-segmented g = 0.41 [0.32,0.50]
                                       // vs learner-segmented g = 0.20 [0.11,0.28], k=32 each
  "elements": [
    {"element_id":"e1","object_id":"obj:Z-symbol","referent":"IS_TARGET"},
    {"element_id":"e2","object_id":"obj:integral-sweep","referent":"POINTS_AT_TARGET"},
    {"element_id":"e3","kind":"ambient-music","referent":"NO_REFERENT","budget_charged":1}
  ],
  "commitment": {"probe_ref":"probe:ebm/Z-tunable-01","gate":"HARD"},
  "utterance": {
    "text":"People often think [ptr:obj:Z-symbol] this is something you pick. It isn't...",
    "deixis_anchors":[{"token_index":6,"object_id":"obj:Z-symbol","op":"point"}]
  },
  "patch_cache_ref": "cache:beat07"    // §4.4
}
```

### 3.6 `L_surf` — the surface bindings

One `L_sem` renders to all five surfaces. This is not a convenience; C1 §4.2 identifies
it as *"the only affordable way"* to serve a static PDF, a screen-reader page, and an
interactive widget from the same idea.

| Surface | Target | Tier (C1 §1.2) | Observed 2026-07-29 (GitHub API) |
|---|---|---|---|
| Animation | **Manim** via deterministic compiler | A (project IR → renderer) | `ManimCommunity/manim` 39,784★ MIT, pushed 2026-07-29 |
| Animation (web) | **Motion Canvas** | A | 18,859★ MIT, pushed **2026-07-02** — slower cadence; treat as secondary |
| Static figure | **Vega-Lite** / Graphviz-DOT | A / B | `vega/vega-lite` 5,425★ BSD-3, pushed 2026-07-29 |
| Interactive widget | **three.js** + symbolic dynamics | A (dynamics symbolic) | `mrdoob/three.js` 114,090★ MIT, pushed 2026-07-29 |
| Prose | templated from claims at the beat's rung | — | — |
| Narration | same text, TTS word-timed, deixis anchors inline | — | §6 |
| *Stage* (optional) | streamed video, **never the physics authority** | — | §4.2 |

**Prohibited targets:** raw SVG and raw D3 emitted by the model. C1 Tier D, and the
measurements behind it — VGBench's *"less desirable performance on low-level formats
(SVG)"*, VectorEdits' *"current methods struggle to produce accurate and valid"* edits.
Generating raw SVG for an educational figure is now a defect, not a choice.

### 3.7 The patch algebra

The reason for the three-layer split is that a revision is a **diff on `L_sem` or
`L_plan`**, never on pixels.

```jsonc
{
  "patch_id":"xp:0041","base_version":"xir:v7","ts":"...",
  "ops":[
    {"op":"annotate","target":"obj:Z-symbol","mark":"HIGHLIGHT"},
    {"op":"insert_beat","after":"beat:07","beat":{...}},
    {"op":"insert_probe","after":"beat:07","probe":{...}},
    {"op":"retarget","beat":"beat:08","addresses":["belief:.../Z-is-a-hyperparameter"]},
    {"op":"demote_rung","scope":["claim:..."],"from":3,"to":2},
    {"op":"replace_claim","claim_id":"claim:...","with":{...}},
    {"op":"run_forward","belief_id":"belief:...","surface":"widget"}    // §5
  ],
  "reverify":"SUBTREE",           // FULL | SUBTREE | NONE
  "render_class":"BRANCH"         // OVERLAY | BRANCH | RESTART
}
```

Two properties fall directly out of this schema and they are the whole of §4:

- **`annotate` is the only op with `reverify: NONE`.** It changes no claim, so no
  invariant can be falsified by it. It is therefore the only op that can legally land
  inside 200 ms.
- **Everything else requires re-verification**, and re-verification is what costs time.

The latency story is not a performance-engineering story. It is a **schema** story.

---

## §4 — Mid-stream revision

### 4.1 Three revision classes

`SPEC`. The mapping from `render_class` to budget is the operative design.

| Class | What changes | Re-verify | Budget | What it feels like | When |
|---|---|---|---|---|---|
| **OVERLAY** | `annotate` only. Highlight, trace, ghost, pair. Timeline continues, nothing restarts | NONE | **≤ 200 ms** | pointing | any time, including mid-utterance |
| **BRANCH** | `insert_beat` / `insert_probe` / `retarget` / `demote_rung`, applied at the **next beat boundary**. Current beat plays out | SUBTREE | **≤ 1,500 ms** — and the real budget is the remainder of the current beat, 8–20 s | the teacher taking a detour | on a wrong committed answer |
| **RESTART** | `replace_claim` at a rung root, or the target belief changing | FULL | **≤ 4,000 ms, and the learner is told** | *"wait — let me start this differently"* | posterior mass moves to a different belief |

**Never revise mid-beat except by OVERLAY.** The warrant is measured: Rey et al. 2019,
instructor-segmented **g = 0.41 [0.32, 0.50]** versus learner-segmented **g = 0.20 [0.11,
0.28]**, k = 32 each (N2). The system owns segmentation. A learner-interruptible timeline
measurably halves the segmentation benefit, so interruption is granted at boundaries the
system chose.

### 4.2 What is a legal trigger

The brief asks about gaze. The answer is that it is prohibited and the prohibition is
good design.

**PROHIBITED — do not build, in any jurisdiction, regardless of consent:**
webcam gaze, facial affect, voice affect, "attention tracking", any `emotional_state`,
`frustration`, `boredom`, or `engagement` field derived from biometric signal.
EU AI Act **Art. 5(1)(f)** prohibits *"the use of AI systems to infer emotions of a
natural person in the areas of workplace and education institutions"* `[VERBATIM]`, read
with Art. 3(39) and Art. 3(34) (biometric data includes *"physical, physiological or
behavioural characteristics... such as facial images"*). **Applicable since 2 February
2025.** COPPA independently classifies facial templates and voiceprints as children's
personal information (16 CFR 312.2). `STATUTE` (F8).

**LEGAL and admissible as evidence:**

1. **A committed response to a probe.** The primary signal. Behavioural, learner-initiated,
   explicit, and the only one that updates a posterior.
2. **A deictic act by the learner** — clicking, tapping, or circling an element and
   saying "this bit". Voluntary, intentional, and carrying strictly *more* information
   than gaze because it is chosen. **This is the substitution for gaze and it is a
   better signal, not a worse one.** `SPEC`.
3. **A learner-produced artifact** — a drawn diagram, a typed rule, a stated procedure.
   The highest-value input in the system because it is what §5 executes.
4. **Response latency on a committed item.** Admissible with a hard constraint: it may
   update a *knowledge* posterior; it may **never** populate an affect field; it may
   **never** be the sole trigger for an intervention. F8 flags the boundary as the
   sharpest open legal question in the area — whether clickstream is "behavioural
   characteristics" under Art. 3(34) — with no authoritative construction found.
   `STATUTE` + `INFERENCE`. Design so that losing this signal costs you nothing.
5. **An explicit "I'm lost" control.** Navigation, not evidence (rule E1).

**MEASURED AND REJECTED — rewind/replay density.** The obvious behavioural signal, and
N4 tested it and killed it: the signal was found, extracted, and measured, then found to
have *"already been built into an interface and evaluated (null), and the one study
testing backward-seeking against a learning outcome found the opposite sign."* Do not
use scrubbing behaviour as a confusion signal. `MEASURED` (N4 §3.6–3.7).

That leaves a short, clean, legal list: **committed answers, deictic acts, produced
artifacts.** Every one of them is a voluntary act. A system built on voluntary acts is
both lawful and better instrumented than one built on inference.

### 4.3 The latency budget

Substrate numbers, all measured:

| Quantity | Value | Source |
|---|---|---|
| Human modal floor-transfer offset | **100–200 ms**; 51–55% of all turn transitions under 200 ms | Levinson & Torreira 2015, `10.3389/fpsyg.2015.00731`, `MEASURED` |
| Full-duplex speech LM | **160 ms theoretical / 200 ms practical** | Moshi, arXiv:2410.00037, `MEASURED` |
| Real-time streamed visual substrate | **640×368 @ 25 FPS, ~200 ms model-side**, ~550 ms total remote incl. 350 ms network | Wan-Streamer v0.2/v0.3, arXiv:2607.04443 (verified 2026-07-29), `MEASURED-BENCH` author-reported |
| Frame budget at 25 FPS | **40 ms** | arithmetic |
| Default hosted VAD | **500 ms silence + 300 ms prefix = 800 ms before the model works** | A4 §7.2, `[DOCUMENTED]` |
| Deixis synchronisation target | **≤ 200 ms** of the referring utterance | F9 OP-8 arm A spec |

**The overlay path, and the constraint that makes it possible.** `SPEC`:

```
learner clicks an element / submits a committed option
  → input event to local orchestrator                          2–10 ms
  → posterior update, closed-form Bayes over ≤ 40 beliefs      < 5 ms
  → policy: table lookup, response → patch class               < 5 ms
  → emit annotate op from the precompiled patch cache          < 5 ms
  → renderer applies annotation on the next frame             ≤ 40 ms   (25 FPS)
  ────────────────────────────────────────────────────────────────────
  perceived                                                ≈ 60–100 ms   ✓
```

> **No language model may sit on the overlay path.** The overlay path is arithmetic over
> a precompiled table. This is the single constraint that makes a 200 ms claim
> survivable, and it is why the belief posterior is a closed-form Bayes update over an
> enumerated library rather than a model call.

The LM sits on the BRANCH path (≤1.5 s, and really the 8–20 s remainder of the current
beat) and the RESTART path (≤4 s, announced). Both are far outside any turn-taking
constraint, and A4 §7.4 notes the pedagogical wrinkle that makes this comfortable: a
tutor is one context where a longer gap is *defensible* — marked silence in tutoring is
often correct (wait time). The design goal is **controllable** latency, not minimal.

### 4.4 The patch cache — the thing that makes branching real

At plan time, for every beat, the compiler pre-generates and **pre-verifies** the *k*
most likely patches given the active belief set. Each beat's probe has ≤4 options; each
option is tagged with the belief that predicts it; each tagged belief has one precompiled
OVERLAY and one precompiled BRANCH. The cache for beat *n+1* is built during beat *n* —
8 to 20 seconds of wall clock, which is generous.

A wrong answer at beat 7 therefore hits a branch that is already generated, already
passed V1–V7, and already rendered to a keyframe. This is speculative execution applied
to explanation. `SPEC`. It is also the answer to "what does a *partial* re-render look
like": you do not re-render, you **switch to a pre-rendered branch and cross-fade at a
system-chosen boundary**, with an overlay covering the sub-200 ms acknowledgement so the
learner never perceives the gap.

Restart is the only class that renders cold, it is rare by construction, and the learner
is told it is happening. Announcing it is not an apology — a tutor who says *"wait, let
me start this differently"* is doing the thing that makes the revision legible.

---

## §5 — Running the learner's own wrong model forward

The strongest move available and nobody has built it.

### 5.1 Why it should beat assertion

Muller's ranking is the warrant and it points precisely here. Exposition: gain 1.77.
Naming the misconception: 4.41, d = 0.79. **Two speakers, one holding the misconception:
4.77, d = 0.83** — the highest condition in the experiment. `MEASURED-RCT`.

Executing the learner's own rule until it fails is the Dialogue condition, mechanised:
the second speaker is the learner's belief, running. And the world delivers the
disconfirmation rather than the tutor asserting it, which removes the one thing an
exposition cannot remove — the learner's option to file the correct account alongside
the wrong one and keep both. `SPEC`, as an extension of a `MEASURED-RCT`.

The sequence is forced and non-negotiable, because of the other Muller result:
*"students who witness demonstrations without being asked to make a prediction perform as
well on follow-up tests as those who don't see the demonstration at all."*

```
probe → COMMIT (hard gate) → instantiate learner's rule → run both → diverge on screen
```

Running the model before the commitment is worth zero. This is why `commitment.gate` in
§3.5 is `HARD` and why the runtime refuses a `run_forward` op with no preceding commit in
the same beat.

### 5.2 The sandbox, in two tiers

**Tier 1 — a total DSL, and this is the default.** Most beliefs are not programs. They
are signed graphs, mutated finite procedures, guarded rules, and quantifier prefixes. A
small **total** interpreter you wrote — arithmetic, signed causal graphs, finite-state
procedures, guard predicates — with no I/O, no loops without bounds, and guaranteed
termination. Covers `PROCEDURAL_BUG`, `CAUSAL_SIGN`, `SCOPE_OVERGENERALISATION`,
`DETERMINED_AS_TUNABLE`. No sandbox escape surface because there is no general
computation. **Build this tier and stop.**

**Tier 2 — real code**, only when the belief genuinely is a program (a physics update
loop, an algorithm implementation the learner wrote). Treat as hostile: the source is
model-authored from a learner's stated rule, which is the worst provenance in the
building.

| Concern | Choice | Observed 2026-07-29 |
|---|---|---|
| Python in-browser | **Pyodide** in a Web Worker | `pyodide/pyodide` 14,760★ MPL-2.0, pushed 2026-07-29 |
| JS, embeddable | **QuickJS** compiled to WASM | `bellard/quickjs` 10,873★, pushed 2026-06-16 |
| Server-side | **Deno** with `--deny-net --deny-read --deny-write` | `denoland/deno` 107,847★ MIT, pushed 2026-07-29 |
| Limits | 250 ms CPU, 64 MB heap, fuel-metered step budget, fixed RNG seed, no clock | `SPEC` |

**The reference model is never the language model's opinion.** It is a verified engine:
SymPy for symbolic (`sympy/sympy` 14,811★, pushed 2026-07-27), Z3 for constraint and
quantifier claims (`Z3Prover/z3` 12,499★, pushed 2026-07-29), or a real physics engine.

This is A5's conclusion applied: *"Keep the world generative; keep the physics
symbolic."* You never ask a generative model for the dynamics, because the dynamics are
measured at **39.6%** prompt-and-physics adherence at best and **22%** on the hard subset,
with no ground truth, no reference implementation, no test suite, and no way for a
14-year-old to know that the pendulum they just watched had the wrong period.

### 5.3 What each belief form gives you

| Form | `break()` available? | Mechanism |
|---|---|---|
| `PROCEDURAL_BUG` | **Yes, directly** | Run the mutated procedure on inputs; the learner's own arithmetic disagrees with itself |
| `SCOPE_OVERGENERALISATION` | **Yes** | Search the complement of the dropped guard; nearly always succeeds fast |
| `CAUSAL_SIGN` | **Yes** | Run the intervention in the reference engine; the sign is visible |
| `DETERMINED_AS_TUNABLE` | **Yes, and most dramatic** | Hand the learner the knob. The system is over-determined; the solver returns **UNSAT**. Showing UNSAT is showing that the choice was never available |
| `QUANTIFIER_ORDER` | **Partly — search, not execution** | Ask Z3 for a witness under the learner's prefix on a pointwise-but-not-uniform case. It returns UNSAT. **The counterexample is the explanation** |
| `RELATIONAL_ORDER_COLLAPSE` | No | Not a domain error; constrains rung selection instead |
| `ONTOLOGICAL_CATEGORY` | **No** | See §5.4 |

### 5.4 The honest hole: you cannot run a category error

There is no dynamics in a category error, so there is nothing to run forward. And this is
the class the literature says is most robust — the Bohr-model hybrid population
**unchanged across a full semester** (§25).

The strongest move in the system does not apply to its hardest case. State it plainly
rather than pretending otherwise.

What is available instead, and it is weaker: run *both* categories' consequences on the
same entity, side by side, and show that they license **different valid questions**.
"Is the limit fast?" is well-formed under PROCESS and nonsense under OBJECT; "is the
limit an element of this set?" is the reverse. You are not disconfirming; you are making
a sort-check visible. `SPEC`, and it should be measured separately because there is no
reason to assume it inherits Muller's effect size.

### 5.5 When the wrong model doesn't break

The case the brief asks about, and the most important paragraph in §5. Three sub-cases
with three different correct actions, and the schema must distinguish them because
conflating them is how this system becomes a liar.

**(a) It doesn't break on the cases you searched, but it does break somewhere.**
A tractability failure, not a truth. Correct action: escalate the search from sampling to
solving — ask Z3/SymPy for a *disagreement witness* between the learner's rule and the
reference rather than enumerating cases. If that also fails, escalate to (b) or (c).
**Never fabricate a break.** A legible, confidently rendered, wrong disconfirmation is
the worst output this system can produce: it is C1's Mirage failure (*"high Normal-mode
accuracy is largely a Mirage"*) combined with A5's observation that fidelity decouples
from correctness and **realism is the cue learners use to decide whether to trust what
they see.** `break()` returns `⊥` and the runtime falls back to NAMING. It does not
improvise.

**(b) It doesn't break within the declared scope, and that is correct.**
The learner's model is a **legal lower rung**. Newtonian mechanics does not break at
3 m/s. Impetus theory gets most everyday cases right. Correct action: **do not attempt to
disconfirm.** Move status to `SCOPE_LIMITED`, state the envelope out loud, and ladder.
F10 §11.4's rule applies exactly: undeclared drops are the violation; a declared drop
("this holds when there's no friction — the friction case is rung 3") is legal and is
what an honest rung looks like. Attempting to break a model inside its domain of validity
teaches the learner that the tutor is arguing rather than showing, which is the failure
mode that makes students distrust demonstrations. This is why `validity_envelope` is a
**required** field in §1.3 and not an optional annotation.

**(c) It doesn't break because it is empirically equivalent on everything reachable.**
A sign convention. An isomorphic formulation. A different but valid decomposition.
Correct action: **retire it as `NOT_A_MISCONCEPTION`** and write it to a per-domain
`false_positive_registry`.

This third path is the only mechanism that stops the system manufacturing errors, and it
is not optional. The relevant measurements: TutorGym says the model's error-labelling is
at chance; C1 says automated checkers *"frequently misclassify non-misleading
visualizations as deceptive"*, and the false-positive direction is the one that makes a
gate unusable. A system that confidently refutes a learner who was right is worse than a
pre-rendered video in every respect. The `false_positive_registry` is the calibration
loop for the belief library and its growth rate is a top-line health metric (§9).

---

## §6 — Deixis in a live artifact

F9 OP-8 states the gap: nobody has built a tutoring system in which the AI points at a
specific element of a shared visual field while talking about it, and nobody has measured
what it does to learning. The census is stark — arXiv `abs:"deictic" AND abs:"tutor"`
→ **0**; GitHub `AI tutor whiteboard pointing` → **0 repos**. `OBSERVED — absence`.
*"This is the clearest case in the survey of a capability gap that is purely one of
assembly."*

### 6.1 The insight that collapses the hard problem

The closest existing work treats visual explanation in geometry as **referring-image
segmentation**: 200,000+ synthetic diagrams with pixel-perfect masks, fine-tuned
Florence-2 at **49% IoU / 85% buffered IoU** against **< 1% zero-shot**
(arXiv:2604.02893, verified 2026-07-29, `MEASURED-BENCH`).

**49% IoU is the number for recovering referents from an image you did not author. If the
renderer draws from XIR, it already knows where every object is, exactly.** Grounding
accuracy on system-authored content is 100% by construction, and no vision model is
involved.

The grounding problem exists only because people have been pointing at images they did
not generate. That is the assembly nobody has done. `SPEC`.

Three deixis channels, with three very different accuracies:

| Channel | Mechanism | Accuracy |
|---|---|---|
| **Tutor → learner** (system points at its own artifact) | scene graph lookup by `object_id` | **exact, by construction** |
| **Learner → tutor** (learner points at the system's artifact) | hit-test click/touch against the scene graph | **exact, free** |
| **Learner's own artifact** (their handwriting, their drawing) | vision grounding | **49% IoU / 85% buffered** — and that is on *synthetic* diagrams, not the messy, partially-occluded artifacts learners actually produce |

Only the third needs a model, and it needs a confirmation step: *"this one?"* with a
highlight, before any action is taken on a low-confidence ground.

### 6.2 What the renderer must expose

```jsonc
// Emitted by every renderer, every frame, for every surface. SPEC.
{
  "frame_index": 4127, "t_ms": 165080, "surface": "animation",
  "objects": [
    {
      "object_id": "obj:Z-symbol",          // assigned at IR COMPILE TIME, not recovered
      "claim_refs": ["claim:normalisation-is-intractable"],
      "bbox": [412, 233, 48, 61],
      "mask_ref": "rle:...",                // optional; bbox sufficient for most marks
      "z": 3, "visible": true,
      "semantic_role": "SYMBOL",            // SYMBOL|AXIS|CURVE|REGION|LABEL|ACTOR|TRACE
      "belief_ghost_of": null               // set when this object is the learner's model's version
    }
  ],
  "id_stability": "STABLE_ACROSS_BEAT_AND_NON_DELETING_PATCH"
}
```

`id_stability` is the load-bearing contract. An `object_id` must survive a patch that
does not delete the object, or every overlay op breaks at exactly the moment revision
happens — which is the only moment that matters.

### 6.3 The tutor's address surface

Five ops. All are `annotate`. All are `reverify: NONE`. All therefore land on the
≤200 ms overlay path, which closes the loop with §4.

| Op | Meaning |
|---|---|
| `point(object_id, style)` | highlight / arrow / halo — the **g = +0.43** row of N2's table, k = 209 |
| `trace(path_id, t0..t1)` | draw along a trajectory over time |
| `ghost(object_id)` | render the **learner's model's** version of this object, faded, alongside the correct one — the §5 divergence, as a mark |
| `pair(a, b)` | show a correspondence between two objects |
| `frame(region_of(claim_id))` | enclose everything bound to a claim |

`ghost()` is the one that only exists because of §1 and §5: you cannot render the
learner's model's version of an object unless you have executed the learner's model. It
is the visual form of the Dialogue condition.

### 6.4 Synchronisation

Utterances carry deixis anchors inline, at token positions:

```
"look at [ptr:obj_17] this term — the one that [ptr:obj_23] disappears when you differentiate"
```

TTS emits word timings; the annotate op fires at the anchor token's **word onset**,
target ≤200 ms, per F9's arm-A specification. F9 is explicit that **a pointer that lags
the speech is worse than no pointer**, so the runtime pre-schedules the annotate ops
against the TTS timing rather than reacting to audio playback.

---

## §7 — The loop, as a sequence

One concept, one learner, ~6 minutes. Times are targets. `SPEC`.

| # | Step | Actor | Budget |
|---|---|---|---|
| 1 | Compute mastery vector over the concept's prerequisite closure; entry rung = weakest link, minus one (F10 R3, R4) | orchestrator | 50 ms |
| 2 | Select ≤3 probes by greedy `bits_per_attention_second` from the domain belief library, seeded with population priors | probe selector | 100 ms |
| 3 | Render probe 1 | renderer | — |
| 4 | **Learner commits.** Hard gate — nothing is revealed before submission | learner | 8–40 s |
| 5 | Closed-form Bayes update over the belief set. Argmax `predict()` over enumerated beliefs. *No model call.* | orchestrator | < 5 ms |
| 6 | Repeat 3–5 for probes 2–3 | | ~90 s total |
| 7 | Emit target belief set. Generate `L_sem` + `L_plan` against it, at the entry rung | generator (LM) | 3–8 s |
| 8 | **Run V1–V7.** Any block → regenerate, max 3 attempts, then fall back to the library's canned rung | verifier | 200–600 ms |
| 9 | Bind `L_surf`; compile; render beat 1; **build the patch cache for beat 2** | renderer | 1–3 s |
| 10 | Play beat *n*. Deixis anchors fire on word onsets, ≤200 ms | renderer | 8–20 s |
| 11 | Any learner deictic act → **OVERLAY** from cache | orchestrator | **60–100 ms** |
| 12 | Beat carries a commitment → learner commits → posterior update → if a rival belief takes mass, **BRANCH** from cache at the boundary | orchestrator | ≤1.5 s, hidden inside the beat |
| 13 | Where the target belief supports it: **`break()`** — instantiate the learner's rule, run both, `ghost()` the divergence | sandbox + renderer | 200 ms–2 s |
| 14 | If posterior mass moves to a belief the plan does not address: **RESTART**, announced | orchestrator | ≤4 s |
| 15 | On completion, status → `ADDRESSED`. **Not** `RETIRED` | belief store | — |
| 16 | At ≥7 days, serve *k*=3 unseen items from `discriminate()`, no assistance. Only this can retire the belief | scheduler | — |

Steps 5 and 11 contain no model call. That is the design.

---

## §8 — Build order

What to build first, what it unblocks, and what is throwaway.

**1 · The belief library and `predict()`, for one domain.** ~40 beliefs, hand-curated,
each with a form, a payload, a Tier-1 executable, a validity envelope, and population
priors. Start where labelled data already exists: the Eedi/NeurIPS-2020 corpus (>20M
misconception-labelled answers) or FCI-covered mechanics.
*Unblocks:* everything. *Throwaway:* nothing. *Estimate:* 2 engineers + 1 domain expert,
6 weeks per domain. The per-domain cost is the honest price of this architecture and it
does not go away.

**2 · The probe generator and the discriminability gate.** `discriminate()` over the
library, greedy selection by `bits_per_attention_second`.
*Unblocks:* all measurement. **Ship this alone as a 90-second diagnostic before building
any rendering at all** — it validates the library against real learners, and if the
library's `predict()` accuracy is at chance on real responses, the entire thesis is dead
and you have spent three months instead of two years finding out.
*Throwaway:* nothing.

**3 · `L_sem` plus verifier passes V1–V7. No renderer.** Run it offline against N4's
atlas of existing explanations. **The gate must reproduce known-bad explanations as
failures before it is allowed to gate generation.** Calibrate the false-positive rate
first — C1's warning about detectors that misclassify non-misleading artifacts as
deceptive applies directly, and an over-firing verifier makes generation impossible.
*Unblocks:* trustworthy generation. *Throwaway:* nothing; this outlives every renderer.

**4 · One renderer, static only.** Vega-Lite or Manim, still frames. Proves that one
`L_sem` renders to two surfaces.
*Unblocks:* multi-surface, accessibility, print. *Throwaway:* the `L_surf` bindings —
assume they are rewritten.

**5 · Patch algebra, patch cache, and the overlay path.** No LM in the loop. This is
where the ~200 ms claim is either true or not.
*Unblocks:* the whole mid-stream thesis. *Throwaway:* nothing.

**6 · `break()` Tier 1** — the total DSL interpreter. Deliberately before Tier 2, and
possibly instead of it.
*Unblocks:* the highest-value move. *Throwaway:* nothing.

**7 · Deixis from the scene graph.** Nearly free once 4 and 5 exist: the object IDs
already exist, the annotate op already exists, the overlay path already exists. F9 ranks
this first in the substrate build order for good reason; it is listed seventh here only
because it is *cheap once the IR exists*, not because it is low value.
*Unblocks:* the F9 OP-8 experiment, which is the cheapest publishable result in this
whole programme.

**8 · The live streamed surface. Last, optional, and behind an interface.**
The video substrate will be replaced within 18 months and the evidence is in the repo
list: `cumulo-autumn/StreamDiffusion` has 10,791★ and has not been pushed since
**2024-12-04**; `chenfengxu714/StreamDiffusionV2` (530★, Apache-2.0) was pushed
2026-07-10; Wan-Streamer is a third lineage again. `OBSERVED`, GitHub API 2026-07-29.
Build nothing above it that is not behind an interface, and never let it own dynamics.

**Explicit throwaway list.** The `L_surf` bindings. The video substrate integration. All
prompt engineering for the generator (replaced by fine-tuning on the IR once the IR is
stable). The cold-start heuristics. Budget for these to be discarded and do not let
anyone defend them.

---

## §9 — The falsifiable claim

### 9.1 The design

Three arms, and the control discipline is the part that matters: **the pre-rendered arm
must be informationally equivalent** — it plays the union of everything the adaptive arm
could have shown, in a fixed order, with the same production quality. Not a weaker
video. F9 names this discipline as the thing this literature has never adopted.

- **A — Responsive.** Probe → belief → generated XIR → mid-stream revision → `break()`.
- **B — Fixed-best.** The same XIR compiled to one linear render. Verified identical on
  `L_sem`. Includes the NAMING beat, so this is not a re-test of Muller's d = 0.79. No
  probe-driven branching.
- **C — Fixed-generic.** A good pre-rendered explanation not targeted at any belief —
  the status quo; a top explanation drawn from N4's atlas.

**Primary outcome:** delayed unassisted transfer at **14 days** on novel items, plus
**belief retirement rate** measured on discriminating items the learner has never seen.
**Secondary:** referential repair rate (how often the learner asks "which one?");
time-to-criterion; seconds of attention spent on probes; `false_positive_registry` growth.

**Population and N.** Following F9's convention: 200/arm detects d = 0.28, and ANCOVA on
a prior-knowledge pre-test brings it to d ≈ 0.22. The subgroup analysis is the claim, so
enrol ~250/arm and screen for belief-holding at entry. FCI-class prevalence is high, so
expect ~60% holders — roughly **N = 750 enrolled, ~450 belief-holders**.

### 9.2 The prediction, stated so it can fail

> **A > B on 14-day transfer at d ≈ 0.35–0.5, among learners who entered holding a
> targeted belief — and A ≈ B among learners who did not.**

The heterogeneity *is* the claim. **If A beats B uniformly, the mechanism is not
targeting — it is production quality, and you have built an expensive video pipeline.**

### 9.3 The two falsifiers

**Falsifier 1 (the thesis).** A ≈ B on transfer among belief-holders. This would mean the
addressing is decorative and the correct product is a well-curated static explanation
library plus a good router — a far cheaper thing to build, and the honest answer if the
data says so.

**Falsifier 2 (mid-stream specifically), and this is the one nobody will want to run.**
Add **A′**: identical content, identical targeting, identical `break()` — but all
revision **deferred to the end** and delivered as a follow-up segment rather than an
interruption. If **A ≈ A′**, then mid-stream revision is theatre and the whole latency
budget in §4 is unnecessary engineering. Live revision would then be a demo property, not
a learning mechanism.

Run A′. It is the cheapest arm in the study and it threatens the most expensive component
in the system, which is exactly why it belongs in the pre-registration rather than in a
follow-up nobody funds.

---

## §10 — Limitations

**1 · The belief library is hand-built and per-domain.** Eedi covers school maths; the
FCI covers mechanics; almost nothing else is covered. Six weeks per domain is the price,
it does not amortise across domains, and it is the reason this architecture is a product
decision rather than a research one. Watch: cost per domain over the first three domains.
If it is not falling, the approach does not scale.

**2 · `break()` does not apply to the class that needs it most.** Ontological crossings
are the most robust misconceptions measured (unchanged across a semester) and there is no
dynamics to run. §5.4's substitute is untested and should not be assumed to inherit
Muller's effect size.

**3 · The pretty parts and the true parts are made by different machinery.** Keeping
dynamics symbolic routes around the 39.6%/22% physics problem, but it introduces a
desynchronisation risk: a rendered animation whose motion does not match the symbolic
trace it claims to depict. Add a hard check — **`L_surf` motion must be *sampled from*
the symbolic trace, never generated alongside it** — and watch for any code path that
lets a generative surface produce motion independently.

**4 · The 200 ms substrate figure is author-reported on one system.** Wan-Streamer
v0.2/v0.3's 640×368 @ 25 FPS / ~200 ms model-side is `MEASURED-BENCH` but self-reported,
and A4 records that neither hosted vendor publishes an end-to-end latency figure at all.
Measure it locally before committing to the overlay budget. The architecture survives a
2× miss (the overlay path is ~60–100 ms of its own arithmetic); it does not survive a
10× miss.

---

## Sources

**Verified in this session (2026-07-29).** arXiv abstract pages fetched directly:
2505.01563 (*TutorGym*), 2604.02893 (*Toward an Artificial General Teacher*), 2607.04443
(*Wan-Streamer v0.2*), 2511.07399 (*StreamDiffusionV2*), 2605.12159 (*ALGOGEN*).
Crossref: `10.1007/978-3-662-03037-0_7`, Ohlsson, *Constraint-Based Student Modeling*
(1994) — the tradition this document's Belief Object departs from.

**GitHub API, 2026-07-29, `OBSERVED`.** `ManimCommunity/manim` 39,784★ MIT pushed
2026-07-29 · `motion-canvas/motion-canvas` 18,859★ MIT pushed 2026-07-02 ·
`mrdoob/three.js` 114,090★ MIT pushed 2026-07-29 · `vega/vega-lite` 5,425★ BSD-3 pushed
2026-07-29 · `vega/vega` 11,943★ pushed 2026-07-29 · `remotion-dev/remotion` 54,824★
pushed 2026-07-29 · `pyodide/pyodide` 14,760★ MPL-2.0 pushed 2026-07-29 ·
`bellard/quickjs` 10,873★ pushed 2026-06-16 · `denoland/deno` 107,847★ MIT pushed
2026-07-29 · `sympy/sympy` 14,811★ pushed 2026-07-27 · `Z3Prover/z3` 12,499★ pushed
2026-07-29 · `chenfengxu714/StreamDiffusionV2` 530★ Apache-2.0 pushed 2026-07-10 ·
`cumulo-autumn/StreamDiffusion` 10,791★ Apache-2.0 **pushed 2024-12-04** (stale).

**Load-bearing measured claims, carried from the repository with their labels.**
Muller (2008), refutation d = 0.79 / dialogue d = 0.83, N = 364, and the felt/real
dissociation (5.7 vs 5.6 flat while learning differed d = 0.71) — §29 §3.3,
`MEASURED-RCT` · TutorGym, 223 domains, no LLM above chance at labelling an incorrect
student action, arXiv:2505.01563, `MEASURED-BENCH` · ALGOGEN 82.5% → 99.8%,
arXiv:2605.12159, `MEASURED-BENCH` · VideoPhy best model 39.6%, VideoPhy-2 22% hard
subset, arXiv:2406.03520 / 2503.06800, `MEASURED-BENCH` · Levinson & Torreira (2015),
modal FTO 100–200 ms, `10.3389/fpsyg.2015.00731`, `MEASURED` · Moshi 160/200 ms,
arXiv:2410.00037, `MEASURED` · Wan-Streamer v0.2/v0.3, 640×368 @ 25 FPS, ~200 ms
model-side, arXiv:2607.04443, `MEASURED-BENCH` (author-reported) · Geometry visual
grounding 49% IoU / 85% buffered vs <1% zero-shot, arXiv:2604.02893, `MEASURED-BENCH` ·
Schneider et al. 2018 signalling g = +0.43 [0.35, 0.50] k = 209; Höffler & Leutner 2007
decorative animation g = −0.05 [−0.17, 0.07]; Sundararajan & Adesope 2020 seductive
details to g = −0.43 — N2 §1.3, `MEASURED-META` · Prequestion guessing g = 0.65 vs
g = 0.22 — N2 §3.2, `MEASURED-META` · Rey et al. 2019 instructor-segmented g = 0.41 vs
learner-segmented g = 0.20, k = 32 each, `MEASURED-META` · Buljan et al. 2018,
preference d ≈ 0.48 / knowledge zero, `10.1016/j.jclinepi.2017.12.003`, `MEASURED-RCT` ·
Tetzlaff et al., novices + assistance d = 0.505, experts d = −0.428 — F10 §12.1 ·
Kalyuga & Sweller rapid dynamic assessment, `10.1007/BF02504800`, `MEASURED-RCT` ·
Brown & Burton (1978), `doi:10.1207/s15516709cog0202_4`; Brown & VanLehn repair theory,
`doi:10.1016/B978-1-4832-1446-7.50031-5` · Hestenes et al. FCI (1992),
`doi:10.1119/1.2343497`, `MEASURED-BENCH` · Eedi/NeurIPS-2020 >20M misconception-labelled
answers, arXiv:2007.12061, `MEASURED-BENCH` · Chi's ontological crossing, Bohr-hybrid
population unchanged across a semester — §25 · Quantifier-prefix check fired zero times
on 1,524 transcript sentences — §29, C-50 · N4 §3.6–3.7, rewind/replay density null and
opposite-signed · EU AI Act Art. 5(1)(f) with Art. 3(34) and 3(39), applicable
2 Feb 2025; 16 CFR 312.2 — F8, `STATUTE`.

**Internal sections this document assembles.** `A4-live-multimodal` · `A5-world-models` ·
`C1-illustration-generation` · `F5-learner-model` (PLM §8.2) · `F8-safety-privacy-children`
· `F9-open-problems` (OP-8) · `F10-explanation-laddering` · `K2-agentic-frontier` ·
`N2-executive-function-and-attention` · `N4-explanation-atlas` ·
`survey/25-the-ladder-of-explanation` · `survey/29-explaining-hard-things` ·
`survey/00-north-star-jarvis` §7.

**Everything marked `SPEC` is designed in this document and measured nowhere:** the
Belief Object and its `predict`/`discriminate`/`break` interface; the two-clock decay
model; the status machine and the illegal exposure→retirement transition; the
`SORT_CHECK` probe; `bits_per_attention_second`; XIR's three layers, patch algebra, and
verifier passes V1–V7; the patch cache and the no-LM-on-the-overlay-path constraint; the
three revision classes; the two-tier `break()` sandbox and its three no-break cases;
compile-time object IDs for exact deixis; and the build order.
