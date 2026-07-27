---
title: "Embodiment, Manipulatives and the Physical (F7) · Reactive & Executable Notebooks (A3) — What Happens When Learning Leaves the Chat Box"
wave: F
date_researched: 2026-07-27
sources_count: 84
---

# F7 + A3 — Two halves of one question

> **The shared question.** Both halves of this report ask what changes when the learner
> stops *reading a response* and starts *manipulating an object*. F7 asks it of physical
> objects — blocks, hands, robots, headsets. A3 asks it of computational objects —
> notebooks whose state recomputes when you touch it. The answers turn out to rhyme:
> **the manipulable thing helps when it constrains what the learner can do, and stops
> helping — or starts hurting — when it merely adds sensation.**
>
> **Deliverables.** §A8 is a decision rule for when a concept needs a physical object,
> when a simulation suffices, and when neither helps. §B6 is a substrate recommendation
> for browser-runnable per-chapter mini-apps with the measured limits stated. §C is the
> negative-results register — **eleven documented nulls, reversals and failed
> replications**, against a required minimum of three.
>
> **Two original measurement suites were built and run for this report** (§B1.3, §B5.2)
> and both are reproducible from the commands given.

---

# PART A — F7 · EMBODIMENT, MANIPULATIVES, AND THE PHYSICAL

## A0. The frame, and the number that sets it

Report **I1** established the cost decomposition that makes this section urgent. AI
collapses **two of seven** cost components to near zero (expert attention-minutes,
assessment labour), substantially reduces two more (authoring, record-keeping), and does
**nothing at all** to three: **physical materials and space, genuine peers with real
stakes, and institutional permission**. F7 owns the first of those three.

I1 also supplied the diagnostic this section must survive:

> **"If I remove the other human and the physical objects, is the thing the learner does
> still the thing that caused the effect?"**

I1 answered **no** for Montessori and scored it `S = 0` — *"the self-correcting physical
material **is** the mechanism… A screen version of the pink tower is not a cheaper pink
tower; it is a different intervention with its own (much weaker) evidence base."* That
verdict is the strongest claim in the project against digital substitution, and this
section's job is to test how far it generalises.

**It does not generalise.** The measured literature says something narrower and much more
useful: *physical presence is worth about **0.2 SD**, and that premium is spent quickly
on extraneous load.* The rest of this part is the evidence, and §A8 is what to build.

**A note on how to read every effect size below.** Kraft (2020, *Educational Researcher*,
doi:10.3102/0013189x20912798, 967 citations) `MEASURED-META` shows that Cohen's
benchmarks badly overstate what is achievable in field education research; effects that
are "small" by Cohen are large relative to actual interventions. Any pooled *d* above
~1.0 for an instructional-media comparison in a K–12 setting should be treated as a
diagnostic of the synthesis, not a finding about the technology. This rule fires four
times below.

---

## A1. Embodied cognition in learning: gesture, enactment, and the replication problem

### A1.1 Gesture — the one embodiment result with a real meta-analysis

`MEASURED-META` · **Dargue, Sweller & Jones (2019), "When our hands help us understand: A
meta-analysis into the effects of gesture on comprehension," *Psychological Bulletin*,
doi:10.1037/bul0000202, 150–156 citations.** **83 independent samples**, each comparing
comprehension when gesture accompanied speech against speech alone.

Verbatim findings:

> *"Across all samples, gesture had a **moderate, beneficial effect on comprehension**
> when either produced or observed by a learner. Further stratified tests revealed that
> gestures significantly benefitted comprehension under a variety of circumstances,
> dependent on the type of gesture used, the information provided by gesture, the
> function of the gesture, the age of the learner, and the way comprehension was
> measured. **The function of the gesture moderated the magnitude of the effect, with
> studies investigating the effect of producing gestures on comprehension yielding
> significantly larger effect sizes on average than studies investigating the effect of
> observing gestures.**"*

`UNVERIFIED-IN-SESSION` — **the pooled point estimate itself.** The paper is closed access
(Unpaywall `is_oa: false`); Semantic Scholar and Crossref return the abstract without the
numeric estimate; PubMed 31219263 carries the same text. **The magnitude is characterised
by the authors as "moderate" and this report will not assert a number it could not
retrieve.** The *ordinal* finding — **producing > observing** — is directly stated and is
the one that matters for design.

### A1.2 The result that actually decides F7: gesture beats acting on objects

`MEASURED-RCT` · **Novack, Congdon, Hemani-Lopez & Goldin-Meadow (2014), "From action to
abstraction: using the hands to learn math," *Psychological Science*,
doi:10.1177/0956797613518351, PMID 24503873, 178+ citations.** Third-graders learned one
strategy for mathematical-equivalence problems, instantiated three ways: **(a) a physical
action performed on objects**, **(b) a concrete gesture miming that action**, **(c) an
abstract gesture**. Verbatim:

> *"**All three types of hand movements helped children learn how to solve the problems
> on which they were trained. However, only gesture led to success on problems that
> required generalizing the knowledge gained.** The results provide the first evidence
> that **gesture promotes transfer of knowledge better than direct action on objects**
> and suggest that the beneficial effects gesture has on learning may reside in the
> features that differentiate it from action."*

Goldin-Meadow's own theoretical restatement (*Developmental Review* 2015,
doi:10.1016/j.dr.2015.07.007, PMID 26692629) `OBSERVED`:

> *"**Gesture is, in fact, a special kind of action in that it represents the world rather
> than directly manipulating the world (gesture does not move objects around).** …gesture
> is able to **highlight components of an action that promote abstract learning while
> leaving out details that could tie learning to a specific context.**"*

`MEASURED-RCT` · The 2026 neural replication (*Journal of Cognitive Neuroscience*,
doi:10.1162/jocn.a.2588, PMID 41870303) ran the same contrast with **fNIRS on 73 children
aged 8–10** and found gesture-based instruction — the V-shaped hand under "4 + 2" —
produced *greater intersubject neural synchrony in motor cortex and right angular gyrus*
than **action-based instruction in which the teacher physically manipulated magnetic
numbers to mimic the same gestures**, and *"synchrony in the right angular gyrus during
gesture instruction predicted learning gains, whereas synchrony during action-based
instruction did not."*

**This is the single most important finding in Part A, and it points the opposite way
from the intuition F7 was commissioned to test.** The abstract, non-manipulative hand
movement beat the physical manipulation of real objects — twice, behaviourally and
neurally — precisely *because* it stripped the object away. Physicality is not the active
ingredient; **representational compression is**, and gesture is the cheapest available
form of it.

### A1.3 The aptitude–treatment interaction, and the first documented reversal

`MEASURED-RCT` — **NEGATIVE RESULT N1** · *Cognitive Science* 2024,
doi:10.1111/cogs.13479, PMID 38980965. Whether a child benefits from gesture instruction
depends on whether that child *spontaneously gestured before the lesson*:

> *"For children who spontaneously gestured before instruction, both doing and seeing
> gesture led to better generalization and retention of the knowledge gained than a
> comparison manipulative action. **For children who did not spontaneously gesture before
> instruction, doing gesture was LESS effective than the comparison action for learning,
> generalization, and retention.**"*

`MEASURED-RCT` — **NEGATIVE RESULT N2** · *Applied Cognitive Psychology* 2023,
doi:10.1002/acp.4093 (Parrill, Shymanski & Cook), brain anatomy taught five ways
(image / physical model / physical model + action / hand model / hand model + action):
*"All trainings improved post-test performance. **Performance in the hand model condition
was worse compared to conditions with action.**"* — i.e. **gesture without action lost to
action in an adult anatomy task**, the mirror image of Novack's result in a different
domain.

`INFERENCE` · N1 and N2 together say the gesture literature has the same shape as the
expertise-reversal literature that **F10** documented (Tetzlaff et al. 2025: low-prior
learners *d* = 0.505 with high assistance, high-prior learners *d* = −0.428 with it).
**There is no "gesture works" fact. There is a matching problem**, and the matching
variable — spontaneous gesture rate — is *observable from video*, which §A7 makes
actionable.

### A1.4 Enactment / subject-performed tasks

`OBSERVED` · The enactment effect (Engelkamp, Zimmer, Cohen; *Memory & Cognition* and
*JEP:LMC* series 1994–2003, doi:10.3758/bf03209257, doi:10.1037/0278-7393.26.3.671,
doi:10.1016/s0001-6918(97)00005-x) is one of the older and more robust laboratory memory
effects: performing an action phrase ("break the toothpick") yields better free recall
than reading it. **No modern meta-analysis of the enactment effect was retrievable via
Crossref, Semantic Scholar, Europe PMC or ERIC in this session** — searches returned only
the 1990s primary literature. `UNVERIFIED-IN-SESSION` for any pooled magnitude.

`INFERENCE` · The enactment literature also has a structural limitation for education
that is rarely stated: **its dependent variable is free recall of action phrases**, not
transfer of a principle. Engelkamp & Dehn's own work is on *item and order information*.
The construct it establishes is a memory-encoding advantage, not an understanding
advantage — and Novack (§A1.2) is the direct test of whether the advantage survives to
generalisation. It did not.

### A1.5 The replication problem, reported rather than elided

The brief asked for scepticism. Here it is, with the specific cases.

`OBSERVED` · **Machery, "The Replication Crisis in Embodied Cognition Research," in *The
Routledge Handbook of Embodied Cognition* (2024), doi:10.4324/9781003322511-50.** A
dedicated handbook chapter on the replication crisis *inside* embodied cognition now
exists — the field's own reference work concedes the problem. Machery's methodological
companion, *"What is a replication?"* (doi:10.31234/osf.io/8x7yn), argues *"the common
notion of conceptual replication is confused"* — which matters because embodied-cognition
defences characteristically appeal to conceptual replications.

`OBSERVED` · **de Zubicaray (2026), "Modelling in the midst of a replication crisis for
embodied action semantics," *Language, Cognition and Neuroscience*,
doi:10.1080/23273798.2026.2683465** — a 2026 commentary that treats the crisis in embodied
*action semantics* as an established premise rather than a claim to be argued.

`MEASURED-RCT` — **NEGATIVE RESULT N3, and the most instructive one** ·
**Mueller & Oppenheimer (2014), "The Pen Is Mightier Than the Keyboard," *Psychological
Science*, doi:10.1177/0956797614524581, 771 citations** is the most-cited
"physical-act-beats-digital-act" finding in all of education. **Morehead, Dunlosky &
Rawson (2019), *Educational Psychology Review*, doi:10.1007/s10648-019-09468-2, ERIC
EJ1225471** ran the direct replication and extended it with eWriter and *no-notes*
groups. Verbatim:

> *"Some trends suggested longhand superiority; however, **performance did not
> consistently differ between any groups (experiments 1 and 2), including a group who did
> not take notes (experiment 2)**. Group differences were further decreased after students
> studied their notes. **A meta-analysis (combining direct replications) of test
> performance revealed small (nonsignificant) effects favoring longhand.** Based on the
> present outcomes and other available evidence, **concluding which method is superior
> for improving the functions of note-taking seems premature.**"*

Note also that the original carries a **Corrigendum** (*Psychological Science* 2018,
doi:10.1177/0956797618781773). `OBSERVED`

`MEASURED-RCT` · The counterweight, so this is not one-sided: **Longcamp,
Zerbato-Poudou & Velay (2005), *Acta Psychologica*, doi:10.1016/j.actpsy.2004.10.019, 414
citations** — preschoolers trained on letters by handwriting vs typing; *"in the older
children, the handwriting training gave rise to a **better letter recognition** than the
typing training."* **Motor learning of a specific visual-motor form is a real and
replicated effect. Motor learning as a general study technique is not.** The distinction
runs through every result in Part A.

---

## A2. Physical vs virtual manipulatives — the head-to-head, honestly reported

### A2.1 The two anchor syntheses

`MEASURED-META` · **Carbonneau, Marley & Selig (2013), "A meta-analysis of the efficacy of
teaching mathematics with concrete manipulatives," *Journal of Educational Psychology*,
doi:10.1037/a0031084, 337 Crossref / 499 S2 citations, ERIC EJ1007941.**

| Parameter | Value |
|---|---|
| Studies | **55**, comparing manipulatives against instruction using **only abstract math symbols** |
| Participants | **N = 7,237**, kindergarten → college |
| Overall | *"Statistically significant results… with **small to moderate effect sizes**, as measured by Cohen's d, in favor of the use of manipulatives"* |
| Retention | k = 53, N = 7,140 — **"moderate to large"** |
| Problem solving | k = 9, N = **477** — **"small"** |
| Transfer | k = 13, N = 3,453 — **"small"** |
| Justification | k = 2, N = **109** — **"small"** |
| Moderation | *"moderated by both instructional and methodological characteristics of the studies"* |

`UNVERIFIED-IN-SESSION` — **exact d values.** The paper is closed (Unpaywall
`is_oa: false`; S2 `openAccessPdf: CLOSED`; no ERIC full text). A single 2024 citing
paper reports *"0.59 for retention and 0.46 for problem-solving"*, which **contradicts the
ERIC abstract's own characterisation of problem solving as "small."** That contradiction
is reported rather than resolved. **Cite the pattern, not the point estimates.**

The pattern is what matters anyway, and it is stark: **the outcome with k = 53 is the one
where manipulatives win most, and it is *retention*. The outcomes that describe
understanding — problem solving (k = 9), transfer (k = 13), justification (k = 2) — are
small and thinly evidenced.** Manipulatives are best supported exactly where §A1.4 said
enactment lives: memory, not generalisation.

`MEASURED-META` · **Moyer-Packenham & Westenskow (2013), "Effects of Virtual Manipulatives
on Student Achievement and Mathematics Learning," *IJVPLE*, doi:10.4018/jvple.2013070103,
125 citations, ERIC EJ1154970**; extended in **doi:10.4018/978-1-4666-8847-6.ch009** to
**104 research reports, 46 studies, 104 effect sizes**. Result: *"**moderate effects for
VMs compared with other instructional treatments**… There were **large, moderate, and
small effects when virtual manipulatives were compared with physical manipulatives**,
textbooks, and examined by mathematical domains, grade levels, study duration, study
quality, year of study publication, and study size."*

