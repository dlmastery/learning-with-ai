---
title: "The Catalogue of Pedagogical Systems: What Humanity Already Figured Out, and Which of It AI Just Made Affordable"
wave: I
section: I1
date_researched: 2026-07-27
sources_count: 86
---

# I1 — The Catalogue of Pedagogical Systems

## 0. The thesis under test, stated precisely enough to be wrong

The claim this section exists to test:

> **Most great pedagogical systems were abandoned for cost, not efficacy. They were labour-intensive
> and lost to economics, not to evidence. If AI changes the cost structure, the right question is not
> "what new pedagogy does AI enable?" but "which known-good pedagogy just became affordable?"**

This is a strong claim with three separable parts, and they do not all survive equally.

**Part 1 — "the evidence was good."** Partly true, and the strength varies wildly across the
catalogue. It is strongest for the Keller Plan, Direct Instruction, peer instruction, tutoring, and
scaffolding. It is weak-to-absent for Montessori-as-a-system, Waldorf, Reggio Emilia, Suzuki,
Kumon, the Oxbridge tutorial, chavruta, Harkness, and every progressive/critical tradition. For
these, "abandoned for cost" is not the right description — several were never adopted at scale
*because they were never measured*, and a few (unassisted discovery, group-based mastery on
standardized tests) were measured and found wanting.

**Part 2 — "cost was the binding constraint."** True for a well-defined subset, and the subset is
identifiable by a signature: the method's per-learner marginal cost scales with *expert human
attention time* rather than with materials, space, or curriculum development. PSI, one-to-one
tutoring, tutorial/supervision teaching, mastery correctives, and cognitive-apprenticeship coaching
all have this signature. But for several systems the binding constraint was **not** cost at all:
Direct Instruction was cheap and *lost on ideology*; group-based mastery learning failed a
best-evidence synthesis; unassisted discovery learning has a *negative* pooled effect. Attributing
those to economics is a factual error, and the survey should not make it.

**Part 3 — "AI relieves the constraint and the mechanism survives."** This is where the interesting
failures live. Cost relief is real and large. Mechanism survival is *selective*. Several mechanisms
are constitutively dependent on properties an AI tutor does not have: a genuine peer with real
stakes (chavruta, jigsaw), a physical manipulative environment (Montessori), an authority who can
be *wrong* and beaten in argument (the tutorial), an audience whose comprehension you actually
change (learning-by-teaching). Section 7 treats these as first-class findings, not caveats.

**The honest summary, stated up front:** the thesis is roughly two-thirds right, and the third that
is wrong is the third most likely to be repeated uncritically by AI-education marketing. The
strongest single vindication is the Keller Plan. The strongest single refutation is Direct
Instruction. Both are in this catalogue.

---

## 1. Evidence labels and how to read the numbers

Every claim below carries one of four labels:

| Label | Meaning |
|---|---|
| `MEASURED-META` | Pooled estimate from a systematic review / meta-analysis with a stated effect size |
| `MEASURED-RCT` | Randomized (or lottery/cluster-randomized) controlled trial with a stated effect |
| `OBSERVED` | Quasi-experimental, pre/post, survey, or within-institution comparison; no randomization |
| `INFERENCE` | My reasoning from the above; not itself a measurement |

Four warnings that apply to every number in this section:

1. **Test alignment dominates.** Kulik & Fletcher's ITS meta-analysis found the pooled effect
   depended "to a great extent on whether improvement was measured on locally developed or
   standardized tests." Rosenshine & Meister's reciprocal-teaching reviews found results "usually
   significant when experimenter-developed tests were used, yet usually non-significant when
   standardized tests were used." Any pedagogy's effect size roughly halves when you move from a
   researcher-made test to a standardized one.
2. **"Months of additional progress" ≠ effect size.** The EEF/Evidence-for-Learning toolkit numbers
   quoted below are a policy-facing translation, and their *evidence security ratings* matter more
   than the headline months. Mastery learning is +5 months at **low** security; peer tutoring is +5
   months at **high** security. Those are not the same finding.
3. **Advocacy literature is over-represented** for Montessori, Waldorf, Reggio, PBL, Suzuki, Kumon
   and every commercial "personalized learning" product. Where evaluations are non-independent I say
   so.
4. **Effect sizes are not costs.** The whole point of this section is the ratio. A g of 0.30 at $20
   per pupil is a better buy than a g of 0.50 at $1,600 per pupil, and the literature almost never
   reports both.

---

## 2. What AI actually changes about cost — mechanically, not rhetorically

Before the catalogue, the cost model. A pedagogy's per-learner cost decomposes into:

| Cost component | Example | Does AI reduce it? |
|---|---|---|
| **Expert attention-minutes** | tutorial, mastery correctives, coaching, oral examining | **Yes — this is the big one.** Marginal cost falls from ~$30–100/hour of skilled labour to cents per session. |
| **Assessment & regrading labour** | PSI unit tests with unlimited retakes, mastery checks | **Yes, near-totally.** Item generation + grading + feedback are now cheap and unlimited. |
| **Curriculum authoring / sequencing** | DI's faultless-communication scripts, PSI unit design | **Partly.** Generation is cheap; *validation* is not, and DI's whole point is that the sequences were empirically debugged over years. |
| **Record-keeping and progress tracking** | PSI's administrative burden, competency-based transcripts | **Yes.** This was a first-order killer of PSI and it is now a solved problem. |
| **Physical materials and space** | Montessori manipulatives, lab equipment, workshop | **No.** (Simulation is a *different* mechanism, not a cheaper version of the same one.) |
| **Genuine peers with real stakes** | chavruta, jigsaw interdependence, peer instruction | **No.** Simulated peers change the mechanism (see §7). |
| **Institutional/political permission** | scripting teachers, ungraded transcripts, self-paced calendars | **No — and this is the constraint that actually killed several systems.** |

`INFERENCE`. The important structural point: **AI collapses exactly two of seven cost components to
near zero (expert attention-minutes, assessment labour), substantially reduces two more (authoring,
record-keeping), and does nothing at all to three (materials, genuine peers, institutional
permission).** The thesis is therefore true precisely for pedagogies whose costs sat in the first two
buckets — and PSI sat almost entirely there, which is why it is the flagship case.

---

## 3. Dialogue-based systems

### 3.1 The Socratic method / elenchus — what it actually is

**1. Mechanism.** The historical *elenchus* is a refutation procedure, not a friendly question-and-answer
style. Following Vlastos's reconstruction: (i) the interlocutor asserts a thesis; (ii) Socrates treats
it as false and targets it; (iii) Socrates secures assent to further premises; (iv) he shows the
premises jointly contradict the thesis; (v) he concludes the thesis false. Frede's objection is
important — showing a thesis false does not establish its negation, so the honest terminus is
*aporia*: productive puzzlement, the recognition that one's belief was not knowledge. The second
metaphor, *maieutikós* ("midwifery", *Theaetetus*), is the claim that the teacher does not implant
understanding but delivers what the learner can be brought to generate.
Source: https://en.wikipedia.org/wiki/Socratic_method — `OBSERVED` (scholarly reconstruction, not a
measurement).

Two features of the real method are systematically dropped by the pop version and by AI products:
**(a) the interlocutor must be genuinely refuted, i.e. left worse off in confidence than they
started**, and **(b) Socrates does not know the answer either.** Modern "Socratic seminars" are a
different animal — collaborative meaning-construction where "students lead the discussion and
questioning" and the teacher keeps discussion moving. That is a discussion protocol, not an
elenchus.

**2. Measured evidence.** There is **no meta-analysis of "the Socratic method" as an instructional
treatment.** This is a genuine hole in the literature and it should be stated plainly rather than
papered over. The closest rigorous evidence is on *structured classroom dialogue*:

- **Dialogic Teaching efficacy trial (EEF, 2017)** — 38 intervention schools (2,492 pupils) vs 38
  control schools (2,466 pupils), Year 5, England. Result: **+2 months' progress in English and
  science, +1 month in maths**; **+2 months in all three subjects for FSM-eligible pupils**;
  3-padlock ("moderately confident") security. Teachers reported two terms was too short to embed
  the approach, so the trial may understate the ceiling.
  https://eric.ed.gov/?q=%22Dialogic+Teaching%3A+Evaluation+Report%22 — `MEASURED-RCT`
  (cluster-randomized). **This is the single best rigorous evidence for dialogue-as-pedagogy and it
  is a modest +1 to +2 months, not a transformation.**
- The only Socratic-specific empirical observation in the reference literature is correlational:
  yeshiva-trained students subsequently succeed in law school, "although it remains an open question
  as to whether that relationship is causal or merely correlative."
  https://en.wikipedia.org/wiki/Socratic_method — `OBSERVED`.

**3. Why isn't it universal?** Not cost, primarily — **skill**. Running an elenchus requires a tutor
who can hold a learner's belief structure in mind, find the specific premise that contradicts it,
and tolerate leaving the learner in aporia. Most teachers cannot do this on demand for 30 students,
and the ratio makes it impossible even for those who can. Secondarily, aporia is *unpleasant* and
sits badly with student-satisfaction metrics.

