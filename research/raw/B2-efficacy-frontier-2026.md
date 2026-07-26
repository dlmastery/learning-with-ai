---
title: "AI tutoring efficacy at the July 2026 frontier"
wave: B
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 22
---

# B2 — AI Tutoring Efficacy at the July 2026 Frontier

## Executive finding

The evidence question has changed.

It is no longer responsible to summarize AI tutoring mainly through studies of
pre-frontier chatbots, generic homework helpers, or one-shot text generation.
By July 2026, randomized studies across school, university, and adult-learning
settings show that well-designed AI-supported learning can produce meaningful
**unaided** gains. The strongest portfolio includes:

- **+0.258 SD in mathematics** across 1,763 junior-secondary students and 12
  schools in Sierra Leone after an eight-week Gemini Guided Learning program;
- **+0.31 SD on a combined outcome index** after a six-week, teacher-supported
  generative-AI program in Nigeria;
- **nearly +0.5 SD in mathematics** when implementation support increased
  sustained Khan Academy use in Indian government residential schools;
- **+0.27 SD on an immediate unaided knowledge test**, with persistence one week
  later, in a July 2026 randomized experiment;
- a measured education performance gap narrowing from **0.548 SD to 0.139 SD**
  in an experiment with 1,174 participants; and
- **approximately 65% unaided SAT-mathematics accuracy** with an AI tutor plus
  role-distinct AI peers, versus approximately 42% without agents.

All are `MEASURED-RCT`, but they are not the same intervention and their effect
sizes are not directly interchangeable.

The constructive conclusion is:

> AI tutoring efficacy is established strongly enough to justify urgent
> deployment, replication, and engineering. The next standard is not “did a
> chatbot help?” It is whether an integrated mentor produces durable,
> transferable, equitable learning at the cost and connectivity level of the
> communities it is intended to serve.

The most effective interventions are systems, not naked models. They combine
curriculum grounding, a learning sequence, immediate feedback, repeated use,
teacher or facilitator support, peer interaction, and measurement of what the
learner can do without assistance.

---

## 1. What counts as evidence now

This review uses five distinct evidence classes:

| Class | Question answered | Appropriate use |
|---|---|---|
| `MEASURED-RCT` | Did learners assigned to an intervention learn more? | Efficacy and causal claims |
| `MEASURED-BENCH` | Can a model perform a specified tutoring or evaluation task? | Component selection and QA |
| `OBSERVED` | How do learners and teachers actually use the system? | Workflow and deployment design |
| `VENDOR` | What does a shipping product claim or expose? | Capability inventory, not outcome proof |
| `INFERENCE` | What architecture follows from the evidence? | Explicit design hypothesis |

The primary outcome is **independent capability**: what the learner recalls,
explains, solves, creates, or transfers when the AI is absent or constrained.
Completion, satisfaction, message count, and artifact polish are useful operating
signals, but they are not substitutes for learning.

Older findings remain relevant when they describe a durable learning mechanism.
They do not define the capability ceiling of July 2026 systems.

---

## 2. The current outcome portfolio

### 2.1 Sierra Leone: direct school evidence at meaningful scale

Google DeepMind’s pre-registered evaluation covered **1,763
junior-secondary students in 12 schools**. After eight weeks, assignment to
Gemini Guided Learning produced a **+0.258 SD intent-to-treat mathematics
effect**. Across approximately **113,000 tutor interactions**, 91.4% focused on
conceptual learning; 76% used scaffolding, and only 2% directly supplied a
solution. Sixty-nine percent of students reached the study’s intended usage
threshold. `MEASURED-RCT`

The intervention is especially valuable for system design because it reports
the dialogue behavior, not only the final effect. The gain came from a tutor
policy that usually explained, questioned, and scaffolded.

The reported heterogeneity also creates a concrete next target: students with
stronger baseline mathematics benefited more. The correct response is not to
withdraw the system; it is to strengthen prerequisite diagnosis, early
confidence-building, language support, and facilitator escalation until gains
are largest for learners who begin furthest behind. `INFERENCE`

Sources:

- [DeepMind evaluation overview](https://deepmind.google/blog/measuring-the-impact-of-learning-with-ai-in-sierra-leone-and-beyond/)
- [LearnLM Sierra Leone technical report](https://storage.googleapis.com/deepmind-media/LearnLM/learnLM_sierraleone_may26.pdf)

### 2.2 Nigeria: teacher-supported, low-infrastructure deployment

The World Bank’s randomized six-week program paired Microsoft Copilot with
teacher facilitation, curriculum-aligned prompts, peer learning, and after-school
sessions twice per week. Students received roughly **13 hours** of exposure.
The reproducibility package reports a **+0.31 SD combined effect** and a
**+0.23 SD English effect**. Outcomes increased with participation despite
intermittent electricity and connectivity. `MEASURED-RCT`

This is evidence for a human-AI service design, not evidence that a model should
replace a classroom. A facilitator can create routines, ensure access, help a
learner recover when a dialogue stalls, and connect AI practice to the local
curriculum. AI makes expert-like attention abundant; trusted adults make it
usable in the learner’s real setting. `INFERENCE`

Sources:

- [World Bank: lessons from the Nigeria program](https://blogs.worldbank.org/en/developmenttalk/addressing-the-learning-crisis-with-generative-ai--lessons-from-)
- [World Bank working paper and report record](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324)
- [World Bank reproducibility package](https://reproducibility.worldbank.org/catalog/419)

### 2.3 India: implementation support is part of the intervention

An evaluation across **83 residential government schools** found that
implementation support raised weekly Khan Academy use from **7.2 to 47.4
minutes** and produced mathematics gains approaching **+0.5 SD**. `MEASURED-RCT`

The result reframes “adoption.” Logging into a good tutor is not the same as
receiving tutoring. Timetabling, reliable access, teacher onboarding, visible
progress, and rapid recovery from technical failures are causal components of
the service. The universal mentor therefore needs an implementation protocol,
not just an application download. `INFERENCE`

Source:

- [NBER Working Paper 34683](https://www.nber.org/papers/w34683)

### 2.4 Peru: diagnostic-first public infrastructure

Peru’s **Eligiendo Mi Camino** program uses an initial diagnostic to recommend
mathematics activities across four competencies, 16 topics, and 80 subtopics.
The current World Bank program page reports **6,600 students, 110 public
schools, and 400 trained teachers**, with two hours per week at school and a
home mode. It describes an evaluation across the 110 schools. `OBSERVED`

An earlier July 2026 results page reports a **4,500-student, 85-school** rollout
snapshot and a separate teacher-training experiment covering 390 schools.
These figures describe different published snapshots and components; they
should not be collapsed into one enrollment count. `OBSERVED`

Peru illustrates the shape of national infrastructure: diagnostic placement,
curriculum mapping, teacher preparation, school-time integration, home
continuity, and evaluation designed into rollout.

Sources:

- [Eligiendo Mi Camino program page](https://www.worldbank.org/en/country/peru/brief/eligiendo-mi-camino)
- [World Bank July 2026 results page](https://www.worldbank.org/en/results/2026/07/02/artificial-intelligence-in-action-in-latin-america-s-schools-evidence-from-peru)

### 2.5 General knowledge acquisition: augmentation beats automation

A randomized July 2026 experiment found **+0.27 SD** on an immediate unaided
test after participants learned an unfamiliar topic with generative AI. Gains
persisted one week later. Delayed gains were larger for learners whose behavior
was classified as **augmentation**—using AI to explain and explore—than for
those who mainly automated text production. Time moved from drafting toward
reading and search, while enjoyment increased. `MEASURED-RCT`

This distinguishes two product policies:

- *produce for me* optimizes the assisted artifact;
- *help me understand and decide* optimizes the learner.

A mentor can still draft, calculate, or demonstrate. It should turn those
actions into inspectable examples and follow them with retrieval, explanation,
verification, or transfer. `INFERENCE`

Sources:

- [Contractor and Reyes, July 2026 preprint](https://arxiv.org/abs/2607.08849)
- [NBER Economics of Education program report](https://www.nber.org/reporter/2026number2/program-report-economics-education)

### 2.6 Closing an education performance gap

In an experiment with **1,174 participants**, access to generative AI reduced a
measured performance gap associated with educational background from **0.548 SD
to 0.139 SD**—roughly three quarters. Later unaided performance showed no
corresponding penalty, and lower-education participants retained part of the
benefit. `MEASURED-RCT`

This is an existence proof for AI as an expertise equalizer. It does not show
that every design automatically closes every gap. It sets an acceptance
criterion: report effects by starting level, language, disability, gender,
device tier, and connectivity tier, then redesign until uplift reaches the
learners for whom expert help is otherwise least available. `INFERENCE`

Source:

- [NBER Working Paper 34851](https://www.nber.org/papers/w34851)

### 2.7 Expert-supervised tutor creation

In an exploratory randomized study with **165 students across five UK schools**,
experts supervised LearnLM-generated mathematics tutoring content. Reviewers
approved **76.4%** of generated tutor drafts with zero or minimal edits.
AI-supported students performed at least as well as students receiving
human-only tutoring, and scored **66.2% versus 60.7%** on novel problems from a
subsequent topic. `MEASURED-RCT`, exploratory

The scalable pattern is not “either AI or expert.” Expert effort shifts upward:
define the curriculum and rubric, supervise generated instruction, inspect
failure clusters, and improve the tutor policy. A small expert team can maintain
many more learning interactions than it could deliver synchronously.

Source:

- [LearnLM/Eedi exploratory randomized study](https://arxiv.org/abs/2512.23633)

### 2.8 Tutor plus peers: social structure on demand

A controlled study with **315 participants** compared no agents, two AI peers,
an AI tutor, and tutor plus peers for SAT mathematics. Mean unaided accuracy was
approximately **42%, 48%, 59%, and 65%**, respectively. Tutor plus peers had the
largest difference from control, although the exploratory pairwise difference
from tutor alone was not statistically significant. `MEASURED-RCT`

A second experiment with **247 writers** found that both one- and two-model
assistance increased quality. The two-model condition preserved idea diversity
near the unassisted baseline. `MEASURED-RCT`

This supports a mentor mesh in which learners can observe alternative
strategies, diagnose a peer’s error, defend a judgment, and receive expert
synthesis. It does not require exposing a confusing crowd: one mentor can
orchestrate the agents and surface only the disagreement that advances learning.

Source:

- [Beyond the AI Tutor: Social Learning with LLM Agents](https://arxiv.org/abs/2604.02677)

### 2.9 Earlier direct tutoring evidence remains a useful bridge

A randomized Harvard physics study found that students using an AI tutor
learned more in less time and reported higher engagement and motivation than an
active-classroom comparison for the studied lesson. `MEASURED-RCT`

Tutor CoPilot studied approximately **900 tutors and 1,800 K–12 students**,
showing how real-time AI support can make high-quality tutoring moves available
to tutors serving historically underserved learners. `MEASURED-RCT`

These studies predate the July 2026 frontier but remain relevant because they
test two durable delivery patterns: direct AI tutoring and AI amplification of
human tutors.

Sources:

- [Kestin et al., Scientific Reports](https://doi.org/10.1038/s41598-025-97652-6)
- [Tutor CoPilot](https://arxiv.org/abs/2410.03017)

---

## 3. What the successful systems have in common

Across subjects and geographies, six properties recur.

### 3.1 Grounded scope

The mentor works from a defined curriculum, source set, or knowledge goal. It
does not improvise an entire course from model memory.

### 3.2 A sequenced learning loop

The experience includes diagnosis, explanation or demonstration, guided
practice, feedback, independent retrieval, and transfer. Chat is an interface
inside the loop, not the loop itself.

### 3.3 Meaningful dose

Learning compounds over repeated sessions. The India and Nigeria results make
time allocation and reliable access part of the causal design.

### 3.4 Teacher or facilitator leverage

Adults establish routines, resolve contextual problems, connect learning to
school and life, and intervene when a learner needs human judgment. Their
capacity expands because AI handles routine differentiation and immediate
practice.

### 3.5 Evidence returned to the next action

Every response, worked step, spoken explanation, hint request, and transfer
attempt updates a learner model. The mentor acts on mastery evidence and
uncertainty rather than on a permanent ability label.

### 3.6 Unaided measurement

The decisive check happens after the AI steps back.

These six properties yield an efficacy chain:

```text
local goal
   → diagnostic evidence
   → right representation and teaching mode
   → guided learner action
   → immediate grounded feedback
   → unaided retrieval and transfer
   → learner-state update
   → next best action
```

---

## 4. Model capability is necessary; tutor policy is decisive

The underlying model must reason, converse, see, use tools, and work across
languages. Those capabilities do not by themselves define a tutor.

A July 2026 **FATE** benchmark evaluates whether tutoring feedback identifies
the mistake, locates it, provides useful guidance, and gives the learner an
actionable next move. Its specialized 8B evaluator gained as much as 22.63
percentage points through distillation. Reported benchmark averages included
82.88 for Gemini 2.5 Flash, 80.75 for ChatGPT 5.5 Instant, 80.13 for DeepSeek V4
Flash, and 74.0 for Claude Sonnet 4.6; actionability remained a common weakness.
`MEASURED-BENCH`

**CSTutorBench** evaluated 11 models from 4B to 120B parameters. Model family and
instruction tuning sometimes mattered more than parameter count, and an
educational prompt improved 10 of 11 tested models. `MEASURED-BENCH`

**EduPanel** divides educational-video evaluation among three
learner-conditioned agents and produces inspectable evidence. It also finds
visual reasoning weaker than transcript-based dimensions, specifying where
human or tool verification is still valuable. `MEASURED-BENCH`

**DeepTutor** combines grounded problem solving, multi-resolution memory,
learner profiles, calibrated question generation, and proactive multi-agent
skills. `MEASURED-BENCH`

These are component evaluations, not learning-outcome trials. Their value is
operational: they make tutor roles testable before exposing them to millions of
learners.

Sources:

- [FATE](https://arxiv.org/abs/2607.10647)
- [CSTutorBench](https://arxiv.org/abs/2607.05571)
- [EduPanel](https://arxiv.org/abs/2607.18529)
- [DeepTutor](https://arxiv.org/abs/2604.26962)

---

## 5. One teaching mode is not enough

The frontier evidence does not justify turning every interaction into prolonged
Socratic questioning. The mentor needs a **teaching-mode router**.

Available modes include:

- diagnose a missing prerequisite;
- explain directly in the learner’s strongest language;
- demonstrate a complete worked example;
- ask a targeted question;
- co-solve one step;
- let the learner finish the next step;
- verify an answer or artifact;
- ask the learner to teach the idea;
- stage contrasting peer solutions;
- schedule retrieval;
- assign a real-world project;
- escalate to a teacher, family member, or specialist.

The router selects a mode from the learner’s goal, starting knowledge, language,
affect, time, error type, and prior response to help. The policy optimizes
**increasing independent capability**, not the number of questions asked or the
amount of content generated. `INFERENCE`

---

## 6. The efficacy stack

No single test is sufficient. A production mentor should move through five
layers:

| Layer | What is tested | Release gate |
|---|---|---|
| 1. Response | Correctness, pedagogy, actionability, citation, safety | Role-specific benchmark passes |
| 2. Simulated sequence | Whether policy adapts across a learner trajectory | Failure clusters are explainable |
| 3. Human usability | Whether real learners understand and continue productively | Language and accessibility parity |
| 4. Learning outcome | Unaided retention and transfer against a strong comparison | Pre-registered meaningful uplift |
| 5. Deployment | Reach, uptime, facilitator load, distributional gains, cost | Target community can sustain service |

The Learning Engagement Assistant classroom study is instructive. Eight
students across three courses reported strong usability and trust, but actual
usage remained shallow and simulations did not predict every behavior.
`OBSERVED`, n=8. Synthetic learners can accelerate development; real learners
remain the authority for release.

Source:

- [Learning Engagement Assistant evaluation](https://arxiv.org/abs/2607.13370)

---

## 7. Acceptance criteria for a universal mentor

The universal mentor should not be certified by a model leaderboard alone. It
should meet explicit service outcomes:

1. **Independent gain:** improves delayed unaided recall, reasoning, or skill.
2. **Transfer:** improves performance on a novel problem, representation, or
   setting.
3. **Distributional uplift:** gains reach learners starting furthest behind.
4. **Language parity:** local-language learning approaches the best-supported
   language, not merely conversational fluency.
5. **Accessibility parity:** speech, text, visual, motor, and cognitive access
   paths support equivalent goals.
6. **Teacher leverage:** more learners receive accurate, timely help per hour of
   expert human attention.
7. **Low-connectivity continuity:** essential diagnosis, explanation, practice,
   and learner-state capture continue offline or under intermittent service.
8. **Grounding:** curriculum, factual, mathematical, and scientific claims are
   traceable and tool-checkable.
9. **Learner ownership:** state is visible, correctable, portable, and
   permissioned.
10. **Economic reach:** cost per successful learning hour fits public and family
    budgets in the target geography.
11. **Safe escalation:** the system recognizes when human context or protection
    is required and transfers the relevant evidence.
12. **Joy and agency:** learners increasingly choose goals, explanations,
    projects, and communities rather than merely complying with prompts.

---

## 8. The deployment program implied by the evidence

### Phase 1 — a grounded mentor in one curriculum slice

- map a local goal graph;
- diagnose prerequisite knowledge;
- implement several teaching modes;
- measure immediate and delayed unaided transfer;
- publish performance by starting level.

### Phase 2 — teacher and facilitator cockpit

- show who needs which kind of help;
- explain the mentor’s current hypothesis;
- let teachers correct goals and state;
- create small-group and peer activities;
- measure saved time and increased reach.

### Phase 3 — multilingual, multimodal parity

- add full-duplex speech and camera/document understanding;
- ground translations in subject vocabulary;
- evaluate learning, not only translation quality;
- generate accessible equivalent representations.

### Phase 4 — low-connectivity school and community node

- run speech, retrieval, routine practice, and state locally;
- synchronize curriculum and learner updates when connectivity returns;
- escalate only hard or safety-critical cases to regional frontier models;
- support shared devices without merging identities.

### Phase 5 — longitudinal replication

- pre-register trials across subjects, ages, languages, and countries;
- test delayed retention and real projects;
- maintain public failure taxonomies and model cards for each mentor role;
- drive cost toward the level required for universal entitlement.

---

## 9. Research priorities after July 2026

The most valuable studies now compare good architectures rather than “AI” with
no AI:

1. Which teaching-mode policies best serve novices, exam learners, and advanced
   creators?
2. When do role-distinct peers add value beyond a strong mentor?
3. Which learner-state variables improve decisions without creating invasive
   profiles?
4. How close can local small models come to frontier learning outcomes with
   retrieval and escalation?
5. Which teacher workflows produce the greatest reach per human hour?
6. How should visual and spoken tutoring be verified?
7. What dosage and spacing produces durable gains by subject?
8. How should outcomes be measured for shared phones, intermittent networks,
   and oral-language communities?
9. Can the largest gains reliably accrue to the lowest-baseline learners?
10. What public procurement metric best represents cost per durable mastery
    gain?

---

## Conclusion

By July 2026, the positive case rests on more than impressive conversation.
Randomized trials show independent learning gains across multiple geographies
and delivery patterns. Benchmark work makes tutoring behavior inspectable.
National and school deployments show how curriculum, teachers, time, devices,
and connectivity fit around the model.

The priority is execution:

- build the mentor as a complete learning system;
- treat implementation as part of efficacy;
- evaluate the learner after assistance;
- design for the lowest-resource setting from the beginning;
- make the human layer more powerful;
- publish who benefits, in which language, on which device tier, at what cost.

Universal expert mentorship is now a credible public objective. The evidence
supports building toward it with the urgency normally reserved for new physical
infrastructure.

---

## Source index

1. [DeepMind: Sierra Leone impact evaluation](https://deepmind.google/blog/measuring-the-impact-of-learning-with-ai-in-sierra-leone-and-beyond/)
2. [LearnLM Sierra Leone technical report](https://storage.googleapis.com/deepmind-media/LearnLM/learnLM_sierraleone_may26.pdf)
3. [World Bank: Nigeria lessons](https://blogs.worldbank.org/en/developmenttalk/addressing-the-learning-crisis-with-generative-ai--lessons-from-)
4. [World Bank Nigeria working-paper record](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324)
5. [Nigeria reproducibility package](https://reproducibility.worldbank.org/catalog/419)
6. [NBER 34683: India implementation support](https://www.nber.org/papers/w34683)
7. [World Bank: Eligiendo Mi Camino](https://www.worldbank.org/en/country/peru/brief/eligiendo-mi-camino)
8. [World Bank: AI in Latin American schools](https://www.worldbank.org/en/results/2026/07/02/artificial-intelligence-in-action-in-latin-america-s-schools-evidence-from-peru)
9. [Generative AI and knowledge acquisition](https://arxiv.org/abs/2607.08849)
10. [NBER Economics of Education program report](https://www.nber.org/reporter/2026number2/program-report-economics-education)
11. [NBER 34851: AI and the education performance gap](https://www.nber.org/papers/w34851)
12. [LearnLM/Eedi exploratory randomized study](https://arxiv.org/abs/2512.23633)
13. [Beyond the AI Tutor](https://arxiv.org/abs/2604.02677)
14. [Kestin et al., Scientific Reports](https://doi.org/10.1038/s41598-025-97652-6)
15. [Tutor CoPilot](https://arxiv.org/abs/2410.03017)
16. [FATE](https://arxiv.org/abs/2607.10647)
17. [CSTutorBench](https://arxiv.org/abs/2607.05571)
18. [EduPanel](https://arxiv.org/abs/2607.18529)
19. [DeepTutor](https://arxiv.org/abs/2604.26962)
20. [Learning Engagement Assistant](https://arxiv.org/abs/2607.13370)
21. [DeepMind: ATL Saathi in India](https://deepmind.google/blog/empowering-indias-next-generation-of-innovators-with-atl-saathi/)
22. [World Bank Education](https://www.worldbank.org/en/topic/education)