`OBSERVED` · The five affordances the authors extract are the most portable part of the
paper and are directly implementable in a browser: **focused constraint** (the tool
constrains attention to the mathematical object), **creative variation**, **simultaneous
linking** (representations update together), **efficient precision**, and **motivation**.
Three of the five are properties a physical block does *not* have. `INFERENCE` — **this,
not "virtual is cheaper," is the argument for virtual manipulatives: the virtual object
can be made to do things the physical object cannot, chiefly linking representations and
refusing illegal states.**

### A2.2 The best-designed head-to-head is a null

`MEASURED-RCT` — **NEGATIVE RESULT N4** · **Moyer-Packenham, Baker, Westenskow & Anderson
(2013), "A Study Comparing Virtual Manipulatives with Other Instructional Treatments in
Third- and Fourth-Grade Classrooms," *Journal of Education*,
doi:10.1177/002205741319300204**, and the companion prediction study
(doi:10.4471/redimat.2014.46). Design features, verbatim: *"1) a large number of students
(**N = 350**); 2) **within-class random-assignment** to treatment groups; 3) retention
effects measured by post-test **and delayed post-test**; 4) **fidelity of instructional
treatments documented through observations**; and 5) instrument development for the unit
of study."* Arms: classroom instruction with **texts + physical manipulatives** vs
computer-lab instruction with **virtual fraction applets**, 17 classrooms.

> *"Results revealed **no significant differences in achievement between the
> treatments.**"*

And a second-order finding worth more than the null: *"**fewer demographic predictors of
student performance (e.g., socio-economic status, English language learner status, and
gender)**"* in the virtual-manipulative condition. `MEASURED-RCT` — **the virtual arm was
not better on average; it was more equitable.** That is a different and, for this
project's SELPA-first mandate, more interesting result.

`MEASURED-RCT` — **NEGATIVE RESULT N5** · **Trory, Howland, Good & du Boulay (2026),
*ACM Transactions on Computing Education*, ERIC EJ1510953** (recovered by **F10**).
166 pupils aged 9–10, computer network structure and routing. Hypothesis H2 was *physical
concrete > virtual concrete*: **not supported. Welch t(41.7) = 1.015, p = 0.316,
M_diff = 0.47, 95% CI [−0.47, 1.41].** A direct, pre-specified, adequately reported
physical-vs-virtual null outside mathematics.

`MEASURED-RCT` · Where the two *do* differ, they differ **by sub-concept, not by
medium**: Westenskow & Moyer-Packenham (*IJTME* 2016, doi:10.1564/tme_v23.2.01), 43
fifth-grade Tier II students with mathematical learning difficulties across ten small-group
sessions — **physical favoured for 5 sub-concepts, virtual for 4, combined for 2.**

`MEASURED-META` · **Tselegkaridis, Sapounidis & Stamovlasis (2023), "Teaching electric
circuits using tangible and graphical user interfaces: A meta-analysis," *Education and
Information Technologies*, doi:10.1007/s10639-023-12164-y**, 13 citations. Conclusion:
*"the **combination** of user interfaces (tangible/graphical) appears to be the most
beneficial for students in the domain of electric circuits teaching."* `UNVERIFIED-IN-SESSION`
for the pooled magnitudes (no abstract retrievable). **Neither medium won; the
conjunction did** — the same shape as Westenskow's per-sub-concept split.

### A2.3 The one synthesis that says virtual wins — and why it should not be believed

`MEASURED-META` (**and a worked example of how to read one**) · **Masitoh & Prasetyawan
(2026), "Enhancing Mathematics Achievement through Virtual Manipulatives: A Meta-Analysis
of K–9 Intervention," *Al-Ishlah: Jurnal Pendidikan* 17(4),
doi:10.35445/alishlah.v17i4.7586.** PRISMA, 23 experimental studies 2012–2022,
random-effects via OpenMEE, control groups restricted to *either* traditional methods
*or* concrete manipulatives:

| Contrast | Cohen's d |
|---|---|
| **Overall** | **1.603**, 95% CI [0.881, 2.324], p < .001 |
| Secondary level | 1.810 |
| Primary level | 1.280 |
| **vs traditional methods** | **1.979** |
| **vs concrete manipulatives** | **1.473** |
| Heterogeneity | **I² = 97.95%** |
| Publication bias | *"not evident"* per the authors |

`INFERENCE` — **do not use these numbers, and say why.** (i) **I² = 97.95%** means
essentially all observed variance is between-study heterogeneity; a random-effects pooled
mean under that condition describes no population. (ii) A *d* of 1.47 for **virtual
beating physical manipulatives** is roughly **7× the largest credible instructional-media
effect** in this report and **~3.7× Kraft's "large" threshold** for education RCTs with
standardised outcomes. (iii) It is contradicted by the two designs with random assignment
and documented fidelity (N4, N5), both null. **This is the only pooled physical-vs-virtual
number that exists, and it is uninterpretable. The honest statement is that no
trustworthy pooled estimate of the physical-vs-virtual difference has been published.**

### A2.4 Verdict for §A2

`INFERENCE` · **Virtual does not lose.** Across the two randomised, fidelity-documented
head-to-heads it ties; across sub-concepts it splits roughly evenly; combined beats
either; and the virtual arm showed *fewer demographic predictors of performance*. The
Montessori verdict from I1 (`S = 0`) is **correct about Montessori specifically and does
not license a general claim about manipulatives**, because Montessori's mechanism is a
material that *self-corrects* — the object, not the adult, signals the error — and that
property is reproducible in software (it is Moyer-Packenham's **focused constraint**),
whereas Courtier et al. 2021's fidelity finding shows the effect lives in the *density and
sequencing of the full material set*, which is what a screen version usually drops.

**The load-bearing distinction is not physical vs virtual. It is: does the object refuse
illegal states, and does it link representations?** A pink tower refuses to stack wrong.
A fraction applet refuses to shade six-fifths. A PDF of a fraction bar refuses nothing.

---

## A3. Concreteness fading — the standing correction, carried forward

**This report reintroduces no phantom number.** Restating **F10**'s established position
because F7 would otherwise be the place someone reinvents it:

- `OBSERVED` **Fyfe, McNeil, Son & Goldstone (2014), *Educational Psychology Review*,
  doi:10.1007/s10648-014-9249-3, ERIC EJ1036777 is a SYSTEMATIC REVIEW, not a
  meta-analysis. No pooled effect size for concreteness fading exists anywhere in the
  retrievable record.** Anyone citing "the effect size of concreteness fading" is citing
  something that does not exist.
- `MEASURED-RCT` **Four-plus nulls stand**: statistical equivalence at pre-specified
  bounds d = ±0.5 (Lichtenberger, Kokkonen & Schalk 2024, *JRST*, doi:10.1002/tea.21947,
  N = 187); **multiple concrete representations actively hurt** (Bennett, Inglis & Gilmore
  2019, *JEP*, doi:10.1037/edu0000318); **richer context reliably degrades transfer** in
  two classroom experiments (Day, Motz & Goldstone 2015, *Front. Psychol.*,
  doi:10.3389/fpsyg.2015.01876); developmental moderation (Jaakkola & Veermans 2018); and
  the computing replication that went **3 of 4 hypotheses null** (Trory et al. 2026, ERIC
  EJ1510953 — H1 F(3,54) = 2.413, p = 0.077; **H2 physical > virtual not supported**;
  H3 three-step > two-step supported; **H4 five-step > three-step not supported**,
  M_diff = 0.16 [−0.78, 1.09], p = 0.738).
- `INFERENCE` **What is robust is *multiple aligned instantiations*, not concrete→abstract
  ordering.** Goldstone & Son's original result had *both* switch directions beating
  static presentation — the directional advantage is a second-order effect on top of a
  multiple-instantiation effect.

**F7's contribution to this thread** is that §A1.2 supplies an independent mechanism for
why ordering underperforms: **Novack's abstract-gesture arm beat the concrete-action arm
on transfer.** If "more concrete" were the engine, the action condition should have won.
It lost. The engine is *alignment across instantiations while surface detail is stripped*
— which is exactly Fyfe et al.'s own mechanism (4), *"fading strips extraneous concrete
properties and distills the generalizable structure"*, and none of mechanisms (1)–(3).

---

## A4. Robots and physical agents: the presence premium is ≈ 0.2 SD

### A4.1 The 2026 meta-analysis, read at the level of the control condition

`MEASURED-META` · **de Winter, Dodou, Moorlag & Broekens (2026), "Social robots: a
meta-analysis of learning outcomes," *Frontiers in Robotics and AI*,
doi:10.3389/frobt.2025.1735198, PMC13051544.** **146 studies retrieved**, physical social
robots training cognitive skills; **183 post-test effect sizes** against controls plus 372
pre-post; **78 studies with control groups** analysed. Numbers read from the full text,
not the abstract:

| Control condition | Cohen's d | SD |
|---|---|---|
| Nothing (no training) | **0.75** | 0.62 |
| Sham task | **0.38** | 0.40 |
| **Virtual interface (tablet / screen)** | **0.20** | **0.37** |
| Human teacher — overall | **0.31** | 0.70 |
| ⤷ robot **co-teaching** with a human | **0.88** | 0.68 |
| ⤷ robot **replacing** the teacher | **−0.06** | 0.40 |

Statistics: d larger for "Nothing" than for "Virtual interface" controls, **t(32) = 3.03,
p = 0.005**. Co-teaching vs robot-only, **t(43) = 5.83, p < 0.001**. In **59 of 78 (76%)**
of studies the robot was *not* accompanied by a human teacher.

Authors' own framing of the physical-embodiment question, verbatim:

> *"The paramount evaluation… involves contrasts with virtual interfaces such as tablets.
> Herein, substantiation of the incremental value of social robots remains contentious…
> **a modest but positive effect size for robots versus virtual interfaces (d = 0.20)**…
> **However, embodiment is not a panacea. Some work even reported that a physical robot
> hindered learning compared to a virtual agent** (Rosenthal-von der Pütten et al., 2016)
> **or that its engaging social features negatively correlated with learning gains,
> possibly by acting as a distraction that increases cognitive load** (Kennedy et al.,
> 2015b)."*

### A4.2 The convergence that answers the brief's question

The brief supplied the prior-project figure for on-screen pedagogical agents:
**g ≈ 0.19–0.20**. Independently verified here: `MEASURED-META` **Schroeder, Adesope &
Gilbert (2013), "How Effective are Pedagogical Agents for Learning? A Meta-Analytic
Review," *Journal of Educational Computing Research*, doi:10.2190/ec.49.1.a, 262
citations** — **43 studies, 3,088 participants**, *"a **small but significant effect** on
learning"*, larger for K-12 than post-secondary, and — a finding worth its own line —
**agents communicating with on-screen text outperformed agents communicating with
narration**.

Now place three independent literatures side by side:

| "Add presence to a screen" | Pooled effect | Source |
|---|---|---|
| On-screen pedagogical agent vs no agent | **g ≈ 0.19–0.20** | Schroeder et al. 2013 (43 studies, N = 3,088) |
| **Physical robot vs the same content on a screen** | **d = 0.20** | de Winter et al. 2026 (78 controlled studies) |
| **Immersive VR (HMD) vs less-immersive desktop / traditional** | **ES = 0.24** | Wu, Yu & Gu 2020 (35 RCT/quasi) — §A5.1 |

`INFERENCE` — **THE PRESENCE PREMIUM.** Three separate research communities, three
different technologies, three different decades of hardware, and the same answer: **adding
presence to a screen buys about 0.2 standard deviations, and it does not matter much which
kind of presence you add.** By Kraft's benchmarks that is a genuinely *large* effect for
education — and it is also **an order of magnitude smaller than the effect of the control
condition you chose**, which ranges from +0.75 to −0.06 in the *same* meta-analysis.

**Answer to the brief's question: physical presence beats screen presence for learning by
d ≈ 0.20 — real, replicated, and modest. It does not beat it by the margins the affect
literature would predict.** The brief's own prior figure — three 2024 field experiments
improving affect at **d = .85–1.01** while learning did not move — is the same dissociation
seen from the other side.

### A4.3 Three documented negatives inside the robot literature

- `MEASURED-RCT` — **NEGATIVE RESULT N6** · **Kennedy, Baxter & Belpaeme (2015), "The
  Robot Who Tried Too Hard: **Social Behaviour of a Robot Tutor Can Negatively Affect
  Child Learning**," ACM/IEEE HRI, doi:10.1145/2696454.2696457, 187 Crossref / 295 S2
  citations.** Increasing the robot's social behaviour *reduced* learning gains. Follow-up:
  *Frontiers in ICT* 2017, doi:10.3389/fict.2017.00006.
- `MEASURED-RCT` — **NEGATIVE RESULT N7** · **Kennedy, Baxter, Senft & Belpaeme (2016),
  "Heart vs hard drive: **Children learn more from a human tutor than a social robot**,"
  HRI, doi:10.1109/hri.2016.7451801**: *"Significant learning occurs in both conditions,
  but the children improve more with the human tutor. This difference is not statistically
  significant, but the effect sizes fall in line with findings from other literature
  showing that **humans outperform technology for tutoring**."*
- `MEASURED-RCT` — **NEGATIVE RESULT N8, the reversal** · **Rosenthal-von der Pütten,
  Straßmann & Krämer (2016), IVA, doi:10.1007/978-3-319-47665-0_23**, title verbatim:
  *"**Robots or agents — neither helps you more or less during second language
  acquisition**."*

### A4.4 A methodological finding that generalises past robots

`MEASURED-META` · de Winter et al. also ran an LLM-based sentiment analysis over the
papers themselves and found a **regional reporting asymmetry**: robot-vs-control effect
size was **d = 0.17 (SD 0.39, k = 36) for European studies vs d = 0.53 (SD 0.69, k = 42)
for non-European studies, t(76) = −2.74, p = 0.008**, and this survived multivariable
regression (**β = −0.37, p = 0.005**) after controlling for control-condition type.
Paper "Positiveness" scores showed the same split (**Europe M = −0.40 vs non-Europe
M = 0.32, t(144) = −4.61, p < .001**; β = −0.71, p = 0.006).

`INFERENCE` · **A 0.36-SD swing attributable to where the paper was written is larger than
the entire physical-embodiment effect it is being used to estimate.** Any effect size
under ~0.4 in the edtech literature needs a provenance moderator before it can be trusted.

### A4.5 A second 2026 robot meta-analysis, for triangulation

`MEASURED-META` · **Shu, Xie & Lin (2026), "Effects of physically embodied educational
robots on children's learning outcomes: A meta-analysis," *Acta Psychologica*,
doi:10.1016/j.actpsy.2026.106576, PMID 41850079.** **34 independent studies, N = 3,665.**
Overall **r = 0.31, 95% CI [0.24, 0.38], p < .001** (≈ *d* = 0.65 by the standard
conversion, **but note the control conditions**). Moderators: **larger effects for active
roles (collaborative / teaching-by-learning), programmable kits, interventions > 4 weeks,
and — decisively — when robots were compared with *traditional materials/tools* rather
than *human instructors or other comparison conditions***. No reliable moderation by
educational stage, country, session length, or outcome domain. Authors' CLT reading:
robots help *"when they help structure task processing and reduce avoidable cognitive
demands in well-scaffolded activities"* and gains are likelier in *"sustained, structured
learning designs rather than brief demonstration-only lessons."*

**Both 2026 meta-analyses independently identify the control condition as the dominant
moderator.** That is the finding, not the headline number.

---

## A5. VR / AR: immersion is a cost before it is a benefit

### A5.1 The pooled picture, sorted by what the control condition was

| Synthesis | Scope | Pooled effect | Control |
|---|---|---|---|
| `MEASURED-META` **Wu, Yu & Gu (2020)**, *BJET*, doi:10.1111/bjet.13023, 460 cites | **35 RCT/quasi**, 2013–2019 | **ES = 0.24** ("small") | **less-immersive desktop VR and other traditional instruction** |
| `MEASURED-META` **Villena-Taranilla et al. (2022)**, *Educational Research Review*, doi:10.1016/j.edurev.2022.100434, 254 cites | K–6 | **d = 0.65** overall; **d = 0.52** for the 5-study mathematics subset (per citing sources) `UNVERIFIED-IN-SESSION` for the primary text | mixed |
| `MEASURED-META` **Coban, Bolat & Goksu (2022)**, *Educational Research Review*, doi:10.1016/j.edurev.2022.100452, 252 cites | immersive VR, general | **magnitude UNRETRIEVABLE** — closed access; S2 returns 404 on the DOI; not in ERIC | — |
| `MEASURED-META` **Bödding, Schriek & Maier (2025)**, *Virtual Reality*, doi:10.1007/s10055-025-01118-z, 19 cites | **k = 53**, mixed reality in vocational education | **behavioural d = 0.40, cognitive d = 0.84, affective d = 0.65** | vs control |
| `MEASURED-META` **Barcenas & Prudente (2026)**, *RPTEL*, doi:10.58459/rptel.2027.22018 | 29 comparisons, 28 studies, **2,841 secondary students**, AR in science | **g = 0.98 [0.74, 1.21]**, I² = 80.67%; duration moderates (6–8 wk **g = 1.63** vs 1–3 wk **g = 0.72**) | mostly traditional |
| `MEASURED-META` **Bermoy & Orbegoso (2025)**, *IJRAMT*, doi:10.65138/ijramt.2025.v6i11.3157 | 80 studies, 6,538 participants, 27 countries | **AR g = 0.82 [0.64, 1.00]; VR g = 1.07 [0.85, 1.29]** | mostly traditional |

`INFERENCE` · **Read that table by the last column and it stops being contradictory.**
Where the control is *the same content on a less-immersive screen*, immersion is worth
**≈ 0.24**. Where the control is *"traditional instruction"* — a different lesson, a
different teacher, a different amount of attention — the effect is **four times larger**.
The technology did not change. The comparison did. This is the identical pattern to
de Winter's 0.75 → 0.20 gradient (§A4.1) and Shu's control-condition moderator (§A4.5).

### A5.2 The reversal, with a mechanism

`MEASURED-RCT` — **NEGATIVE RESULT N9** · **Makransky, Terkildsen & Mayer (2019),
"Adding immersive virtual reality to a science lab simulation causes **more presence but
less learning**," *Learning and Instruction*, doi:10.1016/j.learninstruc.2017.12.007,
**1,221 citations**.** N = 52 university students, biology lab, HMD vs desktop, with
**EEG-based cognitive-load measurement**. The title is the finding.

`MEASURED-RCT` — **NEGATIVE RESULT N10** · **Makransky & Petersen (2020), "Cognitive and
affective processes for learning science in immersive virtual reality," *JCAL*,
doi:10.1111/jcal.12482, 315 citations**, verbatim:

> *"Those who viewed the IVR lesson **performed significantly worse on transfer tests,
> reported higher emotional arousal, reported more extraneous cognitive load and showed
> less engagement based on EEG measures** than those who viewed the slideshow lesson,
> **with or without practice questions added to the lessons.**"*

`MEASURED-RCT` · **Parong & Mayer (2018), "Learning science in immersive virtual reality,"
*JEP*, doi:10.1037/edu0000241, 898 citations** — the same direction. And
`MEASURED-META` · **Makransky, Andreasen, Baceviciute & Mayer (2021), *JEP*,
doi:10.1037/edu0000473, 293 citations**, title verbatim: *"Immersive virtual reality
**increases liking but not learning** with a science simulation, and generative learning
strategies promote learning in immersive virtual reality."*

The literature has a name for it: **the "immersion paradox" — increased presence in VR
produced higher cognitive load and reduced knowledge retention** (as restated by a 2026
citing review).

`MEASURED-META` — **NEGATIVE RESULT N11, and the cleanest one in the section** ·
**Bödding, Schriek & Maier (2025), doi:10.1007/s10055-025-01118-z**, k = 53. The main
effects (d = 0.40 / 0.84 / 0.65) hold when the control has *equal training content*
(d = 0.40 / 0.68 / 0.71). **But in the subset where two MR conditions were compared
against each other — i.e. where medium is the only thing that varies —**

> **d_behavioural = 0.04, d_cognitive = −0.31, d_affective = −0.51.**

**When you strip out content, novelty and attention and vary only the degree of immersion,
the cognitive and affective effects go negative.** This is the meta-analytic form of
Makransky's single-study reversal, and it is the finding that should govern any decision
to build in VR.

### A5.3 Where immersion genuinely earns its cost

`MEASURED-META` · **Haptic/VR in orthodontic training, 9 studies, g = 1.40 [0.82, 1.98],
I² = 77.3%** (*Frontiers in Oral Health* 2026, doi:10.3389/froh.2026.1768079, PMID
42344783) — *"appear valuable for improving **psychomotor learning and procedural
planning**, whereas translation to direct patient-care benefits remains"* limited.
`MEASURED-META` Bödding's **behavioural** outcomes in vocational training survive the
equal-content control (d = 0.40) where cognitive ones collapse.

`INFERENCE` · **The pattern is exactly Longcamp vs Mueller-Oppenheimer (§A1.5) one level
up.** Immersion pays when the *target skill is itself sensorimotor and spatial* — suturing,
bracket bonding, assembly, spatial navigation. It does not pay, and reverses, when the
target is conceptual and the immersion is decoration. **The dependent variable decides,
not the technology.**

---

## A6. The SELPA angle: sensory, motor, and who embodiment actually costs

**H1 was read first, as instructed.** Its content on this exact question is thin, and that
is itself a finding worth recording: **H1 contains essentially nothing on motor
impairment, switch access, occupational therapy, dexterity, or sensory overload.** It
records its own gap: *"Autism-specific instructional research (e.g. NPDC/NCAEP
evidence-based practice reviews) is under-covered here."* F7 fills part of it.

