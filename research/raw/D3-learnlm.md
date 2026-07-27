---
title: "Google's LearnLM programme: the only serious attempt to make pedagogy measurable — and what it teaches"
wave: D
date_researched: 2026-07-27
sources_count: 26
---

# D3 — LearnLM: what the programme published, and what it actually proved

## 0. Method, and what changed versus D1

WebSearch was exhausted. Everything below comes from `curl`/`WebFetch` against
arXiv (`export.arxiv.org` API and `arxiv.org/html/`), `storage.googleapis.com`
(DeepMind media), `services.google.com`, `cloud.google.com`, `blog.google`,
`deepmind.google`, `ai.google.dev`, and `gemini.google`. **I read every primary
document cited here in full text** — not secondary coverage. Where a document is
unreachable I say so.

**Evidence labels** (project standard): `MEASURED-RCT` · `MEASURED-BENCH` ·
`OBSERVED` (human-rated, non-outcome) · `VENDOR` · `INFERENCE`.

**The complete LearnLM publication corpus.** An arXiv API query for `all:LearnLM`
sorted by date returns exactly seven hits, of which four are authored by "LearnLM
Team, Google". A fifth LearnLM Team report — the Sierra Leone RCT — is **not on
arXiv**; it exists only as a PDF on `storage.googleapis.com`. The canonical index
is `https://cloud.google.com/solutions/learnlm`, which lists five reports:

| # | Date | Title | Where | Grade |
|---|---|---|---|---|
| R1 | 2024-05-21 (v4 2025-12-02) | Towards Responsible Development of Generative AI for Education: An Evaluation-Driven Approach | arXiv 2407.12687 | `OBSERVED` |
| R2 | 2024-12-21 (v3 2025-08-22) | LearnLM: Improving Gemini for Learning | arXiv 2412.16429 | `OBSERVED` |
| R3 | 2025-05-19 | Evaluating Gemini in an Arena for Learning | arXiv 2505.24477 · `deepmind-media/LearnLM/learnLM_may25.pdf` | `OBSERVED` |
| R4 | 2025-12-29 | AI tutoring can safely and effectively support students: An exploratory RCT in UK classrooms | arXiv 2512.23633 | `MEASURED-RCT` |
| R5 | 2026-05-15 | Teaching with Gemini: Measuring the impact of Guided Learning on student mathematics progress in Sierra Leone | `deepmind-media/LearnLM/learnLM_sierraleone_may26.pdf` | `MEASURED-RCT` |

Plus one adjacent LearnLM Team paper not on that index: **Towards an AI-Augmented
Textbook** (Learn Your Way), arXiv 2509.13348v4, which contains its own small RCT.

**Three corrections to D1** (all from the primary tech report R5, which D1 did not
have):

1. D1 says "12 schools." The trial was **12 schools *and* 48 classrooms** — the
   classroom, not the school, was the randomisation unit. This matters: the
   authors themselves flag the spillover trade-off.
2. D1 says "113k conversations coded." It was **113,344 *messages* across 7,421
   conversations.** An order-of-magnitude difference in the denominator.
3. D1 dates the Sierra Leone result to Jun 9 2026 (DeepMind blog). The **technical
   report is dated 2026-05-15** and the Google blog version dates to **May 19
   2026**. The DeepMind blog post is a later re-issue. Use the May dates.

---

## 1. The pedagogical principles, verbatim and complete

### 1.1 The five principles and their original operational definitions

The canonical five-item set first appears in the LearnLM launch post
(`blog.google/outreach-initiatives/education/google-learnlm-gemini-generative-ai/`,
**2024-05-14**), each with a one-line operational gloss. Verbatim: `VENDOR`

> - **Inspire active learning**: Allow for practice and healthy struggle with timely feedback
> - **Manage cognitive load**: Present relevant, well-structured information in multiple modalities
> - **Adapt to the learner**: Dynamically adjust to goals and needs, grounding in relevant materials
> - **Stimulate curiosity**: Inspire engagement to provide motivation through the learning journey
> - **Deepen metacognition**: Plan, monitor and help the learner reflect on progress

The technical-report wording (R1 §4.3.1, arXiv 2407.12687v4) is longer and carries
the learning-science citations. Verbatim: `OBSERVED`

> The high-level pedagogical principles we prioritised are: **encourage active
> learning** (the learner should manipulate information through discussion,
> practice, and creation, instead of passively absorbing information [Chi ICAP,
> VanLehn, Weinstein, Oakley]), **manage cognitive load** (the tutor should present
> information in multiple modalities, structure it well, and segment it into
> manageable chunks [Mayer 2022]), **deepen metacognition** ("thinking about
> thinking", which enables learners to generalise their skills beyond a single
> context [Dehaene 2021, Cohen 2022, Lai 2011]), **motivate and stimulate
> curiosity** (as this leads to self-efficacy and lifelong learning [Keller 1987,
> Patall 2008]), and **adapt to learners' goals and needs** (by assessing the
> current state and the goals, and making a plan to bridge the gap).

