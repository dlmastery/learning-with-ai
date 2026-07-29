---
title: "Greenfield — what you would build if none of it existed"
wave: N
date_researched: 2026-07-29
sources_count: 71
---

# Greenfield

> If you had no school, no textbook, no curriculum, no grade levels, no timetable, no exam
> and no teacher — and attention were free and a verifier existed — what would you
> actually build?

## §0 — Why this section exists, and the rule it runs under

On 2026-07-29 an audit of this project counted **756 critique markers against 24
construction markers across 33 sections, with 19 sections at exactly zero.** A 31:1
ratio. The cause was not temperament. It was the label set. `MEASURED-RCT`,
`MEASURED-META`, `MEASURED-BENCH`, `OBSERVED`, `VENDOR`, `DEMO`, `INFERENCE` — seven
labels, and not one of them can be attached to a thing that does not exist yet. A
standard that can only grade citations will only reward citation, and every round of
adversarial review deepens the asymmetry, because a reviewer can falsify a claim about
the past and cannot falsify one about the future.

Two labels are added here and used heavily.

- **`DESIGN`** — a specified artifact that does not exist. Not a wish. It states inputs,
  outputs and failure modes, it **names what would show it was the wrong design**, and it
  **cites the measured finding it is built on**. A `DESIGN` claim is never restated
  anywhere as a finding.
- **`OPEN`** — a question the field has not asked, as distinct from one it has failed to
  answer. It must state **why nobody asked it**.

Construction anchored to nothing measured is a pitch. Every design below carries its
anchor in the text, not in a footnote.

### The test that separates this section from the rest of the survey

For every proposal: **does it have a pre-AI analogue?** If it is a better version of
something that already existed, it is brownfield and it belongs in another section. Six
of this survey's thirty-three sections are already about doing existing things better.
This one is about artifacts with **no pre-AI analogue at all** — and where a proposal
turns out to be only a scaled-up version of something old, the section says so rather
than dressing it up. Two of the six designs below get that flag applied to them. That is
the discipline working, not failing.

### The three variables that actually changed

Everything here rests on three quantities, and it is worth stating them before the
designs so the reader can check each one against them.

1. **The marginal cost of one hour of a learner's undivided attention is
   ~US$0.05.** `INTERNAL-PRIOR` (F4 §"the section's central question", derived from
   measured per-token and per-audio-hour prices — Whisper Large v3 Turbo at $0.04 per
   hour of audio at 228× realtime, plus a measured token budget). This is the variable
   that every high-fidelity pedagogical tradition in history was rationing. I2's
   exclusion ledger makes the point better than a new argument could: "the traditional
   mechanisms are not expensive because they are good; they are good *and* they were
   affordable because they were exclusive," with roughly **90–95% of the population held
   ineligible** across the surveyed traditions.

2. **Error data now exists at population scale, and did not before.** The Eedi
   diagnostic-questions corpus released for the NeurIPS 2020 Education Challenge supplied
   "**over 20 million examples of students' answers to mathematics questions**," and the
   results paper frames the underlying problem as using "data on **hundreds of millions of
   answers** to MCQs" (Wang et al., arXiv:2007.12061; Wang et al., arXiv:2104.04034;
   nearly 400 teams, ~4,000 submissions). `MEASURED-BENCH`. Critically, these are
   *diagnostic* questions — "multiple-choice questions whose **distractors embody
   misconceptions**." Nothing of this shape existed before, at any scale, in any
   tradition.

3. **The check did not change.** K2's load-bearing finding: "**an agentic loop is worth
   exactly as much as the external check it closes on, and pedagogy is the domain where
   that check is hardest to build**" — the signal is slow, sparse and confounded. Across
   **223 real tutoring domains built from ground-truth ITS logs, no LLM beat chance at
   labelling an incorrect student action**; next-step correctness ran ~52–70% (TutorGym,
   Weitekamp, Siddiqui & MacLellan, arXiv:2505.01563). `MEASURED-BENCH`.

The brief for this section grants a verifier as a premise. That premise is doing enormous
work, and §4 pays for it honestly rather than spending it quietly.

---

## §1 — Interrogating the containers

Each of the following is an **administrative artifact**, not a fact about learning. For
each: where it came from, what constraint produced it, whether that constraint still
binds, and what replaces it.

The historical claims in this sub-section were researched fresh. **They are not in this
survey's existing corpus.** A grep across all 36 files in `research/raw/` for
`prussia|lancaster|lancastrian|monitorial|committee of ten|carnegie unit|quincy|philbrick`
returns **zero hits**. Everywhere the survey has previously invoked "the calendar," "the
credit hour," "grade-level staffing" or "seat time" as the constraint that killed mastery
learning, PSI, and competency-based education, it has done so as an unsourced
present-tense assertion labelled `INFERENCE`. That is a real gap in a 406,000-word corpus
and it is closed here, incompletely.

### 1.1 Age-graded cohorts — and the Prussian story, which does not survive checking

**The popular claim** is that American age-graded schooling was imported from Prussia in
order to manufacture obedient factory workers. It is repeated constantly, including by
people who should be more careful. It does not survive contact with the historiography,
and the way it fails is instructive.

The Prussian-borrowing thesis is not a modern internet artifact. It is a **specific
academic claim, made in 1916, and contested at the time.** F. Dean McClusky, writing in
*The Elementary School Journal* in 1920, opens:

> "There has never, until very recently, been any attempt in the history of education to
> explain the origin of the American graded system of schools. Nor is there any complete
> explanation of the four-year high school or its relation to the lower grades. In recent
> years this matter has come to the front and **is a subject of controversy**. Bunker, in
> 1916, published a monograph in which he advanced evidence to show that the present
> American system is **borrowed from Prussia**. **His interest in the matter is due to the
> fact that he sees in the present system a foreign and un-American type of organization
> which should be superseded by a new type of school system.** Judd takes the same
> position…"

McClusky, F. D. (1920), "Introduction of Grading into the Public Schools of New England,
Part I," *The Elementary School Journal*, doi:10.1086/454874 (Part II:
doi:10.1086/454893). `HISTORICAL`, full abstract retrieved, article body not retrieved.

Three things follow, and they matter.

**First**, the Prussian-origins story was advanced by a reformer who wanted the graded
system abolished, and the origin claim was **an argument in that campaign** — the system
is foreign, therefore un-American, therefore replaceable. The story's rhetorical function
predates its evidentiary status by a century.

**Second**, it was disputed by contemporaries who went looking for a domestic origin in
New England municipal practice. McClusky's two-part paper is that search.

**Third** — and this is the honest reporting the brief asks for — **I could not verify
either side.** I could not retrieve McClusky's body text, Bunker's 1916 monograph, or any
modern meta-historiographic adjudication. What I can report is that the standard modern
reference works on the topic locate the graded classroom in **urban administrative scale**
rather than in foreign import: David Tyack, *The One Best System: A History of American
Urban Education* (1974, doi:10.4159/9780674251120), and, very recently, Fanny Isensee,
*The Graded School: Reassembling Public School Organization in New York City, 1805–1921*
(Palgrave Macmillan, 2025). Neither was read in full.

**Verdict: `UNVERIFIED`.** The Prussian-origins claim should not be printed as fact by
this survey. What can be printed is the weaker and better-supported statement below.

**What is sourced is the constraint, and it is not ideological — it is arithmetic.** The
system that immediately preceded age-grading is the **monitorial or Lancasterian system**,
and its design parameters are documented. Joseph Lancaster's method was devised in late
eighteenth-century England explicitly "to keep educational costs down in order to continue
teaching poor people," and was "organized so that **one master teacher could instruct from
200 to 1,000 pupils at one time**," with pupils divided into groups of ten taught by
monitors (Ediger, ERIC 1987, `HISTORICAL`, tertiary). Its diffusion is well studied:
Tschurenev, "Diffusing Useful Knowledge: The Monitorial System of Education in Madras,
London and Bengal, 1789–1840," *Paedagogica Historica* (2008); Mesquita, "The Lancasterian
Monitorial System as an Education Industry with a Logic of Capitalist Valorisation,"
*Paedagogica Historica* (2012), doi:10.1080/00309230.2012.658159; Ressler, "Marketing
Pedagogy: Nonprofit Marketing and the Diffusion of Monitorial Teaching in the Nineteenth
Century," *Paedagogica Historica* (2013); Hogan, "Factories, Monitorial Schools and Jeremy
Bentham: The Origins of 'The Management Syndrome' in Popular Education," *Journal of
Educational Administration and History* (1973).

**And it is documented to have failed on quality.** Rayman, "Joseph Lancaster's Monitorial
System of Instruction and American Indian Education, 1815–1838," *History of Education
Quarterly* (1981): missionary schools adopted the system "but **abandoned it when it proved
ineffective**." `HISTORICAL`.

That is the whole story of age-grading, stated without the folklore: **a scarce adult
facing several hundred children needs a partition, and date of birth is the only variable
that is free to observe, impossible to falsify, and monotonic.** The monitorial system
partitioned by attainment and collapsed; the graded classroom partitioned by age and
persisted. It is a sorting heuristic chosen for its administrative properties, not its
predictive ones.

**Does the constraint still bind?** No. At ~$0.05 per learner-hour there is no scarce
adult to partition around.

**And the heuristic is measurably the wrong one.** Koedinger, Carvalho, Liu & McLaughlin
(2023), "An astonishing regularity in student learning rate," *PNAS* 120(13):e2221311120,
doi:10.1073/pnas.2221311120 — **1.3 million observations across 27 datasets**, individual
Additive Factors Model. Holding learning rate fixed, a student in the bottom half of
initial knowledge needs **13.13 opportunities** to reach 80% mastery of a knowledge
component and one in the top half needs **3.66** — a **3.6× spread**. Holding initial
knowledge fixed, the 25th and 75th percentiles of *learning rate* need 7.89 and 6.94
opportunities — a **1.14× spread**. `MEASURED-BENCH`. And, in the authors' words, this is
"a large difference for students who have **met course prerequisites**."

Read that last clause slowly. **The 3.6× spread is entirely inside the population the
system has already certified as ready.** Age-grading sorts on a variable with no
demonstrated relationship to the binding parameter, *within* a band the system says is
homogeneous. It was never a readiness test. It was a queue.

**What replaces it:** not "competency grouping" — that is the pre-AI analogue and it was
tried (see §7, rejected design 5). The replacement is developed as `N1-D5`, the
evidence-maintained graph, in which the question "is this learner ready?" is not asked of
a cohort at all but of a single edge.

### 1.2 The course, the credit hour, and the twelve-week unit

**Origin, as reported in the secondary literature:** the Carnegie unit was defined by the
Carnegie Foundation for the Advancement of Teaching in the first decade of the twentieth
century, as a by-product of establishing a free pension system for college professors —
which required a definition of what counted as a college, which required a definition of
adequate secondary preparation, which was operationalised as **seat time**. The best
available sources are Tompkins & Gaumnitz, "The Carnegie Unit: Its Origin, Status, and
Trends," *NASSP Bulletin* 48(288), 1964, doi:10.1177/019263656404828801; Shedd, "The
Carnegie Unit — How Did We Get It?", *Educational Forum*, 1970,
doi:10.1080/00131727009340411; and Silva, White & Toch, *The Carnegie Unit: A Century-Old
Standard in a Changing Education Landscape*, Carnegie Foundation for the Advancement of
Teaching, 2015.