### A6.1 The first thing to say: physical manipulation is an access barrier

`INFERENCE` — and it should not need a citation, but it needs stating because the
embodiment literature never states it. **Every intervention in §§A1–A5 has an unstated
inclusion criterion: a learner with typical fine-motor control, bimanual coordination,
visual tracking, and tolerance for a head-mounted display.** Gesture-production
instruction (§A1.2, the strongest result in Part A) requires producing gestures.
Manipulatives require grasping. Tangible interfaces require placement accuracy. HMDs
require vestibular tolerance and rule out learners for whom simulator sickness is
disabling — a moderator Thorp et al. 2024 (*Frontiers in Virtual Reality*,
doi:10.3389/frvir.2024.1343872) measured directly: *"simulation sickness negatively
impacted spatial ability in the more immersive condition."* `MEASURED-RCT`

**The virtual manipulative is the accessible one.** It accepts switch input, dwell-click,
eye gaze, keyboard, and screen reader; it obeys WCAG 2.2 AA target sizes (≥24×24 CSS px)
and **2.5.7 Dragging Movements**, which exists precisely so that a manipulative can be
operated without a drag. The physical manipulative accepts hands. **This inverts the usual
framing: the argument for going virtual is not cost, it is reach.** And it is corroborated
by the one measured equity finding in §A2.2 — the virtual arm of the N = 350 randomised
comparison had **fewer demographic predictors of performance**.

### A6.2 Sensory-motor intervention: the evidence base is a warning, not a warrant

`MEASURED-META` — **NEGATIVE RESULT N12** · **Vargas & Camilli (1999), "A Meta-Analysis of
Research on Sensory Integration Treatment," *American Journal of Occupational Therapy*,
doi:10.5014/ajot.53.2.189, 95 citations.** 16 studies SI vs no treatment, 16 SI vs
alternative treatment:

| Contrast | Weighted mean ES |
|---|---|
| SI vs **no treatment** | **0.29** |
| ⤷ **earlier studies** | **0.60** |
| ⤷ **more recent studies** | **0.03** |
| SI vs **alternative treatment** | **0.09** — *"not significantly different from zero"* |
| psychoeducational outcomes | 0.39 |
| motor outcomes | 0.40 |

**A textbook decline effect (0.60 → 0.03) and a null against active comparators.** This is
the oldest and largest sensorimotor-intervention literature in education-adjacent practice
and it does not survive contact with an active control.

`MEASURED-META` — **NEGATIVE RESULT N13** · **Systematic review of sensory-based
interventions for children and youth, 2015–2024** (*Frontiers in Pediatrics* 2025,
doi:10.3389/fped.2025.1720179, PMID 41321460), 21 level-I/II studies: **"Strong strength
of evidence supported use of deep pressure tactile input and caregiver training… Moderate
strength of evidence supported that *alternative seating did not improve attention*."**
Wobble stools and therapy balls — the most widely deployed "embodiment" intervention in
classrooms — have **moderate-strength evidence of no effect on attention.**

`OBSERVED` · **Camarata, Miller & Wallace (2020), *Frontiers in Integrative Neuroscience*,
doi:10.3389/fnint.2020.556660, 79 citations** is the standing methodological critique of
the whole SI/SP-T framework.

These join H1's own set: **Orton-Gillingham's multisensory branding is non-significant
(g = 0.22, p = .40; g = 0.14, p = .59; Stevens et al. 2021)**, and **Galuschka et al.
2014's RCT-only synthesis found every non-phonics family — auditory training, coloured
overlays, motor exercises, "sunflower therapy" — non-significant.**

`INFERENCE` · **The SELPA-relevant rule: sensory and motor engagement is a *channel*, not
a *treatment*.** Deep-pressure input and caregiver training have support; sensory
*integration* as a route to academic outcomes does not. **A system that markets embodiment
as therapeutic is marketing the unevidenced part** — the exact error H1 identified in
multisensory reading branding.

### A6.3 Where embodiment overloads rather than helps

H1's Archetypes 4.1 (attention), 4.2 (working memory), 4.5 (processing speed) and 4.7
(anxiety) all specify **externalising load**, and H1's prohibition is categorical:
*"**Do not build a working-memory trainer… The capacity is not trainable; the demand is
designable.**"* Every result in §A5 is that prohibition restated in hardware: **immersion
adds extraneous load (Makransky, EEG-measured), and adding load to a learner whose
bottleneck is load is not a neutral act.**

H1's §4.8 composition problem bites hardest here: *"Segmentation for working memory
increases the number of steps, which taxes sustained attention… **The system needs an
explicit conflict-resolution policy over accommodations, not an additive stack of
toggles.**"* An embodied activity is a *bundle* — motor demand + spatial demand + social
demand + novelty — and it cannot be toggled apart. **That, not cost, is the argument for
preferring the virtual manipulative in a SELPA-first system: its demands are separable.**

`MEASURED-META` · One genuine positive worth carrying: **immersive VR for cognitive
deficits in children with ADHD**, 7 RCTs, *"large effect sizes in favour of VR-based
interventions on outcomes of global cognitive functioning, attention, and memory"*
(*Virtual Reality* 2023, doi:10.1007/s10055-023-00768-1, 82 citations). `INFERENCE` — but
read it against H1's Melby-Lervåg, Redick & Hulme (2016) finding of **no convincing far
transfer from working-memory training across 87 publications / 145 comparisons**. VR
cognitive training measures *cognitive tasks*, not schoolwork. **The 2023 result is a
promising within-domain finding and must not be restated as an academic one.**

---

## A7. What an AI can and cannot reach — and what camera-in genuinely unlocks

This is the forward-looking section, and the honest headline is that **the capability is
real, is arriving now, and has one specific failure mode that would silently destroy its
pedagogical value if shipped unguarded.**

### A7.1 What is measurably possible today

