---
title: "Explanation depth laddering — one concept rendered at every sophistication level, and building intuition before formalism"
wave: F
section: F10
date_researched: 2026-07-27
sources_count: 96
---

# F10 — Explanation Depth Laddering

> **The claim this section defends:** rendering one concept at five sophistication
> levels is not the same problem as sequencing a curriculum, and the difference is
> load-bearing. A curriculum moves a learner *through topics over time*; a ladder
> renders *the same concept at N levels simultaneously* so the learner enters at
> their measured level and climbs. The literature that actually governs this is not
> "spiral curriculum" (which is cited constantly and evidenced thinly). It is
> **concreteness fading**, **expertise reversal**, **structure mapping**, and
> **conceptual change**. Those four converge on one uncomfortable engineering
> conclusion: **a ladder is only safe if it is generated top-down under a
> non-falsification constraint, and only useful if the entry rung is chosen by
> measurement rather than by preference.** Learner preference is a *systematically
> biased* signal here — simplification raises confidence faster than it raises
> competence.

---

## 0. Retrieval note

`WebSearch` was exhausted before this section began. Retrieval was done through
**OpenAlex** (works API, until its daily budget was exhausted mid-session),
**Crossref** REST, **Semantic Scholar Graph** (batch endpoint), **ERIC** (IES API —
by far the most productive source for this topic), **Unpaywall**, **arXiv**, and
targeted `WebFetch`.

**Unreachable / partially verified — flagged, not guessed:**

- **Fyfe, McNeil, Son & Goldstone (2014)**, the systematic review that is the
  empirical backbone of this section, is **closed access**. Unpaywall returns
  `is_oa: false`; Semantic Scholar reports the abstract field "elided by the
  publisher." The full abstract *was* recovered from the **ERIC** record
  (`EJ1036777`) and is quoted below. **Per-study effect sizes from inside that
  review could not be extracted** and are therefore not asserted. Where this
  document gives effect sizes for concreteness fading, they come from primary
  studies retrieved independently.
- **Fyfe & Nathan (2018)** has a green-OA record at `iu.tind.io/record/1753`; the
  bitstream returns HTTP 202 behind a challenge and could not be downloaded. Abstract
  verified via OpenAlex + ERIC (`EJ1219042`).
- **Spiro, Feltovich, Coulson & Anderson (1989)** — the IDEALS bitstream returns
  403. Only the title and Semantic Scholar's machine-extracted summary were verified;
  the paper's internal *taxonomy* of analogy-induced error is therefore described at
  the level the extracted summary supports and is labelled as such.
- **Tetzlaff et al. (2025)** expertise-reversal meta-analysis: `d = 0.505` and
  `d = −0.428` are **verified from the publisher abstract**. The **interaction
  figure `d = 0.971` given in the brief could not be verified in this session** —
  it does not appear in the abstract, and the paper is hybrid-OA behind Elsevier.
  The verified values imply an interaction of ≈ **0.93** by simple difference; the
  0.971 figure is plausibly a model-estimated interaction term from the full text
  but is **not asserted here**. See §5.1.
- **r/explainlikeimfive rule text** — reddit.com and old.reddit.com are both blocked
  in this environment (WebFetch refused; the `about/rules.json` endpoint returned
  non-JSON). The subreddit is characterised below only via the **peer-reviewed ELI5
  corpus paper** (Fan et al., 2019), which documents its structure quantitatively.
- **Nature** and **PNAS** author-guideline pages return 303-to-IdP and 403
  respectively. Tiered-abstract practice is therefore evidenced through the
  **plain-language-summary literature**, which is directly measured, rather than
  through publisher marketing pages.

---

## 1. Concreteness fading — the empirical backbone

### 1.1 What the technique claims

> "A longstanding debate concerns the use of concrete versus abstract instructional
> materials… we argue for an approach that moves beyond this dichotomy and combines
> their advantages. Specifically, we recommend beginning with concrete materials and
> then explicitly and gradually fading to the more abstract."
> — Fyfe, McNeil, Son & Goldstone (2014), *Educational Psychology Review*

