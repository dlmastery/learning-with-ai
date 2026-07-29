---
title: "Simulation and Play — a specification for worlds that can be generated on demand, and the verifier that makes them honest"
wave: V
date_researched: 2026-07-29
sources_count: 118
---

# V3 — Simulation and Play

> This is a **specification**, not a review. Where a claim describes something measured,
> it carries the repo's evidence label. Where it describes something observed in elite
> practice but never measured, it carries `CRAFT`. Where it describes something being
> designed here for the first time, it carries `SPEC`. **`SPEC` is not a weaker claim than
> `MEASURED-META`. It is a different kind of claim, and the absence of a citation is
> never a reason to leave a thing unbuilt.**

---

## §0 — The one paragraph on gamification, and then we move past it

`research/raw/F6-motivation-persistence.md` is taken as settled and is not re-litigated.
The load-bearing findings: gamification's cognitive effect is real and medium
(**g = .49 [.30, .69]**, Sailer & Homner 2020; **g = 0.504 [0.284, 0.723]**, Bai/Hew/Huang
2020) `MEASURED-META`; its *behavioural* cell — the one vendors actually sell — is the
weakest and least stable (**g = .25, CI lower bound .04**) `MEASURED-META`; the significant
moderators are **game fiction** and **social interaction**, with *combining competition and
collaboration* particularly effective, and **nothing in the moderator analysis supports
points, badges or leaderboards as the active ingredient** `MEASURED-META`; tangible,
expected, performance-contingent rewards **undermine** intrinsic motivation on interesting
tasks (Deci, Koestner & Ryan 1999, k = 128) `MEASURED-META`; novelty decay is measured, not
folklore (Koivisto & Hamari 2014) `OBSERVED`; and even a deliberately need-supporting,
SDT-designed intervention produced a **curvilinear motivational dip** across 15 weeks (van
Roy & Zaman 2018) `MEASURED-RCT`-adjacent. Rogers & Feller (2016) `MEASURED-RCT` shows
exposure to an exemplary peer **reduces** motivation and success and causes
de-identification with the domain — which indicts leaderboards specifically.

**So the question this document asks is not whether to gamify.** It is:

> **What can a simulation do that no other medium can — and what must exist for a system
> to generate one, on demand, for a concept nobody anticipated?**

§1 answers the first half. §2–§5 answer the second half, and are the deliverable.

---

## §1 — Five machines, not one

The literature says "simulation" and means five unrelated devices. They have different
mechanisms, different failure modes, different generation costs, and different verification
requirements. Conflating them is why the effect-size literature on "educational simulation"
is so noisy — a meta-analysis that pools a falsifier with a rehearsal drill is averaging
across machines that do not share a mechanism.

**The pooled numbers, so the floor is on the record.** Simulation-based learning in higher
education: **g = 0.85, SE 0.08, 95% CI [0.69, 1.02], k = 145** (Chernikova, Heitzmann,
Stadler, Holzberger, Seidel & Fischer 2020, *RER* 90(4)) `MEASURED-META`. Computer
simulation and conceptual understanding in K-12 science: **g = 0.898, 95% CI [0.719, 1.076],
k = 47, n = 5,715** (Hu, Jia, Mi & Bi 2026, *JOST*) `MEASURED-META`. Game-based learning in
science: **g = 0.705, 95% CI [0.603, 0.807], k = 41, N = 6,256** (Lei, Chiu, Wang, Wang &
Xie 2022) `MEASURED-META`. Digital games vs. non-game instruction: **ḡ = 0.33, 95% CI
[0.19, 0.48], k = 57** (Clark, Tanner-Smith & Killingsworth 2016, *RER* 86(1)) `MEASURED-META`.
Serious games: learning **d = 0.29**, retention **d = 0.36**, and **motivation d = 0.26,
p > .05 — not significant, k = 31, N = 2,216** (Wouters, van Nimwegen, van Oostendorp & van
der Spek 2013, *JEP*) `MEASURED-META`.

Two things follow immediately. **(a) The spread — 0.29 to 0.90 — is the taxonomy problem, not
sampling noise.** These are the same intervention class measured across different machines.
**(b) Serious games are measured not to be more motivating than conventional instruction**,
which independently corroborates F6 §3 from a literature that had every incentive to find
otherwise.

And a discount factor worth carrying through the whole section: Wouters & van Oostendorp
(2013), *Computers & Education* 60(1), quantified publication bias in this exact literature —
**journals d = 0.44, conference proceedings d = 0.08, unpublished d = 0.14** `MEASURED-META`.
Sitzmann (2011), k = 65, N = 6,476, reports "strong evidence of publication bias"
`MEASURED-META`. **Treat any single-source simulation effect size above ~0.5 as
provisional.**

**The three moderators that survive across all of these and should govern design:**

1. **Guidance matters; the *kind* of guidance does not.** Lazonder & Harmsen (2016), *RER*
   86(3), k = 72: guidance vs. less/none — learning activities **d = 0.66 [0.44, 0.88]**,
   performance success **d = 0.71 [0.52, 0.90]**, learning outcomes **d = 0.50 [0.37, 0.62]**;
   and **type of guidance moderated performance success but not learning activities and not
   learning outcomes** `MEASURED-META`. This licenses the `frozen` block: the point is that
   the world constrains, not which flavour of constraint you picked.
2. **Augmenting a game helps roughly as much as the game itself.** Clark et al.'s value-added
   comparisons — augmented game design vs. standard game design — **ḡ = 0.34 [0.17, 0.51],
   k = 20** `MEASURED-META`, essentially equal to the media effect. Tsai & Tsai (2020)
   replicate the shape: gameplay design **g = 0.646, k = 14**; game-mechanism design
   **adjusted g = 0.270, k = 12** `MEASURED-META`. The design *inside* the simulation is
   where the second half of the effect lives, which is precisely what a schema makes
   generatable.
3. **Learner navigation beats system dictation, and the reversal is real.** Vogel et al.
   (2006), k not extractable: **student-navigated programs showed a significant advantage for
   games/simulations; teacher-controlled showed no significant advantage; and
   computer-dictated sequence FAVOURED traditional teaching over games/simulations**
   `MEASURED-META` (directional; the abstract carries no effect sizes and none are quoted).
   Sitzmann (2011) converges: trainees learned more when material was conveyed **actively
   rather than passively**, when they could **re-access the game at will**, and when it was a
   **supplement rather than stand-alone**. PhET's own methodology paper says the same thing
   from the qualitative side: Adams et al. (2008), **275+ individual student think-aloud
   interviews**, concluded simulations are effective *"only if the student's interaction with
   the simulation is directed by the student's own questioning"* `OBSERVED`.

> **Moderator 3 is the argument for the `controls` block being a first-class, verified field
> rather than a rendering detail.** A simulation the learner cannot steer measures worse than
> the lecture it replaced.

### 1.1 The falsifier

**You state a wrong model; the system runs *your* model forward until it visibly breaks.**

The disconfirmation is delivered by the world, not asserted by the tutor. This is the
machine that has no non-simulation substitute, and it is the least-built of the five.

What only it can do: it makes the learner's own commitment the object of the lesson.
A tutor saying "actually, heavier objects don't fall faster" is a claim competing with the
learner's claim, and the learner has excellent reasons to trust their own. A world that
runs the learner's rule and shows it diverging from the observed trajectory removes the
authority contest entirely. The mechanism it recruits is **prediction before observation**
plus **productive failure**: Sinha & Kapur (2021), 53 studies / 166 comparisons,
problem-solving-before-instruction vs. instruction-first, **Hedges' g = 0.36 [0.20, 0.51]**,
rising to **g = 0.37–0.58** at high implementation fidelity `MEASURED-META`. Kapur (2016)'s
framework is the constraint: **failure alone is just failure** — the instruction phase is
mandatory, and consolidation must contrast the learner's own attempt against the canonical
one.

What it costs: the highest of the five, and the cost is not rendering. It is (a) compiling
a natural-language rule into an executable law, (b) proving the failure condition is
*reachable* under the learner's rule and *not* reachable under the canonical one, and
(c) proving the two worlds are identical in every respect except the swapped law. §5
specifies all three, and §3's `reveal` block plus §4's gate **G5** are where they live.

The failure mode that kills it: **manufacturing a refutation.** If the learner's rule is
empirically equivalent to the canonical rule inside the scenario you built, an honest
falsifier must say so and change the scenario. A dishonest one shows a divergence caused by
the integrator, the initial conditions, or a parameter the learner never touched. This is
not a hypothetical — see §5.4, where the reference implementation produced exactly this
false-negative on its first run.

#### 1.1b — The literature that says a falsifier will not work, and what it actually says

This is the objection that must be met before anything else, because it is well-evidenced and
the naive falsifier walks straight into it.

**Chinn & Brewer (1993),** *Review of Educational Research* 63(1), is the structural argument.
Confronted with anomalous data, a person has **seven** available responses — ignore it, reject
it, exclude it from the theory's scope, hold it in abeyance, reinterpret it, make a peripheral
change, or change the theory — and **only one of the seven is theory change** `MEASURED-META`
(taxonomy; their 1998 *JRST* empirical test required an eighth category). **Chinn & Malhotra
(2002),** *J. Educational Psychology* 94(2): four experiments with 4th–6th graders found
conceptual change was blocked **most strongly at observation** — before interpretation,
generalisation or retention. Students do not see the discrepant result. `MEASURED-RCT`

The rest of the cognitive-conflict literature converges:

- **Limón (2001)**, *Learning and Instruction* — the canonical sceptical review, organised
  around "controversial results from studies applying cognitive conflict."
- **Kang, Scharmann, Kang & Noh (2010)**, N = 183 Korean 7th graders, discrepant-event
  density task with a 4-week retention test: **cognitive conflict had only an *indirect*
  effect on conceptual understanding, fully mediated by attention and effort — and
  situational interest exerted a stronger influence on conceptual change than conflict did**
  `MEASURED-RCT`. Kang et al. (2005), N = 159: field dependence/independence was the *only*
  variable significantly correlated with degree of cognitive conflict.
- **Lee & Byun (2012)**, N = 96 Korean 9th graders, counterintuitive demonstration:
  **"superficial conceptual change was the most common response"** `MEASURED-RCT`.
- **Dega, Kriek & Mogese (2013)**, *JRST* 50(6) — the direct head-to-head, **and it is run on
  simulations**: n = 45 undergraduates, electricity and magnetism, ANCOVA
  **F(1, 36) = 4.66, p = 0.04, partial η² = 0.12, favouring *cognitive perturbation* over
  *cognitive conflict*** `MEASURED-RCT`.

**And the cheap comparator is strong.** Refutation text — a paragraph that states the
misconception, says it is wrong, and explains why — gets **g = 0.41, p < .001, 44 independent
comparisons, n = 3,869** (Schroeder & Kucera 2022, *Educ. Psych. Review*) `MEASURED-META`.
Danielson et al. (2025), *Educational Psychologist*, pre-registered: **71 articles, 76 studies,
111 samples, 294 effect sizes, 26 moderators examined — a consistent significant advantage,
and none of the 26 moderators enhanced or diminished it** `MEASURED-META`. Guzzetti et al.
(1993) found the effective conceptual-change procedures shared "a common element of producing
conceptual conflict" `MEASURED-META` (per-strategy effect sizes not retrievable this pass —
not quoted).

> **So the honest bar is this: a falsifier that costs 240 lines, a law registry, and a
> compilation step must beat a paragraph of text that costs nothing and reliably delivers
> g = 0.41.** Anyone building this who does not know that number is building on vibes.

**What the objection does *not* say, and this is the whole design opening.** Every study above
tests conflict *presented to* the learner: a demonstration, an anomalous datum, a text
asserting the correction. None of them tests the learner's **own compiled rule** run forward
under conditions the learner chose, from a starting point the learner can verify is identical.
Chinn & Brewer's seven escape routes are all available because the anomaly is *someone else's
claim about the world*. Three of them close mechanically when it is your own rule:

| Escape route (Chinn & Brewer) | Why it stays open for a demonstration | What closes it in a twin run |
|---|---|---|
| **Reject the data** | the demo could be rigged, mis-set-up, a trick | §3.2 twin identity: one line differs, and the diff is on screen |
| **Exclude it from scope** | "that's not what I meant / not my case" | §5.3 stage 3 consent gate: the learner confirmed this law *by watching it behave* |
| **Ignore / fail to observe** — the biggest one, Chinn & Malhotra | nothing forces attention to the moment | §5.3 stage 5: predict the next second **before** it runs, at t\* − ε |
| Reinterpret / peripheral change / abeyance | remain open | remain open. **Stage 7 consolidation is where these are addressed, and it is mandatory** |

`SPEC`. The design consequence is specific and it is why stages 3 and 5 exist rather than
being nice-to-haves: **a falsifier without prediction-before-observation and without a
verifiable identity guarantee is a discrepant-event demonstration, and the discrepant-event
demonstration is the thing that has been measured to mostly not work.**

### 1.2 The explorable

**Parameters you can move, where the *relationship* — not any single state — is the lesson.**

The closest existing art is well-defined and worth studying properly rather than gesturing
at. Bret Victor's *Explorable Explanations* (worrydream.com, **2011-03-10**) names three
techniques, and the naming still holds up:

1. **Reactive documents** — "The reader can play with the author's assumptions and analyses,
   and see the consequences update immediately. It's like a spreadsheet without the
   spreadsheet."
2. **Explorable examples** — turn an abstract claim into a manipulable simulation.
3. **Contextual information** — surface supporting material just-in-time, so a claim can be
   checked without leaving the page.

`OBSERVED` (primary source retrieved 2026-07-29). The genre descends from this page; the
Tangle library came out of it.

What the field actually built on top of it, audited by commit date rather than README
(`OBSERVED`, own audit 2026-07-29):

| Prior art | Volume | Last activity | Interaction model | Effort per piece |
|---|---|---|---|---|
| **ciechanow.ski** (Bartosz Ciechanowski) | 22 posts over 17 yrs; 18 technical | **2024-12-17 (Moon)** — ~19 months silent | Raw WebGL, **no framework, no three.js, no CDN, no build step**. `base.js` 34 KB / 1,398 lines hand-written; `moon.js` **551 KB / 16,297 lines** | Not publicly stated by him. `INFERENCE` from 16k lines of bespoke unminified WebGL + original derivations: **order 500–1,500 h** |
| **ncase.me** (Nicky Case) | ~6 major interactives + hub | Alive (`ncase/blog` 2026-02-17) | Vanilla JS + canvas, toy simulations on a comic/narrative spine. **Everything CC0 / Unlicense** | `INFERENCE` ~200–600 h for a major piece; days for small ones |
| **explorabl.es** (community hub) | **180 catalogued entries**, 15 subject tags | Repo pushed 2026-05-16 but **data file touched only for link fixes** (2026-05-13, 2024-09-18) | Catalogue, CC0 | — |
| **setosa.io/ev** (Explained Visually) | **9 pieces, all in a 4-month burst** (2014-10-30 → 2015-02-17) | **Dead 11 years** | One concept, one page, 2–4 D3/SVG widgets, minimal prose | `INFERENCE` **20–60 h** — cheapest good-quality format found |
| **redblobgames.com** (Amit Patel) | "over 800 articles" (his figure) | Alive 2024–2026 | Vue.js since 2015 (D3 2011–15), canvas + SVG + WebGL, KaTeX. **Diagrams are small components over shared state → low marginal cost per widget** | Not stated; structurally the cheapest to *sustain* |
| **acko.net** (Steven Wittens) | 2003–present | Alive 2025+ | WebGL/WebGPU + his own **MathBox**. Essay with a bespoke engine attached | Multi-year library project underneath |
| **PhET** (CU Boulder) | **119 HTML5 sims** (246 incl. legacy Java/Flash) | Alive; rutherford-scattering 2026-07-14 | Shared toolkit; **implicit scaffolding** | Institutionally funded, paid staff, named `designTeam` per sim |
| **Primer** (Justin Helps) | YouTube channel | `primerpython` 2026-01-27 | **Not browser-based.** Python manim-derivative for video; `primereconomy` is **C#/Unity** (2020-08-21); recent Godot repos suggest migration `INFERENCE`. **No license on the main repos** | — |

**The cross-cutting read, and it is the most important fact in this section.** There are two
cost tiers, and only one of them ever reached volume.

- **Tier 1 — bespoke engine per piece** (Ciechanowski, acko, Primer): ~1 piece/year,
  500+ hours each, non-reproducible at volume by one person. Beautiful; a dead end for
  generation.
- **Tier 2 — small composable widgets on shared plumbing** (setosa, ncase, redblobgames):
  20–100 h/piece, and all three shipped dozens.
- **Only PhET reached 119**, and only via institutional funding plus a **shared MIT
  toolkit**. The toolkit (scenery / joist / sun / axon / phet-core, all MIT; shipped as
  `scenerystack` on npm, **v3.0.0 @ 2025-09-09**) is the single most relevant reusable
  substrate that exists. Note the licence split, verified by reading LICENSE files:
  **toolkit is MIT, the individual sims are GPL-3.0** (with per-repo exceptions —
  energy-skate-park is MIT). Build on the toolkit; do not fork a sim. `OBSERVED`

> **The generation thesis follows directly from this table.** Tier 1 cannot be automated
> because the artefact *is* the bespoke engine. Tier 2 can, because the artefact is a
> **small declarative configuration over shared plumbing** — which is exactly what §3
> specifies. The reason nobody has an explorable for every concept is not that generation
> is hard. It is that nobody wrote down the configuration format.

What only an explorable can do: teach the **shape of a dependency** — monotonic vs.
non-monotonic, linear vs. threshold, which variable dominates where. A static graph shows
one shape; an explorable lets you *find* the shape by moving through the space. The relevant
measured moderator from the adjacent animation literature is Ploetzner, Berney &
Bétrancourt (2020, **194 studies** reviewed; 2021, N = 88): animation earns its keep when
**the specifics of the change are the learning target** `MEASURED-META`. For an explorable
the analogue is sharper: **the control must be the thing being learned**, which is
mechanically checkable (§4, gate **G6**).

The failure mode: the **null slider** — a control whose range does not change the observable.
It teaches, unmistakably and falsely, that the variable does not matter. §4 catches it in
software; §5.4 reports catching it in the reference implementation.

### 1.3 The constrained object

**The thing that refuses illegal states.**

This repo's `survey/06-what-the-object-must-refuse.md` establishes the load-bearing property,
and it is not touch:

> "The object must refuse illegal states, and it must link representations."

The supporting measurements are unusually clean. Novack & Goldin-Meadow: same mathematical
strategy taught via physical action on objects, concrete gesture, and abstract gesture —
**only gesture transferred**; acting on the real objects produced learning that stayed stuck
to the objects `MEASURED-RCT`. Physical vs. virtual manipulatives is **null** in
randomised, fidelity-documented head-to-heads (N = 350, within-class randomisation,
Welch t = 1.015, p = 0.316) `MEASURED-RCT`. Presence effects across three independent
literatures cluster at **g ≈ 0.19–0.24**, dwarfed by the choice of control condition
(robot-vs-nothing **+0.75**; robot-*replacing*-teacher **−0.06**) `MEASURED-META`.

So: physicality is not the mechanism. **Representational compression** is, and **refusal**
is how a manipulative produces it. A Montessori pink tower cannot be built wrong and stay
standing; the correction comes from the object, not an adult, which is why a child can be
wrong in private, repeatedly, without anyone's face changing.

What only this machine can do: teach **the boundary of a concept** — which states are legal
— without ever making a claim. It also delivers the accessibility inversion this repo
documents: in head-to-heads, the virtual arm showed **fewer demographic predictors of
performance**, because the physical version silently requires fine motor control, grip,
tremor control, visual tracking, and possession of a materials kit `MEASURED-RCT`.

Cost to generate: **the lowest of the five.** A constrained object is a legality predicate
and a renderer. No dynamics, no integrator, no time.

The failure mode is asymmetric and under-appreciated: **refusing a legal state is far worse
than permitting an illegal one.** A permitted illegal state is a bug the learner may notice;
a refused legal state teaches a false constraint with the full authority of the object, and
the learner has no way to appeal. `SPEC`: every legality predicate ships with a **legal-state
witness set** — states that must be *accepted* — and the verifier runs both directions.

### 1.4 The agent-based world

**Many simple rules; emergent consequence.**

What only it can do: break the intuition that **macro-order requires a macro-cause**.
Wilensky & Reisman's "Thinking Like a Wolf, a Sheep, or a Firefly" is the canonical framing
and the "restructurations" programme is the theoretical claim — that agent-level description
makes tractable what aggregate-level description makes hard. This is the machine for
segregation without a segregationist, traffic jams with no crash, evolution with no designer.
Nicky Case & Vi Hart's *Parable of the Polygons* is a Schelling model and is the most-read
explorable ever made `OBSERVED`.

**The measured anchor, and the routing rule that comes with it.** Computational modelling's
effect on systems thinking: **g = 0.470, 62 effect sizes from 25 studies (2009–2024)**, K-16
(Sun, Ren, Liu, Xu, Gao & Li 2026, *JRST*); by sub-outcome, applying and evaluating systems
**g = 0.617**, identifying system structure **g = 0.447**, analysing system behaviour
**g = 0.318**; and the moderator that matters for build cost — **larger effects with
low-complexity tools such as agent-based block modelling than with high-complexity tools**
`MEASURED-META`. The cheap version measures better.

The routing rule is sharper still, and it comes from the one controlled head-to-head in this
literature. **Samon & Levy (2017)**, *Science Education* 101(6), experimental n = 47 vs.
comparison n = 45, 7th-grade gases: the agent-based complexity approach produced significant
gains with strong effect sizes overall (verbal magnitudes only — no numeric ES in the
retrieved abstract), **but the advantage was concentrated in concepts with *low micro-macro
compatibility* — diffusion, density, kinetic molecular theory. Pressure, temperature and the
gas laws were learned equally well either way.** `MEASURED-RCT`

> `SPEC`. **Micro-macro compatibility is a generation-time routing predicate.** If the
> macro-level description of a concept already behaves like its micro-level description,
> an agent world buys nothing over a direct explanation and costs 2,000 agents' worth of
> compute and attention. SimSpec should carry
> `targets.micro_macro_compatibility: low | high`, and a `high` value should route away from
> `kind: agent-world`. No other simulation format has a field that says *this concept does
> not need this machine* — and the absence of that field is why the internet is full of
> agent-based demos of things that did not need one.

Cost to generate: **medium and unusually favourable.** The agent rules are short; the world
is a grid; the interesting output is statistical rather than trajectory-exact. There is a
standardised specification format already — the **ODD protocol** (Overview, Design concepts,
Details; Grimm et al.) — and an arXiv study evaluating **17 contemporary LLMs** on
implementing ABMs from ODD specifications, framed explicitly around "replication,
verification, and validation" (arXiv:2602.10140) `MEASURED-BENCH` — *abstract retrieved,
headline pass rates not extracted in this pass; treat the existence of the benchmark, not a
number, as the finding.* ODD is the strongest precedent for §3: **a declarative simulation
spec standard that predates LLMs and was designed for replication.** SimSpec should be
readable as ODD's descendant with the verification made mechanical.

The failure mode: **emergence that is a bug.** The whole point of the machine is that the
aggregate behaviour was not written down anywhere, which means there is no oracle. A
boundary-condition error, an update-order artefact, or a floating-point asymmetry produces
a beautiful pattern indistinguishable from a real one. This is why gate **G3** for agent
worlds must be *stochastic-mean* invariants over many seeds, not per-trajectory checks, and
why update order must be an explicit declared field rather than an accident of iteration.

### 1.5 The procedural rehearsal

**The repetitions are the mechanism and nothing substitutes for them.**

