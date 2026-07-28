---
title: "The edtech landscape as a taxonomy of design hypotheses, and LessonOrca as primary evidence"
wave: E
sections: [E1, E2]
date_researched: 2026-07-27
sources_count: 44
status: raw-research
---

# E1 + E2 — The market frontier

> **Retrieval note.** The WebSearch budget for this project was exhausted before this
> section began. Retrieval therefore ran on: targeted `WebFetch` of primary vendor
> artefacts; `curl` against the **Wikipedia Action API** (encyclopedic/`REFERENCE` claims
> only), the **Crossref REST API** (peer-reviewed anchors), the **arXiv API** (returned
> empty payloads throughout this session — logged as a retrieval failure, not a null
> finding), and the **Semantic Scholar graph API** (returned empty result sets; likewise a
> retrieval failure); direct HTML extraction of `lessonorca.com` where its client-rendered
> pages defeated the markdown converter; and the author's own **PostHog** project for E2's
> original measurement.
>
> Sources that returned hard blocks and are therefore *not* cited as evidence:
> `papers.ssrn.com` (403), `openai.com/index/chatgpt-study-mode` (403 to WebFetch, JS-wall
> to curl), `educationendowmentfoundation.org.uk` (403), `holoniq.com` (404 on the funding
> notes path), `carnegielearning.com` efficacy path (404). Claims that would have depended
> on them are either sourced elsewhere or marked `UNVERIFIED-IN-SESSION`.
>
> Evidence labels follow PRD §3: `MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH` ·
> `OBSERVED` · `VENDOR`. Two additional labels are used and defined here: `REFERENCE`
> (tertiary encyclopedic source, used only for dates, ownership, and corporate events) and
> `UNVERIFIED-IN-SESSION` (believed true, source not retrievable in this session).
> **No `VENDOR` claim is restated as a finding.**

---

## 0. The thesis of this section

A directory of edtech companies is worthless six months after it is written. What survives
is the **structure of the bets**. Every company in this market has chosen one primitive to
be the load-bearing wall of its product — the thing that, if it works, makes everything else
follow. The primitive is a falsifiable hypothesis about how learning happens. Nine of them
are in the market as of mid-2026.

Reading the market this way produces one uncomfortable finding immediately, and it is the
finding of E1:

> **The strength of a company's evidence is inversely correlated with the size of its
> claim, and both are uncorrelated with its funding.** The best-evidenced products in this
> survey (ASSISTments, Cognitive Tutor) are a nonprofit and a 40-year-old curriculum
> company, and both report effect sizes an order of magnitude smaller than the marketing
> copy of products with no evidence at all.

The second finding is the graveyard's. Six canonical failures are examined in §5. They
failed for six apparently different reasons, and one actual reason.

And the third — the one that matters most for the rest of this survey — is that the single
strongest piece of causal evidence in the entire 2024–2026 AI-in-education literature is a
**negative** one, and it is the empirical foundation of the refusal-engine argument this
survey makes. It is stated first, in §1, because everything else should be read against it.

---

## 1. The result that organises the field

