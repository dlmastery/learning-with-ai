---
title: "The L0–L4 grounding ladder for a universal expert AI mentor"
wave: G
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 20
---

# G1 — The Grounding Ladder

## Executive finding

A frontier model can explain almost anything. An expert mentor must also know
**what permits it to make each claim**.

As of July 2026, the implementation pieces are mature enough to make grounding
an explicit runtime contract:

- current search tools return claim-linked citation annotations;
- file and URL tools can limit answers to approved curriculum;
- code execution and function calls can check calculations and constraints;
- formal systems can verify proof objects with a small independent kernel;
- content-provenance standards can preserve how a visual or document was made;
- multi-agent tutoring systems can separate generation, retrieval, verification,
  and teaching policy.

The proposed standard assigns every substantive mentor claim a **required
grounding tier** and an **achieved grounding tier**:

| Tier | Name | What permits the claim |
|---|---|---|
| L0 | Visibly generated | It is clearly presented as invented, illustrative, or exploratory |
| L1 | Source-attested | A claim-level span in an appropriate, versioned source supports it |
| L2 | Tool-checked | A deterministic or independently checkable tool validates it |
| L3 | Measurement-checked | Data, experiment, sensor, or validated simulation supports it |
| L4 | Human-authorized | A named accountable human makes the consequential decision |

This is not a ranking of intelligence. It is a routing system. A metaphor belongs
at L0; a historical date at L1; an arithmetic result at L2; a claim about a
physical system at L3; and a safeguarding or credential decision at L4.

The rule is:

> If the achieved tier is lower than the required tier, the mentor retrieves,
> calls a tool, measures, escalates, or says “not yet verified.” It does not
> silently lower the standard.

---

## 1. Why “the answer has citations” is not enough

Grounding combines several distinct questions:

1. **Existence:** does the cited source or tool result exist?
2. **Entailment:** does it support this exact claim?
3. **Authority:** is it appropriate for this domain and decision?
4. **Currency:** is it still valid for the relevant date and version?
5. **Scope:** does the claim stay inside the evidence’s population, conditions,
   units, and assumptions?
6. **Provenance:** can a reviewer reconstruct how the answer or artifact was
   produced?
7. **Authorization:** who is accountable when evidence does not determine the
   decision?

The July 2026 Gemini Interactions API can automatically search and return inline
`url_citation` annotations tied to text spans. Its URL-context and file-search
tools can combine public search with specified material. OpenAI deep research
can restrict browsing to selected trusted sites and produces documented
reports. Anthropic exposes source citations and search-result provenance.
`VENDOR`

These are major capability gains. They solve citation transport, not the full
epistemic problem. A URL can exist and still be weak, obsolete, mis-scoped, or
misread. The mentor must store the evidence decision, not merely render a
superscript.

Sources:

