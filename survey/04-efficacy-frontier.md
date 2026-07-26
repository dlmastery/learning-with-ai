---
title: "The Efficacy Frontier — From Promising Tutor to Universal Learning Infrastructure"
section: B2-ai-tutoring-efficacy
status: draft
date: 2026-07-25
---

# The Efficacy Frontier

![Six evidence cards summarizing positive AI-supported learning results available by July 2026](../assets/diagrams/evidence-frontier-2026.svg)

*These results use different populations, interventions, and outcome measures.
They are a portfolio of signals—not a single pooled effect size.*

The evidence question has changed.

The useful question is no longer whether an AI conversation can sometimes help
a learner. Randomized studies across school, university, and adult-learning
settings now show meaningful **unaided** gains. The task is to turn that signal
into dependable learning infrastructure that reaches every child.

> AI tutoring is effective enough to deploy, replicate, and improve with
> urgency. Its next standard is durable, transferable, equitable learning at the
> device, connectivity, and cost level of the communities it serves.

## 1. The positive evidence is now a portfolio

| Study or deployment | Result | System lesson |
|---|---:|---|
| Sierra Leone, 1,763 students and 12 schools | **+0.258 SD mathematics** | Guided, scaffolded dialogue can work in a school deployment |
| Nigeria, teacher-supported six-week program | **+0.31 SD combined index** | Facilitators, curriculum, peers, and scheduled access are part of efficacy |
| India, 83 government residential schools | **nearly +0.5 SD mathematics** | Implementation support turned light use into sustained learning |
| July 2026 knowledge experiment | **+0.27 SD immediate unaided test** | Explanation-oriented use persisted one week later |
| Education performance-gap experiment | gap **0.548→0.139 SD** | AI can make scarce expertise disproportionately available |
| Tutor plus role-distinct AI peers | **~65% vs ~42%** unaided accuracy | A learner can benefit from an orchestrated social learning environment |

Sources:

- [Sierra Leone impact evaluation](https://deepmind.google/blog/measuring-the-impact-of-learning-with-ai-in-sierra-leone-and-beyond/) `MEASURED-RCT`
- [Nigeria working paper](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324) `MEASURED-RCT`
- [India implementation experiment](https://www.nber.org/papers/w34683) `MEASURED-RCT`
- [July 2026 knowledge-acquisition experiment](https://arxiv.org/abs/2607.08849) `MEASURED-RCT`
- [Education performance-gap experiment](https://www.nber.org/papers/w34851) `MEASURED-RCT`
- [Tutor-and-peers experiment](https://arxiv.org/abs/2604.02677) `MEASURED-RCT`

The interventions differ. That is their collective strength: the positive
signal is not confined to one country, age, subject, product, or delivery
pattern.

## 2. Efficacy belongs to the whole service

The successful unit is not a naked model. It is a learning system.

In Sierra Leone, the tutor produced approximately 113,000 interactions:
91.4% were conceptual, 76% used scaffolding, and only 2% directly supplied a
solution. In Nigeria, teacher facilitation, curriculum-aligned prompts, peer
learning, and repeated after-school sessions surrounded the AI. In India,
implementation support increased weekly use from 7.2 to 47.4 minutes.

These deployments converge on six requirements:

1. **Ground the mentor** in the local curriculum and trusted sources.
2. **Diagnose before teaching** so the next step fits the learner.
3. **Sequence action** through explanation, guided practice, retrieval, and
   transfer.
4. **Provide a meaningful dose** through scheduled, reliable access.
5. **Amplify teachers and facilitators** with timely evidence and interventions.
6. **Test independently** after the AI steps back.

The resulting loop is:

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

## 3. The equity opportunity is measurable

The performance-gap experiment reduced a measured education gap by roughly
three quarters. That is an existence proof: cheap, on-demand expertise can
reach people who were previously denied it.

The Sierra Leone trial also found that stronger starting mathematics predicted
larger gains. That finding should become an engineering target. The mentor must
add better prerequisite diagnosis, language support, confidence-building,
facilitator cues, and accessible representations until the largest gains reach
learners who begin furthest behind.

Every deployment should therefore report outcomes by:

- starting mastery;
- language and literacy level;
- disability and access mode;
- gender and age;
- device and connectivity tier;
- school and community context.

The goal is not identical interaction. It is equivalent opportunity to reach
mastery.

## 4. Augmentation is a teaching policy

In the July 2026 knowledge experiment, learners gained on an immediate unaided
test and retained the gain one week later. Delayed results were stronger when
learners used AI to explain and explore than when they mainly used it to
automate production.

This does not mean the mentor must withhold demonstrations or finished
examples. It means every productive shortcut should become a learning object:

- inspect the generated example;
- explain why each decision works;
- find an assumption or error;
- compare an alternative;
- retrieve the idea later;
- apply it in a new case.

The product objective is not “never answer.” It is **increase what this learner
can do next without help**.

## 5. One teaching ritual cannot serve everyone

The mentor needs a policy router that can:

- explain directly in the learner’s strongest language;
- demonstrate a complete worked example;
- diagnose a missing prerequisite;
- ask one targeted question;
- co-solve a step;
- let the learner complete the next step;
- verify an answer, diagram, program, or experiment;
- invite the learner to teach the concept;
- stage contrasting peer solutions;
- schedule retrieval;
- escalate to a teacher or specialist.

The choice depends on the learner’s goal, time, current understanding, error,
language, affect, and response to previous help. A novice may need a clear
example before productive inquiry. An experienced learner may need only a
counterexample. A child on a shared phone may need a short spoken exchange now
and a local practice bundle later.

## 6. Tutor quality is becoming testable

July 2026 component research turns pedagogy into an engineering discipline:

- [FATE](https://arxiv.org/abs/2607.10647) evaluates mistake identification,
  mistake location, guidance, and actionability. `MEASURED-BENCH`
- [CSTutorBench](https://arxiv.org/abs/2607.05571) finds that model family and
  instruction tuning can matter more than parameter count for a tutoring role;
  an educational prompt improved 10 of 11 tested models. `MEASURED-BENCH`
- [EduPanel](https://arxiv.org/abs/2607.18529) uses learner-conditioned agents
  and inspectable evidence to evaluate educational videos. `MEASURED-BENCH`
- [DeepTutor](https://arxiv.org/abs/2604.26962) combines grounding,
  multi-resolution memory, learner profiles, calibrated questions, and
  proactive tutoring skills. `MEASURED-BENCH`

These benchmarks do not prove learning outcomes. They let a team test each
specialist before a classroom trial and identify why a tutor response failed.

## 7. The five-layer efficacy stack

| Layer | Evidence | Gate |
|---|---|---|
| Response | correctness, pedagogy, actionability, grounding, safety | each mentor role passes a published evaluation |
| Sequence | adaptation across a simulated learner trajectory | decisions and failure clusters are inspectable |
| Usability | real learners understand, trust, and continue productively | language and accessibility parity |
| Learning | delayed unaided retention and transfer | meaningful uplift against a strong comparison |
| Deployment | reach, uptime, human load, distributional gains, cost | the target community can sustain the service |

Synthetic learners and model judges accelerate development. Real learners
remain the outcome authority. A small July 2026 classroom evaluation of the
[Learning Engagement Assistant](https://arxiv.org/abs/2607.13370) found strong
usability and trust but shallow use, while simulations did not predict every
behavior. `OBSERVED`, n=8

## 8. A public promise needs public acceptance tests

A universal mentor is ready to scale when it can demonstrate:

1. higher delayed unaided performance and transfer;
2. the largest gains for learners starting furthest behind;
3. local-language learning near the best-supported language;
4. equivalent goals through speech, text, visual, motor, and cognitive access
   paths;
5. more timely expert-quality help per teacher hour;
6. useful continuity under weak or absent connectivity;
7. traceable curriculum, factual, mathematical, and scientific grounding;
8. inspectable, correctable, portable learner state;
9. a sustainable cost per successful learning hour;
10. safe, contextual transfer to teachers, families, and specialists;
11. growing learner agency, curiosity, and choice.

## 9. Build the infrastructure in widening circles

The evidence supports an incremental deployment:

1. **One grounded curriculum slice:** diagnosis, several teaching modes, and
   delayed transfer measurement.
2. **Teacher cockpit:** clear learner needs, editable mentor hypotheses,
   small-group actions, and time-leverage measures.
3. **Multilingual multimodality:** speech, camera, diagrams, accessible
   alternatives, and subject-grounded translation.
4. **Local school or community node:** routine inference and learner state
   offline; delay-tolerant synchronization; frontier escalation when needed.
5. **Longitudinal replication:** multiple subjects, languages, ages, countries,
   and device tiers with public results and costs.

Peru’s [Eligiendo Mi Camino](https://www.worldbank.org/en/country/peru/brief/eligiendo-mi-camino)
shows this infrastructure pattern at public-system scale: diagnostic placement,
thousands of curriculum items, trained teachers, school-time use, home
continuity, and evaluation designed into rollout. `OBSERVED`

## Conclusion

The July 2026 frontier supports decisive optimism. AI-supported learning gains
are no longer isolated. The components needed for multilingual, multimodal,
adaptive mentorship are becoming cheaper and testable. Schools and public
systems are learning how to deploy them.

The mandate is to build:

- for the learner furthest from existing expertise;
- for the language they think in;
- for the device and network they have;
- with teachers and families made more capable;
- with independent learning as the outcome;
- with the cost curve of universal infrastructure.

The next great education program can be a standing entitlement to expert
attention: every learner, every day, wherever they are.

---

**Research basis:** [B2 raw research and source index](../research/raw/B2-efficacy-frontier-2026.md)  
**Related:** [The frontier has crossed](01-central-finding.md) ·
[The expert mentor mesh](03-expert-mentor-mesh.md) ·
[Content roadmap](../CONTENT_ROADMAP.md)
