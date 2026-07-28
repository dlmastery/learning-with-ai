---
title: "H2 — The practitioner's week: IEP machinery, IDEA/504/ADA, LRE, procedural safeguards, caseload, and safeguarding"
wave: H
date_researched: 2026-07-28
sources_count: 118
---

# H2 — SELPA practitioner reality

**Why this report exists.** A hostile review of `survey/04-the-empty-chair.md` found it
"costume over a genuine core": the curriculum-based-measurement spine is real, but
**PLAAFP, 504, LRE, caseload, prior written notice, and escalation return zero across the
whole corpus.** A special-education coordinator would recognise the research and would
not recognise their week. This report supplies the missing half — the operational and
legal machinery — at practitioner resolution.

**Relationship to H1.** `H1-selpa-accessibility.md` covers the *intervention evidence
base* (Direct Instruction, structured literacy, CBM/DBI, RTI's null, the AI-tutoring
census, UDL, WCAG). H2 does not redo any of it. H2 covers the *documents, statutes,
timelines, people, and hours*. Where H1 said "an AI may not author an IEP," H2 says
exactly which clause, who signs it, what an AI may draft, and what would make the
omission a legal defect rather than a stylistic one.

**Currency warning, and one thing this project would otherwise have got wrong.** All
34 CFR text below was pulled verbatim from the eCFR API at the **2026-07-01** point-in-time
snapshot on 2026-07-28. One high-traffic deadline changed three months ago and most
secondary sources are still wrong about it — see §3.4.

---

## 0. Headline findings

1. **The single largest AI opportunity in special education is administrative, not
   instructional — and that is a finding, not a consolation prize.** The federal
   government's own regulatory impact analysis for the 2006 IDEA rule prices an IEP
   meeting at 1.5 hours and estimates 1.2 IEP Team meetings per child per year, then
   admits: *"we lack detailed data on the number of IEP Team meetings conducted each
   year"* (71 FR 46845). Twenty years later the field still runs on estimates. The work
   an AI can legitimately absorb — drafting, summarising, cross-checking, deadline
   tracking, translation, meeting-notice logistics — is real, large, and legally
   permissible. The work it may not touch is small, sharply bounded, and load-bearing.

2. **"Placement" does not mean a room. It means the services.** ED's longstanding
   position, stated in the 2006 preamble: *"placement refers to the provision of special
   education and related services rather than a specific place, such as a specific
   classroom or specific school"* (71 FR 46588). This single sentence decides most of the
   AI question. An AI that alters *what services a child receives* is altering placement.
   An AI that alters *how a lesson is taught inside an unchanged service* is not.

3. **The brief's framing — "an AI that changes a child's programme without generating PWN
   has created a procedural violation" — is directionally right and technically
   imprecise in three ways that a coordinator would catch instantly.** Corrected version
   in §5.3. Short form: the PWN duty attaches to the *public agency*, not to a tool; it
   is triggered by changes to identification, evaluation, educational placement or
   provision of FAPE, **not** by changes to teaching methodology; and a procedural
   violation is a violation immediately but denies FAPE only if it clears one of the
   three gates in 34 CFR §300.513(a)(2).

4. **The most dangerous thing an AI can do in this domain is not to be wrong. It is to be
   early.** ED itself warned that issuing a proposal in advance of the IEP meeting *"could
   suggest, in some circumstances, that the public agency's proposal was improperly
   arrived at before the meeting and without parent input"* (71 FR 46691). That is the
   predetermination doctrine, and an AI recommendation engine is a predetermination
   machine unless deliberately designed not to be. See §5.4.

5. **Three prior attempts to reduce this administrative load were measured and all returned
   zero — and a fourth was never even attempted.** Computerisation: *"Using a computer to prepare
   IEPs was not significantly related to time spent writing each IEP"* (SPeNSE, n = 972). Human
   delegation: no significant effect, *"because much of the paperwork teachers complete cannot be
   appropriately delegated to an aide or secretary."* Deregulation: ED priced its own
   meeting-excusal provision at approximately nothing. And **IDEA §609's paperwork-waiver
   authority has, in twenty-one years, produced no documented waiver and no required
   effectiveness report.** The AI claim is the fifth attempt, and its entire measured evidence
   base is one randomised trial of 22 novice teachers on one sub-task.

6. **The single most widely deployed intervention in American special education —
   accommodations — has a weak, inconsistent, sometimes-reversed evidence base, and the What
   Works Clearinghouse has certified nothing about it in 30 Practice Guides.** Two meta-analyses
   return overall nulls; teachers assign accommodations *at chance* (N = 1,218); benefit is
   item-conditional rather than student-conditional, so better learner profiling cannot fix it.
   `survey/04` argues AI's job is fidelity to known-good intervention. Accommodations are
   mandated and not known-good, and the survey must hold both facts at once.

7. **In safeguarding, the binding constraint is disclosure, not detection — which means an AI
   flagging system intervenes on the wrong variable.** NIS-4: at least 80% of maltreatment
   recognised by school staff never reached an investigation, and CPS would have investigated 72%
   of what it never saw. Wyman's RCT: gatekeeper training moved confidence by ES 1.22 and moved
   identification behaviour by nothing. Meanwhile GoGuardian's own figure is 4.6 alerts per
   student per year, and a six-day census of 4,400 children produced 9,387 flags with **zero**
   genuine suicide references.

8. **IEP services must be "based on peer-reviewed research to the extent practicable"
   (34 CFR §300.320(a)(4)), and ED reads that as an obligation to *use methods research
   has shown to be effective, to the extent such methods are available* (71 FR 46665).**
   Cross this with H1's census — zero RCTs of generative AI with students with
   disabilities — and the conclusion is unavoidable: **an AI tutor is not currently a
   defensible IEP service line.** It can be the *delivery mechanism* for a service whose
   method has a research base. It cannot itself be the method.

---

## 1. What an AI can genuinely take off a coordinator's plate (and the constraint carried in the same breath)

Leading with this because it is the true finding and because the prohibitions are more
credible once the opportunity is stated honestly.

| Task | Why it is takeable | The constraint that rides along |
|---|---|---|
| **Drafting PLAAFP prose from data the team already holds** | The PLAAFP is a *summary of existing evidence*. Assembling probe scores, work samples, observations and parent input into readable prose is transcription and synthesis, not judgement. | Every clause must be traceable to a source datum. §300.320(a)(1) requires the statement to say **how the disability affects involvement and progress in the general education curriculum** — that is an inference about a specific child and must be a human's inference. |
| **Checking goals for measurability** | Goal quality is a *formal* property: does it name a condition, an observable behaviour, a criterion, and a timeframe? This is exactly what a language model is good at. | The AI checks form. It does not choose the target, the criterion level, or whether the goal is ambitious enough — *Endrew F.* makes ambition a substantive legal question. |
| **Deadline and timeline tracking** | 60-day evaluation clock (§300.301(c)(1)), 30-day IEP-development clock (§300.323(c)(1)), annual review (§300.324(b)(1)(i)), triennial reevaluation (§300.303(b)(2)), 10-school-day manifestation clock (§300.530(e)(1)). These are arithmetic. | Missing a timeline is the most common compliance failure and the easiest to automate away. Automating it does not transfer the duty; the agency still owns it. |
| **Meeting-notice logistics and the §300.322(d) paper trail** | §300.322(d) requires "detailed records of telephone calls made or attempted," correspondence copies, visit records, if a meeting proceeds without a parent. This is a logging problem. | The record must be true. A generated record of an attempt that did not happen is fabrication of a compliance artefact. |
| **Translation and plain-language rendering** | §300.503(c) requires notices "written in language understandable to the general public" and provided "in the native language of the parent or other mode of communication." | §300.503(c)(2)(iii) requires **written evidence** that an oral translation happened and that the parent understood. Machine translation produces the artefact; it does not produce the evidence of understanding. |
| **Progress-report generation against graphed goals** | §300.320(a)(3)(ii) requires periodic progress reports concurrent with report cards. Rendering probe data against a goal line is pure computation. | H1's CBM-plus-expert-system result applies: the report is inert unless it carries a *prescribed change*. And the change is the team's. |
| **Preparing the parent** | Nothing in IDEA restricts helping a parent understand their own child's data before a meeting. | This is the highest-leverage, least-regulated use in the whole domain and is almost entirely unbuilt. |
| **Cross-checking internal consistency of the IEP** | Do the services listed support the goals? Does the LRE justification in §300.320(a)(5) actually correspond to the minutes in the services grid? Is there a goal for every area of identified need? | Inconsistency is the fingerprint of an IEP that will not survive a hearing. Detecting it is a diff; fixing it is a team decision. |

`INFERENCE` on the allocation; `STATUTE` on every citation. The pattern is consistent:
**an AI may operate on the document, on the calendar, and on the data. It may not operate
on the child's entitlement.**

---

## 2. The IEP document, part by part

### 2.1 The statutory content list

`STATUTE` — **34 CFR §300.320(a)**, verbatim, eCFR snapshot 2026-07-01:

> "As used in this part, the term *individualized education program* or *IEP* means a
> written statement for each child with a disability that is **developed, reviewed, and
> revised in a meeting** in accordance with §§ 300.320 through 300.324, and that must
> include— (1) A statement of the child's present levels of academic achievement and
> functional performance, including— (i) How the child's disability affects the child's
> involvement and progress in the general education curriculum (i.e., the same curriculum
> as for nondisabled children) […] (2)(i) A statement of measurable annual goals,
> including academic and functional goals designed to— (A) Meet the child's needs that
> result from the child's disability to enable the child to be involved in and make
> progress in the general education curriculum; and (B) Meet each of the child's other
> educational needs that result from the child's disability; (ii) For children with
> disabilities who take alternate assessments aligned to alternate academic achievement
> standards, a description of benchmarks or short-term objectives; (3) A description of—
> (i) How the child's progress toward meeting the annual goals described in paragraph (2)
> of this section will be measured; and (ii) When periodic reports on the progress the
> child is making toward meeting the annual goals (such as through the use of quarterly or
> other periodic reports, concurrent with the issuance of report cards) will be provided;
> (4) A statement of the special education and related services and supplementary aids and
> services, **based on peer-reviewed research to the extent practicable**, to be provided
> to the child, or on behalf of the child, and a statement of the program modifications or
> supports for school personnel that will be provided […] (5) An explanation of the
> extent, if any, to which the child will not participate with nondisabled children in the
> regular class […] (6)(i) A statement of any individual appropriate accommodations that
> are necessary to measure the academic achievement and functional performance of the
> child on State and districtwide assessments […] (7) The projected date for the beginning
> of the services and modifications described in paragraph (a)(4) of this section, and the
> anticipated **frequency, location, and duration** of those services and modifications."

Plus (b) transition services no later than the first IEP in effect when the child turns
16, and (c) transfer of rights at majority.

**Nine components. That is the whole legal specification.** Everything else practitioners
argue about — the state's form, the district's template, the drop-downs in the compliance
system — is local accretion. §300.320(d) says so explicitly: nothing requires additional
information "beyond what is explicitly required in section 614 of the Act."

That matters for AI design more than it first appears. **The document a coordinator
actually fills in is mostly not required by federal law.** A large fraction of the
paperwork burden this report quantifies in §7 is state and vendor-imposed, which means it
is also, in principle, negotiable — a fact almost never surfaced in product discussions.

### 2.2 Who writes each part

`STATUTE` — **34 CFR §300.321(a)**: the team **must** include (1) the parents; (2) not less
than one regular education teacher of the child, if the child is or may be participating
in the regular education environment; (3) not less than one special education teacher or
provider of the child; (4) a public agency representative qualified to provide or
supervise specially designed instruction, knowledgeable about the general education
curriculum and about agency resources; (5) an individual who can interpret the
instructional implications of evaluation results; (6) at the discretion of parent or
agency, others with knowledge or special expertise; and (7) **whenever appropriate, the
child**.

In practice, and this is what an outsider gets wrong:

| Part | Who typically drafts it | Who legally owns it |
|---|---|---|
| PLAAFP | Case manager, assembling from school psychologist's report, related-service providers' reports, general-ed teacher input, parent input | The team, in the meeting |
| Annual goals | Case manager + relevant service provider (SLP writes speech goals, OT writes OT goals) | The team |
| Services grid (type, frequency, location, duration) | Case manager, constrained by what the district can staff | The team — but see §4.5 on the staffing/LRE collision |
| Accommodations | Case manager + general-ed teacher | The team |
| State-assessment participation | Case manager, per state rules | The team |
| LRE justification (§300.320(a)(5)) | Case manager | The team |
| Transition (age 16+) | Transition specialist or case manager, with the student | The team, and the student must be invited (§300.321(b)(1)) |
| Prior written notice | The agency — usually the case manager or the administrator/LEA representative | The **public agency**, not the team |

Note the last row. **PWN is not a team document.** It is the agency's unilateral statement
of what it proposes or refuses and why. Conflating it with the IEP is the most common
outsider error and it inverts who the accountable party is.

`STATUTE` — §300.321(e) permits a team member to be excused, in whole or in part, if the
parent and agency agree in writing and — where the member's area is being modified or
discussed — the member submits **written input in advance**. ED's own impact analysis
found this saves nothing: *"The change is unlikely to generate notable savings because
reduced time spent in meetings is likely to be offset by the time required to draft
written input, send it to the parents and other IEP Team members, and secure the consent
of parents and public agency to the excusal"* (71 FR 46843). `OBSERVED` — a documented
null result on a paperwork-reduction provision, and the first of several.

### 2.3 PLAAFP — the anchor

**What it is.** The Present Levels of Academic Achievement and Functional Performance is
the only part of the IEP that describes the child rather than the plan. Everything
downstream is supposed to be derivable from it: goals address the needs it identifies,
services deliver the goals, accommodations address the access barriers it names, and the
LRE statement justifies removal by reference to needs it documents.

**What legal sufficiency requires**, reading §300.320(a)(1) with §300.305(a)(2)(ii) and
the 2006 preamble:

1. **Both academic achievement and functional performance.** Not optional per child. ED
   rejected the request to make functional statements discretionary: *"We cannot make the
   changes requested by the commenters. Section 614(d)(1)(A)(i)(I) of the Act requires an
   IEP to include a statement of the child's present levels of academic achievement and
   functional performance"* (71 FR 46662). `STATUTE`
2. **The effect-of-disability statement.** §300.320(a)(1)(i) requires it to state *how the
   disability affects involvement and progress in the general education curriculum.* ED:
   *"The IEP Team's determination of how the child's disability affects the child's
   involvement and progress in the general education curriculum is a primary consideration
   in the development of the child's annual IEP goals"* (71 FR 46662). `STATUTE`
3. **Baseline data specific enough to write a measurable goal against.** This is not
   spelled out in §300.320 but is forced by it: a goal cannot be measurable if there is no
   present level to measure from. ED declined to require formal alignment language,
   holding that the correspondence between §300.320(a)(1)(i) and §300.320(a)(2)(i)(A) is
   already explicit (71 FR 46662–63). `STATUTE`
4. **Coverage of every area of identified need**, because §300.304(b)(6) requires the
   evaluation to be "sufficiently comprehensive to identify all of the child's special
   education and related services needs, **whether or not commonly linked to the
   disability category** in which the child has been classified." `STATUTE`

**Documented failure modes.** Empirical audits of IEP quality are covered in §2.7; the
recurring structural failures a coordinator would name are: PLAAFPs written as narrative
prose with no numbers, so no goal can be anchored; PLAAFPs copied forward year to year
with the date changed; PLAAFPs that describe the disability category rather than the
child's performance; and PLAAFPs that omit functional performance entirely for
"academic-only" cases, which is a facial violation of §300.320(a)(1).

**The AI reading.** PLAAFP drafting is the single best-fit task in the entire document for
a language model — it is summarisation of held evidence into constrained prose — *and* it
is the part where a fluent, plausible, unsourced paragraph does the most damage, because
everything downstream inherits its errors. The design answer is not "don't draft PLAAFPs."
It is: **every sentence carries its source, and any sentence the model cannot source is
rendered as a gap for a human to fill, not as prose.**

### 2.4 Measurable annual goals

**Required by statute:** goals must be *measurable*, must be *annual*, must include
*academic and functional* goals, and must be designed both to enable progress in the
general education curriculum and to meet other disability-related needs
(§300.320(a)(2)(i)). Progress toward them must have a stated *measurement method* and a
stated *reporting schedule* (§300.320(a)(3)).

**What the statute does *not* require**, and this surprises people: goals need not be
discipline-specific, need not name a specific assessment instrument, and need not have
short-term objectives. ED, verbatim: *"The Act does not require goals to be written for
each specific discipline or to have outcomes and measures on a specific assessment tool"*
(71 FR 46663). `STATUTE`

**The short-term objectives change is a live, quantified example of paperwork policy.**
IDEA 2004 removed benchmarks/short-term objectives for all children **except** those
taking alternate assessments aligned to alternate achievement standards
(§300.320(a)(2)(ii)). ED's own arithmetic: 486,000 children still required them; 6.461
million no longer did; at $48/hour teacher compensation, *"a reduction in time as modest
as 15 minutes could save approximately $12 per IEP or $77.5 million total in opportunity
costs"* (71 FR 46843). `OBSERVED` — federal estimate, 2006 dollars, explicitly framed as
an upper bound on a 15-minute assumption.

Read that number the right way. **Fifteen minutes per IEP was worth $77.5 million a year
to the federal government's own accountants.** That is the scale at which administrative
relief in this domain operates, and it is why the administrative case for AI here is not
a small claim.

**What makes a goal legally inadequate.** The four-part practitioner test — *condition,
behaviour, criterion, timeframe* — is professional convention, not regulation; the
regulation says only "measurable." But the convention is doing real work, because a goal
lacking any of the four cannot support the §300.320(a)(3)(i) requirement to describe how
progress will be measured. The failure modes are:

- **Unmeasurable verbs.** "Will improve reading comprehension." No criterion, no
  condition, no instrument.
- **Criterion without baseline.** "Will read 90 words per minute" with a PLAAFP that gives
  no current rate — nobody can tell whether that is ambitious or already achieved.
- **Percentage-of-trials goals with no denominator.** "80% accuracy" over an unstated
  number of opportunities is not measurable.
- **Goals that restate the standard.** A goal that is simply the grade-level standard is
  not *specially designed instruction*; §300.39(b)(3) defines that as *adapting* content,
  methodology or delivery.
- **Insufficient ambition.** After *Endrew F.*, this is substantive, not stylistic. See
  §4.6.

### 2.5 The services grid

§300.320(a)(4) and (a)(7) together require: what service, based on peer-reviewed research
to the extent practicable, plus **projected start date, anticipated frequency, location,
and duration.** In practice this is the row of numbers that decides staffing, and it is
the part of the IEP that is most often written to what the district can supply rather than
to what the child needs — a tension IDEA does not acknowledge and every coordinator lives
inside.

**The peer-reviewed-research clause is the most under-read sentence in IDEA and it is
directly load-bearing for this project.** ED's interpretation, verbatim:

> "Section 612(d)(1)(A)(i)(IV) of the Act requires special education and related services,
> and supplementary aids and services, to be based on peer-reviewed research to the extent
> practicable. **States, school districts, and school personnel must, therefore, select and
> use methods that research has shown to be effective, to the extent that methods based on
> peer-reviewed research are available.** This does not mean that the service with the
> greatest body of research is the service necessarily required for a child to receive
> FAPE. Likewise, there is nothing in the Act to suggest that the failure of a public
> agency to provide services based on peer-reviewed research would automatically result in
> a denial of FAPE." (71 FR 46665) `STATUTE`

Two consequences, and the survey must state both.

1. **Where a strong research base exists (decoding, explicit instruction, CBM/DBI),
   choosing something else is legally exposed.** This is the statutory backing for H1's
   "fidelity and dosage of known-good intervention" thesis. H1 argued it from effect
   sizes; §300.320(a)(4) argues it from law.
2. **Where no research base exists — which is precisely where generative AI sits for this
   population — the clause does not forbid the service, but it does mean the service
   cannot be justified by pointing at research.** ED: *"If no such research exists, the
   service may still be provided, if the IEP Team determines that such services are
   appropriate"* (71 FR 46665). So an AI tutor can lawfully appear in an IEP. It just
   cannot appear there *on the strength of evidence*, because there isn't any. It appears
   on the strength of the team's individualised judgement, which is a much weaker and much
   more honest footing than any vendor deck admits.

### 2.6 Accommodations vs modifications — the distinction outsiders collapse

This is the distinction practitioners care about most intensely and it is almost never
handled correctly in AI products.

- **Accommodation** — changes *how* a student accesses content or demonstrates learning.
  The learning expectation and the standard are unchanged. Extended time, read-aloud of
  non-reading-target text, scribe, preferential seating, text-to-speech, reduced-distraction
  setting, chunked assignments.
- **Modification** — changes *what* the student is expected to learn or demonstrate. Fewer
  items, lower-level text, alternate standards, different grading basis, alternate
  assessment.

**Why it matters legally.** IDEA regulates the two differently and asymmetrically:

- §300.320(a)(6)(i) speaks only of **accommodations** on State and districtwide
  assessments; anything beyond that requires the **alternate assessment** route under
  (a)(6)(ii), with a written justification of why the child cannot participate in the
  regular assessment and why the particular alternate assessment is appropriate.
  `STATUTE`
- §300.116(e): *"A child with a disability is not removed from education in
  age-appropriate regular classrooms **solely because of needed modifications** in the
  general education curriculum."* `STATUTE` — modifications are not a placement
  justification.
- §300.323(d)(2)(ii) requires every teacher and provider to be informed of *"the specific
  accommodations, modifications, and supports that must be provided."* `STATUTE`
  Non-implementation is a FAPE issue, and under §300.530(e)(1)(ii) it is also a
  manifestation-determination trigger — see §8.4.

**Why it matters practically.** Modifications accumulate. A student on modified curriculum
across four years of high school may not be on a diploma track, and families are
frequently not told this in those words. **An AI that silently modifies — shortens a task,
lowers text complexity, reduces the item count, accepts a partial answer as complete — has
made a curricular decision reserved to the team, and has made it invisibly.** That is a
sharper prohibition than "don't write the IEP," and it is the one most likely to be
violated by a well-meaning adaptive system.

The design consequence is concrete: **a system serving this population must be able to
state, for every adaptation it applies, whether that adaptation is an accommodation or a
modification, and must refuse to apply modifications that are not in the IEP.** Adaptive
difficulty, as universally shipped, cannot answer that question about itself.

`INFERENCE`, but tightly constrained by the three cited provisions.

**And there is one measured reason to hold the line that has nothing to do with law.**
`MEASURED-QUASI` — Sahli Lozano, Brandenberg, Ganz & Wüthrich (2022), *Educational Research
and Evaluation* 27(5–6), DOI 10.1080/13803611.2022.2103571, multilevel analysis across **110
lower-secondary classes**: students with *"reduced learning objectives […] or individual
support by a special education teacher get systematically underestimated by their teachers
regarding their cognitive abilities, **although this is NOT the case for students receiving
accommodations**."* **Modifications carry a measurable teacher-expectancy penalty;
accommodations do not.** The distinction practitioners defend so fiercely turns out to have an
effect size attached to it.

### 2.6b Do accommodations actually work? The evidence is far weaker than the practice

This is the largest null-result cluster in the report and it is uncomfortable, because
accommodations are the single most widely deployed intervention in American special education.

**The "interaction hypothesis" — that an accommodation helps students with disabilities and
not others — did not survive testing.** `MEASURED-META` — Sireci, Scarpati & Li (2005),
*Review of Educational Research* 75(4):457–490, DOI 10.3102/00346543075004457, verbatim:
*"Consistent conclusions were not found across studies… But two consistent findings emerged:
**Extended time tended to improve the performance of all students**, although students with
disabilities tended to exhibit relatively greater score gains; and oral accommodations on math
tests were associated with increased test performance for **some** students with
disabilities."* The field retreated to the weaker "differential boost" claim — the
accommodation helps *both* groups but helps disabled students *more*.

