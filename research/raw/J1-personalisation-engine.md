---
title: "The personalisation engine — which technique fires, on what signal, and how the system learns it chose wrong"
wave: J
section: J1
date_researched: 2026-07-28
sources_count: 78
status: raw-research
---

# J1 — The Personalisation Engine

> **The named conceptual gap.** Every section before this one catalogues *which techniques
> work*. None of them specifies the **selection policy**: given THIS learner, THIS topic,
> THIS moment — which technique fires, on what signal, with what latency, and how does the
> system learn it chose wrong? This section builds that policy, grades every proposed
> personalisation dimension, and states the experiment that would falsify the whole idea.

**Source reachability log (2026-07-28).** WebSearch exhausted per CLAUDE.md §5. Retrieval ran on
**Crossref** (working), **OpenAlex** (working), **ERIC API** (working), **Semantic Scholar**
(HTTP 429 for most of the session — used only where a second source corroborated), and targeted
`curl`/`WebFetch` of primary PDFs. **arXiv's API was unreachable for the entire session**
(`export.arxiv.org` returned empty bodies on every attempt across two hosts and four retries with
backoff) — no arXiv-only claim appears below. `psycnet.apa.org` returned 403; `citeseerx` returned
an empty body; the JEDM article portal returned 404 and was routed via the ERIC full-text mirror
instead. Primary PDFs successfully extracted and quoted verbatim: Cronbach (1975), Rafferty, Ying
& Williams (2019), Riedmann, Schäper & Lugrin (2025).

Evidence labels per CLAUDE.md §2: `MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH` · `OBSERVED`
· `VENDOR` · `DEMO` · `INFERENCE`. A `VENDOR` claim is never restated as a finding.