**Honest flag: I retrieved metadata and author lists for all three and body text for
none.** The pension-fund origin account is consistent across the secondary literature but
is reported here as `HISTORICAL`, tertiary, unverified against a primary source.

What *is* verifiable is the modern regulatory descendant: 34 CFR 600.2, which yields a
3-credit semester course as **135 nominal student hours across 15 calendar weeks**
(`INTERNAL-PRIOR`, K1 §"Carnegie arithmetic", `INFERENCE` from the regulation).

**The constraint that produced it:** an accounting unit for a pension fund, generalised
into a unit of knowledge because no other unit was available. Nobody claimed at the time
that twelve or fifteen weeks was a natural quantum of understanding. The claim was that it
was an auditable quantum of *instruction delivered*.

**Does it still bind?** The regulatory constraint binds hard — F9 and I1 both correctly
identify accreditation and financial-aid rules keyed to seat time as *permission*
constraints AI does not touch. The **epistemic** constraint does not bind at all, and is
measured not to:

> "we find these learning opportunities are much more predictive of learning outcomes than
> calendar time (**a time-based model, time-AFM, systematically provides poor predictive
> fit**)." — Koedinger et al. 2023. `MEASURED-BENCH`.

The course is a unit of funding wearing the costume of a unit of knowledge, and the
mismatch is now quantified.

**What replaces it:** nothing, in the sense that no container of comparable rigidity
should be built. The unit that carries evidence is developed in §2.

### 1.3 The subject list — and a second story that is misremembered

The canonical high-school subject partition traces to the National Education Association's
Committee of Ten (convened 1892, reported 1893, chaired by Charles W. Eliot). The
sub-committee reports are documented — e.g. "First Efforts toward a National Curriculum:
The Committee of Ten's Report on History, Civil Government, and Political Economy,"
*Theory and Research in Social Education* (1992); "Foundations: The 1892 Committee of
Ten," *Social Education* (1988). `HISTORICAL`.

And here the pattern from §1.1 recurs, in the literature itself. Sheppard & Robbins, "High
School Biology Today: **What the Committee of Ten Actually Said**," *CBE—Life Sciences
Education* (2007), doi:10.1187/cbe.07-03-0013, exists specifically to "correct the
frequently held, but **erroneous** view" of what the Committee recommended about the
organisation of high-school biology. `HISTORICAL`.

**The general finding, and it is the most useful historical result in this section: the
origin stories of the containers are systematically misremembered, in both directions,
and by professionals.** Two of the three origin claims I attempted to verify turned out to
have a published correction attached — one from 1920 and one from 2007. A survey that
wants to abolish these containers should not do so on the strength of an origin story it
has not checked, because the origin stories are unreliable. Abolish them on the strength
of what they *do*, which is measurable now.

### 1.4 The timetable and the 50-minute period

**I could not source this and I am reporting it as unsourced.** No search of ERIC,
OpenAlex, Crossref or Semantic Scholar returned a primary account of the origin of the
50-minute secondary period.

What can be offered is an arithmetic `INFERENCE`, flagged as such: the Carnegie unit
standardised a year's study of a subject at roughly 120 hours. Distributed across ~180
school days at five meetings per week, that forces a class period of approximately 40–55
minutes. If that is the derivation, then **the length of a lesson is a rounding artifact of
a pension calculation**, which is a good line and one I decline to print as a finding
because I cannot support it. `INFERENCE`, `UNVERIFIED`.

What *is* measured is what the period does to time. The Beginning Teacher Evaluation Study
(Fisher et al. 1980, ERIC ED192454, `OBSERVED`, via K1 §2.1) decomposed allocated time into
engaged time into **academic learning time** — time on tasks at high success:

- Grade-2 mathematics **allocated** ranged **25–60 minutes/day** across classes; at
  sub-skill level, one class averaged **9 minutes of money arithmetic for an entire school
  year** against another class's **315 minutes**.
- Class-average engagement ranged **~50% to ~90%**.
- "The average student in the study spent **about half the time** working on tasks that
  provided high success. In grade five mathematics… **about one-third**."
- Worked extremes: **~4 minutes/day** of academic learning time at the bad end,
  **~52 minutes/day** at the good end. **A 13× spread inside identical timetables.**

The period is not a container of learning. It is a container of *allocation*, and the
measured conversion rate from allocation to learning varies by an order of magnitude
between two rooms in the same building.

### 1.5 The chapter and the textbook

A textbook is a physical object with a fixed binding, a single linear sequence, and a
revision cycle governed by print economics. A chapter is a unit of **typesetting and
reissue** — of what can be revised without resetting the rest. It is not, and has never
claimed to be, a unit of conceptual closure.

There is no origin mystery here and no controversy: the constraint is that paper is
sequential and expensive to change, and both halves of that constraint are gone.

**The measured consequence of the linear sequence** is the one this survey keeps
rediscovering from different directions. B1's expertise-reversal result — Tetzlaff,
Simonsmeier, Peters & Brod (2025), *Learning and Instruction* 98:102142,
doi:10.1016/j.learninstruc.2025.102142, **60 studies, 176 effect sizes, N = 5,924** — finds
high-assistance material helps low-prior-knowledge learners at **d = 0.505** and *harms*
high-prior-knowledge learners at **d = −0.428**, an interaction of **d = 0.971** with
**I² ≈ 90%**. `MEASURED-META`. A single fixed exposition cannot be on the right side of a
near-full-standard-deviation interaction for two readers at once. The authors' own
instructional implication is asymmetric and worth quoting because it constrains every
design below: *"rather provide assistance than to withhold it when in doubt."*

**What replaces it:** `N1-D3` and `N1-D4`.

### 1.6 The grade level, and "behind"

"Behind" is a statement about a person's position relative to a calendar. It contains no
information about what the person knows.

Three measured findings dissolve it.

1. **Koedinger's 3.6×**, above: half of any certified-ready cohort is, by construction, in
   the half that needs 13.13 rather than 3.66 opportunities. "Behind" describes a
   permanent structural half of every population and therefore describes nothing.
2. **Wheel-spinning is a property of the prerequisite, not the learner.** Wan & Beck
   (2015), EDM, ERIC ED560558, ASSISTments: "students in the **bottom 20% of pre-required
   knowledge exhibited wheel spinning behavior 50% of the time**, while those in the **top
   20%… only 10%**." `OBSERVED`. A 5× difference in stuck-ness, keyed to prior state.
3. **Learning rate barely varies.** 1.14×. `MEASURED-BENCH`.

Assembled: a child called "behind" is, with high probability, a child carrying an
unrepaired prerequisite, learning at within 14% of everyone else's rate, and being
described by a word that names neither fact.

Note the honest limit. K1 labels the *collapse* claim — that repairing the prerequisite
actually moves the initial-knowledge parameter — as `INFERENCE`, not measurement, because
**the repair-then-remeasure experiment has never been run.** That experiment is the hinge
of `N1-D5`.

### 1.7 The credential

**What does a diploma certify, to whom?** The cleanest measured answer in the literature is
close to *nothing beyond what the underlying schooling already signalled*. Clark &
Martorell (2014), "The Signaling Value of a High School Diploma," *Journal of Political
Economy*, doi:10.1086/675238: a regression-discontinuity comparison of the earnings of
workers who **barely passed** against those who **barely failed** high-school exit exams —
a design in which human capital is held essentially constant and only the piece of paper
differs — finds "**little evidence of diploma signaling effects**." `MEASURED-RCT`
(quasi-experimental, RD).

That is a striking result to hold next to the fact that the entire architecture of
schooling is organised around producing the document.

**Two structural facts about credentials, from this survey's own history section:**

- I2's analysis of the *ijāza* against the examination credential: the exam credential
  certifies "that you scored above a threshold on a sample of tasks, **once**"; the *ijāza*
  certifies that "a **named person** vouches that you can transmit a **named text**," and
  its chain "is public and inspectable." `HISTORICAL`. And its measured failure mode is
  **honorific inflation** — wealthy families obtaining grants for children incapable of
  understanding the material. I2's law: "a purely reputational credential inflates when the
  grantors' incentives shift."
- The W3C Verifiable Credentials Data Model 2.0 (W3C Recommendation, 15 May 2025) states
  it outright: "**Verifiability of a credential does not imply the truth of claims encoded
  therein.**" `OBSERVED`.

**So what could replace it that is not a worse credential?** Not a blockchain badge, not an
AI-issued certificate — I2 already names the latter as "a certificate with an **empty
signature field**," and §7 rejects it formally.

The replacement has to change the *thing being certified* rather than the issuing
authority. That is `N1-D2`.

---

## §2 — What is the atom?

This survey has assumed the unit of learning is a **topic** or a **concept**. That
assumption should be challenged, because the field's own best models of it perform badly.

**Candidate A: the topic / concept.** Status quo. Measured against it: the
knowledge-component alignment problem (Gervet et al., via F9 OP-6, `MEASURED-BENCH`) —
**expert-authored KC models add ≤ 0.01 AUC on 7 of 9 datasets**, and on **4 of 9** the KC
model is so poor that a skill-only model **loses to an item-difficulty-only model**. A
committee's decomposition of a subject into topics is, in nearly half of tested datasets,
worse than knowing nothing about the subject and only how hard each question is.

**Candidate B: the knowledge component.** Koedinger's unit. It has the strongest
quantitative footing of any candidate — **~7 opportunities (median 6.54) to 80% mastery**,
stable across 27 datasets, elementary through college, across mathematics, science and
language. `MEASURED-BENCH`. But K1 flags the load-bearing weakness itself: **N_kc, the
number of knowledge components in a body of material, is "an assumption, not a
measurement,"** and it calls this "the weakest link in the chain." And KC models are
hand-authored, which returns us to Candidate A's problem one level down.

**Candidate C: the demonstrable capability.** The atom is *a thing you can do, unassisted,
on a novel instance, weeks later*. Its attraction is that it is identical to the only
outcome this survey trusts (F9 OP-1). Its cost is granularity: a capability that takes
weeks to verify cannot be the unit you schedule against, because the scheduler needs a
decision every few minutes and the capability yields one every few weeks. This is K2's
"slow, sparse, confounded" restated as a units problem.

**Candidate D: the resolved confusion.** The atom is a specific wrong model that was
replaced by a specific right one.

**This is the candidate with no pre-AI analogue as a unit of curriculum**, for a precise
reason: **no author could enumerate the wrong models.** A textbook writer can enumerate
what is true; they cannot observe the distribution of what ten million readers believed
instead, because they never saw it. Misconception research exists and is old and good
(the Force Concept Inventory, diSessa's p-prims, Chi's ontological categories) but it is
interview-based, and its samples are in the dozens. The Eedi corpus is the first object
of the other kind: **20 million+ responses to items whose distractors were authored to
embody named misconceptions.** `MEASURED-BENCH`.

**Candidate E: the question you can now ask that you could not before.** Genuinely
attractive and currently unmeasurable. See `N1-O5`.

### The proposal

`DESIGN` **`N1-A1` — the atom is a transition, not a state.**

A knowledge component is a *state*: you have it or you do not. The unit that carries
evidence is a **directed pair — (wrong model *w*, correct model *c*)** — together with the
probe that distinguishes them and the intervention observed to move learners across it.

**Inputs.** A population-scale response corpus with distractor-level labels (the Eedi
shape). A set of probes. A record of which intervention preceded each observed crossing.

