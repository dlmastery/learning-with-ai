---
title: "The Market — nine bets, one graveyard, and the number that shrinks as you look at it"
section: market
status: draft
date: 2026-07-28
source_report: research/raw/E1-E2-edtech-landscape-lessonorca.md, research/raw/E3-latest-sweep.md
---

# The Market

ASSISTments publishes its own evidence page. Read the studies in order of sample
size:

| Study | Design | n | Effect |
|---|---|---|---|
| Mendicino, Razzaq & Heffernan (2009) | small RCT | 28 students | **0.61** |
| Kehrer, Kelly & Heffernan (2013) | small RCT | 65 students | 0.37 |
| Maine (2012–2015) | RCT | 46 schools, 2,769 students | **0.22** |
| North Carolina (2018–2021), WestEd | RCT, delayed outcome | 63 schools, 5,991 students | **0.10** one year later |
| Gates Foundation / SRI | independent evaluation | not stated | **0.03** |

**0.61 → 0.22 → 0.10 → 0.03**, as the sample grows and the evaluator stops being
the vendor.

That gradient is the single most instructive object in the edtech market, and it is
published by the company itself, on its own site, without spin. It is to their
enormous credit. It is also the number you should hold in your head every time a
product quotes you an effect size.

Note the last translation. ASSISTments' public headline is "60% more growth in math
scores" — which is the **0.22** study rendered in percentage-of-a-year terms. A
0.22 SD effect is a genuinely good result in education. "60% more growth" sounds
like something else entirely. **The translation layer between effect sizes and
marketing copy is where most of this market's dishonesty lives, and it does not
require anyone to lie.**

---

## 1. Nine bets

A directory of companies is worthless six months after it is written. What survives
is the structure of the bets. Every product in this market has picked one primitive
to be its load-bearing wall — the thing that, if true, makes everything else follow.
Each primitive is a falsifiable hypothesis about how learning happens.

| Primitive | The bet | State of the evidence |
|---|---|---|
| **Content generation** | The bottleneck is materials | Every retrievable metric is a **teacher-time** metric |
| **Tutoring** | The bottleneck is one-to-one attention | Splits into answer-giving and withholding; only the pre-LLM generation has trials |
| **Assessment** | The bottleneck is grading cost | Works where the mechanism is clustering; fails where it is judgement |
| **Teacher tooling** | The highest leverage is not on the student at all | Best evidence-to-deployment ratio; least glamorous |
| **Language** | The bottleneck is practice hours with a patient interlocutor | The one cluster where "practice, not answers" is commercially natural |
| **Early literacy** | The bottleneck is an adult who will listen | The most defensible bet in the market |
| **STEM representation** | The bottleneck is symbolic abstraction | Strong lab support, almost no field-scale randomised evidence |
| **Credentialing** | The bottleneck is the signal, not the learning | Succeeds only when it displaces one specific gatekept test |
| **Infrastructure** | Whoever owns rostering and the LTI socket owns the market | Where the money is, and where the risk is |

Two clusters deserve their evidence stated rather than summarised.

**Tutoring's real numbers are pre-LLM.** Kulik & Fletcher (2016) — 50 controlled
evaluations, **median 0.66 SD** — is the most-cited figure in the market and comes
with its own debunking attached: the improvement "depended to a great extent on
whether improvement was measured on locally developed or standardized tests," and
§24 puts test alignment at a factor of 2–3. Pane et al.'s Cognitive Tutor Algebra I
trial, matched-pair randomisation across seven states, is the best large-scale
evidence anyone has: **no effect in year one**, positive in year two, significant
for high schools and **not** for middle schools, at roughly eight percentile points.
The LLM generation inherited the marketing claim and none of the measurement.

**Early literacy is the most defensible bet in the market**, in mechanism terms
rather than enthusiasm terms. The AI does something a human demonstrably cannot
scale — listening to twenty-five children read aloud at once. The output is a
measured behaviour, oral reading fluency, not a self-report. And the pedagogy
underneath, decoding practice with immediate corrective feedback, is among the
best-replicated results in education. If AI-in-education works anywhere, it works
here first. The headline claims still need their qualifiers read: one vendor's "68%
faster reading growth" is conditioned on students who used it "at dosage," which is
a selection effect unless dosage was randomised.

---

## 2. What the market measures instead of learning

**Finding one: the evidence gradient runs opposite to the funding gradient.** The
two products in this section with genuine independent randomised evidence —
ASSISTments, a nonprofit that is free to teachers, and Cognitive Tutor, a
forty-year-old curriculum publisher — report **0.03 to 0.22 SD**. The products with
the largest claims report no retrievable design, sample or comparison group. And the
best-funded entity in the sector, at a $4.8bn buyout, makes no learning claim at all.

**Finding two: "time saved" has quietly replaced "learning gained" as the industry's
success criterion.** Across the content-generation and teacher-tooling clusters it is
the only quantity anyone measures. That is not a criticism in itself — teacher time
is real and scarce. But it needs one distinction that no vendor in this survey makes:
**teacher time saved is a legitimate benefit; learner time saved is the documented
signature of harm.** The unguarded arm of the Bastani trial also saved the student
enormous time, and §01 carries what happened when the tool was taken away.