`MEASURED-BENCH` · **FERMAT** (arXiv:2501.07244, Jan 2025) — the benchmark for exactly
this capability. **2,200+ handwritten mathematics solutions from 609 curated grade-7–12
problems**, perturbed along **four error dimensions: computational, conceptual, notational,
presentation**; **nine VLMs** across **error detection, localization, correction**. Result:
*"significant shortcomings in current VLMs in reasoning over handwritten text, with
**Gemini-1.5-Pro achieving the highest error correction rate (77%)**"* — and, tellingly,
*"some models struggle with processing handwritten content, as their **accuracy improves
when handwritten inputs are replaced with printed text or images**."*

`MEASURED-BENCH` · **arXiv:2606.11477 (Jun 2026), fairness-aware automated exam grading.**
Benchmark of **61 anonymised exams, 3,141 answer positions**. Prior template-matching
approaches reached **88–91% recognition**; general-purpose VLMs that *interpret the page*
reach **98.4%**. The fairness engineering is the transferable part: they separate **false
negatives (a correct answer marked wrong — the harm that lands on the student)** from
false positives, and *"a lightweight prompt that supplies the reference solution as
context lowers the **false-negative rate to 0.58%**."* Under an exemplary scheme **3 of 61
exams would be graded worse, all caught by a student self-review step.**

`MEASURED-BENCH` · **arXiv:2506.04822** — **14K+ handwritten answers from grade-4
classrooms in Indonesia**, mathematics and English, naturally messy handwriting: *"the VLM
struggles with handwriting recognition, causing **error propagation** in LLM grading, yet
**LLM feedback remains pedagogically useful despite imperfect visual inputs**."*

### A7.2 The failure mode that must be designed against — and it is not the one you expect

`MEASURED-BENCH` — **NEGATIVE RESULT N14, and the most consequential in Part A** ·
**arXiv:2604.22774 (Apr 2026), "When VLMs 'Fix' Students: Identifying and Penalizing
Over-Correction in the Evaluation of Multi-line Handwritten Math OCR."** Evaluated **15
state-of-the-art VLMs on FERMAT**:

> *"…revealing a critical failure mode of Vision-Language Models: **over-correction.
> Instead of faithfully transcribing a student's work, these models often 'fix' errors,
> thereby hiding the very mistakes an educational assessment aims to detect.**"*

Their PINK metric (LLM rubric grading with an explicit over-correction penalty) produces
**"substantial ranking reversals compared to BLEU: models like GPT-4o are heavily
penalized for aggressive over-correction, whereas Gemini 2.5 Flash emerges as the most
faithful transcriber."** Human experts preferred PINK over BLEU **55.0% to 39.5%**.

`INFERENCE` · **A tutor that looks at a child's work and silently corrects it while
reading it has destroyed the only signal it was there to collect.** This is the visual
analogue of F3's laundering failure (*"a harness that adds assumptions to make checks pass
is a laundering machine"*) and it is worse, because the correction happens inside
perception rather than inside reasoning, so nothing downstream can detect it.
**Requirement: transcription and evaluation must be separate calls, the transcription must
be scored for fidelity, and the fidelity score must be a shipped artifact.**

### A7.3 Watching a physical manipulation: the honest ceiling

`MEASURED-BENCH` — **NEGATIVE RESULT N15** · **"Transparent and Coherent Procedural
Mistake Detection" (arXiv:2412.11927, v5)**: *"Procedural mistake detection… Despite
significant recent efforts, **machine performance in the wild remains nonviable**, and the
reasoning processes underlying this performance are opaque… **VLMs struggle
off-the-shelf.**"* Related infrastructure exists and is growing — **PREGO**
(arXiv:2404.01933), **TI-PREGO** (arXiv:2411.02570), **EgoOops** (arXiv:2410.05343),
**HoloAssist** (arXiv:2309.17024, seven synchronised streams from an MR headset while a
remote instructor guides), **IndEgo** (arXiv:2511.19684, 3,460 egocentric recordings /
~197 h with mistake annotations, eye gaze, hand pose), **PIE-V** (arXiv:2604.15134, 2026),
**SHands** (arXiv:2603.26400, 52 participants, five synchronised RGB views of suturing
with frame-level error annotation). **Differentiable task-graph learning** improves
online mistake detection by **+16.7%** on CaptainCook4D (arXiv:2406.01486).

`INFERENCE` · The gradient is unambiguous: **static 2-D work on paper is solved
(98.4% / 77%); dynamic 3-D manipulation is not (nonviable in the wild).** A camera-in
tutor should be scoped to the first and must not pretend to the second.

### A7.4 What this unlocks — specified concretely

`INFERENCE` · Three capabilities are buildable now, in increasing order of ambition:

1. **The physical-work bridge.** The learner works on paper, wood, a circuit board, a pile
   of blocks — the medium the evidence in §A2 supports — and photographs it. The system
   grounds its response in *what is actually there*. **This restores the one thing the
   chat box destroyed: the tutor can see the work.** Requirements: (i) transcription and
   evaluation as **separate** calls; (ii) a **fidelity score** on the transcription, with
   over-correction explicitly penalised (arXiv:2604.22774); (iii) **false-negative rate
   reported separately** from overall accuracy, because they land on different people
   (arXiv:2606.11477); (iv) a **student self-review step** in the loop — the measured
   mechanism that caught all 3 mis-grades in 61 exams; (v) **abstention** when the image
   is illegible, propagated as `unverified` per F3's abstention rule, never as `passed`.