**Even the weaker claim holds only about a third to a half of the time.** `MEASURED` (review
tallies, via NCEO Report 412, ERIC ED600669): Kettler (2015) found differential boost supported
in **8 of 19** extended-time tests (42%), **11 of 19** oral-delivery tests (58%), **6 of 9**
accommodation bundles (67%). Lane & Leventhal (2015), verbatim: *"of the **11 studies**
examining the possibility of differential boosts for students with disabilities using
accommodations, **four studies** reported evidence demonstrating differential boosts"* — 36%,
falling to **30%** for middle/high school and **30%** for mathematics.

**The differential for extended time is small enough to be a validity problem.**
`MEASURED-META` — Chiu & Pearson (1999), ERIC ED433362, k = 30 studies: target population
(students with disabilities plus English learners) **g = 0.16**; general-education students
**g = 0.06**; **differential 0.10**. By accommodation type, the *relative* effect for
extended time was **+0.07**; response-format accommodations **−0.11** and accommodation
combinations **−0.17** — i.e. general-education students benefited *more*. `INFERENCE` — on a
target-group extended-time effect of roughly 0.31–0.37 against a differential of 0.07,
approximately **80% of the extended-time boost accrues to students without disabilities.**
That is not an accommodation; that is a change to the test.

**Two large meta-analyses return overall nulls.**

`MEASURED-META` — Kieffer, Lesaux, Rivera & Francis (2009), *Review of Educational Research*
79(3):1168–1201, DOI 10.3102/0034654309332490 (numbers from the identical technical-report
version, Francis et al. 2006, ERIC ED517792). **37 randomized samples, 7 accommodations**,
fixed effects:

| Accommodation | k | g | 95% CI | p |
|---|---|---|---|---|
| English dictionary/glossary | 11 | **.146** | [.063, .230] | **.001** |
| Simplified English | 15 | .020 | [−.064, .104] | .637 **null** |
| Extra time | 2 | .209 | [−.069, .488] | .141 **null** |
| Bilingual dictionary/glossary | 5 | −.096 | [−.223, .031] | .139 **null** |
| Spanish version | 2 | **−.263** | [−.463, −.062] | **.010 negative** |
| **OVERALL** | **37** | **.034** | **[−.016, .084]** | **.180 null** |

Authors' verdict, verbatim: *"**The results in Table 2 tell a somewhat disheartening story. Of
the seven types of accommodations used, only one had an overall positive effect on ELL
outcomes.**"* And a moderator finding that should chasten any bundling instinct: the one
effective accommodation got **worse** when combined with the popular one — English dictionary
*without* extra time g = .238, *with* extra time g = .074.

`MEASURED-META` — Rios, Ihlenfeldt & Chavez (2020), *Educational Measurement: Issues and
Practice*, ERIC EJ1276694. **26 studies, 95 effect sizes, N = 11,069.** Overall +0.16 SD, but
verbatim: *"**none of the accommodations investigated were found to have intervention effects
that were statistically different from zero**."* Conclusion: currently employed accommodations
*"lack evidence of their effectiveness."*

**Read-aloud is the strongest case, and it inverts with age.** `MEASURED-META` — Li (2014),
*EMIP* 33(3), DOI 10.1111/emip.12027, 114 effect sizes across 23 studies: both groups
benefited, the disability effect significantly larger, stronger for reading than mathematics.
Buzick & Stone (2014), *EMIP* 33(3), DOI 10.1111/emip.12040, verbatim: *"the read aloud
accommodation increases reading test scores for **both groups, but more so for students with
disabilities**, and […] mathematics score gains… are **small for both**."*

But the primary studies keep returning nulls, and one returns a reversal:

- `MEASURED` **Meloy, Deville & Frisbie (2002)**, ERIC EJ652089, N = 260: *"Students with
  learning disabilities in reading, **as well as those without**, exhibited statistically
  significant gains with the read aloud test administration. **Interaction effects were not
  significant.**"*
- `MEASURED` **Elbaum, Arguelles, Campbell & Saleh (2004)**, *Exceptionality* 12(2), N = 311
  (230 with LD): *"students' test performance **did not differ in the 2 conditions**, and
  **students with LD did not benefit more from the accommodation than students without LD.**
  However, students with LD… were **almost twice as likely** as students without LD to show a
  substantive change in test performance **in either the positive or negative direction**."*
- `MEASURED` **★ Elbaum (2007)**, *Journal of Special Education* 40(4), ERIC EJ758191, N = 625
  secondary students (388 with LD), oral accommodation on mathematics: *"**students without
  disabilities benefited significantly more from the accommodation (ES = 0.44) than students
  with LD (ES = 0.20).**"* Her pooled analysis found the boost favours LD students at
  elementary level and *"for **secondary** students, **the converse was true**."*
  **Differential boost inverts with age.**
- `MEASURED` **McKevitt & Elliott (2003)**, ERIC EJ823576: accommodation packages *"had
  **minimal benefit** […] and **did not differentially benefit one group of students over
  another**,"* with the authors noting *"**reading aloud a reading test may have an
  invalidating effect**."*
- `MEASURED` **Fuchs, Fuchs, Eaton, Hamlett, Binkley & Crouch (2000)**, ERIC EJ613002, N = 181
  LD + 184 non-LD: LD students *"profited differentially from reading aloud **but NOT from
  extended time or large print**."*

**For balance, the one clean positive.** `MEASURED-RCT` — Fletcher et al. (2006), *Exceptional
Children*: grade-3 students with dyslexic decoding difficulty versus average decoders,
randomly assigned. *"**Only** students with decoding problems benefited… a significant increase
in average performance and a **7-fold increase in the odds of passing**."* The interaction
hypothesis held — **with a narrowly and objectively defined deficit and an accommodation
targeted precisely to that deficit.** That is the specification under which accommodations
work, and it is not how they are assigned.

**Because assignment is at chance.** `MEASURED` — **★ Helwig & Tindal (2003)**, *Exceptional
Children* 69(2), ERIC EJ659301, **N = 1,218** (973 general education, 245 special education),
experimental: *"**Teachers were no more successful than chance at predicting which students
would benefit from the accommodation. A developed student profile did not match accommodation
outcomes.**"*

**And the reason profiling cannot fix it is structural.** `MEASURED-RCT` — Ketterlin-Geller,
Yovanoff & Tindal (2007), *Exceptional Children*, ERIC EJ757111: grade-3 mathematics —
lower-reading students differentially benefited from read-aloud **only on items with high
mathematics difficulty *and* high linguistic complexity**, and did not benefit at all from
simplified language. `INFERENCE` — **benefit is item-conditional, not student-conditional.** A
student-level blanket assignment is mis-specified by construction, and no amount of better
learner modelling repairs a mis-specification of that kind.

Corroborating the practice gap: `OBSERVED` — Weis, Dean & Osborne (2016), *Journal of Learning
Disabilities* 49(5), DOI 10.1177/0022219414559648, document audit: *"**Many of their
recommendations for accommodations were not supported by objective evidence** from students'
history, diagnosis, test data, and current functioning… **clinicians often recommended
accommodations that were not specific to the student's diagnosis or area of disability.**"* And
Crawford & Ketterlin-Geller (2013), ERIC EJ995079, interviews with 20 special-education
teachers across five states: *"a **general lack of knowledge about the theoretical and
empirical basis** for making accommodation assignment decisions."*

**A documented federal absence.** `OBSERVED` — the What Works Clearinghouse product catalogue
at `ies.ed.gov/ncee/wwc/` (HTTP 200) lists **all 30 Practice Guides** from 2007 to December
2024. **None addresses testing or instructional accommodations for students with
disabilities.** The catalogue holds 619 Intervention Reports and 1,949 study reviews, with 509
tagged to the "Children and Youth with Disabilities" population facet — and **no accommodations
topic in the taxonomy at all.** `INFERENCE` on the mechanism: WWC review protocols are built
for between-subjects intervention designs, while the accommodations literature is dominated by
within-subject counterbalanced designs that fall outside WWC group-design standards. The
federal evidence clearinghouse has certified nothing about a practice applied to millions of
students every year.

**What this means for the survey, stated without softening.** `survey/04` argues that AI's job
at the margin is fidelity and dosage of known-good intervention. **Accommodations are not
known-good intervention.** They are a legally mandated, universally deployed practice with a
weak, inconsistent, sometimes-reversed evidence base, assigned by professionals performing at
chance, conferring benefit that is conditional on item properties nobody profiles. An AI that
faithfully delivers a student's accommodations is doing something legally required and
evidentially unsupported, and the survey should say both halves. `INFERENCE`.

### 2.7 Progress reporting

§300.320(a)(3) requires the IEP to state *how* progress toward each annual goal will be
measured and *when* periodic reports will be provided — the statutory example is
"quarterly or other periodic reports, concurrent with the issuance of report cards."
§300.324(b)(1)(ii)(A) then requires the team to revise the IEP to address *"any lack of
expected progress toward the annual goals."*

That pair is the legal skeleton of exactly the loop H1 established empirically: measure,
compare to goal line, and — crucially — **act**. IDEA requires the revision. H1's Fuchs
CBM-plus-expert-system trial says the revision only helps when it is *prescribed* rather
than merely *triggered*. The statute and the RCT agree, which is rare enough to be worth
saying in the survey.

**The documented failure mode** is progress reports that report *effort* or *participation*
rather than performance against the goal's stated criterion, and progress reports that
mark "progressing" for four quarters and then, at the annual review, discover the goal was
not met. A coordinator will recognise this immediately. It is also the single easiest
thing on this list for an AI to fix, because the fix is arithmetic against a stated
criterion.

---

## 3. IDEA vs Section 504 vs ADA — three statutes, three eligibility standards, three procedural regimes

Outsiders treat a 504 plan as a lightweight IEP. It is not; it is a different legal
instrument under a different statute with a different theory of the case. IDEA is a
**funding statute with an entitlement attached** — a state accepts Part B money and owes
FAPE. Section 504 and ADA Title II are **civil-rights statutes** — they forbid
discrimination on the basis of disability, and the remedy is non-discrimination, not a
programme.

### 3.1 The eligibility gate

| | **IDEA (Part B)** | **Section 504** | **ADA Title II** |
|---|---|---|---|
| Authority | 20 U.S.C. §1400 et seq.; **34 CFR Part 300** | 29 U.S.C. §794; **34 CFR Part 104** (ED's implementing regs) | 42 U.S.C. §12131 et seq.; **28 CFR Part 35** |
| Who is covered | A child with **one of 13 enumerated conditions** (§300.8(a)(1)) **who, by reason thereof, needs special education and related services** | Any person with a physical or mental impairment that **substantially limits a major life activity**, has a record of such, or is regarded as having one | Same disability definition as 504 as amended by the ADAAA |
| Trigger for services | Both prongs: a listed condition **and** need for specially designed instruction | Substantial limitation only — no category list, no requirement of specially designed instruction | Same |
| What is owed | FAPE via an IEP; specially designed instruction; related services | FAPE defined as regular or special education **and related aids and services** designed to meet individual needs as adequately as the needs of nondisabled persons are met | Program access, effective communication, reasonable modifications |
| Applies to | LEAs receiving Part B funds | **Any recipient of federal financial assistance** — including private schools that take federal money | **All** state and local government entities, funded or not |
| Federal funding attached | Yes | **No** | **No** |

`STATUTE` on the IDEA column. **34 CFR §300.8(a)(1)**, verbatim, is the thirteen-category
gate:

> "*Child with a disability* means a child evaluated in accordance with §§ 300.304 through
> 300.311 as having an intellectual disability, a hearing impairment (including deafness),
> a speech or language impairment, a visual impairment (including blindness), a serious
> emotional disturbance (referred to in this part as 'emotional disturbance'), an
> orthopedic impairment, autism, traumatic brain injury, an other health impairment, a
> specific learning disability, deaf-blindness, or multiple disabilities, **and who, by
> reason thereof, needs special education and related services**."

And the two-prong logic is made explicit at §300.8(a)(2)(i): a child who has one of the
conditions but *"only needs a related service and not special education, […] is not a child
with a disability under this part."*

**States may add a fourteenth route:** §300.8(b) permits, at state option, a
*developmental delay* category for children aged 3 through 9 (or a subset). Some states
use it, some do not, and §300.111(b)(4) forbids an LEA from using the term if the state has
not adopted it. This is why "there are thirteen categories" is true federally and
incomplete locally.

### 3.2 Why a 504 plan is not a small IEP

Four structural differences, all of which a coordinator will name:

1. **No specially designed instruction requirement.** A 504 plan delivers *access*.
   Extended time, seating, a nurse's health plan, a bathroom pass, an elevator key. If a
   child needs their instruction *adapted*, they need IDEA, and a 504 plan that is
   quietly delivering adapted instruction is a district doing IDEA work without IDEA
   protections.
2. **Broader gate, thinner procedure.** Anyone substantially limited qualifies. But the
   procedural apparatus of Part 300 — prior written notice, the 60-day evaluation clock,
   the composed team, stay-put, IEE at public expense as of right — does not transfer to
   Part 104. §104.36 requires a system of procedural safeguards including notice, record
   review, an impartial hearing with parent participation and counsel, and a review
   procedure — and expressly permits compliance with IDEA's procedures as one way to
   satisfy it. Many districts therefore run 504 on a thin local process.
3. **No federal money and no federal count.** IDEA Part B child count is reported annually
   under Section 618. Section 504-only students are not in it. They surface, if at all, in
   OCR's Civil Rights Data Collection. Any product sizing "students with disabilities" off
   the IDEA count is systematically undercounting the population it will actually serve.
4. **Different enforcement.** IDEA disputes go to due process hearings under §§300.507–300.518
   and then to court. 504/ADA complaints go to OCR, or to court. The remedial vocabulary
   differs: compensatory education and tuition reimbursement under IDEA; injunctive relief
   and, under Title II, damages.

### 3.3 The exhaustion question — and why it changed

The practically important interaction is: when must a family run IDEA's due process
machinery before suing under 504/ADA? Two Supreme Court decisions govern — *Fry* (2017)
supplies a **gravamen** test and *Perez* (2023) an independent **remedy-availability** test.
Both are set out with verbatim holdings at **§10.5**, with the consequence that a family
seeking damages may bypass IDEA's administrative process entirely.

**The verbatim 504 provisions**, for the record, because practitioners argue about them and
paraphrases drift. `STATUTE` — eCFR snapshot 2026-07-01:

**§104.33(b)(1)** — the 504 definition of appropriate education:

> "the provision of regular or special education and related aids and services that (i) are
> designed to meet individual educational needs of handicapped persons **as adequately as the
> needs of nonhandicapped persons are met** and (ii) are based upon adherence to procedures
> that satisfy the requirements of §§ 104.34, 104.35, and 104.36."

And **§104.33(b)(2)**: *"Implementation of an Individualized Education Program developed in
accordance with the Education of the Handicapped Act is **one means** of meeting the standard."*
Note the comparative standard — 504 asks whether the child's needs are met *as adequately as*
a nondisabled child's. That is a different question from IDEA's *Endrew F.* progress standard,
and it is why a 504 plan is not a small IEP but a different instrument answering a different
question.

**§104.34(a)** — the 504 LRE analogue, materially identical in structure to §300.114(a)(2):

> "A recipient shall place a handicapped person in the regular educational environment operated
> by the recipient **unless it is demonstrated by the recipient that the education of the person
> in the regular environment with the use of supplementary aids and services cannot be achieved
> satisfactorily.**"

**§104.35(b)(1)** — evaluation, and note the wording, which is *tighter* than IDEA's on
instrument validity:

> "Tests and other evaluation materials have been **validated for the specific purpose for which
> they are used** and are administered by trained personnel **in conformance with the
> instructions provided by their producer**."

**§104.36** — the entire procedural regime, in one sentence:

> "A recipient […] shall establish and implement, with respect to actions regarding the
> identification, evaluation, or educational placement of persons who, because of handicap, need
> or are believed to need special instruction or related services, **a system of procedural
> safeguards that includes notice, an opportunity for the parents or guardian of the person to
> examine relevant records, an impartial hearing with opportunity for participation by the
> person's parents or guardian and representation by counsel, and a review procedure.**
> Compliance with the procedural safeguards of section 615 of the Education of the Handicapped
> Act is **one means** of meeting this requirement."

**Compare the length.** IDEA's procedural safeguards run from §300.500 to §300.536 — 37
sections. Section 504's run to one sentence with four elements. **There is no PWN equivalent in
Part 104, no 60-day clock, no composed team, no stay-put, and no IEE-at-public-expense right.**
A district may voluntarily import IDEA's procedures, and many do — but where it has not, a
system built to IDEA's procedural assumptions will demand artefacts that do not exist and that
nobody is obliged to produce.

### 3.4 The ADA Title II web rule — and the date almost every secondary source has wrong

This is where a stale source would have burned this project a second time.

`STATUTE` — **28 CFR §35.200(b)**, eCFR snapshot 2026-07-01, verbatim:

> "(1) **Beginning April 26, 2027**, a public entity, other than a special district
> government, with a total population of 50,000 or more shall ensure that the web content
> and mobile apps that the public entity provides or makes available, directly or through
> contractual, licensing, or other arrangements, comply with Level A and Level AA success
> criteria and conformance requirements specified in **WCAG 2.1** […]
> (2) **Beginning April 26, 2028**, a public entity with a total population of less than
> 50,000 or any public entity that is a special district government shall ensure […]"

Source note in the section: *"[AG Order No. 5919-2024, 89 FR 31337, Apr. 24, 2024, as
amended by AG Order No. 6742-2026, **91 FR 20912, Apr. 20, 2026**]"*.

Confirmed against the Federal Register API: **91 FR 20902 (2026-04-20)**, DOJ interim final
rule, abstract verbatim: *"The compliance date for State and local government entities with
a total population of 50,000 or more is extended from April 24, 2026, to April 26, 2027.
The compliance date for public entities with a total population of less than 50,000, or any
special district government, is extended from April 26, 2027, to April 26, 2028."*
`STATUTE`

HHS did the same for its own Section 504 web rule three weeks later: **91 FR 25496
(2026-05-11)**, extending compliance from 2026-05-11 to **2027-05-11** (recipients with 15+
employees) and from 2027-05-10 to **2028-05-10** (fewer than 15). `STATUTE`

Four things follow, and they are all consequential for this project:

1. **The binding federal standard for public-school web content and mobile apps is WCAG
   2.1 Level AA, not 2.2.** The rule incorporates WCAG 2.1 by reference, naming the 2018
   W3C Recommendation explicitly. H1's WCAG 2.2 AA floor is *higher than the law* and
   should be described that way — as a deliberate choice, not as compliance.
2. **The deadlines moved by twelve months in April–May 2026 and most published guidance
   still says April 2026.** Any survey text asserting a 2026 deadline is now wrong.
3. **§35.200(a) covers content provided "directly or through contractual, licensing, or
   other arrangements."** A district that licenses an inaccessible edtech product has not
   outsourced the obligation. This is the single most commercially relevant sentence in
   the rule for anyone building in this space.
4. **§35.201(d) exempts "individualized, password-protected or otherwise secured
   conventional electronic documents"** about a specific individual. A PDF of one child's
   IEP behind a login is exempt. The parent portal that serves it is not.

---

## 4. LRE — Least Restrictive Environment

### 4.1 The requirement

`STATUTE` — **34 CFR §300.114(a)(2)**, verbatim:

> "Each public agency must ensure that— (i) **To the maximum extent appropriate**, children
> with disabilities, including children in public or private institutions or other care
> facilities, are educated with children who are nondisabled; and (ii) Special classes,
> separate schooling, or other removal of children with disabilities from the regular
> educational environment occurs **only if the nature or severity of the disability is such
> that education in regular classes with the use of supplementary aids and services cannot
> be achieved satisfactorily.**"

Note the structure: a strong presumption of the regular class, rebuttable only by a
showing that **supplementary aids and services have been considered and are insufficient.**
The burden is on removal, and the test is not "would a special class be better" but "can
the regular class work *with supports*."

### 4.2 The continuum

`STATUTE` — **§300.115**: each public agency must ensure a continuum of alternative
placements is available; it must include the placements named in the §300.39 definition of
special education — *"instruction in regular classes, special classes, special schools,
home instruction, and instruction in hospitals and institutions"* — and must "make
provision for supplementary services (such as resource room or itinerant instruction) to
be provided in conjunction with regular class placement."

**A continuum, not a ladder.** Nothing requires a child to fail at one rung before
accessing the next, and there is no federal "least restrictive first, then escalate" rule.
That is a widespread practitioner myth and a system that encodes it encodes a legal error.

### 4.3 How placement is decided

`STATUTE` — **§300.116**, verbatim in the operative parts:

> "(a) The placement decision— (1) Is made by a group of persons, **including the parents**,
> and other persons knowledgeable about the child, the meaning of the evaluation data, and
> the placement options […] (b) The child's placement— (1) Is determined at least annually;
> (2) **Is based on the child's IEP**; and (3) Is as close as possible to the child's home;
> (c) Unless the IEP of a child with a disability requires some other arrangement, the child
> is educated in the school that he or she would attend if nondisabled; (d) In selecting the
> LRE, consideration is given to any **potential harmful effect** on the child or on the
> quality of services that he or she needs; and (e) A child with a disability is **not
> removed from education in age-appropriate regular classrooms solely because of needed
> modifications** in the general education curriculum."

The sequencing in (b)(2) is the thing outsiders reverse. **The IEP is written first; the
placement follows from it.** Writing the placement first and then reverse-engineering an
IEP to fit the available programme is a recognised violation pattern.

### 4.4 What "placement" actually means

`STATUTE`/preamble — ED, 71 FR 46588, verbatim:

> "The terms 'educational placement' and 'placement' are used throughout the Act, and we
> have followed the language of the Act whenever possible. We do not believe it is
> necessary to define 'educational placement.' […] **The Department's longstanding position
> is that placement refers to the provision of special education and related services rather
> than a specific place, such as a specific classroom or specific school.**"

This is the most important sentence in this report for AI design, and it should appear in
the survey verbatim. It means:

- **Changing which classroom a child sits in is often *not* a change of placement.**
- **Changing the services — type, frequency, duration — often *is*,** even if the child
  never moves rooms.
- Therefore an AI that adjusts *how much* of a service a child receives is operating on
  placement, and an AI that adjusts *where a lesson is delivered* may not be.

### 4.5 The genuine unresolved conflict: LRE vs intensity

IDEA presumes the regular class. The intervention evidence base H1 assembled — explicit,
systematic, small-group, high-dosage instruction — is overwhelmingly evidence about
*pulling children out* and teaching them intensively. The statute pushes one way; the
effect sizes push the other. There is no clean resolution and the survey should stop
pretending there is.

Three things sharpen it rather than resolve it:

1. **H1's RTI regression-discontinuity result cuts *for* LRE.** Grade-1 students just below
   the screening cut, assigned to reading intervention, had *lower* spring scores than
   those just above. The proposed mechanism was that intervention pulled children out of
   effective core instruction. That is an opportunity-cost argument, and it is exactly the
   argument §300.114(a)(2)(ii) encodes in law. The statute and the null result agree.
2. **§300.116(d)** requires consideration of *"any potential harmful effect on the child
   **or on the quality of services** that he or she needs."* The regulation itself
   acknowledges that inclusion can degrade service quality. It requires the trade-off to
   be *considered*, not resolved in either direction.
3. **This is where an AI's contribution is real and non-obvious.** The reason pull-out is
   the default delivery mode for intensive intervention is a staffing constraint, not a
   pedagogical one: you cannot give one child forty minutes of explicit decoding
   instruction inside a class of thirty without removing them. A system that can deliver
   fidelity and dosage *without physical removal* is not a marginal convenience — it
   attacks the exact mechanism that forces the LRE trade-off. **That is the strongest
   forward-looking claim in this entire report, and it is a hypothesis, not a finding.**
   `INFERENCE` — no trial has tested it.

### 4.6 The substantive standard the placement must meet

*Endrew F.* and *Rowley* set the substantive FAPE standard and the two-part inquiry; the
circuit LRE tests (*Roncker*, *Daniel R.R.*, *Rachel H.*, *Oberti*, *Hartmann*) are the
frameworks courts actually apply. These are set out with verbatim holdings in the case-law
block at §10.

---

## 5. Prior Written Notice, consent, and the procedural safeguards

### 5.1 PWN — what it is and when it must issue

`STATUTE` — **34 CFR §300.503**, verbatim and complete on the operative parts:

> "(a) *Notice.* Written notice that meets the requirements of paragraph (b) of this section
> must be given to the parents of a child with a disability **a reasonable time before** the
> public agency— (1) **Proposes to initiate or change** the identification, evaluation, or
> educational placement of the child or the provision of FAPE to the child; or (2)
> **Refuses to initiate or change** the identification, evaluation, or educational placement
> of the child or the provision of FAPE to the child.
>
> (b) *Content of notice.* The notice required under paragraph (a) of this section must
> include— (1) A description of the action proposed or refused by the agency; (2) An
> explanation of why the agency proposes or refuses to take the action; (3) A description of
> each evaluation procedure, assessment, record, or report the agency used as a basis for the
> proposed or refused action; (4) A statement that the parents of a child with a disability
> have protection under the procedural safeguards of this part and, if this notice is not an
> initial referral for evaluation, the means by which a copy of a description of the
> procedural safeguards can be obtained; (5) Sources for parents to contact to obtain
> assistance in understanding the provisions of this part; (6) **A description of other
> options that the IEP Team considered and the reasons why those options were rejected**; and
> (7) A description of other factors that are relevant to the agency's proposal or refusal.
>
> (c) *Notice in understandable language.* (1) The notice required under paragraph (a) of
> this section must be— (i) Written in language understandable to the general public; and
> (ii) Provided in the native language of the parent or other mode of communication used by
> the parent, unless it is clearly not feasible to do so. (2) If the native language or other
> mode of communication of the parent is not a written language, the public agency must take
> steps to ensure— (i) That the notice is translated orally or by other means to the parent in
> his or her native language or other mode of communication; (ii) That the parent understands
> the content of the notice; and (iii) That there is **written evidence** that the requirements
> in paragraphs (c)(2)(i) and (ii) of this section have been met."

**Why it is the most litigated procedural requirement.** Four reasons, and they compound:

1. **The trigger is enormous.** Four categories — identification, evaluation, placement,
   FAPE provision — and it fires on both *proposal* and *refusal*. Every "no" a district
   says to a parent is a PWN event. Districts routinely fail to issue PWN for refusals,
   because a refusal does not feel like an action.
2. **§300.503(b)(6) is the clause districts fail.** "Other options considered and the
   reasons why those options were rejected" is an affirmative obligation to document a
   deliberation. A conclusory notice that names the decision but not the rejected
   alternatives is facially deficient, and it is the deficiency most often found.
3. **No fixed deadline.** "A reasonable time before" — ED declined to set a number,
   reasoning that *"prior written notice is provided in a wide variety of circumstances for
   which any one timeline would be too rigid"* (71 FR 46691). An undefined standard is a
   litigable standard.
4. **It is the paper trail everything else is built on.** In a due process hearing, the PWN
   file is the district's contemporaneous account of its own reasoning. A thin PWN file
   leaves the district arguing from memory.

Two useful clarifications from the preamble, both verbatim (71 FR 46691):

- The IEP itself can serve as PWN: *"There is nothing in the Act or these regulations that
  would prohibit a public agency from using the IEP as part of the prior written notice so
  long as the document(s) the parent receives meet all the requirements in Sec. 300.503."*
- **A meeting is not a precondition:** *"A public agency is not required to convene an IEP
  Team meeting before it proposes a change in the identification, evaluation, or educational
  placement of the child, or the provision of FAPE to the child. **The proposal, however,
  triggers the obligation to convene an IEP Team meeting.**"*

### 5.2 Consent

`STATUTE` — **§300.9** defines consent as: the parent has been *"fully informed of all
information relevant to the activity for which consent is sought, in his or her native
language,"* understands and agrees **in writing**, the consent *"describes that activity and
lists the records (if any) that will be released and to whom,"* and the parent understands
that consent is voluntary and revocable at any time.

**Where consent is required** (§300.300): initial evaluation (a)(1); initial provision of
special education and related services (b)(1); each reevaluation (c)(1)(i).

**Where it is not** (§300.300(d)(1)): *"Parental consent is not required before— (i)
Reviewing existing data as part of an evaluation or a reevaluation; or (ii) Administering a
test or other evaluation that is administered to all children unless, before administration
of that test or evaluation, consent is required of parents of all children."*

**The revocation asymmetry, which practitioners feel and outsiders miss.** §300.300(b)(4):
if a parent revokes consent in writing after services have begun, the agency *"may not
continue to provide special education and related services to the child, but **must provide
prior written notice in accordance with § 300.503 before ceasing** the provision"* — and may
**not** use mediation or due process to override the revocation. A parent can unilaterally
end IDEA services; a parent cannot unilaterally start them. And §300.9(c)(3) confirms
revocation is not retroactive and does not require the district to scrub the education
record.

**The consent override, and its asymmetry.** For initial *evaluation*, a district may — but
need not — use due process to override a refusing parent (§300.300(a)(3)(i)). For initial
*services*, it may not (§300.300(b)(3)(i)). For *reevaluation*, consent is not needed at
all if the agency *"made reasonable efforts to obtain such consent"* and *"the child's
parent has failed to respond"* (§300.300(c)(2)).

### 5.3 Independent educational evaluation at public expense

`STATUTE` — **§300.502(b)(1)–(2)**: a parent who *disagrees with an evaluation obtained by
the public agency* has the right to an IEE at public expense, and the agency must,
**"without unnecessary delay,"** either *"(i) File a due process complaint to request a
hearing to show that its evaluation is appropriate; or (ii) Ensure that an independent
educational evaluation is provided at public expense."*

There is no third option. This is the most operationally sharp provision in Part 300: a
parent's request starts a clock on which the district must either pay or sue. §300.502(b)(4)
adds that the agency *"may not require the parent to provide an explanation and may not
unreasonably delay"* either course. §300.502(b)(5) caps it at one IEE at public expense per
agency evaluation disagreed with.

**Why this matters for AI.** If a district's evaluation incorporates AI-generated analysis
and a parent disagrees, the district must be able to defend that evaluation *in a hearing*
— which means being able to explain how the analysis was produced. An unexplainable
component in an evaluation converts a routine IEE request into a case the district cannot
win, and the cheapest response becomes "just pay for the IEE." That is a real, foreseeable
cost of opaque tooling and it does not require anyone to behave badly.

### 5.4 Mediation, due process, stay-put

- **Mediation** (§300.506): voluntary, state-funded, conducted by a qualified impartial
  mediator selected *"on a random, rotational, or other impartial basis,"* confidential
  (*"Discussions that occur during the mediation process must be confidential and may not be
  used as evidence in any subsequent due process hearing or civil proceeding"*), and
  producing a **legally binding written agreement** enforceable in state or federal court.
  `STATUTE`
- **Due process complaint** (§300.507): either party may file on identification,
  evaluation, placement, or FAPE. Two-year statute of limitations from when the party *"knew
  or should have known"* about the alleged action, unless state law says otherwise.
  `STATUTE`
- **Stay-put** (§300.518(a)): *"during the pendency of any administrative or judicial
  proceeding regarding a due process complaint notice […] unless the State or local agency and
  the parents of the child agree otherwise, the child involved in the complaint **must remain
  in his or her current educational placement**."* `STATUTE`

Stay-put deserves a design note. Combined with the §300.116 definition of placement as
*services*, stay-put freezes the child's **service package** for the duration of a dispute.
**A system that automatically adjusts service intensity would, during a stay-put period, be
capable of violating a federal freeze without any human forming an intent to do so.** Any
serious product in this space needs a per-child "frozen" state that no adaptive loop can
override. `INFERENCE` — but a direct reading of §300.518(a) with 71 FR 46588.

### 5.5 The framing, corrected

The brief asked whether this is right: *"An AI that changes a child's programme without
generating PWN has created a procedural violation."*

**Verdict: directionally correct, technically wrong in three ways.** The precise statement
follows.

**(i) The duty belongs to the public agency, not to the tool.** §300.503(a) obliges the
*public agency*. An AI has no legal duty and cannot commit a procedural violation. What
happens is that **the LEA commits the violation by acting on the AI's output without
issuing PWN.** This is not pedantry — it determines who is liable, what a vendor can be
sued for, and what a district must build around the tool. Say it as: *an AI that changes a
child's services without forcing the agency through PWN has manufactured a procedural
violation for its operator.*

**(ii) "Programme" is too broad.** PWN is triggered by changes to **identification,
evaluation, educational placement, or provision of FAPE** (§300.503(a)). It is not
triggered by changes to teaching methodology or lesson content. §300.501(b)(3) is explicit:

> "A meeting does not include informal or unscheduled conversations involving public agency
> personnel and conversations on issues such as **teaching methodology, lesson plans, or
> coordination of service provision.**" `STATUTE`

And ED on methodology in the IEP: *"There is nothing in the Act that requires an IEP to
include specific instructional methodologies. […] The Department's longstanding position on
including instructional methodologies in a child's IEP is that it is an IEP Team's decision.
Therefore, if an IEP Team determines that specific instructional methods are necessary for
the child to receive FAPE, the instructional methods may be addressed in the IEP"* (71 FR
46665). `STATUTE`

So the actual boundary is:

| AI action | PWN required? | Basis |
|---|---|---|
| Changes which worked example, hint, or representation a child sees this minute | **No** | §300.501(b)(3) — teaching methodology |
| Changes the sequence or content of a lesson inside an unchanged service | **No** | ibid. |
| Changes the *method* where the IEP names a method | **Yes** | The IEP would have to be amended; 71 FR 46665 |
| Changes minutes, frequency, duration, or type of a service | **Yes** | Change to provision of FAPE / placement; §300.503(a)(1), 71 FR 46588 |
| Moves a child between settings or groups in a way that alters services | **Yes** | ibid. |
| Declines to provide something a parent requested | **Yes** | §300.503(a)(2) — refusals trigger PWN |
| Flags a child as possibly needing evaluation, and the district acts on it | **Yes** | Change to identification/evaluation |
| Flags a child, and the district declines to evaluate | **Yes** | Refusal to initiate evaluation |

The last two rows are the ones product teams never anticipate. **A screening feature is a
child-find feature, and child-find outputs are PWN events in both directions.**
§300.111(a)(1)(i) obliges the state to ensure all children with disabilities *"are
identified, located, and evaluated."* Once an AI hands a district a signal, the district's
response — evaluate or decline — is a §300.503 event.

**(iii) A procedural violation is not automatically a denial of FAPE.** `STATUTE` —
**§300.513(a)**, verbatim:

> "(1) Subject to paragraph (a)(2) of this section, a hearing officer's determination of
> whether a child received FAPE must be based on **substantive grounds**.
> (2) In matters alleging a procedural violation, a hearing officer may find that a child did
> not receive a FAPE **only if** the procedural inadequacies— (i) Impeded the child's right to
> a FAPE; (ii) **Significantly impeded the parent's opportunity to participate** in the
> decision-making process regarding the provision of a FAPE to the parent's child; or
> (iii) Caused a deprivation of educational benefit.
> (3) Nothing in paragraph (a) of this section shall be construed to preclude a hearing officer
> from **ordering an LEA to comply with procedural requirements**."

So: the omission is a violation the moment it happens, and §300.513(a)(3) preserves an order
to comply regardless. But the remedy escalates to a FAPE denial — compensatory education,
tuition reimbursement, attorneys' fees under §300.517 — only through one of the three gates.
**Gate (ii) is the one an AI trips.** A system that shifts a child's services through an
automated loop, without a document the parent can read, *is* impeding parental participation
in the decision. It is hard to construct an AI-driven service change that does not land on
gate (ii).

**The corrected formulation for the survey:**

> An AI does not commit procedural violations; agencies do. But an AI that changes what
> services a child receives, without forcing the agency to issue prior written notice under
> 34 CFR §300.503, has manufactured a procedural violation for the district operating it —
> and because the mechanism of the violation is that the parent was not told, it lands
> squarely on §300.513(a)(2)(ii), the gate that converts a procedural defect into a denial
> of FAPE. Changing *how* something is taught inside an unchanged service is not a PWN
> event; §300.501(b)(3) puts teaching methodology outside the meeting requirement entirely.
> The line is not between big changes and small ones. It is between the *service* and the
> *method*.

### 5.6 The predetermination problem — the sharpest AI-specific risk in this report

Every recommendation engine wants to arrive at the meeting with an answer. IDEA's structure
is hostile to exactly that, and ED said so in the preamble while explaining why it would
*not* require PWN before an IEP meeting:

> "**Providing prior written notice in advance of meetings could suggest, in some
> circumstances, that the public agency's proposal was improperly arrived at before the
> meeting and without parent input.** Therefore, we are not changing Sec. 300.503 to require
> the prior written notice to be provided prior to an IEP Team meeting." (71 FR 46691)
> `STATUTE`

That is ED describing predetermination as a recognised failure mode, in its own voice, in
the context of documents produced before meetings.

The tension is genuine and is not resolved by good intentions:

- §300.501(b)(3) expressly protects preparation: *"A meeting also does not include
  preparatory activities that public agency personnel engage in to develop a proposal or
  response to a parent proposal that will be discussed at a later meeting."* Districts are
  **allowed** to prepare drafts.
- But a draft that arrives complete, confident, and machine-authored, and that the team
  ratifies, is functionally a decision made before the parent spoke.

**Design consequences, stated flatly:**

1. **A draft must look like a draft.** Provenance visible, gaps visible, alternatives
   visible. An AI output styled as a finished document is an invitation to ratify.
2. **The system must generate the §300.503(b)(6) content — options considered and why
   rejected — as a first-class artefact, not an afterthought.** This is the clause districts
   fail, it is the clause that rebuts predetermination, and it is genuinely well-suited to a
   model that can enumerate alternatives.
3. **The system must be able to change its recommendation in the meeting, visibly, in
   response to the parent.** A recommendation that cannot move in response to parent input
   is evidence of predetermination.
4. **Never present a single option.** A single machine-generated option is the strongest
   possible predetermination artefact and it will be produced in discovery.

`INFERENCE` from §300.501(b)(3), §300.503(b)(6), and 71 FR 46691. Case-law support at §10.

---

## 6. Evaluation and eligibility

### 6.1 The clocks

`STATUTE` — **§300.301(c)(1)**: the initial evaluation *"Must be conducted within 60 days of
receiving parental consent for the evaluation; or […] If the State establishes a timeframe
within which the evaluation must be conducted, within that timeframe."*

**The federal number is 60 calendar days from consent, and a large number of states have
substituted their own.** Any product that hard-codes 60 days is wrong in those states. The
two exceptions (§300.301(d)): a parent who *"repeatedly fails or refuses to produce the child
for the evaluation,"* and a mid-evaluation transfer between agencies — and the transfer
exception applies only if the receiving agency is *"making sufficient progress to ensure a
prompt completion"* and the parties agree a completion date (§300.301(e)).

**§300.323(c)(1)**: once eligibility is determined, *"A meeting to develop an IEP for a child
is conducted **within 30 days** of a determination that the child needs special education and
related services."*

**§300.303(b)**: reevaluation *"May occur not more than once a year, unless the parent and the
public agency agree otherwise"* and *"Must occur **at least once every 3 years**, unless the
parent and the public agency agree that a reevaluation is unnecessary."*

**§300.324(b)(1)(i)**: the team reviews the IEP *"periodically, but not less than annually."*

**§300.323(a)**: at the beginning of each school year, an IEP must be **in effect** for every
eligible child in the agency's jurisdiction.

That is the compliance calendar in five citations. It is fully mechanisable and it is where
districts most often fail.

### 6.2 The evaluation standard

`STATUTE` — **§300.304(b)**, verbatim:

> "In conducting the evaluation, the public agency must— (1) Use a **variety** of assessment
> tools and strategies to gather relevant functional, developmental, and academic information
> about the child, **including information provided by the parent** […] (2) **Not use any single
> measure or assessment as the sole criterion** for determining whether a child is a child with
> a disability and for determining an appropriate educational program for the child; and
> (3) Use technically sound instruments that may assess the relative contribution of cognitive
> and behavioral factors, in addition to physical or developmental factors."

And §300.304(c) requires that assessments be *"selected and administered so as not to be
discriminatory on a racial or cultural basis,"* be provided *"in the child's native language
or other mode of communication and in the form most likely to yield accurate information,"*
be *"used for the purposes for which the assessments or measures are valid and reliable,"* be
*"administered by trained and knowledgeable personnel,"* and be *"administered in accordance
with any instructions provided by the producer of the assessments."*

**Five of those clauses are direct constraints on any AI-mediated assessment**, and the last
two are the ones a software product breaks silently: an AI that alters administration
conditions — reads an item aloud, rephrases, offers a hint, changes timing — has departed
from the producer's instructions and the instrument's validity argument no longer holds.
`INFERENCE`, but a direct application of §300.304(c)(1)(iii) and (v).

The **no-single-measure rule** at §300.304(b)(2) has a specific implication that this project
should state: **a model's confidence score is a single measure.** However many features it
consumed, it arrives at the meeting as one number, and it cannot be the sole criterion for
anything. It is an input to a group of qualified professionals plus the parent
(§300.306(a)(1)), not a substitute for them.

### 6.3 The disability categories

Thirteen, enumerated verbatim at §300.8(a)(1) — see §3.1. Definitions at §300.8(c). Two
features matter operationally:

- **Every definition ends in the same clause: "adversely affects a child's educational
  performance."** Category membership alone is never enough.
- **§300.111(d)**: *"Nothing in the Act requires that children be classified by their
  disability so long as each child who has a disability that is listed in § 300.8 […] is
  regarded as a child with a disability."* Categories are a reporting and eligibility
  construct, not a treatment prescription. H1's "no diagnosis, no labelling" constraint has
  statutory company here.

**The eligibility exclusions** are load-bearing and rarely quoted. §300.306(b): a child must
**not** be found eligible if the determinant factor is *"(i) Lack of appropriate instruction
in reading, including the essential components of reading instruction […]; (ii) Lack of
appropriate instruction in math; or (iii) Limited English proficiency."* `STATUTE`

Read that against H1's finding that explicit systematic decoding instruction is the
evidenced ingredient and that many children referred for reading difficulty have never
received it. **§300.306(b)(1)(i) makes "we never taught them properly" a legal bar to
eligibility** — which is either a safeguard against over-identification or a mechanism for
denying services to children failed by their core instruction, depending entirely on
whether the district's core instruction is any good.

### 6.4 Specific learning disability — three methods, and who may use them

This is the most state-variable part of IDEA and the most misdescribed.

`STATUTE` — **§300.307(a)**: a state must adopt SLD criteria which:

> "(1) **Must not require** the use of a severe discrepancy between intellectual ability and
> achievement for determining whether a child has a specific learning disability […];
> (2) **Must permit** the use of a process based on the child's response to scientific,
> research-based intervention; and (3) **May permit** the use of other alternative
> research-based procedures."

The precise federal position, which almost every secondary summary garbles:

| Method | Federal status |
|---|---|
| **Severe discrepancy** (IQ–achievement) | A state **may not require** it. A state **may permit** it. It is not banned. |
| **RTI / response to scientific, research-based intervention** | A state **must permit** it. |
| **Pattern of strengths and weaknesses (PSW)** | Falls under "other alternative research-based procedures" — a state **may permit** it. |

`STATUTE` — **§300.309(a)** sets the substantive finding. The child must (1) not achieve
adequately for age or state-approved grade-level standards in at least one of eight named
areas — *oral expression, listening comprehension, written expression, basic reading skill,
reading fluency skills, reading comprehension, mathematics calculation, mathematics problem
solving* — **and** (2) either *"does not make sufficient progress to meet age or State-approved
grade-level standards […] when using a process based on the child's response to scientific,
research-based intervention"* **or** *"exhibits a pattern of strengths and weaknesses in
performance, achievement, or both, relative to age, State-approved grade-level standards, or
intellectual development"* — **and** (3) the findings are not primarily the result of a
visual/hearing/motor disability, intellectual disability, emotional disturbance, cultural
factors, environmental or economic disadvantage, or limited English proficiency.

`STATUTE` — **§300.309(b)** is the instructional-adequacy gate, and it is the one that makes
data infrastructure legally necessary. The group must consider:

> "(1) Data that demonstrate that prior to, or as a part of, the referral process, the child
> was provided **appropriate instruction in regular education settings, delivered by qualified
> personnel**; and (2) **Data-based documentation of repeated assessments of achievement at
> reasonable intervals**, reflecting formal assessment of student progress during instruction,
> **which was provided to the child's parents.**"

**This is the strongest legal argument in this report for the H1 architecture.** §300.309(b)(2)
requires *repeated, documented, parent-reported progress measurement during instruction* as a
precondition of SLD eligibility. That is curriculum-based measurement, written into federal
regulation. A system that produces that record as a by-product of instruction is not adding a
compliance feature; it is producing the evidentiary substrate that eligibility determination
requires. `INFERENCE` from §300.309(b) + H1 §1.4.

**Documentation requirements** at §300.311 include a striking provision most people have
never read — **§300.311(b)**: *"Each group member must **certify in writing** whether the
report reflects the member's conclusion. If it does not reflect the member's conclusion, the
group member must submit a separate statement presenting the member's conclusions."*
`STATUTE`

Individual, attributed, written certification, with a dissent mechanism. **This is the
clearest statement in Part 300 that eligibility is a set of named human judgements, not a
determination.** An AI cannot certify. An AI's output cannot be a member's conclusion. And
the dissent right means the statute anticipates disagreement and refuses to average it away —
the opposite of what an ensemble model does.

**Additional required group members** for SLD (§300.308): the child's regular teacher (or a
qualified equivalent), **and** *"At least one person qualified to conduct individual
diagnostic examinations of children, such as a school psychologist, speech-language
pathologist, or remedial reading teacher."*

---

---

## 7. Caseload, workload, and where the time actually goes

This is the reality check, and it is where the largest practical finding in this report sits.

### 7.1 The population being served

`OBSERVED` — U.S. Department of Education, OSEP, **IDEA Section 618 Part B Child Count and
Educational Environments, SY 2023–24**, Table 1 and Table 3, retrieved from data.ed.gov on
2026-07-28.

| Measure | SY 2023–24 |
|---|---|
| Children and students served under IDEA Part B, **ages 3–21** | **7,892,433** |
| Students served, ages 5 (in kindergarten) through 21 | 7,304,525 |
| Ages 3–5 (not in kindergarten) | 587,908 |
| Ages 18–21 | 321,867 |

Disability distribution, ages 5(K)–21, SY 2023–24:

| Category | Count | Share |
|---|---|---|
| Specific learning disabilities | **2,445,500** | 33.5% |
| Speech or language impairments | **1,298,318** | 17.8% |
| Other health impairments | **1,197,312** | 16.4% |
| Autism | 998,348 | 13.7% |
| Intellectual disabilities | 419,334 | 5.7% |
| Emotional disturbance | 317,641 | 4.3% |
| Developmental delay | 297,478 | 4.1% |
| Multiple disabilities | 123,735 | 1.7% |
| Hearing impairments | 63,296 | 0.9% |
| Orthopedic impairments | 27,010 | 0.4% |
| Traumatic brain injury | 23,668 | 0.3% |
| Visual impairments | 23,113 | 0.3% |
| Deaf-blindness | 1,795 | 0.02% |

**Three categories are two-thirds of the caseload.** SLD, speech/language and other health
impairment together are **4,941,130 students — 67.6%** of the 5–21 count. `MEASURED` (my
arithmetic on the OSEP file.) A product designed around the categories that dominate the
public imagination is designed for the last third.

`OBSERVED` — NCES, *Condition of Education*, "Students With Disabilities," last updated May
2024: *"In 2022–23, the number of students ages 3–21 who received special education and/or
related services under the Individuals with Disabilities Education Act (IDEA) was 7.5 million,
or the equivalent of **15 percent of all public school students.** Among students receiving
special education and/or related services, the most common category of disability was specific
learning disabilities (32 percent)."*

NCES Digest table 204.30 gives the same year as **7,526,000 served, ages 3–21 = 15.2% of total
public enrolment**, up from 13.0% in 2010–11 and 14.1% in 2018–19. Computed directly from the
§618 CSVs: **2023–24 = 7,783,464** across the 50 states and DC (New Mexico suppressed), and
**2024–25 = 8,081,816** across all 51. `MEASURED` / `INFERENCE` on the recomputation, which was
validated by reproducing the published 2022–23 figure to within 59 students.

