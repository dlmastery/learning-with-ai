---
title: "Frontier capability, rolling quarter (April–July 2026): what became newly possible for learning"
wave: D
date_researched: 2026-07-25
sources_count: 48
---

# D1 — Frontier capability, rolling quarter (April–July 2026)

## 0. Method and evidence grading

WebSearch was unavailable for this pass. Everything below came from direct
fetches of vendor index pages, vendor model-card/docs pages, the arXiv search
UI, and — where vendors block automated fetching (OpenAI serves a Cloudflare JS
challenge to every non-browser client) — the Internet Archive snapshot of the
vendor's own page. Every OpenAI date below is read off the dateline of the
archived OpenAI page itself, not inferred.

**Grading used throughout:**

- `DEMO` — a curated video, prototype, or research preview. No general
  availability, no third-party replication.
- `VENDOR` — a claim made in a vendor blog post or model card. May include
  numbers, but the vendor chose the eval, ran it, and reported it.
- `MEASURED-BENCH` — a number on a named public benchmark with a published
  methodology, where an outside party could in principle reproduce it. Note
  that in this window essentially all frontier benchmark numbers are still
  *vendor-run* even when the benchmark is public; I flag those as
  `MEASURED-BENCH (vendor-run)`.
- `RCT` — a pre-registered randomised field trial with human subjects. This
  window contains exactly one at frontier scale.

**A methodological warning that materially affected this research.** OpenAI's
`sitemap.xml` reports `lastmod` of 2026-07-25 for hundreds of pages, including
pages that are over a year old. Naively trusting those timestamps would have
placed *ChatGPT Study Mode* and *ChatGPT for Teachers* inside this quarter.
Both are older (2025-07-29 and 2025-11-19 respectively, per their own
datelines). Anyone building a "what shipped this quarter" timeline from
sitemaps will get this wrong. I re-derived every OpenAI date from the page
dateline.

---

## 1. The dated capability timeline, April–July 2026

### April 2026

| Date | Item | Vendor | Grade | Learning-relevant content |
|---|---|---|---|---|
| Apr 8 | "Scaling How We Build and Test Our Most Advanced AI" | Meta | VENDOR | Infrastructure post. No learning content. |
| Apr 21 | ChatGPT Images 2.0 | OpenAI | VENDOR | Image generation. Diagram/illustration generation is the only plausible learning hook; no pedagogical claims. |
| Apr 23 | **GPT-5.5** (API availability Apr 24, incl. GPT-5.5 Pro) | OpenAI | VENDOR | Framed entirely as agentic coding, computer use, knowledge work, early scientific research. Explicitly claims per-token latency parity with GPT-5.4 while being larger. **Zero education framing.** |
| Apr 24 | **DeepSeek V4-Pro (1.6T total / 49B active) and V4-Flash (284B / 13B active)** | DeepSeek | VENDOR | **1M context is now the default across all official DeepSeek services.** Dual Thinking/Non-Thinking modes. OpenAI- and Anthropic-API compatible. Legacy `deepseek-chat` / `deepseek-reasoner` retired 2026-07-24. |
| Apr 27 | Workflows public preview | Mistral | VENDOR | Enterprise orchestration. No learning content. |

### May 2026

| Date | Item | Vendor | Grade | Learning-relevant content |
|---|---|---|---|---|
| May 19 | **Gemini 3.5 (Flash)** — "frontier intelligence with action" | Google DeepMind | MEASURED-BENCH (vendor-run) | Terminal-Bench 2.1 76.2%; GDPval-AA 1656 Elo; MCP Atlas 83.6%; CharXiv Reasoning (multimodal) 84.2%. Claims 4× faster output tokens/sec than other frontier models. Gemini 3.5 Pro flagged as internal-only, "rolling out next month." **No education or math claims in the post.** |
| May 19 | **Project Genie + Street View grounding** | Google DeepMind | DEMO | General-purpose world model; generates interactive environments now grounded in real Street View locations (US only). Google AI Ultra subscribers, $200/month, 18+, global. Explicitly "an experimental research prototype in Google Labs." **No education use case named.** |
| May (I/O) | **Gemini Omni** | Google DeepMind | VENDOR / partial DEMO | "Create anything from any input — starting with video." Input: image, audio, video, text. Output: **video only** at launch; image and audio output promised "in time." Gemini app (AI Plus/Pro/Ultra), Flow, YouTube Shorts. Developer/enterprise API "in the coming weeks." No latency, no benchmarks, no pricing published. |
| May 22 | Mistral Medium 3.5 + remote agents in Vibe | Mistral | VENDOR | No learning content. |
| May 27–28 | Physics AI; Vibe; Search Toolkit | Mistral | VENDOR | Physics-AI is a surrogate-model class for physical systems, not a tutoring capability. |