2. **The self-correcting virtual manipulative.** Not a picture of a manipulative — an
   object that **refuses illegal states** (Moyer-Packenham's *focused constraint*) and
   **links representations simultaneously**. This is the recoverable half of the
   Montessori mechanism, and §B is the substrate for building it.
3. **Gesture as an observable, not an intervention.** §A1.3's aptitude–treatment
   interaction turns on **whether the learner spontaneously gestures before instruction** —
   a variable that is *visible on camera* and currently measured by hand-coding video in
   research labs. `INFERENCE` — this is the highest-value, lowest-risk use of camera-in
   in the whole section: **not to instruct with gesture, but to detect whether this learner
   is one for whom gesture instruction helps or hurts.** Note N14's lesson applies here
   too: an observation channel must never become a silent correction channel.

### A7.5 What an AI cannot reach, stated plainly

- **Proprioceptive and haptic feedback.** No amount of vision closes the loop that
  suturing, pipetting, bowing a violin, or feeling a bearing bind depends on. §A5.3's
  g = 1.40 for haptic orthodontic training is evidence *for* haptics, not for cameras.
- **The self-correcting *material*.** I1's Montessori verdict stands for the *physical*
  material set at fidelity. What survives digitally is the *constraint property*, not the
  material.
- **Real-time correction of an unfolding physical manipulation.** N15: nonviable in the
  wild, today.
- **Genuine peers and institutional permission.** Not F7's, and I1 already ruled them out.

---

## A8. DELIVERABLE (a) — When a concept needs a physical object

The rule below routes on the **target competence and the dependent variable**, never on
the topic and never on the technology, because every measurement in Part A says the
dependent variable decides.

### The decision rule

**Step 1 — Classify the target competence.**

| Class | Recogniser | Route | Warrant |
|---|---|---|---|
| **P — Sensorimotor / proprioceptive** | The competence *is* a motor programme; success is judged on the movement or its physical product (suturing, pipetting, soldering, bowing, letter formation) | **PHYSICAL OBJECT REQUIRED**, or haptic simulation if the force loop is faithful | Haptic/VR orthodontics **g = 1.40**; Bödding behavioural **d = 0.40** survives equal-content control; Longcamp handwriting > typing for letter recognition |
| **S — Spatial / 3-D structural** | The competence is understanding a 3-D configuration that cannot be laid flat without loss (molecular geometry, crystal structure, anatomy in situ, field-scale terrain) | **SIMULATION SUFFICES; immersion optional and must be justified against a desktop control** | Wu et al. **ES = 0.24** for immersion over desktop; Thorp et al. find immersive VR did *not* enhance spatial performance over non-immersive |
| **C — Constraint-structured conceptual** | The concept has *illegal states* a well-built object can refuse (fractions, place value, equation balance, circuit topology, type systems, DAGs) | **MANIPULATIVE REQUIRED — physical or virtual, PREFER VIRTUAL** | Two randomised fidelity-documented head-to-heads null (N4, N5); virtual arm had *fewer demographic predictors*; combined interfaces beat either alone |
| **R — Relational / symbolic** | The competence is a mapping between representations with no illegal physical state (algebraic manipulation, proof, statistical inference, most of what a textbook contains) | **NEITHER — use multiple aligned instantiations and gesture-class representational compression** | Novack: gesture > action on objects for transfer; F10's four concreteness-fading nulls; Carbonneau's transfer k = 13 "small" |
| **F — Factual / conventional** | Definitions, notation, history, disciplinary norms | **NEITHER — this is F3's L1 tier** | No mechanism in Part A applies |

**Step 2 — Apply four modifiers, in order.**

1. **The equal-content test (mandatory gate).** *Would this comparison survive a control
   that receives the same content, the same time and the same attention on a plain
   screen?* If not, you have measured novelty. **Bödding: d = 0.04 / −0.31 / −0.51** when
   only the medium varies. **Never justify a physical or immersive build against a
   "traditional instruction" control.**
2. **The load test.** Every physical or immersive element adds extraneous load
   (Makransky, EEG-measured). If the learner's binding constraint is working memory,
   attention, anxiety or processing speed — H1 Archetypes 4.1/4.2/4.5/4.7 — **the added
   load is a direct cost against the binding constraint and the burden of proof
   inverts.**
3. **The access test.** If the object requires fine-motor control, bimanual coordination
   or vestibular tolerance, it has an inclusion criterion. **Virtual manipulatives accept
   switch, dwell, gaze and keyboard input and can meet WCAG 2.2 AA 2.5.7 (Dragging
   Movements) and 2.5.8 (Target Size ≥24×24 px). Physical ones accept hands.**
4. **The presence-premium ceiling.** Adding presence to a screen is worth **≈ 0.2 SD**
   (§A4.2, three independent literatures). If a physical build costs more than 0.2 SD's
   worth of anything — including the engineering time that would otherwise buy dosage,
   which H1's R5 names as *"the primary scalable lever"* — **it is the wrong trade.**

**Step 3 — Build to the property, not the medium.** In every case where a manipulative is
indicated, the two properties that carry the effect are:

- **Refusal.** The object must make the illegal state unreachable. This is Montessori's
  self-correction and Moyer-Packenham's *focused constraint*, and it is the single
  transferable feature.
- **Simultaneous linking.** Changing one representation must visibly change the others.
  This is the property no physical object has, and it is the strongest argument for
  virtual.

**Step 4 — Choose the observation channel, not the instruction channel.** §A7.4(3): use
camera-in to *detect* who benefits (spontaneous gesture rate, actual work on paper), and
route accordingly. **Do not use it to instruct by gesture generically — N1 says that
actively harms the non-gesturing half of the class.**

### The rule in one sentence

> **A concept needs a physical object only when the competence is the movement itself; it
> needs a manipulable object — preferably virtual — whenever the concept has illegal
> states an object can refuse; and it needs neither, in favour of multiple aligned
> instantiations, whenever the competence is a mapping between symbols.**

---

# PART B — A3 · REACTIVE / EXECUTABLE NOTEBOOKS

## B0. What F3 already established — not re-derived

Named entity **#17** in the original brief ("Morimo interactive colabs") resolved to
**marimo**. F3 absorbed the engineering half; this section owns the pedagogical half and
the substrate decision. **Carried forward, not re-argued:**

| Established in F3 | Value |
|---|---|
| Pimentel et al. MSR 2019 corpus | **1,159,166** deduplicated notebooks; **863,878** with unambiguous execution order |
| Ran without error | **24.11%** (208,323) |
| **Reproduced their own stored outputs** | **4.03%** |
| Out-of-order cells | 36.36%; NameError = 14.53% of failures |
| **Declaring dependencies made it WORSE** | ImportError **45.18%** (declared) vs **31.24%** (undeclared) |
| Notebooks importing any testing module | **1.54%** |
| marimo's reactive DAG | eliminates the **ordering** class of hidden state; **explicitly does not track mutations** |
| marimo's cited "36% not reproducible" | traces to a **JetBrains execution-count proxy**, not re-execution. Quote **4.03%** and cite Pimentel |
| Quarto | **does not execute `.ipynb` cells by default**; `freeze` exists so published output need not be reproducible |
| F3's substrate ruling | *"reactive notebook (marimo / Pluto class) executed in CI from a cold container, with pinned dependencies serialised inside the artefact, failing the build on any cell error and on any assertion failure"* |

`MEASURED-BENCH` — **one new corroboration of F3's most counter-intuitive result.**
**arXiv:2602.07195 (Feb 2026)** mined **12,720 notebooks from 79 popular Kaggle
competitions**: **only 35.4% remain reproducible today.** And, independently reproducing
Pimentel's 2019 finding on a completely different corpus seven years later:

> *"Crucially, we find that **environment backporting, i.e., downgrading dependencies to
> match the submission time, does not improve reproducibility but rather introduces
> additional failure modes.**"*

**NEGATIVE RESULT N16.** Two corpora, seven years apart, both find that **the obvious
environment-management intervention makes reproducibility worse.** The reflexive fix
(pin harder, pin older) is measurably counterproductive; §B5 is built on the opposite
principle.

---

## B1. The reactive model as a pedagogical object

### B1.1 The claim, stated precisely so it can be tested

The pedagogical claim implicit in reactive notebooks is: *a DAG that recomputes on change
means the learner cannot observe a state that is inconsistent with the code in front of
them, so the learner never forms a belief grounded in an artefact that does not exist.*

That is a claim about **misconception formation**, and it is a good one. Misconceptions
are built from *observations*, and a stale notebook cell is an observation the code cannot
justify. In Jupyter, a learner can edit `rate = 0.10` to `rate = 0.50`, not re-run the
downstream cell, and read a number that was never produced by the visible program. There
is no error, no warning, and nothing to notice. **In a strict reactive notebook that state
is unreachable.**

### B1.2 Is there evidence? No. Say so.

`OBSERVED — ABSENCE` · Searches across **Crossref** (`query.bibliographic`), **ERIC**,
**Europe PMC**, **arXiv** and **Semantic Scholar** on 2026-07-27 for reactive-notebook
learning studies returned **zero** empirical evaluations of reactive notebooks as an
instructional medium. Crossref queries for `reactive notebook marimo dataflow` return
minor-planet and cell-line records. ERIC's computational-notebook corpus is entirely
**Jupyter** and entirely **case-study / course-report** in genre (e.g. EJ1269976,
EJ1265289, EJ1370890, EJ1344385). The single relevant quantitative education study found —
EJ1344385, **115 students, full semester, computational notebooks in a first-year business
IT course** — evaluated *gamification*, not reactivity, and concluded that *"engagement in
active learning activities can be a stronger determinant of learning outcomes than initial
knowledge."*

**Ruling: the reactive-notebook-prevents-misconceptions claim is an UNTESTED DESIGN CLAIM.
It must be labelled `INFERENCE` wherever the survey uses it, and it is a strong candidate
for the project's own first study** (§D).

There is, however, adjacent measured evidence that the *hazard being eliminated is real*:

`MEASURED-BENCH` · **NBSafety (arXiv:2012.06981)** — a Jupyter kernel using **runtime
tracing plus static analysis** to track lineage. Evaluated by **replaying 666 real
notebook sessions**: **117 sessions contained potential safety errors**, and in the
remaining 549, the cells NBSafety flagged as resolving a staleness issue were **more than
7× more likely to be selected by users for re-execution than a random baseline** — *even
though those users were not running NBSafety and could not have been influenced by it.*
**That 7× is the best available measurement that staleness is a real, felt hazard rather
than a theoretical one.**

`MEASURED-BENCH` · **FlowBook (arXiv:2605.01560, May 2026)** — and note its framing of the
reactive approach: *"Prior approaches either employ dependency analyses or **enforce
reactive dataflow models that face fundamental tradeoffs among expressiveness, precision,
and performance**."* FlowBook's alternative is the definition this report adopts in §B5:

> *"a notebook is reproducible **if and only if executing its cells in top-to-bottom order
> from an empty store produces exactly the outputs currently recorded**."*

Implemented as a dynamic read/write-set analysis at cell boundaries, with **median 70 ms
latency overhead**.

### B1.3 ORIGINAL MEASUREMENT — what the reactive DAG eliminates, and what it does not

`MEASURED-BENCH` — **original, this survey.** F3 quoted marimo's docs on the mutation
hole. This report *measured* it, along with the whole hazard taxonomy.

**Method.** marimo **0.23.15** (installed via `uv`, Python 3.12.3). For each hazard class,
a minimal marimo notebook was constructed and `app.run()` invoked in a fresh subprocess;
the identical cells were then executed (a) in source order and (b) in a plausible
learner-chosen order, under the Jupyter "cells are a mutable global namespace" model.

```
uv venv .venv && uv pip install marimo && .venv/bin/python marimo_guarantees.py
```

| # | Hazard class | marimo | Jupyter model, source order | Jupyter model, learner order |
|---|---|---|---|---|
| **H1** | Use-before-define (cell reading `x` sits above cell defining `x`) — *14.53% of Pimentel's failures are NameError* | **RAN, `y = 42` (correct)** | `NameError: name 'x' is not defined` | 42 |
| **H2** | Two cells define the same global | **REFUSED at load: `MultipleDefinitionError: This app can't be run because it has multiple definitions of the name x`** | `x = 99` | **`x = 1`** — *the same document yields two different answers* |
| **H3** | Mutual dependency (cycle) | **REFUSED at load: `CycleError: This app can't be run because it has cycles.`** | NameError | NameError |
| **H4** | Stale downstream after an upstream edit | **NOT EXHIBITABLE** — `app.run()` always executes the full DAG | 1100.0 | 1100.0 |
| **H5** | **In-place mutation** (`xs = [1,2,3]` / `xs.append(100)` / `total = sum(xs)`) | **RAN, `total = 106`** — *see H5b* | 106 | **6** |
| **H6** | **Attribute mutation** (`cfg.n = 999`) — marimo's own documented non-guarantee | **RAN, `area = 998001`** | 998001 | **100** |
| **H7** | Deleted-cell residue (`helper` deleted from the document, still referenced) | **REFUSED: `NameError: name 'helper' is not defined`** | 10 *(kernel memory keeps it alive; the notebook "works")* | 10 |
| **H8** | Unseeded randomness *(control)* | RAN, 0.4038… | 0.9057… | 0.7863… |

**H5b — the decisive follow-up.** The same three cells, same dependency structure, built in
two source orders:

| Source order | `total` |
|---|---|
| A, B, C — bind, mutate, read | **106** |
| A, C, B — bind, read, mutate | **6** |

`MEASURED-BENCH` · **The answer is determined by source position, not by the dependency
graph.** Neither B nor C *defines* a name the other *reads* — both merely read `xs` — so
the DAG imposes no edge between them and marimo falls back to document order. The
notebook is deterministic; **it is not dependency-justified.** Editing the mutation cell
does not invalidate the reading cell, because as far as the static analysis is concerned
nothing changed.

**What this establishes, precisely:**

- ✅ **Eliminated by construction (H1, H3, H7):** the ordering class and the
  deleted-cell-residue class. H7 is worth emphasising because it is invisible in Jupyter:
  the notebook *appears to work* until someone restarts the kernel, at which point the
  learner's mental model and the artefact diverge silently.
- ✅ **Eliminated by refusal (H2):** the notebook will not load. Note the Jupyter column:
  the *same file* yields `x = 99` or `x = 1` depending on click order. **There is no
  correct answer, and nothing surfaces that fact.** For a teaching artefact this is the
  worst failure mode there is, and marimo makes it structurally impossible.
- ❌ **Not addressed (H5, H6):** mutation. The docs say *"tracking mutations reliably is
  impossible in Python"* and the measurement confirms the consequence.
- ❌ **Orthogonal (H8):** determinism. Reactivity says nothing about it, which is why §B5
  makes it a separate rule.

`INFERENCE` — **the pedagogical translation.** Rewrite the marketing claim as an honest
one: **a reactive notebook removes the class of inconsistency caused by *when the learner
clicked*, and does not remove the class caused by *what the learner's code did to an
object*.** For teaching material this is a very good trade, because teaching code mutates
little and the ordering hazard is the one a novice cannot even perceive. **But it means
reactivity is a hazard reduction, not a guarantee, and it cannot be the only thing
standing between a learner and a wrong number.** This is exactly G3's Rot Rule 3 — *ship
the checker with the claim* — and it is why §B5's specification requires assertions
regardless of the notebook engine.

---

## B2. In-browser execution: what actually runs today, measured

All figures in this section are `MEASURED-BENCH` originals produced for this report on
2026-07-27 unless marked otherwise; commands are given so each is reproducible.

### B2.1 The cold-start byte budget

| Substrate | Engine bytes to first output (wire) | Language |
|---|---:|---|
| **Observable runtime 6.0.0** | **0.027 MB** (27 KB; whole npm package 39 KB) | JavaScript only |
| **PyScript + MicroPython 1.28.0-6** | **0.53 MB** (`micropython.wasm` 446,411 B + `.mjs` 108,321 B) | MicroPython |
| **Quarto Live 0.2.0 shim** | 0.66 MB | + an engine below |
| **Pyodide 314.0.3 core** | **5.70 MB** (`pyodide.asm.wasm` 3.28 MB br / 9.15 MB identity; `python_stdlib.zip` 2.39 MB) | CPython 3.14 |
| **marimo 0.23.15 `export html-wasm`** | **≈8.0 MB** (2.27 MB gzip app shell + 5.71 MB Pyodide fetched from jsDelivr) | CPython 3.14 |
| **JupyterLite 0.8.1 + Pyodide** | **≈11.3 MB** (5.60 MB gzip app-shell upper bound + Pyodide core) | CPython 3.14 |
| **stlite 1.8.1** | **≈11.5 MB** minimum (30.42 MB non-map assets total; PlotlyChart chunk alone 6.60 MB) | CPython (Pyodide **0.29.3**) |
| **WebR 0.6.0** | **≈15.28 MB** (`R.wasm` 11.76 MB) | R 4.4/4.5 |

**And the number that decides §B6:**

| Teaching stack | Packages in closure | **Total wire, incl. Pyodide core** |
|---|---:|---:|
| Pyodide core only | — | **5.70 MB** |
| **numpy + matplotlib + pandas** | 13 | **21.89 MB** |
| numpy + sympy + matplotlib | 14 | ≈22.3 MB |
| + scikit-learn | 17 | ≈40 MB |
| + scipy, sympy, networkx, statsmodels | 24 | ≈54 MB |

Wheels are already ZIP-compressed — **brotli buys ~1% on them; only the 5.70 MB core
compresses.** Derived (not measured on a throttled link): 21.89 MB is ~2.9 s at 60 Mbps,
**~17.5 s at 10 Mbps, ~70 s at 2.5 Mbps.**

### B2.2 The cost that is *not* bytes

`MEASURED-BENCH` · Pyodide 314.0.3 under **Node v24.18.0**, where the engine is read from
the local filesystem and **zero network bytes are transferred** — so this is a **floor on
compute alone**:

| Phase | Run 1 | Run 2 | Run 3 |
|---|---:|---:|---:|
| `loadPyodide()` | 1.057 s | 1.009 s | 1.029 s |
| `runPython("1+1")` | 0.4 ms | 0.4 ms | 1.2 ms |
| `loadPackage("numpy")` | 0.383 s | 0.180 s | 0.216 s |
| `import numpy`; `np.arange(10).sum()` | 0.269 s | 0.255 s | 0.258 s |
| `loadPackage(["matplotlib","pandas"])` | 0.926 s | 0.510 s | 0.548 s |
| **`import matplotlib.pyplot`; `import pandas`** | **2.350 s** | **2.501 s** | **2.480 s** |
| **Total to a usable numpy+pandas+matplotlib session** | **4.99 s** | **4.46 s** | **4.53 s** |

**The dominant cost is not download — it is ~2.5 s of pure CPU spent importing matplotlib
and pandas, paid on every page load, because there is no way to cache a warm interpreter.**
Add the network on a real browser.

`MEASURED-BENCH` · **Pyodide vs native CPython on the same host:**

| Benchmark | Pyodide (wasm32) | Native CPython 3.12.3 | Ratio |
|---|---:|---:|---:|
| Pure-Python `sum(range(3e6))` | 0.349 s | 0.144 s | **2.4×** |
| numpy 300×300 matmul ×20, 1 thread | 0.302 s | 0.018 s | **16.9×** |
| same, native BLAS unrestricted (20 cores) | 0.302 s | 0.007 s | **43×** |

The pure-Python ratio matches Pyodide's own claim `VENDOR`: *"**Across benchmarks Pyodide
is currently around 3x to 5x slower than native Python**"* (roadmap.md @ tag 314.0.3 —
note `pyodide.org` returns HTTP 403 to WebFetch and 429 to curl; the docs had to be read
from the git tag). **The numpy gap is 7–18× worse than the advertised figure** because
Pyodide's `libopenblas` is single-threaded wasm32 without SIMD tuning. *(Caveat: versions
not matched — CPython 3.12/numpy 2.5.1 native vs CPython 3.14/numpy 2.4.3 wasm. Treat the
numpy ratio as indicative.)*

### B2.3 The package universe, and the absences that decide designs

`OBSERVED`, parsed from `pyodide-lock.json` @ 314.0.3: **354 lock entries, 293 real
packages** (61 are `*-tests`), 9 shared libraries, **446.4 MB** for the whole distribution.

**PRESENT:** numpy 2.4.3, scipy 1.18.0, pandas 3.0.2, matplotlib 3.10.8, **sympy 1.14.0**,
scikit-learn 1.8.0, networkx 3.6.1, statsmodels 0.14.6, requests, altair 6.0.0, pillow,
micropip, polars, duckdb, pyarrow, xarray, bokeh, sqlalchemy, opencv-python, geopandas.
`sqlite3` ships inside `python_stdlib.zip`.

**ABSENT — and this is the finding:**

| Package | In distribution | micropip fallback | Cost |
|---|---|---|---|
| **plotly** | ❌ | ✅ pure-Python wheel | **+9.45 MB** |
| **ipywidgets** | ❌ | ✅ (0.13 MB) | + host page must supply a widget manager |
| **anywidget** | ❌ | ✅ (0.30 MB) | — |
| **seaborn** | ❌ | ✅ (0.28 MB) | — |
| **torch / tensorflow** | ❌ | ❌ | **impossible** |
| **jax** | ❌ | ⚠️ pure-py wheel exists but needs native `jaxlib` | **unusable** |

`OBSERVED` · The **xeus-python / emscripten-forge** alternative is **not a superset**:
351 distinct packages, but **networkx, requests, altair, plotly, ipywidgets, anywidget,
seaborn, polars and pytorch are all ABSENT.** It trades packages away, it does not add
them. *(Only the `-dev` channel was enumerated.)*

`MEASURED-BENCH` · **R's browser ecosystem is 74× larger than Python's.**
`repo.r-wasm.org/bin/emscripten/contrib/4.4/PACKAGES` contains **21,623 packages**
pre-built for wasm32/emscripten — ggplot2, dplyr, tidyverse, data.table, shiny, knitr,
plotly, lme4, caret, sf, **torch 0.14.2** and **keras 2.15.0** are all present. The price
is a **2.7× heavier engine** (15.28 MB vs 5.70 MB). **If the mini-app is statistical, WebR
is not the eccentric choice; it is the better-provisioned one.**

### B2.4 The hard limits, verbatim

`VENDOR` · Pyodide `docs/usage/wasm-constraints.md` and `faq.md` @ tag 314.0.3:

> *"The following modules can be imported, but are **not functional** due to the
> limitations of the WebAssembly VM: **multiprocessing, threading, sockets** — as well as
> any functionality that requires these."*
> *"**fork and pthreads do not work in Pyodide. Attempts to use threading, multiprocessing,
> or subprocess will raise a RuntimeError.**"*
> *"**ssl: SSL module is replaced with a stub implementation that does not use OpenSSL.**"*
> Removed stdlib: *curses, dbm, ensurepip, fcntl, grp, idlelib, lib2to3, msvcrt, pwd,
> resource, syslog, termios, tkinter, turtle.py, turtledemo, venv, winreg, winsound*
> (plus `pty`/`tty` unimportable via `termios`). `decimal`'s C implementation only;
> `hashlib` loses OpenSSL-dependent algorithms; `zoneinfo` needs `tzdata`.
> Networking: *"all network calls are done via the browser… you have very little or no
> control over certificates, timeouts, proxies… sometimes things will be blocked by CORS."*

`OBSERVED` · Memory, read from build flags (`Makefile.envs` @ 314.0.3):
`INITIAL_MEMORY=30 MB`, `ALLOW_MEMORY_GROWTH=1`, **`MAXIMUM_MEMORY=4GB`** (the wasm32
address-space limit), `STACK_SIZE=10MB`. Real per-browser caps are lower and
**UNVERIFIED**.

`VENDOR` · **marimo WASM** (`docs/guides/wasm.md` @ 0.23.15):
> *"**WASM notebooks have a memory limit of 2GB**"*; *"PDB is not currently supported"*;
> concurrency adapters exist for `threading.Thread`, `ThreadPoolExecutor`, and
> process-shaped APIs but *"**They do not create OS threads, shared-memory processes, or
> true CPU parallelism**"*, while `threading.Lock`, `Condition`, `Semaphore`, `Barrier`,
> `Timer`, `multiprocessing.Pipe`, managers and shared memory are **unsupported**;
> *"**Chrome is the recommended browser**"*; and the export *"**must be served over HTTP**
> … it cannot be opened directly from the filesystem (`file://`)."*

`OBSERVED` · **marimo's export ships 705 files / 25.08 MB**, of which **192 files /
5.48 MB raw / 2.27 MB gzip** are fetched upfront. `--mode run` and `--mode edit` emit a
**byte-identical file inventory**; `--mode` only sets a runtime flag. Largest assets:
`Plot-*.js` 4.60 MB, `loro_wasm_bg-*.wasm` 3.11 MB (a CRDT), `node-sql-parser-*.js`
2.48 MB. **Pyodide is not bundled** — the worker pins `314.0.0` and fetches it from
jsDelivr at runtime, which is a live third-party dependency on every page load.

`VENDOR` · **JupyterLite** troubleshooting docs: *"not all Python packages that work in a
standard Python environment will work"*; a **Service Worker** is required for kernel
filesystem access and *"**Service Workers are not supported in Firefox private windows**"*;
content and settings live in browser **local storage / IndexedDB**, and *"Clear Browser
Data… cannot be undone"*. **Only the last two releases are actively supported.** A known
race produces `FileNotFoundError: [Errno 44]` when code runs before the kernel is ready
(issue #1371).

`VENDOR` · **stlite**: *"**time.sleep() is no-op**"*; *"stlite runs on a **single-threaded
environment**"* so `st.spinner()` cannot render during a blocking call; dataframes are
serialised as **Parquet rather than Arrow IPC**, producing genuine behavioural differences
in `st.dataframe`/`st.data_editor`; `st.bokeh_chart` is broken by a Bokeh 2/3 version
conflict. It pins **Pyodide 0.29.3 — an older major line than 314.x.**

`OBSERVED` · **Binder**, the server-backed contrast, from
`mybinder.org-deploy/mybinder/values.yaml`: **memory guarantee 450 M, limit 2 G; CPU
guarantee 0.01, limit 1; idle cull at 600 s.** — i.e. Binder gives you *the same 2 GB
ceiling marimo advertises for WASM*, plus one CPU, at the cost of a container, an image
build, and death after ten minutes idle. `jupyterhub/binderhub` publishes **no GitHub
releases** at all.

### B2.5 Maintenance risk, measured

`OBSERVED` (GitHub API, 2026-07-27) — because G3's **Rot Rule 5** requires dating every
capability claim:

| Project | License | Stars | Latest release | Age of release |
|---|---|---:|---|---|
| pyodide/pyodide | MPL-2.0 | 14,756 | `314.0.3` (2026-07-24) | **3 days** |
| marimo-team/marimo | Apache-2.0 | 22,073 | `0.23.15` (2026-07-23) | **4 days** |
| jupyterlite/jupyterlite | BSD-3 | 4,856 | `v0.8.1` (2026-07-08) | 19 days |
| pyscript/pyscript | Apache-2.0 | 18,690 | `2026.7.2` (2026-07-09) | 18 days |
| r-wasm/webr | *NOASSERTION* | 1,085 | `v0.6.0` (2026-05-19) | 2 months |
| r-wasm/quarto-live | MIT | **259** | `v0.2.0` (2026-05-22) | 2 months |
| observablehq/framework | ISC | 3,558 | `v1.13.4` (2026-03-02) | 5 months |
| **observablehq/runtime** | ISC | 1,080 | `v6.0.0` (**2024-11-06**) | **20 months** |
| r-wasm/quarto-drop | MIT | 190 | — (last push **2025-09-26**) | **10 months** |
| **jupyter-book/thebe** | BSD-3 | 442 | `thebe-lite@0.4.10` (**2024-09-06**) | **23 months** |

Two governance flags: **`r-wasm/webr` has no SPDX-identifiable license** (`gh api
repos/r-wasm/webr/license` → "Other") — a real blocker for a redistributable teaching
artefact until resolved. And G3's observation restated with 2026 numbers: **Quarto Live,
the only browser-native toolchain with real client-side grading, has 259 stars against
mdBook's 22,014. Capability and adoption are nearly uncorrelated in this space.**

---

## B3. Observable and the reactive-JS lineage: what they learned first

`OBSERVED` · Observable's runtime is **39 KB unpacked, 27 KB of source** — three orders of
magnitude smaller than any Python substrate, because it executes no Python. Its guarantees,
verbatim (`observablehq/runtime` README @ v6.0.0, `observablehq/framework`
`docs/reactivity.md` @ v1.13.4):

> *"Framework runs like a spreadsheet: code re-runs automatically when referenced variables
> change… **Code blocks in Markdown run in topological order determined by top-level
> variable references (a.k.a. dataflow), rather than in top-down document order.**"*
> *"Reactivity also allows **incremental evaluation**… **only the code blocks that are
> downstream of changed variables run.**"*
> *"**A variable without an associated observer is only computed if any transitive output
> of the variable has an observer**; variables are computed on an as-needed basis for
> display."*
> *"If multiple blocks define top-level variables with the same name… any references to
> duplicated variables in other blocks will **throw a duplicate definition error** because
> the definition is ambiguous."*

**Four lessons Python reactive notebooks are repeating, and one they are not.**

1. **Single definition per name is not a marimo invention; it is the price of dataflow,
   and Observable paid it first.** marimo's `MultipleDefinitionError` (measured, §B1.3 H2)
   and Observable's "duplicate definition error" are the same design decision reached
   independently eight years apart. `INFERENCE` — this is strong evidence the constraint
   is *necessary*, not stylistic.
2. **Lazy evaluation by observer-reachability is the feature marimo reimplemented as an
   opt-in and thereby weakened.** Observable computes only what is *displayed*; marimo's
   lazy runtime marks cells stale instead of running them, which F3 correctly noted gives
   *"the same staleness problem as Jupyter, by choice."* Observable's version is
   *demand-driven and still consistent*; marimo's is *deferred and possibly inconsistent*.
   **Prefer Observable's semantics; if using marimo lazily, treat it as Jupyter.**
3. **Scope discipline is a real constraint.** *"Only pages can declare top-level reactive
   variables. Components can't define their own reactive state."* Reactivity does not
   compose freely; it needs an ownership boundary. Any per-chapter mini-app framework will
   rediscover this.
4. **Implicit awaiting and generator iteration across cells** — Observable made promises
   and generators first-class members of the dataflow graph. This is the piece Python
   reactive notebooks have *not* fully absorbed, and it is why marimo needs bespoke
   cooperative concurrency adapters under WASM (§B2.4).

`OBSERVED` — **and the most important lesson of all, because it is a retreat.**
Observable Framework's README describes it as *"a free, open-source, **static site
generator** for data apps… Framework features **data loaders** that **precompute static
snapshots of data at build time**."*

**The most experienced reactive-notebook team in the world, having built the reactive
runtime that everyone else copied, answered "how do we run computation in the browser?"
with: mostly, don't — precompute at build time and ship the result.** §B6 takes that
seriously.

`OBSERVED` · The caveat, per G3's Rot Rule 5: **`observablehq/runtime` has not had a
release since 2024-11-06 (20 months)**, and Framework since 2026-03-02. Svelte-style
signal reactivity (fine-grained, compiler-driven dependency tracking) has since become the
mainstream JS implementation of the same idea and is far better maintained; a 2026 build
should treat *the semantics* as the inheritance and not necessarily the package.

---

## B4. Notebooks as assessment artefacts

### B4.1 The baseline that reframes the question

`MEASURED-BENCH` · From **C2 §8.1** — **Messer, Brown, Kölling & Shi (2025), "How
Consistent Are Humans When Grading Programming Assignments?", *ACM TOCE*, ERIC
EJ1488833**. **28 participants**, each grading **40 CS1 Java assignments** on correctness,
elegance, readability and documentation, in seven groups of four, with **one assignment
secretly duplicated** to measure intra-rater consistency:

| Measure | Result |
|---|---|
| Krippendorff's α, **correctness** | **≈ 0.20** |
| α, elegance / readability / documentation | **< 0.10** |
| Threshold for even tentative conclusions | α > 0.667 |
| Graders reproducing their own grade on the hidden duplicate | **1 of 22** |
| Mean self-inconsistency, correctness | **1.79 grade points** |

> *"human graders in our study **cannot agree** on the grade to give a piece of student
> work and are often **individually inconsistent**, suggesting that **the idea of a 'gold
> standard' of human grading might be flawed**."* — and *"a shared rubric alone was not
> enough."*

C2's ruling, which governs this section: *"code correctness is **verifiable** — **a test
suite is not a rater, it is a proof** — while code elegance, readability and design are
rater judgments where humans hit α < 0.1. **These must never be reported on the same scale
or with the same confidence.**"*

### B4.2 So: can a notebook be auto-graded meaningfully? Yes — on exactly one axis.

`INFERENCE` · **Yes, and the reactive notebook makes it strictly easier, for a reason that
has nothing to do with grading and everything to do with §B1.3.**

The obstacle to grading a Jupyter notebook has never been the assertions. It is that
**the submitted artefact does not determine the computation**: H2 showed the same file
yielding `x = 99` or `x = 1`; H7 showed a notebook that "works" only because a deleted
cell's variable survives in kernel memory. A grader re-running a submission is not
re-running what the student ran, and a grader reading stored outputs is reading something
no execution may have produced. **A reactive notebook eliminates that ambiguity for the
ordering class: the file *is* the program.** marimo's `.py` storage makes this literal —
the submission is a script, `git diff`-able and directly executable.

The honest scope, then:

| Axis | Grade it? | Instrument | Confidence |
|---|---|---|---|
| **Correctness of a computation** | **Yes** | Hidden test suite / assertion set executed against the submission in a clean environment | **Proof, not rating.** No inter-rater reliability applies because there is no rater |
| **Reproducibility of the artefact** | **Yes** | FlowBook's criterion (§B5): top-to-bottom from an empty store reproduces recorded outputs | Binary, mechanical |
| **Process / exploration path** | **Partly, and only with consent and instrumentation** | Execution telemetry — but see F1's ruling that unsupervised remote artefacts cannot support a process claim | Weak |
| **Elegance, readability, design** | **No** | — | **Humans reach α < 0.10.** Report separately, never on the same scale, never as a score |

`MEASURED-BENCH` · Messer et al.'s companion systematic review — **121 papers, 2017–2021**,
ERIC EJ1419855 — finds most automated tools assess *correctness in object-oriented
languages*, **the dimension where humans were least bad**, and largely ignore the ones
where human agreement collapses. **The field automated the easy axis and left the hard one
to α = 0.1 humans.** That is the correct division of labour and it should be stated as a
design decision rather than apologised for.

`OBSERVED` · The tooling, dated per Rot Rule 5 (from G3 §7.5): **otter-grader** 157★,
v7.0.0 released **2026-07-27** — healthy. **nbgrader** 1,369★, v0.9.5 from **2025-01-17**
(~18 months) with **269 open issues**. **GitHub Classroom autograding** — **ARCHIVED**,
*"This project does not currently have a roadmap."* And **Quarto Live** ships the only
browser-native grading path: a `#| check: true` block receives `.result`,
`.evaluate_result`, `.user_code`, `.solution_code`, and runs **entirely client-side**.

`MEASURED-BENCH` · Two anchors on how far automated feedback generalises beyond code:
**~86.5% accuracy** on a ~10M question-answer-pair multilingual autograding corpus, rising
to teaching-assistant parity with a human in the loop (ERIC EJ1369213); and, for exams on
paper, the fairness architecture measured in §A7.1 — **98.4% recognition, false-negative
rate driven to 0.58%, 3 of 61 exams mis-graded and all 3 caught by student self-review.**

`INFERENCE` — **the rule.** *An executable notebook is a valid assessment artefact for
verifiable claims and an invalid one for judgment claims, and the only reason it becomes
valid even for the first is that the reactive model makes the file determine the
computation. Grade the assertions; report the judgments as prose with no number attached.*

---

## B5. The reproducibility specification — generalising the G3 recipe

### B5.1 What G3 measured, and why it generalises

`MEASURED-BENCH` (G3 §1.4) · The **xiaol** book: **16 example scripts, 1,940 Python LOC,
numpy in 2 of 16 and stdlib-only in the other 14, full run exit code 0 in 0.555 s on
Python 3.12.3, and 16/16 committed outputs reproduced byte-identically.** Against F3's
**4.03%** baseline for published notebooks, that is **two orders of magnitude**, achieved
with **no infrastructure at all**.

G3's own diagnosis — **Rot Rule 2, "reproducibility is bought by subtraction, not by
infrastructure"** — and its two caveats: **there are no assertions** (nothing can fail, so
nothing can be *known* to have broken), and **the datasets are 3–84 rows** (the book fits a
5-feature regression on 14 rows and then interprets the coefficients).

