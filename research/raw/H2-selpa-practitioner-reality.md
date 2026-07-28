---
title: "H2 — The practitioner's week: IEP machinery, IDEA/504/ADA, LRE, procedural safeguards, caseload, and safeguarding"
wave: H
date_researched: 2026-07-28
sources_count: 61
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

5. **IEP services must be "based on peer-reviewed research to the extent practicable"
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
machinery before suing under 504/ADA? Two Supreme Court decisions govern (*Fry* 2017;
*Perez* 2023). This is assigned to the case-law strand — see §4 and the case-law block —
and is stated there rather than here to keep the citations in one place.

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

*(Sections 7–12 follow: caseload and workload; escalation and safeguarding; the
coordinator's week; the ownership table; the null-results ledger; and what `survey/04` must
say. Case-law block at §10.)*

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
