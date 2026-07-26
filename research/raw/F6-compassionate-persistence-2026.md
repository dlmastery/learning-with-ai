---
title: "Compassionate persistence and learner agency at the July 2026 frontier"
wave: F
section: F6
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 20
supersedes: "research/raw/F6-motivation-persistence.md (removed)"
---

# F6 — Compassionate Persistence and Learner Agency

## Executive finding

The July 2026 question is not whether learners can remain engaged with an AI
mentor. Well-designed tutors can already improve measured learning while learners
report greater engagement and motivation than strong classroom comparison
conditions.

The design question is how to turn that availability into **voluntary,
productive, learner-owned continuation**.

The persistence primitive is:

> **Connect learning to a purpose the learner owns; offer the smallest meaningful
> next action; calibrate challenge; make capability growth visible; connect the
> learner to people and projects; and make every return shame-free.**

The optimization target is independent capability and durable re-engagement—not
minutes, clicks, streaks, emotional attachment, or dependence on the mentor.

This report replaces the prior F6 draft, which centered historical MOOC
completion and framed motivational adaptation primarily as an engagement hazard.
That framing was removed rather than carried into the active evidence base.

## Evidence labels

| Label | Meaning |
|---|---|
| `MEASURED-RCT` | Randomized learner or goal-pursuit comparison |
| `MEASURED-BENCH` | Quasi-experimental, deployed, or conversation-level evaluation |
| `OBSERVED` | Inspectable system or behavior |
| `INFERENCE` | Architecture derived from the evidence |

## 1. Current tutors can support motivation and engagement

### 1.1 A strong positive RCT