Source: [10.1007/s10648-014-9249-3](https://doi.org/10.1007/s10648-014-9249-3) ·
abstract recovered from [ERIC EJ1036777](https://eric.ed.gov/?id=EJ1036777)
`OBSERVED` (review claim, not a pooled effect)

The review states four mechanisms: (1) concrete objects let learners interpret
otherwise-opaque abstract symbols, (2) embodied perceptual experience grounds
abstract thought, (3) learners accumulate memorable images to fall back on when
symbols lose meaning, (4) fading *strips extraneous concrete properties* and
distills the generalizable structure. Note that (4) is the one that matters for
laddering: **fading is subtraction of the wrong specifics, not addition of the
right generalities.**

**Critically: this is a systematic review, not a meta-analysis.** No pooled effect
size is reported for concreteness fading anywhere in the retrievable record for this
paper. Anyone citing "the effect size of concreteness fading" is citing something
that, as far as this session could verify, **does not exist**. `INFERENCE`

### 1.2 The primary experiments

**Goldstone & Son (2005)**, *Journal of the Learning Sciences* — the origin study.
Two experiments; participants interacted with simulations of complex adaptive
systems; transfer between two simulations governed by the same principle was the
dependent measure.

> "Transfer was better when the appearance of the elements switched… **The best
> transfer was observed when originally concrete elements became idealized.**
> …Progressive idealization ('concreteness fading') allows originally grounded and
> interpretable principles to become less tied to specific contexts and hence more
> transferable."

[10.1207/s15327809jls1401_4](https://doi.org/10.1207/s15327809jls1401_4)
`MEASURED-RCT` (lab, randomized to appearance condition)

Two things in that abstract are usually dropped by people citing it. First,
**switching in either direction beat not switching** — concrete→idealized *and*
idealized→concrete both outperformed static conditions, "consistent with theories
predicting more general schemas when the schemas are multiply instantiated." The
directional advantage of fading is a *second-order* effect on top of a
multiple-instantiation effect. Second, the outcome is *transfer*, not acquisition.

**McNeil & Fyfe (2012)**, *Learning and Instruction* — undergraduates, modular
arithmetic, three conditions (generic symbols / concrete meaningful images / faded),
transfer tested immediately, at 1 week, and at 3 weeks.

> "Undergraduates in the fading condition exhibited the best transfer performance.
> Additionally, undergraduates in the generic condition exhibited somewhat better
> transfer than those in the concrete condition, **but this advantage was not
> robust.**"

[10.1016/j.learninstruc.2012.05.001](https://doi.org/10.1016/j.learninstruc.2012.05.001)
· [ERIC EJ978023](https://eric.ed.gov/?id=EJ978023) `MEASURED-RCT`

**Fyfe, McNeil & Borjas (2015)**, *Learning and Instruction*, "Benefits of
'concreteness fading' for children's mathematics understanding" —
[10.1016/j.learninstruc.2014.10.004](https://doi.org/10.1016/j.learninstruc.2014.10.004).
Abstract not retrievable in this session (closed at Elsevier; not in ERIC; S2
returns null). Cited here as an existence claim only. `UNVERIFIED-IN-SESSION`

**Ottmar & Landy (2017)**, "Concreteness Fading of Algebraic Instruction: Effects on
Learning," *Journal of the Learning Sciences* —
[10.1080/10508406.2016.1250212](https://doi.org/10.1080/10508406.2016.1250212).
Introduces **"notational concreteness"**: perceptual-motor support *inside the
representation itself* rather than through external examples/analogies, hypothesizing
"perceptual support may be maximally beneficial as an initial scaffold… so that later
static symbol use may be interpreted using a dynamic perspective."
[ERIC EJ1131886-class record](https://eric.ed.gov/?q=%22Concreteness+Fading+of+Algebraic+Instruction%22)
`OBSERVED`

This matters for a text-based ladder: the "concrete" rung need not be a *story*. It
can be a manipulable notation. That is the difference between a decorative analogy
and a load-bearing one (§3).

### 1.3 Boundary conditions and the negative results

This is where the honest picture diverges sharply from the popular one.

**(N1) Concreteness fading vs. simultaneous presentation: statistical equivalence.**
Lichtenberger, Kokkonen & Schalk (2024), *JRST*, N = 187 high-school students,
Faraday's law:

> "We found **no significant differences between conditions** in posttest
> performance, and an **equivalence test with bounds d = −0.5 to 0.5 showed that both
> approaches performed equally.** …The results align with previous findings
> questioning the superiority of concreteness fading over other ways of sequencing
> MERs. Therefore, facilitating students' understanding of a complex physics content
> **may involve more than determining the optimal order** of presenting MERs."

[10.1002/tea.21947](https://doi.org/10.1002/tea.21947) `MEASURED-RCT` — **negative
result, pre-specified equivalence bounds.** This is the strongest single caution in
the section: *ordering is not the mechanism.*

**(N2) Multiple concrete representations actively hurt.** Bennett, Inglis & Gilmore
(2019), *JEP*, three experiments with children learning novel numerical symbols:

> "Children who learned the meaning of novel symbols by pairing them with numerosities
> represented by **arrays of dots performed better** on a subsequent symbolic
> comparison task than those who paired them with multiple concrete representations,
> or a mixture… **This advantage was not due to abstract representations being
> inherently superior** to concrete representations, but instead to **the use of
> multiple concrete representations.**"

[10.1037/edu0000318](https://doi.org/10.1037/edu0000318) `MEASURED-RCT` — **negative
result.** Note the precise diagnosis: the harm is *variety of surface*, not
concreteness. A ladder that renders ELI10 as "here are four fun everyday analogies"
is reproducing exactly this failure.

**(N3) Richer context reliably degrades transfer.** Day, Motz & Goldstone (2015),
*Frontiers in Psychology*, two classroom experiments (undergraduates, then
middle-schoolers), same content, varied contextualization:

> "In both studies, we found that **greater contextualization was associated with
> poorer transfer performance.** We interpret these results as reflecting a greater
> degree of embeddedness for the knowledge acquired from richer, more concrete
> materials, such that the underlying principles are represented in a **less abstract
> and generalizable form.**"

[10.3389/fpsyg.2015.01876](https://doi.org/10.3389/fpsyg.2015.01876)
`MEASURED-RCT` — **negative result for concreteness, in ecological settings.**

**(N4) Mostly-null replication in computing, with exact statistics.** Trory, Howland,
Good & du Boulay (2026) — three between-groups pre/post experiments, 166 pupils aged 9–10, computer network structure
and routing (ACM *Transactions on Computing Education*, 2026):

| Hypothesis | Result |
|---|---|
| H1: Fading > Abstract, Concrete, Concreteness-Introduction | **Not supported.** ANCOVA F(3,54) = 2.413, p = 0.077, ηp² = 0.118. Only the Fading-vs-Concrete contrast was significant (Mdiff = 1.00, 95% CI [0.26, 1.75], p = 0.010) |
| H2: Physical concrete > virtual concrete | **Not supported.** Welch t(41.7) = 1.015, p = 0.316, Mdiff = 0.47 [−0.47, 1.41] |
| H3: Three-step > two-step | **Supported.** ANOVA F(2,56) = 3.670, p = 0.032, ηp² = 0.116; Mdiff = 0.99, p = 0.037 |
| H4: Five-step > three-step | **Not supported.** Mdiff = 0.16 [−0.78, 1.09], p = 0.738 |

[ERIC EJ1510953](https://eric.ed.gov/?id=EJ1510953) `MEASURED-RCT` — **three of four
hypotheses null.** H3 and H4 together are the most directly useful finding in this
entire section for ladder design: **three rungs beat two; five rungs did not beat
three.** There is a diminishing return, and it arrives early.

**(N5) The effect is developmentally moderated.** Jaakkola & Veermans (2018),
*Instructional Science*, N = 127, grades 4–6, electric circuits in simulation
(bulbs → resistors):

> "The most important finding was that the outcomes seemed to be influenced by a
> **developmental factor**: the study found a **significant interaction between
> condition and grade level**… outcomes generally improved as a function of grade
> level, but there were notable differences [between grades]."

[10.1007/s11251-017-9428-y](https://doi.org/10.1007/s11251-017-9428-y) ·
[OA PDF](https://www.utupub.fi/bitstream/10024/162998/1/Jaakkola_Veermans_IS_2018.pdf)
`MEASURED-RCT`

**(N6) Domain generality is contested on principled grounds.** Kokkonen & Schalk
(2021), *Educational Psychology Review*:

> "Our analysis suggests that **concreteness fading may not be as generalizable as
> has been suggested.** Two main reasons: (1) the types of representations and the
> relations between them **differ across domains**, and (2) the instructional goals
> between domains and subsequent **roles of the representations vary.**"

[10.1007/s10648-020-09581-7](https://doi.org/10.1007/s10648-020-09581-7)
`OBSERVED` (conceptual analysis, not measurement)

**(N7) Even the theory's own authors say it is underspecified.** Fyfe & Nathan (2018)
wrote an entire paper titled *"Making 'concreteness fading' more concrete as a theory
of instruction"*, whose stated goal was "to improve the theoretical framework… by
defining and bringing greater clarity to the terms **abstract, concrete and
fading**." [10.1080/00131911.2018.1424116](https://doi.org/10.1080/00131911.2018.1424116)
`OBSERVED`

### 1.4 What survives

`INFERENCE` — synthesizing §1.2–1.3:

1. **Multiple instantiation of the same structure is the robust part.** (Goldstone &
   Son: both switch directions beat static.)
2. **Concrete→abstract ordering is a weak second-order effect** that fails to
   replicate against strong alternatives (N1), fails in some domains (N4, N6), and
   is moderated by development (N5).
3. **Surface variety without structural alignment is harmful** (N2, N3).
4. **Three rungs is the empirically supported granularity; five is not** (N4/H3+H4).
   This is a direct, quantitative constraint on the ELI10/15/20/25 scheme: the brief's
   five levels are **one more than the evidence supports for a single learning
   episode**, though not for a *library* that different learners enter at different
   points. The distinction between "a learner traverses all five" and "five exist so
   each learner traverses two or three" is the whole design.

---

## 2. Bruner's spiral curriculum — ubiquitous citation, thin evidence

The spiral is the ancestor claim ("any subject can be taught in some intellectually
honest form to any child at any stage of development" — Bruner, 1960). It is cited as
the foundation of concreteness fading (the enactive → iconic → symbolic progression
*is* Bruner's), and it is cited constantly in curriculum documents.

**The evidence base does not match the citation rate.** An ERIC research-into-practice
brief states it flatly:

> "**Although there is no clear empirical evidence of the overall effects of the
> spiral curriculum on student learning**, 'features' of that curriculum have been
> linked to improved learning outcomes."

[ERIC ED538282](https://eric.ed.gov/?id=ED538282), Education Partnerships Inc. (2012)
`OBSERVED` — **negative result / absence-of-evidence claim.**

Harden's canonical definitional paper, *"What is a spiral curriculum?"*
([10.1080/01421599979752](https://doi.org/10.1080/01421599979752), *Medical Teacher*,
1999, 741 citations) is a **definition and advocacy piece**, not an evaluation. Its
740+ citations are doing structural work in the literature that its evidentiary
content cannot support. `OBSERVED`

**The strongest genuine spiral RCT retrieved.** Kim et al. (2024), *Developmental
Psychology* — the Model of Reading Engagement (MORE) intervention. 30 elementary
schools, **N = 2,870**, cluster-randomized; treatment = full spiral (Grades 1→2→3
thematically linked content-literacy lessons + summer wide reading), control =
partial spiral (Grade 3 lessons only):

> "Treatment students outperformed control students on science vocabulary knowledge
> across all three grades. …intent-to-treat analyses revealed positive transfer
> effects on **Grade 3 science reading (ES = 0.14), domain-general reading
> comprehension (ES = 0.11), and mathematics achievement (ES = 0.12).** Treatment
> impacts were **sustained at 14-month follow-up** on Grade 4 reading comprehension
> (ES = 0.12) and mathematics achievement (ES = 0.16)."

[ERIC EJ1430484](https://eric.ed.gov/?id=EJ1430484) · working paper
[ERIC ED638864](https://eric.ed.gov/?id=ED638864) `MEASURED-RCT`

This is real and it is durable, but note the size: **ES ≈ 0.11–0.16**, i.e. small.
And note what varied — the treatment spiraled *topics and vocabulary across three
years*, which is sequential curriculum, **not** the same concept rendered at multiple
depths simultaneously.

Other spiral evidence retrieved is weaker in design:

- Grove, Hershberger & Bretz (2008), *Chemistry Education Research and Practice* —
  spiral organic chemistry at Miami University against a 30–50% baseline attrition
  rate; **qualitative case study of 18 students** with interviews and reflective
  essays. [10.1039/b806232n](https://doi.org/10.1039/b806232n) `OBSERVED`
- Masters & Gibbs (2007), *BMC Medical Education* — 70% of medical students revisited
  previous online courses; the paper's contribution is that *deleting* prior-year
  material breaks the spiral.
  [10.1186/1472-6920-7-52](https://doi.org/10.1186/1472-6920-7-52) `OBSERVED`
- IEEE *Transactions on Education* (2023), spiral computer-engineering curriculum,
  quasi-experimental, mixed methods; higher motivation on three subscales and higher
  grades. [ERIC EJ1364684](https://eric.ed.gov/?id=EJ1364684) `MEASURED-BENCH`

**Conclusion for laddering.** `INFERENCE` — Bruner supplies the *representational
grammar* (enactive → iconic → symbolic) that concreteness fading operationalized and
that a ladder can reuse. He does not supply evidence that revisiting-at-increasing-
complexity is itself efficacious; the one large RCT that tests something close finds
small-but-durable effects for *thematic* spiraling. **Cite Bruner for the grammar,
never for the warrant.**

---

## 3. Analogy and structure mapping — what makes an analogy load-bearing

### 3.1 The theory that tells you which analogies work

Gentner's structure-mapping theory (1983, *Cognitive Science*) gives the two rules
that decide whether an analogy is a rung or a decoration:

> "(a) **Relations between objects, rather than attributes of objects, are mapped**
> from base to target; and (b) the particular relations mapped are determined by
> **systematicity**, as defined by the existence of **higher-order relations.**"

[10.1016/S0364-0213(83)80009-3](https://doi.org/10.1016/S0364-0213(83)80009-3)
`OBSERVED` (theory)

The operational consequence: **an analogy is load-bearing iff the mapped relations
are causally interconnected in the base and remain interconnected in the target.**
Shared *attributes* ("an atom is like a tiny solar system because both are round and
have a big thing in the middle") are decorative and are the exact substrate of later
misconception.

Gentner & Toupin (1986) measured this developmentally: children 5–7 and 8–10 re-enacted
stories with new characters; **systematicity** (degree of explicit causal structure)
and **transparency** (surface similarity of object mappings) were crossed.

> "A preference for systematic mappings is a central aspect of analogical processing
> in adults… Does systematicity make analogical mapping easier? And if so, when,
> developmentally, do children become able to utilize systematicity?"

[10.1207/s15516709cog1003_2](https://doi.org/10.1207/s15516709cog1003_2) ·
[OA PDF](https://onlinelibrary.wiley.com/doi/pdfdirect/10.1207/s15516709cog1003_2)
`MEASURED-RCT`

Gentner (1988), *Child Development*, "Metaphor as Structure Mapping: The Relational
Shift" established that **children understand attribute-based comparisons before
relation-based ones**, with a developmental increase in relational interpretation and
a shift from attributional to relational readings for ambiguous metaphors.
[10.2307/1130388](https://doi.org/10.2307/1130388) ·
[OA PDF](https://www.ideals.illinois.edu/items/18153/bitstreams/64931/data.pdf)
`MEASURED-RCT`

**This is the single most important developmental fact for a depth ladder.** `INFERENCE`
An ELI10 analogy will be read *attributionally* by its intended audience even if the
author intended it relationally. The relational shift is not complete at 10. Therefore
an ELI10 rung must either (i) carry its relational structure explicitly and
redundantly, or (ii) not be an analogy at all.

### 3.2 The intervention that makes analogies work: comparison, not exposure

Gentner, Loewenstein & Thompson (2003), *Journal of Educational Psychology* —
**analogical encoding**: learning by *drawing a comparison across two examples*
rather than studying examples serially. Three studies on schema abstraction and
transfer in novice negotiators.
[10.1037/0022-0663.95.2.393](https://doi.org/10.1037/0022-0663.95.2.393) ·
[ERIC EJ671102](https://eric.ed.gov/?id=EJ671102) `MEASURED-RCT`

Related: Loewenstein, Thompson & Gentner (1999), "Analogical encoding facilitates
knowledge transfer in negotiation," [10.3758/BF03212967](https://doi.org/10.3758/BF03212967)
`MEASURED-RCT`; Thompson, Gentner & Loewenstein (2000), "Analogical training more
powerful than individual case training," *OBHDP*,
[10.1006/obhd.2000.2887](https://doi.org/10.1006/obhd.2000.2887) `MEASURED-RCT`;
Gentner et al. (2009), "Reviving Inert Knowledge: Analogical Abstraction Supports
Relational Retrieval of Past Events," five experiments,
[10.1111/j.1551-6709.2009.01070.x](https://doi.org/10.1111/j.1551-6709.2009.01070.x)
`MEASURED-RCT`

This converges exactly with Goldstone & Son's "multiple instantiation" finding
(§1.2/§1.4) and with Bennett et al.'s diagnosis that *unaligned* variety hurts (§1.3
N2). **The active ingredient across all of them is aligned comparison of two
instantiations of the same relational structure.** `INFERENCE`

### 3.3 When analogies create misconceptions requiring unlearning

**Spiro, Feltovich, Coulson & Anderson (1989)**, "Multiple analogies for complex
concepts: **antidotes for analogy-induced misconception** in advanced knowledge
acquisition," in *Similarity and Analogical Reasoning* (CUP).
[10.1017/CBO9780511529863.023](https://doi.org/10.1017/CBO9780511529863.023)

Semantic Scholar's machine-extracted summary of the paper (the full text returned 403
from IDEALS; this is quoted as an extracted summary, **not** as the authors' own
abstract):

> "…there exists a **pervasive tendency for analogies to contribute to the development
> of entrenched misconceptions** in the form of **reducing complex new knowledge to
> the core of a source analogy**, and presents **a taxonomy of ways that simple
> analogy induces conceptual error** and an alternative approach involving
> **integrated sets of multiple analogies.**"

`OBSERVED` / `UNVERIFIED-IN-SESSION` (extracted summary; the taxonomy's internal
categories were not retrievable)

The named failure mode — *reductive bias*, the collapse of a complex target onto the
source's core — is precisely the mechanism by which a well-intentioned ELI10 becomes
a persistent adult misconception. The prescribed antidote is **integrated sets of
multiple analogies**, i.e. deliberately *disanalogous* multiple sources so no single
source can be over-extended.

**Duit (1991)**, "On the role of analogies and metaphors in learning science,"
*Science Education*, 906 citations —
[10.1002/sce.3730750606](https://doi.org/10.1002/sce.3730750606). Abstract not
retrievable in this session (closed at Wiley, absent from ERIC/S2). Cited as the
canonical review of the double-edged character of science analogies.
`UNVERIFIED-IN-SESSION`

**Clement (1993)**, "Using **bridging analogies** and **anchoring intuitions** to deal
with students' preconceptions in physics," *JRST*, 362–619 citations —
[10.1002/tea.3660301007](https://doi.org/10.1002/tea.3660301007) ·
[ERIC EJ480228](https://eric.ed.gov/?id=EJ480228) `OBSERVED`

Clement's earlier pilot (ERIC ED283712, 1987) is the clean demonstration: 21 high
school students with no physics; 14 initially denied that a table exerts an upward
force on a book; matched groups received either a *bridging* chain of analogies or
standard example-based teaching:

> "After instruction, the experimental group performed **significantly better on
> target and transfer problems**, as well as indicating significantly higher
> subjective estimates of how 'understandable and believable' the explanation was.
> These findings suggest that: (1) teachers need to be aware that certain examples
> **they themselves find compelling may not be at all illuminating for the student**;
> (2) even when the example is compelling to the student, **it may not be seen as
> analogous** to the target problem."

[ERIC ED283712](https://eric.ed.gov/?id=ED283712) `MEASURED-RCT` (small, matched groups)

Clement's related principle — "**Not all preconceptions are misconceptions**: finding
'anchoring conceptions' for grounding instruction on students' intuitions" (1989) — is
the correct entry-rung strategy for concepts that cannot be honestly simplified (§6,
§7).

**Analogies do repair misconceptions when structured.** Two ERIC-indexed classroom
studies:

- Bridging-analogies strategy vs. control, N = 119 Turkish high-schoolers, Mechanics
  Misconception Test pre/post, ANCOVA: "bridging analogies teaching strategy **was an
  effective means of reducing the number of misconceptions** students held about
  normal forces, frictional forces, tension, gravity, inertia, and Newton's third
  law." [ERIC EJ751998](https://eric.ed.gov/?id=EJ751998) `MEASURED-RCT`
- 19 purpose-built analogies for chemical equilibrium, N = 151, experimental vs.
  traditional control, pre/post Chemical Equilibrium Misconception Test + 24
  interviews: experimental students held fewer misconceptions.
  [ERIC EJ933450](https://eric.ed.gov/?id=EJ933450) `MEASURED-BENCH`

**(N8) But a well-motivated analogy manipulation can produce nothing.** Sota (2012), a dissertation
study on *contrasting analogies* for natural selection, randomly assigned participants
to refutational contrasting analogies, non-refutational contrasting analogies, or no
contrasting analogies:

> "**Analysis of variance showed no differences among groups on either understanding
> of or reasoning about natural selection** as measured by the posttests. However,
> there were significant differences between groups on the analogy portion of the
> instructional materials."

[ERIC ED547079](https://eric.ed.gov/?id=ED547079) `MEASURED-RCT` — **negative
result.** Learners engaged differently with the analogies and learned the same amount.

### 3.4 The analogy contract

`INFERENCE` — the operational rule this section extracts:

> An analogy may appear on a rung **only** with a declared **alignment set** (which
> relations map) and a declared **limit set** (which relations do *not* map). An
> analogy shipped without a limit set is indistinguishable, at retrieval time, from
> a planted misconception. For concepts with high reductive-bias risk, ship **two
> mutually disanalogous** analogies rather than one good one (Spiro).

---

## 4. Multiple external representations — Ainsworth's DeFT

Ainsworth (1999), "The functions of multiple representations," *Computers &
Education*, 1,112–1,173 citations —
[10.1016/S0360-1315(99)00029-9](https://doi.org/10.1016/S0360-1315(99)00029-9).
Semantic Scholar's extracted summary: "By identifying the functions that MERs can
serve, it is claimed that **many of the conflicting findings arising out of the
existing evaluations of multi-representational learning environments can be
explained**." `OBSERVED`

Ainsworth (2006), **DeFT** (Design, Functions, Tasks), *Learning and Instruction*,
1,608–1,726 citations —
[10.1016/j.learninstruc.2006.03.001](https://doi.org/10.1016/j.learninstruc.2006.03.001).
Extracted summary: "The utility of the DeFT framework is proposed to be in
identifying a broad range of factors that influence learning, **reconciling
inconsistent experimental findings**, revealing under-explored areas… and pointing
forward to potential design heuristics." `OBSERVED`

Both papers are closed access; Unpaywall returns `is_oa: false` for each. The **three
functions** are verified through an independent empirical paper that adopts them as
its coding frame — Won, Yoon & Treagust (2014), *Science Education*, Grade 11 human
biology:

> "The functions of multiple representations — **complementary, constraining, and
> deeper understanding** — suggested by Ainsworth (2008) were adapted as the
> analytical framework…"

[10.1002/sce.21128](https://doi.org/10.1002/sce.21128) ·
[OA PDF](https://espace.curtin.edu.au/bitstream/20.500.11937/26961/2/200145_200145b.pdf)
`OBSERVED`

### 4.1 When MERs help vs. overload

**They help when the learner is prompted to relate them — not merely shown them.**
Hansen & Richland (2020), *CBE—Life Sciences Education*, mitosis/meiosis, middle
school + adults + pre-service teachers:

> "…most people reported **beliefs about teaching others that were different from
> beliefs about how they would learn**. Teaching beliefs were most often that others
> would learn better from presenting representations **one at a time, serially**;
> while learning beliefs were that they themselves would learn best from
> **simultaneous** presentations. **Students did learn best from simultaneously
> presented representations… but only when paired with self-explanation prompts to
> discuss the relationships between the graphics.**"

[10.1187/cbe.19-11-0253](https://doi.org/10.1187/cbe.19-11-0253) ·
[OA PDF](https://www.lifescied.org/doi/pdf/10.1187/cbe.19-11-0253) `MEASURED-RCT`

Three findings in one: (a) simultaneous beat serial; (b) **only with self-explanation
prompts**; (c) **instructor intuition about sequencing was wrong and was
systematically different from the same people's intuitions about their own
learning.** (c) is a direct warning against designing ladder sequencing by expert
introspection.

**They help when translation between representations is explicitly supported.** Van
der Meij & de Jong (2003/2006), N = 90, simulation-based physics ("moment"), three
conditions: separated / dynamically linked / integrated representations.
[OA PDF](https://ris.utwente.nl/ws/files/51155649/VanderMeij2003learning.pdf) `MEASURED-RCT`

**They overload when the learner lacks prior knowledge to interpret them.** Cook
(2006), *Science Education*, 533 citations:

> "Learners have a limited working memory, and instructional representations should be
> designed with the goal of reducing unnecessary cognitive load. However, cognitive
> architecture alone is not the only factor… **individual differences, especially
> prior knowledge, are critical** in determining what impact a visual representation
> will have."

[10.1002/sce.20164](https://doi.org/10.1002/sce.20164) ·
[OA PDF](https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/sce.20164) `OBSERVED`

**(N9) And they hurt when the multiplicity is surface-level** — Bennett, Inglis &
Gilmore (2019), already cited as N2: multiple *concrete* representations were worse
than a single abstract one, and the harm was attributable specifically to
multiplicity. [10.1037/edu0000318](https://doi.org/10.1037/edu0000318)
`MEASURED-RCT` — **negative result.**

**(N10) Adding coherent-but-extraneous material is costly.** The seductive-details
literature: Rey (2012), *Educational Research Review*, review + meta-analysis
[10.1016/j.edurev.2012.05.003](https://doi.org/10.1016/j.edurev.2012.05.003);
Sundararajan & Adesope (2020), "Keep it Coherent: A Meta-Analysis of the Seductive
Details Effect," *EPR*
[10.1007/s10648-020-09522-4](https://doi.org/10.1007/s10648-020-09522-4);
a 2026 multi-level meta-analysis + MASEM
[10.1007/s10648-025-10099-z](https://doi.org/10.1007/s10648-025-10099-z).
`MEASURED-META` (abstracts for the latter two were not retrievable this session; the
existence and direction of the effect are well established, pooled magnitudes are
**not asserted here**). The relevance to laddering is direct: an "engaging" ELI10 is
the natural habitat of seductive details.

---

## 5. Expertise reversal — why the ladder must be adaptive, and why preference must not drive it

### 5.1 The meta-analytic numbers

Tetzlaff, Simonsmeier, Peters & Brod (2025), "A cornerstone of adaptivity — A
meta-analysis of the expertise reversal effect," *Learning and Instruction*.
PRISMA-conformant; PsycINFO + ERIC searched Dec 2022 and Nov 2024; **1,590 studies
screened → 176 effect sizes from 60 experimental studies, N = 5,924**; `metafor` with
dependency handling:

> "**Low prior knowledge learners learn better from high-assistance instruction
> (d = 0.505). High prior knowledge learners learn better from low-assistance
> instruction (d = −0.428).** These effects are moderated by **the type of prior
> knowledge assessment, the educational status of the sample, and the domain** of the
> learned content. …the expertise reversal effect is **robust across a wide variety of
> contexts.** However, for **younger students** and some fields (**humanities and
> language learning**), the evidence for effectiveness is **less clear**. Furthermore,
> **the expertise reversal effect is not symmetrical: providing novices with
> assistance has a stronger effect than withholding assistance from experts.**"

[10.1016/j.learninstruc.2025.102142](https://doi.org/10.1016/j.learninstruc.2025.102142)
`MEASURED-META`

**Four things in that abstract change the design.**

1. **The `d = 0.971` interaction figure in the brief is not verifiable from the
   abstract.** The two verified marginal effects differ by ≈ **0.93**. Report 0.505 /
   −0.428 / ≈0.93; do not restate 0.971 without the full text. `UNVERIFIED-IN-SESSION`
2. **"Type of prior knowledge assessment" is a significant moderator.** How you
   measure the learner's level changes the size of the effect you are trying to
   exploit. The measurement instrument is not incidental to the system — it *is* the
   system.
3. **The effect is weaker for younger students and in humanities/language.** A ladder
   for a 10-year-old learning a language does not get to assume this mechanism.
4. **The asymmetry sets the default.** Under-assisting a novice costs more than
   over-assisting an expert. **Under uncertainty, enter one rung low and climb fast.**

### 5.2 The primary literature

- **Kalyuga, Ayres, Chandler & Sweller (2003)**, "The Expertise Reversal Effect,"
  *Educational Psychologist*, 1,860 citations — the canonical review: "Instructional
  techniques that are highly effective with inexperienced learners **can lose their
  effectiveness and even have negative consequences** when used with more experienced
  learners."
  [10.1207/S15326985EP3801_4](https://doi.org/10.1207/s15326985ep3801_4) ·
  [OA](http://handle.unsw.edu.au/1959.4/42177) `OBSERVED`
- **Kalyuga (2007)**, "Expertise Reversal Effect and Its Implications for
  **Learner-Tailored Instruction**," *EPR* — explicitly ties the effect to
  Aptitude-Treatment Interactions (Cronbach & Snow, mid-1960s) and to "recent
  experimental attempts of implementing these findings into **realistic adaptive
  learning environments**."
  [10.1007/s10648-007-9054-3](https://doi.org/10.1007/s10648-007-9054-3) ·
  [ERIC EJ785056](https://eric.ed.gov/?id=EJ785056) `OBSERVED`
- **Chen, Kalyuga & Sweller (2017)**, "The Expertise Reversal Effect is a Variant of
  the More General **Element Interactivity** Effect," *EPR*: both effects "rely on
  equivalent changes in element interactivity with the changes induced by different
  factors." [10.1007/s10648-016-9359-1](https://doi.org/10.1007/s10648-016-9359-1)
  `OBSERVED` — **theoretically the most useful framing for laddering**: a rung's
  correct level is a function of *element interactivity relative to the learner's
  schemas*, which is why the correct rung is per-concept, not per-person (§9c).
- **Rey & Buchwald (2011)**, *JEP: Applied*, N = 104, gradient descent, 2×2 (induced
  expertise × explanatory text): "Novices receiving additional text scored higher on
  retention and transfer than did novices without additional text, **while this result
  was reversed for experts.** …this effect can be explained by the learner's
  **cognitive load** differences rather than overall motivation differences."
  [10.1037/a0022243](https://doi.org/10.1037/a0022243) ·
  [ERIC EJ919603](https://eric.ed.gov/?id=EJ919603) `MEASURED-RCT`

**(N11) A partial null in the case that matters most for laddering.** Rey & Fischer
(2013), *Instructional Science* — the expertise reversal effect tested
specifically on **instructional explanations**, N = 93, expertise induced
experimentally, 2×2 (novice/expert × explanation present/absent):

> "The expertise reversal effect was **replicated for the dependent measure transfer,
> but not for retention.**"

[ERIC EJ999802](https://eric.ed.gov/?id=EJ999802) `MEASURED-RCT` — **partial negative
result.** This is the single closest experimental analogue to "give an ELI-explanation
to an expert," and the harm shows up on **transfer**, not on **retention**. A ladder
that measures itself with recall tests will not see the damage it is doing.

### 5.3 Adaptivity beats fixed schedules — and fixed support becomes harmful over time

- **Kalyuga & Sweller (2005)**, "Rapid dynamic assessment of expertise to improve the
  efficiency of adaptive e-learning," *ETR&D* — elementary algebra tutor, **yoked
  control design**: "instruction was dynamically tailored to changing levels of
  expertise using **rapid tests of knowledge combined with measures of cognitive
  load**… The experimental group demonstrated **higher knowledge and cognitive
  efficiency gains** than the control group."
  [10.1007/BF02504800](https://doi.org/10.1007/BF02504800) ·
  [OA](http://handle.unsw.edu.au/1959.4/42174) `MEASURED-RCT` — **the canonical entry-
  level-selection mechanism.**
- **Salden, Aleven, Schwonke & Renkl (2010)**, *Instructional Science* — one lab and
  one classroom experiment, Cognitive Tutor, three arms (standard tutored problem
  solving / fixed worked-example fading / **adaptive** fading): "**Both experiments
  provide evidence of improved learning results from adaptive fading over fixed fading
  over problem solving.**"
  [10.1007/s11251-009-9107-8](https://doi.org/10.1007/s11251-009-9107-8) ·
  [ERIC EJ880294](https://eric.ed.gov/?id=EJ880294) `MEASURED-RCT`
- **Nückles et al. (2010)**, *Instructional Science* — two longitudinal journal-writing
  studies over a term. Experiment 1: prompted group beat control in the first half of
  the term, then **lost its superiority** as the control group internalized the
  strategies. Experiment 2: gradual adaptive fading of prompts vs. permanent prompts —
  "at the end of the term, the **permanent prompts group showed substantially lower
  learning outcomes** than the fading group. …the more the students became skilled…
  the more the external guidance by prompts became a **redundant stimulus that
  interfered** with the students' internal tendency to apply the strategies."
  [ERIC EJ880291](https://eric.ed.gov/?id=EJ880291) `MEASURED-RCT` — **support that is
  not withdrawn turns negative.**
- **Blayney, Kalyuga & Sweller (2015)**, *Educational Technology & Society* — accounting, isolated vs.
  interactive element presentation. Experiment 1 found the interaction (expertise
  reversal). Experiment 2 assigned format **by pre-test of prior knowledge** vs. random
  assignment: "**the adaptive instruction group was superior to the non-adaptive
  group.**" [ERIC EJ1078240](https://eric.ed.gov/?id=EJ1078240) `MEASURED-RCT`
- A 2026 replication in an AI/VR context: N = 77, ANCOVA, "a significant Expertise
  Reversal Effect: AI significantly enhanced [outcome] for novices (low prior
  knowledge) by reducing cognitive load (mean difference = 0.169, p = 0.003), while VR
  induced overload in this group. Conversely, VR boosted [outcome] for high-prior-
  knowledge learners." [ERIC EJ1510005](https://eric.ed.gov/?id=EJ1510005) `MEASURED-RCT`

### 5.4 Preference is a corrupted signal

This is the hinge of deliverable (c), and it has its own literature.

**Scharrer, Rupieper, Stadtler & Bromme (2017)**, "When science becomes too easy:
Science popularization inclines laypeople to **underrate their dependence on
experts**," *Public Understanding of Science*, 150 citations:

> "…the simplification of information required to achieve this accessibility may lead
> to the risk of audiences **relying overly strongly on their own epistemic
> capabilities**… After reading popularized articles addressed to a lay audience,
> laypeople **agreed more with the knowledge claims** they contained and were **more
> confident in their claim judgments** than after reading articles addressed to expert
> audiences."

[10.1177/0963662516680311](https://doi.org/10.1177/0963662516680311) `MEASURED-RCT`

**Salzmann, Walther & Kaspar (2025)**, *Frontiers in Psychology*, N = 179, 2×2
(plain-language vs. scientific animated video abstract × debiasing video vs. none):

> "Animated PLS, compared to animated scientific abstracts, **actually enhanced
> comprehensibility**… This effect was accompanied by a **significant easiness
> effect**, as PLS were perceived as more credible and produced higher confidence in
> the recipients' perceived ability to evaluate the study… **the easiness effect… is
> very robust, as it persists even if a debiasing intervention is carried out
> beforehand.**"

[10.3389/fpsyg.2025.1584695](https://doi.org/10.3389/fpsyg.2025.1584695) ·
[OA PDF](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1584695/pdf)
`MEASURED-RCT` — **negative result for the obvious mitigation.** Warning learners
about the bias does not remove it.

**Buljan et al. (2018)**, *Journal of Clinical Epidemiology*, **three parallel RCTs**
(students n = 171, consumers n = 99, doctors n = 64), infographic vs. plain-language
summary vs. scientific abstract of a Cochrane review:

> "We found **no difference in knowledge** between the infographic and the text-based
> PLS in any of the trials or in the whole participant sample. **All three participant
> groups preferred the infographic** and gave it higher ratings for reading experience
> (d = 0.48) and user-friendliness (d = 0.46)."

[10.1016/j.jclinepi.2017.12.003](https://doi.org/10.1016/j.jclinepi.2017.12.003)
`MEASURED-RCT` — **negative result, and the cleanest possible demonstration that
preference and learning dissociate.** Preference moved by d ≈ 0.5 while knowledge
moved by zero.

Add Hansen & Richland (2020) from §4.1: instructor intuition about sequencing was
also wrong, and inconsistent with the same people's beliefs about their own learning.

`INFERENCE` — **Neither the learner's preference nor the instructor's intuition is an
admissible input to rung selection.** Both are measurably decoupled from learning
outcomes, in opposite directions. The only admissible input is *measured, concept-
specific prior knowledge plus measured load*.

---

## 6. Threshold concepts — which ideas cannot be simplified without being falsified

Meyer & Land (2005), "Threshold concepts and troublesome knowledge (2)," *Higher
Education*, ~1,463–1,525 citations:

> "…the generative notion of threshold concepts within (and across) disciplines, in
> the sense of **transforming the internal view of subject matter**… linked to forms
> of knowledge that are '**troublesome**', after Perkins (1999). …these twinned sets of
> ideas may define **critical moments of irreversible conceptual transformation** in
> the educational experiences of learners."

[10.1007/s10734-004-6779-5](https://doi.org/10.1007/s10734-004-6779-5) ·
[OA repository](https://durham-repository.worktribe.com/output/1601228) `OBSERVED`

Also: Meyer & Land (2003), the ETL project paper (1,054 citations) — a threshold
concept is "something distinct within what university teachers would typically
describe as 'core concepts'"; Land, Cousin, Meyer & Davies (2005), "implications for
course design and evaluation"; Meyer & Land (2006), *Overcoming Barriers to Student
Understanding*, [10.4324/9780203966273](https://doi.org/10.4324/9780203966273).

The five canonical criteria (transformative, irreversible, integrative, bounded,
troublesome) are the useful part for laddering: **a concept that is *transformative*
and *irreversible* is, by construction, one whose pre-crossing and post-crossing
renderings are not related by refinement.** That is exactly the class of concept for
which an honest ELI10 rung may not exist. `INFERENCE`

### 6.1 The framework is seriously contested — do not treat it as measurement

**(N12)** **Salwén (2019)**, "Threshold concepts, obstacles or scientific dead ends?",
*Teaching in Higher Education*:

> "Educational researchers have concluded that there are threshold concepts in a large
> number of disciplines. Yet, these researchers **have not paid enough attention to
> the objection** to the theory. It is beset with **severe definitional and empirical
> problems**… the definitions **fail**… and even if the definitional problems were
> solved and we were able to identify some threshold concepts, their **scientific
> importance would be limited if not nil.**"

[10.1080/13562517.2019.1632828](https://doi.org/10.1080/13562517.2019.1632828) ·
[ERIC EJ1282383](https://eric.ed.gov/?id=EJ1282383) `OBSERVED` — **negative result
(theoretical).**

**Stopford (2020)**, *Higher Education*: "TCF has struggled to articulate key
dimensions of its theory: **it is without a methodology for identifying threshold
concepts.** It has also faltered in explaining how student difficulty is a function of
difficulties endemic to the *concepts*, rather than as a contingent phenomenon about
individual *students*."
[10.1007/s10734-020-00628-w](https://doi.org/10.1007/s10734-020-00628-w) ·
[OA PDF](https://link.springer.com/content/pdf/10.1007/s10734-020-00628-w.pdf)
`OBSERVED`

**O'Donnell (2010)**, economics critique: the hypothesis "has deep-seated conceptual
problems… is subject to **disturbingly elastic interpretation**… some of its
educational and social consequences are undesirable," and opportunity cost — the
stock example — is "unsustainable" as a threshold concept.
[RePEc record](https://ideas.repec.org/p/mac/wpaper/1002.html) `OBSERVED`

**(N13) The one paper that tried to *measure* threshold crossing found it hard.**
Walck-Shannon, Batzli, Pultorak & Boehmer (2019), *CBE—Life Sciences Education*, biological variation, 29 students
in a cross-sectional design (Pre / Current / Post / postbaccalaureate Outgroup),
semistructured interviews coded on four dimensions (discursive, troublesome, liminal,
integrative):

> "Despite the value of threshold concepts as a learning 'portal' for heuristic
> purposes, **there is limited empirical evidence of threshold crossing or achieving
> mastery.** …**Pre, Post, and Outgroup explanations revealed liminality, with
> discomfort and uncertainty regardless of accuracy.**"

[10.1187/cbe.18-12-0241](https://doi.org/10.1187/cbe.18-12-0241) ·
[OA PDF](https://www.lifescied.org/doi/pdf/10.1187/cbe.18-12-0241) ·
[ERIC EJ1225640](https://eric.ed.gov/?id=EJ1225640) `MEASURED-BENCH`

Note the killer detail: **even the advanced outgroup showed liminality regardless of
accuracy.** "Feels uncertain" does not identify "has not crossed."

`INFERENCE` — **Use threshold concepts as a design *prompt*, never as a *classifier*.**
The framework has no identification methodology (Stopford), elastic definitions
(O'Donnell), and weak measurement (Batzli). A ladder generator that asks "is this a
threshold concept?" and branches on the answer is branching on an unreliable label.
The reliable substitute is the **ontology test** of §7, which is grounded in
conceptual-change research that *does* have measurement behind it.

---

## 7. The "lie-to-children" problem — is a productive simplification distinguishable from a planted misconception?

### 7.1 The two competing theories of what a learner brings

**Posner, Strike, Hewson & Gertzog (1982)**, "Accommodation of a scientific
conception: Toward a theory of conceptual change," *Science Education*, **5,087–5,553
citations** — [10.1002/sce.3730660207](https://doi.org/10.1002/sce.3730660207).
The classical four conditions for accommodation (dissatisfaction with the existing
conception; the new conception must be intelligible, plausible, and fruitful). Full
abstract not retrievable in this session (closed at Wiley, not in ERIC/S2).
`UNVERIFIED-IN-SESSION` for text; asserted here only as the canonical framework
citation.

**diSessa (1993)**, "Toward an Epistemology of Physics," *Cognition and Instruction*,
1,276–1,321 citations — **knowledge in pieces**:

> "…to understand the **intuitive sense of mechanism** that accounts for commonsense
> predictions, expectations, explanations… and to understand **how those intuitive
> ideas contribute to and develop into school physics.** …I provide a framework for
> describing and correlating characteristics of **weakly organized knowledge
> systems.**"

[10.1207/s1532690xci1002&3_2](https://doi.org/10.1207/s1532690xci1002&3_2)
`OBSERVED`. See also diSessa (2018), "A Friendly Introduction to 'Knowledge in
Pieces'": KiP "consists mainly of several detailed and empirically consequential
**models of different kinds of knowledge**, including both intuitive 'preconceptions'
and normative knowledge," spanning "**multiple time-scales — from details of real-time
learning to multi-year accomplishments**."
[10.1007/978-3-319-72170-5_5](https://doi.org/10.1007/978-3-319-72170-5_5) ·
[OA PDF](https://link.springer.com/content/pdf/10.1007%2F978-3-319-72170-5_5.pdf)
`OBSERVED`

**Chi (2005)**, "Commonsense Conceptions of Emergent Processes: **Why Some
Misconceptions Are Robust**," *JLS*, 873 citations — the ontological account:

> "…some processes (such as the apparent flow in diffusion of dye in water) are
> **emergent** and other processes (such as the flow of blood in human circulation)
> are **direct**… students' misconceptions for **direct** kinds of processes… are of
> **the same ontological kind as the correct conception**, suggesting that
> misconceptions of direct processes may be **nonrobust**. However, students'
> misconceptions of **emergent** processes are **robust** because [they are of a
> different ontological kind]."

[10.1207/s15327809jls1402_1](https://doi.org/10.1207/s15327809jls1402_1) `OBSERVED`

**This is the single most operationally useful result in the whole section.** It gives
a *principled, domain-general* criterion separating simplifications that can be
revised later from ones that cannot: **an error within an ontological category is
repairable; an error across ontological categories is not.** `INFERENCE`

### 7.2 The empirical evidence that simplifications become permanent

**Vosniadou & Brewer (1992)**, "Mental Models of the Earth: A Study of Conceptual
Change in Childhood," *Cognitive Psychology*, 1,670 citations. 60 students, grades
1/3/5, questioned about the earth's shape:

> "In the process of knowledge acquisition, children appear to **modify their initial
> models to make them more consistent with the culturally accepted model.**"

[10.1016/0010-0285(92)90018-W](https://doi.org/10.1016/0010-0285(92)90018-w) ·
[ERIC EJ455189](https://eric.ed.gov/?id=EJ455189) `MEASURED-BENCH`

The phenomenon this paper is famous for is the **synthetic model** — the hollow-sphere
earth, the flat-disc-inside-a-sphere earth — produced when instruction is *grafted onto*
an incompatible prior model instead of replacing it. Cross-culturally replicated:
Samarapungavan, Vosniadou & Brewer (1996), "Mental Models of the Earth, Sun, and Moon:
Indian Children's Cosmologies," *Cognitive Development* — "Indian children's
cosmologies honor a variety of implicit assumptions governing the construction of
**initial cosmological models**, and **folk models are also incorporated to provide a
psychologically easier way of satisfying first-order constraints.**"
[ERIC EJ538086](https://eric.ed.gov/?id=EJ538086) `MEASURED-BENCH`

**The Bohr atom, measured.** Cunha, Dias & Streit (2023), *Journal of Chemical
Education* — Brazilian
university chemistry students across three majors and lower/upper level courses,
structured questionnaires at the start and end of semester:

> "Students in upper-level courses achieved better averages than students in
> lower-level courses. …The number of students able to conceive a mental model of the
> atom based on quantum concepts increased by the end of the semester. **However, the
> number of students who imagined the atom according to the Bohr model, invoking both
> classical and quantum ideas, remained the same, suggesting no meaningful learning
> occurred.**"

[ERIC EJ1442536](https://eric.ed.gov/?id=EJ1442536) `MEASURED-BENCH` — **this is the
"lie-to-children" bill arriving.** The population holding the *synthetic*
classical-quantum hybrid did not shrink across a semester of university instruction
explicitly aimed at it. The taught simplification did not fade; it fused.

### 7.3 So: is a productive simplification distinguishable from a planted misconception?

`INFERENCE` — **Yes, and the distinguishing test is not vagueness-vs-precision. It is
whether the later account *refines* the earlier one or *contradicts* it.**

The literature above yields three separable failure classes:

| Class | What goes wrong | Evidence | Repairable? |
|---|---|---|---|
| **Under-specification** | The simple account is true but incomplete (drops precision, drops edge cases, drops mechanism depth) | — | **Yes.** The later account is a strict extension. |
| **Reductive collapse** | The learner over-extends a source analogy, reducing the target to the source's core | Spiro et al. 1989 (analogy-induced misconception) | **Partly.** Antidote: multiple disanalogous sources + declared limit set. |
| **Ontological miscategorization** | The simple account places the concept in the wrong ontological category (object where there is a process; direct process where the process is emergent; deterministic where stochastic) | Chi 2005; Vosniadou & Brewer 1992 synthetic models; the Bohr persistence data | **No.** These are the robust misconceptions. Instruction produces *synthetic* hybrids rather than replacement. |

The Bohr atom is a **class-3** error: it places a quantum stationary state in the
ontological category "object following a trajectory." That is why teaching it and then
un-teaching it does not work, and why the *Journal of Chemical Education* data shows
the hybrid population flat across a semester.

Compare a **class-1** simplification of the same subject: "electrons in an atom can
only have certain specific energies, and light is emitted when an electron changes
from one to another." Every proposition there survives into the quantum-mechanical
account verbatim. It drops the mechanism, the wavefunction, the selection rules, and
the entire concept of orbital shape. It falsifies nothing. **It is a legal ELI10 rung
for a concept whose most famous ELI10 rung is illegal.**

---

## 8. Self-explanation and the Feynman technique — explaining simply as a *learning* act

### 8.1 Self-explanation: strong, well-replicated, moderate

**Chi, de Leeuw, Chiu & LaVancher (1994)**, "Eliciting self-explanations improves
understanding," *Cognitive Science*, 2,118 + 729 citations across records. 14
eighth-graders prompted to self-explain after each line of a circulatory-system text
vs. 10 controls reading the text twice:

> "The prompted group had a **greater gain from the pretest to the posttest.**
> Moreover, prompted students who generated a large number of self-explanations (the
> **high explainers**) learned with greater understanding than **low explainers.**"

[10.1207/s15516709cog1803_3](https://doi.org/10.1207/s15516709cog1803_3) ·
[OA PDF](https://onlinelibrary.wiley.com/doi/pdfdirect/10.1207/s15516709cog1803_3)
`MEASURED-RCT` (small N)

**Bisra, Liu, Nesbit, Salimi & Winne (2018)**, "Inducing Self-Explanation: a
Meta-Analysis," *Educational Psychology Review*, 210–268 citations —
[10.1007/s10648-018-9434-x](https://doi.org/10.1007/s10648-018-9434-x). The published
abstract is elided by the publisher; the **numbers were recovered from the first
author's dissertation**, which reports the same analysis:

> "A meta-analysis was conducted on research that investigated learning outcomes of
> participants who received self-explanation prompts while studying or solving
> problems. Our systematic search… identified **69 effect sizes (from 64 research
> reports)**… The overall weighted mean effect size using a random effects model was
> **g = .55**. We coded and analyzed **20 moderator variables**…"

Bisra (2020), SFU dissertation — [summit.sfu.ca/item/20986](http://summit.sfu.ca/item/20986)
`MEASURED-META`

Also: Rittle-Johnson, Loehr & Durkin (2017), "Promoting self-explanation to improve
mathematics learning: A meta-analysis and instructional design principles," *ZDM*
[10.1007/s11858-017-0834-z](https://doi.org/10.1007/s11858-017-0834-z) (abstract
closed; existence + framing only) `UNVERIFIED-IN-SESSION`; Durkin (2011), SREE, "The
Self-Explanation Effect when Learning Mathematics: A Meta-Analysis"; Tan et al.
(2025), "Enhancing Academic Performance Through Self-Explanation in Digital Learning
Environments: A Three-Level Meta-Analysis," *EPR*
[10.1007/s10648-025-10001-x](https://doi.org/10.1007/s10648-025-10001-x) (abstract not
retrievable) `UNVERIFIED-IN-SESSION`.

Chi's **ICAP** framework (2009), *Topics in Cognitive Science*, 1,555 citations,
supplies the ordering hypothesis: "**interactive** activities are most likely to be
better than **constructive**, which in turn might be better than **active**, which are
better than being **passive**."
[10.1111/j.1756-8765.2008.01005.x](https://doi.org/10.1111/j.1756-8765.2008.01005.x) ·
[OA PDF](https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1756-8765.2008.01005.x)
`OBSERVED`

### 8.2 Learning by teaching / generating explanations for others

**Kobayashi (2022)**, "Do students learn what they teach when generating teaching
materials for others? A meta-analysis through the lens of learning by teaching,"
*Educational Research Review*, 43–60 citations —
[10.1016/j.edurev.2022.100475](https://doi.org/10.1016/j.edurev.2022.100475).
The publisher abstract is not exposed by Crossref, OpenAlex, or S2 in this session;
**the pooled effect size is therefore not asserted.** `UNVERIFIED-IN-SESSION`

Hansen & Richland (2020) — §4.1 — is relevant here too: representations helped **only
when paired with self-explanation prompts.**
[10.1187/cbe.19-11-0253](https://doi.org/10.1187/cbe.19-11-0253) `MEASURED-RCT`

### 8.3 The "Feynman technique" specifically has almost no research base

**(N14)** An ERIC search for `"Feynman technique"` across the entire corpus returns
**two records**, both from 2025–2026, both small, both from the same
English-as-a-second-language niche, and both combining the technique with analogical
reasoning so that it cannot be isolated:

- "An Instructional Exploration of Integrating Analogical Reasoning and the Feynman
  Technique in ESL at the Primary Level," *Journal of Education and Educational
  Development* (2025) — **qualitative, proposal-stage.**
- "The Impact of Analogical Learning and the Feynman Technique on English Achievement
  and Reasoning Ability in Grade Six: An Experimental Study," *Journal of English
  Teaching* (2026) — quasi-experimental, **n = 29 vs. n = 27**, two intact classes.

[ERIC search: "Feynman technique"](https://eric.ed.gov/?q=%22Feynman+technique%22)
`OBSERVED` — **absence of evidence.**

`INFERENCE` — **The Feynman technique is a folk repackaging of the self-explanation
effect.** The *mechanism* (generating an explanation, detecting gaps, iterating)
carries `g ≈ .55` from Bisra et al.'s 69 effect sizes. The *branded four-step
protocol* carries essentially nothing. Cite the mechanism; do not cite the brand as if
it were evidenced.

### 8.4 The consequence for laddering

`INFERENCE` — This flips the ladder from an output artifact into an assessment
instrument. If explaining simply is itself a learning act, then the highest-value use
of a ladder is not *serving* the learner an ELI10 but **asking the learner to produce
one**, and diffing it against the system's own rung. The diff localizes the gap: a
missing relation, a wrong ontological category, an over-extended analogy. This is
`INFERENCE`, but it is entailed by combining Chi (1994/2009) with the fidelity
taxonomy of §7.3 and §10.

---

## 9. Existing practice as corpus — what the world already ships

### 9.1 r/explainlikeimfive

Reddit is unreachable from this environment (§0), so the subreddit is characterised
through the peer-reviewed corpus built from it: **Fan, Jernite, Perez, Grangier,
Weston & Auli (2019), "ELI5: Long Form Question Answering," ACL** —
[10.18653/v1/P19-1346](https://doi.org/10.18653/v1/p19-1346) ·
[arXiv:1907.09190](https://arxiv.org/abs/1907.09190) `MEASURED-BENCH`

The dataset is ~270K threads of questions requiring multi-sentence explanatory
answers. Two properties matter for laddering: (i) the community's operative norm is
"**layperson-friendly, not literally for a five-year-old**" — the "5" is a genre
signal, not a reading level; (ii) ELI5 answers are *long-form* — simplification in
practice **increases** length rather than decreasing it, because dropped formalism has
to be replaced by narrative. `INFERENCE` (property ii follows from the task
definition; the rule text itself is `UNVERIFIED-IN-SESSION`).

### 9.2 Simple English Wikipedia — the only corpus with an explicit written spec

Fetched from
[Wikipedia:How to write Simple English pages](https://simple.wikipedia.org/wiki/Wikipedia:How_to_write_Simple_English_pages)
`OBSERVED`:

- **Vocabulary is tiered, not fixed**: primary target **Basic English 850**; **BE 1500**
  when BE 850 "sounds unnatural"; **VOA Special English** when clarity requires less
  common terms. The guideline explicitly declines a hard cap: Simple English "follows
  some of the rules of Basic English, but **is not so strict** about using only a
  certain number of words."
- **Syntax**: prefer subject–verb–object; "**try to avoid compound sentences** — those
  with embedded conjunctions"; "try to have **only one subordinate clause**."
- **Voice/person**: active voice ("change 'The bird was eaten by the cat' to 'The cat
  ate the bird'"); no contractions; not second person.
- **The fidelity clause**: "**Simple English is not bad English**" — the *ideas* do not
  have to be simple, only the language, and "explanations and context should be added
  when necessary to preserve accuracy."

That last clause is, verbatim, a hand-written version of the fidelity rule this
section formalizes in §11. It is the only place in the surveyed corpus where the
"drop vs. falsify" distinction is stated as policy rather than discovered as a bug.

### 9.3 Tiered abstracts / plain-language summaries — the measured tier system

Nature and PNAS author-guideline pages are unreachable (§0). But the **plain-language-
summary** literature measures exactly the phenomenon a tiered abstract is supposed to
produce, and it is the most directly relevant applied corpus in the section.

**It works on readability.** Stricker, Chasiotis, Kerwer & Günther (2020), *PLoS ONE*,
103 article/PLS pairs from two psychology journals, four readability indices, ANOVA:
"**PLS were easier to read than scientific abstracts.** This effect emerged in both
included journals and **across all readability indices.**"
[10.1371/journal.pone.0231160](https://doi.org/10.1371/journal.pone.0231160)
`MEASURED-BENCH`

**It works on comprehension.** Kerwer, Chasiotis, Stricker, Günther & Rosman (2021),
*Collabra: Psychology*, preregistered within-person design, N = 166:
"comprehensibility for laypeople was **higher for plain language summaries**… and we
also found that laypeople **actually understood the corresponding information more
correctly**… Moreover, **in line with the easiness effect of science popularization**,
individuals perceived PLS as **more credible** and were **more confident** about their
ability to make a decision based on them."
[10.1525/collabra.18898](https://doi.org/10.1525/collabra.18898) `MEASURED-RCT`

Note the same paper reports both the benefit **and** the easiness-effect cost.

**(N15) But they still miss their target audience.** Wen & Yi (2024), *Public
Understanding of Science*, large corpus from six biomedical/life-sciences journals:
"(1) PLS were more readable than scientific abstracts… (4) **the readability of and
the jargon use in both plain language summaries and scientific abstracts exceeded the
recommended threshold for the general public.**"
[10.1177/09636625241252565](https://doi.org/10.1177/09636625241252565)
`MEASURED-BENCH` — **negative result: the tier exists but does not land.** A "tier"
declared by an author is not a tier achieved for a reader.

**(N16) And format changes preference far more than knowledge.** Buljan et al. (2018),
three RCTs — see §5.4. `MEASURED-RCT`

Supporting: "Comparing lay summaries to scientific abstracts for readability and
jargon use," *Scientometrics* (2023)
[10.1007/s11192-023-04807-1](https://doi.org/10.1007/s11192-023-04807-1);
"Plain language summaries: A systematic review of theory, guidelines and empirical
research," *PLoS ONE* (2022)
[10.1371/journal.pone.0268789](https://doi.org/10.1371/journal.pone.0268789);
"Video abstracts and plain language summaries are more effective than graphical
abstracts and published abstracts," *PLoS ONE* (2019)
[10.1371/journal.pone.0224697](https://doi.org/10.1371/journal.pone.0224697).
`MEASURED-BENCH`

### 9.4 The corpus verdict

`INFERENCE` — Every existing tiering practice in §9 shares one defect: **the tier is
defined by the producer's intent and validated (if at all) by readability formulas,
never by a fidelity constraint linking the tiers to each other.** Simple English
Wikipedia states the fidelity principle in prose but has no mechanism enforcing it.
PLS have measurement (readability, comprehension) but no relation to the abstract they
summarize other than topical. Nobody in the surveyed corpus ships a **refinement
chain**. That absence is the contribution space.

---

## 10. DELIVERABLE (a) — A level taxonomy

`INFERENCE` throughout §10–§12. These are constructions, not findings; each dimension
is anchored to a cited result.

### 10.1 Why not readability formulas

The obvious operationalization — Flesch–Kincaid grade level — is the wrong instrument.
Crossley et al. (2017), *Discourse Processes*, adult readers, NLP + crowd ratings +
machine learning: "the results indicate the **traditional readability formulas are
less predictive** than models of text comprehension, processing, and familiarity
derived from advanced natural language processing tools."
[ERIC EJ1151995](https://eric.ed.gov/?id=EJ1151995) `MEASURED-BENCH`

The older debate is unresolved in the direction that matters: defenders argue formulas
"predict (are correlated with) comprehension" ([ERIC ED267385](https://eric.ed.gov/?id=ED267385));
critics argue they "**overlook text and reader characteristics that affect
comprehension**" and that "shortened sentences and simplified vocabulary used to
conform texts to formulas **sacrifice precision and connectedness, thus reducing
comprehensibility**" ([ERIC EJ319793](https://eric.ed.gov/?id=EJ319793)). `OBSERVED`

That last critique is decisive for laddering: **optimizing a rung against a readability
formula is a documented way to make it less comprehensible.** Sentence length is a
symptom of the real variables, not one of them.

### 10.2 The eight operational dimensions

| # | Dimension | Definition | Anchor |
|---|---|---|---|
| **D1** | **Prerequisite closure size** `|P|` | Count of distinct concepts that must already be held for the rung to be interpretable, transitively closed | Element interactivity (Chen/Kalyuga/Sweller 2017); Cook 2006 |
| **D2** | **Formalism grade** `F0–F4` | F0 natural language only · F1 named quantities, arithmetic, proportion · F2 algebra, functions, graphs · F3 calculus / linear algebra / probability notation · F4 proof-level with explicit quantifiers and existence conditions | Bruner enactive→iconic→symbolic; Fyfe & Nathan 2018 |
| **D3** | **Representation ladder position** | enactive / iconic / notational-concrete / symbolic; plus **number of simultaneous representations** and whether they are **aligned** | Goldstone & Son 2005; Ainsworth DeFT; Bennett et al. 2019 (multiplicity harms if unaligned) |
| **D4** | **Vocabulary tier budget** | Max domain-technical (Tier-3) terms introduced per 100 words, and whether each is glossed on first use | Simple English Wikipedia BE850/BE1500/VOA tiering; Wen & Yi 2024 (jargon is the binding constraint, not sentence length) |
| **D5** | **Relational order** | Highest order of relation asserted: 0 = attributes · 1 = single causal relation · 2 = causal chain · 3 = interacting systems of constraints | Gentner 1983 systematicity; Gentner 1988 relational shift |
| **D6** | **Scope-condition density** | Count of explicitly stated assumptions, domain restrictions, and "except when" clauses retained | Chi 2005 (direct vs. emergent); the fidelity rule §11 |
| **D7** | **Edge-case retention ratio** | Fraction of the concept's known boundary cases that are stated (even if unexplained) | §11 scope-flag requirement |
| **D8** | **Assessment ceiling** | What the learner can now do: recognize → retell → predict a familiar case → apply to a new instance in-context → derive → far-transfer → identify the model's failure conditions → critique/extend | Transfer as the outcome that discriminates (Goldstone & Son 2005; McNeil & Fyfe 2012; ERIC EJ999802 — reversal appears on transfer, not retention) |

### 10.3 The five rungs, operationally

| | **ELI10** | **ELI15** | **ELI20** | **ELI25** | **Research** |
|---|---|---|---|---|---|
| **D1** `|P|` | ≤ 5, all everyday | ≤ 15, school-level | course-level prerequisite chain | graduate prerequisite chain | active literature |
| **D2** Formalism | **F0–F1** | **F1–F2** | **F2–F3** | **F3–F4** | **F4** |
| **D3** Representation | enactive or notational-concrete; **exactly one** primary instantiation, plus **one aligned contrast** | iconic + symbolic **side by side, explicitly linked** | symbolic-primary, iconic support on demand | symbolic only | symbolic + formal counterexamples |
| **D4** Tier-3 budget | ≤ 2 per explanation, each glossed, each **the real term** (never a coined substitute) | ≤ 6, glossed | unbounded, defined on first use | assumed | assumed, contested terms flagged |
| **D5** Relational order | **1** (one causal relation, stated explicitly) | **2** (a causal chain) | **3** (interacting constraints) | 3 + formal structure | 3 + open structure |
| **D6** Scope conditions | **0 stated, ≥1 flagged** ("this holds when… we'll come back to why") | 1–2 stated | full assumption list | assumptions + their necessity | assumptions + which are known to be relaxable |
| **D7** Edge cases | 0 explained, **all flagged by existence** | the 1–2 that a learner will meet | those inside the stated scope | all known | including disputed ones |
| **D8** Ceiling | recognize, retell, predict a familiar case | apply to a new instance in-context | derive; near transfer; state when it breaks | far transfer; critique; extend | identify what would falsify it; design a study |

**Three constraints on using this table:**

1. **A learner traverses two or three rungs, not five.** Three-step beat two-step;
   five-step did not beat three-step ([ERIC EJ1510953](https://eric.ed.gov/?id=EJ1510953),
   H3 supported / H4 not). The five rungs exist so that different learners *enter* at
   different points — they are a **library**, not an itinerary.
2. **D4's "never a coined substitute" is load-bearing.** Replacing "eigenvalue" with
   "stretchiness number" creates a term the learner must later *unlearn* and cannot
   look up. Simplify the *explanation*, keep the *name*. This is the vocabulary
   corollary of §11.
3. **ELI10 renders at relational order 1, deliberately.** Gentner (1988): the
   attributional→relational shift is not complete at 10. A rung that asserts a
   three-deep causal chain to a ten-year-old will be *received* as a set of attributes,
   which is the reductive-collapse failure of §7.3.

---

## 11. DELIVERABLE (b) — The fidelity rule

### 11.1 The core constraint: monotone refinement

> **A rung at level `n` is legal iff every proposition it asserts is entailed by the
> level-`n+1` account under an explicitly stated domain restriction. Climbing may add
> and may narrow scope. Climbing may never require negating a previously asserted
> proposition.**

Equivalently: the ladder is a **refinement chain**, not five independent texts. Level
`n` = level `n+1` minus declared drops. This is why ladders must be generated
**top-down**: you cannot check a non-falsification constraint against an account you
have not written yet.

### 11.2 What a simplification MAY drop

| Droppable | Why safe | Anchor |
|---|---|---|
| **Numeric precision** | Refinement, not contradiction | — |
| **Higher-order corrections** | Strict addition later | — |
| **Formal machinery** (the derivation, the notation, the proof) | The *claim* survives; only its warrant is deferred | Fyfe & Nathan 2018 (fading is subtraction of specifics) |
| **Mechanism depth** — black-boxing a subcomponent | Legal **iff** the box is *named* as a box | §11.4 |
| **Edge cases outside the declared scope** | Legal **iff** the scope is declared | Chi 2005 |
| **Historical provenance, attribution, competing formulations** | Not truth-bearing about the object | — |
| **One of several equivalent formulations** | Legal **iff** not asserted as *the* formulation | Kokkonen & Schalk 2021 (roles of representations vary by domain) |

### 11.3 What a simplification may NEVER falsify

| Never | Failure mode | Anchor |
|---|---|---|
| **Ontological category** — thing vs. process vs. **emergent** process; object vs. field vs. state | Produces the *robust*, non-repairable misconception class | **Chi 2005** — misconceptions across ontological kinds are robust; within-kind are not |
| **Sign or direction of a causal relation** | Requires literal negation to fix | Gentner 1983 (relations are what gets mapped) |
| **Deterministic vs. stochastic vs. emergent** character | Special case of ontological category; the most common one in practice | Chi 2005 |
| **Quantifier strength** — "all" asserted where only "some" holds | Cannot be narrowed later without retraction | — |
| **Conservation / invariance / impossibility claims** | These *are* the structure; weakening them changes the concept | — |
| **Uniqueness of a mechanism** — presenting one of several mechanisms as *the* mechanism | Reductive collapse | **Spiro et al. 1989** |
| **Existence of a boundary** — implying a model is unrestricted when it is not | Undeclared drops are indistinguishable from planted misconceptions at retrieval | Vosniadou & Brewer 1992 (synthetic models) |

**Worked contrast (the Bohr case).**

- *Illegal (class-3, ontological):* "Electrons orbit the nucleus like planets orbit the
  sun." Places a stationary state in the category "object on a trajectory." Empirically
  this does not wash out: [ERIC EJ1442536](https://eric.ed.gov/?id=EJ1442536) found the
  classical-quantum hybrid population **unchanged across a semester** of university
  chemistry.
- *Legal (class-1, under-specification):* "An electron in an atom can only have certain
  specific amounts of energy — not anything in between. Light is given off when it
  drops from a higher one to a lower one." Every proposition survives into the full
  quantum account. Nothing is negated later; the ELI25 rung *adds* the wavefunction,
  the orbital, and the selection rules.

### 11.4 Four tests a rung must pass

1. **Entailment test.** Take every declarative sentence in rung `n`. Is each entailed
   by rung `n+1` under the rung's declared scope? Any sentence requiring the word
   "actually" or "in fact" at level `n+1` is a fidelity violation.
2. **Ontology test (Chi).** Does the rung place the concept in the correct ontological
   category — *thing*, *direct process*, or *emergent process*? A category error is
   non-negotiable regardless of how helpful it feels. This is the test that replaces
   the unreliable "is it a threshold concept?" classifier (§6.1).
3. **Scope-flag requirement.** Every drop must leave a **named, retrievable marker** —
   not a vague "it's more complicated than that," but a token the learner can carry
   upward: *"This assumes no friction — the friction case is rung 3."* Undeclared drops
   are, at retrieval time, indistinguishable from planted misconceptions.
4. **Analogy contract (§3.4).** Every analogy ships with a declared **alignment set**
   and a declared **limit set**. For concepts with high reductive-bias risk, ship **two
   mutually disanalogous** analogies rather than one good one (Spiro et al. 1989).

### 11.5 When no legal ELI10 exists

Some concepts fail test 2 at every simplification a designer can construct: any
sufficiently simple rendering commits an ontological error. This is what "threshold
concept" was gesturing at, minus the identification problem (§6.1).

`INFERENCE` — For these, the correct move is not a false model but a **pre-concept
rung**: build the *phenomenology* without asserting a *mechanism*. Clement's
**anchoring intuitions** are exactly this — "not all preconceptions are
misconceptions"; find the intuition the learner already holds that is *correct*, and
build a **bridging chain** from it (Clement 1993,
[10.1002/tea.3660301007](https://doi.org/10.1002/tea.3660301007); measured version:
[ERIC ED283712](https://eric.ed.gov/?id=ED283712), significant gains on target **and
transfer** problems).

Operationally: rung 0 states **what happens** and **what is surprising about it**, and
explicitly declines to say why. "When you cool helium enough it flows up the walls of
its container. Nothing in everyday physics explains that. Here is what it rules out…"
This is honest, is a real rung by D8 (ceiling: *recognize + predict*), and plants
nothing.

---

## 12. DELIVERABLE (c) — How a system should choose the entry level

### 12.1 The five rules, each with its warrant

**R1 — Measure, never ask.**
Rung selection is driven by **measured, concept-specific prior knowledge plus measured
cognitive load**, never by stated preference, self-rated expertise, or declared goal.
Warrant: Buljan et al. 2018 — preference moved d ≈ 0.48 while knowledge moved **zero**
([10.1016/j.jclinepi.2017.12.003](https://doi.org/10.1016/j.jclinepi.2017.12.003));
Scharrer et al. 2017 and Salzmann et al. 2025 — simplification *raises* confidence and
perceived credibility independent of competence, and the bias **survives explicit
debiasing** ([10.1177/0963662516680311](https://doi.org/10.1177/0963662516680311),
[10.3389/fpsyg.2025.1584695](https://doi.org/10.3389/fpsyg.2025.1584695)). A learner
who has just read an ELI10 is *more* confident and *therefore less* likely to ask for
ELI15. Preference-driven laddering has a built-in downward ratchet.

Instructor intuition is also inadmissible: Hansen & Richland 2020 found teaching
intuitions about sequencing were wrong **and** inconsistent with the same individuals'
beliefs about their own learning
([10.1187/cbe.19-11-0253](https://doi.org/10.1187/cbe.19-11-0253)).

**R2 — Use rapid dynamic assessment, and re-run it continuously.**
The validated instrument is Kalyuga & Sweller's **rapid dynamic assessment**: short
first-step/verification tasks that probe the *content of working memory*, combined
with a cognitive-load rating; instruction retargeted on the fly. Under a yoked control
design this produced higher knowledge **and** cognitive-efficiency gains
([10.1007/BF02504800](https://doi.org/10.1007/BF02504800)). Kalyuga 2015 confirms the
end-to-end result: assigning format by pre-test beat random assignment
([ERIC EJ1078240](https://eric.ed.gov/?id=EJ1078240)).

Corollary from Tetzlaff et al. 2025: **the type of prior-knowledge assessment is a
significant moderator of the effect size.** The probe design is not incidental — it is
the largest tunable parameter in the system.

**R3 — Select per prerequisite, not per learner; take the minimum.**
Prior knowledge is concept-specific, and the relevant quantity is element interactivity
*relative to the learner's existing schemas* (Chen, Kalyuga & Sweller 2017,
[10.1007/s10648-016-9359-1](https://doi.org/10.1007/s10648-016-9359-1)). The same
person is ELI25 on linear algebra and ELI10 on measure theory. Compute a **mastery
vector over the concept's prerequisite closure (D1)** and set the entry rung to the
**weakest link**, then ladder that prerequisite independently rather than dragging the
whole explanation down.

**R4 — Under uncertainty, enter one rung low and climb fast.**
Tetzlaff et al.: novices + assistance **d = 0.505**; experts + assistance
**d = −0.428**; the effect is **not symmetrical** — "providing novices with assistance
has a stronger effect than withholding assistance from experts." The expected cost of
under-shooting is smaller than the expected cost of over-shooting, so the prior should
be low. But the gap between the two marginals (≈ 0.93) means mis-targeting is still
the largest single design lever in the system — a low entry rung is a *default*, not
an excuse to skip R2.

Two caveats from the same abstract: the effect is **weaker for younger students and in
humanities/language learning.** Do not assume this mechanism for a 10-year-old learning
a language.

**R5 — Fading must itself be adaptive, and support must actually be withdrawn.**
Salden et al. 2010: adaptive fading of worked examples > fixed fading > tutored problem
solving, in both a lab and a classroom experiment
([10.1007/s11251-009-9107-8](https://doi.org/10.1007/s11251-009-9107-8)). Nückles et
al. 2010: permanent prompts produced **substantially lower** outcomes than faded
prompts by end of term, because internalized strategies make external support a
"redundant stimulus that interfered"
([ERIC EJ880291](https://eric.ed.gov/?id=EJ880291)). **A system that leaves a learner
on ELI15 because they never asked to move is actively harming them by week 6.**

### 12.2 The control loop

```
for each concept C requested by learner L:
  1. P ← transitive prerequisite closure of C            # D1
  2. m ← rapid dynamic assessment over P                 # R2, Kalyuga & Sweller 2005
     (2–4 first-step items per prerequisite + subjective load rating)
  3. rung ← min over p in P of level(m[p]) − 1           # R3 weakest link, R4 low prior
  4. render rung under the fidelity rule (§11)           # top-down, never bottom-up
  5. probe with a TRANSFER item, not a recall item       # ERIC EJ999802: reversal
                                                          appears on transfer only
  6. climb  iff  transfer correct AND load low
     hold   iff  transfer correct AND load high      → same rung, aligned second
                                                        instantiation (Goldstone & Son)
     descend iff two consecutive transfer failures
  7. re-run step 2 on a schedule; force-fade assistance  # R5, Nückles 2010
```

**Notes on the loop.**

- **Step 5 is the one people get wrong.** Rey & Fischer (2013) found the expertise
  reversal effect for **instructional explanations** replicated on *transfer* but
  **not** on *retention* ([ERIC EJ999802](https://eric.ed.gov/?id=EJ999802)). A ladder
  that self-evaluates with recall questions is instrumented to be blind to its own
  primary failure mode.
- **Step 6's "hold" branch is not a stall.** When transfer succeeds but load is high,
  the evidenced move is a **second aligned instantiation at the same level** —
  multiple instantiation is the robust part of the concreteness-fading result
  (Goldstone & Son 2005), and comparison-based encoding is what converts examples into
  schemas (Gentner, Loewenstein & Thompson 2003). This must be an **aligned** contrast,
  not surface variety: unaligned multiplicity is what harmed learners in Bennett et al.
  2019.
- **Step 4's "top-down, never bottom-up"** is forced by §11.1. Generating ELI10 first
  and then "adding detail" cannot satisfy the entailment test, because there is no
  level-`n+1` account to check against.
- **The learner-produced rung.** From §8.4: the highest-information probe available is
  asking the learner to *write* the ELI10 and diffing it against the system's. The diff
  localizes the defect by class (missing relation / wrong ontology / over-extended
  analogy — §7.3), and the act of writing it carries the self-explanation effect
  (g ≈ .55, Bisra et al. 2018). This is `INFERENCE`, not a measured design, but it is
  the cheapest way to make step 5 diagnostic rather than merely binary.

### 12.3 What this design refuses to do

- **No "choose your level" dropdown as the primary control.** (R1.) It may exist as an
  override; it may never be the default input. The easiness effect guarantees it drifts
  down.
- **No level inferred from stated credentials or self-rated expertise.** (R2 —
  assessment type is a significant moderator; self-report is not one of the assessed
  types.)
- **No single global level per learner.** (R3.)
- **No fixed five-step traversal.** (§1.3 N4: five-step did not beat three-step,
  p = 0.738.)
- **No optimizing rungs against readability formulas.** (§10.1: documented to *reduce*
  comprehensibility by sacrificing precision and connectedness,
  [ERIC EJ319793](https://eric.ed.gov/?id=EJ319793).)

---

## 13. Negative and null results, collected

Required by the project's evidence rules; gathered here for auditability.

| # | Finding | Source |
|---|---|---|
| N1 | Concreteness fading **statistically equivalent** to simultaneous presentation, pre-specified bounds d = ±0.5, N = 187 | [10.1002/tea.21947](https://doi.org/10.1002/tea.21947) |
| N2 | **Multiple concrete representations harmed** symbol learning vs. a single abstract one; harm attributable to multiplicity | [10.1037/edu0000318](https://doi.org/10.1037/edu0000318) |
| N3 | **Greater contextualization → poorer transfer**, both undergraduates and middle schoolers, ecological settings | [10.3389/fpsyg.2015.01876](https://doi.org/10.3389/fpsyg.2015.01876) |
| N4 | **3 of 4 hypotheses null** in computing replication; five-step ≯ three-step (p = 0.738) | [ERIC EJ1510953](https://eric.ed.gov/?id=EJ1510953) |
| N5 | Concreteness-fading benefit **moderated by grade level** (significant condition × grade interaction) | [10.1007/s11251-017-9428-y](https://doi.org/10.1007/s11251-017-9428-y) |
| N6 | Concreteness fading **not domain-general** on principled analysis | [10.1007/s10648-020-09581-7](https://doi.org/10.1007/s10648-020-09581-7) |
| N7 | The theory's own authors: *abstract*, *concrete*, *fading* were **undefined** | [10.1080/00131911.2018.1424116](https://doi.org/10.1080/00131911.2018.1424116) |
| N8 | **Contrasting analogies for natural selection: no group differences** on understanding or reasoning | [ERIC ED547079](https://eric.ed.gov/?id=ED547079) |
| N9 | (= N2, in the MER frame) | — |
| N10 | Seductive details: coherent-but-extraneous material is **costly** | [10.1007/s10648-020-09522-4](https://doi.org/10.1007/s10648-020-09522-4) |
| N11 | Rey & Fischer 2013: expertise reversal for **instructional explanations** replicated on transfer but **not retention** | [ERIC EJ999802](https://eric.ed.gov/?id=EJ999802) |
| N12 | Salwén 2019: threshold-concept **definitions fail; scientific importance "limited if not nil"** | [10.1080/13562517.2019.1632828](https://doi.org/10.1080/13562517.2019.1632828) |
| N13 | Threshold crossing: **limited empirical evidence**; liminality present even in the advanced outgroup **regardless of accuracy** | [10.1187/cbe.18-12-0241](https://doi.org/10.1187/cbe.18-12-0241) |
| N14 | **"Feynman technique": two ERIC records total**, both tiny, both confounded with analogical reasoning | [ERIC search](https://eric.ed.gov/?q=%22Feynman+technique%22) |
| N15 | Plain-language summaries **still exceed the readability threshold for the general public** — the tier does not land | [10.1177/09636625241252565](https://doi.org/10.1177/09636625241252565) |
| N16 | Infographic vs. PLS: **no knowledge difference** across three RCTs, while preference moved d ≈ 0.48 | [10.1016/j.jclinepi.2017.12.003](https://doi.org/10.1016/j.jclinepi.2017.12.003) |
| N17 | **No clear empirical evidence** for overall effects of the spiral curriculum (ERIC research brief) | [ERIC ED538282](https://eric.ed.gov/?id=ED538282) |
| N18 | Easiness effect **survives an explicit debiasing intervention** | [10.3389/fpsyg.2025.1584695](https://doi.org/10.3389/fpsyg.2025.1584695) |
| N19 | Bohr-model synthetic conception **did not shrink** across a semester of university chemistry | [ERIC EJ1442536](https://eric.ed.gov/?id=EJ1442536) |
| N20 | Permanent (non-faded) prompts → **substantially lower** end-of-term outcomes than faded prompts | [ERIC EJ880291](https://eric.ed.gov/?id=EJ880291) |
| N21 | Traditional readability formulas **less predictive** than NLP comprehension models; formula-conformance can **reduce** comprehensibility | [ERIC EJ1151995](https://eric.ed.gov/?id=EJ1151995) · [ERIC EJ319793](https://eric.ed.gov/?id=EJ319793) |

---

## 14. Open questions this section could not close

1. **No pooled effect size for concreteness fading exists.** Fyfe et al. 2014 is a
   *systematic review*, not a meta-analysis. Given N1/N4/N5/N6, a proper meta-analysis
   would plausibly return a small and heterogeneous estimate. Nobody should quote a
   number for this technique today.
2. **The `d = 0.971` interaction figure** for expertise reversal is unverified (§5.1);
   the abstract supports 0.505 / −0.428 only.
3. **No study in the retrieved literature tests laddering as such** — i.e. the same
   concept authored at N levels under a fidelity constraint, with entry-level chosen by
   measurement. Every component is evidenced; the composite is not. That is
   simultaneously the contribution and the risk.
4. **The fidelity rule (§11) is untested.** Its ontology test rests on Chi 2005, which
   is well-cited and well-argued but is a theoretical account supported by domain
   examples, not an RCT of a design rule. The obvious experiment — same concept, same
   rungs, entailment-checked vs. not, measured by *later* transfer after the advanced
   rung — does not appear to have been run.
5. **Learner-authored rungs as assessment** (§8.4, §12.2) combines two well-evidenced
   effects but is itself `INFERENCE`.

---

## 15. Source index

Concreteness fading: [10.1007/s10648-014-9249-3](https://doi.org/10.1007/s10648-014-9249-3) ·
[10.1016/j.learninstruc.2012.05.001](https://doi.org/10.1016/j.learninstruc.2012.05.001) ·
[10.1016/j.learninstruc.2014.10.004](https://doi.org/10.1016/j.learninstruc.2014.10.004) ·
[10.1207/s15327809jls1401_4](https://doi.org/10.1207/s15327809jls1401_4) ·
[10.1080/00131911.2018.1424116](https://doi.org/10.1080/00131911.2018.1424116) ·
[10.1007/s10648-020-09581-7](https://doi.org/10.1007/s10648-020-09581-7) ·
[10.1002/tea.21947](https://doi.org/10.1002/tea.21947) ·
[10.1037/edu0000318](https://doi.org/10.1037/edu0000318) ·
[10.3389/fpsyg.2015.01876](https://doi.org/10.3389/fpsyg.2015.01876) ·
[10.1007/s11251-017-9428-y](https://doi.org/10.1007/s11251-017-9428-y) ·
[ERIC EJ1510953](https://eric.ed.gov/?id=EJ1510953) ·
[10.1080/10508406.2016.1250212](https://doi.org/10.1080/10508406.2016.1250212) ·
[10.1016/j.compedu.2020.103811](https://doi.org/10.1016/j.compedu.2020.103811) ·
[10.3390/su12062211](https://doi.org/10.3390/su12062211) ·
[10.1145/3392063.3394413](https://doi.org/10.1145/3392063.3394413) ·
[10.1016/j.learninstruc.2021.101524](https://doi.org/10.1016/j.learninstruc.2021.101524)

Spiral curriculum: [10.1080/01421599979752](https://doi.org/10.1080/01421599979752) ·
[ERIC ED538282](https://eric.ed.gov/?id=ED538282) ·
[ERIC EJ1430484](https://eric.ed.gov/?id=EJ1430484) ·
[ERIC ED638864](https://eric.ed.gov/?id=ED638864) ·
[10.1039/b806232n](https://doi.org/10.1039/b806232n) ·
[10.1186/1472-6920-7-52](https://doi.org/10.1186/1472-6920-7-52) ·
[ERIC EJ1364684](https://eric.ed.gov/?id=EJ1364684)

Analogy / structure mapping: [10.1016/S0364-0213(83)80009-3](https://doi.org/10.1016/s0364-0213(83)80009-3) ·
[10.1207/s15516709cog1003_2](https://doi.org/10.1207/s15516709cog1003_2) ·
[10.2307/1130388](https://doi.org/10.2307/1130388) ·
[10.1037/0022-0663.95.2.393](https://doi.org/10.1037/0022-0663.95.2.393) ·
[10.3758/BF03212967](https://doi.org/10.3758/bf03212967) ·
[10.1006/obhd.2000.2887](https://doi.org/10.1006/obhd.2000.2887) ·
[10.1111/j.1551-6709.2009.01070.x](https://doi.org/10.1111/j.1551-6709.2009.01070.x) ·
[10.1207/s15516709cog1303_1](https://doi.org/10.1207/s15516709cog1303_1) ·
[10.1017/CBO9780511529863.023](https://doi.org/10.1017/cbo9780511529863.023) ·
[10.1002/sce.3730750606](https://doi.org/10.1002/sce.3730750606) ·
[10.1002/tea.3660301007](https://doi.org/10.1002/tea.3660301007) ·
[ERIC ED283712](https://eric.ed.gov/?id=ED283712) ·
[ERIC EJ751998](https://eric.ed.gov/?id=EJ751998) ·
[ERIC EJ933450](https://eric.ed.gov/?id=EJ933450) ·
[ERIC ED547079](https://eric.ed.gov/?id=ED547079) ·
[10.1080/0950069042000276712](https://doi.org/10.1080/0950069042000276712)

Multiple external representations: [10.1016/S0360-1315(99)00029-9](https://doi.org/10.1016/s0360-1315(99)00029-9) ·
[10.1016/j.learninstruc.2006.03.001](https://doi.org/10.1016/j.learninstruc.2006.03.001) ·
[10.1002/sce.21128](https://doi.org/10.1002/sce.21128) ·
[10.1187/cbe.19-11-0253](https://doi.org/10.1187/cbe.19-11-0253) ·
[10.1002/sce.20164](https://doi.org/10.1002/sce.20164) ·
[van der Meij & de Jong 2003](https://ris.utwente.nl/ws/files/51155649/VanderMeij2003learning.pdf) ·
[10.1187/cbe.16-06-0193](https://doi.org/10.1187/cbe.16-06-0193) ·
[10.1016/j.edurev.2012.05.003](https://doi.org/10.1016/j.edurev.2012.05.003) ·
[10.1007/s10648-020-09522-4](https://doi.org/10.1007/s10648-020-09522-4) ·
[10.1007/s10648-025-10099-z](https://doi.org/10.1007/s10648-025-10099-z)

Expertise reversal / adaptivity: [10.1016/j.learninstruc.2025.102142](https://doi.org/10.1016/j.learninstruc.2025.102142) ·
[10.1207/S15326985EP3801_4](https://doi.org/10.1207/s15326985ep3801_4) ·
[10.1007/s10648-007-9054-3](https://doi.org/10.1007/s10648-007-9054-3) ·
[10.1007/s10648-016-9359-1](https://doi.org/10.1007/s10648-016-9359-1) ·
[10.1007/BF02504800](https://doi.org/10.1007/bf02504800) ·
[10.1007/s11251-009-9107-8](https://doi.org/10.1007/s11251-009-9107-8) ·
[ERIC EJ880291](https://eric.ed.gov/?id=EJ880291) ·
[10.1037/a0022243](https://doi.org/10.1037/a0022243) ·
[ERIC EJ1078240](https://eric.ed.gov/?id=EJ1078240) ·
[ERIC EJ999802](https://eric.ed.gov/?id=EJ999802) ·
[10.1016/j.chb.2010.05.011](https://doi.org/10.1016/j.chb.2010.05.011) ·
[10.1016/j.learninstruc.2006.02.008](https://doi.org/10.1016/j.learninstruc.2006.02.008) ·
[ERIC EJ1510005](https://eric.ed.gov/?id=EJ1510005)

Threshold concepts: [10.1007/s10734-004-6779-5](https://doi.org/10.1007/s10734-004-6779-5) ·
[10.4324/9780203966273](https://doi.org/10.4324/9780203966273) ·
[10.1080/13562517.2019.1632828](https://doi.org/10.1080/13562517.2019.1632828) ·
[10.1007/s10734-020-00628-w](https://doi.org/10.1007/s10734-020-00628-w) ·
[10.1187/cbe.18-12-0241](https://doi.org/10.1187/cbe.18-12-0241) ·
[10.1080/13562517.2016.1248390](https://doi.org/10.1080/13562517.2016.1248390)

Conceptual change: [10.1002/sce.3730660207](https://doi.org/10.1002/sce.3730660207) ·
[10.1207/s15327809jls1402_1](https://doi.org/10.1207/s15327809jls1402_1) ·
[10.1207/s1532690xci1002&3_2](https://doi.org/10.1207/s1532690xci1002&3_2) ·
[10.1007/978-3-319-72170-5_5](https://doi.org/10.1007/978-3-319-72170-5_5) ·
[10.1016/0010-0285(92)90018-W](https://doi.org/10.1016/0010-0285(92)90018-w) ·
[ERIC EJ538086](https://eric.ed.gov/?id=EJ538086) ·
[ERIC EJ1442536](https://eric.ed.gov/?id=EJ1442536)

Self-explanation / learning by teaching: [10.1207/s15516709cog1803_3](https://doi.org/10.1207/s15516709cog1803_3) ·
[10.1007/s10648-018-9434-x](https://doi.org/10.1007/s10648-018-9434-x) ·
[summit.sfu.ca/item/20986](http://summit.sfu.ca/item/20986) ·
[10.1007/s11858-017-0834-z](https://doi.org/10.1007/s11858-017-0834-z) ·
[10.1007/s10648-025-10001-x](https://doi.org/10.1007/s10648-025-10001-x) ·
[10.1016/j.edurev.2022.100475](https://doi.org/10.1016/j.edurev.2022.100475) ·
[10.1111/j.1756-8765.2008.01005.x](https://doi.org/10.1111/j.1756-8765.2008.01005.x) ·
[ERIC "Feynman technique"](https://eric.ed.gov/?q=%22Feynman+technique%22)

Existing practice as corpus: [10.18653/v1/P19-1346](https://doi.org/10.18653/v1/p19-1346) ·
[arXiv:1907.09190](https://arxiv.org/abs/1907.09190) ·
[Simple English Wikipedia guideline](https://simple.wikipedia.org/wiki/Wikipedia:How_to_write_Simple_English_pages) ·
[10.1371/journal.pone.0231160](https://doi.org/10.1371/journal.pone.0231160) ·
[10.1525/collabra.18898](https://doi.org/10.1525/collabra.18898) ·
[10.1177/09636625241252565](https://doi.org/10.1177/09636625241252565) ·
[10.1016/j.jclinepi.2017.12.003](https://doi.org/10.1016/j.jclinepi.2017.12.003) ·
[10.1371/journal.pone.0268789](https://doi.org/10.1371/journal.pone.0268789) ·
[10.1371/journal.pone.0224697](https://doi.org/10.1371/journal.pone.0224697) ·
[10.1007/s11192-023-04807-1](https://doi.org/10.1007/s11192-023-04807-1) ·
[10.1177/0963662516680311](https://doi.org/10.1177/0963662516680311) ·
[10.3389/fpsyg.2025.1584695](https://doi.org/10.3389/fpsyg.2025.1584695)

Readability / operationalization: [ERIC EJ1151995](https://eric.ed.gov/?id=EJ1151995) ·
[ERIC ED267385](https://eric.ed.gov/?id=ED267385) ·
[ERIC EJ319793](https://eric.ed.gov/?id=EJ319793) ·
[ERIC ED207021](https://eric.ed.gov/?id=ED207021)
