---
title: "Designed from the Margin"
section: H1-accessibility-first
status: draft
date: 2026-07-25
---

# Designed from the Margin

![An accessibility-first tutoring loop preserves an ambitious learning goal while observing learner-selected evidence, composing access supports, probing privately, pivoting method, and escalating to a human when needed; the resulting curb cuts benefit every learner](../assets/diagrams/accessibility-first-pivot-loop.svg)

*Preserve the goal. Change the access path.*

The universal mentor should be built as though its first learner has dyslexia,
ADHD, low vision, a language-processing difference, an unreliable connection,
and years of being underestimated.

That learner is not an edge case. Designing for them produces a better mentor
for everyone:

- captions work in a loud home;
- speech input helps a beginning writer;
- visible steps help anyone solving a hard problem;
- self-pacing serves a learner working in a second language;
- multiple representations help everyone cross from intuition to formalism;
- offline, resumable sessions serve a remote village and an interrupted commute.

This is the curb-cut architecture. Build the SELPA-grade system first; the center
inherits the quality.

## The evidence has crossed from possibility to implementation

A 2026 meta-analysis of 29 (quasi-)experimental studies found a medium overall
effect for AI interventions with students with disabilities:
\(g = 0.588\). `MEASURED-META`

In May 2026, a randomized six-week study with 83 Chinese primary students
diagnosed with dyslexia found significantly greater arithmetic word-problem
gains with an adaptive, multisensory AI chatbot than with traditional
instruction. Intrinsic motivation increased and amotivation fell.
`MEASURED-RCT`

A 2026 single-case experiment used AI-generated visual explanations with three
Saudi learners aged 9–11 in an Arabic Grade 4 curriculum. All three showed
immediate, consistent, sustained reading-comprehension improvement during the
study. `MEASURED-SCED`

A 2025 review of 33 special-education GenAI studies estimated a large effect in
its experimental subset, \(g = 1.49\), but the estimate was statistically
inconclusive because the evidence base was small. `MEASURED-META`

The honest, optimistic conclusion is precise: AI-enabled visual, multisensory,
adaptive, and individually paced support already has a positive signal. The next
job is to identify which support worked, preserve validated intervention
sequences, measure durable independent performance, and expand large real-world
trials.

## The IEP boundary is clear

Under IDEA, required people form the IEP Team and parents must have meaningful
opportunity to participate. The AI can prepare editable drafts, translate,
summarize evidence, graph progress, generate candidate materials, and check
internal consistency.

It cannot:

- decide eligibility, placement, services, or accommodations;
- turn generated text into an authorized IEP;
- diagnose a child;
- replace parent, learner, educator, specialist, or agency authority;
- silently change the plan.

The rule is not “AI may never draft a sentence.” The rule is that people retain
informed authorship, consent, review, and decision authority.

## Accessibility is the base platform