### June 2026

| Date | Item | Vendor | Grade | Learning-relevant content |
|---|---|---|---|---|
| Jun 3 | **Gemma 4 12B** | Google DeepMind | VENDOR | Unified **encoder-free** multimodal model — no separate vision or audio encoder; raw audio projected directly into token space. First mid-sized Gemma with native audio input. Runs in **16GB VRAM / unified memory**. Apache 2.0. Multi-Token-Prediction drafters for latency. Shipped to HF, Kaggle, LM Studio, Ollama, Google AI Edge. Context window not stated. |
| Jun 9 | **"Measuring the impact of learning with AI in Sierra Leone and beyond"** | Google DeepMind + Fab AI, Sierra Leone MoE, Google.org, Gates Foundation, EducAid, Laterite, Oxford MeasurEd | **RCT** | **The single most important learning item in the quarter.** Pre-registered RCT, 1,763 junior-secondary students, 12 schools, Port Loko District, 8 weeks. Gemini **Guided Learning**. Result: **+0.258 SD in maths**, characterised by the authors as ~1.2–1.7 years of typical learning progress; ~1.8–2.5 years in high-engagement classrooms (12h of instruction). 69% of students met/exceeded usage targets. 113,000+ conversations analysed: 91.4% of conversations coded as building conceptual understanding rather than answer-seeking; scaffolding questions in 76% of model responses vs. direct solutions in 2%. Explicitly credited to "years of research and work in our **LearnLM** efforts." |
| Jun 9 | **Gemini 3.5 Live Translate** | Google DeepMind | VENDOR | Near-real-time speech-to-speech, **70+ languages**, 2000+ language pairs in one session, stays "a few seconds behind the speaker." Live API + AI Studio public preview; Google Meet private preview; Google Translate Android/iOS global rollout. Post explicitly names "lessons" as a use case. |
| Jun 9 | **Claude Fable 5 GA; Claude Mythos 5 (invite-only, Project Glasswing)** | Anthropic | VENDOR | Fable 5: 1M context, 128k max output, $10/$50 per MTok, adaptive thinking always on, reliable knowledge cutoff Jan 2026. |
| Jun | DiffusionGemma — 4× faster text generation | Google DeepMind | VENDOR | Diffusion-based decoding. Latency delta, not capability delta. |
| Jun | Computer use in Gemini 3.5 Flash | Google DeepMind | VENDOR | Agentic UI control. |
| Jun | Nano Banana 2 Lite + Gemini Omni Flash | Google DeepMind | VENDOR | Cheaper generation tier. |
| Jun 23 | Mistral OCR 4 | Mistral | VENDOR | Document intelligence. **Genuinely relevant to learning** — worksheet/textbook digitisation is the unglamorous bottleneck in most classroom pipelines. No education framing in the post. |
| Jun 29 | Brain2Qwerty | Meta | DEMO | Non-surgical brain-to-text. Accessibility-adjacent, not a near-term learning capability. |
| Jun 30 | **Claude Sonnet 5** | Anthropic | VENDOR | 1M context, 128k output, intro pricing **$2/$10** per MTok through Aug 31 2026 (then $3/$15). Available on Free tier. Framed as "most agentic Sonnet yet." No education claims. |

### July 2026