`INFERENCE` · The subtraction recipe generalises for a reason that is now measurable rather
than aesthetic: **the profile that makes an artefact reproducible is the same profile that
makes it run in a browser.** No network (Pyodide's `ssl` is a stub, all traffic is
CORS-bound), no threads or processes (RuntimeError), no large data (2 GB WASM ceiling,
21.89 MB just to reach pandas), no native extensions (293 packages, torch impossible).
**Subtraction buys durability, browser-portability and gradeability with one move.** And
§B0's N16 shows the alternative — pin harder — has now failed twice, on two corpora, seven
years apart.

### B5.2 ORIGINAL MEASUREMENT — the specification, made executable

`MEASURED-BENCH` — **original, this survey.** A specification that cannot fail is a wish.
So it was written as a checker and run.

**`teachcheck` — nine rules for reproducible executable teaching material.** Reproducibility
is defined per **FlowBook (arXiv:2605.01560)**: *executing from an empty store reproduces
the recorded outputs exactly* — strengthened here to *twice, in fresh processes, under a
scrubbed environment* (`env -i PATH=/usr/bin:/bin HOME=/nonexistent LC_ALL=C
PYTHONHASHSEED=0 TZ=UTC`).

| Rule | Requirement | How it is checked |
|---|---|---|
| **R1** | No network access | AST scan for `urllib`/`requests`/`httpx`/`socket`/`ftplib`/… |
| **R2** | No unseeded nondeterminism | AST scan for `random` without `seed()`, `secrets`, `uuid1/4`, `os.urandom`, `time.time()`, `datetime.now/today` |
| **R3** | Stdlib-only, or declared **and pinned** inline (PEP 723) | Imports diffed against `sys.stdlib_module_names`; PEP 723 block parsed and each requirement checked for a version specifier |
| **R4** | **Byte-identical across two runs in fresh processes** | Two scrubbed-env subprocess runs; SHA-1 of stdout compared; non-zero exit is a failure |
| **R5** | Reproduces its **committed** expected output byte-for-byte | stdout diffed against `expected/<name>.txt` |
| **R6** | **Contains at least one assertion** — it must be able to fail | AST count of `ast.Assert` |
| **R7** | Portable to a WASM runtime | Imports diffed against Pyodide's removed-and-broken list (§B2.4), verbatim from `wasm-constraints.md` |
| **R8** | Inside the wall-clock budget | measured, budget 5.0 s |
| **R9** | Input data inside the size budget | `data/` tree size, budget 64 KB |

**Corpus.** Four conformant teaching scripts written to the recipe — gradient descent
checked against the closed-form least-squares solution; Shannon entropy with the
uniform-maximises-entropy property asserted; the base-rate / screening-test paradox; a
regression read from the same 5-row CSV the figures would be drawn from — plus two
deliberately non-conformant controls.

**Result:**

```
script                     R1   R2   R3   R4   R5   R6   R7   R8   R9
01_gradient_descent.py     ok   ok   ok   ok   ok   ok   ok   ok   ok
02_entropy.py              ok   ok   ok   ok   ok   ok   ok   ok   ok
03_bayes.py                ok   ok   ok   ok   ok   ok   ok   ok   ok
04_csv_regression.py       ok   ok   ok   ok   ok   ok   ok   ok   ok
90_bad_network.py         FAIL FAIL  ok  FAIL FAIL FAIL FAIL  ok   ok
                            R1: urllib,urllib.request
                            R2: random imported without seed()
                            R4: rc=0/0 sha1=aebd2cd8cc/7ec00a1ee2   ← caught empirically
                            R6: 0 assert(s)
                            R7: threading
91_bad_noassert.py         ok   ok   ok  FAIL FAIL FAIL  ok   ok   ok

4/6 scripts fully conformant; execution 121 ms; checker wall-clock 231 ms; exit 1
```

Two things this measurement establishes that a written specification could not:

1. **R2 and R4 are independent detectors of the same defect and both are needed.** R2
   caught `random` statically; **R4 caught it empirically** via two differing stdout SHA-1s
   on a script whose exit code was 0 both times. A script can be nondeterministic without
   any recognisable import — and it can import `random` and still be deterministic if
   seeded. **Neither check subsumes the other.**
2. **The assertion requirement (R6) is what converts a reproducible artefact into a
   verifiable one — measured by mutation.** A single sign flip was injected into the
   entropy definition (`-sum(...)` → `sum(...)`) — precisely the class of derivation slip
   F3's grounding-ladder harness targets:

   ```
   02_entropy.py   ok ok ok FAIL FAIL ok ok ok ok
       R4: rc=1/1 ... ERR: AssertionError: uniform over 4 outcomes must be exactly 2 bits
       R5: differs (158B vs 155B)
   checker exit code = 1
   ```

   **The artefact failed loudly, named the violated teaching claim, and returned a
   non-zero exit code.** The xiaol book, with the same 100% reproduction rate, would have
   printed the wrong number serenely — G3's Rot Rule 3, demonstrated.

**Cost:** the full nine-rule suite over six scripts, including twelve subprocess launches,
runs in **0.23–0.32 s** (five repeats). **Per-script marginal cost ≈ 38 ms.** There is no
economic argument for not running it in CI on every commit.

*(Reproduce: `python3 teachcheck.py <dir>`, ~200 lines, stdlib only, no third-party
dependencies. Corpus build commands are in the run log.)*

### B5.3 The specification, stated

> **A unit of executable teaching material is CONFORMANT iff:**
> **(1)** it is a single file with no network, no unseeded randomness, no threads,
> processes or sockets, and no dependency outside the Python standard library — or, if it
> has one, that dependency is declared inline (PEP 723) **and pinned** and is present in
> the target WASM distribution's package set;
> **(2)** its input data is committed alongside it and small enough to read;
> **(3)** it contains **at least one assertion that encodes the teaching claim**, so that
> the claim has a falsifying condition;
> **(4)** its expected output is committed, and executing it from an empty store in a
> clean process reproduces that output **byte-for-byte, twice**;
> **(5)** it exits non-zero on any failure, and **CI treats that as a build failure**;
> **(6)** any figure it displays is **generated from the same data the code runs on**
> (G3's "unadvertised good property" — figures as renderings of the computation, not
> illustrations of the argument); and
> **(7)** it carries F3's **tier badge** — L0/L1/L2a/L2b/L3/L4 — and `ABSTAIN` is
> representable and never collapsed to `PASS`.
>
> **Reactivity is orthogonal to all seven** (§B1.3, H8) and is worth adopting anyway,
> because it eliminates the ordering and residue hazards that make (4) meaningless in
> Jupyter — **but it substitutes for none of them.**

---

## B6. DELIVERABLE (b) — Substrate recommendation for per-chapter mini-apps

### B6.1 The number that decides it

A per-chapter interactive figure built on **numpy + matplotlib + pandas** costs
**21.89 MB over the wire and ~4.5 s of CPU on every cold visit** — before the app's own
code, on every chapter, for every reader. The **same** figure rendered to SVG at build time
and driven by a slider costs **tens of kilobytes and ~27 KB of reactive runtime**. That is
roughly a **400× ratio**, and the pedagogically load-bearing properties identified in Part
A — **refusal of illegal states** and **simultaneous linking of representations** (§A2.4) —
require *neither* Python *nor* a notebook. They require a constraint and a dependency
graph.

**Observable's own team reached this conclusion and shipped a static site generator with
build-time data loaders. Follow them.**

### B6.2 The recommendation: a four-tier ladder, routed by what the demo must do