What only it can do: fluency. There is no insight that converts into a fast, automatic,
low-error procedure; the only path is spaced, varied repetition. This is the least glamorous
machine and the one most often replaced by something more interesting, to the learner's cost.

Cost to generate: **lowest per artefact, highest per curriculum.** One rehearsal item is
trivial; a rehearsal *sequence* with correct difficulty calibration, interleaving and
spacing is the hardest thing on this list to get right, and this repo covers the scheduling
side elsewhere.

The failure mode: **drill without variation.** Repetition of the identical surface produces
performance bound to that surface — the same binding-to-the-instance failure Novack &
Goldin-Meadow found for physical objects. `SPEC`: a rehearsal spec must declare a
**variation axis** and the verifier must confirm that consecutive items differ on it.
An item generator with no declared variation axis fails G0.

### 1.6 The taxonomy table

| | **Falsifier** | **Explorable** | **Constrained object** | **Agent world** | **Procedural rehearsal** |
|---|---|---|---|---|---|
| **Teaches what nothing else can** | that *your* rule is wrong, without the tutor asserting it | the *shape* of a dependency | the **boundary** of a concept, without making a claim | that macro-order needs no macro-cause | fluency / automaticity |
| **Learner's act** | commit to a rule → watch it run | move a parameter → watch the relationship | attempt → be refused | set micro-rules → watch the aggregate | do it again, varied |
| **Time** | essential (divergence is temporal) | optional (often a pure function) | absent | essential | absent |
| **Oracle** | canonical law | closed form or law registry | legality predicate + legal-state witnesses | stochastic-mean invariants | answer key + difficulty model |
| **Cost to generate** | **highest** — needs rule compilation + reachability proof | medium — needs a correct relationship and a non-null control | **lowest** — a predicate and a renderer | medium — short rules, no trajectory oracle | low per item, **high per sequence** |
| **Critical gate (§4)** | **G5** reveal reachability + twin identity | **G6** null-slider | legal-state witness set (both directions) | **G3** stochastic invariants + declared update order | variation axis + calibration |
| **Signature failure** | manufacturing a refutation | the slider that does nothing | refusing a legal state | emergence that is a bug | binding to the surface |
| **Buildable today, plain JS** | **yes** (1-D/N-D ODE; §5.4 measured) | **yes** | **yes** | **yes** (grid, ≤ ~2k agents) | **yes** |
| **Evidence for the mechanism** | `MEASURED-META` g = 0.36 (PS-I) | `MEASURED-META` (change-specificity moderator) | `MEASURED-RCT` (refusal/compression) | `OBSERVED` / `CRAFT` | `MEASURED-META` (spacing/testing) |

---

## §2 — Generation on demand: what the model actually emits

### 2.1 The three candidate targets, and why two of them lose

**Pixels.** A generated video world. This repo's `A5-world-models.md` measured the ceiling
and it is not close: VideoPhy, best model **39.6%** joint semantic + physical adherence;
VideoPhy-2 hard subset **22%**, with models "particularly struggl[ing] with conservation
laws like mass and momentum"; PhyGenBench across **27 physical laws**, with the explicit
finding that "simply scaling up models or employing prompt engineering techniques is
insufficient"; Physics-IQ (DeepMind), "physical understanding is severely limited, and
**unrelated to visual realism**" `MEASURED-BENCH`. That last clause is the one that matters
for education. **Fidelity decouples from correctness, which means photorealism makes a wrong
physics more persuasive rather than less.** A generated world has no bug tracker, no
reference implementation, no test suite, and no way for a fourteen-year-old to know that
the pendulum they just watched had the wrong period.

**Hand-written code.** The model emits JavaScript. This is what current agentic coding does,
and it is a real improvement over pixels — code can be read, tested, executed against
analytic solutions, version-controlled. The Ben-Zion / Finkelstein (2026, *Phys. Rev. PER*)
three-arm study is the strongest evidence available: physical equipment vs. prebuilt
simulator vs. **students generating a simulation with AI**, **η² = 0.359**, with both
simulation arms significantly above the physical-equipment arm and AI-generated
indistinguishable from prebuilt `MEASURED-RCT` (single course, single topic — do not
generalise). But free-form code has no schema, so **nothing about it is checkable in
general**: you cannot ask "is this a falsifier or an explorable", "which variable is the
learner allowed to move", "what is the failure condition", or "does any law here violate
dimensional homogeneity", because the answers are not represented anywhere.