| Date | Item | Vendor | Grade | Learning-relevant content |
|---|---|---|---|---|
| Jul 2 | **Leanstral 1.5** | Mistral | MEASURED-BENCH (vendor-run) | 119B total / 6B active, **Apache-2.0, weights on HF, free API endpoint**. Lean 4 formal proof engineering with compiler-feedback multi-turn refinement and agentic file/command/goal inspection. **Saturates miniF2F (100% val and test)**; 587/672 PutnamBench; FATE-H 87%; FATE-X 34%. |
| Jul 7 | Muse Image, Muse Video | Meta | VENDOR | Generative media. |
| Jul 8 | **GPT-Live (GPT-Live-1, GPT-Live-1 mini)** | OpenAI | VENDOR | **Full-duplex architecture — listens and speaks simultaneously.** Backchannels ("mhmm", "yeah"), can stay silent while you think. Delegates hard sub-tasks to a frontier model (GPT-5.5 at launch) *in the background while continuing to talk*. Rolling out to ChatGPT users globally; **API "soon", sign-up form only**. |
| Jul 9 | **GPT-5.6 family: Sol (flagship), Terra, Luna** | OpenAI | MEASURED-BENCH (vendor-run) | GA following limited preview. **Agents' Last Exam: Sol 53.6**, +13.1 over Claude Fable 5 (adaptive reasoning); at medium reasoning still +11.4 at ~¼ estimated cost. Artificial Analysis Intelligence Index: Sol at max reasoning within 1 point of Fable 5, 61% less time, ~half estimated cost. New `ultra` setting coordinates multiple agents across parallel workstreams. Pricing per secondary source (Simon Willison, unconfirmed on the OpenAI page I retrieved): Luna $1/$6, Terra $2.50/$15, Sol $5/$30. |
| Jul 9 | Muse Spark 1.1 | Meta | VENDOR | First Spark model with API access. |
| Jul 13 | Pelé "lost goal" reconstruction | Google DeepMind | DEMO | Mini-documentary. Pure demo. Worth noting only because video reconstruction of historical events is a plausible future learning surface and this is the state of the demo. |
| Jul 14 | **Claude for Teachers** | Anthropic | VENDOR | Free for **verified US K-12 educators only**; sign up by Jun 30 2027 for a full year. Lesson planning against evidence-based curricula mapped to standards in all 50 states; differentiation; class-data analysis via Claude Code and Cowork; scheduled task automation. Nine platform integrations (ASSISTments, Brisk, Canva Education, …). Skills co-developed with Learning Commons. FERPA; no training on data. **No published benchmark.** Anthropic's own post concedes that evidence of teacher-tool impact *on students* is "mixed." |
| Jul 14 | **ATL Saathi** | Google DeepMind / Google India | VENDOR | Gemini 3.5 Flash powering a 24/7 planning and training assistant for Atal Tinkering Lab educators. **Pilot: 100 schools**; network reach cited as 11M students. 8 languages at launch. NotebookLM used for content curation. **No baseline metrics or success targets published.** |
| Jul 21 | **Gemini 3.6 Flash; Gemini 3.5 Flash-Lite; Gemini 3.5 Flash Cyber** | Google DeepMind | MEASURED-BENCH (vendor-run) | 3.6 Flash: **17% fewer output tokens** than 3.5 Flash on the AA index (up to 65% on DeepSWE); DeepSWE 49% vs 37%; MLE-Bench 63.9% vs 49.7%; OSWorld-Verified 83.0% vs 78.4%. **$1.50/$7.50 per 1M.** 3.5 Flash-Lite: **350 output tokens/sec**, Terminal-Bench 2.1 54% vs 31% for 3.1 Flash-Lite, **$0.30/$2.50 per 1M**. |
| Jul 24 | **Claude Opus 5** | Anthropic | MEASURED-BENCH (vendor-run) | $5/$25 per MTok (unchanged from Opus 4.8), 1M context, 128k output, reliable knowledge cutoff May 2026. Frontier-Bench v0.1: >2× Opus 4.8 at lower cost/task. CursorBench 3.2 within 0.5% of Fable 5 at half cost. **ARC-AGI 3: 3× the next-best model.** Zapier AutomationBench ~1.5× next-best. OSWorld 2.0 above Fable 5 at ~⅓ cost. Fast mode ~2.5× speed at 2× price. **No GPQA or dedicated maths score published.** Gains highlighted in organic chemistry (+10.2pp) and protein prediction (+7.7pp). |

---

## 2. LearnLM: the specific investigation

This was the assignment's flagged item and the answer is clean and slightly
deflationary.

**LearnLM no longer exists as a model family.** Google's own Gemini API
documentation states:

> "LearnLM is no longer a separate listing in AI Studio. Instead, LearnLM
> capabilities have been integrated into Gemini starting with the 2.5 model
> series."

Verified 2026-07-25 at `https://ai.google.dev/gemini-api/docs/learnlm`. There
is no LearnLM entry in the current Gemini model list
(`https://ai.google.dev/gemini-api/docs/models`), which enumerates Gemini 3.6
Flash, 3.5 Flash, 3.5 Flash-Lite, 3.1 Flash-Lite, the 2.5 series, 3.1 Flash
Live, 2.5 Flash Live, Gemini Embedding 2, Deep Research, and Computer Use —
and nothing pedagogy-branded.

**What this means, and why it is the most important structural fact in this
report.** The pedagogy-tuned model as a *purchasable artifact* is dead. There
is no model ID you can call to get a tutor. What survives is:

1. **Post-training that is now diffused into the base model** and therefore
   not separately steerable, measurable, or attributable. You cannot A/B a
   "LearnLM-on" against a "LearnLM-off" Gemini, because there is no switch.
2. **A product surface — "Guided Learning"** — which is where the pedagogy
   actually lives now, as system instructions and product scaffolding on top
   of a general model.

This is the identical architectural pattern to OpenAI's Study Mode, which the
Study Mode announcement describes explicitly as "powered by custom system
instructions we've written in collaboration with teachers, scientists, and
pedagogy experts." Both labs converged on the same answer: **pedagogy is a
prompt layer, not a weights layer.**

