---
title: "The Empty Chair — designing for the margin first"
section: selpa
status: draft
date: 2026-07-27
source_report: research/raw/H1-selpa-accessibility.md
---

# The Empty Chair

Start with a specific child, because the general case is where this field goes to
avoid the work.

She is eleven. She reads, but decoding costs her enough that by the time she
reaches the end of a sentence the beginning has gone. She can hold a conversation
about photosynthesis that would impress you and then fail a worksheet about
photosynthesis, and the gap between those two facts is invisible to every system
she is enrolled in. She is not lazy and she is not slow. She is running a working
memory that spends most of its capacity on the part everyone else automated years
ago.

There are millions of her. In the United States they are served under
individualised education programs, coordinated regionally, and in California
through Special Education Local Plan Areas. Roughly one child in seven.

Here is the state of the evidence on whether generative AI helps her.

---

## 1. The census

We ran it rather than cited it. ERIC and Europe PMC, 2026-07-27:

| Query | Hits |
|---|---|
| `(generative AI \| ChatGPT \| LLM) AND "randomized controlled trial" AND students` | **30** |
| The same, plus *disability · dyslexia · ADHD · autism · special education · IEP* | **0** |

Zero. Not "few" — the intersection is empty. Re-run independently a second time
during this project, same result.

Widen from RCTs to everything: the entire world literature on AI interventions for
students with learning disabilities, 2022–2025, across seven databases, is
**11 studies, 10 independent experiments, 3,033 participants**. At most one is a
randomised trial (n = 60). **None** was rated low risk of bias. All eleven reported
positive results, which is a publication-bias signature and not an encouragement.

So every effect size quoted in the AI-tutoring conversation — every headline, every
pilot, every deck — was measured on somebody else's child.

That is the empty chair. It is not a verdict. Nobody has run the experiment.

---

## 2. The inversion that makes this the *best* place to build

The intuitive read is that the margin is the hardest problem and should therefore
come last. The evidence says the opposite.

**Special education is the most replication-rich area in all of education.**

While the AI-and-disabilities literature totals eleven studies, the Direct
Instruction literature alone is **328 studies, 413 designs, roughly 4,000 effect
estimates**, all positive, all significant except on affective outcomes, with
unusually *no publication-bias signature*. Swanson's syntheses of interventions for
learning disabilities cover 180 experimental studies and land at **M = 0.79**.
Gersten's mathematics synthesis draws on 42 randomised and quasi-experimental
studies.

Read the ratio: the known-good intervention base for these learners is **two orders
of magnitude larger** than the AI base.

That inverts the job description. In most of education, the interesting question is
*what should we teach and how*. Here, that question has largely been answered, in
public, with replication, for decades. What has never been solved is **delivery**:
the fidelity, the dosage, the individualisation, the sheer number of adult-attention
minutes that explicit systematic instruction requires to work.

> **The AI's job at the margin is not invention. It is fidelity and dosage of
> known-good intervention, at a frequency no staffing model has ever afforded.**

That is a smaller claim than "AI will revolutionise special education," and a much
stronger one, because the thing being scaled already has 4,000 effect estimates
behind it.

---

## 3. Where the folk consensus is wrong

Building faithfully means knowing what to be faithful *to*. Four widely-held beliefs
do not survive contact with the primary literature, and a system that automates them
will automate a mistake at scale.

**Orton-Gillingham is not the evidenced ingredient.** It is the intervention most
requested by parents of dyslexic children. Against active comparison instruction it
shows **g = 0.22, p = .40** and **g = 0.14, p = .59**, both non-significant. What
*is* evidenced is explicit, systematic decoding instruction. The multisensory
branding is not carrying the effect. Ship the mechanism and drop the brand name.

UDL is a design philosophy, not an evidence-based intervention. The best
meta-analysis concludes it improves the learning *process* while "the impact on
educational outcomes has not been demonstrated"; a policy review found no rigorous
published research demonstrating improvement. The component practices it bundles
(multiple representations, choice, scaffolded engagement) are individually
well-evidenced. Keep the components; drop the claim. We build to the accessibility
standard the law actually incorporates, described below, because access is a right
and not because a framework promises a score.

Do not build a working-memory trainer. Working-memory training produces reliable
near-transfer to the trained task and does not transfer to anything anyone cares
about. Given that our eleven-year-old's central constraint *is* working memory, the
temptation is enormous and the evidence is unambiguous. **Externalise memory
instead.** Off-load it into the environment, the notation, the shared canvas, the
persistent record. Do not try to enlarge the buffer. Reduce what has to go in it.

And a framework can be implemented faithfully and still hurt. The federal
evaluation of Response to Intervention covered **146 schools across 13 states**, all
experienced with RTI, 86% reporting full implementation. Regression discontinuity
around the screening threshold found that Grade-1 students who scored *just below*
the cut, and were therefore assigned to reading intervention, had lower spring
scores than those just above it. Grades 2 and 3: no significant impact.

The mechanism most discussed is that intervention pulls a child *out of* effective
core instruction, and the replacement is not better than what it replaced. The design
lesson is permanent and it applies directly to any AI that routes learners:

> **Routing a child into "intervention" is never neutral. It has an opportunity cost,
> and that cost belongs inside the decision.**

---

## 4. The architecture the evidence forces

Three findings, each of which kills a popular product pattern.

### 4.1 Measurement without a decision rule is inert

The result that most constrains the whole system is a clean randomised trial.
Thirty-three teachers, three arms, twenty weeks: curriculum-based
measurement plus an expert system that told teachers *what to change*; CBM alone; and
no-CBM control.

