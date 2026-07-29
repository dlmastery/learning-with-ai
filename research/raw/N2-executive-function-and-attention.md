---
title: "Executive Function and Attention — what actually grabs a learner, what actually holds them, and the resource every product requires and never supplies"
wave: N
section: N2
date_researched: 2026-07-29
sources_count: 96
status: raw-research
---

# N2 — Executive Function and Attention

> **The claim under test**, in the project owner's words:
>
> *"The best teachers in the world always grab attention — play jokes, have a strong attractive
> story for each section. The best narrators also ask the right questions to sustain interest and
> keep focus. With so much stuff available, students need motivation and a rapid zero-to-hero plan
> with clear memory retention and intuition forming — not super-slow classes."*
>
> **The finding, stated first.** Three of these four instincts survive contact with the measured
> literature, and each survives *for a different reason than the one implied*.
>
> 1. **The joke.** Transience is **not** the operative variable — the corpus's own hinge is
>    weaker than it looks. The operative variable is **referential status**: whether an element
>    has a referent inside the target schema. An element that points at the target helps
>    (signalling **g = 0.43**); an element that *is* the target, dressed, helps (emotional design
>    **g ≈ 0.27–0.39**); an element merely adjacent to the target does nothing (decorative
>    animation **g = −0.05**); an element carrying its own competing referent harms
>    (**g = −0.16 to −0.43**). The great teacher's joke is *about the thing*. That is the whole
>    mechanism, and it is not a joke mechanism.
> 2. **The story.** A story is a vehicle when it supplies the referent for a mapping the learner
>    must make, and a competitor when it supplies a referent the learner does not need. These are
>    routinely elided because both are called "story." Only **28%** of the effect sizes in the
>    narrative-superiority meta-analysis come from studies that controlled content across genres.
> 3. **The question.** Right, and for the wrong reason. Prequestions work at **g = 0.54** on
>    exactly what they ask about and **g = 0.04** on everything else. The work is done by the
>    *attempt* (guessing **g = 0.65** vs not-guessing **g = 0.22**), not by the felt curiosity —
>    and the effect is **g = 0.62** in adults but **g = 0.22** in grade-school children.
> 4. **"Not super-slow classes."** Right about the class, wrong if it means handing the pace to
>    the learner. Design principles are worth **g = 0.41 system-paced** and **g = 0.27
>    learner-paced**; instructor-segmented content beats learner-segmented **0.41 vs 0.20**; and
>    segmented content **takes longer** (g = 0.92) while teaching better.
>
> **And the reframe the section exists for.** Executive function is not only a learner trait to
> accommodate. It is a **resource every learning product silently requires and never supplies**.
> Twenty-five years before the Khanmigo null, the Cognitive Tutor log data measured the exact
> failure: after **three consecutive errors on a step**, a student's next action was a hint
> request only **34%** of the time; students clicked through **68%** of hint levels in under a
> second to mine the answer. And when Carnegie Mellon built a tutor that fixed the help-seeking
> behaviour — successfully, durably, months after removal — **domain learning did not move.**

---

## Source reachability log (2026-07-29)

WebSearch exhausted per `CLAUDE.md` §5. Retrieval ran on **OpenAlex**, **Crossref**,
**Semantic Scholar**, **ERIC**, **Europe PMC**, **NCBI E-utilities**, **OSF/PsyArXiv**, and
targeted `curl`/`pdftotext` of open-access PDFs.

- **OpenAlex hard-stopped mid-session** with `HTTP 429 — "Insufficient budget. This request costs
  $0.001 but you only have $0.0008 remaining. Resets at midnight UTC."` OpenAlex now meters by
  daily spend. Approximately 25 queries were available. Everything after that point was recovered
  through ERIC, Europe PMC, Semantic Scholar and Crossref.
- **Semantic Scholar** returns `HTTP 429` on any burst; usable at ~1 call per 3–4 s. It carries
  abstracts that OpenAlex does not (Brom et al. 2018 was recovered this way, Springer having
  deposited no abstract).
- **SAGE, Wiley, APA PsycNet, Taylor & Francis, Elsevier** all return `403` to `curl` and
  `WebFetch`. Sinha & Kapur (2021), Kellman et al. (2010), Alfieri et al. (2013), Brunmair &
  Richter (2019), Chi et al. (1981) full texts were unobtainable by that route.
- **Springer** open-access PDFs *do* serve to `curl` at `link.springer.com/content/pdf/<DOI>.pdf`
  — this recovered the two workhorse full texts of this section: **St. Hilaire, Chan & Ahn
  (2024)** on prequestions and **Mar et al. (2021)** on narrative, both quoted verbatim below,
  plus **Aleven et al. (2016)** on help seeking.
- **OSF/PsyArXiv**: `osf.io/<id>/download` works and returned **Noetel et al. (2021)** as a
  `.docx` (not a PDF) — extracted via `zipfile` + regex. This is the single richest source in the
  section, because it quotes every multimedia meta-analysis's pooled estimate with CI and k.
- **Europe PMC `fullTextXML`** works for PMC-native records (this recovered **Park et al. 2025**,
  PMC12770468, in full including the pre-registered nulls) and 404s for NIHMS author manuscripts,
  where **NCBI `efetch.fcgi?db=pmc`** succeeds instead.
- **ERIC API** (`api.ies.ed.gov/eric/`) is the only route to the special-education and
  accommodations literature — DuPaul et al. (2012), Lewandowski et al. (2007), Spiel et al.
  (2016/2019), Clark et al. (2021) appear in no biomedical index. Field-qualified quoted phrases
  (`title:"..."`) work for some records and return `numFound 0` for others; bare keyword queries
  are the reliable fallback.
- **Unverifiable and flagged as such below:** Willcutt et al. (2005) domain-level effect sizes;
  Chi, Feltovich & Glaser (1981) sorting data; Kornell & Bjork (2008) accuracy percentages;
  Schwartz & Martin (2004) numbers; Gawrilow & Gollwitzer (2008) ADHD implementation-intention
  effect sizes; the conceptual-knowledge vs transfer cells of Sinha & Kapur (2021). Each is
  reported as **UNVERIFIED** at point of use and no claim rests on one.

**Evidence labels**, per `CLAUDE.md` §2 plus two new ones authorised for this wave:

`MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH` · `OBSERVED` · `VENDOR` · `DEMO` ·
`INFERENCE` · **`DESIGN`** · **`OPEN`**

- A **`VENDOR`** claim is never restated as a finding.
- A **`DESIGN`** claim specifies an artifact that **does not exist** and must name what would show
  it was the wrong design. **A `DESIGN` claim may never be restated as a finding.**
- An **`OPEN`** claim states a question nobody has asked and **must state why not**.

**Builds on, does not repeat:** B1 (the learning-science floor), C1 (illustration and the
coherence principle), F6 (motivation, gamification moderators, the curiosity primaries), F7
(gesture beats action on objects), F10 (expertise reversal, concreteness fading), F11 (retrieval
practice, spacing, FSRS), H1/H2 (SELPA, accommodations, Kieffer and Rios), K1 (the compression
bound), E3 (the Khanmigo null and its diagnosis).

---

## 0. Executive summary — the numbers that carry the argument

| # | Quantity | Value | Source | Label |
|---|---|---|---|---|
| 1 | Coherence principle — removing seductive details, overall | **g = 0.33 [0.18, 0.48]**, k = 68 | Sundararajan & Adesope 2020 | `MEASURED-META` |
| 2 | …when details are **persistent** on screen | **g = 0.43 [0.29, 0.57]**, k = 47 | ibid. | `MEASURED-META` |
| 3 | …when details are **transient** | **g = 0.12 [−0.33, 0.57]**, k = 18 — *the CI contains the persistent estimate* | ibid. | `MEASURED-META` |
| 4 | Newest and largest seductive-details synthesis | **g = −0.16** overall; comprehension −0.19, recall −0.17, transfer −0.12; 177 ES / 50 studies | Cheng et al. 2026 MASEM | `MEASURED-META` |
| 5 | Mediator of the seductive-details harm | **extraneous load only**; intrinsic and germane load do **not** mediate | ibid. | `MEASURED-META` |
| 6 | Emotional design (faces, pleasant colours) on **learning** | retention **d+ = 0.387** (k=18), comprehension **0.317** (k=14), transfer **0.327** (k=27) | Brom, Stárková & D'Mello 2018, 33 samples, N = 2,924 | `MEASURED-META` |
| 7 | The same manipulations on **feeling** | liking/enjoyment **0.109**, positive affect **0.113**, perceived learning **0.097 n.s.**, effort **0.051 n.s.** (ps > .227) | ibid. | `MEASURED-META` |
| 8 | Independent replication of both halves | retention **0.35**, transfer **0.27**, comprehension **0.29**; positive affect **0.09**, intrinsic motivation **0.15**, liking **0.10** | Wong & Adesope 2021 | `MEASURED-META` |
| 9 | **Representational** animation vs static | **g = 0.40 [0.34, 0.46]**, k = 59 | Höffler & Leutner 2007, via Noetel et al. 2021 | `MEASURED-META` |
| 10 | **Decorational** animation vs static | **g = −0.05 [−0.17, 0.07]**, k = 17 — zero | ibid. | `MEASURED-META` |
| 11 | Signalling (an element that points at the target) | **g = 0.43 [0.35, 0.50]**, k = 209 | Schneider et al. 2018, via Noetel | `MEASURED-META` |
| 12 | Personalisation — conversational "you" instead of formal register | **g = 0.33 [0.23, 0.44]**, k = 55 | Ginns, Martin & Marsh 2013 | `MEASURED-META` |
| 13 | Arousal as a moderator of the seductive-details effect | detrimental effect of seductive details **absent** under induced higher arousal; N = 100, 2×2 false-heartbeat | Rey & Steib 2018 | `MEASURED-RCT` |
| 14 | Does *interruption count* matter, or dose? | **no significant difference** between 5 details grouped (1 interruption) and interspersed (5); extraneous load ↑ and transfer ↓ in both | Wirzberger group 2025 | `MEASURED-RCT` |
| 15 | Narrative vs expository text, memory + comprehension | **g = 0.55 [0.31, 0.79]**, 150 ES, >75 samples, N > 33,000, I² = 98% | Mar et al. 2021 | `MEASURED-META` |
| 16 | …share of those effect sizes where **content was controlled** across genres | **28%** | ibid. | `MEASURED-META` |
| 17 | …publication-bias test | Egger's b = **2.68 [0.57, 4.80]**, p = .01 overall (n.s. for comprehension alone, p = .30) | ibid. | `MEASURED-META` |
| 18 | Narrative **as framing around unchanged content** — interest-personalised algebra story problems | faster and more accurate in-unit; largest for symbolic-equation writing and for **struggling** students; persisted after removal | Walkington 2013, N = 145 9th graders, randomised | `MEASURED-RCT` |
| 19 | **Prequestion effect, specific** (on the material the question asked about) | **g = 0.54 [0.42, 0.66]**, k = 97, p < .001 | St. Hilaire, Chan & Ahn 2024, preregistered | `MEASURED-META` |
| 20 | **Prequestion effect, general** (on everything else in the lesson) | **g = 0.04 [−0.04, 0.11]**, k = 91, **p = .349** | ibid. | `MEASURED-META` |
| 21 | The strongest moderator of the prequestion effect | **guessing g = 0.65 vs not-guessing g = 0.22**, p < .001 | ibid. | `MEASURED-META` |
| 22 | Prequestions by age | **adults g = 0.62 vs grade-school children g = 0.22**, p = .020 | ibid. | `MEASURED-META` |
| 23 | Prequestions, factual vs conceptual | **0.58 vs 0.28**, p = .073 — *contrary to* the curiosity account | ibid. | `MEASURED-META` |
| 24 | Problem-solving-before-instruction vs instruction-first | **g = 0.36 [0.20, 0.51]**, 53 studies / 166 comparisons; **reverses for grades 2–5** and for domain-general skills | Sinha & Kapur 2021 | `MEASURED-META` |
| 25 | Teaching 5–7-year-olds to ask questions — **science learning** | **null**: Mdn 62.5% vs 50.0%, b = 7.74 [−1.93, 17.40], t = 1.59, **p = .12**, p_FDR = .20 | Park et al. 2025, preregistered RCT, N = 103 | `MEASURED-RCT` |
| 26 | …**valuing** new information (willingness-to-pay) in the same trial | b = 2 [0.76, 3.24], t = 3.19, **p = .002**, p_FDR = .010; Wilcoxon r = .23 | ibid. | `MEASURED-RCT` |
| 27 | **After three consecutive errors on a step, the learner asks for a hint** | **34% of the time** | Aleven & Koedinger 2000, Geometry Cognitive Tutor logs | `OBSERVED` |
| 28 | Share of hint levels viewed for **under one second** (answer mining) | **68%** | Aleven & Koedinger 2001 | `OBSERVED` |
| 29 | Fixing help-seeking behaviour with a metacognitive tutor | **lasting behaviour change months after removal; no improvement in domain-level learning** | Roll et al.; stated by Aleven et al. 2016 as "the main disappointment" | `MEASURED-RCT` (null) |
| 30 | When do hints help at all? | **only at intermediate skill.** At low or high skill, attempting without help was more effective | Roll et al. 2014 EDM, via Aleven et al. 2016 | `OBSERVED` |
| 31 | Metacognitive prompts in computer-based environments | **SRL activity g = 0.50 [0.37, 0.63]; learning outcomes g = 0.40 [0.31, 0.49]**; moderated by feedback, specificity, adaptability | Guo 2022 | `MEASURED-META` |
| 32 | Implementation intentions ("if X, then I will Y") in children | **g = 0.31 [0.21, 0.41]**, 52 ES / 42 studies, **N = 12,957**, I² = 65.2%; stronger in younger children and, in some analyses, children with ADHD | Breitwieser & Reinelt 2026, registered report | `MEASURED-META` |
| 33 | SRL interventions, average effect — **and who delivers them** | ES = 0.69; **higher when delivered by researchers than by regular teachers** | Dignath & Büttner 2008, 84 studies / 357 ES | `MEASURED-META` |
| 34 | Instructor-segmented vs learner-segmented content | **g = 0.41 [0.32, 0.50] vs g = 0.20 [0.11, 0.28]**, k = 32 each | Rey et al. 2019, via Noetel | `MEASURED-META` |
| 35 | Multimedia design principles, system-paced vs learner-paced | **g = 0.41 [0.33, 0.49] vs 0.27 [0.19, 0.35]**, p = .02 | Noetel et al. 2021 meta-meta | `MEASURED-META` |
| 36 | Segmenting **costs study time** while improving learning | **g = 0.92 [0.82, 1.02]**, k = 19 (more time taken) | Rey et al. 2019, via Noetel | `MEASURED-META` |
| 37 | ADHD — is the deficit in *sustaining*? | **No.** Overall CPT omissions **δ = 1.34**; performance-over-time omissions **δ = 0.54, 80% CV −0.14 to 1.22** (crosses zero). Mechanism: d′ **d = 0.98**, drift rate **d = 0.75**, response bias **d = 0.04 n.s.** | Huang-Pollock et al. 2012, 47 studies | `MEASURED-META` |
| 38 | ADHD — reaction-time variability | children **g = 0.76**, adults **g = 0.46**, 319 studies; stimulants attenuate **g = −0.74**; **unaffected by non-stimulant medical and psychosocial interventions**; adolescents/adults **indistinguishable from clinical controls** | Kofler et al. 2013 | `MEASURED-META` |
| 39 | ADHD — delay discounting | **d = 0.43**, 25 comparisons, N = 3,913, p < 10⁻¹⁵, no moderation by age or reward reality | Jackson & MacKillop 2016 | `MEASURED-META` |
| 40 | Does high incentive normalise ADHD working memory? | **No — but it normalises persistence.** €10 and gaming improved performance without normalising it; only the ADHD group declined over time, and the strongest incentives **normalised the decline** | Dovis et al. 2012, 30 vs 31 | `MEASURED-RCT` |
| 41 | Methylphenidate on **academics** vs symptoms | symptoms **SMD −0.70 [−0.85, −0.55]** (placebo arm itself −0.68); math productivity **+7.8%**, math accuracy **+3.0%**, reading speed SMD .47, **reading accuracy n.s.** | Cerrillo-Urbina 2018; Kortekaas-Rijlaarsdam 2019 | `MEASURED-META` |
| 42 | Cognitive training in ADHD, blinded | ADHD total **SMD 0.12 [−0.01, 0.25]**; inattention 0.17 [0.02, 0.31] rising to 0.40 **only inside the training setting**; **no effect on attention, inhibition, reading or arithmetic** | Westwood et al. 2023, 36 RCTs | `MEASURED-META` |
| 43 | School-based ADHD intervention, between-subjects | behaviour **0.18 n.s.**; academic **0.43 n.s.** (between) and **0.42 n.s.** (within) | DuPaul, Eckert & Vilardo 2012, 60 studies / 85 ES | `MEASURED-META` |
| 44 | Extended time for ADHD — differential boost | **three independent failures**; one finds the *opposite* direction (more symptoms → **less** benefit). No ADHD-specific meta-analysis exists; first RCT still running | Lewandowski 2007; Miller 2015; Lovett & Leja 2015; Malcon 2026 protocol | `MEASURED-RCT` (null) |
| 45 | The one accommodation with a differential boost in ADHD | **read-aloud** — two randomised experiments, younger students | Lovett & Nelson 2021, 510 screened / 68 included | `MEASURED-META` |
| 46 | Perceptual learning module — solving *time* on algebra transformations | **~28 s → ~12 s** per problem, accuracy already ~80% at pretest, **preserved at 2 weeks**; learners never solved equations, only judged legality | Kellman, Massey & Son 2010, N = 30 | `MEASURED-RCT` |
| 47 | Perceptual learning module vs narrated lecture, at 1 month | PALM accuracy **d = 0.89**, fluency **d = 1.16**; lecture retained accuracy (**d = 0.44**) and **not fluency** | Ahmad et al. 2021 RCT, N = 83 | `MEASURED-RCT` |
| 48 | Learning through case comparison | **d = 0.50 [0.44, 0.56]**, 57 experiments / 336 tests; only 4 of 15 moderators reliable | Alfieri, Nokes-Malach & Schunn 2013 | `MEASURED-META` |
| 49 | Interleaving — and where it reverses | overall **g = 0.42**; paintings **0.67**, mathematics **0.34**, expository texts and tastes **n.s.**, **words g = −0.39 (blocking wins)** | Brunmair & Richter 2019, 59 studies / 238 ES | `MEASURED-META` |
| 50 | Generation effect | **d = 0.40**, 86 studies / 445 ES / N = 17,711; **incidental d = .65 vs intentional d = .32**; **anagrams reverse, d = −.05** | Bertsch et al. 2007 | `MEASURED-META` |
| 51 | Prediction before reveal — memory | **no main effect** (b = −0.090, p = .330); **condition × expectancy-violation b = 0.195, SE = .062, p = .002** | Theobald & Brod 2022 | `MEASURED-RCT` |
| 52 | Gesture vs action on objects | **no difference on trained problems**; near transfer action worse than abstract gesture **β = −1.58, p = .049**; far transfer **β = −2.06, p = .02** | Novack et al. 2014, N = 142 | `MEASURED-RCT` |