And the one hard result of the quarter — the Sierra Leone RCT — is a result
about *Guided Learning*, the prompt-and-product layer, not about a
pedagogy-tuned model. DeepMind credits the LearnLM research lineage in prose,
but what was deployed and measured was a product surface.

The practical consequence for anyone building: **the pedagogical layer is
yours to build and yours to own.** No vendor is selling it to you as a model.
That is simultaneously the biggest opportunity and the reason most of this
quarter's model releases are irrelevant to you.

---

## 3. Vendor-by-vendor, through the learning lens

**Google DeepMind** — the only lab that shipped *both* a learning product and
learning evidence this quarter. Sierra Leone RCT (Jun 9) is the strongest
piece of AI-education evidence any lab has produced. ATL Saathi (Jul 14) is a
real deployment at pilot scale. Guided Learning is the live surface. Against
that: Gemini 3.5 (May 19) and 3.6 Flash (Jul 21) posts contain **no education
or maths claims at all**, and Genie remains a $200/month Labs prototype.

**OpenAI** — shipped GPT-5.5 (Apr 23), GPT-Live (Jul 8), GPT-5.6 (Jul 9), all
framed around agentic coding, knowledge work, cyber, and science. **OpenAI
launched no new education product in this window.** Its education surface —
Study Mode (2025-07-29) and ChatGPT for Teachers (2025-11-19) — entirely
predates the quarter. GPT-Live's full-duplex architecture is the single most
pedagogically interesting thing OpenAI shipped, and it is not in the API.

**Anthropic** — Fable 5 (Jun 9), Sonnet 5 (Jun 30), Opus 5 (Jul 24), all 1M
context. Claude for Teachers (Jul 14) is a genuine education launch but is
**teacher-facing, US-only, and unmeasured** — the post cites external Stanford
work rather than its own evaluation, and concedes student-level evidence is
mixed. Sonnet 5 at $2/$10 intro on the Free tier is the meaningful number here.

**Meta** — Muse Image/Video (Jul 7), Muse Spark 1.1 (Jul 9), Brain2Qwerty (Jun
29). **Nothing education-facing.** No Llama release in-window surfaced on the
AI-at-Meta blog index.

**Mistral** — the surprise. **Leanstral 1.5 (Jul 2)** is the most
consequential maths release of the quarter and it is Apache-2.0 with a free
API endpoint. Saturating miniF2F is a "this benchmark is now retired" event.
Also OCR 4 (Jun 23), which matters more for classroom pipelines than most
frontier model news. No education product.

**Qwen** — **could not verify.** `qwen.ai/blog` renders client-side and
returned no content; `qwenlm.github.io/blog` is stale (latest post
2025-09-23); the Hugging Face org page shows Qwen3-ASR-0.6B/1.7B and
Qwen-AgentWorld-35B-A3B with relative timestamps that do not resolve to
absolute dates. **I cannot make any claim about Qwen releases in April–July
2026.**

**DeepSeek** — V4-Pro and V4-Flash (Apr 24). **1M context by default across
all official services** is the single cleanest long-context delta of the
quarter and it came from the cheapest vendor. Benchmark table exists on the
page but the specific AIME/MATH figures did not survive extraction; treat
DeepSeek maths claims as **unverified**.

**Moonshot** — **could not verify.** `moonshotai.github.io` is a bare
redirect. The Hugging Face org lists Kimi-K2.7-Code (1.1T), Kimi-K2.6 (1.1T),
Kimi-VL-A3B-Thinking-2506, but the "updated" dates returned (2025-06-15,
2025-05-19, 2025-01-30) are internally inconsistent with the version numbering
and I do not trust them. **No dated Moonshot claim should be made from this
research.**

---

## 4. arXiv sweep: 20 most relevant, and the clusters

The arXiv API (`export.arxiv.org`) rate-limited every request across a 20-minute
window; Semantic Scholar returned 429 as well. The sweep below was done through
the arXiv **search UI**, which worked. Six queries, IDs and months as reported
by arXiv.

### The 20 most relevant (April–July 2026, plus three Feb/Mar anchors)