**This corrects `survey/04`.** The section says "roughly one child in seven" (14.3%). The
published figure is **15.2%** and the count has risen from 7.53M to **8.08M** in two years.
**"About one in six, and rising"** is the accurate phrasing.

**And it excludes every Section 504-only student — who are not in this count at all, and whose
numbers have doubled.** `MEASURED` — ED Office for Civil Rights, Civil Rights Data Collection
national estimations (`b_DIS5Count`):

| CRDC year | Enrolment | IDEA | **504-only** | 504-only % |
|---|---|---|---|---|
| 2011–12 | 49,756,058 | 6,082,307 | 760,114 | 1.53% |
| 2015–16 | 50,574,476 | 6,352,285 | 1,156,811 | 2.29% |
| 2017–18 | 50,922,401 | 6,728,064 | 1,380,146 | 2.71% |
| **2020–21** (latest published) | 49,150,566 | 6,853,313 (13.94%) | **1,605,564** | **3.27%** |

**Section 504-only enrolment has grown 2.11× in nine years.** IDEA plus 504 combined in 2020–21
is **8,416,507**. This is a caseload channel with no IDEA procedural machinery, no federal
personnel count, and no dedicated funding — and it is the fastest-growing part of the
population a product in this space will serve.

**One further distribution fact that changes where the work happens.** `OBSERVED` — NCES
*Condition of Education*, 2022–23: **67%** of school-age students served under IDEA spend **80%
or more of the day in general education classes**, up from 61% in 2012. State prevalence ranges
from **12%** (Idaho, Hawaii) to **21%** (Pennsylvania, New York, Maine); Puerto Rico is 37%;
males 18% versus females 10%. **Two-thirds of the caseload is mostly in the general-education
room**, which means the special educator's load is disproportionately *consultative* — and
consultation is the §300.323(d)(2) duty to inform every teacher of every accommodation, for
every child, every time anything changes.

### 7.2 Where the hours go — the SPeNSE Paperwork Substudy

The best empirical answer to "what fraction of the week is instruction versus paperwork" is
still a federal study from 2002, which is itself a finding about how little anyone has measured
since.

`MEASURED` (national probability survey) — **Study of Personnel Needs in Special Education
(SPeNSE), Final Report of the Paperwork Substudy**, Westat for the Office of Special Education
Programs, U.S. Department of Education, 2002. ERIC **ED479674**. Subsample **n = 972** special
education teachers drawn from the main SPeNSE interview sample.

**The headline numbers:**

| Finding | Value |
|---|---|
| Time on administrative duties and paperwork | **median 5 hours/week, mean 6 hours/week** |
| Time *available* in the school week for it | **4 hours/week** |
| **The gap** | *"there was a two-hour discrepancy between the number of hours teachers needed to complete their administrative duties and paperwork and the number of hours they actually had available"* |
| Class coverage granted for paperwork | **2 days per year** (= 0.07 hours/week) |
| Time in the school day for paperwork | **50 minutes** |
| Teachers with **no** help from a paraprofessional, volunteer, or secretary | **50%** |
| Said paperwork interfered with teaching to a **moderate or great** extent | **88%** |
| Said routine duties and paperwork interfered **to a great extent** (2000 SPeNSE survey) | **53%** |
| Share of time on forms and administrative paperwork | *"over 10 percent"* |
| Rank of paperwork among teachers' concerns | **third**, behind caseloads and planning time |

**The per-task breakdown**, verbatim from the report:

> "2 hours on each IEP (range: 0 to 30 hours) […] 1.5 hours attending each IEP meeting […]
> 4 hours per month printing or copying special education forms […] 2 hours per month scheduling
> IEP meetings […] 1 hour per month mailing notices to parents […] and 4 hours per month tracking
> paperwork from other teachers that is required for the IEP process."

Plus: **8 hours** to complete each cycle of written parent progress reports, which are due on
average **every 7 weeks** — and **80%** of special education teachers reported their progress
reports contain more detail than reports for nondisabled students. Behaviour work adds 5
hours/month on behaviour logs, 2 on behaviour intervention plans, 2 on functional behavioural
assessments. Of the 35% who conduct initial evaluations: 7.5 hours/month administering plus 4.2
reviewing. Of the 51% who conduct triennials: 5 plus 3.

**The caseload arithmetic, which is the number to carry:**

> "On average, teachers spent **0.4 hours per week per child** on administrative duties and
> paperwork for children they taught. That figure was **0.6 hours per week for children for whom
> they served as case manager** […] The case management function was clearly tied to paperwork
> responsibilities."

Apply that to California's statutory cap. **34 CFR** has no caseload cap; California does.

`STATUTE` — **California Education Code §56362(c)**, current text as amended by AB 560 (Stats.
2025, Ch. 560), effective January 1, 2026, verbatim:

> "Caseloads for resource specialists shall be stated in the local policies developed pursuant to
> Section 56195.8 and in accordance with regulations established by the board. **A resource
> specialist shall not have a caseload that exceeds 28 pupils.**"

28 case-managed children × 0.6 hours/week = **16.8 hours per week of administrative work at a
legal maximum caseload** — against 4 hours available. The SPeNSE mean of 5–6 hours/week is
therefore not a measure of the work required; **it is a measure of how much of the required work
gets done.** `INFERENCE` — and it reframes the entire question. The paperwork burden is not
"teachers spend too long on forms." It is that the forms are being triaged, and the triage is
invisible.

### 7.2b The observational study, which is worse than the self-report

`MEASURED` (direct observation) — **Vannest & Hagan-Burke, "Special Education Teacher Time Use
in Four Types of Programs," *Journal of Educational Research* (2011)**, DOI
10.1080/00220671003709898. Direct observation plus one-hour interval self-report; **more than
7,000 data points, 31 teachers, 24 schools, 9 districts**, across one academic year, with
interrater reliability established using concurrent observers. Verbatim:

> "**only 20% of class time spent on academic instruction and nearly 17% spent on special and
> general education paperwork.**"

Companion studies from the same programme: *Teacher Time Use in Special Education*, *Remedial
and Special Education* (2010), DOI 10.1177/0741932508327459 — **36 teachers, 2,200 hours**
logged; and *Measuring Time*, *Journal of Special Education* (2010), which finds that roughly
**10 days of sampling** are needed for a stable time-use estimate.

**Twenty per cent of class time on academic instruction, measured by observers rather than by
memory.** That is the number `survey/04` is implicitly assuming away.

### 7.2c Three professions, two decades, one convergent estimate

| Source | Method | Documentation share |
|---|---|---|
| SPeNSE (2002), n = 972 special ed teachers, nationally weighted | Self-report | **~12–13%** of a 40-hour week (5 h median) |
| Vannest & Hagan-Burke (2011), 31 teachers, >7,000 data points | **Direct observation** | **~17%** |
| ASHA Schools Survey (2024), n = 2,347 SLPs | Self-report | **15%** (6 of 40 hours) |

**Independent methods, two decades apart, three professions, converging on 13–17% of
professional time going to documentation — and the observational study, the one that does not
rely on memory, returns the highest figure.** `MEASURED` / `MEASURED-META` on the convergence.

### 7.2d Speech-language pathology, where the caseload-versus-workload distinction was invented

`MEASURED`/`OBSERVED` — **ASHA 2024 Schools Survey**. Stratified random sample of 15,000
ASHA-certified SLPs; 14,628 eligible; **3,749 respondents, 25.6% response rate** — itself down
from 69.7% in 2004, which is a datum about the profession.

- **Median actual monthly caseload: 50** (range 4–351, n = 2,815).
- **Median caseload SLPs consider *manageable*: 40** (range 0–200, n = 2,776).
- **The 50-versus-40 gap is the entire workload argument, quantified.**
- Twenty-year trend: 50 (2004–2010) → 47–48 → **back to 50 in 2024**. No net progress.
- State extremes: **Indiana 78**, **New York 32** — and New York is the state whose regulation
  caps SLP caseload at 65 (below).
- **80%** are required to make up missed sessions.

Weekly hours by activity (n = 2,347): direct intervention **23** (57.5%); **documentation 6
(15%)**; diagnostic evaluations 4; collaborative consultation 3; supervision and other 4.
Corroborating: Katz et al. (2010), *LSHSS*, n = 634 full-time SLPs across 49 states — mean
caseload **49**, and at the 41–50 band roughly **60%** already describe it as unmanageable.

### 7.2e School psychologists — the assessment engine

`MEASURED` — NASP Research Reports (Affrunti), computed from NCES Common Core of Data FTE
counts. **NASP's recommended ratio is 1:500.**

| School year | National students-per-school-psychologist ratio |
|---|---|
| 2019–20 | 1,211:1 |
| 2020–21 | 1,151:1 |
| 2021–22 | 1,127:1 |
| 2022–23 | 1,119:1 |
| 2023–24 | 1,065:1 |
| **2024–25** | **1,071:1** |

NASP on the latest year: the ratio *"essentially remained the same."* **Only 3 of 51
jurisdictions meet 1:500** (Connecticut, Puerto Rico, District of Columbia); some states
approach 1:5,000. Practitioner-reported ratios run higher still — 2020 NASP Membership Survey,
full-time school-based psychologists, n = 993: mean **1,233** (SD 1,285, range 0 to 16,667).

**And the volume of evaluations each one carries.** `MEASURED` — 2020 NASP Membership Survey
Part 2 (Farmer et al. 2021), school-based n = 1,006: **55 evaluations per year on average
(median 50)** — mean 23.5 initial plus 31.5 reevaluations. **88%** report spending *"a great
deal of their time"* completing evaluations; **78%** are involved in IEP-meeting-related work.
Psychologists serving more than 700 students showed practice significantly less consistent with
the NASP Practice Model.

Set that against the 60-day statutory clock in §300.301(c)(1). **Fifty-five evaluations a year,
each on its own clock, at a national ratio more than double the professional recommendation.**
That is the resource the whole eligibility system runs on.

### 7.2f What the federal government said about this in 2002, and never fixed

`OBSERVED` — **President's Commission on Excellence in Special Education (2002)**, ERIC
ED473830, verbatim:

> "Special education teachers feel excessive paperwork interferes with their ability to serve
> children with disabilities more effectively… **The typical special education teacher spends
> five hours per week completing forms and doing administrative paperwork. Moreover, special
> educators spend more time on paperwork than grading papers, communicating with parents,
> sharing expertise with colleagues, supervising paraprofessionals and attending IEP meetings
> combined.**"

And the diagnosis of where the load comes from: documentation *"driven by the more than **814
federal monitoring requirements** for state and local special education programs to comply with
IDEA."*

### 7.3 California, and the fact that most of the country has no cap at all

`STATUTE` — **Cal. Ed. Code §56362(f)**: *"At least 80 percent of the resource specialists within
a local plan shall be provided with an instructional aide."* And, added by AB 560 in 2025, new
subsection **(g)**: *"Local educational agencies shall take all reasonable steps to distribute the
workload associated with initial assessments across all resource specialists employed by the
local educational agency in an equal manner, unless otherwise collectively bargained."*

**A state legislature passed a law in 2025 requiring districts to share out assessment
workload fairly.** Legislatures do not legislate on problems that are not happening.

More striking: **AB 560 also added Ed. Code §56364.3**, which requires the State Superintendent,
*"on or before July 1, 2027,"* to *"**recommend** a maximum adult-to-pupil staffing ratio for
special classes […] for pupils 3 to 22 years of age"* — after consulting current special-class
teachers, administrators, paraprofessionals, parents, researchers and disability-rights
advocates, and after considering *"other states' adult-to-pupil ratios for special classes"* and
*"the effects on the education of pupils with disabilities in the least restrictive environment,
as required by the federal Individuals with Disabilities Education Act."* `STATUTE`

**Read that plainly. In 2026, the most heavily regulated special-education system in the United
States has no staffing ratio for its most restrictive settings, and has just told its
Superintendent to go and *recommend* one by 2027.** That is a documented systemic gap in the
one place a builder would most expect a rule to exist.

**There is no federal caseload cap, and this was verified rather than assumed.** The full text
of 34 CFR Part 300 was pulled from the eCFR API and searched: `caseload` **0 occurrences**,
`class size` **0**, `student-teacher ratio` **0**. The 20 hits for "ratio" are all *risk ratio*
in §300.647 (significant disproportionality). `STATUTE` (verified absence).

**Where caps do exist, they are state law and they vary by an order of magnitude.**

`STATUTE` — **New York, 8 NYCRR §200.6**, the strictest regime located:
- §200.6(d)(1): *"The total number of students with disabilities assigned to a consultant
  teacher **shall not exceed 20**."*
- §200.6(e)(2): speech and language — *"the total caseload of such students for teachers
  providing such services **shall not exceed 65**."*
- §200.6(f)(5): resource room caseload **20** (**25** in grades 7–12); §200.6(f)(3):
  instructional group **5**.
- §200.6(g)(1): integrated co-teaching — *"the number of students with disabilities in such
  classes **shall not exceed 12 students**."*
- §200.6(h)(4): special class **15**; **12** with management needs plus supplementary personnel;
  **8** intensive; **6** highly intensive; **12** for severe multiple disabilities with an
  additional **1:3** staff-to-student ratio.
- §200.6(h)(5): *"The chronological age range within special classes of students with
  disabilities who are less than 16 years of age **shall not exceed 36 months**."*
- New York City receives a **+50%** variance on all of these.

`STATUTE` — **Illinois, 23 Ill. Adm. Code §226.730(b)** (amended 47 Ill. Reg. 2244, effective
6 February 2023): **15:1** where students are in special education ≤20% of the day; **10:1** for
>20–60%; **8:1** for >60%; **5:1** for ages 3–5 — each expandable by +2/+5/+5/+5 with a
paraprofessional assigned to the class for its entirety. And §226.730(a) requires general
education classes to be *"composed of students of whom at least 70 percent are without IEPs."*

`STATUTE` — **Illinois §226.735(c)**, the only explicit *workload* construction found in any
state code, and the one worth copying:

> "The number of children served by a speech and language pathologist shall be based on the
> speech-language needs of each child. The other provisions of this Section notwithstanding,
> **at no time shall the caseload of a speech and language pathologist exceed 60 students.**"

§226.735(b) requires the workload limit to be built from *"1) individualized instruction;
2) consultative services…; 3) attendance at IEP meetings and other staff conferences; and
**4) paperwork and reporting**."* **An American state regulator has written paperwork into a
statutory workload formula.** That is the closest thing in US law to an acknowledgement that
documentation is part of the job rather than an overhead on it.

`STATUTE` — **California §56363.3** (speech-language): *"The average caseload for language,
speech, and hearing specialists in special education local plan areas **shall not exceed 55
cases**, unless the local plan specifies a higher average caseload and the reasons for the
greater average caseload."*

**And the states with no numeric special-education cap at all**, each verified by full-text
search of the relevant code rather than by absence of a citation:

| State | What was searched | Result |
|---|---|---|
| **Texas** | 19 TAC Ch. 89 Subch. AA & D; TEC Ch. 29 & 30 | **0 hits.** Only "ratio" language is 19 TAC §89.1005(a)(1), listing *"reduction of ratio of students to instructional staff"* as an **example of a service**, not a limit. Generic caps only: TEC §25.112 = 22 (PreK–4) |
| **Florida** | All **136** rules in FAC Ch. 6A-6 enumerated | No class-size or caseload rule exists; the historical programme rules (6A-6.03015, .03021, .03025, .0312) are all **repealed**. Generic §1003.03 F.S. caps only |
| **Washington** | WAC 392-172A (~5,000 lines) and RCW 28A.155 | `caseload` **0**, `class size` **0**. Washington's numbers are *funding* assumptions in RCW 28A.150.260, not caps |
| **Oregon** | All 177 rules of OAR Ch. 581 Div. 15 | None found |

**So: the federal government, Texas, Florida, Washington and Oregon place no numeric limit on
how many children one special educator may be responsible for.** `STATUTE` (verified absence).

`STATUTE` — the SELPA structure `survey/04` names: **Cal. Ed. Code §56195** — *"Each special
education local plan area, as defined in subdivision (d) of Section 56195.1, shall administer
local plans […] and shall administer the allocation of funds."* **§56205(a)** requires each SELPA
to have in effect policies consistent with state and federal law on FAPE, full educational
opportunity, child find and referral, IEPs, **least restrictive environment**, procedural
safeguards, annual and triennial assessments, confidentiality, Part C transition, private-school
children, and compliance with IDEA, Section 504 and the ADA. A SELPA is, in law, a **compliance
and funding administration layer** — which is exactly why an AI's contribution to it is likely to
be administrative.

### 7.4 The two null results that should govern every claim made about AI here

Both are from the SPeNSE Paperwork Substudy, both are directly on point, and both are almost
never cited.

**NULL 1 — Computerisation produced no measured reduction in paperwork time.** Verbatim:

> "**Access to reliable computers was not related to the time teachers spent on administrative
> duties and paperwork.** […] Seventy percent of teachers reported using a computer, at least in
> part, for writing IEPs. **Using a computer to prepare IEPs was not significantly related to time
> spent writing each IEP or completing administrative duties and paperwork, in general.** Teachers
> who used computers said their computer equipment was quite reliable and their access to the
> equipment was good or excellent." `MEASURED` (null)

The last sentence closes the obvious escape route: it was not a bad-tools problem. Seventy
percent had good tools and it did not show up in the hours.

**NULL 2 — Delegating the work to another person produced no measured reduction either, and the
report says why.** Verbatim:

> "**The amount of help teachers had was not significantly related to the time they spent on
> administrative duties and paperwork or to whether administrative duties and paperwork interfered
> with their job of teaching. This may be the case because much of the paperwork teachers complete
> cannot be appropriately delegated to an aide or secretary.**" `MEASURED` (null)

**That second null is the most important sentence in this report for anyone building an AI
assistant in this space.** The work resisted delegation not because there was too much of it but
because of *what it is*: professional judgement expressed in prose. An aide cannot write a
PLAAFP. **The honest question is therefore not "can AI reduce paperwork" — the last two
labour-saving interventions measured at zero — but "is a language model a different kind of
delegate from an aide, given that the barrier was judgement rather than throughput?"** That
question has not been answered, and this project should not pretend otherwise.

### 7.5 What *did* measurably reduce the time

Three things did, and all three are structural rather than technological:

| Intervention | Effect |
|---|---|
| **Selecting goals from a pre-developed list** rather than composing from scratch | 2.2 hours per IEP vs **2.6** |
| **Rewriting only the changed sections** at annual review rather than the whole document | 2.0 hours per IEP vs **2.5** |
| Not rewriting the whole document (risk model) | Full rewriters had a **15 percent higher risk** of being in the group without enough time to complete their duties, *"after controlling for caseload and case management responsibilities […] regardless of their years of experience"* |

`MEASURED` — all three from the SPeNSE Paperwork Substudy.

**The goal-bank result is the pre-AI ancestor of AI goal drafting, and it is a warning as much as
an encouragement.** Selecting from a fixed menu saved about 15% of the time on each IEP. It is
also the mechanism most likely to produce the boilerplate, non-individualised goals that
*Endrew F.* now makes substantively challengeable. **A goal bank is a time-saving device that
trades individualisation for speed. A generative model is a much better goal bank, which means it
is a much better version of both the saving and the hazard.** `INFERENCE`.

The federal government's own paperwork-reduction moves show the same pattern: ED priced the
removal of short-term objectives at $77.5M/year on a 15-minute assumption (71 FR 46843), and
priced the IEP-team-member excusal provision at approximately **nothing**, because *"reduced time
spent in meetings is likely to be offset by the time required to draft written input"* (71 FR
46843). `OBSERVED` — a third documented null, this one from the regulator.

### 7.5b ★ The largest documented failure: IDEA §609, twenty-one years, zero waivers

This is the strongest single piece of evidence in the report that the paperwork problem is
structural rather than technical, and it appears to be almost entirely unremarked.

1. **2002** — the President's Commission recommends the Secretary *"determine up to **10 states**
   that will be allowed to submit proposals for IDEA paperwork reduction."*
2. **3 December 2004** — Congress enacts **IDEA §609 = 20 U.S.C. §1408, "Paperwork reduction."**
   `STATUTE`, verbatim: *"the Secretary is authorized to grant waivers of statutory requirements
   of, or regulatory requirements relating to, subchapter II for a period of time not to exceed
   **4 years** with respect to **not more than 15 States**…"* And §1408(b) **requires** the
   Secretary, *"Beginning 2 years after December 3, 2004,"* to report to Congress on waiver
   effectiveness in *"reducing (A) the paperwork burden on teachers, principals, administrators,
   and related service providers; and (B) noninstructional time spent by teachers."*
3. **19 December 2005** — proposed requirements published.
4. **6 July 2007** — final requirements, framed as *"a single, one-time-only competition."*
5. **12 October 2007** — applications invited, deadline 11 February 2008 (72 FR 58066).
6. **Then nothing.** A Federal Register API search for the paperwork-waiver programme across all
   years returns **exactly one further document** — a 2020 proposed rule. **No award notice, no
   granted waiver, and no §1408(b) effectiveness report has ever appeared.**
7. **5 June 2020** — ED proposes the requirements *again*, explaining only that the 2007 criteria
   *"were only eligible to be used once, which the Department did in 2007"* and that it is
   *"proposing to use many of the same requirements… because we believe they still represent a
   sensible and practical approach."* **It reports no results, no participating states and no
   findings from the 2007–08 competition — despite the standing statutory duty to report exactly
   that.**
8. **The 2020 proposal was never finalised.** No final rule exists.

`OBSERVED` — **the statutory paperwork-reduction mechanism Congress created in 2004 has produced
no documented waiver and no documented hour of reduction in twenty-one years, and the
effectiveness report the statute mandates has never been filed.**

### 7.5c The one measured study of AI and IEP work

`MEASURED-RCT` (small) — **Rakap, "Chatting with GPT: Enhancing Individualized Education Program
Goal Development for Novice Special Education Teachers," *Journal of Special Education
Technology*** (online 2023), DOI 10.1177/01626434231211295, ERIC EJ1434044. **n = 22** novice
special-education teachers **randomly assigned** to a ChatGPT condition or control, writing IEP
goals for five children with autism, scored on the Revised IEP/IFSP Goals and Objectives Rating
Instrument. The ChatGPT group produced **significantly higher-quality goals** and **spent
significantly less time.**

**Report it with its limits attached, because they are severe.** n = 22, single site, novices
only, goal drafting only — not the full IEP, and *not* the printing, copying, scheduling,
notice-mailing, cross-teacher tracking and progress reporting that SPeNSE showed actually
dominate the weekly hours. An ERIC query for `"ChatGPT" AND "individualized education program"`
returns **numFound: 2**, of which this is the only study; the other is a practitioner article.

**That is the entire measured evidence base for AI in special-education paperwork: one
randomised trial of 22 novice teachers on one sub-task.** Every larger claim in the market is
`VENDOR`.

### 7.6 What is *not* measured, and should be said plainly

- **There is no current national time-use study.** The best federal data is from 2002. ED's own
  2006 impact analysis admits *"we lack detailed data on the number of IEP Team meetings conducted
  each year"* (71 FR 46845) and works from an assumed **1.2 meetings per child per year** at **1.5
  hours** each. Twenty years on, the field is still estimating.
- **The federal §618 collection does not code dispute issue categories.** There is no national
  dataset answering "is it eligibility, LRE, services, or procedure?"
- **School psychologist and speech-language pathologist caseload figures are published by NASP
  and ASHA** and are the right sources; the NASP series (annual, using NCES counts) is at ERIC
  ED662590 / ED662727 / **ED673365 (2023–24)**. The ED673365 full text returned **HTTP 404** from
  files.eric.ed.gov on 2026-07-28 and the specific national ratio is therefore **UNVERIFIED
  here** — do not quote a number for it without retrieving the brief.
- **No published evaluation of AI paperwork reduction in special education met an evidence bar
  in this search.** Treat all vendor time-savings claims as `VENDOR` until a controlled
  comparison exists. Given NULL 1 and NULL 2 above, the prior should be sceptical.

### 7.7 The finding, stated as the brief asked