**Outputs.** For each transition: a prevalence (what fraction of learners occupy *w*), a
crossing rate per intervention type, and a **residence time** — how long learners sit in
*w* before crossing. None of these three quantities exists for any concept in any subject
today.

**Why the transition rather than the state.** Three measured reasons.

1. It is the unit the data is already in. A response to a diagnostic item is not evidence
   about a state; it is evidence about *which* wrong model is occupied. The state
   formulation discards the distractor and keeps the bit, and the discarded part is the
   larger part.
2. It is the unit the instruction is in. Tetzlaff's **d = 0.971** interaction says the
   correct instructional action depends on where the learner currently is, not on where
   they are going.
3. It is the unit that makes `N1-D5`'s graph *causal* rather than correlational, because a
   transition has a before and an after and can be intervened on. A state cannot.

**What would show this was the wrong atom.** If the crossing rate for a transition is
approximately **independent of the intervention** — i.e. learners leave *w* at the same
rate regardless of what was done to them, and the only predictor is total opportunity
count — then the transition carries no information the knowledge component did not already
carry, and Candidate B wins on parsimony. This is directly testable on existing Eedi-shape
data plus an intervention log, and it should be tested before anything else in this
section is built.

**Second falsifier, and the more likely one.** If **residence times are dominated by a
single "generic wrong" cluster** — if it turns out that most learners occupying *w* are not
occupying a *coherent* wrong model but are guessing — then the atlas in `N1-D1` is mapping
noise. The measurable signature is a distractor-choice distribution close to uniform across
the non-key options, conditional on ability. This is checkable today.

---

## §3 — Artifacts with no pre-AI analogue

Six designs. Each states inputs, outputs, failure modes, its measured anchor, and what
would show it wrong. Two carry an explicit **brownfield flag** where the honest answer is
that a pre-AI analogue exists in miniature.

### `N1-D1` — The error atlas

`DESIGN`. **Brownfield flag: partial.** Misconception research is a pre-AI field. What has
no analogue is the *census*: complete, live, versioned, population-scale, and public. The
novelty is in kind of object, not kind of question, and the section says so.

**What it is.** A public, shared, versioned map of how humans actually get a concept
wrong — one entry per transition in the sense of `N1-A1`, with prevalence, residence time,
demographic stratification, and the probes that discriminate.

**Why no textbook has ever contained one.** Because no author could observe it. This is not
a criticism of authors; it is a statement about what was observable. The observability
changed in 2020, and nobody has built the map.

**Anchor.** Eedi / NeurIPS 2020 Education Challenge (arXiv:2007.12061, arXiv:2104.04034),
`MEASURED-BENCH` — 20M+ responses, distractors authored to embody misconceptions, four data
mining tasks, ~400 teams. **Critically, every one of those four tasks was a *prediction*
task** — predict the student's answer, predict item quality, sequence items. **None was a
cartography task.** The corpus that would support an atlas was built, competed over, and
used for something else. That is the gap.

**Inputs.** Distractor-labelled response streams; a misconception vocabulary (initially
seeded by teachers, subsequently revised by clustering); demographic strata sufficient for
subgroup analysis and no finer.

**Outputs.** Per concept: a ranked list of occupied wrong models with prevalence and
uncertainty; the discriminating probe set; the observed crossing interventions with rates.
Published openly, versioned, with a changelog — the atlas is a scientific object, not a
product feature.

**Failure modes.**
- *Misconception vocabulary drift.* If the labels are revised faster than the prevalence
  estimates converge, no entry is ever stable.
- *Correct-answer contamination.* Measured, and severe. arXiv:2606.23205, "The Correct
  Answer Trap," using **20,964 real student responses from Eedi**: automated systems that
  rely on answer correctness will **reinforce** misconceptions when students reach the
  correct answer through flawed reasoning. Fine-tuned classifiers detect **57%** of these
  hidden misconceptions; an open-weight reasoning model detects **84%**, but at realistic
  prevalence **false alarms outnumber genuine detections roughly 8 to 1**.
  `MEASURED-BENCH`. An atlas built only from wrong answers is systematically missing the
  wrong models that produce right answers, and that missing set is not small.
- *Population non-transfer.* See falsifier.

**What would show it was the wrong design.** **If the clusters do not survive a second
population.** The measured warning is direct: trace-based learner models are found **not to
generalise across national populations** (Finland / Slovakia / US, PIAAC 2012; ERIC
EJ1501422, Gorgun & Yildirim-Erbasli 2026, `OBSERVED`, via F9 OP-5/OP-15). If the
prevalence ranking of wrong models for, say, fraction division reorders substantially
between two countries with different curricular sequences, then there is no atlas — there
are national atlases, and a single published one is a curricular monoculture wearing the
costume of a scientific finding. **This is the falsifier for five of the six designs
below, because they all read from the atlas.** It should be tested first and cheaply: two
existing distractor-labelled corpora from different school systems, one rank correlation.

**Second falsifier.** If knowing *which* wrong model a learner occupies does not beat
knowing only *that* they are wrong — i.e. if an intervention conditioned on the specific
misconception does not outperform a generic corrective on a delayed unassisted novel-item
outcome — the atlas is an expensive way to learn nothing. That is a two-arm trial and it
is the cheapest experiment in this section.

### `N1-D2` — The decaying capability portfolio

`DESIGN`. **No pre-AI analogue.** Every existing record of learning is a record of *past
events* — a transcript, a certificate, a licence. None of them decays continuously,
because none of them was ever connected to a live measurement. Professional licences
expire on a calendar, which is a different object: a discrete administrative reset, not a
decaying estimate.

**What it is.** A learner-held record whose entries are **current capability estimates with
confidence intervals that widen with time since last evidence**, and which can be
**re-verified on demand** by a probe. Not "she passed Algebra II in 2024." Rather: "as of
this morning, unassisted, on novel items, P(succeeds at solving a two-step linear equation
in a word-problem context) = 0.86 [0.79, 0.91], last evidenced 11 days ago."

**Anchor, and it is the sharpest one in this section.** Arthur, Bennett, Stanush &
McNelly (1998), "Factors That Influence Skill Decay and Retention: A Quantitative Review
and Analysis," *Human Performance*, doi:10.1207/s15327043hup1101_3 — meta-analysis of
**189 independent data points from 53 articles**. "There is **substantial skill loss with
nonpractice or nonuse**, with the amount of skill loss ranging from an effect size of
**d = −0.01 immediately after training to d = −1.4 after more than 365 days of nonuse**."
And the moderator that matters: "**Physical, natural, and speed-based tasks were less
susceptible to skill loss than cognitive, artificial, and accuracy-based tasks.**"
`MEASURED-META`.

Read that against the transcript. **A transcript asserts a constant. The underlying
quantity is measured to fall by up to 1.4 standard deviations in a year, and to fall
fastest for exactly the cognitive-accuracy skills that transcripts are mostly about.** The
error of the transcript is not random; it grows monotonically, and it grows fastest where
the transcript is most confident.

That is a defect with no defender. Nobody argues that a grade from four years ago
describes current capability. The reason we use it anyway is that re-measurement was
unaffordable. At $0.05 per learner-hour it is not.

**Inputs.** A probe bank (see `N1-D3`); a decay model per capability class initialised from
Arthur et al.'s moderators and updated per-learner; an event log of unassisted performances
in the wild.

**Outputs.** A portfolio the learner holds and controls, presentable in whole or in part,
with every entry carrying its evidence date and its confidence interval. Re-verification is
a probe the learner *initiates*, and its result is written whether or not it is favourable
— this is non-negotiable and is the difference between a portfolio and a marketing asset.

**Failure modes.**
- *Gaming by selective re-verification.* If the learner may re-probe until a favourable
  result and then freeze, the portfolio is a high-water mark, which is a transcript with
  extra steps. **Mitigation: every probe is recorded, the count is part of the record, and
  the estimate is the posterior over all probes, not the maximum.**
- *The probe becomes the construct.* Solved only if `N1-D3` works.
- *Decay-model misspecification.* Arthur et al.'s **I²** and moderator structure mean a
  single global decay curve is wrong. Per-learner, per-capability estimation is required,
  and that requires more probes than the learner will tolerate. This is the design's real
  cost and it is not small.

**What would show it was the wrong design.** **If the decay estimate does not predict
unassisted performance in the wild better than the last recorded score does.** That is a
single comparison against a trivially available baseline and it is the whole ballgame. If a
2024 grade predicts a 2026 unassisted performance as well as a decay-adjusted estimate
does, the portfolio is machinery around a variable that was not moving.

**Second falsifier, and the one I expect to bite.** The 350-million-review spaced-repetition
result already in this corpus: **a zero-parameter moving average beats every released FSRS
version on log loss** (`INTERNAL-PRIOR`, F5 via F9 OP-6). If the same holds here — if a
naive "assume it decays at the population average" estimator beats a fitted per-learner
model — then the personalised half of the portfolio is decorative and only the *decay* idea
survives. That would still be a useful result and a much cheaper artifact.

**The consequence I am obliged to name and do not like.** A live, continuously updated,
comparable estimate of what a person can currently do is also a surveillance object of a
kind that has never existed. §4.5 develops this. It is not a reason not to build it; it is
a reason the custody question (`N1-O7`) is a design constraint and not a policy footnote.

### `N1-D3` — The object that is the same object and never the same instance

`DESIGN`. **Brownfield flag: partial.** Automatic item generation is a pre-AI field with a
literature. What has no analogue is the *inversion* below.

**What it is.** A learning-and-assessment object defined by a generator with declared
parameters, such that no two encounters are the same instance, and such that the
**variation itself is the measurement** rather than noise to be suppressed.

**Anchor — and this one is a published account of the design failing.** Westacott, Badger,
Kluth, Gurnell & Reed (2023), "Automated Item Generation: impact of item variants on
performance and standard setting," *BMC Medical Education*,
doi:10.1186/s12909-023-04457-0. Fifty MCQ item models generated four isomorphic 50-item
papers, standard-set by modified Angoff, delivered to **2,218 final-year students at 12 UK
medical schools**. Results: average facility across papers ranged **0.55–0.61**, cut scores
**0.58–0.61** — but **20 of 50 item models had a facility difference > 0.15** and **10 had
a standard-setting difference > 0.1**. The authors' conclusion: "**Item facility varied to a
greater extent than the standard set**," and "variation in parameters that could alter
clinical reasoning strategies had the greatest impact on item facility." `MEASURED-RCT`
(controlled multi-site comparison).

The standard reading of that result is that isomorphic generation is not yet reliable
enough for high-stakes use. **The greenfield reading is the opposite: the human
standard-setters could not see the difficulty variation that the students could.** Expert
judgement was *flatter* than reality. The variance is real, it is large, and it is
invisible to the instrument we currently use to certify items.

**The inversion.** Stop trying to make the variants identical. Declare the generator's
parameters, **measure the difficulty surface across the parameter space at population
scale**, and treat a learner's success profile *across that surface* as the construct.
Under this design, an item is not "a question of difficulty 0.58"; it is **a function from
parameter settings to success probability**, and what you know about a learner is which
region of that function they command.

This has no pre-AI analogue because it requires (a) generation at zero marginal cost and
(b) enough responses per parameter cell to estimate the surface. Both arrived at once.

**Inputs.** A parameterised generator with named, ordered parameters. A response corpus
dense enough to estimate a difficulty surface — this is the binding constraint and the
number is unknown (`N1-O3`).

**Outputs.** A difficulty surface per object; per learner, a command region; and, as a
by-product, the **first empirical account of what actually makes a problem hard**, which
does not currently exist for any topic.

