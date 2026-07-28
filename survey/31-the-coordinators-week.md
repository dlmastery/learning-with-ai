---
title: "The Coordinator's Week — what special education actually consists of"
section: selpa-practice
status: draft
date: 2026-07-28
source_report: research/raw/H2-selpa-practitioner-reality.md
---

# The Coordinator's Week

A hostile reviewer read §04 — the section this project exists for — and judged it
**costume over a genuine core.** The intervention evidence was real; the job was
absent. PLAAFP, 504, LRE, caseload, prior written notice, escalation: all returned
zero. A coordinator would recognise the research and would not recognise their week.

The verdict was accepted and this section is the repair. It is also, on the numbers
below, where an AI's largest practical contribution to special education probably
lies — and that is not a concession.

---

## 1. Half of the legal test is procedural, and §04 argued only the other half

The federal standard for a free appropriate public education has **two prongs**
(*Rowley*, 458 U.S. at 206–07). One asks whether the programme was reasonably
calculated to confer educational benefit. The other asks whether the state complied
with the **procedures** set out in the Act.

A survey that discusses only instructional efficacy has addressed one half of the
statute. That is why §04 read as research wearing a lanyard: it was arguing about
whether the intervention works while the practitioner's week is largely governed by
whether the paperwork is defensible.

The asymmetry between the statutes is worth stating plainly, because outsiders
routinely collapse it:

| | IDEA | Section 504 |
|---|---|---|
| Procedural safeguards | **37 sections** of regulation | **One sentence** |
| Eligibility | 13 categories, team determination, 60-day timeline | Substantial limitation of a major life activity |
| Document | IEP — nine required components under §300.320(a) | A plan, form largely undefined |

A 504 plan is not a small IEP. It is a different statute with a different gate and
almost no procedural machinery, and a system that treats them as points on one scale
will generate advice that is wrong in both directions.

---

## 2. The correction to our own prior-written-notice claim

An earlier framing in this project said: *an AI that changes a child's programme
without generating prior written notice has created a procedural violation.*
Directionally right; **wrong in three specifics**, and the specifics matter because
they decide what a system is allowed to do without a meeting.

1. **The duty attaches to the agency, not to the tool.** A vendor cannot create or
   discharge a PWN obligation; the district holds it.
2. **It fires on identification, evaluation, placement, and the provision of FAPE —
   not on teaching methodology.** §300.501(b)(3) places methodology outside the
   meeting requirement entirely.
3. **A procedural violation denies FAPE only through §300.513(a)(2)'s three gates** —
   impeding the right to FAPE, significantly impeding parental participation, or
   causing deprivation of educational benefit. Not every misstep is a denial.

The load-bearing sentence is the Department's own, from the 2006 commentary:

> *"Placement refers to the provision of special education and related services rather
> than a specific place."* (71 FR 46588)

So the line an AI must not cross is between the **service** and the **method** — not
between a big change and a small one. Changing which explanation strategy a child
sees on Tuesday is methodology. Changing the minutes of specialised instruction is
placement, and that is a team decision with notice.

---

## 3. Predetermination is the sharpest AI-specific legal risk

This is the finding with the most immediate consequence for anyone building, and the
regulator described the failure mode without being asked about AI at all.

Explaining why it would *not* require prior written notice to be issued before an IEP
meeting, the Department wrote that doing so:

> *"could suggest… that the public agency's proposal was improperly arrived at before
> the meeting and without parent input."* (71 FR 46691)

That is the *Deal v. Hamilton County* predetermination doctrine, stated by the
regulator, in advance.

Now consider what a recommendation engine does. It arrives at a proposal before the
meeting, without parent input, and presents it with the authority of having processed
the data. **Every recommendation engine is a predetermination machine by default.**

The design consequence is specific and cheap: an AI may prepare *options with their
evidence*, and must not arrive with *a recommendation*. The difference is legally
load-bearing and it costs nothing to respect.

---

## 4. Four prior attempts to cut the paperwork, all measured, all zero

The administrative burden in special education is not a new complaint, and the
history of trying to fix it is a graveyard:

| Attempt | Result |
|---|---|
| **Computerisation** | SPeNSE, n = 972 — **no significant relationship** to hours spent |
| **Human delegation** | Same null, *"because much of the paperwork teachers complete cannot be appropriately delegated"* |
| **Deregulation** | ED priced its own excusal provision at **nothing** |
| **IDEA §609 waiver authority** | **21 years, 15 state slots, zero documented waivers** — and the effectiveness report the statute mandates **has never been filed** |

The AI claim is the fifth attempt. Its entire measured base is **one RCT of 22 novice
teachers on goal drafting.**

We report that ratio rather than soften it. Four measured nulls against one small
trial is the correct prior, and anyone promising administrative relief should be made
to say why this attempt differs from the four that did not work. Our answer — that the
previous four automated *storage and transmission* while the cost is in *composition
and judgement* — is a hypothesis, not a finding.

---

## 5. Where the hours actually go

In the only direct-observation study: **20% of class time on academic instruction,
17% on paperwork.**

Read those two numbers next to each other. The instructional minutes and the
compliance minutes are nearly the same quantity.

This changes what the honest pitch is. This survey has argued that AI's contribution
at the margin is *fidelity and dosage of known-good intervention* (§04). That remains
true. But the largest **practical** contribution available today is probably
**administrative** — and saying so strengthens the instructional argument rather than
conceding it, because every hour returned from paperwork is an hour available for the
thing with 4,000 effect estimates behind it.

---

## 6. Accommodations: mandated, and weak

§04 treated testing accommodations as part of the known-good base being scaled. That
was wrong, and the correction is uncomfortable enough to state in full:

- Kieffer et al., overall **g = .034, p = .180**
- Rios et al., across **N = 11,069**: **none statistically different from zero**
- Elbaum 2007: the effect **reverses** at secondary level
- Teachers assign accommodations **at chance** (N = 1,218)

Both halves have to be held at once. Accommodations are **legally required** and
**evidentially weak**. That is not an argument for withholding them — the legal
obligation is not contingent on effect size, and access is a right rather than an
intervention. It is an argument against counting them in the efficacy column, and
against a system that recommends them as though it were prescribing something
measured.

The most useful thing an AI can do here is not select accommodations. It is to record
which were provided, so that somebody can eventually run the study that the field has
not run.

---

## 7. Escalation, and a null that should temper every safeguarding feature

Two figures define the gap. NIS-4 found that **≥80% of school-recognised maltreatment
never reached investigation**, while CPS would have investigated **72%** of it. The
recognition is happening; the referral is not.

And the obvious fix has been tested. Wyman's randomised trial of gatekeeper training
moved **confidence by ES 1.22** and **identification behaviour by nothing.**

That pattern — large movement in how prepared people feel, zero movement in what they
do — is the felt-learning trap in a safeguarding costume, and it is the reason a
safeguarding feature must be measured on **referrals made**, never on staff confidence
or completion of a module.

---

## 8. The ownership line

The question a builder needs answered is not "can AI help" but "who owns this
artefact." The full table is in the source report; the rule it produces is short:

> **An AI may draft anything and may author nothing that a signature attaches to.**

It may draft PLAAFP language from progress data, propose goal wording, assemble the
evidence packet, track service minutes, prepare a parent for a meeting, and surface
that a decision rule has fired. It may not author the IEP, determine eligibility,
decide placement, select a disability category, or arrive at a meeting with a
recommendation.

And one more, from §3: it may prepare **options with their evidence**. Never a
recommendation.

---

## 9. What this section commits us to

- **Argue both prongs of FAPE.** Substantive efficacy is half the statute. A system
  that ignores procedure is not deployable regardless of its effect size.
- **Draw the line at service versus method**, not at size of change. Methodology sits
  outside the meeting requirement; minutes of specialised instruction do not.
- **Present options, never a recommendation.** Every recommendation engine is a
  predetermination machine by default, and the regulator said so before AI existed.
- **State the four nulls whenever claiming administrative relief.** Computerisation,
  delegation, deregulation and the waiver authority all returned zero.
- **Never count accommodations in the efficacy column.** Required by law; not
  established by evidence; and assigned at chance.
- **Measure safeguarding on referrals**, not on confidence. ES 1.22 on feeling ready
  and zero on doing anything is the whole warning.

§04 asked what the evidence says a system should teach. This section is the answer to
a different question, and a coordinator would ask it first: **what is this allowed to
touch, and who signs.**