**If AI's contribution here is administrative rather than instructional, that is a finding — and
it is the largest practical one in this section.** But it must be stated with the nulls attached,
or it is just another promise:

> The binding constraint on special education is adult hours, and a substantial and unmeasured
> fraction of those hours is not instruction. At a legal maximum California caseload the
> administrative load implied by federal per-child measurements is **four times** the time
> teachers report having. Two prior labour-saving interventions — computerisation and human
> delegation — were **measured and found to have no significant effect**, the second because the
> work is judgement rather than throughput. That is the specific gap a language model might
> genuinely close, and it is the specific reason no one should assume it will.

---

## 8. Escalation and safeguarding in a school context

### 8.1 The federal floor and the state patchwork

`STATUTE` — the federal requirement is **CAPTA, 42 U.S.C. §5106a(b)(2)(B)(i)**, which
conditions state grants on the state having *"provisions or procedures for requiring certain
individuals to report known or suspected instances of child abuse and neglect."* Federal law
sets no reporter list, no standard, and no timeline. **All of the operative rules are state
law**, and they differ in ways that matter to any product with a disclosure path.

Source for all figures in this subsection: Child Welfare Information Gateway, Children's
Bureau/ACYF/ACF/HHS, *Mandatory Reporting of Child Abuse and Neglect*, State Statutes series,
**current through May 2023**. `STATUTE` (state-statute compilation)

- **~46 states**, DC, American Samoa, Guam, CNMI and the Virgin Islands designate professions
  as mandated reporters. School personnel are on every such list.
- **~17 states and Puerto Rico require *any person* to report.** Of those, 13 states and
  Puerto Rico name professions *and* also require all persons. **Four states — Indiana, New
  Jersey, North Carolina, Wyoming — require all persons and name no professions at all.**
- **Standards vary.** The common trigger is that the reporter, *in their official capacity*,
  "suspects or has reason to believe" a child has been abused or neglected. A second common
  formulation triggers on knowledge or observation of conditions that "would reasonably result
  in harm."
- **Training is not universal.** 23 states, Puerto Rico and the Virgin Islands require
  mandated reporters to be trained; 22 states and DC do not require it in law.

**How much of the national reporting volume schools actually carry — and a widely-repeated claim
that is now out of date.** `MEASURED-ADMIN` — HHS/ACF, NCANDS *Child Maltreatment 2024*,
verbatim: *"professionals submitted **70.9 percent** of reports… The highest percentages of
reports are from **legal and law enforcement personnel (21.8%), education personnel (20.8%)**,
and medical personnel (11.0%)."*

| Federal fiscal year | #1 source | #2 source |
|---|---|---|
| 2018 | **Education 20.5%** | Legal/law enforcement 18.7% |
| 2019 | **Education 21.0%** | Legal/law enforcement 19.1% |
| 2020 | Legal/law enforcement 20.9% | Education **17.2%** |
| 2021 | Legal/law enforcement 21.8% | Education **15.4%** |
| 2022 | Legal/law enforcement 21.2% | Education 20.7% |
| 2023 | Legal/law enforcement 21.4% | Education 21.1% |
| 2024 | Legal/law enforcement 21.8% | Education 20.8% |

**The common claim that education personnel are the largest single source of maltreatment
referrals was true through FFY2019 and has not been true since.** Education was displaced during
COVID school closures (21.0% → 17.2% → 15.4%) and has not regained the top position in any year
FFY2020–FFY2024. **Correct phrasing: the largest or second-largest source, consistently about
one in five of all referrals.** Context from CM2024: **4,365,000 referrals** covering ~7,693,000
children; **47.1% screened in, 52.9% screened out**; 532,228 victims; mean CPS response time 104
hours.

**On substantiation by source — a number that does not exist and should not be invented.**
NCANDS does not publish substantiation rate by report source. The closest is CM2022 Table 7–3, a
special-focus table that does not recur in later editions: legal and law enforcement produced
237,837 substantiated maltreatment types (**37.9%**) against 21.2% of reports, while education
produced 72,189 (**11.5%**) against 20.7% of reports. **CM2022 itself warns that the two tables
use different denominators, units and state coverage**, so the implied 3× conversion-rate
difference is `INFERENCE` and must not be presented as a substantiation rate. What *is* clean:
composition of education-source substantiations — neglect **58.6%**, physical abuse 20.1%,
**sexual abuse 11.4%**, psychological 6.1%. **Schools are disproportionately where sexual abuse
surfaces.**

### 8.2 The routing question — and why it is the crux for AI

This is the part that decides whether an automated escalation path is safe or negligent.

Verbatim from the Child Welfare Information Gateway compilation:

> "Statutes in 33 States, the District of Columbia, and the Virgin Islands provide procedures
> that must be followed in those cases. In **18 States**, the District of Columbia, and the
> Virgin Islands, **any staff member who suspects maltreatment must notify the head of the
> institution** when the staff member feels that maltreatment or possible maltreatment should
> be reported to an appropriate authority. In **nine States**, the District of Columbia, and
> the Virgin Islands, **the staff member who suspects maltreatment notifies the head of the
> institution first, and then the head or their designee is required to make the report.** In
> **10 States**, **the person who suspects maltreatment must first make the report to the
> appropriate child protection authority and then notify the institution that a report has
> been made.**"

And the clause that governs everything:

> "Laws in **17 States**, the District of Columbia, and the Virgin Islands make clear that,
> **regardless of any policies within the organization, the mandatory reporter is not relieved
> of their responsibility to report.** In **12 States**, an employer is expressly prohibited
> from taking action to prevent or discourage an employee from making a report. In **17
> States**, an employer is expressly prohibited from retaliating against an employee who has
> made a report."

The 17 non-relief states: **AK, CA, FL, IN, IA, KY, ME, MI, MO, ND, OK, OR, SC, TN, TX, WV,
WY.** The 9 where the institution head reports: **GA, ID, IN (hospitals), KY, ME, MA, SD, VA,
WY**. The 10 where the staff member must report *first* and then notify the institution: **CA,
CT, HI, IL, IN (schools), MI, NY, PA, TN, WV**.

**Three state statutes settle the AI question directly. Quoted verbatim because paraphrase
would soften them.**

`STATUTE` — **Texas Family Code §261.101(b)**:

> "…the professional shall make a report not later than the 48th hour after the hour the
> professional first has reasonable cause to believe… **A professional may not delegate to or
> rely on another person to make the report.** …The term includes teachers, nurses, doctors,
> day-care employees…"

`STATUTE` — **California Penal Code §11166(i)(1)–(3)**:

> "(1) **The reporting duties under this section are individual**, and no supervisor or
> administrator may impede or inhibit the reporting duties… **An internal policy shall not
> direct an employee to allow the employee's supervisor to file or process a mandated report
> under any circumstances.**
> (2) The internal procedures shall not require any employee… to disclose the employee's
> identity to the employer.
> (3) **Reporting the information… to an employer, supervisor, school principal, school
> counselor, coworker, or other person shall not be a substitute for making a mandated report**
> to an agency specified in Section 11165.9."

The only sanctioned "someone else files for me" mechanism, §11166(h), requires two or more
*mandated reporters* with *joint knowledge* who *agree*, and then: *"Any member who has
knowledge that the member designated to report has failed to do so **shall thereafter make the
report**."* **The personal duty revives and never extinguishes.**

`STATUTE` — **Michigan MCL 722.623(1)(a)**: *"**A notification to the person in charge of a
hospital, agency, or school does not relieve the member of the staff… of the obligation of
reporting to the department** as required by this section."* And **Fla. Stat. §39.201(2)(b)**:
*"Nothing in this section… may be construed to **remove or reduce the duty and responsibility of
any person**… to report."*

**Timeframes** `STATUTE`: California §11166(a) — *"immediately or as soon as is practicably
possible,"* written follow-up **within 36 hours**. Texas §261.101 — universal duty
*"immediately"*; professionals **not later than the 48th hour**. Michigan MCL 722.623(1)(a) —
*"immediate report,"* written within **72 hours**. Florida §39.201(1)(a)1 — *"report
**immediately** to the central abuse hotline."*

**Penalties** `STATUTE` — Child Welfare Information Gateway, *Penalties for Failure to Report*
(current through February 2019): *"Approximately **49 States**… impose penalties… Failure to
report is classified as a **misdemeanor or similar charge in 40 States**… jail terms ranging
from **30 days to 5 years**, fines ranging from **$300 to $10,000**."* Florida makes it a
**felony** and imposes up to **$1 million** on an institution of higher learning that fails to
report or prevents reporting. Civil liability in addition to criminal in AR, CO, IA, MI, MT, NY,
RI. **Wyoming has no failure-to-report penalty statute at all** — and is one of the four pure
"any person" states.

**Federal floor, with a citation correction most secondary sources get wrong.** `STATUTE` — the
CAPTA definition of "child abuse and neglect" is **no longer at 42 U.S.C. §5106g**; Pub. L.
111-320 §142(b) (20 December 2010) struck it and relocated it to Pub. L. 93-247 §3, set out as a
Definitions note under **42 U.S.C. §5101**. Anyone citing §5106g is citing pre-2010 law. The
mandate hook is **42 U.S.C. §5106a(b)(2)(B)(i)**, a *funding condition on states* requiring *"a
State law for mandatory reporting."* `INFERENCE` — **federal law says nothing about who or what
may *perform* the reporting act. The delegation question is resolved entirely at state level,
and at state level the answer is no.**

**Four consequences, stated flatly.**

1. **The duty is personal, and in at least 17 states plus DC and the Virgin Islands expressly
   non-delegable — with Texas prohibiting delegation in terms.** It attaches to the human who
   formed the suspicion. **An AI cannot hold it, cannot discharge it, and cannot be interposed
   between the human and the authority.** Texas §261.101(b) forecloses both readings at once:
   if an AI counts as "another person," delegating to it is prohibited conduct; if it does not,
   the teacher has delegated to a non-person and has simply failed to report.
2. **An in-product "flag to admin" workflow is not a report.** California §11166(i)(3) says so
   in terms. And §11166(i)(2) additionally bars internal procedures that require the reporter to
   disclose their identity to the employer — **which most SaaS audit logging does by default.**
3. **The correct routing differs by state and it inverts.** In nine states the staff member
   tells the head and *the head reports*; in ten the staff member *reports first*. **A product
   with one hard-coded escalation flow is wrong in roughly half the country**, and being wrong
   in the direction of "route to the principal" is the documented failure mode — see §8.4.
4. **The statutes have no vocabulary for a system that forms the suspicion.** §11166(a) ties the
   duty to the reporter's *"professional capacity"* and to that human's own knowledge. The
   defensible claim is therefore narrower and sharper than "AI cannot report": **in no US
   jurisdiction does an AI system's flag discharge the individual mandated reporter's duty, and
   in Texas, California and Michigan — plus fourteen more per the Children's Bureau — the
   statute forecloses the reading that routing a concern to any intermediary discharges it. An
   AI can at most be a detection aid feeding a human who must then personally report.**

### 8.3 Academic concern vs safeguarding concern

The two look similar from inside a piece of software — both are "something is wrong with this
child" — and they are governed by entirely different regimes with entirely different clocks.

| | **Academic / educational concern** | **Safeguarding concern** |
|---|---|---|
| Trigger | Lack of expected progress, non-response to intervention, new skill deficit | Suspicion of abuse, neglect, self-harm, or immediate danger |
| Who it goes to | Case manager → student support / MTSS team → IEP team | The named mandated reporter, then CPS or law enforcement per state routing |
| Clock | Weeks. §300.324(b)(1)(ii)(A) requires revision on lack of expected progress; H1's trend rule says 7–10 weeks of probe data before a method change | **Immediately**, on suspicion. No accumulation of evidence, no confidence threshold |
| Evidentiary standard | Data-based; §300.309(b)(2) documentation | **Suspicion**, expressly not proof. The reporter's job is to report, not to investigate |
| Who decides | A team including the parent | The individual reporter, alone |
| Consent | Parental consent required for evaluation (§300.300(a)) | **No parental consent, and no parental notification requirement** |

**The last row is the one that breaks naive product design.** Every other flow in this report
routes through the parent. Safeguarding does not, and must not — a system that notifies the
parent of a safeguarding flag may be notifying the person the child needs protection from.
**A product that has one "notify the guardian" pathway has built a mechanism for endangering
children.** That is a design defect, not a policy preference. `INFERENCE` — from the structure
of mandated reporting, and it is a hard requirement, not a recommendation.

Two more asymmetries a coordinator would name:

- **The academic path tolerates waiting; the safeguarding path punishes it.** The instinct an
  AI system is trained into — gather more evidence, raise confidence, avoid false positives —
  is correct for the left column and actively wrong for the right one.
- **The academic path is reversible; the safeguarding path is not.** A wrongly-changed reading
  intervention can be changed back. A report to CPS cannot be unmade, and §8.4 documents whom
  those reports fall on.

### 8.4 Documented failure modes

**(1) "Report it to the principal" — the failure the statutes were written against.** In nine
states plus DC and the Virgin Islands, telling the head of the institution *is* the required
first step and the head then reports. In ten states it is expressly the wrong order. And in 17
states plus DC and the Virgin Islands the statute has to say out loud that institutional policy
does not relieve the individual — a clause legislatures do not write unless the failure is
common. `STATUTE` — the existence and wording of the non-relief provisions is itself the
documentation of the failure mode.

**(2) Under-training.** 22 states and DC do not require mandated-reporter training by law
(Child Welfare Information Gateway, current through May 2023). A duty that attaches personally,
triggers on suspicion, carries criminal exposure in many states, and has no required training
in nearly half the country is a system with a predictable error rate. `STATUTE`/`INFERENCE`.

**(3) The disability interaction.** Children with disabilities are simultaneously at elevated
risk of maltreatment and less likely to be able to disclose it in a form an adult recognises —
which is exactly the population this survey is about, and exactly the population for whom a
communication-mediating system sits between the child and the adults. A system that becomes the
main channel through which a non-speaking or language-impaired child communicates has, whether
or not anyone intended it, become a disclosure surface. `INFERENCE` — H1 §4.6 establishes the
language/reading-access archetype; the disclosure implication follows and is not optional to
design for.

**(4) The over-referral risk runs the other way, and the base rates are extreme.**
`MEASURED-ADMIN` — Kim, Wildeman, Jonson-Reid & Drake (2017), *American Journal of Public
Health* 107(2):274–280, DOI 10.2105/AJPH.2016.303545, PMID 27997240; NCANDS Child Files
2003–2014 with Census denominators, synthetic-cohort life tables, verbatim:

> "**37.4% of all children experience a child protective services investigation by age 18
> years.** …a higher rate for **African American children (53.0%)** and the **lowest rate for
> Asians/Pacific Islanders (10.2%)**."

**A 5.2× spread, on a base rate where more than one child in three is investigated before
adulthood.** An automated flag lowers the cost of raising a concern to nearly zero, and anything
that lowers that cost raises volume — into a system with that distribution. `OBSERVED` — Krase
(2015), *Children & Schools* 37(2), ERIC EJ1061332: *"**racial disproportionality and disparity
in reporting by educational personnel exist at the national level and significantly differ
within a state.**"*

**A sensitivity setting on a safeguarding classifier is a policy decision about which families
get investigated, and it must never be set by a vendor default.** `INFERENCE`.

**(5) And more volume probably means worse signal, not better detection.**
`MEASURED-QUASI` (natural experiment) — S. Kim (2025), EdWorkingPaper 25-1214,
Annenberg/Brown, ERIC ED674099, exploiting county-level variation in remote-instruction weeks in
2020–21 against NCANDS: counties with higher remote exposure had *"**fewer screened-in
allegations of school-aged children, but a higher substantiated allegations and an increase in
maltreatment-related child fatalities. The reduction in allegations was primarily driven by
those reported by education personnel.**"*

Both halves matter and they cut in opposite directions. Educator reporting does real detection
work — removing it raised substantiated cases *and* fatalities. But its volume is partly
threshold-driven: fewer reports, **higher** substantiation rate among those remaining.
`INFERENCE` — **an AI that increases flag volume should be expected to lower the substantiation
rate rather than raise detection.**

### 8.4b ★ The failure quantified: NIS-4

`MEASURED` — Sedlak et al. (2010), *Fourth National Incidence Study of Child Abuse and Neglect
(NIS-4): Report to Congress*, HHS/ACF/OPRE. **10,791 sentinel professionals in 1,094 agencies.**
Verbatim, §8.1 at 16–17:

> "**School sentinels recognized 52% of the children who suffered Harm Standard maltreatment**
> and 39% of the Endangerment Standard total."
> "CPS investigated the maltreatment of **only 32%** of children who experienced Harm Standard
> maltreatment…"
> "**The lowest rates of investigation occurred for children recognized at schools (20% or less
> across the definitional standards)**, day care (12% or less), or shelters (19% or less)."

**Roughly 80% or more of the maltreatment recognised by school staff never reached a CPS
investigation.** Police and sheriff sentinels: 53–64%.

**And NIS-4 locates the failure precisely**, which is what makes it usable. Verbatim at 17:

> "The CPS Screening Policies Study… indicated that **CPS probably would have investigated nearly
> three-fourths (72%) of the uninvestigated children who experienced Harm Standard maltreatment**
> and two-thirds (66%) of the uninvestigated children with Endangerment Standard maltreatment."

`INFERENCE` — **the bottleneck is recognition→report, not CPS screening capacity.**

**School staff are the worst non-reporters of the four sentinel groups.** Verbatim, §8.5.3 at
8–41 to 8–43:

> "Whereas an average of **23% of all sentinels** said they would not report the countable
> maltreatment cases to CPS, **29% of school sentinels** did so… An average of **33% of school
> sentinels say they would not report situations described in neglect vignettes** compared to
> 21%–26% of sentinels in the other three agency groups."

Table 8–6 (uninvestigated % / % of sentinels who would not report): all maltreatment 74% / 23%;
sexual abuse 53% / 6%; all neglect 85% / 28%; **educational neglect 93% / 35%**.

**And the "report it to the principal" failure mode, measured.** Verbatim, §8.1 at 18:

> "More sentinels from health and law enforcement (**96% or more**) said their agencies allowed
> them to **report directly to CPS (versus having to go through an agency representative or
> committee) than did sentinels in schools (80%)**… Moreover, when allowed to do so, **fewer
> sentinels in schools… said they had ever reported a case (54%…) compared to 87% of law
> enforcement sentinels and 77% of sentinels in health agencies.**"

**One in five school staff cannot report directly to CPS at all; among those who can, only 54%
ever have.**

**(6) Self-report on this topic is systematically optimistic.** `MEASURED` — Kenny (2001),
*Child Abuse & Neglect* 25(1):81–92, PMID 11214815, n = 197 teachers: *"**Seventy-three percent
of this sample reported that they had never made a report of child abuse**… **Only 11% of
teachers reported that there were instances in which they believed abuse may have occurred, but
failed to report.** …**The teachers' responses to the case vignettes were not consistent with
their previous reports.** …when presented with legally reportable case vignettes, many failed to
report."* Corroborated by Walsh et al. (2012), *Children and Youth Services Review*, whose title
is the finding: *"Understanding teachers' reporting of child sexual abuse: **Measurement methods
matter**."*

**(7) ★ And training does not fix it — the Cochrane null.** `MEASURED-META` — Walsh, Eggins,
Hine, Mathews, Kenny et al. (2022), "Child protection training for professionals to improve
reporting of child abuse and neglect," *Cochrane Database of Systematic Reviews* Issue 7, DOI
10.1002/14651858.CD011775.pub2, PMID 35788913. **11 trials, 1,484 participants.** Self-reported
reports SMD 0.81 [0.18, 1.43], **very low certainty**, n = 42; vignette responses SMD 1.81
[1.30, 2.32], **very low certainty**, n = 87. Verbatim:

> "**We identified no studies that measured the number of cases of child abuse and neglect via
> official records of reports made to child protection authorities, or adverse effects of
> training.** …However, the evidence is very uncertain."

**In eleven trials, zero measured reports against official CPS records and zero measured adverse
effects.** The entire evidence base rests on the two measures Kenny showed diverge from each
other.

### 8.4c ★ Suicide-risk gatekeeping: the null that reframes the whole detection argument

`MEASURED-RCT` — Wyman, Brown, LoMurray, Schmeelk-Cone et al. (2008), *Journal of Consulting and
Clinical Psychology* 76(1):104–115, PMID 18229988. Group-randomised, **32 schools, 249 staff**,
QPR gatekeeper training, ~1-year follow-up, plus 2,059 8th and 10th graders surveyed. Verbatim:

> "Gatekeeper-training programs… are **widespread but largely untested**. …training increased
> self-reported **knowledge (ES = 0.41)**, **appraisals of efficacy (ES = 1.22)**, and **service
> access (ES = 1.07)**. …**Consistent with the communication model, increased knowledge and
> appraisals were NOT sufficient to increase suicide identification behaviors.** Also
> consistent… were results from 2,059 8th and 10th graders surveyed showing that **fewer students
> with prior suicide attempts endorsed talking to adults about distress.**"

**Large, clean effects on knowledge and confidence. No increase in the behaviour that matters.
And the reason is on the student side: the highest-risk students are the least likely to talk to
an adult at all.**

Confirmed meta-analytically. `MEASURED-META` — *Prevention Science* 25:978–988 (2024), PMID
39023720, **43 studies, 21,720 participants**: behavioural *intention* 1.03 [0.80, 1.25]
post-training; actual *intervention behaviour* 0.33 [0.21, 0.46] short-term and **0.22 [0.14,
0.30] long-term**. **Intention effects are roughly 4.7× larger than behaviour effects**, and the
authors flag *"the low methodological quality of the currently available evidence."* A second
meta-analysis, *BMC Public Health* 25:1206 (2025), PMID 40165179, 16 RCTs: knowledge SMD 0.72
decaying to 0.25 long-term; offline self-efficacy **non-significant** (0.53, CI [−0.08, 1.17]).
**Neither meta-analysis reports attempts or deaths as an outcome.**

**The read-across, and it is the most important inference in this section.** `INFERENCE` — Wyman
decomposes safeguarding into *detection capability* and *disclosure behaviour*, and shows the
binding constraint is **disclosure**. NIS-4 shows the same thing from the other end: the failure
is recognition→report, and CPS would have investigated 72% of what it never saw. **An AI that
improves detection capability is intervening on the non-binding constraint.**

There is one plausible counter — that children will disclose to a machine what they will not
disclose to an adult. It is a real hypothesis, it is exactly the kind of thing this project
should want to be true, and **Wyman does not test it and neither does anything else located
here.** It needs its own evidence before anyone builds on it.

For contrast, the interventions that *do* move behaviour work on the student side, not the staff
side. `MEASURED-RCT` — Wyman et al. (2010), *AJPH* 100(9):1653–1661, PMID 20634440, **18 high
schools randomised, 453 peer leaders, 2,675 students**: *"**Trained peer leaders in larger
schools were 4 times as likely as were untrained peer leaders to refer a suicidal friend to an
adult.** …**Perception of adult support increased most in students with a history of suicidal
ideation.**"* Same author, opposite result, different target. And SOS Signs of Suicide
(Aseltine & DeMartino 2004, *AJPH* 94(3), PMID 14998812; replicated Aseltine et al. 2007, *BMC
Public Health* 7:161, 4,133 students across 9 schools) reports significantly lower self-reported
attempt rates — with the authors themselves flagging that *"differential attrition is the most
serious limitation"* and all outcomes being self-reported rather than record-based.

### 8.4d ★ Automated flagging in schools: measured false-positive rates

`OBSERVED` (primary documents via public-records requests) — Electronic Frontier Foundation,
*GoGuardian: A Red Flag Machine By Design*, redflagmachine.com/research, based on FOIA requests
to more than ten districts in CA, FL, NM, RI and TX.