**Failure modes.**
- *The surface is not smooth.* If success probability jumps discontinuously across
  neighbouring parameter settings, there is no surface and the object is a bag of unrelated
  items.
- *Interaction with `N1-D1`.* Westacott found the largest facility swings came from
  "parameters that could alter clinical reasoning **strategies**" — i.e. the parameters
  that switch which *wrong model* is available. That is not a nuisance; it is the atlas
  showing up inside the item. It is also the reason the two designs must be built together
  or not at all.
- *Reliability theory does not cover this.* F9 OP-3 already establishes that Cronbach's α
  is **undefined** when items are generated per learner. Do not repeat OP-3; note only that
  this design makes OP-3 *more* urgent, not less, and that OP-3's proposed
  generalisability-theory answer (a crossed p × i:g × o G-study with the generator as a
  facet) is the right instrument for it.

**What would show it was the wrong design.** **If between-variant variance in a single
person's success is not predictable from the declared parameters** — i.e. if, after
conditioning on ability and on every parameter the generator exposes, residual variance
across variants remains as large as the parameter-explained variance — then the parameters
are not the construct, the surface is not estimable, and this is an expensive way to write
inconsistent items. Westacott's own thematic analysis is the pilot: they found the
high-variance models *were* thematically characterisable. That is encouraging and it is
n = 50 items in one domain.

### `N1-D4` — The derivation rooted in the learner's own wrong model

`DESIGN`. **No pre-AI analogue in the form specified**, though the neighbourhood is
occupied: bridging analogies, conceptual-change instruction, and refutation texts are all
pre-AI. What is new is per-learner derivation *from an observed occupied model*, which
requires `N1-D1`.

**What it is.** An explanation that does not start from the canonical starting point. It
starts from **the model the learner is measured to hold**, continues that model faithfully
until it produces a consequence the learner can check and finds false, and then repairs the
specific step that produced the false consequence — leaving everything else the learner
believed intact.

**Anchors, and there are two, pulling in opposite directions.**

*In favour:* Tetzlaff et al. 2025's **d = 0.971** interaction establishes that prior
knowledge is the single best-supported basis for adaptation, and B1 says so in those words.
But every deployed instantiation of that finding adapts one dimension — **how much
scaffolding**. Nobody adapts the *origin of the derivation*. That is a strictly richer use
of the same measured moderator.

*Against, and it must be printed:* Barbieri, Miller-Cotto, Clerjuste & Chawla (2023),
"the first proper meta-analysis" of worked examples, *Educational Psychology Review*,
doi:10.1007/s10648-023-09745-1 — screening **8,033 abstracts** to **43 articles / 55
studies / 181 effect sizes**, robust variance estimation, **g = 0.48**. Two moderators are
direct warnings against the naive version of this design:

- "**Correct examples alone outperformed incorrect-only or correct+incorrect
  combinations.**"
- "**Pairing examples with self-explanation prompts significantly *reduced* the effect**" —
  the authors: "pairing examples with self-explanation prompts may not be a fruitful design
  modification."

`MEASURED-META`. Showing learners wrong work is measured to be worse than showing them
right work. That is the strongest single counter-argument to this design and it exists
already.

**The distinction the design turns on.** Barbieri's incorrect examples are *someone else's*
errors, presented as objects to study. This design presents *the learner's own currently
occupied model*, applied by the system as though it were true, until it breaks on a case
the learner can verify. Those are different interventions with different mechanisms — the
first is study of an artifact, the second is disconfirmation of a live commitment — and
this survey's teachable-agent thread (F9 OP-7) rests on the same distinction. **But the
distinction is untested, and Barbieri is the prior.** Anyone building this should expect to
lose.

**Inputs.** An atlas entry with a discriminating probe (`N1-D1`); a check the learner can
run themselves — an execution result, a physical observation, a numerical case — because the
disconfirmation must come from the world and not from the system's assertion.

**Outputs.** A derivation whose first line is the learner's, and a repair localised to one
step.

**Failure modes.**
- *Absorption rather than repair.* survey §21 §7 flags this against ourselves: "a confident
  agent demonstrating a wrong procedure across several worked examples is, from a different
  angle, a very effective way to teach that wrong procedure." This is the same risk in a
  different costume and it inherits the same unstudied status.
- *No checkable consequence exists.* For many humanities and conceptual-science
  misconceptions there is no cheap case the learner can run. The design's domain is
  narrower than it first appears — it works where a verifier exists, which returns us to
  K2's rule.

**What would show it was the wrong design.** **If learners receiving the
misconception-rooted derivation do worse on a delayed, unassisted, novel-item outcome than
learners receiving the canonical derivation.** Barbieri predicts they will. A two-arm
trial, matched on total instructional time, with the delayed-unassisted primary outcome, is
the whole test. **If it loses, this design should be deleted and Barbieri should be
believed** — and the section commits to that in advance.

### `N1-D5` — The curriculum as a graph maintained by intervention

`DESIGN`. **No pre-AI analogue.** Prerequisite graphs are old. Prerequisite graphs whose
edges are *added and removed by continuous randomised probing* are not, because the probes
were unaffordable and the response volume was absent.

**What it is.** A curriculum in which an edge A → B exists **if and only if repairing A
measurably reduces opportunities-to-mastery on B**, established by intervention rather than
by fit, and re-checked continuously.

**Anchor, positive.** Cen, Koedinger & Junker (2006), "Learning Factors Analysis — A
General Method for Cognitive Model Evaluation and Improvement," LNCS,
doi:10.1007/11774303_17. `MEASURED-BENCH`. The measured fact is that hand-authored
cognitive models **can be improved from data**. Committees are beatable, and the machinery
to beat them is twenty years old.

**Anchors, negative, and they are why this design is specified the way it is.**

1. **Fit is not instruction.** Rollinson & Brunskill (2015), EDM, ERIC ED560516: "student
   models with **similar predictive accuracies** can suggest **substantially different
   amounts of practice**… predictive accuracy may not be a sufficient metric by itself when
   choosing which student model to use." `OBSERVED`. A graph learned to maximise held-out
   AUC is not a graph that implies correct instruction, and this is measured, not argued.
2. **The prediction ceiling is low and already reached.** Cleaned of leakage, PFA matches
   DKT; IRT variants match or beat DKT on all tested datasets; SAKT fails independent
   replication on all nine (0.85 reported → 0.73 observed). `MEASURED-BENCH` via F5/F9.
   There is no more signal to be had by fitting harder.
3. **Expert KC models add ≤ 0.01 AUC on 7 of 9 datasets** (Gervet et al.). The
   hand-authored graph is worth almost nothing predictively — which is either an
   indictment of the graph or evidence that prediction is the wrong target. Given (1), it
   is the second.

**The move.** Stop fitting the graph and start **intervening on it**. K1 names the required
experiment exactly once and treats it as a single study:

> "**The repair-then-remeasure experiment.** Koedinger's 13.13 → 3.66 gap is measured.
> Whether diagnosing and repairing the missing components *moves a learner's
> initial-knowledge parameter* — and by how much — **has not been tested**. This is the
> experiment that would convert the largest term in §7.3 from `INFERENCE` to `MEASURED`."

**This design's extension past K1 and F9 is to run that experiment continuously, as the
curriculum's own maintenance loop, on every edge, forever.** Not one study establishing one
number; a standing policy in which a small randomised fraction of every learner's
opportunities is spent probing edges whose evidence has gone stale. The curriculum stops
being a document and becomes a **running experiment with a version number**.

**Inputs.** Per-KC mastery estimates; a probe budget expressed as a fraction of
opportunities; an edge register with per-edge evidence age and effect estimate.

**Outputs.** A directed graph with an effect size and a date on every edge. Edges below a
threshold are **deleted**, publicly, with the date — this is the artifact's most valuable
output and no curriculum has ever produced it. Every curriculum in history has only ever
accumulated.

**Failure modes.**
- *The probe budget is unaffordable.* Rafferty, Williams & Ying (2019), JEDM, ERIC
  EJ1220507: adaptive and bandit assignment **cost false-positive rate and statistical
  power** in educational experiments. `OBSERVED`. That cost is real and this design pays it
  continuously.
- *Confounding by the learner's own trajectory.* K2: the signal is "confounded — the
  learner is also changing for other reasons."
- *Edges are not stable across populations.* Same falsifier as `N1-D1`.

**What would show it was the wrong design.** **If the probe budget required to establish
one edge to a useful precision exceeds the instructional value of knowing it.** This is
arithmetic and it can be done now. Take K1's worked scenario: ~20 knowledge components per
"week" of material, ~7 opportunities each, ~90 seconds per opportunity — around 3.3 hours
of median-learner effort and roughly 140 opportunities. If establishing one edge at
adequate power consumes, say, 40 opportunities across a learner population, the question is
how many edges the population can afford per unit time and whether the graph converges
before the curriculum changes underneath it. **Nobody has computed this.** See `N1-O3`.

If the answer is that it does not converge, the honest fallback is the *static* version:
run the repair-then-remeasure experiment once, on the highest-prevalence edges only, and
accept a mostly-unverified graph with a small verified core. That is a much smaller claim
and still an improvement on a graph with no verified edges at all, which is what every
curriculum currently is.

### `N1-D6` — The probe that is scored downstream

`DESIGN`. **No pre-AI analogue.** Formative assessment is pre-AI. A probe whose *score is
not computed at the time of the response* is not, because deferring the score required
being able to observe the learner's later unassisted acts, which required persistence and
free attention.

**What it is.** A single object that is simultaneously the instruction and the assessment,
resolving the contradiction by **separating the moment of instruction from the moment of
scoring**. The learner responds; the system responds instructionally *immediately*; the
**probe's score is assigned later, from whether the learner's subsequent unassisted
performance on a related, novel item succeeded.**

**Anchor, positive, and it is the best-replicated finding in the corpus.** Yang, Luo,
Vadillo, Yu & Shanks (2021), *Psychological Bulletin*, doi:10.1037/bul0000309 — retrieval
practice in classroom settings, **g = 0.499, 95% CI [0.442, 0.557], I² = 88%, from 222
studies and 48,478 students**. `MEASURED-META`. Corroborated by Rowland (2014), g = 0.50,
and Adesope et al. (2017), g = 0.51 against restudy.

The implication is rarely stated in its strong form: **the single largest well-replicated
effect in learning science says that the act of being tested is an act of learning.
Separating assessment from instruction is therefore not an administratively neutral choice.
It is measured to throw away the largest lever available.**

**Anchor, constraining.** Rowland (2014) and Fiechter & Benjamin (2018): unsuccessful
retrieval **without corrective feedback** produces little or negative benefit. So the probe
must carry feedback — which under classical validity theory contaminates it as a
measurement. Hence the deferral.

**Anchor, obstructive, and it is decisive for how the score is computed.** The correct
answer trap, twice measured:

- arXiv:2605.23925, "Catching The Correct Answer Trap": on real Eedi responses, **71% of
  model failures concentrate in just two question types**, both sharing a structure where
  flawed reasoning happens to produce the correct numerical answer. Fine-tuned T5 vs a
  frontier LLM: **57% vs 84% detection accuracy**. "Even the best-performing model generates
  **roughly four false alarms for every genuine detection**, making stand-alone screening
  impractical at realistic class sizes." `MEASURED-BENCH`.
- arXiv:2606.23205, 20,964 responses: **8:1** false alarms at realistic prevalence.