| # | arXiv ID | Date | Title | Why it matters |
|---|---|---|---|---|
| 1 | 2606.16206 | Jun 2026 | Measuring Whether LLM Tutors Teach or Solve: A Diagnostic for Educational Impact | **The finding of the sweep.** Solving ability and pedagogical ability are only partially aligned (r=0.421) on public benchmarks. Model capability ≠ tutoring capability. |
| 2 | 2607.09919 | Jul 2026 | When LLM Tutoring Responses Work: Evidence from Student Programming Conversations | 16,851 real interactions; verification feedback most predictive of productive student continuation. Rare large-N observational study. |
| 3 | 2606.15766 | Jun 2026 | Rethinking Scaffolding in LLM Tutors: The Interactional Mismatch Between Benchmarks and Real-World Deployments | Argues the benchmarks don't measure what deployment needs. Directly on-topic for §5. |
| 4 | 2607.03303 | Jul 2026 | Reflective Dialogue or Prompt Refinement? Effects of Tutor Scaffolding on Students' Independent LLM Use | Socratic guidance beats prompt-refinement for long-term learning. |
| 5 | 2605.14604 | May 2026 | Sycophancy is an Educational Safety Risk: Why LLM Tutors Need Sycophancy Benchmarks | Models resist context-switch attacks but fold under social-epistemic pressure — i.e. they cave when a student pushes back. |
| 6 | 2605.12748 | May 2026 | Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators | LLM "students" treat feedback as an abandonment cue, not a belief update. Undermines simulator-based tutor evaluation. |
| 7 | 2603.02775 | Mar 2026 | From Solver to Tutor: Evaluating the Pedagogical Intelligence of LLMs with KMP-Bench | KMP-Bench (K-8 maths) + KMP-Pile (150K dialogues). One of the few substantial pedagogical benchmarks. |
| 8 | 2604.22134 | Apr 2026 | SHAPE: Unifying Safety, Helpfulness and Pedagogy for Educational LLMs | 9,087 pairs; introduces "pedagogical jailbreaks" (getting the tutor to just give the answer). |
| 9 | 2607.10647 | Jul 2026 | Knowledge Distillation for Automated AI Tutor Evaluation | FATE — an 8B specialised evaluator for mistake identification and guidance quality. Cheap pedagogical judging. |
| 10 | 2605.29582 | May 2026 | PEARL: Training Socratic Tutors with Pedagogically Aligned Reinforcement Learning | RL on pedagogy with a controllable student simulator; competitive at 30B. |
| 11 | 2605.27088 | May 2026 | LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring | **Prompt evolution beats RL-trained baselines.** The strongest published evidence that pedagogy is a prompt layer. |
| 12 | 2606.11744 | Jun 2026 | Hey Chat, Can You Teach Me? Structuring Socratic Dialogue for Human Learning in the Wild | PPO sequencing beats frontier models by decoupling curriculum, dialogue, and knowledge inference. |
| 13 | 2604.18660 | Apr 2026 | Evaluating Answer Leakage Robustness of LLM Tutors against Adversarial Student Attacks | Students attacking their own tutor is now a named threat model. |
| 14 | 2607.05571 | Jul 2026 | CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming | 4B–120B: **instruction-tuning matters more than parameter count** for tutoring. |
| 15 | 2606.20713 | Jun 2026 | FairTutor: Equity-Aware Pedagogical LLM Routing for Budget-Constrained AI Tutoring | 97.1% of premium quality at 71.6% cost reduction via routing. Introduces TutorAccessEval. |
| 16 | 2604.26962 | Apr 2026 | DeepTutor: Towards Agentic Personalized Tutoring | Open-source; +10.8% on personalisation metrics via hybrid knowledge-memory coupling. |
| 17 | 2606.18372 | Jun 2026 | Redact or Keep? Fully Local AI Cascade for Educational Dialogue De-Identification | 0.958 F1 on maths tutoring transcripts, fully local. The unglamorous enabler for school deployment. |
| 18 | 2606.31012 | Jun 2026 | Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations | Closest thing to an "is this a good explanation" metric; scores interaction design, validated against human pedagogical judgement. |
| 19 | 2607.11292 | Jul 2026 | The Paternalistic Filter: Epistemic Injustice in LLM-Mediated History Education | Safety-aligned refusal falls differentially on marginalised students. Alignment tax paid by learners. |
| 20 | 2605.30670 | May 2026 | Reinforcement Learning for Special Education: Disability-Adaptive Training | Special-R1; difficulty coupled to disability-specific teaching styles across five profiles. |

Anchors just outside the window, included because §5 needs them:
2603.17373 (SafeTutors, Mar 2026), 2602.15531 (EduEVAL-DB, Feb 2026),
2602.16033 (CS1 prompting RCT, n=979, Feb 2026).

### Six clusters, not a list

**C1 — "Teaching ≠ solving," now measured.** 2606.16206 (r=0.421),
2607.05571, 2603.02775. The field has moved from asserting this to
quantifying it. Frontier model capability gains do **not** transfer to
tutoring quality, and there is now a correlation coefficient saying so. This
is the single most important cluster for anyone deciding whether to wait for
the next model.

**C2 — Pedagogy is a prompt layer (and the evidence is embarrassing for the
RL camp).** 2605.27088 shows training-free prompt optimisation beating
RL-trained baselines. 2605.29582 (PEARL) and 2606.11744 push back with RL
methods. But the cheap-method-wins result, arriving in the same quarter that
Google folded LearnLM into Gemini and OpenAI shipped Study Mode as system
instructions, is a consilience worth taking seriously.