**The five sentences the section exists to license.**

1. **Referential status, not persistence, decides whether an added element helps or harms**
   (rows 1–12). Persistence is a *dose multiplier* on an element that already has a competing
   referent; it is not the mechanism.
2. **The benefit of "making it engaging" is not mediated by making the learner feel good**
   (rows 6–8). Two independent meta-analyses put learning at 0.27–0.39 and liking at 0.09–0.11 in
   the same studies.
3. **A question holds attention because it can be attempted; an exhortation cannot** (rows 19–23).
   And it holds attention on *its own answer only* — g = 0.54 specific, g = 0.04 general.
4. **Executive function is a resource products require and do not supply** (rows 27–36). The
   measured failure point is *recognising the need*, not *accessing the help* — and repairing the
   recognition, on its own, does not repair learning.
5. **The ADHD design target is signal-to-noise per opportunity and delay-to-payoff, not session
   length** (rows 37–41). The vigilance decrement is the folk model; the data locate the deficit
   in the first block.

---

## 1. The joke question, resolved

### 1.1 What the corpus's hinge actually says, read at full precision

The corpus treats **Sundararajan & Adesope (2020)** as the hinge: seductive details harm at
**g = 0.43 when persistent** and **g = 0.12, n.s. when transient**. That reading licenses a clean
inference — a teacher's aside is transient, a decorated sidebar is persistent, therefore the aside
is safe.

The confidence intervals do not support that inference. Recovered verbatim from Noetel et al.
(2021), which quotes the pooled estimates with their intervals:

> "Effects were bigger when seductive details were otherwise displayed persistently on-screen
> (g = 0.43, 95% CI [0.29, 0.57], k = 47; Sundararajan & Adesope, 2020) as opposed to being
> transient (**g = 0.12, 95% CI [−0.33, 0.57]**, k = 18; Sundararajan & Adesope, 2020)."

`MEASURED-META`. **The transient interval runs from −0.33 to 0.57. It contains 0.43.** The data
are consistent with transient details being harmless, and equally consistent with transient
details being *exactly as harmful as persistent ones*. With k = 18 the transient cell is not a
null result; it is an **unmeasured** cell. The honest statement is: *nobody has measured the
transient case with enough power to distinguish it from the persistent case.*

This is a correction to the corpus's own framing and it should be carried forward. Everything the
section builds must therefore rest on something other than transience.

### 1.2 The estimate has also shrunk

**Cheng, Wu, Wang & Wang (2026)**, *Educational Psychology Review*, `10.1007/s10648-025-10099-z`
— a multi-level meta-analysis and MASEM over **177 effect sizes from 50 studies**, recovered via
ERIC (EJ1510171):

> "(a) seductive details have a small but statistically significant negative effect on overall
> learning outcomes (**g = −0.16**); (b) the negative effects are observed for comprehension
> (**g = −0.19**), recall (**g = −0.17**), and transfer (**g = −0.12**); (c) sample size, language
> of seductive text, and learning environment significantly moderate the effect; and (d) seductive
> details undermine learning outcomes primarily by **increasing extraneous cognitive load**,
> whereas intrinsic and germane cognitive load do not play significant mediating roles."

`MEASURED-META`. Two things follow. First, the newest and largest synthesis puts the effect at
roughly **half** the 2020 estimate — the seductive-details effect is real, replicated, and
**small**. Second, the mediation is specific: the harm travels through *extraneous* load. Not
through distraction of interest, not through emotional interference, not through schema
competition. That narrows the candidate mechanisms sharply and is the strongest available
evidence on the *why*.

### 1.3 The adjudication: four candidate variables, tested

The brief asks whether transience is the operative variable, or relevance, or arousal, or the
teacher's social presence. Each has a test in the retrieved literature.

**Candidate A — persistence.** Falsified as *the* mechanism by §1.1 (the interval) and by a direct
experiment. **Wirzberger and colleagues (2025)**, *Applied Cognitive Psychology*,
`10.1002/acp.70065`, asked whether the *number of interruptions* is what matters, comparing five
seductive details grouped together (one interruption) against five interspersed (five
interruptions):

> "Results confirmed that extraneous cognitive load was increased and transfer performance
> impaired in conditions with seductive details. However, **no significant differences were found
> between the grouped condition … and the interspersed condition**. … The extent of the seductive
> detail effect might rather depend on the **amount** of seductive details presented than the
> number of interruptions caused."

`MEASURED-RCT`. Interruption structure is not the variable. **Dose is.** Persistence is best
understood as *dose extended over time* — an element on screen for twenty minutes is a larger dose
than the same element for twenty seconds — which is why it moderates without being the mechanism.

**Candidate B — arousal.** Tested directly. **Rey & Steib (2018)**, *Applied Cognitive Psychology*,
`10.1002/acp.3473`, N = 100, 2 (seductive details present/absent) × 2 (lower/higher false
heartbeat feedback), with cognitive load, motivation, heart rate and electrodermal activity
measured:

> "Results show learning-inhibiting effects for seductive details and learning-enhancing effects
> for higher false heart rates. Cognitive processes mediate both effects. However, **the
> detrimental effect of seductive details was not present when heart rate was higher.** Results
> indicate that the seductive detail effect is moderated by a learner's state of arousal."

`MEASURED-RCT`. Arousal *is* a moderator — an aroused learner absorbs the extraneous load without
cost. But this is one experiment at N = 100 with a deceptive-biofeedback manipulation, and no
replication was retrieved. It licenses a hypothesis, not a design principle. Note also its
direction: arousal does not make the detail *useful*; it makes the learner *able to afford* it.

**Candidate C — the teacher's social presence.** The closest measured proxy is the pedagogical
agent, and the numbers are unflattering to the naive reading. From Noetel et al. (2021), quoting
four reviews:

- Pedagogical agents overall: **g = 0.19 [0.12, 0.27], k = 43** (Schroeder et al. 2013).
- Agents that **gesture toward what is important** — i.e. that serve a *signalling* function:
  **g = 0.28 [0.01, 0.54], k = 7** (Davis 2018).
- Agents in **3D: g = 0.11 [−0.06, 0.27], k = 21** (n.s.); agents in **2D: g = 0.38 [0.16, 0.60],
  k = 11** (Castro-Alonso et al. 2021). The more elaborate agent is worse.
- **School students g = 0.56** vs university students; **text-based agents g = 0.51 vs voice
  g = 0.12** (Schroeder et al. 2013).

`MEASURED-META`. Social presence *per se* is worth about 0.19. Social presence that **points at
the referent** is worth more; social presence rendered more vividly is worth less. Presence is not
the variable either — what the presence *does* is.

**Candidate D — referential status.** This is the one that survives every test. Assemble the
comparison the individual literatures never assemble, because they are published in different
sub-fields:

| The added element's relation to the target | Measured effect | Source |
|---|---|---|
| **Points at** the target (arrow, highlight, laser pointer, agent's gesture) | **g = +0.43 [0.35, 0.50]**, k = 209 | Schneider et al. 2018 |
| **Is** the target, dressed (round shapes, warm colours, a face on the enzyme) | **d+ = +0.33 to +0.39** across retention, comprehension, transfer | Brom et al. 2018; Wong & Adesope 2021 |
| **Speaks about** the target in the second person ("your blood vessels" not "the blood vessels") | **g = +0.33 [0.23, 0.44]**, k = 55 | Ginns et al. 2013 |
| **Moves, but represents nothing** (decorative animation) | **g = −0.05 [−0.17, 0.07]**, k = 17 | Höffler & Leutner 2007 |
| **Sits adjacent, representing nothing** (decorative borders, headers, footers) | **no significant effect on retention, transfer, or time**, N = 95, 3×3 design | Rey 2012 (JEMH) |
| **Carries its own competing referent** (an interesting, self-contained, irrelevant story) | **g = −0.16** (177 ES) to **−0.43** (k = 47, persistent) | Cheng et al. 2026; Sundararajan & Adesope 2020 |

`MEASURED-META` throughout; the Rey (2012) row is `MEASURED-RCT`.

The ordering is monotone in one variable and one only: **does the element have a referent, and is
that referent inside or outside the target schema?**

- Referent **is** the target → helps most.
- Referent **points to** the target → helps most.
- **No referent at all** → does nothing. Not harmful. *Inert.* This is the finding that kills
  "extraneousness" as the explanation: a decorative border is maximally extraneous and maximally
  persistent, and costs nothing.
- Referent is **outside** the target and self-sufficient → harms, in proportion to dose.

### 1.4 What this says about the joke

**The measured literature does not distinguish jokes from non-jokes. It distinguishes referents
from non-referents.** A joke is not a category the evidence recognises. What the evidence
recognises is what the joke is *about*.

Sort the teacher's repertoire by referent, not by form:

| The teacher does | Referential status | Predicted effect | Basis |
|---|---|---|---|
| An absurd extreme case ("what if the elephant weighed nothing?") | **is** the target, at a boundary | positive | signalling + emotional design bands |
| A comic analogy that maps onto the structure | **is** the target, in another dress | positive | personalisation g = 0.33; case comparison d = 0.50 |
| A pun on the technical term | **points at** the target, weakly | small positive | signalling, low dose |
| A funny voice while explaining the mechanism | no referent, transient, low dose | inert | decorative-animation g = −0.05 |
| A self-contained anecdote about the teacher's weekend | competing referent | negative, dose-proportional | seductive details g = −0.16 to −0.43 |
| A gripping true story about a scientist's tragic life, told before the equation | competing referent, high interest, high dose | negative — **this is the canonical seductive detail** | Garner et al. 1989; Harp & Mayer 1998 |

`INFERENCE` — this table is a mapping of a well-measured variable onto an unmeasured taxonomy. It
is stated as a design hypothesis, not a finding. What is measured is the referential ordering; the
assignment of specific teacher behaviours to rows in it is not.

**The owner's instinct is right and the reason he gives for it is wrong.** Great teachers do grab
attention with jokes, and it is not because the joke is funny, and it is not because the joke is
brief. It is because a great teacher's joke is *about the thing* — it is the concept, held at a
strange angle. The teacher who tells an unrelated funny story is running the canonical
seductive-details manipulation on their own class, and does so at the measured cost.

### 1.5 The second falsification: "make it fun" is not the mechanism

This is the most consequential number in §1 and it is easy to miss because it appears twice in two
independent meta-analyses of the same manipulation.

**Brom, Stárková & D'Mello (2018)**, *Educational Research Review*, `10.1016/j.edurev.2018.09.004`,
33 independent samples, N = 2,924, recovered verbatim via Semantic Scholar:

> "We found significant positive meta-analytic effects for **retention (k = 18, d+ = 0.387)**,
> **comprehension (k = 14, d+ = 0.317)**, and **transfer (k = 27, d+ = 0.327)** under a
> random-effects model. Effects for affective-motivational variables were mixed, with a robust
> effect for **intrinsic motivation (k = 23, d+ = 0.255)**, a **weaker effect for liking/enjoyment
> (k = 20, d+ = 0.109)**, and a **marginal effect for positive affect (k = 15, d+ = 0.113)**. The
> manipulations **did not significantly (ps > .227) influence perceptions of learning (k = 11,
> d+ = 0.097) or effort (k = 20, d+ = 0.051)**, but reduced perceptions of difficulty
> (k = 14, d+ = −0.208)."

**Wong & Adesope (2021)**, *Educational Psychology Review*, `10.1007/s10648-020-09545-x`, a
declared replication and extension over 28 articles, recovered via ERIC (EJ1295978):

> "Results showed that including emotional designs enhanced learning outcomes (**retention:
> g+ = 0.35; transfer: g+ = 0.27; comprehension: g+ = 0.29**), **change in positive affect
> (g+ = 0.09)**, **intrinsic motivation (g+ = 0.15)**, mental effort (g+ = 0.11),
> **liking/enjoyment (g+ = 0.10)**, and reduced perceived difficulty (g+ = −0.21)."

`MEASURED-META`, twice, independently. **In the same studies, learning moves 0.27–0.39 and liking
moves 0.09–0.11.** If the mechanism were "the learner enjoys it more and therefore attends more,"
the affective effect would have to be at least as large as the cognitive one. It is a third the
size.

The one affective variable that moves in a way consistent with the learning effect is **perceived
difficulty, down 0.21**. That is a different claim entirely: emotional design does not make the
material *fun*, it makes the material *look approachable*. Brom et al. also report `ps > .227` on
**perceived effort** — learners do not think they are working less; they think the thing is less
hard to face.

**Design consequence.** `INFERENCE`. Optimise the affective surface for **approachability**, not
for amusement. The measured lever is "this looks like something I could do," not "this is
enjoyable." One further datum in the same direction, from Brom et al.: the intrinsic-motivation
effect was moderated by age, "such that **larger effects were revealed for children compared to
older learners**" — the affective surface matters more for the younger learner even though it is
not the mechanism for anyone.

### 1.6 Three moderators that decide whether any of this matters at all

From Noetel et al.'s (2021) meta-meta-analysis, 29 reviews / 1,189 studies / 78,177 participants,
recovered in full:

- **Element interactivity.** Design principles were worth **g = 0.70 [0.59, 0.81]** in complex
  media and **g = 0.20 [0.02, 0.39]** in simple media (p < .001). Getting the coherence of a
  simple explanation right buys almost nothing; getting it right on a hard one buys 0.70.
- **Pacing.** **g = 0.41 [0.33, 0.49]** system-paced vs **g = 0.27 [0.19, 0.35]** learner-paced
  (p = .02). Sundararajan & Adesope independently list *learner pacing* among their significant
  moderators. **A live teacher is a system-paced medium. A textbook is learner-paced.** The joke
  and the sidebar are therefore not only different in referent — they are being delivered into
  regimes where design fidelity carries different weight.
- **Prior knowledge did not moderate** (30 pooled effects, R² = 0.14, **p = .14**), and neither
  did education level (p = .95), presentation format (p = .24), or subject (p = .22). `MEASURED-META`.
  This is a useful null: the coherence discipline is not something advanced learners can be spared.

---

## 2. Narrative — vehicle or competitor?

### 2.1 The headline number, and the confound that decides how to read it

**Mar, Li, Nguyen & Ta (2021)**, *Psychonomic Bulletin & Review*, `10.3758/s13423-020-01853-1`,
full text recovered as PDF. A three-level random-effects meta-analysis of **150 effect sizes** from
**more than 75 unique samples** and **more than 33,000 participants**:

> "Our three-level random-effects meta-analysis of 150 effect-sizes found that, on average, memory
> and comprehension of narrative texts was superior to that for expository texts. The mean
> effect-size was a Hedge's g of **.55, with a 95% CI ranging from .31 to .79, p < .001**."

`MEASURED-META`. Robust to leave-one-out at both effect-size level (g range .54–.57) and study
level (g range .48–.59). Comprehension alone **G = .48 [.21, .75]**; corroborated by an independent
meta-analysis of inferential comprehension, **Clinton et al. (2020), G = .36 [.07, .66], k = 38**,
which the authors note emerged "despite different sampling criteria, different meta-analytic
methods, and a complete independence of efforts."

Now the three qualifications, all from the paper itself:

1. **Heterogeneity is essentially total.** Q(149) = 2884.68, p < .001; **I² = 98%**, of which
   I²_level3 = 67% is between-study. The pooled 0.55 describes a distribution, not a phenomenon.
2. **Publication bias is present.** Egger's regression: "higher standard errors did predict larger
   effect-sizes, **b = 2.68 (95% CI: .57, 4.80), SE = 1.04, p = .01**." Split by outcome, the bias
   signal is absent for comprehension (b = 1.62, 95% CI −1.56 to 4.81, p = .30) and present for
   memory.
3. **The confound that decides the brief's question.** Verbatim: *"only a minority of our
   effect-sizes came from studies in which content was controlled (**28%**)."* And on the
   moderators: "Little difference was observed … when researchers reported an attempt to control
   the difficulty (**Gdiff = .03**) or content across the genres (**Gdiff = .02**)" — with the
   authors' own caution that "failure to attain statistical significance may be a function of small
   sample sizes and/or large amounts of variability."

**How to read this honestly.** The g = 0.55 is overwhelmingly a comparison of *stories about
people doing things* against *essays about abstractions*. In **72%** of the effect sizes the two
genres are not carrying the same content. The moderator test says matching content does not change
the result, and that test is underpowered. So the pooled estimate licenses: *narrative-structured
material is remembered and understood better than expository material*. It does **not** license:
*wrapping any content in a story adds 0.55*.

One further moderator worth carrying, because it interacts with everything in §1: **"Non-adults
also exhibited a larger benefit from narrative texts compared to adults (Gdiff = .23)"** —
non-significant, and the direction is the opposite of the age pattern for questions (§3.5). Report
as a signal, not a finding.

### 2.2 The distinction the field elides — stated precisely