**Therefore the probe cannot be scored on answer correctness (it misses the hidden
misconceptions) and cannot be scored by a model judging method validity (8:1 false alarms,
and TutorGym's chance-level result on the simpler binary task).** Both cheap scorers are
measured to be broken. What remains is the expensive one: **score the probe by what the
learner subsequently does unassisted.** That is the design.

**Inputs.** A probe; an immediate instructional response; a scheduled downstream unassisted
novel item at a delay; a credit-assignment rule mapping downstream outcomes back to
upstream probes.

**Outputs.** A probe score that is late, noisy, and *valid*, plus the instruction the
learner already received regardless.

**Failure modes.**
- *Credit assignment is under-determined.* Many probes precede any downstream outcome.
- *Sparsity.* K2 states the constraint numerically: "a learner produces **a few dozen
  scorable acts per hour**, not a few thousand." The credit signal is orders of magnitude
  thinner than any RL setting where this technique works.
- *The learner notices the delay.* If probes never return a score, the retrieval-practice
  benefit — which depends on effortful retrieval *with corrective feedback* — may survive
  (feedback is immediate) or may not (the stakes are gone). Untested.

**What would show it was the wrong design.** **If downstream credit is too sparse to
distinguish any two probes.** The arithmetic: with a few dozen scorable acts per hour and a
downstream outcome measured at weeks, a single learner supplies on the order of hundreds of
probe–outcome pairs per term against a probe bank of thousands. **Pooling across learners
with per-learner shrinkage is mandatory** — K2 identifies exactly this constraint for its
own proposed optimiser — and if the pooled estimate does not separate probes that a
domain expert can separate by inspection, the deferral bought nothing and the design should
revert to expert-authored probe quality.

---

## §4 — What becomes possible when attention is free and the loop closes

This survey establishes that a **delayed, unassisted, novel-item outcome is the only
trustworthy signal**, and that it is slow and sparse. The brief grants, as a premise, that
it becomes dense and fast. Following that premise honestly produces four consequences, and
at least two of them are unwelcome.

### 4.1 Pedagogy becomes a search problem rather than a craft

K2 names the object and states plainly that nobody has attempted it:

> "**A GEPA-class optimiser whose fitness function is measured human retention at delay has
> never been attempted by anyone.**"

The optimiser machinery exists and its gains are measured: GEPA at **+6% average and up to
20% over GRPO with 35× fewer rollouts**, and **>10% over MIPROv2**; DSPy at **>25%
(GPT-3.5)** and **65% (llama2-13b-chat)**; PromptBreeder taking PaLM 2-L from **59.3% to
83.9%** on GSM8K. `MEASURED-BENCH`. Every one of those numbers was obtained against a
**cheap automatic check**.

If the delayed-unassisted check becomes cheap, the whole apparatus points at pedagogy, and
the consequence is that **instructional design stops being a matter of opinion within a
few weeks of the switch being thrown.** This is the single largest thing that changes, and
it changes something the field has never had: an arbitration procedure.

It also means every mechanism this survey has proposed becomes falsifiable on a timescale
of weeks. Including — and survey §21 already commits to this — the ones we like. §21's
concession condition is a well-powered trial landing *inside* 0.2–0.4 SD. Under a dense
check, that trial runs continuously and returns a verdict on each mechanism separately
rather than on the assembled bundle. **That is strictly worse for the survey's thesis and
strictly better for the field**, and the section should want it.

### 4.2 The optimiser will find the wrong thing first, and this is measured

Three findings, all already in the corpus, say what a dense loop will do if pointed
carelessly.

- **Felt and real learning move in opposite directions.** Deslauriers, McCarty, Miller &
  Callaghan (2019), *PNAS*, doi:10.1073/pnas.1821936116: randomised passive lecture vs
  active learning with identical materials — students in the active classroom **learned
  more but felt they learned less**, mediated by increased cognitive effort.
  `MEASURED-RCT`. B1's summary is the design constraint: "any system that optimizes for
  learner-reported satisfaction, felt fluency, or in-session performance will
  **systematically select against** the interventions with the best long-term evidence.
  This is a measurable, predictable failure mode, not a hypothetical one."
- **Time on task is not the signal.** Kestin et al. (2025), *Scientific Reports* 15:17458,
  doi:10.1038/s41598-025-97652-6, N = 194 crossover: median AI-arm time on task **49
  minutes** against a 60-minute in-class hour, with **d ≈ 0.63 more learned** — and
  "**there was no correlation between the time on task and students' post-test scores**."
  `MEASURED-RCT`.
- **The sign flips when the window widens.** Unguarded LLM access: **+48% during access,
  −17% once withdrawn** (Bastani et al. 2025, *PNAS*, doi:10.1073/pnas.2422633122).
  `MEASURED-RCT`.

The honest form of the consequence: **a dense check does not remove the risk of optimising
the wrong thing. It industrialises whichever thing you point it at.** The only protection is
that the fitness function is the delayed unassisted outcome and nothing else, which is
expensive precisely because it is the only one that works.

### 4.3 The uncomfortable one: the check is a measurement of a child

A dense, fast, delayed-unassisted signal is, viewed from any angle other than the
engineering one, **a continuous behavioural measurement of a minor**, retained, modelled,
and acted upon.

F9 OP-19 already asks whether clickstream-derived affect detection falls inside EU AI Act
Art. 5(1)(f). This is the adjacent and larger question and it is not the same one: not
whether inferring *emotion* is prohibited, but what it means that **the artifact that makes
the whole design work is also the artifact that makes it dangerous.**

The section's design commitment, stated as a constraint on everything above rather than as
a separate artifact: **the check is possessed by the learner.** The probe results, the
portfolio, the atlas entry the learner occupies — these are held by the learner and the
learner's guardian, presentable in part, deletable in whole, and the system's access is by
grant and revocable. This is not a privacy position (who may see it) but a **custody**
position (who holds it), and the distinction is the subject of `N1-O7`.

This costs the design real capability. A portfolio the learner can delete is a portfolio
that can be gamed by deletion, and §3's `N1-D2` explicitly forbids selective
re-verification. Those two commitments are in tension and I do not have a clean resolution.
**Stating the tension is better than resolving it by quietly dropping one.**

### 4.4 The consequence the survey has already named and not followed

survey §21 §5: "Every effect size in this document was measured in a world where the
treatment group had something the control group did not… If a tutor lifts everyone by 0.4
SD, the *absolute* learning is real and the *positional* benefit is zero."

Follow it into this section's designs and it gets worse, not better. `N1-D2` produces a
**live, continuously updated, directly comparable estimate of what every person can
currently do.** Under scarcity, credentials were coarse, stale, and hard to compare —
which is a defect from the measurement point of view and a **protection** from the
positional point of view. A grade from four years ago is a bad estimate of capability and
therefore a weak instrument of sorting.

**Sharpen the estimate and you sharpen the sort.** A world with a perfect live capability
portfolio for every person is a world in which every hiring, admission, and assignment
decision has a better instrument, and in which the people at the bottom of the distribution
are visible with a precision no previous era achieved. This survey's own exclusion-ledger
finding is that high-fidelity traditions bought quality by rationing access. **The failure
mode of this design is different and possibly worse: it does not ration access, it rations
nothing, and it makes the ranking exact.**

I do not have a design answer to this. It is the strongest argument against `N1-D2` and it
comes from inside the survey. See rejected design 7 in §7, which is the same artifact with
the custody constraint removed, and which should not be built.

---

## §5 — What should not be rebuilt, and what must be

Greenfield is also the freedom to delete. It is not the freedom to forget why things are
there. A design that ignores that school is also a **building** will fail on contact with
parents, and it should, because the building is doing measured work.

### 5.1 Things that exist for reasons that are still valid

**Safeguarding. This is the strongest item on the list and it is measured.** Chen & Dube
(2025), "School closures, child maltreatment reporting and victimization during the
pandemic," *Child Abuse & Neglect*, doi:10.1016/j.chiabu.2024.107243 — linking child file
data from the **National Child Abuse and Neglect Data System** to the **U.S. School Closure
& Distance Learning Database**, county-month level, **January 2018 – May 2022**, estimating
the effect of closures on maltreatment reports **by reporting source and maltreatment
type**. The paper's premise, stated in its own opening: "**School closures during the
pandemic correlated with declines in child maltreatment reports in the U.S.**"
`OBSERVED` (quasi-experimental panel; abstract retrieved, body not). Corroborated for a
single state and a single maltreatment type by Georgia NCANDS analysis,
doi:10.1016/j.chiabu.2025.107434.

The design implication is blunt: **the school building is a sensor.** Roughly a fifth of
maltreatment referrals in the US come from education personnel; when the children stop
being seen, the referrals stop, and the maltreatment does not. **No artifact in §3 replaces
this and none of them should pretend to.** An AI tutor that a child uses alone at home
removes the child from the field of view of the only adults legally obliged to look.

**Childcare.** Amuedo-Dorantes, Marcén, Morales & Sevilla (2022), "Schooling and Parental
Labor Supply: Evidence from COVID-19 School Closures in the United States," *ILR Review*,
doi:10.1177/00197939221099184 — district-level closure data merged to CPS individual data,
Jan 2019 – May 2020, difference-in-differences: "**non-negligible labor supply
reductions**," offset partly by a partner at home, and with "a **long-lasting negative
impact** on parental labor supply." `OBSERVED`.

School is load-bearing infrastructure for the labour market, and this is measured rather
than asserted. Any design that assumes a supervising adult at home is a design for a
minority of households.

**Somewhere to be.** Downstream of both of the above and not separately measured here.

**A peer group.** I2's chavruta analysis is the relevant finding and it cuts against the
naive design: of chavruta's four mechanisms, **forced articulation survives digital
substitution and "symmetric stakes" and "durable pairing with social cost" DIE.**
`INFERENCE`, but well-argued and grounded in the multi-agent-debate literature (Smit
arXiv:2311.17371 — debate "does not reliably outperform self-consistency and ensembling";
Wang arXiv:2402.18272 — a single agent with strong prompts matches the best discussion
method). **You cannot synthesise the partner.** You can synthesise the objection.

### 5.2 Things I could not verify and am therefore not asserting

**Socialisation.** I looked for a credible causal estimate of schooling's effect on social
outcomes, net of selection, and did not find one I would print. The homeschooling and
unschooling outcome literature is, in I1's assessment, "**essentially nil**" — "virtually
no empirical outcome data," and "predominantly self-selected retrospective survey."
`OBSERVED`. **The honest position is that the socialisation argument for school is widely
held, plausible, and not measured to a standard this survey accepts, and I am not going to
manufacture a citation for a claim I sympathise with.**

### 5.3 Pure scarcity artifacts — delete without ceremony

| Artifact | Constraint that produced it | Still binds? |
|---|---|---|
| Age-graded cohort | one adult, hundreds of children, need a partition | **No** |
| The 12/15-week course | pension-fund accounting unit generalised | **No** epistemically; **yes** as regulation |
| The 50-minute period | (unsourced) plausibly Carnegie arithmetic | **No** |
| The chapter as a container | print economics: sequential, expensive to revise | **No** |
| The single canonical exposition | one book, many readers | **No** — and measured to be wrong at d = 0.971 |
| The fixed item bank | item writing was the scarce good | **No** |
| Assessment separated from instruction | assessment had to be invigilated and hand-marked | **No** — and measured to discard g ≈ 0.50 |
| "Behind" | a cohort exists, therefore a position in it exists | **No** — the cohort is the artifact |

### 5.4 The line this section will not cross

I2's exclusion ledger states the deepest thing this survey's history sections found: "the
traditional mechanisms are not expensive because they are good; they are good *and* they
were affordable **because they were exclusive**. AI changes exactly one variable — the
marginal cost of attention — and that is precisely the variable the exclusions were
rationing."

That is true and it is also the boundary of the claim. **The building was never rationing
attention.** It was rationing supervision, safety, food, and a place to be. Those costs are
not attention costs, they did not fall, and none of the six designs above touches them. A
greenfield design that deletes the building has not been clever; it has confused the
variable that changed with the ones that did not.

---

## §6 — What only makes sense at population scale

Not personalisation. **The opposite.** The designs in §3 that are worth the most are the
ones that require ten million learners' data to be **one corpus** — the atlas (`N1-D1`),
the difficulty surface (`N1-D3`), and the edge register (`N1-D5`). None of them is a
per-learner artifact. Each is a public scientific object that no individual learner's data
could produce and every individual learner reads from.

This is the inversion of the field's stated direction. Personalisation makes ten million
private models. **The population artifacts make one public map, from which per-learner
routing is a cheap lookup.** The second is more valuable and much less built, for the
straightforward reason that a public map is not a defensible product.

### 6.1 What becomes possible

- **Prevalence.** For the first time, an answer to "what fraction of learners believe X
  instead of Y" for any X in any subject. Currently unknown for every concept in every
  subject.
- **Residence time.** How long learners occupy a wrong model before crossing. Currently
  unknown, everywhere.
- **Difficulty as a function rather than a number.** `N1-D3`.
- **Deletion.** A curriculum that can *remove* an edge because the evidence stopped
  supporting it. No curriculum in history has had a deletion procedure. Every one has only
  accumulated, which is why they are all too long.

### 6.2 The danger, and it now has its first empirical leg

This survey's §21 names **correlated pedagogical error** and states its evidential status
honestly: "Nobody has studied this. There is no monitoring for it, no benchmark that would
detect it, and — as far as we can determine — **no name for it in the literature**." The
backing is an argument from structure: thirty teachers make thirty uncorrelated mistakes and
the system averages them out; one model makes one mistake for every learner on the same
afternoon.

Three measured results can be attached to it, and to my knowledge this is the first time
they have been.

1. **The formal result that the risk is not merely a shock risk.** Kleinberg & Raghavan
   (2021), "Algorithmic monoculture and social welfare," *PNAS*,
   doi:10.1073/pnas.2018340118. `MEASURED-BENCH` (analytical, with a probabilistic
   framework). Their finding: "monocultural convergence on a single algorithm by a group of
   decision-making agents, **even when the algorithm is more accurate for any one agent in
   isolation, can reduce the overall quality of the decisions being made by the full
   collection of agents**. Unexpected shocks are therefore **not needed** to expose the
   risks of monoculture; it can hurt accuracy **even under 'normal' operations**."

   This is the precise formal shape of correlated pedagogical error, proved in a different
   domain. A model that is a better tutor than the average teacher, deployed to everyone,
   can make the *population's* learning worse. That is not a worry; it is a theorem with
   minimal assumptions.

2. **Measured homogenisation of output.** Doshi & Hauser (2024), "Generative AI enhances
   individual creativity but reduces the collective diversity of novel content," *Science
   Advances*, doi:10.1126/sciadv.adn5290. `MEASURED-RCT`. The same shape again: individual
   improvement, collective narrowing.

3. **A measured instance of a systematic pedagogical blind spot.** arXiv:2605.23925 again:
   **71% of a model's misconception-detection failures concentrate in just two question
   types**, both sharing a common structure. `MEASURED-BENCH`.

   That third result is the important one, and it deserves to be stated plainly: **model
   pedagogical error is measured to be structurally concentrated rather than randomly
   distributed.** It is not an argument that a model's blind spots are systematic; it is an
   observation that they are, in the one place anybody has looked. It is one data point in
   one domain, obtained incidentally by researchers studying something else. **It gives
   correlated pedagogical error its first empirical leg and the field has not noticed.**

And one negative result that closes the cheapest escape route: **resampling does not
manufacture independence.** Self-MoA (arXiv:2502.00674) found homogeneous self-aggregation
*beat* mixed Mixture-of-Agents by **+6.6% on AlpacaEval 2.0**; majority voting and reward
models **plateau beyond several hundred samples** in domains without automatic verifiers
(arXiv:2407.21787). `MEASURED-BENCH`. Asking the same model five times and taking the
consensus does not detect its correlated error; it confirms it.

### 6.3 The monitor

`DESIGN` **`N1-D7` — the disagreement register.**

**What it is.** Not an ensemble that votes. An ensemble that **records where genuinely
independent explainers disagree about the *mechanism* — not the answer — and publishes the
disagreement as a standing public artifact keyed to the atlas.**

survey §21 already proposes the detection principle: "an ensemble of genuinely independent
models and human experts, explaining the same concept, with disagreement in the
*explanation* — not the answer — treated as the signal." K2 arrives at a near-identical
object from a different direction — a **heterogeneous-arbiter** ensemble (proof assistant +
CAS + numerical simulation + retrieval over a fixed corpus), "each able to falsify the
others, with disagreement surfaced to the learner" — and notes that "this survey found **no
experiment that directly contrasts tool-heterogeneous against prompt-heterogeneous
multi-agent ensembles** on a matched task."

**What this design adds** is the thing neither of them specifies: **a falsifier, obtained by
joining the register to the atlas.**

**Inputs.** ≥3 explainers with genuinely different grounding — different base model
families, at least one non-neural symbolic checker, and at least one human expert panel.
The same concept, the same target learner state (from `N1-D1`).

**Outputs.** A per-concept disagreement rate over *mechanism*, versioned, public, with the
disagreements themselves published rather than resolved.

**What would show it was the wrong design.** **If the disagreement rate is uncorrelated
with measured downstream learner error.** This is the test that makes the register a
scientific instrument rather than a diversity metric: concepts where the explainers
disagree most should be concepts where learners, taught by any single explainer, most often
end up in a wrong model that the atlas records. If that correlation is absent, the register
is measuring model heterogeneity and nothing about truth, and it should be switched off.

**Second failure mode, and it is the likelier one.** Independence is asserted, not achieved.
Models trained on overlapping corpora with overlapping preference data are not independent
explainers, and Self-MoA suggests our intuitions about ensemble diversity are wrong in the
optimistic direction. The register's own independence must be measured — by planting a
known error in one explainer's grounding and checking that the others catch it — before any
of its outputs are trusted.

### 6.4 The question underneath all of this, which nobody has asked

`OPEN` **`N1-O1` — what is the correct *variance* of instruction across a population?**

Every system, human and machine, optimises the **mean** quality of instruction. Nobody has
ever asked what the *variance* should be. Under human teaching, instructional variance was
free, unmeasurable, and universally regarded as a defect to be reduced — the entire
standards, curriculum-alignment, and teacher-development apparatus exists to reduce it.

**Why nobody asked:** because before a single model taught ten million children, variance
was not a *design parameter*. You could not set it. It was an uncontrolled by-product of
having many minds, and the only available direction of travel was down. It has now become a
dial, and the first time anyone touches the dial they will turn it toward zero, because a
century of professional instinct says lower variance is better.

Kleinberg & Raghavan's result says that instinct may be exactly wrong at the population
level. **The optimal instructional variance is not obviously zero, it has never been
estimated, and there is no theory that would predict it.**

---

## §7 — Designs considered and rejected

A section of only good ideas is a pitch. Seven were considered seriously and rejected.

**R1 — The fully personalised curriculum in which no two learners encounter the same
object.**
The natural endpoint of personalisation and the thing the market is building.
**Rejected**, on three grounds, two measured. (a) It destroys the population artifacts:
**the atlas needs collisions.** Prevalence, residence time and difficulty surfaces are all
estimated across learners who met the *same* object; if every object is unique, the
denominator is one and none of §6 exists. (b) F9 OP-5 already establishes that
personalisation-induced differential item functioning has never been measured, and this
design maximises the exposure. (c) I2's chavruta analysis identifies **"text as arbiter"**
as one of only two mechanisms that survive digital substitution — and a text can only
arbitrate between two people who are both reading it. Full personalisation deletes the
arbiter.

**R2 — The AI-issued credential.**
A verifiable credential attesting capability, issued by the system. **Rejected on this
survey's own prior analysis**, which is better than any argument I would construct: I2 on
the *ijāza* — "a system that issues 'AI ijāzas' has built **a certificate with an empty
signature field**," because "a purely reputational credential inflates when the grantors'
incentives shift," and this is documented for the *ijāza* itself (grants to children
incapable of understanding the material). Reinforced by W3C VC 2.0: "verifiability of a
credential does not imply the truth of claims encoded therein." **And it fails the
greenfield test twice over:** it is a straight copy of an existing artifact, and Clark &
Martorell (2014) measured the existing artifact's signalling value as approximately
**nothing**. Building a better version of something measured to do little is the definition
of brownfield.

