---
title: "The Explanation Atlas — grading the best explanations in the world against a fidelity standard nobody has applied"
wave: N
date_researched: 2026-07-29
sources_count: 58
---

# The Explanation Atlas

> *"There is some YouTube creator-educator in every field who is like this — zero to hero
> in a few hours. The point is researching the best-of-best in the field or chapter or
> module from YouTube, and deciding a plan to deliver the best way."*

The instinct is correct and the trap is real, and this section is about the distance
between them. It resolves in a specific place: **the candidate explanations are public,
free, and enormous in number; the grading standard exists (§29); the outcome data does
not exist and never has.** The first two are assets. The third is the whole opportunity.

---

## §0 — Lead with what becomes possible

Three things are true simultaneously, and holding all three is the section's job.

1. **The corpus is already built.** Several thousand hours of the best explanation
   humans have produced, for essentially every concept in the undergraduate canon, sitting
   in public at zero marginal cost. Nothing in the pre-AI world had this.
2. **Every number attached to it measures the wrong variable.** Views, likes, subscribers,
   average view duration, audience retention — all of these live on the *felt* axis, which
   §01 establishes moves at **d ≈ 0.48 while knowledge moves zero**. `MEASURED-META`,
   §01/§22. And this is not merely an inference from the general finding: it has been
   measured directly on this exact corpus (§1.4 below).
3. **The grading predicates exist and require no learners.** §29's four fidelity
   invariants plus its two failure modes can be evaluated against a transcript. If those
   mechanical grades predict delayed unassisted transfer, you can select — and eventually
   generate — explanations without running a trial each time.

**Step 3 is the compounding part and it is also the falsifier.** If mechanically graded
features do not predict delayed transfer, the atlas is a taste ranking with extra steps
and should not be built.

### The observation this section is organised around

> **YouTube has run the largest uncontrolled experiment in explanation in human history —
> billions of hours — and instrumented entirely the wrong variable.**