There are two things called "story" and they are different interventions with different measured
literatures:

- **(a) Narrative as the structure of the content.** The causal chain of the material *is* the
  narrative — a mechanism unfolding in time, an agent with a goal encountering an obstacle. This
  is what Mar et al. measured, at g = 0.55 with the genre confound above.
- **(b) Narrative as framing around unchanged content.** The content is identical; a situational
  wrapper is added or swapped. This has its own measured literature and its own, much more
  specific, result.

They are elided because both are described as "using stories to teach." §1's framework predicts
the difference: in (a) the narrative *is* the referent; in (b) the narrative is a *second* referent
whose value depends entirely on whether the learner needs a bridge to the first.

### 2.3 Narrative-as-framing, measured

**Walkington (2013)**, *Journal of Educational Psychology*, `10.1037/a0031882`, recovered via ERIC
(EJ1054444). A randomised learning experiment: **145 ninth-grade Algebra I students**, randomly
assigned within the Cognitive Tutor Algebra ITS. For one instructional unit, half received normal
algebra story problems and half received **matched problems personalised to their out-of-school
interests** — sports, music, movies — with the mathematics unchanged.

> "Results showed that students in the personalization condition **solved problems faster and more
> accurately** within the modified unit. The impact of personalization was **most pronounced for
> one skill in particular — writing symbolic equations from story scenarios — and for one group of
> students in particular — students who were struggling to learn** within the tutoring environment.
> **Once the treatment had been removed**, students who had received personalization continued to
> write symbolic equations for normal story problems with increasingly complex structures more
> accurately and with greater efficiency."

`MEASURED-RCT`. Effect sizes are not stated in the retrievable abstract and the article is not
open access — **the magnitudes are UNVERIFIED**; the pattern is not.

Read against §1's framework, this is exactly the predicted result and it is highly specific. The
narrative wrapper did **not** make the algebra easier. It helped at the **one step where the story
is the referent** — mapping a described situation onto a symbolic expression — and it helped most
for the learners with the least prior structure to map with. This is the same shape as Ginns et
al.'s personalisation principle (g = 0.33, k = 55, changing register alone), and the same shape as
the emotional-design result: the wrapper works when it is *attached to the thing*, and its benefit
concentrates on the learner who needs the attachment.

### 2.4 Verdict

**A story is a vehicle when it supplies the referent for a mapping the learner must make. It is a
competitor when it supplies a referent the learner does not need.** `INFERENCE`, built on the
combination of §1.3's referential ordering, Mar et al.'s content-control confound, and Walkington's
skill-specific transfer.

Three operational consequences:

1. **Ask what the story is the referent for.** If the answer is "nothing — it makes it
   interesting," you are running the seductive-details manipulation. If the answer is "the mapping
   from situation to formalism," you are running Walkington's manipulation.
2. **Narrative structure is free when the content already has one.** Mechanisms, derivations,
   proofs, algorithms and histories all *are* causal chains. Presenting them as such is (a), not
   (b), and costs nothing.
3. **The load a narrative wrapper adds is real and is charged to extraneous load** (Cheng et al.
   2026's mediation). Which means the wrapper's benefit has to exceed its own cost — and that
   margin is widest, per Walkington, for the struggling learner and narrowest for the fluent one.
   This is the expertise-reversal shape the corpus already documents in F10.

`OPEN` — **Nobody has run the crossed design.** The clean experiment is 2 × 2: narrative-structured
vs expository content, crossed with personalised vs generic framing, same domain, same test. It has
not been run. *Why not:* the two literatures live in different fields with different outcome
instruments — text-comprehension research (Mar) uses recall and inference measures on prose;
context-personalisation research (Walkington) uses within-tutor performance on symbolic tasks.
Neither instrument works on the other's materials, so no single study has ever had both factors.

---

## 3. The question as the actual mechanism

This is the owner's strongest instinct and it is the best-measured claim in the section. It is also
the one where the *reason* matters most, because the mechanism dictates the design.

### 3.1 The prequestion effect, and the null hiding inside it

**St. Hilaire, Chan & Ahn (2024)**, *Psychonomic Bulletin & Review* 31:411–441,
`10.3758/s13423-023-02353-8` — a **preregistered** meta-analysis, full text recovered as PDF. This
is the single most important source in the section.

> "The pooled effect size for the **specific effect** was **g = 0.54 [0.42, 0.66]**, providing
> solid evidence that prequestions enhance learning of the tested material (**k = 97**), p < .001.
> … In stark contrast to the specific effect, there was **virtually no evidence for the general
> effect, g = 0.04 [−0.04, 0.11]**, as 54% of studies showed positive effects and 46% of studies
> showed either no effect or a negative effect (**k = 91**), **p = .349**."

`MEASURED-META`. Publication-bias-adjusted estimates: **0.45 specific, 0.04 general**. Published
vs unpublished: specific 0.59 vs 0.49; general 0.06 vs 0.003 — the bias is small and does not
change the conclusion.

**This is the most important structural fact about questions in the whole literature.** A question
asked before instruction improves learning of *the thing the question asked about*, by half a
standard deviation, and improves learning of everything else in the lesson by **nothing**. A
prequestion is not an attention-setting device for a lesson. It is a **spotlight with a beam the
exact width of the question**.

### 3.2 The mechanism: it is the attempt, not the curiosity

The meta-analysis was designed to adjudicate between a *memory precursor* account and a *curiosity
precursor* account, and it does. The moderator results, verbatim:

- **Guessing is the dominant moderator.** "Both the memory and curiosity precursor accounts
  correctly predicted a greater specific effect when participants were asked to **guess** the
  answer to the prequestions during the pre-study phase (**g = 0.65**) than when they were not
  (**g = 0.22**), **p < .001**. Indeed, **amongst all of the moderator variables, prequestion
  guessing had the strongest influence on the PE**."
- **Against the curiosity account.** "a marginally larger specific effect was observed for
  **factual prequestions (g = 0.58)** than for **conceptual prequestions (g = 0.28)**, p = .073"
  — described by the authors as "a pattern that was contrary to that predicted by the curiosity
  precursor account."
- **Lower prior knowledge helps.** Negative association between the effect and prequestion
  performance, **β = −0.49, p = .094** (authors flag outliers and under-reporting; treat as
  suggestive).

`MEASURED-META`. **The question does its work by being attempted.** A question that is merely
*read* is worth 0.22; a question that is *answered wrongly* is worth 0.65. That is a factor of
three, and it is the largest moderator in a meta-analysis of 97 effect sizes.

This converges exactly with the curiosity primaries the corpus already holds. **Kang et al. (2009)**,
*Psychological Science*, "The Wick in the Candle of Learning," verbatim via Semantic Scholar:

> "The functional imaging also showed that **curiosity increased activity in memory areas when
> subjects guessed incorrectly**, which suggests that curiosity may enhance memory for **surprising**
> new information. This prediction about memory enhancement was confirmed in a behavioral study:
> Higher curiosity in an initial session was correlated with better recall of **surprising** answers
> 1 to 2 weeks later."

`MEASURED-BENCH`. The memory benefit in the founding curiosity study rides on **the wrong guess and
its correction**, not on the feeling. And **Gruber, Gelman & Ranganath (2014)**, *Neuron*: the
incidental-material benefit was supported by *anticipatory* midbrain–hippocampal connectivity — the
state before the answer arrives, not the state of enjoying the topic.

And it converges with the generation-effect meta-analysis. **Bertsch, Pesta, Wiscott & McDaniel
(2007)**, *Memory & Cognition*, `10.3758/BF03193441`: **86 studies, 445 effect sizes, N = 17,711**,
overall **d = .40**; **incidental learning d = .65 vs intentional d = .32**; and the reversal —
**anagram generation d = −.05**, CI excluding zero, across 18 studies and >1,000 subjects.
`MEASURED-META`. Generating helps; generating something with no semantic relation to the target
hurts. The same referential rule as §1.

### 3.3 Why a question holds attention where an exhortation does not

Four mechanisms, each with a number:

1. **A question creates a specific, checkable retrieval target.** The specific/general split
   (0.54 vs 0.04) *is* this claim, measured. An exhortation — "this next part is important, pay
   attention" — is a general instruction, and general effects in this literature are 0.04.
2. **A question can be attempted; an exhortation cannot.** Guessing 0.65 vs 0.22. The attempt is
   the act that converts the interval from passive to committed.
3. **The attempt creates an open loop with a pending answer.** This is Loewenstein's (1994)
   information-gap account, and it is the only part of this section that is theory rather than
   measurement — `INFERENCE`. What the data supply is the *consequence*: Pan & Carpenter's (2023)
   review concludes the mechanisms "appear to involve **test-induced changes in subsequent learning
   behaviors**." The question changes what the learner *does next*. It is a behavioural
   intervention wearing a cognitive costume.
4. **The error makes the correction memorable.** Kang's surprising-answer recall at 1–2 weeks;
   Theobald & Brod's (2022) finding (§7.5) that prediction has **no main effect on memory**
   (b = −0.090, p = .330) but a **condition × expectancy-violation interaction b = 0.195,
   SE = .062, p = .002**. Prediction does not amplify memory. It *routes* memory to the surprises.

**Therefore: a question is a commitment device.** It converts an interval of exposure into an
interval with an outstanding, checkable obligation. An exhortation asks for a state of mind. A
question asks for an output. `INFERENCE`, resting on rows 19–23 and 50–51.

And the same mechanism names the failure mode: **if the learner does not attempt, there is no
effect.** Which returns the whole argument to §4.

### 3.4 How a question differs from a quiz

| | **Question (prequestion)** | **Quiz (retrieval practice)** |
|---|---|---|
| When | Before the answer is available | After the answer has been available |
| Expected accuracy | Low, by design | Moderate to high |
| Measured effect | **g = 0.54** on what it asks; **g = 0.04** on the rest | **g = 0.51 vs restudy** (corpus B1: Adesope, Trevisan & Sundararajan 2017) |
| Requires | An attempt and then feedback | Successful or near-successful retrieval |
| Fails when | The learner does not attempt | The material was never encoded |
| Does the work | The error and its correction | The retrieval itself |

`MEASURED-META` both columns. They are not substitutes and neither replaces the other:
**questions before, quizzes after.** Pan & Carpenter's condition is explicit — pretesting benefits
learning "**if there is an opportunity to study the correct answers afterwards**." A prequestion
without a subsequent answer is not a weak intervention; it is not the intervention.

### 3.5 Where the instinct breaks: children, and the classroom

Four results, in increasing order of how much they should change the design.

**(i) Prequestions are substantially weaker in children.** "The age group moderator showed that
**adult participants (g = 0.62)** tended to produce a larger specific effect than **grade school
children (g = 0.22)**, **p = .020**." The authors caution: "borderline p value and the limited
number of effect sizes (k = 20 for the specific effect and k = 18 for the general effect) in the
grade school category." `MEASURED-META`.

**(ii) The whole "struggle before instruction" family reverses for younger children.** Sinha &
Kapur (2021), *Review of Educational Research*, `10.3102/00346543211019105`: 53 studies, 166
comparisons, problem-solving-then-instruction over instruction-then-problem-solving
**g = 0.36 [0.20, 0.51]**, publication-bias-corrected **g = 0.87**. And: "**Contrasting trends were,
however, observed for younger age learners (second to fifth graders) and for the learning of
domain-general skills, for which effect sizes favored I-PS.**" `MEASURED-META`. Two independent
literatures, same boundary.

**(iii) Prequestions did not work in an actual classroom.** **Geller, Carpenter, Lamm, Rahman,
Armstrong & Coffman (2017)**, *Cognitive Research: Principles and Implications*,
`10.1186/s41235-017-0078-z` — an undergraduate chemical-engineering course, prequestions at the
start of class, the same question again at the end, plus a new question, plus weekly quizzes:

> "Performance on questions at the end of class revealed **no difference in performance for
> postquestions vs. new questions**. Although weekly quiz performance revealed **an effect of
> retrieval practice** … there was **no difference in weekly quiz performance on postquestions vs.
> new questions**. These results suggest that retrieval practice is beneficial to learning in the
> classroom. **However, prequestions do not appear to enhance learning, nor to enhance the effects
> of retrieval practice.**"

`MEASURED-RCT` (null). The quiz worked in the classroom. The question did not.

**(iv) Teaching young children to ask questions produced a preregistered null on learning.**
**Park, Colantonio, Delgado Reyes et al. (2025)**, *npj Science of Learning*,
`10.1038/s41539-025-00384-5`, PMC12770468, full text recovered. **N = 103 children aged 5–7**,
randomly assigned to be encouraged to *ask questions* or to *listen carefully*, across **eight
one-on-one science lessons over two weeks**. Verbatim from the results:

- **Willingness-to-pay for new information — the one positive.** "QA: Mdn = 6, L: Mdn = 5,
  **b = 2, 95% CI [.76, 3.24], t = 3.19, p = 0.002, p_FDR = 0.010**, n = 103" (Wilcoxon r = .23).
- **Science learning — null.** "We also did not find a significant difference on the science
  learning measure (QA: Mdn = **62.5%**, L: Mdn = **50.0%**, **b = 7.74, 95% CI [−1.93, 17.40],
  t = 1.59, p = 0.12, p_FDR = 0.20**, n = 103)."
- **Persistence — null.** "b = −21.73, 95% CI [−64.13, 20.67], t = −1.02, p = 0.31."
- **Prompted question-asking about a novel animal — null.** "b = −0.39, 95% CI [−1.51, 0.74],
  t = −0.68, p = 0.5."
- **Cued exploration — significant in the *wrong* direction.** "the **listening group opened more
  cued envelopes than the question asking group** … b = −1, 95% CI [−1.88, −0.12], t = 2.27,
  p = 0.02, p_FDR = 0.05."
- **The moderation that matters.** "**WISC Vocabulary × Condition: b = −1.80, 95% CI [−3.40,
  −0.20], t(97) = −2.23, p = .028**" — and the authors' reading: "The relationship between final
  science learning scores and vocabulary was **weaker in the question-asking condition**,
  suggesting that this intervention **'equalized' children's learning outcomes**."
- **The exploratory result that must be reported with its caveats.** "children with greater
  attention problems showed greater science learning in the question-asking condition (CBCL
  attention problems × condition: **b = 4.13, 95% CI [0.08, 8.191], t(97) = 2.02, p = 0.046**)…
  **because this effect … was driven by two outliers, and not preregistered, it should be
  interpreted with caution.**"

`MEASURED-RCT`. This is the best-designed available test of "teach the child to ask the questions"
and its primary learning outcome is null. Its positive result is that children came to **value new
information more** — a real and possibly more important outcome, on a two-week horizon, with no
demonstrated learning consequence yet.

**(v) And a fifth, from a full school year.** **Clark, Harbaugh & Seider (2021)**, *Applied
Developmental Science*, ERIC EJ1263074 — the Question Formulation Technique, a
question-brainstorming intervention, quasi-experimental with multiple-group SEM: "Results indicated
a **positive impact of the QFT on students' curiosity**, but a **negative impact on students'
self-regulatory self-efficacy … and cognitive engagement**." `OBSERVED` (quasi-experimental).
Teaching adolescents to generate questions raised curiosity and lowered their sense of being able
to regulate their own learning.

### 3.6 Socratic questioning: the evidence base is close to empty

The brief asks for "Socratic questioning's actual evidence base." Exhaustive retrieval across
OpenAlex and ERIC returns, for education: conceptual essays, law-school pedagogy commentaries,
practitioner descriptions, and a set of asynchronous-discussion-forum studies with self-report or
rubric-coded critical-thinking outcomes. The randomised trials that surface under the term are
**cognitive behavioural therapy** trials, where "Socratic questioning" is a therapist technique.

The one randomised education study retrieved with a standardised outcome — **Lowenstein (2010)**,
ProQuest ED514978, 25 undergraduates randomly assigned to instructor-facilitated Socratic
questioning or traditional responses in online discussion, six discussions, California Critical
Thinking Skills Test pre/post — reports:

> "The findings of the study revealed that **Socratic questioning, compared with traditional
> instructional methods, did not have a statistically significant influence on the critical
> thinking of students** with diverse critical thinking skills. **Frequency of participation also
> was not affected** by Socratic questioning."

`MEASURED-RCT` (null, N = 25 — underpowered, and reported as such).

**No meta-analysis of Socratic questioning as an instructional method was located.** The evidence
usually cited under the label belongs to adjacent, better-measured constructs: prequestions
(g = 0.54 specific), elaborative interrogation and self-explanation, tutorial dialogue in ITSs, and
case comparison (d = 0.50). `OPEN` — see §9.

A 1980 conceptual paper found in the same search makes the point that the whole section has been
converging on, and it is worth stating plainly: analysing the *Meno*, its author concludes
"**curiosity cannot be seen to follow from the questioning methods**. Other factors, including the
felt need to know, may account for curiosity but constitute **preconditions rather than results**
of questioning." That is exactly what the 2024 meta-analysis found forty-four years later: the
question does not manufacture the state; the attempt does, and the attempt is itself something the
learner must be able to initiate.

### 3.7 What to build

`DESIGN` — **the prequestion is a per-knowledge-component instrument, not a lesson opener.**
Because the specific effect is 0.54 and the general effect is 0.04, the correct object is not "one
hooking question per section." It is **one attemptable question per knowledge component the lesson
intends to teach**, each with an immediate correction, each requiring an overt guess (0.65 vs 0.22),
each *factual before conceptual* (0.58 vs 0.28) at first exposure. The artifact does not exist:
no deployed system generates a prequestion per KC, requires the guess, and scores its own coverage
against the lesson's KC list.

**What would show this was the wrong design:** if a cohort receiving one attemptable prequestion per
knowledge component does not outperform a cohort receiving a single engaging opening question on a
posttest **weighted by KC coverage** — that is, if the coverage-specific benefit does not
materialise, then the specific/general distinction does not survive the move from lab lists to real
lesson structure, and the cheaper single-hook design is correct. A second falsifier: if requiring
the overt guess increases session abandonment enough to cancel the 0.65-vs-0.22 gain, the
requirement must be dropped, and the design is wrong in the field regardless of being right in the
meta-analysis.