**Bastani, Bastani, Sungu, Ge, Kabakcı & Mariman (2025), "Generative AI without guardrails
can harm learning: Evidence from high school mathematics," *PNAS*.**
`MEASURED-RCT` — DOI [10.1073/pnas.2422633122](https://doi.org/10.1073/pnas.2422633122)
(earlier SSRN preprint DOI [10.2139/ssrn.4895486](https://doi.org/10.2139/ssrn.4895486);
a correction was issued at DOI
[10.1073/pnas.2518204122](https://doi.org/10.1073/pnas.2518204122) — the survey should cite
the corrected record).

Field experiment, "nearly a thousand" high-school mathematics students, two AI arms:

| Arm | Effect **while tool available** | Effect **after tool removed** |
|---|---|---|
| **GPT Base** (standard ChatGPT-like interface) | **+48%** grade improvement | **−17%** vs. never having had access |
| **GPT Tutor** (prompted with learning safeguards) | **+127%** grade improvement | negative effect "largely mitigated" |

Quoting the abstract directly: *"when access is subsequently taken away, students actually
perform worse than those who never had access (17% reduction in grades for GPT Base) — i.e.,
unfettered access to GPT-4 can harm educational outcomes… students attempt to use GPT-4 as
a 'crutch' during practice problem sessions, and subsequently perform worse on their own."*

Three things follow, and they structure the whole of E1:

1. **Performance improvement and learning are not the same measurement, and can have
   opposite signs.** Any vendor metric of the form "students using X score higher *while
   using X*" is uninformative about learning by construction. This disqualifies most of the
   `VENDOR` evidence catalogued below.
2. **The difference between harm and benefit was a prompt.** Same model, same students, same
   task; the delta came entirely from whether the system was designed to withhold. That is
   the anti-sycophancy / refusal-engine thesis, tested, in the field, with a control group.
3. **The harm mechanism is behavioural, not epistemic.** GPT Base did not teach wrong things.
   It taught the student to outsource. The failure mode is *dependency*, which no
   accuracy benchmark detects.

Everything in the tutoring cluster (§2.2) should be read as an answer — usually an
unexamined one — to the question this trial poses.

---

## 2. The nine primitives

For each cluster: the **hypothesis** (what has to be true for the bet to pay), who is in it,
what is claimed, what is actually measured, and traction/funding where retrievable.

### 2.1 Content generation — *"the bottleneck is materials"*

**Hypothesis:** teachers and tutors are constrained by the cost of producing aligned
materials; collapse that cost to zero and quality rises.

| Company | Claim | Evidence |
|---|---|---|
| **MagicSchool AI** ([magicschool.ai](https://www.magicschool.ai/)) | "80+ teacher tools", "50+ student tools"; named districts incl. Denver, Atlanta, Seattle Public Schools; "7-10 hours time saved per week on average"; "28% improvement in students meeting literacy grade-level expectations"; "88% of teachers say it helps them reach every learner"; SOC 2, FERPA/COPPA, "We don't use student or teacher data to train AI" | `VENDOR` — no design, sample, or comparison group disclosed for the 28% figure on the page retrieved |
| **LessonOrca free tools** ([lessonorca.com/tools](https://lessonorca.com/tools)) | AI Worksheet Generator, AI Lesson Plan Generator; "Every worksheet and lesson plan is unique"; K-12, 30/45/60/90-min plans, PDF export, no signup | `VENDOR` — but see §7 for `OBSERVED` telemetry on actual completion rates |
| **Diffit, Curipod, Brisk Teaching** (category peers) | Levelled-text and slide generation inside existing teacher workflows | `UNVERIFIED-IN-SESSION` — vendor pages not retrieved this session; listed for taxonomic completeness only, no claims attributed |

**What is actually measured:** essentially nothing about learning. Every retrievable metric
in this cluster is a *teacher-time* metric. That is not a criticism of the products — teacher
time is a real and scarce good — but it means the cluster has quietly redefined its own
success criterion from "students learn more" to "adults work less." Those can diverge: the
Bastani trial's GPT Base arm also saved the student enormous time.

**The unexamined risk in this cluster** is *volume without spacing*. Infinite fresh
worksheets is precisely the wrong affordance if retention, not comprehension, is the binding
constraint (survey §F11) — novel items every session is the opposite of scheduled retrieval
of previously-failed items.

### 2.2 Tutoring — *"the bottleneck is one-to-one attention"*

**Hypothesis:** Bloom's two-sigma gap is an availability problem; a good-enough synthetic
tutor closes some of it.

This cluster splits cleanly into two sub-bets that are rarely distinguished and should be:

**(a) Answer-giving tutors.** Photomath (acquired by Google; the Wikipedia record notes the
acquisition "was cited as a strategic move by Google in response to ChatGPT" and closed June
2023 — `REFERENCE`, [Photomath](https://en.wikipedia.org/wiki/Photomath)), Chegg, and the
homework-solver category generally. Chegg's own encyclopedic record notes it "has been widely
criticized for facilitating cheating and academic dishonesty among students"
(`REFERENCE`, [Chegg](https://en.wikipedia.org/wiki/Chegg)). This sub-bet is the GPT Base arm
of the Bastani trial, commercialised. Its measured effect on learning, per §1, is plausibly
negative.

**(b) Withholding tutors.** The interesting bet.

| Product | Pedagogical claim (verbatim) | Evidence |
|---|---|---|
| **Khanmigo** ([khanmigo.ai](https://www.khanmigo.ai/)) | "it guides learners to find the answer themselves" with "limitless patience"; free for teachers in 44+ countries with Microsoft support; parent accounts for up to 10 children under 18 | `VENDOR`. Third-party recognition cited on the page is *ratings* (Common Sense Media 4 stars; WSJ), not outcome studies. No peer-reviewed efficacy study is presented |
| **Anthropic Claude for Education / Learning Mode** ([anthropic.com](https://www.anthropic.com/news/introducing-claude-for-education), launched 2 Apr 2025) | Learning Mode asks *"How would you approach this problem?"* and *"What evidence supports your conclusion?"* rather than answering; campus-wide at Northeastern (~50,000 users, 13 campuses, design partner), LSE, Champlain College | `VENDOR`. **Explicit null:** the announcement contains **no evaluation data and no efficacy study**. A frontier lab shipped a Socratic mode to ~50,000 students with zero published outcome measurement |
| **ChatGPT Study Mode** (OpenAI) | Socratic scaffolding mode | `UNVERIFIED-IN-SESSION` — openai.com returned 403/JS-wall on both fetch paths. Listed for completeness; **no claim attributed** |
| **Brilliant / "Koji"** ([brilliant.org](https://brilliant.org/)) | "Every session is visual and interactive. Instead of just memorizing, you play with concepts until they click"; tutor "asks the right questions… gets to the heart of where you're getting stuck"; "10 million+ learners"; 33 math / 14 CS / 5 science / 5 data courses | `VENDOR`. The page "cites no efficacy research or studies" |
| **Third Space Learning** ([thirdspacelearning.com](https://thirdspacelearning.com/)) | AI tutor "Skye", real-time *spoken* one-to-one maths; "7 months' progress in 14 weeks" from "an independent trial"; 196,000+ students, 4,200+ schools, 2,295,000+ tutoring hours; £3,500–£6,000/yr primary, £5,000 secondary; "no pupil data is used to train the AI tutor" | `VENDOR` for the headline. The "independent trial" is asserted without a linked methodology or peer-reviewed publication on the page retrieved. **Note the honest disclosure of price**, which is rare in this cluster |
| **Squirrel AI** | "one of the first companies in the world to offer large scale AI-powered adaptive education solutions" | `REFERENCE` only ([Squirrel AI](https://en.wikipedia.org/wiki/Squirrel_AI)); its published RCTs are company-run and were not retrievable this session |
| **LessonOrca** | "Socratic method only. Guides students to answers, never gives them." | `VENDOR` for the claim; `OBSERVED` telemetry in §7. Full treatment in E2 |

**What is actually measured in this cluster** — the honest answer is: the pre-LLM generation
of it, and only that.

- **Kulik & Fletcher (2016), "Effectiveness of Intelligent Tutoring Systems," *Review of
  Educational Research*.** `MEASURED-META` — DOI
  [10.3102/0034654315581420](https://doi.org/10.3102/0034654315581420). 50 controlled
  evaluations; **median effect 0.66 SD** (50th → 75th percentile). Critically: *"the amount
  of improvement found in an evaluation depended to a great extent on whether improvement was
  measured on locally developed or standardized tests."* The headline 0.66 is substantially an
  artefact of instrument alignment. This is the single most-cited number in the tutoring
  market and it comes with its own debunking attached.
- **Pane et al. (2014), "Effectiveness of Cognitive Tutor Algebra I at Scale," *EEPA*.**
  `MEASURED-RCT` — DOI [10.3102/0162373713507480](https://doi.org/10.3102/0162373713507480).
  Matched-pair school randomisation, seven states. **No effect in year 1.** Positive in year
  2, statistically significant for high schools but **not** middle schools. Effect magnitude
  ≈ moving the median student ~8 percentile points.
- **Tutor CoPilot (2024).** `MEASURED-RCT` — DOI
  [10.21203/rs.3.rs-5363154/v1](https://doi.org/10.21203/rs.3.rs-5363154/v1). *"the first
  randomized controlled trial of a Human-AI system in live tutoring, involving 900 tutors and
  1,800 K-12 students from historically under-served communities."* Note the architecture:
  the AI advises the **human tutor in real time**, it does not tutor the student. This is the
  same architectural choice LessonOrca makes (§6) and it is the one AI-tutoring architecture
  with a live-classroom RCT behind it.

**Synthesis of the cluster:** the pre-LLM ITS literature says intelligent tutoring works, at
roughly a fifth of the effect its own meta-analysis headline implies once instrument bias is
removed, and only in year two. The LLM generation has inherited the marketing claim and none
of the measurement. The one LLM-era RCT in live tutoring put the AI behind the human.

### 2.3 Assessment — *"the bottleneck is the cost of grading"*

**Hypothesis:** grading is the rate limiter on feedback frequency; automate it and the
feedback loop tightens.

| Company | Claim | Evidence |
|---|---|---|
| **Gradescope** ([gradescope.com](https://www.gradescope.com/), owned by Turnitin, LLC) | 700M+ questions graded; 2,600+ universities; 140,000+ instructors; 3.2M+ students; "Answer Groups & AI-assisted Grading" clusters similar responses so one rubric decision grades many | `VENDOR` for the counts. Mechanism is *clustering*, not judgement — which is why it works. "The page does not include academic research citations" |
| **Turnitin** | Licensed worldwide, "more than 71 million students enrolled"; acquired by Advance Publications for **US$1.75bn** (2019); acquired VeriCite (2018), Unicheck (2020), Ouriginal (2021) | `REFERENCE` ([Turnitin](https://en.wikipedia.org/wiki/Turnitin)) |
| **ASSISTments** ([assistments.org](https://www.assistments.org/)) | Free to teachers; 200,000+ standards-aligned problems; "ESSA Strong Evidence" Tier 1; "60% more growth in math scores"; 1M+ students since 2019 | See below — the best-evidenced product in this survey |

**The negative result this cluster must carry.** Turnitin's AI-detection feature, shipped
early 2023, is the clearest case in edtech of a product whose core claim was falsified after
sale.

- **Weber-Wulff et al. (2023), "Testing of detection tools for AI-generated text,"
  *International Journal for Educational Integrity*.** `MEASURED-BENCH` — DOI
  [10.1007/s40979-023-00146-z](https://doi.org/10.1007/s40979-023-00146-z). 12 public tools
  plus **two commercial systems in wide academic use (Turnitin and PlagiarismCheck)**;
  examined accuracy *and error type*, and the effect of machine translation and obfuscation.
  The tools are not reliable discriminators.
- Corroborating institutional behaviour (`REFERENCE`,
  [Turnitin](https://en.wikipedia.org/wiki/Turnitin)): *"some schools disabled Turnitin's AI
  detection software due to concerns that, like all other AI detection tools the software is
  not entirely accurate. Concerns arose after cases were brought with students alleging
  Turnitin falsely accused them of using AI. This has happened when students use the
  grammar-correcting software Grammarly, which is recommended for student use by many
  schools."* Turnitin's own stated false-positive rate is ~1% of papers — against tens of
  millions of submissions, that is a large number of accused innocents.
- Pricing opacity in the same cluster is documented: per *The Markup* (June 2025, via
  `REFERENCE`), per-student prices for the same service ranged **$1.79 (CUNY) to $6.50 (UC
  Irvine Continuing Education)**, with AI detection sold as a **$3.19/student upgrade** to
  the California State University system on top of $2.71/student base.

**ASSISTments is the counter-example the whole survey needs.** From its own evidence page
([assistments.org/evidence-of-impact](https://www.assistments.org/evidence-of-impact)):

| Study | Design | n | Effect size | Label |
|---|---|---|---|---|
| Maine (2012–2015) | RCT | 46 schools, 2,769 grade-7 students | **0.22** | `MEASURED-RCT` |
| North Carolina (2018–2021), WestEd | RCT, delayed outcome | 63 schools, 5,991 grade-7 students | **0.10** one year later | `MEASURED-RCT` |
| Kelly et al. (2013) | small RCT | 63 students | 0.52 / 0.56 | `MEASURED-RCT` |
| Kehrer, Kelly & Heffernan (2013) | small RCT | 65 students | 0.37 | `MEASURED-RCT` |
| Mendicino, Razzaq & Heffernan (2009) | small RCT | 28 students | 0.61 | `MEASURED-RCT` |
| **Gates Foundation / SRI evaluation** | independent | not stated on page | **0.03** | `MEASURED-RCT` — **the near-null** |

Two observations. First, the **effect size falls as the sample grows and the evaluator
becomes independent** — 0.61 at n=28 in-house, 0.22 at n=2,769, 0.10 at delayed follow-up,
0.03 in the independent SRI evaluation. That gradient is the single most instructive object
in this entire section, and it is published *by the vendor on its own evidence page*, which
is to the vendor's enormous credit. Second, note that the vendor's headline — "60% more
growth" — is the **0.22** study rendered in percentage-of-a-year's-growth terms. A 0.22 SD
effect is a genuinely good edtech result. "60% more growth" sounds like something else
entirely. The translation layer between effect sizes and marketing is where most of this
market's dishonesty lives, and it does not require anyone to lie.

### 2.4 Teacher tooling — *"the bottleneck is the teacher's week"*

**Hypothesis:** the highest-leverage intervention is not on the student at all.

- **SchoolAI** ([schoolai.com](https://schoolai.com/)) — student-facing "Spaces" that a
  teacher authors, plus a "Mission Control" monitoring dashboard: teachers *"see exactly
  who's engaged, who's stuck, and what to do next."* Safety posture is unusually explicit —
  the platform *"flags crises in real time, never poses as human, and connects students to
  trusted adults"*, and *"every AI provider… is contractually bound never to train on or sell
  student data."* Claims ESSA Level III certification and *"28% boost in student critical
  thinking"* / *"2x students engaging in higher-order reasoning"*, attributed to an
  Instructure review and a Stanford SCALE Initiative analysis. `VENDOR` — ESSA Level III is
  the *correlational* tier, and the survey should say so plainly: Tier III means "promising",
  i.e. a positive correlation with statistical controls, not a causal estimate.
- **MagicSchool** — see §2.1.
- **LessonOrca** — the entire product is in this cluster despite having a student-facing
  tutor; see §6.

**Cross-cluster note.** "Never poses as human" (SchoolAI) and "AI-generated content is
clearly labeled" (LessonOrca) are the same design commitment, arrived at independently. This
is a candidate for a **generalisable norm** the survey should name: *disclosure of synthetic
origin at the point of consumption, not in the terms of service.*

### 2.5 Language — *"the bottleneck is practice hours with a patient interlocutor"*

**Hypothesis:** language acquisition is dominated by low-stakes production practice, which
humans are too expensive and too judgmental to supply.

- **Duolingo** ([Duolingo](https://en.wikipedia.org/wiki/Duolingo), `REFERENCE`) — 42
  languages plus music, chess and maths; "gamification to motivate users with points, rewards
  and interactive lessons featuring **spaced repetition**"; freemium; also operates the
  **Duolingo English Test** (a credentialing product — see §2.8) and **Duolingo ABC** (early
  literacy — §2.6). Duolingo is the only company in this survey that spans four of the nine
  primitives, which is itself the story: the language primitive generalises to *any* domain
  with a large item pool and a retention problem. **Negative note:** `duolingo.com/efficacy`
  was retrieved but rendered no substantive content to the fetcher, so **no Duolingo efficacy
  claim is carried in this survey from this session** — logged as a retrieval gap, not as
  absence of evidence.
- **Speak** ([speak.com](https://www.speak.com/)) — "built to get you speaking a new language
  — not just studying it"; the "Speak Method" is learn → practice to automaticity → apply in
  "real back-and-forth conversation with the Speak Tutor AI"; **15M+ downloads**; "a formal
  partnership with OpenAI" and "backed by the OpenAI Startup Fund". `VENDOR`. The page
  contains **no independent efficacy research** — claims rest on testimonials.

The language cluster is the one place where the "practice, not answers" design is
*commercially* natural: nobody buys a language app to be told the answer. It is worth asking
in F2/G2 why the pedagogical discipline that language apps get for free has to be
engineered against the grain everywhere else.

### 2.6 Early literacy — *"the bottleneck is a listener"*

**Hypothesis:** the scarcest resource in K-2 is an adult who will listen to a child read
aloud and correct in real time. This is the cluster with the clearest theory of value.

- **Amira Learning** ([amiralearning.com](https://www.amiralearning.com/)) — an AI agent that
  *"listens as students read aloud, assessing proficiency, and responding in English and
  Spanish"*; integrates assessment + tutoring + lesson planning; **5.5M+ students**, **4,000+
  districts and schools**; headline claim: *"Students who read with Amira at dosage
  experience **68% faster reading growth** in one school year than those using other reading
  technologies."* `VENDOR`. Note the load-bearing qualifier **"at dosage"** — a
  compliance-conditioned comparison, which is a selection effect unless dosage was randomised.
  The site references "independent studies conducted by state agencies, universities and
  education ministries" but names no ESSA tier and no RCT on the page retrieved.
- **Ello** ([ello.com](https://ello.com/)) — ages 4–9; AI that *"listens, understands, and
  adapts to your child in real time"* and *"makes teaching decisions in the moment"*; a Public
  Benefit Corporation; freemium. Claim: *"88% of children read more after 4 weeks of Ello"*
  — `VENDOR`, and note that *reading more* is a behavioural proxy, not a reading-skill
  outcome. To Ello's credit the claim is stated as what it is.
- **ABCmouse / Age of Learning** — included here as a cautionary datum, not a design
  hypothesis: in 2020 the parent company *"agreed to pay $10 million and settle a Federal
  Trade Commission complaint alleging that some of its past marketing and billing practices
  were unfair"* (`REFERENCE`, [ABCmouse](https://en.wikipedia.org/wiki/ABCmouse)). The
  consumer-subscription early-learning model has a documented history of dark-pattern
  billing, and any survey recommending consumer edtech to parents must say so.

**Why this cluster is the most defensible in the market:** the AI is doing something a
human demonstrably cannot scale (listening to 25 children read aloud simultaneously), the
output is a measurable behaviour (oral reading fluency) rather than a self-reported one, and
the pedagogy — decoding practice with immediate corrective feedback — is the best-replicated
result in all of education. If AI-in-education works anywhere, it works here first.

### 2.7 STEM — *"the bottleneck is representation"*

**Hypothesis:** mathematics and science are hard because they are taught symbolically to
learners who have no concrete anchor; make the abstraction manipulable and the difficulty
falls.

- **Brilliant** — see §2.2; the interactive-representation bet, explicitly: *"you play with
  concepts until they click."*
- **Photomath** (Google) — the *anti*-hypothesis in the same subject: the bottleneck is
  getting unstuck, so show the steps. Raised $23M Series B (2021) led by Menlo Ventures with
  GSV Ventures, Learn Capital, Cherubic, Goodwater; acquired by Google, EC-approved March
  2023, closed June 2023 — *"the largest startup acquisition in Croatian history"*
  (`REFERENCE`).
- **Carnegie Learning / MATHia** — the pre-LLM incumbent whose RCT (Pane et al., §2.2)
  remains the best large-scale randomised evidence for adaptive STEM software, including its
  year-one null and its middle-school null.

The cluster's honest state: the representation bet (Brilliant, Desmos, PhET) has strong
laboratory support in the multimedia-learning and concreteness-fading literatures covered in
survey §B1/§F10, and almost no field-scale randomised evidence of its own. The step-showing
bet (Photomath) has enormous adoption and, after Bastani, a serious prima facie case to
answer.

### 2.8 Credentialing — *"the bottleneck is the signal, not the learning"*

**Hypothesis:** learning is already abundant; what is scarce is a portable, trusted claim
about it.

- **1EdTech Open Badges** and **Comprehensive Learner Record (CLR)**
  ([1edtech.org/standards/details](https://www.1edtech.org/standards/details)) — Open Badges
  for *"capturing learner achievements that are verifiable, portable, and interoperable"*;
  CLR as *"a comprehensive digital learner record for education and workforce learning
  supporting competency-based education."* `REFERENCE`. **Negative finding:** the standards
  page gives **no adoption or conformance numbers for either**, which after a decade of
  Open Badges is itself the datum. The portable-credential thesis has excellent
  specifications and no demonstrated demand-side pull.
- **Coursera** ([Coursera](https://en.wikipedia.org/wiki/Coursera), `REFERENCE`) — 375+
  university and company partners, ~7,000 courses (2024). In December 2024, under new CEO
  Greg Hart, Coursera *"ended the opportunity to audit courses for free, putting all of the
  previously free university courses under a paywall starting at USD49 per month."* The MOOC
  access thesis, formally retired by its largest surviving vendor.
- **Instructure → Parchment** — Instructure acquired credential-management platform
  **Parchment** in 2024 (`REFERENCE`, [Instructure](https://en.wikipedia.org/wiki/Instructure)),
  i.e. the LMS incumbent bought the credential rails rather than the standards body's
  ecosystem delivering them.
- **Duolingo English Test** — the successful case: a credential that displaced an incumbent
  (TOEFL/IELTS) by attacking price and access rather than portability (`REFERENCE`,
  [Duolingo](https://en.wikipedia.org/wiki/Duolingo)).

**The pattern:** credentialing succeeds when it replaces a *specific, expensive, gatekept
test* and fails when it tries to build a general-purpose portable record. Open Badges has had
twelve years; Duolingo English Test had one adversary.

### 2.9 Learning infrastructure — *"the bottleneck is plumbing"*

**Hypothesis:** whoever owns rostering, gradebook, identity and the LTI socket owns the
market regardless of pedagogy.

This is the cluster where the money actually is, and where the risk actually is.

| Fact | Label |
|---|---|
| Instructure (Canvas LMS) acquired by **Thoma Bravo for $2bn (2020)**; IPO 2021; acquired by **KKR and Dragoneer for $4.8bn (2024)**; ~4,000 institutions as of 2020 | `REFERENCE` — [Instructure](https://en.wikipedia.org/wiki/Instructure) |
| Turnitin acquired by Advance Publications for **$1.75bn (2019)** | `REFERENCE` |
| 1EdTech standards stack: **LTI** (tool integration), **Caliper Analytics** (learning-activity event stream — *"a common language for labeling learning data"*), **QTI** (item/test/result exchange), **OneRoster 1.2** (people, memberships, courses, outcomes), **CASE** (standards/competency exchange), **Edu-API** (SIS data exchange) | `REFERENCE` — [1edtech.org](https://www.1edtech.org/standards/details) |

**The negative result this cluster must carry — and it is the largest single event in edtech
in the survey period.** In late April 2026, **Canvas LMS experienced a security breach**,
with an outage following in early May. Per the encyclopedic record (`REFERENCE`,
[Instructure](https://en.wikipedia.org/wiki/Instructure)): *404 Media* described it as **"the
largest educational security breach ever on record"**; the ShinyHunters group claimed **3.65
terabytes / approximately 275 million records**, affecting **8,809 universities and education
institutions**, with a ransom deadline of 12 May; **by 8 May, seven federal lawsuits had been
filed** against Instructure, one naming **KKR** as a co-defendant, with a California class
action following on 13 May.

Three implications the survey must carry forward into §F8:

1. **Consolidation is a concentration of blast radius.** The same $4.8bn logic that made
   Canvas a good private-equity asset — one integrated platform, near-universal adoption —
   made 8,809 institutions a single point of failure.
2. **Every "we don't train on student data" promise in §2.1–2.8 is a promise about *use*, not
   about *custody*.** A vendor can honour it perfectly and still lose the data.
3. **Data minimisation is a security control, not a compliance chore.** The single most
   effective mitigation available to any product in this survey is to not hold the record in
   the first place — which is precisely the design pressure the inBloom failure (§5) applied
   twelve years earlier and which the market un-learned.

**Foundation-model layer.** The frontier labs have all entered this cluster as
infrastructure rather than product: Claude for Education with campus-wide agreements
(Northeastern ~50,000 users, LSE, Champlain — `VENDOR`), and Google's **LearnLM**, whose
current status is itself a finding: *"LearnLM is no longer a separate listing in AI Studio.
Instead, LearnLM capabilities have been integrated into Gemini starting with the 2.5 model
series"* (`REFERENCE`, [ai.google.dev](https://ai.google.dev/gemini-api/docs/learnlm)). The
pedagogically-tuned model did not survive as a distinct artefact; it was absorbed into the
general model. Whether pedagogy survived the absorption is unmeasured and is exactly the kind
of question §F9 should flag as open.

---

## 3. What this taxonomy reveals when read across

**Finding E1-a. The evidence gradient runs opposite to the funding gradient.**
The two products in this section with genuine independent randomised evidence — ASSISTments
(nonprofit, free to teachers) and Cognitive Tutor (a curriculum publisher) — report effects of
**0.03–0.22 SD**. The products with the largest claims (68% faster growth; 28% critical
thinking gains; 7 months in 14 weeks) report no retrievable design, sample, or comparison
group. The best-funded entity in the section (Instructure, $4.8bn) makes no learning claim at
all.

**Finding E1-b. "Time saved" has silently replaced "learning gained" as the industry's
success metric.** Across §2.1 and §2.4 this is the only quantity anyone measures. It is a
real value — but the Bastani trial establishes that time saved by the *learner* is the
signature of harm, and no vendor in this survey distinguishes teacher-time savings from
learner-time savings in its metrics.

**Finding E1-c. The market has converged on three safety primitives without coordinating.**
Adult visibility into every AI interaction, explicit synthetic-content labelling, and "the AI
never claims to be human" appear independently at SchoolAI, MagicSchool, and LessonOrca.
These are candidate norms, and they are stronger than anything in current regulation.

**Finding E1-d. Every cluster's dominant claim is a *mechanism* claim, and mechanisms are not
outcomes.** "Guides rather than answers", "listens as students read aloud", "makes teaching
decisions in the moment" — these describe what the system does, and are all verifiable by
inspection. The survey should treat mechanism claims as *checkable and therefore valuable*,
and hold them to a different standard than outcome claims: a mechanism claim that survives
adversarial inspection is worth more than an outcome claim that cannot be replicated.

---

## 4. Retrieval gaps and honest caveats for E1

- **Funding aggregates could not be retrieved.** HolonIQ's venture-funding notes returned 404.
  The survey therefore carries **no total-market funding figure**. Consolidation is evidenced
  only by named transactions (Thoma Bravo $2bn, KKR/Dragoneer $4.8bn, Advance $1.75bn, 2U's
  $800m edX purchase, Wiley's sub-$17m Knewton purchase).
- **Crunchbase-class traction data is absent throughout.** All per-company user counts in §2
  are `VENDOR` self-report from the company's own homepage on the date fetched.
- **The EEF Toolkit's digital-technology entry (the best independent UK synthesis) returned
  403** and is not cited. Its expected contribution — a small positive effect with low
  security — is flagged `UNVERIFIED-IN-SESSION` and should be re-fetched before publication.
- **Several named category peers (Diffit, Curipod, Brisk, Lexia, Desmos, PhET, Riiid) are
  listed taxonomically with no claims attributed**, because their pages were not retrieved in
  this session.

---

## 5. The graveyard

Edtech's failure rate is the most informative dataset it has, and unlike its success
literature it is not vendor-controlled. Six canonical deaths.

### 5.1 One Laptop Per Child (2005–2014) — *died of the device fallacy*

The mission was to distribute a $100 laptop to transform education in the developing world,
rooted in Papert's constructionism. The hardware organisation shut down in 2014 after
disappointing sales (`REFERENCE`,
[OLPC](https://en.wikipedia.org/wiki/One_Laptop_per_Child)).

**The verdict is randomised.** Cristia et al., "Technology and Child Development: Evidence
from the One Laptop per Child Program" — `MEASURED-RCT`, DOI
[10.18235/0012202](https://doi.org/10.18235/0012202). 319 rural Peruvian primary schools, 15
months. Computers per student rose **0.12 → 1.18**; use rose substantially at school and at
home. *"No evidence is found of effects on enrollment and test scores in Math and Language."*
Some positive effects on general cognitive measures (Raven's, verbal fluency, coding). The
long-run follow-up across 531 schools over 10 years found *"no significant effects on
academic performance, primary and secondary completion, or university enrollment."*

**Cause of death:** the intervention was **access**, and access was never the binding
constraint. Delivery succeeded completely; the theory of change was wrong. Nothing about
teaching changed, so nothing about learning changed.

### 5.2 inBloom (2013–2014) — *died of consent*

A student-data warehouse funded with **$100 million in start-up funding from the Gates
Foundation**. *"After every district and state withdrew from inBloom because of parent
protests, the corporation closed its doors in April 2014"* (`REFERENCE`,
[Leonie Haimson](https://en.wikipedia.org/wiki/Leonie_Haimson); contemporaneous coverage
cited there: Kamisar, *"InBloom Sputters Amid Concerns About Privacy of Student Data"*, 8
Jan 2014). The organised opposition produced a durable institution: the **Parent Coalition
for Student Privacy**, founded July 2014.

**Cause of death:** it treated parental consent as a compliance formality rather than the
product's licence to operate. The technology worked; every customer left anyway. inBloom is
the reason "parents can see everything" is a *market* requirement in 2026 and not merely an
ethical one — and, read against §2.9's Canvas breach, the reason it should also be an
*architectural* requirement.

### 5.3 Knewton (2008–2019) — *died of an unfalsifiable claim*

Raised across seven rounds: $2.5M, $6M (Bessemer), $12.5M (FirstMark), **$33M Series D
(Founders Fund, 2011)**, **$51M Series E (Atomico, 2013)**, **$52M Series F (Sofina/Atomico,
2016)** — roughly **$157M disclosed**. Partnerships with Pearson (MyLab/Mastering), Houghton
Mifflin Harcourt, Macmillan. **Assets acquired by Wiley in May 2019 for less than $17
million** (`REFERENCE`, [Knewton](https://en.wikipedia.org/wiki/Knewton)).

The claim was *"sophisticated, real-time analysis of reams of student performance data"*
producing per-student adaptive recommendations. The retrievable outcome evidence is one
partner's before/after comparison: at Arizona State, *"the portion of students withdrawing
from the courses fell from 13% to 6%, and pass rates rose from 66% to 75%"* — a
**pre/post with no control group**, in a course that was simultaneously redesigned.

**Cause of death:** the central claim was never stated in a form that could fail. "Adaptive"
was a category, not a mechanism with a measurable output. When publishers eventually asked
what the adaptivity bought, no one could answer, and — as survey §F5 independently
establishes — the answer was structurally bounded anyway: knowledge-tracing AUC has sat in a
0.70–0.83 band since 2015. Knewton was selling accuracy from a part of the design space
where accuracy had already plateaued. **~$157M in, <$17M out: a ~90% capital destruction.**

### 5.4 AltSchool → Altitude Learning (2013–2019) — *died of the wrong customer*

Founded by Max Ventilla in 2013; raised **$33M (2014)** and **$100M (2015)**; by 2016 ran six
schools in San Francisco, Palo Alto and Brooklyn plus partner schools in California and
Virginia; opened a Union Square middle school in 2017. The model: student-and-teacher-authored
"playlists" of personalised projects, with progress *"streamed to parents using a portal
app."* The company then closed or divested its schools, and in 2019 *"ceased operating schools
directly and rebranded as Altitude Learning, an educational software company"* (`REFERENCE`,
[Altitude Learning](https://en.wikipedia.org/wiki/AltSchool)).

**Cause of death:** it built a **school** in order to build **software**, and the school was
the R&D cost centre for a product that did not exist yet. Real children were the pilot
population for an unvalidated model, and when the software pivot came, the schools — the
thing families had actually bought — were closed. Note also that the surviving artefact, the
parent progress portal, is now a table-stakes feature (§2.4, §6): AltSchool was right about
the feature and wrong about the business.

### 5.5 2U / edX (2008–2024) — *died of unit economics dressed as mission*

2U pioneered the online program manager (OPM) model: 10-year revenue-share contracts with
universities, students paying standard tuition. It grew by acquisition — **GetSmarter for
$103M (2017)**, Trilogy — and in 2021 bought **edX from the Harvard/MIT nonprofit for $800M
in cash**, a transaction one Harvard-affiliated academic called *"a betrayal and a
fundamentally misguided choice by Harvard and MIT."* 2U reported *"$1.3B invested in its
non-profit partners' degree programs"* and 275,000+ students by late 2020.

Then: the USC social-work programme, where *"USC social-work graduates who took out federal
loans borrowed a median $112,000. Half of them were earning $52,000 or less annually two
years later."* Class actions over rankings (2022). A 20% workforce layoff (July 2022). USC
and 2U ending most programmes on 9 November 2023 — **shares fell 57% that day**. 2U suing the
Department of Education over third-party-servicer oversight (2023). **As of 2023, 2U had
never made an annual profit.** **Chapter 11 on 25 July 2024**, eliminating over $450M of debt
(`REFERENCE`, [2U](https://en.wikipedia.org/wiki/2U_(company)),
[edX](https://en.wikipedia.org/wiki/EdX)).

**Cause of death:** the revenue share made student *volume*, not student *outcome*, the
company's only lever, and the marketing spend required to hit volume was the very thing that
made the degrees unaffordable. The mission language was sincere and structurally
unenforceable. edX — a genuine public good built by two universities — was collateral.

### 5.6 Byju's (2011–2025) — *died of growth as a substitute for pedagogy*

The world's most valuable edtech company: **$22bn valuation (2022)**, **150 million+ claimed
registered students (April 2023)**, India's first edtech unicorn. Product: 12–20 minute
animated concept videos, self-paced, freemium. Then: a 17-month delay filing audited FY2021
financials, prompting a Ministry of Corporate Affairs letter (August 2022); reports of over
5,000 employees fired (November 2022); Enforcement Directorate searches under FEMA seizing
*"incriminating"* documents (April 2023); ~500 further layoffs (2024); the Android app
**delisted from Google Play over unpaid AWS bills (May 2025)**; **insolvency proceedings as
of 2025**. In October 2024 founder Byju Raveendran said publicly that *"the company is worth
zero."* Forbes' 2024 index recorded his net worth falling from ~₹17,545 crore (~US$2.1bn) to
zero (`REFERENCE`, [Byju's](https://en.wikipedia.org/wiki/Byju%27s)).

**Cause of death:** a direct-sales machine wearing a learning product as a costume. Byju's
optimised the one number the capital markets rewarded — registered users — and the
sales practices required to move that number were the subject of the reputational collapse
that ended it. The 85% retention rate the company reported was never independently verified,
and the survey should not repeat it.

### 5.7 The recurring cause of death

Six failures; six different proximate causes: hardware economics, parent revolt, an
unfalsifiable claim, an over-extended school network, negative unit economics, and a sales
scandal. The common structure underneath all six:

> **Each one succeeded completely at the thing it measured, and the thing it measured was not
> learning.**

- OLPC measured **laptops delivered** (0.12 → 1.18 per student — a total success) and moved
  no test scores.
- inBloom measured **data integrated** and lost every customer.
- Knewton measured **model sophistication** in a regime where sophistication had a proven
  ceiling.
- AltSchool measured **product iteration velocity** using enrolled children as the substrate.
- 2U measured **enrolment volume** and produced $112,000 median debt against $52,000 salaries.
- Byju's measured **registered users** and reached 150 million of them on the way to zero.

The proxy is always something the organisation controls, and learning is always something it
doesn't. This is not an edtech-specific pathology — it is Goodhart's law with children in the
loop — but edtech has an aggravating feature: **the delay between the proxy and the truth is
measured in school years, so the company can be dead right on its own metrics for a decade.**

The operational test this yields, and the one E2 must be held to: *name the metric that would
tell you your product is not working, and state how long you would have to wait to see it.*
Every company in §5 would have failed that test. Most companies in §2 would too.

---

# E2 — LessonOrca as primary evidence

**Status of this section.** LessonOrca is the survey author's own deployed product. Per PRD
§4 it is quarantined as a *design* influence and admitted only as an *evidence* source.
Everything in §6 is `VENDOR` (the company's own marketing copy, quoted verbatim so the reader
can audit the gap between claim and evidence). Everything in §7 is `OBSERVED` — single
product, non-randomised, no control group, three weeks of data, small n. **Nothing here is
`MEASURED-RCT` and nothing here may be restated as a general finding about Socratic
tutoring.** §8 assesses the product adversarially against the survey's own criteria, and §9
states what it fails.

## 6. What the product is, in its own words

Retrieved 2026-07-27 from [lessonorca.com](https://lessonorca.com) (verbatim extraction from
the rendered page; the site is a client-rendered SPA and several routes return a "Waking up
our servers" cold-start shell to fetchers, including `/privacy` and `/terms` — see §9).

### 6.1 The positioning: AI for the tutor, not instead of the tutor

> *"Your tutors are awesome. We give them context. So every tutor walks in knowing the
> student, the plan, and what happened last time."*

> *"AI will not replace tutors, but it will redefine how they work. Families don't want AI
> teachers! Families just want better human tutors."*

The problem statement is stated as continuity failure, not comprehension failure:

> *"When you're teaching 12 students a week, you're gonna have no memory of what you did last
> Wednesday, what Jeremy Johnson did at home, and no easy way to show parents what's
> happening."*

This is architecturally the **Tutor CoPilot** configuration (§2.2) — the only AI-tutoring
architecture with a live-classroom RCT behind it (900 tutors, 1,800 students, DOI
[10.21203/rs.3.rs-5363154/v1](https://doi.org/10.21203/rs.3.rs-5363154/v1)) — with one
difference: LessonOrca *also* exposes a student-facing tutor between sessions. That hybrid is
the thing to watch, because it is where the product's risk concentrates.

### 6.2 The stated economics

> **$1,600** — *"lost per churned student"* — *"~$200/mo × 8 months avg"*
> **$15,000** — *"wasted labor per tutor, per year"* — *"~10 hrs/week on plans, reports ×
> $25-30/hr"*

`VENDOR`. Both are **stated as derivations, with their inputs shown** — which is materially
more honest than the norm in §2 and lets a reader falsify them. Two observations the survey
should make:

1. **$1,600 is a churn-cost figure, not a learning figure.** It prices the *business*
   consequence of a student leaving. Arithmetically it is unimpeachable ($200 × 8 = $1,600)
   and it is a lifetime-value calculation, not a loss.
2. **The $15,000 figure is the "time saved" metric that Finding E1-b flags as the industry's
   substitute success criterion** — and it is *teacher* time, which is the defensible side of
   that distinction. But it is the same metric MagicSchool reports ("7-10 hours/week"), which
   means LessonOrca's stated economic case is, so far, indistinguishable from the content-
   generation cluster's. The Socratic differentiation is not priced.

### 6.3 The pedagogical commitment

The load-bearing claim, quoted exactly from two places on the page:

> Trust & safety → Safety guardrails: *"**Socratic method only. Guides students to answers,
> never gives them.** Custom AI guidelines per organization. COPPA-compliant parent
> linking."*

> FAQ → *"How does the AI tutor work?"* — *"It uses the Socratic method. **It guides students
> to answers through questions, never gives answers directly.** Parents and teachers can view
> every conversation. The AI follows custom guidelines set by each organization."*

Note where the claim is placed: **under "Safety guardrails," not under "Features."** The
product classifies answer-withholding as a *safety* property. That is the refusal-engine
thesis of §F2 stated as product taxonomy, and it is the correct classification — Bastani et
al. establish that unfettered answering is the harm condition.

### 6.4 The rest of the mechanism claims

| Feature | Verbatim claim | Maps to |
|---|---|---|
| Persistent learner profile | *"It builds a learning profile for each student that gets smarter with every interaction."* | §F5 learner model |
| Pre-session generation | *"Pre-session flag: Scored 45% on fraction word problems last week. Computation is strong — focus on applied problems."* + *"AI builds the lesson plan. Just give it your vision."* | §F5 → instruction coupling |
| Between-session support | *"The AI handles admin work and provides **24/7 student support between sessions**"* | §F11 retention / continuity |
| Full transparency | *"**Parents can view every AI conversation. Teachers see all student interactions.** AI-generated content is clearly labeled."* | §F8 oversight |
| Humans in the loop | *"Tutors review AI-generated profiles before they're shared. Flagged items require teacher attention. Parent emails are reviewed before sending."* | §F8 + §H1.2 |
| Data governance | *"Each center's data is fully isolated… role-based access control, COPPA-compliant parent linking… You can export your data at any time."* | §F8 |
| White-label | *"Every center gets its own subdomain at yourname.lessonorca.com."* | commercial, not pedagogical |
| Scope | *"Any K-12 subject."* | — |

### 6.5 Traction and provenance

From the company blog (`VENDOR`):

- **Founders:** Waleed and Abhiraam Eranti. *"We both decided to start this company because we
  found issues with the current system of tutoring and we're deciding to make it better."*
  ([/blog/our-origin](https://lessonorca.com/blog/our-origin), 25 Mar 2026)
- **Problem discovery:** the founders could not *"keep track of: what each student struggled
  with last time, what you planned to cover next, how they're actually progressing."* Waleed
  interviewed **50+ tutors**; finding: *"everyone has a system"* and *"no one feels like it's
  perfect."* — i.e. the wedge is **continuity**, not instruction. That is the correct read of
  the literature (§F11), arrived at from customer discovery rather than from citation.
- **Accelerators and scale:** accepted into **Berkeley SkyDeck Pad-13 (Batch 22)** and
  **Founders, Inc. Canopy**; *"live in 3 Bay Area tutoring centers, supporting 25 tutors and
  100 students."* No funding amount disclosed.
  ([/blog/skydeck-pad-13-canopy](https://lessonorca.com/blog/skydeck-pad-13-canopy), 19 Apr
  2026)
- First blog post 3 Feb 2026 ([/blog/hello-from-lessonorca](https://lessonorca.com/blog/hello-from-lessonorca)).

**Scale caveat, stated plainly: 3 centers, 25 tutors, 100 students.** This is a pre-seed-stage
product. It is admitted here as evidence of *what a design that takes the survey's arguments
seriously looks like when built*, and as a source of instrumented behaviour — **not** as
evidence that the design works.

---

## 7. Original measurement: what the telemetry actually shows

> **Provenance note added 2026-07-28.** Unlike §6 — which quotes the company's own
> published marketing copy and is therefore already public — this section reports
> **non-public product analytics** from the author's own instance. It is included with
> the owner's knowledge because a deployed, instrumented product is *evidence* where a
> landing page is not. If it should be withdrawn, it is this section and not §6.

`OBSERVED` — single product, non-randomised, no control condition. Source: the author's
PostHog project (org "LessonOrca", project 499062), aggregate queries only, no individual
learner data retrieved, no session content inspected. Window: **all data present in the
project, 2026-07-05 → 2026-07-26 (21 days).**

### 7.1 The event taxonomy that exists

Custom instrumented events in the project:

`landing_section_viewed` · `landing_tab_switched` · `landing_reached_faq` ·
`landing_cta_clicked` · `demo_video_play` · `tool_page_view` · `tool_generate_started` ·
`tool_generate_completed` · `tool_pdf_downloaded` · `tool_gate_shown` ·
`tool_gate_signup_clicked` · `tool_signup_completed` · `tool_student_added`

### 7.2 Volumes

| Event | Count | Unique persons | First → last |
|---|---|---|---|
| `$pageview` | 531 | 360 | 2026-07-05 → 07-26 |
| `$autocapture` | 739 | 123 | 07-05 → 07-26 |
| `landing_section_viewed` | 304 | 65 | 07-05 → 07-24 |
| `landing_reached_faq` | 37 | 35 | 07-05 → 07-24 |
| `demo_video_play` | 28 | 17 | 07-05 → 07-24 |
| `tool_page_view` | 24 | 16 | 07-05 → 07-26 |
| `tool_generate_started` | 46 | 32 | 07-06 → 07-26 |
| `tool_generate_completed` | 31 | 23 | 07-06 → 07-26 |
| `tool_pdf_downloaded` | 11 | 8 | 07-12 → 07-26 |
| `landing_cta_clicked` | 8 | 8 | 07-07 → 07-24 |
| `tool_signup_completed` | 7 | 7 | 07-07 → 07-25 |
| `tool_student_added` | 2 | 2 | 07-08 → 07-12 |
| `$rageclick` | 1 | 1 | 07-14 |

Traffic composition: 530 of 531 pageviews classified `Regular`, 1 `Automation` — so the
sample is human, but the `$pageview` unique-person count (360) exceeding `$autocapture`'s
(123) indicates substantial single-page bounce traffic that never interacts.

### 7.3 The free-tool funnel (the only funnel that exists)

| Step | Events | Persons | Conversion |
|---|---|---|---|
| `tool_generate_started` | 46 | 32 | — |
| `tool_generate_completed` | 31 | 23 | **67% of starts complete; 72% of starters** |
| `tool_pdf_downloaded` | 11 | 8 | **35% of completions exported; 25% of starters** |
| `tool_signup_completed` | 7 | 7 | **22% of starters signed up** |
| `tool_student_added` | 2 | 2 | **6% of starters reached the product's first real action** |

By tool:

| Tool | Started | Completed | PDFs | Unique users |
|---|---|---|---|---|
| Worksheet generator | 38 | 27 (71%) | 9 | 28 |
| Lesson-plan generator | 8 | 4 (50%) | 2 | 4 |

Page distribution (top): `/` 256 views / 212 persons · `/tools/worksheet` 114/101 ·
`/login` 41/40 · `/tools` 31/22 · `/signup/organization` 25/23 · `/tools/lesson-plan` 17/11 ·
`/blog` 13/9 · `/contact` 9/9 · `/privacy` 4/2 · `/terms` 2/2.

### 7.4 The finding — and it is a negative one

**There is no instrumentation of the Socratic tutoring loop.** Not a single event in the
project describes a tutoring session, a student turn, an AI question, a refusal to answer, a
profile update, a parent viewing a transcript, or a between-session support interaction. The
pathname distribution contains no authenticated application routes at all — no
`/dashboard`, no `/students`, no `/sessions`. There are **zero** `$ai_generation`,
`$ai_trace`, or `$ai_span` events, so the LLM layer is not wired to observability either.
The two `tool_student_added` events are the deepest the telemetry reaches into the product.

The PRD's stated **original-measurement opportunity for E2** — *"session completion, return
rate, question-depth distributions, drop-off points, and… whether Socratic sessions retain
learners better than answer-giving fallbacks"* — **cannot be delivered from the data that
exists.** What exists is a marketing-site and free-tools funnel.

This is reported as the section's principal `OBSERVED` result because it is a real finding
about the state of the field, not merely a gap in one product:

> **The product in this survey most explicitly designed around a falsifiable pedagogical
> claim has not instrumented the claim.** It measures acquisition to four decimal places and
> pedagogy not at all.

That is precisely the §5.7 pathology — measuring what the organisation controls — appearing
in the survey author's own work, three weeks into instrumentation, at 100 students. It is
included here rather than omitted because the survey's credibility depends on applying its
own test to itself first.

**Secondary `OBSERVED` results worth carrying:**

- **A third of generations are abandoned before completion** (46 → 31). For a synchronous
  single-prompt generator, a 33% abandonment rate is a latency or quality signal worth
  chasing, and it is consistent with the cold-start behaviour observed directly during
  retrieval for this section (`/privacy` and `/terms` served a "Waking up our servers" shell
  to an unauthenticated fetch on 2026-07-27).
- **Only 35% of completed generations were exported as PDF.** If the artefact is the value,
  two-thirds of successful generations produced nothing the user kept.
- **The lesson-plan generator completes at 50% vs. the worksheet generator's 71%** (n=8 vs.
  n=38 — well within noise, flagged as a hypothesis only). If it survives more data, the
  reading is that the higher-cognitive-load artefact is the one users abandon, which would be
  an argument for decomposing lesson-plan generation into staged confirmations.
- **`/privacy` was viewed 4 times by 2 persons and `/terms` twice by 2**, against 212 persons
  on the homepage. Empirically, **~1% of visitors read the privacy policy.** This is a small
  but real datum for §F8: consent architectures that route through policy pages reach
  essentially nobody, which is an argument for in-line, in-context disclosure of the kind
  LessonOrca actually implements ("AI-generated content is clearly labeled") over the kind
  the law contemplates.

---

## 8. Assessment against the survey's own criteria

### 8.1 Against the refusal engine (§F2)

**Satisfies, in design.** "Socratic method only… never gives answers directly," classified as
a *safety guardrail* rather than a feature, with per-organisation configurable guidelines.
This is the GPT Tutor arm of Bastani et al. shipped as a commercial default rather than as an
experimental condition — and as far as this session's retrieval can establish, it is the only
product in §2 that states withholding as an **exclusive** policy rather than a mode. Khanmigo
"guides learners to find the answer themselves"; Claude Learning Mode is a *mode* within a
general assistant; Study Mode is toggleable. LessonOrca claims no answer-giving path exists.

**Short of it, in three ways.**

1. **The refusal is unverified.** There is no published transcript audit, no red-team result,
   no adversarial evaluation, and — per §7.4 — no telemetry that would detect a refusal
   failure. "Never gives answers directly" is currently an assertion about a prompt. The
   survey's own §F3 standard (make generated behaviour *checkable*) is not met by the product
   that most needs it.
2. **Refusal is necessary but not sufficient, and the product does not distinguish the
   cases.** §H1's archetype table is explicit that for **reasoning/abstraction gaps**,
   *"discovery learning… is actively harmful here — this is well replicated,"* and the
   required design consequence is **explicit instruction over discovery**. A system that is
   Socratic *only*, with no explicit-instruction path, is by construction mis-specified for
   that archetype. "Socratic method only" is a stronger commitment than the evidence
   supports; the defensible version is *"never answers the question the student was assigned;
   may directly instruct on the prerequisite the student lacks."*
3. **The escape hatch is unmodelled.** A student blocked by a Socratic tutor at 11pm has
   ChatGPT in the next tab. Bastani's harm condition is not eliminated by one vendor
   refusing; it is *relocated*. A refusal engine with no theory of the substitute is
   measuring its own compliance, not the student's behaviour. This is the most important open
   question the product poses and it is not addressed anywhere in the retrieved material.

### 8.2 Against F5's learner model

**Satisfies:** persistence across sessions is the product's central premise, not a feature
("builds a learning profile… gets smarter with every interaction"); the model is **coupled to
action** rather than merely displayed — the pre-session flag ("Scored 45% on fraction word
problems last week. Computation is strong — focus on applied problems") converts state into a
generated lesson; and it is **portable** (full data export), which §F5 argues matters more
than accuracy.

**Short of it:** F5's central finding is that the frontier is *not* predictive accuracy but
**what the model is made of, who owns it, how long it lives, and whether it models error as
well as knowledge.** On that test:

- *What it's made of* — undisclosed. Free-text summaries, a skill graph, and a scored mastery
  vector have radically different failure modes and the product does not say which it is.
- *Who owns it* — the tutoring center, not the family. The child's longitudinal record dies
  when the center's subscription does. Export exists, but export **to the org**. §F5's
  lifelong-learner criterion is not met.
- *Error modelling* — the one retrievable example flags a **score** ("45%") and a
  **strength/weakness split**, not a misconception. Knowing a student failed fraction word
  problems is a fraction of the value of knowing *which* misconception produced the failure.
- *How long it lives* — three weeks of production data. Unknowable.

### 8.3 Against F8's oversight requirements

**This is where the product is strongest, and it is genuinely ahead of the field.** Four
concrete mechanisms:

1. *"Parents can view every AI conversation. Teachers see all student interactions."* —
   total, not sampled, oversight.
2. *"AI-generated content is clearly labeled"* — synthetic-origin disclosure at the point of
   consumption.
3. Human review gates on the paths that leave the system: profiles reviewed before sharing,
   flagged items requiring teacher attention, **parent emails reviewed before sending**.
4. COPPA-compliant parent linking; per-center data isolation; RBAC; full export.

Read against §5.2, this is the **inBloom lesson correctly learned**: the parent is not a
data subject to be notified, they are a *viewer with standing*. And read against §7.4's
finding that ~1% of visitors open the privacy policy, in-product visibility is the only
oversight mechanism that could possibly work.

**Short of it:**

- **The transparency is unverifiable from outside.** `/privacy` and `/terms` did not render to
  an unauthenticated fetch on 2026-07-27 (cold-start shell), so the actual COPPA mechanism,
  retention periods, subprocessor list, and deletion guarantees **could not be read**. A
  product whose central safety claim is transparency should have a machine-readable,
  always-available policy. Flagged `UNVERIFIED-IN-SESSION`.
- **Visibility is not review.** "Parents *can* view every conversation" is an affordance.
  Nobody has measured whether any parent ever does — and §7 shows the instrumentation to
  measure it does not exist. §F8's requirement is *effective* oversight; an unexercised right
  is not oversight, and the industry-wide default assumption that it is should be one of the
  survey's named failure modes.
- **Total visibility is in tension with adolescent trust.** A 16-year-old who knows every
  word is surfaced to a parent will not disclose confusion, which is exactly the disclosure
  the learner model depends on. §H1's *anxiety / learned helplessness* archetype makes this
  acute: for a student whose history is failure, a fully-surveilled channel is not a safe
  place to be wrong. The right design is almost certainly age-graduated and
  category-graduated (safety flags always escalate; struggle is private by default). The
  product treats transparency as a scalar.
- **§2.9's Canvas breach applies directly.** Full conversation logs of minors, retained
  indefinitely, are the highest-value target in the sector. The COPPA-compliance posture
  addresses *use*; it does not address *custody*. The mitigation is retention limits and
  minimisation, neither of which is stated.

### 8.4 Against H1's archetypes

Scored honestly against the seven archetypes in PRD §H1.1:

| Archetype | Status |
|---|---|
| **Attention / ADHD** | **Partial.** Timed lesson segmentation (10/25/10 min) is the right shape. But a Socratic dialogue is an *unbounded* interaction; nothing in the retrieved material caps turn count or detects disengagement, and §H1 warns the system will read disengagement as inability |
| **Working-memory limitation** | **Unaddressed, and Socratic-only makes it worse.** Question-chaining requires the student to hold prior turns in mind. §H1's requirement is to *externalise* memory — visible steps, persistent scaffolds, "never make the child hold state." A pure dialogue does the opposite by construction |
| **Long-term retention difficulty** | **Partial.** Continuity across sessions is the product's premise, but nothing indicates a **scheduled retrieval** mechanism (§F11). Pre-session flags are driven by *last session's* failure, which is recency, not spacing. Re-surfacing a mastered-then-decayed item is exactly what this archetype needs and there is no evidence of it |
| **Reasoning / abstraction gaps** | **Contradicted.** See §8.1(2). "Socratic method only" is the documented harmful condition for this archetype |
| **Processing speed** | **Satisfied by default.** Asynchronous, untimed, 24/7 |
| **Language / reading access** | **Unaddressed.** No TTS/STT, no dual coding, no language options in the retrieved material. A text-only Socratic tutor assesses physics through a reading test — §H1's named failure mode, verbatim |
| **Anxiety / learned helplessness** | **Ambiguous, and possibly negative.** Low-stakes and private-from-peers: good. But being questioned rather than answered, while a parent watches the transcript, is a high-threat configuration for a student with a failure history |

**Verdict:** LessonOrca is built for the median tutoring-center student. It satisfies 1.5 of
7 archetypes cleanly. §H1's whole argument is that this ordering is backwards — build for the
margin and the median comes free. This product is a clean example of the standard ordering,
and it is the survey author's own, which makes it the most useful possible illustration.

---

## 9. What E2 does not establish

Stated flatly so nothing in this file can be laundered upward:

1. **No efficacy claim.** There is no evidence, of any strength, that Socratic-only tutoring
   improves learning at LessonOrca. Not observational, not correlational. §7 measures a
   marketing funnel.
2. **No retention comparison.** The PRD's hoped-for "do Socratic sessions retain learners
   better than answer-giving fallbacks" cannot be answered — there is no answer-giving arm,
   no session instrumentation, and no control group.
3. **n = 100 students, 25 tutors, 3 centers, 21 days of analytics.** Every quantity in §7 has
   a denominator small enough that a single unusual user moves it.
4. **The Socratic constraint is unaudited.** No transcript sample, no adversarial test, no
   refusal-failure rate.
5. **The privacy and terms pages could not be read.** COPPA mechanism, retention, and
   subprocessors are `UNVERIFIED-IN-SESSION`.
6. **The author is the founder.** Every `VENDOR` claim in §6 is self-report by an interested
   party, and the reader should discount accordingly — which is why §8 was written
   adversarially and §7.4's principal result is a criticism.

**What E2 *does* establish**, and it is worth something: that a production system can commit
to answer-withholding as a *safety* property, expose every AI turn to an adult, gate every
outbound artefact on human review, and still be a shippable commercial product with paying
tutoring centers. The refusal engine is not a thought experiment. It is buildable, and the
constraint that stops it being validated is not technical — it is that nobody, including its
author, instrumented the pedagogy.

---

## 10. Deliverables this section owes the survey

1. **The primitive taxonomy (§2)** as the organising frame for the market chapter — nine
   design hypotheses, each with its own falsification condition.
2. **The evidence-gradient table (§2.3, ASSISTments)** — 0.61 → 0.22 → 0.10 → 0.03 as sample
   size rises and evaluator independence increases. Use it whenever a vendor effect size
   appears.
3. **Finding E1-b** — "time saved" as the field's substituted success criterion, and the
   Bastani-derived rule that *learner* time saved is a harm signal while *teacher* time saved
   is not.
4. **The graveyard's single cause of death (§5.7)** and the operational test it yields:
   *name the metric that would tell you your product is not working, and how long you would
   wait to see it.*
5. **The three convergent safety norms (Finding E1-c)** — total adult visibility,
   synthetic-origin labelling at point of consumption, no human impersonation — as candidate
   standards, with §7's ~1%-read-the-privacy-policy datum as the argument for why in-product
   beats in-policy.
6. **§8.4's archetype scorecard** as the template for auditing *any* product in §2 against
   H1 — including, and especially, the survey's own.