Nobody knows which explanation of eigenvectors, or entropy, or the limit definition,
produces the best **delayed unassisted transfer**. This section spent its budget
establishing that this sentence is literally true rather than rhetorically true, and it
survives (§1.5, §5's falsifier).

### A standing rule for this section

**Creator and platform metrics are `OBSERVED` at best and are never evidence of learning.**
This is restated at every point where a platform number appears, because the entire failure
mode this section guards against is a reader carrying a view count forward as if it meant
something about teaching. 211,453 views tells you a video is watchable. It tells you
nothing about whether it teaches.

### Original measurement in this section

Unusually for this survey, §3 and §4 report **measurements taken by this survey rather than
retrieved from a literature.** They are labelled `OBSERVED (own harvest, 2026-07-29)` with
n stated, and the extraction method is described well enough to be re-run. They are
observational and popularity-biased, and §3.6 says exactly how.

---

## §1 — What is actually known about explanation quality

The brief for this section predicted this literature would be nearly empty. **That
prediction was wrong, and the correction is the more useful result.** The literature is
large, decades old, and filed under a name nobody searching for "explanation quality"
would find: **refutation text**.

### 1.1 The head-to-head studies exist

These take two or more different explanations of the *same* concept, randomise learners,
and measure a learning outcome.

| Study | Design | Outcome | Delay |
|---|---|---|---|
| **Muller, Bewes, Sharma & Reimann (2008)**, *J. Computer Assisted Learning* 24(2), DOI `10.1111/j.1365-2729.2007.00248.x` | **N = 364** first-year physics students randomised to **four different explanations of the same content** (Newton's First and Second Laws): Exposition / Extended Exposition / Refutation / Dialogue | Mechanics conceptual inventory items. **d = 0.79** (Refutation vs Exposition), **d = 0.83** (Dialogue vs Exposition). Low prior knowledge benefited most; high prior knowledge **not** disadvantaged | **None.** Pre/post, same session |
| **Kulgemeyer (2020)**, *Research in Science Education*, DOI `10.1007/s11165-018-9787-7` | Two purpose-built explanation videos, **same topic, both scientifically correct, same learning opportunities** — one high explaining quality, one low. **n = 90 vs 86** | Declarative knowledge **d = 0.42, p = 0.007**. Conceptual knowledge measured but not reported as significant — treat as a **partial null** | **None** |
| **Peltier, Heddy & Peltier (2020)**, *Annals of Dyslexia* | **n = 97** preservice teachers randomised to a researcher-written refutation text **or an actual published document** — the International Dyslexia Association's "Dyslexia Basics" fact sheet | **η² = 0.33** posttest; **η² = 0.175** delayed posttest (n = 75 retained) | Yes, interval not retrieved |

All `MEASURED-RCT`.

Muller is the load-bearing one for this section, and not only for its effect size. **The
person who ran it is Derek Muller, who then founded Veritasium.** The single most
successful science explainer on the platform built his format out of a randomised trial he
ran himself. That is the strongest existing bridge between the literature and the corpus,
and §5 returns to it.

### 1.2 The meta-analytic picture

**Schroeder & Kucera (2022)**, "Refutation Text Facilitates Learning: A Meta-Analysis of
Between-Subjects Experiments," *Educational Psychology Review* 34, DOI
`10.1007/s10648-021-09656-z`. `MEASURED-META`.

- Overall **g = 0.41, 95% CI [0.30, 0.51], k = 44 independent comparisons, n = 3,869**.
- Against **expository text on the same topic specifically: k = 30, g = 0.36**.
- Heterogeneity **Q(43) = 109.59, p < .001, I² = 60.76**.
- Publication bias: Egger t(42) = 0.55, one-tailed p = .29; **trim-and-fill imputed 10
  studies and adjusted the estimate down to g = 0.28 [0.16, 0.39]**; fail-safe N = 1,625.

Quote the adjusted **g = 0.28**, not the headline 0.41, and say which.

**Danielson, Jacobson, Patall & Sinatra (2024)**, *Educational Psychologist*, DOI
`10.1080/00461520.2024.2365628` — pre-registered; **71 articles (53 published, 18
unpublished), 76 studies, 111 samples, 294 effect sizes, 26 moderators**; consistent
significant advantage for refutation, and **"moderators neither enhanced nor diminished"**
it. The overall g **could not be retrieved** (paywalled, no OA copy, no preprint located).
Do not quote a number for this one.

**Guzzetti (2000)**, *Reading & Writing Quarterly*, states two things worth carrying:
*"only refutational text shows long-term effects"* and *"students prefer refutational
text."* A preference/learning statement made in 2000, in the same sentence pair, in the
one place where they happen to agree. They usually do not.

### 1.3 Delay is where the evidence thins to nothing

This is the finding that matters most for the atlas, because delayed unassisted transfer
is the atlas's outcome variable.

Schroeder & Kucera coded delay and found it **did not moderate**: same day k = 17
(g = 0.39); 2 days–1 week k = 11 (g = 0.38); 8 days–1 month k = 13 (g = 0.43); **more than
one month k = 2 (g = 0.56)**. **Qb(4) = 0.48, p = .98.** `MEASURED-META`.

Read the k values, not the g values. **Exactly two studies in a 44-comparison meta-analysis
looked past one month**, and both were on light and heat/temperature. The non-moderation
result is real but it rests on almost no long-delay data.

Worse for our purposes: **Schroeder & Kucera did not code transfer at all.** They coded item
*format* (multiple choice, open-ended, true/false, Likert), which did not moderate either
(Qb(5) = 3.76, p = .58). The multimedia-principle meta-analyses that *do* separate transfer
from retention — Ginns et al. on personalisation, Rey et al. on segmenting — test transfer
**immediately**.

**Rittle-Johnson, Loehr & Durkin (2017)**, *ZDM*, DOI `10.1007/s11858-017-0834-z`, states
the gap plainly for the adjacent self-explanation literature: gains appear *"when assessed
immediately after the intervention,"* but *"evidence that self-explanation reliably promotes
learning within a classroom context or retention of knowledge over a delay is much more
limited."*

> **`OPEN` — nobody has measured delayed unassisted transfer as a function of which
> explanation you read.** *Why nobody asked:* the refutation-text literature is a
> conceptual-change literature. Its research question is whether a misconception was
> displaced, which is naturally tested immediately and with recognition items, because
> that is what conceptual-change theory predicts about. Nobody framed the question as
> *ranking explanations*, so nobody needed the outcome that ranking requires. The
> instruments exist; the framing did not.

### 1.4 Real published explanations: rated, never tested

Here the brief's prediction *was* right, and precisely. The field does study real published
explanations — and it stops at rating them.

- **Kulgemeyer & Peters (2016)**, "Exploring the explaining quality of physics online
  explanatory videos," *European Journal of Physics* 37(6), DOI
  `10.1088/0143-0807/37/6/065705`. Rates real YouTube videos against a rubric. **No
  learning outcome.**
- **Bitzenbauer et al. (2023)**, "Exploring the Relationship Between Surface Features and
  Explaining Quality of YouTube Explanatory Videos," *Int. J. Science and Mathematics
  Education*, DOI `10.1007/s10763-022-10351-w`. **N = 60 real YouTube videos** on quantum
  entanglement and tunnelling, coded for explaining quality, correlated against YouTube's
  public metrics. **No learners tested.** The abstract states the result this section needs,
  verbatim:

  > *"the surface features provided by YouTube (e.g. number of views or likes) do not seem
  > to be suitable indicators of the videos' explaining quality. Instead, the number of
  > content-related comments was found to be statistically significantly correlated with
  > the explaining quality."*

  `MEASURED-BENCH`. **This is the direct measurement of the collision.** It is not a
  general argument about felt-versus-real learning applied to YouTube by analogy — someone
  graded sixty real videos and checked. Views and likes did not track quality. Note
  carefully what the positive result is and is not: *content-related comment count*
  correlates with a **rubric score for explaining quality**, not with any learning outcome.
  It is the best public signal anyone has found and it is still two steps from the thing
  we care about.
- **Abed & Barzilai (2023)**, *J. Computer Assisted Learning*. Eighth-graders rank six real
  YouTube climate-change videos. The outcome is **students' evaluation criteria and quality
  judgments** — the preference-for-learning substitution, executed deliberately, as the
  study's actual research question.
- **Mikk (2002)** (ERIC, conference paper, no DOI, not peer-reviewed) reports an
  experimental comparison of **two Estonian textbooks** on comprehension, acquisition,
  information gain and persistence of knowledge. **This is the only textbook-versus-textbook
  learning experiment located, and it is grey literature.** `UNVERIFIED`.

So the strict version of the question — *take two real, already-published explanations of
the same concept and test which one teaches better* — has, as far as this survey can
establish, **one journal-quality instance (Peltier et al. 2020, against a dyslexia fact
sheet) and one grey-literature instance (Mikk 2002)**, in the entire literature.

### 1.5 The expert blind spot literature does not measure learning

This is a clean, locatable gap and it is worth stating exactly, because the phrase is
often invoked as though it carried outcome evidence.

- **Nathan & Petrosino (2003)**, "Expert Blind Spot Among Preservice Teachers," *AERJ*
  40(4), DOI `10.3102/00028312040004905`, **N = 48**. The outcome variable is preservice
  teachers' **judgments** of student problem difficulty, checked against known student
  performance patterns. **No student learning outcome. No explanation is delivered to any
  learner.**
- **Nathan & Koedinger (2000)**, *Cognition and Instruction* 18(2), DOI
  `10.1207/s1532690xci1802_03`, and *JRME* 31(2), DOI `10.2307/749750`. Outcome:
  **teacher belief rankings.**

A terminology warning that matters for anyone reading downstream: **the "reversal effect"
in this literature is a reversal of the expected *difficulty ordering*** — students solve
story problems better than the matching symbolic equations — **and is unrelated to the
cognitive-load "expertise reversal effect"** of Kalyuga et al. Two literatures, one phrase.

> **`OPEN` — nobody has closed the loop from expert misprediction to learner outcome.**
> No study takes an expert-generated explanation and a novice-informed explanation of the
> same concept and compares what learners actually learn from each. *Why nobody asked:*
> the expert-blind-spot programme sits in teacher-education research, where the dependent
> variable of interest is teacher cognition; the outcome-measurement programme sits in
> instructional design, where the manipulation is a design principle rather than an
> author's expertise. The two never had a reason to meet.

### 1.6 And a null that undercuts the whole premise of "instructional explanation"

**Wittwer & Renkl (2010)**, "How Effective are Instructional Explanations in Example-Based
Learning? A Meta-Analytic Review," *Educational Psychology Review*, DOI
`10.1007/s10648-010-9136-5`, **k = 21**. Verbatim: *"the benefits of instructional
explanations for example-based learning per se are minimal"* — they help conceptual more
than procedural knowledge, and are *"not necessarily more effective than other methods
supporting example processing such as self-explaining."* `MEASURED-META`.

Two cautions. First, **the numeric d/g could not be retrieved** (paywalled, no OA copy);
quote the qualitative conclusion and k = 21 only. Second, **a correction to this section's
own brief**: the 2008 paper often cited here — Wittwer & Renkl, "Why Instructional
Explanations Often Do Not Work," *Educational Psychologist* 43(1), DOI
`10.1080/00461520701756420` — is a **theoretical framework paper with no pooled effect
sizes.** The meta-analysis is the 2010 one.

This null is the one that should worry an atlas-builder most, and §6 treats it as a
boundary condition rather than a refutation: it says that *being explained to* is a weak
intervention relative to *explaining*, which is exactly what §05 and §02 of this survey
already say (learning by teaching **g = 0.56**, robust at delay). An atlas of explanations
is therefore an input to a loop that ends in the learner producing, not a product on its
own. That constraint is load-bearing in the design.

---

## §2 — Is video instruction measured at all?

Yes, once, well, and the headline number is routinely misread.

### 2.1 The meta-analysis

**Noetel, Griffith, Delaney, Sanders, Parker, Cruz & Lonsdale (2021)**, "Video Improves
Learning in Higher Education: A Systematic Review," *Review of Educational Research*, DOI
`10.3102/0034654321990713`, 333 citations. `MEASURED-META`.

- Five databases, 27 keywords, **9,677 unique records**, 329 full texts screened,
  **105 studies met inclusion**, pooled **N = 7,776** students. Randomised trials only.
- **Swapping video for existing teaching: g = 0.28.**
- **Adding video to existing teaching: g = 0.80.**

**The g = 0.80 is a dose effect, not a medium effect.** Adding video to existing teaching
adds instruction; the comparison is more-instruction versus less-instruction, and it would
look similar if you added anything. The fair comparison — the one that asks whether video
is a good way to explain — is the **swap**, and it is **g = 0.28**. Anyone quoting 0.80 as
evidence that video teaches well is quoting the wrong row.

g = 0.28 is a real, positive, modest effect. It is smaller than retrieval practice
(g = 0.499, §01), smaller than learning by teaching (g = 0.56, §01), smaller than refutation
text over expository text before publication-bias correction (g = 0.36, §1.2), and roughly
equal to it after (g = 0.28). **Video is not a strong intervention. A good explanation
delivered any way is a moderate one.**

### 2.2 Khan Academy's own evaluation says, in its own words, that it is not an evaluation

This is the most-cited evidence about the most-used educational video corpus in the world,
and it is routinely misread.

**Murphy, Gallagher, Krumm, Mislevy & Hafter (2014), "Research on the Use of Khan Academy
in Schools," SRI Education**, funded by the Bill & Melinda Gates Foundation. Nine California
pilot sites, two years, public/charter/independent, elementary through high school.
`OBSERVED` — retrieved and read in full, 2026-07-29.

The report's own framing, verbatim:

> *"Because of the early-stage, emergent nature of both Khan Academy as a school resource
> and the schools' personalized learning implementation practices, **SRI conducted an
> implementation study rather than an evaluation of Khan Academy's impact.** An experimental
> test of an intervention's impact (a randomized control trial) would have required a
> clearly specified treatment, including a protocol for its enactment. Because neither the
> Khan Academy resources and tools nor the way in which they were used in classrooms was
> stable across the various study sites and across the 24 months of this work, it was too
> soon to attempt a rigorous evaluation."*

And: *"**Providing definitive evidence of the effectiveness of Khan Academy use in classrooms
is not yet possible.**"* And on the correlational analyses that do appear:
*"these analyses are exploratory and warrant further investigation, and **cannot be used to
establish a causal connection** between Khan Academy use and improved test scores."*

**The effect sizes that circulate from this report are confounded and the report says so in
the same sentence.** The widely-quoted **+0.61 SD** (ninth-grade Algebra 1, SY 2011-12) and
**+1.03 SD** (same cohort, tenth grade) are described by SRI as the gain *"as a result of
attending the school after the school introduced **Khan Academy and other instructional
reforms**."* One site, no randomisation, a bundle of simultaneous changes. Anyone quoting
+0.61 as Khan Academy's effect size is quoting a school-reform effect and attributing it to
a video library.

**What the report does measure cleanly is belief.** *"Roughly 85% of teachers reported that
they believed Khan Academy had made a positive impact (somewhat or strong) on students'
learning and understanding of the material overall,"* and 87% believed it improved
independent working. `OBSERVED`. **This is the felt axis, measured on teachers instead of
students, and it is the only well-powered outcome in the study.** The pattern §01 describes
reproduces itself perfectly: the attitudinal variable is measured precisely and at scale;
the learning variable is declared not yet measurable.

### 2.3 The one controlled Khan Academy study, and the trap inside its second finding

**Kelly & Rutherford (2017), "Khan Academy as Supplemental Instruction: A Controlled Study
of a Computer-Based Mathematics Intervention," *International Review of Research in Open and
Distributed Learning*.** Seventh-grade students, four weeks, Khan Academy as intervention
versus control, plus a comparison of students with and without supplemental maths
instruction. `MEASURED-RCT`.

> *"In both cases, we found **no statistically significant differences in student test
> scores.**"*

And then, in the very next sentence of the abstract:

> *"Khan Academy has several internal metrics used to track student performance and use.
> **We found significant relationships between these metrics and student test scores** in
> this study."*

**Read those two findings together, because together they are this section's thesis in
miniature.** The platform's own engagement metrics correlate with test scores. The platform
itself, randomised, moves test scores by nothing. Cross-sectional correlation between
engagement and achievement is exactly what you would expect if stronger students engage
more — it is a selection signature, not a causal one. **A metric can correlate with learning
and still be worthless as a target**, and this is a measured instance rather than a
theoretical worry.

`OPEN` — **there is no adequately-powered randomised trial of Khan Academy's video corpus
as such.** *Why nobody asked:* SRI states the reason precisely — an RCT *"would have
required a clearly specified treatment,"* and a library that teachers use however they like
is not a treatment. The corpus's greatest strength as a product, its flexibility, is exactly
what makes it unevaluable by the standard design. **An explanation atlas does not inherit
this problem**, because its unit of analysis is a *single explanation of a single concept*,
which is a specifiable treatment. That is an underrated argument for building it.

---

## §3 — Is any YouTube-side signal behavioural rather than attitudinal?

This is the section's first original contribution, and the answer is **partly yes, and it is
much weaker than the hypothesis predicted.**

The hypothesis worth testing: views, likes and subscribers are attitudinal and therefore on
the felt axis, but **where viewers scrub backwards** is a *behaviour*, and is plausibly
where comprehension failed. Similarly, **drop-off location** (as distinct from drop-off
rate) is behavioural. Are either measured, and are either exposed?

### 3.1 What the APIs expose — the negative result first

`MEASURED-BENCH`, from the API documentation, retrieved 2026-07-29.

**YouTube Data API v3** (`videos.list`, `statistics` part) exposes exactly five properties:
`viewCount`, `likeCount`, `dislikeCount` (deprecated), `favoriteCount` (deprecated, always
0), `commentCount`. **There is no property relating to retention, watch time, average view
duration, replays or rewinds.** All five surviving fields are attitudinal or aggregate-count.

**YouTube Analytics API** does expose exactly the two metrics we want:
- **`audienceWatchRatio`** — the proportion of viewers watching at a given point in the
  video, requiring the `elapsedVideoTimeRatio` dimension. This is drop-off *location*.
- **`relativeRetentionPerformance`** — retention against similar-length videos, 0–1 scale,
  same dimension.

**And it is owner-only.** The scopes are `yt-analytics.readonly` and
`yt-analytics-monetary.readonly`, both scoped to *"your YouTube content"*; the resource
documentation restricts groups to content *"you have uploaded or claimed or that are linked
to a channel that you administer."* You cannot obtain retention curves for a video you do
not own.

> **`OBSERVED` — the single most diagnostic signal YouTube computes is computed for every
> video on the platform, shown to one person per video, and exposed to nobody else.**

### 3.2 What *is* public: the replay heatmap

The exception is real and, as far as this survey can establish, unexploited by the research
literature.

Fetching a watch page with an ordinary browser user-agent returns, inside the page's
embedded JSON, a `macroMarkersListEntity` with `"markerType": "MARKER_TYPE_HEATMAP"` — the
data behind the player's *"Most replayed"* graph. Each entry is
`{startMillis, durationMillis, intensityScoreNormalized}`, plus a `markersDecoration`
carrying the literal label *"Most replayed"* at the peak.

This is **behavioural**. It is aggregated rewatch density. It requires no API key, no OAuth,
and no channel ownership.

`OBSERVED (own harvest, 2026-07-29)`. Extraction confirmed on 51 videos; method is a single
`curl` with a browser user-agent plus a regular expression over the returned JSON.

### 3.3 Four structural properties, measured, that constrain every use of it

`OBSERVED (own harvest, 2026-07-29, n = 51 educational videos)`.

**(a) It is exactly 100 buckets, always.** Bucket duration is video length ÷ 100, verified
across lengths from 175 s to 9,500 s. So the temporal resolution *degrades linearly with
video length*: 2.4 s per bucket for a 4-minute explainer, **30.8 s per bucket for MIT
OpenCourseWare's 51-minute eigenvalue lecture**, and roughly 230 s per bucket for a
6-hour compiled course. **For long-form single-take teaching — precisely the format the
owner's proposal is about — the signal cannot localise below a four-minute window.**

**(b) It is min–max normalised inside each video.** Of 51 videos, **51 had a minimum of
exactly 0.0 and 51 had a maximum of exactly 1.0.** Not approximately — exactly, in all
cases. **Cross-video comparison of replay amplitude is therefore impossible by
construction.** You cannot use this to rank two explanations of the same concept against
each other. You can only use it to locate the hardest spot *within* one explanation. This
single property removes the most obvious application.

**(c) Coverage is gated on popularity.** 51 of 60 search-returned educational videos (85%)
exposed a heatmap. The lowest view count *with* a heatmap was **54,373**; the videos
*without* had a median of **8,173** views. Cassie Kozyrkov's MFML Part 1 (211,453 views) and
Part 2 (65,603) both expose heatmaps; **Part 3 (47,699 views) does not.** So the one
non-attitudinal signal on the platform is only available where the attitudinal signal is
already large — **popularity selection re-enters through the only door that was supposed to
be free of it.** The 85% figure is itself popularity-biased, since the sample came from
search results; the true coverage over all educational video is far lower.

**(d) It is weak.** This is the important one. Normalised entropy of the interior replay
distribution has a **median of 0.976** across the 51 videos (1.0 = perfectly flat), range
0.862–0.992. The top decile of buckets holds a **median 19.5%** of interior replay mass
against 10% under uniformity — **a 1.95× enrichment**. Half the replay mass is spread over
**33% of the video** where uniformity would give 50%.

> **The replay heatmap is a real behavioural signal with roughly a 2× signal-to-background
> ratio. It is not a comprehension-failure detector. It is a faint tilt.**

### 3.4 The decisive test: peaks do not track the concept

If replay density tracked *where a concept is intrinsically hard*, then different
explanations of the same concept should peak in the same place — because expositions of a
canonical topic run in roughly canonical order.

`OBSERVED (own harvest, 2026-07-29)`. Six concepts, 49 videos with heatmaps, peak position
measured as percent-through-video, first and last 5% excluded to remove the restart artifact:

| Concept | n | Interior peak positions | SD |
|---|---|---|---|
| eigenvectors | 8 | 14, 14, 32, 39, 48, 57, 67, 85 | 23.4 pp |
| entropy | 8 | 24, 37, 45, 47, 48, 48, 82, 89 | 20.6 pp |
| derivative / limit | 6 | 47, 49, 56, 64, 77, 85 | 14.1 pp |
| Bayes' theorem | 9 | 10, 12, 19, 27, 53, 71, 79, 92, 95 | 32.7 pp |
| transformers | 10 | 21, 32, 34, 56, 57, 60, 62, 66, 73, 77 | 17.7 pp |
| Fourier transform | 8 | 29, 33, 50, 57, 62, 67, 71, 74 | 15.8 pp |

- **Mean within-concept SD: 20.7 pp**
- **Total SD across all videos: 22.6 pp**
- **SD of a uniform distribution on [5, 95]: 26.0 pp**

Knowing which concept the video is about explains roughly **16% of the variance in peak
position** (1 − 20.7²/22.6²), and some of that is contamination — the "transformer" query
returned electrical transformers alongside attention transformers, which are genuinely
different topics and inflate the between-concept term.

**Null result.** Replay density is **not** a property of the concept. Two readings survive
the data and they have opposite consequences:

- *(a) It is mostly noise*, in which case the signal is useless.
- *(b) It is a property of the specific explanation rather than of the concept*, in which
  case it is exactly the per-explanation diagnostic an atlas wants.

> **`OPEN` — which of these is true is not decidable from the heatmap alone**, and the
> discriminating experiment is cheap: instrument one cohort on one video, collect both the
> scrub log and a delayed transfer test, and check whether individual rewind location
> predicts individual item failure. *Why nobody asked:* the people with scrub logs are
> platforms optimising watch time, for whom "this bit was confusing" is a retention risk to
> be edited out rather than a diagnostic to be published; the people who want the diagnostic
> have never had the logs.

### 3.5 The confound that damages it further

`OBSERVED (own harvest, 2026-07-29, n = 10 videos with ≥4 chapter timestamps)`. For each
video, distance from the interior replay peak to the nearest chapter start, against a
Monte-Carlo null of 2,000 random interior points per video:

- Mean distance, **observed peak → nearest chapter start: 49.8 s**
- Mean distance, **random point → nearest chapter start: 87.6 s**
- Peaks closer to a chapter boundary than chance: **7 of 10**

n = 10 is small and this should not be over-read, but the direction is unambiguous and the
mechanism is obvious: **the chapter UI generates navigation clicks, and navigation clicks
land in the replay data.** A chunk of what looks like "viewers went back because they were
confused" is "viewers clicked a chapter link."

This is a third `OBSERVED` negative, and it is the one that most directly damages the
proposal to mine rewinds for comprehension failure: **the signal is contaminated by the
navigation affordance, and the contamination scales with how well-structured the video
is** — which is to say, it is worst precisely for the carefully-chaptered videos that the
atlas would most want to grade.

### 3.6 What §3 concludes

| Signal | Nature | Public? | Diagnostic of learning? |
|---|---|---|---|
| Views, likes, subscribers | Attitudinal | Yes (Data API) | **No** — measured null, Bitzenbauer 2023 |
| Comment count | Attitudinal-behavioural mix | Yes (Data API) | Only *content-related* comments, and only against a rubric, not an outcome |
| Average view duration, retention curve | Behavioural | **No** — owner-only | Untested by anyone |
| Drop-off *location* | Behavioural | **No** — owner-only | Untested by anyone |
| **Replay / rewind density** | **Behavioural** | **Yes** — undocumented, page-embedded | **~2× enrichment, concept-independent, chapter-confounded, popularity-gated, 100-bucket resolution** |

The honest summary: **the distinction between attitudinal and behavioural signals is real
and worth making, it does identify one public behavioural signal nobody in the research
literature appears to have used, and that signal is too weak and too confounded to grade
explanations on its own.** It belongs in the atlas as a *localiser* — a hint about where
inside a given explanation to look — and never as a ranker.

---

## §4 — Can a pipeline grade explanations mechanically? A prototype, and what it caught

§29 supplies four fidelity invariants a legal simplification may never falsify —
**ontology, causal sign, quantifier strength, uniqueness of mechanism** — plus two failure
modes: **machinery presented before the obstacle it dodges**, and **a determined quantity
presented as tunable.** §29 argues that several of these are *checkable predicates* rather
than judgements, and singles out the quantifier prefix as *"decidable, cheap, and where the
damage is."*

This survey built the checker and ran it. `DESIGN`, with the prototype's measured results
reported as `OBSERVED (own harvest, 2026-07-29)`.

### 4.1 The corpus, and why it is that corpus

Three MIT OpenCourseWare 18.06 (Linear Algebra, Gilbert Strang) lecture transcripts —
Lecture 1 (geometry of linear equations), Lecture 21 (eigenvalues and eigenvectors),
Lecture 22 (diagonalisation and powers of A). **1,524 sentences, 17,164 words.** Published
by MIT under **CC BY-NC-SA**, fetched directly from `ocw.mit.edu` as PDF transcripts.

The corpus is OCW rather than YouTube for a reason that turns out to be structural, and §7
develops it: **YouTube caption endpoints now return HTTP 200 with a zero-byte body for
unauthenticated requests.** Verified 2026-07-29 against 3Blue1Brown's Chapter 1 caption
track across four format parameters (none, `fmt=json3`, `fmt=srv3`, `fmt=vtt`). Every one
returned 200/0 bytes. The transcripts the pipeline needs are, on YouTube, no longer freely
fetchable.

### 4.2 What the predicates were

Six checks, implemented as lexical patterns over sentence-segmented transcript:

- **P1 — quantifier prefix order.** Sentences containing both a universal marker (*for
  every/all/any, whenever, no matter what*) and an existential marker (*there is/exists, we
  can find*), reporting the order. §29's flagship predicate.
- **P2 — obstacle before machinery.** First-occurrence index of an obstacle marker (*the
  problem is, can't, won't work, fails, hopeless, no way to*) versus a machinery marker
  (*define, we introduce, the algorithm/method/trick/formula, here's the trick*).
- **P3 — unlabelled numeric constants.** Every numeric constant with no
  determined/fitted/arbitrary marker within a ±1-sentence window.
- **P3b — determined-but-tunable.** Knob language (*hyperparameter, you can tune, up to
  you*) within ±2 sentences of a determination marker.
- **P4 — unhedged causal claim.** Causal verb with no correlational hedge in the sentence.
- **P5 — ontology balance.** Process-language sentences versus object-language sentences.

### 4.3 What it caught, hand-adjudicated

Every flag was read and judged individually. This is the whole point of the exercise; a
grader you have not adjudicated is a grader whose precision you do not know.

| Predicate | Flags | True positives | Precision |
|---|---|---|---|
| **P1 — quantifier prefix** | **0** | — | **no recall at all** |
| P2 — obstacle marker | 8 | 6 | **75%** |
| P2 — machinery marker | 3 | 1 | **33%** |
| P3 — unlabelled constant | 5 | 0 | **0%** |
| P3b — determined-but-tunable | 0 | — | — |
| P4 — unhedged causal | 14 | 0 | **0%** |
| P5 — ontology | 3 (all "PROCESS-ONLY") | 0 | vacuous — object lexicon never fired |
| **Total** | **30** | **7** | **23%** |

Over 1,524 sentences of graduate mathematics.

### 4.4 The four things this measurement establishes

**(i) §29's most confident claim about mechanical checkability does not survive contact
with spoken explanation.** P1 — the quantifier prefix, which §29 calls decidable and cheap
and the place where the damage is — **fired zero times in 1,524 sentences of a linear
algebra course.** The reason is not that the checker is bad. It is that **spoken
mathematics does not utter quantifiers; it elides them.** Strang says *"Ax is some multiple
— and everybody calls that multiple lambda — of x"*, not *"for every x there exists a
lambda."* And **elision is not detectable as falsification.** You cannot flag a quantifier
that was never said. The invariant is correct; the predicate has no purchase on the medium
where the explanations actually live. This is the section's most useful negative result,
because it is a negative about *our own* prior section.

**(ii) The false-positive risk is concentrated and diagnosable, not diffuse.** P4's 0/14
is not random error — it is one systematic failure. Mathematical *production* language
looks exactly like causal language: *"let me make it easy"*, *"combine these three vectors
to produce this one"*, *"this S inverse makes the whole thing diagonal."* Every P4 flag was
this. Similarly, three of five P3 flags were the string `18.06` — the course number. A
lexical grader in a technical domain fails on domain-specific idiom, and it fails the same
way every time, which means the failures are enumerable.

**(iii) The one predicate that half-works is §29's own original contribution.** P2's
obstacle marker reached 75% precision — genuine hits included *"there's just no way to find
out what A plus B does"* (eigenvalues do not add), *"If we don't have n independent
eigenvectors, we can't diagonalize the matrix"*, and *"you can't really visualize it."*
The false positives were an idiom (*"Two by two, it can't be that tough"*) and a sense
collision (*"the problem"* meaning exercise, not obstacle). But **recall was terrible** —
2 to 3 obstacle markers per 500-sentence lecture, and Strang names far more obstacles than
that. So the ordering verdict for P2 rests on a handful of hits and flips on any one of
them: Lecture 21 was scored a violation entirely because a single machinery marker
(*"Here's the trick"*) appeared at sentence 174 and the first surviving obstacle marker at
409.

**(iv) The design is not refuted — it is relocated.** §29's predicates are defined over
**propositional content**: a quantifier prefix, a causal sign, a labelled constant, an
ontological category. They are not defined over surface strings. Running them as regular
expressions asks a string matcher to do semantics, and it gets 23%.

### 4.5 The corrected design

`DESIGN`.

**Two stages, not one.** An extraction stage produces a structured claim representation
from the transcript — for each substantive assertion: the proposition, its quantifier
prefix made explicit (including where the speaker elided it), each numeric constant tagged
determined / fitted / arbitrary / unstated, each causal claim tagged causal / correlational
/ unmarked, and each concept's ontological category. A predicate stage then checks §29's
invariants against **that** representation, where they are genuinely decidable and cheap.

**Why this is the right split.** The expensive, error-prone, model-dependent work is
extraction, and it is *auditable*: a human can check an extracted claim against a
timestamp. The predicate check is deterministic, free, and reproducible. This is the same
architecture §13 argues for on the grounding ladder, and it inherits §13's honest ceiling
— **97% autoformalisation × 69% proving = 36% end-to-end**, because the formal statement
stops matching the informal one. Expect the extraction step to be the whole error budget.

**What it would catch that the lexical version misses:** elided quantifiers (the whole of
P1, currently at zero recall); obstacles stated without any lexical marker, which is most
of them; constants whose determination is stated three paragraphs earlier.

**What it will still miss:** anything requiring domain ground truth. Whether *"√ε is the
unique scale at which the stationary distribution equals p"* is *true* is not a linguistic
property (§29 §4.3). The grader can check that the explanation **says which kind of
constant it is**; it cannot check that the answer is right without a domain oracle.

> **What would show this was the wrong design.** If a two-stage extractor-plus-predicate
> grader does not clear **80% precision at 60% recall against a hand-adjudicated set of
> 200 flagged spans** — the standard the lexical prototype missed by a factor of three —
> then §29's invariants are not mechanically checkable at all, and every downstream use of
> mechanical grading in this section collapses. That test costs three transcripts and a
> day, and it should be run **before** anything else in §6 is built.

---

## §5 — What the elite explainers actually do

The brief asked to test the candidate mechanisms rather than assume them, and to separate
what is **measurable** from what is **stylistic**. The separation turns out to be sharp, and
one of the four canonical explainers is a clean counterexample that keeps the rest honest.

### 5.1 A provenance note, because it changes what is quotable

3Blue1Brown publishes his own transcripts at `github.com/3b1b/captions`, cross-checkable
against YouTube's **manually uploaded** caption track (`vssId: ".en"`, not ASR). Those are
safe to quote. His podcast and TEDx appearances are ASR-only and are **not** quoted verbatim
here. Two corrections worth recording so they do not propagate: the phrase **"curse of
knowledge" appears nowhere in his 241-video caption corpus** (he expresses the idea and
never uses the label), and there is **no talk titled "What makes people engage with math"** —
the real one is TEDx Berkeley 2020 (`s_L-fp8gDzY`, 19:01, 1,613,639 views), ASR-only.

### 5.2 The five candidate mechanisms, tested

**(1) Obstacle stated before machinery — MEASURABLE, and it is the strongest result here.**

Sanderson states the principle explicitly, and states it as a first-draft failure mode he has
to correct against — which is more informative than stating it as a virtue:

> *"Try very hard to structure your explanation to go from the concrete to the abstract.
> **I think almost always when you understand something the natural inclination is to go the
> other way around. I find myself doing this in pretty much any first draft of a script that
> I have.** … Otherwise it's a little bit like trying to build a building from the top floor
> down."* (SoME1 announcement, `ojjzXyQCzso`, 9:58)

> *"It makes it so that once the equation comes on the screen, or the algorithm is described,
> it doesn't feel like an expression handed down with nothing to hold onto. Instead, **it
> arrives only once it's articulating something that already exists at least loosely in the
> viewer's mind**."* ("What makes a great math explanation?", `cDofhN-RJqg`, 8:10)

> *"Another good template… is to **start with a naive but flawed solution, and then
> progressively refine it**."* (ibid., 9:52)

That is §29 §3.1 — *lead with the constraint that forces the design* — arrived at
independently and stated in almost the same words.

**And it is measurable from artifacts alone, without watching anything.** The position of
the first piece of named machinery, as a fraction of runtime, is readable off published
chapter timestamps. `OBSERVED`:

| Video | First named machinery | % of runtime |
|---|---|---|
| 3b1b, *Eigenvectors and eigenvalues* | first symbolic definition 5:27; determinant machinery 7:29 | **31.6% / 43%** |
| 3b1b, *Convolutions* | the formula | **37.7%** |
| 3b1b, *Central Limit Theorem* | the formula | **50.9%** |
| 3b1b, *Reinventing Entropy* (`l6DKRf-fAAM`) | entropy defined | **75%** |
| 3b1b, *Holograms* (`EmKQsSDlaa4`) | "The formal explanation" chapter | **82.9%** |
| Veritasium, modern chaptered videos | named machinery | **~43%** |
| **The Organic Chemistry Tutor** | machinery first, then exercises | **~0%** |

The eigenvector video is worth reading in full because the whole pattern is in one artifact.
It opens by naming the obstacle rather than the topic:

> *"Eigenvectors and eigenvalues is one of those topics that a lot of students find
> particularly unintuitive. Questions like, why are we doing this and what does this actually
> mean, are too often left just floating away in an unanswered sea of computations."*
> (0:19–1:20)

Then **one sustained 2×2 transformation for four minutes with no symbols** (1:20–5:27),
first symbolic definition at 5:27, determinant machinery at 7:29, and the payoff line at
9:16: *"an expression like this would feel completely out of the blue."* He is naming §29's
failure mode, in the video, as the thing his structure exists to avoid.

**(2) One sustained example rather than many shallow ones — MEASURABLE.**

Sanderson, from reviewing thousands of SoME entries — note that this is his *observation
across a corpus*, not a self-report about his own practice, which makes it better evidence:

> *"In general, entries that struck me as especially clear would often **keep one or two
> examples front and center**, and they'd often give a feeling of playing with those
> examples… giving the viewer a chance to build their own intuitions before general rules
> are presented."* (`cDofhN-RJqg`, 11:14)

The measurable form is **example density**, and the spread across the class is enormous.
3Blue1Brown gives one example four minutes of runtime. The Organic Chemistry Tutor's
*General Chemistry 1 Review* (`5yw1YH7YA7c`, 8,348 s) states in its own description that it
contains *"about 160 multiple choice questions"* — **roughly 52 seconds per worked
problem.** `OBSERVED`. Two formats at opposite ends of a single measurable axis.

**(3) Prediction requested before the reveal — MEASURABLE in principle, weakly executed in
the medium.**

Sanderson grounds this in the productive-failure literature (Kapur), which this survey
independently rates at **g = 0.36, rising to 0.58 at high fidelity** (§01):

> *"**If you seriously engage with a problem before you're told the answer, that actually
> makes you engage more meaningfully with the answer once it's told to you**… So the third
> thing that I put on this checklist is does the lesson start with some kind of motivating
> question?"* (JMM 2023, *"Math's pedagogical curse"*, `UOuxo6SA8Uc`)

And he concedes the medium's limit in the same talk: *"you have to invite the audience to
pause and think about it… realistically, a lot of people are a little bit more passive in
that moment."* The marker is countable — **"pause and ponder" appears in 34 of his
videos** — but the *compliance* is not observable from the artifact at all, and it is the
compliance that carries the effect. This is the mechanism where video is structurally
weakest, and it is exactly what §8.3's bolt-ons exist to supply.

**(4) Explicit naming of the misconception being displaced — MEASURABLE, and it is the only
one with a randomised trial attached.**

This is Muller's manipulation, and §1.1's numbers are the evidence: **Refutation d = 0.79,
Dialogue d = 0.83, against Exposition, N = 364.** The feature is countable in a transcript —
does the explanation state a wrong belief and mark it as wrong before correcting it —
and it is the highest-value entry in the atlas's feature set because it is the one whose
effect size is already known.

**(5) Long single-take duration as a signal of coherence — NOT VERIFIABLE, and the claim
should be dropped in its current form.**

Duration is trivially measurable. **Single-take is not verifiable from any artifact.**
Metadata cannot demonstrate the absence of cuts, and the widely-repeated claim about Khan
Academy turns out to be a journalist's paraphrase rather than Khan's words: *"He never
writes a script… Khan also never edits. Either he nails the lecture in a single take or he
redoes the entire thing"* is Clive Thompson in *WIRED* (2011-07-15), not a quotation from
Khan. `UNVERIFIED`. The same applies to the Organic Chemistry Tutor and to Kozyrkov: the
single-take property is inferred from the look of the artifact, not established.

What Khan *does* say, verbatim, is about a different variable entirely — the absence of an
observer:

> *"That way, it doesn't seem like I'm up on a stage lecturing down at you. It's intimate,
> like we're both sitting at a table and we're working through something together."*
> *"The worst time to learn something is when someone is standing over your shoulder going,
> 'Do you get it?'"* (*WIRED*, 2011)

> *"Probably the least-appreciated aspect of this is the notion that the very first time
> that you're trying to get your brain around a new concept, the very last thing you need is
> another human being saying, 'Do you understand this?'"* (TED 2011)

And **another widely-repeated rationale turns out to be wrong.** The famous ten-minute video
length was not chosen for attention span. Khan Academy's own FAQ, in the first person
(Wayback, 2010-09-25):

> *"The content is made in digestible 10-20 minute chunks **especially purposed for viewing
> on the computer** as opposed to being a longer video of a conventional 'physical'
> lecture."*
> *"Because of the **granular nature** of the 10 minute videos, the content can be mapped to
> almost any state's or nation's standards."*

Computer-viewing fit and standards-mapping granularity. `HISTORICAL`. A format constraint
that has been rationalised for fifteen years as a cognitive finding was a distribution
decision. Canonical early Khan videos in fact run **5:50–11:32**, clustering at 6–8 minutes —
shorter than the shorthand.

### 5.3 The counterexample, and it is the biggest channel of the four

**The Organic Chemistry Tutor**: 10.8M subscribers, 3,106 videos, **1,762,799,135 total
views**, channel opened 2015-02-28. `OBSERVED`.

He does **none** of it. Across 23 videos fetched, **zero descriptions contain chapter
timestamps** and `DESCRIPTION_CHAPTERS` is 0 on every one — where markers exist at all they
are auto-generated. Descriptions open flatly (*"This algebra video tutorial explains how to
find the domain of a function…"*) with no problematising move. The structure is machinery
first, then a long queue of exercises: *"It contains mole to mole conversions, grams to grams
and mole to gram dimensional analysis problems"*; *"This video contains a ton of examples and
practice problems."* Instead of chapters he ships a numbered topic manifest with **no
times** — 42 items on one video, 40 on another. He runs very long (Algebra 2, 3h59m,
4,697,813 views; Introduction to Chemistry, 3h01m, 5,539,405 views).

**And this survey's own replay data shows the format signature.** His *Introduction to
Limits* (`YNstP0ESndU`, 20m19s, 6,715,294 views) has **the lowest first-decile replay mass in
the entire 51-video sample: 0.081**, against a sample mean of 0.291, with the peak at 71%
through. `OBSERVED (own harvest)`. Nobody replays the opening because there is nothing there
to replay; they navigate to the problem they need. That is a different artifact serving a
different job — **a reference work, not an explanation** — and it is the most-watched of the
four.

**Muller's own trial already ran this comparison and it is the cleanest result available:
Worked Examples grouped with the Exposition condition, not with the misconception
treatments.** The worked-problem format is on the *low*-gain side of a d = 0.79 gap. So the
largest channel in the class is, by the one relevant randomised trial, using the format that
loses — which is the whole point about popularity and learning being separable, demonstrated
inside a single study rather than argued by analogy.

### 5.4 The circularity, stated because it would otherwise look like convergence

There is a striking agreement between what the elite explainers say and what the trials
report: obstacle first, one sustained example, name the misconception, request a prediction.
Muller's refutation result (d = 0.79) and Sanderson's independently-stated rule land in the
same place.

**But Muller is Veritasium.** The strongest trial in this literature was run by one of the
four explainers being analysed, on the format he then went on to build a channel around. The
convergence between "what the best explainers do" and "what the evidence says" is *partly*
one person appearing on both sides of the ledger. `INFERENCE`.

That is not a reason to discount Muller — a practitioner who ran a randomised trial before
adopting a format is the best case in the sample, not the worst. It is a reason to **stop
counting creator agreement as independent corroboration.** Sanderson's SoME observation is
better evidence than his self-report precisely because it is about a corpus he did not make.

### 5.5 The measurable/stylistic split

| Feature | Measurable from artifact? | Trial evidence? |
|---|---|---|
| Position of first named machinery (% runtime) | **Yes** — chapter timestamps | Indirect (§29 §3.1; refutation d = 0.79) |
| Example density (seconds per example) | **Yes** — description + timestamps | Indirect (Muller: worked examples grouped with Exposition) |
| Misconception named explicitly | **Yes** — transcript predicate | **Direct: d = 0.79 / 0.83, N = 364** |
| Prediction requested before reveal | Partly — marker countable, compliance not | Productive failure g = 0.36–0.58 (§01) |
| Presence of authored chapter structure | **Yes** — `DESCRIPTION_CHAPTERS` | None |
| Duration | Yes | Swap g = 0.28 (§2.1); nothing on length |
| **Single-take / unedited** | **No** — not verifiable | None |
| Voice, animation quality, humour, "intimacy" | No | None |
| Being off-camera | Yes (trivially) | None |

The first three rows are what the atlas grades. The last four are style, and this section
takes no position on them beyond noting that they are where almost all of the public
discussion lives.

---

## §6 — `N4-D1`: the explanation atlas

`DESIGN`. **Brownfield flag: none.** There has never been a graded, outcome-linked census
of explanations, because the explanations were not public in one place and the grading
standard did not exist. Both changed. What follows is the counterpart to `N1-D1`'s error
atlas and the same class of asset: a public, versioned, shared scientific object rather
than a product feature.

**Anchor.** §29's four invariants and two failure modes (the grading standard); Schroeder &
Kucera 2022, g = 0.41 raw / **0.28 publication-bias adjusted**, k = 44, n = 3,869 (proof
that explanation *format* moves learning at all); Muller et al. 2008, N = 364, d = 0.79/0.83
(proof it moves it a lot when the manipulation is right); Bitzenbauer et al. 2023, N = 60
(proof that public metrics do not track quality); Noetel et al. 2021, swap **g = 0.28**
(the honest size of the video medium's own contribution).

### 6.1 The four steps

**Step 1 — Harvest.** Candidate explanations per concept, keyed to the same concept
vocabulary as `N1-D1`'s error atlas so the two objects join. Sources ordered by licence
cleanliness, not by fame (§7). Per candidate: transcript, structure (chapters, section
headings), duration, format class, and — where exposed — the replay heatmap, stored as a
localiser and explicitly **not** as a ranking input (§3.6).

**Step 2 — Grade mechanically.** §4.5's two-stage grader. **No learners are required for
this step**, which is what makes the atlas cheap enough to be comprehensive. Output per
explanation: a fidelity record (which invariants are respected, which are falsified, which
are unstated), an obstacle-before-machinery ordering verdict, a constant-labelling
completeness score, and a misconception-naming inventory. Every finding carries a timestamp
into the source so it is auditable.

**Step 3 — Measure delayed unassisted transfer on a subset. This is the part nobody has
done.** §1.3 establishes that exactly two studies in a 44-comparison meta-analysis exceeded
one month, that transfer was not coded at all, and that the multimedia literature tests
transfer immediately. So the measurement is genuinely absent rather than merely scattered.
The trial: same concept, 4–6 real published explanations as arms, random assignment,
**unassisted transfer at ≥ 21 days**, plus §22's 15–40-second dynamic-assessment probe at
entry so prior knowledge — the 3.6× lever from §30 — is measured rather than assumed. Two
design constraints inherited from this survey, both non-negotiable:

- **Probe on the obstacle, not the definition** (§29 §5). *"Why can't we just compute the
  probability directly?"* rather than *"what is an energy-based model?"*
- **Collect the felt-learning rating too, and expect it to diverge.** §01's Deslauriers
  result — students in the condition that taught them more reported learning less — and
  §30's Whillier & Lystad (worse grades at **P = 0.001**, higher satisfaction) both predict
  the divergence. If the trial does *not* find preference and outcome dissociating, that is
  itself a surprise worth reporting.

**Step 4 — Learn what predicts transfer from the checkable features.** Regress the delayed
transfer outcome on the Step-2 mechanical features. **This is the compounding step**: once
graded features predict outcome, selection and eventually generation no longer require a
trial per explanation. Steps 1, 2 and 4 scale at ~zero marginal cost. Step 3 is the only
part that costs money, and its cost falls as Step 4's model improves, because you only need
to run trials where the model is uncertain.

### 6.2 Inputs, outputs, and what joins to what

**Inputs.** Concept vocabulary shared with `N1-D1`; licence-clean transcripts (§7);
§29's predicate set; one instrumented cohort for Step 3.

**Outputs.** Per concept: a ranked list of explanations with fidelity records, the specific
invariant each one falsifies if any, the obstacle each one leads with, the misconceptions
each one names, and — for the subset that has been through Step 3 — a measured delayed
transfer estimate with its interval. Published openly, versioned, with a changelog.

**The join to `N1-D1` is the reason both are worth more than either.** The error atlas says
*which wrong models a population actually occupies for this concept*. The explanation atlas
says *which explanations name and displace which wrong models*. Together they answer a
question neither can answer alone: **given that this learner holds this specific wrong
model, which published explanation has been measured to displace it?** Muller's refutation
result (d = 0.79) is precisely the claim that this pairing is the active ingredient. Neither
atlas contains that claim; the pair does.

### 6.3 Failure modes

- **The felt-learning trap re-entering through the harvest.** If Step 1's candidate set is
  assembled by view count, the atlas grades a popularity-selected sample and will report
  that popular explanations are good. Mitigation: harvest by concept coverage and licence,
  and **record the view count as a covariate to be controlled, never as an inclusion
  criterion.** §3.3(c) shows this bites even for the replay heatmap, whose coverage is
  popularity-gated at roughly 54,000 views.
- **Extraction error is the whole error budget.** §4.5. Inherits §13's 36% end-to-end
  ceiling as a warning.
- **Explanations are not independent of the learner.** The expertise reversal effect
  (Kalyuga et al. 2003, DOI `10.1207/s15326985ep3801_4`, 1,336 citations — **a review, not
  a meta-analysis; no pooled effect size exists**) and §29 §6's **d = −0.428 for experts**
  both say the best explanation is conditional on prior knowledge. A single ranking per
  concept is therefore wrong on its face; the atlas must be indexed by *(concept, learner
  state)*, which multiplies the Step-3 trial cost by the number of states.
- **Rating drift.** If the predicate set is revised faster than the transfer estimates
  accumulate, no entry is ever stable — the same failure `N1-D1` names for misconception
  vocabulary.
- **Wittwer & Renkl's null (§1.6) as a ceiling.** Instructional explanation is a weak
  intervention *per se*. The atlas is an input to a loop that ends in the learner producing
  and being verified, not a delivery product. Build it as the former or it will underperform
  its own anchors.

### 6.4 What would show it was the wrong design

> **If mechanically graded features do not predict delayed unassisted transfer, the atlas
> is a taste ranking with extra steps.**

Made operational, so it can actually fail:

1. **The primary falsifier.** Step 4's regression of delayed transfer on Step-2 features
   fails to beat a baseline of *(video length + view count + a fluency rating)* by a
   pre-registered margin. If §29's invariants carry no more information than a popularity
   metric and a vibes score, the grading standard is decorative.
2. **The prerequisite falsifier**, and it is cheaper and comes first: **§4.5's grader fails
   to clear 80% precision at 60% recall.** If the features cannot be extracted reliably,
   step 1 of the primary test cannot even be run. **Run this before anything else.**
3. **The scope falsifier.** If the ranking of explanations for a concept reorders
   substantially between two learner-state strata, there is no atlas — there are
   per-population atlases, and the shared-object economics collapse. This is the exact
   falsifier `N1-D1` carries for misconception prevalence, and it should be tested the same
   way, on the same cohorts, at the same time.

### 6.5 The cheapest version that is still worth building

Because Step 3 is the only expensive part, there is a real version at a fraction of the
cost: **grade mechanically, publish the fidelity records, run no trial, and claim nothing
about learning.** That object is honest, immediately useful (an author can check their own
explanation against §29 before publishing), and it is the substrate Step 3 later attaches
to. It must be labelled for what it is — **a fidelity audit, not a quality ranking** — or
it becomes exactly the taste ranking its own falsifier warns about.

---

## §7 — Rights, and the honest constraint

This decides whether the design is buildable, so it is treated at length rather than
waved at. The finding that reorganises it:

> **Every US decision in 2025 held the *analysis* lawful and the *acquisition* unlawful.
> The binding constraint on the explanation atlas is contract, not copyright.**

You can win the fair-use argument completely and still lose, because the ways of getting
the text are foreclosed by terms of service, and terms of service are a separate cause of
action that fair use does not answer.

### 7.1 The copyright doctrine is favourable, and it is not the problem

`HISTORICAL` / case law, retrieved 2026-07-29.

- **Authors Guild v. HathiTrust**, 755 F.3d 87 (2d Cir. 2014): *"the creation of a full-text
  searchable database is a quintessentially transformative use."* And on the argument a
  creator would make against the atlas: *"Lost licensing revenue counts under Factor Four
  only when the use serves as a substitute for the original, and the full-text-search use
  does not."*
- **Authors Guild v. Google**, 804 F.3d 202 (2d Cir. 2015): Google Books was fair use
  because it *"augments public knowledge by making available information about Plaintiffs'
  books without providing the public with a substantial substitute."* The operative design
  constraints are quantitative and worth copying directly: the blacklisting *"permanently
  blocks about 22% of a book's text from snippet view"*, and *"in no case were they able to
  access as much as 16% of the text."*
- **Bartz v. Anthropic**, No. C 24-05417 WHA (N.D. Cal., June 23, 2025), Alsup J.: training
  was *"transformative — spectacularly so"*, and *"such a market for that use is not one the
  Copyright Act entitles Authors to exploit."* **And**: *"Anthropic had no entitlement to use
  pirated copies for its central library. Creating a permanent, general-purpose library was
  not itself a fair use excusing Anthropic's piracy."* Settled; **final approval 2026-07-20**,
  **$1.5 billion**, non-reversionary, roughly **$3,000 per work**.

**Read the two halves of Bartz together.** Anthropic won every fair-use question about what
it did with the files and paid $1.5 billion for how it got them. That is the exact risk
profile of a transcript pipeline built with `yt-dlp`.

**And one case cuts directly against this section's design.** **Thomson Reuters v. Ross
Intelligence**, 765 F. Supp. 3d 382 (D. Del., Feb. 2025), Bibas J.: *"Ross's use is not
transformative because it does not have a 'further purpose or different character'… Ross was
using Thomson Reuters's headnotes as AI data to create a legal research tool to compete with
Westlaw. It is undisputed that Ross's AI is not generative AI."* And the sentence that names
the atlas's exposure: *"it does not matter whether Thomson Reuters has used the data to
train its own legal search tools; the effect on a potential market for AI training data is
enough."* Bibas expressly limited the ruling — *"only non-generative AI is before me
today"* — and it is on interlocutory appeal (3d Cir. No. 25-2153, briefed, **undecided**).

> **`OPEN` — is the explanation atlas Bartz or Ross?** An atlas that *retrieves and ranks
> existing explanations* looks like Ross: non-generative, same purpose as the original,
> competing for the same attention. An atlas whose graded features are used to *generate new
> explanations* looks like Bartz: transformative, producing something the source did not.
> **This is a design choice with a legal consequence and it should be made deliberately, not
> discovered later.** §6.5's cheapest version — a published fidelity audit with snippet-level
> quotation, linking rather than reproducing — sits on the HathiTrust/Google Books side of
> the line and is the safest thing to build first. *Why nobody asked:* the question only
> arises for an artifact that grades third-party explanations at scale, and nobody has built
> one.

### 7.2 The contract forecloses the acquisition, and this is where it dies

`MEASURED-BENCH`, quoted from the live documents.

**YouTube Terms of Service** (effective 2023-12-15) grants a viewer *"personal,
non-commercial use"* and the embeddable player, and prohibits: *"access, reproduce,
download… any part of the Service or any Content except… as expressly authorized"*, and
*"access the Service using any automated means (such as robots, botnets or scrapers)."*
The clause that ends the argument about what a public video licenses you to do:

> *"You also grant each other user of the Service a worldwide, non-exclusive, royalty-free
> license to access your Content through the Service… **only as enabled by a feature of the
> Service**… **For clarity, this license does not grant any rights or permissions for a user
> to make use of your Content independent of the Service.**"*

**`robots.txt`** disallows `/get_video`, `/get_video_info`, `/timedtext_video`, `/youtubei/`,
`/results` — which is to say, precisely the endpoints every transcript tool calls, including
the search-results endpoint this survey used in §3.

**Developer Policies** (updated 2026-06-24): III.E.2 bans downloading, caching or storing
copies of audiovisual content; III.E.6 bans scraping **"or obtain[ing] scraped YouTube data
or content"** — a clause that reaches downstream users of somebody else's scrape; III.I bans
using *"any technology other than YouTube API Services to access or retrieve API Data."*

**And there is no compliant path to a third party's transcript.** `captions.download`
states: *"This method requires the user to have permission to edit the video."*
`captions.list` will enumerate someone else's caption tracks and will not give you the text.

This survey's own §4.1 measurement is the technical face of that policy: **the unauthenticated
`timedtext` endpoint returns HTTP 200 with a zero-byte body**, across four format parameters,
verified 2026-07-29. The door is not merely locked contractually; it has been closed.

**A note on honesty about the ecosystem.** `youtube-transcript-api` and `yt-dlp` exist, are
widely used, and violate four separate prohibitions simultaneously (automated access;
download; III.I non-API access; robots.txt). `youtube-transcript-api`'s own README warns it
*"uses an undocumented part of the YouTube API."* YouTube's CEO has said it on the record:
*"It does not allow for things like transcripts or video bits to be downloaded, and that is
a clear violation of our terms of service."* **"Everyone does it" is a risk statement, not a
permission**, and this section will not pretend otherwise.

**The 30-day rule breaks the atlas as an artifact even where access is legitimate.**
Developer Policies III.E.4.c–d cap storage of API data at **30 calendar days**, after which
it must be deleted or refreshed. An atlas is a *versioned, durable, citable public object*
(§6). A 30-day-refresh corpus is a cache. The **derived-metrics amendment** (added 2026-05-04,
clarified 2026-06-01) lets audited developers store derived metrics for **36 months** — but
explicitly: *"Other data (such as video titles, creator names, descriptions, and comment
text) must still follow the 30-day refresh and deletion policy"*, and it does not cover
transcripts or audiovisual content at all. It is worth applying for; it does not solve this.

### 7.3 The live litigation risk, which is new and specific

**Ted Entertainment, Inc. v. Nvidia / OpenAI / Apple** (N.D. Cal., 5:25-cv-10287-EJD filed
2025-11-26; 3:26-cv-02935 and 3:26-cv-02936 filed 2026-04-03). Plaintiffs are YouTube
creators, including a golf *instructional* channel. **The sole cause of action is DMCA
§1201(a) anti-circumvention, not copyright infringement**, and the pleading explains exactly
why:

> *"Most YouTube videos are not registered with the U.S. Copyright Office. That lack of
> registration, however, does not render them valueless or leave them unprotected… Because
> copyright registration is not a prerequisite for protection against unlawful
> circumvention of access controls…"*

This theory routes around everything that sank the earlier **Millette v. OpenAI/Google/Nvidia**
wave (state-law claims dismissed with prejudice 2025-03-24; the Google and Nvidia actions
voluntarily dismissed). No registration is required. **Fair use is not a defence to §1201**,
because §1201 governs *access*, not *use*. And it converts YouTube's own terms of service
into something a *creator* can enforce.

**Nvidia's motion to dismiss is set for hearing 2026-08-27 — four weeks from this survey's
date, and undecided.** `OBSERVED`. If it survives, scraping YouTube becomes independently
actionable by any creator whose video was touched, with no fair-use answer available. **This
is the single largest legal risk to the design and it will be resolved, one way or the other,
within a month.** Anything built before then is built on an open question.

### 7.4 What the named channels actually permit

`MEASURED-BENCH`, from the licence documents themselves.

| Source | Licence | Covers the video? | Commercial use |
|---|---|---|---|
| **MIT OpenCourseWare** | CC BY-NC-SA 4.0 | **Yes — whole corpus, transcripts included** | **No** |
| **Khan Academy** | CC BY-NC-SA **3.0 US** (opt-in per item) | Yes | **No** |
| Khan Academy CS module code | MIT | n/a | Yes |
| **3Blue1Brown — `manim`** | MIT | n/a (library) | Yes |
| **3Blue1Brown — `videos` repo** | CC BY-NC-SA 4.0 | **No — scene source code only** | No |
| **3Blue1Brown — the actual videos** | All rights reserved | — | **No** |
| **Veritasium** | None (© Electrify US LLC) | — | **No** |
| **Cassie Kozyrkov** | None ("All rights reserved") | — | **No** |

Details that matter operationally:

- **MIT OCW is the one clean corpus, and it is why §4 used it.** Transcripts are published as
  PDFs directly on `ocw.mit.edu`, no scraping required, no API involved, licence stated on
  the page. MIT's own gloss is useful: *"Determination of commercial vs. non-commercial
  purpose is based on the use, not the user"* — a corporation may use OCW materials for
  internal training. But: *"Commercialization is prohibited… A commercial education or
  training business may not offer courses based on OCW materials if students pay a fee."*
  **A trap worth flagging: OCW's YouTube uploads carry the Standard YouTube Licence** — the
  CC grant lives in the description text — so a `videoLicense=creativeCommon` API filter will
  not find them.
- **Khan Academy's §7.4 is stricter than CC-NC's own definition**, expressly banning *"the
  sale or rental of… any derivative works based at least in part on the Licensed Educational
  Content."* Their help centre adds that advertisements on a website count as commercial.
- **3Blue1Brown permits under 60 seconds with on-screen attribution** and requires a
  licensing enquiry for anything more, including *"uploading full lessons to an alternate
  educational platform."* The CC BY-NC-SA on the GitHub repo is for the Python that renders
  the animations, not for the videos. This is a common and consequential misreading.
- **YouTube's own CC option offers only CC BY** — no NC, SA or ND variants — so the API's
  `videoLicense=creativeCommon` flag is a **floor, not a ceiling**: its absence tells you
  nothing.

> **Null result: no reliable count of CC-BY videos on YouTube exists.** Creative Commons'
> *State of the Commons* does not report one; YouTube's old announcement 404s and is not in
> the Wayback Machine; `search.list` caps at ~500 results so the corpus cannot be enumerated
> either. Any circulating figure is unsourced. `UNVERIFIED`.

**The bind, stated plainly.** The clean corpus (MIT OCW, Khan) is non-commercial. The
commercially clean corpus (arbitrary CC-BY uploads) is unvetted and does not contain any of
the explainers the proposal is actually about. And the explainers the proposal *is* about —
Kozyrkov, Veritasium, 3Blue1Brown — are all rights reserved, with no licence and, in two
cases, no stated reuse policy at all.

### 7.5 What a creator would want, and what has actually been paid

**YouTube built the permission rail and explicitly declined to build the payment rail.** The
third-party AI training setting is **off by default**; training permission status is exposed
per video ID; companies *"can apply to join the list"*. And then:

> *"YouTube isn't facilitating payments between third-party companies and creators or other
> rights holders at this time."*

`MEASURED-BENCH`. That sentence is the entire commercial gap. Consent is brokered;
compensation is not.

**The documented complaints are from educational creators, and one of them is in this
section's own data.** Proof News (2024-07-16) established that EleutherAI's "YouTube
Subtitles" dataset — **173,536 videos from 48,000+ channels, plain-text subtitles only,
5.7 GB, 489 million words** — was used by Anthropic, Nvidia, Apple and Salesforce, and
*"contains video transcripts from educational and online learning channels like Khan Academy,
MIT, and Harvard."* The named objectors:

- **Julie Walsh Smith, CEO of Complexly** (Crash Course, SciShow): *"We are frustrated to
  learn that our thoughtfully produced educational content has been used in this way without
  our consent."*
- **Dave Farina, "Professor Dave Explains"**: *"If you're profiting off of work that I've
  done [to build a product] that will put me out of work or people like me out of work, then
  there needs to be a conversation on the table about compensation or some kind of
  regulation."*
- **David Pakman**: *"No one came to me and said, 'We would like to use this.'"*
- Proof News: *"Of the creators we spoke to, none were aware their information had been
  taken."*

Note the coincidence and take it seriously: **"Professor Dave Explains" is one of the 51
videos in this section's own §3 harvest** — his eigenvalue video, 1,362,273 views, appears in
the peak-clustering table. The person whose explanation this survey measured is on the record
objecting to exactly the class of use this section is designing. That is not a reason not to
build it. It is a reason the design must have an answer for him, and §7.6 is that answer.

**The compensation anchors, from SEC filings rather than press:**

| Benchmark | Figure |
|---|---|
| Coursera content cost, consumer | **38.6%** of revenue (2025); 40.3% (2024) |
| Coursera content cost, enterprise | **30.3%** (2025); 31.4% (2024) |
| Udemy instructor share, subscription | 20% (2024) → 17.5% (2025) → **15% (2026)** |
| Reddit AI data licensing | **$203.0M aggregate contract value**, 2–3 year terms (S-1); "other revenue" $15.2M → $114.7M → **$140.0M** |
| Shutterstock data/distribution revenue | $137.3M → $175.3M → **$203.3M**, contributors paid per licence on a tiered schedule |

`OBSERVED` (SEC filings). **Educational platforms pay creators roughly 15–40% of
attributable revenue and the trend is sharply downward** — Coursera has moved to
engagement-based allocation and introduced a platform fee, noting it *"experienced opposition
to our content fee terms"*; Udemy's absolute instructor payouts fell ~$22.8M year over year
while gross margin rose from 63% to 66%. Anyone designing a creator deal should know that the
existing market is contracting, not expanding.

Do **not** cite: the 2U/edX 60/40 split (in no 10-K; press folklore), Skillshare's royalty
pool (sources conflict), or the Reddit–Google $60M/yr and News Corp–OpenAI $250M/5yr figures
(single-source, "people familiar"). `UNVERIFIED`.

**Shutterstock is the structurally correct model** and the only one in the set that pays
contributors specifically for machine-learning use: content *"is also made available for
delivery to our data offering partners for machine learning purposes"*, with contributors
earning a royalty on a tiered schedule. It is a marketplace where the creator opts in, is
identified, and is paid per use. That is the shape of the thing that does not exist for
educational video.

### 7.6 What is actually buildable, in order

`DESIGN`. The architecture the constraints leave standing:

1. **Grade the licence-clean corpus first, and say so.** MIT OCW (CC BY-NC-SA, full
   transcripts, no scraping) and Khan Academy. This is enough to run §6.4's falsifiers,
   which is what matters — you do not need Veritasium to find out whether §29's predicates
   predict transfer. **§4's prototype already ran on exactly this corpus, without violating
   anything.** The research question is fully answerable inside the permissible set.
2. **Publish as a fidelity audit with links and snippets, not reproductions.** Copy Google
   Books' quantitative discipline: hard-cap the fraction of any source reproduced, embed
   rather than host, keep YouTube's attribution intact where the player is used. This sits
   on the transformative side of HathiTrust and away from Ross.
3. **Take the EU Article 3 route seriously if this is research.** DSM Art. 3 covers research
   organisations doing scientific research, has **no opt-out**, and permits copies to be
   *"retained for the purposes of scientific research, including for the verification of
   research results"* — i.e. exactly the durable versioned corpus a 30-day API rule forbids.
   Art. 4 (the general commercial exception) is almost certainly unavailable, because
   Recital 18 counts *"terms and conditions of a website or a service"* as a valid
   reservation and YouTube's ToS plus robots.txt are a textbook one. The UK's s.29A
   similarly covers non-commercial research only — but note s.29A(5): *"To the extent that a
   term of a contract purports to prevent or restrict the making of a copy [under this
   section], that term is unenforceable."* **Within its scope, UK research use beats the
   YouTube ToS.** That is a real and underused asymmetry.
4. **Ask, per creator, with something specific to offer.** Not "may we use your video."
   Rather: *here is a fidelity audit of your explanation against a published standard, here
   is the replay-density localiser for it, here is where your explanation was measured to
   produce transfer and where it was not, you keep it, and the atlas links to you rather
   than replacing you.* The measured transfer estimate is a thing no creator can currently
   obtain at any price, and it is the only chip on the table that is not money. Whether it is
   enough is unknown.
5. **Apply for the audited derived-metrics status** for the metadata layer (36-month
   retention on derived metrics) and **apply to YouTube's third-party training list**, which
   is the only sanctioned route to creator-consented YouTube training data.

> **What would show this was the wrong approach.** If the licence-clean corpus (MIT OCW plus
> Khan) proves too narrow to contain **two or more genuinely different explanations of the
> same concept** across enough concepts to run §6.4's tests, then the falsifier cannot be
> evaluated inside the permissible set, and the whole design becomes contingent on licences
> nobody has granted. **This is checkable in an afternoon** by counting concept overlap
> between OCW courses and the Khan library, and it should be checked before anything else in
> §7 is acted on.
>
> **A partial check, already done, is encouraging.** For *eigenvectors and eigenvalues* alone,
> the licence-clean set already contains at least four distinct explanations: MIT OCW 18.06
> Lecture 21 (Strang, ~51 min, transcript published as PDF), OCW 18.06 Lecture 22
> (diagonalisation and powers), and two Khan Academy treatments (`PhfbEr2btGQ`, 7m42s,
> 1,335,271 views; `3Md5KCCQX-0`, 15m34s, 612,864 views) — differing sharply in length,
> formalism, and order of presentation. `OBSERVED (own harvest, 2026-07-29)`. One concept is
> not a corpus, but it establishes that the permissible set is not degenerate.

---

## §8 — "Zero to hero in a few hours", tested

### 8.1 The worked example, verified

`OBSERVED (own harvest, 2026-07-29)`, from video page metadata. The owner's two figures
check out exactly:

| Video | Duration | Views | Likes | Replay heatmap? |
|---|---|---|---|---|
| MFML Part 1 — *Introduction to ML and AI* (`lYWt-aCnE2U`) | 5,260 s = **1h 27m 40s** | **211,453** | 3,770 | Yes |
| MFML Part 2 — *Life of an AI project* (`lIFLeHDanmA`) | 5,005 s = **1h 23m 25s** | **65,603** | 966 | Yes |
| MFML Part 3 — *Taking AI from prototype to production* (`fwK5xKUwQbw`) | 7,246 s = **2h 00m 46s** | **47,699** | — | **No** |

**Total series: 17,511 s = 4 hours 52 minutes.** "A few hours" is literally accurate.

**And the series funnel is the most informative number on the page.** 211,453 → 65,603 →
47,699 is **31.0%** and **22.6%** of Part 1. `OBSERVED`. This is a behavioural measure, not
an attitudinal one, and it is the one thing on the page that is not on the felt axis: it
says that **roughly three-quarters of the people who started the course did not reach the
end of it.** That is a completion figure in the normal MOOC range, and it is a fact about
the *series*, not about Kozyrkov — the same shape appears in every multi-part course ever
measured. Note the corollary for the proposal: a curation plan that assumes learners consume
a five-hour series end-to-end is planning against the behaviour of the top quartile.

Restating the standing rule: **none of these numbers is evidence about learning.** 211,453
views establishes that a great many people found it worth starting.

### 8.2 The compression arithmetic

§30 establishes the bounds, and they are not one number:

| Resource | Compression |
|---|---|
| Elapsed calendar time | **10–40×** (once ~300×, Sherlock) |
| Engaged effort | **3–5×** |
| Durability / retention | **1×** |
| Procedural and production skill | **1×** |

Applied to a 4h52m video series:

**What it can plausibly deliver.** At 3–5× on engaged effort, five focused hours of a
high-density, well-ordered explanation is a defensible substitute for **15–25 hours of
engaged study** — comfortably a week's or two weeks' *understanding* of a field's
orientation layer. §30 identifies orientation as the part that compresses most completely,
because it is retrieval, structuring and diagnosis, none of which require the learner's own
working memory: *"what limits polymathy is not how many fields you can learn. It is how
many times you can afford to be a beginner."* A great explainer series is an
orientation-compression device, and orientation is exactly what the 3.6× prior-knowledge
lever is made of.

**What it cannot deliver, and the reasons are measured, not rhetorical.**

- **Durability is 1×.** A memory durable for a year needs retrieval gaps of **18–36 days**
  (§30 §6). There is no version where you finish on Tuesday. Watching five hours on Tuesday
  produces something that will be substantially gone by August.
- **Procedural fluency is 1×.** The Foreign Service Institute has spent seventy years
  removing every compressible element from language training and still needs **552–2,200
  hours** (§30 §5). Nothing in a video shortens the repetitions of the productive act.
- **Watching is not attempting, and this one is a measured harm rather than a mere absence.**
  §01/§30: unguarded assistance leaves learners **17% worse on later unassisted work**,
  while practice scores rise **+48%**. §30 states the principle exactly: *"compression
  achieved by watching someone else solve it is not compression; it is substitution."* A
  brilliant explanation is the most efficient possible delivery of watching-someone-else.
  It is on the wrong side of that line by construction.
- **Time does not predict learning; opportunities do.** Koedinger et al. (PNAS 2023), 1.3
  million observations, 27 datasets: *"A time-based model, time-AFM, systematically provides
  poor predictive fit"* (§30 §2). "Five hours of video" is a time quantity. It is the
  category of thing measured not to predict the outcome.
- **And the intensive-format nulls point straight at this format.** Seamon (2004): the
  intensive-format advantage is real immediately and **gone at three years.** Whillier &
  Lystad: the same contact hours compressed produced significantly **worse** grades
  (**P = 0.001**) — **and higher satisfaction.** §30. The felt-learning trap arrives exactly
  where a compression claim is most tempting to believe, which is here.

### 8.3 The honest claim, and what must be bolted on

> **A great explainer series delivers a week's orientation in an evening. It delivers
> approximately none of the retention and none of the skill. It is the cheapest known way
> to buy the 3.6× prior-knowledge lever, and it is not a course.**

What must be bolted on, in order of measured effect size, all from §01 and §30:

1. **Retrieval practice** — g = 0.499 [0.442, 0.557], 222 studies, 48,478 students. The
   video is the encoding event; without retrieval there is no durability at any price.
2. **Spacing on an 18–36-day gap** — classroom d = 0.54. §30's Rohrer & Taylor result is
   the key economic fact: the four-week benefit came from **the same ten problems, merely
   split** across sessions. **Same total effort, same items, different calendar.**
   Durability is nearly free; it is only slow.
3. **Explaining it back, with the expectancy set first** — g = 0.48 with, **g = −0.02**
   without (§05). Ordering matters and is free.
4. **Unassisted attempts with the answer withheld** — the guardrail that turns +48%
   practice with −17% exam into +127% practice with a null exam coefficient (§01).
5. **Entry diagnosis** — 15–40 seconds, r = 0.66–0.92 against full diagnostics (§22). The
   whole value of a curated explanation is that it is aimed at the right rung; §29 §5 says
   probe on the obstacle, not the definition.

Item 2 is the one that makes the proposal's economics work rather than break: **the
expensive resource is calendar patience, not effort.** A curation plan that hands someone
five hours of the best explanations in the world and nothing else has bought the cheapest
component and skipped the four that compound.

---

## §9 — The nulls ledger

Collected because the brief asked for at least three and this section found substantially
more, and because the negative results are load-bearing rather than decorative.

**From this survey's own measurements:**

1. **The replay heatmap is nearly flat.** Median normalised entropy **0.976** (1.0 =
   uniform) across n = 51; top decile of buckets holds 19.5% of mass against 10% under
   uniformity — **1.95× enrichment**. The hypothesised comprehension-failure detector is a
   faint tilt. `OBSERVED (own harvest)`.
2. **Replay peaks do not track the concept.** Mean within-concept SD of peak position
   **20.7 pp** against a total SD of **22.6 pp** and a uniform-distribution SD of 26.0 pp,
   over 49 videos across 6 concepts. Concept identity explains ~16% of variance.
   `OBSERVED (own harvest)`.
3. **Replay peaks are contaminated by the chapter UI.** Peak-to-nearest-chapter distance
   **49.8 s** against a Monte-Carlo null of **87.6 s**; 7 of 10 videos closer than chance.
   `OBSERVED (own harvest)`.
4. **§29's flagship predicate has zero recall on spoken mathematics.** The quantifier-prefix
   check fired **0 times in 1,524 sentences** of graduate linear algebra, because speech
   elides quantifiers rather than reordering them, and elision is not detectable as
   falsification. `OBSERVED (own harvest)`.
5. **Lexical fidelity grading has 23% precision** (7 true positives from 30 flags), with
   P4 at **0/14** and P3 at **0/5**. Surface-string grading of §29's invariants does not
   work. `OBSERVED (own harvest)`.
6. **YouTube caption endpoints return empty for unauthenticated requests.** HTTP **200 with
   0 bytes** across four format parameters, verified 2026-07-29. `OBSERVED (own harvest)`.

**From the literature:**

7. **Views and likes do not indicate explaining quality.** Bitzenbauer et al. 2023, N = 60
   real YouTube videos graded against a rubric — surface features *"do not seem to be
   suitable indicators."* `MEASURED-BENCH`. The direct measurement of this section's
   central collision.
8. **Four presentation formats, 3 weeks and 9 months, no difference.** van Peppen,
   Verkoeijen, Heijltjes, Janssen & van Gog (2021), "Enhancing students' critical thinking
   skills: is comparing correct and erroneous examples beneficial?", *Instructional Science*,
   DOI `10.1007/s11251-021-09559-0`, **N = 170**, four conditions (correct + erroneous
   examples / correct only / erroneous only / practice problems), pretest, immediate
   posttest, **3-week and 9-month delayed posttest**: *"no differences in learning gains or
   transfer performance between the four conditions."* `MEASURED-RCT`. The domain is
   critical-thinking/reasoning-bias tasks rather than conceptual explanation, so it is not a
   direct test of this section's premise — but it is **the longest-delay head-to-head
   format comparison located anywhere in this literature, and it found nothing.** Read it as
   the prior an atlas has to beat.
9. **Instructional explanations are minimal per se.** Wittwer & Renkl (2010), *EPR*, k = 21:
   *"benefits… are minimal"*, and not necessarily better than self-explaining.
   `MEASURED-META`.
10. **Instructional explanations can actively reduce learning.** Schworm & Renkl (2006),
    *Computers & Education*, DOI `10.1016/j.compedu.2004.08.011`, N = 80: instructional
    explanations **reduced self-explanation activity and thereby reduced learning
    outcomes.** A reversal, not a null. `MEASURED-RCT`.
11. **Presentation mode does not matter, only time does.** Hefter, ten Hagen, Krense et al.
    (2019), *J. Educational Psychology*, N₁ = 57, N₂ = 43: **video versus written versus
    graphic-novel worked examples of the same content** produced *"similar learning
    processes… as well as a large effect on learning outcomes"* regardless of mode. Formats
    differed in **efficiency**, not effectiveness. `MEASURED-RCT`. Directly relevant: it
    says the *video-ness* of a great video explainer is not where the value is.
12. **Refutation advantage absent in two well-powered replications.** Mason, Zaccoletti &
    Carretti (2019), *IJSME*, N = 85: students improved *"regardless of text read"*; Mason,
    Borella & Diakidoy (2020), *Discourse Processes*, N = 110: same. `MEASURED-RCT`.
13. **Immediate structure effects vanish at two weeks.** Troyer (1992), ERIC, N = 71:
    collection beat comparison at immediate posttest; *"no significant differences among the
    groups at the delayed posttest."* `UNVERIFIED` (ERIC, no DOI).
14. **No meta-analysis of the expertise reversal effect exists.** The canonical source
    (Kalyuga et al. 2003, DOI `10.1207/s15326985ep3801_4`, 1,336 citations) is a narrative
    review with no pooled effect size; the nearest quantitative synthesis is Whitener (1989),
    *RER*, **k = 9**, which predates the term. A 1,336-citation effect with no pooled
    estimate.
15. **The Data API exposes nothing behavioural.** Five statistics properties, two
    deprecated, none relating to retention, watch time, replay or rewind.
    `MEASURED-BENCH`.

### 9.1 Numbers deliberately not quoted

Retrieved as citations but with values unobtainable behind paywalls, listed so nobody
back-fills them from memory: **Danielson et al. (2024)** overall g; **Wittwer & Renkl
(2010)** numeric d/g and its conceptual-versus-procedural moderators; **Sundararajan &
Adesope (2020)** seductive-details g; **Rey (2012)** retention/transfer values;
**Rey, Beege & Nebel (2019)** segmenting values; **Noetel et al. (2022)** per-principle
table.

---

## §10 — What this section commits us to

- **Never carry a platform metric forward as evidence of teaching.** Views, likes,
  subscribers, retention: `OBSERVED`, felt axis, and directly measured not to track
  explaining quality (Bitzenbauer 2023, N = 60). Say it every time, because the failure mode
  is silent.
- **Quote the swap, not the add.** Video's honest meta-analytic effect is **g = 0.28**
  (swap), not g = 0.80 (add), and the difference is that one of them is a dose effect.
- **Quote refutation text at g = 0.28 adjusted, not g = 0.41 raw**, and say which.
- **Treat the replay heatmap as a localiser, never a ranker.** It is min–max normalised
  within each video in 51 of 51 cases, which makes cross-video comparison impossible by
  construction, and it is chapter-confounded and popularity-gated besides.
- **Run the grader falsifier before building the atlas.** Three transcripts, one day, and
  it decides whether §6 is a real design or a taste ranking. The lexical prototype missed
  the bar by a factor of three, which is informative rather than fatal — but only if the
  two-stage version is actually tested rather than assumed.
- **Index explanations by learner state, not by concept alone.** Kalyuga's reversal and
  §29's **d = −0.428 for experts** both say a single ranking per concept is wrong on its
  face.
- **Claim orientation, not durability, and never procedural fluency.** A five-hour series
  buys a week's understanding at 3–5× on engaged effort and **1× on everything that lasts**.
- **Bolt on retrieval, spacing, teach-back and withheld answers, or do not ship it.** The
  explanation is the cheapest component and the only one that does not compound.

The sentence to keep: **the best explanations in the world are already public, already
free, and have never once been measured against the only outcome that matters.**
