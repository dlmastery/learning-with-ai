---
title: "LessonOrca as a measurement-ready learning system"
wave: E
section: E2
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
measurement_status: "public product audit complete; no authorized telemetry export available"
sources_count: 20
---

# E2 — Turn LessonOrca into Evidence

## Executive finding

LessonOrca is not merely an AI tutor. Its public July 2026 product is a
human-plus-AI continuity system for tutoring centers:

- the next tutor receives the learner’s history and current focus;
- AI drafts lesson plans, notes, homework, and parent communication;
- the learner can receive between-session support;
- parents and tutors can review AI interactions;
- organizations set guidelines and retain control.

On 19 April 2026, LessonOrca publicly reported live use in three Bay Area
centers by 25 tutors supporting 100 students. `VENDOR`

That is meaningful deployment, but it is not yet a measured learning effect.
This repository contains no authorized PostHog export, preregistered analysis,
or de-identified outcome dataset. Therefore this section reports:

1. what the public product currently implements;
2. which claims those observations support;
3. the exact privacy-preserving event contract needed for measurement;
4. a staged study that can test the product without disrupting tutoring;
5. the product decisions that should follow each result.

The central measurement decision is:

> **Do not optimize chat duration, turns, or return rate as the learning goal.
> Optimize delayed independent transfer, then use engagement only to explain
> whether the learner reached enough high-quality practice.**

## Evidence labels

| Label | Meaning |
|---|---|
| `MEASURED-RCT` | Randomized learner or human-AI field comparison |
| `MEASURED-BENCH` | Tutor-policy or dialogue benchmark |
| `OBSERVED` | Publicly inspectable product or policy |
| `VENDOR` | LessonOrca or provider-reported deployment/capability |
| `INFERENCE` | Product or study decision derived from evidence |

## 1. The public product as of 25 July 2026

### 1.1 The primary product is tutor continuity

The current homepage leads with “Your tutors are awesome. We give them context.”
It describes a platform for tutoring centers that connects:

- pre-session flags;
- AI-generated plans;
- session notes;
- student support between sessions;
- persistent learning profiles;
- parent communication;
- center-level branding and guidelines.

`OBSERVED`

This positioning is important. The strongest current field evidence for AI in
tutoring includes human-AI systems:

- Tutor CoPilot’s preregistered K–12 trial found that offering AI guidance to
  tutors increased topic mastery by 4 percentage points overall and by 9 points
  for students of lower-rated tutors, at a reported annual AI cost of about $20
  per tutor. `MEASURED-RCT`
- The 2025 LearnLM/Eedi exploratory trial had expert tutors supervise AI-drafted
  messages. Tutors approved 76.4% with zero or minimal edits; the AI-supported
  group was 5.5 percentage points more likely to solve novel subsequent
  problems than the human-tutor-only group. `MEASURED-RCT`

LessonOrca therefore sits in a high-value architecture: AI can raise the
consistency and context available to a real tutor while the human preserves
relationship, judgment, and accountability.

### 1.2 The between-session tutor is Socratic-oriented

The homepage states “Socratic method only” and “guides students to answers,
never gives them.” It also advertises organization-specific guidelines,
parent linking, role-based access, isolated data per center, and data export.
`VENDOR`

Socratic dialogue is a useful controlled baseline, not a universal endpoint.
Current 2026 research sharpens this:

- *Hey Chat, Can You Teach Me?* separates curriculum sequencing, Socratic
  dialogue, and learner-state inference. A learned policy over a prerequisite
  graph outperforms heuristic, frontier-model, and dialogue-specialized
  baselines on simulated curriculum mastery and turn efficiency.
  `MEASURED-BENCH`
- PEARL trains a 30B Socratic tutor with explicit learner-state simulation and
  multi-objective pedagogical rewards, showing that tutor behavior is a policy
  optimization problem, not a system-prompt slogan. `MEASURED-BENCH`
- 2026 studies of dynamic Socratic assessment, K–12 programming, and
  question-only writing feedback report promising engagement, reasoning, or
  learning signals in their contexts. Scope and designs vary.

The product hypothesis should become:

> Socratic prompts work best when the learner has enough prerequisite knowledge
> to answer and when the target is explanation, justification, or reflection.
> A teaching router should select worked example, explicit instruction,
> verification, retrieval, or direct answer-with-teach-back when those better
> fit the learner and moment.

### 1.3 The public deployment snapshot

The April 2026 LessonOrca post reports:

| Measure | Public value | Evidence |
|---|---:|---|
| Centers | 3 | `VENDOR` |
| Tutors | 25 | `VENDOR` |
| Students | 100 | `VENDOR` |
| Geography | Bay Area | `VENDOR` |
| Report date | 2026-04-19 | `OBSERVED` |