**4. Does AI change the constraint, and does the mechanism survive?** The cost constraint: yes,
completely — this is a pure attention-minutes cost and it goes to ~zero. Both **LessonOrca**
("guides students to answers through questions, never gives answers directly",
https://lessonorca.com) and **Google Guided Learning** (announced 6 Aug 2025, powered by LearnLM
inside Gemini 2.5; "encourages participation through probing and open-ended questions",
https://blog.google/outreach-initiatives/education/guided-learning/) bet on exactly this. Neither has
published an independent outcome evaluation. `OBSERVED`.

Mechanism survival is **partial, and the failure is specific**: an LLM is trained to be agreeable and
to resolve tension, which is the opposite of the elenchus. It will not usually leave a learner in
aporia, and it *cannot* honestly occupy Socrates' position of not knowing the answer. What survives
well is the *questioning-instead-of-answering* discipline; what does not survive by default is
refutation and productive discomfort. The empirical hint that this matters is striking: in a
randomized crossover study of four GPT-based study tools (n = 195, ACT-derived passages), **the
Socratic discussion chatbot produced the largest benefit for low-baseline readers while AI tools
significantly *worsened* comprehension for high-baseline readers** — the summary tool worst of all.
https://doi.org/10.31234/osf.io/7mf5r — `MEASURED-RCT` (preprint, crossover). Socratic framing is
the AI tutoring design most likely to help the weakest learners and least likely to help the
strongest.

### 3.2 Socratic seminar, Harkness table, Paideia seminar

**1. Mechanism.** All three are structured whole-group text-centred discussion with the teacher
deliberately de-centred: a shared text, a prepared opening question, norms requiring students to
address each other rather than the teacher, and (Harkness) a literal oval table of ~12 seating
everyone as an equal. The mechanism claims are: obligatory articulation, exposure to peer
misconception, and accountability for having read.

**2. Measured evidence.** **Essentially none at controlled-trial standard.** Systematic ERIC searches
for Harkness and Paideia evaluations return descriptive and practitioner literature, not effect
sizes. The relevant transferable evidence is (a) the Dialogic Teaching trial above and (b) EEF
collaborative learning: **+5 months, ~$20 per pupil per year, LOW evidence security, 212 studies**,
with explicit caveats that unstructured grouping yields minimal benefit, students need explicit
instruction in collaboration, poorly implemented versions *widen* gaps when high achievers solve
problems with "no input from their peers", optimal group size is 3–5, and **technology-mediated
collaborative learning drops to +3 months**.
https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/collaborative-learning-approaches
— `MEASURED-META`.

**3. Why isn't it universal?** Cost of a specific kind: it requires a class of ~12, which is a
staffing-ratio decision, plus every student having done the reading. Harkness is a marker of elite
private schooling because the ratio is what is being purchased.

**4. Does AI change it, and does the mechanism survive?** Cost: **no.** The expensive input is not the
teacher's attention but the *twelve prepared peers*. An AI cannot supply that; a room of simulated
peers removes the only thing the seminar is for, which is being answerable to real people whose
respect you want. `INFERENCE`. **The seminar is the clearest case in this catalogue where AI does not
relieve the binding constraint.** What AI can do is the *preparation* side: guarantee every student
arrives having actually engaged the text, which the Dialogic-Teaching-style +1–2 months suggests is
where the marginal gain is anyway.

### 3.3 The Oxbridge tutorial / supervision system

**1. Mechanism.** Weekly hour-long meetings, **groups of one to three**, with a college fellow or
postdoc expert in the subject; the student submits work in advance (essay, problem set) and the hour
is spent defending it. https://en.wikipedia.org/wiki/Tutorial_system — `OBSERVED`. The mechanism is
not explanation; it is **serial obligation to produce and defend original work in front of someone
who can dismantle it.**

**2. Measured evidence.** No controlled evaluation of the tutorial system exists — you cannot
randomize Oxford. The nearest proxies:
- **One-to-one tuition: +5 months, 123 studies, moderate security, moderate cost — and an explicit
  cost figure: "a single student receiving 30 minutes tuition, five times a week for 12 weeks
  requires about four full days of a teacher's time, ... approximately $1,625 per student."**
  https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/one-to-one-tuition
  — `MEASURED-META`.
- **Tutoring meta-analysis (Nickow, Oreopoulos & Quan 2020, NBER w27476)**: pooled **0.37 SD** across
  PreK-12 experiments; teacher and paraprofessional tutors beat non-professional and parent tutors;
  effects strongest in earlier grades; in-school beats after-school. https://www.nber.org/papers/w27476
  — `MEASURED-META`.
- **The corrective to Bloom's 2-sigma claim.** VanLehn's review found that the widely believed
  ordering (answer-based CAI d = 0.3, ITS d = 1.0, human tutors d = 2.0) **did not replicate**:
  "the effect size of human tutoring was much lower: d = 0.79. Moreover, the effect size of
  intelligent tutoring systems was 0.76, so they are nearly as effective as human tutoring."
  https://eric.ed.gov/?q=%22The+Relative+Effectiveness+of+Human+Tutoring%22 — `MEASURED-META`.
  **This is load-bearing for the whole survey: expert human 1:1 is worth ~0.8 SD, not 2 SD, and
  machine tutoring already matched it before LLMs.**

**3. Why isn't it universal?** Cost, and unambiguously so. A 1:2 weekly hour with a subject expert is
the most expensive delivery mode in education. $1,625 per pupil per 12-week block (E4L) is the
industrial-scale version; the Oxford version is more expensive still. (I could not obtain a
published Oxford-specific per-student teaching cost; Wikipedia's tutorial-system article "contains
no figures regarding the cost of this system." Treat any specific Oxbridge cost figure as
unsourced.)

**4. Does AI change it, and does the mechanism survive?** Cost: **yes, maximally** — this is the purest
attention-minutes cost in the catalogue. Mechanism: **partially, with one specific casualty.**
Surviving: unlimited "defend your work" sessions, immediate high-quality challenge to written
argument, per-learner pacing. Not surviving: **the tutor who can be wrong and argued into changing
their mind.** The tutorial's status mechanism — that a real expert's opinion of your work matters and
that you can *win* — has no machine analogue, and current models capitulate under mild pushback
rather than holding a defensible position. `INFERENCE`. Design implication: an AI tutorial must be
built to *hold ground under pressure* and to be occasionally, defensibly right against the student,
or it degenerates into flattery.

### 3.4 Chavruta / havruta — Talmudic paired study

**1. Mechanism.** Two learners (occasionally 2–5) work a text aloud together as *equals* — no
teacher-student hierarchy. They "analyze, question, debate, and defend their points of view to
arrive at a mutual understanding." The canonical description of the mechanism is a rabbinic one:
"whenever I would say something, he would pose 24 difficulties and I would give him 24 solutions,
and as a result the subject became clear." Each partner must articulate reasoning precisely, defend
by argument rather than authority, attack the partner's weak links, and accept criticism. A
secondary mechanism is **commitment**: partners are "loath to disappoint or cancel."
https://en.wikipedia.org/wiki/Chavruta — `OBSERVED`.

**2. Measured evidence.** **None at controlled standard.** It is one of the oldest continuously
practised methods in the world and it has essentially no quantitative evidence base. The reference
literature notes enhanced reasoning and later law-school success but concedes "causality remains
unclear." `OBSERVED`. The transferable evidence is peer-instruction and collaborative-learning data
(§6).

**3. Why isn't it universal?** Not cost — chavruta is *cheaper* than lecturing, needs no expert per
pair, and scales linearly with enrolment. It isn't universal because it requires (a) a canonical
text dense enough to sustain 24 objections, (b) a community norm that argument is affection, and (c)
partners of comparable preparation who cannot walk away. Mainstream schooling supplies none of the
three. **This is a counter-example to the cost thesis: a method lost to culture and text-structure,
not economics.**

**4. Does AI change it, and does the mechanism survive?** Cost: irrelevant, it was already cheap.
Mechanism: **this is the clearest failure of substitution in the catalogue.** Chavruta's engine is
symmetry between two people who both have something at stake and neither of whom can be dismissed.
An AI partner is (i) not an equal, (ii) has nothing at stake, (iii) can be dismissed by closing a
tab, and (iv) removes the accountability mechanism ("loath to disappoint") entirely. An LLM can
*simulate* the 24 difficulties — and that is genuinely useful as a **stress-test tool** — but the
simulated version is closer to a Socratic tutor than to chavruta. `INFERENCE`. The honest framing:
**AI can supply the objections but not the partner.** Where AI plausibly helps chavruta is as
scaffolding *around* real pairs — matching partners, preparing each side, adjudicating a stuck
dispute — not as one of the two chairs.

### 3.5 Case method (HBS) and case-based learning

**1. Mechanism.** A dense, ambiguous, decision-forcing narrative; students prepare individually,
discuss in small groups, then a large-group discussion in which a skilled instructor cold-calls,
sequences contributions, and withholds resolution. The mechanism claims are transfer via
concrete-to-abstract induction, tolerance of underdetermined problems, and public accountability for
a position.

**2. Measured evidence.** Medical/professional-education meta-analyses of case-based learning report
large effects but on very weak substrate:
- CBL combined with PBL vs lecture in clinical medical education: **SMD = 2.161 [1.215, 3.106]** for
  theory exams, **1.594 [1.037, 2.152]** for practical skills — from only **7 studies, 604
  participants**. https://doi.org/10.1093/postmj/qgaf220 — `MEASURED-META`. **An SMD above 2 in
  education is a red flag for local-test alignment and small-study bias, not a discovery.**
- CBL vs lecture in pharmacy education: 11 studies, 1,339 students, significantly higher exam
  scores. https://doi.org/10.1186/s12909-025-07927-9 — `MEASURED-META`.
- No rigorous evaluation of the *HBS* case method specifically was locatable via ERIC.

**3. Why isn't it universal?** Two costs, one of them not attention-minutes: **case authoring** (a
good case is a research project) and **discussion-leading skill**. Plus the ratio: cold-call
dynamics need ~80 students who all prepared, which is a selection artefact of professional schools.

**4. Does AI change it, and does the mechanism survive?** Cost: **yes for authoring** — generating and
localizing decision-forcing cases is exactly what LLMs are good at, and this was a real bottleneck.
Mechanism: partially. What survives is preparation, individual position-forming, and being
interrogated on your recommendation. What does not survive is *watching 79 peers disagree with you
in public*, which is where the case method's attitude change comes from. `INFERENCE`.

---

## 4. Mastery and structure — the strongest ground for the thesis

### 4.1 The Keller Plan / PSI — the flagship case

**1. Mechanism.** Five defining features: (i) written materials as the primary vehicle, chosen
because text maximizes learner control; (ii) content divided into "separable, meaningful units" with
stated objectives and prerequisite structure; (iii) **self-pacing**; (iv) **unit mastery** —
typically ~90% required before progressing, with multiple equivalent test forms so retakes are not
retakes of the same items; (v) **proctors** (peers or advanced students) who administer and mark the
unit tests immediately, certify mastery, and provide social reinforcement.
https://en.wikipedia.org/wiki/Keller_Plan — `OBSERVED`.

**2. Measured evidence.**
- **Kulik, Kulik & Cohen (1979), "A meta-analysis of outcome studies of Keller's Personalized System
  of Instruction", *American Psychologist* 34(4):307–318, doi 10.1037/0003-066X.34.4.307** — **75
  comparative studies.** Conclusion: PSI "generally produces **superior student achievement, less
  variation in achievement, and higher student ratings** in college courses."
  https://doi.org/10.1037/0003-066x.34.4.307 — `MEASURED-META`. Note carefully: the *reduced
  variance* finding is as important as the mean shift and is almost never quoted. Mastery designs
  compress the bottom tail.
  *Caveat I must flag:* the frequently repeated "PSI ≈ 0.5 SD on final exams" figure is consistent
  with this literature but I could not verify it from the primary abstract in this pass. Treat the
  *direction and consistency* as `MEASURED-META` and the *specific 0.5* as unverified.
- **Kulik, Kulik & Bangert-Drowns (1990), "Effectiveness of Mastery Learning Programs: A
  Meta-Analysis", *Review of Educational Research* 60(2), doi 10.3102/00346543060002265** — **108
  controlled evaluations**; positive effects on examination performance in colleges, high schools and
  upper-elementary grades; also reports effects on attitudes, instructional time and college
  completion. https://doi.org/10.3102/00346543060002265 — `MEASURED-META`.
- Cross-domain replication: a meta-analysis of 130 studies / **341 effect sizes** of instructional
  systems in science teaching includes PSI among the systems favoured over conventional instruction.
  https://eric.ed.gov/?q=%22A+Meta-Analysis+of+Instructional+Systems+Applied+in+Science+Teaching%22 —
  `MEASURED-META`.
- **Mastery testing specifically** (49 comparative studies): positive, but effect size "depends on
  the stringency of the criterion used and the degree of experimental control."
  https://eric.ed.gov/?q=%22Mastery+Testing+and+Student+Learning%22 — `MEASURED-META`. The
  stringency dependence is a design instruction, not a caveat: **a low mastery bar destroys the
  effect.**

**3. Why isn't it universal?** This is the crux of the whole section, and the documented reasons are
overwhelmingly administrative and labour-based, not evidential. PSI peaked in the 1970s and "the
number of new research publications about PSI gradually declined" thereafter, despite "robust,
significantly positive effects on learning." The stated causes:
- **"Too radical [a] deviation from established teaching practices and educational management
  routines"** — the university calendar, the fixed-term grade, the lecture hall.
- **"PSI demands more teaching effort"** — proctor recruitment, training, scheduling, unlimited
  retake generation and marking.
- **Student withdrawal and procrastination** under self-pacing.
- Conflicts within the PSI movement itself.
https://en.wikipedia.org/wiki/Keller_Plan — `OBSERVED`.

**4. Does AI change the constraint, and does the mechanism survive?** **Yes, and yes — this is the
strongest case in the catalogue.** Map the five features onto the cost model in §2:

| PSI feature | Historic cost | AI cost |
|---|---|---|
| Written materials, unit structure | Authoring labour | Near-zero to generate, non-zero to validate |
| Self-pacing | Administrative chaos | Trivially handled |
| Unit mastery at ~90%, multiple equivalent forms | **Item writing + marking + immediate feedback at unbounded volume** | **Near-zero — this was the killer and it is now solved** |
| Proctors | **Recruit, train, schedule, pay humans** | **Near-zero** |
| Records | Filing-cabinet nightmare | Solved |

Mechanism survival is high because PSI's active ingredients are *structural* — a high mastery bar, a
prerequisite graph, unlimited low-stakes retesting on fresh items, immediate certification — none of
which depend on the proctor being human. The proctor's *social reinforcement* function is the one
partial casualty.

**But two documented threats to the naive version, and both matter:**
- **Procrastination and withdrawal under self-pacing is a documented failure mode of PSI itself**, and
  an AI tutor with no deadline inherits it exactly. `OBSERVED`.
- **The EEF/E4L mastery-learning entry states the approach becomes "much less effective when students
  work at their own pace"** and that "a high bar is set for achievement of mastery (usually 80% to
  90%)" is a critical success factor. https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/mastery-learning
  — `MEASURED-META`. **This is a direct, evidence-based warning against the most obvious AI-mastery
  product design (fully self-paced, no cohort, soft mastery bar).** The affordable version of PSI is
  not "self-paced AI"; it is "high mastery bar, unlimited fresh retests, external pacing pressure."

### 4.2 Mastery learning (Bloom's Learning for Mastery) — and its best-documented null

**1. Mechanism.** Group-paced, unlike PSI: the whole class moves through a unit together, takes a
formative assessment, and then splits — those at mastery get enrichment, those below get
**correctives** (different activities, individualized instruction, more time) and are reassessed.
Mastery is typically 80–90%. https://en.wikipedia.org/wiki/Mastery_learning — `OBSERVED`.

**2. Measured evidence — and the null.**
- Positive: Kulik, Kulik & Bangert-Drowns 1990, 108 evaluations (above). `MEASURED-META`.
- **The documented null (this is the section's flagship negative result): Slavin (1987), "Mastery
  Learning Reconsidered", *Review of Educational Research* 57(2):175–213, doi
  10.3102/00346543057002175.** Using best-evidence synthesis over applications of group-based mastery
  learning lasting ≥4 weeks in elementary and secondary schools: **"There was essentially no evidence
  to support the effectiveness of group-based mastery learning on standardized achievement measures.
  Effects were generally positive, though moderate, on experimenter-made measures, with little
  evidence that they were maintained over time."**
  https://eric.ed.gov/?q=%22Mastery+Learning+Reconsidered%22 — `MEASURED-META`. This provoked a
  literature of rebuttals (Kulik's "Is There Better Evidence on Mastery Learning? A Response to
  Slavin"; Guskey et al.; Slavin's rejoinder "Taking the Mystery Out of Mastery"), which is itself
  informative: **the dispute is about inclusion criteria and test type, and the honest reading is
  that mastery learning's effect is real on aligned assessments and small-to-absent on standardized
  ones.**
- Policy translation: **+5 months, very low cost (~$236/pupil/year including PD and intensive support
  for 20% of the class), LOW evidence security (down two padlocks), 80 studies. +8 months primary vs
  +3 secondary; +6 maths/science vs +3 reading.**
  https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/mastery-learning —
  `MEASURED-META`.

**3. Why isn't it universal?** Documented obstacles: teacher commitment (substantial setup and
maintenance), classroom-management complexity of running two tracks at once, and **administrative
fit** — mastery conflicts with fixed-time instructional schedules, so "many mastery programs in
schools have been replaced by more traditional forms of instruction."
https://en.wikipedia.org/wiki/Mastery_learning — `OBSERVED`. Note this is *partly* cost (correctives
are extra teacher time for 20% of the class) and *partly* the calendar.

**4. Does AI change it, and does the mechanism survive?** Cost: yes — correctives-on-demand is exactly
the attention-minutes bucket. Mechanism: yes for the corrective loop; **but the evidence says the
gain is concentrated where the assessment is aligned to instruction, which is precisely where an AI
system is most tempted to grade its own homework.** `INFERENCE`. The design rule that follows:
**an AI mastery system must be evaluated on an assessment it did not author.** Without that, the
Slavin critique applies to it verbatim.

### 4.3 Bloom's "2 sigma problem"