---

## 4. Executive function — the reframe

### 4.1 The corpus says don't train it. Here is why that is not the interesting half.

The training nulls are settled and are not re-derived here. For the record, three independent
confirmations retrieved this session:

- **Kassai, Futó, Demetrovics & Takács (2019)**, *Psychological Bulletin*, `10.1037/bul0000180`:
  "training a component **did not have a significant effect on the untrained components**
  (g = 0.11, k = 17, **p = .11**). By showing the absence of benefits that generalize beyond the
  trained components, **we question the practical relevance of training specific executive function
  skills in isolation**." `MEASURED-META`.
- **Rapport, Orban, Kofler & Friedman (2013)**, *Clinical Psychology Review*, 25 studies:
  short-term-memory training improved short-term memory (d = 0.63); **training attention did not
  improve attention**, and **training mixed executive functions did not improve the targeted
  executive functions** — both 95% CIs include 0.0. Far transfer to academics and to blinded
  behaviour ratings: non-significant. `MEASURED-META`.
- **Westwood, Parlatini, Rubia, Cortese & Sonuga-Barke (2023)**, *Molecular Psychiatry*, 36 RCTs,
  blinded-outcome subset: ADHD total **SMD 0.12 [−0.01, 0.25]**; inattention 0.17 [0.02, 0.31],
  rising to 0.40 [0.09, 0.71] **only when measured inside the training setting** — "a
  setting-specific effect"; **no effect on attention, inhibition, reading or arithmetic**.
  `MEASURED-META`.

So: externalise. The interesting question is *what*, exactly, to externalise. The literature that
answers it is not the EF-training literature. It is the twenty-five years of intelligent-tutoring
log data that measured, action by action, where a struggling learner's session falls apart.

### 4.2 The Khanmigo diagnosis, quantified — twenty-five years early

The corpus records that Khanmigo's mechanism worked and "only fired when a student recognised they
needed help and went to get it." That is precisely the failure Carnegie Mellon measured in 2000 and
has been publishing about ever since.

From **Aleven, Roll, McLaren & Koedinger (2016)**, "Help Helps, But Only So Much," *IJAIED*
26:205–223, `10.1007/s40593-015-0089-1`, full text recovered, quoted verbatim:

> "Students frequently used the tutor's on-demand help facilities in ways that seemed unlikely to
> help them learn. For example, they often clicked through the hint levels really quickly to get to
> the last level (the 'bottom-out hint'), which gave the answer. That is, **they viewed 68% of the
> hint levels prior to the last for less than 1 second** (Aleven and Koedinger 2001), not enough
> time to read and understand the content. Also, students often appeared reluctant to ask for hints.
> For example, **even after 3 errors on a step, the student's next action was a hint request only
> 34% of the time** (2000). Further, we found a **negative correlation between the frequency with
> which students used the tutor's on-demand help and their learning gains** … the finding also
> suggests that any positive effect on learning from hints is not strong, at least not strong enough
> to offset the selection effect."

`OBSERVED` — educational data mining on Geometry Cognitive Tutor logs, tens of thousands of actions.

> "The finding of widespread ineffective help seeking was at odds with (in retrospect, idealized)
> notions at the time of how learners approach learning with an ITS, for example, that they
> **continuously and carefully monitor their comprehension, seeking help when things are not
> clear**."

That idealised notion is the design assumption inside every conversational tutor shipping today.

### 4.3 And then they fixed it, and learning did not move

This is the result that makes the reframe necessary rather than merely elegant. Carnegie Mellon
built the **Help Tutor** — a model-tracing tutor agent for help-seeking itself, ~80 production
rules, with a taxonomy of maladaptive behaviours (Help Abuse, Help Avoidance, Try-step Abuse),
delivering real-time metacognitive feedback ("Repeated errors may mean that you are not learning …
Perhaps ask for a hint?"). Two classroom studies.

The 2010 *Learning and Instruction* abstract (Roll, Aleven, McLaren & Koedinger,
`10.1016/j.learninstruc.2010.07.004`, Study 1 N = 58, Study 2 N = 67) reports that the Help Tutor
improved help-seeking behaviour and that "the improved help-seeking skills **transferred to learning
new domain-level content** during the month following the intervention, while the help-seeking
support was no longer in effect."

The same authors' 2016 retrospective states it differently, and more starkly:

> "We found that this feedback led to a **lasting improvement in help-seeking behavior, even months
> after the Help Tutor was turned off**. Specifically, students who had received feedback on help
> seeking used the hints more deliberately … **However, we did not find improved domain-level
> learning due to feedback on help seeking.**"
>
> "**The main disappointment was that despite improvement in help-seeking behavior, the Help Tutor
> had no influence on students' domain-level learning outcomes.** It is perhaps worth noting that at
> least one related project found, in a close parallel to our findings, that an intervention aimed
> at improving help seeking had an influence on the targeted learning behaviors but not on
> domain-level learning outcomes (Tai et al. 2013). After years of agonizing and soul searching, we
> have come to view **this null result as interesting and important in its own right**."

`MEASURED-RCT` (null). **Both statements are reported here; the tension between them is real and is
not resolved by the sources.** The 2016 paper is the same team's considered position eleven years
into the programme and is the one this section relies on.

Two further findings from the same paper close the loop:

> "When students have a **medium level of skills**, hints do have beneficial effect on student
> learning within the tutor. Specifically, help use led to better performance on the next
> opportunity to apply the same skill. … When students have a **low or high level of skill, attempts
> at solving (without help) are more effective**." `OBSERVED` (Roll et al. 2014 EDM).

> "principle-based hints during tutored problem solving may aid conceptual learning … For these
> beneficial effects to occur, **students must self-explain the hints or otherwise make sense of
> them, which however cannot be taken for granted**."

**The full diagnosis, then, is two-layered.** Layer one: the learner does not recognise the need
(34%). Layer two: even when they do, the help is a hard piece of domain text that requires a second
executive act — sense-making — to convert into learning, and that act "cannot be taken for granted."
Fixing layer one alone moves behaviour and not learning. That is exactly what happened to Khanmigo,
and it is exactly what the Help Tutor predicted a decade and a half earlier.

### 4.4 The audit: every point in a session where the design assumes an executive function

This is the section's core deliverable. Each row names a moment, the executive function it silently
requires, what products currently assume, and what would supply it externally.

| # | Moment in the session | Executive function silently required | What products assume | External supply | Supporting number |
|---|---|---|---|---|---|
| 1 | **Initiating** | Task initiation; overriding delay aversion | The learner opens the app because they decided to | An **if-then cue bound to an existing routine**, and the session opens *itself* at the cue with the first item already on screen and answerable in one action | Implementation intentions in children **g = 0.31 [0.21, 0.41]**, N = 12,957, stronger in younger children and in ADHD (Breitwieser & Reinelt 2026) |
| 2 | **Choosing what to work on** | Goal setting, prioritisation, resisting the easy option | A menu, a dashboard, a course tree | **No menu.** One next item, selected by the learner model. The choice is made upstream and is not shown | Prior-knowledge spread drives 3.6× of time-to-mastery vs 1.14× for learning rate (corpus K1, Koedinger et al. 2023) |
| 3 | **Holding the goal while working** | Working-memory maintenance of the objective | The learner remembers why they are here | The objective is **rendered continuously**, in the learner's own words, not in curriculum language | Signalling **g = 0.43 [0.35, 0.50]**, k = 209 — an on-screen element that points at the target is the best-evidenced design act available |
| 4 | **Sustaining within a segment** | Sustained attention | Uninterrupted attention for the length of the material | **Instructor-segmented, not learner-segmented**, chunks | Rey et al. 2019: instructor-segmented **g = 0.41 [0.32, 0.50]** vs learner-segmented **g = 0.20 [0.11, 0.28]**, k = 32 each |
| 5 | **Noticing confusion** | Metacognitive monitoring | The learner notices they are lost | **Monitoring is instrumented, not asked.** Latency, error runs, hint-mining pattern, response-time variability | The 34% figure: after three consecutive errors, only a third of learners act. The trigger must therefore be the system's, not the learner's |
| 6 | **Deciding to seek help** | Help-seeking; tolerating the admission of not knowing | A help button, always available, never pressed | **Never a button.** The system *offers* at the measured trigger, and offers **content**, not an invitation to ask | Aleven & Koedinger: help-seeking is the measured bottleneck, and fixing the *request* behaviour did not fix learning |
| 7 | **Making sense of the help** | Self-explanation | The learner reads the hint and integrates it | Help arrives as a **worked step with a required response**, not as text to be read | 68% of hint levels viewed for <1 s; "students must self-explain the hints … which cannot be taken for granted" |
| 8 | **Sustaining across an interruption** | Working memory; prospective memory | The learner holds the thread | An externalised, continuously-written **state card**: current goal, last action, next action, the open question | Segmentation improves learning while *increasing* study time (g = 0.92) — the gap between segments is where state is lost |
| 9 | **Resuming after a break** | Task re-entry, re-orientation | The learner reconstructs where they were from the screen | Resumption is a **re-entry item**, not a screen: one retrieval question about the last thing done, answerable in seconds | Prequestion specific effect **g = 0.54**; retrieval practice **g = 0.51 vs restudy** (corpus B1) |
| 10 | **Self-terminating a wasteful strategy** | Inhibition, set-shifting | The learner notices they are stuck and changes approach | A **wheel-spinning detector** with a forced strategy change, not a hint | Corpus: bottom prerequisite quintile wheel-spins at **50%** vs 10% for the top quintile (Wan & Beck 2015) |
| 11 | **Stopping at the right time** | Self-monitoring of satiation and diminishing return | The learner stops when they feel done | The session **terminates itself** at a measured competence threshold, not at a clock | Corpus K1: ≈7 opportunities to 80% mastery; time-based models "systematically provide poor predictive fit" |
| 12 | **Returning tomorrow** | Prospective memory | A notification, and the learner's intent | The **schedule is the system's job** (FSRS, corpus F11). The learner is never asked to remember a date | Optimal gap = 5–10% of the retention interval (Cepeda et al. 2008) — a computation no learner performs |

`INFERENCE` for the mapping; every number in the right-hand column is `MEASURED-META` or
`OBSERVED` and is sourced above or in the named corpus section.

**Three observations about the table.**

First, **eleven of the twelve supplies are things software can do and a human teacher cannot do at
scale.** This is the constructive core: the machine's comparative advantage over a human tutor is
not explanation quality — it is *never getting tired of supplying executive function*.

Second, **the supplies are not exotic.** Segmentation, signalling, scheduling, retrieval prompts and
if-then cues are the best-evidenced interventions in instructional psychology. What does not exist
is a product that treats them as a **single coherent obligation** rather than as twelve unrelated
features.

Third, **the external-supply literature is directly supportive and honestly bounded.** Metacognitive
prompts in computer-based environments: **Guo (2022)**, *JCAL*, `10.1111/jcal.12650` — "metacognitive
prompts significantly enhanced **SRL activities (g = 0.50 [0.37, 0.63])** and **learning outcomes
(g = 0.40 [0.31, 0.49])** … the effects varied as a function of three prompt features: **feedback,
specificity and adaptability**." `MEASURED-META`. Prompts *do* transfer to learning when they are
specific, adaptive and paired with feedback — which is exactly the difference between the Help
Tutor's generic "perhaps ask for a hint?" and a supplied worked step.

Two bounding results that must be held alongside it:

- **Dignath & Büttner (2008)**, *Metacognition and Learning*, 84 studies / 357 effect sizes, average
  **ES = 0.69** — and, verbatim, "for both school levels, **effect sizes were higher when the
  training was conducted by researchers instead of regular teachers**." `MEASURED-META`. This is the
  fidelity-and-dosage argument the corpus already makes about special education, and it is the
  strongest single argument for a machine: a machine delivers at researcher fidelity on every
  session, to every learner, forever. (Corroborated in online/blended settings: **Xu et al. (2022)**,
  *Behaviour & Information Technology*, ES = 0.69 across elementary through higher education.)
- **Jansen, van Leeuwen, Janssen, Jak & Kester (2019)**, *Educational Research Review*, meta-analytic
  SEM: "**Contrary to popular belief, the results only provide evidence for partial mediation**" —
  SRL activity only partly explains why SRL interventions raise achievement; "other factors, such as
  **task motivation and time on task**, potentially influence the effectiveness." `MEASURED-META`.
  So supplying executive function is not the whole story even where it works, and the honest claim
  is bounded accordingly.

### 4.5 `DESIGN` — the Executive Function Ledger

**The artifact.** A per-session, per-learner record with exactly three columns for each of the
twelve demand points in §4.4: *demanded* (did this session require it), *supplied* (did the system
provide it externally), *unaided* (did the learner have to produce it alone). It emits a single
scalar per session — the **unaided-demand count** — and a per-learner trajectory of that scalar over
time.

**Why it does not exist.** Every instrument in the field measures executive function as a property
of a *person*: BRIEF, CPT, n-back, Stroop, the Tower tasks. There is no instrument anywhere that
scores an **interface** for how much executive function it charges the user. Products publish
engagement, completion, time-on-task and learning gain. None publishes a demand ledger, and no
meta-analysis codes for one, because the construct has never been operationalised on the product
side.

**What it buys.** It makes the reframe falsifiable and it makes the twelve supplies prioritisable.
Right now "reduce cognitive load" and "support self-regulation" are exhortations with no unit. The
unaided-demand count is a unit.

**What would show this was the wrong design.** The ledger is wrong if, across a real cohort, the
**unaided-demand count does not predict session non-completion over and above time-on-task and
prior knowledge**. Those two predictors are already available, cheap, and known to work. If adding
the EF-demand count to a model containing them produces no significant increment in explained
variance in non-completion — and no significant increment in predicting the *next-session return*
rate — then executive-function demand is not a distinct product property, the reframe is decorative,
and the ledger should be abandoned rather than refined.

A second, harder falsifier: if the ledger's count is highly correlated with a simple proxy — number
of screens, number of decisions, or number of clicks per knowledge component — then it is a
complicated way of saying "fewer steps," and the simple proxy should be used instead.

**This is a `DESIGN` claim. It is not a finding and may not be restated as one.** Nothing in §4.4 or
§4.5 asserts that supplying executive function externally *does* improve learning. What is measured
is: the demands exist and are unmet (34%, 68%); repairing one of them in isolation moved behaviour
and not learning (the Help Tutor null); and adaptive, specific, feedback-paired prompts move both
(g = 0.50 / g = 0.40). The ledger is a proposal for finding out whether the twelve together do what
the one alone did not.


---

## 5. ADHD, specifically and carefully

**Standing constraint, restated before anything else.** Per `CLAUDE.md` §3, an AI may not diagnose
or label a child. Nothing in this section is a screening instrument, a diagnostic aid, or a basis
for assigning a child to a category. Everything below describes **a measured profile that some
learners have**, so that a system can be designed to serve it **without ever needing to identify who
has it**. The design consequences in §5.7 are deliberately constructed from *observable task states*
— error runs, response latency, response-time variability, time-to-first-action — which are
properties of the interaction, not inferences about the person.

### 5.1 What is actually measured

**Executive function.** **Willcutt, Doyle, Nigg, Faraone & Pennington (2005)**, *Biological
Psychiatry*, `10.1016/j.biopsych.2005.02.006`: 83 studies, ADHD N = 3,734 vs non-ADHD N = 2,969.
Verbatim: "Effect sizes for all measures fell in the medium range (**.46–.69**), but the strongest
and most consistent effects were obtained on measures of **response inhibition, vigilance, working
memory, and planning**." And the authors' own conclusion: the "moderate effect sizes and lack of
universality of EF deficits … suggest that **EF weaknesses are neither necessary nor sufficient**."
`MEASURED-META`. Domain-by-domain effect sizes are **UNVERIFIED** — the paper is closed access
(Unpaywall `is_oa: false`); only the .46–.69 range is source-verified here.

**Response-time variability — the most robust signal, and non-specific.** **Kofler, Rapport,
Sarver, Raiker, Orban, Friedman & Kolomeyer (2013)**, *Clinical Psychology Review*,
`10.1016/j.cpr.2013.06.001`, **319 studies**, corrected for measurement unreliability and
publication bias: children/adolescents **Hedges' g = 0.76**; adults **g = 0.46**. Psychostimulants
attenuate it (**g = −0.74**) and it is "**unaffected by non-stimulant medical and psychosocial
interventions**." Critically: "Individuals with ADHD did **not** evince slower processing speed
(mean RT) after accounting for RT variability, whereas large magnitude RT variability deficits
remained after accounting for mean RT." And: adolescents/adults with ADHD were **indistinguishable
from clinical controls**; children only **g = 0.25** vs clinical controls. `MEASURED-META`.

Read carefully, that last clause matters enormously for a SELPA-serving product: **RT variability
separates ADHD from typical development and does not separate it from other clinical
presentations.** It is a good design signal and a bad diagnostic one — which is precisely the
combination this project needs.

### 5.2 The sustaining myth, falsified

This is the finding that should change how a product is built, and it contradicts the folk model
that underlies nearly every "shorter lessons for shorter attention spans" design.

**Huang-Pollock, Karalunas, Tam & Moore (2012)**, *Journal of Abnormal Psychology*,
`10.1037/a0027205`, PMC3664643 — 47 between-group continuous-performance-test studies.

**Overall performance** (the deficit that is definitely there):

| Measure | k | N | δ | 80% credibility interval |
|---|---|---|---|---|
| Omission errors | 39 | 3,192 | **1.34** (SD 0.28) | 0.98 – 1.69 |
| Commission errors | 33 | 3,165 | **0.98** (0.27) | 0.63 – 1.32 |
| Reaction time | 26 | 1,342 | 0.61 (0.73) | −0.33 – 1.55 |
| SD of reaction time | 16 | 930 | 0.93 (0.38) | 0.45 – 1.41 |

**Performance over time — the vigilance decrement** (the deficit the folk model assumes):

| Measure | k | N | δ | 80% credibility interval |
|---|---|---|---|---|
| Omission errors | 7 | 488 | **0.54** (0.53) | **−0.14 – 1.22** *(crosses zero)* |
| Commission errors | 5 | 431 | **0.24** | — |
| Reaction time | 5 | 338 | **0.27** | — |
| SD of reaction time | 4 | 299 | **0.22** | — |

**The mechanism**, from signal-detection and diffusion modelling in the same paper: perceptual
sensitivity **d′ = 2.68 (0.89) in ADHD vs 3.57 (0.93) in controls, d = 0.98, p < .001**; drift rate
**v = 0.18 (0.11) vs 0.28 (0.16), d = 0.75, p = .001**; **response bias ln β: d = 0.04, n.s.**

`MEASURED-META`. **The impairment is present from the first block, in the rate at which evidence
accumulates from each stimulus — not in a steeper decline across time.** The decrement effects are
a quarter to a third the size of the overall effects and the largest one's interval includes zero.

**Design consequence.** `INFERENCE`, and it is the most actionable inference in the section:
**"short attention span" is the wrong design target. "Lower signal-to-noise per opportunity" is the
right one.** Do not shorten the lesson. Raise the discriminability of each item — signalling
(g = 0.43), contiguity (g = 0.63–0.78), removing competing referents (§1) — and increase the
*number* of opportunities, since acquisition is counted in opportunities (corpus K1: ≈7 to 80%
mastery) and each one is worth less to this learner than to the next one.

### 5.3 Delay is the largest clean effect

**Jackson & MacKillop (2016)**, *Biological Psychiatry: CNNI*, `10.1016/j.bpsc.2016.01.007`: 21
investigations, 25 case-control comparisons, **N = 3,913**, delay discounting **d = 0.43,
p < 10⁻¹⁵**. No moderation by age (<18 vs >18), by real vs hypothetical reward, or by comorbid
conduct/oppositional disorder. Minimal heterogeneity, minimal publication bias. `MEASURED-META`.

**Patros, Alderson, Kasper, Tarle, Lea & Hudec (2016)**, *Clinical Psychology Review*,
`10.1016/j.cpr.2015.11.001`: 28 tasks / 26 studies, **N = 4,320** (2,360 ADHD, 1,960 typically
developing), choice impulsivity **g = .47**. `MEASURED-META`.

**Marco et al. (2009)**, *Neuropsychology*, `10.1037/a0014914`: 360 ADHD probands, 349 siblings, 112
controls — the smaller-sooner preference was elevated in ADHD under both conditions **and larger
when the smaller-sooner choice reduced total trial delay**, which is the design signature that
separates *delay aversion* from *pure impulsive drive*. `MEASURED-BENCH`.

**Design consequence.** The interval between an action and its payoff is a design parameter, and it
carries the cleanest, largest, most replicated effect in this literature. Every architectural choice
that lengthens that interval — batching feedback, end-of-unit grading, deferred results — is a
tax levied specifically on this population, at d ≈ 0.43–0.47.

### 5.4 Does high-interest material normalise performance? The precise answer.

**Dovis, Van der Oord, Wiers & Prins (2012)**, *Journal of Abnormal Child Psychology*,
`10.1007/s10802-011-9601-8`, PMC3375007: 30 children with ADHD vs 31 controls on a visuospatial
working-memory task under four reinforcement conditions — feedback-only, €1, €10, and a computer-game
condition. Verbatim:

> "In the Feedback-only condition, children with ADHD performed worse … Although incentives
> significantly improved the WM performance of children with ADHD, **even the strongest incentives
> (10 euros and Gaming) were unable to normalize their performance** … **Only children with ADHD
> showed a decrease in performance over time. Importantly, the strongest incentives (10 euros and
> Gaming) normalized persistence of performance in these children**, whereas 1 euro had no such
> effect."

`MEASURED-RCT`. This is the single most precise answer to the "make it engaging" question in the
ADHD context, and it splits the outcome in two:

- **Level of performance: not normalised, by any incentive tested.**
- **Persistence within the session: normalised, but only by the strongest incentives.** €1 did
  nothing. The dose mattered.

Set alongside the corpus's gamification finding — Sailer & Homner (2020): cognitive g = .49,
motivational g = .36, **behavioural g = .25 [.04, .46]**, the weakest cell; moderators are game
fiction and social interaction, not points/badges/leaderboards; and 128 experiments show tangible
expected performance-contingent rewards undermine intrinsic motivation — the design reading is
sharp: **the legitimate target of a game layer is within-session persistence, not accuracy and not
motivation.** And it must not be a tangible expected performance-contingent reward, which is the
only kind Dovis actually tested. That tension is real and unresolved: the manipulation with the
measured persistence benefit is the manipulation the motivation literature warns against.
`INFERENCE`.

The weaker cousin of this claim should be marked down. **Optimal stimulation theory** — Antrop,
Roeyers, Van Oost & Buysse (2000), *JCPP* — is often cited for "novelty normalises ADHD behaviour."
The authors' own 2002 re-analysis states that in the original study "confirmation for this
hypothesis was only found for **2 of 25 target behaviors**." `OBSERVED`, weak, and should not be
carried as support.

### 5.5 The dissociation that defines the opportunity: throughput vs accuracy

Medication is the best-evidenced intervention in this space. What it buys is very specific.

**Symptom ratings.** Cerrillo-Urbina et al. (2018), *J Child Adolesc Psychopharmacol*, 15 RCTs,
N = 4,648: ADHD-RS-IV **SMD −0.70 [−0.85, −0.55]**; stimulants **−0.83 [−1.11, −0.54]**. Note for
calibration that the **placebo arm itself was SMD −0.68 [−0.82, −0.54]**. `MEASURED-META`.

**Academic outcomes.** **Kortekaas-Rijlaarsdam, Luman, Sonuga-Barke & Oosterlaan (2019)**, *European
Child & Adolescent Psychiatry*, `10.1007/s00787-018-1106-3`, 34 studies: methylphenidate improved
**math productivity +7.8%, p < .001**; **math accuracy +3.0%, p = .001**; **reading speed SMD .47,
p < .001**; **reading accuracy: not significant.** The authors' summary: "Academic improvements were
**small compared to symptom improvements**; qualitative changes limited to math." `MEASURED-META`.

**Prasad, Brogan, Mulvaney, Grainge, Stanton & Sayal (2013)**, *European Child & Adolescent
Psychiatry*, 43 studies, pooled N = 2,110: work *completed* up by **up to 15%**; on-task time up by
**up to 14%**; accuracy improved "less consistently." **Atomoxetine (2 studies): no significant
effect.** `MEASURED-META`.

**This is the design opportunity, stated plainly.** The best pharmacological intervention available
buys **throughput** — more work done, more time on task — and buys **accuracy** barely at all
(+3.0% in math, nothing in reading). A learning system's job is the accuracy half: the correctness
of the next opportunity, the immediacy of its correction, the discriminability of its signal. That
is the half medication does not deliver, and it is the half §5.2 identifies as the actual deficit.
`INFERENCE`.

### 5.6 Which accommodations have evidence, and which are folklore

The corpus already records the general finding: testing accommodations are **legally mandated and
evidentially weak** — Kieffer, Lesaux, Rivera & Francis (2009), overall **g = .034, p = .180**;
Rios, Ihlenfeldt & Chavez (2020), 26 studies / 95 effect sizes / **N = 11,069**, overall +0.16 SD
with none statistically different from zero. Both halves are held here without softening either.

The ADHD-specific picture, retrieved this session, is sharper.

**The systematic review.** **Lovett & Nelson (2021)**, *JAACAP*, `10.1016/j.jaac.2020.07.891`, 510
documents screened, 68 included, verbatim:

> "**most accommodations fail to show evidence of benefits that are specific to students with ADHD,
> and many of the more common accommodations have few or no experimental studies supporting them.
> An exception is read-aloud accommodations, which have two randomized experiments finding specific
> benefits for younger students with ADHD.**"

`MEASURED-META`. The authors recommend clinicians "be hesitant to recommend accommodations
immediately after a diagnosis."

**Extended time — three independent failures.**

- **Lewandowski, Lovett, Parolin, Gordon & Codding (2007)**, *J Psychoeducational Assessment*,
  grades 5–7, time-and-a-half on mathematics: "**The results did not support the differential boost
  hypothesis in that the ADHD group did not make more gains than the control group with extended
  time**," despite the ADHD group having lower processing speed and math fluency. `MEASURED-RCT`
  (null).
- **Miller, Lewandowski & Antshel (2015)**, *J Attention Disorders*, `10.1177/1087054713483308`, 38
  college students with ADHD vs 38 matched controls on the Nelson-Denny under standard / 1.5× / 2×
  time: "**Groups did not differ in the number of items attempted or correctly answered at standard
  time, time and one half, or double time.**" Authors conclude extended time is "not specific and
  perhaps not necessary." `MEASURED-RCT` (null).
- **Lovett & Leja (2015)**, *J Attention Disorders*, `10.1177/1087054713510560`: "**Students
  reporting more symptoms of ADHD and executive functioning deficits actually benefited LESS from
  extended time**, and students' perceptions of their timing needs did not predict benefit."
  `MEASURED-RCT` (negative direction).

No ADHD-specific meta-analysis of extended time was located. Gregg & Nelson (2012), *J Learning
Disabilities*, meta-analysed extra time for transitioning adolescents with **learning disabilities**
and concluded the results "raised **more questions than answers**." The first purpose-built RCT is
only now running — Malcon et al. (2026), *JMIR Research Protocols*, `10.2196/80271`, NCT06063382,
103 enrolled, 25% vs 50% extra time — **with no results yet**. `OBSERVED`.

**The constructive move.** The one accommodation in this space with a differential-boost finding —
**read-aloud, two randomised experiments, younger students** (Spiel, Mixon, Holdaway, Evans,
Harrison, Zoromski & Yost 2016, *Remedial and Special Education*, n = 36; Spiel, Evans & Harrison
2019, *J Applied School Psychology*, n = 45, grades 5–6, randomised; exact effect sizes **UNVERIFIED**
from ERIC abstracts) — is **the one a machine supplies for free, universally, to everyone, with no
eligibility determination and no stigma**. That is the curb-cut argument in its cleanest form: the
accommodation with evidence is the accommodation software gives away.

**Task initiation.** **Breitwieser & Reinelt (2026)**, *British Journal of Psychology*,
`10.1111/bjop.70065`, a **registered-report** meta-analysis: 52 effect sizes from 42 studies,
**N = 12,957**, mean age 10.67, spanning 1975–2025. **Hedges' g = 0.31 [0.21, 0.41]**;
Q(51) = 146.47, p < .001, I² = 65.2%. "The effects were **stronger in studies with younger children
and (in some analyses) children with ADHD**, suggesting that implementation intentions are
**particularly effective when self-regulation abilities are limited**." `MEASURED-META`. This is
the best-evidenced task-initiation lever available and it is the warrant for §4.4 row 1. Primary
ADHD studies exist (Gawrilow & Gollwitzer 2008, `10.1007/s10608-007-9150-1`; Gawrilow, Gollwitzer &
Oettingen 2011 ×2; Gawrilow et al. 2013) but their **effect sizes are UNVERIFIED** — Springer
deposited no abstracts for that era and no OA copies were reachable.

**Body doubling.** Widely practised, entirely unmeasured. Exhaustive retrieval returns exactly two
academic sources, both the same 220-person descriptive survey with no control condition, no task
measure and no effect size — **Eagle, Baltaxe-Admony & Ringland (2023)**, ASSETS '23,
`10.1145/3597638.3614486`, which states outright that "**no academic exploration exists on the
topic**," and its 2024 *ACM TACCESS* extension, `10.1145/3689648`. Europe PMC `TITLE:"body doubling"`
returns **0 results**. Reported honestly: this is a community practice with **zero controlled
outcome data**. Folklore in the evidentiary sense, which is not the same as false. `OPEN` — see §9.

**Exercise.** The best-replicated finding is acute, not chronic: **Xu, Zhao & Hu (2026)**,
*Psychology of Sport and Exercise*, `10.1016/j.psychsport.2026.103088` — acute exercise on
inhibitory control **Hedges' g = 0.55 [0.32, 0.79], p < 0.001**; core symptoms **g = 0.23 [0.03,
0.43], p = 0.024**; chronic exercise "mixed results." In children: working memory **SMD 0.51 [0.34,
0.69]** (Cheng, Song & Hong 2025, 11 studies, N = 667); cognitive flexibility **SMD 0.70 [0.09,
1.31]** but **inhibition switching SMD −0.35 [−0.74, 0.03], crossing zero** (Li et al. 2025, 19
studies); and a flat null on executive functioning across neurodevelopmental disorders —
**g = 0.492, p = 0.215, 95% CI [−0.286, 1.269]** (Carcelén-Fraile et al. 2025, 16 RCTs).
`MEASURED-META`, heterogeneous and mutually inconsistent. A movement break before a hard segment has
the best-replicated number in this space and costs nothing; the chronic-training claims should not
be carried.