These values establish active use at small pilot scale. They do not establish
retention, learning gain, parent satisfaction, center economics, or causal
impact. Every later number must have a date and denominator because this
snapshot will age quickly.

## 2. What can be claimed today

### Supported by public evidence

- LessonOrca is deployed in tutoring centers. `VENDOR`
- It implements cross-session context and persistent profiles. `OBSERVED`
- It supports AI-drafted tutor workflow artifacts. `OBSERVED`
- It exposes AI interactions to parent/tutor oversight. `OBSERVED`
- It has a Socratic-oriented between-session tutor. `OBSERVED`
- It offers organization guidelines, role separation, tenant isolation, and
  data export as product features. `VENDOR`

### Not yet supported by public evidence

- students learn more because of LessonOrca;
- Socratic-only is the best tutoring policy;
- persistent profiles improve outcomes;
- tutor preparation time has fallen by a measured amount;
- parent transparency reduces churn;
- the system is COPPA compliant in operation;
- generated plans, worksheets, summaries, or profiles are accurate;
- benefits persist without AI support;
- effects generalize beyond the three reported centers.

These are not criticisms. They are the measurement queue.

## 3. Privacy posture before analytics

The public privacy policy is dated 3 January 2025, before the FTC’s April 2025
publication of final COPPA amendments. It describes:

- student account, learning, chat, audio/transcript, and usage data;
- parental consent records;
- Gemini processing;
- education-only use;
- no advertising or sale;
- parent review and deletion rights;
- deletion within 30 days after account closure;
- indefinite retention only for anonymized aggregate data;
- encryption and role-based access.

`OBSERVED`

Before research telemetry is used, update the policy and implementation together:

1. Name PostHog or any analytics processor and its data region.
2. State that raw chat, audio, transcript, names, email, IP, and free text are
   never sent as product-analytics properties.
3. Replace “improving educational algorithms and content” with a specific,
   consented purpose and state whether any training occurs.
4. Define purpose-specific retention for active accounts, not only closed ones.
5. Address audio, voice, and biometric treatment under the 2025 COPPA changes.
6. Separate consent for any third-party disclosure that requires it.
7. Make delete/export controls testable from the parent dashboard.
8. Publish the date, cohort, and definition behind every aggregate claim.

This follows F8: analytics should produce evidence without creating a shadow
learner dossier.

## 4. Event contract: no raw child content in analytics

Product analytics receives pseudonymous, enumerated events. The product database
may contain authorized educational records under its own controls; the two
stores are not interchangeable.

### Identity boundary

```yaml
analytics_actor_id: random_rotating_id
organization_id: pseudonymous_center_id
learner_age_band: [under_13, 13_15, 16_17, adult, unknown]
allowed:
  - broad grade band
  - subject taxonomy
  - concept identifier
  - assigned experiment variant
forbidden:
  - name
  - email
  - phone
  - IP copied into event properties
  - raw prompt or response
  - audio
  - transcript
  - disability label
  - parent message
```

### Minimum event set

| Event | Required properties | Why |
|---|---|---|
| `learning_goal_started` | concept ID, grade band, subject, source of goal, baseline band | denominator |
| `support_mode_selected` | mode, selector: learner/tutor/router, rationale code, hint level | policy exposure |
| `attempt_submitted` | item/version ID, support level, correctness, error taxonomy, confidence band | learning trace |
| `teaching_move_delivered` | move taxonomy, grounded tier, human-edited yes/no | tutor behavior |
| `human_override_recorded` | artifact type, accept/edit/reject, reason code | AI quality |
| `goal_mastered_in_session` | mastery rule/version, evidence count | immediate outcome |
| `independent_probe_completed` | delay band, no-AI flag, transfer distance, score | primary outcome |
| `session_ended` | completed/paused/abandoned, active minutes band, reason code | reach |
| `profile_hypothesis_updated` | field taxonomy, evidence count, confidence band, reviewer | learner model |
| `parent_or_tutor_reviewed` | artifact type, action, accuracy rating band | oversight |
| `privacy_action_completed` | export/delete/revoke, latency band, success | rights |
| `safety_or_access_handoff` | route level, completion, latency band | guardrail |

Free-text notes and dialogue stay outside PostHog. If a research classifier
derives an error or teaching-move code, it runs in the controlled backend and
stores model/version, confidence, and a human-audit sample.

## 5. The metric tree

### North-star outcome

**Delayed independent transfer**

```text
correct solution to a new problem
at least 7 days after instruction
without tutor or AI assistance
using the target concept in a changed surface context
```

