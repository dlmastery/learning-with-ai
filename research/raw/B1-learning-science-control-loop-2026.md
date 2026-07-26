---
title: "Learning science as a real-time control loop"
wave: B
section: B1
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 24
---

# B1 — Learning Science Becomes a Control System

## Executive finding

Frontier AI does not repeal learning science. It makes its strongest principles
executable at the level of one learner, one concept, and one moment.

The useful 2026 translation is not a static checklist of pedagogical effects. It
is a closed control loop:

```text
meaningful goal
  → diagnose current state
  → select a teaching action
  → require learner action
  → give informative feedback
  → update uncertain state
  → schedule retrieval and variation
  → test delayed transfer
  → connect a human when useful
```

The loop resolves a false debate. An AI mentor should not be “Socratic,” “direct
instruction,” “discovery,” “practice,” or “project based” all the time. Those are
actions. The system’s scientific task is to choose and sequence them from the
learner’s knowledge, goal, memory, context, and access needs.

## Evidence labels

| Label | Meaning |
|---|---|
| `MEASURED-RCT` | Randomized learner outcome |
| `MEASURED-BENCH` | Disclosed benchmark or structured evaluation |
| `OBSERVED` | Field study or public implementation |
| `VENDOR` | Provider-reported capability or product experiment |
| `FOUNDATIONAL` | Replicated pre-frontier learning principle retained as an invariant |
| `INFERENCE` | 2026 architecture consequence |

## 1. The enduring floor, compressed

The detailed 109-source
[learning-science archive](B1-learning-science.md) documents the effect sizes,
moderators, and replication record behind the principles below. It remains a
source spine, not the organizing story.

The mentor needs only a compact set of durable invariants:

1. **Prior knowledge changes the best support.** Novices often need explicit
   models, worked examples, and reduced search; greater expertise can make the
   same scaffold redundant. `FOUNDATIONAL`
2. **Retrieval strengthens memory when it is effortful and corrected.** Repeated
   exposure is not a substitute for recalling and using knowledge.
   `FOUNDATIONAL`
3. **Spacing changes what survives.** Memory should be revisited near the edge
   of forgetting and across increasing time horizons. `FOUNDATIONAL`
4. **Feedback must be actionable.** A score alone is weak; useful feedback
   identifies the current gap and the next attempt. `FOUNDATIONAL`
5. **Self-explanation and teaching reveal structure.** Asking a learner to
   predict, justify, compare, teach, or repair produces evidence richer than
   asking for recognition. `FOUNDATIONAL`
6. **Variation supports transfer.** A capability becomes robust when it works
   across representations, contexts, and problem families. `FOUNDATIONAL`
7. **Motivation is part of the learning mechanism.** Purpose, agency, visible
   progress, belonging, calibrated challenge, and a shame-free return determine
   whether the learner re-enters the loop. `FOUNDATIONAL`
8. **Collaboration can add thinking that solo practice cannot.** Explaining,
   coordinating, critiquing, and jointly building are themselves learning
   actions. `FOUNDATIONAL`

These principles are not an argument for a restrictive tutor. They are a richer
menu of support.

## 2. The strongest 2026 evidence is already loop-shaped

### 2.1 Sierra Leone: diagnosis, guided work, and teacher context