**R3 — The rich persistent psychological learner model.**
The system builds a deep, durable model of the person. **Rejected**, on four measured
grounds plus one structural. (a) The predictive ceiling is already reached: a
**zero-parameter moving average beats every released FSRS version on 350 million reviews**;
PFA matches DKT once leakage is cleaned; SAKT fails replication on all nine datasets.
(b) Rollinson & Brunskill: models with similar accuracy imply **substantially different
amounts of practice** — accuracy is not the right target and improving it does not improve
instruction. (c) Trace-based models **do not generalise across national populations**
(PIAAC 2012). (d) F5's blocker: "you cannot mine a transcript for a pattern; you can mine a
structured error record. **Nobody stores one.**" And structurally, survey §21 §4: the model
"may be a category error" for a child, and its worst failure is not staleness but
**constraint** — "the prediction becomes a wall… it is called tracking." **What survives is
the narrow version already adopted:** a typed per-KC state plus a misconception register,
inspectable and correctable, decaying by default, with restriction requiring stronger
evidence than expansion.

**R4 — The teachable agent that holds a misconception under pressure.**
Genuinely the most interesting mechanism in the survey. **Rejected here, not on merit but
on ownership:** it is F9 OP-7, fully specified, down to the proposed mechanism (weight-level
unlearning plus targeted belief insertion with a per-turn held-belief persistence check).
This section's brief is to extend past F9, not restate it. Noted also that survey §21 §7
flags its unstudied risk against ourselves — whether the learner repairs the error or
absorbs it — and that `N1-D4` inherits that risk in a different form and says so.

**R5 — Abolishing the cohort entirely in favour of pure competency grouping.**
**Rejected as brownfield, and it is the clearest case in the section.** This was tried, at
national scale, in the 1960s and 70s, under the name **non-graded schooling**. The
literature is right there and its titles tell the story: "The Effectiveness of the
Non-Graded School," *International Review of Education* (1972); "**Continuous Pupil Progress
in the Non-graded School: Hope or Hoax?**," *Elementary School Journal* (1970); "An
Alternative to Self-Contained, Age-Graded Classes" (Klausmeier & Quilling, 1967).
`HISTORICAL`. A greenfield section that proposes competency grouping as a novel artifact
has not done its reading. It is also a design that deletes the peer group, which §5 finds is
doing measured work that no artifact here replaces.