- [Gemini grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search)
- [Gemini tools](https://ai.google.dev/gemini-api/docs/tools)
- [Gemini URL context](https://ai.google.dev/gemini-api/docs/url-context)
- [OpenAI deep research, 2026 update](https://openai.com/index/introducing-deep-research/)
- [OpenAI Academy: research with citations](https://openai.com/academy/search-and-deep-research/)
- [Anthropic citations](https://docs.anthropic.com/en/docs/build-with-claude/citations)
- [Anthropic web search tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool)

---

## 2. L0 — visibly generated

### Appropriate claims

- invented stories and characters;
- metaphors and analogies;
- hypothetical scenarios;
- candidate explanations;
- unvalidated practice variants;
- brainstorming and speculative design.

### Required record

- generation label;
- model and policy version;
- prompt or transformation lineage when relevant;
- content credential for distributable media;
- any source ingredients used.

### Release rule

L0 material may be vivid and useful. It may not be presented as observed fact,
authentic historical evidence, a real quotation, a validated assessment item,
or an accurate scientific world.

C2PA 2.4 provides a current interoperable mechanism for recording the origin
and edit history of images, audio, video, and documents. It makes provenance
tamper-evident; by design, it does **not** determine whether the underlying
content is true. That distinction maps exactly to L0: preserve how the artifact
was generated, then separately validate any factual claims inside it.

Sources:

- [C2PA specifications 2.4](https://spec.c2pa.org/specifications/)
- [C2PA Content Credentials explainer](https://c2pa.org/specifications/specifications/2.2/explainer/Explainer.html)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)

---

## 3. L1 — source-attested

### Appropriate claims

- definitions and curriculum facts;
- historical, geographic, literary, and civic claims;
- current information;
- quotations;
- instructions taken from an approved manual;
- a reported study result.

### Required record

- stable source identifier and exact supporting span;
- title, author or institution, publication date, and retrieval date;
- source class and authority;
- content or version hash where possible;
- claim-to-span entailment result;
- scope and expiry rule;
- visible learner citation.

### Source policy

The source policy depends on the claim. A local curriculum authority may define
the expected sequence. A primary paper supports its own measured result. A
government source supports a current law or program description. A community
knowledge holder may be the proper source for a local practice. Search ranking
alone is not an authority policy.

At L1 the mentor should separate:

- **source says** — direct report or quotation;
- **source implies** — bounded interpretation;
- **mentor infers** — reasoning beyond the source;
- **sources disagree** — preserve the disagreement instead of averaging it.

### Failure behavior

If a source cannot be recovered, the claim becomes unverified rather than
retaining a decorative citation. If sources conflict, the mentor shows the
conflict, explains the decision rule, and asks a specialist when needed.

July 2026 education systems are already converging on this pattern. DeepTutor
couples citation-grounded problem solving to question generation. EduGuard uses
instructor-approved retrieval, pedagogical strategy selection, claim-level
verification, and a 600-query instructor-authored, TA-validated bilingual
benchmark. `MEASURED-BENCH`

Sources:

- [DeepTutor](https://arxiv.org/abs/2604.26962)
- [EduGuard](https://arxiv.org/abs/2607.15738)

---

## 4. L2 — tool-checked

### Appropriate claims

- arithmetic and symbolic manipulation;
- dimensional analysis and unit conversion;
- executable code behavior;
- type and schema conformance;
- formal proofs;
- data transformations with reproducible inputs;
- satisfaction of declared constraints.

### Required record

- tool name, version, and execution environment;
- exact input or input hash;
- parameters and random seed;
- output or output hash;
- pass/fail predicate;
- stderr, warnings, and timeout state;
- link to a learner-visible replay when feasible.

Google’s current prompting guidance explicitly recommends code execution for
arithmetic, counting, and calculation. The larger design principle is
vendor-independent: do not ask a language model to approximate an answer that a
cheap, inspectable tool can establish. `VENDOR`, generalized as `INFERENCE`

Lean 4 illustrates the strongest L2 pattern. Automation may propose a proof, but
a minimal kernel checks the proof term. The claim does not become valid because
the model sounds confident; it becomes valid because an independent checker
accepts the formal object.

Sources:

- [Gemini prompting strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- [Lean language reference](https://lean-lang.org/doc/reference/latest/)
- [Theorem Proving in Lean 4](https://docs.lean-lang.org/theorem_proving_in_lean4/)
- [JSON Schema specification](https://json-schema.org/specification)

### Boundary

A passing tool result proves only the declared predicate:

- a test suite proves the tested behaviors, not that the software solves the
  right human problem;
- a formal proof proves the theorem under its definitions and axioms, not that
  the theorem models the intended physical situation;
- a calculator proves a numeric transformation, not that the inputs were
  measured correctly;
- an autograder proves an artifact passed, not that a learner understands it.

The mentor states what the tool established and what remains open.

---

## 5. L3 — measurement-checked

### Appropriate claims

- the observed behavior of a physical or social system;
- a measured learning outcome;
- an experimental result;
- a sensor reading;
- an empirical model prediction with a known validation domain;
- a simulation result used as evidence about a specified system.

### Required record

- dataset, specimen, device, or environment identity;
- measurement protocol and units;
- raw observations or immutable reference;
- analysis code and parameters;
- uncertainty;
- validation set or calibration record;
- assumptions and validity domain;
- time, place, and responsible agent.

W3C PROV provides stable primitives—entity, activity, and agent—for representing
how a result was generated. NIST’s Generative AI Profile requires organizations
to document provenance methods and evaluate their accuracy, quality,
reliability, and authenticity against known ground truth. The standards are
older than the frontier models because provenance is an enduring systems
requirement, not a model fashion.

Source:

- [NIST AI 600-1 Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

### Simulations and generated worlds

A simulation is L3 only for claims inside its validated domain. A visually
plausible generated world is L0 until it is tied to a model with published
assumptions and validation. A physics engine can be L2 for its own equations and
L3 only to the extent that those equations and parameters represent the target
system.

This rule lets the universal mentor use world models boldly without confusing
immersion with evidence:

- explore an imagined ecosystem at L0;
- cite the biology source at L1;
- check population equations at L2;
- compare against field data at L3.

---

## 6. L4 — human-authorized

### Appropriate decisions

- safeguarding and child-welfare action;
- diagnosis or treatment;
- legal authorship of an individualized education program;
- final credential, grade, or exclusion;
- consent and access to sensitive learner state;
- culturally consequential interpretation;
- exceptions whose impact cannot be reversed cheaply.

### Required record

- named authorized person and role;
- evidence packet shown to that person;
- decision and rationale;
- consent basis;
- jurisdiction and policy;
- review or expiry date;
- appeal and correction path.

L4 does not mean the AI becomes silent. It can assemble evidence, translate,
surface patterns, simulate options, and draft a plan. It cannot convert a
prediction into authority.

The routing rule is based on consequence and accountability:

```text
AI prepares → human understands → human decides → learner can contest
```

NIST’s current Generative AI Profile treats human oversight, measurement, and
governance as lifecycle controls rather than a final disclaimer. EduAgentBench
similarly evaluates source-grounded pedagogical judgment, situated multi-turn
tutoring, workflow execution, complementary verification, and human review.
`STANDARD`; `MEASURED-BENCH`

Source:

- [EduAgentBench](https://arxiv.org/abs/2605.14322)

---

## 7. The claim evidence record

Every learner-visible claim that can affect understanding or action receives a
compact record:

```yaml
claim_id: clm_...
claim_text: "..."
required_tier: L2
achieved_tier: L2
evidence:
  sources:
    - uri: "..."
      version: "..."
      span: "..."
      authority: "primary"
  tool:
    name: "lean"
    version: "4.33.0-rc1"
    input_hash: "sha256:..."
    output_hash: "sha256:..."
    predicate: "kernel accepted proof term"
scope: "theorem under listed definitions and axioms"
uncertainty: null
generated_by:
  model: "..."
  policy: "mentor-grounding-router-v..."
checked_at: "..."
expires_at: null
human_authorization: null
learner_explanation: "The proof checker accepted every logical step."
```

The record is append-only for provenance but correctable through superseding
entries. It can be represented with W3C PROV relationships and attached to
generated media through C2PA. A school does not need a global blockchain: signed
local records and content hashes are sufficient for most educational claims.
`INFERENCE`

---

## 8. Runtime routing

### Step 1: classify the claim

Identify domain, consequence, freshness, checkability, and whether the claim is
descriptive, computational, empirical, or authoritative.

### Step 2: assign the minimum required tier

Do this before generation. The model does not choose a lower tier because a tool
is slow or a source is unavailable.

### Step 3: collect evidence

Retrieve from approved sources, call a deterministic tool, run or locate a
measurement, or build a human review packet.

### Step 4: verify the evidence relationship

Check source existence, entailment, tool pass conditions, validity scope,
currency, and identity of any authorizer.

### Step 5: teach with calibrated visibility

Most young learners should not see a compliance console. They should see a
simple signal:

- “I made this example.”
- “This comes from your science book, page 42.”
- “I checked this calculation.”
- “This is what the experiment measured.”
- “Your teacher needs to decide this.”

The full record remains available to teachers, auditors, and curious learners.

### Step 6: invalidate when dependencies change

A claim expires when a source changes, a tool version is revoked, a dataset is
corrected, the learner’s context changes, or authorization ends.

---

## 9. Offline and low-connectivity grounding

Grounding cannot disappear when the network does.

A local school or community node should carry:

- signed curriculum bundles and primary-source excerpts;
- a local full-text and vector index;
- calculators, unit libraries, code runtimes, and schema validators;
- compact proof checkers where relevant;
- versioned simulation packages;
- a queue for unresolved searches and expert escalation;
- learner-visible timestamps showing how current the bundle is.

The claim record synchronizes when connectivity returns. L0 and locally
supported L1/L2 work continue immediately. Current web claims wait or are
explicitly marked as based on the last synchronized bundle. This is better than
silently fabricating freshness.

---

## 10. Acceptance tests

A grounding implementation passes when:

1. every consequential claim has required and achieved tiers;
2. a missing source or failed tool cannot silently become prose;
3. each citation points to a supporting span, not merely a related document;
4. source authority and expiry rules are domain-specific;
5. deterministic claims use tools when available;
6. tool logs are replayable and versioned;
7. simulations expose assumptions, uncertainty, and validity domain;
8. media preserves generation and edit provenance;
9. human-only decisions identify an accountable authorizer and appeal path;
10. the learner sees an age-appropriate explanation of why a claim is trusted;
11. the full path works offline for the local curriculum bundle;
12. teachers can override a claim without deleting its history;
13. specialist disagreement remains inspectable;
14. grounding latency and cost are measured;
15. learning outcomes are tested separately from factual correctness.

---

## 11. Relationship to pedagogy

Grounding answers **why this claim may be trusted**. It does not answer **what
the learner needs next**.

A perfectly sourced answer can still be badly timed, too advanced, demotivating,
or inaccessible. A beautiful analogy can teach powerfully while remaining L0.
The mentor therefore runs two coordinated policies:

```text
epistemic router: what evidence permits this claim?
pedagogical router: what action advances this learner?
```

The expert mentor mesh certifies specialist agents against both. A mathematics
specialist must pass correctness and tool-use evaluations. A visual teacher
must preserve source and transformation provenance. A safeguarding liaison must
recognize the L4 boundary. The conductor chooses the simplest learner-facing
explanation that retains the necessary evidence.

---

## Conclusion

The frontier mentor should be imaginative without being ambiguous, current
without pretending search is authority, computationally powerful without
mistaking a passed check for understanding, and helpful in consequential
decisions without claiming human authority.

L0–L4 makes that operational. Every claim has a route, a record, a release gate,
and a graceful failure behavior. The standard is light enough for a shared
offline school server and strong enough for a global expert-agent mesh.

---

## Source index

1. [Gemini grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search)
2. [Gemini tools](https://ai.google.dev/gemini-api/docs/tools)
3. [Gemini URL context](https://ai.google.dev/gemini-api/docs/url-context)
4. [Gemini prompting strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
5. [Gemini safety and factuality](https://ai.google.dev/gemini-api/docs/safety-guidance)
6. [OpenAI deep research](https://openai.com/index/introducing-deep-research/)
7. [OpenAI Academy: search and deep research](https://openai.com/academy/search-and-deep-research/)
8. [Anthropic citations](https://docs.anthropic.com/en/docs/build-with-claude/citations)
9. [Anthropic web search tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool)
10. [C2PA specifications 2.4](https://spec.c2pa.org/specifications/)
11. [C2PA explainer](https://c2pa.org/specifications/specifications/2.2/explainer/Explainer.html)
12. [W3C PROV-O](https://www.w3.org/TR/prov-o/)
13. [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
14. [Lean language reference](https://lean-lang.org/doc/reference/latest/)
15. [Theorem Proving in Lean 4](https://docs.lean-lang.org/theorem_proving_in_lean4/)
16. [JSON Schema](https://json-schema.org/specification)
17. [DeepTutor](https://arxiv.org/abs/2604.26962)
18. [EduGuard](https://arxiv.org/abs/2607.15738)
19. [EduAgentBench](https://arxiv.org/abs/2605.14322)
20. [FATE tutoring evaluator](https://arxiv.org/abs/2607.10647)