> "Compared to the control group, **both** CBM groups appeared to revise students'
> instructional programs more frequently. However, **only the CBM-ExS group effected
> superior student achievement.**"

Frequent measurement, frequent program changes, no guidance on what to change: **no
achievement benefit.** Replicated in a companion randomised study in spelling.

Now look at what the industry ships. Dashboards. Streaks. Mastery bars. Adaptive
difficulty. Engagement analytics. Every one of those is the **CBM-without-expert-system
arm** — the arm that measured more, changed more, and moved nothing.

So build the expert system, and not the dashboard. The active ingredient is a
prescribed, principled change of instruction, drawn from a known-good menu,
triggered by a stated rule.

### 4.2 Two clocks, and the slow one is slower than you think

Trend-based decision rules on weekly academic probes are **not statistically viable
until 7–10 weeks** of data. An AI tutor that changes method after three wrong
answers is not adapting. It is fitting noise, and it destroys exactly the
consolidation that explicit instruction depends on.

But a tutor that does nothing for ten weeks is useless. The resolution is that these
are two different loops that get conflated:

| Clock | Signal | Latency | Permitted action |
|---|---|---|---|
| **Fast** — within session | Error *type*, latency, help-seeking, disengagement | Seconds to minutes | Micro-scaffold: hint, worked step, re-represent *this item*. **May not change the method.** |
| **Slow** — across sessions | Graphed probe scores against a goal line | 4 points minimum; 7–10 weeks for a trend judgement | **Change the method.** Fire the adaptation step. Log it. |

The fast loop is responsive. The slow loop is skeptical. A system with only the fast
loop thrashes; a system with only the slow loop is inert. Most products have built
the fast loop, called it personalisation, and shipped.

### 4.3 Restraint matters *more* at the margin

Unconstrained LLM access widens the gap between low- and high-prior-knowledge
learners. The largest AI-tutoring trial in Nigeria found gains accruing
disproportionately to students with higher initial performance. Sierra Leone's
effect loaded at **+0.195 SD per SD of baseline mathematics** — the strong pulled
further ahead (§09).

An unguarded answer-machine is not neutral technology that helps everyone a bit. It
is a gap amplifier, and our learner is on the wrong side of it. The refusal engine —
the judgment to ask instead of tell, to wait, to let a struggle run — is not a
pedagogical nicety here. It is the difference between a tool that closes the gap and
one that widens it.

There is an important asymmetry to state honestly, because it constrains what we may
claim. Guardrails have been measured to remove harm: unguarded assistance left
learners **17% worse** on later unassisted work, and the guardrailed arm's unassisted
coefficient was **−0.004 (not significant).** Harm removed (§01). **Benefit not
demonstrated.** Anyone selling guardrails as a learning gain is ahead of the
evidence, including us.

---

## 5. What the system may not do

Four hard limits, and they are not negotiable by product decision.

- **An AI may not author an IEP.** It is a legally binding document authored by a
  team including the parent. An AI may draft materials, track goals, surface
  evidence, and prepare a parent for the meeting. It does not sign.
- **An AI may not diagnose or label a child.** It may observe that a strategy is not
  working and say so, in behavioural terms, to the humans responsible.
- **The accessibility standard is WCAG 2.1 AA, and the deadline moved.** *Corrected
  2026-07-28:* the ADA Title II web rule incorporates **WCAG 2.1** and not 2.2, and the
  compliance dates were pushed twelve months in April 2026 (91 FR 20902) to
  **26 April 2027** and **26 April 2028**. Most published guidance, including an
  earlier version of this section, still says WCAG 2.2 and April 2026. Build to 2.2
  if you like; conform to 2.1 because that is what is enforceable.
- **Disability status is sensitive data.** Under **IDEA §300.624**, personally
  identifiable information "must be destroyed at the request of the parents." An
  undeletable model weight is therefore a compliance failure for the population the
  system claims to serve. The learner model is
  local, inspectable, correctable, and deletable, or it is not shippable.

---

## 6. Curb cuts, and the half of the thesis that survives

The design instinct behind this section is the curb cut: build the ramp for
wheelchairs, and it turns out to serve strollers, suitcases, delivery carts and
everyone with a bad knee. Build the SELPA-grade system and it serves every learner.

The engineering half of that thesis holds well. Explicit instruction, externalised
memory, a shared canvas that carries working-memory load, honest pacing, a decision
rule instead of a dashboard, restraint by default. None of these are concessions.
They are what good instruction looks like for anyone, made visible because at the
margin you cannot get away with anything less.

The evidential half needs a caveat we should state ourselves rather than have pointed
out. Effects for learners with disabilities do not transfer automatically to
typical learners or the reverse; non-responders to well-implemented intervention
exist and are predictable; and an effect size of 0.41 is a statement about a
distribution, never a promise to a child. "It works for the margin so it works for
everyone" is a design heuristic, not a finding.

---

## 7. Filling the chair

Everything in this section is an argument that the pieces exist. Four thousand effect
estimates on what to teach. A randomised trial telling us that measurement without
prescription is inert. A number — 7 to 10 weeks — on how long to wait before
changing course. A clear prohibition on the brain-trainer, and a clear instruction to
externalise memory instead. A gap-widening result that makes restraint mandatory
instead of optional.

What does not exist is a single randomised trial of any of it, assembled, with these
learners.

We do not treat that absence as a reason to wait. We treat it as the specification
for the first experiment worth running, and building this system carries the
obligation to run it: a delayed, unassisted, novel-item primary outcome, published
whichever way it lands.

The chair is empty because nobody sat down. Not because the seat was taken.