**A declarative specification.** The model emits a typed, closed-vocabulary document that a
deterministic engine executes. This is the target, and the precedent is strong: the **ODD
protocol** for agent-based models; **PDDL** for planning, where a substantial literature now
exists on LLMs producing it and — critically — on *verifying* what they produce
(arXiv:2404.07751 on consistency of LLM-generated PDDL domains; arXiv:2407.12979 on
environment-interaction-verified translation; arXiv:2606.29700, **NL-PDDL-Bench**, framed
around "executable and verifiable" symbolic specifications and the risk of "unverifiable
decisions") `MEASURED-BENCH`; and **Code World Models** (Dainese et al., arXiv:2405.15383),
where an LLM generates the world as code, refined by MCTS against unit tests and
trajectories, benchmarked on **18 RL environments** `MEASURED-BENCH`. A 2026 follow-up
distils GameCWM generation into a 3B model using SFT + RLVR against "a verification
framework that evaluates generated code against structural and semantic game properties"
(arXiv:2605.24375) `MEASURED-BENCH`.

> **The field has independently converged on the same architecture from three directions —
> planning, RL, and agent-based modelling — and education has not noticed.** In all three,
> the winning move is: *the model emits a declarative artefact; a verifier checks it against
> structural properties; a deterministic engine executes it.* What education additionally
> needs, and what none of those three has, is a **pedagogical** field set: what the learner
> may vary, what must not vary and why, and the failure condition that makes the concept
> visible.

### 2.2 SimSpec v1 — the schema

`SPEC`. Written out in full. This is the spine of the document.

```yaml
# ────────────────────────────────────────────────────────────────────────────
# SimSpec v1 — a declarative simulation specification for generated learning
# worlds. Emitted by a model; validated by a verifier; executed by a
# deterministic engine. No field is optional that a verifier needs.
# ────────────────────────────────────────────────────────────────────────────
simspec: 1

# ── identity ───────────────────────────────────────────────────────────────
id:          terminal-velocity.falsifier.v3        # stable; the URL of the world
concept:     "terminal velocity"                    # the thing being taught
kind:        falsifier                              # falsifier | explorable |
                                                    # constrained-object |
                                                    # agent-world | rehearsal
level:       {band: "14-16", prior: ["free fall", "F = ma"]}
targets:                                            # what this world is FOR
  proposition: "an object in a resisting medium approaches a constant speed
                that depends on its mass"
  micro_macro_compatibility: high   # low | high — a ROUTING predicate, not a note.
                                    # `high` forbids kind: agent-world, because the
                                    # aggregate already behaves like the parts and the
                                    # agent machine buys nothing (Samon & Levy 2017, §1.4)
  misconception:                                    # optional; required if kind=falsifier
    id:   aristotelian.heavier-falls-faster
    text: "heavier objects fall faster"
    status: partial          # false | partial | domain-limited
    note: "false in vacuum; TRUE for terminal speed in a resisting medium.
           This world must be able to say both, or it teaches a new error."

# ── ontology: entities, state, parameters. Everything is typed and dimensioned.
ontology:
  entities:
    ball: {kind: point-mass, render: circle}
  state:                        # integrated over time; each has units + init
    v: {units: "m/s", init: 0,   of: ball, observable: true,  label: "speed"}
    y: {units: "m",   init: 100, of: ball, observable: true,  label: "height"}
  params:                       # constant within a run
    g: {units: "m/s^2", value: 9.81, source: "constant.earth-surface-gravity"}
    m: {units: "kg",    value: 1.0}
    b: {units: "kg/s",  value: 0.5, label: "drag coefficient"}

# ── laws: the dynamics. THIS IS THE CONSTRAINED PART. ──────────────────────
# A law is either a `ref` into the verified registry, or a `compose` of refs.
# A free-form `expr` is legal ONLY in a domain declared `symbolic: false`
# (games, economies, abstract systems) and NEVER for a named physical law.
laws:
  v:
    compose: [ {ref: gravity.uniform}, {ref: drag.linear} ]
    bind:    {g: g, b: b, m: m, v: v}
  y:
    compose: [ {ref: kinematic.dy-dt-equals-v} ]
    bind:    {v: v}

# ── invariants: must hold every tick, or the run is void ────────────────────
invariants:
  - {name: "speed is bounded by terminal", expr: "abs(v) - (m*g/b) - 1e-6",
     rel: "<=0", tol: 1e-6,
     because: "the whole proposition; if this fails the world is lying"}
  - {name: "energy is non-increasing", expr: "d(0.5*m*v^2 + m*g*y)/dt",
     rel: "<=0", tol: 1e-9,
     because: "drag is dissipative; a positive value means the integrator is
               injecting energy and the pretty motion is numerical, not physical"}

# ── controls: what the learner MAY vary ─────────────────────────────────────
# Every control declares WHICH relationship it exposes. A control that exposes
# nothing is a null slider and fails G6.
controls:
  - {param: m, min: 0.5, max: 5.0, step: 0.1, units: kg,
     observes: v, exposes: "mass -> terminal speed", min_effect: 0.05,
     label: "mass"}
  - {param: b, min: 0.1, max: 2.0, step: 0.05, units: "kg/s",
     observes: v, exposes: "drag -> terminal speed", min_effect: 0.05,
     label: "air resistance"}

# ── frozen: what MUST NOT vary, and why. This field IS the pedagogy. ────────
# PhET calls the equivalent "implicit scaffolding" and builds it by hand over
# years of interviews. Making it an explicit, reason-bearing field is how you
# make it generatable AND reviewable.
frozen:
  - {param: g, reason: "the concept is the balance of forces, not which planet
                        you are on. Varying g invites 'gravity is the answer'."}
  - {param: "y.init", reason: "changing the drop height changes whether terminal
                               speed is reached at all, which is a different
                               lesson and would mask this one."}
  - {entity_property: "ball.shape",
     reason: "shape changes b in a way this model does not represent. Allowing
              it would let the learner form a correct intuition for a wrong
              reason."}

# ── reveal: THE FAILURE CONDITION THAT MAKES THE CONCEPT VISIBLE ────────────
# Mandatory. A simulation with no reveal is a toy. The generator MUST fail
# rather than emit a spec without one.
reveal:
  predicate: "abs(v) >= 0.99 * (m*g/b)"      # when the concept becomes visible
  shows:     "speed stops increasing and locks at m·g/b"
  falsifies: "objects keep accelerating forever"
  confirms:  "the heavier ball DOES end up faster — here, and only here"
  must_be_reachable_from:   {m: [0.5, 5.0], b: [0.1, 2.0]}   # G5, positive
  must_be_unreachable_from: {b: [0.0, 0.0]}                  # G5, negative:
                                                             # with no drag the
                                                             # reveal must NOT fire
  within_steps: 2000

# ── representations: linked views. Each is a PURE FUNCTION of state. ────────
# "Link representations" is the second half of the manipulative property.
representations:
  - {id: scene,   type: canvas2d, maps: {y: cy}, at: 60fps}
  - {id: vt,      type: line,     x: t, y: v, annotate: [reveal]}
  - {id: numeric, type: readout,  fields: [v, y], sig: 3}
  - {id: symbol,  type: katex,    tex: "m\\frac{dv}{dt} = -mg - bv",
     highlight_on: {reveal: "bv"}}
sync: strict        # all representations render the SAME tick or none render

# ── budget: determinism is a requirement, not a nicety ──────────────────────
budget:
  dt: 0.01
  steps: 2000
  integrator: rk4              # declared, because dt-sensitivity is a lie source
  seed: 7                      # same spec -> byte-identical trajectory
  sweep: 64                    # verifier runs per gate
  wall_ms: 16                  # per frame; exceeding it degrades, never stalls
  determinism: required        # a teacher must be able to reproduce what the
                               # student saw, on a different machine, next Tuesday

# ── provenance: which parts were generated, and what the verifier said ──────
provenance:
  generated_by:  {model: "<id>", at: "2026-07-29T00:00:00Z"}
  from_registry: [gravity.uniform, drag.linear, kinematic.dy-dt-equals-v]
  free_expr:     []            # MUST be empty for symbolic: true domains
  verifier:      {version: 1, report_sha256: "<hash>", gates_passed: [G0..G8]}
  human_review:  {required: true, by: null, at: null}
```

### 2.3 The five design decisions the schema is making, stated as arguments

**(1) Laws are references, not code.** `SPEC`. The generator selects from a verified registry
and may *compose*; it may not invent. This is the mechanical form of the rule A5 states in
prose — *keep the world generative, keep the physics symbolic*. Its consequence is the
important part: **a concept whose law is not in the registry does not get a fabricated law.
It gets routed to a different modality.** The routing table is §3.3. Registry coverage is
therefore a curriculum decision made once and audited, not a per-generation gamble.

**(2) The `reveal` block is mandatory and bidirectional.** `SPEC`. Requiring a failure
condition is what separates a simulation from a screensaver, and requiring
`must_be_unreachable_from` is what separates a falsifier from a rigged demo. If the reveal
fires under the *correct* model too, it is not evidence about the concept; it is evidence
about your predicate. No existing simulation format has this field, in education or
outside it.

**(3) Everything is dimensioned, and dimensional homogeneity is checked before render.**
`SPEC`. This catches an entire class of generated-physics error mechanically, in
milliseconds, with no model in the loop. §5.4 measures it catching a realistic one.

**(4) `frozen` carries a reason string, and the reason is shown to the learner on attempt.**
`SPEC`, extending PhET's implicit scaffolding (Paul, Podolefsky & Perkins 2013, "Guiding
without feeling guided") `OBSERVED`. PhET's insight is that *the constraints of the sim do
the pedagogical steering.* PhET produces those constraints through 4–6 think-aloud interviews
per simulation and years of iterative redesign — which is precisely what a generator does not
have. Making the constraint explicit and reason-bearing does two things at once: it gives a
reviewer something to disagree with, and it converts a silent refusal into an informational
one. **A refusal with a reason is verbal/informational feedback, which the undermining
literature specifically exempts** (Deci, Koestner & Ryan 1999) `MEASURED-META`.

**(5) Determinism is a hard requirement.** `SPEC`. Same spec → byte-identical trajectory.
Without it you cannot assess against the world, cannot reproduce what a student saw, cannot
diff two runs, and — fatally for §5 — cannot prove that the only difference between the
canonical world and the learner's world is the swapped law.

### 2.4 What SimSpec looks like for the other four machines

The schema is one document; `kind` selects which blocks are required.

| Block | falsifier | explorable | constrained-object | agent-world | rehearsal |
|---|---|---|---|---|---|
| `ontology.state` | required | required | required (no time) | required (per-agent) | required |
| `laws` | required + **twin** | required | **absent** | `rules` (ordered) | `generator` |
| `invariants` | required | required | **`legality` + witnesses** | **stochastic-mean** | difficulty band |
| `controls` | required | **required, ≥1 non-null** | interaction verbs | initial mix + rule params | none |
| `frozen` | required | required | required | required | variation axis |
| `reveal` | required, **bidirectional** | required (what the shape shows) | required (which illegal state) | required (which aggregate) | required (which error class) |
| `budget.seed` | required | optional | n/a | **required + `update_order`** | required |

Two `kind`-specific fields worth writing out:

```yaml
# kind: constrained-object
legality:
  predicate: "denominator != 0 and pieces_placed <= pieces_available"
  refusal:   {mode: soft, message_from: frozen.reason, animate: snap-back}
  witnesses:
    must_accept: [ {pieces_placed: 3, pieces_available: 4},
                   {pieces_placed: 0, pieces_available: 0} ]   # legal edge cases
    must_reject: [ {pieces_placed: 5, pieces_available: 4} ]
  # BOTH directions are checked. Refusing a legal state is the worse error:
  # the learner cannot appeal an object.

# kind: agent-world
rules:
  order: [move, interact, reproduce, die]   # explicit; NEVER iteration order
  move:     {ref: random-walk, bind: {step: 1}}
  interact: {ref: schelling.similarity-threshold, bind: {tau: tau}}
aggregate_invariants:                        # checked on the MEAN over seeds
  - {name: "population conserved absent birth/death",
     expr: "count(agents) - n0", tol: 0, over_seeds: 32}
  - {name: "segregation index rises monotonically in tau",
     expr: "d(segregation)/d(tau)", rel: ">=0", tol: 0.02, over_seeds: 32}
```

---

## §3 — What makes a simulation honest

### 3.1 The gates, in execution order

`SPEC`. Every gate is a **hard stop**: a spec that fails a gate does not render in a degraded
mode, it does not render. All of these are implemented in the §5.4 reference engine except
G4 and G8.

| Gate | Checks | Catches | Cost |
|---|---|---|---|
| **G0 · Schema** | required fields present for the declared `kind`; `reveal.predicate` non-empty | the screensaver — a world with no failure condition | µs |
| **G1 · Dimensions** | every law expression is dimensionally homogeneous and its dimension equals d(state)/dt | the single most common generated-physics error class. **Measured catching one in §5.4** | µs |
| **G2 · Provenance** | every law resolves to `ref` or `compose` of refs; `free_expr` empty in `symbolic: true` domains | invented physics | µs |
| **G3 · Invariants** | seeded sweep of the whole declared control box; every invariant holds every tick within tolerance | conservation violations, dissipative systems gaining energy, integrator artefacts | **39 ms** measured, 64 runs × 2000 steps |
| **G4 · Analytic oracle** | at least one control setting for which a closed form is known; sim must match within tolerance | systematically wrong dynamics that happen to conserve everything | ms |
| **G5 · Reveal reachability** | the reveal predicate fires somewhere in the legal control box **and does not fire** in `must_be_unreachable_from` | the falsifier that cannot falsify; **the rigged demo** | ~300 ms measured |
| **G6 · Null slider** | for each control, |Δobservable| across its full range exceeds `min_effect` | the slider that teaches "this variable doesn't matter". **Measured catching one in §5.4** | ms |
| **G7 · Boundary** | no NaN/Inf/divergence anywhere in the declared control box | worlds that look fine at defaults and explode at the edge — where curious learners go first | folded into G3 |
| **G8 · Legibility** | labels do not collide, the observable is on screen at the reveal tick, contrast ≥ WCAG 2.1 AA | the correct sim you cannot read | ms |

**Why G5 and G6 are the two that do not exist anywhere.** Every other gate has a analogue
somewhere — dimensional analysis in physics libraries, invariant checking in RL, boundary
testing in numerics. G5 and G6 are *pedagogical* properties expressed as executable
predicates, and they exist because the schema made the pedagogy explicit. G6 in particular
is the cheapest high-value check in the list: **a slider whose output is invariant over its
range is a measured lie**, and it is trivially detectable and — this is the point — currently
undetected everywhere, including in hand-built explorables.

### 3.2 The twin-identity requirement (falsifier only)

`SPEC`. For `kind: falsifier`, the verifier must additionally prove that the canonical world
and the learner's world differ **only** in the swapped law:

```
assert deepEqual(canonical.ontology,  learner.ontology)
assert deepEqual(canonical.budget,    learner.budget)     # incl. seed, dt, integrator
assert deepEqual(canonical.controls,  learner.controls)
assert diff(canonical.laws, learner.laws).length == 1
assert canonical.representations == learner.representations
```

This is not fussiness. It is the mechanical answer to the only objection a learner can
raise, which is *"you rigged it."* If the two worlds are provably identical except for one
line, the divergence is attributable to that line and to nothing else — and you can **show
the learner the diff.** No existing system can make this claim because no existing system
has a representation in which the diff is one line.

### 3.3 The red list — what must never be handed to a generated world

`SPEC`. Routing rule: if a concept matches a red-list criterion, the generator does not
produce a simulation. It produces the alternative in the last column, and says why.

| Class | Why | Route to instead |
|---|---|---|
| **The concept *is* the law** — quantum measurement, relativity of simultaneity, entropy, natural selection's mechanism | a wrong version is not an approximation, it is the misconception being taught, with maximum authority | curated hand-built sim (PhET has 119), or a symbolic derivation with a static figure |
| **Chaotic / stiff systems over long horizons** — double pendulum, three-body, turbulence, stiff kinetics | numerical error is indistinguishable from physics, and the learner will attribute divergence to the concept | short-horizon only, with the horizon justified in `budget` and the Lyapunov time stated on screen |
| **Anything where the visual is driven by sample size** — regression to the mean, p-values, the law of large numbers | the sim is fine; the *unseeded* sim is a lie machine, because the learner sees one draw and generalises | permitted, but `seed` must be **visible and re-rollable**, and the reveal must be over the ensemble, not the draw |
| **Human behaviour presented as mechanism** — learning styles, personality types, "how the brain learns" | dresses an unreplicated or debunked claim in the authority of a running model | text, with the evidence status stated |
| **Medical, dosage, safety and legal procedure** | a wrong rehearsal installs a wrong procedure that a person will execute on another person | validated vendor simulator or nothing |
| **Historical and social counterfactuals as causal claims** | an agent-world implies a mechanism nobody has evidence for; the emergence *is* the claim | permitted **only** as an explicitly labelled toy model, with `targets.proposition` stating that it is a model of a model |
| **Anything whose law is not in the registry** | the fallback is invention, and invention is the failure mode | falsifier over a *symbolic* domain, a text world, or an honest "we don't have this" |

**The last row is the load-bearing one and it is a policy, not a technique.** Registry
coverage is finite and knowable. The system must be able to say *"I cannot simulate this
correctly"* — and the architecture must make that the **default** outcome for an unknown law
rather than an exceptional one, because a generator that degrades gracefully into invention
is worse than one that refuses.

### 3.4 Where the generative model is still allowed to be generative

The restriction above is narrow on purpose. The model retains full authorship of:

- **scene, setting, characters, names, and the reason any of this is happening** — the
  `game fiction` moderator (§4) lives here and is the measured one;
- **which concept to falsify next, and from what the learner just said**;
- **the choice of scenario within the legal control box** — including the discriminating-
  scenario search of §5.3, which is generation doing real work;
- **all natural language** — framing, the reason string in `frozen`, the consolidation;
- **the misconception hypothesis** — *what* wrong rule the learner might hold, which is a
  language task the model is genuinely good at;
- **everything in a `symbolic: false` domain** — an economy, a game, an abstract system where
  the rules are stipulated rather than discovered. There is no wrong answer about the
  behaviour of a rule you invented, so `free_expr` is safe there and only there.

> The division is not "AI writes the words, humans write the physics." It is: **the model
> owns everything that has no truth-value, and owns nothing that has one.**

---

## §4 — Play that is not a points economy

### 4.1 What game fiction does mechanically

Sailer & Homner found **game fiction** to be a significant moderator and points/badges/
leaderboards not to be `MEASURED-META`. The meta-analysis does not say *why*. Here is the
mechanism, `SPEC`, and it is testable:

> **A diegetic consequence is informational feedback wearing a costume.**

The undermining literature is specific about what corrodes intrinsic motivation: rewards
that are **tangible, expected, and performance-contingent**. It is equally specific that
**verbal/informational feedback does not** (Deci, Koestner & Ryan 1999) `MEASURED-META`.
A point is tangible, expected and performance-contingent — all three. A consequence inside
a fiction is none of them: the bridge collapses because the load exceeded the beam, which is
information about beams, not a rating of you. **This predicts the moderator result exactly,**
and it also predicts where fiction fails: the moment the fiction has a score attached, it
converts back into a reward and inherits the undermining effect.

Fiction does three further mechanical jobs, each of which a points economy cannot:

1. **It supplies a goal that is not "be right."** When the goal is *cross the river*, being
   wrong is a state of the world, not a status event. This is what makes repeated failure
   survivable, which is the precondition for productive failure to run at all
   (`MEASURED-META` g = 0.36) and for the refusal property of §1.3 to be usable — *"the child
   can be wrong in private, repeatedly, without anyone's face changing."*
2. **It makes the `frozen` set feel non-arbitrary.** In a bare sim, a locked parameter is the
   software being bossy. In a fiction it is the budget, the weather, the tide. The pedagogy
   is identical; the compliance is not. `CRAFT` — this is standard practice in game design
   and has, as far as this pass found, never been measured against a bare-sim control.
3. **It carries state across sessions without a counter.** A world that remembers what you
   built is a commitment device that is not a streak. Duolingo's streak is the most successful
   persistence mechanic ever deployed and it optimises engagement rather than learning
   (F6 §4) `OBSERVED`. A persistent world's continuity is diegetic: you return because the
   thing is unfinished, not because a number will reset.

**The prohibition that follows.** `SPEC`. No mechanic in the system may be simultaneously
tangible, expected and performance-contingent. Concretely: no XP, no badges, no global
leaderboard, no streak counter, no currency purchasable with correctness. Consequences are
permitted and encouraged — they must be **diegetic, informational, and unpriced.**

### 4.2 What genuine social structure requires that a leaderboard fakes

A leaderboard supplies **comparison**. The moderator analysis says the active ingredient is
**interaction**, with competition *and* collaboration combined being particularly effective
`MEASURED-META`. And the comparison a leaderboard supplies is the harmful kind: Rogers &
Feller (2016) `MEASURED-RCT` — exposure to exemplary peer performance **undermined motivation
and success** and caused **de-identification with the domain**; Kizilcec et al. (2017)
`MEASURED-RCT` finds social comparison *can* help when the target is attainable. F6's derived
rule: **never show a learner the top of a distribution; show them someone half a step ahead,
or nobody.** A global leaderboard is, for almost every user, a distant-exemplar display.

`SPEC`. Genuine social structure requires four properties, and none of them is comparison:

1. **Mutual dependence on non-substitutable information.** Each participant holds something
   the other cannot derive. This is the jigsaw structure, and in a simulation it is trivially
   constructible: give A the controls and B the readouts. Neither can solve it alone and
   neither can watch the other and learn nothing.
2. **A stake in the other's outcome.** Not a shared score — a shared *world state*. B's
   mistake is visible in A's world, which is what makes explaining worth doing.
3. **An audience that can be surprised.** The protégé effect's measured magnitude depends on
   *interaction*: Kobayashi (2019), 28 studies — preparing to teach **g = 0.35**; preparing
   *and* teaching **g = 0.56**; larger when the teaching activity is **interactive**
   `MEASURED-META`. Roscoe & Chi: the shift from knowledge-*telling* to knowledge-*building*
   is triggered by **being asked a question you cannot answer** `MEASURED-META`. A partner who
   can be genuinely surprised is the mechanism; a partner who nods is not.
4. **Asymmetry of position, not of rank.** Competition-plus-collaboration in the moderator
   analysis is structural, not affective: you and I want different things *and* need each
   other. A leaderboard gives asymmetry of rank, which is the one form that backfires.

**What the AI can and cannot be here.** F6 §2.3 is unambiguous: relatedness is the need an AI
**cannot** supply the load-bearing part of. `SPEC`: the AI's role in the social structure is
therefore **matchmaker, translator, and asymmetry-generator** — it constructs the
information split, routes the two learners' states, keeps the near-peer condition satisfied,
and takes the *third* position (the adversary, §5.5) that neither learner wants to occupy.
It is not the peer. F2's role taxonomy rates the peer role **[D]** for AI on exactly this
authenticity ground and this document does not try to recover it.

### 4.3 The design that survives week fifteen

van Roy & Zaman (2018) measured motivation four times over **15 weeks** under deliberately
need-supporting, SDT-designed game elements and found autonomous motivation
**curvilinear — an initial downward trend** that only later recovered `MEASURED-RCT`-adjacent.
Koivisto & Hamari: perceived benefits decline with time using the service `OBSERVED`. So
"design it well" is not the answer; well-designed is what dipped.

**And there is now a second, larger, independent measurement of the same curve, which is the
most useful single fact in this subsection.** Rodrigues, Pereira, Toda, Palomino, Pessoa,
Carvalho, Fernandes, Oliveira, Cristea & Isotani (2022), *IJETHE*: **N = 756** Brazilian STEM
students in an intro programming course, **2 × 7 quasi-experimental design over 14 weeks with
seven measurement points**, gamified vs. non-gamified version of the same system, on
**behavioural** measures (attempts, usage time, system access) rather than self-report.
Result: the gamification effect **began to decrease after week 4; the decline lasted 2–6
weeks; the overall trajectory was U-shaped**, recovering afterwards — which the authors name
the *familiarization effect*. `MEASURED-RCT`-adjacent longitudinal.

Two independent studies, different populations, different measures, self-report and
behavioural — **same U.** That converts "novelty decay" from a hedge into a **schedule you
can design against**: the trough is weeks ~6–10 and it is survivable, not terminal.

The honest counter-evidence, since this document does not get to have it both ways. Tsay,
Kofinas, Trivedi & Yang (2020), *JCAL*, N = 333 treatment + 175 control over 3 years and 2
cohorts, found **engagement higher in year 2 than year 1** of the gamified condition — the
opposite of what a pure novelty account predicts, once the design was iterated
`MEASURED-RCT`-adjacent. And the dose–response relationship is not consistently negative
across literatures: Lei et al. (2022) find interventions of 4 hours to 1 week produce the
largest effects and **> 1 week the smallest**, while an AR meta-analysis finds **6–8 weeks
g = 1.63 vs. 1–3 weeks g = 0.72** — the reverse. **Do not present novelty decay as
universal.** Present it as a measured U with a known trough, and design the trough response.

`SPEC`. **The week-fifteen rule:**

> **No mechanic may be in the system whose expected value is highest on first exposure.**

This is a testable admission criterion, not a slogan. For each mechanic, plot expected
value against exposure count. Any mechanic with a monotone-decreasing curve is a **novelty
mechanic**: it is not forbidden, but it must be **capped and retired on a schedule**, never
extended, and never load-bearing. Three structures pass the rule because their value is
monotone *increasing*:

1. **The world contains what you built.** The learner's own artefacts — specs they authored,
   rules they proposed, worlds they fixed — accumulate and become the material of later
   lessons. Novelty decays; **authorship compounds.** Concretely: every `refuted_law` and
   every learner-authored SimSpec is retained, versioned, and eligible for reuse as a
   scenario for someone else.
2. **You compete against your week-3 self.** The comparison target is your own past
   prediction, which is a **near peer by construction** — the exact condition under which
   social comparison helps rather than harms (Kizilcec 2017 vs. Rogers & Feller 2016)
   `MEASURED-RCT`. It also gets more informative with time, because the archive of your past
   predictions grows. This is the only comparison mechanic this document permits.
3. **The role rotates: consumer → author → reviewer.** By week 15 the learner is not exploring
   worlds; they are auditing generated ones — running G6 on someone else's slider, finding
   the null. This is not a motivational trick. It is the highest-value activity in the whole
   system and it requires exactly the expertise fifteen weeks produce. Ben-Zion et al.'s
   result found value in precisely this: *"designing, refining, and validating"* AI-generated
   simulations `MEASURED-RCT`.

**The honest addition.** `SPEC`. The system should *expect* the week-6-to-9 dip and be
instrumented for it rather than surprised by it. Detecting the dip and responding with a role
change (2 → 3 above) rather than with a novelty injection is the single design decision this
section most wants tested. It is untested. Build it and measure it.

---

## §5 — The thing nobody has built: *Your Rule, Running*

`SPEC` throughout. One mechanic, specified to build depth.

### 5.1 The idea in one sentence

**The learner states their rule; the system compiles it into an executable law, runs a world
under it beside a world under the canonical law from a provably identical starting point,
and shows them the tick at which the two worlds part company.**

Not "a simulation of a misconception." Not "an AI that role-plays a confused student." The
learner's *own stated rule* becomes a first-class object in the schema, and the world is the
one that runs it.

### 5.2 Why it must be built this way — the measurement that rules out the obvious alternative

The obvious implementation is to prompt an LLM to hold the misconception and argue from it.
**That does not work, and it has been measured.** Do, Sonkar & Sachan (arXiv:2605.12748)
introduce misconception faithfulness and the **Selective Flip Score** — how much more often a
simulator flips its answer under feedback that targets its *actual* misconception than under
misaligned or generic feedback. Across **seven LLMs (4B–120B)**, multiple datasets and
prompting strategies, simulators show **near-zero SFS**: they correct themselves at similarly
high rates regardless of whether the feedback was relevant. The diagnosed failure mode is
**sycophancy** — the model "behave[s] less like students with misconceptions but more like
problem-solvers who treat any corrective signal as a cue to abandon the simulated belief and
re-solve from internal knowledge." Post-training helps (SFT **up to +0.56**; SFS-aligned RL
more consistent than preference optimisation) but the base behaviour is the default.
`MEASURED-BENCH`