**Volume, from the vendor.** `VENDOR` — GoGuardian CEO Advait Shinde, 2021 letter to Senators
Warren and Markey: *"Over the course of 2020, Admin generated **44 million alerts or
approximately 4.6 alerts per student** over 2020… approximately 90% were for explicit or
inappropriate content and **approximately 10% were for self-harm.**"* Across 6,700
schools/districts and 9.5 million monitored accounts that is roughly **4.4 million self-harm
alerts in a single year** (`INFERENCE`, arithmetic on the vendor's own figures). The same letter:
*"some larger school districts can generate upwards of **50,000 alerts per day**."*

**Precision, from the districts' own logs.** `OBSERVED`:

- **Alvord ISD (TX)**, 15 Feb – 22 Mar 2023: 2,313 websites flagged, **14% for the keyword
  "unblocked"** — students looking for video games.
- **Imperial USD (CA)**, 10–17 Mar 2023: **more than 25% of 15,000 flags** were "unblocked."
- **Imperial USD census, 6 days, ~4,400 students: 9,387 flagged website visits** — including 548
  YouTube Shorts, 107 visits to the YouTube front page, 427 Spotify, 157 Wikipedia, **68 to the
  district's own Instructure learning platform**, 72 searches for political cartoons, 44 job
  searches, and **44 visits to the United States Holocaust Memorial Museum's website.** EFF,
  verbatim: *"**We found no direct references to suicide**"* — the only near-hit was a rapper's
  song titled *Suicidal*.
- **Lake Travis ISD (TX)**, Feb–Mar 2023: **more than 900 website visits flagged for the term
  "colon"** — punctuation, mathematical formulae, biographies of Cristóbal Colón, anatomy. Other
  systematic false-positive keywords: "cox," "wang," "nazi" (WWII research), "sex" (biology).

**The specific harm to the population this survey is about.** `OBSERVED` — Lake Travis ISD, 15
Feb – 17 Mar 2023: *"more than 75 websites"* flagged with "transgender," "LGBT," "gay,"
"homosexual," "non-binary" or "queer" in the URL — including an academic paper on family
rejection and suicide among transgender adults, a Planned Parenthood transition resource, and
the Wikipedia Transgender Rights page. Documented incident, Alvord ISD, May 2022: before school
opened, a student searched *"am I gay test,"* opened a quiz site, and triggered an "explicit"
alert escalated to administrators — flagged partly because the string "testi" appears in a
**Finnish** translation entry in the page source. EFF's conclusion: the software *"effectively
out[s] them to that staff."* Both GoGuardian and Gaggle removed LGBTQ keywords after EFF's 2022
records requests, and the 2023 data still flagged the same content through "sex" and "breasts."

`OBSERVED` — racial skew in the same corpus: *"of the **43 individual songs on Spotify flagged
by GoGuardian in Imperial USD during a 30 day period, 85% were by Black artists**."*

**The vendor's own admissions**, `VENDOR`: flags fire on **page source**, and *"the specific
word(s) flagged may not have been visible to the student"*; the Smart Alerts feature exists *"to
reduce some of the **unnecessary and often times innocuous noise** that Flagged Activity can
create"*; its threshold is *"50% or more confident"*; *"a search for cats may cause what may
appear to be inappropriate flagged activity."* And adoption: *"Of more than 10 school districts
we queried, **only one was using Smart Alerts**."*

**And the routing.** `OBSERVED` — Baltimore City Public Schools told *The Real News*: *"Clinical
supervisors, school police, principals and designated school staff receive all GoGuardian
alerts,"* and *"**wellness checks are conducted by school police.**"*

**The arithmetic is the argument.** NIS-4 says at least 80% of school-recognised maltreatment
never reaches an investigation and that CPS would have investigated 72% of it — so the binding
constraint is human recognition and follow-through. GoGuardian generates 4.6 alerts per student
per year and, in a six-day census of 4,400 children, produced 9,387 flags containing **zero**
genuine suicide references. **Adding alert volume to a pipeline whose binding constraint is human
follow-through is intervening on the wrong constraint, and it does so by routing children's
searches to school police.** `INFERENCE`.

### 8.5 The discipline path, which is where safeguarding and IDEA collide

`STATUTE` — **§300.530(e)(1)**: within **10 school days** of any decision to change a child's
placement because of a code-of-conduct violation, the LEA, the parent, and relevant IEP Team
members must review all relevant information to determine:

> "(i) If the conduct in question was caused by, or had a direct and substantial relationship
> to, the child's disability; or (ii) **If the conduct in question was the direct result of the
> LEA's failure to implement the IEP.**"

If either is met, the conduct **is** a manifestation (§300.530(e)(2)), and if it is (e)(1)(ii),
*"the LEA must take immediate steps to remedy those deficiencies"* (§300.530(e)(3)).

**Read (e)(1)(ii) as a builder.** It makes *non-implementation of the documented programme* a
formal legal finding available at every disciplinary removal. A system that is responsible for
delivering a documented service and silently fails — the session that did not run, the
accommodation that was not applied, the minutes that were not delivered — has created evidence
for a manifestation determination against its own district. **Reliable delivery logging is not
a nice-to-have in this domain; it is the artefact that answers §300.530(e)(1)(ii).**
`INFERENCE` from the regulation.

The rest of the discipline frame, briefly: removals up to **10 consecutive school days** without
special process (§300.530(b)(1)); services must continue after 10 cumulative days
(§300.530(b)(2), (d)); a change of placement occurs at more than 10 consecutive days or a
qualifying **pattern** of removals (§300.536(a)); and **45 school days** in an interim alternative
setting regardless of manifestation for weapons, drugs, or serious bodily injury (§300.530(g)).

---

## 9. What a coordinator's week actually looks like — and which parts an AI may touch

### 9.1 The week, assembled from the regulations and the measured hours

Nothing below is invented. Each element is either a statutory duty with a citation or a measured
time cost from §7.

**Standing, every week**
- Direct instruction and service delivery — the part of the job the job is named after.
- Consultation with general-education teachers, who under §300.323(d)(2) must be informed of
  their specific responsibilities and of *"the specific accommodations, modifications, and
  supports that must be provided."* Every new teacher, every schedule change, every substitute
  is a re-notification event.
- Progress-monitoring probes and their graphing — the §300.320(a)(3) measurement method, and the
  §300.309(b)(2) evidentiary record.
- Administrative duties and paperwork: median **5 hours**, against **4** available (SPeNSE).

**On a rolling cycle**
- IEP meetings: **1.5 hours** each in attendance, **2 hours** to write the document, plus
  **2 hours/month** scheduling and **1 hour/month** mailing notices — and each meeting carries
  the §300.322 parent-participation duties, including the §300.322(d) record of attempts if the
  parent does not attend and the §300.322(e) duty to *"take whatever action is necessary to
  ensure that the parent understands the proceedings."*
- Progress reports: **8 hours** per cycle, every **7 weeks**.
- Evaluations: for the 35% who do initial evaluations, **7.5 hours/month** administering and
  **4.2** reviewing; for the 51% who do triennials, **5** and **3**.
- Behaviour: **5 hours/month** on behaviour logs, **2** on behaviour intervention plans, **2** on
  functional behavioural assessments.

**On the compliance calendar**
- 60 days from consent to evaluation (§300.301(c)(1)).
- 30 days from eligibility to the IEP meeting (§300.323(c)(1)).
- An IEP in effect for every child at the start of the school year (§300.323(a)).
- Annual review (§300.324(b)(1)(i)); triennial reevaluation (§300.303(b)(2)).
- Procedural safeguards notice once a year and on the triggers in §300.504(a).
- 10 school days to a manifestation determination after a disciplinary placement change
  (§300.530(e)(1)).

**Unscheduled, and non-deferrable**
- A safeguarding disclosure. Personal duty, immediate, routed around the parent (§8).
- A crisis: behaviour, a removal, a parent's IEE request that starts the §300.502(b) clock, a
  transfer student arriving mid-year who must receive comparable services immediately
  (§300.323(e)–(f)).

### 9.2 Which of these an AI can touch

**Can touch, and should.** Everything on the compliance calendar. Scheduling. Notice generation
and translation. The §300.322(d) attempts log. Progress-report assembly against a stated
criterion. First-draft PLAAFP prose with per-sentence provenance. Goal measurability checking.
Internal-consistency checking of the document. Assembling the §300.305(a) existing-data review
packet. Preparing the parent to participate. Generating §300.503(b)(6) alternatives-considered
text. Logging service delivery against the IEP — which is the artefact that answers
§300.530(e)(1)(ii).

**Cannot touch.** The nine items in the prohibition column of §11: authorship of the IEP, the
eligibility certification, the placement decision, service quantities, modifications, the
determination that progress is or is not adequate, the safeguarding report, the consent, and the
agency's stated reasons in a PWN.

**Would be actively dangerous to touch.** Four, and they are not the same as "cannot":

1. **Safeguarding triage.** Not merely prohibited — a confidence threshold on a disclosure is a
   decision to let some children's disclosures fail silently, taken by a system whose error
   profile nobody has characterised on this population. And it converts a personal, non-delegable
   statutory duty into a queue.
2. **Placement recommendation.** Four circuits, four incompatible tests (§10.2). A recommendation
   is legally incoherent before it is even evaluated for accuracy, and it will be produced in
   discovery as the district's contemporaneous reasoning.
3. **Silent modification of the curriculum.** An adaptive system that shortens, simplifies or
   accepts-partial has made a curricular decision reserved to the team and made it invisibly
   (§2.6). It is dangerous specifically because it is *invisible* — it will not appear in any
   log, any meeting, or any dispute, and its effects compound across years toward a diploma
   track nobody chose.
4. **Producing a confident recommendation before the meeting.** This is *Deal* (§10.3) and it is
   dangerous because it is the most natural thing for the technology to do and the most useful to
   the humans in the short run. A team that ratifies a machine draft has held a meeting that a
   hearing officer can find was not meaningful.

**The pattern.** An AI may operate on **documents, calendars and data**. It may not operate on
**entitlements, determinations, or disclosures**. The dangerous zone is not where the
prohibitions are obvious — nobody is shipping an IEP auto-signer. It is where a helpful
behaviour quietly crosses into a reserved decision.

### 9.3 The reframing this forces on `survey/04`

`survey/04` §4.1 establishes that measurement without a decision rule is inert, and §4.2 that
the slow loop takes 7–10 weeks. Both are correct. Both are also *instructional* framings of a
job that is roughly half something else.

The honest synthesis: **the fast loop is instruction, the slow loop is instruction, and the
third loop — the one neither section names — is compliance, and it runs on a calendar rather
than on data.** An AI that only serves the first two loops is helping with the part of the week
that is already the most rewarding. **An AI that serves the third returns hours to the first
two.** That is the mechanism by which an administrative contribution becomes an instructional
one, and it is the argument `survey/04` is currently missing.

### 9.4 What happens when it goes wrong — dispute volume and documented systemic failure

`OBSERVED` — U.S. Department of Education, OSEP, **IDEA Part B Dispute Resolution Survey,
2023–24** (EDFacts Metadata and Process System; data extracted 13 November 2024), national
totals:

| Measure | SY 2023–24 |
|---|---|
| Written, signed State complaints filed | **9,927** |
| — reports issued | 5,894 |
| — **reports with findings** | **3,696 (62.7% of reports issued)** |
| Mediation requests | 12,914 |
| — mediations held | 7,085 (54.9%) |
| **Due process complaints filed** | **39,151** |
| — resolution meetings held | 5,852 |
| — resolution meetings reaching written settlement | 1,623 (27.7%) |
| — **hearings fully adjudicated** | **8,621 (22.0%)** |
| — pending at year end | 9,864 (25.2%) |
| — **withdrawn or dismissed** | **20,666 (52.8%)** |
| Expedited due process complaints | 618 |

**Documented systemic failure 1 — the adversarial channel does not decide.** 52.8% of due process
complaints are withdrawn or dismissed and only 22.0% are fully adjudicated, while the low-cost,
paper-based state-complaint channel produces **findings against districts in 62.7%** of the cases
it decides. A system in which the cheap channel finds violations two-thirds of the time and the
expensive channel disposes of half its docket without a decision is not allocating disputes by
merit. `MEASURED-META` (arithmetic on the OSEP file).

**Documented systemic failure 2 — the volume is one state.** New York alone accounts for **26,708
of 39,151** due process complaints (**68.2%**) and **7,640 of 8,621** fully adjudicated hearings
(**88.6%**). The top five states are 88.9% of complaints and 96.6% of hearings. California files
4,555 complaints and adjudicates **49**. `OBSERVED` — and it means national dispute statistics
are, in practice, statistics about New York.

**Documented systemic failure 3 — most states are not meeting IDEA requirements, on the
Department's own assessment.** U.S. Department of Education, *2026 Determination Letters on State
Implementation of IDEA*, **18 June 2026**. Part B, **"needs intervention"**: Bureau of Indian
Education, District of Columbia, Maine, New Mexico, **New York**, Vermont. Part B, **"needs
assistance for two or more consecutive years"**: **34 entities**, including Arizona, California,
Georgia, Hawaii, Louisiana, Michigan, Mississippi, North Carolina, Oregon, Puerto Rico, Tennessee,
Washington. **Only 22 entities met requirements.** Part C "needs intervention": Louisiana.
`OBSERVED`

The consequence is statutory, verbatim from the determination letters fact sheet: *"For States
that received a determination of 'needs assistance' for two or more consecutive years, the
Department must take one or more enforcement actions, including […] designating the State as a
high-risk grantee, or directing the use of State set-aside funds."*

**The co-occurrence worth naming:** New York is simultaneously the source of 68% of the nation's
due process complaints and under a federal "needs intervention" determination. Dispute volume and
formally-identified non-compliance co-occur. `OBSERVED` on the co-occurrence; `INFERENCE` on any
causal reading, and it should not be asserted.

**Documented systemic failure 4 — federal civil-rights enforcement capacity has fallen as demand
has risen.** `OBSERVED` — ED Office for Civil Rights, *Report to the President and Secretary of
Education* (FY 2024), verbatim: *"FY 2024 saw still another new record number of complaints filed
with OCR, at **22,687 complaints received**, up from 19,201 in FY 2023. The total number of
complaints has almost tripled since FY 2009, and during this same period OCR's number of full
time equivalent (FTE) staff has decreased from 629 to 588. […] **OCR's overall staffing level has
declined significantly – falling from nearly 1,100 FTE staff in FY 1981 to 588 FTE staff in FY
2024.**"* Disability allegations were **37% (8,457)** of FY2024 complaints (all education levels,
not K-12 only). Per-FTE caseload has moved from roughly 2.7 to 38.6 complaints per year.
`MEASURED-META` on the per-FTE arithmetic.

