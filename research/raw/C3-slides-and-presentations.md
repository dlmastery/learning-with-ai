---
title: "Slides on demand, and the learner as presenter: generative visual exposition and learning-by-explaining"
wave: C
section: C3
date_researched: 2026-07-27
sources_count: 57
status: raw-research
---

# C3 — Slides on demand, and the learner as presenter

> **Why this section exists.** The project owner asked for two things no other section owns:
> **"on the fly slide generation"** and **"having students explain topic to gain deeper
> understanding, giving presentation etc. — best way to learn is to teach others."** These are two
> distinct mechanisms with two distinct literatures, and they meet in exactly one place: the moment
> a learner has to *produce* an exposition rather than receive one.

> **Scope boundaries.** **A2** owns animation pedagogy, Manim, Remotion, and LLM→video toolchains.
> **C1** owns single-figure generation and its correctness gate — its central finding (emit a
> declarative spec, render deterministically; hand-written SVG is Tier D) is a *premise* here, not a
> result to re-derive. **F2** owns the AI-as-tutee role (teachable agents, the protégé effect,
> capability leakage). C3 owns (a) the **deck** as a unit — sequencing, per-slide budgets, the
> text/narration channel split, reading order — and (b) the **learner as the one presenting**, where
> the audience is the design variable and the artifact is the learner's own explanation.

> **Retrieval note.** WebSearch budget exhausted. The arXiv **API** (`export.arxiv.org`) returned
> `HTTP 429 Rate exceeded` at the host level for this entire session and was never usable. Retrieval
> ran on: (a) **Crossref REST** — bibliographic records and, where publishers deposit them, verbatim
> abstracts; (b) **ERIC API** (`api.ies.ed.gov/eric`) — this was the single most productive channel
> for education research and returned **full verbatim abstracts** for the Part B core; (c) **Europe
> PMC REST** — verbatim abstracts for the clinical/psychophysiological material; (d) **Semantic
> Scholar Graph API** by DOI — intermittently rate-limited, but delivered the Baker meta-analysis
> abstract verbatim; (e) **WebFetch** on `arxiv.org/abs/…` and `arxiv.org/search/…`, which returns a
> *model-summarised rendering* rather than raw text; (f) the authenticated **GitHub API**.
>
> Claims marked `[verbatim]` were retrieved as publisher- or repository-supplied abstract text this
> session. Claims marked `[fetched-summary]` came through route (e) — quoted fragments are quoted as
> they appeared, but unquoted text is paraphrase and should be re-verified before entering the
> survey. Claims marked `[biblio-only]` have a verified bibliographic record but the abstract was
> **not retrievable this session** — Elsevier returned `HTTP 403`, Springer redirected to an IdP
> login, and APA journals have their abstracts elided from the Semantic Scholar corpus. Nothing
> below is reported from memory. Where a number could not be verified, that is stated in the line
> where the number would have gone.

**Evidence labels** (PRD §2): `MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH` · `OBSERVED` ·
`VENDOR` · `DEMO` · `INFERENCE`.

---

## 0. The thesis, compressed

**Four findings organise this section.**