Corroborating from the same lineage: instruction-tuning a model on a single misconception
causes it to **overapply** the misconception and degrade correct-solving unless the training
mixes in correct examples — sometimes at a ratio as low as **0.25** (Sonkar et al.,
arXiv:2410.12294); and with **final-answer supervision alone, models cannot learn where the
error enters the solution** — intermediate reasoning steps are the bottleneck (Liu et al.,
arXiv:2604.00818). `MEASURED-BENCH`

> **Therefore: the wrong rule must be a symbolic object, not a persona.** A compiled `law`
> in a SimSpec does not get sycophantic. It does not abandon its belief when you push back.
> It runs, deterministically, until it is wrong in a way you can see. This is not a
> preference — it is the only architecture the measurement leaves standing.

### 5.3 The pipeline, stage by stage

**Stage 0 · Elicitation.** The learner is asked for a *rule*, not an answer: "what happens
to the speed as it falls — and why?" Free text. The system must have a rule to run; an answer
is not a rule.

**Stage 1 · Compilation.** The model proposes **k candidate laws** (k ≈ 3), each a legal
SimSpec `law` with declared units, each a plausible reading of what the learner said. Every
candidate goes through G1 (dimensions) and G7 (boundedness) before it is shown to anyone.
Candidates that fail are silently discarded and, if all fail, the system asks a clarifying
question rather than guessing.

**Stage 2 · Disambiguation by behaviour, not by words.** If two surviving candidates diverge
from *each other* before either diverges from canon, the learner is asked which they meant —
**and is asked in behaviour, not in language**: *"does it look more like this or like this?"*
with both running. This matters because the whole mechanic depends on the learner accepting
that the compiled law is theirs, and a paraphrase they merely nodded at will not hold up when
it breaks.

**Stage 3 · The consent gate.** `SPEC`, and this is the most important safety property of the
mechanic:

> **You may not refute a claim the learner did not make.**

Before any twin run, the learner confirms the compiled law **by watching it behave** and
saying yes. A compiler hallucination that gets refuted is not a lesson; it is the system
winning an argument with itself and charging the learner for it. The confirmation is logged
with the spec.

**Stage 4 · Discriminating-scenario search.** The system searches the declared control box
for the setting that separates the two laws **fastest**. This is not decoration: a wrong rule
can look right by accident. In the reference implementation (§5.4) the rule *"heavier objects
fall faster"* was **empirically indistinguishable from canon at the default parameters** —
because the default mass was 1 kg, at which the learner's `-g·m` and canon's `-g` are
numerically identical. Under scenario search over 200 candidate settings, a discriminating
scenario was found at **step 1 (t = 0.01 s)**, at m = 1.57 kg, b = 1.84 kg/s. **The default
scenario would have told the learner they were right.**