### 5.7 The non-diagnostic route

Everything above describes a profile. The system must serve the profile **without assigning it**.
That is technically possible because every design trigger in §4.4 is defined on an **observable task
state**, not on an inference about the child:

| Design trigger | What it observes | What it does **not** claim |
|---|---|---|
| Three-error run → offer worked step | A sequence of responses in this session | That the learner has an attention disorder |
| Response-time variability above the learner's own rolling baseline → shorten the current opportunity's evidence demand | Within-learner variance | That variability indicates a diagnosis (it does not — g = 0.25 vs clinical controls) |
| Time-to-first-action beyond threshold → fire the if-then cue and pre-load the first item | Latency at session start | That the learner has a task-initiation deficit |
| Hint dwell-time < 1 s → replace text hint with required-response step | Dwell time | Anything about the person |
| Wheel-spinning signature → forced strategy change | Opportunity count without accuracy gain | Anything about the person |

`DESIGN`. **What would show this was the wrong design:** if these five triggers, applied
universally, produce **worse** outcomes for learners without the profile than a non-triggered
baseline — that is, if universal application of profile-derived design costs the majority anything
measurable — then the curb-cut assumption fails here and the triggers must be gated, which
reintroduces exactly the eligibility determination this design exists to avoid. That is a real
possible outcome and it is the falsifier that matters most, because the entire SELPA-first argument
in this project rests on the curb-cut holding.


---

## 6. The pacing question — "not super-slow classes"

### 6.1 What the corpus already prices

From K1: acquisition compresses **10–40× on elapsed calendar** and **3–5× on engaged effort**;
durability compresses **1×**; procedural skill compresses **1×**. Acquisition is counted in
**opportunities**, not minutes (≈7 to 80% mastery of a knowledge component, median 6.54); the
dominant source of time variance is **prerequisite state (3.6×)**, not learner speed (1.14×); and a
time-based model of learning "systematically provides poor predictive fit."

The owner's instinct is therefore correct about the target and wrong about the lever. **The slowness
of a slow class is not caused by the pace of delivery.** It is caused by delivering opportunities
that are wrong for the learner's prerequisite state, which is a 3.6× tax, and by the fact that most
of an allocated hour is not encoding at all (corpus K1: 4 minutes vs 52 minutes of productive
learning time inside the same allocated day).

### 6.2 The finding the owner will not expect

Going faster and **handing the pace to the learner** are different things, and the second one is
measured, and it is not good news for the EF-constrained learner.

- **Multimedia design principles are worth more when the system paces than when the learner does:**
  **g = 0.41 [0.33, 0.49] system-paced vs g = 0.27 [0.19, 0.35] learner-paced**, p = .02
  (Noetel et al. 2021, 22 pooled effects). Sundararajan & Adesope independently list *learner
  pacing* among the significant moderators of the seductive-details effect.
- **Instructor-segmented content beats learner-segmented content by more than 2×:**
  **g = 0.41 [0.32, 0.50] vs g = 0.20 [0.11, 0.28]**, k = 32 each (Rey et al. 2019), "presumably
  because instructors can more easily ensure that the chunks are meaningful and appropriately
  sized."
- **Prequestions worked better under experimenter-paced than self-paced study** (St. Hilaire et al.
  2024, ps < .05 for both specific and general effects), and the general effect grew with **more**
  study time per unit of material (reading-speed regression β = −0.004, p = .005).
- **Segmented content takes longer to study and teaches better:** **g = 0.92 [0.82, 1.02], k = 19**
  on time taken (Rey et al. 2019) — "suggesting they used time between segments to consolidate."

`MEASURED-META` throughout.

Noetel et al.'s explanation of the pacing moderator is the operative one: "when self-paced, learners
can more easily use their **own strategies** to manage high levels of cognitive load." That is
exactly the resource §4 says the struggling learner does not have. **Learner-paced is not faster. It
is a design that offloads the load-management problem onto the learner's executive function.**

### 6.3 The two clocks that must not be conflated

| | **Clock A — acquisition** | **Clock B — durability** |
|---|---|---|
| Unit | Opportunities, correctly targeted | Elapsed days |
| What compresses it | Correct prerequisite diagnosis; opportunity delivery rate; immediacy of feedback | **Nothing** |
| Measured compression | **3–5× on effort, 10–40× on calendar** (corpus K1) | **1×** |
| Governing number | ≈7 opportunities to 80% mastery; prior-knowledge spread 3.6× | Optimal gap = **5–10% of the retention interval** (Cepeda et al. 2008, N > 1,350) |
| Whose job | The learner's — this is where effort goes | **The system's** — the learner should never compute a schedule |
| Honest sales claim | "A week's understanding in an hour" | "A year's retention costs a month of calendar and about forty minutes of extra effort" |

Corpus K1 supplies both right-hand columns. The contribution here is the insistence that they are
**two different products** and that conflating them is the standard failure of every "learn X in a
weekend" claim.

### 6.4 `DESIGN` — the two-clock zero-to-hero plan

**The artifact.** A learning plan that runs two schedules with different owners and different units,
and that reports them separately to the learner:

1. **Clock A, front-loaded and system-paced.** Diagnose prerequisites first (the 3.6× term).
   Deliver correctly-difficult opportunities at the maximum rate the learner's
   read–attempt–feedback loop supports. Instructor-segmented, not learner-segmented. One
   attemptable prequestion per knowledge component (§3.7). Terminate on measured competence, not on
   a clock. **Target: functional competence in days.**
2. **Clock B, deferred, thin, and never the learner's responsibility.** Consolidation runs on
   calendar at 5–10% of the retention interval, scheduled by the system (FSRS, corpus F11),
   costing the learner minutes per session. **The learner is never asked to decide when to
   review.**
3. **Two separate progress reports.** "You can now do X" (Clock A) and "You will still be able to do
   X in ninety days if you complete N minutes across M days" (Clock B). Products currently report
   one number and imply both.

**What the learner has to accept in exchange for the speed.** Three things, all measured:

- **In-session performance will be worse.** Schwartz, Chase, Oppezzo & Chin (2011): the
  contrasting-cases group did **worse on the in-lesson worksheet (84.7% vs 91.8%, F(1,113) = 4.5,
  p = .037)** and better on delayed transfer (**d = .33**). Segmentation *increases* study time
  (g = 0.92). The fast curve feels slower and worse from inside it.
- **Procedural and motor skill does not compress at all** (corpus, 1×). Anything with a fluency or
  motor component runs on its own clock regardless of how well the conceptual material is
  compressed.
- **The fast curve is a comprehension curve.** Selling it as a retention curve is the specific
  dishonesty this design exists to prevent.

**What would show this was the wrong design.** Two falsifiers, and the first is decisive:

- **It is the wrong design if learners on the compressed Clock-A schedule with system-run Clock B
  show worse 90-day retention than learners on a conventional distributed schedule *at matched
  total effort*.** If durability degrades under compression once effort is held constant, then Clock
  A is borrowing from Clock B, the separation is false, and the compression is not free.
- **It is also the wrong design if compressed acquisition with deferred consolidation produces
  higher dropout than a slower uniform schedule.** A plan that is correct in the lab and produces
  abandonment in the field is wrong, and the correct object is then the slower one. Note that this
  falsifier is more likely to fire for the EF-constrained learner than for anyone else — an intense
  front-loaded phase makes the largest single demand on task initiation and sustained effort in the
  whole design.

**`DESIGN` claim; not a finding.** Nothing here asserts that the two-clock plan produces better
outcomes. What is measured is the compression asymmetry (K1), the pacing and segmentation
moderators (§6.2), and the in-session cost of the desirable difficulties it recommends (§6.4). The
plan is a proposal for testing whether the asymmetry survives being built into a product.

---

## 7. Intuition formation

### 7.1 An operational definition, since the word is doing real work in this project

The brief asks for a definition "rather than gesturally." Here is one, constructed so that every
clause names a measurement:

> **A learner has intuition in a domain when, on *novel* instances, they can (a) classify by deep
> structure rather than surface features, (b) do so *fluently* — correctly within a time gate, not
> merely eventually, (c) judge legality or plausibility *without executing the procedure*, and (d)
> generate a correct expectation before the answer is revealed, and be surprised in the right
> places.**

Each clause is measurable and each has a source:

- **(a) Deep-structure classification.** Chi, Feltovich & Glaser (1981), *Cognitive Science*,
  `10.1207/s15516709cog0502_2` — the founding demonstration that experts sort physics problems by
  underlying principle and novices by literal surface features. The **exact sorting data are
  UNVERIFIED**; no open-access copy exists and Wiley returns 403. The construct is standard; the
  numbers are not quoted here.
- **(b) Fluency, not just accuracy.** Krasne, Hillman, Kellman & Drake (2013), *J Pathology
  Informatics*, `10.4103/2153-3539.123991`: on a skin-histopathology perceptual learning module,
  **raw accuracy declined at the 6–7 week delay while "Score" — correct *within 12 seconds* — did
  not.** Fluency is the thing that retains. `MEASURED-RCT`.
- **(c) Judging without executing.** Kellman, Massey & Son (2010), *Topics in Cognitive Science*,
  `10.1111/j.1756-8765.2009.01053.x`: the Algebraic Transformations PLM trained learners only to
  *recognise which transformations were legal*. Learners never solved equations. Pretest solving
  accuracy was already ~80% but took **~28 s per problem**; after the module, **~12 s per problem**,
  "fully preserved after a two-week delay." N = 30, 8th–9th graders, two 40-minute sessions.
  `MEASURED-RCT`.
- **(d) Expectation and calibrated surprise.** Theobald & Brod (2022), *Psychonomic Bulletin &
  Review*, `10.3758/s13423-022-02124-x` — see §7.5.

**The instrument this definition names: a timed classification test on untrained instances.**
Nothing in it asks the learner to report a feeling. That is the point — "intuition" as normally used
is a phenomenological report, and the phenomenological report is not what transfers.

### 7.2 Many varied instances, under a classification-only regime

This is the strongest-evidenced generator of the thing defined above, and it is almost entirely
absent from commercial learning products.

**Kellman, Massey & Son (2010)**, three studies, full text via NCBI efetch (PMC6124488):

- **MultiRep PLM** — N = 68, 9th–10th graders, two sessions × 60 mapping trials. No pretest
  difference (t(67) = 1.11, p = .27); **test × condition interaction F(1,66) = 21.17**. The control
  group practised **the exact posttest task** (32 generation problems with answer keys). The PLM
  group, which never generated a graph or an equation, still beat them.
- **Algebraic Transformations PLM** — the ~28 s → ~12 s result above.
- **Linear Measurement PLM** — N = 63 6th graders against 78 uninstructed 7th/8th graders, on a
  44-point assessment in which "virtually all items were transfer items": **F(2,138) = 19.687,
  p < .001**, with 6th graders scoring "nearly identical" at a **four-month** delayed posttest.
  Before instruction, the 6th graders scored the same as students two years further through the
  curriculum — i.e. two years of ordinary schooling had moved this competence not at all.

`MEASURED-RCT`. **Krasne et al. (2013)**: 261 images, 8 categories, 12 s target response time,
category retired after 3 consecutive correct-within-time; **median completion 17.5 min (2011 cohort)
and 11.5 min (2012)**; test items were **unseen exemplars**; effect sizes on Score **0.8–1.6,
P < 0.0001** at 6–7 weeks.

**Ahmad, Ashraf, Kellman, Krasne & Ramanathan (2021)**, `10.21203/rs.3.rs-806381/v1` — a randomised
comparison of an ophthalmology PALM against a narrated video lecture, **N = 83**, five optic-nerve
findings, mastery = 3 consecutive correct within 8 s. Pre → immediate post: PALM **accuracy
d = 2.94, fluency d = 3.39**; lecture **d = 2.32 / d = 1.06**. **At one month: PALM accuracy
d = 0.89 and fluency d = 1.16 (P < 0.001); the lecture retained accuracy only (d = 0.44, P = 0.02)
and did not retain fluency.** `MEASURED-RCT`.

**Kellman, Krasne, Massey & Mettler (2023)**, CogSci, escholarship qt83z22046 — a skin-cancer PALM
with 10 confusable lesion categories and four adaptive scheduling conditions plus a
conventional-instruction control. Efficiency: condition **F(4,90) = 13.977, p < .001, ηp² = .383**,
with every adaptive-vs-control comparison at **Cohen's d 2.24–2.53** immediate and **2.32–2.68**
delayed. Accuracy: **F(4,90) = 44.098, p < .001, ηp² = .662**, ds **2.66–2.97 / 2.45–3.16**.

And the useful **null inside it**: signal-detection-based *retirement criteria* mattered
(**F(1,72) = 4.861, p = .031, ηp² = .063**) while signal-detection-based *sequencing* did **not**
(**F(1,72) = 0.44, p = .509, ηp² = .006**; t(78) = 0.625, p = .534). **The mechanism is mastery
gating, not clever ordering.** `MEASURED-RCT`.

### 7.3 Comparison of two cases

**Alfieri, Nokes-Malach & Schunn (2013)**, *Educational Psychologist*, `10.1080/00461520.2013.775712`:
**57 experiments, 336 tests**, random-effects **d = .50 [.44, .56]**. Only **4 of 15 moderators**
were reliable: the comparison objective being **finding similarities**; the principle presented
**after** the comparison; **perceptual** content; and a **short** lag to test. `MEASURED-META`.

**Gentner, Loewenstein & Thompson (2003)**, *JEP* 95(2):393–408, `10.1037/0022-0663.95.2.393`:
Exp 1, N = 64 — **47%** of the guided-analogy group produced the target structure vs **6%** of
baseline, χ²(1, N = 64) = 9.06, p < .01. Exp 2, N = 128 — comparing two cases gave **48% vs 19%**
transfer against studying them separately, χ²(1, N = 128) = 11.85, p < .01; full schema articulated
**42% vs 13%**, χ²(2, N = 128) = 15.64, p < .01. Exp 3, live dyads — contingent contracts formed by
**90%** guided-analogy, **70%** comparison, **55%** separate study, **37%** baseline. `MEASURED-RCT`.

Note the ordering constraint from Alfieri: **principle after comparison.** That is the same shape as
productive failure and prequestions — the generative attempt precedes the formalism.

### 7.4 Contrasting cases before instruction — and its boundary

**Schwartz, Chase, Oppezzo & Chin (2011)**, *Journal of Educational Psychology* 103(4):759–775,
`10.1037/a0025140`:

- **Exp 1, N = 128 8th graders.** Deep-structure recall **F(1,120) = 11.0, p = .001, d = .30**;
  **surface-feature recall null, F(1,120) = 1.5, p = .223, d = .11**; interaction F(1,120) = 11.9,
  p < .001. Immediate transfer **F(1,94) = 6.8, p = .011, d = .27**; **delayed transfer at three
  weeks F(1,124) = 13.6, p < .001, d = .33**, means **35.2% vs 13.8%**. **Word-problem computation:
  null, F(1,124) = 1.7, p = .20.** Students who used ratios ranked stiffness correctly **96%** of
  the time vs **1%** for non-ratio users, χ²(1, N = 126) = 113.7, p < .001.
- **Exp 2, N = 120.** Deep-structure recall d = .28; transfer **d = .31**; **word problems null,
  d = .04, p = .65**; no treatment × achievement interaction (p = .67). **And the invention group
  did worse in-lesson: 84.7% vs 91.8%, F(1,113) = 4.5, p = .037.**

`MEASURED-RCT`. The selectivity is the finding: **structure and transfer move; surface memory and
procedural computation do not; and in-lesson performance goes down.**

The boundary conditions are real and should not be smoothed:

- **Glogger-Frey, Treier & Renkl (2022)**, *Instructional Science*, `10.1007/s11251-022-09577-6`,
  N = 45: the **worked-example group clearly outperformed the inventing-with-contrasting-cases group
  on transfer, BF₊₀ > 313**. `MEASURED-RCT` (reversal).
- **Sinha & Kapur (2021)**: effect sizes favoured **instruction-first for grades 2–5** and for
  domain-general skills (§3.5). The conceptual-knowledge and transfer sub-cells are **UNVERIFIED** —
  SAGE and the ETH repository both returned 403.

### 7.5 Prediction before reveal — a router, not an amplifier

The brief lists prediction-before-reveal as a candidate. The measured answer is more interesting
than the candidate.

- **Bertsch et al. (2007)** generation-effect meta-analysis: **d = .40** overall (86 studies, 445
  effect sizes, N = 17,711); **incidental learning d = .65 vs intentional d = .32**; **anagram
  generation reverses at d = −.05** across 18 studies and >1,000 subjects. `MEASURED-META`.
- **Brod & Breitwieser (2019)**, *npj Science of Learning*, `10.1038/s41539-019-0056-y`, N = 29:
  predicting rather than generating an example raised the share of high-curiosity facts (55.55% vs
  46.43%, t(28) = 1.78, p = .043, **d = .330**), raised curiosity ratings (d = .411) and raised
  anticipation-phase pupil dilation (d = .417) — **and memory was flat: 60.42% vs 59.52%,
  t(28) = 0.41, p = .682, d = .077.** `MEASURED-RCT` (null on the outcome that matters).
- **Theobald & Brod (2022)**, `10.3758/s13423-022-02124-x`, Exp 1 N = 23 / Exp 2 N = 28: **no main
  effect of prediction vs postdiction (b = −0.090, p = .330)**, but a **condition ×
  expectancy-violation interaction, b = 0.195, SE = 0.062, p = .002** — prediction produced a
  U-shaped memory curve (quadratic b = 0.044, p = .012) while postdiction decayed linearly with
  unexpectedness (b = −0.254, p < .001). `MEASURED-RCT`.

**Prediction does not raise average memory. It reallocates memory to the cases that violate
expectation.** For intuition formation that is exactly the right property — the boundary cases are
where deep structure lives — and it is exactly not the property claimed when "predict before you
look" is sold as a memory technique.

### 7.6 Interleaving — a discrimination tool, not a general one

**Brunmair & Richter (2019)**, *Psychological Bulletin* 145(11), `10.1037/bul0000209`: **59 studies,
238 effect sizes, 158 samples**, overall **Hedges' g = 0.42**. By material:

| Material | g |
|---|---|
| Paintings (artist style) | **0.67** |
| Mathematical tasks | **0.34** |
| Expository texts | **n.s.** |
| Tastes | **n.s.** |
| **Words** | **−0.39 — blocking wins** |

Metaregression: interleaving is stronger with **higher between-category similarity**, **lower
within-category similarity**, and **more complex** material. `MEASURED-META`.

That moderator profile is the perceptual-discrimination profile exactly. **Interleave confusable
categories; do not interleave a syllabus.**

Null in the same space: **Nemeth, Werker, Arend, Vogel & Lipowsky (2019)**, *Frontiers in
Psychology* 10:86, `10.3389/fpsyg.2019.00086`, N = 233 — interleaved vs blocked practice of
subtraction strategies: adaptive use of the stepwise strategy showed **no group effect
(F(1,193) = 0.13, p = .72, ηp² = .00)** and **no group × time interaction (F(2.88, 555.96) = 0.13,
p = .94)**; interleaved students' adaptive algorithm use **declined** from T3 to T4 (p = .02,
d = −0.26). `MEASURED-RCT`.

### 7.7 Gesture as representational compression

The corpus's finding that **gesture beat action on objects for transfer** is confirmed at full
precision. **Novack, Congdon, Hemani-Lopez & Goldin-Meadow (2014)**, *Psychological Science* 25(4),
`10.1177/0956797613518351`, PMC3984351, **N = 142 third-graders**:

- **Trained problems: no condition effect.** Action β = −0.22, z = −0.41, p = .68; concrete gesture
  β = 0.71, z = 1.27, p = .20 (abstract gesture as baseline).
- **Near transfer:** action worse than abstract gesture, **β = −1.58, z = −1.97, p = .049**;
  concrete vs abstract **null (β = −0.031, p = .962)**; concrete beat action β = 1.55, p = .04.
- **Far transfer:** action vs abstract gesture **β = −2.06, z = −2.30, p = .02**; concrete vs
  abstract marginal (β = −1.15, p = .09).
- Parroted-strategy × success correlation: concrete gesture **R = .76**, abstract **R = .64** (both
  p < .001), **action R = .25, p = .17**.

`MEASURED-RCT`. **Equal training performance; ordered transfer.** The abstraction of the movement,
not the movement, is what generalises — which is the same claim as (c) in §7.1: representing the
operation without executing it is what produces the transferable representation.

### 7.8 `DESIGN` — the intuition trainer

**The artifact.** A training object that combines the five things that each independently produce
transfer at d ≈ 0.3–1.2 and that no shipping product combines:

1. A bank of **many varied novel instances** — not worked examples, instances.
2. Presented as **classification under a time gate**, with **signal-detection-based mastery
   retirement** (which mattered, F(1,72) = 4.861, p = .031) and **no clever sequencing** (which did
   not, p = .509).
3. **Interleaved across confusable categories only**, per Brunmair & Richter's moderator profile —
   and blocked wherever the categories are not confusable, since that cell is g = −0.39.
4. **Prediction before reveal** on every instance, to route encoding to the expectancy violations
   (Theobald & Brod's interaction, p = .002) rather than to raise the average (which it does not,
   d = .077).