**Builds on, does not repeat:** F5 (learner model, PLM schema, KT ceiling, cold start),
F10 (explanation laddering, expertise-reversal numbers, preference corruption), H1 §1.4
(CBM/DBI, the two-clock architecture, Fuchs 1991, Van Norman 2023), B1 (the learning-science
floor), I1 (mechanism-survival taxonomy), F11 (Doroudi's field-level tally, spacing, retrieval),
F8 (EU AI Act Art. 5), AUDIT.md (tone: lead with what becomes buildable).

---

## 0. The thesis, stated so it can be wrong

Here is what becomes buildable this year, and it is genuinely new.

For fifty years the reason nobody could ship a real selection policy was not compute and not
ideology — it was **measurement cost**. Choosing the right technique for a learner requires
knowing where that learner sits *on this specific concept, right now*. The only instrument for
that was a pretest, and a pretest before every lesson costs more attention than the lesson. So
systems fell back on the two things that are free: what the learner *says* they prefer, and what
a *label* says about them. Both are documented dead ends (§1, §7.4).

Two things changed. First, the measurement problem was solved in the literature and then largely
ignored: **Kalyuga and Sweller's rapid dynamic assessment recovers an actionable expertise
estimate from one to three items in 15–40 seconds, correlating r = 0.66 to 0.92 with a full
diagnostic test** (§2.3). Second, a generative model can now *author* those probe items on the
fly, for any concept, at the moment of need — which is the one thing that made rapid assessment
impractical to deploy at scale in 2005.

Put those together and the selection policy becomes a small, cheap, auditable control loop rather
than a research programme. But it is a *small* loop, and the discipline of this section is to
keep it small:

> **There is exactly one personalisation axis in the entire corpus on which the *sign* of a
> treatment effect reliably flips with the learner: assistance level × prior knowledge, measured
> per concept.** `MEASURED-META` (Tetzlaff et al. 2025). Everything else is either a universal
> that should be always-on rather than selected, a plausible hypothesis that has not survived
> replication, or a fifty-year-old null wearing new clothes.

The engine that follows therefore has three parts, and the ordering is the argument:

1. A **universal substrate** that is never selected and never pivoted away from — retrieval
   practice with feedback, spacing, and expectancy framing. These are the largest measured
   effects in the corpus and they are *not personalised*. Conceding this is what makes the rest
   honest (§8).
2. A **fast loop** (seconds) that adjusts assistance level, rung, and granularity *within* a
   method, gated on a rapid probe and on error type. It may never change the method.
3. A **slow loop** (≥4 probe points) that changes the method, from a fixed ordered menu, with a
   logged reason — because measurement without a named decision rule is inert (Fuchs, Hamlett &
   Stecker 1991).

And the guardrails come in the same breath, not as an appendix: the probe is a *knowledge* probe,
never an affect probe (EU AI Act Art. 5(1)(f) makes emotion inference in education unlawful, and
that is good policy); the selection state is inspectable and contestable by the learner and the
guardian; and exploration on a child is spent only where the evidence is genuinely absent.

---

## 1. Aptitude–Treatment Interaction: the honest history, and it must lead

### 1.1 What Cronbach actually proposed, and what he actually found

Lee Cronbach's 1957 APA address proposed crossbreeding the "manipulating" (experimental) and
"correlating" (differential) schools into "a science of Aptitude × Treatment interactions (ATIs)."
Eighteen years later he returned to the same podium to report on it. The 1975 paper —
**Cronbach, L. J. (1975), "Beyond the Two Disciplines of Scientific Psychology," *American
Psychologist* 30(2):116–127, [10.1037/h0076829](https://doi.org/10.1037/h0076829)** — is the
field's central cautionary document, and it is not usually read. Full text retrieved and quoted
verbatim below. `OBSERVED` (primary source, author's own progress report)

Cronbach's framing of the design: *"The typical ATI study is a two-group experiment. The measure
of outcome is regressed onto a score recorded prior to treatment. If the regression lines in the
two treatments differ in slope, that is evidence of Aptitude × Treatment interaction."* Note what
this implies and what most modern "personalisation" claims skip: **an ATI claim is a claim about
a crossover of regression slopes, not about a subgroup mean.**

On abilities — the aptitudes everyone expected to work — the report is blunt:

> **"As for abilities, the interactions did not turn out as we had anticipated."**

And on the single most intuitive hypothesis in the entire programme, the one that is the direct
ancestor of every "visual learner" claim ever made:

> *"One hypothesis Snow and I pursued ran like this: 'High spatial ability makes for success when
> the instruction uses diagrams as much as possible, and minimizes words.'* **No interaction of
> this sort was found, in our shop (Markle, 1968) or elsewhere."**

`OBSERVED` — **NEGATIVE RESULT N1.** This is the origin point of the modality-matching myth, and
its own authors reported it as a null in 1975.

On personality × instructional press, where the programme's *best* results lived (Domino 1968/1971;
Majasan 1972 — 11 of 12 classes showed the predicted trend), Cronbach's summary of the
replication record is the sentence that should be printed above every adaptive-learning
architecture diagram:

> *"But results were strangely inconsistent from year to year and from course to course. Some
> effects were significantly moderated by sex or ability of the student. Insofar as a
> generalization can be glimpsed through the tangle of evidence, it is this: …"*

— and even the generalisation he then offers is immediately hedged: **"But the generalization is
weak, with many studies running counter to the trend."** `OBSERVED`

### 1.2 The hall of mirrors — why ATI is structurally hard, not merely under-powered

The paper's most-quoted passage is a claim about the *logic* of interaction research, and it
applies with undiminished force to a 2026 contextual bandit:

> *"An ATI result can be taken as a general conclusion only if it is not in turn moderated by
> further variables. If Aptitude × Treatment × Sex interact, for example, then the Aptitude ×
> Treatment effect does not tell the story.* **Once we attend to interactions, we enter a hall of
> mirrors that extends to infinity.** *However far we carry our analysis—to third order or fifth
> order or any other—untested interactions of a still higher order can be envisioned."*

And its companion, which is the real reason personalisation policies rot in deployment:

> **"Generalizations decay.** *At one time a conclusion describes the existing situation well, at
> a later time it accounts for rather little variance, and ultimately it is valid only as history.
> The half-life of an empirical proposition may be great or small.* **The more open a system, the
> shorter the half-life of relations within it are likely to be."**

`OBSERVED`. Cronbach's own conclusion for the field was to abandon the search for stable
interaction laws in favour of *"assess[ing] local events accurately, to improve short-run
control."* That is not a counsel of despair. **It is, almost exactly, a specification for a
control loop with a short memory and a live measurement — which is what §4 builds.** The
difference between 1975 and 2026 is that "assess local events accurately" was then a research
aspiration and is now a 20-second API call.

### 1.3 The post-mortem literature agrees on the diagnosis

**Driscoll, M. P. (1987), "Aptitude-Treatment Interaction Research Revisited,"
[ERIC ED285532](https://eric.ed.gov/?id=ED285532).** `OBSERVED` — reviews *"four methods or
assumptions that might explain why ATI research has not generated the anticipated empirical
support: (1) the lack of a theoretical base; (2) disagreement over what a given aptitude means and
how it should be measured; (3) difficulties in defining instructional methods as treatments; and
(4) the inability to generalize from context-specific results."* Driscoll's own forward-looking
note in 1987 identifies the exit that the field eventually took: *"increased recognition of the
role of **prior knowledge** as an aptitude variable and the more precise definition of
instructional treatments."*

**Snow, R. E. (1991), "Aptitude-Treatment Interaction as a Framework for Research on Individual
Differences in Psychotherapy," [ERIC EJ428196](https://eric.ed.gov/?id=EJ428196).** `OBSERVED` —
Snow writing a *lessons-learned* document for a neighbouring field. The abstract's list of
required correctives is itself the indictment: *"aptitude distributions, multivariate aptitude
complexes, detective work with scatterplots, disattenuation, treatment and therapist
characteristics, therapist-client matching, ecological validity, outcome variables, **statistical
power**, aggregation, and person independence."* A framework that needs eleven methodological
correctives before it yields a usable result is not a framework you deploy against a child's
Tuesday afternoon.

### 1.4 Which ATIs survived — there are two, and they are the same one

**(a) The Snow generalisation: ability × information-processing load.** The Stanford Aptitude
Research Project's own final report states the one result that came out of two decades of work:

> *"Research on aptitude-instructional treatment interactions has shown that* **the relation of
> general ability to learning tends to increase as instruction places increased information
> processing burdens on learners and to decrease as instruction is designed to reduce the
> information processing demands on learners."**

**Snow et al. (1980), *Aptitudes and Instructional Methods: Research on Individual Differences in
Learning-Related Processes*, Final Report 1975–1979,
[ERIC ED204407](https://eric.ed.gov/?id=ED204407).** `OBSERVED` — this is the survivor. Cronbach
states the same finding in 1975 in regression terms: *"the regression of outcome onto general
ability tends to be relatively steep when the instruction requires the learner to actively
transform information, and it tends to be shallow when the demands are less."*

**(b) Expertise reversal.** The modern, better-measured, per-topic version of exactly the same
mechanism (§2).

**These are not two findings.** Chen, Kalyuga & Sweller (2017) demonstrate that the expertise
reversal effect *"is a variant of the more general **element interactivity** effect"* — both
*"rely on equivalent changes in element interactivity"*
([10.1007/s10648-016-9359-1](https://doi.org/10.1007/s10648-016-9359-1)) `OBSERVED`. Snow's
finding says: instructional load interacts with the learner's capacity to absorb it. Kalyuga's
finding says: instructional support interacts with the schemas that would otherwise have to carry
that load. **The surviving ATI is one law about the fit between the load an activity imposes and
the structures the learner already has.** That is the entire evidenced basis for personalisation,
and it is enough to build on.

**The difference that matters for engineering:** Snow's version indexes the learner by a *trait*
(general ability), which is stable, expensive to measure, legally fraught, and not actionable.
Kalyuga's version indexes the learner by *prior knowledge of this concept*, which is unstable by
design (it is what instruction is trying to change), cheap to measure, and directly actionable.
**Build on (b). Cite (a) as the reason to believe (b) generalises.**

### 1.5 Working memory as an ATI axis — plausible, not evidenced

WM capacity is the obvious candidate for a second axis, and there is a 2025 review arguing exactly
that: **Working Memory and Instructional Fit: Reintroducing Aptitude–Treatment Interaction in
Education Research, *Behavioral Sciences* 15(6):765,
[10.3390/bs15060765](https://doi.org/10.3390/bs15060765).** `OBSERVED` — but read the genre
honestly: it is a **narrative review**, not a meta-analysis, and its own framing is prospective
(*"highlights how this framework **can guide** the development of adaptive instructional
strategies"*). It reports no pooled crossover interaction. Grade: **PLAUSIBLE**, not EVIDENCED.

Two constraints kill WM as a *deployable* selection variable even if the interaction is real:

- **NEGATIVE RESULT N2 — WM is not modifiable.** Melby-Lervåg, Redick & Hulme (2016),
  *Perspectives on Psychological Science*,
  [10.1177/1745691616635612](https://doi.org/10.1177/1745691616635612): 87 publications, 145
  experimental comparisons. *"For measures of far transfer (nonverbal ability, verbal ability,
  word decoding, reading comprehension, arithmetic) there was **no convincing evidence of any
  reliable improvements** when working memory training was compared with a treated control
  condition."* `MEASURED-META`. Corroborated by Schwaighofer, Fischer & Bühner (2015),
  *Educational Psychologist*, [10.1080/00461520.2015.1036274](https://doi.org/10.1080/00461520.2015.1036274):
  far transfer *"small, limited to nonverbal (g = 0.14) and verbal (g = 0.16) ability and **not
  sustained at follow-up**."* `MEASURED-META`
- **Measuring WM per session is not cheap**, unlike a 2-item knowledge probe. A span task is
  minutes, not seconds, and it is off-task minutes.

The practical resolution: **do not measure WM; measure load.** Self-reported mental effort (one
tap, Paas scale) is a legal, cheap, on-task proxy that indexes the same quantity the policy
actually needs, and Kalyuga & Sweller (2005) used exactly *"rapid tests of knowledge combined with
measures of cognitive load"* in the trial that worked. WM belongs in the **PLAUSIBLE** row of §9,
and its practical role is as a *reason to believe the load axis is real*, not as an input.

### 1.6 What the honest history licenses

1. **Do not claim a personalisation dimension without a crossover.** A subgroup mean difference is
   not an ATI; it is a moderator at best and a fishing expedition at worst.
2. **Expect the dimension to decay.** Cronbach's half-life argument means a selection policy needs
   a live measurement, not a fitted parameter, and needs to be re-validated rather than trusted.
3. **Prefer the axis whose theory is mechanistic.** Element interactivity explains *why* the sign
   flips. "Visual learner" explains nothing, which is why it never replicated (§7.4).
4. **The word "personalisation" has been carrying fifty years of noise.** The honest version of the
   product claim is narrow and it is still large: *we measure where you are on this concept and we
   set the assistance level accordingly, per concept, continuously.*

---

## 2. The one selection rule with real evidence — and how to measure it in 30 seconds

### 2.1 The magnitudes (verified, with a standing correction carried forward)

**Tetzlaff, Simonsmeier, Peters & Brod (2025), "A cornerstone of adaptivity — A meta-analysis of
the expertise reversal effect," *Learning and Instruction*,
[10.1016/j.learninstruc.2025.102142](https://doi.org/10.1016/j.learninstruc.2025.102142).**
PRISMA; 1,590 studies screened → **176 effect sizes from 60 experimental studies, N = 5,924**;
`metafor` with dependency handling. `MEASURED-META`

| Comparison | Effect |
|---|---|
| **Low prior knowledge**: high- vs. low-assistance instruction | **d = 0.505**, 95% CI [0.260, 0.750], k = 88, I² = 90.9% |
| **High prior knowledge**: high- vs. low-assistance instruction | **d = −0.428**, 95% CI [−0.647, −0.209], k = 88, I² = 87.6% |
| The reversal itself (interaction) | reported in B1 as **d = 0.971** [0.631, 1.312]; **flagged unverifiable from the abstract in F10**; the two verified marginals differ by **≈0.93** |

⚠️ **Standing correction (CLAUDE.md §8).** `d = 0.971` is recorded as *retired pending full text*.
This section reports **0.505 / −0.428 / ≈0.93** and does not restate 0.971 as a finding.
`UNVERIFIED-IN-SESSION`.

Four properties of this result do all the engineering work:

1. **Asymmetry.** *"Providing novices with assistance has a stronger effect than withholding
   assistance from experts."* The authors' own instructional implication: **"rather provide
   assistance than to withhold it when in doubt."** → *Under uncertainty, assist. A low entry is a
   default, not a diagnosis.*
2. **Heterogeneity ≈ 90%.** The reversal point is **not a fixed threshold**. Any system claiming a
   universal "fade at 80% mastery" constant is asserting something the meta-analysis explicitly
   does not support.
3. **Moderated by how prior knowledge was assessed.** The measurement instrument is a significant
   moderator of the effect you are trying to exploit. **The probe is not incidental to the system;
   it is the system.**
4. **Weaker for younger students and in humanities/language learning.** A ladder for a 10-year-old
   learning vocabulary does not get to assume this mechanism. This is a scope boundary, stated up
   front, not a caveat buried at the end.

### 2.2 It is per-topic, not per-person — and this is the whole design consequence

Chen, Kalyuga & Sweller's element-interactivity framing makes the unit of analysis explicit: a
learner's position on the assistance axis is a function of *element interactivity relative to the
schemas they hold*, which are concept-specific. `OBSERVED`

The engineering consequence is severe and liberating at once. There is no `learner.expertise`
field. There is `learner.expertise[concept]`, and it is stale the moment instruction succeeds.
This is why the trait-based personalisation of the 1970s could not work even in principle: it
indexed a per-concept quantity with a per-person variable.

It also means the estimate must be recovered *at concept entry*, which is a problem only if
recovering it is expensive. It is not.

### 2.3 The minimum viable prior-knowledge probe — the numbers

This is the load-bearing retrieval of this section, and the literature is better than its citation
count suggests. Kalyuga's rapid-assessment programme replaces the pretest with a **first-step /
rapid-verification** task: show a partially worked solution, ask for the immediate next step (or
ask the learner to verify a proposed step), and score the *first response* under time pressure.
The construct being measured is *"the extent to which working memory limits have been altered by
solution schemas held in long-term memory."*

| Study | Domain / N | Correlation with full diagnostic | Time saving |
|---|---|---|---|
| **Kalyuga & Sweller (2004)**, *J. Educational Psychology* 96(3):558–568, [ERIC EJ685015](https://eric.ed.gov/?id=EJ685015) | algebra & geometry, Grades 9–10 | **up to r = .92** vs. traditional measures | **× 4.9** and **× 2.5** faster |
| **Kalyuga (2006)**, *Learning and Instruction*, [10.1016/j.learninstruc.2005.12.002](https://doi.org/10.1016/j.learninstruc.2005.12.002) | arithmetic word problems, **N = 55, Grade 8** | **r = 0.72** | **× 2.8** faster |
| **Kalyuga (2006)**, *Educational Psychology*, [ERIC EJ753417](https://eric.ed.gov/?id=EJ753417) | reading skill | **r = 0.66**, with *"a substantial increase in reliability"* | **× 3.8** faster |
| **Kalyuga & Sweller (2008)**, *JEP* 100(3):603, [10.1037/0022-0663.100.3.603](https://doi.org/10.1037/0022-0663.100.3.603) | kinematics + graph transformation, **N = 33** | *"high degree of correlation"* with in-depth diagnosis from video + concurrent verbal reports | rapid verification method |

`MEASURED-RCT` / `MEASURED-BENCH` (validation studies against a criterion instrument).

**And it was shown to work as a controller, not just as a measure.** Kalyuga & Sweller (2005),
*ETR&D*, [10.1007/BF02504800](https://doi.org/10.1007/BF02504800) — elementary algebra tutor,
**yoked control design**: instruction *"dynamically tailored to changing levels of expertise using
rapid tests of knowledge combined with measures of cognitive load… The experimental group
demonstrated **higher knowledge and cognitive efficiency gains** than the control group."*
`MEASURED-RCT`. Corroborated by **Blayney, Kalyuga & Sweller (2015)**, *ETS*,
[ERIC EJ1078240](https://eric.ed.gov/?id=EJ1078240): Experiment 2 assigned instructional format
**by pre-test of prior knowledge** vs. random assignment — *"the adaptive instruction group was
superior to the non-adaptive group."* `MEASURED-RCT`

### 2.4 The probe specification (the deliverable's first component)

Derived from the above. `INFERENCE` on the packaging; the components are each measured.

```
PROBE(concept c, learner L):
  P  ← prerequisite closure of c, transitively closed   # F10 D1
  for p in the 2–3 highest-leverage members of P:
      present a partially-completed instance at the midpoint of p's canonical procedure
      ask: "what is the immediate next step?"   (first-step)
        OR: "is this step correct?"             (rapid verification — cheaper to score)
      record: correctness, latency_ms
  ask once: "how much mental effort did that take?"  (Paas 9-point, one tap, SELF-REPORT)
  return: ordinal level per p ∈ {absent, partial, held}, + a load reading
  budget: ≤ 3 items, ≤ 40 s, ≤ 1 turn
```

Four design rules that follow from the evidence rather than from taste:

- **Ordinal, not continuous.** The policy needs to pick an assistance level from a small set. It
  does not need a calibrated probability. This is why the *policy's* cold-start problem is far
  smaller than the *predictor's*: F5 reports DKT needing ~10 interactions and Best-LR ~60 to reach
  near-peak accuracy (Gervet et al. 2020) `MEASURED-BENCH` — but a 2-item probe yields an
  actionable ordinal on interaction zero.
- **Score the first response only.** The construct is schema availability, which is destroyed by
  letting the learner work it out.
- **Generate the probe items fresh each time.** Otherwise the probe becomes a memorised item and
  measures the wrong thing. This is the specific capability a frontier model adds that Kalyuga did
  not have in 2005, and it is why this is buildable now.
- **Never reuse a probe item as an instructional item in the same session.** Pan & Rickard (2018)
  found retrieval transfer is *weakest* to rearranged stimulus–response items
  ([10.1037/bul0000151](https://doi.org/10.1037/bul0000151)) `MEASURED-META`; a probe that doubles
  as practice contaminates both readings.

**Adaptive-testing theory supplies the stopping rule, not the item count.** The classical CAT
result (Weiss 1982, *Applied Psychological Measurement*,
[10.1177/014662168200600408](https://doi.org/10.1177/014662168200600408)) `OBSERVED` is that
*"through appropriate combinations of item pool design and use of different test termination
criteria, adaptive tests can be designed to improve both measurement quality and measurement
efficiency."* The relevant modern refinement is the **predicted standard error reduction (PSER)**
stopping rule (Choi, Grady & Dodd 2011, *EPM*,
[ERIC EJ914074](https://eric.ed.gov/?id=EJ914074); extended in *International Journal of Testing*
2020, [ERIC EJ1254419](https://eric.ed.gov/?id=EJ1254419)) `MEASURED-BENCH`, which *"administers
fewer items when predictive gains in information are small"* — i.e. it stops when the *next* item
would not change the decision. That is precisely the right criterion for a probe whose only job is
to select among three assistance levels: **stop as soon as the remaining uncertainty cannot flip
the decision.** For a 3-level decision that is typically one or two items.

---

## 3. Entry-level selection for laddered explanation — the ELI question, answered as measurement

### 3.1 What F10 established and what it left open

Carried forward, not re-derived:

- **Three rungs beat two** — ANOVA F(2,56) = 3.670, **p = 0.032**, ηp² = 0.116; Mdiff = 0.99,
  p = 0.037. `MEASURED-RCT`
- **Five rungs did not beat three** — Mdiff = 0.16 [−0.78, 1.09], **p = 0.738**. `MEASURED-RCT`
  ([ERIC EJ1510953](https://eric.ed.gov/?id=EJ1510953))
- **Preference is a corrupted signal** — across three RCTs, infographic vs. plain-language
  summary moved **preference d ≈ 0.48** and **knowledge zero**
  ([10.1016/j.jclinepi.2017.12.003](https://doi.org/10.1016/j.jclinepi.2017.12.003)).
  `MEASURED-META`

What F10 did **not** specify: the signal that selects the entry rung, and the detector that fires
when the rung was wrong. That is this subsection.

### 3.2 The entry rule

The rung is a *level of assistance and abstraction*, so the expertise-reversal axis is the correct
one, and the probe of §2.4 is the correct instrument. The rule:

```
ENTRY(concept c, learner L):
  P     ← prerequisite closure of c
  m     ← PROBE(c, L)                        # §2.4, ≤3 items, ≤40 s
  rung  ← min over p ∈ P of level(m[p]) − 1  # weakest link, then one lower
  clamp rung to the 3 rungs actually instantiated for c
```

Three warrants, each independently sourced:

- **Weakest link, not average.** A rung is interpretable only if *every* prerequisite it invokes is
  held. Averaging across P hides exactly the gap that will break the explanation. Warrant:
  element interactivity is computed over the whole set of interacting elements (Chen, Kalyuga &
  Sweller 2017). `INFERENCE` from a measured mechanism.
- **Minus one.** Tetzlaff's asymmetry: under-assisting a novice costs more (+0.505) than
  over-assisting an expert costs them (−0.428). The expected cost of entering one rung low is
  strictly smaller than the expected cost of entering one rung high. `INFERENCE` from
  `MEASURED-META`.
- **Three rungs instantiated, five authored.** Five rungs exist so different learners can *enter*
  at different points; any individual learner traverses two or three. The p = 0.738 null forbids
  making a learner climb five.

### 3.3 The wrong-rung detector, and its latency

This is the part nobody specifies, and it is where most adaptive tutors go wrong: they detect
"struggling" from *errors*, which is the noisiest available signal.

**Rung too high** — detected by a **generation probe**, not by an error. Ask the learner to restate
the rung's central claim in their own words, or to predict one consequence of it. Warrant: F11
§5.2 (the generation effect is the mechanism an LLM can actually manipulate) and F10 §8.4 (the
learner-produced rung is the highest-information probe available). If the restatement drops or
contradicts a load-bearing proposition, the rung was too high.
**Latency: within 2 exchanges (~60–90 s).** `INFERENCE` from measured components.

**Rung too low** — detected by the **transfer + effort conjunction**: a near-transfer item answered
correctly *and* self-reported effort low *and* latency below the item's population median. Any one
of these alone is noise; the conjunction is a real fade signal.
**Latency: within 1 probe cycle (~2 min).** `INFERENCE`

**Why transfer and not retention.** This is the single most important measurement decision in the
ladder, and it comes from a partial null:

> **NEGATIVE RESULT N3.** Rey & Fischer (2013), *Instructional Science*, N = 93, expertise induced
> experimentally, 2×2 (novice/expert × explanation present/absent) — the closest experimental
> analogue in existence to "give an ELI-explanation to an expert":
> *"The expertise reversal effect was **replicated for the dependent measure transfer, but not for
> retention**."* [ERIC EJ999802](https://eric.ed.gov/?id=EJ999802) `MEASURED-RCT`

**A ladder that measures itself with recall tests cannot see the damage it is doing.** The
wrong-rung detector must be a transfer item. If the system's only instrument is "did they remember
it," over-assistance is invisible by construction.

### 3.4 Fade on evidence, and the cost of not fading

> **NEGATIVE RESULT N4.** Nückles et al. (2010), *Instructional Science*, two longitudinal
> journal-writing studies over a term. Experiment 1: the prompted group beat control in the first
> half of the term and then **lost its superiority** as controls internalised the strategies.
> Experiment 2, fading vs. permanent prompts: *"at the end of the term, the **permanent prompts
> group showed substantially lower learning outcomes** than the fading group… the more the
> students became skilled… the more the external guidance by prompts became a **redundant stimulus
> that interfered** with the students' internal tendency to apply the strategies."*
> [ERIC EJ880291](https://eric.ed.gov/?id=EJ880291) `MEASURED-RCT`

Support that is not withdrawn turns negative. And the positive control exists too: **Salden,
Aleven, Schwonke & Renkl (2010)**, *Instructional Science*, Cognitive Tutor, three arms —
*"Both experiments provide evidence of improved learning results from **adaptive fading over fixed
fading over problem solving**."*
[10.1007/s11251-009-9107-8](https://doi.org/10.1007/s11251-009-9107-8) `MEASURED-RCT`

That is the cleanest existing demonstration that a *selection policy* on this axis beats both a
fixed schedule and no policy at all. It is the closest thing the corpus has to a proof of concept
for J1.

### 3.5 What must not select the rung

- **Not preference.** d ≈ 0.48 on liking, zero on knowledge (§3.1).
- **Not a readability formula.** F10 §10.1 documents that optimising rungs against readability
  metrics *reduces* comprehension.
- **Not self-assessed understanding.** Scharrer et al. (2017), *Public Understanding of Science*:
  simplified science makes laypeople *"rely overly strongly on their own epistemic capabilities"* —
  the ELI10 rung actively inflates the signal you would be reading. `MEASURED-RCT` (via F10)
- **Not a declared grade level or age.** It is a per-concept quantity (§2.2).

---

## 4. The pivot policy, formalised — the two-clock controller

### 4.1 The two findings that constrain the whole design

**Constraint A — measurement without a decision rule is inert.** Fuchs, Hamlett & Stecker (1991),
*AERJ* 28(3), [10.3102/00028312028003617](https://doi.org/10.3102/00028312028003617): 33 teachers
randomly assigned to CBM + expert-system instructional consultation, CBM without it, or no CBM.
*"Compared to the control group, **both** CBM groups appeared to revise students' instructional
programs more frequently. However, **only the CBM-ExS group effected superior achievement**."*
`MEASURED-RCT`

**Read that twice.** The arm that measured more and changed more but was not told *what* to change
did not move achievement. Dashboards, mastery bars, streaks, and "the system adapts" are the
CBM-NExS condition. **The decision rule is the product; the measurement is the input.**

**Constraint B — pivoting fast is fitting noise.** Van Norman, Klingbeil, Truman & Nelson (2023):
on weekly academic probes, **trend-based non-response judgements are not statistically viable for
7–10 weeks**. `MEASURED-BENCH`. Related: Van Norman & Christ (2016) on the accuracy of three-point
decision rules ([10.17105/spr45-3.296-309](https://doi.org/10.17105/spr45-3.296-309)) and
visual-analysis-vs-decision-rules ([10.1016/j.jsp.2016.07.003](https://doi.org/10.1016/j.jsp.2016.07.003))
`MEASURED-BENCH`; Ardoin, Christ, Morena & Cormier (2013), systematic review of CBM-R decision
rules ([10.1016/j.jsp.2012.09.004](https://doi.org/10.1016/j.jsp.2012.09.004)) `OBSERVED`.

A tutor that changes method after two wrong answers is operating far inside the noise floor, and
it destroys the consolidation that any method needs in order to work.

### 4.2 The controller

Constraints A and B look contradictory — *decide, but slowly*. They are reconciled by separating
**what** is being decided. H1 §1.4 established the two-clock frame; J1's contribution is to
specify the permission boundary precisely, because that boundary is the entire safety property.

| | **Fast loop** | **Slow loop** |
|---|---|---|
| **Signals** | error *type* (slip / misconception / prerequisite gap, from distractor identity); first-response correctness; latency vs. item median; hint requests; self-reported effort (Paas); generation-probe fidelity; near-transfer probe | one graphed score per session on a **freshly generated, fixed-difficulty probe of the same construct**, plotted against a goal line |
| **Latency to act** | 1 turn (seconds) to 2 exchanges (~90 s) | ≥ 4 probe points before any action; **7–10 weeks** before a *trend* claim is defensible |
| **May change** | assistance level · rung (± 1) · granularity of *this* item · representation of *this* item · whether a worked step is shown · probe format (transfer vs. retention) · immediate re-teach of a named prerequisite | **the method** — one named item from the §5 menu |
| **May NOT change** | **the method**; the concept; the goal; the schedule; the assessment construct | more than one method per dwell window; anything without a logged reason |
| **Anti-thrash** | rung may move ±1 per exchange, max 2 rung moves per concept per session | **minimum dwell = 4 probe points.** A method change before 4 points is prohibited by construction, not by policy |
| **Audit** | every fast-loop action writes `(signal, rule_id, action, ts)` to the evidence log | every slow-loop action writes `(4+ probe points, goal line, menu_item_id, reason_template, actor, ts)` and is surfaced to learner and guardian |

`INFERENCE` — synthesised from Fuchs et al. 1991 (change must be principled and named), Van Norman
et al. 2023 (trend latency), Kalyuga & Sweller 2005 (within-session probe-driven tailoring works),
Salden et al. 2010 (adaptive fading > fixed fading > none), Nückles et al. 2010 (unfaded support
turns negative), Stockard et al. 2018 (dosage/consolidation).

### 4.3 The three properties that make this a controller rather than a vibe

1. **The fast loop is bounded in what it can destroy.** It cannot abandon a method, so the
   consolidation argument (Constraint B) is satisfied *structurally* rather than by asking the
   model to be patient. This is the design point that most LLM tutors violate: given a free-text
   policy, a model will happily switch pedagogy mid-paragraph.
2. **The slow loop cannot fire without naming its action.** The menu is closed and the reason is a
   template instantiation, not free generation. This is Fuchs 1991 implemented as a type system.
3. **Responsiveness is preserved without method-thrash** because the fast loop's action space is
   genuinely rich — assistance level, rung, granularity, representation, prerequisite drop-back —
   and *all* of those are within-method moves. The learner experiences a highly responsive system;
   the method underneath is stable for weeks. The felt responsiveness and the statistical patience
   are not in tension once the action spaces are separated.

### 4.4 The stopping rule that is not optional

Non-response is a **designed-for state**, not an error. The controller must define, in advance,
the condition under which it stops adapting and escalates to a human: *k* consecutive slow-loop
method changes without the probe series crossing the goal line. H1 R4 makes this non-negotiable
(Al Otaiba & Fuchs 2006; DBI step 5), and it is also the AI Act Art. 26(2) human-oversight
obligation discharged in a concrete mechanism rather than a policy document.

---

## 5. What to pivot TO — the menu, and precedence when two rules fire

A decision rule without a principled next action is a random walk with paperwork. The menu is
ordered by the largest **independent** effect estimate available for each component in this
corpus. Where a component's best estimate is not a pooled effect size, that is stated rather than
invented.

### 5.1 The universal substrate — always on, never selected

**This is the most important structural claim in the section.** The three largest measured effects
in the corpus are not personalisation dimensions. They belong in the substrate, running for every
learner on every concept, and they are never the thing you "pivot to."

| # | Always-on mechanism | Best estimate | Source |
|---|---|---|---|
| U1 | **Retrieval practice with corrective feedback** | **g = 0.499** [0.442, 0.557], **222 studies, 48,478 students, classroom settings** | Yang, Luo, Vadillo, Yu & Shanks (2021), *Psych. Bulletin*, [10.1037/bul0000309](https://doi.org/10.1037/bul0000309) `MEASURED-META` |
| U2 | **Spacing**, gap ≈ 10–20% of the target retention interval | **d = 0.54** [0.31, 0.77] on curriculum materials; of 271 massed-vs-spaced comparisons only 12 showed no or negative effect | classroom meta-analysis 2025 (PMC12189222); Cepeda et al. (2006), [10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354) `MEASURED-META` |
| U3 | **Expectancy framing** — tell the learner they will have to teach it, before they study | **g = 0.48** [0.34, 0.63] with teaching expectancy vs. **g = −0.02** [−0.14, 0.11] without | Kobayashi (2024), k = 39, via C3 `MEASURED-META` |

U3 deserves emphasis because it is the largest free lever in the entire corpus and it is a
*sentence spoken before the lesson starts*. The contrast g = 0.48 vs. g = −0.02 is not a moderator;
it is the effect. `MEASURED-META`

**Design rule: you never pivot to retrieval practice. You pivot *within* a system that already
does retrieval practice.** Anything in the substrate that is presented as a personalisation win is
a category error — and it is the specific category error that makes most adaptive-learning
efficacy claims unreproducible, because the adaptive arm and the control arm differ in the
substrate rather than in the policy (§8.2).

### 5.2 The pivot menu — ordered

Fired by the slow loop only, one item, logged.

| Order | Action | Warrant | Estimate |
|---|---|---|---|
| **M1** | **Raise assistance: worked example / explicit model before requiring production** | Barbieri, Miller-Cotto, Clerjuste & Chawla (2023), *EPR*, 8,033 abstracts screened → 43 articles / 55 studies / 181 ES, RVE, [10.1007/s10648-023-09745-1](https://doi.org/10.1007/s10648-023-09745-1) | **g = 0.48** `MEASURED-META` |
| **M2** | **Drop to the weakest prerequisite and re-teach it** | element interactivity; DBI step 3; F10 weakest-link rule | no pooled ES; mechanism-level `INFERENCE` |
| **M3** | **Reduce granularity — segment the task further** | Swanson & Sachse-Lee (2000): segmentation carries significant variance in the LD intervention literature | component-level `MEASURED-META` (via H1) |
| **M4** | **Add an emphasis/signalling channel — but only if the probe says low prior knowledge** | Schneider et al. (2018), k = 209: **g = 0.43** [0.35, 0.50]; Richter, Scheiter & Eitel (2016): r = 0.17, benefit **concentrated in low-prior-knowledge learners**, [10.1016/j.edurev.2015.12.003](https://doi.org/10.1016/j.edurev.2015.12.003) | **g = 0.43** overall, gated `MEASURED-META` |
| **M5** | **Change representation along the concreteness ladder, faded** | Fyfe, McNeil, Son & Goldstone (2014), [10.1007/s10648-014-9249-3](https://doi.org/10.1007/s10648-014-9249-3) — ⚠️ **systematic review with no pooled effect size** (standing correction, CLAUDE.md §8) | direction only; **no ES** `MEASURED-META` |
| **M6** | **Change modality to remove a non-target load** (TTS, STT, dictation) | multimedia modality principle; accessibility-first (H1) | small, principle-level |
| **M7** | **Increase dosage / distributed review before concluding non-response** | Stockard et al. (2018) dosage effect (via H1) | `MEASURED-META` |
| **M8** | **Escalate to a human.** Non-negotiable stopping rule | Al Otaiba & Fuchs (2006); DBI step 5; AI Act 26(2) | not an effect claim |

**What is deliberately absent from the menu:** anything indexed on a sensory-modality label
(§7.4), anything indexed on preference (§3.5), and anything indexed on an inferred emotional or
diagnostic state (§7.5). Their absence is enforced by the menu being closed.

### 5.3 Precedence — when two rules fire at once

Deterministic, published, and testable. `INFERENCE` on the ordering; each rung is sourced.

| Rank | Precedence rule | Why it outranks the next one |
|---|---|---|
| **P0** | **Safety / safeguarding escalation** preempts everything and halts the loop | F8; a disclosure is not a pedagogical event |
| **P1** | **Named misconception → refutation**, not re-explanation | You cannot scaffold a learner past a belief they hold. The belief is the obstacle, and it is *diagnosed*, not inferred: the chosen distractor maps to a named misconception id (F5 §6, L4). Re-explaining at higher assistance leaves the belief intact |
| **P2** | **Prerequisite gap → drop back (M2)**, before any rung or representation change | A missing prerequisite is not a presentation problem. Presenting the same missing thing more vividly is the most common failure mode of generative tutors |
| **P3** | **Assistance-level change (M1/M4)** before representation change (M5/M6) | The assistance axis has a meta-analytic crossover (d = 0.505 / −0.428). The representation axis has direction without a pooled magnitude. Prefer the better-evidenced lever |
| **P4** | **Fast-loop action** before slow-loop action, always | If a within-method move is available, take it. Method changes are expensive in consolidation and are capped at one per dwell window |
| **P5** | **Do nothing** beats acting on a single signal | One wrong answer is not a signal. The floor for a fast-loop action is the *conjunction* specified in §3.3; the floor for a slow-loop action is 4 probe points |

P5 is the rule most systems lack and it is the one that makes the others survive contact with
noise.

---

## 6. Contextual bandits, RL, and adaptive experimentation — what has been MEASURED

### 6.1 The field-level tally (carried from F11 §4.7, because it is still the organising fact)

**Doroudi, Aleven & Brunskill (2019), *IJAIE* 29:568–620,
[10.1007/s40593-019-00187-x](https://doi.org/10.1007/s40593-019-00187-x)** — every empirical study
comparing a model-induced instructional policy to a baseline on a learning outcome, sorted by what
is being sequenced. `MEASURED-META`

| Cluster | Sig | ATI | Mixed | **Not sig** | Sig **worse** |
|---|---|---|---|---|---|
| All studies | 21 | 4 | 4 | 11 | 1 |
| **Paired-associate / flashcard (spacing)** | **11** | 0 | 0 | 2 | 1 |
| Concept-learning tasks | 4 | 0 | 2 | 1 | 0 |
| **Sequencing interdependent content** | **0** | **0** | **2** | **6** | **0** |
| Sequencing activity types (worked example vs. problem solving) | 4 | 4 | 0 | 2 | 0 |
| Maximizing other objectives | 2 | 0 | 0 | 0 | 0 |

Verbatim, pp. 586–587: *"when it comes to sequencing interdependent content, **there is not yet
evidence that RL can induce instructional policies that are significantly better than reasonable
baselines**."* And: *"**only three out of 15 studies that were run in classroom settings** found an
RL-induced policy was significantly better than baselines."* Of the 24 studies reporting a
significant effect or ATI, **17 (71%) compared against a *random* baseline**.

### 6.2 The 2025 replication of that tally — new to this section, and it lands the same way

**Riedmann, A., Schäper, P. & Lugrin, B. (2025), "Reinforcement Learning in Education: A Systematic
Literature Review," *IJAIED* 35:2669–2723,
[10.1007/s40593-025-00494-6](https://doi.org/10.1007/s40593-025-00494-6)** — PRISMA, **89
manuscripts, 2000–2024**, IEEE Xplore + Google Scholar + ACM. Full text retrieved and read.
`MEASURED-META`

Evaluation strategy: **live with real learners n = 41; real interaction datasets n = 23; simulated
users n = 24.** So roughly *half* the field never touches a learner.

Their Table 2, which is the most useful single table published on this question since Doroudi:

| Level of significance | **Guidance-related** | **Content-related** | Total |
|---|---|---|---|
| ≥1 RL policy outperforming baseline | **14** | **4** | 18 |
| Significant ATI effect | 2 | 0 | 2 |
| Mixed results | 8 | 3 | 11 |
| **No significant effect** | 3 | 1 | 4 |
| **No statistical comparison at all** | 9 | **45** | **54** |

Four findings, and three of them are negative:

- **NEGATIVE RESULT N5 — over half the field runs no statistical test.** *"Over half of all
  publications included in this review provided **no statistical proof** for their assumptions,"*
  reporting only descriptives or *"figures, displaying different policies with the proposed policy
  **visually outperforming** the baseline(s)."* **54 of 89.** And **45 of those 54 are
  content-sequencing papers** — the exact cluster Doroudi found 0-for-8 on when tests were run.
- **NEGATIVE RESULT N6 — almost nobody uses a non-adaptive control.** *"While half of all papers
  testing for statistical significance found RL approaches to outperform non-adaptive control
  conditions, **only 14 of the overall 89 studies reviewed included such a baseline in the first
  place**."* You cannot estimate the value of adaptation from a corpus that mostly does not
  contain an unadaptive arm.
- **The guidance/content split replicates Doroudi exactly.** Of 18 papers with a policy beating all
  baselines, **14 are guidance-related** (which hint, which feedback, worked example vs. problem
  solving) and **4 are content-related**. Two independent reviews, six years apart, different
  inclusion criteria, same shape.
- **The genuinely encouraging update:** among the 8 papers that used *expert-designed* baselines
  and still found significance, all 8 beat a domain-expert policy, and 6 of those used delayed
  learning gain as the reward. Baseline quality in the field is improving. `MEASURED-META`

**The synthesis of §6.1 and §6.2 is a design rule, not a mood:** *put the optimiser on
interchangeable micro-actions, never on the curriculum graph.*

### 6.3 The positive results, read precisely

Three real deployments. All three are worth building on; none of them says what a vendor deck
would say it says.

**(a) Schmucker, Pachapurkar, Bala, Shah & Mitchell (2023), "Learning to Give Useful Hints,"
AIED, [10.1007/978-3-031-42682-7_26](https://doi.org/10.1007/978-3-031-42682-7_26).** A *fielded*
system that learns which of several candidate assistance actions to give when a student answers
incorrectly. Trained on **>190,000 students** in an online Biology course, framed as a multi-armed
bandit per question. *"We evaluate the trained policy… comparing it to a randomized assistance
policy in live use with **over 20,000 students**, showing **significant improvements** resulting
from the system's ability to learn to teach better based on data from earlier students."*
`MEASURED-RCT` (live randomised comparison)
**Honest reading:** the comparator is a *randomised* assistance policy — precisely the weak-baseline
pattern Doroudi flagged. This is strong evidence that learned hint selection beats *random* hint
selection at scale; it is not yet evidence that it beats a well-designed fixed hint policy. It is
also exactly the **guidance-related** category where the wins concentrate.

**(b) Bassen, Balaji, Schaarschmidt, Thille, Painter, Zimmaro, Games, Fast & Mitchell (2020),
"Reinforcement Learning for the Adaptive Scheduling of Educational Activities," CHI,
[10.1145/3313831.3376518](https://doi.org/10.1145/3313831.3376518).** *"Using a controlled
experiment with **over 1,000 learners**… our model produces **better learning gains using fewer
educational activities than a linear assignment condition**, and produces **similar learning
gains** to a self-directed condition using fewer educational activities and with lower dropout
rates."* `MEASURED-RCT`
**Honest reading:** the win over a fixed linear sequence is real and is one of the few
content-related wins in the corpus. But against **self-directed** learners the learning gains were
*similar* — the measured advantage was efficiency and dropout, not learning. That is a valuable
result and it is not "the AI taught them better."

**(c) Cai, Grossman, Lin, Sheng, Wei, Williams & Goel (2021), "Bandit algorithms to personalize
educational chatbots," *Machine Learning*,
[10.1007/s10994-021-05983-y](https://doi.org/10.1007/s10994-021-05983-y).** MathBot; a contextual
bandit personalises conversation pace (insert extra practice / skip explanations); participants
randomised between uniform-random action selection (an A/B test) and the bandit. *"We found the
bandit **learned a similarly effective pedagogical policy to that learned by the randomized A/B
experiment** while incurring a **lower cost of experimentation**."* `MEASURED-RCT`
**Honest reading — NEGATIVE RESULT N7 for the usual claim.** The bandit did not produce a better
policy. It produced *the same* policy at lower cost to the learners who were in the experiment.
That is the correct and defensible reason to use a bandit in education, and it is a much narrower
claim than "personalisation improves learning."

**(d) The result that should be quoted more.** Papoušek, Stanislav & Pelánek (2016), LAK '16 (via
F11): ~1.3M answers, ~20,000 learners, randomised 2×2 of adaptive/random **item selection** ×
adaptive/random **distractor construction**, probed with randomly constructed reference questions.
*"In all cases the conditions with **adaptive construction of options** beat the conditions with
random options. **The item selection part does not seem to have large effect on learning.**"*
`MEASURED-RCT` — the learner model's contribution was calibrating the *distractors*, not choosing
what to practise.

### 6.4 The statistical cost of adapting while you measure

**Rafferty, A. N., Ying, H. & Williams, J. J. (2019), "Statistical Consequences of using
Multi-armed Bandits to Conduct Adaptive Educational Experiments," *JEDM* 11(1):47–79,
[ERIC EJ1220507](https://eric.ed.gov/?id=EJ1220507).** Simulation study, 500 runs per parameter
set, calibrated against modelled data from **ten previous educational experiments**. Full text
retrieved. `MEASURED-BENCH` (simulation grounded in real experiment parameters — **not** a trial on
learners, and it should not be cited as one).

> *"Results suggest that MAB experiments can lead to much higher average benefits to students than
> traditional experimental designs, although **at least twice as many participants are needed for
> acceptable statistical power**… Yet, **MAB assignment does increase false positive rates**,
> especially if there are temporal biases in when students enter the experiment."*

**NEGATIVE RESULT N8, with a number that should stop people:** under temporal bias in which
students enter (higher-performing students arriving later — the *normal* pattern in a term), *"the
false positive rate (Type I error rate) substantially increases with the amount of bias…
**reaching as high as 95%**."* And, contrary to intuition, *"**larger sample sizes also increase
false positive rates**"* under that bias, because a chance early difference sets up a
self-reinforcing sampling cycle.

The paper's own scope statement is the fair summary: MAB designs are beneficial *"in scenarios
where student characteristics do not vary over time."* In a school year, student characteristics
vary over time by construction.

**Practical consequence for the engine:** a bandit deployed on a cohort must either (i) block on
entry time, (ii) use an optimistic prior (which the paper shows *"mitigates the loss in power…
without significantly reducing benefits to students"*), or (iii) be treated as an *optimiser* whose
output is never read as an *inference*. Most deployments do (iii) implicitly and then publish the
inference anyway.

### 6.5 Cold start

Three separable problems, usually conflated:

1. **Predictor cold start.** F5: DKT reaches near-peak accuracy on a new learner in ~10
   interactions where Best-LR needs ~60 — a 6× burn-in reduction (Gervet et al. 2020).
   `MEASURED-BENCH`. In spaced repetition the analogue is FSRS default parameters costing ~0.02 log
   loss vs. optimised (log loss 0.3629 vs 0.3437). `MEASURED-BENCH`. Newer work continues on this
   exact question — *Cold Start Problem: An Experimental Study of Knowledge Tracing Models with New
   Students*, AIED 2025 LNCS, [10.1007/978-3-031-98459-4_30](https://doi.org/10.1007/978-3-031-98459-4_30)
   — but its abstract was not retrievable from OpenAlex or Crossref this session and no claim is
   made from it. `UNVERIFIED-IN-SESSION`
2. **Policy cold start — much smaller, and this is good news.** The policy needs an *ordinal over
   3 levels*, not a calibrated probability. A 2-item rapid probe supplies that on interaction zero
   (§2.3). **The expensive cold start belongs to the predictor, and the policy specified here does
   not depend on the predictor.** `INFERENCE` from measured components.
3. **Bandit cold start — the one with an ethical cost.** Early in a bandit's life its assignments
   are近 random by design; that randomness is *paid for by real children in real sessions*. §6.6.

### 6.6 The exploration cost is an ethical constraint, not a regret term

This is where the engineering literature and the duty of care diverge, and the divergence must be
resolved on the side of the child.

- **Exploration is not free even when both arms are defensible.** Meyer, Heck, Holtzman, Anderson,
  Cai, Watts & Chabris (2019), "Objecting to experiments that compare two unobjectionable policies
  or treatments," *PNAS*, [10.1073/pnas.1820701116](https://doi.org/10.1073/pnas.1820701116) —
  **16 studies, 5,873 participants, three populations, nine domains**: *"people frequently rate
  A/B tests designed to establish the comparative effectiveness of two policies or treatments as
  **inappropriate even when universally implementing either A or B, untested, is seen as
  appropriate**. This 'A/B effect' is as strong among those with **higher educational attainment
  and science literacy** and among **relevant professionals**."* `MEASURED-RCT`
  **This is not irrationality to be designed around. It is the operating environment.** A system
  that experiments on children must be able to say, to a parent, exactly what was randomised, why,
  and what the floor was.
- **Exploration on a child buys less information than exploration on a user.** Rafferty et al.:
  ≥2× participants for the same power, and Type I inflation up to 95% under the temporal bias that
  school terms produce by construction (§6.4).
- **The prohibition side is legally settled.** EU AI Act **Art. 5(1)(b)** prohibits systems
  exploiting *"vulnerabilities of a natural person… due to their **age, disability**"*
  `[VERBATIM, via F8]`; **Art. 5(1)(f)** prohibits emotion inference in education (§7.5); Art. 6(3)
  makes any profiling system high-risk with no derogation; Art. 26(11) obliges disclosure to the
  affected person. An exploration policy tuned on a child's known impulsivity is not a research
  design, it is a prohibited practice.

**The exploration budget rule, stated as a constraint the engine enforces.** `INFERENCE`, grounded
in the above:

> **Never explore on a dimension already graded EVIDENCED** — that is pure cost with no
> information return. **Explore only within the PLAUSIBLE tier.** Every arm must sit above a
> declared floor: the best known policy is always one of the arms and always receives at least a
> fixed minimum share. Explore only over **reversible micro-actions** (which hint, which probe
> format, which representation of *this* item) — never over method, never over goal, never over
> assessment. Cap total exposure per learner. Declare it in the interface.

### 6.7 Off-policy evaluation — the mechanism that spends data instead of children

The right way to retire a candidate policy is to kill it on logged data before any learner sees
it. The canonical educational treatment is **Mandel, Liu, Levine, Popović & Brunskill (2014),
"Offline policy evaluation across representations with applications to educational games," AAMAS**
([DOI](https://doi.org/10.5555/2615731.2617417)): *"These domains are also **high stakes, making it
infeasible to evaluate candidate representations by running them online**. Instead, one must
leverage existing data to learn and evaluate new policies for future use. …Our method is
**unbiased, agnostic to representation**."* `MEASURED-BENCH` — and Mandel et al. (2014) appears in
Riedmann's list of studies whose induced policy significantly outperformed its baselines in live
use, so the offline-then-online pipeline has at least one end-to-end success on record.

The complementary result is Rollinson & Brunskill (2015), "From Predictive Models to Instructional
Policies," EDM: *"A large amount of work has been done on building student models that can predict
student performance on the next question"* — and the paper's contribution is a *when-to-stop*
policy compatible with any such model. `OBSERVED`. This is the same message as F5 §2.3 and F11
§8.3 from a different direction: **the research frontier is the decision rule, not the predictor.**

**Design consequence:** the J1 engine logs `(state, action, outcome, propensity)` on every
fast-loop and slow-loop action — the propensity being the missing field in almost every deployed
tutor, and the one without which off-policy evaluation is impossible. Logging propensity costs one
float. Not logging it costs the ability to ever improve the policy without experimenting on
children.

---

## 7. Bidirectional learning — the system learns the student while the student learns the topic

### 7.1 What "bidirectional" has to mean to be more than a slogan

The learner's model of the topic is updated by instruction. The system's model of the learner is
updated by evidence. For this to be *bidirectional* rather than merely *two directional processes
running in the same tab*, three things must hold, and only the third is hard:

1. The system's model must be **visible** to the learner.
2. It must be **correctable** by the learner.
3. **A correction must change the policy.** Otherwise it is a comment box.

Point 3 is the one the literature is unambiguous about, and the finding is a null:

> **NEGATIVE RESULT N9.** Jivet, Scheffel, Drachsler & Specht (2017), *"**Awareness Is Not
> Enough**: Pitfalls of Learning Analytics Dashboards in the Educational Practice,"* EC-TEL,
> [10.1007/978-3-319-66610-5_7](https://doi.org/10.1007/978-3-319-66610-5_7). Corroborated across
> four independent reviews (Bodily et al. 2018 LAK; Matcha, Uzir, Gašević & Pardo 2020 IEEE TLT,
> [10.1109/TLT.2019.2916802](https://doi.org/10.1109/TLT.2019.2916802)): the open-learner-model
> and dashboard literature evaluates **perception** far more than **learning**, its SRL grounding
> is thin or post-hoc, and comparison-to-peer-average — the most common design — targets awareness,
> the weakest link in the chain. `MEASURED-META` (via F5 §3.2)

Plus the sharper risk from the same literature: **social-comparison displays can demotivate**;
showing a struggling learner they are below the class average is a documented hazard. `MEASURED-META`

And the blocker F5 §3.3 identified: **an open learner model inherits the calibration debt of the
model it opens.** Showing "62% mastery" with interface authority, on top of a model the KT
critique literature calls severely biased, is worse than showing nothing.

The design that survives all three problems is **negotiated learner modelling** (Bull 2016,
*RPTEL*, [10.1186/s41039-016-0035-3](https://doi.org/10.1186/s41039-016-0035-3)) `OBSERVED` — the
learner may *argue with* the model, and the argument is part of the record.

### 7.2 The schema — L5b, the selection state

F5's Portable Learner Model already specifies L0–L6 and deliberately leaves **L5 (instructional
priors) short and empty of learning styles**. J1 supplies the missing piece: the layer that records
*not what the learner knows, but what the system decided and why*. `INFERENCE` — this is the
section's schema contribution, and it extends F5 rather than replacing it.

```yaml
# ── L5b. SELECTION STATE (the policy's own memory, fully inspectable) ──
# Every field here is a DECISION, not a trait. Decisions have reasons,
# authors, and expiry dates. Traits do not, which is why traits do not
# belong in a policy layer.

selection:

  per_concept:
    - kc_id: "wikidata:Q11473"
      assistance_level: high | medium | low
      set_by:
        probe_id: <ulid>                 # points into L2 evidence log
        instrument: "rapid_verification" # §2.4; NEVER "preference", NEVER "self_report_of_level"
        items_administered: 2
        result: [{prereq: kc_id, level: partial}, ...]
        effort_self_report: 6            # Paas 1–9, LEARNER-ENTERED, not inferred
        ts: <iso8601>
      expires_after: "1 session"         # Cronbach's half-life, made operational:
                                         # a selection decision is not a durable fact
      rung_current: 2
      rung_entry_rule: "min_over_prereqs_minus_one"   # §3.2

  fast_loop_log:                          # append-only; one row per action
    - ts: <iso8601>
      signals: { error_type: misconception, distractor_id: "fci:impetus",
                 latency_vs_median: 1.4, hints: 0, effort: 7 }
      rule_id: "P1_misconception_refutation"
      action: { type: refutation, target_misconception: "fci:impetus" }
      propensity: 1.0                     # ← REQUIRED. Enables off-policy eval (§6.7).
                                          #   Deterministic rules log 1.0; explored
                                          #   actions log their true sampling probability.

  slow_loop_log:                          # append-only; one row per METHOD change
    - ts: <iso8601>
      probe_series: [ {ts, score, goal_line}, ... ]   # ≥4 points REQUIRED
      dwell_satisfied: true
      menu_item_id: "M2_prerequisite_dropback"        # closed menu, §5.2
      reason: <template_id + slot values>             # NOT free-form model text
      actor: system | teacher | learner | guardian
      escalation_counter: 1                           # → human at k, §4.4

  contest:                                # bidirectionality, made load-bearing
    - target: <probe_id | selection field | slow_loop_log row>
      by: learner | guardian
      claim: "I misread the sign — I know this one"
      effect: reprobe | override | annotate            # MUST be one of these.
                                                       # A contest that only annotates
                                                       # is the 'awareness is not enough'
                                                       # failure mode (§7.1).
      ts: <iso8601>

  calibration_ref: <reliability-diagram-hash>   # F5 G3: no number without its reliability
```

**Four guarantees this layer must make**, extending F5's G1–G9:

| # | Guarantee | Enforced by |
|---|---|---|
| **G10** | **Every selection decision names its instrument and its expiry.** No decision persists as a fact | `set_by.instrument` + `expires_after` required |
| **G11** | **Every action logs its propensity.** The policy can be improved offline, without further experimentation on learners | `propensity` required on every logged action |
| **G12** | **Every method change names a menu item and a reason template.** Fuchs 1991 as a type constraint | `menu_item_id` drawn from a closed enum; `reason` is a template id, never free generation |
| **G13** | **A contest changes the policy or it is not a contest.** `effect` ∈ {reprobe, override, annotate}, and `annotate` alone is a conformance failure if the contest targets a live decision | `contest.effect` required and audited |

### 7.3 What the learner and the guardian actually see

Not a mastery bar. A sentence with a receipt and a button:

> *"You're seeing worked examples for **factoring quadratics** because a 2-question check on
> 2026‑07‑28 showed the **distributive property** step wasn't automatic yet. That check expires
> after this session."*  **[Re-check now]  [That's wrong — here's why]  [See all decisions]**

Three properties, each answering a documented failure:
- **A receipt, not a score** — answers the calibration-debt problem (F5 §3.3): the learner sees the
  *evidence and the rule*, whose provenance is exact, rather than a posterior whose reliability is
  unknown.
- **No peer comparison anywhere** — answers the demotivation hazard (§7.1).
- **Re-check is one tap** — a 40-second probe is cheap enough that "I think you're wrong about me"
  can be *settled empirically in the same minute*. This is the concrete thing a frontier model
  makes possible that was not possible in 2016, and it converts negotiated learner modelling from
  a research prototype into an interaction.

### 7.4 What must never enter the model — the debunked

- **Learning styles / sensory-modality labels.** Pashler, McDaniel, Rohrer & Bjork (2008/2009),
  *PSPI*, [10.1111/j.1539-6053.2009.01038.x](https://doi.org/10.1111/j.1539-6053.2009.01038.x):
  the meshing hypothesis requires a crossover in a randomised design; virtually no study meets the
  standard and those that do contradict it. `MEASURED-META`. Direct tests: Rogowsky, Calhoun &
  Tallal (2015), *JEP*; **Husmann & O'Loughlin (2019), N = 426** — VARK scores uncorrelated with
  performance, alignment uncorrelated with outcome
  ([10.1002/ase.1777](https://doi.org/10.1002/ase.1777)); **Melzner & Kappes (2024), N = 222**,
  adequately powered, **no interaction**
  ([10.1007/s11251-024-09689-1](https://doi.org/10.1007/s11251-024-09689-1)). All `MEASURED-RCT`.
  And the belief persists at **89.1% among 15,405 educators across 18 countries with no decline
  over time** (Newton & Salvi 2020,
  [10.3389/feduc.2020.602451](https://doi.org/10.3389/feduc.2020.602451)) `MEASURED-META` — which
  is precisely why a schema must *structurally exclude* the field rather than merely omit it.
  A field that does not exist cannot be populated by a well-meaning prompt.
- **Preference over technique.** §3.5.
- **Any personality or "style" trait as a policy input.** Cronbach 1975's own verdict on the best
  results the ATI programme ever produced: *"strangely inconsistent from year to year and from
  course to course."* `OBSERVED`

### 7.5 What must never enter the model — the prohibited

Carried from F8, restated because it binds this layer specifically:

| Prohibited | Authority |
|---|---|
| **Emotion / affect inference in education** — no webcam engagement detection, no voice-affect scoring, no `emotional_state` field derived from biometric signal | **EU AI Act Art. 5(1)(f)** `[VERBATIM]`, read with Art. 3(39) (biometric-based inference of emotions or intentions) and Art. 3(34). Applicable since **2 Feb 2025**. COPPA independently classifies facial templates and voiceprints as children's personal information (16 CFR 312.2) |
| **Engagement or difficulty mechanics personalised on a known disability, impulsivity profile, or inferred emotional state** | **AI Act Art. 5(1)(b)** — exploiting vulnerabilities due to *"age, disability"* `[VERBATIM]`; ICO AADC Std. 13 |
| **`suspected_dyslexia`, `adhd_likelihood`, `depression_risk`, `home_instability`** as durable fields, dashboard rows, exports, or API responses | GDPR Art. 9(1); IDEA (disability records are sensitive and destroyable on parental demand); an AI may not diagnose or label a child (CLAUDE.md §3) |
| **Self-exemption from high-risk classification** | AI Act Art. 6(3) final clause — profiling ⇒ always high-risk `[VERIFIED]` |

**The load-bearing distinction, and it is a design gift rather than a constraint.** The engine's
load signal is **self-reported mental effort** — one tap, learner-entered, appearing in the record
as a *learner statement*, not a system inference. It is lawful, it is cheap, it is on-task, it is
contestable, and Kalyuga & Sweller's own successful controller used exactly a self-report load
measure alongside the knowledge probe. **The legal line and the good-engineering line are in the
same place here**, which is worth saying out loud because it is not always true.

---

## 8. The falsification — the strongest case that this should not be built

Stated as strongly as it can honestly be stated, then answered, conceding what must be conceded.

### 8.1 The case against, in three claims

**F-1 — The biggest measured wins are universal, not personalised.** Retrieval practice g = 0.499
across 222 classroom studies and 48,478 students. Spacing d = 0.54 on curriculum materials, with
271 of 283 comparisons favouring spacing. Expectancy framing g = 0.48 vs. g = −0.02. None of these
requires knowing anything about the individual learner. A system that simply *always* did those
three things, in a fixed sequence, would capture effects larger than any documented
personalisation gain in this corpus.

**F-2 — A single well-designed non-adaptive sequence is a very strong baseline, and adaptive
systems mostly have not beaten one.** Doroudi: **0 of 8** for sequencing interdependent content;
3 of 15 classroom studies; 71% of positive results compared against *random* baselines. Riedmann
2025: only **14 of 89** studies included a non-adaptive control at all, and **54 of 89** ran no
statistical test. Papoušek: adaptive item selection had no large effect on learning, and one
random-selection arm was *slightly better*. Doroudi's one "significantly worse" entry is Mettler et
al. (2011), where a data-fitted policy was beaten by **ARTS, a response-time heuristic that was not
fit to data at all** — the review's own gloss: *"in some cases, a good psychological theory might
be more useful for finding good instructional policies than a data-driven model."* And Memrise's
fixed ladder (F11 §4.9) is a commercial existence proof that a hard-coded schedule serves hundreds
of millions of sessions.

**F-3 — The measurement is not free, and its cost lands on the learner's attention, not on a
server.** Every probe is 30–40 seconds not spent learning. Across a 40-concept course that is
20–25 minutes of pure measurement. Add the "type of prior knowledge assessment" moderator from
Tetzlaff — the *instrument* changes the size of the effect you are exploiting — and you are
spending real attention on an instrument whose measurement properties are themselves a moderator.
Meanwhile the strongest personalisation result in the corpus is *asymmetric*: withholding
assistance from experts helps them only d = 0.428, and the authors' own advice under uncertainty is
**"rather provide assistance than to withhold it."** If the correct policy under uncertainty is
"assist," and uncertainty is the normal state, **"always assist" may be the optimal policy and
requires no measurement whatsoever.**

### 8.2 The answer, with the concessions made explicitly

**Concede F-1 entirely.** It is correct, and §5.1 is the concession made structural: retrieval,
spacing, and expectancy framing are **removed from the policy** and placed in a substrate that is
always on and never selected. This is not a rhetorical move; it changes the build. It also
predicts, correctly, why so much of the adaptive-learning literature is unreproducible: when the
adaptive arm and the control arm differ in the *substrate* as well as the policy, the measured
"personalisation effect" is a retrieval-practice effect with a different name. Riedmann's finding
that only 14 of 89 studies had a non-adaptive control is exactly this failure at field scale.
**The honest product claim is: universals first, and they are most of the value.**

**Concede most of F-2, and narrow the claim to where the evidence is.** The corpus does not support
model-induced *content sequencing*, and this section does not propose it. It proposes selection
over **guidance micro-actions and assistance level**, which is the cluster where wins concentrate
in both reviews: Doroudi 11/14 on paired associates and 4-sig/4-ATI on activity types; Riedmann
14 of 18 guidance-related. The strongest single positive is Salden et al. (2010) — **adaptive
fading > fixed fading > problem solving**, in one lab and one classroom experiment — which is a
direct head-to-head of an adaptive policy against a *well-designed fixed sequence*, and the
adaptive policy won. Blayney et al. (2015) is a second: format assigned by prior-knowledge pretest
beat random assignment. **The claim survives, but only in the guidance layer.** The curriculum
graph should be authored, versioned, and fixed — exactly as I1's build order (PSI's spine) already
implies.

**Answer F-3, and take the sting seriously.** Three responses, one of which is a concession.

- The probe is **1–3 items and 15–40 seconds**, validated at r = 0.66–0.92 against instruments
  taking 2.5–4.9× longer. On a 20-minute concept that is 2–3% of session time.
- The probe is **not only measurement**. A first-step or verification item is itself a retrieval
  event with feedback, which is the substrate's highest-value activity (g = 0.499). Careful: it
  must not double as the *instructional* item for the same content in the same session (Pan &
  Rickard on rearranged S–R items). But the attention is not lost; it is spent on the best-evidenced
  activity available.
- **The concession, and it is real: "always assist" is a legitimate rival policy and the experiment
  must be able to select it.** Tetzlaff's asymmetry means the cost of over-assisting is genuinely
  smaller than the cost of under-assisting. If the falsification test in §8.3 finds the entire
  advantage of the probe-assigned arm sits in the low-prior tail — that is, the probe only ever
  tells you to do what "always assist" would have done anyway — then **the correct engineering
  conclusion is to delete the probe and always assist**, and to redirect the measurement budget to
  the misconception diagnosis (P1), which no fixed policy can substitute for. That is a good
  outcome. A section that cannot specify the finding that would delete its own centrepiece is not
  doing evidence.

### 8.3 The falsifiable claims

These are what distinguish the engine from a fixed sequence. Each is a runnable experiment.

> **Claim J1-A (the entry rule).** With the universal substrate held **identical in both arms**
> (retrieval + feedback, spacing, expectancy framing all on), assigning entry assistance level from
> a ≤3-item rapid-verification probe over the prerequisite closure produces higher **delayed
> transfer** scores (≥7 days, transfer items not retention items) than the single best **fixed**
> assistance level chosen in advance by a domain expert.
> **Falsified if** the probe arm does not beat the best fixed arm on delayed transfer; **or** if
> there is no crossover (i.e. no arm×prior-knowledge interaction, only a main effect); **or** if
> the advantage is confined to the low-prior tail — in which case the correct policy is "always
> assist" and the probe should be deleted (§8.2).
> *Why transfer, not retention:* Rey & Fischer (2013) found the reversal on transfer and **not** on
> retention. A retention-only outcome measure cannot falsify this claim in either direction.

> **Claim J1-B (the pivot rule).** Logging a **named** method change drawn from the closed §5.2
> menu, with a template reason, produces better achievement than logging progress alone at the
> same measurement frequency.
> This is a direct replication of Fuchs, Hamlett & Stecker (1991) with the 1991 expert system
> replaced by a model constrained to the same closed menu.
> **Falsified if** the advice arm matches the measurement-only arm — which would mean the 1991
> result was about *teacher* cognition and does not port to an automated recommender. That is a
> live possibility and it is the single highest-value replication available to this project.

> **Claim J1-C (the bandit scope prediction).** A contextual bandit over **guidance micro-actions**
> (which hint, which worked step, which probe format) beats a well-designed fixed guidance policy;
> a bandit over **content sequencing** does not beat a well-authored fixed curriculum sequence.
> Predicted from Doroudi (11/14 paired-associate vs. 0/8 interdependent content) and Riedmann
> (14 guidance vs. 4 content among 18 wins). **Falsified if** the content-sequencing bandit wins
> against an expert-authored sequence — which would be the most important positive result in the
> field since 2019, and would licence a much more ambitious engine than the one specified here.

> **Claim J1-D (the two clocks).** A controller in which the fast loop cannot change the method
> outperforms an otherwise identical controller with a single unconstrained loop, on delayed
> transfer, with the difference concentrated in learners whose early performance is noisiest.
> **Falsified if** the unconstrained controller matches or beats it — which would mean the
> consolidation argument (Van Norman) does not bind at session granularity.

---

## 9. The grading table — every proposed personalisation dimension

**EVIDENCED** = a crossover interaction or a direct adaptive-vs-fixed comparison, meta-analytic or
replicated RCT. **PLAUSIBLE** = mechanism is credible and some evidence exists, but no crossover
has been demonstrated at scale. **DEBUNKED** = tested with adequate design and failed, or the
canonical claim is a documented null. **PROHIBITED** = unlawful in education regardless of
evidence.

| # | Dimension (signal → decision) | Grade | Best evidence | Effect |
|---|---|---|---|---|
| 1 | **Prior knowledge (per concept) → assistance level** | **EVIDENCED** | Tetzlaff et al. 2025, 60 studies, N = 5,924 | **d = +0.505 novice / −0.428 expert**; asymmetric; I² ≈ 90% `MEASURED-META` |
| 2 | **Prior knowledge → adaptive vs. fixed worked-example fading** | **EVIDENCED** | Salden et al. 2010, 1 lab + 1 classroom experiment | *"adaptive fading over fixed fading over problem solving"* `MEASURED-RCT` |
| 3 | **Prior-knowledge pretest → instructional format assignment** | **EVIDENCED** | Blayney, Kalyuga & Sweller 2015, Exp. 2 | adaptive group superior to non-adaptive `MEASURED-RCT` |
| 4 | **Prior knowledge → whether to signal / emphasise** | **EVIDENCED** | Schneider et al. 2018 (k = 209); Richter, Scheiter & Eitel 2016 | **g = 0.43** overall; benefit **concentrated in low-prior**; harms high-prior `MEASURED-META` |
| 5 | **Adapting to learner *level* vs. to interest/feedback** | **EVIDENCED** | Major, Francis & Tsapali 2021, *BJET*, 16 RCTs, **53,029 learners** | overall **d = 0.18**; level-adaptive **d = 0.35** vs. interest/feedback-only `MEASURED-META` |
| 6 | **Named misconception (from distractor) → refutation** | **EVIDENCED** | F5 §6 (concept inventories, diagnostic distractors); Papoušek 2016 (adaptive *distractor* construction beat random in all conditions) | direction robust `MEASURED-RCT` |
| 7 | **Item-level assistance-action selection (which hint)** | **EVIDENCED** | Schmucker et al. 2023, trained on 190k, live on **20k+** students | *"significant improvements"* vs. **randomised** policy `MEASURED-RCT` ⚠️ weak baseline |
| 8 | **Scheduling of paired associates / flashcards** | **EVIDENCED** | Doroudi et al. 2019, Table 2 | **11 of 14** significant `MEASURED-META` |
| 9 | **Activity-type selection (worked example vs. problem solving)** | **EVIDENCED** | Doroudi et al. 2019 | 4 sig + **4 ATI**, 2 n.s. `MEASURED-META` |
| 10 | **Working memory capacity → instructional load** | **PLAUSIBLE** | Snow et al. 1980 (ability × processing burden — the one surviving Cronbach–Snow generalisation); *Behavioral Sciences* 2025 narrative review | no pooled crossover; and WM is **not trainable** (Melby-Lervåg 2016) `OBSERVED` |
| 11 | **Entry-rung selection for laddered explanation** | **PLAUSIBLE** | F10: 3 rungs > 2 (p = 0.032); 5 ≯ 3 (p = 0.738); mechanism = expertise reversal | rung *count* measured; **rung *entry selection* untested** — this is Claim J1-A |
| 12 | **Response latency as a load/fluency proxy** | **PLAUSIBLE** | ARTS (response-time heuristic) **beat** a data-fitted Atkinson policy — Doroudi's one "significantly worse" entry | works as a *heuristic*; not validated as a load measure `MEASURED-RCT` |
| 13 | **Self-reported mental effort (Paas) as a fast-loop gate** | **PLAUSIBLE** | Kalyuga & Sweller 2005 used knowledge probe **+ load self-report** in the arm that won | confounded with the probe; not isolated `MEASURED-RCT` |
| 14 | **Cross-domain prior knowledge for cold start** | **PLAUSIBLE** | F5 §4.2: *"Nobody has shown that knowing a learner's model in algebra improves the cold-start prior in chemistry"* | **untested; no dataset exists** `OBSERVED` |
| 15 | **Interest / relevance personalisation** | **PLAUSIBLE** | Major et al. 2021: interest-linked personalisation is the *weaker* half of the 0.18 pooled effect | not separably estimated `MEASURED-META` |
| 16 | **Self-regulation profile → strategy prompts** | **PLAUSIBLE** | SRL training **g = 0.38** (Theobald 2021, via B1) | evidence is for *training* SRL, not for *selecting on* it `MEASURED-META` |
| 17 | **Dosage personalisation** | **PLAUSIBLE** | Stockard et al. 2018 dosage effect | dosage matters; *personalised* dosage untested |
| 18 | **Learning styles / sensory-modality matching** | **DEBUNKED** | Pashler 2008; Rogowsky 2015; **Husmann N = 426**; **Melzner N = 222**; and **Cronbach 1975's own spatial×diagram null** | *"No interaction of this sort was found, in our shop or elsewhere"* `MEASURED-META` + `OBSERVED` |
| 19 | **Learner preference → explanation level** | **DEBUNKED** | 3 RCTs, infographic vs. PLS | **preference d ≈ 0.48, knowledge = 0** `MEASURED-META` |
| 20 | **Expanding vs. uniform spacing intervals** | **DEBUNKED** | Latimier, Peyre & Ramus 2020, 54 effect sizes | **g = 0.034, n.s.** — the folklore in every SRS `MEASURED-META` |
| 21 | **Personality / cognitive style × instructor press** | **DEBUNKED (as deployable)** | Cronbach 1975 on the ATI programme's best results | *"strangely inconsistent from year to year and from course to course"* `OBSERVED` |
| 22 | **General/specific ability × instructional method (as a specific-ability ATI)** | **DEBUNKED** | Cronbach 1975 | *"Between 1960 and 1970, many of us searched fruitlessly"*; *"the interactions did not turn out as we had anticipated"* `OBSERVED` |
| 23 | **Model-induced sequencing of interdependent content** | **DEBUNKED** | Doroudi 2019 **0 of 8**; Riedmann 2025: 45 of 53 content papers ran **no test** | *"there is not yet evidence that RL can induce instructional policies significantly better than reasonable baselines"* `MEASURED-META` |
| 24 | **Scheduling-algorithm choice (SM-2 → FSRS) as a learning intervention** | **DEBUNKED** | F5 §1.8 / F11 §4.8; srs-benchmark README: *"no randomized user trials or measurement of actual learning outcomes"* | zero controlled evidence `MEASURED-BENCH` |
| 25 | **Working-memory *training* as a personalised intervention** | **DEBUNKED** | Melby-Lervåg, Redick & Hulme 2016, 87 publications / 145 comparisons | **no convincing far transfer** `MEASURED-META` |
| 26 | **Emotion / affect inference from biometric signal** | **PROHIBITED** | EU AI Act **Art. 5(1)(f)** + 3(39) + 3(34); applicable 2 Feb 2025 | unlawful in education `[VERBATIM, via F8]` |
| 27 | **Engagement mechanics tuned on age, disability, or impulsivity** | **PROHIBITED** | EU AI Act **Art. 5(1)(b)**; ICO AADC Std. 13 | unlawful `[VERBATIM, via F8]` |
| 28 | **Inferred diagnosis / disability status as a policy input** | **PROHIBITED** | IDEA; GDPR Art. 9(1); CLAUDE.md §3 (an AI may not diagnose or label a child) | unlawful and out of scope |

**Read the table as a build order.** Rows 1–9 are the engine. Rows 10–17 are the exploration
budget (§6.6) and nothing else. Rows 18–25 are what the schema must structurally exclude, because
89.1% of educators believe row 18 and a permissive schema will be filled with it. Rows 26–28 are
not design decisions.

---

## 10. The deliverable — the selection policy, specified

Signals in, decision rule, action out, latency for each. `INFERENCE` on the composition; every
component cited above.

### 10.1 Signal register

| id | Signal | Source | Latency | Legal note |
|---|---|---|---|---|
| S1 | Ordinal prior-knowledge level per prerequisite | rapid verification / first-step probe, ≤3 items | **15–40 s**, at concept entry | knowledge only |
| S2 | Error type (slip / misconception / prerequisite gap) | chosen distractor id → misconception vocabulary (F5 L4) | **< 5 s**, per item | knowledge only |
| S3 | Latency vs. that item's population median | timing | per item | behavioural, non-biometric, aggregate-referenced |
| S4 | Hint requests | interaction log | per item | — |
| S5 | Self-reported mental effort | Paas 9-point, one tap | per probe cycle | **learner statement, never an inference** |
| S6 | Generation-probe fidelity ("say it back") | LLM comparison against the rung's declared propositions | **≈60–90 s** | knowledge only |
| S7 | Near-transfer probe result | freshly generated transfer item | ≈2 min | knowledge only |
| S8 | Session probe score vs. goal line | fixed-difficulty freshly generated probe, 1 per session | **≥4 sessions** to act | knowledge only |

### 10.2 The rules

| id | Condition | Action | Loop | Latency to act |
|---|---|---|---|---|
| **R0** | safeguarding trigger | halt, escalate to human | — | immediate |
| **R1** | S2 = named misconception | refutation targeted at that misconception (**not** re-explanation, **not** more assistance) | fast | 1 turn |
| **R2** | S1 shows a prerequisite absent | drop back to that prerequisite (M2) and re-teach | fast | 1 turn |
| **R3** | S1 low over P | assistance level = high; rung = min(level(p)) − 1 | fast | at entry |
| **R4** | S1 high over P **and** S7 correct **and** S5 low **and** S3 below median | reduce assistance one step; rung + 1 | fast | ≈2 min |
| **R5** | S6 drops or contradicts a load-bearing proposition | rung − 1; re-render top-down | fast | ≈90 s |
| **R6** | S8: ≥4 consecutive points below goal line **and** dwell satisfied | **one** method change from the closed menu (§5.2), by precedence (§5.3), with logged reason | slow | ≥4 sessions |
| **R7** | *k* method changes without crossing the goal line | escalate to a human; stop adapting | slow | on counter |
| **R8** | none of the above fires with its full conjunction | **do nothing** | — | — |

Always-on and never subject to R1–R8: retrieval practice with feedback, spacing at ≈10–20% of the
target retention interval, and expectancy framing before every study episode (§5.1).

### 10.3 The one-line claim that distinguishes this from a fixed sequence

> **With the universal substrate identical in both arms, a ≤3-item rapid-verification probe at
> concept entry, driving assistance level and entry rung, produces higher delayed *transfer* than
> the best expert-chosen fixed assistance level — and the advantage takes the form of a crossover,
> not a main effect.**
>
> If there is no crossover, personalisation is not what is working. If the advantage is confined to
> the low-prior tail, **delete the probe and always assist.** If the fixed arm wins outright, the
> engine reduces to the substrate — which is still most of the measured value in this corpus, and
> saying so is the reason to trust the rest.

---

## 11. Consolidated negative and null results (PRD §8.2 — nine, against a floor of four)

| # | Result | Source |
|---|---|---|
| **N1** | **Spatial ability × diagrams: no interaction found, anywhere.** The direct ancestor of every modality-matching claim, reported null by its own authors in 1975 | Cronbach 1975, [10.1037/h0076829](https://doi.org/10.1037/h0076829) `OBSERVED` |
| **N2** | **Working memory training: no convincing far transfer**, 87 publications / 145 comparisons; far-transfer g = 0.14–0.16 elsewhere and not sustained | Melby-Lervåg, Redick & Hulme 2016; Schwaighofer et al. 2015 `MEASURED-META` |
| **N3** | **Expertise reversal for instructional explanations replicates on transfer but NOT retention** — a ladder measured by recall cannot see its own damage | Rey & Fischer 2013, [ERIC EJ999802](https://eric.ed.gov/?id=EJ999802) `MEASURED-RCT` |
| **N4** | **Unfaded support turns negative**: permanent-prompt group ended a term *substantially lower* than the fading group; prompts became *"a redundant stimulus that interfered"* | Nückles et al. 2010, [ERIC EJ880291](https://eric.ed.gov/?id=EJ880291) `MEASURED-RCT` |
| **N5** | **54 of 89 RL-in-education papers ran no statistical test at all** — and **45 of those 54 are content-sequencing papers**, exactly the cluster Doroudi found 0-for-8 on | Riedmann, Schäper & Lugrin 2025, Table 2 `MEASURED-META` |
| **N6** | **Only 14 of 89 studies included a non-adaptive control condition** — the field largely cannot estimate the value of adaptation | Riedmann et al. 2025 `MEASURED-META` |
| **N7** | **A contextual bandit matched, and did not beat, a randomised A/B experiment** on policy quality; its advantage was lower experimentation cost | Cai, Grossman, Lin, Sheng, Wei, Williams & Goel 2021, *Machine Learning* `MEASURED-RCT` |
| **N8** | **Bandit assignment needs ≥2× participants for acceptable power**, and under temporal entry bias the **Type I error rate reaches 95%** — with larger samples making it *worse* | Rafferty, Ying & Williams 2019, *JEDM* `MEASURED-BENCH` (simulation) |
| **N9** | **"Awareness is not enough"** — the open-learner-model and dashboard literature evaluates perception far more than learning; peer-comparison displays risk demotivating the learners they target | Jivet et al. 2017; Bodily et al. 2018; Matcha et al. 2020 `MEASURED-META` |
| **N10** | **The A/B effect:** people rate a comparison of two policies as inappropriate even when deploying either untested is fine — undiminished among the science-literate and among professionals; 16 studies, 5,873 participants | Meyer et al. 2019, *PNAS* `MEASURED-RCT` |
| **N11** | **Expanding intervals ≯ uniform intervals**, g = 0.034 n.s. across 54 effect sizes — the personalisation folklore embedded in every SRS | Latimier, Peyre & Ramus 2020 `MEASURED-META` (carried from B1/F11) |
| **N12** | **Adaptive item selection had no large effect on learning**; the measurable gain came from adaptive *distractor* construction, and one random-selection arm was slightly better | Papoušek, Stanislav & Pelánek 2016, LAK `MEASURED-RCT` (carried from F11) |

---

## 12. Open problems this section could not close

1. **Claim J1-A has not been run.** Nobody has compared probe-assigned entry assistance against the
   best fixed assistance level, with the substrate held constant, measured on delayed transfer.
   This is the highest-value experiment in the project and it is small: three arms, one concept,
   a 7-day delayed transfer test.
2. **Claim J1-B — does Fuchs 1991 port to an automated recommender?** The 1991 result may be about
   changing *teacher* cognition. If it does not port, the slow loop's entire justification changes.
3. **No public dataset carries propensities.** Off-policy evaluation of educational policies is
   blocked on a one-float logging convention that essentially no deployed system follows (F5 §4.2,
   §6.7 here).
4. **The misconception vocabulary problem** (F5 §8.5) is the binding constraint on rule R1, which
   is the highest-precedence pedagogical rule in the policy. The FCI's ~30 items encode decades of
   physics-education interviews; nothing comparable exists for most of the curriculum. This remains
   the most obvious high-value application of frontier models in learner modelling.
5. **The `d = 0.971` interaction figure** for expertise reversal is still unverified from the
   abstract (standing correction). Obtaining the Tetzlaff full text would resolve it either way.
6. **Cross-domain cold start is untested and the dataset does not exist** (row 14).
7. **arXiv was unreachable for this session**, so the 2025–2026 preprint literature on
   LLM-driven adaptive policies is unrepresented here. Flagged, not guessed.

---

## 13. Sources

**Aptitude–treatment interaction, primary**
1. Cronbach, L. J. (1975). Beyond the two disciplines of scientific psychology. *American Psychologist* 30(2):116–127. https://doi.org/10.1037/h0076829 — **full text retrieved and quoted** `OBSERVED`
2. Cronbach, L. J. (1957/1963). The two disciplines of scientific psychology. https://doi.org/10.1037/14156-015 `OBSERVED`
3. Cronbach, L. J. & Snow, R. E. (1977). *Aptitudes and Instructional Methods.* Irvington. — cited via Cronbach 1975's own forward references (*"in press"*); the book itself was not retrievable this session `UNVERIFIED-IN-SESSION`
4. Snow, R. E. et al. (1980). Aptitudes and Instructional Methods: Final Report 1975–1979, Aptitude Research Project. https://eric.ed.gov/?id=ED204407 `OBSERVED`
5. Snow, R. E. (1977). An Overview of Current Research on Aptitude Processes. https://eric.ed.gov/?id=ED148977 `OBSERVED`
6. Snow, R. E. (1991). ATI as a Framework for Research on Individual Differences in Psychotherapy. https://eric.ed.gov/?id=EJ428196 `OBSERVED`
7. Driscoll, M. P. (1987). Aptitude-Treatment Interaction Research Revisited. https://eric.ed.gov/?id=ED285532 `OBSERVED`
8. Tobias, S. (2009). The expertise reversal effect and aptitude treatment interaction research. *Instructional Science.* https://doi.org/10.1007/s11251-009-9103-z `OBSERVED` (via F5)

**Expertise reversal and rapid assessment**
9. Tetzlaff, Simonsmeier, Peters & Brod (2025). *Learning and Instruction.* https://doi.org/10.1016/j.learninstruc.2025.102142 `MEASURED-META`
10. Kalyuga, Ayres, Chandler & Sweller (2003). *Educational Psychologist* 38(1). https://doi.org/10.1207/s15326985ep3801_4 `OBSERVED`
11. Kalyuga (2007). Expertise Reversal Effect and Its Implications for Learner-Tailored Instruction. *EPR.* https://doi.org/10.1007/s10648-007-9054-3 · https://eric.ed.gov/?id=EJ785056 `OBSERVED`
12. Chen, Kalyuga & Sweller (2017). *EPR.* https://doi.org/10.1007/s10648-016-9359-1 `OBSERVED`
13. **Kalyuga & Sweller (2004).** Measuring Knowledge to Optimize Cognitive Load Factors During Instruction. *JEP* 96(3):558–568. https://eric.ed.gov/?id=EJ685015 — **r up to .92; time ÷4.9 and ÷2.5** `MEASURED-RCT`
14. **Kalyuga (2006).** Rapid Cognitive Assessment of Learners' Knowledge Structures. *L&I.* https://doi.org/10.1016/j.learninstruc.2005.12.002 — **N=55, r=0.72, time ÷2.8** `MEASURED-RCT`
15. **Kalyuga (2006).** Rapid Assessment of Learners' Proficiency. *Educational Psychology.* https://eric.ed.gov/?id=EJ753417 — **r=0.66, time ÷3.8** `MEASURED-RCT`
16. **Kalyuga & Sweller (2008).** When Less Is More in Cognitive Diagnosis. *JEP* 100(3):603. https://doi.org/10.1037/0022-0663.100.3.603 — **N=33, rapid verification** `MEASURED-RCT`
17. **Kalyuga & Sweller (2005).** Rapid dynamic assessment of expertise. *ETR&D.* https://doi.org/10.1007/BF02504800 — **yoked control; experimental group superior** `MEASURED-RCT`
18. Blayney, Kalyuga & Sweller (2015). *ETS.* https://eric.ed.gov/?id=EJ1078240 `MEASURED-RCT`
19. Salden, Aleven, Schwonke & Renkl (2010). *Instructional Science.* https://doi.org/10.1007/s11251-009-9107-8 `MEASURED-RCT`
20. Rey & Buchwald (2011). *JEP: Applied.* https://doi.org/10.1037/a0022243 `MEASURED-RCT`
21. Rey & Fischer (2013). *Instructional Science.* https://eric.ed.gov/?id=EJ999802 `MEASURED-RCT` **(N3)**
22. Nückles et al. (2010). *Instructional Science.* https://eric.ed.gov/?id=EJ880291 `MEASURED-RCT` **(N4)**
23. Kalyuga (2012). For Whom Exploratory Learning May Not Work. *TICL.* https://eric.ed.gov/?id=EJ1258248 `OBSERVED`

**Decision rules, progress monitoring, the two clocks**
24. **Fuchs, Hamlett & Stecker (1991).** *AERJ* 28(3). https://doi.org/10.3102/00028312028003617 `MEASURED-RCT`
25. Van Norman, Klingbeil, Truman & Nelson (2023) — trend-rule latency 7–10 weeks `MEASURED-BENCH` (via H1)
26. Van Norman & Christ (2016). *SPR* 45(3). https://doi.org/10.17105/spr45-3.296-309 `MEASURED-BENCH`
27. Van Norman & Christ (2016). *JSP* 58. https://doi.org/10.1016/j.jsp.2016.07.003 `MEASURED-BENCH`
28. Ardoin, Christ, Morena & Cormier (2013). *JSP* 51(1). https://doi.org/10.1016/j.jsp.2012.09.004 `OBSERVED`
29. Deno (1985). CBM origin. *Exceptional Children* (via H1) `OBSERVED`

**Bandits, RL, adaptive experimentation**
30. **Doroudi, Aleven & Brunskill (2019).** *IJAIE* 29:568–620. https://doi.org/10.1007/s40593-019-00187-x `MEASURED-META`
31. **Riedmann, Schäper & Lugrin (2025).** Reinforcement Learning in Education: A Systematic Literature Review. *IJAIED* 35:2669–2723. https://doi.org/10.1007/s40593-025-00494-6 — **full text retrieved** `MEASURED-META` **(N5, N6)**
32. **Rafferty, Ying & Williams (2019).** *JEDM* 11(1):47–79. https://eric.ed.gov/?id=EJ1220507 — **full text retrieved** `MEASURED-BENCH` **(N8)**
33. **Cai, Grossman, Lin, Sheng, Wei, Williams & Goel (2021).** Bandit algorithms to personalize educational chatbots. *Machine Learning.* https://doi.org/10.1007/s10994-021-05983-y `MEASURED-RCT` **(N7)**
34. **Schmucker, Pachapurkar, Bala, Shah & Mitchell (2023).** Learning to Give Useful Hints. *AIED*, LNCS. https://doi.org/10.1007/978-3-031-42682-7_26 `MEASURED-RCT`
35. **Bassen et al. (2020).** RL for the Adaptive Scheduling of Educational Activities. *CHI.* https://doi.org/10.1145/3313831.3376518 `MEASURED-RCT`
36. Mandel, Liu, Levine, Popović & Brunskill (2014). Offline policy evaluation across representations. *AAMAS.* https://doi.org/10.5555/2615731.2617417 `MEASURED-BENCH`
37. Rollinson & Brunskill (2015). From Predictive Models to Instructional Policies. *EDM.* `OBSERVED`
38. Papoušek, Stanislav & Pelánek (2016). *LAK '16* `MEASURED-RCT` (via F11) **(N12)**
39. Liu & Koedinger (2017). Closing the Loop. *EDM.* https://doi.org/10.5281/zenodo.3554625 — abstract reports *"significant learning gains relative to a control condition"*; **effect size not retrievable, PDF truncated to first page** `MEASURED-RCT` / partly `UNVERIFIED-IN-SESSION`
40. Cen, Koedinger & Junker (2006). Learning Factors Analysis. *ITS*, LNCS. https://doi.org/10.1007/11774303_17 `OBSERVED`
41. *Cold Start Problem: An Experimental Study of Knowledge Tracing Models with New Students* (2025). *AIED*, LNCS. https://doi.org/10.1007/978-3-031-98459-4_30 — **abstract not retrievable; no claim made** `UNVERIFIED-IN-SESSION`

**Adaptive testing**
42. Weiss (1982). Improving Measurement Quality and Efficiency with Adaptive Testing. *APM.* https://doi.org/10.1177/014662168200600408 `OBSERVED`
43. Choi, Grady & Dodd (2011). A New Stopping Rule for CAT (PSER). *EPM.* https://eric.ed.gov/?id=EJ914074 `MEASURED-BENCH`
44. Stopping Rules for CAT When Item Banks Have Nonuniform Information (2020). *IJT.* https://eric.ed.gov/?id=EJ1254419 `MEASURED-BENCH`

**Ethics, law, and the cost of exploration**
45. **Meyer, Heck, Holtzman, Anderson, Cai, Watts & Chabris (2019).** *PNAS.* https://doi.org/10.1073/pnas.1820701116 `MEASURED-RCT` **(N10)**
46. EU AI Act (Reg. 2024/1689) Arts. 3(34), 3(39), 5(1)(b), 5(1)(f), 6(3), 26(2), 26(11), Annex III(3)(b) — via F8, verified against artificialintelligenceact.eu `[VERIFIED]`
47. COPPA 16 CFR 312.2 (facial templates, voiceprints) — via F8 `[VERBATIM]`
48. IDEA; GDPR Arts. 9(1), 17, 20, 22(1) — via F8/F5 `[VERIFIED]`

**Learning-science floor (magnitudes used in the menu and the substrate)**
49. Yang, Luo, Vadillo, Yu & Shanks (2021). *Psych. Bulletin.* https://doi.org/10.1037/bul0000309 — **g = 0.499**, 222 studies, 48,478 students `MEASURED-META`
50. Rowland (2014). *Psych. Bulletin.* https://doi.org/10.1037/a0037559 — g = 0.50 `MEASURED-META`
51. Pan & Rickard (2018). *Psych. Bulletin.* https://doi.org/10.1037/bul0000151 — transfer d = 0.40; weakest to rearranged S–R items `MEASURED-META`
52. Cepeda, Pashler, Vul, Wixted & Rohrer (2006). *Psych. Bulletin.* https://doi.org/10.1037/0033-2909.132.3.354 `MEASURED-META`
53. Cepeda, Vul, Rohrer, Wixted & Pashler (2008). *Psych. Science.* https://doi.org/10.1111/j.1467-9280.2008.02209.x `MEASURED-META`
54. Classroom spacing meta-analysis (2025), PMC12189222 — d = 0.54 [0.31, 0.77] `MEASURED-META`
55. Latimier, Peyre & Ramus (2020). *EPR.* https://doi.org/10.1007/s10648-020-09572-8 — **expanding vs uniform g = 0.034 n.s.** `MEASURED-META` **(N11)**
56. Kobayashi (2024) — teaching expectancy g = 0.48 vs g = −0.02 (via C3) `MEASURED-META`
57. Barbieri, Miller-Cotto, Clerjuste & Chawla (2023). *EPR.* https://doi.org/10.1007/s10648-023-09745-1 — worked examples g = 0.48 `MEASURED-META`
58. Schneider et al. (2018) — signalling g = 0.43, k = 209 (via C1/C3) `MEASURED-META`
59. Richter, Scheiter & Eitel (2016). *Educational Research Review.* https://doi.org/10.1016/j.edurev.2015.12.003 `MEASURED-META`
60. Fyfe, McNeil, Son & Goldstone (2014). https://doi.org/10.1007/s10648-014-9249-3 — ⚠️ systematic review, **no pooled ES** `MEASURED-META`
61. Alfieri, Brooks, Aldrich & Tenenbaum (2011). *JEP.* https://doi.org/10.1037/a0021017 `MEASURED-META`
62. Major, Francis & Tsapali (2021). *BJET.* https://doi.org/10.1111/bjet.13116 — **16 RCTs, 53,029 learners, d = 0.18 overall / 0.35 level-adaptive** `MEASURED-META`
63. Stockard, Wood, Coughlin & Rasplica Khoury (2018) — DI dosage (via H1/I1) `MEASURED-META`
64. Swanson & Hoskyn (1998); Swanson & Sachse-Lee (2000) (via H1) `MEASURED-META`
65. Gersten et al. (2009). *RER* (via H1) `MEASURED-META`

**Learning styles and the debunked tier**
66. Pashler, McDaniel, Rohrer & Bjork (2008/2009). *PSPI.* https://doi.org/10.1111/j.1539-6053.2009.01038.x `MEASURED-META`
67. Rogowsky, Calhoun & Tallal (2015). *JEP.* https://doi.org/10.1037/a0037478 `MEASURED-RCT`
68. Husmann & O'Loughlin (2019). *ASE.* https://doi.org/10.1002/ase.1777 — N = 426 `MEASURED-RCT`
69. Melzner & Kappes (2024). *Instructional Science.* https://doi.org/10.1007/s11251-024-09689-1 — N = 222 `MEASURED-RCT`
70. Newton & Salvi (2020). *Frontiers in Education.* https://doi.org/10.3389/feduc.2020.602451 — 89.1% of 15,405 educators `MEASURED-META`
71. Melby-Lervåg, Redick & Hulme (2016). *PoPS.* https://doi.org/10.1177/1745691616635612 `MEASURED-META` **(N2)**
72. Schwaighofer, Fischer & Bühner (2015). *Educational Psychologist.* https://doi.org/10.1080/00461520.2015.1036274 `MEASURED-META`
73. Working Memory and Instructional Fit (2025). *Behavioral Sciences* 15(6):765. https://doi.org/10.3390/bs15060765 — **narrative review** `OBSERVED`
74. Buljan et al. (2018). *J. Clinical Epidemiology.* https://doi.org/10.1016/j.jclinepi.2017.12.003 — preference d ≈ 0.48, knowledge 0 `MEASURED-META` (via F10)
75. Scharrer, Rupieper, Stadtler & Bromme (2017). *PUS* (via F10) `MEASURED-RCT`

**Open learner models and bidirectionality**
76. Jivet, Scheffel, Drachsler & Specht (2017). Awareness Is Not Enough. *EC-TEL.* https://doi.org/10.1007/978-3-319-66610-5_7 `MEASURED-META` **(N9)**
77. Matcha, Uzir, Gašević & Pardo (2020). *IEEE TLT.* https://doi.org/10.1109/TLT.2019.2916802 `MEASURED-META`
78. Bull (2016). Negotiated learner modelling. *RPTEL.* https://doi.org/10.1186/s41039-016-0035-3 `OBSERVED`

*(Bodily et al. 2018 LAK, Gervet et al. 2020, Mettler et al. 2011, Pelánek et al. 2016, and the
srs-benchmark README are cited in-text and are fully referenced in F5 §10 and F11 §14; they are not
re-listed here.)*

---

## 14. Handoff notes for the survey draft

- **Lead with §0 and §2, not §1.** The history is the *warrant*, not the opening. What becomes
  buildable is a 30-second probe that makes fifty years of failed personalisation finally
  tractable, in one narrow place. Open there; carry the guardrail in the same breath (AUDIT §3.4).
- **§5.1 is the section's honest centre of gravity.** Universals go in the substrate; the policy is
  small. Any survey prose that implies the policy is where the value lives will be contradicted by
  the corpus this project already assembled.
- **The two tables to reproduce verbatim in the survey:** Riedmann's Table 2 (§6.2) and the
  grading table (§9). They do more work than any paragraph.
- **Do not restate `d = 0.971`.** Standing correction; report 0.505 / −0.428 / ≈0.93.
- **Claim J1-A is a runnable experiment and should be proposed as one**, with the deletion
  condition stated. A survey section that names the experiment that would kill its own proposal is
  the standard this project set.
