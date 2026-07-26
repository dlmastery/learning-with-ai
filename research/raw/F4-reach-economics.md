---
title: "Universal Reach — the economics and delivery architecture of an expert AI mentor for every learner"
wave: F
date_researched: 2026-07-25
sources_count: 21
status: supersedes the earlier F4 report
---

# Universal Reach

## Executive finding

The July 2026 question is no longer whether an AI tutor can produce meaningful
learning. Multiple randomized deployments now show that it can. The question is
whether that capability can be delivered to every learner, including a child
sharing a low-cost phone, speaking a locally underserved language, with weak
connectivity and no nearby subject specialist.

The answer is increasingly **yes, if the delivery system is designed for the
margin first**.

Three frontiers have crossed at once:

1. **Learning efficacy.** Guided AI tutoring has produced +0.258 SD in Sierra
   Leone and +0.31 SD in Nigeria; a July 2026 undergraduate trial found +0.27 SD
   on an immediate unaided test with gains persisting a week. `MEASURED-RCT`
2. **Inference economics.** Useful model inference is now measured in cents per
   hour, with open and on-device models able to handle routing, speech,
   translation, retrieval, and routine tutoring locally. `MEASURED-BENCH`
3. **Language and modality.** Current systems span text, speech, vision,
   handwriting, diagrams, and hundreds to thousands of languages. Small systems
   now run on ordinary phones and laptops. `MEASURED-BENCH`

This changes the governing thesis:

> Expert mentorship is becoming a public-utility deployment problem, not a
> scarce-intelligence problem.

The remaining work is substantial—devices, electricity, curriculum grounding,
teacher integration, child safety, and rigorous local evaluation—but each is an
implementable workstream. None is a reason to ration high-quality mentorship to
children already lucky enough to live near it.

---

## 1. Evidence that the model can reach the margin

### 1.1 Sierra Leone: guided AI tutoring in ordinary schools

Google DeepMind and partners ran a pre-registered randomized trial with **1,763
students across 12 schools**. Eight weeks of Gemini Guided Learning produced a
**+0.258 SD mathematics gain**. The system handled 113,000 interactions; reported
coding found **91.4% conceptual exchanges**, scaffolding in **76%** of tutor
responses, and direct solutions in only **2%**. `MEASURED-RCT`

This is not a story about elite students with perfect devices. It is evidence
from one of the world's most resource-constrained school systems that a carefully
designed conversational tutor can create material gains now.

Primary sources:

- [DeepMind: Measuring the impact of learning with AI in Sierra Leone](https://deepmind.google/blog/measuring-the-impact-of-learning-with-ai-in-sierra-leone-and-beyond/)
- [Pre-registered technical report](https://storage.googleapis.com/deepmind-media/LearnLM/learnLM_sierraleone_may26.pdf)

### 1.2 Nigeria: teacher-supported tutoring at scale

A World Bank randomized evaluation of an after-school program with roughly
**800 students** found that six weeks of teacher-supported generative-AI tutoring
improved outcomes by **0.31 SD**. Gains appeared in English, AI/digital skills,
and regular curricular examinations. `MEASURED-RCT`

The deployment pattern matters as much as the number: a teacher orchestrated the
room while each learner received individualized assistance. The scalable unit is
not “replace the teacher”; it is **give every teacher a room full of
one-to-one-capable mentors**.

Source: [World Bank working paper on generative AI tutoring in Nigeria](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324)

### 1.3 India and Peru: implementation is becoming a repeatable discipline

In Indian residential government schools, implementation support increased Khan
Academy use from **7.2 to 47.4 minutes per week** and generated an effect close to
**0.5 SD in mathematics**. `MEASURED-RCT`

Source: [NBER: Making AI Work in Schools](https://www.nber.org/papers/w34683)

In July 2026, the World Bank reported a Peru program delivering an AI mathematics
tutor and career coach to **4,500 students in 85 public schools**, alongside a
separate randomized teacher-training program spanning **390 schools**.
`OBSERVED`

Source: [World Bank: Artificial Intelligence in Action in Latin America’s Schools](https://www.worldbank.org/en/results/2026/07/02/artificial-intelligence-in-action-in-latin-america-s-schools-evidence-from-peru)

These projects move the discussion from speculative product demos to a practical
deployment science: teacher preparation, timetabling, device logistics,
curriculum alignment, usage quality, and feedback loops.

### 1.4 AI can expand educational opportunity

A randomized study of **1,174 people** reported an initial education performance
gap of **0.548 SD** that fell to **0.139 SD** with AI access—roughly three quarters
of the measured gap closed during the task. A later unaided assessment found no
overall harm, and lower-education participants retained some benefit.
`MEASURED-RCT`

Source: [NBER: Can AI Close the Skills Gap?](https://www.nber.org/papers/w34851)

A separate July 2026 randomized undergraduate study found **+0.27 SD** on an
immediate unaided knowledge test, with gains persisting one week later.
Participants who used AI to augment their thinking performed better than those
who delegated the task. `MEASURED-RCT`

Source: [Randomized study of generative AI and knowledge acquisition](https://arxiv.org/abs/2607.08849)

The correct research program is therefore not “prove that access is dangerous.”
It is **identify the interaction patterns, local supports, and product features
that make these gains reproducible for every learner**.

---

## 2. The cost curve has crossed the feasibility threshold

### 2.1 July 2026 reference prices

Representative public API prices per million tokens:

| System | Input | Output | Important capability |
|---|---:|---:|---|
| DeepSeek V4 Flash | $0.14 uncached; $0.0028 cached | $0.28 | 1M-token context |
| Gemini 3.5 Flash-Lite | $0.30 | $2.50 | low-cost multimodal reasoning |
| GPT-5.6 Luna | $1.00 | $6.00 | frontier-family routing tier |
| GPT-5.6 Terra | $2.50 | $15.00 | stronger specialist tier |
| GPT-5.6 Sol | $5.00 | $30.00 | hardest-case frontier tier |

Sources:

- [DeepSeek V4 pricing](https://api-docs.deepseek.com/quick_start/pricing/)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [OpenAI GPT-5.6](https://openai.com/index/gpt-5-6/)

An equitable tutor should not send every turn to the most expensive model. It
should route:

- pronunciation, turn-taking, review, and local retrieval to an on-device model;
- normal explanation and practice to a low-cost cloud model;
- ambiguous, safety-sensitive, or unusually difficult questions to a frontier
  specialist;
- verified calculations to tools rather than to any language model.

This is the same operational shape as a strong school: most work is handled near
the learner; specialists are called when their expertise is actually needed.

### 2.2 A transparent one-hour session calculation

Consider a deliberately generous text session:

- 120 conversational turns;
- 30,260 uncached input tokens;
- 1,895,110 cached context reads;
- 9,360 output tokens.

At the published DeepSeek V4 Flash prices:

```
uncached input = 0.030260M × $0.14   = $0.00424
cached input   = 1.895110M × $0.0028 = $0.00531
output         = 0.009360M × $0.28   = $0.00262
                                                  --------
illustrative model cost per hour                  $0.01217
```

This is an engineering model, not a vendor quote. Real usage varies with turn
length, caching behavior, retries, moderation, and regional hosting. Its purpose
is to establish order of magnitude: **routine personalized dialogue can cost
around one cent per learner-hour at a low-cost tier**.

At 180 hours per learner-year:

- text reasoning with local speech: about **$2.19 per learner-year**;
- adding cloud speech recognition at $0.04/hour: about **$9.39 per
  learner-year**.

For a stress-test scenario of 1.9 billion learners, those figures imply roughly
**$4.2B/year** for text inference with local speech or **$17.8B/year** with the
illustrative cloud speech cost. They are not a budget proposal. They show that
inference is no longer the impossible line item; devices, delivery, support, and
public infrastructure are likely to dominate.

### 2.3 On-device intelligence changes the denominator

The cost floor approaches zero when common functions run locally:

- **Gemma 4 E2B/E4B** targets phones and laptops, accepts image and audio, covers
  more than 140 pretraining languages, and supports long context.
- **Sarvam Edge** is a sub-1GB on-device stack designed for all 22 scheduled
  Indian languages.
- **Qwen3.6-35B-A3B** activates about 3B parameters while retaining multimodal
  capability, enabling stronger local or school-server deployments.
- **Mistral Voxtral** provides open speech recognition options for edge and
  private deployments.

Sources:

- [Gemma documentation](https://ai.google.dev/gemma/docs)
- [Gemma 4 developer guide](https://developers.googleblog.com/gemma-4-12b-the-developer-guide/)
- [Sarvam Edge](https://www.sarvam.ai/products/edge)
- [Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b)
- [Mistral Voxtral](https://mistral.ai/news/voxtral/)

The universal system should therefore be **offline-capable by default**, not a
cloud application with an offline afterthought.

---

## 3. Language is shifting from exclusion to routing

A world tutor that requires polished English is not universal.

The July 2026 stack is materially better:

- Meta’s open Omnilingual ASR reports coverage of **1,600+ languages**, including
  500 newly supported low-resource languages. `MEASURED-BENCH`
- Gemini 3.5 Live Translate covers **70+ languages and 2,000+ language pairs**.
  `VENDOR`
- Sarvam Saaras v3 handles English plus all **22 scheduled Indian languages** and
  code-mixed speech. `VENDOR`
- Mistral OCR 4 reports document understanding in **170 languages**, including
  layout, bounding boxes, and confidence. `VENDOR`
- Qwen Image 3 targets dense educational layouts and legible small text across
  multiple writing systems. `VENDOR`

Sources:

- [Meta Omnilingual ASR](https://ai.meta.com/blog/omnilingual-asr-advancing-automatic-speech-recognition/)
- [Gemini 3.5 Live Translate](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/)
- [Sarvam speech-to-text](https://www.sarvam.ai/speech-to-text)
- [Mistral OCR 4](https://mistral.ai/news/ocr-4/)
- [Qwen Image 3](https://qwen.ai/blog?id=qwen-image-3.0)

No single model will cover every dialect, accent, script, and classroom register.
The practical architecture is an **ensemble language layer**:

1. detect language, dialect, and code-switching locally;
2. preserve the learner’s original speech and writing;
3. route to the best available ASR/translation model;
4. ground explanations in locally reviewed terminology and curriculum;
5. speak back in the learner’s strongest language;
6. expose confidence and invite correction;
7. feed corrections into a community-governed language pack.

This turns language coverage into a continuously improving infrastructure
project rather than a one-vendor dependency.

---

## 4. The universal mentor mesh

The scalable product is not one enormous chatbot. It is a layered mesh.

### Tier 0 — on the learner’s device

- wake word and turn detection;
- speech recognition and text-to-speech;
- local-language translation;
- cached curriculum and examples;
- retrieval practice and routine feedback;
- privacy-preserving learner state;
- sync queue for intermittent connectivity.

### Tier 1 — school or community node

- stronger open model on a shared laptop, mini-PC, or local server;
- local curriculum and textbook index;
- shared content cache;
- teacher dashboard;
- peer-group and timetable coordination;
- updates delivered opportunistically by network or physical media.

### Tier 2 — regional cloud

- frontier reasoning for hard cases;
- specialist agents for mathematics, science, languages, vocational skills, and
  accessibility;
- dynamic visual and interactive artifact generation;
- safety review and human escalation;
- evaluation, monitoring, and model updates.

### Human layer

- teachers choose goals, orchestrate groups, and interpret context;
- parents and guardians receive understandable progress summaries;
- local experts validate language and cultural fit;
- governments and civil society set curriculum, privacy, and child-safety rules.

The AI supplies abundant individual attention. People supply community,
legitimacy, care, and local judgment. These are complementary assets.

---

## 5. Design for weak infrastructure first

The International Telecommunication Union estimated that nearly three quarters
of humanity were online in 2025, leaving about **2.2 billion people offline**,
while mobile-network coverage was close to universal. `OBSERVED`

Source: [ITU Facts and Figures 2025](https://www.itu.int/itu-d/reports/statistics/facts-figures-2025/)

That gap determines the product specification:

- **store-and-forward:** a lesson remains fully usable without a live connection;
- **audio-first:** speech can be more accessible than dense screens and large
  downloads;
- **shared-device mode:** separate learner profiles on one family or classroom
  device;
- **tiny updates:** content and model deltas rather than complete downloads;
- **solar-compatible hardware:** low power, replaceable batteries, local repair;
- **paper bridge:** photograph a worksheet, generate or print the next activity,
  and continue offline;
- **teacher broadcast:** one connected teacher device can seed a whole classroom;
- **graceful model routing:** never make learning stop because the premium model
  is unavailable.

UNESCO’s current Ethiopia work, described as reaching **200,000 learners across
200 towns**, is an example of offline digital delivery being treated as core
infrastructure rather than a fallback. `OBSERVED`

Source: [UNESCO: Building resilient education systems](https://www.unesco.org/sdg4education2030/en/articles/building-resilient-education-systems-global-lessons-good-practices)

---

## 6. What July 2026 makes newly buildable

The components now exist for a mentor that:

- talks naturally and can be interrupted;
- reads a learner’s notebook, textbook page, diagram, or screen;
- creates a tailored explanation, simulation, worked example, or quiz;
- diagnoses prerequisite gaps and maintains a persistent learner model;
- changes language and explanation depth without changing the underlying truth;
- schedules retrieval and transfer practice over months;
- routes difficult questions to stronger specialists;
- works locally when disconnected and synchronizes later;
- gives the teacher a live view of who needs help and why.

Relevant current products include GPT-Live, ChatGPT Study Mode with dynamic
visual explanations, Gemini Study Notebooks, Claude Opus 5 interactive
artifacts, and the open model stacks above. Their significance is not that any
one product is the final tutor. It is that the formerly separate primitives are
now available for integration.

Sources:

- [OpenAI GPT-Live](https://openai.com/index/introducing-gpt-live/)
- [ChatGPT Study Mode](https://help.openai.com/en/articles/11780217-study-mode)
- [OpenAI dynamic visual explanations](https://openai.com/index/new-ways-to-learn-math-and-science-in-chatgpt/)
- [Gemini Study Notebooks](https://blog.google/innovation-and-ai/products/gemini-app/gemini-study-notebooks/)
- [Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)

---

## 7. Deployment acceptance tests

Optimism becomes credible when it is testable. A universal-mentor deployment
should publish:

1. **Learning:** pre-registered gains on unaided, curriculum-relevant
   assessments.
2. **Equity:** effects by baseline knowledge, language, disability, gender,
   device access, and geography.
3. **Reach:** active learners, completed sessions, offline completion, and cost
   per successful learning hour.
4. **Instructional quality:** conceptual guidance, worked examples, feedback,
   practice, transfer, and escalation rates.
5. **Reliability:** ASR/OCR accuracy by local language and classroom condition.
6. **Teacher leverage:** students served well per teacher hour and teacher
   workload saved.
7. **Continuity:** retained learning and progress across terms, not just one
   session.
8. **Safety:** child-protection incidents, response quality, privacy, and time to
   human escalation.

These are not arguments against deployment. They are the instrumentation needed
to improve it quickly and distribute what works.

---

## Conclusion

In 2026, scarcity of expert attention is no longer an immutable fact of
education. The intelligence, voice, vision, translation, personalization, and
content-generation components have crossed the threshold from research promise
to deployable system.

The strongest north star is therefore literal:

> Every child—whether in a capital city, a rural village, a refugee settlement,
> an island community, or a remote mountain school—should be able to call on an
> expert AI mentor in their own language, at their own pace, whenever they need
> help.

The field should now optimize for reach, learning gain, dignity, local language,
teacher leverage, and cost per successful learning hour. The task is not to
defend scarcity. It is to engineer abundance.