5. **Paired-case comparison** with *finding similarities* as the stated objective and the principle
   stated **after** (Alfieri's four reliable moderators).

Measured on the instrument §7.1 names: **accuracy-under-time-gate on untrained instances at four
weeks or more.**

**What would show this was the wrong design.** It is wrong if a matched-time cohort trained this way
does **not** beat a worked-example cohort on timed classification of untrained instances at 4+ weeks.
And there is a second, sharper check that must be run in the same trial: on **in-lesson accuracy**
and on **routine procedural problems**, the evidence predicts this design will *lose* — Schwartz
et al.'s word-problem nulls (d = .04, p = .65), their worksheet deficit (84.7% vs 91.8%, p = .037),
and Glogger-Frey's transfer reversal (BF₊₀ > 313). **If it wins on those too, the comparison is
broken** — most likely because the control condition was not a genuine worked-example condition —
and the result should not be believed.

**`DESIGN` claim; not a finding.** No source combines these five. The evidence supports each
component separately and says nothing about their combination.


---

## 8. Negative and null results register

The editorial standard requires at least one per section and the brief requires at least four. There
are seventeen, each with numbers.

| # | Null / negative result | The numbers | Why it matters here |
|---|---|---|---|
| 1 | **The "transient details are harmless" cell is not a null — it is unmeasured** | g = 0.12, **95% CI [−0.33, 0.57]**, k = 18. The interval contains the persistent estimate of 0.43 | The corpus's hinge cannot bear the weight placed on it. §1 is rebuilt on referential status instead |
| 2 | **Decorative animation does nothing** | **g = −0.05 [−0.17, 0.07]**, k = 17, vs representational animation g = 0.40 [0.34, 0.46], k = 59 (Höffler & Leutner 2007) | Kills "extraneousness" as the mechanism. Non-referential decoration is inert, not harmful |
| 3 | **Decorative page furniture does nothing** | N = 95, 3 × 3 degrees of decoration in header/footer and flow chart: **no significant effect on retention, transfer, or time** (Rey 2012, JEMH) | Same conclusion, from a primary experiment |
| 4 | **Emotional design does not work by making learners feel good** | Learning d+ = 0.317–0.387; **liking d+ = 0.109, positive affect d+ = 0.113; perceived learning 0.097 n.s., perceived effort 0.051 n.s., ps > .227** (Brom et al. 2018). Replicated: learning 0.27–0.35, affect 0.09, liking 0.10 (Wong & Adesope 2021) | Falsifies the "make it fun" theory of engagement, twice, independently |
| 5 | **Interruption count does not drive the seductive-details effect; dose does** | Five details grouped (one interruption) vs interspersed (five): **no significant difference**; load ↑ and transfer ↓ in both (Wirzberger group 2025) | Removes the last structural rescue for the transience reading |
| 6 | **Prequestions do nothing for the material they did not ask about** | **g = 0.04 [−0.04, 0.11], k = 91, p = .349**; 46% of studies at or below zero (St. Hilaire et al. 2024) | A question is a spotlight, not floodlighting. Governs §3.7 |
| 7 | **Prequestions failed in an actual classroom** | Chemical engineering course: no difference postquestions vs new questions at end of class, and none on weekly quizzes — **while retrieval practice worked in the same study** (Geller et al. 2017) | Lab-to-classroom transfer of the prequestion effect is not established |
| 8 | **Teaching 5–7-year-olds to ask questions produced no learning gain** | Preregistered RCT, N = 103: science learning **b = 7.74, 95% CI [−1.93, 17.40], p = .12, p_FDR = .20**; persistence null; prompted question-asking null; **cued exploration significantly worse (p = .02)** (Park et al. 2025) | The best-designed test of the owner's instinct in young children. Only "valuing information" moved |
| 9 | **Teaching adolescents to generate questions lowered self-regulatory self-efficacy** | Question Formulation Technique over one school year: positive on curiosity, **negative on self-regulatory self-efficacy and cognitive engagement** (Clark et al. 2021) | Question training is not free |
| 10 | **Socratic questioning has essentially no experimental base in education** | No meta-analysis located. The one randomised study with a standardised outcome (N = 25): **no significant influence on critical thinking; no effect on participation frequency** (Lowenstein 2010) | A canonical method with a near-empty evidence file |
| 11 | **Fixing help-seeking behaviour did not improve learning** | Help Tutor: lasting behaviour change months after removal; **"we did not find improved domain-level learning"** — the authors' "main disappointment," paralleled by Tai et al. 2013 (Aleven et al. 2016) | The load-bearing null of §4. Repairing one executive demand in isolation is not enough |
| 12 | **Hints do not help at low or high skill** | Help helps only at **intermediate** skill; at low or high skill, attempting without help was more effective (Roll et al. 2014 EDM) | The always-available help button is the wrong affordance at both ends |
| 13 | **Training an executive function does not transfer to untrained ones** | **g = 0.11, k = 17, p = .11** (Kassai et al. 2019). Training attention did not improve attention; training mixed EF did not improve targeted EF, both 95% CIs include 0.0 (Rapport et al. 2013) | Confirms the corpus. Externalise, do not train |
| 14 | **ADHD is not primarily a deficit in sustaining over time** | Vigilance-decrement omissions **δ = 0.54, 80% CV −0.14 to 1.22 (crosses zero)**; commissions 0.24, RT 0.27, SDRT 0.22 — against overall omissions δ = 1.34 and d′ d = 0.98 (Huang-Pollock et al. 2012) | The folk model that drives "shorter lessons" is wrong. §5.2 |
| 15 | **Blinding removes most behavioural and cognitive-training effects in ADHD** | Under probably-blinded assessment, **only free fatty acids (0.16) and food-colour exclusion (0.42) survived**; behavioural interventions, neurofeedback, cognitive training and elimination diets all attenuated to non-significance (Sonuga-Barke et al. 2013, 54 RCTs). Cognitive training: blinded ADHD total **SMD 0.12 [−0.01, 0.25]**, academics n.s. (Westwood et al. 2023) | The vendor-visible effect and the real effect differ by the rater |
| 16 | **School-based ADHD interventions do not reliably move achievement** | Between-subjects behaviour **0.18 n.s.**; academic **0.43 n.s.** between and **0.42 n.s.** within (DuPaul et al. 2012). Organisational skills training: organisational deficits d = 0.96–1.20, **"effects on academic measures were not significant"** (Nissley-Tsiopinis et al. 2024); parent-rated d = .63–1.05, **teacher ratings not significant** (Langberg et al. 2012) | Organisational training reliably teaches organisation |
| 17 | **Extended time shows no differential boost for ADHD, and once the wrong sign** | Three independent failures; **Lovett & Leja (2015): more ADHD/EF symptoms → *less* benefit**, and self-perceived need did not predict benefit. No ADHD-specific meta-analysis exists | Mandated and unevidenced. §5.6 |
| 18 | **Prediction does not raise average memory** | 60.42% vs 59.52%, **t(28) = 0.41, p = .682, d = .077** (Brod & Breitwieser 2019); no main effect b = −0.090, p = .330 (Theobald & Brod 2022) | It routes memory; it does not amplify it. §7.5 |
| 19 | **Interleaving reverses for word learning** | **g = −0.39**; n.s. for expository texts and tastes (Brunmair & Richter 2019). And a classroom null: subtraction-strategy adaptivity F(1,193) = 0.13, p = .72, no group × time p = .94 (Nemeth et al. 2019) | Interleaving is a discrimination tool, not a schedule |
| 20 | **Contrasting cases buy nothing on procedure, and cost in-lesson performance** | Word problems **d = .04, p = .65**; worksheet **84.7% vs 91.8%, p = .037** (Schwartz et al. 2011). Reversal: worked examples beat inventing on transfer, **BF₊₀ > 313** (Glogger-Frey et al. 2022) | The trade is real and must be sold honestly |
| 21 | **Generation reverses when what is generated has no semantic relation to the target** | Anagram generation **d = −.05**, CI excluding zero, 18 studies, >1,000 subjects (Bertsch et al. 2007) | Same referential rule as §1, in a different literature |
| 22 | **SRL activity only partially mediates SRL interventions' effect on achievement** | "Contrary to popular belief, the results only provide evidence for **partial mediation**" (Jansen et al. 2019, MASEM) | Bounds the externalisation argument in §4 |
| 23 | **Prior knowledge did not moderate multimedia design principles** | 30 pooled effects, R² = 0.14, **p = .14**; education level p = .95, format p = .24, subject p = .22 (Noetel et al. 2021) | Coherence discipline is not something advanced learners can be spared |
| 24 | **Sequencing did not matter in the perceptual learning module; retirement criteria did** | Sequencing **F(1,72) = 0.44, p = .509**; retirement **F(1,72) = 4.861, p = .031** (Kellman et al. 2023) | Mastery gating, not clever ordering |

---

## 9. `OPEN` — questions nobody has asked, and why not

**O1. Nobody has measured the transient seductive detail with adequate power.**
k = 18, CI [−0.33, 0.57]. *Why not:* the seductive-details paradigm is built on text-and-static-image
materials — Cheng et al. (2026) find the effect cleanest in "paper-and-pencil learning settings" —
where transience is difficult to manipulate at all. Transience lives in live instruction and video,
where randomisation is expensive and the unit of assignment is a class rather than a page. The
result is that the single most common instructional act in the world — the teacher's aside — has a
literature of eighteen effect sizes.

**O2. Nobody has asked whether a question and a joke are the same intervention.**
Both open a gap and close it. Kang et al.'s curiosity → caudate anticipation → enhanced encoding of
the surprising resolution is structurally identical to setup → tension → punchline, and the two have
never been contrasted in one design. *Why not:* instructional humour research lives in communication
studies and uses satisfaction, immediacy and rating-scale outcomes; curiosity research lives in
cognitive neuroscience and uses delayed cued recall and fMRI. There is no shared instrument, so
there has been no shared experiment.

**O3. Nobody has measured executive-function demand as a property of a product.**
*Why not:* every instrument in the field — BRIEF, CPT, n-back, Stroop, Tower — operationalises
executive function as a property of a *person*. There is no validated instrument that scores an
*interface* for how much executive function it charges its user. The measurement tradition has no
place to put the question, so the question does not get asked. This is what §4.5's ledger proposes to
change.

**O4. Body doubling has zero controlled outcome data despite mass adoption.**
Europe PMC `TITLE:"body doubling"` returns **0 results**; the only two academic sources are the same
220-person descriptive survey, whose authors state that "no academic exploration exists on the
topic." *Why not:* the practice was invented and propagated by the ADHD community outside clinical
research, it has no pharmaceutical or device sponsor, and it does not map onto any existing funded
trial category. It is a plausible external supply for §4.4 row 1 and row 4 with nothing to cite.

**O5. Whether the prequestion age penalty is developmental or scaffolding-dependent.**
Adults g = 0.62, grade-school children g = 0.22, and the entire children's cell is **k = 20**. It is
unknown whether children benefit less because the mechanism requires metacognitive machinery they do
not yet have, or because the questions used with children were not scaffolded to produce genuine
attempts. *Why not:* the studies have not been run. The literature grew out of adult list-learning
paradigms and has migrated into classrooms only recently.

**O6. Whether acquisition compression borrows from durability at matched effort.**
The central assumption of every "learn X fast" claim, including §6.4's, is that the two clocks are
independent. *Why not:* testing it requires a primary endpoint 90+ days after the product stops
being used, on a compressed-acquisition arm, with total effort held constant across arms. Nobody
funds a trial whose primary outcome is measured three months after the intervention ends and whose
best possible result is "no worse."

**O7. Whether the five profile-derived triggers in §5.7 harm the learners who do not need them.**
The whole SELPA-first / curb-cut argument in this project rests on universal application being
harmless-or-better for the majority. *Why not:* universal-design research measures whether
accommodations *help* the target group, not whether they *cost* the non-target group, because the
non-target group is the control condition rather than an outcome of interest.

---

## 10. What to build — the constructive summary

Six things, ordered by evidence strength per unit of engineering effort. None of these is a `DESIGN`
claim; each is an application of a measured effect.

1. **Delete every element that has no referent in the target schema, and add elements that point at
   it.** Signalling g = 0.43 (k = 209) is the best-evidenced single design act available; removing
   competing referents is worth g = 0.16–0.43; and non-referential decoration is *free* (g = −0.05),
   so the discipline is about competing stories, not about visual austerity.
2. **Write in the second person.** Personalisation g = 0.33 [0.23, 0.44], k = 55. This is the
   cheapest measured effect in instructional design and it is the one thing on this list that costs
   a prompt line.
3. **Segment for the learner; do not let them segment for themselves.** g = 0.41 vs 0.20, and accept
   that it takes longer (g = 0.92) because the time between segments is where consolidation happens.
4. **One attemptable prequestion per knowledge component, with a required guess and immediate
   correction.** Specific g = 0.54; guessing 0.65 vs reading 0.22. And do not expect it to cover
   anything it did not ask about (general g = 0.04).
5. **Never require the learner to recognise that they need help.** Trigger on the observable state —
   the three-error run, the sub-second hint dwell, the wheel-spinning signature — and deliver a
   worked step with a required response rather than text. The 34% and 68% figures are the
   justification, and the Help Tutor null is the warning that this alone will not be sufficient.
6. **Give away the accommodation that has evidence.** Read-aloud is the one accommodation with a
   differential-boost finding in ADHD, and it is free in software, universal, and requires no
   eligibility determination. Extended time is mandated, must be provided, and should not be
   described to a family as an intervention that is known to work.

---

## 11. Bibliography

Ordered by first appearance. `†` marks sources whose full text was recovered and quoted verbatim;
`‡` marks sources with numbers flagged **UNVERIFIED** at point of use.

**Coherence, seductive details, emotional design**

1. † Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., & Parker, P. D. (2021). Multimedia design for learning: An overview of reviews with meta-meta-analysis. *Review of Educational Research*. `10.3102/00346543211052329` (preprint recovered via `osf.io/pynzr/download`). `MEASURED-META`
2. Sundararajan, N., & Adesope, O. (2020). Keep it coherent: A meta-analysis of the seductive details effect. *Educational Psychology Review*, 32, 707–734. `10.1007/s10648-020-09522-4`. `MEASURED-META`
3. Cheng, C., Wu, Y., Wang, R., & Wang, Z. (2026). Seductive details, cognitive load, and learning outcomes: A multi-level meta-analysis and MASEM. *Educational Psychology Review*. `10.1007/s10648-025-10099-z` (ERIC EJ1510171). `MEASURED-META`
4. Rey, G. D. (2012). A review of research and a meta-analysis of the seductive detail effect. *Educational Research Review*, 7(3), 216–237. `10.1016/j.edurev.2012.05.003` (ERIC EJ986386). `MEASURED-META`
5. Rey, G. D. (2012). How seductive are decorative elements in learning materials? *Journal of Educational Multimedia and Hypermedia* (ERIC EJ981639). `MEASURED-RCT` (null)
6. Rey, G. D., & Steib, N. (2018). The moderating role of arousal on the seductive detail effect in a multimedia learning setting. *Applied Cognitive Psychology*. `10.1002/acp.3473` (ERIC EJ1263899). `MEASURED-RCT`
7. Wirzberger group (2025). Seductive details in learning text — less harmful if they are grouped together instead of interspersed? *Applied Cognitive Psychology*. `10.1002/acp.70065` (ERIC EJ1474777). `MEASURED-RCT`
8. † Brom, C., Stárková, T., & D'Mello, S. K. (2018). How effective is emotional design? *Educational Research Review*, 25, 100–119. `10.1016/j.edurev.2018.09.004`. `MEASURED-META`
9. Wong, R. M., & Adesope, O. (2021). Meta-analysis of emotional designs in multimedia learning: A replication and extension study. *Educational Psychology Review*. `10.1007/s10648-020-09545-x` (ERIC EJ1295978). `MEASURED-META`
10. Höffler, T. N., & Leutner, D. (2007). Instructional animation versus static pictures: A meta-analysis. *Learning and Instruction*, 17(6), 722–738. `10.1016/j.learninstruc.2007.09.013` (numbers via Noetel). `MEASURED-META`
11. Schneider, S., Beege, M., Nebel, S., & Rey, G. D. (2018). Signalling meta-analysis (numbers via Noetel). `MEASURED-META`
12. Ginns, P., Martin, A. J., & Marsh, H. W. (2013). Designing instructional text in a conversational style: A meta-analysis. *Educational Psychology Review*, 25, 445–472. `10.1007/s10648-013-9228-0`. `MEASURED-META`
13. Rey, G. D., Beege, M., Nebel, S., et al. (2019). Segmenting meta-analysis (numbers via Noetel). `MEASURED-META`
14. Schroeder, N. L., Adesope, O. O., & Gilbert, R. B. (2013). How effective are pedagogical agents for learning? *Journal of Educational Computing Research*, 49(1). `10.2190/ec.49.1.a`. `MEASURED-META`
15. Davis, R. O. (2018); Castro-Alonso, J. C., et al. (2021) — pedagogical-agent moderators (numbers via Noetel). `MEASURED-META`
16. Alemdag, E., & Cagiltay, K. (2018). Eye-tracking review of multimedia learning (via Noetel). `MEASURED-META`
17. Adesope, O. O., & Nesbit, J. C. (2012). Verbal redundancy meta-analysis (via Noetel). `MEASURED-META`

**Narrative**

18. † Mar, R. A., Li, J., Nguyen, A. T. P., & Ta, C. P. (2021). Memory and comprehension of narrative versus expository texts: A meta-analysis. *Psychonomic Bulletin & Review*, 28, 732–749. `10.3758/s13423-020-01853-1`. `MEASURED-META`
19. Clinton, V., et al. (2020). Genre differences in inferential comprehension (via Mar et al.). `MEASURED-META`
20. Walkington, C. A. (2013). Using adaptive learning technologies to personalize instruction to student interests. *Journal of Educational Psychology*, 105(4), 932–945. `10.1037/a0031882` (ERIC EJ1054444). `MEASURED-RCT` ‡ (effect sizes UNVERIFIED)

**Questions, curiosity, pretesting**

21. † St. Hilaire, K. J., Chan, J. C. K., & Ahn, D. (2024). Guessing as a learning intervention: A meta-analytic review of the prequestion effect. *Psychonomic Bulletin & Review*, 31, 411–441. `10.3758/s13423-023-02353-8`. `MEASURED-META`
22. Pan, S. C., & Carpenter, S. K. (2023). Prequestioning and pretesting effects. *Educational Psychology Review*. `10.1007/s10648-023-09814-5`. `MEASURED-META`
23. Geller, J., Carpenter, S. K., Lamm, M. H., Rahman, S., Armstrong, P. I., & Coffman, C. R. (2017). Prequestions do not enhance the benefits of retrieval in a STEM classroom. *Cognitive Research: Principles and Implications*, 2, 42. `10.1186/s41235-017-0078-z`. `MEASURED-RCT` (null)
24. Kang, M. J., Hsu, M., Krajbich, I. M., et al. (2009). The wick in the candle of learning. *Psychological Science*, 20(8), 963–973. `MEASURED-BENCH`
25. Gruber, M. J., Gelman, B. D., & Ranganath, C. (2014). States of curiosity modulate hippocampus-dependent learning via the dopaminergic circuit. *Neuron*, 84(2), 486–496. `10.1016/j.neuron.2014.08.060`. `MEASURED-BENCH`
26. Loewenstein, G. (1994). The psychology of curiosity. *Psychological Bulletin*, 116(1), 75–98. `INFERENCE` (theory)
27. † Park, A. T., Colantonio, J., Delgado Reyes, L., et al. (2025). Question asking practice fosters aspects of curiosity in science content in young children. *npj Science of Learning*. `10.1038/s41539-025-00384-5`, PMC12770468. `MEASURED-RCT`
28. Clark, S., Harbaugh, A. G., & Seider, S. (2021). Teaching questioning fosters adolescent curiosity. *Applied Developmental Science* (ERIC EJ1263074). `OBSERVED`
29. Lowenstein, A. (2010). The influence of Socratic questioning in online discussions on the critical thinking skills of undergraduate students. ProQuest, ERIC ED514978. `MEASURED-RCT` (null, N = 25)
30. Reichardt, R., Polner, B., & Simor, P. (2023). Influencing prior knowledge through a short reading impacts curiosity and learning. *Applied Cognitive Psychology*. `MEASURED-RCT`
31. Sinha, T., & Kapur, M. (2021). When problem solving followed by instruction works. *Review of Educational Research*, 91(5). `10.3102/00346543211019105` (ERIC EJ1308129). `MEASURED-META` ‡
32. Bertsch, S., Pesta, B. J., Wiscott, R., & McDaniel, M. A. (2007). The generation effect: A meta-analytic review. *Memory & Cognition*, 35(2), 201–210. `10.3758/BF03193441`. `MEASURED-META`
33. Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). Rethinking the use of tests. *Review of Educational Research*, 87(3), 659–701. `10.3102/0034654316689306` [carried from B1]. `MEASURED-META`