**1. Mechanism/claim.** Bloom (1984), "The 2 Sigma Problem: The Search for Methods of Group
Instruction as Effective as One-to-One Tutoring", *Educational Researcher* 13(6):4–16, doi
10.3102/0013189X013006004. The paper's framing — that one-to-one tutoring plus mastery produced ~2
SD over conventional instruction, and that the research programme should be to find group methods
that match it — is the founding text of the entire "AI tutor" genre.
https://doi.org/10.3102/0013189x013006004 — `OBSERVED` (I was unable to retrieve the article body;
the JSTOR-hosted PDF I obtained contained only the citation apparatus. The 2-sigma figure should be
cited to Bloom as a *claim in a 1984 review*, not as a replicated meta-analytic estimate.)

**2. The correction.** VanLehn (2011) explicitly tested the belief and found **d = 0.79 for human
tutoring, not 2.0**, with ITS at 0.76. `MEASURED-META`. Nickow et al. (2020) find **0.37 SD** pooled
across PreK-12 tutoring RCTs. `MEASURED-META`.

**3–4. Implication.** `INFERENCE`, and important enough to state as a finding: **the survey should not
use "2 sigma" as the target that AI tutoring is chasing.** The defensible target is 0.4–0.8 SD, and
Kestin et al.'s AI-tutor RCT (§8) landed at 0.63–0.73 — i.e. *within the human-tutoring range,
which is the honest and still remarkable claim.* Repeating "2 sigma" inflates expectations by ~2.5×
and sets up an inevitable disappointment cycle.

### 4.4 Direct Instruction (Engelmann) — the counter-example to the cost thesis

**1. Mechanism.** Explicitly *not* "teacher talks a lot." Engelmann's DI is a
**faultless-communication** engineering discipline: instructional sequences are designed so that the
examples presented logically permit only the intended generalization; scripted teacher wording
eliminates ambiguity; students are placed by assessment into skill-homogeneous groups; delivery uses
signals and rapid choral/individual response to get a high response rate per minute; mastery
criteria gate progression; and the sequence is *empirically debugged* — if children misgeneralize,
the script is the thing that gets fixed. The delivery frame is "I do / we do / you do."
https://en.wikipedia.org/wiki/Direct_instruction — `OBSERVED`.

**2. Measured evidence — this is one of the best-evidenced systems in education.**
- **Stockard, Wood, Coughlin & Rasplica Khoury (2018), "The Effectiveness of Direct Instruction
  Curricula: A Meta-Analysis of a Half Century of Research", *Review of Educational Research*
  88(4):479–507, doi 10.3102/0034654317751919.** Literature 1966–2016; **328 studies, 413 study
  designs, almost 4,000 effects.** "**All of the estimated effects were positive and all were
  statistically significant except results from metaregressions involving affective outcomes.**
  Characteristics of the publications, methodology, and sample were **not** systematically related to
  effect estimates. Effects showed **little decline during maintenance**, and effects for academic
  subjects were **greater when students had more exposure**. Estimated effects were educationally
  significant, moderate to large ..., and similar in magnitude to effect sizes that reflect
  performance gaps between more and less advantaged students."
  https://eric.ed.gov/?id=EJ1194248 — `MEASURED-META`. The "publication and methodology
  characteristics were not related to effect estimates" finding is unusual and strong: it is the
  absence of the small-study/publication-bias signature that discredits most of this literature.
  Reported magnitude is ~0.6 SD (secondary summary: https://en.wikipedia.org/wiki/Direct_instruction,
  `OBSERVED` for the specific number; Hattie's synthesis of 304 studies gives 0.59).
- Earlier: Adams & Engelmann (1996), 25-years-beyond-DISTAR meta-analysis, mean effect per study
  "more than .75". `MEASURED-META` (advocacy-adjacent source; discount accordingly).
- Special education: 25 studies; **none** favoured comparison groups; 53% of outcomes significantly
  favoured DI; effects not restricted to particular disabilities, ages or skill areas.
  https://eric.ed.gov/?q=%22A+Meta-Analysis+of+the+Effects+of+Direct+Instruction+in+Special+Education%22
  — `MEASURED-META`. **Directly relevant to the SELPA priority elsewhere in this survey.**
- **Project Follow Through.** "The largest and most expensive experimental project in education funded
  by the U.S. federal government that has ever been conducted": ~352,000 children, 178 projects, 20
  sponsored models at peak, after Congress cut Johnson's proposed $120M to $15M and forced a pivot
  from service to R&D. Result: on **basic skills**, DI was strongest — "models that emphasize basic
  skills succeed better than other models in helping children gain these skills"; on **cognitive
  skills** no model was notably superior; on **affective/self-esteem** the structured basic-skills
  models beat the unstructured alternatives (i.e. DI did *not* damage self-concept, contrary to the
  standard objection). Longitudinal DI-cohort data: children starting DI in kindergarten were
  accelerated ~7 months over those starting in first grade; in maths, DI students performed highest
  of ten approaches across computation, problem solving and concepts.
  https://en.wikipedia.org/wiki/Project_Follow_Through ;
  https://eric.ed.gov/?q=%22Direct+Instruction+Mathematics%3A+Longitudinal+Evaluation%22 — `OBSERVED`
  (no random assignment; treatment groups were often the neediest children).
- **The critique, fairly stated.** House, Glass, McLean & Walker (1978, *Harvard Educational Review*)
  argued the instruments did not capture what different models aimed at, that the evaluation
  privileged basic skills, and that self-concept instruments were not valid for young children.
  Others noted the absence of random assignment. `OBSERVED`.

**3. Why isn't it universal?** **Not cost — and this is the single most important entry in this
section, because it falsifies the strong form of the thesis.** DI is *cheap*: student workbooks ~$20,
teacher guides $180–232. It won the largest educational experiment ever run. And it was then
sidelined. Documented reasons:
- **Teacher resistance to scripting**, framed as a constraint on "both student and teacher
  creativity."
- **Ideological mismatch** with constructivist orthodoxy in teacher education; objections that
  scripted approaches cannot replace "in-depth experience with science concepts that inquiry-based
  strategies provide."
- Concerns about cultural insensitivity and inflexibility.
- **Political economy of dissemination**: the Joint Dissemination Review Panel and National Diffusion
  Network went on to recommend programmes that had *not* been validated in Follow Through, and
  funding for successful programmes was reduced from 1982. Former Education Commissioner Ernest
  Boyer called endorsing all models when "only one of the sponsors (Direct Instruction) was found to
  produce positive results more consistently" **"inappropriate and irresponsible."**
https://en.wikipedia.org/wiki/Direct_instruction ; https://en.wikipedia.org/wiki/Project_Follow_Through
— `OBSERVED`.

**4. Does AI change the constraint, and does the mechanism survive?** **AI does not change the binding
constraint at all, because the binding constraint was professional identity and institutional
politics, not money.** `INFERENCE`. But there is a genuine and underrated twist: **an AI tutor has no
professional identity to protect and cannot resent a script.** The one thing that blocked the
best-evidenced curriculum in education is exactly the thing an AI does not have. That is a real
opportunity, and it is *not* a cost argument.

Mechanism survival is high but not total. Surviving: faultless-communication sequence design,
placement, mastery gating, high response rate per minute (an AI can demand a response every few
seconds indefinitely, which no teacher can), immediate error correction. Not surviving: **choral
response** and the group-energy management that DI teachers are trained in. Also at risk: DI's
sequences were *empirically debugged over decades*; an LLM generating "DI-style" scripts on the fly
is producing the *form* without the validation that is the entire source of the effect size. **This
is the most likely way an AI product claims DI's evidence base without inheriting it.**

### 4.5 Precision teaching, mastery-based grading, competency-based education

**Precision teaching / frequency building.** Mechanism: define a pinpointed behaviour, time short
practice trials, chart rate-per-minute on a standard celeration chart, and let the *slope of the
chart* drive instructional decisions — the decision rule is the intervention. Evidence: a 2022
systematic review evaluated against WWC and CEC standards found **11 studies, 170 participants**,
with "small to large effects ... for all included variables."
https://eric.ed.gov/?q=%22Frequency+Building+and+Precision+Teaching%22 — `MEASURED-META` (very thin
corpus; do not oversell). Why not universal: charting and timing labour, plus its confinement to
behaviour-analytic special education. AI change: **large and under-exploited** — rate-based fluency
measurement and celeration charting are pure measurement labour, which is precisely what software
does for free. Mechanism survives essentially intact (the learner's response rate is the datum; who
counts it is irrelevant). `INFERENCE`. **This is a high-ratio, low-attention candidate that almost no
AI-education product implements.**

**Mastery-based / standards-based grading.** Mechanism: report against standards rather than
averaging, allow reassessment, decouple behaviour from achievement. Evidence: thin and mostly
descriptive in ERIC. Why not universal: **not cost — transcripts, GPA, and admissions.** AI does not
change that. `INFERENCE`.

**Competency-based education.** Mechanism: progression on demonstrated competence, not seat time.
Evidence: ERIC returns predominantly programme descriptions and policy pieces rather than rigorous
comparative outcomes; the honest statement is **"widely advocated, sparsely evidenced."** `OBSERVED`.
Why not universal: accreditation, credit-hour regulation, financial-aid rules keyed to seat time —
i.e. **institutional permission, which AI does not touch.** The E4L "individualised instruction"
entry is the closest quantitative proxy and is a warning: **+4 months but LIMITED evidence, 198
studies, downgraded three levels for dated research, *reliance on non-independent evaluations
particularly from commercial providers*, and substantial unexplained variation**; it also warns the
teacher's role "may become more managerial," reducing engaged learning time.
https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/individualised-instruction
— `MEASURED-META`. **Read that as the base rate for AI-personalization claims.**

---

## 5. Constructivist and inquiry systems — where the thesis mostly fails

### 5.1 Vygotsky's ZPD and scaffolding — the best mechanism-level match for AI

**1. Mechanism.** Scaffolding is not "help." Van de Pol, Volman & Beishuizen (2010) identify **three
constitutive characteristics: contingency (support is calibrated to the learner's current
performance), fading (support is systematically withdrawn), and transfer of responsibility.**
https://eric.ed.gov/?q=%22Scaffolding+in+Teacher-Student+Interaction%22 — `OBSERVED`. Remove fading
and you have not scaffolded, you have answered.

**2. Measured evidence.**
- **Belland, Walker, Kim & Lefler (2017), "Synthesizing Results From Empirical Research on
  Computer-Based Scaffolding in STEM Education", *Review of Educational Research*, doi
  10.3102/0034654316670999** — **144 experimental studies, 333 outcomes**: computer-based scaffolding
  had a "consistently positive (ḡ = **0.46**) effect on cognitive outcomes across various contexts."
  Notably, effects did **not** vary with context-specificity, presence/absence of scaffolding change,
  or the logic of fading; effects were greatest at the principles level and among adult learners, but
  "substantial and significantly greater than zero across all age groups and assessment levels."
  https://doi.org/10.3102/0034654316670999 — `MEASURED-META`. **This is the most directly
  AI-relevant meta-analysis in the whole catalogue: it is specifically about *computer-based*
  scaffolding, and it says the effect is robust and largely insensitive to design details.**
- Van de Pol et al. (2010): the number of *effectiveness* studies is small, results suggest
  scaffolding is effective, "however, more research is needed," and **"the main challenge in
  scaffolding research appears to be its measurement."** `OBSERVED`. Honest caveat: scaffolding is
  conceptually slippery and hard to operationalize.

**3. Why isn't it universal?** Contingency requires continuous real-time diagnosis of one learner's
current state — the most attention-expensive act in teaching. At 1:30 it is impossible; teachers
default to uniform support.

**4. Does AI change it, and does the mechanism survive?** **Yes and yes, with the highest confidence in
this document**, because the evidence is *already* about the machine-delivered version (ḡ = 0.46).
The one design hazard is that fading is the part products omit — an always-available hint system with
no withdrawal schedule is the anti-scaffold. `INFERENCE`.

### 5.2 Bruner's discovery learning — measured, and largely negative

**1. Mechanism.** The learner induces structure from examples with minimal telling; the claim is
deeper encoding and better transfer.

**2. Measured evidence — the cleanest negative result in the catalogue.**
**Alfieri, Brooks, Aldrich & Tenenbaum (2011), "Does discovery-based instruction enhance learning?",
*Journal of Educational Psychology* 103(1):1–18, doi 10.1037/a0021017.** Two meta-analyses over **164
studies**: unassisted discovery vs explicit instruction, **580 comparisons, random effects: d =
−0.38, 95% CI [−0.44, −0.31] favouring EXPLICIT instruction**; enhanced/assisted discovery vs other
instruction, **360 comparisons: d = +0.30 [0.23, 0.36] favouring enhanced discovery.** Conclusion:
"unassisted discovery does not benefit learners, whereas feedback, worked examples, scaffolding, and
elicited explanations do." https://doi.org/10.1037/a0021017 — `MEASURED-META`.

Supporting theory: **Kirschner, Sweller & Clark (2006), "Why Minimal Guidance During Instruction Does
Not Work", *Educational Psychologist* 41(2):75–86, doi 10.1207/s15326985ep4102_1** (4,294 citations),
and their 2007 reply to commentaries. https://doi.org/10.1207/s15326985ep4102_1 — the argument is
from cognitive-load theory and long-term-memory architecture. `OBSERVED` (theoretical review).

**3. Why isn't it universal?** It *is* extremely widespread in teacher education and curriculum
rhetoric — which is the interesting inversion. **Unassisted discovery is the one item in this
catalogue that is culturally dominant and empirically negative.** The cost thesis does not apply; the
efficacy verdict does.

**4. Does AI change it?** AI makes *enhanced* discovery cheap: the d = +0.30 condition is defined by
feedback, worked examples, scaffolding, and elicited explanations — all four of which are
attention-minutes costs that collapse. **AI does not rescue unassisted discovery; it makes the
assisted variant affordable, which is a different and better claim.** `INFERENCE`. This is the single
most useful design instruction extractable from the constructivist literature.

### 5.3 Montessori — be strict about the evidence