**Documented systemic failure 5 — child-find litigation is rising and districts win it.**
`MEASURED-META` — Zirkel, *"The 'Red Flags' for Child Find under the IDEA: Separating the Law from
the Lore," Exceptionality* (2015): 42 court decisions, late 1996 to early 2014, finding *"(a) an
upward trajectory in their frequency; (b) an outcome ratio of 2:1 in favor of the defendant school
districts."* Corroborated in the same author's *Exceptional Children* (2018) RTI/child-find
analysis (*"the majority of the rulings have been in favor of school districts"*) and *School
Psychology Review* (2011) ADHD analysis (51 rulings, *"the majority […] in favor of school
districts"*). Rising volume with a stable pro-district outcome ratio is the signature of an
under-identification problem that adjudication is not correcting. *(Read from ERIC abstracts;
full texts not retrieved — percentages are as stated in the abstracts.)*

---

## 10. The case law a coordinator actually operates under

All holdings below were retrieved from primary or archival full-text sources
(supremecourt.gov, tile.loc.gov US Reports, law.resource.org F.2d/F.3d mirror,
cdn.ca9.uscourts.gov). Source-reachability notes at §13.

### 10.1 The substantive standard: *Rowley*, then *Endrew F.*

`CASE-LAW` — ***Board of Education v. Rowley*, 458 U.S. 176, 206–07 (1982)**, verbatim:

> "Therefore, a court's inquiry in suits brought under § 1415(e)(2) is twofold. **First, has
> the State complied with the procedures set forth in the Act?** And second, is the
> **individualized educational program developed through the Act's procedures reasonably
> calculated to enable the child to receive educational benefits?** If these requirements
> are met, the State has complied with the obligations imposed by Congress and the courts
> can require no more."

**Half the federal test for whether a child received a free appropriate public education is
procedural.** That is the single fact most missing from `survey/04`, and it reframes
everything: in this domain, process is not overhead around the pedagogy. Process is half
the entitlement.

*Rowley* also sets the limit that protects instructional judgement from courts — and, by
extension, from anyone else: *"In assuring that the requirements of the Act have been met,
courts must be careful to avoid imposing their view of preferable educational methods upon
the States"* (458 U.S. at 206).

`CASE-LAW` — ***Endrew F. v. Douglas County School District RE-1*, 580 U.S. 386 (2017)**,
verbatim from the slip opinion:

> "**To meet its substantive obligation under the IDEA, a school must offer an IEP reasonably
> calculated to enable a child to make progress appropriate in light of the child's
> circumstances.**"

> "Of course this describes a general standard, not a formula. But whatever else can be said
> about it, **this standard is markedly more demanding than the 'merely more than de minimis'
> test applied by the Tenth Circuit.** […] When all is said and done, a student offered an
> educational program providing '**merely more than de minimis**' progress from year to year
> **can hardly be said to have been offered an education at all.**"

And the sentence that should govern every AI-assisted decision in this space:

> "A reviewing court may fairly expect those authorities to be able to **offer a cogent and
> responsive explanation for their decisions** that shows the IEP is reasonably calculated to
> enable the child to make progress appropriate in light of his circumstances."

**That is a judicially imposed explainability requirement, arrived at eight years before
anyone was arguing about explainable AI in schools.** A district using a system whose
recommendations it cannot explain cannot meet *Endrew F.*'s expectation. Not "should not" —
cannot. This is the strongest available argument that interpretability in this domain is a
legal requirement rather than a preference. `INFERENCE` from the quoted text, but a short one.

*Endrew F.* also makes **goal ambition** justiciable. A goal that locks in trivial progress
is no longer merely poor practice; it is substantively defective. Any AI that drafts goals by
extrapolating a child's historical trend line will systematically produce *Endrew F.*-deficient
goals, because a trend line encodes the status quo. `INFERENCE` — and it is a specific,
foreseeable, testable failure mode of the most-published AI application in special education.

### 10.2 LRE: four tests, and the circuit split is real

`CASE-LAW` — ***Daniel R.R. v. State Board of Education*, 874 F.2d 1036, 1048 (5th Cir. 1989)**,
verbatim:

> "Adhering to the language of the EHA, we discern a two part test for determining compliance
> with the mainstreaming requirement. **First, we ask whether education in the regular
> classroom, with the use of supplemental aids and services, can be achieved satisfactorily
> for a given child.** […] If it cannot and the school intends to provide special education or
> to remove the child from regular education, we ask, **second, whether the school has
> mainstreamed the child to the maximum extent appropriate.** […] no single factor is
> dispositive in all cases. Rather, our analysis is an individualized, fact-specific
> inquiry…"

Prong-one factors, verbatim:

1. **Steps taken to accommodate.** *"If the state has made no effort to take such
   accommodating steps, our inquiry ends, for the state is in violation of the Act's express
   mandate… **The Act does not permit states to make mere token gestures to accommodate
   handicapped students; its requirement for modifying and supplementing regular education is
   broad.**"*
2. **Educational benefit.** *"This inquiry necessarily will focus on the student's ability to
   grasp the essential elements of the regular education curriculum… We reiterate, however,
   that academic achievement is not the only purpose of mainstreaming."*
3. **Overall experience / non-academic benefit.** *"a child may be able to absorb only a
   minimal amount of the regular education program, but may benefit enormously from the
   language models that his nonhandicapped peers provide"* (at 1049).
4. **Effect on others.** *"If, however, the handicapped child requires so much of the teacher
   or the aide's time that the rest of the class suffers, then the balance will tip in favor
   of placing the child in special education."*

The court expressly refuses to use *Rowley*'s two-part test for LRE: *"the Rowley test thus
assumes the answer to the question presented in a mainstreaming case."*

`CASE-LAW` — ***Sacramento City Unified School District v. Rachel H.*, 14 F.3d 1398, 1404
(9th Cir. 1994)**, verbatim:

> "The result was a four-factor balancing test in which the court considered **(1) the
> educational benefits of placement full-time in a regular class; (2) the non-academic
> benefits of such placement; (3) the effect Rachel had on the teacher and children in the
> regular class; and (4) the costs of mainstreaming Rachel.** […] **Accordingly, we approve
> and adopt the test employed by the district court.**"

Factor 3 has a two-part sub-inquiry: *"(1) whether there was detriment because the child was
disruptive, distracting or unruly, and (2) whether the child would take up so much of the
teacher's time that the other students would suffer from lack of attention."* On cost, the
burden is the district's: *"the District did not meet its burden of proving that regular
placement would burden the District's funds or adversely affect services available to other
children."*

`CASE-LAW` — ***Roncker v. Walter*, 700 F.2d 1058, 1063 (6th Cir. 1983)**, the portability
test, verbatim:

> "In a case where the segregated facility is considered superior, the court should determine
> whether the services which make that placement superior **could be feasibly provided in a
> non-segregated setting.** If they can, the placement in the segregated school would be
> inappropriate under the Act."

With the three carve-outs and cost expressly in play: *"…because the handicapped child would
not benefit from mainstreaming, because any marginal benefits received from mainstreaming are
far outweighed by the benefits gained from services which could not feasibly be provided in
the non-segregated setting, or because the handicapped child is a disruptive force… **Cost is
a proper factor to consider since excessive spending on one handicapped child deprives other
handicapped children.**"*

`CASE-LAW` — ***Oberti v. Board of Education of Clementon School District*, 995 F.2d 1204,
1215 (3d Cir. 1993)** adopts *Daniel R.R.* and says why:

> "**the Roncker test fails to make clear that even if placement in the regular classroom
> cannot be achieved satisfactorily for the major portion of a particular child's education
> program, the school is still required to include that child in school programs with
> nondisabled children** (specific academic classes, other classes such as music and art,
> lunch, recess, etc.) whenever possible."

`CASE-LAW` — ***Hartmann v. Loudoun County Board of Education*, 118 F.3d 996 (4th Cir. 1997)**
applies *Roncker* through *DeVries v. Fairfax County School Board*, 882 F.2d 876, 879 (4th
Cir. 1989): mainstreaming is not required where *"(1) the disabled child would not receive an
educational benefit from mainstreaming into a regular class; (2) any marginal benefit from
mainstreaming would be significantly outweighed by benefits which could feasibly be obtained
only in a separate instructional setting; or, (3) the disabled child is a disruptive force in
a regular classroom setting."* *Hartmann* squarely rejects discounting disruption.

**The circuit map** — sourced from a court's own survey, ***L.B. ex rel. K.B. v. Nebo School
District*, 379 F.3d 966, 976–77 (10th Cir. 2004)**, not from a secondary summary:

| Test | Circuits |
|---|---|
| *Daniel R.R.* two-part | 3d, 5th, 10th (without the cost factor), 11th (*Greer*, with cost) |
| *Rachel H.* four-factor (*Daniel R.R.* + cost as co-equal factor) | 9th |
| *Roncker* portability | 4th, 6th, 8th |
| Cost acknowledged as relevant | 7th |
| Own framework, **expressly declined** *Daniel R.R.* | 1st (*Roland M.*; reaffirmed in *C.D. v. Natick Public School District*, 924 F.3d 621 (1st Cir. 2019): *"We reject both arguments"*) |
| **Not mapped from a retrieved source** | 2d, D.C. Cir. — `UNVERIFIED`. *P. ex rel. Mr. & Mrs. P. v. Newington Board of Education*, 546 F.3d 111 (2d Cir. 2008) is the mapping case; its full text could not be retrieved from four mirrors. Do not cite without independent verification. |

**Why this matters for a product and not just for lawyers.** The four tests weight *cost* and
*disruption* differently. A recommendation engine that proposes a placement is implicitly
applying one of them. **There is no circuit-neutral placement recommendation.** Any system
that offers placement guidance is either encoding a jurisdiction it was never told, or
averaging four incompatible legal standards into one number. Both are wrong. This is the
strongest single argument in this report for the flat prohibition in §11: **an AI may not
recommend placement.**

### 10.3 Predetermination — the doctrine that governs pre-meeting AI output

`CASE-LAW` — ***Deal v. Hamilton County Board of Education*, 392 F.3d 840 (6th Cir. 2004)**,
verbatim:

> "The evidence reveals that the School System, and its representatives, **had pre-decided not
> to offer Zachary intensive ABA services regardless of any evidence concerning Zachary's
> individual needs** and the effectiveness of his private program. **This predetermination
> amounted to a procedural violation of the IDEA. Because it effectively deprived Zachary's
> parents of meaningful participation in the IEP process, the predetermination caused
> substantive harm and therefore deprived Zachary of a FAPE.**"

And the line that draws the boundary exactly where an AI sits, quoting *Ms. C. ex rel. N.L. v.
Knox County Schools*, 315 F.3d 688, 693–95 (6th Cir. 2003):

> "**school officials are permitted to form opinions and compile reports prior to IEP
> meetings.** The Court cautioned, however, that **such conduct is only harmless as long as
> school officials are 'willing to listen to the parents'** … school system representatives
> should '**come to the meeting with suggestions and open minds, not a required course of
> action**'."

`CASE-LAW` — ***Spielberg v. Henrico County Public Schools*, 853 F.2d 256, 258–59 (4th Cir.
1988)**, verbatim:

> "The decision to place Jonathan at Randolph **before developing an IEP on which to base that
> placement** violates this regulation as interpreted by the Secretary of Education. It also
> **violates the spirit and intent of the EHA, which emphasizes parental involvement. After
> the fact involvement is not enough.**"

`INFERENCE` — a necessary caveat: *Spielberg*'s "sufficient in itself" framing predates IDEA
2004's codified harmless-error filter at 20 U.S.C. §1415(f)(3)(E)(ii) / 34 CFR §300.513(a)(2).
*Deal* already runs the substantive-harm analysis. Do not quote *Spielberg* as if per-se
invalidity survives unqualified.

Also collected in *Deal*, the no-predetermination side: *Fuhrmann v. East Hanover Board of
Education*, 993 F.2d 1031, 1036 (3d Cir. 1993); *Hanson v. Smith*, 212 F. Supp. 2d 474, 486
(D. Md. 2002) (district came to meetings *"with an open mind"*); *Doyle v. Arlington County
School Board*, 806 F. Supp. 1253, 1262 (E.D. Va. 1992) (district *"merely proposed"* a
placement and had not *"fully made up its mind before the parents ever [got] involved"*); and
*W.G. v. Board of Trustees of Target Range School District No. 23*, 960 F.2d 1479, 1484–85
(9th Cir. 1992) (the district *"was required to conduct, **not just an IEP meeting, but a
meaningful IEP meeting**"*).

**The operative rule: pre-meeting analysis is lawful; a pre-committed outcome is not.** An AI
draft is lawful. An AI draft that the team cannot realistically move is the *Deal* fact
pattern with better typography.

### 10.4 PWN failure, and the harmless-error escape hatch

`CASE-LAW` — ***J.B. v. Kyrene Elementary School District No. 28*, 112 F.4th 1156 (9th Cir.
2024)**. The district issued prior written notices refusing to continue the IEP process and
refusing an independent educational evaluation **solely because the student was not enrolled**
— a rationale the whole panel agreed was not legitimate. The majority nonetheless affirmed for
the district on harmless-error grounds, **accepting substitute reasons developed later in the
administrative proceedings and never contemporaneously given to the parent.**

Collins, J., dissenting, states the governing standard verbatim:

> "Under the IDEA, procedural violations—such as **the failure to provide a valid explanation
> for proposed agency action in a PWN**, see 20 U.S.C. § 1415(c)(1)(B)—'constitute a denial of
> a [FAPE],' and therefore warrant a remedy, only if they (1) 'seriously impair the parents'
> opportunity to participate in the IEP formulation process'; (2) 'result in the loss of
> educational opportunity for the child'; or (3) 'cause a deprivation of the child's
> educational benefits.' *Timothy O. v. Paso Robles Unified Sch. Dist.*, 822 F.3d 1105, 1124
> (9th Cir. 2016)… In my view, the District's procedural error was plainly harmful under the
> first of these three alternatives."

**This is the most recent and most directly analogous authority in the report.** A district
that acts on an opaque recommendation, writes a thin PWN, and reconstructs its reasoning at
hearing may well win. That is not a reason for a builder to relax; it is a description of how
the accountability loop fails. **The system that gets built should produce the
contemporaneous reasoning, because the legal system will not reliably force it to.**

### 10.5 Exhaustion — when a family can bypass IDEA entirely

`CASE-LAW` — ***Fry v. Napoleon Community Schools*, 580 U.S. 154 (2017)**, verbatim:

> "**Held: 1. Exhaustion of the IDEA's administrative procedures is unnecessary where the
> gravamen of the plaintiff's suit is something other than the denial of the IDEA's core
> guarantee of a FAPE.** […] In determining whether a plaintiff seeks relief for the denial of
> a FAPE, **what matters is the gravamen of the plaintiff's complaint, setting aside any
> attempts at artful pleading.** … **examination of a plaintiff's complaint should consider
> substance, not surface**."

`CASE-LAW` — ***Perez v. Sturgis Public Schools*, 598 U.S. 142 (2023)**, verbatim:

> "**Held: IDEA's exhaustion requirement does not preclude Mr. Perez's ADA lawsuit because the
> relief he seeks (i.e., compensatory damages) is not something IDEA can provide.**"

> "The statute's administrative exhaustion requirement applies only to suits that 'see[k]
> relief . . . also available under' IDEA. And that condition simply is not met in situations
> like ours, where a plaintiff brings a suit under another federal law for compensatory
> damages—a form of relief everyone agrees IDEA does not provide."

*Fry* supplies a **gravamen** test; *Perez* adds an independent **remedy-availability** test.
They are cumulative. `INFERENCE` — practical consequence: a family alleging disability
discrimination and seeking damages may go straight to federal court under ADA/§504 without
ever filing a due process complaint. The §618 due-process counts in §12 therefore
**understate** total dispute volume by an unmeasured amount, and a product's exposure is not
bounded by IDEA's administrative process.

---

## 11. THE TABLE — artefact by artefact: who owns it, what an AI may draft, what it may never author, what would be a violation

The requested deliverable. `STATUTE` on every citation; the AI columns are `INFERENCE` from
those citations and are stated as design rules, not legal advice.

| Artefact / process | Who owns it legally | What an AI **may** draft | What an AI may **never** author | What would constitute a procedural violation |
|---|---|---|---|---|
| **PLAAFP** | IEP Team, in a meeting — §300.320(a), §300.321(a) | Prose synthesis of held data; a gap list of areas with no data; a first pass at the effect-of-disability statement, marked as a proposal | The final effect-of-disability determination; any statement not traceable to a source datum; a diagnostic characterisation of the child | An IEP adopted with a PLAAFP omitting functional performance, or lacking baselines sufficient to anchor its goals — facially deficient under §300.320(a)(1) |
| **Measurable annual goals** | IEP Team — §300.320(a)(2) | Candidate goal language; a measurability check (condition / behaviour / criterion / timeframe); alignment check to identified needs | The target, the criterion level, or the judgement that the goal is ambitious enough — *Endrew F.*, 580 U.S. 386 | Goals not measurable, or an IEP with no goal for an identified area of need. Goals set by trend extrapolation risk *Endrew F.* insufficiency |
| **Progress measurement method & reporting schedule** | IEP Team — §300.320(a)(3) | The graph, the trend line, the report text, the schedule reminder | The decision to change the programme when progress lags — §300.324(b)(1)(ii)(A) | Failure to issue promised periodic reports; reporting effort rather than performance against the stated criterion |
| **Services grid (type, frequency, location, duration)** | IEP Team — §300.320(a)(4), (a)(7) | Options with their research base; a staffing-feasibility annotation; a consistency check of services against goals | Any change to type, frequency, location or duration. **This is placement** — 71 FR 46588 | Changing service minutes without PWN (§300.503(a)(1)) and without either a team meeting or a written amendment (§300.324(a)(4)) |
| **Accommodations** | IEP Team — §300.320(a)(6); implementation duty §300.323(d)(2)(ii) | Candidate accommodations; a check that each maps to a documented access barrier; delivery logging | Applying an accommodation not in the IEP as if it were, or removing one that is | Non-implementation of a documented accommodation — a FAPE issue and a §300.530(e)(1)(ii) manifestation trigger |
| **Modifications** | IEP Team | A flag that a proposed adaptation *is* a modification, routed to the team | **Applying any modification.** Shortening a task, lowering text complexity, reducing item count, accepting partial as complete — all are modifications | Silent modification: a curricular decision reserved to the team, taken invisibly. Also implicates §300.116(e) |
| **Placement / LRE** | A group including the parents — §300.116(a)(1); LRE §300.114(a)(2) | A record of supplementary aids and services already tried and their measured effect — the evidentiary predicate for *Daniel R.R.* prong one | **Any placement recommendation.** Four circuits apply four different tests; there is no circuit-neutral recommendation | Placement decided before the IEP is written (*Spielberg*, 853 F.2d 256); placement decided without the parent (§300.116(a)(1)); removal without a supplementary-aids analysis |
| **Prior Written Notice** | **The public agency** — §300.503(a). Not the team | The full §300.503(b)(1)–(7) skeleton, including (b)(6) options-considered-and-rejected; native-language rendering under §300.503(c) | The decision the notice describes; the agency's reasons | Acting on a change to identification, evaluation, placement or FAPE provision without PWN. Under §300.513(a)(2)(ii) this is the gate most likely to convert to a FAPE denial |
| **Parental consent** | The parent — §300.9; §300.300 | Plain-language explanation of what is being consented to; tracking of the §300.300(d)(5)/§300.322(d) reasonable-efforts record | Consent itself; any inference of consent from non-response beyond §300.300(c)(2)'s narrow reevaluation exception | Evaluating without consent (§300.300(a)(1)); continuing services after written revocation (§300.300(b)(4)(i)); fabricating a reasonable-efforts record |
| **Evaluation** | A group of qualified professionals + the parent — §300.306(a)(1) | Scheduling; consolidating existing data for the §300.305(a) review; drafting report sections from held results | The eligibility determination; any single score offered as decisive — §300.304(b)(2) forbids a single measure as sole criterion | Altering standardised administration conditions (§300.304(c)(1)(v)); missing the 60-day clock (§300.301(c)(1)); using an instrument outside its validity argument (§300.304(c)(1)(iii)) |
| **Eligibility determination** | Named group members, **certifying individually in writing** — §300.311(b) | A summary of the evidence for each §300.309(a) element; the §300.309(b) instructional-adequacy documentation | The determination. **An AI cannot certify, and §300.311(b) requires individual certification with a written-dissent right** | A determination made without the required members (§300.308); determining SLD without the §300.309(b) data on prior appropriate instruction |
| **Reevaluation** | Public agency + parent consent — §300.303, §300.300(c) | The triennial clock; the §300.305(a) existing-data review packet; the §300.305(d)(1) no-additional-data notice | The decision that no further data are needed | Exceeding three years without reevaluation or a documented parental agreement that it is unnecessary — §300.303(b)(2) |
| **IEE at public expense** | The parent's right — §300.502(b)(1) | Nothing beyond providing the §300.502(a)(2) information about where an IEE may be obtained and agency criteria | Any gatekeeping. §300.502(b)(4): the agency *"may not require the parent to provide an explanation"* | Delay. §300.502(b)(2) leaves exactly two options — file for a hearing, or fund the IEE — *"without unnecessary delay"* |
| **Instructional method inside an existing service** | The IEP Team **if** the IEP names a method; otherwise the provider — 71 FR 46665 | Hints, worked steps, re-representation, sequencing, item selection — §300.501(b)(3) puts teaching methodology outside the meeting requirement | A change to a method the IEP names, without amendment | Departing from an IEP-specified methodology without amending the IEP |
| **Manifestation determination** | LEA + parent + relevant team members, within 10 school days — §300.530(e)(1) | The service-delivery record answering §300.530(e)(1)(ii) — was the IEP actually implemented? | The determination | Removal beyond 10 consecutive days, or a §300.536(a)(2) pattern, without a manifestation determination |
| **Safeguarding disclosure** | The individual mandated reporter; non-delegable in ≥17 states + DC + VI | Preserving the child's exact words; surfacing to the correct human immediately; making the state's routing rule visible | **The report itself, and any triage, threshold, or delay.** An AI cannot hold a personal statutory duty | Routing to a supervisor in a state requiring direct report first; interposing a confidence threshold; **notifying the parent** |
| **Records and confidentiality** | Public agency — §§300.610–300.627; FERPA | Access logs; retention-clock tracking; the §300.624(a) "no longer needed" notice | Disclosure decisions — §300.622(a) requires parental consent for disclosure outside participating agencies | Disclosing PII without consent where §300.622 requires it; failing to destroy on request under §300.624(b), subject to its permanent-record carve-out |

### 11.1 The four flat prohibitions, restated without hedging

1. **An AI may not recommend a placement.** Not because it would be inaccurate — because four
   circuits apply four incompatible legal tests and there is no jurisdiction-neutral answer.
2. **An AI may not apply a modification.** Accommodations adjust access; modifications adjust the
   expectation, and the expectation belongs to the team. A system that cannot tell which of the
   two it is doing must do neither.
3. **An AI may not make, triage, delay, or threshold a safeguarding report,** and must never
   route a safeguarding concern to the parent by default.
4. **An AI may not certify an eligibility conclusion.** §300.311(b) requires named individuals to
   certify in writing, with a dissent right. That is the statute refusing to average judgements.

Everything else on the table is negotiable engineering. These four are not.

---

## 12. What `survey/04` must say to stop being costume

Blunt list. Each item names the defect, the fix, and the citation the fix rests on.

**1. It has no documents in it.** The section is about a child in the American special-education
system and never once mentions the artefact that system runs on. Add the IEP's nine statutory
components (34 CFR §300.320(a)), name the PLAAFP explicitly, and say who authors each part
(§300.321(a)). A coordinator reads §5's "an AI may not author an IEP" and asks *which part were
you going to author?* — and the section has no answer because it has never looked inside the
document.

**2. It asserts the IEP prohibition without the mechanism.** "It is a legally binding document
authored by a team including the parent" is true and unfalsifiable-sounding. The mechanism is
better: §300.320(a) says the IEP is *"developed, reviewed, and revised **in a meeting**"*;
§300.321(a) names the seven required participants; §300.311(b) requires each SLD group member
to *"certify in writing"* their own conclusion with a right of written dissent. **Authority in
this statute is located in named humans in a room, individually attributable, with dissent
preserved.** That is a much stronger sentence than "it is legally binding," and it explains
*why* averaging judgements — which is what a model does — is the wrong shape.

**3. Half the legal test is procedural and the section does not know it.** *Rowley*, 458 U.S. at
206–07: *"First, has the State complied with the procedures set forth in the Act? And second, is
the individualized educational program developed through the Act's procedures reasonably
calculated to enable the child to receive educational benefits?"* `survey/04` is entirely about
the second question. A practitioner's week is dominated by the first. Until the section says
that procedure *is* half the entitlement — not friction around the entitlement — it will keep
reading as a research summary wearing a school lanyard.

**4. Add prior written notice, and get the framing right.** §300.503 in full: it fires on
proposals *and refusals*, across identification, evaluation, educational placement, and provision
of FAPE, and §300.503(b)(6) requires *"a description of other options that the IEP Team
considered and the reasons why those options were rejected."* Then state the corrected rule from
§5.5: **an AI does not commit procedural violations; agencies do — but an AI that changes a
child's services without forcing the agency through PWN manufactures one for its operator, and it
lands on §300.513(a)(2)(ii), the parent-participation gate.** And carry the limiting principle:
changing *method* inside an unchanged service is not a PWN event, because §300.501(b)(3) puts
*"teaching methodology, lesson plans, or coordination of service provision"* outside the meeting
requirement entirely.

**5. Add LRE, and admit it conflicts with the section's own thesis.** §300.114(a)(2)(ii) permits
removal *"only if the nature or severity of the disability is such that education in regular
classes with the use of supplementary aids and services cannot be achieved satisfactorily."* The
intervention base `survey/04` celebrates is overwhelmingly evidence about intensive pull-out.
The section currently presents dosage and fidelity as an unalloyed good; LRE says removal has to
be justified every time. **Then make the forward-looking claim, which is the best idea in this
whole report:** the reason intensity requires removal is a staffing constraint, not a pedagogical
one, and a system that delivers fidelity and dosage *without physical removal* attacks the exact
mechanism that forces the trade-off. Label it `INFERENCE`. No trial has tested it.

**6. Correct the placement vocabulary before it is used.** ED, 71 FR 46588: *"placement refers to
the provision of special education and related services rather than a specific place, such as a
specific classroom or specific school."* Any sentence in the survey about "grouping,"
"routing," or "moving a learner" is about placement in the legal sense whether or not anyone
moves rooms. And §300.518(a) freezes it during a dispute — **stay-put means a per-child state
that no adaptive loop may override.**

**7. Add the accommodation/modification distinction, which the section currently collapses into
"personalisation."** Accommodations change access; modifications change the expectation.
§300.116(e) forbids removal *"solely because of needed modifications"*; §300.320(a)(6) treats
assessment accommodations and alternate assessments as different legal objects. **The specific,
sharp prohibition to add: an AI that silently shortens a task, lowers text complexity, reduces
item count, or accepts a partial answer as complete has applied a modification, which is a
curricular decision reserved to the team — and has applied it invisibly.** Adaptive difficulty,
as universally shipped, cannot say whether its own adjustments are accommodations or
modifications. That is a much sharper claim than "restraint matters," and it indicts a feature
every product in the category ships.

**8. Fix the eligibility framing — there are 13 categories and a second prong.** §300.8(a)(1)
lists thirteen conditions; §300.8(a)(2)(i) says a child who has one but *"only needs a related
service and not special education"* is **not** a child with a disability under Part B. And
§300.306(b)(1)(i) bars eligibility where the determinant factor is *"lack of appropriate
instruction in reading, including the essential components of reading instruction."* Set that
against the section's own argument that explicit systematic decoding is the evidenced ingredient
and is frequently not delivered: **the statute makes "we never taught them properly" a bar to
services.** That is either a safeguard or a trapdoor depending entirely on the quality of core
instruction, and the section should say so.

**9. Add Section 504, and stop implying every child in scope has an IEP.** 34 CFR Part 104: a
broader eligibility gate, no specially designed instruction requirement, no federal funding, and
a thinner procedural regime (§104.36 requires notice, records access, an impartial hearing and a
review procedure — and expressly permits IDEA compliance as *one means* of satisfying it).
Many, possibly most, learners a product serves have a 504 plan and no IEP, and they are not in
the IDEA child count. A product sized off the Part B number is undercounting its own users.

**10. Get the peer-reviewed-research clause into the argument, because it is the survey's own
thesis in statutory form.** §300.320(a)(4) requires services *"based on peer-reviewed research to
the extent practicable,"* and ED reads it as: *"States, school districts, and school personnel
must, therefore, select and use methods that research has shown to be effective, to the extent
that methods based on peer-reviewed research are available"* (71 FR 46665). H1 argued
"fidelity and dosage of known-good intervention" from effect sizes. **§300.320(a)(4) argues it
from law.** And the corollary the section must not dodge: with zero RCTs of generative AI in this
population, an AI tutor cannot be justified as an IEP *service* on the strength of evidence. It
can be the delivery mechanism for a method that has one.

**11. Add *Endrew F.*, because it is a judicial explainability requirement.** 580 U.S. 386: the
IEP must be *"reasonably calculated to enable a child to make progress appropriate in light of
the child's circumstances,"* a standard *"markedly more demanding than the 'merely more than de
minimis' test."* And: *"A reviewing court may fairly expect those authorities to be able to offer
a **cogent and responsive explanation for their decisions**."* **A district cannot meet that
expectation with a recommendation it cannot explain.** This is the strongest argument available
that interpretability here is a legal requirement, not a preference — and it is more persuasive
than any appeal to good practice.

**12. Add predetermination, and name it as the sharpest AI-specific risk in the domain.** *Deal
v. Hamilton County*, 392 F.3d 840: predetermination *"effectively deprived Zachary's parents of
meaningful participation in the IEP process,"* and therefore denied FAPE. The boundary, from
*Knox County*: officials may *"form opinions and compile reports prior to IEP meetings"* but must
*"come to the meeting with suggestions and open minds, not a required course of action."* And ED's
own words, 71 FR 46691: issuing a proposal before the meeting *"could suggest… that the public
agency's proposal was improperly arrived at before the meeting and without parent input."* **Every
recommendation engine is a predetermination machine by default.** The design answers — drafts
that look like drafts, mandatory alternatives, provenance on every clause, visible
responsiveness to parent input in the room — are concrete and buildable and belong in the
section.

**13. Add the workload reality, and let it change the conclusion.** The section's implicit model
is that the AI's job is instruction. §7 says the binding constraint on this system is adult
hours, and that most of those hours are not instructional — **20% of class time on academic
instruction and 17% on paperwork in the only direct-observation study located** (Vannest &
Hagan-Burke 2011, 31 teachers, >7,000 data points), converging with SPeNSE's self-report and
ASHA's 2024 SLP survey on 13–17% of professional time going to documentation. **If AI's largest
contribution here is administrative rather than instructional, the section should say so plainly
— it is the most practically consequential finding in the H-wave and it is currently absent.** It
strengthens rather than weakens the instructional argument: hours returned to a caseload are
hours available for the explicit instruction the evidence base actually supports.

**But carry the track record in the same breath, or the claim is just marketing.** Computerisation:
measured, zero. Human delegation: measured, zero, *"because much of the paperwork teachers
complete cannot be appropriately delegated to an aide or secretary."* Deregulation: priced by ED
at approximately zero. Statutory waiver authority: twenty-one years, no waiver, no required
report. **The AI claim is the fifth attempt and rests on one randomised trial of 22 novice
teachers on one sub-task.** The honest framing is a specific question, not a promise: *the barrier
to delegation was judgement rather than throughput — is a language model a different kind of
delegate from an aide?*

**14. Say out loud that accommodations — the most deployed intervention in the field — do not have
the evidence base the section's framework assumes.** Two meta-analyses return overall nulls
(Kieffer et al., g = .034, p = .180; Rios et al., *"none… statistically different from zero"*
across 95 effect sizes and N = 11,069). Elbaum (2007) found the differential boost **reversed** at
secondary level. Teachers assign accommodations **at chance** (Helwig & Tindal, N = 1,218). Benefit
is **item-conditional, not student-conditional** (Ketterlin-Geller 2007), which means no amount of
better learner modelling can fix the assignment problem. And the What Works Clearinghouse has
certified nothing about accommodations in thirty Practice Guides. **`survey/04` argues AI's job is
fidelity to known-good intervention. Accommodations are legally mandated and not known-good. The
section must hold both facts at once, because a system that faithfully delivers a child's
accommodations is doing something required by law and unsupported by evidence.**

**15. Add escalation, and build the one-way door.** Mandated reporting is personal,
non-delegable in at least 17 states plus DC and the Virgin Islands, triggers on *suspicion*, and
routes **around** the parent. Texas Family Code §261.101(b): *"A professional may not delegate to
or rely on another person to make the report."* California Penal Code §11166(i)(3): reporting to
*"an employer, supervisor, school principal, school counselor, coworker, or other person **shall
not be a substitute for making a mandated report**."* Every other flow in the survey routes
*through* the parent. **A product with a single "notify the guardian" pathway has built a
mechanism for endangering children.** State it as a flat prohibition, not a consideration.

**16. And state the finding that should stop the section from building a detector at all.** The
binding constraint in school safeguarding is **disclosure, not detection.** NIS-4: school
sentinels recognised 52% of Harm Standard maltreatment, at least 80% of it never reached an
investigation, and CPS *"probably would have investigated nearly three-fourths (72%)"* of what it
never saw. Wyman's group-randomised trial: gatekeeper training moved staff confidence by **ES
1.22** and moved identification behaviour by **nothing** — because *"fewer students with prior
suicide attempts endorsed talking to adults about distress."* Meanwhile GoGuardian's own figure is
**4.6 alerts per student per year**, and a six-day census of ~4,400 children produced **9,387 flags
with zero genuine suicide references** — including 44 visits to the US Holocaust Memorial Museum's
website — routed, in at least one large district, to **school police**. **An AI that improves
detection is intervening on the non-binding constraint, and the cost of doing so lands on the
children least able to absorb it.** There is one live counter-hypothesis — that children will
disclose to a machine what they will not disclose to an adult — and the section should name it as
an untested hypothesis worth testing, not as a reason to ship.

**17. Fix three factual details.**
- *"Roughly one child in seven"* → NCES reports **15 percent** of all public school students,
  7.5 million ages 3–21, for 2022–23; OSEP's §618 count for **2023–24 is 7,892,433**. "About one
  in six and rising" is the accurate phrasing.
- The §300.624 quotation is correct but **incomplete in a way that overstates the right**. The
  destruction duty is conditioned by §300.624(a) — the agency must inform parents *"when
  personally identifiable information […] is no longer needed to provide educational services"* —
  and §300.624(b) carves out a permanent record of *"name, address, and phone number, his or her
  grades, attendance record, classes attended, grade level completed, and year completed"* which
  *"may be maintained without time limitation."* The deletability argument survives; the
  quotation should not be presented as an unconditional right.
- **WCAG 2.2 AA is above the legal floor, not equal to it.** 28 CFR §35.200(b) incorporates
  **WCAG 2.1** Level A and AA, and the compliance dates were extended in April 2026 to **April 26,
  2027** (population ≥50,000) and **April 26, 2028** (under 50,000 or special district) by 91 FR
  20902. Describing 2.2 AA as compliance is wrong; describing it as a deliberate choice above the
  floor is both accurate and a better argument.

**18. And keep the empty chair.** The central image survives all of this intact. The correction
is not that the chair is full. It is that the room the chair sits in has a statute, a calendar,
a caseload and a paper trail, and the section currently describes none of them.

---

## 13. Null and negative results ledger

The brief asked for at least three documented negative/null results or systemic failures. There
are twenty-nine.

### 13.1 Administrative burden — the interventions that were measured and failed

| # | Result | Type | Source |
|---|---|---|---|
| 1 | **Computerisation of IEP work produced no measured reduction in time.** *"Access to reliable computers was not related to the time teachers spent on administrative duties and paperwork […] Using a computer to prepare IEPs was not significantly related to time spent writing each IEP or completing administrative duties and paperwork, in general."* 70% used computers; they rated access good or excellent. | `MEASURED` null | SPeNSE Paperwork Substudy, ED479674, n=972 |
| 2 | **Human delegation produced no measured reduction either, and the report explains why.** *"The amount of help teachers had was not significantly related to the time they spent […] This may be the case because much of the paperwork teachers complete cannot be appropriately delegated to an aide or secretary."* 50% had no help at all. | `MEASURED` null | ibid. |
| 3 | **The IEP-team-member excusal provision (§300.321(e)) was priced by ED at approximately zero savings.** *"reduced time spent in meetings is likely to be offset by the time required to draft written input, send it to the parents and other IEP Team members, and secure the consent."* | `OBSERVED` (regulatory impact analysis) | 71 FR 46843 |
| 4 | **A legal maximum caseload implies roughly four times the administrative time teachers report having.** 28 case-managed pupils (Cal. Ed. Code §56362(c)) × 0.6 hours/week/case (SPeNSE) = 16.8 h/week against 4 h available. The measured 5–6 h/week is therefore a measure of triage, not of requirement. | `INFERENCE` on measured inputs | §7.2 |
| 5 | **California, the most regulated system in the country, has no adult-to-pupil ratio for special classes** and in 2025 instructed its Superintendent to *recommend* one by 1 July 2027 (Ed. Code §56364.3, added by AB 560). | `STATUTE` | Cal. Ed. Code §56364.3 |
| 6 | **The due process system disposes of most of its docket without deciding anything.** 52.8% withdrawn or dismissed; 25.2% pending; 22.0% adjudicated — while the state-complaint channel finds against districts in 62.7% of decided cases. | `MEASURED-META` | OSEP IDEA Part B Dispute Resolution Survey 2023–24 |
| 7 | **Most states are not meeting IDEA requirements on the Department's own assessment.** Part B: 6 entities "needs intervention," 34 at "needs assistance, two or more consecutive years," only 22 meeting requirements. | `OBSERVED` | ED, 2026 Determination Letters, 18 June 2026 |
| 8 | **Federal civil-rights enforcement capacity has fallen while demand has risen.** 22,687 complaints against 588 FTE in FY2024, versus under 3,000 against ~1,100 FTE in FY1981. | `OBSERVED` + `MEASURED-META` | ED OCR Report to the President, FY2024 |
| 9 | **Child-find litigation is rising and districts win it 2:1.** | `MEASURED-META` | Zirkel, *Exceptionality* (2015), 42 decisions; corroborated 2011, 2018 |
| 10 | **A PWN with an admittedly invalid rationale can be cured post hoc.** *J.B. v. Kyrene*, 112 F.4th 1156 (9th Cir. 2024): the panel agreed the stated reason was illegitimate and affirmed for the district on harmless-error grounds, accepting reasons never contemporaneously given to the parent. | `CASE-LAW` | §10.4 |
| 11 | **Federal data on the actual volume of IEP work does not exist.** ED, 2006: *"we lack detailed data on the number of IEP Team meetings conducted each year,"* working from an assumed 1.2 meetings/child/year at 1.5 hours. No newer national time-use study was located; the best available remains 2002. | `OBSERVED` (documented data gap) | 71 FR 46845 |

| 12 | **★ IDEA §609 (20 U.S.C. §1408) paperwork-waiver authority: 21 years, 15 state slots available, one one-time competition run in 2007–08, zero documented waivers, and the effectiveness report the statute *requires* has never been filed.** ED re-proposed the same requirements in 2020, reported no results from 2007–08, and never finalised the rule. | `OBSERVED` (documented regulatory failure) | 20 U.S.C. §1408; 72 FR 58066; 2020-11416 |
| 13 | **No national special-education-specific teacher attrition rate exists.** NTPS/TFS reports attrition by experience and sector, not by teaching field; IDEA §618 Personnel has no vacancy or attrition variable. The 2021–22 TFS "most important reason for leaving" instrument **contains no paperwork or caseload option** — the most-cited driver of the shortage is the one the federal instrument has no checkbox for. | `OBSERVED` (data gap) | §7.6 |
| 14 | **The research infrastructure that produced these numbers has been dismantled.** COPSSE's site now redirects to a different centre; ERIC indexes two documents mentioning it, neither authored by it. Project Forum's 2011 *Paperwork in Special Education* (ED526876) has no ERIC full text (404) and nasdse.org returns 404. | `OBSERVED` | §14.4 |

**The meta-finding for this group.** Items 1, 2, 3 and 12 are four independent, federally-run or
federally-measured attempts to reduce administrative burden in special education — through
technology, through people, through deregulation, and through statutory waiver — and **all four
measured at or near zero, with the fourth never even reporting.** Any claim that AI will reduce
this burden is the fifth attempt, and the only measured evidence for it is **one randomised trial
of 22 novice teachers on one sub-task** (§7.5c). It should be stated as a hypothesis with a
track record behind it, never as an expectation.

### 13.2 Accommodations — the practice with the weakest evidence and the widest deployment

| # | Result | Type | Source |
|---|---|---|---|
| 15 | **The interaction hypothesis failed.** Extended time *"tended to improve the performance of all students"*; the field retreated to the weaker "differential boost" claim. | `MEASURED-META` | Sireci, Scarpati & Li (2005), *RER* 75(4) |
| 16 | **Differential boost appears in roughly a third to a half of tests of it.** 8/19 extended time (42%), 11/19 oral delivery (58%); Lane & Leventhal 4/11 (36%), falling to 30% at secondary and 30% in mathematics. | `MEASURED` | Kettler (2015); Lane & Leventhal (2015) |
| 17 | **★ Kieffer et al.: overall accommodation effect g = .034, CI [−.016, .084], p = .180 — null.** Six of seven accommodation types non-significant; the Spanish-version accommodation **negative** (g = −.263, p = .010). Authors: *"a somewhat disheartening story."* | `MEASURED-META` | *RER* 79(3), 37 randomized samples |
| 18 | **★ Rios et al.: *"none of the accommodations investigated were found to have intervention effects that were statistically different from zero."*** | `MEASURED-META` | *EMIP* (2020), 95 ES, N = 11,069 |
| 19 | **★ Elbaum (2007): the differential boost *reversed*** — students **without** disabilities benefited more (ES 0.44) than students with LD (ES 0.20) on a secondary mathematics oral accommodation. | `MEASURED` | *J. Special Education* 40(4), N = 625 |
| 20 | **Four further primary nulls on read-aloud and extended time:** Meloy et al. (2002) interaction n.s.; Elbaum et al. (2004) no differential benefit; McKevitt & Elliott (2003) no differential benefit; Fuchs et al. (2000) null for extended time and large print. | `MEASURED` | §2.6b |
| 21 | **★ Teachers assign accommodations at chance.** *"Teachers were no more successful than chance at predicting which students would benefit… A developed student profile did not match accommodation outcomes."* | `MEASURED` | Helwig & Tindal (2003), N = 1,218 |
| 22 | **The What Works Clearinghouse has certified nothing about accommodations.** All 30 Practice Guides (2007–2024) enumerated; none addresses accommodations; the product taxonomy has no accommodations topic, despite 509 studies tagged to the disability population facet. | `OBSERVED` (documented absence) | ies.ed.gov/ncee/wwc |

### 13.3 Safeguarding — where the constraint actually is

| # | Result | Type | Source |
|---|---|---|---|
| 23 | **★ NIS-4: at least 80% of maltreatment recognised by school staff never reached a CPS investigation** — and CPS *"probably would have investigated nearly three-fourths (72%)"* of what it never saw. The bottleneck is recognition→report, not screening. | `MEASURED` | Sedlak et al. (2010), 10,791 sentinels |
| 24 | **School staff are the worst non-reporters of the four sentinel groups:** 29% would not report countable cases versus 23% overall; **33% would not report neglect vignettes**; 35% would not report educational neglect. | `MEASURED` | NIS-4 §8.5.3 |
| 25 | **★ Wyman et al. (2008) RCT: gatekeeper training raised knowledge (ES 0.41), efficacy appraisals (ES 1.22) and service access (ES 1.07) — and did NOT increase suicide identification behaviour.** The binding constraint is student disclosure, not staff detection. | `MEASURED-RCT` | *JCCP* 76(1), 32 schools |
| 26 | **Gatekeeper meta-analysis: intention effects are ~4.7× larger than behaviour effects** (1.03 versus 0.22 long-term), on evidence the authors describe as low quality. Neither of two meta-analyses reports attempts or deaths. | `MEASURED-META` | *Prevention Science* 25 (2024), 43 studies |
| 27 | **★ Cochrane: in 11 trials of child-protection training, ZERO measured reports against official CPS records and ZERO measured adverse effects.** | `MEASURED-META` | Walsh et al. (2022), CD011775.pub2 |
| 28 | **Self-report on reporting is systematically optimistic.** 73% of teachers had never made a report; only 11% admitted failing to report; *"the teachers' responses to the case vignettes were not consistent with their previous reports."* | `MEASURED` | Kenny (2001), n = 197 |
| 29 | **★ Automated flagging: a six-day census of ~4,400 students produced 9,387 flags containing no genuine suicide references** — including 44 visits to the US Holocaust Memorial Museum, 68 to the district's own learning platform, and 900+ flags for the term "colon" in a neighbouring district. LGBTQ content flagged and escalated; 85% of flagged Spotify songs by Black artists. | `OBSERVED` (primary records) | EFF, *Red Flag Machine* |

---

## 14. Sources, retrieval notes, and unreachable material

### 14.1 Regulatory text

All 34 CFR Part 300, 34 CFR Part 104 and 28 CFR Part 35 text in this report was retrieved
verbatim from the **eCFR versioner API**, point-in-time snapshot **2026-07-01**, on 2026-07-28:
`https://www.ecfr.gov/api/versioner/v1/full/2026-07-01/title-{34|28}.xml?part={300|104|35}&section={n}`
— all requests HTTP 200. Sections retrieved: 300.8, 300.9, 300.34, 300.39, 300.101, 300.111,
300.114, 300.115, 300.116, 300.300, 300.301, 300.303, 300.304, 300.305, 300.306, 300.307,
300.308, 300.309, 300.311, 300.320, 300.321, 300.322, 300.323, 300.324, 300.501, 300.502,
300.503, 300.504, 300.506, 300.507, 300.510, 300.511, 300.513, 300.517, 300.518, 300.530,
300.536, 300.610, 300.622, 300.624; 104.3, 104.33, 104.34, 104.35, 104.36; 28 CFR 35.200,
35.201, 35.202.

Preamble material ("Analysis of Comments and Changes") is from the IDEA Part B final rule,
**71 FR 46540 (14 August 2006)**, full text retrieved from federalregister.gov (HTTP 200).
Page citations are to the printed Federal Register pagination as it appears in that text.

The ADA Title II compliance-date extension is **91 FR 20902 (20 April 2026)**, DOJ interim final
rule; the parallel HHS Section 504 extension is **91 FR 25496 (11 May 2026)**. Both confirmed via
the federalregister.gov API.

California statutes retrieved verbatim from leginfo.legislature.ca.gov (HTTP 200): Ed. Code
§§56195, 56195.1, 56205, 56362 (as amended by AB 560, Stats. 2025 Ch. 560, effective 1 January
2026), and AB 560's text adding §56364.3.

### 14.2 Data

- IDEA §618 Part B Child Count and Educational Environments, SY 2023–24, Tables 1 and 3 —
  data.ed.gov CKAN API, XLSX parsed directly (HTTP 200).
- IDEA Part B Dispute Resolution Survey, 2023–24 — same source, `bdispres2023-24.xlsx`.
- ED, *2026 Determination Letters on State Implementation of IDEA*, 18 June 2026 —
  sites.ed.gov/idea (HTTP 200).
- ED OCR, *Report to the President and Secretary of Education*, FY2024 — ed.gov (HTTP 200).
- NCES, *Condition of Education*, "Students With Disabilities" (updated May 2024) — nces.ed.gov
  (HTTP 200).
- SPeNSE Paperwork Substudy — files.eric.ed.gov/fulltext/ED479674.pdf (HTTP 200), read in full.
- Child Welfare Information Gateway, *Mandatory Reporting of Child Abuse and Neglect*, State
  Statutes series, current through May 2023 — retrieved from the CWIG S3 bucket (HTTP 200) after
  childwelfare.gov returned HTTP 404.
- HHS/ACF, NCANDS *Child Maltreatment* reports FFY2018–FFY2024 — acf.hhs.gov (HTTP 200 with a
  full browser user-agent; **acf.gov returns HTTP 202 bot-challenge and zero bytes**).
- Sedlak et al., *Fourth National Incidence Study of Child Abuse and Neglect (NIS-4): Report to
  Congress* (2010) — HHS/ACF/OPRE (HTTP 200), read in full.
- EFF, *GoGuardian: A Red Flag Machine By Design* — redflagmachine.com/research (HTTP 200);
  underlying district records obtained by EFF under public-records law.
- ASHA 2024 Schools Survey; NASP Research Reports series (Affrunti) on
  students-per-school-psychologist ratios 2019–20 through 2024–25 and on turnover; 2020 NASP
  Membership Survey Parts 1 and 2.
- Vannest & Hagan-Burke (2011), *Journal of Educational Research* — abstract via ERIC and
  OpenAlex (article closed access).
- President's Commission on Excellence in Special Education (2002) — ERIC ED473830.
- ED Office for Civil Rights, Civil Rights Data Collection national estimations API (HTTP 200)
  for Section 504-only counts, 2011–12 through 2020–21.
- IDEA §618 Part B Personnel (`bpersonnel2023-24.csv`) and Part B Child Count CSVs — data.ed.gov.
- US DoE Teacher Shortage Areas — raw API `POST tsa.ed.gov/api/ViewReportsAPI/Reports`.
- NCEO Reports 41, 47 and 412; ERIC full texts ED459571, ED499407, ED600669, ED517792, ED433362.
- Cochrane CD011775.pub2; PubMed eutils for Kim et al. (2017), Wyman et al. (2008, 2010),
  Kenny (2001), Aseltine et al. (2004, 2007), and the 2024/2025 gatekeeper meta-analyses.

### 14.3 Case law

Retrieved and read in full: *Rowley* (Library of Congress U.S. Reports PDF, HTTP 200);
*Endrew F.* and *Fry* and *Perez* (supremecourt.gov slip opinions, HTTP 200 — note the *Perez*
slip is `21-887_k53m.pdf`; the commonly-cited `_k53l.pdf` is a 404); *Roncker*, *Daniel R.R.*,
*Oberti*, *Rachel H.*, *Hartmann*, *Deal*, *Spielberg*, *L.B. v. Nebo*, *C.D. v. Natick* (via the
law.resource.org F.2d/F.3d mirror, HTTP 200 — note F3 volume directories are zero-padded to three
digits); *J.B. v. Kyrene* (cdn.ca9.uscourts.gov, HTTP 200).

### 14.4 Unreachable or unverified — flagged, not guessed

| Item | Status |
|---|---|
| CourtListener `/api/rest/v4/opinions/{id}/` full-text endpoint | **HTTP 401** (token now required). Search endpoint `/v4/search/?type=o` works at 200 for metadata only. |
| courtlistener.com HTML opinion pages | **HTTP 202**, Cloudflare challenge, empty body |
| bulk.resource.org (the host CourtListener returns in `download_url`) | **dead / HTTP 000**; rewrite to law.resource.org |
| law.justia.com, openjurist.org, casetext, findlaw | **HTTP 403** to both curl and WebFetch |
| leagle.com | HTTP 200 but Cloudflare interstitial |
| *P. ex rel. Mr. & Mrs. P. v. Newington Bd. of Educ.*, 546 F.3d 111 (2d Cir. 2008) | **Not retrieved** from four mirrors. **The 2d Circuit and D.C. Circuit LRE tests are therefore UNVERIFIED in this report.** Do not cite. |
| *Schaffer v. Weast*, 546 U.S. 49 (2005) | **Not retrieved.** Needed to qualify *Oberti*'s burden-of-proof holding. `UNVERIFIED` |
| GAO-20-22 full report body | **HTTP 403** on the PDF asset; only GAO's product-page summary was read |
| CADRE national DR data summaries (August 2025) | Landing pages 200; PDF payloads not extractable. CADRE's source is the same OSEP §618 collection reported here, so the primary figures supersede them. |
| NASP 2023–24 student:school-psychologist ratio brief (ERIC ED673365) | **files.eric.ed.gov HTTP 404.** The national ratio figure is **UNVERIFIED** in this report. |
| NCANDS *Child Maltreatment* annual report (acf.gov / acf.hhs.gov) | **HTTP 202, zero bytes** — bot challenge. The claim that education personnel are the largest single source of maltreatment referrals is therefore **UNVERIFIED here** and must not be asserted without retrieval. |
| Perry Zirkel litigation analyses | **ERIC abstracts only**; full texts not retrieved. Percentages are as stated in the abstracts. |
| sites.ed.gov/idea site search | Returns HTTP 200 but reports no results for every query including controls — **the search endpoint is unusable**, so the absence of OSEP AI guidance could **not** be established this way. |
| OSEP guidance on artificial intelligence under IDEA | **Not located.** The nearest official statement is ED OET, *Artificial Intelligence and the Future of Teaching and Learning* (May 2023): *"Laws such as the Individuals with Disabilities Education Act (IDEA) may likewise be considered as new situations arise in the use of AI-enabled learning technologies."* A Federal Register API search for documents containing both "artificial intelligence" and "individualized education program" since 2023 returned **5 results, all grant priorities or unrelated rules — none IDEA implementation guidance.** Best available characterisation: **regulatory silence**, stated as such. |
| **Empirical audits of PLAAFP and IEP-goal quality** — what fraction of PLAAFPs contain baselines, what fraction of goals are actually measurable | **Not retrieved.** This remains the largest gap in the report. Treat any figure on "what percentage of IEP goals are measurable" as **UNVERIFIED** until sourced. |
| Sireci, Scarpati & Li (2005) study-by-study support counts | RER closed; Unpaywall `is_oa: false`; Sage PDF **403**. Tallies substituted from Kettler (2015) and Lane & Leventhal (2015) via NCEO Report 412. |
| Buzick & Stone (2014) and Li (2014) exact effect sizes | Wiley **402/403**; Wayback no PDF snapshot. Direction of effect is verbatim from abstracts; **magnitudes UNVERIFIED**. |
| Gregg & Nelson (2012), *JLD* 45(2) extended-time meta-analysis | Abstract only; Sage **403**, Unpaywall CLOSED. Its own title is *"More questions than answers."* |
| Helwig & Tindal (2003) exact accuracy/kappa; Weis et al. (2016) exact percentages; Sahli Lozano et al. (2022) coefficients | Sage **403**; Taylor & Francis not OA. **Verbatim conclusions quoted; numbers UNVERIFIED.** |
| Rakap (2023) effect sizes and minute-level times | Full text paywalled. Direction and significance from the abstract; **magnitudes UNVERIFIED**. |
| Center for Democracy & Technology student-monitoring survey figures | **cdt.org returns HTTP 403 to every route** (full Chrome fingerprint, WebFetch, Wayback `id_` 404, CDX API 504). The figures quoted in EFF's report — 88% of schools monitoring, one in two teachers reporting law-enforcement contact, 48%/55%/41% discipline disparity — are **secondary-quoted and their sample sizes and question wording are UNVERIFIED.** |
| Gaggle "1,300 students" statistic and the 2024 AP / *Seattle Times* investigation | Every route failed: apnews.com domain-blocked and `/hub/gaggle` 404; seattletimes.com 404; lawrencekstimes.com and kansasreflector.com 403; the74million.org 404; gaggle.net 404; Wayback CDX 504. **Do not cite.** |
| "Vanderbilt/Lawrence Hidden Harms" | *Hidden Harms* is a **CDT** report title, not a Vanderbilt product; rand.org returned an empty shell; OpenAlex found no peer-reviewed cluster. **Likely a conflation. UNVERIFIED.** |
| C-SSRS as a school risk-screening protocol | PubMed returns only studies *using* C-SSRS as an instrument in school epidemiological samples, not evaluations of it as a screening protocol. **Do not assert an evidence base.** |
| Modern national IEP document length | The only national measurement located is **1980** (ED199970: mean ~5 pages, median under 3.5; state/special facilities mean 8, median 5). **No modern national page or word count exists.** |
| Number of IEP meetings per case manager per year | ERIC query `"number of IEP meetings"` returns **numFound: 0**. Genuine measurement gap. |
| Florida rule 6A-6.03028 running text | fldoe.org PDF **403**; title and 27 Aug 2024 effective date verified, **text UNVERIFIED**. |
| Texas Administrative Code and statutes via official sites | texreg.sos.state.tx.us serves a 2,517-byte "Site Has Moved" stub (TAC migrated to a JS-only portal mid-2025); statutes.capitol.texas.gov now returns an identical navigation shell for every chapter. **Rule text recovered from 2024 Wayback captures.** Also failed: ilga.gov 403, justia 403, casetext 410, regs.nysed.gov DNS failure, secure.sos.state.or.us JS challenge. |
| NCES Digest table 204.30 for 2023–24 and 2024–25 | `dt24_204.30.asp` **404**; percentages for those years recomputed from §618 CSVs against CCD enrolment and flagged as `INFERENCE`. Fall 2024 CCD enrolment not yet published, so the 2024–25 percentage is **UNVERIFIED**. |
| US DoE Teacher Shortage Area counts versus LPI's "45 states" | TSA raw API returns **37–43 of 51** jurisdictions listing special education across 2021–22 to 2025–26 (California never appears under this subject code, so these are floors). **The widely repeated "all 50 states" is not what the raw data shows, and the LPI figure exceeds the TSA-derived count. The discrepancy is unresolved.** |

### 14.5 A note on method

The one thing this report changed its mind about mid-research: the ADA Title II web-accessibility
deadline. Every secondary source and most of this project's own priors said **April 2026**. The
eCFR point-in-time text said April 2027, sourced to an amendment three months old. That was
verified against the Federal Register API before it was written down. **The discipline that caught
it — pull the regulation, never the summary of the regulation — is the same discipline this
report is asking `survey/04` to adopt about special education generally.**