This is a stringent outcome for a pilot. It converts tutoring from “chat felt
good” into “the learner can now do something new alone.”

### Leading learning indicators

- baseline-to-exit change on equivalent items;
- independent step reached;
- hint level needed at final attempt;
- misconception repaired;
- time to first successful explanation or equivalent expression;
- next-session retrieval;
- scaffold fading without performance loss;
- transfer distance.

### Human-tutor indicators

- preparation minutes;
- percentage of plan accepted, edited, or rejected;
- grade/level appropriateness;
- use of guiding questions, worked examples, checking, and error diagnosis;
- tutor confidence;
- learner mastery stratified by tutor baseline;
- time spent with learner versus administration.

### Engagement as a mediator, not the goal

- assigned session started;
- active learning minutes;
- meaningful attempts;
- return for scheduled retrieval;
- completion;
- learner-requested pause;
- reason for abandonment.

A June 2026 pair of elementary RCTs found that human engagement support increased
AI-platform engagement by 71–80%, but usage remained low and reading outcomes
did not improve. The lesson is constructive: access and minutes are upstream
conditions, not substitutes for instructional quality and learning measurement.
`MEASURED-RCT`

### Guardrails

- incorrect or ungrounded generated item;
- human correction rate;
- false mastery;
- refusal on valid educational content;
- repeated question loop;
- learner-reported frustration;
- privacy deletion failure;
- safety escalation failure;
- outcome disparity by language, access need, center, and device.

## 6. The staged evidence program

### Stage 0 — instrument and audit

Duration: four weeks or until event completeness is stable.

- publish event dictionary and metric definitions;
- validate denominator consistency against product records;
- manually audit a stratified sample of AI artifacts;
- verify privacy separation and deletion;
- measure missingness by center, role, device, and age band;
- freeze the primary metric before inspecting variants.

Output: a data-quality report, not a learning claim.

### Stage 1 — prospective observational baseline

Record current Socratic-oriented behavior without changing teaching.

- delayed independent transfer;
- tutor edits/rejections;
- session completion;
- return for retrieval;
- parent/tutor review;
- center and concept variation.

Use the baseline to estimate variance, intraclass correlation, and feasible
sample size. At the April 2026 scale of three centers and 100 learners, ordinary
center-level A/B tests are likely underpowered. Repeated concept-level measures
can inform design, but should not be mistaken for independent learners.

### Stage 2 — test the teaching-mode router

**Question:** Is Socratic-only better than an evidence-routed mix?

Eligible concept units are blocked within learner by subject and baseline, then
randomized to:

1. **Socratic-first:** questions and hints, current policy.
2. **Adaptive router:** explicit/worked for missing prerequisites or overload;
   Socratic for partial knowledge and explanation; retrieval for known material;
   direct answer plus teach-back when the learner needs a fact or time-sensitive
   correction.

Both groups receive:

- the same learning goal;
- verified content;
- equivalent practice opportunity;
- the same access accommodations;
- human escalation;
- a delayed no-AI transfer probe.

Primary outcome: delayed independent transfer.  
Secondary: mastery efficiency, frustration, hint dependence, and next-session
retrieval.  
Analysis: intention-to-treat, learner-clustered uncertainty, concept and center
effects, preregistered exclusions.

This is not “Socratic versus cheating.” It compares two valid teaching policies.

### Stage 3 — test tutor continuity

Randomize eligible sessions or use a stepped-wedge rollout:

- basic scheduling/context;
- AI-generated evidence-linked pre-session brief and candidate plan.

Measure:

- tutor preparation time;
- plan edit/reject rate;
- teaching-move quality;
- mastery and delayed transfer;
- differential effect by tutor experience;
- parent summary accuracy.

Tutor CoPilot predicts the largest gain may occur for tutors who begin with less
experience or lower historical ratings. Pre-register that heterogeneity rather
than discovering it after the fact.

### Stage 4 — test memory over months

Randomize retrieval scheduling and profile use only after the learner state is
inspectable and correctable.

- current-session-only context;
- learner-owned persistent evidence plus scheduled retrieval.

Primary outcome: retention and transfer after 30–90 days. Do not randomize away
a legally required accommodation or human-authored plan.

## 7. Dashboards that answer decisions

### Product quality

```text
How often is an AI artifact accepted unchanged?
When it is edited, what kind of error was fixed?
Which concepts and grade bands cause rejection?
Does the correction recur after a model or prompt release?
```

### Learner impact

```text
Did the learner independently solve a new problem later?
Which support mode produced that result for this prerequisite state?
Did scaffolds fade?
Was the gain retained next session and next month?
```

### Center value

```text
How much tutor preparation time moved into learner-facing time?
Did session continuity improve?
Did parent-reviewed summaries become more accurate and timely?
Did outcomes improve most where expert support was previously scarce?
```