**Finding three: mechanism claims are checkable and outcome claims usually are not.**
"Guides rather than answers." "Listens as students read aloud." "Makes teaching
decisions in the moment." Each of those describes what the system *does*, and each is
verifiable by inspection. That makes them worth more than an unreproducible outcome
number — and §23 records the case that limits the principle, where a fully true
mechanism claim bought nothing because the mechanism only fired when a student first
recognised they needed help.

**Finding four: a resolving DOI is not a result.** Several products' "studies"
resolve only to AEA RCT registry identifiers with the prefix `10.1257/rct.` — for
example `10.1257/rct.13519`. **Those are pre-registrations. They contain no results.**
A DOI here means someone intends to run a trial. Treat the prefix as a red flag, not
a citation.

And the case that shows the gradient inside a single company: Curipod holds the most
real evidence of any product in its batch and markets on the weakest number it owns.
Its homepage leads with district testimonials — pre/post state-test comparisons with
no control group, no sample size and no statistical test, one of them spanning **two
teachers**. Its genuine study is a randomised trial with **n = 142** at
**d = 0.301–0.800** — in *university nursing students*, against a control of
"conventional lectures supplemented with PowerPoint presentations and textbooks," on
survey constructs rather than achievement tests. It cannot support the K-12 state-test
claim on the homepage, and it is a category error to let it. **A company can hold
genuine evidence and still market on testimonials, because the genuine evidence is
narrower and less flattering.**

---

## 3. The graveyard, and its single cause of death

Edtech's failure record is the most informative dataset it has, and unlike its
success literature it is not vendor-controlled.

**One Laptop Per Child** has a randomised verdict. Cristia et al., **319 rural
Peruvian primary schools**, 15 months: computers per student rose from **0.12 to
1.18** and use rose substantially at school and at home. "No evidence is found of
effects on enrollment and test scores in Math and Language." The ten-year follow-up
across 531 schools found no significant effects on academic performance, completion,
or university enrolment. Delivery succeeded completely. The theory of change was
wrong.

**inBloom** was a $100 million student-data warehouse. Every district and state
withdrew after parent protests and it closed in April 2014. The technology worked;
every customer left. §11 and §15 carry the custody lesson.

**Knewton** raised roughly **$157M disclosed** across seven rounds against a claim —
"sophisticated, real-time analysis of reams of student performance data" — that was
never stated in a form that could fail. Its assets sold to Wiley for **under $17
million** in 2019. Roughly 90% capital destruction. §11 establishes the deeper
problem independently: knowledge-tracing accuracy had already plateaued. Knewton was
selling precision from a region of the design space where precision had run out.

**AltSchool** raised $133M and built a network of schools in order to build software.
The schools were the R&D cost centre for a product that did not exist yet; when the
software pivot came, the schools — the thing families had actually bought — closed.
The surviving artefact, a parent progress portal, is now a table-stakes feature.
Right about the feature, wrong about the business.

**2U** bought edX from the Harvard/MIT nonprofit for **$800M**, never made an annual
profit, and filed Chapter 11 on 25 July 2024. Its revenue-share structure made
student *volume*, not student *outcome*, the only lever it had.

**Byju's** reached a **$22bn valuation** and 150 million claimed registered users. Its
founder said publicly in October 2024 that "the company is worth zero." Its reported
85% retention rate was never independently verified and this survey does not repeat
it.

Six deaths, six different proximate causes, one structure:

> **Each one succeeded completely at the thing it measured, and the thing it measured
> was not learning.**

Laptops delivered. Data integrated. Model sophistication. Iteration velocity.
Enrolment volume. Registered users. The proxy is always something the organisation
controls; learning is always something it does not. This is Goodhart's law with
children in the loop, and edtech has an aggravating feature: **the delay between the
proxy and the truth is measured in school years, so a company can be dead right on
its own metrics for a decade.**

The operational test that falls out of it is the one this project should be held to
as well:

> **Name the metric that would tell you your product is not working, and state how
> long you would have to wait to see it.**

Every company above would have failed that test.

---

## 4. Two failures that are still running

The graveyard is retrospective. Two live failures matter more.

**A core claim was falsified after sale.** Turnitin shipped AI-detection in early
2023. Weber-Wulff et al. (2023, *International Journal for Educational Integrity*)
tested twelve public tools plus two commercial systems in wide academic use for
accuracy, error type, and robustness to machine translation and obfuscation. The
tools are not reliable discriminators. Schools subsequently disabled the feature;
students alleged false accusations, including cases involving grammar-correction
software those schools recommend. A vendor-stated false-positive rate of about 1%,
against tens of millions of submissions, is a large number of accused innocents.

**And consolidation concentrated the blast radius.** In late April 2026 Canvas LMS
suffered a security breach that *404 Media* described as the largest educational
security breach on record: **3.65 terabytes, approximately 275 million records,
8,809 universities and education institutions.** By 8 May, seven federal lawsuits had
been filed, one naming the private-equity owner as co-defendant.