**C3 — Adversarial pedagogy is now a real subfield.** 2604.18660 (answer
leakage under student attack), 2604.22134 (pedagogical jailbreaks),
2605.14604 (sycophancy as a safety risk), 2605.06669 (prompt injection
defences), 2603.17373 (SafeTutors, 11 harm dimensions). The threat model is
no longer "the model says something harmful" — it is **"the student
successfully talks the tutor into doing the work."** This did not exist as a
research area 12 months ago.

**C4 — Simulated students, and the crisis of their validity.** 2606.14113,
2605.30144, 2605.06307, 2604.26962 all build or use student simulators. But
2605.12748 shows simulators treat corrective feedback as an abandonment cue
rather than updating a misconception, and 2605.06307 shows persona drift in
unscripted dialogue. **The evaluation infrastructure the field is building
its benchmarks on is itself unvalidated.** This is a load-bearing weakness.

**C5 — Cost, locality, and equity as first-class design constraints.**
2606.20713 (FairTutor routing, −71.6% cost), 2606.18372 (fully-local
de-identification), 2606.30662 (ELEVATE, consumer hardware), 2607.05571
(small models as tutors). The field has stopped assuming frontier API access.
This cluster tracks the on-device/cheap-inference delta better than any
vendor blog does.

**C6 — Curriculum grounding via RAG, not long context.** 2605.06963 (Moodle
RAG, 0.97 faithfulness), 2607.15738 (EduGuard RAG + BILearn-CS), 2606.17507
(curriculum-grounded marking), 2604.09619 (Nepal K-10 curriculum alignment).
**Notably: a targeted arXiv query for long-context / whole-textbook-in-context
educational grounding returned literally zero results.** Nobody is putting the
textbook in the context window. Everyone is retrieving. See §6.

---

## 5. Benchmarks: does a good "is this a good explanation" benchmark exist?

**No. Not in any meaningful sense. This is the finding.**

Here is what does exist, as of 2026-07-25:

| Benchmark | Date | What it measures | What it does not |
|---|---|---|---|
| KMP-Bench + KMP-Pile (2603.02775) | Mar 2026 | Pedagogical intelligence, K-8 maths, 150K dialogues | Human learning outcomes |
| SHAPE (2604.22134) | Apr 2026 | Safety × helpfulness × pedagogy, 9,087 pairs | Learning gain |
| SafeTutors (2603.17373) | Mar 2026 | Pedagogical safety, 11 harm dimensions, 3 subjects | Whether teaching works |
| CSTutorBench (2607.05571) | Jul 2026 | 17 scenario questions + rubric, block-based programming | Generality; n=17 |
| TutorAccessEval (2606.20713) | Jun 2026 | Quality-under-budget across 5 domains | Absolute pedagogical validity |
| BILearn-CS (2607.15738) | Jul 2026 | 600 instructor-authored CS queries | Non-CS domains |
| EduEVAL-DB (2602.15531) | Feb 2026 | 854 explanations, pedagogical *risk* rubric | Pedagogical *benefit* |
| FATE (2607.10647) | Jul 2026 | 8B judge for mistake-ID and guidance | It is a judge, not a ground truth |
| Interactivity assessment (2606.31012) | Jun 2026 | Interaction design of explorable explanations | Text explanations |

**Every one of these is a proxy.** They fall into three families, and all three
families share the same defect:

1. **Rubric-scored-by-LLM-judge** (most of them). Circular: you are asking a
   model whether a model explained well. 2607.10647 distils this into a
   cheaper judge, which makes the circularity cheaper, not less circular.
2. **Human-expert-rated dialogue quality.** Better, but experts rate
   *plausibility of pedagogical form* — did it ask a question, did it scaffold
   — not whether a human ended up knowing more.
3. **Risk / harm rubrics** (EduEVAL-DB, SafeTutors, SHAPE). These measure the
   absence of bad, not the presence of good.

**The missing benchmark is one where the dependent variable is a human
learning outcome.** A good explanation is one that produces comprehension,
retention, and transfer in a person who did not previously understand. That is
a measurement that requires human subjects, a delay, and a transfer test. No
public benchmark does this. Every benchmark in the table above substitutes a
judgement about the explanation for a measurement of its effect.

Three corroborating signals that the field knows this:

- 2606.15766 is literally titled around "the interactional mismatch between
  benchmarks and real-world deployments."
- 2606.16206 shows benchmark pedagogy scores and solving scores are only
  weakly correlated (r=0.421) — which means the benchmarks are measuring
  *something*, but nobody has shown that something predicts learning.
- The one study in the quarter that did measure a human learning outcome —
  the Sierra Leone RCT — is not a benchmark. It is a field trial that costs
  months and a ministry partnership, and it produced a single number (+0.258
  SD) for a single product in a single context.

