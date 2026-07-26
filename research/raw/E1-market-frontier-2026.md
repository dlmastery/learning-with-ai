---
title: "The July 2026 learning-AI market as a capability stack"
wave: E
section: E1
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 36
---

# E1 — The 2026 Market Frontier

## Executive finding

The July 2026 learning-AI market is no longer a collection of speculative
chatbots. Important parts of a world-class personal mentor are already shipping:

- Socratic and guided-learning modes in globally distributed frontier assistants;
- course-grounded study notebooks that diagnose gaps and update lessons;
- teacher workspaces that create, differentiate, assess, and assign;
- speech-first reading and language tutors;
- curriculum-grounded, multimodal student tutors;
- human-plus-AI tutoring operations;
- no-cost standardized-test practice;
- open, self-hostable tutoring frameworks;
- measured deployments in public schools in Sierra Leone and Nigeria.

No single product yet composes all of these into a multilingual, full-duplex,
grounded, learner-owned, disability-first, offline-capable mentor with a human
support network and verified delayed transfer. `INFERENCE`

That is not a reason to wait. It identifies the engineering opportunity:

> **The universal mentor is now principally a composition, verification, access,
> and deployment problem—not a bet that language models might someday become
> capable enough to teach.**

## Evidence labels

| Label | Meaning |
|---|---|
| `MEASURED-RCT` | Randomized field comparison with learner outcomes |
| `MEASURED-BENCH` | Disclosed benchmark or structured evaluation |
| `OBSERVED` | Public product, policy, standard, or open implementation |
| `VENDOR` | Provider-reported capability, use, price, or traction |
| `RESEARCH` | Current research system, not assumed production-ready |
| `INFERENCE` | Architecture or market conclusion derived from evidence |

## 1. Method: map learning primitives, not logos

This sweep was conducted against a 25 July 2026 cutoff. It prioritizes official
product documentation, primary research, open implementations, and measured
field evidence. A company appears only when it demonstrates a distinct learning
primitive or meaningful distribution path.

The unit of analysis is a capability:

1. general learning conversation;
2. curriculum grounding and teacher amplification;
3. adaptive tutoring and practice;
4. assessment and feedback;
5. language, speech, and early literacy;
6. learner memory and planning;
7. multimodal artifacts and generated environments;
8. human coordination;
9. offline and low-cost distribution;
10. portable evidence and credentials;
11. open orchestration infrastructure.

Funding, customer counts, and adoption are included only when they illuminate
deployment capacity, and are labelled `VENDOR`.

## 2. General learning conversation is becoming a commodity

Three frontier assistants now expose explicit learning behavior:

- [ChatGPT Study Mode](https://help.openai.com/en/articles/11780217-study-mode)
  asks questions, explains in layers, checks understanding, works with uploaded
  materials, supports voice, and can use Memory for personalization. It is
  globally available across ChatGPT plans and models. `OBSERVED`
- [Gemini Guided Learning](https://blog.google/products-and-platforms/products/education/guided-learning/)
  uses LearnLM-derived behaviors to ask probing questions, break problems into
  steps, adapt explanations, and support rich responses. `VENDOR`
- [Claude for Education](https://www.anthropic.com/news/introducing-claude-for-education)
  provides a Learning mode that guides reasoning, uses Socratic questions,
  emphasizes core concepts, and supplies structured templates. `VENDOR`

In June 2026 Google moved beyond a chat mode. Gemini
[study notebooks](https://blog.google/products-and-platforms/products/education/iste-students-2026/)
begin with a diagnostic, create bite-sized lessons, track quiz progress, and
update the plan as results or source materials change. They also synchronize
with NotebookLM. `VENDOR`

The market implication is decisive:

- answer generation is not a durable education product moat;
- basic guided dialogue is rapidly becoming a standard model surface;
- the valuable layer is the closed loop around dialogue: trusted knowledge,
  learner state, teaching-policy selection, real practice, humans, and outcomes.
  `INFERENCE`

## 3. Teacher amplification is already a major production surface

### 3.1 Frontier-model workspaces

[ChatGPT for Teachers](https://openai.com/index/chatgpt-for-teachers/) gives
verified U.S. K–12 educators a protected workspace for adapting materials,
planning, and collaboration; OpenAI says it is free through June 2027.
`VENDOR`

[Claude for Teachers](https://www.anthropic.com/news/claude-for-teachers),
launched 14 July 2026, combines premium Claude capabilities, teaching skills,
state-standards mappings, curriculum connectors, differentiation, and classroom
material creation. It also exposes third-party education skills including Eedi,
MagicSchool, Snorkl, TeachFX, Diffit, and Coteach. `VENDOR`

[Gemini in Classroom](https://blog.google/products-and-platforms/products/education/classroom-ai-features/)
provides no-cost educator tools and teacher-authored Gems and NotebookLM
experiences grounded in selected class resources. Google’s June 2026 release
adds a connected Classroom context, teacher-assigned study notebooks, and
student understanding summaries. `VENDOR`

### 3.2 School-native workflow layers

- [MagicSchool](https://www.magicschool.ai/faq) reports 80+ teacher tools,
  50+ student tools, 24 interface languages, translation into 98 languages,
  assessment and feedback modules, student rooms, and LMS integration.
  `VENDOR`
- [Brisk](https://help.briskteaching.com/hc/en-us/articles/38789659161364-What-is-Brisk-Teaching)
  combines an in-context browser extension, teacher planning hub, and
  teacher-controlled student workspace; its current product can transform
  trusted curriculum into differentiated activities. `VENDOR`
- [Flint](https://flintk12.com/teachers) lets educators create spoken, written,
  visual, simulated, and assessment activities and review learning analytics.
  It reports support for historical simulations, science labs, diagram
  annotation, code collaboration, leveled reading, and language practice.
  `VENDOR`

The primitive being commoditized is not merely “generate a worksheet.” It is:

```text
trusted class context
  → editable lesson and differentiation
  → assigned learner experience
  → formative evidence
  → teacher decision
```

The universal mentor should treat the teacher workspace as one view of the same
learner and knowledge system, not as a separate content factory. `INFERENCE`

## 4. Tutoring is splitting into four useful architectures

### 4.1 General assistants with a teaching policy

ChatGPT Study Mode, Gemini Guided Learning, and Claude Learning mode can tutor
across domains, languages, files, and learner questions. Their breadth and
distribution make them the fastest path to abundant explanation. Their current
public surfaces do not provide a portable learner-owned mastery graph or a
complete school/community human-support workflow. `OBSERVED`

### 4.2 Curriculum-grounded tutors

[Khanmigo](https://blog.khanacademy.org/learning-in-the-open-what-ai-is-and-isnt-changing/)
is connected to Khan Academy content and mastery state. Its 2026 redesign changes
support based on whether a learner is encountering or reviewing a skill and can
offer prerequisite review. Khan Academy reports that product tests from October
2025 to April 2026 produced a six-percentage-point improvement in its
  next-item-learning metric. `VENDOR`

[Flint’s tutor](https://flintk12.com/tools/ai-tutor) grounds help in teacher
syllabi, notes, and materials and supports voice, diagrams, a whiteboard,
graphing, document uploads, and feedback on prior work. `VENDOR`

[Squirrel AI](https://squirrelai.com/) combines adaptive diagnosis, a Large
Adaptive Model, multimodal agents, learning tablets, and physical learning
centers. Its current public claims are useful evidence of product direction and
distribution in China, but are not treated here as independent outcome findings.
`VENDOR`

### 4.3 Human-plus-AI continuity

[LessonOrca](../../survey/21-lessonorca-evidence-loop.md) connects tutor context,
AI-created plans and notes, between-session Socratic support, parent visibility,
and center guidelines. On 19 April 2026 it reported use by 25 tutors and 100
students across three Bay Area centers. `VENDOR`

[Tutor CoPilot](https://arxiv.org/abs/2410.03017) offered AI-generated expert
guidance to live K–12 tutors. Its preregistered trial found a four-percentage-
point increase in topic mastery overall and a nine-point increase for students
of lower-rated tutors. `MEASURED-RCT`

The [LearnLM/Eedi study](https://arxiv.org/abs/2512.23633) had expert tutors
review AI-drafted messages. Tutors approved 76.4% with zero or minimal edits;
AI-supported learners were 5.5 percentage points more likely to solve novel
subsequent problems than learners receiving the comparison human-tutor
experience. `MEASURED-RCT`

### 4.4 Agentic and open tutors

[DeepTutor](https://arxiv.org/abs/2604.26962) is a 2026 open research framework
with static grounding, multi-resolution learner memory, citation-grounded
problem solving, calibrated question generation, collaborative writing,
multi-agent research, proactive skills, and multichannel access. `RESEARCH`

[Open TutorAI](https://opentutorai.com/) is self-hostable and combines
learner-configured tutoring supports, source grounding, classrooms, analytics,
and avatar-based voice/video interaction for learners, educators, and parents.
`RESEARCH`

These architectures are converging. The reference product should combine the
general assistant’s breadth, the curriculum tutor’s grounding, the human-AI
system’s accountability, and the open agent framework’s composability.
`INFERENCE`

## 5. Assessment is moving inside the teaching loop

In the 2026 market, assessment increasingly produces the next lesson:

- Gemini study notebooks diagnose focus areas, generate a plan, and update it
  from subsequent quizzes. `VENDOR`
- Gemini now offers or has announced no-cost full-length SAT, JEE Main, NEET,
  ACT, GRE, and Brazil ENEM practice through content partnerships, with
  topic-level performance breakdowns. `VENDOR`
- MagicSchool’s quizzes and class-writing feedback provide real-time summaries
  and teacher-facing evidence. `VENDOR`
- Khanmigo tests next-item correctness after a tutor interaction and uses
  mastery and prerequisite information to change support. `VENDOR`
- [AI-ALOE Apprentice Tutors](https://aialoe.org/wp-content/uploads/2026/03/AI-ALOE-Newsletter-Spring-26.pdf)
  reached 1,000+ adult learners in 256 sections in 2025; its A/B study found
  on-demand scaffolding increased adoption by 50% relative to full scaffolding
  and learners solved more problems more efficiently. `OBSERVED`

The missing market-wide primitive is portable proof:

```text
claim about a capability
  → evidence from a new task
  → delayed retest
  → changed context
  → independent performance
  → learner-owned, selectively shared record
```

[Open Badges 3.0 and Comprehensive Learner Records](https://www.1edtech.org/sites/default/files/media/docs/2025/Wellspring_Phase_I_Report.pdf)
provide standards-based credential containers, but current AI tutors do not
generally emit verified, interoperable transfer evidence into a learner-owned
record. `OBSERVED`

## 6. Speech and literacy show why vertical systems still matter

General multimodal models can hear and speak, but child speech, phoneme-level
feedback, reading progression, and rapid conversational timing remain valuable
specializations.

- [Ello](https://www.ello.com/about) describes a custom low-latency stack from
  child-specific speech perception through a hierarchical teaching agent and
  expressive speech generation. Its reading product listens while children read
  real books and supplies targeted support. `VENDOR`
- [Amira](https://amiralearning.com/) listens to oral reading, assesses
  proficiency, and provides Science-of-Reading-aligned tutoring in English and
  Spanish. `VENDOR`
- [Google Read Along](https://support.google.com/readalong/answer/12279465)
  uses text-to-speech and speech recognition to listen and respond during oral
  reading. `VENDOR`
- [Duolingo Video Call](https://blog.duolingo.com/video-call/) provides
  spontaneous, level-adjusted conversation practice. Duolingo reports support
  across nine major courses by 2026 and identifies Video Call, Explain My
  Answer, and Roleplay as its AI subscription layer. `VENDOR`
- Flint offers spoken language practice with feedback across the school tutor
  surface. `VENDOR`

The universal mentor should not replace these domain stacks with generic chat.
It should route to specialist perception, curriculum, and feedback modules
behind one continuous learner relationship. `INFERENCE`

## 7. Multimodal learning has moved from media retrieval to generation

Current products can already create or coordinate:

- source-grounded audio and video overviews, quizzes, flashcards, infographics,
  and study guides in NotebookLM; `VENDOR`
- short generated explanatory animation through Google’s Sparkify experiment;
  `DEMO`
- whiteboard, graphing, diagram annotation, historical simulation, language
  conversation, coding, and guided science-lab activities in Flint; `VENDOR`
- podcasts and custom student tools in MagicSchool; `VENDOR`
- avatar-led voice and video tutoring in Open TutorAI; `RESEARCH`
- pedagogical, execution, safeguard, and tutoring agents that assemble K–12 XR
  scenes in a [2026 multi-agent XR prototype](https://arxiv.org/abs/2604.04728).
  `RESEARCH`

Generation alone is increasingly available. The scarce capability is a verified
learning object whose behavior, sources, visual truth, accessibility, and
assessment are compiled from the same concept specification. `INFERENCE`

## 8. The strongest global signal is measured learning, not a market forecast

### 8.1 Sierra Leone

Google and Fab AI ran an eight-week preregistered RCT in 48 classrooms with
nearly 1,800 Grade 7–8 learners. Google reports that Guided Learning increased
externally validated math-assessment scores by 0.26 standard deviations, which
it equates to roughly 1.2–1.7 years of typical progress in low- and
middle-income countries. `MEASURED-RCT`

The [official release](https://blog.google/products-and-platforms/products/education/measuring-the-impact-of-ai-on-teaching-and-learning/)
also describes mobile-first educator training in Maharashtra, Chhattisgarh,
Assam, Ladakh, and Punjab, plus institutional deployments in Ghana and South
Africa. `VENDOR`

### 8.2 Nigeria

A six-week, teacher-guided after-school program in Edo State used Microsoft
Copilot/GPT-4 for English learning. The
[World Bank evaluation](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324)
found an effect of approximately 0.31 standard deviations, with transfer into
regular curriculum subjects; the World Bank compares it with 1.5–2 years of
typical progress in similar settings. `MEASURED-RCT`

These are not demonstrations from wealthy one-device-per-child laboratories.
They are evidence that teacher-guided frontier tutoring can produce substantial
gains in African public-school contexts. `INFERENCE`

## 9. Offline distribution exists; offline frontier intelligence is the gap

[Kolibri](https://learningequality.org/kolibri/about-kolibri/) is an open,
offline-first learning platform designed for low-cost and legacy devices. It
proves that curriculum distribution, progress tracking, and local network
delivery can operate without continuous internet. `OBSERVED`

But the current market still largely separates:

- **offline learning infrastructure**, which is robust but usually static; and
- **frontier AI tutoring**, which usually assumes cloud connectivity.

The build target is a three-tier system:

1. on-device voice, retrieval, learner state, and compact teaching policies;
2. school or community hub for stronger local inference, content, and sync;
3. intermittent regional/cloud specialists for hard problems and model updates.

This composition is more promising than waiting for universal broadband. It
also supports local custody of child data and shared-device use. `INFERENCE`

## 10. Market capability matrix

| Primitive | July 2026 state | Representative evidence | Universal-mentor requirement |
|---|---|---|---|
| General learning dialogue | Broadly shipped | ChatGPT Study, Gemini Guided Learning, Claude Learning | Keep model-pluggable |
| Grounded study plan | Shipping | Gemini study notebooks, Khanmigo mastery context | Compile from verified sources and goals |
| Teacher amplification | Broadly shipped | Claude/OpenAI/Google, MagicSchool, Brisk, Flint | One shared learner/knowledge system |
| Adaptive tutoring | Shipping, unevenly integrated | Khanmigo, Flint, Squirrel, DeepTutor | Teaching router with explicit modes |
| Human-AI tutoring | Measured and early-production | Tutor CoPilot, Eedi, LessonOrca | Local escalation and continuity by default |
| Assessment/feedback | Broadly shipping | Google practice tests, MagicSchool, AI-ALOE | Delayed independent transfer as north star |
| Language conversation | Mature vertical | Duolingo, Flint | Low-latency multilingual full duplex |
| Early literacy | Mature specialist perception | Ello, Amira, Read Along | Child-speech and disability-aware routing |
| Generated media | Broadly shipping | NotebookLM, Sparkify, MagicSchool | Verifiable, executable concept objects |
| Interactive worlds | Emerging | Flint, Open TutorAI, multi-agent XR | Executable laws + observation bridge |
| Learner memory | Emerging and provider-bound | ChatGPT Memory, Gemini notebooks, DeepTutor | Portable, uncertain, learner-owned state |
| Offline delivery | Mature static layer | Kolibri | Local inference + opportunistic sync |
| Portable credentials | Standards exist | Open Badges 3.0, CLR | Evidence-native learner wallet |
| Open orchestration | Emerging | DeepTutor, Open TutorAI, Moodle Gemini | Interoperable tools, models, sources, policies |

## 11. What is already commoditized

By July 2026, a new system should usually buy, route, or reuse rather than invent:

- fluent multilingual explanation;
- document and image understanding;
- basic voice conversation;
- quiz, flashcard, rubric, and lesson generation;
- generic Socratic prompting;
- source-grounded chat;
- standard content adaptation and translation;
- initial teacher productivity workflows.

These remain important, but they are inputs to the mentor—not the product’s
defining invention. `INFERENCE`

## 12. What remains genuinely differentiating

The highest-leverage build work is now:

1. **Learner-owned longitudinal state** — a portable, inspectable model of what
   is known, uncertain, forgotten, preferred, and accessible.
2. **Pedagogical routing** — choosing direct instruction, worked examples,
   Socratic questioning, retrieval, simulation, collaboration, or human help
   from the learner’s state and goal.
3. **Verified executable knowledge** — explanations, diagrams, simulations,
   problems, and assessments compiled from one checked concept model.
4. **Full-duplex observation and action** — seeing handwriting, hearing
   uncertainty, following tool use, and coaching real-world activity.
5. **Human mesh** — family, peer, teacher, tutor, accessibility specialist, and
   subject expert connected through minimum-necessary context.
6. **Offline frontier delivery** — useful intelligence on the actual device,
   stronger intelligence on a community hub, and opportunistic cloud reach.
7. **Independent-transfer evidence** — proof that the learner can succeed later,
   without the tutor, in a changed context.
8. **Child-safe freedom** — broad access to knowledge while consequential
   actions, data power, and escalations remain appropriately governed.

## 13. Reference architecture consequence

The market should be composed as replaceable layers:

```text
ACCESS FOUNDATION
device + voice + accessibility + offline sync
        ↓
MODEL INTELLIGENCE
multilingual multimodal reasoning + tools
        ↓
VERIFIED KNOWLEDGE
authorized sources + executable concept contracts
        ↓
PEDAGOGY ROUTER
teach + hint + question + retrieve + simulate + collaborate
        ↓
LEARNER-OWNED STATE
uncertain mastery + memory + goals + access preferences
        ↓
HUMAN NETWORK
family + peer + teacher + tutor + specialist
        ↓
OUTCOME EVIDENCE
delayed independent transfer + learner-owned credentials
```

No vendor needs to control all seven layers. In fact, universal reach is more
likely when models, curriculum, delivery, human support, and evidence can be
substituted locally. `INFERENCE`

## 14. Final market judgment

The 2026 market already contains enough capability to deliver remarkably strong,
low-cost learning support:

- frontier assistants make patient expert dialogue abundant;
- school-native tools let one teacher differentiate for many learners;
- specialist speech systems listen to early readers and language learners;
- human-AI systems improve the consistency of real tutoring;
- open projects expose the beginnings of personalized agent orchestration;
- African public-school trials show large measured gains are possible now.

The missing product is the integration worthy of a child’s whole learning life.

The next category is not “another AI tutor.” It is a **learner-controlled mentor
mesh** that composes the best available models and specialists, works through
connectivity interruptions, includes trusted humans, and proves growing
independence over time.

That is a credible July 2026 build target.

## Sources

1. OpenAI, [Using Study Mode in ChatGPT](https://help.openai.com/en/articles/11780217-study-mode), current 2026.
2. OpenAI, [Introducing study mode](https://openai.com/index/chatgpt-study-mode/), 2025.
3. OpenAI, [A free version of ChatGPT built for teachers](https://openai.com/index/chatgpt-for-teachers/), 2025.
4. OpenAI, [Education for Countries](https://openai.com/index/edu-for-countries/), 2026.
5. OpenAI, [Why teens deserve access to safe AI](https://openai.com/index/why-teens-deserve-access-safe-ai/), 2026.
6. Google, [Guided Learning in Gemini](https://blog.google/products-and-platforms/products/education/guided-learning/), 2025.
7. Google, [Supporting students with connected AI tools](https://blog.google/products-and-platforms/products/education/iste-students-2026/), 2026.
8. Google, [Gemini in Classroom](https://blog.google/products-and-platforms/products/education/classroom-ai-features/), 2025.
9. Google, [From test prep to graduation](https://blog.google/products-and-platforms/products/education/ai-tools-programs-educators/), 2026.
10. Google, [Measuring the impact of AI on teaching and learning](https://blog.google/products-and-platforms/products/education/measuring-the-impact-of-ai-on-teaching-and-learning/), 2026.
11. Google, [Learn Your Way](https://blog.google/products-and-platforms/products/education/learn-your-way/), 2025.
12. Anthropic, [Introducing Claude for Education](https://www.anthropic.com/news/introducing-claude-for-education), 2025.
13. Anthropic, [Introducing Claude for Teachers](https://www.anthropic.com/news/claude-for-teachers), 2026.
14. Khan Academy, [Building a better AI tutor](https://blog.khanacademy.org/how-khan-academy-is-building-a-better-ai-tutor-our-most-recent-learnings/), 2026.
15. Khan Academy, [Learning in the Open](https://blog.khanacademy.org/learning-in-the-open-what-ai-is-and-isnt-changing/), 2026.
16. MagicSchool, [FAQ](https://www.magicschool.ai/faq), updated 2026.
17. MagicSchool, [2026 teaching tools](https://www.magicschool.ai/blog-posts/ai-teaching-tools-updates-2026), 2026.
18. Brisk, [What is Brisk Teaching?](https://help.briskteaching.com/hc/en-us/articles/38789659161364-What-is-Brisk-Teaching), updated 2026.
19. Flint, [AI tutor](https://flintk12.com/tools/ai-tutor), current 2026.
20. Flint, [Teachers](https://flintk12.com/teachers), current 2026.
21. Squirrel AI, [Large Adaptive Model and learning platform](https://squirrelai.com/), current 2026.
22. LessonOrca, [product and evidence program](../../survey/21-lessonorca-evidence-loop.md), 2026.
23. Wang et al., [Tutor CoPilot](https://arxiv.org/abs/2410.03017), field trial.
24. Google DeepMind/Eedi, [LearnLM tutoring trial](https://arxiv.org/abs/2512.23633), 2025.
25. Zhao et al., [DeepTutor](https://arxiv.org/abs/2604.26962), 2026.
26. El Hajji et al., [Open TutorAI](https://arxiv.org/abs/2602.07176), 2026.
27. AI-ALOE, [Spring 2026 deployment report](https://aialoe.org/wp-content/uploads/2026/03/AI-ALOE-Newsletter-Spring-26.pdf), 2026.
28. Duolingo, [Video Call](https://blog.duolingo.com/video-call/), current 2026.
29. Ello, [About the AI tutor](https://www.ello.com/about), current 2026.
30. Amira, [AI reading tutor](https://amiralearning.com/), current 2026.
31. Google, [Read Along](https://support.google.com/readalong/answer/12279465), current 2026.
32. Elmqaddem et al., [Multi-agent XR content creation](https://arxiv.org/abs/2604.04728), 2026.
33. World Bank, [From Chalkboards to Chatbots](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324), 2025.
34. Learning Equality, [About Kolibri](https://learningequality.org/kolibri/about-kolibri/), current 2026.
35. 1EdTech, [Wellspring Phase I / CLR horizon](https://www.1edtech.org/sites/default/files/media/docs/2025/Wellspring_Phase_I_Report.pdf), 2025.
36. Fischer, Rau, and Rilke, [AI Tutoring Enhances Student Learning Without Crowding Out Reading Effort](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5992341), 2026.