Three consequences the rest of this survey has to carry. The same logic that made
Canvas a good $4.8bn asset — one integrated platform, near-universal adoption — made
8,809 institutions a single point of failure. **Every "we don't train on student
data" promise in this market is a promise about *use*, not about *custody*.** A
vendor can honour it perfectly and still lose the data. And therefore data
minimisation is a security control, not a compliance chore: the most effective
mitigation available to any product here is to not hold the record at all — which is
exactly the pressure the inBloom failure applied twelve years earlier, and which the
market un-learned.

---

## 5. One deployed case, and what it got right by accident

LessonOrca is this project owner's own product. It is admitted here as **one
deployed, instrumented case study among several**, not as evidence that anything
works. Its scale is three tutoring centres, 25 tutors, 100 students. Its marketing
copy is `VENDOR` and is not restated as a finding. Its operating economics are not
discussed.

What is interesting is a set of design decisions arrived at from customer discovery
rather than from citation, which converge with the evidence in this survey.

**Withholding is classified as a safety property, not a feature.** "Socratic method
only. Guides students to answers, never gives them" sits on the page under *safety
guardrails*. That is the correct taxonomy: the trial evidence says unfettered
answering is the harm condition, so answer-withholding belongs with the guardrails
and not with the features.

**The architecture puts the AI behind the human.** The positioning — "AI will not
replace tutors, but it will redefine how they work" — is structurally the Tutor
CoPilot configuration, which is the one AI-tutoring architecture with a
live-classroom randomised trial behind it (§09, §26). The wedge identified from
interviewing tutors was **continuity**, not comprehension: nobody remembers what
happened last Wednesday. That is the correct read of the literature, reached without
reading it.

**Oversight is total rather than sampled**, with human review gates on every artefact
that leaves the system — profiles reviewed before sharing, parent emails reviewed
before sending — and synthetic-origin labelling at the point of consumption. The
same three commitments appear independently at SchoolAI and MagicSchool: **adult
visibility into every AI interaction, explicit labelling of synthetic content, and
never posing as human.** Three companies converged on them without coordinating, and
they are stronger than anything in current regulation. That convergence is the
candidate norm this section contributes.

### The null, and it is our own

There is no instrumentation of the pedagogical claim. Not one event in the product's
analytics describes a tutoring session, a student turn, an AI question, a refusal to
answer, a profile update, or a parent opening a transcript. **The product in this
survey most explicitly designed around a falsifiable pedagogical claim has not
instrumented the claim.** It measures acquisition precisely and pedagogy not at all.

That is the §3 pathology — measuring what the organisation controls — appearing in
the survey author's own work. It is reported rather than omitted because the survey's
credibility depends on applying its own test to itself first.

Three further criticisms follow from the same evidence base, and they are not
softened. **The refusal is unverified**: no transcript audit, no red-team result, no
refusal-failure rate. "Never gives answers directly" is currently an assertion about
a prompt. **"Socratic only" is stronger than the evidence supports**: §04's archetype
work is explicit that for reasoning and abstraction gaps, discovery learning is
actively harmful and explicit instruction is required. The defensible version is
narrower — *never answer the question the student was assigned; may directly instruct
on the prerequisite they lack.* And **the substitute is unmodelled**: a student
blocked by a Socratic tutor at eleven at night has a general-purpose chatbot in the
next tab. One vendor refusing does not eliminate the harm condition. It relocates it.
A refusal engine with no theory of the substitute is measuring its own compliance,
not the student's behaviour.

One more datum from the same instance generalises. Its privacy and terms pages were
opened by a vanishingly small fraction of visitors. **Consent architectures that
route through policy pages reach essentially nobody**, which is the argument for
in-product, in-context disclosure over the kind the law contemplates — and it is why
the three convergent norms above are worth more than a longer policy.

---

## 6. What this section commits us to

- **Quote the gradient, not the number.** 0.61 → 0.22 → 0.10 → 0.03 as n rises and
  the evaluator becomes independent. Any effect size from a vendor sits somewhere on
  that curve, and usually at the left end.
- **Distinguish teacher time from learner time.** One is a benefit. The other is the
  documented signature of the harm condition.
- **Prefer mechanism claims and audit them.** A mechanism claim that survives
  adversarial inspection is worth more than an outcome claim nobody can replicate —
  provided somebody actually inspects it.
- **Treat `10.1257/rct.` as a red flag.** It is an intention, not a finding.
- **Name the disconfirming metric and its latency**, before shipping. Every company
  in the graveyard would have failed that test, and so, today, would ours.
- **Instrument the pedagogy before marketing it.** Our own product does not, and that
  is the section's principal negative result.
- **Minimise custody.** 275 million records, 8,809 institutions. The strongest privacy
  control is not holding the record.

The market's problem is not that it lies. It is that it measures the thing it can
move, publishes the number that survives translation into marketing, and waits out
the school years it would take for anyone to notice the difference. The fix is not
better claims. It is naming, in advance, the observation that would prove you wrong.