**The set is stable across the entire programme.** The 2026 partner-facing prompt
guide (`services.google.com/fh/files/misc/learnlm_prompt_guide.pdf`, "Gemini 3.1:
grounded in learning science") still lists exactly: *inspires active learning ·
manages cognitive load · deepens metacognition · stimulates curiosity · adapts to
the learner.* `VENDOR` The brief's expected set is **confirmed, complete, and
unchanged over two years and four model generations.**

Note what is *absent*: no principle for retrieval practice, spacing,
interleaving, worked-example/expertise-reversal, or prior-knowledge diagnosis.
Those are the highest-effect-size items in the learning-science literature and
they are not in LearnLM's rubric. `INFERENCE` The five chosen principles are
optimised for what is *observable in a single conversation transcript*, not for
what most moves a learner over a term.

### 1.2 R1's own candour about why this list is short

R1 §3.1 is unusually honest and worth quoting because it is the strongest
argument in the whole corpus *against* the rubric it then proposes: `OBSERVED`

> "a lot of learning science experiments are done with small homogeneous
> populations, limited to specific narrow educational contexts … and typically
> conducted in WEIRD countries, thus limiting their generality. The interventions
> also often come with variable implementation parameters … resulting in a
> combinatorial explosion in possible, often context-dependent, recommended
> pedagogical strategies."

That is the stated reason the team reduced learning science to five
principles: not because five is right, but because optimisation needs a short,
measurable list.

---

## 2. How each principle was operationalised — the rubric you can actually apply

This is the most valuable artifact in the programme. It exists in three
generations; I give the **25-item May-2025 version** (R3 Appendix A, Table 4)
because it is the cleanest mapping of principle → item, and then note the
Dec-2024 additions.

Rating protocol as used: **seven-point Likert** ("Strongly disagree" →
"Strongly agree"), applied at the **conversation level** (not turn level), by a
third party who reads the transcript — *not* by the person who had the
conversation. An explicit **"Not applicable"** option is offered, and selecting it
*forces* the rater to choose a reason from {"It would not make sense for the tutor
to do this in this conversation", "The tutor had no opportunity to do this in this
conversation", "Another reason"} plus free text. That forced-justification
mechanic is a genuinely good design and is the cheapest thing on this page to
copy.

### The LearnLM pedagogy rubric (25 items, 5 principles) `OBSERVED`

**Principle 1 — Manages cognitive load** (9 items)

| Item | Statement |
|---|---|
| Appropriate response length | The tutor's responses are an appropriate length for the student. |
| Manageable chunks | The tutor uses bullet points and other formatting to break information down into smaller, manageable chunks. |
| Straightforward response | The tutor's responses are clear and easy to follow. |
| No irrelevant information | The tutor avoids irrelevant information. |
| Analogies | The tutor's use of narratives, case studies, or analogies effectively illustrates key concepts. |
| Information presentation | The tutor presents information in an appropriate style and structure. |
| Information order | The tutor develops explanations in a logical order, building on previous concepts. |
| No repetition | The tutor avoids repeating information unnecessarily. |
| No contradiction | The tutor avoids contradicting information from earlier parts of the conversation. |

**Principle 2 — Inspires active learning** (4 items)

| Item | Statement |
|---|---|
| Opportunities for engagement | The tutor provides opportunities for engagement from the student. |
| Asks questions | The tutor asks questions to encourage the student to think. |
| Guides to answer | The tutor does not give away answers too quickly. |
| Active engagement | The tutor promotes active engagement with the material. |

**Principle 3 — Deepens metacognition** (4 items)

| Item | Statement |
|---|---|
| Guide mistake discovery | The tutor guides the student to discover their own mistakes. |
| Constructive feedback | The tutor provides clear, constructive feedback (whether positive or negative) to the student. |
| Acknowledge correctness | The tutor acknowledges when part or all of the student's response is correct. |
| Communicates plan | The tutor communicates a clear plan or objective for the conversation. |

**Principle 4 — Stimulates curiosity** (3 items)

| Item | Statement |
|---|---|
| Stimulates interest | The tutor tries to stimulate the student's interest and curiosity. |
| Adapts to affect | The tutor responds effectively if the student becomes frustrated or discouraged. |
| Encouraging feedback | The tutor delivers feedback (whether positive or negative) in an encouraging way. |

**Principle 5 — Adapts to learner** (5 items)

| Item | Statement |
|---|---|
| Leveling | The tutor's explanations are appropriate for the level of the student. |
| Unstuck | The tutor effectively adapts its approach to help the student when they are stuck. |
| Adapts to needs | Overall, the tutor adapts to the student's needs. |
| Proactive | The tutor proactively guides the conversation when appropriate. |
| Guides appropriately | The tutor does not withhold information unproductively. |

**The Dec-2024 (R2) version adds a sixth "Overall" block of 4 items** (making 29):
*No inaccuracies* ("To the best of my knowledge, there are no inaccuracies in the
statements made by the tutor"); *Expresses uncertainty* ("The tutor expresses
uncertainty when appropriate"); *No refusals* ("The tutor does not refuse to answer
any reasonable questions from the student"); *Overall quality* ("The tutor is as
good as a very good human tutor"). Source: R2 Appendix B.6, Table 8.

**Comparative (side-by-side) rubric, 5 items** (R2 Appendix B.7, Table 9), each on
a seven-point "first tutor much better" → "second tutor much better" scale:

1. **Better pedagogy** — "Which tutor demonstrated better tutoring?"
2. **More like a very good human tutor** — "Which tutor was more like a very good human tutor?"
3. **Better instruction following** — "Which tutor did a better job of following its 'system instructions'?"
4. **Better adapted to learner** — "Which tutor better adapted to the student's needs and proficiency?"
5. **Better supported learning goal** — "Which tutor better helped the student achieve their 'learning goal'?"

### 2.1 Note the two deliberate self-cancelling pairs

The rubric contains two items designed to *fight* two others. This is the single
most sophisticated thing in it and the easiest to miss:

- **Guides to answer** ("does not give away answers too quickly") vs.
  **Guides appropriately** ("does not withhold information unproductively").
- **Asks questions** vs. **Appropriate response length** / **No irrelevant information**.

R1 §5.5 documents the team walking the first dial back deliberately: `OBSERVED`

> "The regression in Guides to Answer is in direct contrast to a significant
> improvement in Questions Appropriately, which is naturally opposed. **Over time
> we steered the model to exhibit Guides to Answer behaviour less, after receiving
> feedback that earlier models would unnecessarily ask questions of users, slowing
> their learning and leading to frustration.**"

Any builder who ships "always Socratic, never tell" has not read this. Google
measured that failure mode and tuned *against* it.

### 2.2 The other operationalisation: the turn-level rubric (9 moves)

R1 Table 13 is a different, cheaper instrument — nine binary "should the tutor do
this here? / did it?" judgements per turn, explicitly mapped to the principles:
`OBSERVED`

| Principle | Move | Statement |
|---|---|---|
| Manage cognitive load | Explains concepts | Explains the underlying concepts or skills in a clear way that is easy for the student to understand |
| Encourage active learning | Promotes engagement | Keeps the student actively participating (for example, through questions or practice problems that the student has to answer) |
| Encourage active learning | Guides student | Guides student to an answer with appropriate steps |
| Deepen metacognition | Identifies mistakes | Provides clear feedback identifying any mistakes made by the student |
| Deepen metacognition | Identifies successes | Provides clear feedback pointing out "successes" by the student |
| Motivate / stimulate curiosity | Inspires interest | Inspires and stimulates the interest or curiosity of the student |
| Motivate / stimulate curiosity | Monitors motivation | Monitors the student's motivational state and adjusts responses accordingly |
| Motivate / stimulate curiosity | Speaks encouragingly | Delivers feedback (whether positive or negative) in an encouraging way |
| Adapt to learners' goals and needs | Identifies goal | Identifies the student's goal or prior knowledge |

The **two-step design** — first "should the tutor demonstrate this attribute at
this point?", then "does it?" — is the correct way to avoid punishing a tutor for
not asking a question when a question was not called for. Copy this.

### 2.3 The automatic (LLM-critic) operationalisation

R1 Table 2 maps each principle onto narrow, promptable critic tasks: `OBSERVED`

| Principle | Auto-eval metrics |
|---|---|
| Manage cognitive load | Stay on topic |
| Encourage active learning | Do not reveal the answer; guide towards the answer; promote active engagement |
| Deepen metacognition | Identify and address misconceptions |
| Motivate and stimulate curiosity | Communicate with positive tone; respond appropriately to explicit affect cues |
| Adapt to the learners' goals and needs | Adapt to the learner's level |

The team's own caption is the caveat: "**LMEs measure narrow behaviours and do not
comprehensively cover each pedagogy rubric dimension. Instead, they are used as
spot checks** to expedite model development and inform which model candidate is
sent for a more comprehensive human evaluation."

R1 §6.1 makes the asymmetry argument explicitly, and it is the best justification
for LLM-judging in this domain I have read: prompting a model to *do* pedagogy is
hard, but prompting it to *judge* pedagogy is easier, because (a) evaluation is
generally easier than generation, (b) each critic judges one narrow dimension
against a targeted prompt set, and (c) **the critic gets privileged information
the tutor does not** — e.g. the correct solution when judging misconception
identification. That third point is the design insight worth stealing.

---

## 3. Training methodology, and what the ablations showed

### 3.1 R1 (2024): SFT only, on five hand-built datasets

`OBSERVED` Models M0→M4; M0–M3 fine-tuned over PaLM 2.0, **M4 (= LearnLM-Tutor)
over Gemini 1.0**, full-parameter SFT. No RL. Data mixture (R1 Table 1):

| Dataset | What it is | Role |
|---|---|---|
| **Human tutoring** | Real paid learner↔educator chat transcripts | "not targeted to any specific pedagogical behaviour… uneven quality overall" |
| **Gen AI role-play** | Two models play tutor and learner, with *dynamic prompting* and **privileged injection of the learner's internal state into the tutor prompt** (e.g. learner selects "make mistake" state → state is inserted into tutor prompt) | Long, consistent pedagogical dialogue |
| **GSM8k dialogue** | GSM8k "Socratic" step solutions in-painted into dialogue, then rewritten by a second model for flow | Correctness-guaranteed synthetic |
| **Golden conversations** | Teacher-authored transcripts against a rubric (scenario + minimal learner persona + required behaviours), AI-assisted drafting, human-edited | Highest-quality, up-weighted in M4 |
| **Safety** | Pedagogy-specific safety SFT | Refusal/harm behaviour |

**The ablation finding that matters** (R1 §3.4): `OBSERVED`

> "the more **human** examples were used to demonstrate the **stylistic** attributes
> (e.g. appropriate encouragement, when to pause, how to give proactive guidance),
> while the more **synthetic** examples helped fill more **substantive** gaps (e.g.
> how to identify and correct mistakes)."

And: "fully synthetic data without human intervention cannot have enough useful
pedagogical signal to be useful."

**Regression check** (R1 §4.1): LearnLM-Tutor reproduced Gemini Pro on MMLU (0.72)
and MATH (0.33). Turn-level factual accuracy in conversation: **96% of Gemini 1.0
turns vs 93% of LearnLM-Tutor turns "fully verified" (p=0.13, Welch)** — i.e. no
significant regression, but the point estimate moved the wrong way. `MEASURED-BENCH`

### 3.2 R2 (2024-12): the reframe to *pedagogical instruction following*, plus RLHF and co-training

Three changes, all stated in R2 §2: `OBSERVED`

1. **SFT data reframed** so that *every* conversation begins with a **different
   System Instruction that specifically describes the pedagogical behaviour present
   in that conversation.** The stated reason is sharp and is a training-data lesson
   in its own right: "**More general or vague instructions are counterproductive
   because the model learns to ignore instructions that are not useful for
   predicting the target model turns.**"
2. **RLHF added.** Raters label model samples "based on the degree to which they
   adhere to those instructions" → reward model → RL. Finding: "**While SFT seems
   to improve pedagogical instruction following somewhat, RL is significantly more
   effective**, as preference judgements often contain subtle distinctions in how
   instructions are interpreted and followed in the context of long conversations."
3. **Co-training, not sequential post-training.** "rather than running our own
   post-training after Gemini's standard post-training, we co-train with Gemini,
   meaning we mix our data directly with Gemini's SFT, RM, and RL stages." Stated
   benefit: no catastrophic forgetting of reasoning/multimodal/factuality/safety,
   and no persona conflict — because pedagogical responses are *conditioned on
   system instructions* rather than baked into the default persona.

**The strategic sentence** (R2 §1, quoting feedback from >20 follow-up interviews
with EdTech companies, schools, NGOs and governments): `VENDOR`

> "Post-hoc fine-tuning for each application can be effective in the short-term,
> but is impractical because of cost, maintenance, and rapidly improving base
> models. Thus, **despite its shortcomings, prompting will likely remain the best
> way for education product developers to specify behavior.**"

Google wrote that in December 2024. Everything that followed — the fold into
Gemini 2.5, Guided Learning as a product layer, "no fine-tuning required" on the
Cloud page — is the execution of that sentence.

### 3.3 The most damning number in the corpus, from Google's own 2024 report

R1 §3.3.2, comparing the SFT'd model to a *well-prompted* base model: `OBSERVED`

> "While M3 far outperformed PaLM 2.0 across many of our metrics, **the gap between
> M4 (which basically differs from M3 only in the base model it adapts) and prompt
> tuned Gemini 1.0 is much smaller.** Our ultimate goal may not be the creation of a
> new pedagogical model, but to enable future versions of Gemini to excel at
> pedagogy under the right circumstances."

The pedagogy-tuned model's advantage over a prompted general model was *shrinking
as the base model improved* — and Google said so 18 months before the fold-in. See
§7.

---

## 4. The evaluation methodology — and the honest answer to "did they measure learning?"

### 4.1 Who rated, and how (R2, the flagship evaluation)

Three-stage pipeline (R2 §3): `OBSERVED`

- **Stage 1 — Scenario bank.** 49 scenarios across core academic subjects, built in
  three phases: use-case elicitation from EdTech companies / institutions / Google
  product teams; template design; collaborative drafting by team members "including
  two with years of professional experience educating students and training
  teachers," reviewed for "clarity, completeness, correctness, and relevance to our
  pedagogical principles." Each scenario carries a subject, learning goal, learner
  persona, initial learner query, a conversation plan, grounding material, and
  **its own system instructions**.
- **Stage 2 — Conversation collection.** **N = 168** pedagogy experts "with advanced
  academic degrees and two or more years of experience as a tutor" role-play
  learners. Trained, quizzed, then paired-conversation protocol: same participant
  runs the same scenario with LearnLM and with one comparison system, order
  randomised, systems unlabelled, identical system instructions/grounding/initial
  query, **minimum 10 conversational turns** before ending.
- **Stage 3 — Pedagogical assessment.** A *separately recruited* pool of **N = 228**
  pedagogy experts (same credential bar) reads transcripts and applies the 29-item
  rubric plus the 5-item comparative rubric. Target: **three independent assessments
  per conversation pair.**

Volume: **2,360 conversations, 58,459 messages, 10,192 expert assessments.**
Analysis: Bayesian hierarchical regression with random effects for participant
and scenario, weakly informative priors, four chains × (1000 warmup + 2000
sampling), R̂ and ESS convergence checks, 95% HDI reported. Ethics: independent
review, Google DeepMind Human Behavioural Research Ethics Committee #23 011.

**Data-quality control worth copying:** the assessors' *first* rubric item is
about the human, not the model — "The student followed the instructions of their
'learner persona'." This catches conversations where the role-player broke
character. Result: the learner followed scenario instructions in **93.2%** of
transcripts (R2 Appendix A.2).

> ⚠️ **Internal inconsistency in R2.** §3 of the main text states N=186 (stage 2)
> and N=248 (stage 3); §3.2 and §3.3 of the same paper state N=168 and N=228. I
> report the section-level numbers. This is unresolved in v3 and I flag it rather
> than pick one.

### 4.2 Inter-rater reliability — the number Google published once and never again

**This is the finding of this section.** R1 Appendix (turn-level ratings) reports
Krippendorff's alpha per pedagogical dimension: `OBSERVED`

| Dimension | α (LearnLM-Tutor) | α (Gemini 1.0) | Turns (LLM-T / G1.0) |
|---|---|---|---|
| Explains concepts | **0.657** | 0.655 | 274 / 369 |
| Promotes engagement | **0.663** | 0.554 | 331 / 259 |
| Identifies successes | 0.434 | 0.467 | 104 / 76 |
| Guides student | 0.319 | 0.318 | 175 / 191 |
| Speaks encouragingly | 0.300 | 0.244 | 229 / 203 |
| Identifies mistakes | 0.278 | 0.231 | 24 / 16 |
| **Inspires interest** | **0.066** | **−0.006** | 201 / 216 |
| **Monitors motivation** | **0.023** | **−0.038** | 159 / 157 |
| **Identifies goal** | **0.031** | **−0.009** | 218 / 231 |
| **Overall** | **0.359** | **0.325** | 1595 / 1570 |

Read that bottom block again. On *inspires interest*, *monitors motivation*, and
*identifies goal* — three of the nine moves, spanning two of the five principles —
**trained pedagogy experts agreed with each other at approximately chance, and in
Gemini 1.0's case slightly worse than chance.** Two of the five LearnLM principles
("stimulates curiosity", "adapts to the learner") rest substantially on constructs
that credentialed raters cannot reliably identify in a transcript.

Google's own framing of this (R1): `OBSERVED`

> "Although Krippendorff (2018) discusses a possible threshold of α ≥ 0.80,
> ultimately no universal recommendation is made (p. 241–242). Our Krippendorff's
> alpha is similar to the values reported in similar experimental conditions in
> literature [Glaese et al. 2022: α=0.37 general harm rule, α=0.53 specific harm
> rules]."

That defence is legitimate for a *safety* rubric where you only need to detect a
violation. It is much weaker for a *quality* rubric whose whole purpose is to rank
systems on a continuous scale.

**And then it disappears.** I searched R2, R3 and R4 for `krippendorff`,
`inter-rater`, `interrater`, `agreement`, `reliability`. **R2 and R3 report no
inter-rater reliability statistic at all.** R2 says only that it "aimed to collect
three independent assessments … to reduce the effects of interrater variability."
R4 mentions "reliability" only in the MCMC-convergence sense. The one report that
does compute IRR after R1 is **R5 (Sierra Leone), and only for the *qualitative
teacher focus-group codebook*** — where it obtained **α = 0.69** and correctly
described the procedure as a *simulated* IRR, since thematic analysis does not
normally admit one.

`INFERENCE` The programme measured the reliability of its central instrument once,
got a number that would not pass in most social-science venues, published it
honestly, and then stopped reporting it. Every win rate in R2 and R3 sits on top
of that unreported α.

### 4.3 Comparison models and win rates

**R2 (Dec 2024)** — LearnLM (2024-11-19, based on gemini-1.5-pro-002) vs.
contemporaneous flagships as of 2024-10-01: GPT-4o (2024-08-06), Claude 3.5 Sonnet
(2024-06-20), Gemini 1.5 Pro (2024-09-24). `OBSERVED`

| Comparison | Average preference strength for LearnLM |
|---|---|
| vs. GPT-4o | **+31%** |
| vs. Gemini 1.5 Pro (its own base) | **+13%** |
| vs. Claude 3.5 Sonnet | **+11%** |

Rubric-level: LearnLM scored highest across **all** rubric categories and "almost
all 29 rubric questions", with the largest leads on **inspiring active learning,
deepening metacognition, and stimulating curiosity** — note that two of those three
are precisely the categories with near-zero rater agreement in R1.

Conversation stats (R2 Fig. 3): LearnLM 11.0 turns/conversation, **174 words/turn**;
Gemini 1.5 Pro 10.3 / 130; GPT-4o 10.1 / 137; Claude 3.5 Sonnet 9.7 / 179. The team
reports "no clear relationship between length and perceived quality" in aggregate.

**R3 (May 2025) — the "arena for learning."** Gemini 2.5 Pro (2025-05-06, default
thinking) vs. Claude 3.7 Sonnet (2000-token thinking budget), OpenAI o3 (medium),
ChatGPT-4o, GPT-4o (2024-08-06). N=189 educators produced 2,666 interactions in
1,333 head-to-heads; N=206 experts produced 4,306 assessments (avg 3.2 per
match-up); 25-item rubric; Elo via Bradley–Terry on "Which tutor demonstrated
better tutoring?" `OBSERVED`

| Match-up | Gemini 2.5 Pro win rate (ties excluded) |
|---|---|
| vs. GPT-4o | **81.8%** |
| vs. OpenAI o3 | **74.2%** |
| vs. Claude 3.7 Sonnet | **71.3%** |
| vs. ChatGPT-4o | **61.0%** |
| Overall (all match-ups) | **73.2%** |

Per-principle (on the −3.0…+3.0 scale, reported as % of maximum): manages cognitive
load 82.1% (+2.0), inspires active learning 84.4%, deepens metacognition 82.8%,
stimulates curiosity 82.9%, adapts to learner 82.0%.

Targeted evals in R3: **text re-levelling** (Gemini 2.5 Pro grade-deviation 0.99 vs
1.74 ChatGPT-4o, 2.11 Claude 3.7, 2.44 o3, 2.54 GPT-4o; coverage 0.94);
**short-answer grading** against Ghanaian Ministry of Education rubrics on 2,000
real student answers via partner Milgo/T-Tel (Gemini 2.5 Pro and ChatGPT-4o tied at
84.1%; o3 83.3%; Claude 3.7 80.8%; GPT-4o 76.3%); **mistake identification** on Khan
Academy's public benchmark (Gemini 2.5 Pro 87.4% overall / 93.1% on correct answers
/ 80.1% on wrong; Claude 3.7 85.8%; o3 83.0%; ChatGPT-4o 79.6%; GPT-4o 78.4%).
`MEASURED-BENCH (vendor-run)` R3's own comment on the last: "we observed relatively
narrow gaps among the best-performing models, suggesting the need for
more-challenging benchmarks on mistake identification."

### 4.4 THE NEGATIVE RESULT: the learners did not agree with the experts

**Twice, in two separate reports, the people who actually had the conversation
reported no meaningful preference — and only the third-party experts did.**

R2 Appendix A.1: `OBSERVED`

> "The participants role-playing as learners revealed a preference toward LearnLM
> over GPT-4o for all four comparative assessment categories… **These participants
> indicated no substantial preference between LearnLM and Gemini 1.5 Pro or between
> LearnLM and Claude 3.5 Sonnet.**"

So the headline "+11% vs Claude, +13% vs Gemini 1.5 Pro" is a **third-party-observer
effect**. From inside the conversation, LearnLM and Claude 3.5 Sonnet and its own
base model were indistinguishable.

R3 reproduces it exactly: "**When educators directly interacted with the models and
role-played as students, Gemini 2.5 Pro and ChatGPT-4o tied for first in terms of
supporting learning goals.** … However, a different picture emerged when a pool of
experts independently reviewed those same interactions."

Google's interpretation is the correct one and they say it plainly: "what students
find immediately helpful often diverges from what is pedagogically sound," with the
best single quote in the corpus — an educator on ChatGPT-4o: **"As a lazy student,
I'd have loved it. As a tutor, not good at all!"**

`INFERENCE` But there is a second reading Google does not offer, and it is the one a
builder must hold: **the win is measured by the population that shares the rubric's
theory of pedagogy.** Third-party experts read a transcript and score form. A
learner in the conversation experiences effect. When those two diverge, the rubric
is measuring form. That is not proof the rubric is wrong — but it means the rubric
cannot be validated by learner preference, and Google never validated it against
anything else in R1–R3.

### 4.5 So: did LearnLM measure learning, or pedagogical plausibility?

**Direct answer: R1, R2 and R3 measured pedagogical plausibility only. R4 and R5
measured learning. The famous evaluations are the plausibility ones.**

The authors say it themselves. R2 §5, Conclusion — **this is the authors' own
stated limitation the brief asked for, and it is the load-bearing one:** `OBSERVED`

> "Second, we would like to start moving from **intrinsic evaluations**, which measure
> the model's performance according to a predefined pedagogy standard, to
> **extrinsic evaluation**, which measure impact such as learning outcomes. …
> However, while the core principles of our rubric, such as encouraging active
> learning and managing cognitive load, are broadly agreed upon and evidence-based,
> **it is unclear how well the results translate to improvements in learning
> outcomes.**"

And R2 immediately before that: "Although learning science principles underlie our
current pedagogy rubric, **we need to work more closely with a diverse set of
stakeholders to make sure it is appropriate for all learners and achieves the trust
and approval of the broader education community.**"

And R3 §4: "**A crucial question remains: do these pedagogical capabilities translate
to concretely better learning outcomes for students?**"

Two further points of precision:

- **The ASU Study Hall deployment (R1 §7) is not an outcome study.** 113 learners in
  CSE 110 opted in to "HallMate"; **74 actually used it**; evidence = **10
  semi-structured interviews**. No assessment, no control group. Findings were
  qualitative and included a red flag: **5 of 10 interviewees "felt they needed to
  fact-check HallMate or that its responses were not trustworthy."**
- **The "no regression" checks are the only quantitative outcome-adjacent numbers in
  R1–R3**, and they measure *accuracy*, not learning.

D1's finding therefore survives contact with the primary sources, in a sharpened
form: **LearnLM's flagship evaluation is the most rigorous *rubric* in the field and
still has no human learning outcome as its dependent variable.** What changed
between D1 and D3 is that Google *did* eventually run two studies that do — R4 and
R5 — and neither of them is the evaluation that the "+31% / 73.2%" numbers come
from.

---

## 5. The Eedi RCT (R4) — the study D1 did not have, and the one builders should read

`MEASURED-RCT` arXiv 2512.23633v1, "LearnLM Team Google, Eedi", submitted
2025-12-29; trial ran **May–June 2025**; **N = 165** students, Years 9–10 (ages
13–15), **five UK secondary schools**.

**Design.** Two-level randomisation on the Eedi maths platform. When a student
answers the first question of a study unit wrong, they get a support intervention:
randomised to (a) a **pre-written static hint** targeted at their specific
misconception, or (b) an **interactive chat tutoring session**. Within (b), a second
randomisation: **human expert tutor alone**, or **LearnLM drafting under human tutor
supervision** — with the tutors held to the standard "revise each of LearnLM's drafts
until they were satisfied sending the message as their own." Bayesian estimation
throughout (rstanarm, 4 chains × 2000, R̂ < 1.01).

**Results.** `MEASURED-RCT`

| Outcome | Static hint | Human tutor | LearnLM (supervised) |
|---|---|---|---|
| Correct on 2nd attempt, same question | 65.4% [63.8, 66.9] | 91.2% [88.5, 93.6] | **93.0% [90.4, 95.3]** |
| Misconception resolved (any post-intervention question) | 86.8% [85.7, 88.0] | 94.9% [92.6, 96.8] | **95.4% [93.1, 97.1]** |
| **Transfer: first question of the *next* study unit** | 56.2% [54.2, 58.2] | 60.7% [55.8, 65.4] | **66.2% [61.1, 71.2]** |

Transfer delta LearnLM − human = **+5.5 pp, 95% CrI [−1.4, +12.4]** — i.e. **the
credible interval includes zero**; the authors report "high credibility (93.6%)"
under their Bayesian framing rather than a significance claim. That is an honest
presentation, but a frequentist reader should treat the headline transfer result as
suggestive, not established.

**Safety/reliability audit.** 3,617 LearnLM-drafted messages. Tutors accepted
**74.4% with no edits at all** (the abstract's 76.4% is "zero or minimal edits",
where minimal = 1–2 characters, "virtually always … a tutor deleting or changing an
emoji"). Median intervention altered 59 characters. Post-hoc systematic review:
**zero instances of harmful or risky content; five factual errors = 0.1% of 3,617
messages.**

**Why tutors edited (the 25.6%) — the most useful failure taxonomy in the corpus:**

- **44.3% of all edits: moderating pedagogical pacing** — i.e. stopping LearnLM from
  Socratically questioning a student past their patience. Raised in **5 of 5**
  interviews. "[LearnLM] will go, 'Okay, you've got the answer. Let's dig a little
  deeper about why you've got that answer.' And the child is just like, 'No, I've
  got it. I know what I'm doing. Can I go now?'" (T1)
- **19.5%: persona/tone and social-emotional nuance** — adding continuity the model
  had no access to ("if you'd already helped that student twice before, [LearnLM]
  didn't quite have the capability to go like, 'Oh Sarah, it's you again. Hi!'",
  T3), and removing emoji ("comes across as a bit fake, and […] the students pick up
  on that", T1).

**Authors' own stated limitation** (R4 §4): "this design offers only a partial glimpse
at the broader trajectory of learning. Randomizing the source of tutoring
session-by-session … **prevented it from isolating the cumulative impact of working
with LearnLM over time.** … If tutors applied those insights in sessions without
LearnLM, **that crossover might dampen the measured difference between the two
tutoring conditions.**" And on generality: "**LearnLM's performance in this trial
offers limited evidence for its ability to shepherd students through more
interpretive activities in fields like history or literature.**"

**Two things I could not verify:** R4 makes **no mention of pre-registration** (I
searched for `preregist`, `pre-regist`); and the throughput/efficiency claim is
explicitly not measurable from the design — the authors say so and fall back on a
post-hoc simulation in Appendix H.

**The actual production system prompt is published** (R4 Appendix D.1) — this is
rare and directly copyable. Highlights, verbatim:

```
Act as a mathematics tutor named {BotName} who is currently helping a student
named {FirstName} with the activity below in a clipped, Socratic style.
# Directives
- Do not let students know you are a bot, you are {BotName} the tutor.
- No LaTeX or markdown. Plaintext only. Even if the question has latex in it.
- Use short, focused sentences.
- Ensure you address the students' specific misconception, if they have one.
- Keep it direct, concise and friendly. Try to keep messages short and to one line
  where possible.
- End session if the user is rude, they've resolved their misconception / guessed
  the correct answer, or finished.
- Only ask the student one question at a time.
- If the user asks to go, let them go!
- If a user knows the correct answer (e.g. "It's B)"), say you can return them to
  their lesson Or you can dig deeper to help them understand (in case they are
  guessing!)
- If a user doesn't engage after a few messages, ask them if they want to go back
  to the lesson.
# The Current student activity … # Activity details … # Students ability level
# Examples of good Socratic responses  [~15 verbatim exemplars]
## Checking understanding …  ## Closing remarks …  ## Rudeness …
# Important response guidelines
- Do not use the word "bot" or "AI" in your responses.
- Do not give the student the answer.
```

Adaptivity is **injected as two lookup-table directives**, not learned:

| Year group | Directive |
|---|---|
| Year 9 | Discuss more abstract ideas and build logical arguments. |
| Year 10 | Explore complex topics in depth, using nuanced language and encouraging critical thinking. |

| Predicted quiz score | Directive |
|---|---|
| ≥ 80% | The student is predicted to do well. Help with more advanced concepts. |
| ≥ 60% | The student is predicted to do okay. Check for understanding of core concepts. |
| ≥ 50% | The student is predicted to struggle. Help with core concepts using simple explanations. |
| < 50% | The student is predicted to really struggle. Use brief, simple language. |

> ⚠️ **Ethics flag, mine not theirs.** "Do not let students know you are a bot",
> "Do not use the word 'bot' or 'AI' in your responses", and the scripted "please
> remember you are speaking to a real person!" are **instructions to deceive
> 13–15-year-olds about whether they are talking to a human.** In this trial a human
> tutor did approve every message, so the claim was arguably literally true — but the
> prompt as written is not conditional on that. The authors do not discuss it. Any
> builder copying this prompt must strip those three lines. Cross-reference the
> project's SELPA/children-safety constraints (H1, F8).

---

## 6. The Sierra Leone RCT (R5) — full design, subgroups, and what it can and cannot attribute

`MEASURED-RCT` `deepmind-media/LearnLM/learnLM_sierraleone_may26.pdf`, dated
**2026-05-15**. "LearnLM Team, Google & Fab AI." Pre-registered: **AEA RCT Registry
AEARCTR-0016651** (registry entry itself not fetched — flagged). Ethics: Sierra
Leone Ethics and Scientific Review Committee **No. 007/09/2025** + Ministry
authorisation; parental consent, teacher consent, student assent.

### 6.1 Design

- **Two-arm cluster RCT**, **classroom** as cluster, **blocked (stratified) by
  school × grade**. 12 government-supported junior secondary schools, **Port Loko
  District**. **N = 1,763** students aged ≥13, **48 classrooms** (16 grade 7, 32
  grade 8). Allocation: 9 G7 + 15 G8 treatment; 7 G7 + 17 G8 control.
- **Intervention ran 6 Oct – 5 Dec 2025** (nine calendar weeks for an eight-week
  dose, staggered starts). Requested dose: Guided Learning in **2 of 4** weekly maths
  periods = **90 min/week = 12 h total.**
- **Model:** Gemini app, Guided Learning, **Pro** tier. Students hit **Gemini 2.5 Pro
  for the first six weeks and Gemini 3.0 Pro for the final three** — a mid-trial model
  swap the authors chose deliberately ("As Gemini improved, students and teachers
  simply used the latest version available, just like any classroom would").
- **Devices:** tablets/desktops at **2:1 student-to-device**, with explicit
  **driver/navigator pair-programming roles that swap each lesson**.
- **Teacher-led four-part lesson structure**: (1) teacher introduces learning
  objectives and checks prior knowledge; (2) students work in pairs with Gemini;
  (3) whole-class consolidation discussion; (4) plenary summary. Teachers had to
  **pre-write the starter prompts students would type** and **draft question stems on
  the chalkboard as scaffolds**, and were trained to embed grade level and Sierra
  Leone context into prompts.
- **Training:** cascade model — 5 h to EducAid trainers, who then trained all
  teachers in a single 5–6 h day. **Crucially, training happened *before*
  randomisation, so control teachers received identical training.**
- **Measurement insulation:** **Oxford MeasurEd** wrote and scored curriculum-aligned
  maths assessments (half on intervention-period content, half on broader/earlier
  curriculum) plus a **baseline English reading assessment**, and applied **IRT to
  pooled data without access to treatment assignment.** **Laterite** collected data,
  separate from **EducAid** who implemented. This modular partner structure is the
  single best design feature and is explicitly justified in the playbook as
  "institutional insulation".
- **Fidelity/spillover:** one field monitor stationed at each of the 12 schools for
  the whole trial, instructed to stay *outside* classrooms except for technical
  fixes. **Documented spillover: two isolated incidents** of a control student sitting
  in on part of a lesson.

### 6.2 Results

**Uptake:** 69.0% of the 871 treatment students hit the 12-hour threshold; treatment
classrooms averaged **~15 h (25% above requested)**.

**Overall effect (Table C.4):**

| Specification | Estimate | SE | p |
|---|---|---|---|
| (1) Unadjusted | **0.216** | 0.137 | **n.s.** |
| (2) Baseline-adjusted (ANCOVA) | **0.258** | 0.115 | 0.029 |
| (3) Fully adjusted (+ gender, age) | **0.259** | 0.116 | 0.031 |
| Diff-in-diff (Table C.5) | 0.317 | 0.146 | <0.05 |

> **Read specification (1).** The **unadjusted ITT is not statistically
> significant.** The headline +0.258 SD requires ANCOVA adjustment for baseline
> score. That is a completely standard and pre-registered analysis choice, and the
> DiD estimate corroborates it — but "+0.258 SD" is a covariate-adjusted estimate,
> not a raw arm difference, and no press coverage of this trial says so.

**Dosage (ToT, treatment assignment as instrument):** +0.016 SD per hour
(95% CI [0.002, 0.031], p=0.026); **completing the requested 12 h: +0.380 SD**
(95% CI [0.040, 0.719], p=0.029). Note the CI lower bound of 0.040 — the 12-hour
effect is compatible with being nearly zero.

**Heterogeneity (Tables C.10–C.15):**

| Moderator | Interaction with treatment | Verdict |
|---|---|---|
| **Baseline maths score** | **+0.195 SD per SD** (95% CI [0.074, 0.315], p=0.002) | **Strong. Gaps widen.** |
| **Grade** | Grade 8 × treatment **+0.429** (p<0.01); Grade 7 main effect **−0.078** (p<0.05) | **Strong. Effect is essentially a Grade-8 effect.** |
| Baseline reading | −0.027 (n.s.) | No moderation |
| Pre-foundational readers (level 0) | −0.033 to −0.038 on 12 h dose (n.s.) | No moderation |
| Gender | +0.083 (n.s.); female main effect **−0.315** (p<0.01) | No moderation, large baseline gender gap |
| Age above expected for grade | +0.041 (n.s.) | No moderation |

The **grade interaction is the under-reported result**: in the baseline-adjusted
model, Grade 7's treatment coefficient is **negative and significant** (−0.078,
p<0.05) and the whole positive effect loads onto Grade 8 (+0.429). The blog posts
do not mention this.

**Attrition:** baseline N=1,547 → 124 dropouts → balanced panel N=1,423; 214 new
entrants → endline N=1,637. Follow-up rate 90.7% control vs **93.3% treatment**, and
**Table C.3 shows treatment assignment significantly predicted retention (+0.032,
p<0.05)** — i.e. **differential attrition favouring treatment**. Baseline maths also
predicted retention (+0.021, p<0.05). This is a real, small threat to internal
validity that the report presents but does not discuss in prose.

**Baseline imbalance:** control mean maths 0.086 (SD 0.860) vs treatment −0.081
(SD 0.837) — a **0.167 SD gap favouring control** at baseline. ANCOVA handles it, but
it is why specification (1) and (2) differ.

**Pre-registration deviation, stated by the authors** (R5 §C.2): `OBSERVED`

> "Our pre-analysis plan specified the estimation of treatment and dosage effects on
> five mathematics subdomains … **We ultimately did not conduct these analyses; in
> retrospect, the assessment contained too few items per subdomain for IRT scoring to
> produce stable subdomain-level estimates.**"

They also swapped the pre-specified per-grade separate regressions for a single
interaction model (stated in Table C.14's note). Both are disclosed. Good practice —
and a reminder that "pre-registered" is not "un-deviated-from".

### 6.3 The conversation coding — and the fatal disconnect

Coded with **Gemini 3.1 Flash-Lite** on de-identified transcripts, threads split into
conversations by a 20-minute inactivity gap. Two taxonomies: student *goal
orientation* (Wigfield & Cambria) at conversation level, weighted by length; and
Gemini *tutoring moves* (Chi et al. 2001) at message level.

| Measure | Overall | Week 1 | Final week |
|---|---|---|---|
| Messages / conversations | 113,344 / 7,421 | 5,241 / 458 | 6,821 / 382 |
| On-topic (length-weighted) | **97.4%** | 98.1% | 98.0% |
| Student **skill-seeking** | **91.4%** | 67.7% | 91.7% (peak 98.0% wk of 24–30 Nov) |
| Student **solution-seeking** | **5.0%** | 25.1% | 6.3% (trough 1.0%) |
| Gemini **scaffolding questions** | **76.4%** | 64.2% | 74.2% (peak 80.9%) |
| Gemini **direct solutions** | **2.1%** | 7.0% | 2.2% (trough 0.4%) |

The trajectory is the interesting part: solution-seeking **fell from 25.1% to ~5%**
over eight weeks. That is a behavioural change in the students, not the model.

**But — and this is decisive for the brief's central question** (R5 §B): `OBSERVED`

> "Both because students shared tablets in pairs and because different pairs used the
> same device across lessons, **we could not link transcripts to individual students'
> assessment outcomes.**"

**So the pedagogical-quality coding and the learning outcome are statistically
disconnected in the only trial that has both.** The 91.4% / 76.4% / 2.1% numbers
describe what happened in the conversations; the +0.258 SD describes what happened on
the test; and **nothing in this study links them.** No dose-response of scaffolding on
score, no mediation, nothing. The authors know it and commit to fixing it: "we intend
to move our future trials beyond aggregate analysis and **link specific tutoring moves
and student experiences directly to learning outcomes**."

Until someone does that, "91.4% concept-building" is a **process metric that has never
been shown to predict the outcome metric it sits next to.**

### 6.4 What the trial cannot attribute — stated by the authors

R5 §Reflections: "**the intervention in this trial is not a technological fix. It is
an integrated approach that weaves together pedagogical structure, teacher design and
direction, peer interactions between students, and pedagogical AI.**"

The accompanying **RCT Playbook** (`learnLM_sierraleone_playbook_jun26.pdf`) is
blunter, and this is the most important methodological admission in the entire D3
corpus: `OBSERVED`

> "In an ideal setting with unlimited resources, multiple control arms could isolate
> distinct causal contributions—for example, **paired practice without AI to identify
> the benefits of the collaborative structure alone, or interaction with a
> general-purpose AI system to isolate the effect of the learning science insights
> incorporated into Guided Learning.** However, each additional arm requires a
> disproportionately larger sample… a two-arm RCT was selected to estimate the
> aggregate effect of the **full intervention package**."

The counterfactual was **business-as-usual instruction**. So the +0.258 SD is the
combined effect of: tablets · a 2:1 pair-work protocol with driver/navigator roles ·
a teacher-authored four-part lesson structure · teacher-written starter prompts ·
chalkboard scaffolds · 5–6 h of teacher PD (which control teachers also got) ·
novelty/Hawthorne · **and** Guided Learning's pedagogy. **There is no arm that isolates
the pedagogy layer.** By the authors' own framing, this trial does not measure Guided
Learning; it measures a classroom programme that contains Guided Learning.

### 6.5 Other author-stated limitations and negative findings

- "**In this trial, studying with Gemini conferred the greatest benefits to students
  who started with strong mathematics skills. This is a common pattern in educational
  technology: new tools frequently widen achievement gaps rather than close them.**
  But our ambition is the opposite… **The latter will not come for free from improving
  AI capabilities like accuracy, explanation, or personalization.**" — This is the
  cleanest published statement anywhere that capability scaling will not solve the
  equity problem. `OBSERVED`
- Teacher-reported barriers surfaced in focus-group coding (7 themes, 43 codes,
  simulated α=0.69): **literacy gaps**, **foundational knowledge gaps**, **limited skills
  with technology**, **verbosity of content created by Gemini**, **inconsistent responses
  from Gemini across the classroom**, **Gemini introducing content from outside the
  intended lesson**, **Guided Learning sessions disrupting the planned class
  curriculum**, **off-task distractions**, **need for audio outputs**, **Gemini responses
  fall short of cultural expectations**, **teacher burden from student questions during
  Guided Learning lessons**, **internet and power reliability**, **security concerns with
  tablets**, and **general misconceptions of AI** ("And I came to understand that ChatGPT
  is the only AI").
- **The strongest qualitative signal is not about students at all.** "Use of Gemini for
  lesson preparation" was raised by **13 of the teachers** and "Professional learning
  from Gemini use" by **12** — the two most-cited codes in the study, ahead of any
  student-facing code. `INFERENCE` In a system where "qualified teachers remain scarce",
  the teacher-capability channel may be doing more work than the student-tutoring
  channel, and this design cannot separate them either.

---

## 7. Guided Learning — what is documented, and what is not

**What Google says it does** (blog.google, **2025-08-06**, Maureen Heymans, "Guided
Learning in Gemini: From answers to understanding"): `VENDOR`

> "Guided Learning **encourages participation through probing and open-ended questions**
> that spark a discussion and provide an opportunity to dive deeper into a subject."
> "Guided Learning **breaks down problems step-by-step and adapts explanations to your
> needs** — all to help you build knowledge and skills."
> "Guided Learning provides **rich, multimodal responses — including images, diagrams,
> videos and interactive quizzes** — that can help you build and test your knowledge."
> Built on "the core principle that **real learning is an active, constructive
> process**."

**The Sierra Leone playbook's operational description** is tighter: `OBSERVED`

> "Guided Learning — a tool in the Gemini app **built to act as a teacher rather than
> an assistant.** Instead of giving away the answer, Guided Learning invites the learner
> to actively engage in a conversation, **breaking down the problem into smaller chunks
> and scaffolding the learner to do the work themselves, encouraging productive
> struggle and avoiding cognitive offloading.**"

**What is not documented, and I could not obtain:** `INFERENCE`

**The Guided Learning system instructions are not published anywhere.** I probed
`gemini.google/overview/guided-learning/` (404), `support.google.com/gemini/answer/…`
(404 on two candidate IDs), and `blog.google/.../guided-learning-back-to-school-2026/`
(404). `gemini.google/students/` renders but says only: "Gemini breaks down the
concepts and tricky problems behind your study materials, with step-by-step guides
that teach you the 'why' as well as the 'how.'" D1 reported the same 404 on the
support article; that is still true as of 2026-07-27. **The single most valuable
artifact — the prompt that produced +0.258 SD — is unpublished.**

The closest published proxies are (a) the **Eedi production prompt** in §5 above, which
is a real deployed pedagogical system instruction from the same team; and (b) the
**scenario system instructions in R2 Appendix B.3**, which are the eval-time
instructions the models were graded against. Two verbatim examples: `OBSERVED`

> "You are a tutor that excels in promoting active learning. Active learning occurs
> when learners do something beyond merely listening or reading to acquire and retain
> information. Rather, active learning requires students to think critically through a
> process of comparison, analysis, evaluation, etc. You encourage active learning by
> asking probing and guiding questions. / Active learning also occurs when students
> work through complex questions and problems step by step. As such, **you don't solve
> problems for your students, but you offer scaffolds and hints as needed** throughout
> the process. / Active learning can be difficult, and students may get frustrated.
> Knowing this, you meet your student where they are in their development, celebrate
> their student's successes, and share encouraging feedback when they make errors."

> "Begin each learning conversation with a brief overview of the topic shared in the
> student's initial query. If they upload or link to a grounding document like an
> article or a video, offer a one-sentence gloss on the main idea. Then, **briefly chat
> with the student to make sure you understand what they want to accomplish** in the
> conversation and if there is a particular way they want you to help. … Adapt to meet
> the needs of the student. **Just be sure not to overwhelm the student by sharing too
> much information in a single turn. Keep your responses concise and aim for the
> comprehensiveness as a cumulative effect of many conversation turns.** / Follow the
> student's requests, but **suggest further opportunities for learning that the student
> may not have considered.**"

That last clause — "comprehensiveness as a cumulative effect of many conversation
turns" — is the single best-phrased pedagogical instruction I found in the corpus.

**Note on R2's setting distinction** (R1/R2 scenario template, §B.2): system
instructions are handled differently by setting. In **"Classroom"** settings "the
system instructions come from the teacher or school, and the AI tutor should follow
the system instructions in the interaction **regardless of the student's** [requests]";
in **"Self-taught"** settings the instructions come from a third party and the tutor
"**also has leeway to defer to learner instructions in cases of conflict**." That is an
explicit, documented authority model — and it is exactly the design surface where
D1's C3 cluster (pedagogical jailbreaks, answer-leakage under student attack) lives.

---

## 8. Google's wider education research, checked

| Item | Status as of 2026-07-27 | Evidence |
|---|---|---|
| **Learn Your Way** (AI-augmented textbook) | arXiv 2509.13348v4, LearnLM Team. **Lab RCT, N=60** students aged 15–18, Chicago area, screened to ±1 SD on a reading-comprehension task. Same chapter (LibreTexts, "Brain Development for Adolescents") in Learn Your Way vs. **Adobe Acrobat Reader v25.001.20531**. 20–40 min study, 15-min immediate assessment, **3-day-delayed retention assessment** (58/60 completed). Learn Your Way higher on **both** (immediate **p=0.03**, retention **p=0.03**, Mann-Whitney U). | `MEASURED-RCT` (small) |
| ↳ Learn Your Way limitations, authors' own | "**Since Learn Your Way contains multiple components, including formative quizzes, a natural question is which of these contributes most to learning efficacy. Since the current study did not hone in on this, there might be some transformations that have impact while others do not.**" Also: single chapter, single topic. **And no effect size is reported in the text** — only p-values; the means are in a figure. | `OBSERVED` |
| **Socratic** (acquired 2018) | **Discontinued as an independent product.** `https://socratic.org/` now **301s to `https://lens.google/#homework`** (verified by following redirect, 2026-07-27). Folded into Google Lens Homework. | `OBSERVED` |
| **Read Along** | Live product (`readalong.google`). Reading-buddy "Diya", real-time speech feedback, 1000+ stories, 11 languages; partners Google.org, StoryWeaver, Room to Read, Global Book Alliance, African Storybook Initiative, Book Dash. **The product page cites no research, no RCT, no effect size, no usage statistic.** No arXiv record surfaced for a Read Along efficacy study. | `VENDOR` |
| **Khan Academy** | Named as a LearnLM pilot partner in the 2024-05-14 launch post, alongside **MIT RAISE, Columbia Teachers College, Arizona State University, NYU Tisch**. **No published joint evaluation, benchmark, or outcome study from the Google side.** (Khanmigo itself is OpenAI-based; that relationship is out of scope here.) | `VENDOR` |
| **ASU** | The Study Hall / HallMate deployment in R1 §7. 113 opt-ins, 74 users, 10 interviews, no outcome measure. | `OBSERVED` |
| **Project Genie** | I re-checked `deepmind.google/models/genie/`. The only "learns with you" link on the page goes to **SIMA 2**, an agent paper, not education. **D1's finding stands: no education use case is named for Genie.** | `INFERENCE` (absence) |
| **deepmind.google/education/** | Scholarships, fellowships, AIMS Pan-African AI-for-Science masters, Undergraduate Research Ready, **Experience AI** (free secondary AI-literacy curriculum, "educators in 180 countries", 19 languages), academic chairs. **No impact studies, no RCTs, no effect sizes on this page.** | `VENDOR` |
| **Nov 2025 commitments** (`blog.google/outreach-initiatives/education/ai-learning-commitments/`, **2025-11-11**) | **$30M over three years via Google.org**; Estonia "AI Leap" (20,000+ students/teachers); YouTube conversational AI in the UK; partners **Eedi, Estonia AI Leap Foundation, Raspberry Pi Foundation, Fab AI, Playlab, Digital Promise**. **Announces a programme of further RCTs in the U.S., UK, India, Sierra Leone "and beyond."** | `VENDOR` |
| **Third-party use of LearnLM as a judge** | arXiv 2506.17410 (Thomas, Borchers, Lin, … Koedinger — **CMU, not Google**) uses LearnLM alongside GPT-4/4o/turbo and Gemini-1.5-Pro to assess **real** tutor moves in 50 transcripts of college tutors helping middle-schoolers: 94–98% accuracy detecting praise situations, 82–88% detecting a student maths error, **83–89% / 73–77% agreement with human judgements** on adherence to best practice. | `MEASURED-BENCH` |
| **Independent replication of the capability** | arXiv 2505.15607 — online RL alignment on simulated student–tutor interactions trains a **7B tutor with no human annotations that "reaches similar performance to larger proprietary models like LearnLM."** | `MEASURED-BENCH` |

**Non-LearnLM RCT Google itself cites as prior art:** De Simone et al., *From
chalkboards to chatbots: Evaluating the impact of generative AI on learning outcomes
in Nigeria*, World Bank Policy Research Working Paper 11125 (2025) — cited as ref [9]
in R5. Not read in this pass; flagged for B2.

---

## 9. Why fold LearnLM into Gemini? The evidence, and what it means for builders

I can answer this almost entirely from Google's own words, in chronological order.
This is not reconstruction — it is a documented decision trail.

**Step 1 (R1, May 2024).** The team tries prompting first and rejects it: "**most
pedagogy is too nuanced to be explained with prompting**", "prompting produced
unreliable and inconsistent results". They turn to SFT. `OBSERVED`

**Step 2 (R1, same document, §3.3.2).** They immediately notice the ground moving:
"**the gap between M4 … and prompt tuned Gemini 1.0 is much smaller** [than M3 vs PaLM
2.0]. **Our ultimate goal may not be the creation of a new pedagogical model, but to
enable future versions of Gemini to excel at pedagogy under the right
circumstances.**" `OBSERVED` — *The exit is announced in the first paper.*

**Step 3 (R2, Dec 2024).** After 20+ interviews with the education sector, three
findings, all pointing the same way: (i) pedagogy "is prohibitively difficult to
define … and **it is best left to the developer or teacher to specify**"; (ii) what
customers actually want is reliable **instruction following**, "even if a student tries
to circumvent them"; (iii) "**Post-hoc fine-tuning for each application … is
impractical because of cost, maintenance, and rapidly improving base models. Thus,
despite its shortcomings, prompting will likely remain the best way for education
product developers to specify behavior.**" `VENDOR`

The reframe to **pedagogical instruction following** is the fold-in, executed as a
research programme. It is explicitly designed to make the pedagogy data
*mixture-compatible* with mainline Gemini post-training: "This framing … **clears a path
to improving Gemini models for learning — by enabling the addition of our pedagogical
data to post-training mixtures — alongside their rapidly expanding set of
capabilities.**"

**Step 4 (R3, May 2025).** LearnLM ships inside Gemini 2.5 Pro/Flash and the arena
paper's job is to show the merged model still wins (73.2%). `OBSERVED`

**Step 5 (2026).** `ai.google.dev/gemini-api/docs/learnlm`: "LearnLM is no longer a
separate listing in AI Studio." `cloud.google.com/solutions/learnlm` sells
"**Build and deploy enterprise-ready AI experiences for learning, no fine-tuning
required.**" The 2026 prompt guide: "we've fine-tuned it to follow pedagogical system
instructions. This means you can bring out behaviors like 'act as a supportive math
tutor' **without the need for additional fine-tuning by the developer or user**."
`VENDOR`

### 9.1 So: was the pedagogy-tuned model failing to beat a well-prompted general model?

**Partly — and Google said so, but the fuller story is a strategy change, not a
defeat.** Three strands:

1. **Direct evidence of a shrinking gap, from Google (R1 §3.3.2, quoted above).** The
   fine-tuning advantage over *prompted* base models was already "much smaller" for
   M4/Gemini-1.0 than for M3/PaLM-2.0. `OBSERVED`
2. **Independent evidence that the moat is thin.** arXiv 2505.15607 trains a **7B**
   tutor with online RL and no human annotations to "similar performance to larger
   proprietary models like LearnLM." `MEASURED-BENCH` And D1's 2605.27088 shows
   **training-free prompt optimisation beating RL-trained pedagogical baselines**
   outright.
3. **But the fold-in was not only about performance.** R2's own reasons are
   *maintenance* ("keep LearnLM in sync with Gemini as the training recipe evolves"),
   *capability preservation* (co-training avoids forgetting reasoning/multimodal/safety
   — a real cost of a separate pedagogy model), and *customer demand for
   specifiability* ("best left to the developer or teacher to specify"). A separate
   pedagogy model with a fixed pedagogy is the wrong product shape for a market where
   every customer wants a different pedagogy.

### 9.2 The claim the evidence supports — and the important qualification

**Supported:** for a builder without a training budget, **the pedagogical layer is
buildable in prompt space, on a frontier base model, and you are not structurally
disadvantaged versus a lab.** This is not inference from vibes; it is:

- Google's own stated conclusion that prompting "will likely remain the best way for
  education product developers to specify behavior" (R2);
- Google's own commercial framing: "no fine-tuning required" (Cloud, 2026);
- the mechanism they built to make it true: **post-training that specifically teaches
  the model to follow pedagogical system instructions**, so your prompt lands on
  receptive weights;
- two independent results (2505.15607, 2605.27088) showing cheap methods matching or
  beating expensive ones;
- and a **deployed pedagogical system prompt, published in full** (R4 Appendix D.1),
  which produced a measured learning outcome under human supervision.

**The qualification, which the evidence forces.** The +0.258 SD in Sierra Leone was
produced by a *product surface plus a classroom programme*, not by a prompt; and the
Eedi transfer effect was produced by a prompt **plus a human tutor editing 25.6% of
messages, 44.3% of those edits fixing pacing the prompt got wrong.** In both trials
with a real outcome, **the human structure around the prompt is doing visible work,
and no design isolates the prompt's contribution.** "Pedagogy is a prompt layer" is
well-supported as a statement about *where the leverage is available to you*. It is
**not** supported as a statement that a prompt alone produces learning gains — nobody
has published that, including Google.

---

## 10. Deliverables

### (a) The rubric, as something you can apply on Monday

Use the 25-item, five-principle instrument in §2 with these five protocol rules,
each of which is a real design decision from the papers:

1. **Rate the conversation, not the turn**, on a **seven-point** agreement scale.
   Turn-level is cheaper and needs less expertise, but R1 states plainly that "not
   everything can be judged at turn-level."
2. **Offer "Not applicable" and force a reason.** Without it, "Adapts to affect" is
   scored against tutors whose students never became frustrated.
3. **Separate the person who has the conversation from the person who scores it.**
   R2/R3's whole design rests on this — and §4.4 is why: the two populations disagree.
4. **Score the *human* first.** Item zero is "the learner followed their persona."
   Discard transcripts that fail it (R2 kept 93.2%).
5. **≥3 independent raters per item**, and **report Krippendorff's α per dimension.**
   If your α on "stimulates curiosity" looks like Google's (0.066), that item is not
   measuring anything and you must either re-word it or delete it. **Do not do what
   the programme did and stop reporting α after the first paper.**

Two rubric-design points to carry over: keep the **self-cancelling pairs** (Guides to
answer ↔ Guides appropriately) so over-Socratism is penalised, and keep the
**two-step turn-level form** ("should it? / did it?").

### (b) Did LearnLM measure learning, or pedagogical plausibility? — the honest answer

**Both, in different papers, and the famous numbers are the plausibility ones.**

- **R1, R2, R3 measured pedagogical plausibility.** Zero learning outcomes. The
  dependent variable is always an expert's agreement with a statement about a
  transcript. Google states this in R2's conclusion in the strongest possible terms:
  "**it is unclear how well the results translate to improvements in learning
  outcomes.**" The "+31% over GPT-4o" and "73.2% win rate" numbers are *not* claims
  about learning and were never presented as such by the authors.
- **The plausibility instrument is not fully reliable.** Two of the five principles
  rest on dimensions where credentialed experts agreed at ~chance (α ≈ 0.02–0.07).
- **The plausibility instrument does not track learner experience.** Twice, in two
  reports, role-playing learners saw no meaningful difference where third-party
  experts saw a clear one.
- **R4 (Eedi) measured learning** — immediate correction, misconception resolution,
  and **transfer to the next topic** — and got a positive transfer signal (+5.5 pp,
  CrI crossing zero, 93.6% posterior credibility). **But LearnLM was human-supervised
  throughout**, so this is a measurement of *LearnLM + expert tutor*, not LearnLM.
- **R5 (Sierra Leone) measured learning** properly — pre-registered, cluster-randomised,
  blocked, IRT-scored by an insulated third party — and got **+0.258 SD (ANCOVA;
  unadjusted 0.216, n.s.)**. **But the counterfactual was business-as-usual**, the
  package included tablets/pair-work/teacher-designed lessons/PD, the authors state
  they could not isolate Guided Learning's contribution, **and the transcripts could
  not be linked to individual outcomes** — so even here, pedagogical quality and
  learning are measured in the same study but never joined.

**Verdict.** LearnLM built the field's best instrument for pedagogical plausibility
and has been transparently, publicly honest that it does not know whether that
instrument predicts learning. Its two outcome trials are real and are the best
evidence any lab has published — and neither of them validates the rubric. **D1's
central finding holds: as of 2026-07-27, no public evaluation links a pedagogical
quality score to a human learning outcome. Google has come closest, said so, and
committed to closing the gap in future trials.**

### (c) Copy / discard

**Copy:**

1. **The five-principle, 25-item rubric with the N/A-with-reason mechanic.** It is
   free, complete, and better than anything you would write.
2. **The two-stage eval separation** (role-players ≠ scorers) and the **scenario bank**
   as the unit of coverage: subject × learning goal × learner persona × grounding
   material × conversation plan × system instruction, ≥10 turns minimum.
3. **Score your role-players' fidelity as item zero.**
4. **The LLM-critic design where the judge gets privileged information the tutor did
   not have** (the correct answer, the misconception label). This is the reason
   auto-eval works here at all.
5. **The Eedi prompt architecture** — a short directive block, then ~15 *verbatim
   exemplar responses* grouped by situation (Socratic / checking understanding /
   closing / rudeness), then two lookup-table directives for level and predicted
   performance. Concrete exemplars over abstract instruction. Minus the deception
   lines.
6. **"Aim for comprehensiveness as a cumulative effect of many conversation turns."**
   One sentence; it is the whole anti-wall-of-text discipline.
7. **The Sierra Leone partner architecture** — implementation, data collection, and
   assessment design in three *separate* organisations, with the psychometrician
   blind to arm. If you ever run a trial, this is how you buy credibility.
8. **The four-part teacher-led lesson wrapper and driver/navigator pairing.** The one
   published intervention with a real effect size wrapped the AI in exactly this. Do
   not ship a bare chatbot into a classroom.
9. **The "productive struggle vs. exasperation" dial as an explicit, tunable
   parameter**, and instrument it. Google walked it back once (R1 §5.5) and human
   tutors spent 44.3% of their edits walking it back again (R4).

**Discard:**

1. **The belief that a pedagogy-tuned model is a moat.** Google's own numbers show the
   gap to a prompted base model shrinking; a 7B RL model matches it; prompt
   optimisation beats RL baselines. Build the layer, don't buy the model.
2. **Rubric items with near-zero inter-rater reliability** — "monitors motivation",
   "identifies goal", "inspires interest" as *turn-level* judgements. Either
   operationalise them into observable behaviours (did the tutor ask what the learner
   already knows? — binary, checkable) or drop them.
3. **"Always Socratic."** Both outcome trials show it failing at the margin.
   "Guides appropriately — the tutor does not withhold information unproductively" is
   in the rubric for a reason.
4. **Expert-panel preference as your primary metric.** It is expensive, it has
   unreported reliability, and twice it disagreed with the people in the conversation.
   Use it as a development signal (as Google does) and instrument outcomes as truth.
5. **Deception directives** ("do not let students know you are a bot"). Legally and
   ethically indefensible for minors without the human-in-the-loop that made it
   arguably true in the Eedi trial.
6. **Treating conversation-coding percentages as evidence of impact.** 91.4% / 76.4% /
   2.1% are beautiful numbers that have never been shown to predict a test score — in
   the very study that reports both.

---

## 11. Explicitly could not verify / did not obtain

- **The Guided Learning system instructions.** Not published. Four candidate URLs
  404'd (§7). The prompt that produced the only frontier-scale education RCT result is
  unavailable.
- **AEA RCT Registry entry AEARCTR-0016651.** Cited in R5; I did not fetch the
  registry record, so I cannot independently confirm the pre-registered primary
  outcome or verify the two disclosed deviations against the original filing.
- **`learnLM_nov25.pdf` and `learnLM_sierraleone_teacher_training_jun26.pdf`.** URLs
  confirmed live on the Cloud page but not read in this pass. `learnLM_nov25.pdf` is
  almost certainly the PDF of R4 (Eedi), which I read in full on arXiv.
- **Learn Your Way effect sizes.** Only p-values (0.03 / 0.03) appear in the text;
  means and SDs are in figures I could not extract from HTML.
- **R2's participant-count inconsistency** (186/248 in §3 vs 168/228 in §3.2/§3.3) is
  unresolved in v3.
- **Whether R4 (Eedi) was pre-registered.** No statement in the paper; I searched for
  it. Reported as absent, not as confirmed-absent.
- **OpenAlex, Semantic Scholar.** Both returned sustained HTTP 429 across this
  session. The publication sweep is from the arXiv API and Google's own index, so it
  is recall-limited for non-arXiv, non-Google literature.
- **De Simone et al. (World Bank, Nigeria, 2025)**, cited by R5 as prior art for
  genAI learning outcomes. Not read. Flagged for B2.
- **Read Along efficacy research.** No arXiv record surfaced; the product page cites
  none. Absence of evidence only.