**R6 — Real-time adaptation to detected affect or frustration.**
**Rejected on two grounds.** Legally, F9 OP-19 is unresolved and the exposure is
prohibition-level rather than high-risk-level: whether interaction traces count as
"behavioural characteristics" under EU AI Act Art. 3(34), and therefore whether sensor-free
affect detection in education falls under Art. 5(1)(f), "has no authoritative
construction." Empirically, there is no validated affect signal in this corpus to adapt to.
And it fails the greenfield test — affect-adaptive tutoring is a thirty-year-old research
programme.

**R7 — A public live capability ranking.**
The natural product of `N1-D2` with the custody constraint removed: everyone's portfolio,
comparable, current, queryable. **Rejected as specified, and named here rather than
quietly omitted because it is what `N1-D2` becomes if you stop paying attention.** §4.4 is
the argument: sharpening the estimate sharpens the sort, and this survey's own
exclusion-ledger finding is about who gets excluded. The scarcity-era credential's
coarseness was a defect that functioned as a protection. **A design that removes the defect
without replacing the protection has made something worse and called it progress.**

---

## §8 — Open questions

Each states why nobody asked it, which is the criterion for `OPEN` as distinct from
"unanswered."

`OPEN` **`N1-O1` — what is the correct variance of instruction across a population?**
Developed in §6.4. *Why nobody asked:* variance was an uncontrolled by-product of many
minds and the only available direction of travel was down; it became a settable parameter
approximately five years ago and nobody has framed it as one.

`OPEN` **`N1-O2` — do learners' wrong models transfer across populations?**
Not whether *achievement* differs — that is measured constantly. Whether the *set of wrong
models occupied*, and their prevalence ranking, is stable across curricular systems.
*Why nobody asked:* misconception research is interview-based with samples in the dozens, so
a prevalence *ranking* was never estimable in one population, let alone comparable across
two. The corpora that would answer it (Eedi-shape, distractor-labelled, multi-country)
arrived after the research tradition that would have asked had already settled into
qualitative methods.

`OPEN` **`N1-O3` — what is the probe budget, as a fraction of opportunities, at which a
causally-maintained curriculum graph converges before it goes stale?**
*Why nobody asked:* no curriculum has ever been maintained causally, so there was no budget
to compute. The adjacent literature (Rafferty, Williams & Ying 2019) prices the *statistical
cost* of adaptive assignment inside a single experiment; nobody has asked the standing-policy
version, because standing policies of randomised instructional probing did not exist.

`OPEN` **`N1-O4` — is "behind" a coherent construct once the cohort is removed?**
The word names a position in a queue. Delete the queue and it has no referent — but the
underlying concern (a child who will not reach some threshold in time for some external
gate) is real and needs a name. *Why nobody asked:* the cohort was never optional, so the
question of what "behind" would mean without it never arose. The competency-based-education
literature dodges it by substituting "not yet," which is a rebranding, not a construct.

`OPEN` **`N1-O5` — what is the minimum collision rate?**
How many learners must encounter the *same* object for population-scale inference (atlas,
difficulty surface, edge register) to work? *Why nobody asked:* the collision rate was
**100% by construction** — everyone read the same textbook and sat the same paper — so the
parameter did not exist. Generation at zero marginal cost makes it a free variable for the
first time, and it trades directly against personalisation. There is a frontier here and
nobody has drawn it.

`OPEN` **`N1-O6` — does a continuously decaying credential change behaviour differently from
one that expires?**
*Why nobody asked:* no credential has ever decayed continuously. Professional licences
expire discretely, which produces a well-known cramming spike before renewal. A continuous
decay produces a different incentive gradient — always slightly stale, never suddenly
invalid — and there is no empirical or theoretical work on what that does to study
behaviour, because the object has not existed.

`OPEN` **`N1-O7` — what does a child own?**
Not "who may see the data" (privacy, extensively litigated) but "**who holds it**"
(custody, almost entirely unexamined). A learner's atlas position, portfolio, and probe
history are the substrate of every design here. *Why nobody asked:* the school held the
record, the record was inert, and the interesting question about an inert record is access.
A **live** record that determines what the learner is offered next is a different object,
and the framing has not caught up. F8 treats this as a safety-and-privacy question; it is
also a property question and nobody has said so.

`OPEN` **`N1-O8` — is a model's pedagogical error correlated *across concepts*, and does it
cluster by conceptual structure?**
survey §21 establishes that a model's errors are identical across *learners*. The unasked
sub-question is whether they are correlated across *concepts* — whether a model that
misteaches limits also misteaches convergence, in a way predictable from the concepts'
relationship. *Why nobody asked:* correlated pedagogical error was named three weeks ago in
this document and has no literature. The one relevant data point — arXiv:2605.23925's **71%
of failures in two question types** — was produced by researchers studying detection
accuracy, who reported the concentration as a methodological note rather than as a finding
about model structure. **The test is immediate and cheap: take a model's error rate across
the atlas and check whether it is independent of the graph's edge structure.** If it is not,
correlated pedagogical error is not a diffuse risk but a *targetable* one, and the monitor
in `N1-D7` knows where to look.

---

## §9 — The nulls, and this section's own falsifier

Every section of this survey carries at least one documented null with space of its own.
This section carries five, and three of them argue against designs printed above.

1. **Wrong examples lose to right ones.** Barbieri et al. (2023), 43 articles / 55 studies /
   181 effect sizes: "correct examples alone outperformed incorrect-only or
   correct+incorrect combinations," and self-explanation prompts **reduced** the effect.
   `MEASURED-META`. This is the prior against `N1-D4` and it should be believed unless
   beaten.
2. **Automated method-validity screening is impractical at realistic prevalence.**
   arXiv:2606.23205 / arXiv:2605.23925: **8:1** and **~4:1** false alarms to genuine
   detections; best model 84%, fine-tuned classifier 57%. `MEASURED-BENCH`. This kills the
   cheap version of `N1-D6` and forces the expensive one.
3. **Human standard-setters cannot see the difficulty variation that students experience.**
   Westacott et al. (2023), 2,218 students, 12 schools: 20 of 50 item models varied by
   > 0.15 in facility while the modified-Angoff cut scores varied by ≤ 0.03 across whole
   papers. `MEASURED-RCT`. Expert judgement was flatter than reality — which is the
   *premise* of `N1-D3` and simultaneously the reason `N1-D3` is hard.
4. **Expert-authored knowledge-component models are worth ≈ nothing predictively.** Gervet
   et al.: ≤ 0.01 AUC on 7 of 9 datasets; on 4 of 9, skill-only loses to
   item-difficulty-only. `MEASURED-BENCH`. Every curriculum graph in existence, including
   the one `N1-D5` proposes to maintain, starts from an object with this track record.
5. **The pre-AI mass-attention system was tried and abandoned on quality.** Rayman (1981),
   *History of Education Quarterly*: missionary schools adopted Lancaster's monitorial
   system "but **abandoned it when it proved ineffective**." `HISTORICAL`. Every previous
   attempt to make attention cheap made it cheap by making it worse. This section's entire
   premise is that the marginal cost fell without the quality falling, and **that premise
   has one prior attempt on record and it failed.**

### The section's own falsifier, stated in advance

**If the atlas's clusters do not survive a second population, five of the seven designs
fall.** `N1-D1` becomes a national artifact; `N1-D3`'s difficulty surfaces become
population-local; `N1-D4` has no stable model to root a derivation in; `N1-D5`'s edges do
not transfer; `N1-D7` has nothing stable to key its disagreements to. Only `N1-D2`, the
decaying portfolio, is independent of the atlas — and `N1-D2` has its own, separate and
more likely, falsifier: that a naive population-average decay curve beats a fitted
per-learner one, exactly as a zero-parameter moving average beats FSRS on 350 million
reviews.

**The cheapest experiment in this section is therefore also the most decisive**, and it
requires no new data collection: two existing distractor-labelled response corpora from
different school systems, one rank correlation over misconception prevalence per concept.
It could be run this month. Nobody has run it, and until somebody does, everything above is
`DESIGN`.

And the survey-level concession condition from §21 applies here without modification: a
well-powered trial of the assembled system, with a **delayed, unassisted, novel-item**
primary outcome, landing *inside* the 0.2–0.4 SD band rather than above it, would mean the
mechanisms are decorative and the band is the ceiling. That applies to these seven designs
as much as to the rest of the document, and if it happens the honest rewrite is the one
already drafted: *AI's contribution is scalable, high-fidelity, high-dosage delivery of what
already worked.*

---

## §10 — Sources

**Historical (researched fresh for this section; not present elsewhere in this corpus)**

1. McClusky, F. D. (1920). "Introduction of Grading into the Public Schools of New England,
   Part I." *The Elementary School Journal*. doi:10.1086/454874. `HISTORICAL` — abstract
   retrieved; body not retrieved.
2. McClusky, F. D. (1920). "…Part II." doi:10.1086/454893. `HISTORICAL` — metadata only.
3. Tyack, D. B. (1974). *The One Best System: A History of American Urban Education.*
   Harvard UP. doi:10.4159/9780674251120. `HISTORICAL` — not read in full.
4. Isensee, F. (2025). *The Graded School: Reassembling Public School Organization in New
   York City, 1805–1921.* Palgrave Macmillan. `HISTORICAL` — metadata only.
5. Ediger, M. (1987). "The Lancastrian Monitorial System of Instruction." ERIC.
   `HISTORICAL`, tertiary.
6. Tschurenev, J. (2008). "Diffusing Useful Knowledge: The Monitorial System of Education in
   Madras, London and Bengal, 1789–1840." *Paedagogica Historica.* `HISTORICAL`.
7. Mesquita, L. (2012). "The Lancasterian Monitorial System as an Education Industry with a
   Logic of Capitalist Valorisation." *Paedagogica Historica.*
   doi:10.1080/00309230.2012.658159. `HISTORICAL`.
8. Ressler, P. (2013). "Marketing Pedagogy: Nonprofit Marketing and the Diffusion of
   Monitorial Teaching in the Nineteenth Century." *Paedagogica Historica.* `HISTORICAL`.
9. Hogan (1973). "Factories, Monitorial Schools and Jeremy Bentham: The Origins of 'The
   Management Syndrome' in Popular Education." *Journal of Educational Administration and
   History.* `HISTORICAL`.
10. Rayman, R. (1981). "Joseph Lancaster's Monitorial System of Instruction and American
    Indian Education, 1815–1838." *History of Education Quarterly.* `HISTORICAL` — **the
    documented failure**.
11. Racine, K. (2020). "Monitors and Moralists: the Lancasterian System of Mutual Education
    …" *History of Education.* doi:10.1080/0046760x.2020.1712619. `HISTORICAL`.
12. Stevenson, W. R. III (2015). "MOOCs and Joseph Lancaster: Lessons from a Two-Hundred
    Year Precedent in Mass Learning on a Global Scale." *Educational Studies in Japan.*
    `HISTORICAL`.
13. Tompkins, E., & Gaumnitz, W. H. (1964). "The Carnegie Unit: Its Origin, Status, and
    Trends." *NASSP Bulletin* 48(288). doi:10.1177/019263656404828801. `HISTORICAL` —
    **body not retrieved**.
14. Shedd (1970). "The Carnegie Unit — How Did We Get It?" *Educational Forum.*
    doi:10.1080/00131727009340411. `HISTORICAL` — metadata only.