**1. Mechanism.** Multi-age classrooms; a specific, sequenced set of self-correcting physical
materials; **child-chosen work in long uninterrupted blocks**; three-hour work cycles; absence of
grades and tests; individual and small-group presentation of lessons; teacher as observer/preparer of
environment. The self-correcting *material* is load-bearing: the manipulative, not the adult, signals
error.

**2. Measured evidence — positive on average, but weaker than advocates claim, and with a documented
partial null.**
- **Randolph et al. (2023), "Montessori education's impact on academic and nonacademic outcomes: A
  systematic review", *Campbell Systematic Reviews*, doi 10.1002/cl2.1330.** Searched 19 databases
  plus grey literature and Montessori-specific journals. Finding: "Montessori education had a
  significant positive impact on academic and nonacademic outcomes. **Studies with random
  assignment, elementary school age level, and private Montessori schools had larger effects.**"
  The review's own framing is that "its effectiveness has not been clearly established" prior to
  this. https://doi.org/10.1002/cl2.1330 — `MEASURED-META`. **Note the moderator honestly: the
  effect is larger in *private* Montessori, which is exactly where selection is strongest.**
- **Courtier et al. (2021), "Effects of Montessori Education on the Academic, Cognitive, and Social
  Development of Disadvantaged Preschoolers: A Randomized Controlled Study in the French
  Public-School System" — the best-designed null.** Preregistered; disadvantaged preschoolers in a
  French public school randomly assigned to conventional or (adapted) Montessori classrooms.
  Cross-sectional in kindergarten (N = 176) and longitudinal over three years (N = 70). Result:
  **"the adapted Montessori curriculum was associated with outcomes comparable to the conventional
  curriculum on math, executive functions, and social skills"** — i.e. **null on three of four
  domains** — with an advantage only on reading (**d = 0.68**). The paper opens by noting prior
  Montessori research "is inconsistent and prone to analytic flexibility."
  https://eric.ed.gov/?q=Courtier+Montessori+randomized — `MEASURED-RCT`. Critically, the
  adaptations were *fewer materials, shorter work periods, limited teacher training* — so this is
  also evidence that **fidelity to the material environment is where the effect lives.**
- Lillard & Else-Quest (2006), "Evaluating Montessori Education", *Science*, doi
  10.1126/science.1132362 — lottery-based comparison at a single school; academic and social outcomes
  equal or superior. https://doi.org/10.1126/science.1132362 — `MEASURED-RCT` (small, single-site;
  the *Science* brief format reports no effect sizes).
- Lillard (2012): "classic Montessori" (higher exposure to Montessori materials) outperformed
  "supplemented Montessori" and conventional classrooms — a **fidelity dose-response**. `OBSERVED`.
- Documented mixed/negative: a 2005 Buffalo study "found no evidence that Montessori enrollment
  improved academic achievement relative to traditional programs"; a 2020 public-school analysis
  found Montessori students **scored lower than district peers in 3rd-grade math** while doing better
  in ELA at 3rd and 8th grade. https://en.wikipedia.org/wiki/Montessori_education — `OBSERVED`.
- A national lottery-based RCT across 24 public Montessori preschools (13 localities, 9 states),
  following children from age 3 through kindergarten, is the study to watch.
  https://eric.ed.gov/?q=%22A+National+RCT+of+the+Impact+of+Public+Montessori+Schools%22 — `OBSERVED`
  (design description).

**3. Why isn't it universal?** Genuinely multi-factorial: teacher training is a multi-year
certification; the material set is capital-intensive; multi-age classrooms conflict with grade-level
staffing and testing; and the no-grades/no-tests commitment conflicts with accountability regimes.
Cost is real but not the whole story.

**4. Does AI change it, and does the mechanism survive?** **Cost: barely. Mechanism: no.** The
self-correcting *physical* manipulative is the mechanism, and the Courtier RCT is direct evidence
that thinning the material environment thins the effect. A screen version of the pink tower is not a
cheaper pink tower; it is a different intervention with its own (much weaker) evidence base.
`INFERENCE`. **Montessori is the catalogue's clearest case of a mechanism that does not survive
digital substitution, and the survey should say so bluntly.** What AI can plausibly do is the
Montessori *teacher's* observation-and-record function — tracking which presentations a child has
had and what they have chosen — which is real but peripheral.

### 5.4 Waldorf and Reggio Emilia — evidence status: absent, plus documented harms

**Waldorf/Steiner. 1. Mechanism.** Developmental-stage theory derived from anthroposophy; delayed
formal literacy (until ~7); main-lesson blocks; same class teacher for years; heavy arts
integration; phenomenological science teaching.

**2. Measured evidence.** Effectively none at controlled standard. A 2005 independent review found
support for benefits to "creative, social and other capabilities" but the studies "tend to be
small-scale and vary in national context"; on Waldorf's own secondary-education aims, **"no
independent studies have been published as to whether or not Waldorf education achieves these aims
more than any other approach."** Positive scattered findings (higher Torrance creativity scores; a
2007 German study of graduate occupations) are uncontrolled. Pattern finding: Waldorf students "tend
to score below their peers in the earliest grades" but "catch up or surpass their peers by middle
school" — unadjusted for selection. Phenomenological science yields "high motivation" but "average
achievement." https://en.wikipedia.org/wiki/Waldorf_education — `OBSERVED`.

**Documented harms, which belong in any honest catalogue.** A 2010 UK Government report classified
Steiner schools as "high risk populations" for measles; a 2018 chickenpox outbreak at Asheville
Waldorf School involved 110 of 152 students lacking varicella vaccination; some California Waldorf
kindergartens showed 7% vaccination rates. California State University researchers identified
"patently pseudoscientific" curricular content ("animals evolved from humans", "Lemurian" and
"Atlantean epochs"). Multiple UK Steiner academies were judged "inadequate" by Ofsted for
safeguarding lapses and "mistreatment of children with special educational needs." Stockholm
University closed its Waldorf teacher training in 2008. The article also notes an unusual
meta-problem: the "unscientific foundation has been blamed for the scarcity of systematic empirical
research" because academics fear reputational cost in studying it. — `OBSERVED`.

**3–4.** Why isn't it universal: it is a worldview, not a technique, and it is not evidence-limited so
much as evidence-*averse*. Does AI change anything: **no.** There is no cost constraint to relieve and
no measured mechanism to port. `INFERENCE`. Include Waldorf in the survey as a case study in **how
pedagogical traditions survive without evidence**, not as a candidate for AI implementation.

**Reggio Emilia.** Mechanism: emergent, project-driven curriculum; documentation of children's work
as both assessment and pedagogy; the environment as "third teacher"; atelier and atelierista.
Evidence: no controlled comparative outcome literature was locatable; the tradition is documented
through practitioner accounts. `OBSERVED`. The one genuinely AI-relevant element is **documentation**
— Reggio's core practice is capturing and re-presenting children's thinking, which is a
labour-intensive recording task that multimodal AI does well. That is a defensible, narrow claim.
`INFERENCE`.

### 5.5 Problem-based and project-based learning — the assessment-dependent case

**1. Mechanism.** PBL: ill-structured authentic problem first, in small groups, with a facilitating
tutor; knowledge acquired in service of the problem. PjBL: extended production of an artefact.

**2. Measured evidence — the effect depends on what you measure, which is the whole finding.**
- **Dochy, Segers, Van den Bossche & Gijbels (2003), "Effects of problem-based learning: a
  meta-analysis", *Learning and Instruction*, doi 10.1016/S0959-4752(02)00025-7** — 43 articles.
  **"A robust positive effect on skills, but a tendency to a negative effect, strongly influenced by
  two studies, on student knowledge."** https://eric.ed.gov/?q=%22Effects+of+Problem-Based+Learning%3A+A+Meta-Analysis%22
  — `MEASURED-META`. **This is the documented negative for PBL and it is on knowledge acquisition.**
- **Gijbels, Dochy, Van den Bossche & Segers (2005), *RER* 75(1), doi 10.3102/00346543075001027** —
  reframes the whole dispute: PBL's effects depend on the level of the knowledge structure assessed
  (concepts / principles linking concepts / linking to conditions and procedures). **"PBL had the
  most positive effects when the focal constructs being assessed were at the level of understanding
  principles that link concepts."** https://doi.org/10.3102/00346543075001027 — `MEASURED-META`.
- **Walker & Leary (2009)** — 82 studies, 201 outcomes: **d_w = 0.13 ± 0.025**, with "a lack of
  homogeneity (Q = 954.27)". https://eric.ed.gov/?q=%22A+Problem+Based+Learning+Meta+Analysis%22 —
  `MEASURED-META`. **A pooled effect of 0.13 with Q ≈ 954 is close to "we cannot say."**
- **Albanese & Mitchell / "why curricula are likely to show little effect on knowledge and clinical
  skills", *Medical Education* 2000, doi 10.1046/j.1365-2923.2000.00753.x** — the title is the
  finding. `MEASURED-META`.
- **Project-based: Chen & Yang (2019), "Revisiting the effects of project-based learning on students'
  academic achievement: A meta-analysis investigating moderators", *Educational Research Review*, doi
  10.1016/j.edurev.2018.11.001** — **46 effect sizes from 30 journal articles (1998–2017), 12,585
  students, 189 schools, 9 countries: mean weighted d+ = 0.71**, "a medium to large positive effect
  ... compared with traditional instruction." Moderated by subject area, school location, hours of
  instruction and IT support; **not** by educational stage or small-group size.
  https://doi.org/10.1016/j.edurev.2018.11.001 — `MEASURED-META`. **Note the tension with Walker &
  Leary's d_w = 0.13 for PBL: the two constructs are not the same, and PjBL's much larger pooled
  effect rests on a comparator of "traditional instruction," i.e. lecture — the same soft comparator
  that inflates the active-learning literature generally.**
- A useful discriminator from an adjacent 2025 STEM-integration meta-analysis (79 effect sizes, 40
  studies, 15,577 students, **g = 0.661**): effects were "largest for **inquiry-based** learning, and
  progressively smaller for **problem-based**, **design-based**, and **project-based** learning."
  https://eric.ed.gov/?q=%22A+Meta-Analysis+of+STEM+Integration%22 — `MEASURED-META`. **Within the
  inquiry family, the more open-ended and production-oriented the format, the smaller the measured
  achievement effect.** That ordering is consistent with Alfieri and with Kirschner/Sweller/Clark.

**3. Why isn't it universal?** It nearly is, in rhetoric. Where it fails to stick, the reasons are
facilitator skill, coverage anxiety, and assessment mismatch — not money.

**4. Does AI change it, and does the mechanism survive?** Cost: moderately — problem authoring,
just-in-time domain input, and per-group facilitation are attention-minutes. But **the evidence says
the intervention's weakness is knowledge acquisition, which is exactly the thing AI-supplied
just-in-time explanation could fix.** So the honest AI claim about PBL is not "make PBL cheaper" but
**"repair PBL's documented knowledge deficit by pairing it with cheap explicit instruction on
demand"** — which turns it into Alfieri's *enhanced* discovery condition (d = +0.30) rather than the
unassisted one (d = −0.38). `INFERENCE`. That is the most defensible synthesis in this subsection.

### 5.6 Productive failure (Kapur)

**1. Mechanism.** Deliberately have learners attempt a problem *before* instruction (PS-I), so that
they generate and differentiate representations, discover the limits of their prior knowledge, and
are primed to encode the canonical solution when it arrives. The failure is the preparation.

**2. Measured evidence.** **Sinha & Kapur (2021), "When Problem Solving Followed by Instruction Works:
Evidence for Productive Failure", *Review of Educational Research*, doi 10.3102/00346543211019105** —
**53 studies, 166 comparisons** of PS-I vs I-PS: **Hedges' g = 0.36 [0.20, 0.51]** favouring PS-I;
**g = 0.37–0.58** where PS-I was implemented with high fidelity to Productive Failure principles;
publication-bias-corrected estimate **g = 0.87**. Moderators: grade level, intervention time span,
and (quasi-)experimental nature. **Documented boundary conditions / reversals: "Contrasting trends
were, however, observed for younger age learners (second to fifth graders) and for the learning of
domain-general skills, for which effect sizes favored I-PS."**
https://eric.ed.gov/?q=%22When+Problem+Solving+Followed+by+Instruction+Works%22 — `MEASURED-META`.

**3. Why isn't it universal?** It is counterintuitive, it looks like bad teaching to observers, it
consumes time, and — critically — it requires *designed* failure: a task that fails informatively.
That design is expert work.

**4. Does AI change it, and does the mechanism survive?** Cost: yes, on two fronts — generating tasks
whose failure modes are informative, and (harder) *diagnosing which productive failure a given
learner actually had* before delivering the consolidating instruction. Mechanism: survives well,
because nothing about it requires a human. **But an AI tutor's default behaviour — helping
immediately — is the direct negation of productive failure**, and the Bastani PNAS result (§8) is
essentially a large-scale demonstration of what happens when help arrives too readily. `INFERENCE`.
Design rule: **withholding is a feature and must be explicitly engineered, with the age and
skill-type boundary conditions respected (do not do PF with 2nd–5th graders or for domain-general
skills).**

---

## 6. Apprenticeship and practice

### 6.1 Cognitive apprenticeship — the best structural match for an AI tutor