| Tier | Substrate | Cold-start cost | Use when | Do not use when |
|---|---|---:|---|---|
| **T0 — Precomputed** | Static SVG/JSON emitted at build time by a T4 pipeline; reactive JS only for parameter binding | **~0 MB** | The parameter space is small and enumerable — most explorable figures, most animations, every "drag the slider and watch the curve" | The learner must supply arbitrary input |
| **T1 — Reactive JS** ★ **DEFAULT** | Signal-based reactive JS (Observable-runtime semantics; a modern signals library for maintenance), plain ESM, no build step required | **≈0.03 MB** | The mini-app is a **constrained manipulative**: it refuses illegal states, links representations, and responds to learner action. **This is where the F7 evidence says the effect lives** | The learner must read, edit and run *real Python* as part of the lesson |
| **T2 — MicroPython** | PyScript 2026.7.2 + MicroPython 1.28.0-6 | **0.53 MB** | The point *is* that the learner reads and edits real Python — control flow, data structures, recursion, algorithms | numpy/pandas/matplotlib are needed (they do not exist here) |
| **T3 — Pyodide** | **marimo `export html-wasm`** (≈8.0 MB) for a full notebook; raw Pyodide (5.70 MB) for a single embedded widget | **5.7–22+ MB** | numpy / sympy / matplotlib is genuinely **load-bearing** — the chapter is *about* the numerical or symbolic computation. **≤ 3 per book, budgeted explicitly** | Anything T0–T2 can do |
| **T3-R — WebR** | webR 0.6.0 via **Quarto Live** | ≈15.9 MB | The chapter is **statistical** and needs the R ecosystem (**21,623 wasm packages** vs Pyodide's 293) | The license question is unresolved — `r-wasm/webr` has **no SPDX license** |
| **T4 — Server** | Container in **CI only** | n/a | Building, verifying and precomputing everything above | **Never in the reader's path.** Binder is 450 M guarantee / 2 G limit / 1 CPU / 600 s idle cull, self-described as a research pilot |

**★ The default is T1, and the burden of proof is on anything heavier.** Every tier above
T1 must justify itself against a stated learning objective, not against "it would be nice
to run Python here."

### B6.3 Three concrete rulings

1. **Use marimo, and use it as the authoring and CI substrate first, the delivery
   substrate second.** Its `.py` file format is the whole argument: git-diffable,
   directly executable as a script, `teachcheck`-able, and — measured in §B1.3 — it
   *refuses to load* the two document states that make a Jupyter submission ambiguous.
   Export to WASM only for the ≤3 chapters that earn T3. **And never configure the runtime
   lazily: F3 established, and §B1.3 confirms, that lazy marimo is Jupyter by choice.**
2. **Quarto Live is the right tool for graded exercises and the wrong tool to bet the book
   on.** It is the only substrate with real client-side grading (`#| check: true` receiving
   `.result` / `.user_code` / `.solution_code`), MIT-licensed, 0.66 MB of shim. It also
   has **259 stars**, pins **Pyodide `^0.28.1`** against the current 314.x line, still
   requires a manual `_knitr.qmd` include described in its own docs as *"a temporary
   requirement"*, and its sibling `quarto-drop` has been unpushed for ten months. **Use it
   for exercises; keep the chapter content independent of it.**
3. **Do not build on stlite, Thebe, or Observable's npm packages as-is.** stlite pins an
   older Pyodide major, makes `time.sleep()` a no-op, and swaps Arrow for Parquet with
   visible behavioural consequences. Thebe's last release was **2024-09-06** and its own
   README says the current line is *"still under development."* Observable's *runtime*
   hasn't shipped since **2024-11-06** — inherit its **semantics**, not its package.

### B6.4 The measured limits, stated as the brief requires

- **Bytes:** T1 **0.027 MB** · T2 **0.53 MB** · T3 **5.70 MB** engine, **21.89 MB** with
  the standard teaching stack, **≈54 MB** with scipy+sympy+networkx+statsmodels ·
  T3-R **15.28 MB**.
- **Time:** **~4.5 s of pure CPU** to a usable numpy+pandas+matplotlib session with **zero
  network** (Node floor); **~2.5 s of that is `import matplotlib.pyplot` + `import
  pandas`**, unavoidable and uncacheable. On 10 Mbps add ~17.5 s of download.
- **Speed:** **2.4× slower than native CPython** on pure Python (matching Pyodide's own
  "3x to 5x" claim); **17–43× slower on numpy** because wasm BLAS is single-threaded and
  untuned.
- **Memory:** marimo WASM **2 GB** (vendor); Pyodide built with `MAXIMUM_MEMORY=4GB`,
  `INITIAL_MEMORY=30MB`; real browser caps **UNVERIFIED**.
- **Packages:** **293** real packages in the Pyodide distribution. **plotly (+9.45 MB),
  seaborn, ipywidgets, anywidget absent but micropip-installable; torch, tensorflow and
  jax unavailable.** xeus-python is **not** a superset. WebR offers **21,623**.
- **Capabilities:** **no threads, no processes, no sockets, no subprocess** (RuntimeError);
  `ssl` is a stub; 17 stdlib modules removed; all networking is CORS-bound browser fetch.
- **Delivery:** marimo WASM **must be served over HTTP**, not `file://`; Chrome is the
  vendor-recommended browser; JupyterLite needs a **Service Worker**, which **does not
  work in Firefox private windows**.
- **Third-party runtime dependency:** marimo's WASM export **fetches Pyodide 314.0.0 from
  jsDelivr at page load**. For an artefact that must survive, **vendor the engine** — G3's
  Rot Rule 1, *never make a vendor behaviour load-bearing*.

---

# C. NEGATIVE / NULL RESULTS REGISTER

The editorial standard requires ≥1 per section. This report has **sixteen**, of which
**two are original to it**.

| # | Result | Source | Label |
|---|---|---|---|
| **N1** | Gesture instruction **harmed** children who did not spontaneously gesture beforehand — worse than the manipulative-action control on learning, generalization *and* retention | *Cognitive Science* 2024, doi:10.1111/cogs.13479 | MEASURED-RCT |
| **N2** | Hand-model (gesture-only) condition **worse** than action conditions in adult brain anatomy | *Applied Cognitive Psychology* 2023, doi:10.1002/acp.4093 | MEASURED-RCT |
| **N3** | **"The pen is mightier than the keyboard" did not replicate.** No consistent differences between any group *including a no-notes group*; pooled replication effect small and non-significant | Morehead, Dunlosky & Rawson 2019, doi:10.1007/s10648-019-09468-2 | MEASURED-RCT |
| **N4** | **Virtual vs physical manipulatives: no significant difference**, N = 350, within-class randomisation, documented fidelity, delayed post-test — and the virtual arm had **fewer demographic predictors of performance** | Moyer-Packenham et al. 2013, doi:10.1177/002205741319300204 | MEASURED-RCT |
| **N5** | Physical concrete > virtual concrete **not supported**: Welch t(41.7) = 1.015, p = 0.316, M_diff = 0.47 [−0.47, 1.41], N = 166 | Trory et al. 2026, ERIC EJ1510953 | MEASURED-RCT |
| **N6** | **Increasing a robot tutor's social behaviour reduced child learning** | Kennedy, Baxter & Belpaeme 2015, doi:10.1145/2696454.2696457 | MEASURED-RCT |
| **N7** | Children learned **more from a human tutor than a social robot** | Kennedy et al. 2016, doi:10.1109/hri.2016.7451801 | MEASURED-RCT |
| **N8** | *"Robots or agents — **neither helps you more or less** during second language acquisition"* | Rosenthal-von der Pütten et al. 2016, doi:10.1007/978-3-319-47665-0_23 | MEASURED-RCT |
| **N9** | Immersive VR: **more presence, less learning** (EEG-instrumented) | Makransky et al. 2019, doi:10.1016/j.learninstruc.2017.12.007, 1,221 cites | MEASURED-RCT |
| **N10** | IVR learners **performed significantly worse on transfer**, reported higher arousal and more extraneous load, showed less EEG engagement — *with or without practice questions* | Makransky & Petersen 2020, doi:10.1111/jcal.12482 | MEASURED-RCT |
| **N11** | **When only immersion varies** (MR vs MR), meta-analytic effects go negative: **behavioural 0.04, cognitive −0.31, affective −0.51** — vs 0.40/0.84/0.65 against ordinary controls | Bödding et al. 2025, doi:10.1007/s10055-025-01118-z, k = 53 | MEASURED-META |
| **N12** | Sensory-integration treatment: **0.29 vs no treatment, but 0.60 in early studies → 0.03 in later ones**, and **0.09 (n.s.) vs active alternatives** | Vargas & Camilli 1999, doi:10.5014/ajot.53.2.189 | MEASURED-META |
| **N13** | **Alternative seating did not improve attention** (moderate strength of evidence), 21 level-I/II studies | *Frontiers in Pediatrics* 2025, doi:10.3389/fped.2025.1720179 | MEASURED-META |
| **N14** | **VLMs silently "fix" student errors while transcribing**, *"thereby hiding the very mistakes an educational assessment aims to detect"*; 15 SOTA models, substantial ranking reversals vs BLEU | arXiv:2604.22774 | MEASURED-BENCH |
| **N15** | Procedural mistake detection from egocentric video: *"machine performance in the wild remains **nonviable**"*; VLMs struggle off-the-shelf | arXiv:2412.11927 | MEASURED-BENCH |
| **N16** | **Environment backporting made reproducibility worse**, not better — 12,720 Kaggle notebooks, only **35.4%** still reproducible. Independently reproduces Pimentel's 2019 dependency-declaration penalty on a new corpus | arXiv:2602.07195 | MEASURED-BENCH |
| **O1** | **ORIGINAL:** marimo's reactive DAG **does not order mutation**. Identical cells with identical dependencies yield `total = 106` or `total = 6` **purely by source position**. Reactivity is a hazard reduction, not a guarantee | this survey, §B1.3 | MEASURED-BENCH |
| **O2** | **ORIGINAL, an absence:** **zero empirical evaluations of reactive notebooks as an instructional medium** exist in Crossref, ERIC, Europe PMC, arXiv or Semantic Scholar as of 2026-07-27. The misconception-prevention claim is untested | this survey, §B1.2 | OBSERVED — ABSENCE |

**Two more that belong on the register but are inherited rather than found here:** F10's
concreteness-fading nulls (four-plus, including a pre-specified equivalence test at
d = ±0.5), and C2's α ≈ 0.20 human grading baseline.

---

# D. HANDOFFS AND OPEN PROBLEMS

**To the survey.**

1. **Lead with the presence premium.** Three literatures, one number: **adding presence to
   a screen is worth ≈ 0.2 SD** whether the presence is an on-screen agent (g ≈ 0.19), a
   physical robot (d = 0.20), or immersion (ES = 0.24). It is a real effect and it is
   dwarfed by the choice of control condition (+0.75 → −0.06 *within the same
   meta-analysis*). **Every effect size in edtech below ~0.4 needs a control-condition
   moderator and a provenance moderator before it can be believed** — de Winter's
   Europe/non-Europe gap is **0.36 SD**, larger than the effect being estimated.
2. **The physical-vs-virtual question has no trustworthy pooled answer**, and the survey
   should say so. The two randomised, fidelity-documented head-to-heads are null; the one
   published pooled estimate has I² = 97.95% and a d of 1.6.
3. **Correct I1's generalisation, not its verdict.** Montessori's `S = 0` is right about
   *Montessori*. The transferable property is **refusal of illegal states**, and it is
   implementable in software.

**To G1 / the reference implementation.**

4. **T1 (reactive JS, 27 KB) is the default substrate for per-chapter mini-apps**; T3
   (Pyodide, 21.89 MB with the teaching stack, 4.5 s CPU) is capped at ≤3 chapters and must
   be argued for. Build the *refusal* and the *linking*, not the interpreter.
5. **`teachcheck`'s nine rules go into CI**, at ~38 ms per script, with a failing exit code.
   F3 already ruled that the substrate must be *"reactive… executed in CI from a cold
   container… failing the build on any cell error and on any assertion failure"*; §B5
   supplies the executable form and adds the assertion requirement G3 found missing.
6. **Camera-in requires three specific guardrails before it ships**: transcription and
   evaluation as separate calls; an **over-correction-penalised fidelity score** on the
   transcription (N14); and **false-negative rate reported separately** from accuracy,
   because the two harms land on different students.

**Open problems, honestly named.**

7. **O2 is a study waiting to happen and this project is positioned to run it.** *Does a
   reactive notebook reduce misconception formation relative to a sequential one?*
   Pre-register: same content, same tasks, marimo vs Jupyter, primary outcome a
   misconception inventory administered after the tool is withdrawn (H1's S1 design
   pattern). **N = 0 in the literature today.**
8. **The mutation hole is a teachable-moment opportunity, not just a defect.** A checker
   that flags cross-cell mutation in a *student's* notebook is buildable from the same
   read/write-set analysis FlowBook uses at **70 ms** overhead, and cross-cell mutation is
   itself a misconception worth surfacing.
9. **Gesture-rate detection from camera as a routing signal** (§A7.4-3) is, as far as this
   search found, unbuilt — and N1 says the routing decision it enables is worth roughly
   the difference between helping and harming half a classroom.
10. **`r-wasm/webr` has no SPDX-identifiable license.** Resolve before any redistribution.

---

# E. SOURCES

**Embodiment / gesture:** doi:10.1037/bul0000202 · doi:10.1177/0956797613518351 ·
doi:10.1016/j.dr.2015.07.007 · doi:10.1162/jocn.a.2588 · doi:10.1111/cogs.13479 ·
doi:10.1002/acp.4093 · doi:10.1111/desc.12664 · doi:10.1098/rstb.2023.0156 ·
doi:10.3758/s13423-016-1145-z · doi:10.1111/cogs.70055 · doi:10.3758/bf03209257 ·
doi:10.1037/0278-7393.26.3.671 · doi:10.1016/s0001-6918(97)00005-x ·
doi:10.4324/9781003322511-50 · doi:10.31234/osf.io/8x7yn ·
doi:10.1080/23273798.2026.2683465 · doi:10.1177/0956797614524581 ·
doi:10.1177/0956797618781773 · doi:10.1007/s10648-019-09468-2 (ERIC EJ1225471) ·
doi:10.1016/j.actpsy.2004.10.019

**Manipulatives:** doi:10.1037/a0031084 (ERIC EJ1007941) · doi:10.4018/jvple.2013070103
(ERIC EJ1154970) · doi:10.4018/978-1-4666-8847-6.ch009 ·
doi:10.1177/002205741319300204 · doi:10.4471/redimat.2014.46 · doi:10.1564/tme_v23.2.01 ·
doi:10.1007/s10639-023-12164-y · doi:10.35445/alishlah.v17i4.7586 ·
doi:10.1007/978-3-319-32718-1_4 · ERIC EJ1510953

**Robots / agents:** doi:10.3389/frobt.2025.1735198 (PMC13051544) ·
doi:10.1016/j.actpsy.2026.106576 · doi:10.2190/ec.49.1.a · doi:10.1145/2696454.2696457 ·
doi:10.3389/fict.2017.00006 · doi:10.1109/hri.2016.7451801 · doi:10.1109/hri.2016.7451757 ·
doi:10.1007/978-3-319-47665-0_23 · doi:10.1007/978-3-319-47665-0_44 ·
doi:10.1016/j.ijhcs.2015.01.001 · doi:10.1007/s12369-014-0277-4

**VR / AR:** doi:10.1111/bjet.13023 · doi:10.1016/j.edurev.2022.100434 ·
doi:10.1016/j.edurev.2022.100452 · doi:10.1016/j.learninstruc.2017.12.007 ·
doi:10.1111/jcal.12482 · doi:10.1037/edu0000241 · doi:10.1037/edu0000473 ·
doi:10.1111/jcal.12335 · doi:10.1007/s10055-025-01118-z · doi:10.58459/rptel.2027.22018 ·
doi:10.65138/ijramt.2025.v6i11.3157 · doi:10.3389/frvir.2024.1343872 ·
doi:10.3389/froh.2026.1768079 · doi:10.1007/s10055-023-00768-1 ·
doi:10.1016/j.compedu.2023.104931 · doi:10.1007/s11423-022-10139-3

**SELPA / sensory-motor:** doi:10.5014/ajot.53.2.189 · doi:10.3389/fped.2025.1720179 ·
doi:10.3389/fnint.2020.556660 · doi:10.3389/fpsyt.2025.1623149 · W3C WCAG 2.2 (2024-12-12)

**Vision / camera-in:** arXiv:2501.07244 (FERMAT) · arXiv:2604.22774 (PINK) ·
arXiv:2506.04822 · arXiv:2606.11477 · arXiv:2510.22798 (VEHME) · arXiv:2412.11927 ·
arXiv:2404.01933 · arXiv:2411.02570 · arXiv:2410.05343 · arXiv:2309.17024 ·
arXiv:2511.19684 · arXiv:2604.15134 · arXiv:2603.26400 · arXiv:2406.01486

**Notebooks / reproducibility:** arXiv:2605.01560 (FlowBook) · arXiv:2012.06981 (NBSafety)
· arXiv:2602.07195 · arXiv:2509.23645 · arXiv:2410.14393 · doi:10.1145/3313831.3376729 ·
doi:10.1145/3290605.3300500 · doi:10.1145/3173574.3173748 · doi:10.1038/d41586-018-07196-1
· ERIC EJ1369213 · ERIC EJ1344385 · ERIC EJ1488833 · ERIC EJ1419855 ·
Pimentel et al. MSR 2019 (via F3)

**Substrates (all repo/CDN/registry figures measured 2026-07-27):** pyodide/pyodide
`314.0.3` · marimo-team/marimo `0.23.15` · jupyterlite/jupyterlite `v0.8.1` ·
jupyterlite/pyodide-kernel `v0.8.2` · pyscript/pyscript `2026.7.2` · r-wasm/webr `v0.6.0`
· r-wasm/quarto-live `v0.2.0` · observablehq/framework `v1.13.4` · observablehq/runtime
`v6.0.0` · whitphx/stlite `1.8.1` · jupyter-book/thebe `0.9.3` ·
jupyterhub/mybinder.org-deploy `values.yaml` · repo.r-wasm.org PACKAGES (R 4.4) ·
repo.prefix.dev/emscripten-forge-dev

**Effect-size interpretation:** doi:10.3102/0013189x20912798 (Kraft 2020) ·
doi:10.3102/0013189x20985448 (Simpson's critique)

**Prior reports built on:** I1 (cost decomposition, mechanism-survival test, Montessori) ·
F10 (concreteness-fading correction, expertise reversal) · F3 (Pimentel figures, marimo
mechanism, Quarto freeze, grounding ladder) · G3 (xiaol measurement, Rot Rules, WASM
constraints, autograder health) · C2 (α ≈ 0.20, verifiable-vs-judgment split) ·
H1 (SELPA archetypes, WCAG floor, no-cognitive-training prohibition) ·
A2 (interactivity > motion)

**Original artefacts produced by this report** (committed at `evidence/F7-A3/`,
re-verified from that location on 2026-07-27):
`marimo_guarantees.py` (8 hazard classes × 3 execution models, marimo 0.23.15) ·
`swap.py` (the mutation-order discriminator) ·
`teachcheck.py` (9-rule conformance checker, ~200 lines, stdlib-only, 38 ms/script) ·
a 6-script conformance corpus with committed expected outputs and an injected
sign-flip mutation test (`evidence/F7-A3/corpus/`) ·
`browser-substrate-measurements.md` (the full substrate measurement log, ~48 KB,
`evidence/F7-A3/`).

*Reproduce:* `python3 evidence/F7-A3/teachcheck.py evidence/F7-A3/corpus` → exits 1,
4/6 conformant, 221 ms. `uv pip install marimo==0.23.15 && python3
evidence/F7-A3/marimo_guarantees.py` → the H1–H8 table. `python3
evidence/F7-A3/swap.py` → 106 / 6.