**Executive function, help seeking, self-regulation**

34. † Aleven, V., Roll, I., McLaren, B. M., & Koedinger, K. R. (2016). Help helps, but only so much: Research on help seeking with intelligent tutoring systems. *IJAIED*, 26, 205–223. `10.1007/s40593-015-0089-1`. `OBSERVED` + `MEASURED-RCT` (null)
35. Aleven, V., & Koedinger, K. R. (2000). Limitations of student control: Do students know when they need help? *ITS 2000*. `10.1007/3-540-45108-0_33`. `OBSERVED`
36. Roll, I., Aleven, V., McLaren, B. M., & Koedinger, K. R. (2010). Improving students' help-seeking skills using metacognitive feedback in an intelligent tutoring system. *Learning and Instruction*. `10.1016/j.learninstruc.2010.07.004`. `MEASURED-RCT` — **note the tension with #34, reported in §4.3**
37. Kassai, R., Futó, J., Demetrovics, Z., & Takács, Z. K. (2019). A meta-analysis of the experimental evidence on near- and far-transfer among children's executive function skills. *Psychological Bulletin*. `10.1037/bul0000180`. `MEASURED-META` (null)
38. Guo, L. (2022). Using metacognitive prompts to enhance self-regulated learning and learning outcomes. *JCAL*. `10.1111/jcal.12650` (ERIC). `MEASURED-META`
39. Dignath, C., & Büttner, G. (2008). Components of fostering self-regulated learning among students. *Metacognition and Learning* (ERIC EJ817558). `MEASURED-META`
40. Jansen, R. S., van Leeuwen, A., Janssen, J., Jak, S., & Kester, L. (2019). Self-regulated learning partially mediates the effect of SRL interventions on achievement in higher education. *Educational Research Review*. `10.1016/j.edurev.2019.100292`. `MEASURED-META`
41. Xu, Z., Zhao, Y., Zhang, B., Liew, J., & Kogut, A. (2022). A meta-analysis of SRL interventions in online and blended environments. *Behaviour & Information Technology*. `10.1080/0144929x.2022.2151935`. `MEASURED-META`
42. Donker, A., de Boer, H., Kostons, D., Dignath van Ewijk, C., & van der Werf, M. (2014). Effectiveness of learning strategy instruction on academic performance. *Educational Research Review*. `10.1016/j.edurev.2013.11.002`. `MEASURED-META`
43. Breitwieser, J., & Reinelt, T. (2026). The effectiveness of implementation intentions in children: A systematic review and meta-analysis. *British Journal of Psychology*. `10.1111/bjop.70065`. `MEASURED-META`
44. Gollwitzer, P. M., & Sheeran, P. (2006). Implementation intentions and goal achievement: A meta-analysis of effects and processes. *Advances in Experimental Social Psychology*, 38, 69–119. `10.1016/S0065-2601(06)38002-1`. `MEASURED-META` ‡ (the widely cited d = 0.65 could not be verified from a retrieved source this session)

**ADHD**

45. Willcutt, E. G., Doyle, A. E., Nigg, J. T., Faraone, S. V., & Pennington, B. F. (2005). Validity of the executive function theory of ADHD. *Biological Psychiatry*. `10.1016/j.biopsych.2005.02.006`. `MEASURED-META` ‡
46. Kofler, M. J., Rapport, M. D., Sarver, D. E., et al. (2013). Reaction time variability in ADHD: A meta-analytic review of 319 studies. *Clinical Psychology Review*. `10.1016/j.cpr.2013.06.001`. `MEASURED-META`
47. Karalunas, S. L., Huang-Pollock, C. L., & Nigg, J. T. (2013). Is reaction time variability in ADHD mainly at low frequencies? *JCPP*. `10.1111/jcpp.12028`. `MEASURED-META` (null: diagnosis × frequency p = .954)
48. † Huang-Pollock, C. L., Karalunas, S. L., Tam, H., & Moore, A. N. (2012). Evaluating vigilance deficits in ADHD: A meta-analysis of CPT performance. *Journal of Abnormal Psychology*. `10.1037/a0027205`, PMC3664643. `MEASURED-META`
49. Alderson, R. M., Rapport, M. D., & Kofler, M. J. (2007). Attention-deficit/hyperactivity disorder and behavioral inhibition: A meta-analytic review of the stop-signal paradigm. *JACP*. `10.1007/s10802-007-9131-6`. `MEASURED-META`
50. Jackson, J. N. S., & MacKillop, J. (2016). Attention-deficit/hyperactivity disorder and monetary delay discounting: A meta-analysis. *Biological Psychiatry: CNNI*. `10.1016/j.bpsc.2016.01.007`. `MEASURED-META`
51. Patros, C. H. G., Alderson, R. M., Kasper, L. J., et al. (2016). Choice-impulsivity in children and adolescents with ADHD: A meta-analytic review. *Clinical Psychology Review*. `10.1016/j.cpr.2015.11.001`. `MEASURED-META`
52. Marco, R., et al. (2009). Delay and reward choice in ADHD. *Neuropsychology*. `10.1037/a0014914`. `MEASURED-BENCH`
53. † Dovis, S., Van der Oord, S., Wiers, R. W., & Prins, P. J. M. (2012). Can motivation normalize working memory and task persistence in children with ADHD? *JACP*. `10.1007/s10802-011-9601-8`, PMC3375007. `MEASURED-RCT`
54. Antrop, I., Roeyers, H., Van Oost, P., & Buysse, A. (2000). Stimulation seeking and hyperactivity in children with ADHD. *JCPP*. `10.1111/1469-7610.00603`; re-analysis Antrop et al. (2002), *Perceptual and Motor Skills*, `10.2466/pms.2002.95.1.71`. `OBSERVED` (weak: 2 of 25 target behaviours)
55. Kortekaas-Rijlaarsdam, A. F., Luman, M., Sonuga-Barke, E., & Oosterlaan, J. (2019). Does methylphenidate improve academic performance? *European Child & Adolescent Psychiatry*. `10.1007/s00787-018-1106-3`. `MEASURED-META`
56. Prasad, V., Brogan, E., Mulvaney, C., Grainge, M., Stanton, W., & Sayal, K. (2013). How effective are drug treatments for children with ADHD at improving on-task behaviour and academic achievement? *European Child & Adolescent Psychiatry*. `10.1007/s00787-012-0346-x`. `MEASURED-META`
57. Cerrillo-Urbina, A. J., et al. (2018). Prevalence and effects of stimulants: network meta-analysis. *J Child Adolesc Psychopharmacol*. `10.1089/cap.2017.0151`. `MEASURED-META`
58. Rapport, M. D., Orban, S. A., Kofler, M. J., & Friedman, L. M. (2013). Do programs designed to train working memory, other executive functions, and attention benefit children with ADHD? *Clinical Psychology Review*. `10.1016/j.cpr.2013.08.005`. `MEASURED-META` (null)
59. Cortese, S., et al. (2015). Cognitive training for ADHD: Meta-analysis of clinical and neuropsychological outcomes from randomized controlled trials. *JAACAP*. `10.1016/j.jaac.2014.12.010`. `MEASURED-META` (null on academics)
60. Westwood, S. J., Parlatini, V., Rubia, K., Cortese, S., & Sonuga-Barke, E. J. S. (2023). Computerized cognitive training in ADHD: A meta-analysis of RCTs with blinded and objective outcomes. *Molecular Psychiatry*. `10.1038/s41380-023-02000-7`. `MEASURED-META` (null)
61. Sonuga-Barke, E. J. S., et al. (2013). Nonpharmacological interventions for ADHD: Systematic review and meta-analyses of randomized controlled trials of dietary and psychological treatments. *American Journal of Psychiatry*. `10.1176/appi.ajp.2012.12070991`. `MEASURED-META`
62. Daley, D., van der Oord, S., Ferrin, M., et al. (2014). Behavioral interventions in ADHD: Meta-analysis of RCTs across multiple outcome domains. *JAACAP*. `10.1016/j.jaac.2014.05.013`. `MEASURED-META`
63. Fabiano, G. A., Pelham, W. E., Coles, E. K., et al. (2009). A meta-analysis of behavioral treatments for ADHD. *Clinical Psychology Review*. `10.1016/j.cpr.2008.11.001`. `MEASURED-META`
64. DuPaul, G. J., Eckert, T. L., & Vilardo, B. (2012). The effects of school-based interventions for ADHD: A meta-analysis 1996–2010. *School Psychology Review* (ERIC). `MEASURED-META`
65. Abikoff, H., Gallagher, R., Wells, K. C., et al. (2013). Remediating organizational functioning in children with ADHD. *Journal of Consulting and Clinical Psychology*. `10.1037/a0029648`. `MEASURED-RCT`
66. Nissley-Tsiopinis, J., et al. (2024). Organizational skills training, tier 2. *Journal of Consulting and Clinical Psychology*. `10.1037/ccp0000909`. `MEASURED-RCT`
67. Langberg, J. M., Epstein, J. N., Becker, S. P., Girio-Herrera, E., & Vaughn, A. J. (2012). Evaluation of the Homework, Organization, and Planning Skills (HOPS) intervention. *School Psychology Review*, PMC4209597. `MEASURED-RCT`
68. Evans, S. W., Owens, J. S., & Bunford, N. (2014). Evidence-based psychosocial treatments for children and adolescents with ADHD. *JCCAP*. `10.1080/15374416.2013.850700`; updated Evans, Owens, Wymbs & Ray (2018), `10.1080/15374416.2017.1390757`. `MEASURED-META`
69. Lovett, B. J., & Nelson, J. M. (2021). Systematic review: Educational accommodations for children and adolescents with ADHD. *JAACAP*. `10.1016/j.jaac.2020.07.891`. `MEASURED-META`
70. Lewandowski, L. J., Lovett, B. J., Parolin, R., Gordon, M., & Codding, R. S. (2007). Extended time accommodations and the mathematics performance of students with and without ADHD. *Journal of Psychoeducational Assessment* (ERIC). `MEASURED-RCT` (null)
71. Miller, L. A., Lewandowski, L. J., & Antshel, K. M. (2015). Effects of extended time for college students with and without ADHD. *Journal of Attention Disorders*. `10.1177/1087054713483308`. `MEASURED-RCT` (null)
72. Lovett, B. J., & Leja, A. M. (2015). ADHD symptoms and benefit from extended time testing accommodations. *Journal of Attention Disorders*. `10.1177/1087054713510560`. `MEASURED-RCT` (negative direction)
73. Spiel, C. F., Mixon, C. S., Holdaway, A. S., Evans, S. W., Harrison, J. R., Zoromski, A. K., & Yost, J. S. (2016). *Remedial and Special Education*; and Spiel, Evans & Harrison (2019), *Journal of Applied School Psychology* (ERIC). `MEASURED-RCT` ‡
74. Gregg, N., & Nelson, J. M. (2012). Meta-analysis on the effectiveness of extra time as a test accommodation for transitioning adolescents with learning disabilities. *Journal of Learning Disabilities* (ERIC). `MEASURED-META`
75. Malcon, M., et al. (2026). Extra time accommodation RCT protocol. *JMIR Research Protocols*. `10.2196/80271`, NCT06063382. `OBSERVED` (no results)
76. Eagle, T., Baltaxe-Admony, L. B., & Ringland, K. E. (2023). "Proceed with care": Body doubling. ASSETS '23, `10.1145/3597638.3614486`; extension *ACM TACCESS* (2024), `10.1145/3689648`. `OBSERVED` (descriptive; no outcome data)
77. Xu, Zhao & Hu (2026). *Psychology of Sport and Exercise*, `10.1016/j.psychsport.2026.103088`; Li et al. (2025), *J Affective Disorders*, `10.1016/j.jad.2025.01.155`; Cheng, Song & Hong (2025), *Frontiers in Psychiatry*, `10.3389/fpsyt.2025.1578614`; Carcelén-Fraile et al. (2025), *Healthcare*, `10.3390/healthcare13192415`. `MEASURED-META`
78. Kieffer, M. J., Lesaux, N. K., Rivera, M., & Francis, D. J. (2009). *Review of Educational Research* [carried from H2]. `MEASURED-META`
79. Rios, J. A., Ihlenfeldt, S. D., & Chavez, C. (2020). *Educational Measurement: Issues and Practice*, ERIC EJ1276694 [carried from H2]. `MEASURED-META`

**Intuition, perceptual learning, comparison, gesture**

80. † Kellman, P. J., Massey, C. M., & Son, J. Y. (2010). Perceptual learning modules in mathematics. *Topics in Cognitive Science*, 2(2), 285–305. `10.1111/j.1756-8765.2009.01053.x`, PMC6124488. `MEASURED-RCT`
81. Krasne, S., Hillman, J. D., Kellman, P. J., & Drake, T. A. (2013). Applying perceptual and adaptive learning techniques for teaching introductory histopathology. *Journal of Pathology Informatics*, 4, 34. `10.4103/2153-3539.123991`, PMC3908489. `MEASURED-RCT`
82. Ahmad, S., Ashraf, M., Kellman, P. J., Krasne, S., & Ramanathan, S. (2021). Ophthalmology PALM randomised comparison. `10.21203/rs.3.rs-806381/v1`. `MEASURED-RCT`
83. † Kellman, P. J., Krasne, S., Massey, C. M., & Mettler, E. (2023). Adaptive learning schedules in a skin-cancer perceptual learning module. *CogSci*, eScholarship qt83z22046. `MEASURED-RCT`
84. Guerlain, S., et al. (2003). *Proceedings of HFES*, `10.1177/154193120304700330`. `MEASURED-RCT`
85. † Schwartz, D. L., Chase, C. C., Oppezzo, M. A., & Chin, D. B. (2011). Practicing versus inventing with contrasting cases. *Journal of Educational Psychology*, 103(4), 759–775. `10.1037/a0025140`. `MEASURED-RCT`
86. Schwartz, D. L., & Martin, T. (2004). Inventing to prepare for future learning. *Cognition and Instruction*, 22(2). `10.1207/s1532690xci2202_1`. `MEASURED-RCT` ‡
87. Glogger-Frey, I., Treier, A.-K., & Renkl, A. (2022). *Instructional Science*. `10.1007/s11251-022-09577-6`. `MEASURED-RCT` (reversal)
88. Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin*, 145(11). `10.1037/bul0000209`. `MEASURED-META`
89. Nemeth, L., Werker, K., Arend, J., Vogel, S., & Lipowsky, F. (2019). Interleaved learning in elementary school mathematics. *Frontiers in Psychology*, 10, 86. `10.3389/fpsyg.2019.00086`, PMC6385790. `MEASURED-RCT` (null)
90. Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the enemy of induction? *Psychological Science*, 19(6). `10.1111/j.1467-9280.2008.02127.x`. `MEASURED-RCT` ‡
91. † Brod, G., & Breitwieser, J. (2019). Lighting the wick in the candle of learning: Generating a prediction stimulates curiosity. *npj Science of Learning*, 4, 17. `10.1038/s41539-019-0056-y`, PMC6803639. `MEASURED-RCT`
92. † Theobald, M., & Brod, G. (2022). Tackling scientific misconceptions: The element of surprise. *Psychonomic Bulletin & Review*, 29(6). `10.3758/s13423-022-02124-x`, PMC9722848. `MEASURED-RCT`
93. Alfieri, L., Nokes-Malach, T. J., & Schunn, C. D. (2013). Learning through case comparisons: A meta-analytic review. *Educational Psychologist*, 48(2). `10.1080/00461520.2013.775712`. `MEASURED-META`
94. † Gentner, D., Loewenstein, J., & Thompson, L. (2003). Learning and transfer: A general role for analogical encoding. *Journal of Educational Psychology*, 95(2), 393–408. `10.1037/0022-0663.95.2.393`. `MEASURED-RCT`
95. † Novack, M. A., Congdon, E. L., Hemani-Lopez, N., & Goldin-Meadow, S. (2014). From action to abstraction: Using the hands to learn math. *Psychological Science*, 25(4). `10.1177/0956797613518351`, PMC3984351. `MEASURED-RCT`
96. Chi, M. T. H., Feltovich, P. J., & Glaser, R. (1981). Categorization and representation of physics problems by experts and novices. *Cognitive Science*, 5(2), 121–152. `10.1207/s15516709cog0502_2`. `OBSERVED` ‡

**Carried from the corpus, not re-derived:** Sailer & Homner (2020) gamification moderators; Deci,
Koestner & Ryan (1999) 128 experiments on tangible rewards; Koedinger et al. (2023) PNAS
opportunities-to-mastery; Wan & Beck (2015) wheel-spinning; Cepeda et al. (2008) optimal spacing
gap; Fisher et al. (1980) BTES productive learning time; Pashler et al. learning styles;
Khan Academy (2026) on Khanmigo v1.