**1. Mechanism.** Collins, Brown & Newman (1987/1989): make expert *thinking* visible, since unlike
physical crafts the cognitive work is hidden. Six methods:
**modelling** (expert performs the task with reasoning externalized, so the novice can build a
conceptual model); **coaching** (observe the novice and "offer feedback and hints to sculpt the
novice's performance to that of an expert's", adjusting difficulty); **scaffolding** (temporarily
execute the parts the learner cannot); **articulation** (make the learner state their reasoning);
**reflection** (have the learner compare their process against the expert's); **exploration**
(withdraw supports and teach the learner to set their own problems).
https://en.wikipedia.org/wiki/Cognitive_apprenticeship ; doi 10.4324/9781315044408-14 — `OBSERVED`.

**2. Measured evidence.** **There is no meta-analysis of cognitive apprenticeship as a package.** This
must be stated honestly: its evidential support is *compositional* — each of the six methods has its
own literature, and those are strong:
- modelling → worked-example effect (Alfieri's "worked examples" among the ingredients that make
  discovery work; `MEASURED-META`);
- coaching → feedback meta-analyses; the ITS literature (Kulik & Fletcher 0.66 median; VanLehn 0.76);
- scaffolding → Belland et al. ḡ = 0.46 for *computer-based* scaffolding (`MEASURED-META`);
- articulation → self-explanation and the peer-tutoring-tutors' effect (g = 0.43, §6.4);
- reflection, exploration → thinner.
The framework's own empirical documentation is qualitative, in technology-rich environments, online
applications, and clinical skills training. `OBSERVED`.

**3. Why isn't it universal?** All six methods are one-to-few, continuous-attention activities. Every
one of them is in the attention-minutes bucket. Cognitive apprenticeship is the *most* labour-intensive
framework in the catalogue, which is exactly why it stayed a research construct.

**4. Does AI change it, and does the mechanism survive?** **Yes on cost, and the mechanism maps almost
one-to-one — this is the highest-ratio entry in the catalogue.** Modelling = think-aloud generation
on demand. Coaching = continuous hinting calibrated to the observed attempt. Scaffolding = the
Belland-validated 0.46 case. Articulation = the machine can *require* an explanation before
proceeding, which a teacher of 30 cannot. Reflection = automatic side-by-side of the learner's trace
against an expert trace, which is nearly impossible to produce by hand and trivial to produce from
logs. Exploration = programmatic fading.

The single casualty: **the "apprenticeship" part — membership of a community of practice, and an
expert whose regard you are earning.** Cognitive apprenticeship's sociology dimension (working on
real problems, in a community, with legitimate peripheral participation) does not survive; the
methods dimension survives almost entirely. `INFERENCE`. **Build order recommendation: cognitive
apprenticeship is the correct architectural frame for an AI tutor, and PSI is the correct
progression/assessment frame around it.**

### 6.2 Guild apprenticeship

**1. Mechanism.** Long-duration, productive work under a master, with graduated responsibility, real
consequences for defects, and a credential controlled by practitioners.

**2. Measured evidence.** Modern apprenticeship literature is labour-economics rather than
learning-science, and the outcome measures are wages and employment. Not comparable to the effect
sizes above. `OBSERVED`.

**3. Why isn't it universal?** It was displaced by mass schooling and by the economics of firms not
wanting to train workers who can leave. **Political economy, not pedagogy.**

**4. Does AI change it?** **No.** The mechanism is *real production with real consequences*, and
simulated consequences are not consequences. `INFERENCE`. The narrow honest claim: AI lowers the
cost of the *master's explanatory time*, which historically was the scarce part of an apprenticeship
that was otherwise self-funding.

### 6.3 Deliberate practice — and the collapse of the strong claim

**1. Mechanism.** Ericsson's criteria: well-defined tasks with clear goals, performed individually,
with immediate feedback, repeated with refinement, and **designed by a teacher** to sit just beyond
current capability. https://en.wikipedia.org/wiki/Practice_(learning_method) — `OBSERVED`.

**2. Measured evidence — the replication critique is decisive against the strong version.**
- **Macnamara, Hambrick & Oswald (2014), "Deliberate Practice and Performance in Music, Games,
  Sports, Education, and Professions: A Meta-Analysis", *Psychological Science*, doi
  10.1177/0956797614535810** (428 citations), with a **2018 corrigendum**, doi
  10.1177/0956797618769891 — the corrigendum should be cited alongside it.
  https://doi.org/10.1177/0956797614535810 — `MEASURED-META`.
- **Macnamara, Moreau & Hambrick (2016), "The Relationship Between Deliberate Practice and Performance
  in Sports: A Meta-Analysis", *Perspectives on Psychological Science*, doi 10.1177/1745691616635591**:
  "**deliberate practice accounted for 18% of the variance in sports performance**. However ...
  deliberate practice accounted for **only 1% of the variance in performance among elite-level
  performers.** This finding is inconsistent with the claim that deliberate practice accounts for
  performance differences even among elite performers." Also: high-skill athletes did **not** start
  younger. https://doi.org/10.1177/1745691616635591 — `MEASURED-META`. **This is the documented
  refutation of the 10,000-hour claim, and it is stronger than the popular summary suggests: at the
  elite level, practice hours explain essentially nothing.**
- Ericsson himself disputes Gladwell's 10,000-hour formulation, noting hours vary hugely by domain
  and that mere engagement "has a much lower benefit ... than deliberate practice." `OBSERVED`.
- Positive, narrow: deliberate practice in residency training, 10 RCTs / 277 residents, improved
  checklist scores (MD = 4.44 [1.72, 7.15]). https://doi.org/10.21203/rs.3.rs-2957482/v1 —
  `MEASURED-META` (preprint, small).

**3. Why isn't it universal?** Because the *coach who designs the next task* is the expensive part —
and because deliberate practice is aversive, which is a motivational cost, not a financial one.

**4. Does AI change it, and does the mechanism survive?** Cost: yes for task design and immediate
feedback. Mechanism: survives well for well-specified skills with fast objective feedback (language
production, code, mathematics, sight-reading), poorly for domains where "correct" is contested.
**But the survey must not oversell: the meta-analytic ceiling on practice-quantity explanations is
low (18% of variance in sports, 1% at elite level), so an AI system that optimizes practice volume
is optimizing a variable that explains less than advocates claim.** `INFERENCE`.

### 6.4 Suzuki and Kumon — commercially huge, evidentially near-empty

**Suzuki. Mechanism:** "mother-tongue" immersion — daily listening to professional recordings from
infancy; learning by ear before notation; **parental attendance at lessons and supervision of daily
practice**; a common graded repertoire enabling group play.
https://en.wikipedia.org/wiki/Suzuki_method — `OBSERVED`. **Evidence:** the reference article
"does not provide empirical research data" and carries maintenance tags for promotional content;
ERIC returns practitioner and historical analyses (e.g. "Changes after Suzuki", *IJME* 2019, doi
10.1177/0255761419859628) rather than controlled comparisons. `OBSERVED`. **Why not universal:** it
requires a parent's daily labour — the most under-priced input in education. **AI:** cannot supply
the parent. It can supply the listening environment, the graded repertoire, and immediate
pitch/rhythm feedback. The mechanism most at risk is precisely the parental one. `INFERENCE`.

**Kumon. Mechanism:** pencil-and-worksheet incremental progression in very small steps, mastery-and-
speed criteria before advancement, daily short sessions, instructor as pace-setter rather than
explainer; digital programme from 2023. **Evidence:** a 1994 study (Ukai) reported "a high degree of
efficacy"; a developmental psychologist (Hirsh-Pasek) is quoted that such drilling for
pre-kindergarteners "does not give your child a leg up on anything." **No independent controlled
evaluation was locatable via ERIC or Crossref.** https://en.wikipedia.org/wiki/Kumon — `OBSERVED`.
**Why not universal:** it *is* enormous commercially, and unevidenced. **AI:** Kumon is the single
most trivially automatable system in this catalogue (graded worksheet generation, timing, mastery
gating, records) — and it is also the one whose evidence base least justifies automating it. The
honest reading: **Kumon is essentially PSI-for-arithmetic with a franchise model, so port PSI's
evidence, not Kumon's.** `INFERENCE`.

---

## 7. Peer and social systems

### 7.1 Peer instruction (Mazur)

**1. Mechanism.** Seven steps: pose a conceptual question (ConcepTest) targeting a known
misconception → individual thinking → individual commitment to an answer → instructor reads the
distribution → **peer discussion in which students must convince each other** → second individual
commitment → instructor decides whether more explanation is needed.
https://en.wikipedia.org/wiki/Peer_instruction — `OBSERVED`. The mechanism is that a peer who *just*
overcame the misconception explains it better to someone still holding it than an expert who never
held it does.

**2. Measured evidence — strong, but mostly not randomized.**
- **Crouch & Mazur (2001), *American Journal of Physics* 69(9):970–977, doi 10.1119/1.1374249** —
  Harvard, ten years, Force Concept Inventory normalized gain ⟨g⟩:

  | Year | Method | FCI pre | FCI post | ⟨g⟩ | MBT | N |
  |---|---|---|---|---|---|---|
  | 1990 | Traditional | (70%) | 78% | **0.25** | 66% | 121 |
  | 1991 | PI | 71% | 85% | **0.49** | 72% | 177 |
  | 1993 | PI | 70% | 86% | 0.55 | 71% | 158 |
  | 1994 | PI | 70% | 88% | 0.59 | 76% | 216 |
  | 1995 | PI | 67% | 88% | 0.64 | 76% | 181 |
  | 1996 | PI | 67% | 89% | 0.68 | 74% | 153 |
  | 1997 | PI | 67% | 92% | **0.74** | 79% | 117 |
  | 1998 | PI (algebra) | 50% | 83% | 0.65 | 68% | — |
  | 1999 | **Traditional** (algebra) | (48%) | 69% | **0.40** | — | — |
  | 2000 | PI (algebra) | 47% | 80% | 0.63 | 66% | — |

  Also: the 1985 all-quantitative final exam was re-administered in 1991 (first PI year); mean rose
  **63% → 69%, "a statistically significant increase (effect size 0.34)"**, with fewer extremely low
  scores. MBT quantitative subset rose 62% → 66%. Note the internal control: the *same* algebra-based
  course taught traditionally in 1999 by a different instructor gave ⟨g⟩ = 0.40 versus 0.65/0.63 with
  PI. `OBSERVED` (within-institution, non-randomized, instructor confounds acknowledged).
- **Hake (1998), *AJP* 66(1):64–74, doi 10.1119/1.18809** — 62 introductory courses, N = 6,542. **14
  traditional courses (N = 2,084): ⟨g⟩ = 0.23 ± 0.04. 48 interactive-engagement courses (N = 4,458):
  ⟨g⟩ = 0.48 ± 0.14 — "almost two standard deviations of ⟨g⟩ above that of the traditional courses."**
  Mechanics Baseline results for 30 of the courses imply IE also enhances problem-solving.
  https://eric.ed.gov/?q=%22Interactive-Engagement+vs.+Traditional+Methods%22 — `OBSERVED`
  (self-selected survey of instructors, not an experiment; this is the correct caveat and it is
  usually omitted).
- **Freeman et al. (2014), PNAS 111(23):8410, doi 10.1073/pnas.1319030111** — **225 studies**:
  active learning raised examination/concept-inventory performance by **0.47 SD (n = 158 studies)**;
  **odds ratio for failing 1.95 under traditional lecturing (n = 67)**; ≈6% average exam improvement;
  effects hold across STEM disciplines and all class sizes, greatest in classes ≤50; larger on concept
  inventories than course exams. https://doi.org/10.1073/pnas.1319030111 — `MEASURED-META`.
- **The documented null:** a randomized study of 186 second-year medical students (93 peer
  instruction vs 93 conventional group work) in a respiratory-physiology lab: **"There was no
  difference in total test scores between groups"**; PI won only on simple integrated questions, and
  students rated *conventional group work* more highly overall.
  https://doi.org/10.1152/advan.00045.2021 — `MEASURED-RCT`. **When peer instruction is compared to
  another active method rather than to lecture, the advantage can vanish.** That is the correct
  interpretation of most of this literature: the contrast is against *lecture*, not against
  well-designed alternatives.

**3. Why isn't it universal?** Not cost — PI is nearly free (a clicker app and good ConcepTests). The
constraints are: writing diagnostic ConcepTests is expert work; it requires ceding lecture time and
tolerating public wrongness; and it requires **a room of peers at comparable-but-varied
understanding**.