**Implication.** The gap between "we can measure whether a model is smart"
(dozens of benchmarks, updated monthly) and "we can measure whether a model
teaches" (one RCT per year, per organisation, at national-partnership cost) is
the widest measurement gap in applied AI right now. Anyone building in this
space is building without a ruler. The correct posture is not to wait for the
benchmark — it is to instrument your own product for learning outcomes,
because that is the only measurement that exists, and it does not come from
a leaderboard.

---

## 6. Capability deltas: which ones actually change what's buildable

The brief asked me to argue about which deltas matter. My argument is that
**four of the five candidate deltas do not change what's buildable in
learning, and the two things that do change it are not on the list.**

### Delta 1 — Longer context (whole textbook in context): **does not matter**

The evidence is unusually clean. Context is now abundant and cheap: Claude
Fable 5 / Opus 5 / Sonnet 5 all at 1M tokens; DeepSeek shipped **1M as the
default across all services** on Apr 24 at commodity prices. A whole textbook
has been comfortably in-context for over a year.

And yet: a targeted arXiv query for long-context/whole-textbook educational
grounding returned **zero results**, while the RAG-for-curriculum cluster (C6)
is one of the healthiest in the sweep — Moodle RAG at 0.97 faithfulness,
EduGuard, curriculum-grounded marking, Nepal K-10 alignment.

The field looked at "put the textbook in the window" and chose retrieval
instead. That is not inertia. It is because the binding constraint was never
capacity — it was **attribution and verifiability**. A teacher needs to know
*which page* the claim came from, and a stuffed context window destroys that
affordance while adding cost and latency. Long context solved a problem
learning did not have.

### Delta 2 — Better maths: **matters enormously, for research maths; near-zero for learning**

Leanstral 1.5 saturating miniF2F (100%) on Jul 2, Apache-2.0, free endpoint,
is a genuinely historic result. It is also almost entirely irrelevant to
learning, and the reason is C1: **solving and teaching are only weakly
correlated (r=0.421)**.

The maths a learner needs help with is not Putnam. It is fractions, and the
specific fraction misconception this specific child holds. Every model in this
window already solves that problem perfectly. The unsolved problem is
diagnosing the misconception and choosing not to solve it — and no maths
benchmark in existence measures that. Note that DeepMind's own Gemini 3.5 and
3.6 Flash posts make **no maths claims at all**, and Anthropic published **no
maths score for Opus 5**. The frontier labs have stopped competing on the axis
that was never the bottleneck anyway.

Sub-note: the AlphaProof/AlphaGeometry lineage produced **nothing publicly in
this window.** I checked the DeepMind blog index and the Research-filtered
index; no AlphaProof, AlphaGeometry, or IMO post appears in April–July 2026.
The formal-maths story this quarter belongs to Mistral, not DeepMind.

### Delta 3 — Live multimodality: **the one that actually matters, and it isn't shipped**

GPT-Live (Jul 8) is the most pedagogically significant capability in the
quarter and almost nobody framed it that way. **Full-duplex** — listening and
speaking simultaneously, backchannelling with "mhmm," staying silent while the
learner thinks — is not a UX polish item. Turn-taking is the atomic unit of
tutoring. Every human tutor's core skill is knowing when *not* to speak while
a student is mid-thought. Turn-based voice models structurally cannot do this;
they must wait for a terminal silence and then talk. Full-duplex is the first
architecture that can hold a productive silence.

The second half — delegating a hard sub-problem to a frontier model in the
background *while continuing the conversation* — is exactly the shape of a
tutor who says "hold on, let me think about that" and keeps the rapport alive.

**But: GPT-Live is ChatGPT-only. The API is "coming soon" behind a
notification form.** You cannot build on it today. On the Google side, Gemini
3.5 Live Translate (Jun 9) *is* in public preview via the Live API, and the
post names "lessons" as a use case, but it is a translation model, not a
tutoring one.

So the highest-value delta of the quarter is, for builders, **unavailable**.
That is the most actionable single fact in this report.

### Delta 4 — Cheaper inference: **matters, and is under-appreciated**

The numbers this quarter are real: Gemini 3.5 Flash-Lite at **$0.30/$2.50 per
1M and 350 output tokens/sec** (Jul 21); Gemini 3.6 Flash using **17% fewer
output tokens** than its predecessor for better scores; Claude Sonnet 5 at
**$2/$10 intro, available on the Free tier**; GPT-5.6 Terra and Luna reported
to beat Fable 5 at ~1/16 the cost; DeepSeek V4-Flash at 13B active with 1M
context.