The 2025 Harvard physics
[AI tutoring RCT](https://www.nature.com/articles/s41598-025-97652-6)
randomized 194 students in a crossover design comparing a research-informed AI
tutor with in-class active learning on matched content. The AI condition produced
higher learning in less time. Learners reported:

- engagement mean 4.1 versus 3.6, *p* < .0001;
- motivation mean 3.4 versus 3.1, *p* < .001;
- comparable enjoyment and growth-mindset ratings.

`MEASURED-RCT`

The tutor combined:

- active engagement;
- cognitive-load management;
- growth-oriented interaction;
- explicit sequencing for multi-part problems;
- timely feedback;
- learner-controlled pace.

This is the relevant baseline: an AI tutor can be both more effective and more
motivating when the experience is intentionally structured.

### 1.2 July 2026 school evidence

A 22 July 2026
[Scientific Reports study](https://www.nature.com/articles/s41598-026-62920-6)
compared AI-supported and teacher-led Grade 12 mathematics classes in four
Iranian public high schools. The quasi-experimental sample included 97 male
students. The AI-supported group performed better on immediate achievement,
delayed retention, and cognitive, behavioral, and emotional engagement. Learners
described personalized practice, immediate feedback, error correction,
accessibility, and sustained engagement as useful. `MEASURED-BENCH`

The narrow sample and nonrandom assignment bound generalization. They do not
diminish the design signal: personalization, feedback, repair, and teacher
integration can reinforce one another.

### 1.3 Motivation can become visible in interaction

A 10 July 2026 analysis of
[16,851 tutor responses](https://arxiv.org/abs/2607.09919) from 203 students and
2,214 programming conversations measured *productive continuation* after
different response styles. Verification feedback had the highest rate, 82.4%;
direct answers had the lowest, 62.7%. Effects varied with the learner’s situation
and were largest in high-cognitive-load contexts. `MEASURED-BENCH`;
observational associations.

This suggests an operational moment-to-moment metric:

```text
Did the response help the learner take another productive step?
```

That is better than “did the learner send another message?”

## 2. The compassionate-persistence flywheel

### 2.1 Purpose

The learner, family, teacher, or community names why the capability matters:

- pass a certification;
- repair a water pump;
- tell a family story in another language;
- build a game;
- qualify for a course;
- understand a medical decision;
- teach a younger sibling;
- investigate a local problem.

The mentor keeps the purpose visible and revisable. It does not manufacture a
purpose through rewards.

### 2.2 Small meaningful action

When momentum is low, reduce activation energy without making the action empty:

- label one force;
- predict one state change;
- explain one line;
- retrieve one foundational relation;
- record one spoken sentence;
- ask one question of a peer;
- photograph one local example.

The action must produce evidence or an artifact—not merely a click.

### 2.3 Calibrated challenge

The learner gets a task just beyond current fluent performance, plus control over
support:

```text
try independently
  → choose a structural hint
  → request the first step
  → compare a worked example
  → solve a near case
  → return to the original
```

The [KITE tutoring system](https://aclanthology.org/2026.bea-1.57/) uses
intent-aware Socratic responses, targeted hints, guiding questions, progressive
scaffolding, and retrieval grounding for algorithm tracing. Expert and simulated
evaluations report grounded, pedagogically appropriate feedback and improved
follow-up answers in the simulated-student condition. `MEASURED-BENCH`

### 2.4 Visible capability

Show what the learner can now do:

- “You solved this without a cue.”
- “You can now translate between the diagram and equation.”
- “Your recall interval moved from three days to three weeks.”
- “Your model predicted a new case.”
- “Your explanation helped another learner.”

Evidence is specific and inspectable. It does not say “You are smart.”

### 2.5 Belonging and contribution

Learning persists when it joins a social world:

- teacher acknowledgment;
- peer collaboration;
- family participation;
- expert feedback;
- a real audience;
- contribution to a community artifact.

A 2026 preregistered three-arm RCT of
[AI-assisted goal setting](https://arxiv.org/abs/2603.17887) with 517
participants found higher two-week goal progress than no support (*d* = 0.33).
Compared with a matched reflective questionnaire, the clearest added value was
increased perceived social accountability, which mediated progress.
`MEASURED-RCT`; career-goal context, not schooling.

The mentor can supply continuity and accountability while deliberately connecting
the learner to people rather than substituting for them.

### 2.6 Return without shame

A lapse is scheduling information:

- summarize where the learner stopped;
- ask whether the purpose changed;
- offer a two-minute re-entry action;
- reschedule memory work;
- restore the last artifact;
- invite a person if practical barriers remain.

There is no broken streak, lost status, guilt message, or escalating notification.

## 3. Detect friction, then ask

The mentor can observe possible friction:

| Signal | Possible cause | First response |
|---|---|---|
| repeated same error | prerequisite gap, representation mismatch | offer a contrast and ask what feels unclear |
| long pause | thinking, interruption, connectivity, fatigue | wait; offer resumable state |
| rapid guessing | overload, urgency, low value, uncertainty | reduce scope; reconnect to purpose |
| repeated direct-answer requests | deadline, low confidence, task mismatch | ask what outcome is needed; route mode |
| avoidance of one modality | access barrier or preference | offer equivalent modality |
| returning after absence | life happened | restore context and welcome |

The system does not infer an emotion as fact. It says:

> “This looks like it may be costing more effort than it should. Would a smaller
> step, a different representation, or a pause help?”

Emotion and motivation data remain purpose-limited, uncertain, learner-visible,
and deletable. The 2026
[Theory of Mind in education tutorial](https://aclanthology.org/2026.bea-1.1/)
explicitly connects adaptive feedback with mutual modeling, metacognition, and
privacy. `OBSERVED`

## 4. Response policy for productive continuation

| Learner moment | Mentor action |
|---|---|
| confused but engaged | verify what is correct, isolate one gap, give one next step |
| high cognitive load | shorten horizon, externalize state, guide stepwise |
| confident and fluent | fade support, increase transfer distance |
| bored | increase agency, novelty of application, or challenge—not decoration |
| anxious about error | lower consequence, show reversible attempts, normalize revision |
| blocked by access | change modality, device demand, language, or human route |
| asks for answer under deadline | provide mode choices: answer + explanation, scaffold, or verification |
| wants to stop | save state and end cleanly |

[Tutor-persona steering](https://aclanthology.org/2026.bea-1.7/) demonstrates
that scaffolding, directiveness, feedback, and affective support can be controlled
from human dialogue signals while preserving interpretable tutor variation.
`MEASURED-BENCH`

[Training LLM tutors for dialogue outcomes](https://arxiv.org/abs/2503.06424)
generates candidate utterances, estimates follow-up correctness with a student
model, scores pedagogical quality, and preference-trains an 8B open model. The
reported result increases predicted student correctness while maintaining
pedagogical quality. `MEASURED-BENCH`

The next step is to optimize these policies against real learning, transfer,
agency, and return—not proxy engagement.

## 5. Proactive support with consent

[SCALA](https://aclanthology.org/2026.acl-industry.107/) deployed proactive
predicted questions and tutoring in a semester-long Python course with more than
1,500 students. Predictive questions were frequently selected, substantially
overlapped real student questions, and learners preferred SCALA’s answers to
comparison responses for their real queries. `MEASURED-BENCH`

The safe constructive pattern:

1. predict a likely question or obstacle;
2. make the support visible but optional;
3. explain why it appeared;
4. let the learner dismiss or tune it;
5. learn from aggregate usefulness;
6. never turn proactive help into compulsory interruption.

## 6. Goal, progress, and memory operate together

The persistence system integrates:

- the [learner-owned state](../../survey/06-learner-owned-state.md);
- the [depth ladder](../../survey/13-one-concept-four-depths.md);
- the [memory loop](../../survey/14-the-memory-that-compounds.md);
- the assessment evidence stream;
- the teacher, peer, family, and expert network.

Example:

```text
purpose: qualify as a solar technician
current capability: can wire a series circuit; uncertain on fault isolation
friction: reading-heavy explanation on a shared phone
repair: spoken local-language scenario + physical diagram
next action: diagnose one simulated fault
evidence: identifies open circuit with one cue
progress: new capability enters learner-owned state
memory: schedule a varied physical retrieval in four days
social: prepare a two-minute explanation for the workshop mentor
```

Motivation is not a separate “gamification layer.” It is what happens when the
learning system respects the learner’s purpose, makes the next action possible,
and returns evidence of growing agency.

## 7. Metrics that keep the system honest

### Optimize

- learner-chosen goal progress;
- productive continuation after an obstacle;
- successful return after a lapse;
- independent attempts before help;
- declining hint dependence;
- transfer and delayed retention;
- artifacts completed and used;
- learner-reported agency, competence, and belonging;
- human connection when requested;
- equitable outcomes across device, language, disability, and region.

### Monitor

- session length;
- messages;
- daily activity;
- notifications opened.

These are operational diagnostics, not success metrics.

### Never optimize

- time in app;
- compulsive return;
- streak preservation;
- emotional dependency;
- disclosure volume;
- praise acceptance;
- replacement of human relationships.

## 8. Universal-access consequences

- Every session begins from a resumable artifact, not a blank chat.
- The learner can complete a meaningful two-minute action offline.
- Voice and local language reduce activation energy.
- Community projects make progress socially useful.
- Teachers see aggregate friction and can intervene without surveillance.
- Missed sessions trigger workload repair, not punishment.
- Shared devices preserve separate states.
- A trusted person can receive a learner-approved handoff with the exact blocker.
- The learner can choose quiet mode, no notifications, or scheduled check-ins.

A 2025 study of
[rural junior-high learners](https://www.nature.com/articles/s41599-025-05676-0)
examines engagement inside an AI-powered adaptive environment; it is especially
relevant because access context and learner regulation cannot be reduced to model
quality. `MEASURED-BENCH`

## 9. Acceptance tests

- [ ] Purpose is learner-owned, revisable, and visible.
- [ ] Every motivational intervention advances a meaningful action.
- [ ] Challenge and scaffolding adapt from evidence.
- [ ] Progress language describes capability, not fixed traits.
- [ ] The learner controls help, modality, pace, notifications, and stopping.
- [ ] Emotion/motivation inferences are uncertain and confirmed by asking.
- [ ] Returns restore state without shame or lost status.
- [ ] Human connection is strengthened, not replaced.
- [ ] Success metrics include independence, transfer, return, and agency.
- [ ] Session length and click volume are never objectives.
- [ ] The same loop works offline, in local language, and on shared devices.
- [ ] Learner can inspect, export, correct, and delete persistence data.

## Source index

1. AI tutoring vs active learning RCT — [Scientific Reports 2025](https://www.nature.com/articles/s41598-025-97652-6)
2. AI tutoring, retention, and engagement — [Scientific Reports 2026](https://www.nature.com/articles/s41598-026-62920-6)
3. Productive continuation — [arXiv:2607.09919](https://arxiv.org/abs/2607.09919)
4. AI-assisted goal setting RCT — [arXiv:2603.17887](https://arxiv.org/abs/2603.17887)
5. SCALA proactive tutoring — [ACL 2026](https://aclanthology.org/2026.acl-industry.107/)
6. KITE grounded tutoring — [BEA 2026](https://aclanthology.org/2026.bea-1.57/)
7. Tutor-persona steering — [BEA 2026](https://aclanthology.org/2026.bea-1.7/)
8. Training tutor utterances — [arXiv:2503.06424](https://arxiv.org/abs/2503.06424)
9. Just-in-time adaptive feedback — [BEA 2026](https://aclanthology.org/2026.bea-1.8/)
10. Structured programming feedback — [BEA 2026](https://aclanthology.org/2026.bea-1.42/)
11. Theory of Mind for education — [BEA 2026](https://aclanthology.org/2026.bea-1.1/)
12. LongTutor — [ACL 2026](https://aclanthology.org/2026.acl-long.1371/)
13. PathBuilder — [ACL 2026](https://aclanthology.org/2026.acl-demo.50/)
14. IntelliCode — [EACL 2026](https://aclanthology.org/2026.eacl-demo.10/)
15. Teachable-agent engagement patterns — [Scientific Reports 2025](https://www.nature.com/articles/s41598-025-24841-8)
16. Rural learner engagement — [HSSC 2025](https://www.nature.com/articles/s41599-025-05676-0)
17. Motivation to learn AI, self-determination network — [npj Science of Learning 2025](https://www.nature.com/articles/s41539-025-00339-w)
18. AI acceptance and EFL engagement — [Scientific Reports 2025](https://www.nature.com/articles/s41598-025-11305-2)
19. AITutor EvalKit — [EACL 2026](https://aclanthology.org/2026.eacl-demo.32/)
20. CAST — [UDL Guidelines 3.0](https://udlguidelines.cast.org/)

## Decision

**Build for compassionate persistence.** The mentor notices friction early,
offers a useful next move, gives the learner control, makes real growth visible,
and connects learning to a purpose and people. It succeeds when the learner can
continue without it—and trusts that it will be ready, without judgment, whenever
they return.