**4. Does AI change it, and does the mechanism survive?** Cost: **only the ConcepTest-authoring part**,
which is real (misconception-targeted item generation is a genuine AI strength). Mechanism:
**substantially does not survive.** PI's engine is a *distribution* of real peer answers and the
social act of persuasion. A simulated peer has no misconception it actually holds and nothing at
stake in convincing you. `INFERENCE`. **The correct AI role in peer instruction is item author and
misconception analyst, not peer.** (Note also the 2021 null: AI-mediated "discussion with a bot"
would be competing against *another active method*, the condition where PI's advantage disappeared.)

### 7.2 Reciprocal teaching

**1. Mechanism.** Four strategies — predicting, questioning, clarifying, summarizing — practised in a
scaffolded dialogue where the *leader role rotates to students*, with the teacher modelling first and
then fading. https://en.wikipedia.org/wiki/Reciprocal_teaching — `OBSERVED`.

**2. Measured evidence — positive overall, with a very instructive null pattern.**
- **Rosenshine & Meister (1994), "Reciprocal Teaching: A Review of the Research", *RER* 64(4):479–530,
  doi 10.3102/00346543064004479** — 16 quantitative studies, "generally supports the efficacy of
  reciprocal teaching but also indicates the need for further research."
  https://eric.ed.gov/?q=%22Reciprocal+Teaching%3A+A+Review+of+the+Research%22 — `MEASURED-META`.
- **The same authors' fuller technical report on 19 experimental studies gives the pattern that
  matters:** (i) results were "usually more significant when **explicit instruction** in the cognitive
  strategies was provided **before** the reciprocal teaching began than when reciprocal teaching only
  was used"; (ii) results were **"mostly non-significant when below-average students were taught"**,
  yet usually significant for all other students; (iii) results were "usually significant when
  experimenter-developed tests were used, yet usually non-significant when **standardized tests**
  were used." https://eric.ed.gov/?q=%22Reciprocal+Teaching%3A+A+Review+of+19+Experimental+Studies%22
  — `MEASURED-META`. **Three separate nulls in one finding: no standardized-test effect, no effect
  for weak students, and no effect without prior explicit instruction.**

**3. Why isn't it universal?** Teacher skill in running the dialogue and in fading; and the finding
that it needs explicit strategy instruction first — which is more, not less, teacher work.

**4. Does AI change it, and does the mechanism survive?** Cost: yes for the explicit-instruction
front-end and for unlimited practice of the four strategies against fresh text. Mechanism: partly —
**the rotating leader role in front of peers is the social engine and does not transfer**, but the
strategy practice itself does. Critically, the "mostly non-significant for below-average students"
finding is a **direct warning for the SELPA priority**: reciprocal teaching is not the right first
build for struggling readers; explicit instruction is. `INFERENCE`.

### 7.3 Jigsaw and cooperative learning

**1. Mechanism.** Jigsaw creates **structural positive interdependence**: material is partitioned so
each student holds a piece nobody else has, expert groups master a piece, then home groups reassemble
and each member must teach their piece. Nobody can succeed alone and nobody can be ignored.

**2. Measured evidence.**
- Cooperative learning has a very large, old, and generally positive meta-analytic base (e.g. 133
  studies of adult cooperative vs competitive vs individualistic effort, favouring cooperation on
  achievement, relationships and self-esteem;
  https://eric.ed.gov/?q=%22Research+Shows+the+Benefits+of+Adult+Cooperation%22 — `MEASURED-META`).
- Jigsaw-specific: a 2024 meta-analysis in nursing education, **11 studies across 6 countries**,
  finds positive effects. https://doi.org/10.1016/j.nepr.2024.103902 — `MEASURED-META` (small, single
  discipline).
- Policy translation: E4L collaborative learning **+5 months, ~$20/pupil/year, LOW security, 212
  studies** — with the caveats already quoted (structure required; explicit collaboration
  instruction required; poor implementation *widens* gaps; **digital delivery only +3 months**;
  optimal group 3–5). — `MEASURED-META`.
- **Sceptical note worth including:** a re-examination of the Springer, Stanne & Donovan (1999)
  small-group-learning meta-analysis in medical education concluded "the meta-analysis' call for
  more widespread implementation of small group learning is not supported."
  https://eric.ed.gov/?q=%22Small+Group+Learning+in+Medical+Education%22 — `OBSERVED`.

**3. Why isn't it universal?** Not cost. Structure and teacher skill: unstructured group work is what
schools actually do, and E4L is explicit that it "yields minimal benefits."

**4. Does AI change it, and does the mechanism survive?** **Cost: no. Mechanism: no.** Jigsaw's engine
is *irreplaceable human interdependence* — the whole design is that your teammates need you. An AI
teammate that already knows everything destroys the interdependence by construction. Note also the
measured penalty for going digital at all: +3 months vs +5. `INFERENCE`. **AI's legitimate role is
partitioning material, preparing each expert group, and detecting free-riding — orchestration, not
participation.**

### 7.4 Learning by teaching / the protégé effect

**1. Mechanism.** Preparing to teach and then teaching forces retrieval, organization, gap-detection,
and generation of explanations; the "protégé effect" adds a motivational component — learners work
harder for a protégé than for themselves.

**2. Measured evidence.** **An updated meta-analysis of the effect of peer tutoring on *tutors'*
achievement (16 articles) found a weighted mean effect size of g = 0.43 (p < 0.001)**, and identified
parameters that optimize it.
https://eric.ed.gov/?q=%22An+Updated+Meta-Analysis+on+the+Effect+of+Peer+Tutoring+on+Tutors%27+Achievement%22
— `MEASURED-META`. Complementary: E4L peer tutoring **+5 months, VERY LOW cost (<$80/pupil), HIGH
evidence security, 127 studies** — with the honest caveat that "a large percentage of the studies
were not independently evaluated," which may inflate the estimate, and that **training for staff and
tutors is essential**.
https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/peer-tutoring —
`MEASURED-META`.

**3. Why isn't it universal?** Scheduling and the need for a *tutee*. Cross-age tutoring requires
timetable surgery.

**4. Does AI change it, and does the mechanism survive?** **This is the most interesting substitution
case in the catalogue, and the answer is "yes, surprisingly well."** A "teachable agent" that plays a
confused learner supplies the one thing that was scarce — an always-available tutee — and unlike the
chavruta or jigsaw cases, **the tutee's authenticity matters much less, because the cognitive work is
happening in the *tutor's* head.** The mechanism is retrieval + organization + explanation
generation, all of which occur regardless of whether the listener is real. The part that is at risk
is the *motivational* protégé effect, which depends on the learner caring about the agent — an
empirical question, not a design certainty. `INFERENCE`. Combined with the 0.43 tutors' effect size
and <$80 cost, **learning-by-teaching-to-an-AI is a top-tier build candidate and it is
under-implemented relative to Socratic tutoring.**

### 7.5 Flipped classroom — where the hype exceeds the meta-analyses

**1. Mechanism.** Move exposition out of class (video/reading), use class time for the active work
that exposition displaced. It is a *scheduling* intervention, and its effect should be bounded by the
quality of what fills the reclaimed time.

**2. Measured evidence.**
- **van Alten, Phielix, Janssen & Kester (2019), "Effects of flipping the classroom on learning
  outcomes and satisfaction: A meta-analysis", *Educational Research Review* 28, doi
  10.1016/j.edurev.2019.05.003** — **114 studies**, secondary and postsecondary: "a **small positive
  effect on learning outcomes**, but **no effect was found on student satisfaction** regarding the
  learning environment," with "considerable heterogeneity between studies." Two decisive moderators:
  students achieve more **when face-to-face class time is *not* reduced**, and **when quizzes are
  added** to the flipped condition. https://doi.org/10.1016/j.edurev.2019.05.003 — `MEASURED-META`.
  **Both moderators are damning for the usual business case: flipping pays only when you add
  retrieval practice and refuse to cut contact hours — i.e. when it is not a cost saving at all.**
  Note also the direct conflict with Låg & Sæle below on satisfaction (no effect vs g = 0.36); take
  van Alten's larger corpus as the better estimate.
- **Låg & Sæle (2019), "Student Satisfaction with Courses and Instructors in a Flipped Classroom: A
  Meta-Analysis", doi 10.1111/jcal.12421** — 53 studies, 8,429 students: **weak-to-moderate positive
  effect on satisfaction with courses (k = 50, g = 0.36) and with instructors (k = 26, g = 0.40).**
  https://eric.ed.gov/?q=%22Student+Satisfaction+with+Courses+and+Instructors+in+a+Flipped+Classroom%22
  — `MEASURED-META`.
- A 2021 meta-analysis of 20 experimental studies of college flipped classrooms: overall combined
  effect **0.66**, but wildly discipline-dependent — **science 0.75, liberal arts 0.72, engineering
  0.34.** https://eric.ed.gov/?q=%22The+Impact+of+Flipped+Classroom+on+College+Students%27+Academic+Performance%22
  — `MEASURED-META`. A range of 0.34–0.75 by discipline is the honest headline.
- A quasi-experiment in advanced statistics notes flipping "entails **high start-up costs**" while
  producing gains concentrated "in difficult, applied areas emphasized in class."
  https://eric.ed.gov/?q=%22Flipping+the+Classroom+and+Student+Performance+in+Advanced+Statistics%22
  — `OBSERVED`.

**3. Why isn't it universal?** Video production cost, and the fact that it fails when students don't
do the pre-work.

**4. Does AI change it, and does the mechanism survive?** Cost: yes — exposition generation becomes
free, and (more importantly) **AI can verify and enforce that pre-work happened**, which is flipping's
actual failure mode. Mechanism: survives, but note that **flipping is not itself a pedagogy** — its
effect is entirely parasitic on what fills class time, so "AI-powered flipped classroom" is a
delivery claim, not a learning claim. `INFERENCE`.

---

## 8. Progressive and critical traditions — stating the evidence status honestly

**Dewey.** Mechanism: education as experience-reconstruction; the school as a form of community life;
inquiry beginning in genuine indeterminate situations. Evidence status: **philosophical, not measured.**
Dewey's programme predates and largely frames the constructivist literature that *has* been measured
(§5.2, §5.5), and the verdict there — unassisted discovery negative, assisted discovery positive —
is the closest thing to an empirical evaluation of Deweyan pedagogy that exists. `INFERENCE`.

**Freire's critical pedagogy.** Mechanism: problem-posing education against the "banking" model;
dialogue between co-investigators; literacy taught through generative words drawn from the learners'
own political situation; *conscientização* as the outcome. Evidence status: **the outcome variable is
not an achievement test, and the tradition largely rejects the measurement frame.** Systematic
searches return theoretical and programme literature, not controlled comparisons. **State this
plainly in the survey rather than fabricating an evidence base**: critical pedagogy is a normative
theory of the purpose of education, and it is not in competition with mastery learning for the same
metric. `OBSERVED`/absent. Does AI change it? The dialogue-cost argument applies, but Freire's
dialogue is between people who share a political condition — which an AI does not share. The
mechanism does not survive substitution; the *access* argument (Freire was solving for illiterate
adults with no teachers) does. `INFERENCE`.

**Sudbury / democratic schooling.** Mechanism: direct democracy with students and staff holding equal
votes; a weekly School Meeting setting rules, budget and staffing; a formal judicial system with
complaints, hearings and appeals; no curriculum, no classes required, no testing; deliberate
age-mixing. Evidence status: **essentially nil.** The reference literature contains "virtually no
empirical outcome data"; the school's own claim is that "all of their students have learned to read";
the one cited study (Gray & Chanoff 1986) is reported without sample size, methodology or findings.
https://en.wikipedia.org/wiki/Sudbury_school — `OBSERVED`. Unschooling outcome research is
predominantly self-selected retrospective survey. **Do not report these as evidenced.** Does AI
change anything? Only in the sense that self-directed learners now have an on-demand explainer,
which removes one of the strongest practical objections (that a child who wants to learn X in a
school with no X teacher is stuck). That is a genuine and narrow gain. `INFERENCE`.

---

## 9. The AI-side evidence base — what is actually measured, including the negatives

Any ranking of "which pedagogy AI makes affordable" needs the current measured performance of AI
instruction, both directions.

**Positive, high quality.**
- **Kestin, Miller, Klales, Milbourne & Alvarez (2025), "AI tutoring outperforms in-class active
  learning: an RCT introducing a novel research-based design in an authentic educational setting",
  *Scientific Reports*, doi 10.1038/s41598-025-97652-6.** Crossover RCT in Harvard's largest physics
  course (PS2, N = 233; analysis N = 194; 316 pre-test data points). Custom AI tutor built on the
  *same* pedagogical principles as the in-class active-learning lesson. Results: AI group median
  post-score **4.5 (N = 142)** vs in-class **3.5 (N = 174)** against a pre-test baseline of 2.75;
  **"p < 10⁻⁸ ... with a large effect size. While the linear regression suggests an effect size of
  0.63, [a ceiling-robust analysis] provides an effect size in the range of 0.73"**; median AI
  time-on-task **49 minutes vs 60 minutes** in class — *more learning in less time*; and **no
  correlation between time on task and post-test scores**. Engagement (4.1 vs 3.6, t(311) = −4.5) and
  motivation (3.4 vs 3.1, t(311) = −3.4, p < 0.001) both favoured AI; two growth-mindset-related items
  showed no difference. https://www.nature.com/articles/s41598-025-97652-6 — `MEASURED-RCT`. **Note
  what the design controls: the comparator is active learning, not lecture — the hard comparison —
  and the AI tutor was built to implement known pedagogy, not to be a chatbot.**
- **Nigeria after-school generative-AI tutoring RCT (World Bank, Jun–Jul 2024, six weeks):**
  approximately **0.3 SD**, described as outperforming ~80% of comparable interventions in developing
  countries; the evaluation team believes the design "likely underestimated the true impact";
  attendance was disrupted by flooding, teacher strikes and after-school work.
  https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-Transforming-learning-in-Nigeria
  — `MEASURED-RCT`.
- Emerging meta-analyses of ChatGPT on achievement: **g = 0.573** across 22 studies (Nov 2022–Dec
  2024), with a larger effect for middle/high school (g = 0.928) than undergraduates (0.538, ns
  difference); another reports g = 0.86 across 13 studies with chatbots/generative AI at 1.02.
  https://eric.ed.gov/?q=%22A+Meta-Analysis+of+ChatGPT%27s+Influence+on+Learning+Achievement%22 —
  `MEASURED-META`. **Discount heavily: tiny corpora, 2022–2025 publication window, near-certain
  publication bias, and almost all local tests.** These are not comparable to the 225-study Freeman
  or 328-study Stockard bases.

**Negative — the required counterweight.**
- **Bastani, Bastani, Sungu, Ge, Kabakcı & Mariman (2025), "Generative AI without guardrails can harm
  learning: Evidence from high school mathematics", *PNAS*, doi 10.1073/pnas.2422633122** (with a
  published correction, doi 10.1073/pnas.2518204122). Field experiment, **nearly 1,000 high-school
  maths students**, two tutors: "GPT Base" (standard ChatGPT interface) and "GPT Tutor" (prompted with
  learning safeguards). With access during practice: **+48% grades for GPT Base, +127% for GPT
  Tutor.** **When access was removed: GPT Base students performed *worse than students who never had
  access* — a 17% reduction in grades.** GPT Tutor's safeguards "largely mitigated" this. Mechanism:
  "students attempt to use GPT-4 as a **'crutch'** during practice problem sessions, and subsequently
  perform worse on their own."
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/ — `MEASURED-RCT`. **This is the most important
  negative result in AI education and it is a *design* finding, not a verdict: the same model harmed
  or helped depending entirely on whether it withheld answers.**
- **Differential harm by ability.** Randomized crossover study of four GPT-based tools (n = 195,
  ACT-derived passages): **"AI tools significantly improved comprehension in lower performing
  participants and significantly worsened comprehension in higher performing participants"**; low
  performers benefited most from the **Socratic discussion chatbot**; high performers were harmed most
  by the **summary tool**. https://doi.org/10.31234/osf.io/7mf5r — `MEASURED-RCT` (preprint). **A
  single AI pedagogy is the wrong design: the sign of the effect flips with prior attainment.**