This matters for a reason that has nothing to do with capability: **tutoring
is a high-turn-count application.** A coding agent might make 50 calls to
finish a task. A one-hour tutoring session is hundreds of short turns, and the
product only works if the model can afford to be patient — to ask instead of
tell, which costs more turns to reach the same endpoint. Pedagogy is
economically penalised by expensive inference. FairTutor (2606.20713) makes
this explicit: 97.1% of premium quality at 71.6% lower cost via routing.

The price of a Socratic dialogue fell meaningfully this quarter. That changes
what is viable at scale in a way that ARC-AGI scores do not.

### Delta 5 — On-device: **matters for institutions, not for capability**

Gemma 4 12B (Jun 3) is the item: encoder-free unified multimodal, **native
audio input**, runs in **16GB VRAM**, Apache 2.0, shipped to Ollama and LM
Studio and Google AI Edge on day one. Paired with the local de-identification
work (2606.18372, 0.958 F1 on maths tutoring transcripts) and ELEVATE
(2606.30662, consumer hardware), a fully-local school deployment is now
buildable.

The unlock is not capability — a local 12B is worse than a frontier API at
everything. The unlock is **jurisdictional**. Student data is the most
regulated data class outside health, and "the transcript never leaves the
building" converts a two-year procurement into a decision a single school can
make. Note that both education launches this quarter had to solve this
politically instead: Claude for Teachers leads with FERPA and no-training
guarantees, and is US-only *because* of it.

### The two deltas that aren't on the list

**(a) The pedagogy layer became permanently yours.** LearnLM's dissolution
into Gemini (verified §2), Study Mode as system instructions, and 2605.27088
showing prompt optimisation beating RL, all point the same way. No vendor will
sell you a tutor. This is a delta in *market structure*, not capability, and it
is more consequential than any benchmark movement this quarter.

**(b) Adversarial pedagogy arrived as a discipline.** Cluster C3 — answer
leakage under student attack, pedagogical jailbreaks, sycophancy under social
pressure. The finding in 2605.14604 is the sharp one: **models resist
adversarial framing but fold under social pressure.** A student who simply
insists gets the answer. Any tutoring product shipping without a defence here
will be defeated by a determined fourteen-year-old in an afternoon, and this
threat model did not exist as literature a year ago.

### Summary judgement

Of the five nominated deltas: **long context is a non-event for learning;
better maths is a non-event for learning; live multimodality is the real one
and is not yet available to build on; cheaper inference is quietly the most
useful shipped delta; on-device is a compliance unlock rather than a
capability one.** The frontier moved a great deal this quarter and moved
learning very little — with one exception, and it was not a model release. It
was an RCT.

---

## 7. Explicitly could not verify

- **Qwen, April–July 2026 — nothing verified.** `qwen.ai/blog` is
  client-rendered and returned no content to any fetcher; `qwenlm.github.io`
  is stale to 2025-09-23; Hugging Face relative timestamps did not resolve.
  No Qwen claim in this report.
- **Moonshot / Kimi, April–July 2026 — nothing verified.**
  `moonshotai.github.io` is a bare redirect. Hugging Face listed Kimi-K2.7-Code
  (1.1T), Kimi-K2.6 (1.1T), Kimi-VL-A3B-Thinking-2506, but with dates
  (2025-06-15, 2025-05-19) inconsistent with the version numbering. Not used.
- **GPT-5.6 pricing** (Luna $1/$6, Terra $2.50/$15, Sol $5/$30) comes from a
  secondary source (simonwillison.net), not the OpenAI page I retrieved.
- **DeepSeek V4 benchmark specifics.** The announcement page references a
  benchmark chart; specific AIME/MATH/coding figures did not survive text
  extraction. Context (1M default) and parameter counts are verified; maths
  claims are not.
- **Gemini context windows.** `ai.google.dev/gemini-api/docs/models` did not
  expose per-model token limits in the retrieved content. Gemini 3.x context
  lengths are unverified here.
- **Gemini 3.5 Pro.** Announced May 19 as internal-only with rollout "next
  month." I found no post confirming GA. Status unverified.
- **Gemini Omni** — no latency, no benchmarks, no pricing published; output
  is video-only at launch; developer API was "coming weeks" as of May.
  Availability for builders unverified.
- **Guided Learning product page.** The Google support article 404'd. All
  Guided Learning detail here comes from the Sierra Leone RCT post.
- **Meta Llama.** No Llama release surfaced on `ai.meta.com/blog` for the
  window. Absence of evidence only.
- **arXiv API and Semantic Scholar** both returned sustained HTTP 429. The
  paper sweep is from the arXiv **search UI** across six queries and is
  therefore recall-limited; it is not an exhaustive enumeration of the
  period's education-LLM literature.
- **AlphaProof / AlphaGeometry.** No post found in April–July 2026 on either
  DeepMind blog index (including the Research-filtered view). Reported as
  absent, not as confirmed-nonexistent.