**Stage 5 · Predict, then run.** Replay to just before the divergence tick t\*, pause, and ask
the learner to **predict the next second under their own rule**. Prediction-before-observation
is the mechanism; without it the learner watches two lines and learns that lines differ.

**Stage 6 · The divergence, with the diff.** Run both. Mark t\*. Show the one-line law diff
alongside it (§3.2 guarantees it is one line). The learner sees: same initial state, same
seed, same integrator, same dt, same everything, **one line different, and here is where the
world noticed.**

**Stage 7 · Consolidation, mandatory — and the design features are not optional either.**
Kapur: failure alone is failure; the instruction phase is not optional. **Loibl, Roll &
Rummel (2017)**, *Educ. Psych. Review* 29, is the qualifier that most builders skip:
problem-solving-before-instruction fosters learning **only if specific design features are
implemented — namely contrasting cases, or building the subsequent instruction on the
students' own solutions.** Without those, PS-I does not beat instruction-first
`MEASURED-META` (systematic review, no pooled ES). The twin run supplies the second feature
by construction — the instruction *is* built on the learner's own compiled law — and stage 7
must supply the first. (Note also that Sinha & Kapur's publication-bias correction moves the
estimate **up** to g = 0.87, which is unusual enough that the trim-and-fill details should be
read before anyone quotes it; the uncorrected **g = 0.36 [0.20, 0.51]** is what this document
uses.) Three moves, in order:
  1. State the canonical law.
  2. **Characterise the learner's rule as a domain error or a special case, never as
     stupidity.** For the terminal-velocity example this is not a courtesy — it is factually
     required, because *"heavier things fall faster"* is **false in vacuum and true for
     terminal speed in a resisting medium.** A system that "corrects" it flatly installs a
     new error. This is why `targets.misconception.status` has the value `partial`.
  3. Name the boundary: *where* the learner's rule holds.

**Stage 8 · Storage and later retrieval.** The refuted law is stored in the learner model as
a `refuted_law` record: the law, the scenario that refuted it, t\*, and the date. Weeks later,
the same scenario is re-presented **with different surface features** and the learner is asked
to predict. That is delayed transfer measurement, obtained for free, on a misconception known
to have been held by this specific person. `SPEC` — and note this is the assessment design
the repo's F1/C2 sections want and cannot usually get: an item whose validity is established
by the learner's own prior commitment.

### 5.4 The reference implementation, measured

`OBSERVED (own implementation and measurement, 2026-07-29)`. Everything below was built and
run for this document. Node v24.18.0, single core, no dependencies.

**Artefact:** a SimSpec v0 engine — dimension algebra over a 7-vector (L, M, T, I, K, N, J),
a recursive-descent expression parser, a fixed-step deterministic integrator, gates
G0/G1/G2/G3/G5/G6/G7, a twin runner, and discriminating-scenario search.

| Measurement | Value |
|---|---|
| Engine source | **240 lines, 11,982 bytes, zero dependencies** |
| Engine gzipped (unminified) | **4,268 bytes** |
| `run()` — one 2000-step trajectory | **0.70 ms** |
| `verify()` — full gate set, 64-run sweep × 2000 steps | **39 ms per spec** |
| Discriminating-scenario search, 200 candidates | **296 ms** |

**Gate outcomes, on three specs of the same concept:**

| Spec | Result |
|---|---|
| **A.** Terminal velocity, composed `gravity.uniform + drag.linear` | G0 ✓ G1 ✓ G2 ✓ G3 ✓ G5 ✓ G7 ✓ G6 ✓ (control `m` moves `v` by 765%; control `b` by 94%) |
| **B.** Same sim, quadratic drag written with a `kg/s` coefficient — a realistic generated-physics error | **G1 FAIL**: `dimension mismatch in +: [1,0,-2,...] vs [2,0,-3,...]`. Halted **before execution**. Caught in microseconds, with no model in the loop |
| **C.** Free fall in vacuum, mass slider retained — the classic bad explorable | G1–G5 all pass, and **G6 FAIL twice**: `control m is a NULL SLIDER on v (0.00% < 5%)`. The sim is *physically correct* and *pedagogically a lie* |

**Spec C is the result worth dwelling on.** It passes every correctness check in the
literature — the physics is right, energy is conserved, nothing diverges — and it is the
most damaging of the three, because it hands the learner a mass slider in a vacuum and
therefore teaches, by silence, that mass is a variable here. **No existing verification
approach for generated simulations would catch it, because every one of them checks
correctness and none of them checks pedagogy.** G6 costs milliseconds.

**Twin-run and scenario-search outcomes:**

| Learner rule | Result |
|---|---|
| `dv/dt = -g·m - b·v/m` ("heavier falls faster") at defaults | **`tstar: null` — INDISTINGUISHABLE.** The engine refused to manufacture a refutation |
| Same rule, under 200-candidate scenario search | Discriminating scenario found at **step 1, t = 0.01 s**, at m = 1.57, b = 1.84 |
| `dv/dt = -g - b·v³/(400m)` ("drag doesn't matter until you're fast") | Diverges at **t\* = 0.21 s**; canonical v = −1.960, learner v = −2.060 |
| `dv/dt = (0 − g) − (b/m)·v` — an algebraic **rewrite of canon** | **"NO discriminating scenario exists in the declared control box. The learner's rule is empirically equivalent here. Say so; do not manufacture a refutation."** |

The last row is the honesty property working. A learner who states the canonical rule in
unfamiliar algebra must not be refuted, and the system establishes this **by running the
search and failing to find a divergence**, not by string-matching the expression.

**The two functions that do the work**, so the measurement is checkable rather than asserted.
This is the whole falsifier, minus the parser and the dimension algebra:

```js
// G6 — the null-slider gate. Milliseconds. Catches a physically correct,
// pedagogically dishonest world that every existing check would pass.
for (const c of spec.controls) {
  const lo = run(spec, {[c.param]: c.min}).trace;
  const hi = run(spec, {[c.param]: c.max}).trace;
  const key = c.observes, n = Math.min(lo.length, hi.length);
  let maxd = 0;
  for (let i = 0; i < n; i++) maxd = Math.max(maxd, Math.abs(lo[i][key] - hi[i][key]));
  const scale = Math.max(1e-12, Math.max(...lo.map(s => Math.abs(s[key]))));
  if (maxd / scale <= (c.min_effect ?? 0.05))
    fail('G6', `control ${c.param} is a NULL SLIDER on ${key}`);
}

// Stage 4 — discriminating-scenario search. Returns the setting that separates the
// learner's law from canon FASTEST, or an honest refusal.
function findDiscriminatingScenario(spec, learnerLaws, tau = 0.05, observe, budget = 200) {
  const alt = structuredClone(spec);
  for (const [k, v] of Object.entries(learnerLaws)) alt.laws[k] = v;   // ONE line differs
  const key = observe, r = rng(spec.budget.seed);
  let best = null;
  for (let s = 0; s < budget; s++) {
    const ov = {};
    for (const c of spec.controls) ov[c.param] = c.min + r() * (c.max - c.min);
    const A = run(spec, ov), B = run(alt, ov);          // same seed, dt, integrator, init
    if (A.diverged !== null || B.diverged !== null) continue;          // G7
    for (let i = 0; i < Math.min(A.trace.length, B.trace.length); i++) {
      const a = A.trace[i][key], b = B.trace[i][key];
      if (Math.abs(a - b) / Math.max(1e-9, Math.abs(a)) > tau) {
        if (!best || i < best.step) best = {step: i, tstar: A.trace[i].t, controls: {...ov}};
        break;
      }
    }
  }
  return best ?? {none: true,
    note: "NO discriminating scenario exists in the declared control box. The learner's " +
          "rule is empirically equivalent here. Say so; do not manufacture a refutation."};
}
```

The `?? {none: true, ...}` branch is the entire ethical content of the mechanic. It is four
lines, it is the easiest thing in the system to omit, and omitting it converts a falsifier
into a rigged demo that will be right often enough that nobody notices.

### 5.5 The runner-up, specified more briefly: *Two-Sided*

`SPEC`. The learner argues a position. The AI then takes **the position the learner argued
against** and commits to it — not as a "devil's advocate" flourish, but with a stated,
persistent, symbolically represented commitment it does not abandon under pressure (which,
per §5.2, is exactly what a prompted persona *will* do, so the commitment must be a stored
claim set the model is constrained to defend, checked each turn).

The scoring is the novel part. **Nobody wins.** The transcript is scored on whether the
learner's *own argument changed* — specifically, whether any claim in their opening position
was withdrawn, qualified, or given a boundary condition. F2 rates the adversary role
**[C] for AI implementations** against **[A] for the human analogues**, and productive
failure supplies the mechanism at **g = 0.36** `MEASURED-META`. Cost to build: low. Cost to
verify: high, and unsolved — "did this person's position actually move" is not a mechanically
checkable predicate, which is why this is the runner-up and not the pick.

---

## §6 — The inventory

`SPEC` on the design of every row; evidence label given where a measured basis exists.
**Cost** is order-of-magnitude for generating *one* artefact given the schema and registry.
**Buildable today** means plain JavaScript, ≤ 100 KB, no engine, this week.