- **The pre-LLM base rate that should temper everything above.** Kulik & Fletcher (2016), *RER*
  86(1), doi 10.3102/0034654315581420: 50 controlled evaluations of intelligent tutoring systems,
  **median effect 0.66 SD** — *but* the magnitude "depended to a great extent on whether improvement
  was measured on locally developed or standardized tests," and in two excluded groups (six
  evaluations with non-conventional control groups, four with flawed implementations) **"intelligent
  tutoring effects ... were small."**
  https://eric.ed.gov/?q=%22Effectiveness+of+Intelligent+Tutoring+Systems%22 — `MEASURED-META`.
  Machine tutoring at 0.66–0.76 predates LLMs by a decade. **The LLM contribution is coverage,
  authoring cost, and language flexibility — not a step change in effect size.**
- **The commercial-evaluation warning.** E4L downgraded "individualised instruction" three levels
  partly for "reliance on non-independent evaluations (particularly from commercial providers)."
  Every vendor claim in this space should be read against that. `MEASURED-META`.

---

## 10. The substitution test: a taxonomy of what survives

`INFERENCE` throughout this section; it is the analytical contribution rather than a finding.

Sorting the catalogue by *why* a mechanism does or does not survive replacing the human yields four
classes:

**Class A — Survives fully. The mechanism is a property of the learner's cognitive activity; the human
was only the delivery vehicle.**
Mastery gating and unlimited fresh retesting (PSI); scaffolding with contingency and fading;
worked-example modelling; deliberate practice with objective feedback; precision-teaching rate
measurement; productive-failure task sequencing; retrieval/articulation demands; DI's
faultless-communication sequences *if validated*.

**Class B — Survives with a named casualty. The cognitive core transfers; a social or motivational
component does not.**
The tutorial (loses the arguable, fallible expert whose regard you earn); cognitive apprenticeship
(loses community of practice); reciprocal teaching (loses the rotating public leader role); the case
method (loses 79 peers disagreeing in public); learning-by-teaching (keeps the cognitive engine,
risks the protégé motivation); Socratic method (keeps questioning-instead-of-answering, loses
refutation and aporia unless deliberately engineered back in).

**Class C — Does not survive. The mechanism *is* the other human, or the physical world.**
Chavruta (needs a genuine equal with stakes who cannot be dismissed); jigsaw (needs real
interdependence); peer instruction (needs a real distribution of peer misconceptions and real
persuasion); Harkness/seminar (needs twelve prepared peers); guild apprenticeship (needs real
production with real consequences); Montessori (needs the self-correcting physical material);
Suzuki (needs the parent).

**Class D — There was no mechanism to port, because there was never a measurement.**
Waldorf, Reggio (except documentation), Sudbury/unschooling, Freirean conscientização as an
outcome, Kumon's own evidence base, the HBS case method specifically.

The diagnostic question that generates this sorting: **"if I remove the other human and the physical
objects, is the thing the learner does still the thing that caused the effect?"** For PSI, yes. For
chavruta, no. That single question does more work than any amount of enthusiasm about AI tutors.

---

## 11. The ranking table — evidence × cost reduction × mechanism survival

Scoring, all `INFERENCE` from the evidence cited above:

- **Evidence (E), 0–5:** 5 = multiple large meta-analyses, survives bias/design checks; 3 = solid
  meta-analytic support with major moderators; 1 = thin or single-discipline; 0 = none.
- **Cost reduction AI provides (C), 0–5:** 5 = the dominant historical cost was expert
  attention-minutes and/or assessment labour; 0 = the dominant cost was materials, peers, or
  institutional permission.
- **Mechanism survival (S), 0–5:** 5 = Class A; 3 = Class B; 1 = Class C with a useful auxiliary role;
  0 = Class C/D with none.
- **Priority = E × C × S** (max 125). Build order is descending priority.