The U.S. DOJ Title II rule requires covered state and local government
websites and mobile apps to meet WCAG 2.1 AA on its 2027/2028 timetable. The
mentor should target [WCAG 2.2 AA](https://www.w3.org/TR/WCAG22/) now.

Every core learning action needs:

- keyboard, switch, speech, and touch paths where appropriate;
- screen-reader-correct math, diagrams, feedback, and controls;
- captions and transcripts;
- alternatives to color, sound, gesture, dragging, motion, and time pressure;
- zoom and reflow;
- visible focus and accessible authentication;
- learner-tested equivalence across modalities.

An accessible interface is necessary, not sufficient. It must also preserve the
same learning goal and make the learner’s knowledge expressible through an
available channel.

## The mentor composes mechanisms, not personas

| If the barrier is… | The mentor can… | It must not conclude… |
|---|---|---|
| Shorter attention window | Segment, show one action, give immediate feedback, schedule movement | Low ability or low motivation |
| Working-memory overload | Externalize state, keep steps visible, use worked examples | Weak reasoning |
| Retention after initial success | Schedule retrieval, overlearn, vary context | “Never understood” |
| Abstraction without an anchor | Start concrete, teach the mapping, fade toward formalism | Permanently simpler content |
| Slower processing | Remove time pressure and preserve pauses | Lower ceiling |
| Reading or language load | Add TTS/STT, translation, vocabulary preview, visual or AAC access | Lower subject knowledge |
| Errors feel threatening | Probe privately, show personal growth, make return shame-free | Refusal or lack of care |

These mechanisms co-occur. The mentor composes supports and lets the learner,
family, and authorized professionals correct its hypothesis.

## The bidirectional loop

The system learns how to support the learner while the learner learns the
concept:

1. **Set the ambitious goal and access contract.**
2. **Probe prerequisites and interface barriers, not identity.**
3. **Teach a known-good method with fidelity.**
4. **Collect a brief, private, accessible performance sample.**
5. **Continue, fade, or pivot by an explicit rule.**
6. **Update a correctable, expiring hypothesis.**
7. **Escalate to a person when the evidence or authority requires one.**

[Data-Based Individualization](https://intensiveintervention.org/data-based-individualization/progress-monitoring)
provides the operational backbone: frequent graphed evidence, a validated
intervention platform, error analysis when response is insufficient, and team
consultation to intensify support.

### A pivot changes method, not word count

When performance does not improve, the mentor changes in this order:

1. remove interface or language barriers;
2. externalize memory and reduce simultaneous steps;
3. change representation;
4. change granularity or teach the missing prerequisite;
5. move to a worked, guided, or explicit method;
6. change pacing or dosage while preserving the goal;
7. hand the exact evidence and attempts to a person.

It does not pivot after every error. Each intervention has a minimum evidence
window, because constant method-switching prevents consolidation. Access
failure, distress, safety, or a team rule can override that window immediately.

## Known-good instruction becomes executable

Where replicated intervention evidence exists, the AI’s first advantage is
fidelity and dosage—not invention.

```yaml
goal: compare fractions with unlike denominators
method: explicit-worked-faded
sequence:
  - retrieve equal-part meaning
  - model one worked comparison
  - complete one together
  - learner completes one with visible steps
  - fade one scaffold after independent evidence
access:
  speech: optional
  persistent_steps: true
  response_timing: untimed
```

Generation changes the language, example, modality, and pacing. It does not
silently rewrite the teaching sequence.

## Advice must sometimes invert

| Common advice | Accessibility-first routing |
|---|---|
| Discover the method | Begin explicit, worked, and guided when prerequisite or memory load is high |
| Make struggle desirable | Keep challenge in the concept, not decoding, navigation, or inaccessible response mechanics |
| Assess often | Keep probes brief, private, low-stakes, and visibly useful |
| Fade on schedule | Fade on independent evidence; restore without shame |
| Use one elegant representation | Offer equivalents and teach their mapping |
| Personalize by “learning style” | Adapt to measured response, access need, and learner choice |

This does not lower the ceiling. It stops accidental barriers from masquerading
as the learner’s limit.

## Privacy by architecture

FERPA and IDEA protect education records. The 2025 COPPA amendments strengthen
data minimization and retention duties and include biometric identifiers in
covered personal information.

The mentor’s rule is simple:

```text
raw access signal     local when possible
support preference    narrow, correctable, expiring
diagnostic label      never generated
model training        off
disclosure            visible and logged
deletion              real
```

“Reads better with speech at 0.85× today” is useful. A permanent inferred
disability profile is usually unnecessary.

## The global baseline

On the learner’s device:

- semantic accessible UI;
- downloadable lessons and voices;
- resumable offline state;
- print and audio equivalents;
- learner-controlled sensors;
- portable evidence.

At a school or community hub:

- shared accessible peripherals;
- local inference and content cache;
- evidence dashboard without labels;
- local-language and caption review;
- accessible printing and tactile-material workflows;
- family participation and specialist telepresence.

At the regional layer:

- certified intervention library;
- accessibility and outcome evaluation;
- specialist routing;
- lawful records;
- disaggregated performance by access need, language, device, and connectivity;
- verified content pushed back to the edge.

The mentor is only universal if accessibility survives low bandwidth.

## The standard

> **Give every learner a world-class goal and many truthful paths to it. Execute
> proven methods with extraordinary fidelity and dosage. Let evidence change
> the method, never the learner’s worth.**

The system designed around the learner most likely to be excluded becomes the
most responsive mentor for everyone.

## Evidence trail

- [IDEA IEP Team](https://sites.ed.gov/idea/regs/b/d/300.321)
- [IDEA parent participation](https://sites.ed.gov/idea/regs/b/d/300.322)
- [U.S. Department of Education assistive-technology guidance](https://sites.ed.gov/idea/idea-files/at-guidance/)
- [DOJ Title II web/mobile accessibility rule](https://www.ada.gov/resources/2024-03-08-web-rule/)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [CAST UDL Guidelines 3.0](https://udlguidelines.cast.org/)
- [NCII progress monitoring and DBI](https://intensiveintervention.org/data-based-individualization/progress-monitoring)
- [AI interventions for students with disabilities meta-analysis](https://doi.org/10.3102/00346543241293424)
- [Dyslexia arithmetic-chatbot RCT](https://doi.org/10.1177/00222194261450136)
- [Arabic dyslexia visual-instruction study](https://doi.org/10.3389/feduc.2026.1727782)
- [Generative AI in special education review](https://doi.org/10.1177/02666669251335655)