Never show a single “learner ability score.” Show evidence by goal, support,
time, and uncertainty.

## 8. Product decisions already justified

### Keep

- human tutor control;
- cross-session continuity;
- parent/family access and export;
- organization-specific policies;
- generated plans as editable drafts;
- no-ad education-only business model;
- between-session availability.

### Evolve

- “Socratic method only” → **transparent teaching-mode router**;
- persistent profile → **learner-owned, evidence-linked, correctable state**;
- “parents see everything” → **age-aware oversight with clear family policy and
  learner privacy boundaries**;
- product analytics → **outcome instrumentation**;
- content generation → **grounding and artifact verification tiers**;
- session completion → **delayed independent transfer**.

## 9. Acceptance tests

- [ ] Public deployment numbers include date, definition, and denominator.
- [ ] No telemetry result is reported without an authorized aggregate export.
- [ ] Raw child text, audio, transcript, identity, and IP are absent from
      analytics properties.
- [ ] Privacy policy and processor list match the deployed analytics stack.
- [ ] Every goal has a baseline and a delayed independent probe.
- [ ] Engagement metrics are never called learning outcomes.
- [ ] Every AI-generated artifact supports accept/edit/reject with reason.
- [ ] Teaching-mode exposure is logged with selector and rationale.
- [ ] Experiments compare ethically acceptable instruction.
- [ ] Analysis accounts for repeated observations and center clustering.
- [ ] Primary outcomes and exclusions are frozen before variant inspection.
- [ ] Results are disaggregated without publishing small identifiable cells.
- [ ] Parent/tutor review is measured for accuracy, not only opens.
- [ ] The learner can inspect and correct the persistent profile.
- [ ] Any claim of impact can be reproduced from a versioned analysis artifact.

## Source index

1. LessonOrca product — [public homepage, observed 25 July 2026](https://lessonorca.com/)
2. LessonOrca deployment snapshot — [3 centers, 25 tutors, 100 students, 19 April 2026](https://lessonorca.com/blog/skydeck-pad-13-canopy)
3. LessonOrca privacy policy — [last updated 3 January 2025](https://lessonorca.com/privacy)
4. LessonOrca free worksheet generator — [public product](https://lessonorca.com/tools/worksheet)
5. Tutor CoPilot RCT — [Wang et al.](https://arxiv.org/abs/2410.03017)
6. LearnLM/Eedi classroom RCT — [LearnLM Team and Eedi, 2025](https://arxiv.org/abs/2512.23633)
7. AI tutoring and unrestricted access RCT — [Fischer, Rau, and Rilke, 2026](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5992341)
8. AI assistance mode field experiment — [Wang et al., 2026](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6077186)
9. Structuring Socratic dialogue — [arXiv:2606.11744](https://arxiv.org/abs/2606.11744)
10. PEARL Socratic tutor policy training — [arXiv:2605.29582](https://arxiv.org/abs/2605.29582)
11. SocratiCode K–12 participatory study — [arXiv:2605.17857](https://arxiv.org/abs/2605.17857)
12. Socratic Mind formative assessment — [Technology, Knowledge and Learning, 2026](https://doi.org/10.1007/s10758-026-10007-6)
13. LLM Socratic agent field study — [Computers & Education, 2025](https://doi.org/10.1016/j.compedu.2025.105494)
14. Question-only Socratic dialogue — [Assessing Writing, 2026](https://www.sciencedirect.com/science/article/pii/S1060374326000512)
15. Access Is Not Enough RCTs — [Robinson et al., 2026](https://doi.org/10.26300/pz7p-p388)
16. Data-Based Individualization progress monitoring — [NCII](https://intensiveintervention.org/data-based-individualization/progress-monitoring)
17. 2025 COPPA final amendments — [Federal Trade Commission](https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-312-coppa-final-rule-amendments)
18. PostHog product analytics and experiments — [PostHog](https://posthog.com/)
19. PostHog Trust Center — [current security and privacy materials](https://trust.posthog.com/)
20. Generated assessment validity protocol — [this survey’s C2 raw research](C2-generated-assessment-validity-2026.md)

## Decision

**Treat LessonOrca as an evidence engine, not a case-study endorsement.** Preserve
its strong human-tutor continuity architecture. Instrument delayed independent
transfer, artifact correction, tutor time, and learner-owned state. Test
Socratic-first against a transparent adaptive teaching router. Keep child
content out of analytics, update the public privacy contract, and publish only
date-stamped aggregate results with denominators.

The product becomes survey evidence when a reader can reproduce the chain from
assigned teaching policy to independent learning later.