**First — the deck is not the intervention; the design is.** The only meta-analysis that asks
whether *having slides at all* beats chalk-and-talk found **Hedges' g = 0.067, 95% CI [−0.103,
0.236]**, across **48 studies** (Baker, Goodboy, Bowman & Wright 2018,
[10.1016/j.compedu.2018.08.003](https://doi.org/10.1016/j.compedu.2018.08.003), `MEASURED-META`
`[verbatim]`). Zero, with a confidence interval that comfortably contains zero. The authors'
own conclusion is the correct brief for an AI system: *"researchers should move past strictly
comparing the absence or presence of this instructional tool, to instead examine how instructors
are integrating features of PowerPoint in ways that help students learn."* This is liberating rather
than deflating: it means a generator that merely produces slides has produced nothing, and a
generator that enforces the *design principles* — which do have effect sizes, up to g ≈ 0.74 — is
operating in a regime where there is measurable value on the table that human authors routinely
leave there.

**Second — the single most-violated multimedia principle in machine-generated decks is also the one
the literature does not actually support in its popular form.** "Never put on the slide what you
are saying out loud" is stated as a law. The meta-analytic estimate for verbal redundancy is
**g = 0.15 [0.08, 0.22], k = 57**, and it is **direction-dependent**: adding text to audio is
**g = 0.29 [0.20, 0.39]**; adding audio to existing text is **g = −0.04 [−0.14, 0.06], n.s.**
(Adesope & Nesbit 2012, [10.1037/a0026147](https://doi.org/10.1037/a0026147); numbers as recorded
and verified in this project's B1 report, `MEASURED-META`). Three independent studies retrieved this
session found **null or reversed** redundancy effects (§2.3). So the rule an AI slide generator
should encode is *not* "never duplicate." It is a **conditional switch** on learner language
status, pacing, and reading support — which a generator can actually evaluate at runtime and a
human lecturer cannot. That is a case where automation is not imitating the human but exceeding it.

**Third — the presenter-side evidence is much stronger than the slide-side evidence, and it has a
sharp, recently-measured shape.** Learning by teaching works, but **it is the expectancy-framed
preparation that carries it**. Kobayashi's 2024 meta-analysis of 39 studies: teaching after studying
**with** a teaching expectancy is **g = 0.48 [0.34, 0.63]**; teaching after studying **without** one
is **g = −0.02 [−0.14, 0.11]** — indistinguishable from zero. *"Preparing to teach catalyzes learning
by teaching"* (ERIC [EJ1414484](https://eric.ed.gov/?id=EJ1414484),
[10.1007/s10648-024-09871-4](https://doi.org/10.1007/s10648-024-09871-4), `MEASURED-META`
`[verbatim]`). An AI system can set that expectancy reliably, for free, before every study episode.
It is the cheapest high-yield intervention in this entire survey.

**Fourth — and most counter-intuitively — the *audience* is a cost, not a benefit, in its ordinary
form.** In a controlled comparison, college students who explained a lesson **to a camera**
outperformed those who explained **to one student** and **to seven students** on transfer, showed
lower social presence, **lower pulse rate**, lower state anxiety, lower cognitive load, and produced
**more idea units, more elaboration statements, and more monitoring statements** — with the effect
mediated by exactly those two paths (Wang, Cheng & Mayer 2023, *Journal of Educational Psychology*,
ERIC [EJ1386593](https://eric.ed.gov/?id=EJ1386593), `MEASURED-RCT` `[verbatim]`). Set against
Kobayashi's finding that *interactive* teaching beats non-interactive teaching, this produces the
design target that is the intellectual core of Part B:

> **The gain comes from being interrogated. The loss comes from being evaluated. A human audience
> delivers both, welded together. A machine audience is the first artifact in history that can
> deliver interrogation without evaluation — and nobody has run the experiment.**

That is a genuinely open, cheap, high-value experiment, and it is stated as a falsifiable claim in
§18.

---

# PART A — Generative slides and on-the-fly visual exposition

## 1. Does the medium work at all? The measured null everyone forgets

### 1.1 The headline

**Baker, Goodboy, Bowman & Wright (2018)**, *Computers & Education*,
[10.1016/j.compedu.2018.08.003](https://doi.org/10.1016/j.compedu.2018.08.003), 131 citations
(Semantic Scholar), `MEASURED-META` `[verbatim]`:

> "Almost two decades of student learning research has examined the impact of traditional
> instruction (i.e., chalk and talk) versus instruction aided by PowerPoint. This research has
> revealed inconsistent and contrasting results. To probe this inconsistency, a meta-analysis of 48
> studies was conducted to determine if students learn more when taught the same material using
> PowerPoint compared to traditional instruction. **Results revealed that on average, there was no
> difference in students' learning based on the type of instruction they received (Hedges'
> g = 0.067; 95% CI: −0.103 to 0.236).** Moderation analyses revealed that the sampling frame, such
> as a focus on K-12 versus college students, explained heterogeneity in the findings. Specifically,
> **K-12 students' cognitive learning increased as a result of PowerPoint instruction, but this
> effect did not emerge for college students.**"

The K-12 subgroup effect size is **not stated in the abstract** and could not be verified this
session (Elsevier full text returned `HTTP 403`). Report the direction; do not quote a magnitude.

### 1.2 Why this is the right thing to lead with, and why it is not discouraging

Three consequences follow, and all three sharpen rather than weaken the case for generative slides.

1. **A slide-generation system cannot claim credit for producing slides.** Any evaluation whose
   outcome is "the deck exists" or "raters preferred the deck" is measuring something with a
   measured population effect of ~0.07 on learning. §7 shows that this describes essentially the
   entire published slide-generation literature.

2. **The heterogeneity is the opportunity.** g = 0.067 with a CI spanning −0.10 to +0.24 across 48
   studies is not "slides don't work" — it is "slides work when designed well and hurt when designed
   badly, and the field averaged over both." The design principles have their own effect sizes
   (§2), some of them large. A generator that *enforces* the principles is operating on the good
   tail by construction. A human lecturer under time pressure is not.

3. **The K-12 moderator points at the population this project cares about.** The effect emerged for
   school-age learners and not for college students. That is consistent with the broader
   multimedia-design pattern in this project's B1 report, where design effects are larger for
   **system-paced** material (g = 0.41) than learner-paced (g = 0.27) and much larger for **complex,
   high-element-interactivity** material (g = 0.70) than simple (g = 0.20) (Noetel et al., as
   recorded in B1, `MEASURED-META`). Design help matters most for the learner with the least
   capacity to compensate. That is the H1 curb-cut argument arriving from a completely different
   direction.

---

## 2. The multimedia principles as a machine-checkable specification

### 2.1 The corpus-level number

Across the 11 largest systematic reviews of multimedia design — **808 effect sizes, 66,553
participants** — the average effect of multimedia design principles on learning is **g = 0.38,
95% CI [0.27, 0.49]**, with the *specific principle* explaining essentially all between-review
variance (Noetel et al., as verified and recorded in this project's B1 report, `MEASURED-META`).
Two things follow. The principles are real. And *which* principle you apply matters more than the
fact that you applied one — so a generator must encode them individually, with their individual
gates, not as a vague "follow Mayer" instruction in a system prompt.

### 2.2 Per-principle, with what a renderer can actually check

The effect sizes below are taken from this project's **B1** report, where each was verified against
its source review. C1 already converted the *figure-level* subset of these into predicates; the
table below extends that work to the **deck level** — the slide sequence, the text/narration channel
split, and the pacing controls, none of which exist inside a single figure.

| Principle | Effect on learning | Deck-level check the IR can assert | Gate |
|---|---|---|---|
| **Contiguity (overall)** | **g = 0.74 [0.67, 0.82]**, k = 46 (Ginns 2006) | labels adjacent to referents; narration cue-points aligned to build steps | always |
| **Spatial contiguity / split attention** | **g = 0.63 [0.55, 0.71]**, k = 58, n = 2,426 (Schroeder & Cenkci 2018, [10.1007/s10648-018-9435-9](https://doi.org/10.1007/s10648-018-9435-9)) | `distance(label_bbox, referent_bbox) < τ`; no legend-only mapping for ≤6 series; no slide where the figure and its explanatory text are on different slides | always |
| **Signalling** | **g = 0.43 [0.35, 0.50]**, k = 209 (Schneider et al. 2018); **r = 0.17**, concentrated in **low-prior-knowledge** learners (Richter, Scheiter & Eitel 2016, [10.1016/j.edurev.2015.12.003](https://doi.org/10.1016/j.edurev.2015.12.003)) | exactly one salient emphasis channel per slide; emphasis targets the element named in the slide's `claim` | **gate on prior knowledge** — expertise reversal |
| **Segmenting** | **g = 0.34 [0.30, 0.38]**, k = 123 (Rey et al. 2019); **system-segmented g = 0.41 > learner-segmented g = 0.20**; **time on task g = 0.92** | one slide = one claim; explicit learner-advanced boundaries | always segment; **allow skip** — the time cost is real |
| **Coherence / seductive-detail removal** | **g = 0.33 [0.18, 0.48]**, k = 68; **persistent details g = 0.43 harm**, transient **g = 0.12 n.s.** (Sundararajan & Adesope 2020, [10.1007/s10648-020-09522-4](https://doi.org/10.1007/s10648-020-09522-4)) | element budget per slide; every element referenced by the `claim` or the narration; **no decorative stock imagery** | always — and note slides are maximally persistent |
| **Modality** | **g = 0.38 [0.33, 0.43]**, k = 86 → **g = 0.20 [0.15, 0.25]** after publication-bias adjustment (Reinwein 2012); **d = 0.72 [0.52, 0.92]**, k = 39 (Ginns 2005, [10.1016/j.learninstruc.2005.07.001](https://doi.org/10.1016/j.learninstruc.2005.07.001)) | narration channel present when a figure is present | **two meta-analyses of the same principle differ 2–3×; report the range** |
| **Verbal redundancy** | **g = 0.15 [0.08, 0.22]**, k = 57; **text→audio g = 0.29 [0.20, 0.39]**; **audio→text g = −0.04 [−0.14, 0.06] n.s.** (Adesope & Nesbit 2012, [10.1037/a0026147](https://doi.org/10.1037/a0026147)) | token-overlap(on-slide text, narration) ≤ τ **when the switch in §2.4 is on** | **conditional — see §2.3–2.4** |
| **Personalization (conversational style)** | **g = 0.33 [0.23, 0.44]**, k = 55 (Ginns, Martin & Marsh 2013) — but **effects are small and n.s. beyond ~35 minutes** | narration register | short sessions only |

All effect sizes: `MEASURED-META`, sourced from B1's verified table. They were **not independently
re-verified this session** — the underlying reviews are behind Elsevier/Springer/APA paywalls that
returned 403 or IdP redirects to every route available. B1 verified them; this section inherits
them and says so.

**The engineering consequence, restated from C1 and extended:** *the largest effect size is also the
most mechanically checkable one.* Spatial contiguity (g = 0.63–0.74) reduces to a distance predicate
on two bounding boxes. Coherence (g = 0.33) requires judgement. Signalling requires a learner model.
Spend the automated gate's budget where the evidence and the tractability coincide, and reserve
scarce human review for coherence.

### 2.3 The redundancy effect, honestly — including three nulls and one reversal

This is where AI-generated decks most obviously go wrong, and where the folk rule is most obviously
wrong too. Both things are true, and getting the boundary right is the contribution.

**The canonical demonstrations.**

- **Mayer, Heiser & Lonn (2001)**, *Journal of Educational Psychology* 93(1):187, "Cognitive
  constraints on multimedia learning: When presenting more material results in less understanding,"
  [10.1037/0022-0663.93.1.187](https://doi.org/10.1037/0022-0663.93.1.187), **622 citations**
  (Crossref). `[biblio-only]` — **the abstract and effect sizes could not be retrieved this
  session.** APA abstracts are elided from the Semantic Scholar corpus and Crossref carries no
  abstract for this record. The bibliographic existence and citation count are verified; **the
  numbers are not**. Do not quote a d-value for this study in the survey without re-verification.
- **Kalyuga, Chandler & Sweller (1999)**, *Applied Cognitive Psychology*, "Managing split-attention
  and redundancy in multimedia instruction,"
  [10.1002/(sici)1099-0720(199908)13:4<351::aid-acp589>3.0.co;2-6](https://doi.org/10.1002/(sici)1099-0720(199908)13:4%3C351::aid-acp589%3E3.0.co;2-6),
  **401 citations**. The journal's own 2011 retrospective ([10.1002/acp.1773](https://doi.org/10.1002/acp.1773))
  describes it verbatim, `OBSERVED` `[verbatim]`: it *"investigated three major effects in
  multimedia instructional design simultaneously: split-attention, modality and the redundancy
  effect… Redundancy occurs when the two sources contain overlapping material. The study not only
  showed that split-attention could be avoided by modality effects (aligning pictures and spoken
  narrative) but also by directing the learner's attention through colour coding techniques.
  Interactions with redundancy were also identified."* Note what the retrospective says and does
  not say: redundancy *interacts*. It is not a law.

**Three retrieved results that do not replicate the simple rule.** All `MEASURED-RCT`, all
`[verbatim]` from ERIC.

1. **ERIC [ED638032](https://eric.ed.gov/?id=ED638032) (2014).** Teacher-education majors randomly
   assigned to (a) graphics + narration or (b) graphics + narration + **verbatim duplicated text**.
   *"The study results indicated that there was no significant difference between the group that
   received graphics and narration and the group that received graphics, narration, and text on the
   posttest scores, delayed posttest scores, and pedagogical usability perceptions."* **Null at
   immediate test and at six weeks.**
2. **ERIC [ED667496](https://eric.ed.gov/?id=ED667496) (2021).** Four narrated online lectures
   crossing temporal contiguity × verbal redundancy, ANCOVA on pretest. *"There was no significant
   difference in student achievement among the four treatment conditions. **This finding held true
   even when the analysis was limited to low-knowledge students.**"* The low-knowledge subgroup is
   precisely where cognitive-load theory predicts the effect should be *largest*. **Null.**
3. **Lee & Mayer-tradition L2 study, ERIC [EJ1264880](https://eric.ed.gov/?id=EJ1264880) (2018),
   *Applied Cognitive Psychology*.** Korean-speaking university students, 16-minute English video
   lesson, three conditions. *"On a comprehension test, the video + text group scored higher than
   each of the other two groups, **in contrast to the 'modality effect'**; and the video + narration
   + text group outscored the video + narration group, **in contrast to the 'redundancy effect'**.
   Each of the lessons that included text was rated as less difficult than the lesson with narration
   only."* **A double reversal**, in the population — second-language learners — that a global
   learning system is largest for.

**How to read this.** The redundancy effect is real in its original regime: native-language,
system-paced, transient narration, verbatim on-screen duplication, novice learners, short lab
lesson. Outside that regime it weakens, vanishes, or inverts. The meta-analytic estimate
(g = 0.15 overall, **g = 0.29 for adding text to audio**) already told us this and is routinely
mis-cited. B1 says it exactly right and the sentence should survive into the survey: *"the
'redundancy principle' as usually stated ('never duplicate') is wrong in one direction."*

### 2.4 The redundancy switch — a rule a generator can execute and a lecturer cannot

This is the concrete Part A deliverable that follows from §2.3. It is stated as a decision procedure
because that is what an IR can carry.

```
GIVEN slide S with narration N and on-slide text T:

IF   T would be a verbatim or near-verbatim restatement of N
AND  learner.language_status == L1_for_this_material
AND  learner.reading_support == off
AND  pacing == system_paced (video/live narration, learner cannot pause per-word)
AND  learner.hearing_access == unimpaired
THEN suppress verbatim T; retain keywords, labels, symbols, and any string
     the learner must READ EXACTLY (formulae, code, proper nouns, numbers).
     [basis: the redundancy regime; g = 0.15 overall but concentrated here]

ELSE present full T alongside N.
     [basis: EJ1264880 double reversal for L2; ED638032 and ED667496 nulls;
      Adesope & Nesbit text→audio g = 0.29 — adding text to audio HELPS on average]

NEVER add audio narration on top of pre-existing full text as an enhancement.
     [basis: Adesope & Nesbit audio→text g = -0.04 [-0.14, 0.06], n.s. —
      this direction buys nothing and costs channel capacity]

ALWAYS exempt from suppression: mathematical notation, code, chemical formulae,
     proper nouns, numerals, and any term the learner is expected to reproduce
     in writing. Spoken-only delivery of a symbol string is an accessibility
     failure regardless of what the redundancy literature says.
```

`INFERENCE`, derived from `MEASURED-META` and three `MEASURED-RCT` results. The switch is falsifiable
(§18, claim **B**) and — this must be said plainly — **the three retrieved nulls are a live risk to
it**. If the interaction does not appear, the honest conclusion is that the redundancy principle is
not worth encoding at all, and the generator should default to presenting text.

---

## 3. Generation technology: what actually produces a correct, non-decorative deck

### 3.1 The candidate targets, measured where measurable

GitHub API, retrieved 2026-07-27, `OBSERVED`. Star counts are popularity, not evidence about
learning; they are reported because they proxy for corpus size in pretraining data, which *is*
load-bearing for LLM-targetability.

| Target | Repo | Stars | Last push | License | Source form | LLM-targetable as declarative IR? |
|---|---|---:|---|---|---|---|
| **reveal.js** | `hakimel/reveal.js` | 72,036 | 2026-05-21 | MIT | HTML/Markdown sections | **Partially** — HTML is unbounded; the model can emit arbitrary layout. Good *renderer*, poor *IR*. |
| **Typst** | `typst/typst` | 55,118 | 2026-07-25 | Apache-2.0 | markup + scripting | **Yes** — typed, compiles, error messages are machine-readable. Newest; smallest training corpus. |
| **Remotion** | `remotion-dev/remotion` | 54,426 | 2026-07-27 | NOASSERTION | React/TSX | For *video* (A2's territory), not decks. |
| **Slidev** | `slidevjs/slidev` | 47,859 | 2026-07-22 | MIT | Markdown + YAML frontmatter, `---` separators, Vue components embeddable; exports PDF/PPTX/PNG/SPA (`[fetched-summary]` from sli.dev) | **Yes for the Markdown subset; no once Vue components appear** — the component escape hatch is exactly the "model computes layout" failure C1 prohibits. |
| **pandoc** | `jgm/pandoc` | 45,570 | 2026-07-25 | GPL-2.0 | AST-mediated conversion | **As infrastructure, yes** — pandoc's AST *is* a declarative IR and it is the thing Quarto sits on. |
| **manim (3b1b)** | `3b1b/manim` | 88,888 | 2026-07-17 | MIT | Python | A2's territory. Imperative; not a slide IR. |
| **manim (community)** | `ManimCommunity/manim` | 39,717 | 2026-07-26 | MIT | Python | A2's territory. |
| **impress.js** | `impress/impress.js` | 38,197 | 2026-07-23 | MIT | HTML + CSS3 transforms | **No** — spatial positioning is authored by hand. Prezi-style zoom is a coherence hazard. |
| **remark** | `gnab/remark` | 12,999 | **2024-06-19** | MIT | Markdown | Dormant ~2 years. Do not build on it. |
| **Quarto** | `quarto-dev/quarto-cli` | 5,884 | 2026-07-27 | NOASSERTION | Markdown + YAML; `##` → slide, `#` → section, `---` → untitled slide; outputs **revealjs / pptx / beamer**; executable code cells; citations, equations, diagrams (`[fetched-summary]` from quarto.org) | **Yes — the strongest fit.** One source, three renderers, executable cells, native citation and cross-reference machinery. |
| **Marp** | `marp-team/marp-cli` (3,718) + `marp-core` (1,128) | 4,846 combined | 2026-07-26 | MIT | *"a converter for Markdown"*, CommonMark base, *"Split pages by horizontal ruler (`---`). It's very simple!"*, directives + front-matter, exports **HTML/PDF/PPTX**, themes are **plain CSS** (`[fetched-summary]` from marp.app) | **Yes — the most constrained, therefore the safest.** The model cannot express layout; CSS themes own it. |
| **Beamer** | (LaTeX distribution, not a single repo) | — | — | LPPL | LaTeX `frame` environments | **Yes but heavy** — compiles, errors are checkable, huge training corpus, print-quality math. Slow, and PDF accessibility requires deliberate work. |

### 3.2 The ranking, and the reasoning behind it

C1 established the general principle from a measured result: ALGOGEN's decoupling of simulation from
rendering moved success from **82.5% → 99.8%** (arXiv:[2605.12159](https://arxiv.org/abs/2605.12159),
`MEASURED-BENCH`, per C1). **AutoPresent independently reproduces the same conclusion for slides
specifically**, in its own words (`MEASURED-BENCH` `[fetched-summary]`, arXiv:[2501.00912](https://arxiv.org/abs/2501.00912)):

> "We benchmark end-to-end image generation and program generation methods with a variety of models,
> and find that **programmatic methods produce higher-quality slides in user-interactable formats.**"

Two independent groups, two different artifact classes, same architecture. This is settled, and the
survey should say so without hedging.

**Tiering for slides, in the C1 style:**

- **Tier A — constrained declarative source, deterministic renderer owns layout: Marp, Quarto.**
  The model emits Markdown + frontmatter + a *figure spec per C1*. It cannot place a box. Theme CSS
  or the reveal/beamer engine owns geometry. Quarto adds executable cells (which is the F3 grounding
  hook: a plotted curve is *computed*, not drawn) and native citations (which is the provenance
  hook). Marp adds maximum constraint and PPTX export for institutions that require it.
- **Tier B — Typst.** Typed, fast, excellent errors, genuinely a compiler. Held below Tier A only
  because the training corpus is young and the accessibility story for its PDF output is
  less mature than Quarto→revealjs (HTML, where ARIA and reading order are first-class).
- **Tier C — reveal.js authored directly, Slidev with Vue components.** Fine as *render targets*,
  hazardous as *generation targets*, because both let the model author layout.
- **Tier D — model-authored raster slides; model-authored SVG; impress.js.** C1's prohibition
  transfers unchanged: **no raster text-to-image for any artifact containing text, numbers, arrows,
  or a spatial claim**; **no hand-written SVG paths**; **no model-computed layout coordinates**.
  A slide is a figure with more text on it, so the prohibition is strictly stronger here.

**Manim and Remotion** belong to A2 and are not slide targets. They enter C3 only through §5: when
the diagnostic response to a misconception is *a change over time*, the segment renderer may target
Manim — and only then, because A2's honest finding is that animation beats static pictures at
**g = 0.23 [0.12, 0.33]** overall, with **decorative animation at g = −0.05, n.s.** (Höffler &
Leutner, as recorded in A2, `MEASURED-META`). Animate the change; never animate the decoration.

---

## 4. DELIVERABLE (a) — the slide IR and the rules it must satisfy

### 4.1 What the IR is for

C1's argument: the LLM should emit a small, checkable, declarative spec, and a deterministic renderer
should draw. C3 adds the layer above: **the deck is a sequence of claims, each with at most one
figure, a text channel, a narration channel, and a probe.** The IR exists so that every principle in
§2 becomes a predicate rather than an instruction, and so that a generated deck can *fail a gate*
rather than merely *exist*.

### 4.2 The IR

```yaml
deck:
  id:            string
  learner_ref:   string           # links to the F5 learner model
  generated_at:  timestamp
  trigger:       lesson | diagnosis | learner_request
  provenance:    [source_id, ...] # F3 grounding; every claim traces here
  budget:
    slides:            int        # hard cap; coherence
    elements_per_slide: int       # hard cap; coherence
  channels:
    narration_mode:  audio | text | both
    redundancy_switch: on | off   # computed by the §2.4 procedure, NOT chosen by the model
  a11y_profile:
    language_status:  L1 | L2
    reading_support:  on | off
    hearing_access:   unimpaired | impaired
    reduced_motion:   bool
    prior_knowledge:  float       # gates signalling; expertise reversal

  slides:
    - id:        string
      claim:     string           # EXACTLY ONE proposition. This is the slide's reason to exist.
      evidence:  [source_id, ...] # non-empty
      figure:    <C1 figure spec> # Vega-Lite | Mermaid | DOT | PlantUML | GeoGebra |
                                  # trace-IR | TikZ-via-DiagramIR. NEVER raster. NEVER raw SVG.
      text:      [string, ...]    # short labels/keywords ONLY when redundancy_switch == on;
                                  # full prose permitted when it is off
      narration: string           # what is spoken
      exempt_strings: [string,...]# formulae/code/numerals never suppressed (§2.4)
      signal:
        target:  element_id
        channel: colour | weight | arrow | motion   # EXACTLY ONE
        gate:    "prior_knowledge < theta"
      alt:       string           # authored HERE, at generation time, from the spec
      reading_order: [element_id, ...]
      builds:                     # segmenting
        - {reveal: [element_id, ...], advance: learner}   # never timed
      checks:    [<assertion>, ...]
      probe:                      # round-trip; C1 §5.5
        question:    string
        answerable_from: this_slide_alone
        correct:     string
        distractors: [string, ...]
```

### 4.3 The gate — every predicate, with the evidence that licenses it

A deck that fails any **HARD** predicate is not rendered. A deck that fails a **SOFT** predicate is
rendered with a flag and queued for human review.

| # | Predicate | Type | Licensed by |
|---|---|---|---|
| 1 | `len(slide.claim.propositions) == 1` | HARD | segmenting g = 0.34; coherence g = 0.33 |
| 2 | `len(slide.elements) <= budget.elements_per_slide` | HARD | coherence; **persistent details g = 0.43 harm** |
| 3 | every element is referenced by `claim` or `narration` | HARD | coherence — unreferenced element is decoration or an unstated claim |
| 4 | `distance(label_bbox, referent_bbox) < τ` for all labels | HARD | spatial contiguity **g = 0.63** — largest checkable effect |
| 5 | no legend-only encoding when series ≤ 6 | HARD | spatial contiguity + colour accessibility |
| 6 | every distinction carries **two** channels (colour + shape/dash/position) | HARD | C1 §6.1 — only **7.2% (ChartX) / 33.3% (Text2Chart31)** of generated charts satisfied basic colourblindness guidance (arXiv:[2506.06175](https://arxiv.org/abs/2506.06175), `MEASURED-BENCH`, per C1) |
| 7 | `token_overlap(text, narration) <= τ` **iff** `redundancy_switch == on`; `exempt_strings` excluded | HARD | §2.4; g = 0.15 direction-dependent |
| 8 | `narration_mode != audio_added_to_existing_full_text` | HARD | audio→text **g = −0.04, n.s.** — costs channel capacity, buys nothing |
| 9 | exactly one `signal.channel` per slide | HARD | signalling g = 0.43 |
| 10 | `signal` emitted **only if** `prior_knowledge < theta` | HARD | Richter et al. r = 0.17 concentrated in low-prior-knowledge; expertise reversal |
| 11 | `alt` present, non-empty, authored from the spec (not from the raster) | HARD | WCAG 1.1.1; C1 §6.4 (MatplotAlt, arXiv:[2503.20089](https://arxiv.org/abs/2503.20089)) |
| 12 | `reading_order` defined and equals DOM/PDF tag order | HARD | WCAG 1.3.2 Meaningful Sequence |
| 13 | contrast ≥ 4.5:1 text, ≥ 3:1 non-text/UI | HARD | WCAG 1.4.3, 1.4.11 |
| 14 | no `builds` advance on a timer; no auto-advance | HARD | WCAG 2.2.1 Timing Adjustable; **segmenting: system-segmented g = 0.41 but time-on-task g = 0.92** — segment, don't rush |
| 15 | `reduced_motion == true` ⇒ builds collapse to a single static reveal | HARD | WCAG 2.3.3; `prefers-reduced-motion` |
| 16 | interactive targets ≥ 24×24 CSS px | HARD | WCAG 2.2 SC 2.5.8 |
| 17 | `evidence` non-empty for every slide | HARD | F3 grounding; provenance |
| 18 | `probe` answerable from the slide alone, verified by round-trip | SOFT | C1 §5.5 round-tripping |
| 19 | no decorative imagery with no referent | SOFT | coherence g = 0.33 |
| 20 | narration register personalised **only** for sessions < ~35 min | SOFT | personalization effects n.s. beyond ~35 min |

`INFERENCE` for the compilation of the gate; each row's *basis* is `MEASURED-META` or `OBSERVED`
(WCAG) as cited.

### 4.4 The two rules that matter most, stated as prose

**Rule 1 — one slide, one claim, one figure, one signal.** Everything in the gate is downstream of
this. It is also the enabling condition for the probe: if a slide asserts exactly one proposition,
a single atomic question can test whether that proposition landed, and the round-trip check becomes
authorable. Multi-claim slides are unprobeable, and unprobeable slides cannot be improved.

**Rule 2 — the model never places anything.** Not a box, not a label, not a colour, not a build
order that depends on geometry. The renderer and the theme own space. This is C1's finding
(82.5% → 99.8%) and AutoPresent's finding ("programmatic methods produce higher-quality slides")
arriving at the same place, and it is the single design decision that separates a system that can be
trusted at scale from a demo.

---

## 5. Slides as the artifact of a diagnosis, not a lecture

### 5.1 The reframe

The interesting future is not "generate a 30-slide deck about photosynthesis." That is a document
with a measured population effect of ~0.07. The interesting future is **one slide, generated in
under a conversational turn, because the learner just said something that revealed a specific wrong
model, and the fastest repair is contrastive and visual.**

This inverts every design assumption in §3–4 in one respect: the deck is not the unit. The **slide
is the unit**, and it is disposable.

### 5.2 What it requires — a component list

1. **Misconception detection that runs in-turn.** This exists as a research artifact:
   **"Misconception Diagnosis From Student–Tutor Dialogue: Generate, Retrieve, Rerank"**
   (arXiv:[2602.02414](https://arxiv.org/abs/2602.02414), `MEASURED-BENCH` `[fetched-summary]`) — a
   three-stage pipeline (fine-tuned LLM generates plausible misconceptions → embedding retrieval →
   fine-tuned reranker), evaluated on real tutoring-platform dialogues across LLaMA, Qwen and Claude
   in zero-shot and fine-tuned settings, with fine-tuning reported to beat larger closed models.
   **Specific accuracy numbers are not in the retrievable abstract and are not reported here.**
2. **A misconception → figure-template catalogue.** The mapping from "learner believes X" to "the
   figure that discriminates X from the correct model" must be **authored**, not generated. This is
   the same discipline H1 imposes: in special education, the AI's job is *fidelity and dosage of
   known-good intervention, not invention*. A misconception catalogue is a curriculum asset with a
   long shelf life; a per-turn improvisation is an unaudited claim.
3. **Contrastive rendering, not corrective assertion.** The template must render **both** models —
   what the learner's stated belief predicts, and what actually happens — side by side, with the
   discriminating case marked. This is Betty's Brain's architecture (F2 §3.3: the agent's errors are
   *traceable to the learner's own model*) ported from concept maps to figures. A slide that simply
   states the right answer is a correction; a slide that shows the learner's own model failing on a
   case they can check is a diagnosis.
4. **A latency budget the architecture can meet.** Template + parameter substitution + deterministic
   render is bounded and cacheable. Model-drawn pixels are not, and cannot be gated in-turn anyway.
   This is a second, independent argument for the declarative IR: **only a spec is fast enough to
   check before it is shown.**
5. **In-turn revisability.** Diagnosis is a hypothesis. If the learner's next utterance contradicts
   it, the figure must be replaceable without ceremony — which requires that it was never part of a
   "deck" in the first place.
6. **Logging into the learner model (F5).** A misconception that recurs across sessions is a
   different object from one that appears once. The figure is the intervention; the *record* is the
   asset.
7. **A confidence gate that prefers asking to asserting.** `INFERENCE`, and a strong one: C1's
   highest-value missing experiment is that *nobody has measured misconception acquisition from a
   wrong generated figure*, while ~6% of post-repair generated charts contained hallucinations
   (arXiv:[2506.06175](https://arxiv.org/abs/2506.06175), `MEASURED-BENCH`, per C1). A confidently
   wrong diagnostic figure teaches the misconception it was built to repair, and does so with
   visual authority. **Below a confidence threshold, the system asks a discriminating question
   instead of drawing.** A question that turns out to be unnecessary costs ten seconds. A wrong
   figure costs a semester.

### 5.3 Status

`INFERENCE` throughout. The components exist individually — misconception diagnosis
(arXiv:2602.02414), declarative figure generation (C1), fast deterministic renderers (§3) — and
**no retrieved work composes them into an in-turn diagnostic-visual loop, and no work measures
learning from one.** That is a specification, not a summary, and §18 states it as a falsifiable
claim.

---

## 6. The accessibility floor, and what auto-generated decks systematically get wrong

### 6.1 The floor

H1 §6.4 establishes **WCAG 2.2 Level AA** (W3C Recommendation, 12 December 2024,
[w3.org/TR/WCAG22](https://www.w3.org/TR/WCAG22/), `OBSERVED`) as this project's non-negotiable
floor, and notes that three of the 2.2 additions are aimed at cognitive accessibility. C3 inherits
that floor and adds the slide-specific operationalisation in the §4.3 gate.

### 6.2 What generated decks get wrong — and the honest epistemic status

**No study measuring the accessibility of AI-generated presentation decks was retrievable this
session.** arXiv searches for slide/PDF accessibility, alt text, reading order, and screen-reader
evaluation returned **zero results** (three separate queries). This is reported as
`OBSERVED — absence`, and it is itself a finding: the slide-generation literature surveyed in §7
contains **no accessibility metric of any kind**.

What *can* be asserted is the transfer from adjacent measured results:

1. **Colour-only encoding is the measured status quo and it fails.** Only **7.2% (ChartX)** and
   **33.3% (Text2Chart31)** of *machine-generated charts* satisfied basic colourblindness guidance
   (arXiv:[2506.06175](https://arxiv.org/abs/2506.06175), `MEASURED-BENCH`, via C1). A deck is
   mostly charts and boxes. There is no reason to expect the base rate to be better and every
   reason — more elements, more theme colours — to expect it to be worse. `INFERENCE` from
   `MEASURED-BENCH`.
2. **Alt text generated *after the fact* from a raster is the wrong architecture and is not safe
   unsupervised.** C1 records that the STEM alt-text survey (arXiv:[2607.21611](https://arxiv.org/abs/2607.21611))
   reports persistent factual inaccuracies and that evaluation relies on text-overlap metrics which
   *"poorly capture perceived usefulness and trust"* — and that **there is no accuracy figure that
   would license unsupervised deployment to a blind or low-vision learner**. The IR's answer
   (§4.2, predicate 11) is to author `alt` **from the spec at generation time**, where the semantic
   content is still present, rather than reverse-engineering it from pixels.
3. **Reading order is invisible to every quality metric in §7 and is the most common real-world
   failure.** A slide that reads correctly to the eye can traverse in an arbitrary order under a
   screen reader. Predicate 12 makes it explicit in the IR; nothing in the surveyed generation
   literature checks it. `INFERENCE`.
4. **Auto-advance and timed builds violate WCAG 2.2.1 and also violate the segmenting evidence.**
   System-segmented material beats learner-segmented (g = 0.41 vs 0.20) — but segmenting also raises
   time on task at **g = 0.92**. The resolution is: *the system decides where the boundaries are;
   the learner decides when to cross them.* Predicate 14. This is a rare case where the
   accessibility requirement and the learning-science requirement are the same requirement.
5. **The curb-cut restatement.** Every one of these fixes — two-channel encoding, authored alt text,
   defined reading order, learner-paced builds, exempted symbol strings — improves the deck for
   learners with no disability at all. Colour-plus-shape survives a greyscale printout. Authored alt
   text is a caption. Defined reading order is a coherent narrative. This is H1's thesis restated in
   C3's medium, and it is why the accessibility gate belongs in the *generation* path rather than a
   remediation pass.

---

## 7. What the slide-generation field actually measures — and the hole in the middle of it

### 7.1 A census

An exhaustive arXiv search for `"slide generation"` returned **39 results**, of which ~35 are
on-topic (`[fetched-summary]`, retrieved 2026-07-27). The corpus is recent and dense — 20 of the
on-topic entries are from 2025–2026. Selected, with what each measures:

| Paper | ID | What it measures |
|---|---|---|
| **AutoPresent / SlidesBench** | [2501.00912](https://arxiv.org/abs/2501.00912) | 7k train / 585 test from 310 decks, 10 domains; reference-based similarity **and** reference-free design quality; 8B Llama ≈ GPT-4o. `MEASURED-BENCH` `[fetched-summary]` |
| **PPTAgent / PPTEval** | [2501.03936](https://arxiv.org/abs/2501.03936) | Content, Design, Coherence — **an LLM-judge rubric**. `MEASURED-BENCH` `[fetched-summary]` |
| **PresentBench** | [2603.07244](https://arxiv.org/abs/2603.07244) | 238 instances, **average 54.1 binary checklist items per instance**, each *"formulated as a binary question"*; reports *"significantly stronger alignment with human preferences"* than prior methods; NotebookLM best. `MEASURED-BENCH` `[fetched-summary]` |
| **Learning to Present** | [2603.16839](https://arxiv.org/abs/2603.16839) | RL with an **inverse-specification reward** (an LLM tries to recover the original spec from the generated slides); Qwen2.5-Coder-7B + GRPO training **0.5% of parameters** reaches **91.2% of Claude Opus 4.6's quality**, **+33.1%** over base, on 48 business briefs. `MEASURED-BENCH` `[fetched-summary]` |
| **X+Slides** | [2606.19256](https://arxiv.org/abs/2606.19256) | Audience-conditioned generation; 113 topics, **8,133 probes**; Audience Coverage / Domain Coverage / Efficiency / **source-grounded Correctness**. At τ_A = 0.7: *"DeepPresenter reaches a best Audience Coverage of 0.714, SlideTailor reaches 0.594, and the NotebookLM ablation reaches 0.853."* `MEASURED-BENCH` `[fetched-summary]` |
| **OmniPresent / OmniPreBench** | [2607.02590](https://arxiv.org/abs/2607.02590) | Unified poster/slide/video suites via *"a renderable HTML representation"* and a *"self-correcting verify-and-repair loop"*; >1,000 papers; *"a rigorous VLM-based evaluation protocol"* — i.e. a **VLM judge**. `MEASURED-BENCH` `[fetched-summary]` |
| **SlideBot** | [2511.09804](https://arxiv.org/abs/2511.09804) | The only explicitly pedagogical entry: multi-agent, retrieval-grounded, **explicitly built on Cognitive Load Theory and CTML**, evaluated by *domain experts and students* in AI and biomedical education for *"conceptual accuracy, clarity, and instructional value."* **No numbers, sample sizes, or methodology in the retrievable abstract.** `DEMO` `[fetched-summary]` |
| **AeSlides** | [2604.22840](https://arxiv.org/abs/2604.22840) | RL on verifiable **aesthetic** metrics; human evaluation, **+7.6%** quality over baselines. `MEASURED-BENCH` `[fetched-summary]` |
| Others (DeepSlides, DeepSlide, ArcDeck, DECKBench, SlidesGen-Bench, PPTArena, PPTBench, SlideGen, SlideTailor, SlideCoder, PASS, DOC2PPT, D2S, SciBERTSUM, SlideSpawn, MemSlides, ECHO, Visual-SDPO, Paper2Video, PresentAgent-2, SynLecSlideGen) | various | Reference similarity (ROUGE), VLM/LLM judges, human preference, layout fidelity, editability, narrative flow, aesthetics. `[fetched-summary]` |

### 7.2 The finding

**Not one of the ~35 on-topic slide-generation papers measures whether a human learns anything from
the generated deck.** `OBSERVED — absence`, from an exhaustive listing of the arXiv `"slide
generation"` result set. The outcome variables are, in descending frequency: LLM/VLM judge scores,
human *preference* ratings, reference-similarity to an author's original deck, layout fidelity,
editability, and aesthetics.

This exactly reproduces A2's finding for animation and C1's for figures. Three independent
generation literatures, three identical holes. It is the strongest cross-cutting observation this
survey can make about the state of the field, and it should be stated once, loudly, and then used.

**Why it is worse here than for figures.** Reference-similarity to a human-authored deck is a
*regression to the g = 0.067 baseline*. Author-made decks are, on average, worth nothing measurable.
Optimising toward them optimises toward nothing. And human *preference* is the metric A2 identified
as actively adversarial: learners systematically prefer and rate as more comprehensible material
they learn no more from — a metacognitive illusion (A2 §0, `MEASURED-META`). **A slide generator
RLHF'd on preference is being trained on the illusion.** AeSlides' explicit optimisation of
*aesthetics* by RL is the clearest instance in the corpus, and its **+7.6% human-rated quality gain
is not evidence of a learning gain** — it is `MEASURED-BENCH` for aesthetics and silent on learning.

### 7.3 Two things the field got right, and one it should stop doing

**Right #1 — PresentBench's decomposition.** *"An average of 54.1 checklist items per instance, each
formulated as a binary question."* This is the correct move and it generalises far beyond slides: a
holistic 1–5 rubric score from an LLM is unreliable; **the same LLM answering 54 independent binary
questions is a different and better instrument**, because errors are independent, items are
auditable, and the aggregate is a count rather than a judgement. That PresentBench reports
*"significantly stronger alignment with human preferences"* than holistic methods is consistent with
this. It is also the design pattern behind §13's answer to the explanation-scoring problem.

**Right #2 — X+Slides' source-grounded Correctness dimension.** Verifying content against the source
rather than against a judge's impression is the only dimension in the corpus that measures a
*property of the world*. Its conclusion — *"visual presentation quality shouldn't substitute for
rigorous source-grounded evaluation"* — is the field policing itself correctly.

**Stop doing — VLM-judge-only evaluation.** OmniPresent's *"rigorous VLM-based evaluation
protocol"* is the dominant pattern and it is the pattern this project has measured to fail. In this
project's own coding-agent selection benchmark: selection by **public tests +8.14pp**, by
**generated tests +2.70pp**, by **LLM judge alone −3.20pp / −1.68pp** (`artifacts/README.md`,
`MEASURED-BENCH`, in-project). Judge-only selection was **negative**. That result was obtained on
code, where correctness is unusually well-defined; there is no reason to expect judges to do better
on slides, where it is not.

---

# PART B — The learner as presenter

> **Boundary with F2.** F2 owns *the AI as tutee* — teachable agents, capability leakage, Betty's
> Brain, sycophancy destroying the protégé effect. C3 owns *the learner as presenter*: what triggers
> the presentation, who or what is in the room, what the learner produces, and how it is scored. The
> two sections share one literature and answer different questions from it. Where F2 asks "what
> should the agent be?", C3 asks "what should the human do, and how do we know it worked?"

## 8. The effect sizes, verified — and two corrections

The brief for this section carried two numbers from prior project work and asked for verification.
**Both numbers are correct. Both attributions were wrong.** Correcting them matters, because the
mis-attribution points builders at the wrong mechanism.

### 8.1 g = 0.56 — correct number, wrong source

**It is not a teachable-agent effect size. It is a human learning-by-teaching effect size.**

**Kobayashi (2019)**, *Japanese Psychological Research*,
[10.1111/jpr.12221](https://doi.org/10.1111/jpr.12221), 71 citations. Meta-analysis, **28 studies**.
`MEASURED-META` `[verbatim]` (Crossref-deposited abstract):

> "The synthesis of 28 studies indicated that the estimated effect sizes (Hedges' *g*s) were **0.35
> for preparing-to-teach** and **0.56 for teaching with preparing-to-teach**. Both preparing-to-teach
> and teaching with preparing-to-teach were effective in promoting **deep learning** (as well as
> surface learning) and **even after a delay**. The learning benefits of teaching with
> preparing-to-teach were **larger when students expected and engaged in an interactive teaching
> activity than when they expected and engaged in a non-interactive teaching activity**. The mere
> expectation of interactive teaching also produced larger learning effects than the expectation of
> non-interactive teaching."

The comparison condition is *mere studying without teaching expectancy*. The participants are human
learners teaching human recipients. **No teachable agent appears in this meta-analysis.** F2 cites
it correctly; the brief's restatement as "g = 0.56 for teachable agents" is the error, and it is a
consequential one — it would license transferring a human-to-human effect size onto an AI tutee,
which F2 explicitly warns against ("g = 0.56 is not [established for AI tutees]").

### 8.2 g = 0.43 — correct number, and here is where it comes from

**Leung (2018/2019)**, *School Psychology International*,
[10.1177/0143034318808832](https://doi.org/10.1177/0143034318808832), 60 citations,
"An updated meta-analysis on the effect of peer tutoring on **tutors'** achievement."
`MEASURED-META` `[verbatim]`:

> "Meta-analyses on the effect of peer tutoring have rarely examined the effect of peer tutoring on
> tutors' academic gain… The present meta-analytic study examined **16 articles**… **It was found
> that the weighted mean effect size was 0.43 (p < 0.001).** Moreover, the crucial parameters for
> optimizing the effectiveness of peer tutoring interventions are identified as follows: Tutees with
> low academic ability; tutors coming from secondary school; **fewer tutor training sessions per
> week; shorter tutor training time per session**; choosing mathematics as subject content; random
> assignment of tutees and tutors; **structured** peer tutoring; **same-age non-reciprocal** peer
> tutoring; same-sex dyad grouping; and **more weekly tutoring sessions but longer tutoring time for
> each session**."

So: **0.43 is the tutor's own achievement gain from peer tutoring**, k = 16. It is a *different
construct* from Kobayashi's 0.56 (which is a single teaching episode after expectancy-framed study).
Caveats worth carrying: k = 16 is small, no CI is reported in the abstract, and the moderator list
is long relative to k — treat the moderators as hypothesis-generating rather than established.

The historical anchor is consistent: **Cohen, Kulik & Kulik (1982)**, *AERJ*,
[10.3102/00028312019002237](https://doi.org/10.3102/00028312019002237), 673 citations, 65
independent evaluations, `MEASURED-META` `[verbatim]`: *"The meta-analysis also showed that tutoring
programs have positive effects on children who serve as tutors. Like the children they helped, the
tutors gained a better understanding of and developed more positive attitudes toward the subject
matter… Participation in tutoring programs had **little or no effect, however, on the self-esteem of
tutors and tutees**."* Forty-four years old and it already contains a null: the confidence story
that "presenting builds confidence" was not supported then and should not be assumed now.

### 8.3 The consolidated table

| Construct | Estimate | k | Source | Label |
|---|---|---:|---|---|
| Preparing to teach (expectancy only, no delivery) | **g = 0.35** | 28 | Kobayashi 2019 | `MEASURED-META` |
| Preparing to teach + delivering | **g = 0.56** | 28 | Kobayashi 2019 | `MEASURED-META` |
| Teaching after prep, pooled over expectancy conditions | **g = 0.27 [0.15, 0.39]** | 39 | Kobayashi 2024 | `MEASURED-META` |
| Teaching after prep **with** teaching expectancy | **g = 0.48 [0.34, 0.63]** | 39 | Kobayashi 2024 | `MEASURED-META` |
| Teaching after prep **without** teaching expectancy | **g = −0.02 [−0.14, 0.11]** | 39 | Kobayashi 2024 | `MEASURED-META` **null** |
| Delivery's increment over expectancy-framed study alone | **g = 0.38 [0.17, 0.60]** | 14 | Kobayashi 2024 | `MEASURED-META` |
| Peer tutoring — the **tutor's** achievement | **0.43**, p < .001 | 16 | Leung 2018 | `MEASURED-META` |
| Induced self-explanation | **g = 0.55** (69 ES from 64 reports) | 64 | Bisra et al. 2018 | `MEASURED-META` |
| Worked examples on maths performance | **g = 0.48**, p = 0.01 (181 ES, 55 studies) | 43 | Barbieri et al. 2023 | `MEASURED-META` |
| Worked examples **+ self-explanation prompts** vs without | **significantly negative moderator** | 43 | Barbieri et al. 2023 | `MEASURED-META` **negative** |

---

## 9. Preparation or delivery? The literature has an answer, and it is recent and sharp

This was the brief's key design question — *if expectancy suffices, an audience is optional; if
delivery is required, the system must produce a real audience.* The answer turns out to be neither
of the two options offered, and it is better than both.

### 9.1 The decisive meta-analysis

**Kobayashi (2024)**, *Educational Psychology Review*,
[10.1007/s10648-024-09871-4](https://doi.org/10.1007/s10648-024-09871-4), ERIC
[EJ1414484](https://eric.ed.gov/?id=EJ1414484). `MEASURED-META` `[verbatim]`, retrieved in full from
ERIC:

> "A meta-analysis of **39 studies** revealed that a weighted mean effect size for the effect of
> teaching after studying with or without teaching expectancy vs. merely studying without teaching
> expectancy on one's learning was **g = 0.27, 95% CI [0.15, 0.39]**. **Most importantly, teaching
> vs. no teaching expectancy significantly moderated the learning effect of teaching:** The learning
> benefit of teaching after studying **with** teaching expectancy was nearly medium, **g = 0.48, 95%
> CI [0.34, 0.63]**, whereas that of teaching after studying **without** teaching expectancy **did
> not significantly differ from zero, g = −0.02, 95% CI [−0.14, 0.11]**. This moderator effect was
> independent of the effects of two possible confounding factors: comparison treatment (the use of a
> sophisticated or unsophisticated learning strategy) and teaching mode (teaching in written or
> unwritten mode). **An additional meta-analysis of 14 studies** also found that the effect of
> teaching after studying with teaching expectancy vs. **merely studying with teaching expectancy**
> on one's learning was significantly greater than zero, **g = 0.38, 95% CI [0.17, 0.60]**, ruling
> out the possibility that the effectiveness of learning by teaching after studying with teaching
> expectancy is entirely attributable to the learning effects of preparing to teach… **These findings
> suggest that preparing to teach catalyzes learning by teaching.**"

### 9.2 What this means for a system, stated as an ordered claim

1. **Expectancy is a *precondition*, not an alternative.** Teaching after study that was not framed
   by a teaching expectation produced **g = −0.02**. Grabbing a learner after a lesson and saying
   "now explain it back to me" is, on the meta-analytic evidence, **worth nothing**. This is the
   most common way AI tutors implement "explain it back," and it is the wrong one.
2. **Delivery is *not* redundant with expectancy.** The k = 14 sub-analysis holds expectancy
   constant on both sides and still finds **g = 0.38 [0.17, 0.60]** for actually delivering. So
   "just tell them they'll have to teach it and skip the teaching" leaves a medium effect on the
   table.
3. **Therefore the loop is ordered and both halves are load-bearing:** announce the obligation →
   study under it → deliver. Removing the announcement zeroes the effect. Removing the delivery
   costs ~0.38.
4. **Teaching mode — written vs unwritten — was explicitly tested as a confound and did not explain
   the moderator effect.** That is the first of three independent results (see §10.3, §14.3) saying
   the *modality* of delivery is not where the value is. It has direct accessibility consequences.

### 9.3 The corroborating and complicating primary studies

- **Nestojko, Bui, Kornell & Bjork (2014)**, *Memory & Cognition*,
  [10.3758/s13421-014-0416-z](https://doi.org/10.3758/s13421-014-0416-z), PMID 24845756, 80
  citations. `MEASURED-RCT` `[verbatim]` via Europe PMC: participants studied passages expecting a
  test or expecting to teach; *"In reality, all participants were tested, and **no one actually
  engaged in teaching**. Participants expecting to teach produced more complete and better organized
  free recall of the passage (Experiment 1) and, in general, correctly answered more questions about
  the passage than did participants expecting a test (Experiment 1), particularly questions covering
  main points (Experiment 2)."* **Expectancy alone, with delivery removed by design, produced a
  benefit.** Two experiments; no effect sizes in the abstract.
- **Daou et al. (2016)**, *Journal of Motor Learning and Development*,
  [10.1123/jmld.2015-0036](https://doi.org/10.1123/jmld.2015-0036), and *Human Movement Science*,
  [10.1016/j.humov.2016.08.009](https://doi.org/10.1016/j.humov.2016.08.009). `MEASURED-RCT`
  `[verbatim]`: golf putting, expectancy-to-teach vs expectancy-of-test, learning assessed one day
  later. *"Results revealed that expecting to teach enhanced learning, even after controlling for
  the amount of studying and practicing."* The effect generalises beyond declarative material to
  perceptual-motor skill — which matters for any domain where the AI system's target is a procedure.
- **Fiorella & Mayer (2013)**, *Contemporary Educational Psychology*,
  [10.1016/j.cedpsych.2013.06.001](https://doi.org/10.1016/j.cedpsych.2013.06.001), **269
  citations**, and **(2014)**, [10.1016/j.cedpsych.2014.01.001](https://doi.org/10.1016/j.cedpsych.2014.01.001).
  `[biblio-only]` — **Elsevier returned HTTP 403 and both abstracts are elided from the Semantic
  Scholar corpus; neither was retrievable this session.** F2 records their finding as: teaching
  expectancy alone helps on immediate tests, but **actually teaching is required for delayed
  retention and transfer**; expectancy effects decay, teaching effects do not. That claim is carried
  from F2's earlier retrieval, is *consistent with* Kobayashi 2024's k = 14 result, and should be
  re-verified before it appears with a number attached.

**The apparent tension between Nestojko (expectancy alone works) and Kobayashi 2024 (delivery without
expectancy is zero) is not a tension at all.** They are different contrasts. Nestojko removes
delivery and keeps expectancy — the gain survives. Kobayashi removes expectancy and keeps delivery —
the gain vanishes. Both point the same way: **the preparation, framed by the obligation, is where the
learning happens; the delivery consolidates it.** That is a clean, non-obvious, and immediately
actionable design finding.

---

## 10. Who should be in the room? The audience result

### 10.1 The primary experiment

**Wang, Cheng & Mayer (2023)**, *Journal of Educational Psychology*, ERIC
[EJ1386593](https://eric.ed.gov/?id=EJ1386593), "Improving Learning-by-Teaching without Audience
Interaction as a Generative Learning Activity by Minimizing the Social Presence of the Audience."
`MEASURED-RCT` `[verbatim]`:

> "College students watched a multimedia lesson on chemical synaptic transmission with instructions
> that afterward they would explain the materials by making a lecture video (**teach-to-camera**),
> explain to a student face-to-face (**teach-to-student**), or explain to seven students face-to-face
> (**teach-to-group**)… **Compared to the other two groups, the teach-to-camera condition performed
> significantly better on a transfer test, reported significantly lower social presence, experienced
> significantly lower arousal as measured by pulse rate, and engaged in significantly more generative
> processing via quality explanations, which were measured by a number of idea units, elaboration
> statements, and monitoring statements.** The teach-to-camera condition significantly outperformed
> the teach-to-group condition on a retention test and reported significantly lower state anxiety,
> teaching difficulty, and cognitive load during teaching… **The relation between audience presence
> and learning outcome was mediated by the negative impacts of distraction during teaching (e.g.,
> anxiety or extraneous cognitive load ratings) and the positive impacts of generative processing
> during teaching (e.g., number of idea units generated).**"

Note the quality of this evidence: a three-level manipulation of audience presence, an *objective*
physiological measure (pulse rate) confirming the arousal mechanism, *behavioural* measures of
explanation quality, and a **tested mediation model**. This is not a preference study.

### 10.2 The replication and extension

**Cheng, Wang & Mayer (2023)**, *Journal of Computer Assisted Learning*, ERIC
[EJ1391980](https://eric.ed.gov/?id=EJ1391980). `MEASURED-RCT` `[verbatim]`. Two experiments:

> "In Experiment 1, college students received a lesson with instructions that afterwards they would
> explain the material to others by making a video, explain the material aloud to themselves, or
> restudy the material. In Experiment 2, college students viewed a multimedia lesson with
> instructions that afterwards they would explain the materials by making a video, explain to an
> onscreen student, or explain to a student in person. **Results: Teaching by making a video was
> better than restudying, self-explaining, and teaching face-to-face or online. Teaching quality was
> better in video teaching than self-explaining and face-to-face or online teaching.** Teaching by
> making a video is ideal because it **primes generative processing while minimizing extraneous
> processing**."

Experiment 2 includes an **onscreen student** condition — the closest thing in the retrieved
literature to a mediated/virtual audience — and video teaching beat it too. This is important and
slightly awkward for the "AI audience" thesis: an *onscreen human* was worse than no audience.
The distinction that saves the thesis is that an onscreen student still carries social evaluation
while contributing no interrogation — the worst cell of the 2×2. But that distinction is an
`INFERENCE`, not a measurement, and §12 says so.

### 10.3 The finding that makes accessibility fall out for free

**Lim, Wong & Lim (2021)**, *Applied Cognitive Psychology*, "The 'Silent Teacher': Learning by
Teaching via Writing a Verbatim Teaching Script," ERIC [EJ1315998](https://eric.ed.gov/?id=EJ1315998),
**N = 108**. `MEASURED-RCT` `[verbatim]`:

> "Learners studied a science text on the Doppler effect using one of three learning methods: (1)
> generating and studying their own notes (restudying control), (2) preparing to teach and then
> verbally teaching (verbal teaching), or (3) preparing to teach and then writing a verbatim teaching
> script (silent teaching). **On a conceptual knowledge retention test 1 week later, participants who
> wrote teaching scripts performed as well as those who taught verbally; both teaching groups
> outperformed control learners.** Verbal and silent teaching significantly **increased social
> presence and elaboration to comparable extents**, relative to restudying."

**A written teaching script is as good as speaking.** At one week. With comparable elaboration. This
is the third independent result — with Kobayashi 2024's "teaching mode (written or unwritten)" null
moderator and Wang/Mayer's camera result — saying that **the value is in the generative act, not the
performance.** §14 turns this into a design rule with real consequences for SELPA learners.

### 10.4 The tension with "interactivity", and its resolution

Kobayashi 2019: *"benefits were larger when students expected and engaged in an **interactive**
teaching activity."* Wang & Mayer 2023: the *least* interactive condition (a camera) won.

These are not contradictory because they manipulate different variables. Kobayashi's moderator is
about being **questioned** — the tutee's confusion forcing knowledge-building rather than
knowledge-telling (Roscoe & Chi, per F2 §3.2). Mayer's manipulation is about being **watched** —
social presence, arousal, evaluative threat. A human audience delivers both at once and the
literature has never separated them, because until recently there was no way to.

> **The 2×2 nobody has run:**
>
> |  | **Low social evaluation** | **High social evaluation** |
> |---|---|---|
> | **High interrogation** | ← *the target cell. Empty.* | ordinary classroom presentation |
> | **Low interrogation** | teach-to-camera (Wang & Mayer: best measured) | onscreen student (Cheng et al.: worse) |
>
> Three of four cells have data. The fourth — persistent, specific interrogation with no evaluative
> stake — is exactly and only what a machine audience can occupy.

`INFERENCE`, and the central design claim of Part B. Stated falsifiably as claim **D** in §18.

---

## 11. Explanation quality versus quantity

### 11.1 The positive pooled estimate

**Bisra, Liu, Nesbit, Salimi & Winne (2018)**, *Educational Psychology Review*,
[10.1007/s10648-018-9434-x](https://doi.org/10.1007/s10648-018-9434-x), ERIC
[EJ1186664](https://eric.ed.gov/?id=EJ1186664), **210 citations**. `MEASURED-META` `[verbatim]`:

> "Our systematic search of relevant bibliographic databases identified **69 effect sizes (from 64
> research reports)** which met certain inclusion criteria. **The overall weighted mean effect size
> using a random effects model was g = 0.55.** We coded and analyzed 20 moderator variables… We
> found that self-explanation prompts are a potentially powerful intervention across a range of
> instructional conditions. **Due to the limitations of relying on instructor-scripted prompts, we
> recommend that future research explore computer-generation of self-explanation prompts.**"

The brief asked for the pooled g. It is **0.55**, not 0.56. The 95% CI is not stated in the ERIC
abstract and could not be retrieved (Springer redirected to an IdP login); **do not quote a CI**.

Note the authors' own closing recommendation — computer-generated self-explanation prompts. That is
a 2018 request that a 2026 system can straightforwardly satisfy, and it is a rare case where the
meta-analysts explicitly asked for the thing this survey is about.

### 11.2 The negative that must be reported in the same breath

**Barbieri et al. (2023)**, *Educational Psychology Review*, "A Meta-Analysis of the Worked Examples
Effect on Mathematics Performance," ERIC [EJ1364058](https://eric.ed.gov/?id=EJ1364058). 43 articles,
55 studies, **181 effect sizes**, robust variance estimation. `MEASURED-META` `[verbatim]`:

> "The average effect size of worked examples on mathematics performance outcomes was medium with
> **g = 0.48 and p = 0.01**… **The inclusion of self-explanation prompts significantly moderated the
> effect of examples yielding a negative effect in comparison to worked examples conditions that did
> not include self-explanation prompts.** Worked examples studies that used correct examples alone
> yielded larger effect sizes than those that used incorrect examples alone or correct examples in
> combination with incorrect examples… Correct examples are particularly beneficial for learning
> overall, and **pairing examples with self-explanation prompts may not be a fruitful design
> modification.**"

Two meta-analyses, five years apart, in the same journal: one finds inducing self-explanation is
worth g = 0.55; the other finds that adding self-explanation prompts to worked examples makes them
*worse*. The reconciliation is almost certainly **prompt quality and time cost** — self-explaining
consumes study time, and a prompt that elicits a shallow restatement has spent time to buy nothing.
But the reconciliation is `INFERENCE`. **The survey must report the tension, not resolve it by
picking the flattering number.**

### 11.3 Low-quality explanation is worse than none — measured

**Journal of Educational Psychology (2026)**, "The Impact of Incorrect Self-Explanation Prompt
Responses on Fifth-Grade Mathematics Learning," ERIC [EJ1507394](https://eric.ed.gov/?id=EJ1507394).
`MEASURED-RCT` `[verbatim]`:

> "Results indicate that frequent engagement with self-explanation prompts positively impacted
> students' mathematics learning. Furthermore, while the most common student errors were mistakes
> and a lack of precision, **incorrectly answering the prompts, regardless of the type of error,
> negatively impacted learning**. Finally, **incorrectly responding to prompts paired with incorrect
> examples negatively impacted learning, while those paired with correct examples did not.** …
> emphasizing that **the quality of self-explanations directly impacts the learning outcomes** …
> [and] exploring the impact of **reading level** on self-explanation quality."

This is the brief's requested finding, measured, in children, with the error taxonomy. Three
consequences for a system that asks learners to explain:

1. **An unmonitored explanation prompt is a coin flip.** Frequency helps; incorrectness hurts. A
   system that prompts and never checks is running both effects simultaneously and cannot know which
   dominates.
2. **The interaction with example correctness is a hard design constraint.** Incorrect
   self-explanation *paired with an incorrect worked example* was harmful; paired with a *correct*
   example it was not. So the "learn from errors" pattern — showing a wrong worked example and asking
   the learner to explain the flaw — is the highest-risk configuration in the whole family, and must
   not be used without verification of the learner's explanation.
3. **Reading level modulates explanation quality**, which the authors call out explicitly. This is
   the H1 population, and it says that an explanation-heavy pedagogy has a built-in equity gradient
   unless the system supports the production side.

---

## 12. Presenting to an AI audience versus a human audience: the honest answer

**No study measuring learning outcomes from a human learner presenting to an AI audience, compared
against a human audience, was retrievable this session.** `OBSERVED — absence`.

Search routes attempted and their results:
- arXiv full-text search, "learning by teaching large language model student explain" — no relevant
  human-learner studies; results were all LLM-teaches-LLM.
- arXiv full-text search, "learning by teaching chatbot teachable agent human participants learning
  gains" — **zero results** returned by arXiv.
- ERIC, `"teachable agent" AND chatbot` — **zero records**.
- ERIC, `"learning by teaching" AND (ChatGPT OR "large language model")` — **two records**, neither
  a human-vs-AI audience comparison.

**The closest existing evidence, and why it does not answer the question:**

- **Chen, Wei, Le et al. (2025)**, *BJET*, ERIC [EJ1493482](https://eric.ed.gov/?id=EJ1493482),
  "Learning by Teaching with ChatGPT: The Effect of Teachable ChatGPT Agent on Programming
  Education." `MEASURED-RCT` `[verbatim]`: *"Teaching ChatGPT improved students' knowledge gains and
  programming abilities, particularly in writing readable and logically sound code. **However, its
  impact on error-correction skills was limited, likely due to ChatGPT's tendency to generate correct
  code, thus reducing debugging opportunities.** Notably, students' self-regulated learning (SRL)
  abilities improved."* This measures **teaching an AI tutee**, not **presenting to an AI audience**,
  and it has no human-audience control arm. F2 owns it, and rightly reads it as the clearest
  published demonstration of capability leakage breaking the tutee role.
- **Cheng, Wang & Mayer (2023) Experiment 2** contains the nearest thing to a mediated audience — an
  *onscreen student* — and video-with-no-audience beat it. But the onscreen student was a **human**,
  and the design does not separate interrogation from evaluation.
- **Wang et al. (2025)**, CHI EA, [10.1145/3706599.3719863](https://doi.org/10.1145/3706599.3719863),
  teachable agents for children's pronunciation with a Phoneme-level Mispronunciation Projection
  method; pilot, **27 children aged 7–9**; reports perceived performance, motivation to teach, and a
  virtual-vs-physical-robot embodiment comparison favouring the physical robot for engagement.
  `DEMO` `[verbatim]` — a pilot with no learning-outcome control.

**Stating the absence plainly is the finding.** The single most-asked design question about
AI-mediated learning-by-teaching — *does it matter that the audience is a machine?* — has no
measured answer. Given that Wang & Mayer 2023 gives a complete measurement apparatus (transfer test,
retention test, pulse rate, state anxiety, cognitive load, idea-unit counts) and a validated
three-level comparison, **adding a fourth arm is a small, cheap, high-yield replication that
somebody should run immediately.**

---

## 13. Scoring an explanation without an unreliable judge

### 13.1 Why the two obvious answers both fail

**LLM-as-judge fails, measured.** In this project's own selection benchmark: **public tests
+8.14pp**, **generated tests +2.70pp**, **LLM judge alone −3.20pp / −1.68pp** (`artifacts/README.md`,
`MEASURED-BENCH`, in-project). Judge-only selection was *worse than not selecting*. And this was on
code, where correctness is comparatively well-defined.

**Falling back to human graders also fails, measured.** Human graders of programming assignments
reached **Krippendorff's α ≈ 0.20 on correctness** and **< 0.10 on style dimensions**, and **only 1
of 22 reproduced their own grade on a hidden duplicate** — leading the authors to write that *"the
idea of a 'gold standard' of human grading might be flawed"* (Messer, Brown, Kölling & Shi 2025,
*ACM TOCE*, ERIC [EJ1488833](https://eric.ed.gov/?id=EJ1488833), `MEASURED-BENCH`, per C2 §N3).

So the question is not "judge or human." It is **what about an explanation is checkable at all.**

### 13.2 Four things that are checkable, in ascending order of strength

**(1) Idea-unit coverage against a pre-authored reference decomposition.** This is not a proposal —
it is the instrument Wang, Cheng & Mayer used, and it is the instrument that **mediated their
learning effect**: *"quality explanations, which were measured by a number of **idea units**,
**elaboration statements**, and **monitoring statements**."* Three counts. Each is a
classification against a *fixed key*, not an open-ended judgement, which is the regime where
automated scoring is reliable. Concretely:

- Author, per lesson, a reference decomposition: the **N propositions** a complete explanation must
  contain (this is the same asset as the slide `claim` list from §4.2 — one deck, one decomposition).
- Score coverage = |propositions the learner's explanation entails| / N. Entailment against a fixed,
  short, pre-written proposition is a far narrower task than holistic quality rating.
- Count elaborations (statements adding a causal link, an analogy, or a boundary condition not in
  the source) and monitoring statements (explicit comprehension checks: "wait, that doesn't work
  because…"). Both are surface-detectable and both are established as predictive.
- **Report counts, never a 1–5 score.** This is PresentBench's move (§7.3): 54.1 binary items beat a
  holistic rubric and aligned better with humans.

**(2) The explanation as an executable prediction.** The strongest form, and F3's territory. An
explanation asserts a mechanism; a mechanism makes predictions; predictions can be run.

- If the learner explains why a loop terminates, extract the stated variant and **check that it
  decreases** and is bounded below.
- If the learner explains a chemical equilibrium, extract the stated direction of shift and
  **evaluate it against the model** for a perturbation they did not see.
- If the learner explains a statistical result, extract the stated relationship and **check its sign
  and limiting behaviour** against the fitted model.
- If the learner explains an algorithm, **instantiate their description as a trace IR** (C1's
  ALGOGEN pattern) and run it on held-out inputs.

The scoring signal is then a **test result**, not an opinion. This is precisely the +8.14pp arm of
the project's own benchmark, ported from code selection to explanation scoring.

**(3) Consequence-scoring via a capped tutee.** Hand the learner's explanation to an agent whose
capability is capped, and require it to **act** on the explanation on a task with an objective
answer key. Score the learner by the tutee's downstream accuracy. This is Okita & Schwartz's
recursive feedback (F2 §3.3) turned into a metric, and it inherits the same virtue: the tutee is
graded by tests, so no judge enters the loop. **The engineering risk is F2's capability leakage** —
a frontier model instructed to be ignorant drifts toward competence, and Chen et al. 2025 measured
exactly that failure. So the cap must be architectural (a genuinely small model, a restricted
toolset, a retrieval corpus limited to what the learner supplied), never a prompt.

**(4) The learner's own delayed transfer test.** The criterion, not a proxy. Everything above is
instrumentation that exists to make (4) improvable between administrations. Report (4); use (1)–(3)
to steer.

### 13.3 What is explicitly forbidden

- A holistic LLM rubric score reported to the learner or used to gate progression. `MEASURED-BENCH`
  against it, in-project.
- Any evaluation on which the *presentation* is scored for polish, delivery, confidence, or
  aesthetics. Cohen et al. 1982 found no self-esteem effect; Blöte et al. 2010 (§14.2) found that
  in real classrooms, **speech quality was negatively related to peer behaviour**. There is no
  evidence base licensing an AI to grade a child's poise.
- Preference-based optimisation of explanation quality. A2's metacognitive-illusion finding applies
  identically: learners prefer explanations they learn less from.

---

## 14. Speech anxiety and the SELPA question: accommodation or barrier?

The brief asked that this be treated seriously rather than assumed. It resolves cleanly, and the
resolution is good news.

### 14.1 The mechanism is measured, and it is a working-memory mechanism

**Haucke, Golde & Heinzel (2025)**, *Scientific Reports*,
[10.1038/s41598-025-22611-0](https://doi.org/10.1038/s41598-025-22611-0), N = 57 (30 high socially
anxious, 27 low; 13 with diagnosed SAD). `MEASURED-RCT` `[verbatim]` via Europe PMC:

> "We developed the Socio-evaluative N-back Task (SENT), which can measure the impact of acute
> socio-evaluative stress on working memory (WM) performance… **The socio-evaluative stress
> condition, compared to a control condition, increased psychophysiological stress reactions, and
> reduced WM performance.** Moreover, people with low anxiety displayed faster reaction times under
> socio-evaluative stress compared to a control condition. Conversely, individuals with h[igh
> anxiety]…" *(abstract truncated at retrieval; the high-anxiety branch is not quoted here because
> the sentence was cut off. Do not attribute a direction to it without re-verification.)*

This is the mechanism underneath Wang & Mayer's pulse-rate finding. **Social-evaluative threat
consumes working memory.** Learning-by-teaching's benefit runs through *generative processing*,
which is working-memory-hungry. So an evaluative audience taxes exactly the resource the intervention
depends on. H1 records the parallel effect for maths anxiety: **r = −0.168** across 57 studies / 150
effect sizes, with working memory as the mediating pathway (Finell et al. 2022,
[10.3389/fpsyg.2021.798090](https://doi.org/10.3389/fpsyg.2021.798090), `MEASURED-META`, per H1).

### 14.2 The classroom reality is worse than "some students are nervous"

**Blöte et al. (2010)**, *Journal of Youth and Adolescence*, ERIC
[EJ901204](https://eric.ed.gov/?id=EJ901204). Classroom observations during **real oral
presentations**, 94 students aged 13–18. `MEASURED-RCT`/observational `[verbatim]`:

> "Findings showed that the **social performance** of socially anxious students was a predictor of
> class behavior, whereas their **overt nervousness was not**. **Surprisingly, the quality of their
> speech was negatively related to class behavior.**"

Read that last clause carefully. In an actual classroom, **speaking well predicted worse treatment
by peers.** Whatever "give a presentation" is doing socially, it is not a straightforward reward for
competence.

**Selective mutism is not rare and is not a fringe case.** Norwegian Patient Register, n = 1,682
children aged 3–18 with a registered SM diagnosis over 2008–2023: **11.7% co-occurrence with
autism**, sex ratio **2.13 girls per boy** (Helgesen & Nordahl-Hansen 2026,
[10.1007/s10802-025-01414-x](https://doi.org/10.1007/s10802-025-01414-x), `OBSERVED` — registry
study, `[verbatim]`). And on what the children themselves report: **"Throat and body freezing were
reported by children with SM, whether they were also autistic or not. The most common reasons given
by the children that increased their difficulty in speaking were pressure to talk, worries about how
they would be perceived, and fear of making mistakes."** (Landrock-White et al. 2026, *Behavioral
Sciences*, [10.3390/bs16010152](https://doi.org/10.3390/bs16010152), `OBSERVED` `[verbatim]`.)

"Pressure to talk. Worries about how they would be perceived. Fear of making mistakes." That is a
verbatim description, from children, of a mandatory oral presentation.

### 14.3 The resolution — and it is not a compromise

The instinct is to treat "explain it out loud" as core and a written alternative as an
accommodation. **The evidence does not support that hierarchy.** Three independent results say the
delivery modality is not where the learning is:

1. **Lim, Wong & Lim 2021** (N = 108): writing a verbatim teaching script produced the **same**
   one-week conceptual retention as verbal teaching, with comparable elaboration; both beat restudy.
   `MEASURED-RCT`
2. **Kobayashi 2024** (k = 39): **"teaching mode (teaching in written or unwritten mode)"** was
   explicitly tested as a confound and **did not explain** the expectancy moderator. `MEASURED-META`
3. **Wang, Cheng & Mayer 2023**: the *lowest*-social-presence delivery won on transfer, with lower
   state anxiety and lower cognitive load. `MEASURED-RCT`

**Therefore: for a SELPA learner, "give a presentation" as ordinarily construed is a barrier, and it
is a barrier that buys nothing.** But **"produce an explanation, under a prior obligation to teach,
in whatever channel you can produce it in" is not an accommodation — it is the better design for
everyone**, and the evidence says so on transfer tests, not on comfort ratings.

This is UDL's *multiple means of action and expression* (CAST, per ERIC
[ED595394](https://eric.ed.gov/?id=ED595394), `OBSERVED`) arriving not as an equity concession but as
the higher-scoring configuration. It is the cleanest curb-cut in this survey: the design built for
the child who freezes is the design that produced the best transfer scores in college students who
do not.

### 14.4 What must still be offered, and what must never be forced

- **Offer** speaking, typing, writing, drawing-plus-annotating, sign, AAC output, and slide-plus-notes
  as interchangeable delivery channels. Score them identically (§13 scores propositions, not fluency).
- **Never** make a live human audience a precondition for progression or credit.
- **Never** grade delivery, fluency, poise, eye contact, or pace. No evidence base licenses it, and
  Blöte et al. suggests the social consequences of "good delivery" are not even reliably positive.
- **Do offer** live human presentation as an *opt-in* goal with graded exposure for learners who want
  it — the VR-exposure literature for public-speaking anxiety is active (e.g. Colella et al. 2026 RCT
  protocol, [10.1186/s40359-026-04418-4](https://doi.org/10.1186/s40359-026-04418-4), `OBSERVED` —
  **a protocol, not results**). But that is *anxiety treatment*, a clinical goal, and it is not the
  learning intervention. **Do not conflate them.** H1's rule applies: an AI may not diagnose, and
  anxiety treatment is not a domain for unvalidated novel pedagogy.

---

## 15. DELIVERABLE (b) — the learner-presentation loop

### 15.1 The loop

```
0. PRECONDITION — first acquisition has happened.
   Learning by teaching is a consolidation and reorganisation mechanism, not an
   acquisition mechanism (F2 §3.5). Gate on a mastery floor from the learner
   model (F5). Teaching from zero produces confident nonsense.

1. ANNOUNCE — before the study episode, not after.
   "When you're done with this, you'll teach it to <audience>, and <audience>
   will then have to <do a task> using only what you told them."
   THIS IS THE INTERVENTION. Without it: g = -0.02 (Kobayashi 2024).
   Specify the audience and the downstream task, because Kobayashi 2019 found
   expectation of INTERACTIVE teaching beat expectation of non-interactive.

2. STUDY — under the announced obligation.
   This is where the effect is generated. g = 0.35 (Kobayashi 2019) for this
   phase alone. Instrument it: F5 logs what was reread, what was skipped.

3. COMPOSE — the learner produces the explanation.
   Channel: learner's choice. Speech, written script, slides + notes, drawing,
   AAC. Equivalent on evidence (Lim 2021; Kobayashi 2024 mode null).
   DEFAULT AUDIENCE = NONE. Camera or blank editor.
   Wang/Mayer 2023: lowest social presence won on transfer.

4. INTERROGATE — the agent asks, and does not evaluate.
   Persistent, specific follow-up questions targeting the propositions the
   learner did NOT cover (from the reference decomposition, §13.2(1)) and the
   misconceptions the learner model flags as live.
   HARD CONSTRAINT: no praise, no scores, no grades, no "great explanation!"
   during this phase. Questions only. Evaluation is the thing being removed.
   Basis: Kobayashi 2019 interactivity moderator + Roscoe & Chi knowledge-
   building trigger (F2) MINUS Wang/Mayer's social-evaluative cost.

5. CONSEQUENCE — the tutee acts on what it was told.
   A capability-capped agent attempts an objective task using ONLY the learner's
   explanation. It succeeds or fails visibly. The learner sees which of their
   statements the tutee relied on and where it broke.
   Basis: Okita & Schwartz recursive feedback (F2 §3.3); Betty's Brain.
   Cap must be ARCHITECTURAL — small model, restricted tools, retrieval limited
   to the learner's own text. Never a prompt. (F2: capability leakage.)

6. SCORE — counts and tests, never a judge.
   - proposition coverage vs the reference decomposition
   - elaboration count, monitoring-statement count
   - executable check on any extractable prediction (F3)
   - tutee downstream task accuracy
   - the learner's own delayed transfer test = the criterion
   Report counts and test outcomes. Never a 1-5 holistic rubric score.

7. REPAIR — the uncovered propositions become the next study episode's target,
   and any misconception surfaced in step 5 becomes a §5 diagnostic figure.
   This is where Part A and Part B join: the learner's failed explanation is the
   trigger for the on-the-fly slide.
```

### 15.2 Where the two halves of C3 meet

The loop closes: **Part B generates the diagnosis; Part A renders it.** A learner's explanation that
omits proposition 4 of 7, or whose stated mechanism fails an executable check, or whose tutee got the
wrong answer for a traceable reason — that is a *specific, localised, evidenced* misconception, which
is precisely the trigger condition §5 requires and which no amount of dialogue-monitoring produces
as cleanly. The presentation loop is the best misconception detector in the system, and the
diagnostic slide is its highest-value output.

### 15.3 What the loop must not do

- **Must not announce the obligation after study.** g = −0.02.
- **Must not put a human audience in the room by default.** Measured cost on transfer, anxiety,
  cognitive load, and pulse rate.
- **Must not praise during interrogation.** Praise is evaluation; evaluation is the thing being
  removed. (It is also the sycophancy channel F2 §8 identifies as the master obstacle.)
- **Must not run before acquisition.** F2 §3.5.
- **Must not score delivery.**
- **Must not let the tutee be secretly competent.** Chen et al. 2025 measured the failure.

---

## 16. Negative and null results ledger

Reported deliberately, per the editorial standard. Eleven, against a required minimum of three.

| # | Result | Source | Label |
|---|---|---|---|
| **N1** | **PowerPoint vs chalk-and-talk: no difference.** Hedges' **g = 0.067, 95% CI [−0.103, 0.236]**, k = 48. Effect emerged for K-12, **not** for college students. | Baker et al. 2018, [10.1016/j.compedu.2018.08.003](https://doi.org/10.1016/j.compedu.2018.08.003) | `MEASURED-META` |
| **N2** | **Delivering a lesson after studying WITHOUT a teaching expectancy: g = −0.02 [−0.14, 0.11].** Indistinguishable from zero, k = 39. The most common implementation of "explain it back to me" is the null condition. | Kobayashi 2024, ERIC EJ1414484 | `MEASURED-META` |
| **N3** | **Self-explanation prompts significantly and NEGATIVELY moderated the worked-examples effect** (overall g = 0.48, 181 ES). *"Pairing examples with self-explanation prompts may not be a fruitful design modification."* Directly tensions with Bisra's g = 0.55. | Barbieri et al. 2023, ERIC EJ1364058 | `MEASURED-META` |
| **N4** | **Incorrect self-explanations harmed learning**, regardless of error type; the harm was specific to prompts paired with *incorrect* worked examples. | JEP 2026, ERIC EJ1507394 | `MEASURED-RCT` |
| **N5** | **Redundancy null #1:** graphics+narration vs graphics+narration+verbatim text — **no significant difference** on immediate posttest, six-week delayed posttest, or usability perceptions. | ERIC ED638032 (2014) | `MEASURED-RCT` |
| **N6** | **Redundancy null #2:** four conditions crossing temporal contiguity × verbal redundancy — **no significant difference**, and *"this finding held true even when the analysis was limited to low-knowledge students."* | ERIC ED667496 (2021) | `MEASURED-RCT` |
| **N7** | **Redundancy AND modality both reversed** for L2 learners: video+text beat video+narration, and narration+text beat narration alone. | ERIC EJ1264880 (2018), *Applied Cognitive Psychology* | `MEASURED-RCT` |
| **N8** | **Learning-by-teaching lost to plain restudy.** n = 176 student teachers: *"Participants in the control condition prepared significantly more accurate and complete open-minded lessons than participants in the other two conditions"* (LBT-on-video, prepare-to-teach). No differences on any other measure. | van Brussel et al. 2023, *Instructional Science*, ERIC EJ1377200 | `MEASURED-RCT` |
| **N9** | **A live audience is a net cost.** Teach-to-camera beat teach-to-student and teach-to-group on transfer, with lower social presence, lower pulse rate, lower anxiety, lower cognitive load, and *more* generative processing. An *onscreen* human student was also worse than no audience. | Wang, Cheng & Mayer 2023 (ERIC EJ1386593); Cheng, Wang & Mayer 2023 (ERIC EJ1391980) | `MEASURED-RCT` |
| **N10** | **Tutoring had "little or no effect… on the self-esteem of tutors and tutees"** — across 65 evaluations, in 1982. The confidence claim for presenting was never supported. | Cohen, Kulik & Kulik 1982, [10.3102/00028312019002237](https://doi.org/10.3102/00028312019002237) | `MEASURED-META` |
| **N11** | **In real classrooms, better speech quality predicted *worse* peer behaviour** toward socially anxious adolescent presenters; overt nervousness did not predict it at all. | Blöte et al. 2010, ERIC EJ901204 | `OBSERVED` |

Plus, carried from adjacent sections and directly load-bearing here: **decorative animation
g = −0.05, n.s.** (A2); **only 7.2% / 33.3% of generated charts met basic colourblindness guidance**
(C1); **LLM-judge-only selection −3.20pp / −1.68pp** (in-project); **human graders α ≈ 0.20 on code
correctness** (C2).

---

## 17. What is not known — stated plainly, not filled in

1. **`OBSERVED — absence`. No slide-generation paper measures learning.** Exhaustive arXiv
   `"slide generation"` listing: 39 results, ~35 on-topic, **zero** with a human learning outcome.
   Metrics are judges, preferences, reference similarity, layout fidelity, aesthetics. Identical to
   A2's finding for animation and C1's for figures.
2. **`OBSERVED — absence`. No slide-generation paper reports any accessibility metric.** Not alt
   text, not contrast, not reading order, not colour independence. Three arXiv searches on document
   and slide accessibility returned zero results.
3. **`OBSERVED — absence`. No measured comparison of an AI audience against a human audience** for a
   learner delivering an explanation. §12 documents the four search routes that came up empty.
4. **`OBSERVED — absence`. The interrogation × evaluation 2×2 (§10.4) has an empty target cell.**
   Persistent specific questioning with zero evaluative stake has never been tested against either
   camera-only or a live audience.
5. **`OBSERVED — absence`. Nobody has measured learning from an in-turn diagnostic figure.** C1
   flags the parallel gap for static figures ("nobody has measured misconception acquisition from a
   wrong generated figure") and calls it the cheapest high-value missing experiment. The dynamic,
   diagnosis-triggered case is strictly less studied.
6. **Unresolved contradiction: Bisra g = 0.55 vs Barbieri's negative moderator.** Two EPR
   meta-analyses. Prompt quality and time-cost are the plausible reconciliation and are `INFERENCE`.
   Do not resolve it in the survey by choosing.
7. **Unverified this session — Mayer, Heiser & Lonn (2001) effect sizes.** Bibliographic record and
   622 citations verified; abstract and numbers not retrievable (APA abstracts elided from S2;
   Crossref carries none). Do not quote a d-value without re-verification.
8. **Unverified this session — Fiorella & Mayer (2013, 2014) numbers.** Elsevier `HTTP 403`,
   abstracts elided. The immediate-vs-delayed claim is carried from F2's earlier retrieval.
9. **Unverified this session — Bisra et al.'s 95% CI**, Baker's K-12 subgroup magnitude, Leung's CI,
   and Adesope & Nesbit's numbers (inherited from B1, not independently re-verified).
10. **Unknown — whether the §2.4 redundancy switch's predicted interaction exists.** Three retrieved
    nulls make this a live risk, not a formality.
11. **Unknown — whether an architecturally capped tutee can stay capped** across a long
    consequence-scoring session. F2 records this as an unsolved engineering problem; nothing
    retrieved this session solves it.
12. **Unknown — the reliability of proposition-coverage scoring** against a reference decomposition
    when the "grader" is an entailment model. PresentBench's binary-checklist alignment result is
    encouraging by analogy but is about slides, not explanations.

---

## 18. Falsifiable claims

Each is stated so that a specific measured result would kill it.

**A — The slide IR claim.** Decks emitted as a constrained declarative IR (§4.2) and rendered
deterministically will pass the §4.3 hard gate at a materially higher rate than decks produced by
end-to-end raster generation or model-authored HTML/SVG, on matched briefs.
*Predicted from:* ALGOGEN 82.5% → 99.8% (C1); AutoPresent's *"programmatic methods produce
higher-quality slides."*
**Falsified if:** a compile-and-repair raster or free-HTML pipeline matches IR gate-pass rate on
the same briefs. **Cheap to run today.**

**B — The redundancy switch claim.** For L1, system-paced learners, suppressing verbatim on-screen
text raises transfer; for L2 learners or learners with reading support on, it *lowers* it. A
crossover interaction, not a main effect.
*Predicted from:* Adesope & Nesbit direction-dependence; EJ1264880's double reversal.
**Falsified if:** no interaction appears. **This is at real risk** — N5 and N6 are two nulls in the
same family, and if B falls, the honest response is to stop encoding redundancy at all and default
to presenting text.

**C — The expectancy-first claim.** Announcing the teaching obligation *before* the study episode
produces a measurable transfer gain; announcing it *after* produces approximately zero.
*Predicted from:* Kobayashi 2024, g = 0.48 vs g = −0.02.
**Falsified if:** post-hoc announcement matches pre-announcement on delayed transfer.
**This is the cheapest experiment in the entire survey** — it is a one-line prompt-ordering
manipulation with an existing meta-analytic prior.

**D — The interrogation-without-evaluation claim.** *(The central new claim of Part B.)* An agent
audience that asks persistent, specific, non-evaluative follow-up questions will beat **both**
(i) camera-only / no audience and (ii) a live or onscreen human audience, on delayed transfer, and
the advantage will be mediated by *simultaneously* higher generative processing (idea units,
elaborations, monitoring statements) and *no elevation* of arousal (pulse rate) or state anxiety.
*Predicted from:* Kobayashi's interactivity moderator + Roscoe & Chi's knowledge-building trigger,
minus Wang & Mayer's measured social-evaluative cost.
**Falsified if:** the agent audience raises arousal or anxiety to human-audience levels, or fails to
beat camera-only on transfer. **The apparatus already exists** — Wang & Mayer 2023 provides the
complete measurement stack and the three comparison arms. Adding a fourth arm is a small
replication-plus-extension.

**E — The test-based explanation-scoring claim.** Feedback and progression driven by proposition
coverage + executable checks + tutee downstream accuracy will produce higher learner delayed
transfer than feedback driven by an LLM holistic quality score.
*Predicted from:* in-project selection benchmark (tests +8.14pp, judge −3.20pp / −1.68pp);
PresentBench's binary-checklist alignment gain; C2's human α ≈ 0.20.
**Falsified if:** judge-driven feedback matches or beats test-driven feedback on delayed transfer.

**F — The channel-equivalence claim.** Learners who deliver their explanation in writing, by speech,
or through AAC will show statistically equivalent delayed transfer, and the written/AAC channels
will show lower arousal and anxiety.
*Predicted from:* Lim et al. 2021 (written ≡ verbal at one week); Kobayashi 2024 (mode null);
Haucke et al. 2025 (socio-evaluative stress reduces WM).
**Falsified if:** speech is superior on transfer. **If F holds, "give a presentation" as a
requirement is unjustifiable**, and the survey should say so.

---

## 19. Bibliography — verified this session

**Retrieved verbatim (publisher- or repository-supplied abstract text):**

1. Baker, Goodboy, Bowman & Wright (2018), *Computers & Education* — https://doi.org/10.1016/j.compedu.2018.08.003 — `MEASURED-META`
2. Kobayashi (2019), *Japanese Psychological Research* — https://doi.org/10.1111/jpr.12221 — `MEASURED-META`
3. Kobayashi (2024), *Educational Psychology Review* — https://doi.org/10.1007/s10648-024-09871-4 · ERIC EJ1414484 — `MEASURED-META`
4. Leung (2018), *School Psychology International* — https://doi.org/10.1177/0143034318808832 — `MEASURED-META`
5. Cohen, Kulik & Kulik (1982), *AERJ* — https://doi.org/10.3102/00028312019002237 — `MEASURED-META`
6. Bisra, Liu, Nesbit, Salimi & Winne (2018), *Educational Psychology Review* — https://doi.org/10.1007/s10648-018-9434-x · ERIC EJ1186664 — `MEASURED-META`
7. Barbieri et al. (2023), *Educational Psychology Review* — ERIC EJ1364058 — `MEASURED-META`
8. Nestojko, Bui, Kornell & Bjork (2014), *Memory & Cognition* — https://doi.org/10.3758/s13421-014-0416-z · PMID 24845756 — `MEASURED-RCT`
9. Daou et al. (2016), *J. Motor Learning and Development* — https://doi.org/10.1123/jmld.2015-0036 — `MEASURED-RCT`
10. Daou et al. (2016), *Human Movement Science* — https://doi.org/10.1016/j.humov.2016.08.009 — `MEASURED-RCT`
11. Wang, Cheng & Mayer (2023), *Journal of Educational Psychology* — ERIC EJ1386593 — `MEASURED-RCT`
12. Cheng, Wang & Mayer (2023), *J. Computer Assisted Learning* — ERIC EJ1391980 — `MEASURED-RCT`
13. Lim, Wong & Lim (2021), *Applied Cognitive Psychology* — ERIC EJ1315998 — `MEASURED-RCT`
14. van Brussel, Timmermans, Verkoeijen & Paas (2023), *Instructional Science* — ERIC EJ1377200 — `MEASURED-RCT` **(negative)**
15. *JEP* (2026), "Incorrect Self-Explanation Prompt Responses" — ERIC EJ1507394 — `MEASURED-RCT` **(negative)**
16. Chen, Wei, Le et al. (2025), *BJET* — ERIC EJ1493482 — `MEASURED-RCT`
17. ERIC ED638032 (2014), multimedia redundancy — `MEASURED-RCT` **(null)**
18. ERIC ED667496 (2021), temporal contiguity × verbal redundancy — `MEASURED-RCT` **(null)**
19. ERIC EJ1264880 (2018), *Applied Cognitive Psychology*, L2 video — `MEASURED-RCT` **(reversal)**
20. Blöte et al. (2010), *J. Youth and Adolescence* — ERIC EJ901204 — `OBSERVED`
21. Haucke, Golde & Heinzel (2025), *Scientific Reports* — https://doi.org/10.1038/s41598-025-22611-0 — `MEASURED-RCT`
22. Helgesen & Nordahl-Hansen (2026) — https://doi.org/10.1007/s10802-025-01414-x — `OBSERVED`
23. Landrock-White et al. (2026), *Behavioral Sciences* — https://doi.org/10.3390/bs16010152 — `OBSERVED`
24. Deer et al. (2026), *J. Experimental Child Psychology* — https://doi.org/10.1016/j.jecp.2025.106445 — `MEASURED-RCT` (acute stress × executive function, n = 181 children 9–11)
25. Wang et al. (2025), CHI EA — https://doi.org/10.1145/3706599.3719863 — `DEMO`
26. Kalyuga, Chandler & Sweller (1999) retrospective, *Applied Cognitive Psychology* — https://doi.org/10.1002/acp.1773 — `OBSERVED`
27. Colella et al. (2026), *BMC Psychology* — https://doi.org/10.1186/s40359-026-04418-4 — `OBSERVED` **(protocol only, no results)**

**Retrieved as fetched-summary (arXiv abs/search pages; re-verify unquoted text):**

28. AutoPresent / SlidesBench — arXiv:2501.00912
29. PPTAgent / PPTEval — arXiv:2501.03936
30. PresentBench — arXiv:2603.07244
31. Learning to Present — arXiv:2603.16839
32. X+Slides — arXiv:2606.19256
33. OmniPresent / OmniPreBench — arXiv:2607.02590
34. SlideBot — arXiv:2511.09804
35. AeSlides — arXiv:2604.22840
36. Misconception Diagnosis From Student–Tutor Dialogue — arXiv:2602.02414
37. MemSlides — arXiv:2606.17162 · ECHO — arXiv:2606.09851 · CourseBlueprint — arXiv:2606.20608
38. DeepSlides 2605.26451 · DeepSlide 2605.15202 · ArcDeck 2604.11969 · DECKBench 2602.13318 · SlidesGen-Bench 2601.09487 · SlideTailor 2512.20292 · SlideGen 2512.04529 · PPTArena 2512.03042 · PPTBench 2512.02624 · Paper2Video 2510.05096 · SynLecSlideGen 2506.23605 · SlideCoder 2506.07964 · PASS 2501.06497 · SlideSpawn 2411.17719 · DOC2PPT 2101.11796 · D2S 2105.03664 · SciBERTSUM 2201.08495

**Bibliographic record verified, abstract NOT retrievable this session:**

39. Mayer, Heiser & Lonn (2001), *JEP* 93(1):187 — https://doi.org/10.1037/0022-0663.93.1.187 — 622 cites — `[biblio-only]`
40. Adesope & Nesbit (2012), *JEP* — https://doi.org/10.1037/a0026147 — 134 cites — `[biblio-only]` (numbers inherited from B1)
41. Kalyuga, Chandler & Sweller (1999), *ACP* — https://doi.org/10.1002/(sici)1099-0720(199908)13:4<351::aid-acp589>3.0.co;2-6 — 401 cites — `[biblio-only]`
42. Fiorella & Mayer (2013), *CEP* — https://doi.org/10.1016/j.cedpsych.2013.06.001 — 269 cites — `[biblio-only]`
43. Fiorella & Mayer (2014), *CEP* — https://doi.org/10.1016/j.cedpsych.2014.01.001 — `[biblio-only]`
44. Okita & Schwartz (2013), *J. Learning Sciences* — https://doi.org/10.1080/10508406.2013.807263 — 64 cites — `[biblio-only]`
45. Okita (2013), *Computers & Education* — https://doi.org/10.1016/j.compedu.2012.12.005 — 44 cites — `[biblio-only]`
46. Alpizar et al. (2020), *ETR&D* signaling meta — https://doi.org/10.1007/s11423-020-09748-7 — 132 cites — `[biblio-only]`
47. Kobayashi (2019), *Frontiers in Psychology* — https://doi.org/10.3389/fpsyg.2018.02755 — `[biblio-only]`

**Observed (GitHub API / project documentation, 2026-07-27):**

48. `hakimel/reveal.js` 72,036★ · 49. `typst/typst` 55,118★ · 50. `remotion-dev/remotion` 54,426★ ·
51. `slidevjs/slidev` 47,859★ · 52. `jgm/pandoc` 45,570★ · 53. `3b1b/manim` 88,888★ ·
54. `ManimCommunity/manim` 39,717★ · 55. `impress/impress.js` 38,197★ · 56. `gnab/remark` 12,999★
(last push 2024-06-19) · 57. `quarto-dev/quarto-cli` 5,884★ · `marp-team/marp-cli` 3,718★ ·
`marp-team/marp-core` 1,128★. Plus marp.app, sli.dev/guide/why, quarto.org/docs/presentations
(`[fetched-summary]`), and W3C WCAG 2.2 (https://www.w3.org/TR/WCAG22/, `OBSERVED`).

**In-project evidence relied on:** B1 (multimedia effect-size table), C1 (figure IR, tiering,
colourblindness base rates, alt-text architecture), A2 (animation effect sizes, preference illusion),
F2 (protégé effect, recursive feedback, capability leakage, sycophancy), F3 (executable grounding),
F5 (learner model), H1 (WCAG 2.2 AA floor, anxiety archetype, UDL, no-diagnosis rule),
C2 (Krippendorff α ≈ 0.20 for human graders), `artifacts/README.md` (test-vs-judge selection deltas).

---

## 20. Research notes and limitations

- **arXiv API was unusable for the entire session** (`HTTP 429 Rate exceeded` at the host level,
  Google Frontend). All arXiv content came through WebFetch on `arxiv.org/abs/…` and
  `arxiv.org/search/…`, which returns a model-summarised rendering. Quoted fragments are quoted as
  they appeared; unquoted arXiv content is paraphrase and is marked `[fetched-summary]`.
- **OpenAlex was hard-blocked** — the account's daily budget was exhausted before this session began
  (`"Insufficient budget… Resets at midnight UTC"`).
- **Semantic Scholar's `/paper/search` endpoint was rate-limited throughout**; the by-DOI endpoint
  worked intermittently with ~3.5s spacing and delivered the Baker abstract.
- **Elsevier (ScienceDirect / linkinghub) returned HTTP 403** to every attempt. **Springer redirected
  to `idp.springer.com`** on every article URL. **APA-published abstracts are elided** from the
  Semantic Scholar corpus and absent from Crossref. Together these account for every `[biblio-only]`
  entry in §19.
- **ERIC (`api.ies.ed.gov/eric`) was the most productive channel of the session** for education
  research and returned complete verbatim abstracts including full effect-size reporting. It should
  be the first stop for every future education-focused section in this project, ahead of Crossref
  and Semantic Scholar. Note its query syntax: `--data-urlencode "search=title:\"…\""` works;
  boolean `AND`/`OR` across fielded terms silently returns `numFound: null`.
- **Sample-size and CI gaps** are flagged inline wherever a retrieved abstract omitted them; none
  were filled by inference.