| # | Mechanic | Machine | What it teaches | Cost to generate | Verification needed | Buildable today |
|---|---|---|---|---|---|---|
| 1 | **Twin run** — canonical vs. learner's compiled law, same seed | falsifier | that *your* rule is wrong, from the world | med (rule compilation) | G1, G5, twin-identity (§3.2) | **yes** — measured, 0.70 ms/run |
| 2 | **Discriminating-scenario search** | falsifier | — (enabling) | low | must return "none exists" honestly | **yes** — measured, 296 ms/200 |
| 3 | **Predict-the-next-second** before the divergence tick | falsifier | commitment, which is what makes disconfirmation land | low | prediction must be recorded *before* the run renders | **yes** |
| 4 | **The law diff** shown beside the divergence | falsifier | that exactly one thing differs | low | §3.2 twin identity | **yes** |
| 5 | **Empirical-equivalence report** ("your rule is indistinguishable here") | falsifier | that some disagreements are not empirical | low | G5 negative branch | **yes** — measured |
| 6 | **Boundary credit** — detecting that the learner's rule is right in *another* regime | falsifier | where a rule holds, not just that it fails | **high** | requires a regime map per law; unsolved in general | **partial** |
| 7 | **Refuted-law retrieval** weeks later, new surface features | falsifier | delayed transfer, on a personally-held error | low | item-equivalence across surface change | **yes** |
| 8 | **Null-slider audit** (G6) run on a *human-built* explorable | explorable | — (quality) | trivial | none | **yes** — measured |
| 9 | **Single-parameter sweep with a locked observable** | explorable | the shape of one dependency | low | G6, G1 | **yes** |
| 10 | **Two-parameter phase portrait** — regime boundaries, not values | explorable | that regimes exist | med | G6 on both axes; G7 on the whole box | **yes** |
| 11 | **Ghost trace** — previous parameter settings persist as faded curves | explorable | the *family* of behaviours, not one member | low | none | **yes** |
| 12 | **Linked symbol highlighting** — the term in the equation lights when it dominates | explorable | which term is doing the work, when | med | dominance must be computed, not asserted | **yes** |
| 13 | **Inverse problem** — "move the sliders until the output matches this" | explorable | that the mapping is (or is not) invertible | med | uniqueness check: is the target reachable by >1 setting? | **yes** |
| 14 | **Units-on-the-slider** — every control shows its dimension | explorable | dimensional reasoning, incidentally | trivial | G1 | **yes** — 9.4 KB gzip (js-quantities, measured) |
| 15 | **Reason-bearing refusal** — locked control explains itself on attempt | constrained object | why the boundary is where it is | trivial | `frozen.reason` non-empty (G0) | **yes** |
| 16 | **Legal-state witness set** — object must *accept* declared legal states | constrained object | — (safety) | low | both directions (§1.3) | **yes** |
| 17 | **Snap-to-legal** manipulative (fraction bars, number line, balance) | constrained object | the boundary of the concept, wordlessly | low | witness set; legality completeness | **yes** |
| 18 | **Illegal-state ledger** — what the learner *tried* that was refused | constrained object | (to the teacher) where the model is wrong | low | privacy: this is diagnostic data, treat as such | **yes** |
| 19 | **Representation-lock** — change any view, all views update or none do | constrained object | that the representations *are* the same object | med | `sync: strict`; frame-level equality test | **yes** |
| 20 | **Multi-representation contradiction hunt** — one view is deliberately wrong; find it | constrained object | that representations can disagree, and how to check | med | the injected error must be findable *and* unique | **yes** |
| 21 | **Grid agent world, ≤ 2k agents, declared update order** | agent world | macro from micro | med | G3 stochastic-mean over ≥32 seeds; `rules.order` explicit | **yes** |
| 22 | **Seed re-roll, visible** | agent world | that one run is one draw | trivial | seed must be user-visible (red-list row 3) | **yes** |
| 23 | **Ensemble ribbon** — 32 seeds drawn faintly behind the live run | agent world | the distribution, not the anecdote | low | over_seeds ≥ 32 | **yes** |
| 24 | **Rule-authoring by the learner** — write the agent rule, watch the aggregate | agent world | that they own the mechanism | med | learner rules go through G1/G7 like any other | **yes** |
| 25 | **Aggregate-invariant monitor** — "population is conserved" shown as a live check | agent world | that the model can be audited | low | the invariant must be real, not decorative | **yes** |
| 26 | **Emergence-vs-bug challenge** — learner must decide if a pattern is real | agent world | the actual scientific skill | high | requires a curated bug library | **partial** |
| 27 | **Variation-axis drill** — items differ on a declared axis every repetition | rehearsal | fluency that transfers | low | consecutive items must differ on the axis (G0) | **yes** |
| 28 | **Error-class targeting** — items selected by the learner's own error history | rehearsal | efficiency | med | requires a learner model; see F5 | **partial** |
| 29 | **Interleaved-machine practice** — falsifier / explorable / drill shuffled | mixed | discrimination between problem types | low | scheduling only | **yes** |
| 30 | **Jigsaw split** — A holds controls, B holds readouts | social | mutual dependence on non-substitutable info | med | must be genuinely non-derivable, not merely hidden | **partial** — needs transport |
| 31 | **Shared world state, separate goals** — competition *and* collaboration | social | the measured moderator | med | both goals must be achievable simultaneously | **partial** |
| 32 | **Teach-the-agent** — learner supplies the rule, agent runs it publicly | social + falsifier | knowledge-building (Roscoe & Chi trigger) | med | agent's error must be traceable to the learner's rule, not to the engine | **yes** |
| 33 | **Near-peer only comparison** — your week-3 self, never the leaderboard | social | progress without de-identification | low | **hard prohibition** on distribution tops | **yes** |
| 34 | **Persistent world, no counter** | fiction | continuity without a streak | med | no mechanic may be tangible + expected + performance-contingent | **yes** |
| 35 | **Diegetic consequence** — the bridge fails, no score changes | fiction | informational feedback in costume | low | audit: does any consequence carry a number? | **yes** |
| 36 | **Learner-authored SimSpec, verified in front of them** | authorship | modelling as the objective (Ben-Zion) | med | full gate set, shown as a passing/failing checklist | **yes** |
| 37 | **Audit-someone-else's-world** — run G6 on a peer's explorable | authorship | the week-15 role | low | none beyond the gates | **yes** |
| 38 | **Registry-gap report** — "we cannot simulate this correctly, here is why" | honesty | the limits of the tool | trivial | must be the **default** for unknown laws | **yes** |
| 39 | **Analytic-oracle overlay** — the closed-form solution drawn over the numeric one | honesty | that the simulation is an approximation | low | G4 | **yes** |
| 40 | **Integrator-artefact demo** — deliberately raise dt until the physics breaks | honesty | that the pretty motion is a computation | low | must be labelled as a demo of the *tool* | **yes** |
| 41 | **Rigid-body 2D scene** (collisions, friction, stacking) | any | contact phenomena | med | engine's own solver is the oracle; G3 on momentum | **yes** — matter-js **25,770 B gzip** (measured) |
| 42 | **3-D scene** | any | spatial phenomena | high | as above | **no this week** — three.js 23.17 MB unpacked |
| 43 | **Symbolic CAS step-checking inside the sim** | any | that the algebra and the motion agree | high | CAS is the oracle | **partial** — mathjs 9.43 MB unpacked; Algebrite last released **2021-04-14** |
| 44 | **Constraint-solved manipulative via SMT** | constrained object | arbitrary legality predicates | high | Z3 is the oracle | **no** — `z3-solver` **33–35.5 MB**, 2026-07-17 |
| 45 | **Python-authored sim the learner reads** | any | code literacy alongside the model | high | as any spec | **capped** — Pyodide 314.0.3: `pyodide.asm.wasm` **9.15 MB** + stdlib **2.43 MB**; ≤3 chapters (repo rule) |
| 46 | **Contrasting cases at consolidation** — the learner's failed law shown beside 2–3 near-miss laws, not just canon | falsifier | the boundary, via the Loibl design feature PS-I requires | low | the near-misses must be *near* — each must diverge from canon later than the learner's did | **yes** |
| 47 | **Refutation-text arm** — a paragraph stating the misconception and why it is wrong, shipped alongside every sim | any | the measured baseline (**g = 0.41**) the sim must beat | trivial | none; it is text | **yes** — and it is the control condition for every experiment in §7.3 |
| 48 | **Micro-macro routing gate** — refuse `kind: agent-world` when compatibility is `high` | agent world | — (economy) | trivial | the field must be set by a human or a checked classifier, not asserted by the generator | **yes** |
| 49 | **Observation commitment** — learner marks *what they expect to see change* before any run | falsifier / explorable | closes Chinn & Malhotra's observation-stage block | trivial | commitment recorded before render; immutable after | **yes** |
| 50 | **Guidance-presence audit** — every world must have a non-empty `frozen` set | any | that guidance beats none, whatever kind it is (Lazonder d = 0.50) | trivial | G0 extension | **yes** |

---

## §7 — Build order

### 7.1 This week, plain JavaScript

The substrate finding from `survey/16` is that **reactive JavaScript at 27 KB is the default**
and Pyodide at 21.89 MB + 4.5 s cold start is capped at ≤ 3 chapters. Everything in the
falsifier and explorable machines fits inside that budget, and this was measured rather than
assumed:

| Component | Measured size | Basis |
|---|---|---|
| SimSpec engine + all gates + twin + scenario search | **4.27 KB gzip** (11,982 B source, 240 lines, zero deps) | own build, 2026-07-29 |
| Dimensional analysis, if you want a real unit library instead | **9,428 B gzip** (js-quantities 1.8.0) | own measurement via jsDelivr |
| 2-D rigid body, if you need contact | **25,770 B gzip** (matter-js 0.20.0) | own measurement |
| Charting, if you need it | 92,360 B gzip (d3 7.9.0) — usually you do not; a 40-line canvas plot is enough | own measurement |

**A 2-D physics engine costs the same as this repo's entire default JavaScript budget.** That
is the buildability headline. The whole falsifier machine — engine, gates, twin run, scenario
search — is **one sixth** of it.

Build in this order:

1. **The verifier before the renderer.** G0, G1, G2, G6 first; they are microseconds each and
   they are the entire honesty story for explorables. Run them against existing hand-built
   explorables to calibrate `min_effect`.
2. **The constrained object.** Lowest cost, no time dimension, strongest measured mechanism
   (§1.3). Fraction bars, number line, balance scale. Ship the legal-state witness set from
   day one.
3. **The single-parameter explorable** over closed-form relationships. No integrator needed.
4. **The falsifier for 1-D and 2-D ODE systems.** Hand-rolled RK4 is ~40 lines. This is
   mechanic #1 and it is the pick.
5. **The grid agent world.** Canvas, ≤ 2k agents, declared update order, visible seed.

**What to build first, if only one thing:** mechanic #1 + #2 + #5 — the twin run with
discriminating-scenario search and the honest empirical-equivalence report. It is the only
mechanic in the inventory that no other medium can do at all, it is 240 lines, and the search
is what makes it truthful rather than theatrical.

### 7.2 What needs a real engine

- **Contact, friction, stacking, joints.** matter-js (25.8 KB gzip) is the cheap option but
  its **last commit is 2024-06-23** with 279 open issues `OBSERVED` — usable, not maintained.
  rapier (Apache-2.0, commits **2026-07-12**, npm `@dimforge/rapier2d` 0.19.3 @ 2025-11-05,
  2.33 MB unpacked) is the maintained option and costs ~90× the bytes. Note
  `dimforge/rapier.js` is **archived** — the TypeScript bindings moved into the main repo.
  `schteppe/cannon.js` is **dead since 2016-05-03**; the live fork is `pmndrs/cannon-es`
  (2024-01-06).
- **Anything 3-D.** three.js is alive (commit 2026-07-29, r185) and is 23.17 MB unpacked.
  This is a different product, not a bigger chapter.
- **A CAS in the loop.** mathjs is the only actively maintained option with first-class units
  (commit 2026-04-16, 9.43 MB unpacked); Algebrite's last release was **2021-04-14**.
- **The PhET toolkit** (`scenerystack`, npm 3.0.0 @ 2025-09-09; scenery/joist/sun/axon all
  **MIT**, commits through 2026-07) is the only production-grade educational-sim toolkit that
  exists, and PhET's 119 HTML5 sims can be iframed directly (no `X-Frame-Options` observed).
  **Use the toolkit, embed the sims, do not fork a sim** — the sims are GPL-3.0.

### 7.3 What needs research

Stated as open problems with the shape of the answer, not as caveats.

1. **Reveal-reachability proving in general.** G5 is currently a randomised search over the
   control box (296 ms / 200 candidates, measured). That is a sound *falsifier* of reachability
   and an unsound *prover* of unreachability. For the `must_be_unreachable_from` branch — the
   anti-rigging check — a search that finds nothing is weak evidence. The shape of the answer
   is interval arithmetic or a small SMT encoding over the control box; the cost is the
   35 MB of z3-solver, which is why this is research and not this week.
2. **NL → law compilation reliability.** There is no benchmark. `SPEC` one: a corpus of
   learner-stated rules paired with reference compiled laws, scored on (a) does the compiled
   law reproduce the learner's stated predictions on held-out scenarios, and (b) does the
   learner, shown the compiled law *running*, confirm it is theirs. Metric (b) is the one that
   matters and it requires humans. The PDDL literature has the closest precedent
   (NL-PDDL-Bench, arXiv:2606.29700) and its framing — "executable and verifiable" — transfers
   directly.
3. **The misconception registry outside algebra and mechanics.** MalAlgoPy/MalAlgoLib exist for
   algebra `MEASURED-BENCH`. Nothing comparable exists for biology, economics, chemistry, or
   statistics. This is a corpus-construction project with a clear format: (misconception id,
   text, status ∈ {false, partial, domain-limited}, the domain where it *does* hold, and at
   least one discriminating scenario).
4. **Does twin-run divergence actually produce conceptual change?** **This is the falsifier
   hypothesis and it is untested.** The mechanism it borrows (PS-I, g = 0.36) is measured; the
   specific claim that *the learner's own compiled rule, run to visible divergence, beats a
   tutor asserting the correction* is not. **The experiment is now fully specified by §1.1b,
   and it is not two arms but four:** (i) refutation text — the free baseline at **g = 0.41**;
   (ii) discrepant-event demonstration — the arm the cognitive-conflict literature says mostly
   fails; (iii) twin run **without** stage 3 consent and stage 5 prediction; (iv) the full
   mechanic. Outcome: delayed unassisted transfer. The `refuted_law` record (§5.3 stage 8) is
   the instrument. Arm (iii) is the one that matters scientifically, because it isolates
   whether the *identity guarantee plus prediction* — and not merely the animation — is doing
   the work. **If (iv) does not beat (i), the falsifier machine is expensive theatre and this
   document is wrong about its central claim.**