| # | System | E | C | S | **Score** | Why it lands there |
|---|---|---|---|---|---|---|
| 1 | **Keller Plan / PSI (mastery + unit gating + unlimited fresh retests + proctor)** | 4 | 5 | 5 | **100** | Died documented-ly of administrative labour and proctor cost — the two things AI zeroes. Structural mechanism, no human required. Flagship vindication of the thesis. |
| 2 | **Scaffolding (contingency → fading → transfer)** | 5 | 5 | 4 | **100** | ḡ = 0.46 measured *specifically for computer-based* scaffolding across 144 studies; effect robust to design details. The only entry where the AI version is what was measured. |
| 3 | **Cognitive apprenticeship (6 methods)** | 3 | 5 | 5 | **75** | Best structural match for an AI tutor; all six methods are attention-minutes. Evidence is compositional, not packaged — score capped for that. |
| 4 | **Direct Instruction (Engelmann)** | 5 | 3 | 4 | **60** | Best-evidenced system here (328 studies, no bias signature) but was blocked by *ideology*, not cost. AI's real edge: it has no professional identity to offend. Score docked because validated sequences are the effect and cannot be generated on the fly. |
| 5 | **Mastery learning correctives (Bloom LFM)** | 3 | 5 | 4 | **60** | Cheap (+5 months, $236/pupil) but LOW security and Slavin's standardized-test null. Correctives are pure attention-minutes. Must be evaluated on assessments the system didn't author. |
| 6 | **One-to-one tutoring / the tutorial** | 5 | 5 | 2 | **50** | 0.37–0.79 SD measured; $1,625/pupil/block is the highest cost in the catalogue. Substitution loses the fallible arguable expert — the tutorial's status engine. |
| 7 | **Learning by teaching / protégé effect** | 3 | 4 | 4 | **48** | g = 0.43 for tutors, <$80/pupil, HIGH security for peer tutoring. The tutee's authenticity matters least of any social mechanism. Most under-built high-ratio option. |
| 8 | **Productive failure (PS-I)** | 4 | 4 | 3 | **48** | g = 0.36 (0.87 bias-corrected) over 53 studies. Requires deliberately withholding help — the exact opposite of default AI behaviour, and the Bastani result shows what happens otherwise. Reverses for grades 2–5 and domain-general skills. |
| 9 | **Enhanced/assisted discovery (Alfieri's positive arm)** | 5 | 4 | 2 | **40** | d = +0.30, and its four active ingredients (feedback, worked examples, scaffolding, elicited explanations) are all cheap now. Low S because the "discovery" framing keeps collapsing back into the d = −0.38 unassisted version. |
| 10 | **Socratic method / elenchus** | 2 | 5 | 3 | **30** | Huge cost relief, no meta-analysis, and the mechanism (refutation, aporia) is the part LLMs are worst at. Best measured signal: helps low performers, harms high performers. Where LessonOrca and Guided Learning are betting. |
| 11 | **Precision teaching / frequency building** | 2 | 5 | 3 | **30** | Pure measurement labour, trivially automatable, mechanism intact — but only 11 studies / 170 participants. Highest ratio of *neglect* to *feasibility* in the catalogue. |
| 12 | **Deliberate practice** | 2 | 4 | 3 | **24** | Cost relief and mechanism survival both good; **E docked hard** because the ceiling is low — 18% of variance in sports, **1% among elites**. Optimizing practice volume optimizes a weak variable. |
| 13 | **Flipped classroom** | 3 | 4 | 2 | **24** | 114 studies: *small* positive on learning, **no** effect on satisfaction; pays only when contact hours are **not** cut and quizzes **are** added. AI kills video-production cost and can enforce pre-work — but flipping is a schedule, not a pedagogy. |
| 14 | **Problem/project-based learning (as *repaired*)** | 3 | 3 | 2 | **18** | PjBL d+ = 0.71 vs lecture, but PBL trends negative on knowledge and pools at d_w = 0.13 (Q ≈ 954). The AI claim is not "cheaper PBL" but "PBL plus on-demand explicit instruction," i.e. converting it into the enhanced-discovery arm. |
| 15 | **Case method / case-based learning** | 2 | 3 | 2 | **12** | Authoring cost genuinely relieved; SMD > 2 from 7 studies is not credible; the public-disagreement engine doesn't transfer. |
| 16 | **Competency-based education / mastery grading** | 1 | 3 | 3 | **9** | Blocked by accreditation, credit hours and transcripts — permission, not cost. E4L individualised instruction (+4 months, LIMITED, commercial-evaluation contamination) is the honest base rate. |
| 17 | **Peer instruction (Mazur)** | 5 | 1 | 1 | **5** | Excellent evidence (⟨g⟩ 0.23→0.48; 0.47 SD over 225 studies), nearly free already, and the mechanism is *real peers persuading each other*. AI's role is ConcepTest authoring and misconception analysis, full stop. |
| 18 | **Reciprocal teaching** | 3 | 2 | 1 | **6** | Three documented nulls (standardized tests, below-average students, without prior explicit instruction). The rotating public leader role is the engine. Explicitly **not** the right build for struggling readers. |
| 19 | **Jigsaw / cooperative learning** | 4 | 1 | 1 | **4** | +5 months at $20/pupil, but digital delivery already measured *lower* (+3). Interdependence cannot be simulated. AI orchestrates; it does not participate. |
| 20 | **Harkness / Socratic seminar / Paideia** | 1 | 1 | 1 | **1** | No controlled evidence; the expensive input is twelve prepared peers, which AI cannot supply. AI's contribution is guaranteeing preparation. |
| 21 | **Chavruta** | 1 | 0 | 1 | **0** | Already cheap; lost to culture and text-structure, not economics; needs a genuine equal with stakes. AI supplies objections, not a partner. |
| 22 | **Montessori** | 3 | 1 | 0 | **0** | Positive meta-analytic verdict but largest effects in *private* settings; the best RCT (Courtier) is null on math, EF and social skills. The self-correcting physical material *is* the mechanism. |
| 23 | **Guild apprenticeship** | 2 | 2 | 0 | **0** | Real production with real consequences. Simulated stakes are not stakes. |
| 24 | **Suzuki / Kumon** | 1 | 5 | 1 | **5** | Trivially automatable, essentially unevidenced independently. Port PSI's evidence to Kumon-shaped products, not Kumon's. Suzuki needs the parent. |
| 25 | **Waldorf / Reggio / Sudbury / unschooling / Freirean pedagogy** | 0 | — | — | **0** | No measured mechanism to port. Include as case studies in how traditions persist without evidence (Reggio's *documentation* practice is the one narrow exception AI genuinely serves). |

### The build order this implies

1. **PSI's spine** — prerequisite graph, high mastery bar (80–90%), unlimited retests on *freshly
   generated* equivalent items, immediate certification, full records. Plus external pacing pressure,
   because self-pacing is a documented failure mode of both PSI *and* AI tutors, and E4L states
   mastery learning is "much less effective when students work at their own pace."
2. **Scaffolding as the interaction law** — contingency, and above all **fading**. This is the only
   mechanism whose *computer-based* version is directly meta-analytically validated (ḡ = 0.46).
3. **Cognitive apprenticeship as the architecture** — modelling, coaching, scaffolding, articulation,
   reflection, exploration as six named subsystems, with reflection implemented as
   learner-trace-vs-expert-trace comparison (cheap for a machine, near-impossible for a teacher).
4. **DI's discipline where content is hierarchical and learners are struggling** — faultless
   communication, placement, high response rate per minute, mastery gating. With the caveat that
   generated sequences are not validated sequences.
5. **Withholding, by construction** — productive failure before instruction, and Bastani-style
   guardrails against crutch use. The single highest-leverage safety property in AI tutoring.
6. **Learning-by-teaching to a machine protégé** — cheap, g ≈ 0.43 on the tutor, and the least
   damaged by substitution of any social mechanism.
7. **Precision-teaching-style rate measurement** as the telemetry layer, because it is free for
   software and nobody is doing it.
8. **AI as orchestrator, not participant, for everything in Class C** — ConcepTest authoring for peer
   instruction, jigsaw partitioning and free-rider detection, seminar preparation, chavruta partner
   matching and objection stress-testing.

---

## 12. Where the thesis fails — the honest accounting

Five failure modes, each with a named example:

1. **Some systems lost on evidence, not cost.** Group-based mastery learning showed "essentially no
   evidence" on standardized measures (Slavin 1987). Unassisted discovery is *negative* (d = −0.38,
   Alfieri 2011). PBL trends negative on knowledge acquisition (Dochy 2003) and pools at d_w = 0.13
   with Q ≈ 954 (Walker & Leary 2009). Reciprocal teaching is non-significant on standardized tests
   and for below-average students. **AI cannot make a null result affordable.**

2. **Some systems lost on ideology and political economy, which money does not fix.** Direct
   Instruction won the largest educational experiment ever run, costs ~$20 per student workbook, and
   was sidelined for scripting, teacher autonomy, and a dissemination apparatus that recommended
   unvalidated alternatives. Competency-based education is blocked by credit hours and accreditation.
   Standards-based grading is blocked by transcripts and admissions. **These are permission
   constraints, and AI has no purchase on them.**

3. **Some mechanisms are constitutively human or physical.** Chavruta, jigsaw, peer instruction,
   Harkness, guild apprenticeship, Montessori's materials, Suzuki's parent. For these the correct AI
   role is orchestration, and the measured warning is already on the record: E4L finds
   technology-mediated collaborative learning delivers **+3 months against +5 for the in-person
   version.** Digitizing a social mechanism has a measured cost.

4. **Some systems were never measured at all, and "affordable" is not the missing ingredient.**
   Waldorf, Reggio, Sudbury, unschooling, Kumon, the HBS case method, the Oxbridge tutorial as such.
   Building an AI version does not create an evidence base; it creates an unevidenced product with a
   prestigious name.

5. **The cost-relief itself introduces new failure modes that the historical versions did not have.**
   The Bastani PNAS result is the proof: the same GPT-4, with and without guardrails, either
   preserved learning or produced a **17% deficit relative to never having had access.** Cheap help
   is not a free good. And the differential-ability finding (AI tools help low performers, *harm* high
   performers) means the sign of the effect depends on the learner. **Historical pedagogies were
   rate-limited by cost; AI pedagogies are rate-limited by discipline, and discipline is harder to
   buy.**

The steelmanned version of the thesis, which I think survives:

> **A specific and identifiable subset of well-evidenced pedagogies — those whose cost was expert
> attention-minutes and assessment labour rather than materials, peers, or institutional permission —
> has just become 100–1000× cheaper. That subset is PSI, mastery correctives, scaffolding, cognitive
> apprenticeship coaching, and rate-based fluency measurement. The correct programme is to rebuild
> those with fidelity to the features that produced the effect sizes, evaluate on assessments the
> system did not author, and engineer withholding as a first-class feature. Everything else in the
> catalogue is either an orchestration opportunity, an unevidenced tradition, or a measured null.**

---

## 13. Consolidated documented nulls and negative results

The brief required at least one. Here are eleven, all `MEASURED-META` or `MEASURED-RCT`:

| Finding | Source |
|---|---|
| Group-based mastery learning: **"essentially no evidence"** of effect on standardized achievement; positive only on experimenter-made measures, not maintained over time | Slavin 1987, *RER* 57(2), doi 10.3102/00346543057002175 |
| Unassisted discovery learning: **d = −0.38 [−0.44, −0.31]** *favouring explicit instruction*, 580 comparisons | Alfieri et al. 2011, doi 10.1037/a0021017 |
| PBL: **"tendency to a negative effect ... on student knowledge"** | Dochy et al. 2003, doi 10.1016/S0959-4752(02)00025-7 |
| PBL pooled **d_w = 0.13 ± 0.025** with Q = 954.27 (i.e. uninterpretable heterogeneity) | Walker & Leary 2009, ERIC |
| Reciprocal teaching: **non-significant on standardized tests**; **non-significant for below-average students**; weak without prior explicit strategy instruction | Rosenshine & Meister, 19-study review, ERIC |
| Peer instruction vs conventional group work, RCT n = 186: **no difference in total test scores** | doi 10.1152/advan.00045.2021 |
| Montessori RCT (preregistered, French public schools): **null on math, executive function and social skills**; reading only (d = 0.68) | Courtier et al. 2021, ERIC |
| Deliberate practice explains **18% of variance in sports, 1% among elite performers**; elite athletes did not start younger | Macnamara, Moreau & Hambrick 2016, doi 10.1177/1745691616635591 |
| Productive failure **reverses** (favours instruction-first) for grades 2–5 and for domain-general skills | Sinha & Kapur 2021, doi 10.3102/00346543211019105 |
| Human tutoring is **d = 0.79, not 2.0**; ITS 0.76 — the 2-sigma belief did not replicate | VanLehn 2011, ERIC |
| **Unfettered GPT-4 access reduced later unassisted exam performance by 17%** vs never having had access | Bastani et al. 2025, *PNAS*, doi 10.1073/pnas.2422633122 |
| AI study tools **significantly worsened comprehension in higher-performing readers** (crossover RCT, n = 195) | doi 10.31234/osf.io/7mf5r |
| ITS effects were **"small"** in evaluations with non-conventional controls or flawed implementations | Kulik & Fletcher 2016, doi 10.3102/0034654315581420 |
| Technology-mediated collaborative learning: **+3 months vs +5** for in-person | Evidence for Learning toolkit |
| Small-group learning in medical education: the call for widespread implementation **"is not supported"** on re-examination | ERIC, re-examination of Springer, Stanne & Donovan 1999 |

---

## 14. Sources

**Meta-analyses and systematic reviews**
1. Stockard et al. 2018, Direct Instruction — https://doi.org/10.3102/0034654317751919 · https://eric.ed.gov/?id=EJ1194248
2. Kulik, Kulik & Bangert-Drowns 1990, mastery learning — https://doi.org/10.3102/00346543060002265
3. Kulik, Kulik & Cohen 1979, PSI — https://doi.org/10.1037/0003-066x.34.4.307
4. Slavin 1987, Mastery Learning Reconsidered — https://doi.org/10.3102/00346543057002175
5. Kulik & Kulik 1987, mastery testing (49 studies) — ERIC
6. Meta-analysis of instructional systems in science teaching (130 studies, 341 ES) — ERIC
7. Adams & Engelmann 1996, 25 Years Beyond DISTAR — ERIC
8. DI in special education (25 studies) — ERIC
9. Bloom 1984, The 2 Sigma Problem — https://doi.org/10.3102/0013189x013006004
10. VanLehn 2011, human vs computer tutoring — ERIC
11. Kulik & Fletcher 2016, ITS — https://doi.org/10.3102/0034654315581420
12. Nickow, Oreopoulos & Quan 2020, tutoring — https://www.nber.org/papers/w27476
13. Alfieri et al. 2011, discovery learning — https://doi.org/10.1037/a0021017
14. Kirschner, Sweller & Clark 2006 — https://doi.org/10.1207/s15326985ep4102_1
15. Kirschner, Sweller & Clark 2007, reply — https://doi.org/10.1080/00461520701263426
16. Belland et al. 2017, computer-based scaffolding — https://doi.org/10.3102/0034654316670999
17. Van de Pol, Volman & Beishuizen 2010, scaffolding review — https://doi.org/10.1007/s10648-010-9127-6
18. Randolph et al. 2023, Montessori (Campbell) — https://doi.org/10.1002/cl2.1330
19. Dochy et al. 2003, PBL — https://doi.org/10.1016/s0959-4752(02)00025-7
20. Gijbels et al. 2005, PBL from the angle of assessment — https://doi.org/10.3102/00346543075001027
21. Walker & Leary 2009, PBL across disciplines — ERIC
22. Albanese & Mitchell 2000, PBL little effect — https://doi.org/10.1046/j.1365-2923.2000.00753.x
23. Chen & Yang 2019, project-based learning — https://doi.org/10.1016/j.edurev.2018.11.001
24. STEM integration meta-analysis 2025 (79 ES, g = 0.661; inquiry > problem > design > project) — ERIC
25. Sinha & Kapur 2021, productive failure — https://doi.org/10.3102/00346543211019105
26. Kapur 2016, productive failure/success taxonomy — https://doi.org/10.1080/00461520.2016.1155457
27. Macnamara, Hambrick & Oswald 2014 — https://doi.org/10.1177/0956797614535810
28. Corrigendum 2018 — https://doi.org/10.1177/0956797618769891
29. Macnamara, Moreau & Hambrick 2016, sports — https://doi.org/10.1177/1745691616635591
30. Deliberate practice in residency (10 RCTs) — https://doi.org/10.21203/rs.3.rs-2957482/v1
31. Freeman et al. 2014, active learning — https://doi.org/10.1073/pnas.1319030111
32. Hake 1998, interactive engagement — https://doi.org/10.1119/1.18809 · ERIC
33. Crouch & Mazur 2001, Peer Instruction ten years — https://doi.org/10.1119/1.1374249
34. Rosenshine & Meister 1994, reciprocal teaching — https://doi.org/10.3102/00346543064004479
35. Rosenshine & Meister, 19 experimental studies (tech. report) — ERIC
36. Peer tutoring effect on *tutors* (16 articles, g = 0.43) — ERIC
37. Jigsaw in nurse education 2024 — https://doi.org/10.1016/j.nepr.2024.103902
38. Cooperative learning among adults (133 studies) — ERIC
39. Re-examination of Springer, Stanne & Donovan 1999 — ERIC
40. van Alten et al. 2019, flipped classroom — https://doi.org/10.1016/j.edurev.2019.05.003
41. Låg & Sæle 2019, flipped-classroom satisfaction — https://doi.org/10.1111/jcal.12421
42. Flipped classroom in college (20 studies, 0.66; by discipline 0.34–0.75) — ERIC
43. Frequency building & precision teaching systematic review 2022 (11 studies, 170 participants) — ERIC
44. CBL + PBL vs lecture in clinical medicine — https://doi.org/10.1093/postmj/qgaf220
45. CBL in pharmacy education — https://doi.org/10.1186/s12909-025-07927-9
46. ChatGPT and learning achievement (22 studies, g = 0.573) — ERIC
47. Meta-analysis of AI in education (13 studies, g = 0.86) — ERIC
48. Practice vs reciprocal teaching styles in motor learning — ERIC
49. Montessori-based activities for dementia agitation (as a caution on "Montessori" as a label) — https://doi.org/10.1097/MD.0000000000029847

**Randomized / quasi-experimental primary studies**
50. Kestin et al. 2025, AI tutoring vs active learning RCT — https://www.nature.com/articles/s41598-025-97652-6
51. Bastani et al. 2025, Generative AI without guardrails, PNAS — https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/ · https://doi.org/10.1073/pnas.2422633122
52. Correction to Bastani et al. — https://doi.org/10.1073/pnas.2518204122
53. Differential effects of GPT-based tools on comprehension (n = 195) — https://doi.org/10.31234/osf.io/7mf5r
54. Peer instruction vs conventional group work RCT (n = 186) — https://doi.org/10.1152/advan.00045.2021
55. Peer instruction and novel-problem transfer (crossover, n = 38) — https://doi.org/10.1152/advan.00060.2004
56. Courtier et al. 2021, Montessori RCT in French public schools — ERIC
57. Lillard & Else-Quest 2006, Evaluating Montessori Education — https://doi.org/10.1126/science.1132362
58. National RCT of public Montessori preschools (24 sites, lottery) — ERIC
59. Dialogic Teaching efficacy trial (EEF, 76 schools, ~4,958 pupils) — ERIC
60. Nigeria after-school generative-AI tutoring RCT — https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-Transforming-learning-in-Nigeria
61. Socratic Artificial Intelligence Learning (SAIL) randomized within-subjects — https://doi.org/10.1016/j.jsurg.2024.08.006
62. Funnix Beginning Reading randomized study (DI, high-school-aged tutors) — ERIC
63. DI longitudinal maths evaluation, >2,000 low-income children — ERIC

**Cost, mechanism and institutional sources**
64. Evidence for Learning / EEF toolkit — mastery learning — https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/mastery-learning
65. — one-to-one tuition — https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/one-to-one-tuition
66. — individualised instruction — https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/individualised-instruction
67. — peer tutoring — https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/peer-tutoring
68. — collaborative learning approaches — https://evidenceforlearning.org.au/education-evidence/teaching-learning-toolkit/collaborative-learning-approaches
69. Keller Plan features and decline — https://en.wikipedia.org/wiki/Keller_Plan
70. Mastery learning, LFM vs PSI — https://en.wikipedia.org/wiki/Mastery_learning
71. Direct instruction: mechanism, evidence, adoption barriers, materials costs — https://en.wikipedia.org/wiki/Direct_instruction
72. Project Follow Through: scale, results, House et al. critique, dissemination aftermath — https://en.wikipedia.org/wiki/Project_Follow_Through
73. Socratic method: elenchus, aporia, maieutic — https://en.wikipedia.org/wiki/Socratic_method
74. Chavruta mechanism — https://en.wikipedia.org/wiki/Chavruta
75. Tutorial system (Oxford/Cambridge) — https://en.wikipedia.org/wiki/Tutorial_system
76. Cognitive apprenticeship methods — https://en.wikipedia.org/wiki/Cognitive_apprenticeship · https://doi.org/10.4324/9781315044408-14
77. Peer instruction protocol — https://en.wikipedia.org/wiki/Peer_instruction
78. Reciprocal teaching — https://en.wikipedia.org/wiki/Reciprocal_teaching
79. Montessori education research and criticisms — https://en.wikipedia.org/wiki/Montessori_education
80. Waldorf education: evidence status and documented harms — https://en.wikipedia.org/wiki/Waldorf_education
81. Sudbury school: governance and absence of outcome data — https://en.wikipedia.org/wiki/Sudbury_school
82. Kumon mechanism and evidence — https://en.wikipedia.org/wiki/Kumon
83. Suzuki method mechanism — https://en.wikipedia.org/wiki/Suzuki_method · https://doi.org/10.1177/0255761419859628
84. Deliberate practice and the 10,000-hour claim — https://en.wikipedia.org/wiki/Practice_(learning_method)
85. Google Guided Learning / LearnLM announcement, 6 Aug 2025 — https://blog.google/outreach-initiatives/education/guided-learning/
86. LessonOrca product claims — https://lessonorca.com

**Method notes.** ERIC (`api.ies.ed.gov/eric/`) supplied full abstracts for the education literature
and was the workhorse; Crossref supplied DOIs, venues and citation counts; Europe PMC supplied full
abstracts for the biomedical- and PNAS-indexed items; Unpaywall was used to locate open PDFs;
`pdftotext` was used to extract the Crouch & Mazur data table and the Kestin results. Semantic
Scholar, OpenAlex and arXiv were rate-limited or budget-exhausted during this pass; WebSearch was
unavailable. Publisher sites (SAGE, Wiley, Taylor & Francis, PNAS HTML, ScienceDirect) returned
403/402 to automated fetching. Two figures originally flagged as unverified — van Alten et al.'s
flipped-classroom result and Chen & Yang's PjBL d+ = 0.71 — were subsequently recovered from
Semantic Scholar abstracts and are now sourced. **Three items remain unverified against primary text
and should be confirmed before publication: (a) the "PSI ≈ 0.5 SD on final exams" figure (the 1979
*American Psychologist* abstract states direction and variance reduction but no magnitude); (b)
Stockard et al.'s per-subject pooled effect estimates (the ~0.6 SD headline comes from a secondary
summary, not the RER text); (c) the specific numbers in Bloom (1984) — the JSTOR-hosted PDF retrieved
contained only the citation apparatus, so "2 sigma" should be cited as a claim in a 1984 review, not
as a replicated estimate.**