15. Silva, E., White, T., & Toch, T. (2015). *The Carnegie Unit: A Century-Old Standard in a
    Changing Education Landscape.* Carnegie Foundation. `HISTORICAL` — metadata only.
16. Sheppard, K., & Robbins, D. M. (2007). "High School Biology Today: What the Committee of
    Ten Actually Said." *CBE—Life Sciences Education.* doi:10.1187/cbe.07-03-0013.
    `HISTORICAL`.
17. "First Efforts toward a National Curriculum: The Committee of Ten's Report on History,
    Civil Government, and Political Economy" (1992). *Theory and Research in Social
    Education.* `HISTORICAL`.
18. "Foundations: The 1892 Committee of Ten" (1988). *Social Education.* `HISTORICAL`.
19. "The Effectiveness of the Non-Graded School" (1972). *International Review of
    Education.* `HISTORICAL`.
20. "Continuous Pupil Progress in the Non-graded School: Hope or Hoax?" (1970). *Elementary
    School Journal.* `HISTORICAL`.
21. Klausmeier, H. J., & Quilling, M. R. (1967). "An Alternative to Self-Contained,
    Age-Graded Classes." ERIC. `HISTORICAL`.

**Population-scale error data**

22. Wang, Z., et al. (2020). "Instructions and Guide for Diagnostic Questions: The NeurIPS
    2020 Education Challenge." arXiv:2007.12061. `MEASURED-BENCH`.
23. Wang, Z., et al. (2021). "Results and Insights from Diagnostic Questions: The NeurIPS
    2020 Education Challenge." arXiv:2104.04034. `MEASURED-BENCH`.
24. "The Correct Answer Trap: Pedagogically-Grounded Detection and Feedback for Hidden
    Misconceptions" (2026). arXiv:2606.23205. `MEASURED-BENCH`.
25. "Catching The Correct Answer Trap: Characterising AI Tutor Blind Spots When Analysing
    Student Reasoning" (2026). arXiv:2605.23925. `MEASURED-BENCH`.
26. "MCQ Difficulty Prediction via Modeling Learner Heterogeneity Using Data-Driven
    Cognitive Profiling" (2026). arXiv:2605.16290. `MEASURED-BENCH`.

**Measured anchors for the designs**

27. Koedinger, K. R., Carvalho, P. F., Liu, R., & McLaughlin, E. A. (2023). "An astonishing
    regularity in student learning rate." *PNAS* 120(13):e2221311120.
    doi:10.1073/pnas.2221311120. `MEASURED-BENCH`.
28. Arthur, W., Bennett, W., Stanush, P. L., & McNelly, T. L. (1998). "Factors That
    Influence Skill Decay and Retention: A Quantitative Review and Analysis." *Human
    Performance.* doi:10.1207/s15327043hup1101_3. `MEASURED-META`.
29. Westacott, R., Badger, K., Kluth, D., Gurnell, M., & Reed, M. (2023). "Automated Item
    Generation: impact of item variants on performance and standard setting." *BMC Medical
    Education.* doi:10.1186/s12909-023-04457-0. `MEASURED-RCT`.
30. Clark, D., & Martorell, P. (2014). "The Signaling Value of a High School Diploma."
    *Journal of Political Economy.* doi:10.1086/675238. `MEASURED-RCT` (RD).
31. Cen, H., Koedinger, K., & Junker, B. (2006). "Learning Factors Analysis — A General
    Method for Cognitive Model Evaluation and Improvement." LNCS.
    doi:10.1007/11774303_17. `MEASURED-BENCH`.
32. Tetzlaff, L., Simonsmeier, B., Peters, T., & Brod, G. (2025). "…expertise reversal…"
    *Learning and Instruction* 98:102142. doi:10.1016/j.learninstruc.2025.102142.
    `MEASURED-META`.
33. Yang, C., Luo, L., Vadillo, M. A., Yu, R., & Shanks, D. R. (2021). *Psychological
    Bulletin.* doi:10.1037/bul0000309. `MEASURED-META`.
34. Barbieri, C. A., Miller-Cotto, D., Clerjuste, S. N., & Chawla, K. (2023). *Educational
    Psychology Review.* doi:10.1007/s10648-023-09745-1. `MEASURED-META`.
35. Deslauriers, L., McCarty, L. S., Miller, K., & Callaghan, K. (2019). *PNAS.*
    doi:10.1073/pnas.1821936116. `MEASURED-RCT`.
36. Kestin, G., et al. (2025). *Scientific Reports* 15:17458.
    doi:10.1038/s41598-025-97652-6. `MEASURED-RCT`.
37. Bastani, H., et al. (2025). *PNAS.* doi:10.1073/pnas.2422633122. `MEASURED-RCT`.
38. Rowland, C. A. (2014). *Psychological Bulletin.* doi:10.1037/a0037559. `MEASURED-META`.
39. Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). *Review of Educational
    Research.* doi:10.3102/0034654316689306. `MEASURED-META`.
40. Fisher, C. W., et al. (1980). *Beginning Teacher Evaluation Study.* ERIC ED192454.
    `OBSERVED`.
41. Wan, H., & Beck, J. (2015). EDM. ERIC ED560558. `OBSERVED`.
42. Rollinson, J., & Brunskill, E. (2015). EDM. ERIC ED560516. `OBSERVED`.
43. Rafferty, A., Williams, J. J., & Ying, H. (2019). *JEDM.* ERIC EJ1220507. `OBSERVED`.
44. Gorgun, G., & Yildirim-Erbasli, S. (2026). ERIC EJ1501422 (PIAAC 2012 cross-population
    non-generalisation). `OBSERVED`.
45. Weitekamp, D., Siddiqui, M., & MacLellan, C. (2025). "TutorGym." arXiv:2505.01563.
    `MEASURED-BENCH`.

**Correlated pedagogical error and monoculture**

46. Kleinberg, J., & Raghavan, M. (2021). "Algorithmic monoculture and social welfare."
    *PNAS.* doi:10.1073/pnas.2018340118. `MEASURED-BENCH` (analytical).
47. Doshi, A. R., & Hauser, O. P. (2024). "Generative AI enhances individual creativity but
    reduces the collective diversity of novel content." *Science Advances.*
    doi:10.1126/sciadv.adn5290. `MEASURED-RCT`.
48. "Self-MoA: Rethinking Mixture-of-Agents" (2025). arXiv:2502.00674. `MEASURED-BENCH`.
49. Brown, B., et al. (2024). "Large Language Monkeys." arXiv:2407.21787. `MEASURED-BENCH`.
50. Smit, A., et al. (2023). arXiv:2311.17371. `MEASURED-BENCH`.
51. Wang, Q., et al. (2024). arXiv:2402.18272. `MEASURED-BENCH`.
52. "The Homogenizing Effect of Large Language Models on Human Expression and Thought"
    (2025). arXiv:2508.01491. `OBSERVED`.

**What the building does**

53. Chen, W., & Dube, S. R. (2025). "School closures, child maltreatment reporting and
    victimization during the pandemic." *Child Abuse & Neglect.*
    doi:10.1016/j.chiabu.2024.107243. `OBSERVED` — abstract retrieved, body not.
54. "Child sexual abuse reporting: Trends and challenges before, during, and after COVID-19
    school closures in Georgia, USA" (2025). *Child Abuse & Neglect.*
    doi:10.1016/j.chiabu.2025.107434. `OBSERVED`.
55. Amuedo-Dorantes, C., Marcén, M., Morales, M., & Sevilla, A. (2022). "Schooling and
    Parental Labor Supply: Evidence from COVID-19 School Closures in the United States."
    *ILR Review.* doi:10.1177/00197939221099184. `OBSERVED`.

**Optimiser machinery (for §4.1)**

56. GEPA (2025/2026). arXiv:2507.19457 / continual-learning results arXiv:2607.14004.
    `MEASURED-BENCH` — via K2.
57. DSPy; MIPROv2; PromptBreeder; TextGrad; AlphaEvolve; Darwin Gödel Machine — all
    `MEASURED-BENCH` via K2 §6.1, numbers as reported there.

**Internal priors relied on (this survey's own corpus — not re-verified here)**

58. `B1-learning-science.md` — replication grades, multimedia and expertise-reversal
    corpus, the anti-satisfaction design rule.
59. `K1-compression.md` — opportunities-not-days, the floor model, the
    repair-then-remeasure experiment, the Carnegie arithmetic, N_kc as assumption.
60. `K2-agentic-frontier.md` — the bounded-loop rule, TutorGym, the eleven-point
    judge-vs-outcome spread, the heterogeneous-arbiter proposal, the unbuilt
    retention-fitness optimiser.
61. `F9-open-problems.md` — OP-1, OP-3, OP-5, OP-7, OP-19 (referenced, not restated).
62. `F5-learner-model.md` — the FSRS moving-average result, the KC alignment problem, W3C
    Verifiable Credentials.
63. `F4-reach-economics.md` — ~$0.05 per learner-hour.
64. `F8-safety-privacy-children.md` — the safety frame for §4.3.
65. `I1-pedagogical-systems.md` — PSI, mastery learning, Bloom 2σ correction,
    non-graded/permission constraints, unschooling evidence status.
66. `I2-global-traditions.md` — the exclusion ledger, the *ijāza* analysis, chavruta
    mechanism survival, Ekalavya.
67. `survey/21-what-we-cannot-see-from-here.md` — correlated pedagogical error, the
    epistemic curriculum, the learner-model category error, the positional condition, the
    self-falsifier.
68. `survey/14` — the Null-Learner Test.
69. `survey/01` — the felt/real inversion and the −17% withdrawal result.
70. `CORRECTIONS.md` — the ledger discipline this section inherits.
71. 34 CFR 600.2 — the modern credit-hour definition. `OBSERVED`.

**Explicitly unverified, and reported as such**
- The Prussian origin of American age-graded schooling. `UNVERIFIED` — a contested 1916
  thesis with a stated reformist motive, disputed by 1920, not adjudicated here.
- The origin of the 50-minute period. `UNVERIFIED` — no primary source located; the
  Carnegie-arithmetic derivation is `INFERENCE` only.
- The Carnegie unit's pension-fund origin. `HISTORICAL`, tertiary — consistent across the
  secondary literature, no primary text retrieved.
- Schooling's causal contribution to socialisation. **No estimate this survey would print
  was located.**

---

## §11 — The three to build first

**1. The population-transfer check on the error atlas.** Two existing distractor-labelled
corpora from different school systems; one rank correlation over misconception prevalence
per concept. It costs almost nothing, requires no new data collection, and **five of the
seven designs above depend on the answer.** Build the falsifier before the thing it would
falsify.

**2. `N1-D2`, the decaying capability portfolio.** It has the cleanest measured anchor in
the section (Arthur et al.: d = −0.01 → −1.4 over a year of nonuse, and fastest for
cognitive-accuracy skills), the cleanest falsifier (does a decay-adjusted estimate beat the
last recorded score at predicting unassisted performance?), it is the only design
independent of the atlas, and it attacks the artifact — the transcript — that is
simultaneously the most consequential and the least defended thing in education. It is also
the design most likely to be turned into R7 by someone who is not paying attention, which
is a reason to build it carefully rather than a reason not to.

**3. `N1-D1` + `N1-D5` as one object.** The atlas and the evidence-maintained graph are
the same artifact viewed at two resolutions, and neither works alone: the graph's edges are
transitions between atlas entries, and the atlas's crossing rates are the graph's edge
weights. Together they are the first curriculum in history with a **deletion procedure**.
Built separately, both fail.