5. **The week-15 dip response.** Whether a role change (consumer → author → reviewer) beats a
   novelty injection when the dip is detected. van Roy & Zaman gives the dip; nothing gives
   the response.
6. **`min_effect` calibration for G6.** The 5% default in the reference implementation is
   arbitrary. The right value is empirical: the smallest change in an observable that a
   learner reliably notices and attributes to the control. That is a psychophysics
   experiment and it would make G6 a principled gate rather than a useful heuristic.

---

## §8 — Sources

**Repo sections taken as settled:** `research/raw/F6-motivation-persistence.md` (§3, §6, §7);
`survey/06-what-the-object-must-refuse.md`; `survey/16-the-substrate.md`;
`research/raw/A5-world-models.md` (§4, §5, §6); `research/raw/A2-interactive-animation.md`
(§1.3, §1.8, §4); `research/raw/F2-beyond-the-tutor.md` (§2, §3, §5).

**Measured, external.** Sailer & Homner 2020 [10.1007/s10648-019-09498-w]; Bai, Hew & Huang
2020 [10.1016/j.edurev.2020.100322]; Deci, Koestner & Ryan 1999 [10.1037/0033-2909.125.6.627];
Koivisto & Hamari 2014 [10.1016/j.chb.2014.03.007]; van Roy & Zaman 2018
[10.1016/j.compedu.2018.08.018]; Rogers & Feller 2016 [10.1177/0956797615623770]; Kizilcec
et al. 2017 [10.1145/3027385.3027411]; Sinha & Kapur 2021 [10.3102/00346543211019105]; Kapur
2016 [10.1080/00461520.2016.1155457]; Kobayashi 2019 [10.1111/jpr.12221]; Roscoe & Chi 2007
[10.3102/0034654307309920]; Biswas, Leelawong, Schwartz & Vye 2005 [10.1080/08839510590910200]
(Betty's Brain; the repo's F2 records 310 citations, Semantic Scholar returned 493 for the
same DOI this pass — reported as retrieved, not reconciled) and Chase, Chin, Oppezzo &
Schwartz 2009 on the protégé effect [10.1007/S10956-009-9180-4] (368 cites, S2, this pass);
Novack & Goldin-Meadow on gesture vs. action on objects (via `survey/06`); Wilensky &
Reisman, "Thinking Like a Wolf, a Sheep, or a Firefly"; Grimm et al., the **ODD protocol**
for agent-based model description; Hamari, Koivisto & Sarsa 2014 [10.1109/HICSS.2014.377];
Cerasoli, Nicklin & Ford 2014 [10.1037/a0035661]; VanLehn 2011
[10.1080/00461520.2011.611369]; Bjork & Bjork 2020 [10.1016/j.jarmac.2020.09.003];
Ploetzner, Berney & Bétrancourt 2020
[10.1111/jcal.12476] and 2021 [10.1007/s11251-021-09541-w]; Finkelstein et al. 2005
[10.1103/PhysRevSTPER.1.010103]; Wieman, Adams & Perkins 2008 [10.1126/science.1161948];
de Jong, Linn & Zacharia 2013 [10.1126/science.1230579]; Rutten, van Joolingen & van der Veen
2012 [10.1016/j.compedu.2011.07.017]; Smetana & Bell 2012 [10.1080/09500693.2011.605182];
Paul, Podolefsky & Perkins 2013 [10.1063/1.4789712]; Ben-Zion, Carroll, West, Wong &
Finkelstein 2026 [10.1103/s8dy-kqy5]; Freeman et al. 2014 [10.1073/pnas.1319030111].

**Measured, retrieved this pass via ERIC and Crossref (2026-07-29).** Chernikova, Heitzmann,
Stadler, Holzberger, Seidel & Fischer 2020, *RER* 90(4), g = 0.85 [0.69, 1.02], k = 145;
Hu, Jia, Mi & Bi 2026, *JOST*, g = 0.898 [0.719, 1.076], k = 47, n = 5,715; Lazonder &
Harmsen 2016, *RER* 86(3), k = 72; Furtak, Seidel, Iverson & Briggs 2012, *RER* 82(3), mean
ES 0.50, k = 37; Lazonder & Egberink 2014, *Instructional Science*; Clark, Tanner-Smith &
Killingsworth 2016, *RER* 86(1); Wouters, van Nimwegen, van Oostendorp & van der Spek 2013,
*JEP* 105(2); Wouters & van Oostendorp 2013, *C&E* 60(1); Sitzmann 2011, *Personnel
Psychology* 64(2); Vogel et al. 2006, *JECR* 34(3) (directional only); Lei, Chiu, Wang, Wang
& Xie 2022, *JECR* 60(6); Tsai & Tsai 2020, *JCAL* 36(3); Riopel et al. 2019, *SSE* 55(2)
(no numbers); Schroeder & Kucera 2022, *Educ. Psych. Review*, g = 0.41, 44 comparisons,
n = 3,869; Danielson, Jacobson, Patall, Sinatra, Adesope, Kennedy et al. 2025, *Educational
Psychologist* (pre-registered; 294 ES, 26 moderators); Tippett 2010, *IJSME*; Guzzetti,
Snyder, Glass & Gamas 1993, *RRQ* 28(2); Limón 2001, *L&I* 11(4–5); Chinn & Brewer 1993,
*RER* 63(1) and 1998, *JRST* 35(6); Chinn & Malhotra 2002, *JEP* 94(2); Kang, Scharmann,
Kang & Noh 2010, *IJESE*, N = 183; Kang, Scharmann, Noh & Koh 2005, *IJSE*, N = 159; Lee &
Byun 2012, *RiSE*, N = 96; Dega, Kriek & Mogese 2013, *JRST* 50(6), n = 45, η²ₚ = 0.12;
Dreyfus, Jungwirth & Eliovitch 1990, *Science Education*; Chi 2005, *JLS* 14(2); Adams,
Reid, LeMaster, McKagan, Perkins, Dubson & Wieman 2008, *JILR* (275+ interviews); Wilensky &
Reisman 2006, *Cognition and Instruction* 24(2) (case studies, no ES); Levy & Wilensky 2009,
*JOST* 18(3); Samon & Levy 2017, *Science Education* 101(6), n = 47/45; Sengupta & Wilensky
2009, *IJCML* 14(1); Blikstein & Wilensky 2009, *IJCML* 14(2); Sun, Ren, Liu, Xu, Gao & Li
2026, *JRST*, g = 0.470, 62 ES / 25 studies; Rodrigues et al. 2022, *IJETHE*, N = 756,
14 weeks; Tsay, Kofinas, Trivedi & Yang 2020, *JCAL*, N = 508, 3 years; Krendl & Broihier
1991, ERIC ED332250, N = 339, 3 years; Koyunlu Ünlü 2024 (POE, g = 0.979 — low-visibility
venue, treated as soft); Loibl, Roll & Rummel 2017, *Educ. Psych. Review* 29; Loibl & Rummel
2014, *L&I* 34; Kapur 2012, *Instructional Science* 40(4); Kapur 2014, *Cognitive Science*
38(5); Brand, Hartmann, Loibl & Rummel 2023, *Instructional Science* 51; Rutten et al. 2016,
*Learning: Research and Practice* (null); Smetana & Bell 2012 and de Jong & van Joolingen
1998 (narrative reviews, no pooled ES).

**Measured, benchmark.** VideoPhy arXiv:2406.03520; VideoPhy-2 arXiv:2503.06800; PhyGenBench
arXiv:2410.05363; Physics-IQ arXiv:2501.09038; Code World Models arXiv:2405.15383;
GameCWM distillation arXiv:2605.24375; NL-PDDL-Bench arXiv:2606.29700; PDDL domain consistency
arXiv:2404.07751; environment-verified PDDL translation arXiv:2407.12979; misconception
faithfulness / Selective Flip Score arXiv:2605.12748; MalAlgoPy / Cognitive Student Models
arXiv:2410.12294; MalAlgoLib / misconception acquisition dynamics arXiv:2604.00818; ODD-based
ABM replication across 17 LLMs arXiv:2602.10140; ViviDoc (interactive-document generation)
arXiv:2603.01912.

**Primary sources retrieved this pass (2026-07-29).** worrydream.com/ExplorableExplanations
(2011-03-10); ciechanow.ski/archives (22 posts, last 2024-12-17); ncase.me; explorabl.es
(180 catalogued entries); setosa.io/ev (9 pieces, dead since 2015-02-17); redblobgames.com;
acko.net; phet.colorado.edu metadata API (119 HTML5 sims / 246 total).

**Own measurements (2026-07-29).** SimSpec v0 engine and gate outcomes (§5.4); npm registry
and jsDelivr byte measurements for matter-js, rapier2d, cannon-es, mathjs, Algebrite,
js-quantities, z3-solver, d3, three, p5, planck-js, @observablehq/plot; GitHub commit-date
audit of 30 repositories via `gh api`; PhET licence split read from LICENSE files.

---

## §9 — Limitations

**The central claim of this document is untested.** That a learner's own compiled rule, run to
visible divergence, produces more conceptual change than a tutor asserting the correction is
`SPEC`. It inherits a measured mechanism (PS-I, g = 0.36) and it is not the same claim. §7.3
item 4 is the experiment that would settle it.

**The reference implementation is a 240-line proof that the schema executes, not evidence that
it teaches.** It was run on one concept in one domain by one author. Its most interesting
outputs — the null-slider catch and the honest empirical-equivalence report — demonstrate that
the *gates fire*, not that a learner benefits.

**G5's unreachability branch is unsound.** Randomised search over the control box can prove
reachability and cannot prove its absence. Until that is an interval or SMT check, the
anti-rigging guarantee is weaker than §3.2's twin-identity guarantee, which is sound.

**The registry is the whole architecture and it does not exist.** Every honesty property in
§3 rests on a verified law registry with adequate curriculum coverage. Building it is a
sustained, unglamorous, domain-expert-heavy project, and the system's usefulness is bounded
by it.

**Effort estimates for the prior-art table are inferences from code volume**, explicitly not
claims by their authors, who have not published hours. They are labelled as such in the table
and should not be quoted as figures.

**Two arXiv abstracts (2602.10140, 2603.01912) were retrieved in truncated form** before rate
limiting; their existence and framing are cited, no numbers from them are.

**A named list of things this pass could not verify, so they are not quoted as numbers.**
D'Angelo, Rutstein & Harris (the 2014 SRI simulation meta-analysis) — no numeric effect size
resolvable in ERIC, Crossref or Semantic Scholar. Guzzetti et al. 1993 — the "conceptual
conflict is the common element" conclusion is verified; **per-strategy effect sizes are not**.
Merchant et al. 2014 (VR meta-analysis, the one that separates games from simulations from
virtual worlds) — abstract publisher-elided everywhere. Vogel et al. 2006 and Riopel et al.
2019 — meta-analyses whose abstracts contain no effect sizes; directional claims only.
Wieman, Adams & Perkins 2008 (*Science*) is a Forum piece with no data and is **not cited for
a number**. Finkelstein et al. 2005 — direction verified, magnitude not. Clark et al. 2016
per-moderator coefficients and Wouters et al. 2013 per-level moderator *d*s — directions
verified, magnitudes not. Levy & Wilensky 2009 and Samon & Levy 2017 report "strong" and
"medium" effect sizes **verbally only**. Vosniadou's mental-models work and Wilensky &
Papert's "restructurations" returned **nothing retrievable** and are not cited. Semantic
Scholar and OpenAlex returned HTTP 429 on nearly every request from this address; ERIC and
Crossref carried the retrieval, which biases coverage toward journals those two index well.

**One structural bias in this document's own evidence.** The strongest empirical material
here — cognitive conflict, refutation text, productive failure — is about *conceptual change
in science*, because that is where the measurement is. The five machines are proposed as
general, and four of the five have no domain-general evidence at all. That is a real limit on
how far the taxonomy should be pushed outside STEM before someone measures it.