Google and Fab AI ran an eight-week preregistered RCT in 48 classrooms with
nearly 1,800 Grade 7–8 learners. Guided Learning improved externally validated
math scores by 0.26 standard deviations. Google compares that result with
roughly 1.2–1.7 years of typical progress in low- and middle-income countries.
[`MEASURED-RCT`](https://blog.google/products-and-platforms/products/education/measuring-the-impact-of-ai-on-teaching-and-learning/)

This is not evidence for “chat.” It is evidence for structured, teacher-situated
guided learning.

### 2.2 Nigeria: teacher launch, adaptive tutor, reasoning, feedback

The Edo State program paired teacher introduction with a responsive AI tutor
aligned to the official English curriculum. Over six weeks it produced
approximately 0.31 standard deviations of gain and transferred into regular
curriculum subjects. [`MEASURED-RCT`](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324)

The mechanism is a loop: human context, learner interaction, tailored response,
practice, and return.

### 2.3 Higher education: access policy is an empirical variable

A randomized study of 334 university learners found that AI tutoring improved
exam performance by 0.23 standard deviations and that unrestricted access
outperformed a policy requiring initial independent reading by 0.21 standard
deviations. [`MEASURED-RCT`](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5992341)

This finding is important because it rejects pedagogical moralizing. Requiring a
specific sequence does not automatically make a tutor more educational. The
policy must earn its place through learning outcomes.

### 2.4 Human-plus-AI: distribute expert moves

[Tutor CoPilot](https://arxiv.org/abs/2410.03017) improved topic mastery by four
percentage points overall and nine points for learners working with lower-rated
tutors. `MEASURED-RCT`

The [LearnLM/Eedi trial](https://arxiv.org/abs/2512.23633) found that expert
tutors approved 76.4% of AI-drafted messages with zero or minimal edits and that
AI-supported learners were 5.5 percentage points more likely to solve novel
subsequent problems. `MEASURED-RCT`

The loop can run through a human. AI can make a tutor’s context and move
selection more consistent without removing the relationship.

## 3. The control state

The mentor should not infer a fixed “learning style.” It should maintain
uncertain, correctable state relevant to the next action:

| State | Example signal | Why it changes teaching |
|---|---|---|
| Concept evidence | correct explanation with one missing causal link | target the missing link |
| Prerequisite confidence | cannot use fractions in an algebra task | step back and model |
| Memory strength | correct last week, slow today | schedule retrieval |
| Error pattern | consistently reverses conditional probability | contrast cases |
| Independence | succeeds after one hint | fade support |
| Cognitive bandwidth | rushed, overloaded, or interrupted | chunk and resume |
| Goal | exam tomorrow versus durable mastery | change depth and schedule |
| Access | speech, visual, motor, reading, or language need | change channel, not rigor |
| Interest/context | farming, games, local transport, family business | choose meaningful examples |
| Social opportunity | peer nearby, teacher available, expert needed | route to a human or group |

Every state claim requires an evidence pointer and confidence. Demographic
labels may never stand in for observed knowledge.

## 4. The teaching-action library

### 4.1 Direct explanation

Use when a prerequisite is absent, the learner explicitly needs orientation, or
continued search adds load rather than insight.

The July 2026
[AITutor field study](https://arxiv.org/abs/2607.01692) found learners under
time pressure actively resisted rigid Socratic dialogue and used answer-first
checkpoints diagnostically. Layered worked examples, step-linked visual
grounding, and metacognitive scaffolds supported reasoning repair. `OBSERVED`

Directness is not the enemy of learning. Unexamined passivity is.

### 4.2 Worked example and completion

Use for novice schemas, then fade by asking the learner to complete, debug, or
compare steps.

A 2026 CHI experiment with 155 learners tested
[Buggy and Guided interactive worked examples](https://doi.org/10.1145/3772318.3791631)
and found different effectiveness by prior knowledge, supporting adaptive
selection rather than one universal example format. `MEASURED-RCT`

### 4.3 Socratic question or hint

Use when the learner has enough relevant knowledge to reason and a question can
surface or repair a misconception.

Socratic dialogue is valuable as one action, not a universal refusal to answer.

### 4.4 Retrieval

Use when the concept has been learned but needs strengthening. Ask for recall,
prediction, reconstruction, or application before showing the answer, then give
corrective feedback.

The tutor should store the attempt, delay, support level, and next schedule.

### 4.5 Contrast and variation

Use near-neighbor examples, counterexamples, multiple representations, changed
surface features, and context shifts to test whether the learner has a rule or
only a template.

### 4.6 Self-explanation and teach-back

Ask the learner to explain a step, teach a younger learner, critique an AI
answer, or defend a model choice. Convert the explanation into evidence, not a
performance grade.

### 4.7 Simulation, build, and real action

Use when the target is a causal model, procedure, physical skill, design
judgment, or collaborative capability. The mentor changes a parameter, asks for
a prediction, observes action, and compares the result with the model.

### 4.8 Peer or human connection

Use when relationship, cultural interpretation, role modeling, reciprocal
explanation, safeguarding, or expert judgment adds value.

## 5. Adaptive support must fade on evidence

Scaffolding should be easy to restore without shame and should fade only when
the learner demonstrates the relevant step independently.

[AI-ALOE Apprentice Tutors](https://aialoe.org/wp-content/uploads/2026/03/AI-ALOE-Newsletter-Spring-26.pdf)
reported across 1,000+ adult learners and 256 sections that on-demand scaffolding
increased adoption by 50% relative to full scaffolding and that learners solved
more problems more efficiently. `OBSERVED`

A 2026 study of
[scaffolding for prompt-engineering skill](https://doi.org/10.1080/10494820.2026.2649547)
used intersubjectivity, ongoing diagnosis, calibrated support, and fading from
supported practice toward independent mastery. `OBSERVED`

The runtime rule is:

```text
support as much as needed
  → probe the next independent step
  → fade one support
  → restore immediately if the evidence changes
```

## 6. Learning objects should be generated from the action

The mentor should not retrieve the same page for every state. It should compile
the object the selected teaching action requires:

| Teaching action | Generated object |
|---|---|
| Explain | layered explanation with fidelity contract |
| Model | worked example with visible decision points |
| Hint | smallest cue that reopens progress |
| Retrieve | fresh probe without answer leakage |
| Contrast | matched example/counterexample pair |
| Simulate | executable model with inspectable variables |
| Teach-back | audience and rubric for explanation |
| Collaborate | role structure and shared artifact |
| Transfer | new context preserving the deep structure |

Every object inherits the same verified concept specification.

## 7. Memory is part of pedagogy, not storage

Memory should schedule action:

- retrieve concepts before they become inaccessible;
- vary the next context;
- repair repeated misconceptions;
- reconnect a current question to earlier knowledge;
- surface unfinished goals;
- celebrate compounding capability;
- fade supports that are no longer needed.

[Planning-guided tutoring with assessment-driven memory](https://aclanthology.org/2026.acl-long.325/)
is a current model of this direction: assessment and planning share memory rather
than treating chat history as personalization. `RESEARCH`

[LongTutor](https://aclanthology.org/2026.acl-long.1371/) makes long-horizon
personalization independently benchmarkable. `MEASURED-BENCH`

## 8. Self-regulation becomes observable and teachable

The tutor can help a learner set a goal, plan, monitor progress, choose help,
reflect, and revise.

A preregistered 2026 CS1 study with 1,059 learners compared a baseline tutor
with tutors prompted around Zimmerman’s planning/monitoring/reflection cycle and
the ICAP framework. The study’s central design contribution is that engagement
and learning are measured separately rather than treated as synonyms.
[`OBSERVED`](https://icer2026.acm.org/details/icer-2026-papers/18/When-More-Engagement-Doesn-t-Mean-More-Learning-LLM-Tutors-and-Self-Regulated-Learni)

A 2026 adolescent study,
[Regulating the AI Tutor](https://arxiv.org/abs/2606.08568), examines intention,
help-seeking, and self-regulated use rather than reducing learning to message
content. `RESEARCH`

The mentor should make planning and reflection useful but lightweight. A
reflection prompt that delays urgent help is not automatically good pedagogy.

## 9. The objective function

The control loop should optimize a hierarchy:

1. **Delayed independent transfer**
2. **Time to reliable independent success**
3. **Breadth across representations and contexts**
4. **Retention at the learner’s chosen horizon**
5. **Learner agency and willingness to return**
6. **Equitable access and participation**
7. **Human time used where it adds the most value**

Engagement, turns, streaks, content completed, and immediate correctness are
diagnostic variables—not the objective.

## 10. Falsifiable reference loop

For each learning episode:

```yaml
goal:
concept_spec:
prior_evidence:
state_before:
teaching_action:
generated_object:
learner_action:
feedback:
state_after:
next_retrieval:
human_connection:
transfer_probe:
```

A system deserves the word “adaptive” only if:

1. changing the state changes the selected action;
2. the reason is inspectable;
3. the learner or authorized human can correct the state;
4. the action is measured against delayed transfer;
5. the policy can be replaced when evidence finds a better one.

## 11. Final synthesis

The learning-science opportunity in 2026 is larger than digitizing established
techniques.

An abundant mentor can:

- notice the exact missing prerequisite;
- create a worked example around the learner’s world;
- switch to a question when reasoning is ready;
- listen to the learner explain;
- generate a fresh transfer task;
- remember what needs retrieval next month;
- include a peer, teacher, family member, or specialist;
- learn which sequence works from real outcomes.

Learning science becomes a living, inspectable, improvable control system around
each learner.

## Sources

1. Source archive, [The Learning-Science Floor](B1-learning-science.md), 109-source evidence spine.
2. Google, [Sierra Leone Guided Learning RCT](https://blog.google/products-and-platforms/products/education/measuring-the-impact-of-ai-on-teaching-and-learning/), 2026.
3. World Bank, [From Chalkboards to Chatbots](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324), 2025.
4. Fischer, Rau, and Rilke, [AI Tutoring Enhances Student Learning](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5992341), 2026.
5. Wang et al., [Tutor CoPilot](https://arxiv.org/abs/2410.03017).
6. Google DeepMind/Eedi, [Human-supervised AI tutoring trial](https://arxiv.org/abs/2512.23633), 2025.
7. [AITutor reasoning-centered product loop](https://arxiv.org/abs/2607.01692), 2026.
8. [Interactive worked examples](https://doi.org/10.1145/3772318.3791631), CHI 2026.
9. AI-ALOE, [Spring 2026 report](https://aialoe.org/wp-content/uploads/2026/03/AI-ALOE-Newsletter-Spring-26.pdf).
10. [Scaffolding prompt-engineering skill](https://doi.org/10.1080/10494820.2026.2649547), 2026.
11. [Planning-guided tutoring with assessment-driven memory](https://aclanthology.org/2026.acl-long.325/), ACL 2026.
12. [LongTutor](https://aclanthology.org/2026.acl-long.1371/), ACL 2026.
13. [When More Engagement Does Not Mean More Learning](https://icer2026.acm.org/details/icer-2026-papers/18/When-More-Engagement-Doesn-t-Mean-More-Learning-LLM-Tutors-and-Self-Regulated-Learni), ICER 2026.
14. [Regulating the AI Tutor](https://arxiv.org/abs/2606.08568), 2026.
15. [Learning Context Matters](https://scale.stanford.edu/ai/repository/learning-context-matters-measuring-and-diagnosing-personalization-gaps-llm-based), 2026.
16. [Training-free prompt optimization for math tutoring](https://arxiv.org/abs/2605.27088), 2026.
17. Google, [Learn Your Way](https://blog.google/products-and-platforms/products/education/learn-your-way/), 2025.
18. Khan Academy, [Building a better AI tutor](https://blog.khanacademy.org/how-khan-academy-is-building-a-better-ai-tutor-our-most-recent-learnings/), 2026.
19. [Adaptive AI scaffold for collaborative problem solving](https://doi.org/10.1016/j.learninstruc.2026.102418), 2026.
20. [SocratiCode](https://arxiv.org/abs/2605.17857), 2026.
21. [Knowledge-graph digital tutor RCT](https://doi.org/10.1186/s12909-026-09469-0), 2026.
22. Google, [Gemini study notebooks](https://blog.google/products-and-platforms/products/education/iste-students-2026/), 2026.
23. [EduAgentBench](https://arxiv.org/abs/2605.14322), 2026.
24. OECD, [Digital Education Outlook 2026](https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/01/oecd-digital-education-outlook-2026_940e0dd8/062a7394-en.pdf), 2026.
