---
title: "Special education, SELPA, and accessibility-first design: build for the margin and you build for everyone"
wave: H
date_researched: 2026-07-27
sources_count: 69
---

# H1 — Special education, SELPA, and accessibility-first design

**Thesis under test:** build the SELPA-grade system and it serves everyone (Universal
Design for Learning / the curb-cut effect). Designing for the margin first is better
engineering, not charity.

**Verdict after research:** the *engineering* half of the thesis survives and is
strongly supported. The *UDL-as-evidence-base* half does not survive contact with the
literature and must be restated. And the survey's most important empirical finding
lives here: **AI tutoring has essentially never been evaluated on students with
disabilities.** The gap is not "thin." It is, by a reproducible census of two major
databases, approximately zero randomised trials.

---

## 0. Headline findings

| # | Finding | Label |
|---|---|---|
| **F1** | Across ERIC and Europe PMC (censused 2026-07-27), **zero** randomised controlled trials of generative-AI tutoring on students with disabilities could be located. 30 GenAI-education RCTs indexed in Europe PMC mention students; **0** mention disability, dyslexia, ADHD, autism, special education, or IEPs. | `MEASURED-BENCH` (own census, queries below) |
| **F2** | The *entire world literature* on AI interventions for students with learning disabilities, 2022–2025, across seven databases, is **11 studies / 10 independent experiments / 3,033 participants**, of which **at most one is an RCT (n=60)** and **none** was rated low risk of bias. All 11 reported positive results — a publication-bias signature. | `MEASURED-META` (Paglialunga & Melogno 2025) |
| **F3** | By contrast the Direct Instruction literature alone is **328 studies / 413 designs / ~4,000 effects**, all positive and all significant except affective outcomes. The known-good intervention base is *two orders of magnitude* larger than the AI base. The AI's job here is fidelity and dosage, not invention. | `MEASURED-META` (Stockard et al. 2018) |
| **F4** | **UDL is a design philosophy with weak empirical support, not an evidence-based intervention.** The best meta-analysis concludes UDL improves the learning *process* but "the impact on educational outcomes has not been demonstrated." A policy review found "no rigorous published research has demonstrated any improvement." The *component* practices UDL bundles are individually well-evidenced. Keep the components; drop the claim. | `MEASURED-META` + `OBSERVED` |
| **F5** | **Measurement without a decision rule does not work.** In a randomised teacher-level trial, CBM alone produced more frequent program revisions but **no achievement gain**; only CBM *plus* an expert system that told teachers *what to change* produced superior achievement. This is the single most architecturally load-bearing finding for the H1.2 bidirectional loop. | `MEASURED-RCT` (Fuchs, Hamlett & Stecker 1991) |
| **F6** | Pivoting too fast is a real failure mode with a number attached: CBM trend-line decision rules are **not viable until 7–10 weeks of weekly data**. An AI tutor that changes method after two wrong answers is operating far inside the noise floor. | `MEASURED-BENCH` (Van Norman et al. 2023) |
| **F7** | Unconstrained LLM use **widens** the gap between low- and high-prior-knowledge learners (Lehmann et al.), and the largest AI-tutoring RCT gains in Nigeria accrued to **students with higher initial academic performance**. Restraint matters *more* for this population, not less. | `MEASURED-RCT` ×2 |
| **F8** | Orton-Gillingham — the intervention most requested by parents of dyslexic children — shows **non-significant** effects over comparison instruction (g = 0.22, *p* = .40; g = 0.14, *p* = .59). The evidenced ingredient is *explicit, systematic decoding instruction*, not the multisensory branding. | `MEASURED-META` (Stevens et al. 2021) |
| **F9** | The federal at-scale evaluation of RTI found **negative** Grade-1 impacts: students just below the intervention threshold scored *lower* in spring than those just above. Framework fidelity ≠ framework benefit. | `MEASURED-RCT` (regression-discontinuity; Balu et al. 2015) |
| **F10** | Working-memory training does not transfer. Do **not** build a brain-trainer; **externalise memory** instead. | `MEASURED-META` (Melby-Lervåg, Redick & Hulme 2016) |

---

## 1. The evidence base

Special education is the most replication-rich area in education. This section
establishes the numbers the system must be held to, and — equally important — the
places where the folk consensus is wrong.

### 1.1 Reading, structured literacy, and the Orton-Gillingham problem

**National Reading Panel meta-analyses (Ehri et al. 2001).** Two companion syntheses
give the field's anchor numbers.

- *Systematic phonics:* 66 treatment–control comparisons from 38 experiments. Overall
  effect on reading **d = 0.41**. Larger when begun early (**d = 0.55**) than after
  first grade (**d = 0.27**). Effects persisted after instruction ended.
  `MEASURED-META` — https://doi.org/10.3102/00346543071003393
- *Phonemic awareness:* 52 studies, 96 comparisons. Effect on PA itself **d = 0.86**;
  on reading **d = 0.53**; on spelling **d = 0.59**.
  `MEASURED-META` — https://doi.org/10.1598/rrq.36.3.2

**The caveat Ehri herself reported, which is routinely dropped when this work is cited:**
phonics "helped low and middle SES readers, younger students at risk for reading
disability, and older students with RD, **but it did not help low achieving readers
that included students with cognitive limitations**." That is a documented boundary
condition on the field's most-cited finding, and it is exactly the population H1 exists
to serve. `MEASURED-META`

**Randomised-only synthesis (Galuschka et al. 2014, PLoS ONE).** 22 RCTs, 49
experimental–control comparisons, restricted to children and adolescents with diagnosed
reading disabilities. Of the treatment families examined — reading fluency training,
phonemic awareness instruction, comprehension training, phonics instruction, auditory
training, medical treatments, coloured overlays/lenses, "sunflower therapy," motor
exercises — **phonics instruction was the only approach whose efficacy reached
statistical significance.** Every other family's mean effect was non-significant.
`MEASURED-META` — https://doi.org/10.1371/journal.pone.0089900

This is the cleanest available statement of the design constraint: for this population,
the *systematic decoding* channel is the one with randomised support, and the popular
alternatives (coloured overlays, auditory training, motor programmes) are not merely
weaker — they are unsupported.

**Orton-Gillingham: the honest finding (Stevens et al. 2021, *Exceptional Children*).**
24 studies identified, 16 meta-analysed, students with or at risk for word-level reading
disabilities.

| Outcome domain | Hedges *g* | 95% CI | *p* | Significant? |
|---|---|---|---|---|
| Foundational skills (PA, phonics, fluency, spelling) | **0.22** | [−0.33, 0.77] | .40 | **No** |
| Vocabulary & comprehension | **0.14** | [−0.39, 0.66] | .59 | **No** |

Heterogeneity was very large (I² = 88.7% and 81.5%). Authors' conclusion, verbatim:

> "Despite the continued widespread acceptance, use, and support for OG instruction,
> there is little evidence to date that these interventions significantly improve
> reading outcomes for students with or at risk for WLRD over and above comparison
> group instruction."

`MEASURED-META` — https://doi.org/10.1177/0014402921993406 · full text
https://pmc.ncbi.nlm.nih.gov/articles/PMC8497161/

**How to state this without doing harm.** The comparison conditions in these studies
were *also* explicit decoding instruction. The finding is not "OG doesn't work"; it is
"OG does not beat other explicit, systematic decoding instruction." The active
ingredient is explicitness and system, not the multisensory ritual. A system that
delivers explicit, systematic, cumulative decoding instruction with high fidelity and
high dosage is delivering the evidenced thing. A system that markets "multisensory
Orton-Gillingham" as a differentiator is marketing the unevidenced part. `INFERENCE`
(from Stevens et al. + Galuschka et al.)

**The dissenting voice, reported because it exists (Bowers 2020,
*Educational Psychology Review*).** A systematic review of 12 phonics meta-analyses
plus England's national synthetic-phonics policy since 2007 argues the pro-phonics
conclusion "is not justified." Bowers explicitly does *not* argue for whole language.
This is a minority position within the field and is contested, but a survey claiming to
leave no stone unturned should not pretend consensus is unanimous.
`MEASURED-META` (contested) — https://doi.org/10.1007/s10648-019-09515-y

**Non-responders exist and are predictable (Al Otaiba & Fuchs 2006).** 104 children
given best-practice early literacy instruction. A combination of naming speed,
vocabulary, sentence imitation, problem behaviour, and amount of intervention correctly
predicted **82.1%** of non-responders. Of the non-responsive students who received
intervention, **all but one** had been identified for special education with an IEP
containing reading goals by end of third grade.
`OBSERVED` (longitudinal, non-randomised) — https://doi.org/10.1177/00222194060390050401

**Design consequence.** "This intervention has an effect size of 0.41" is a statement
about a distribution, not about a child. The system must be built on the assumption that
some proportion of its learners will not respond to its best first-line method, must
detect that early, and must have a defined next move. Non-response is not an edge case;
it is a designed-for state.

### 1.2 Explicit and direct instruction

**Stockard, Wood, Coughlin & Rasplica Khoury (2018), *Review of Educational Research*.**
Fifty years of Direct Instruction research: **328 studies, 413 study designs, ~4,000
effects.** All estimated effects positive; all statistically significant except
metaregressions on affective outcomes. Effects showed little decline during maintenance,
and **effects for academic subjects were greater when students had more exposure to the
programs** — a dosage relationship. Estimated effects were "moderate to large" and
"similar in magnitude to effect sizes that reflect performance gaps between more and
less advantaged students." Publication, methodology, and sample characteristics were
*not* systematically related to effect estimates.
`MEASURED-META` — https://doi.org/10.3102/0034654317751919

The dosage finding is the licence for this entire project. If more exposure to explicit
instruction produces more learning, and human staffing ratios cap exposure, then a
system that raises exposure at fidelity is doing the one thing the evidence says
increases the effect.

**Swanson & Hoskyn (1998), *Review of Educational Research*.** 180 experimental
intervention studies with students with learning disabilities. Overall mean effect
**M = 0.79**. Crucially: "Effect sizes were more positive for a **combined model that
included components of direct *and* strategy instruction** than for competing models."
Significant predictors of effect size were **controlling task difficulty**, **small
interactive groups**, and **directed responses and questioning of students**.
`MEASURED-META` — https://doi.org/10.3102/00346543068003277

**Swanson (1999), domain-specific.** Word recognition **ES = 0.59**; reading
comprehension **ES = 0.72**. Comprehension gains were highest when studies combined
cognitive-strategy *and* direct instruction; word recognition gains were highest under
direct instruction alone.
`MEASURED-META` — https://doi.org/10.1177/002221949903200605

**Swanson & Sachse-Lee (2000), single-subject designs.** 85 studies. All domains except
handwriting yielded effects at or above Cohen's 0.80. The components carrying variance:
**drill–repetition–practice–review**, **segmentation**, **small interactive groups**,
and **cues to use strategies**.
`MEASURED-META` — https://doi.org/10.1177/002221940003300201

**Swanson & Hoskyn (2001), adolescents.** Of eight instructional factors extracted
across programmes, **only the organisation/explicit-practice factor** contributed
significant unique variance to outcomes.
`MEASURED-META` — https://doi.org/10.1111/0938-8982.00012

**Kirschner, Sweller & Clark (2006).** The theoretical spine: minimal-guidance
instruction fails because it ignores working-memory limits and the absence of relevant
long-term-memory schemas. The argument is *strongest* precisely where prior knowledge is
thinnest — which is the H1 population by definition.
`INFERENCE` from theory + `MEASURED-META` corroboration above —
https://doi.org/10.1207/s15326985ep4102_1

**Project Follow Through.** The largest educational experiment ever conducted in the
United States (≈700,000 children, 1968–1977). Direct Instruction was the only model to
show positive outcomes across basic skills, cognitive skills, and affective measures.
Long-term follow-up found sustained academic effects.
`OBSERVED` (quasi-experimental at scale; the design has been criticised for
non-random site assignment and differential attrition — report it as historically
important, not as an RCT) — Meyer 1984, https://doi.org/10.1086/461371 ·
Meyer, Gersten & Gutkin 1983, https://doi.org/10.1086/461360

**Convergent design consequence.** Every synthesis independently surfaces the same
component list: explicit modelling, controlled task difficulty, segmentation, sequenced
practice with review, frequent directed questioning, small interactive grouping,
scaffolds with cues. That list is a *specification*, and it is one an agent-based system
can implement with more consistency than a human under caseload pressure.

### 1.3 RTI / MTSS — and its most important negative result

**The framework.** Multi-tiered systems of support: universal screening, tiered
intervention of increasing intensity, progress monitoring, data-based decisions about
movement between tiers.

**Balu, Zhu, Doolittle, Schiller, Jenkins & Gersten (2015), NCEE 2016-4000 — the
documented negative result.** A federal evaluation of RTI in Grade 1–3 reading across
**146 schools in 13 states**, all *experienced* with RTI (86% reported full
implementation). Using a regression-discontinuity design around the screening threshold:

> "Students who scored just below school-determined benchmarks on fall screening tests,
> and who were assigned to interventions for struggling readers, had **lower** spring
> reading scores in Grade 1 than students just above the threshold for intervention. In
> Grades 2 and 3, there were **no statistically significant impacts**."

`MEASURED-RCT` (regression-discontinuity) — ERIC ED560820 /
https://ies.ed.gov/ncee/pubs/20164000/

This is the most important cautionary result in the section and must be reported
prominently. A framework can be implemented with high fidelity and still fail. Plausible
mechanisms discussed in the literature include: pulling students *out of* effective
core instruction to deliver intervention; intervention quality below core quality;
and Grade-1 measures being noisy near the threshold. The system-design lesson:
**routing a child into "intervention" is not neutral — it has an opportunity cost, and
that cost must be part of the decision.** `INFERENCE`

### 1.4 Curriculum-Based Measurement, Data-Based Individualization, and the pivot rule

This subsection is the empirical foundation of H1.2 (the bidirectional loop). It is also
where the literature says something an AI-tutor builder will not expect.

**CBM's origin (Deno 1985, *Exceptional Children*).** CBM = brief, standardised,
repeated, curriculum-referenced probes (e.g. 1-minute oral reading rate) that are
reliable enough to graph and sensitive enough to detect growth over weeks. Deno's
framing: standardise the *observation*, not the curriculum.
`OBSERVED` — https://doi.org/10.1177/001440298505200303

**Does it work? (Fuchs & Fuchs 1986, meta-analysis.)** 21 controlled studies, 96 effect
sizes. Average weighted effect of systematic formative evaluation **ES = 0.70**.
Magnitude was moderated by **data-evaluation method** and **data display** — i.e. by
*how* the data were used, not merely that they were collected.
`MEASURED-META` — https://doi.org/10.1177/001440298605300301

**F5 — the finding that should govern the architecture (Fuchs, Hamlett & Stecker 1991,
*AERJ*).** 33 teachers randomly assigned to three conditions: CBM with expert-system
instructional consultation (CBM-ExS), CBM without it (CBM-NExS), and no-CBM control.
20 weeks.

> "Compared to the control group, **both** CBM groups appeared to revise students'
> instructional programs more frequently. However, **only the CBM-ExS group effected
> superior student achievement.**"

`MEASURED-RCT` — https://doi.org/10.3102/00028312028003617

Read that twice. Frequent measurement plus frequent program changes, *without* guidance
on what to change, produced **no achievement benefit**. The benefit came from the
component that told the teacher *what to do next*. A companion randomised study in
spelling replicated the pattern (Fuchs, Fuchs, Hamlett & Allinder 1991,
https://doi.org/10.1080/02796015.1991.12085532). `MEASURED-RCT`

**Direct consequence for this project:** an AI tutor that "monitors engagement and
adapts" is the CBM-NExS condition. Dashboards, streaks, mastery bars, and adaptive
difficulty are *measurement*. They are not the active ingredient. **The active
ingredient is a prescribed, principled change of instruction, drawn from a known-good
menu, triggered by a stated rule.** Build the expert system, not the dashboard.

**Confirmed at review scale (Stecker, Fuchs & Fuchs 2005).** Reviewing experimental
CBM contrast studies in reading and mathematics: "several critical variables appeared to
be associated with enhanced achievement **for students with disabilities**: teachers'
use of **systematic data-based decision rules**, **skills analysis feedback**, and
**instructional recommendations for making program modifications**."
`MEASURED-META` — https://doi.org/10.1002/pits.20113

**Data-Based Individualization (NCII).** The formal five-step process for students who
do not respond to standard-protocol intervention:

1. Validated intervention programme, delivered with fidelity
2. Progress monitoring
3. Diagnostic assessment (academic) / functional behaviour assessment
4. **Intervention adaptation**
5. Progress monitoring → decision point → loop

`OBSERVED` — https://intensiveintervention.org/data-based-individualization

**The decision rules themselves.** Three families are used in practice and studied in
the literature (Ardoin, Christ, Morena & Cormier 2013, systematic review of CBM-R
decision rules, https://doi.org/10.1016/j.jsp.2012.09.004; Van Norman & Christ 2016,
https://doi.org/10.17105/spr45-3.296-309):

- **Data-point rule (the "four-point rule").** Set a goal line from current level to
  the year-end goal. If the most recent *N* consecutive points (classically four) fall
  **below** the goal line → **change the instruction**. If the most recent *N* fall
  **above** it → **raise the goal**. If they straddle it → **continue**.
- **Trend-line rule.** Fit an ordinary-least-squares trend to the collected points. If
  the trend is **flatter than** the goal line → change instruction. Steeper → raise the
  goal.
- **Median rule.** A variant using medians of point sets to reduce sensitivity to
  outliers.

⚠️ **Source caution:** NCII's public DBI landing page describes the five-step process
but does **not** publish the numeric rules; the PDF training modules that do were not
retrievable during this research (404s). The rule specifications above are taken from
the peer-reviewed CBM decision-rule literature (Ardoin et al. 2013; Van Norman &
Christ 2016; Van Norman et al. 2023). The survey should cite the journal literature,
not NCII marketing pages, for the numbers. `OBSERVED` with sourcing caveat noted.

**F6 — how long before pivoting (Van Norman, Klingbeil, Truman & Nelson 2023,
*Remedial and Special Education*).** Simulation study of three decision rules applied to
nonsense word fluency and CBM-R for students receiving Tier-2 support, one observation
per week:

> "The trend-line rule was viable with NWF after **7 weeks** and **9 to 10 weeks** with
> CBM-R."

`MEASURED-BENCH` (simulation from empirical parameters) —
https://doi.org/10.1177/07419325231190812

Related work by the same group: Van Norman, Christ & Newell 2017 on goal-setting and
growth magnitude (https://doi.org/10.17105/spr-2017-0065.v46-3); Van Norman & Nelson
2019 showing seasonal goal lines reduce the weeks of data required
(https://doi.org/10.1177/1534508419872249); Van Norman & Christ 2016 finding decision
rules outperform unaided visual analysis (https://doi.org/10.1016/j.jsp.2016.07.003).

**This is the number the PRD asked for.** The PRD states "too fast is as harmful as too
slow, because method-thrash prevents any method from consolidating." The literature now
puts a floor under it: **on weekly academic probes, a trend-based non-response judgement
is not statistically viable for 7–10 weeks.** An AI tutor that swaps representation
after three wrong answers is not adapting; it is fitting noise, and it destroys the
consolidation that explicit instruction requires.

**The resolution — two clocks, not one.** The literature supports a two-timescale
architecture, and conflating them is the design error:

| Clock | Signal | Latency | Action |
|---|---|---|---|
| **Fast (within-session)** | Error *type*, latency, help-seeking, disengagement, self-report | Seconds–minutes | Micro-scaffold: prompt, hint, worked step, re-representation of *this item*. Do **not** change the method. |
| **Slow (across-session)** | Graphed CBM-equivalent probe scores vs. goal line | 4 points minimum; 7–10 weeks for trend-based judgement | **Change the method.** Fire the DBI adaptation step. Log it. |

`INFERENCE` — synthesised from Fuchs et al. 1991 (change must be principled),
Van Norman et al. 2023 (trend latency), Swanson & Hoskyn 1998 (controlling task
difficulty is a within-session lever), and Stockard et al. 2018 (dosage/consolidation).

**What to pivot *to*, and in what order.** Drawn from the components with the largest
independent effect estimates:

1. **Reduce granularity** — segment the task further (Swanson & Sachse-Lee 2000:
   segmentation carries significant variance).
2. **Add a worked example / explicit model** before requiring production (Swanson &
   Hoskyn 1998: explicit skill modelling).
3. **Change representation along the concreteness ladder** — concrete → pictorial →
   abstract, faded (Fyfe, McNeil, Son & Goldstone 2014,
   https://doi.org/10.1007/s10648-014-9249-3).
4. **Drop to the prerequisite skill** and re-teach it (diagnostic assessment; DBI step 3).
5. **Change modality** to remove a non-target load (text-to-speech, speech-to-text).
6. **Increase dosage / distributed review** before concluding non-response (Stockard
   et al. 2018 dosage effect).
7. **Escalate to a human.** Non-negotiable stopping rule — see §6.

### 1.5 Mathematics and dyscalculia

**Gersten, Chard, Jayanthi, Baker, Morphy & Flojo (2009), *RER*.** 42 RCT and
quasi-experimental interventions for students with learning disabilities. All
instructional components produced significant mean effects ranging **0.21 to 1.56**,
*except* student feedback with goal-setting and within-class peer-assisted learning. In
hierarchical regressions, **two components provided practically and statistically
important increases in effect size: teaching students to use heuristics, and explicit
instruction.**
`MEASURED-META` — https://doi.org/10.3102/0034654309334431

**Jitendra, Lein, Im, Alghamdi, Hefte & Mouanoutoua (2017), *Exceptional Children*.**
Secondary students with LD/mathematics difficulties; 19 studies, 20 independent samples,
treatment–control designs. **g = 0.37, 95% CI [0.18, 0.56]. Instructional time moderated
the effect.**
`MEASURED-META` — https://doi.org/10.1177/0014402917737467

**Lein, Jitendra & Harwell (2020), *JEP*.** Word-problem-solving interventions for
students with LD/MD — the specific area where language load and mathematics load
interact.
`MEASURED-META` — https://doi.org/10.1037/edu0000453

**Early markers (Gersten, Jordan & Flojo 2005).** Valid kindergarten indicators of later
mathematics difficulty: magnitude comparison, sophistication of counting strategies,
fluent number identification, and **working memory (reverse digit span)**. Also: "almost
all students with MD demonstrate problems with accurate and automatic retrieval of basic
arithmetic combinations," and mathematics difficulties are **not stable over time for
many children** — a direct warning against early labelling.
`MEASURED-META` / `OBSERVED` — https://doi.org/10.1177/00222194050380040301

**Design consequences.** (a) Explicit instruction and taught heuristics are the
highest-yield levers — the same answer as reading. (b) Instructional *time* moderates
outcomes; dosage is again the scalable variable. (c) Retrieval of basic facts is a
distinct bottleneck requiring distributed practice (links to F11), not more conceptual
explanation. (d) Because MD is unstable in young children, screening signals must never
become labels (§6).

### 1.6 ADHD and executive function

**Mechanism (Barkley 1997, *Psychological Bulletin*, ~5,300 citations).** Behavioural
inhibition is the primary deficit; it gates four executive functions (nonverbal working
memory, internalised speech, self-regulation of affect/motivation/arousal,
reconstitution), which in turn govern motor control toward goals. ADHD is a disorder of
*performance*, not of *knowledge* — a child can know what to do and not do it.
`OBSERVED` (theoretical synthesis of a large empirical base) —
https://doi.org/10.1037/0033-2909.121.1.65

**Consensus base (Faraone et al. 2021, World Federation of ADHD International Consensus
Statement).** 208 evidence-based conclusions.
`MEASURED-META` — https://doi.org/10.1016/j.neubiorev.2021.01.022

**School-based interventions (DuPaul, Eckert & Vilardo 2012, *School Psychology
Review*).** Meta-analysis 1996–2010 of school-based interventions for ADHD, reporting
effects across contingency management, academic interventions, and cognitive-behavioural
approaches, with academic/instructional modifications showing meaningful academic
benefit.
`MEASURED-META` — https://doi.org/10.1080/02796015.2012.12087496

**F10 — the negative result that redirects the design (Melby-Lervåg, Redick & Hulme
2016, *Perspectives on Psychological Science*).** 87 publications, 145 experimental
comparisons of working-memory training.

> "Immediately following training there were reliable improvements on measures of
> intermediate transfer (verbal and visuospatial working memory). For measures of **far
> transfer (nonverbal ability, verbal ability, word decoding, reading comprehension,
> arithmetic) there was no convincing evidence of any reliable improvements** when
> working memory training was compared with a treated control condition."

`MEASURED-META` — https://doi.org/10.1177/1745691616635612 · earlier:
https://doi.org/10.1037/a0028228 · specific to ADHD/learning disorders:
https://doi.org/10.1521/adhd.2013.21.2.1

Corroborated for ADHD specifically by Westwood et al. (2023, *Molecular Psychiatry*),
a meta-analysis of computerised cognitive training RCTs with **blinded and objective
outcomes** — the design that removes the expectancy inflation which powers most
brain-training claims. https://doi.org/10.1038/s41380-023-02000-7 `MEASURED-META`

**Design consequence, stated as a prohibition.** Do not build a working-memory trainer.
Do not build an "attention trainer." Do not sell cognitive remediation. **Externalise
the load instead:** persistent visible steps, no "remember what we said earlier,"
worked examples on screen, state held by the system rather than the child. The
capacity is not trainable; the demand is designable.

### 1.7 AAC and assistive technology

**AAC does not suppress speech (Millar, Light & Schlosser 2006, *JSLHR*).** The single
most consequential finding in AAC, because the opposite belief delays intervention for
years. 23 studies, 67 individuals; 6 studies / 27 cases met best-evidence criteria.

> "**None** of the 27 cases demonstrated decreases in speech production as a result of
> AAC intervention, 11% showed no change, and the majority (**89%**) demonstrated gains
> in speech."

Gains were modest and likely underestimated due to ceiling effects. Evidence quality is
the weak point: 17 of 23 studies did not establish experimental control.
`MEASURED-META` (best-evidence synthesis; small-*n* single-subject base) —
https://doi.org/10.1044/1092-4388(2006/021)

Related: Schlosser & Lee (2000) on generalisation and maintenance in AAC,
https://doi.org/10.1080/07434610012331279074 `MEASURED-META`; Schlosser &
Raghavendra (2004) on evidence-based practice in AAC,
https://doi.org/10.1080/07434610310001621083 `OBSERVED`.

**Text-to-speech (Wood, Moxley, Tighe & Wagner 2018, *JLD*).** Meta-analysis of TTS and
read-aloud tools for students with reading difficulties: **average weighted d = 0.35,
95% CI [0.14, 0.56], p < .01.** Study design moderated the effect. Authors' caution:
"more studies are needed to further explore the moderating variables."
`MEASURED-META` — https://doi.org/10.1177/0022219416688170

**Design consequence.** TTS is a genuine but *modest* effect, and it is the mechanism
that decouples reading difficulty from concept difficulty. It should be a default
capability, not a flagged accommodation — but the system should not claim it is
transformative. `INFERENCE`

### 1.8 Null and negative results ledger

The editorial standard requires ≥1. This section has ten, and they are load-bearing:

| # | Null / negative | Source |
|---|---|---|
| N1 | Orton-Gillingham: **non-significant** vs. comparison instruction on both foundational skills (p=.40) and comprehension (p=.59) | Stevens et al. 2021 |
| N2 | RTI at scale: **negative** Grade-1 impact at the intervention threshold; null in Grades 2–3 | Balu et al. 2015 |
| N3 | CBM **without** an instructional-recommendation component: more program changes, **no achievement gain** | Fuchs, Hamlett & Stecker 1991 |
| N4 | Working-memory training: **no far transfer** to reading, arithmetic, or ability | Melby-Lervåg, Redick & Hulme 2016 |
| N5 | Phonics "did not help low achieving readers that included students with cognitive limitations" | Ehri et al. 2001 |
| N6 | In RCT-only synthesis, **every** non-phonics treatment family (auditory training, coloured overlays/lenses, motor exercises, "sunflower therapy") was non-significant | Galuschka et al. 2014 |
| N7 | UDL: "the impact on educational outcomes has not been demonstrated" | Capp 2017 |
| N8 | UDL: "no rigorous published research has demonstrated any improvement" | Murphy 2020 |
| N9 | LLMs: **no effect** on overall learning outcomes in two pre-registered, incentivised lab experiments | Lehmann, Cornelius & Sting 2024 |
| N10 | Generative AI without guardrails: students performed **17% worse** than never-had-access controls once the tool was removed | Bastani et al. 2025, PNAS |
| N11 | Student feedback with goal-setting, and within-class peer-assisted learning, were the **only** math components *not* producing significant effects | Gersten et al. 2009 |

---

## 2. Universal Design for Learning — report it honestly

UDL (CAST) organises instruction around three principles — multiple means of
**engagement**, **representation**, and **action & expression** — with a stated
neuroscientific rationale (affective, recognition, and strategic networks).

**The question the section must answer: is UDL evidence-based?**

**Answer: no, not as a framework. Yes, as a bag of individually-evidenced parts.** This
distinction is the whole finding.

**Capp (2017), *International Journal of Inclusive Education*** — the most-cited UDL
meta-analysis (399 citations). 18 empirical pre/post studies, 2013–2016. Conclusion,
verbatim:

> "Results from this analysis suggest that UDL is an effective teaching methodology for
> improving the learning **process** for all students. **The impact on educational
> outcomes has not been demonstrated.**"

`MEASURED-META` — https://doi.org/10.1080/13603116.2017.1325074

**Murphy (2020), *Policy Futures in Education*** — the sharpest critique:

> "While the rhetoric is promising, **no rigorous published research has demonstrated
> any improvement in an education intervention designed with UDL principles in mind.**
> Furthermore, the community of practice around UDL appears to be **hostile to questions
> around the rigor of analysis** used to promote UDL interventions. Studies of UDL
> approaches do not follow best practices in terms of research design, and often solicit
> anecdotes rather than testing the effectiveness of the approach. … **the only
> evidence-based conclusion that can be made about UDL is that further study is
> required.**"

`OBSERVED` (systematic policy review) — https://doi.org/10.1177/1478210320940206

**Boysen (2021), *Scholarship of Teaching and Learning in Psychology*** — "Lessons (not)
learned: the troubling similarities between learning styles and universal design for
learning." The parallel drawn is structural: an intuitively appealing framework, a
neuroscience-flavoured rationale, enormous institutional uptake, and a thin evidence
base that its advocates do not press on. Given that this survey has already ruled
learning-styles matching out of scope (CLAUDE.md §3), consistency demands the same
scepticism be applied here.
`OBSERVED` — https://doi.org/10.1037/stl0000280

**Al-Meqdad, Alodat, Alquraan, Mohaidat & Al-Makhzoomy (2023), *Cogent Education*** —
13 studies, 2015–2021. Reports "total effect sizes for the identified studies were
**3.56**; however, **considerable heterogeneity** was evident," with significant effects
found specifically for **one-group** studies. An aggregate effect of *d* ≈ 3.6 from
predominantly single-group pre-post designs is not a finding; it is a diagnostic of
the design. Report it as evidence of the field's methodological weakness, **never** as
evidence that UDL works.
`MEASURED-META` (methodologically unsound; cite as counter-example) —
https://doi.org/10.1080/2331186x.2023.2218191

**Zhang, Carter, Greene & Bernacki (2024), *Educational Psychology Review*** —
systematic review of UDL implementation challenges, documenting inconsistent
operationalisation across studies. If the treatment is not consistently defined, no
meta-analysis of it can be interpreted.
`OBSERVED` — https://doi.org/10.1007/s10648-024-09860-7

**Bray, Devitt & Banks (2023), *BJET*** — systematic review of technology in
second-level UDL implementations.
`OBSERVED` — https://doi.org/10.1111/bjet.13328

### 2.1 How the survey should restate the thesis

The PRD's mapping table is the correct argument and it does **not** depend on UDL being
evidence-based. Each row is independently supported:

| SELPA accommodation | Mainstream principle | Independent evidence |
|---|---|---|
| Multiple representations | Mayer multimedia; Ainsworth DeFT | `MEASURED-META` (B1) |
| Extended time / self-pacing | Mastery learning | `MEASURED-META` (B1) |
| Reduced distraction | Coherence principle; extraneous load | `MEASURED-META` (B1) |
| TTS / STT | Modality principle; decoding-load removal | **d = 0.35**, Wood et al. 2018 |
| Explicit systematic instruction | Direct instruction; worked examples | **~4,000 effects**, Stockard 2018; **M = 0.79**, Swanson & Hoskyn 1998 |
| Chunking & fading scaffolds | Segmenting; scaffold–fade | Swanson & Sachse-Lee 2000; Fyfe et al. 2014 |
| Frequent low-stakes checks | Retrieval practice; formative assessment | **ES = 0.70**, Fuchs & Fuchs 1986 |

**Therefore: keep the practice, drop the branding.** The correct claim in the paper is:

> *"Every core SELPA accommodation is independently evidenced as a mainstream learning
> principle. That convergence — not the UDL framework's own empirical record — is what
> licenses the curb-cut argument. UDL is a useful organising vocabulary and an unproven
> intervention; the survey adopts the first and declines the second."*

`INFERENCE` — and it is a stronger argument than the one it replaces, because it rests
on Stockard, Swanson, Fuchs, and Mayer rather than on CAST.

**A note on the curb-cut effect itself.** The curb-cut analogy is a genuine historical
observation (kerb ramps mandated for wheelchair users are used far more by people with
strollers, luggage, and delivery carts) but it is an *analogy*, not evidence about
instruction. Use it rhetorically; do not cite it as data. `INFERENCE`

---

## 3. THE CRITICAL QUESTION — has AI tutoring been evaluated on students with disabilities?

This was the PRD's stated open question: *"does AI tutoring actually help students with
disabilities, or has it only been measured on typical learners? Find the evidence; if it
is thin, say so — that gap is itself a finding, and arguably the most important one in
the survey."*

**The evidence is not thin. It is, for randomised designs, absent.**

### 3.1 A reproducible census

Run against live APIs on **2026-07-27**. Exact query strings given so this is
replicable and falsifiable.

**Europe PMC REST API** (`https://www.ebi.ac.uk/europepmc/webservices/rest/search`):

| Query | Hits |
|---|---|
| `ABSTRACT:"randomized controlled trial"` *(calibration)* | **100,478** |
| `ABSTRACT:"AI tutor"` | 46 |
| `ABSTRACT:"AI tutor" AND ABSTRACT:"randomized"` | 4 |
| `(ABSTRACT:"generative AI" OR ABSTRACT:"ChatGPT" OR ABSTRACT:"large language model") AND ABSTRACT:"randomized controlled trial" AND ABSTRACT:"students"` | **30** |
| …**the same query plus** `AND (ABSTRACT:"disability" OR "disabilities" OR "dyslexia" OR "ADHD" OR "autism" OR "special education" OR "IEP")` | **0** |
| `ABSTRACT:"intelligent tutoring" AND (ABSTRACT:"learning disabilities" OR ABSTRACT:"special education")` | 1 |
| …`AND ABSTRACT:"randomized"` | **0** |
| `(GenAI/ChatGPT/LLM) AND ABSTRACT:"special education"` | 6 |
| `(GenAI/ChatGPT/LLM) AND ABSTRACT:"autism"` | 35 |
| …`AND ABSTRACT:"randomized controlled trial"` | **0** |
| `(GenAI/ChatGPT/LLM) AND ABSTRACT:"ADHD"` | 16 |

**ERIC API** (`https://api.ies.ed.gov/eric/`) — the education-specific database, so a
null here is the stronger result:

| Query | Records |
|---|---|
| `("artificial intelligence") AND (education)` *(calibration)* | **24,169** |
| `("generative artificial intelligence") AND (education)` | **922** |
| `("generative artificial intelligence") AND ("students with disabilities")` | **3** |
| …`AND ("randomized controlled trial")` | **0** |
| `("intelligent tutoring") AND ("students with disabilities")` | 20 |
| …`AND (randomized)` | **0** |
| `(ChatGPT) AND ("special education")` | 19 |
| …`AND (randomized)` | **0** |
| `(ChatGPT) AND (dyslexia)` | 2 |
| `("artificial intelligence") AND ("individualized education program")` | 5 |

`MEASURED-BENCH` (own census; method stated, reproducible, and limited to
abstract/keyword indexing — a study reporting a disability subgroup only in its results
section would be missed).

### 3.2 What the 19 ChatGPT × special-education records actually are

Inspected individually. They comprise:

- **IEP-drafting studies** ("Chatting with GPT: Enhancing IEP Goal Development for Novice
  Special Education Teachers," *JSET* 2023; "IEPs in the Age of AI," *JSET* 2026;
  "Enhancing IEP Goal Development for Preschoolers with Autism," *JADD* 2026)
- **Teacher-workload studies** ("Using AI to Support Special Education Teacher Workload,"
  *JSET* 2024)
- **Teacher-preparation and TPACK studies** (several, *Journal of Special Education
  Preparation*)
- **Perception / self-efficacy surveys** of pre-service and in-service teachers
- **Bias audits** ("'Exceptional Talent and Enthusiasm for Math': An Examination of
  Storylines Circulated by ChatGPT about Mathematical Learners")
- **Practice essays and prompt-engineering guides**

**The finding:** AI in special education is currently a **teacher-productivity
literature, not a student-outcomes literature.** Not one of the 19 is a controlled
evaluation of a child's learning. `OBSERVED` (own coding of the ERIC result set)

The three GenAI × "students with disabilities" records are: semi-structured interviews
with disabled university students (*Educ Inf Technol* 2025); a design paper for a
dyslexia AR/GenAI reading tool (*IJTES* 2025); and an Australian secondary-school case
study of learner agency (*BJET* 2026). All qualitative or design-descriptive.
`OBSERVED`

### 3.3 The one systematic review that exists, and what it shows

**Paglialunga & Melogno (2025), "The Effectiveness of Artificial Intelligence-Based
Interventions for Students with Learning Disabilities: A Systematic Review,"
*Brain Sciences* 15(8):806.** PRISMA, PICOS, seven databases (Google Scholar,
ScienceDirect, APA PsycInfo, ERIC, Scopus, PubMed), 2022–2025, formal risk-of-bias
assessment with ROBINS-I and JBI.

**Result: 11 studies, 10 independent experiments, 3,033 participants.** That is the
world literature.

| Study | Design | n | AI type |
|---|---|---|---|
| Zingoni et al. 2024 (IT) | Descriptive / case series | 50 + 100 | Recommender + VR |
| Ayasrah et al. 2024 (JO) | Single-group pre-post | 15 | Gesture-based games |
| Morciano et al. 2024 (IT) | Algorithm dev / quasi-exp | 50 | Recommender |
| **Gharaibeh et al. 2025 (AE)** | **Quasi-experimental / RCT-adjacent** | **60** | **ChatGPT** |
| Wang et al. 2022 | Quasi-experimental | 20 datasets | AI-augmented AAC |
| Hany et al. 2024 | Descriptive / case series | 392 | DALL·E + Google Voice |
| Sukasih et al. 2024 (ID) | Quasi-exp pre-post | 40 | Game-based AI |
| **Rizos et al. 2024 (GR)** | **Case study** | **2** | **ChatGPT 3.5** |
| Chukwuemeka & Agbarakwe 2024 (NG) | Quasi-experimental | 205 | Speechify (TTS) |
| Samuelsson 2023 (SE) | Quasi-experimental | 1,006 (246 MLD) | Personalised arithmetic |
| Fami et al. 2024 (IR) | Single-subject A-B-A | 6 | Cognitive program |

Risk of bias, verbatim:

> "**No studies were rated as having a 'Low' risk of bias.** The majority of studies
> (70%, n = 7) were assessed as having a 'Moderate' risk of bias. Three studies (30%)
> were rated as 'High' risk."

> "The most common methodological limitations identified were the **lack of appropriate
> randomization**, inadequate blinding of participants or outcome assessors, and the
> **absence of a control group** in several studies."

And the tell:

> "**All 11 studies reported positive outcomes.**"

Eleven for eleven, with zero low-risk-of-bias studies, is the canonical signature of
publication bias plus researcher-allegiance effects. The reported effect sizes are
correspondingly implausible: arithmetic fluency **d = 1.63**, reading comprehension
**d = −1.66** (sign convention favouring treatment). For calibration, the entire
half-century Direct Instruction literature averages "moderate to large."

The authors' own conclusion:

> "Future research **must prioritize high-quality randomized controlled trials (RCTs)**
> and longitudinal assessments to establish a definitive evidence base."

`MEASURED-META` — https://doi.org/10.3390/brainsci15080806 ·
https://pmc.ncbi.nlm.nih.gov/articles/PMC12385150/

**Only three of eleven used generative AI at all**, and one of those had **n = 2**.

**Their cognitive-offloading warning deserves quotation in the survey**, because it is
the mechanism by which an AI tutor could specifically harm this population:

> "This phenomenon, where learners become dependent on technology to perform tasks
> rather than developing the underlying cognitive skills, is a major concern,
> **particularly for students with learning disabilities who need to strengthen, not
> bypass, their cognitive functions**."

> "Students using AI for math practice answered more problems correctly but scored lower
> on conceptual understanding tests, suggesting that AI may enhance procedural skills
> without fostering deeper learning."

### 3.4 The flagship AI-tutoring RCTs, audited for disability reporting

I downloaded the full texts and grepped them. This is primary evidence, not inference.

**Kestin, Miller, Klales, Milbourne & Ponti — "AI Tutoring Outperforms Active
Learning."** Randomised, in-class, N = 194 (pre-test N = 316 combined), Harvard
undergraduate physics (PS2), weeks 9–10. AI group median post-score 4.5 vs 3.5 for the
active-lecture group; learning gains "over double." Effect size **0.63** by linear
regression, **0.73–1.3 SD** by quantile regression correcting for ceiling. Median time
on task **49 minutes (AI)** vs **60 minutes (lecture)**.

**Disability reporting: none.** Full-text search for `disabilit|accommodat|IEP|accessib|
dyslex|ADHD|special education|neurodiver` returns **six hits, all on the string
"accessible," and every one of them means "available at low cost / anywhere with an
internet connection"** — "widely accessible AI-powered pedagogy," "broadly accessible,"
"globally accessible," "accessible to any environment with an internet connection." The
word *accessibility* never appears in its disability sense. There is no disability
subgroup, no accommodation reporting, no accessibility conformance statement.
`MEASURED-RCT` for the effect; `OBSERVED` (own full-text audit) for the gap.
Preprint: https://doi.org/10.21203/rs.3.rs-4243877/v1 · published:
https://doi.org/10.1038/s41598-025-97652-6

**Wang, Ribeiro, Robinson et al. — "Tutor CoPilot."** Human–AI system for real-time
tutor support. Students of treatment tutors were **4 percentage points** more likely to
master topics (p < .01); students of the **lowest-rated tutors gained 9 p.p.** — a
genuinely equity-positive heterogeneity result.

**Disability reporting: one mention, as a control variable.** Verbatim: *"The student
covariates include categorical indicators for the student's gender, race, free and
reduced lunch, **special education**, and limited English proficiency, as well as a
continuous variable of the student's pre-study MAP math score."* Special-education
status is adjusted *for*; no subgroup effect on it is reported.
`MEASURED-RCT` / `OBSERVED` (own full-text audit) — https://arxiv.org/abs/2410.03017

**De Simone, Tiberti, Barron Rodriguez et al. (2025), World Bank — Nigeria.** RCT,
first-year senior secondary, Microsoft Copilot (GPT-4), six weeks. **+0.31 SD** overall,
**+0.23 SD** on English. Cost-effectiveness equivalent to 1.5–2 years of
business-as-usual schooling. Heterogeneity: benefits across the ability distribution,
but **"the largest effects are for female students, and those with higher initial
academic performance."** No disability analysis.
`MEASURED-RCT` — https://doi.org/10.1596/1813-9450-11125

**Bastani, Bastani, Sungu, Ge, Kabakcı & Mariman (2025), PNAS.** ~1,000 Turkish high
school maths students. GPT Base **+48%** and GPT Tutor **+127%** on grades *with* access;
but **once access was removed, GPT Base students scored 17% worse than students who
never had access.** Guardrails largely mitigated the harm. No disability analysis.
`MEASURED-RCT` — https://doi.org/10.1073/pnas.2422633122

**Lehmann, Cornelius & Sting (2024), arXiv 2409.09047.** Two pre-registered, incentivised
lab experiments plus a field study. **No effect of LLMs on overall learning outcomes.**
Behaviourally: students who **substitute** learning activities with LLMs increase topic
volume but decrease per-topic understanding; students who **complement** (ask for
explanations) increase understanding without increasing volume. And: **"LLMs widen the
gap between students with low and high prior knowledge."** No disability analysis.
`MEASURED-RCT` — https://arxiv.org/abs/2409.09047 · https://doi.org/10.2139/ssrn.4941259

**One forward-looking signal.** *"Reinforcement Learning for Special Education: Aligning
LLM Tutors to Diverse Learners through Disability-Adaptive Training"* (arXiv 2605.30670,
2026-05-29) opens by stating that "research on aligning [LLM tutors] for special
education **remains absent**," and that prior RL-for-tutoring work "target[s] a generic
learner in a single domain (mathematics)." An independent confirmation of this section's
census, from inside the ML community.
`OBSERVED` (preprint, not peer-reviewed, no student outcomes) —
https://arxiv.org/abs/2605.30670

### 3.5 What the gap means — stated carefully

**What we can say:** as of July 2026, no randomised controlled trial of generative-AI
tutoring on students with disabilities is indexed in ERIC or Europe PMC. The
non-randomised literature is eleven studies, none at low risk of bias, all reporting
positive results.

**What we cannot say:** that AI tutoring *doesn't* work for these students. Absence of
evidence is not evidence of absence, and the mechanistic case is genuinely strong —
infinite patience, unlimited repetition without visible exasperation, no social cost to
asking the same question a ninth time, on-demand re-representation, and dosage
unconstrained by staffing ratio. Every one of those maps onto a component that Swanson,
Stockard, and Gersten found to carry effect-size variance.

**What follows for a builder:**

1. **Every efficacy claim currently made about AI tutoring is a claim about typical
   learners.** Kestin's population was Harvard physics undergraduates. Do not transfer
   those effect sizes to a SELPA student. Say so in the paper.
2. **The expected direction of transfer is negative, not neutral.** Two independent
   findings — Lehmann's gap-widening and Nigeria's larger effects for higher-performing
   students — say the benefit correlates with prior knowledge. Extrapolating a
   typical-learner effect size to a low-prior-knowledge learner is extrapolating in the
   wrong direction.
3. **This is the survey's most defensible original contribution.** A quantified,
   reproducible census showing zero RCTs, with query strings published, is a stronger
   claim than any of the pedagogy in the rest of the paper.
4. **It is also a research agenda.** The single highest-value study anyone could run in
   this field is a properly powered RCT of an LLM tutor with students on IEPs, with
   CBM-equivalent progress monitoring and a documented decision rule.

---

## 4. The archetypes

Per the PRD: each names a **mechanism**, a **design consequence**, and a **failure mode
if ignored**. Evidence attached to each. **They co-occur** — ADHD with working-memory
limits and a history of failure is the modal case, not the edge case, and the system
must *compose* accommodations rather than select one.

### 4.1 Attention / ADHD — executive function

- **Mechanism.** Behavioural inhibition is the primary deficit; it gates working memory,
  internalised speech, affect regulation, and reconstitution (Barkley 1997). ADHD is a
  disorder of *performance*, not of *knowledge*. Sustained attention collapses long
  before comprehension does.
  `OBSERVED` — https://doi.org/10.1037/0033-2909.121.1.65
- **Design consequence.** Short segments; one idea per screen; ruthless removal of
  decorative content (coherence principle); immediate feedback; scheduled movement and
  breaks; novelty deployed deliberately rather than continuously. **Do not build a
  working-memory or attention trainer** (Melby-Lervåg et al. 2016; Westwood et al. 2023).
- **Failure mode if ignored.** A long unbroken explanation. The child disengages, and —
  the specific danger for an instrumented system — **the telemetry reads disengagement
  as inability and updates the learner model downward.** A performance deficit gets
  encoded as a knowledge deficit, and the system then teaches the wrong thing.
  `INFERENCE`

### 4.2 Working-memory limitation

- **Mechanism.** WM capacity is the bottleneck. Instructions holding 3+ steps fail before
  reasoning begins. This is the direct mechanism in Kirschner/Sweller/Clark's argument
  against minimal guidance, and reverse digit span is a validated early predictor of
  mathematics difficulty (Gersten, Jordan & Flojo 2005).
- **Design consequence.** **Externalise memory.** Visible persistent steps, worked
  examples that stay on screen, scaffolds that hold state, never "remember what we said
  earlier." Control task difficulty explicitly — one of only three significant
  effect-size predictors in Swanson & Hoskyn (1998).
- **Failure mode if ignored.** Multi-step verbal instruction. It presents as a reasoning
  failure and is actually a storage failure, and every downstream inference is wrong.
- **Prohibition.** Training the capacity does not work (N4). Designing the demand does.

### 4.3 Long-term retention difficulty

- **Mechanism.** Encoding and consolidation, not comprehension. The child understood it,
  and it decayed.
- **Design consequence.** Scheduled retrieval (survey §F11) is **mandatory, not
  optional**; overlearning; re-teach cycles planned from day one rather than triggered by
  failure. Distributed practice is specifically indicated for automatic retrieval of
  basic arithmetic facts, which "almost all students with MD" struggle with (Gersten,
  Jordan & Flojo 2005). Direct-instruction effects showed "little decline during
  maintenance" *and* grew with exposure (Stockard et al. 2018) — dosage is the lever.
- **Failure mode if ignored.** Teach once and move on. The curriculum advances; the child
  does not; the gap compounds silently.

### 4.4 Reasoning / abstraction gaps

- **Mechanism.** Abstraction without a concrete anchor has nothing to attach to. Schema
  formation requires guidance when long-term memory has no relevant structures
  (Kirschner, Sweller & Clark 2006).
- **Design consequence.** **Explicit instruction over discovery** — the largest and most
  replicated finding in the section (Stockard 2018; Swanson & Hoskyn 1998; Gersten 2009).
  Concreteness fading: concrete → pictorial → abstract, with the fade itself doing the
  work (Fyfe, McNeil, Son & Goldstone 2014,
  https://doi.org/10.1007/s10648-014-9249-3; McNeil & Fyfe 2012,
  https://doi.org/10.1016/j.learninstruc.2012.05.001). Never start at the formal level.
- **Failure mode if ignored.** Discovery learning. Actively harmful here, and this is
  well replicated. See §5.

### 4.5 Processing speed

- **Mechanism.** Slower is not less able. A timed task measures speed; it does not
  measure knowledge. Naming speed is one of the strongest predictors of intervention
  non-response (Al Otaiba & Fuchs 2006) — meaning slow processing is a *reason to change
  method*, never a reason to lower expectations.
- **Design consequence.** **Untimed by default.** Measure mastery, never rate. Where
  fluency genuinely is the construct (oral reading rate, arithmetic-fact retrieval),
  measure it explicitly and separately, and never let it contaminate a conceptual
  assessment. Latency may be used as a *fast-clock signal* for scaffolding, but must
  never enter a mastery judgement.
  `INFERENCE`
- **Failure mode if ignored.** Timed drills. They measure the disability, not the
  learning — and then the learner model records the disability as a knowledge gap.

### 4.6 Language / reading access

- **Mechanism.** Decoding load consumes the capacity needed for meaning. The Simple View
  of Reading: comprehension = decoding × language comprehension; if decoding is
  effortful, nothing is left.
- **Design consequence.** Text-to-speech (**d = 0.35**, Wood et al. 2018) and
  speech-to-text as **defaults**, not flagged accommodations. Dual-coded content.
  Deliberately **decouple reading difficulty from concept difficulty** — assess the
  physics, not the paragraph. For non-speaking learners, AAC with the settled finding
  that it does **not** suppress speech (89% of rigorously-evaluated cases gained speech;
  0% lost it — Millar, Light & Schlosser 2006).
- **Failure mode if ignored.** Assessing physics through a reading test. This is the
  single most common measurement error in special education and the easiest for an
  LLM-based system to reproduce at scale, because LLM tutors are text-first by
  construction.

### 4.7 Anxiety / learned helplessness

- **Mechanism.** A prior failure history is itself a barrier; errors are threatening.
  Anxiety consumes working memory directly — meta-analytically, math anxiety correlates
  with performance at **r = −0.168** across 57 studies / 150 effect sizes, with working
  memory as a mediating pathway (Finell, Sammallahti, Korhonen & Eklöf 2022,
  https://doi.org/10.3389/fpsyg.2021.798090). `MEASURED-META`
- **Design consequence.** Low-stakes everything. Visible **personal** growth curve — the
  open learner model as *my progress*, never as a verdict, never a comparison. Errors
  framed as information. CBM was designed to be non-punitive by construction (Deno 1985);
  preserve that property.
- **Failure mode if ignored.** High-frequency graded testing. It demoralises exactly the
  child it was meant to help — and note the trap: the retrieval-practice literature says
  test frequently, so a naive reading of learning science produces this failure directly.
  The reconciliation is that retrieval practice requires *frequency*, not *stakes*.
  `INFERENCE`

### 4.8 Co-occurrence — the composition requirement

The archetypes are not a menu. Comorbidity is the norm: reading difficulty predicts
slower mathematics progress (Gersten, Jordan & Flojo 2005); the non-responder profile in
Al Otaiba & Fuchs (2006) combined naming speed, vocabulary, sentence imitation, **and
problem behaviour**; anxiety consumes the working memory that is already scarce.

**Architectural consequence:** accommodations must **compose**, and composition can
conflict. Segmentation for working memory increases the number of steps, which taxes
sustained attention. TTS removes decoding load but adds a temporal, non-reviewable
channel that is harder on working memory than static text. Reducing stimulation for
attention can remove the dual coding that language access requires. **The system needs
an explicit conflict-resolution policy over accommodations, not an additive stack of
toggles** — and this is a genuine open design problem that the literature does not
answer. `INFERENCE` — flagged for G4 (research agenda).

---

## 5. Where this survey's own advice inverts

Stated explicitly so the paper does not contradict itself.

| General claim (elsewhere in this survey) | For this population | Evidence |
|---|---|---|
| Productive failure; desirable difficulties | **Explicit instruction wins.** Struggle that is productive for a typical learner is often just failure here. | Swanson & Hoskyn 1998 (M=0.79, direct+strategy beats competing models); Stockard 2018 |
| Discovery and exploration | **Guided, worked, faded.** | Kirschner/Sweller/Clark 2006; Gersten 2009 (explicit instruction one of only two components with practically important effect gains) |
| Frequent assessment is good | Only **low-stakes, brief, private, growth-framed**. | Fuchs & Fuchs 1986 (ES=0.70 for *formative* evaluation); Finell et al. 2022 (anxiety→WM→performance) |
| Reduce scaffolds as expertise grows | Fade **on evidence**, never on schedule; restore without treating restoration as regression. | Expertise-reversal effect (Kalyuga & Sweller) — note it is *reversal*, i.e. the optimum genuinely moves; Van Norman et al. 2023 (7–10 weeks before a trend judgement is reliable) |
| More learner control / agency is good | **Bounded choice.** Substitution behaviour, not tool access, drives LLM harm. | Lehmann et al. 2024; Bastani et al. 2025 |

### 5.1 Why the inversion is principled rather than special-pleading

The inversion is not "these children are different, so the science doesn't apply." It is
the **expertise-reversal effect applied at the low end of the prior-knowledge scale.**
Cognitive load theory predicts that the optimal level of guidance is a decreasing
function of prior knowledge. Desirable difficulties and productive failure are the
*high-prior-knowledge* branch of the same function. Explicit instruction is the
*low-prior-knowledge* branch. There is one theory, not two.

This is why the PRD's conclusion is right: *"A survey that gives one universal answer
here is wrong. The correct claim is that the mode must be selected per learner and per
moment — which is precisely what the bidirectional loop is for."*

**And it is why F5 matters so much.** If the mode must be selected per learner, then the
system's core competence is *selection*, and Fuchs, Hamlett & Stecker (1991) is the
proof that selection is the active ingredient while measurement alone is inert.

### 5.2 The strongest documented harm

The claim that "discovery learning is among the clearest documented harms" should be
stated at the strength the evidence supports, which is:

- In RCT-only synthesis restricted to diagnosed reading disability, **only** phonics
  instruction reached significance; every less-explicit alternative did not
  (Galuschka et al. 2014). `MEASURED-META`
- Across 328 DI studies, effects were positive and significant essentially without
  exception, and **grew with exposure** (Stockard et al. 2018). `MEASURED-META`
- Across 180 LD intervention studies, the models with explicit components outperformed
  competing models (Swanson & Hoskyn 1998). `MEASURED-META`

What is **not** available is a large body of RCTs directly randomising students with
disabilities to discovery vs. explicit instruction and measuring harm. The honest
formulation is: *"the explicit-instruction advantage in this population is very large
and very well replicated; direct head-to-head harm trials of discovery learning in
students with disabilities are ethically and practically rare, so the claim rests on the
consistency of the explicit-instruction advantage rather than on measured damage."*
`INFERENCE` — and this precision is worth keeping, because the overstated version is
easy to attack.

---

## 6. The legal and ethical floor

These are constraints, not features. A system that violates them has failed regardless of
its effect size.

### 6.1 IDEA — an IEP is legally binding and team-authored

**34 CFR §300.320** — an IEP "means a written statement for each child with a disability
that is **developed, reviewed, and revised in a meeting**," and must contain: present
levels of academic achievement and functional performance; **measurable** annual goals;
how progress will be measured and reported; special education, related services and
supplementary aids; explanation of any non-participation with non-disabled peers; testing
accommodations or alternate-assessment rationale; projected start date, frequency,
location and duration; transition services from age 16; and transfer of rights at
majority.
https://sites.ed.gov/idea/regs/b/d/300.320 `OBSERVED` (statutory)

**34 CFR §300.321(a)** — the IEP Team **must** include: (1) **the parents of the child**;
(2) not less than one regular education teacher (if the child is or may be in the regular
education environment); (3) not less than one special education teacher or provider;
(4) a public agency representative qualified to provide or supervise specially designed
instruction and knowledgeable about the general curriculum and agency resources; (5) an
individual who can interpret the instructional implications of evaluation results;
(6) at the discretion of parent or agency, others with knowledge or expertise; and
(7) **whenever appropriate, the child with a disability.**
https://sites.ed.gov/idea/regs/b/d/300.321 `OBSERVED` (statutory)

**The bright line.** An AI may **draft** goal language, **summarise** progress data,
**surface** trends, **prepare** materials, and **check** goals for measurability. An AI
may **not** author the IEP, decide eligibility, set the placement, or substitute for the
team meeting. The statute locates authority in a meeting of named humans including the
parent. Any product claiming to "generate your child's IEP" is describing a legal
failure.

Note the practical tension: the ERIC census (§3.2) shows that **IEP goal drafting is the
single most-published AI application in special education**. It is also the application
closest to the legal line. The correct posture is *AI drafts, team authors, and the
provenance of every clause is visible.* `INFERENCE`

### 6.2 Section 504 of the Rehabilitation Act (29 U.S.C. §794; 34 CFR Part 104)

Prohibits disability discrimination in any programme or activity receiving federal
financial assistance, and requires equal access to educational opportunity. Broader
eligibility than IDEA (any substantially limiting impairment, no requirement of one of
IDEA's 13 categories) and no requirement of specially designed instruction — a 504 plan
provides accommodations. Many learners a product will serve have a 504 plan and no IEP.
https://www.ed.gov/laws-and-policy/individuals-disabilities/section-504
`OBSERVED` (statutory)

### 6.3 FERPA and data protection — disability status is elevated-sensitivity data

Education records are protected under FERPA (20 U.S.C. §1232g; 34 CFR Part 99); IDEA
adds its own confidentiality provisions at 34 CFR §§300.610–300.627; and under GDPR,
health/disability information is special-category data (Art. 9). Practical floor for this
system: **default to on-device or in-region processing; minimise collection; never train
foundation models on it; retain by default for the shortest period consistent with the
educational purpose; and make disability status non-derivable from exported artefacts.**

There is a specific and under-appreciated leak: a **learner model is a de facto
diagnostic record.** A stored profile reading "working-memory span 2, sustained attention
window 6 minutes, non-responsive to phonics after 10 weeks" is disability information
whether or not a diagnosis was ever entered. It must be governed as such.
`INFERENCE` — and this is a design requirement for F5 (learner model), not just a policy
note.

### 6.4 WCAG 2.2 Level AA — the accessibility floor

W3C Recommendation, 12 December 2024. https://www.w3.org/TR/WCAG22/ `OBSERVED`

New criteria over WCAG 2.1:

- **Level A:** 3.2.6 Consistent Help; 3.3.7 Redundant Entry
- **Level AA:** 2.4.11 Focus Not Obscured (Minimum); 2.5.7 Dragging Movements;
  2.5.8 Target Size (Minimum); **3.3.8 Accessible Authentication (Minimum)**
- **Level AAA:** 2.4.12 Focus Not Obscured (Enhanced); 2.4.13 Focus Appearance;
  3.3.9 Accessible Authentication (Enhanced)
- **Removed:** 4.1.1 Parsing

**Three of the 2.2 additions are aimed squarely at cognitive accessibility** and are
therefore directly on-thesis: 3.3.7 Redundant Entry (do not make the user re-supply
information — a memory-load requirement), 3.3.8 Accessible Authentication (authentication
must not depend on a cognitive function test — no puzzles, no transcription, no
remembered strings as the only path), and 3.2.6 Consistent Help. The floor now
explicitly includes the H1 population.

Operational floor for this project: keyboard-only operation; screen-reader correctness
including live regions for streamed model output; captions on all audio; **no
colour-only encoding**; respect `prefers-reduced-motion`; **no time limits by default**;
target sizes ≥24×24 CSS px; and — a requirement generic AI products routinely fail —
**streaming token output must not thrash a screen reader**, which means announcing
completed semantic units rather than every token.
`INFERENCE` from WCAG 2.2 + the archetypes.

### 6.5 No diagnosis, no labelling

Screening signals may be surfaced **to professionals**; the system must never label a
child. The strongest empirical support for this constraint is that mathematics
difficulties **"are not stable over time"** for many children (Gersten, Jordan & Flojo
2005) `MEASURED-META` — a label applied by a system at age 7 can outlive the condition it
described. The system's vocabulary should be about *this task, this week, this method's
response* — never about the child's category.

### 6.6 The AI-detector trap — a specific, foreseeable harm

Students taught formulaic structures **as an accommodation** — sentence frames, paragraph
templates, explicit organisational scaffolds, the exact practices Swanson & Hoskyn found
carry effect-size variance — produce writing that is low-perplexity, low-burstiness, and
structurally regular. That is precisely the signature GPT detectors classify as
machine-generated.

**Liang, Yuksekgonul, Mao, Wu & Zou (2023), *Patterns*** — "GPT detectors are biased
against non-native English writers." Detectors misclassified non-native writing at high
rates while classifying native writing accurately, and **simple prompting to enrich
vocabulary largely evaded detection** — i.e. the detectors key on linguistic
sophistication, not on provenance.
`MEASURED-BENCH` — https://doi.org/10.1016/j.patter.2023.100779 · replicated with
current models: https://doi.org/10.18653/v1/2026.eacl-srw.20

**The inference, stated as such:** the mechanism that produces false positives for
non-native writers — constrained, formulaic, low-variance prose — is the same mechanism
an explicit-instruction writing accommodation deliberately produces. **A student who
followed their IEP writing accommodation faithfully is at elevated risk of being accused
of cheating by an AI detector**, and the accusation is unfalsifiable from the artefact.
`INFERENCE` — Liang et al. did not test students with disabilities. **This is a
falsifiable, high-value, and to my knowledge un-run study, and the survey should propose
it explicitly** (see §8).

**Policy consequence:** any system in this space must (a) never rely on output-artefact
AI detection for students with accommodations; (b) prefer **process evidence** —
keystroke/revision history, in-session dialogue, oral defence — which is what F1
(assessment reconstruction) already argues for on independent grounds; and (c) treat a
detector flag on an accommodated student as evidence about the detector.

### 6.7 Not a domain for novel unvalidated pedagogy

Where decades of replicated intervention research exist, the AI's job is **fidelity and
dosage** — delivering known-good intervention at an intensity no staffing ratio can
afford — not invention. This constraint is now empirically grounded rather than merely
prudent: the DI dosage relationship (Stockard et al. 2018) says *more of the known-good
thing* is the highest-expected-value intervention available, while the AI evidence base
(§3) says novel AI pedagogy has essentially no outcome evidence in this population.
`INFERENCE`

---

## 7. The equity finding — why restraint matters more here

**Lehmann, Cornelius & Sting (2024).** Two pre-registered, incentivised laboratory
experiments plus a field study. Verbatim:

> "we find **no effect** of LLMs on overall learning outcomes. … Students who
> **substitute** some of their learning activities with LLMs (e.g., by generating
> solutions to exercises) increase the volume of topics they can learn about but
> **decrease their understanding** of each topic. Students who **complement** their
> learning activities with LLMs (e.g., by asking for explanations) do not increase topic
> volume but **do increase their understanding**. We also observe that **LLMs widen the
> gap between students with low and high prior knowledge.**"

`MEASURED-RCT` — https://arxiv.org/abs/2409.09047

**Why this compounds specifically for the H1 population.**

1. **Substitution is easier than complementation, and the gap is a substitution gap.**
   Asking a good clarifying question is a metacognitive skill. Pressing "solve this" is
   not. The learner who is least able to formulate a productive question is the learner
   most likely to substitute, and substitution is the branch that *reduces*
   understanding. The tool's benefit is gated on a skill that correlates with the deficit.
   `INFERENCE`
2. **It replicates in the field.** Nigeria: benefits across the ability distribution but
   **largest for students with higher initial academic performance**
   (De Simone et al. 2025). `MEASURED-RCT`
3. **It replicates as harm.** Bastani et al.: unguarded GPT access left students **17%
   worse** than never-having-access once the crutch was removed; guardrails largely
   eliminated the harm. `MEASURED-RCT`
4. **The systematic review of AI for LD independently flags the same mechanism.**
   Cognitive offloading is "a major concern, **particularly for students with learning
   disabilities who need to strengthen, not bypass, their cognitive functions**"
   (Paglialunga & Melogno 2025). `MEASURED-META`

**Four independent lines converging on one conclusion:** the harm channel is
*substitution*, and susceptibility to substitution is inversely related to prior
knowledge and metacognitive skill. This population sits at the maximum of that
susceptibility.

**The design conclusion is the opposite of the intuitive one.** The intuitive move —
"these students struggle, so give them more help and fewer restrictions" — is exactly the
unguarded-access condition that produced the 17% deficit. The correct move is that **the
SELPA build is the *most* constrained configuration, not the least.**

Concretely, and traceable to evidence:

| Constraint | Grounded in |
|---|---|
| Never emit a complete solution to an assigned task | Bastani (crutch), Lehmann (substitution) |
| Default to explanation, worked example, and next-step scaffold | Swanson & Hoskyn; Stockard |
| Withdrawal-of-tool performance is a first-class metric, not an afterthought | Bastani (the harm only appears at withdrawal) |
| Fade scaffolds **on evidence**, and restore without penalty | Expertise reversal; Van Norman (7–10 weeks) |
| Log substitution-vs-complementation behaviour and intervene on it | Lehmann |

**And the honest caveat.** Bastani's "GPT Tutor" guardrails largely eliminated the harm
for Turkish high-schoolers. Whether the same guardrails suffice for a student with
significant working-memory limits and a decade of failure history is **unknown and
untested.** That is F1 again.

---

## 8. What this section obliges the reference architecture (G2) to do

Design requirements, each traceable to a finding above. These are the section's output
into the agent-village design.

| # | Requirement | Traces to |
|---|---|---|
| R1 | **The pivot engine is the product.** Ship the instructional-recommendation component, not the dashboard. Measurement without a prescribed change is the condition that produced no gain. | F5 / Fuchs, Hamlett & Stecker 1991 |
| R2 | **Two clocks.** Fast loop (seconds) micro-scaffolds within a method; slow loop (≥4 points, 7–10 weeks for trend) changes the method. Never let the fast loop change the method. | F6 / Van Norman et al. 2023 |
| R3 | **A finite, ordered, evidence-ranked pivot menu** — granularity, worked example, representation (concreteness fading), prerequisite, modality, dosage, escalate. Not free-form LLM improvisation. | Swanson & Sachse-Lee 2000; Gersten 2009; Fyfe et al. 2014 |
| R4 | **A human-escalation stopping rule**, defined in advance, that fires on repeated non-response. Non-response is a designed-for state, not an error. | Al Otaiba & Fuchs 2006; DBI step 5 |
| R5 | **Dosage is the primary scalable lever**, and it must be measured and reported. | Stockard et al. 2018 (exposure→effect) |
| R6 | **No cognitive training.** Externalise load; never attempt to expand capacity. | Melby-Lervåg et al. 2016; Westwood et al. 2023 |
| R7 | **Untimed by default;** latency may scaffold, never score. | §4.5 |
| R8 | **TTS/STT and dual coding as defaults**, not accommodations behind a flag. | Wood et al. 2018 |
| R9 | **Open, inspectable, parent- and student-correctable learner model**; and it is governed as sensitive data because it is a de facto diagnostic record. | §6.3; PRD H1.2(4) |
| R10 | **Never emit a full solution; withdrawal-performance is a first-class metric.** | Bastani et al. 2025; Lehmann et al. 2024 |
| R11 | **WCAG 2.2 AA as a build gate**, including streamed-output screen-reader correctness. | §6.4 |
| R12 | **AI draft, human authorship, visible provenance** for anything touching an IEP. | 34 CFR §§300.320–321 |
| R13 | **No output-artefact AI detection** applied to students with writing accommodations. | §6.6 |
| R14 | **An explicit accommodation-conflict policy**, because accommodations compose and can conflict. | §4.8 — open problem |

**Two studies the survey should propose in G4, because both are cheap, high-value, and
apparently un-run:**

- **S1.** A properly powered RCT of a guardrailed LLM tutor with students on IEPs, using
  CBM-equivalent weekly progress monitoring, a pre-registered decision rule, and a
  **tool-withdrawal post-test** as the primary outcome. Currently n = 0 in ERIC and
  Europe PMC.
- **S2.** A false-positive audit of commercial AI-writing detectors on writing produced
  by students using IEP/504 writing scaffolds (sentence frames, paragraph templates),
  against a matched non-accommodated sample. Liang et al. established the mechanism for
  non-native writers; nobody appears to have run it for accommodated writers, and the
  harm — a disciplinary accusation that cannot be disproved from the artefact — is severe.

---

## 9. Bibliography

**Reading / literacy**
1. Ehri, Nunes, Stahl & Willows (2001). Systematic phonics instruction helps students learn to read: evidence from the NRP meta-analysis. *RER* 71(3). https://doi.org/10.3102/00346543071003393 — `MEASURED-META`
2. Ehri, Nunes, Willows, Schuster, Yaghoub-Zadeh & Shanahan (2001). Phonemic awareness instruction helps children learn to read. *RRQ* 36(3). https://doi.org/10.1598/rrq.36.3.2 — `MEASURED-META`
3. Galuschka, Ise, Krick & Schulte-Körne (2014). Effectiveness of treatment approaches for children and adolescents with reading disabilities: a meta-analysis of RCTs. *PLoS ONE* 9(2). https://doi.org/10.1371/journal.pone.0089900 — `MEASURED-META`
4. Stevens, Austin, Moore, Scammacca, Boucher & Vaughn (2021). Current state of the evidence: Orton-Gillingham reading interventions. *Exceptional Children* 87(4):397–417. https://doi.org/10.1177/0014402921993406 · https://pmc.ncbi.nlm.nih.gov/articles/PMC8497161/ — `MEASURED-META` **(N1)**
5. Bowers (2020). Reconsidering the evidence that systematic phonics is more effective. *Educ Psych Rev* 32. https://doi.org/10.1007/s10648-019-09515-y — `MEASURED-META` (contested)
6. Al Otaiba & Fuchs (2006). Who are the young children for whom best practices in reading are ineffective? *JLD* 39(5). https://doi.org/10.1177/00222194060390050401 — `OBSERVED`
7. Vaughn et al. (2022). What we know and need to know about literacy interventions for elementary students with reading difficulties and disabilities, including dyslexia. *RRQ*. https://doi.org/10.1002/rrq.458 — `MEASURED-META`

**Explicit / direct instruction**
8. Stockard, Wood, Coughlin & Rasplica Khoury (2018). The effectiveness of Direct Instruction curricula: a meta-analysis of a half century of research. *RER* 88(4). https://doi.org/10.3102/0034654317751919 — `MEASURED-META`
9. Swanson & Hoskyn (1998). Experimental intervention research on students with learning disabilities. *RER* 68(3). https://doi.org/10.3102/00346543068003277 — `MEASURED-META`
10. Swanson (1999). Reading research for students with LD. *JLD* 32(6). https://doi.org/10.1177/002221949903200605 — `MEASURED-META`
11. Swanson & Sachse-Lee (2000). Meta-analysis of single-subject-design intervention research for students with LD. *JLD* 33(2). https://doi.org/10.1177/002221940003300201 — `MEASURED-META`
12. Swanson & Hoskyn (2001). Instructing adolescents with learning disabilities: a component and composite analysis. *LDRP* 16(2). https://doi.org/10.1111/0938-8982.00012 — `MEASURED-META`
13. Kirschner, Sweller & Clark (2006). Why minimal guidance during instruction does not work. *Educational Psychologist* 41(2). https://doi.org/10.1207/s15326985ep4102_1 — `OBSERVED`
14. Meyer (1984). Long-term academic effects of the Direct Instruction Project Follow Through. *Elementary School Journal* 84(4). https://doi.org/10.1086/461371 — `OBSERVED`
15. Meyer, Gersten & Gutkin (1983). Direct Instruction: a Project Follow Through success story in an inner-city school. *ESJ* 84(2). https://doi.org/10.1086/461360 — `OBSERVED`

**CBM / DBI / RTI**
16. Deno (1985). Curriculum-based measurement: the emerging alternative. *Exceptional Children* 52(3). https://doi.org/10.1177/001440298505200303 — `OBSERVED`
17. Fuchs & Fuchs (1986). Effects of systematic formative evaluation: a meta-analysis. *Exceptional Children* 53(3). **ES = 0.70.** https://doi.org/10.1177/001440298605300301 — `MEASURED-META`
18. **Fuchs, Hamlett & Stecker (1991). Effects of CBM and consultation on teacher planning and student achievement in mathematics operations. *AERJ* 28(3). https://doi.org/10.3102/00028312028003617 — `MEASURED-RCT` (F5 / N3)**
19. Fuchs, Fuchs, Hamlett & Allinder (1991). Effects of expert system advice within CBM on teacher planning and student achievement in spelling. *SPR* 20(1). https://doi.org/10.1080/02796015.1991.12085532 — `MEASURED-RCT`
20. Stecker, Fuchs & Fuchs (2005). Using CBM to improve student achievement: review of research. *Psychology in the Schools* 42(8). https://doi.org/10.1002/pits.20113 — `MEASURED-META`
21. Ardoin, Christ, Morena & Cormier (2013). Systematic review of recommendations and research surrounding CBM-R decision rules. *JSP* 51(1). https://doi.org/10.1016/j.jsp.2012.09.004 — `OBSERVED`
22. Van Norman & Christ (2016). CBM-R: accuracy of recommendations from three-point decision rules. *SPR* 45(3). https://doi.org/10.17105/spr45-3.296-309 — `MEASURED-BENCH`
23. Van Norman & Christ (2016). How accurate are interpretations of CBM progress monitoring data? Visual analysis versus decision rules. *JSP* 58. https://doi.org/10.1016/j.jsp.2016.07.003 — `MEASURED-BENCH`
24. Van Norman, Christ & Newell (2017). CBM-R progress monitoring: growth magnitude and goal setting. *SPR* 46(3). https://doi.org/10.17105/spr-2017-0065.v46-3 — `MEASURED-BENCH`
25. Van Norman & Nelson (2019). Seasonal goal lines and CBM-R decision-rule accuracy. *AEI*. https://doi.org/10.1177/1534508419872249 — `MEASURED-BENCH`
26. **Van Norman, Klingbeil, Truman & Nelson (2023). Comparison of decision-rule accuracy from CBM-R and nonsense word fluency. *RASE*. Trend-line rule viable after **7 weeks (NWF) / 9–10 weeks (CBM-R)**. https://doi.org/10.1177/07419325231190812 — `MEASURED-BENCH` (F6)**
27. NCII. Data-Based Individualization: the five-step process. https://intensiveintervention.org/data-based-individualization — `OBSERVED` *(numeric decision rules not published on this page; see 21–26)*
28. **Balu, Zhu, Doolittle, Schiller, Jenkins & Gersten (2015). Evaluation of Response to Intervention Practices for Elementary School Reading. NCEE 2016-4000. https://ies.ed.gov/ncee/pubs/20164000/ — `MEASURED-RCT` (regression-discontinuity) (N2)**
29. Gersten (2016 commentary). Response to Intervention: is the sky falling? *Reading Teacher*. https://doi.org/10.1002/trtr.1457 — `OBSERVED`

**Mathematics**
30. Gersten, Chard, Jayanthi, Baker, Morphy & Flojo (2009). Mathematics instruction for students with learning disabilities: a meta-analysis of instructional components. *RER* 79(3). Effects 0.21–1.56; explicit instruction and heuristics carry the gains. https://doi.org/10.3102/0034654309334431 — `MEASURED-META`
31. Jitendra, Lein, Im et al. (2017). Mathematical interventions for secondary students with LD and mathematics difficulties. *Exceptional Children* 84(2). **g = 0.37 [0.18, 0.56]**. https://doi.org/10.1177/0014402917737467 — `MEASURED-META`
32. Lein, Jitendra & Harwell (2020). Word-problem-solving interventions for students with LD/MD. *JEP* 112(7). https://doi.org/10.1037/edu0000453 — `MEASURED-META`
33. Gersten, Jordan & Flojo (2005). Early identification and interventions for students with mathematics difficulties. *JLD* 38(4). https://doi.org/10.1177/00222194050380040301 — `MEASURED-META`
34. Fyfe, McNeil, Son & Goldstone (2014). Concreteness fading in mathematics and science instruction: a systematic review. *Educ Psych Rev* 26. https://doi.org/10.1007/s10648-014-9249-3 — `MEASURED-META`
35. McNeil & Fyfe (2012). "Concreteness fading" promotes transfer of mathematical knowledge. *L&I* 22(6). https://doi.org/10.1016/j.learninstruc.2012.05.001 — `MEASURED-RCT`
36. Finell, Sammallahti, Korhonen & Eklöf (2022). Working memory and its mediating role on math anxiety and math performance: a meta-analysis. *Front Psychol* 12. **r = −0.168**, 57 studies / 150 ES. https://doi.org/10.3389/fpsyg.2021.798090 — `MEASURED-META`

**ADHD / executive function**
37. Barkley (1997). Behavioral inhibition, sustained attention, and executive functions. *Psychological Bulletin* 121(1). https://doi.org/10.1037/0033-2909.121.1.65 — `OBSERVED`
38. Faraone et al. (2021). World Federation of ADHD International Consensus Statement: 208 evidence-based conclusions. *Neurosci Biobehav Rev* 128. https://doi.org/10.1016/j.neubiorev.2021.01.022 — `MEASURED-META`
39. DuPaul, Eckert & Vilardo (2012). Effects of school-based interventions for ADHD: a meta-analysis 1996–2010. *SPR* 41(4). https://doi.org/10.1080/02796015.2012.12087496 — `MEASURED-META`
40. **Melby-Lervåg, Redick & Hulme (2016). Working memory training does not improve performance on measures of intelligence or other measures of "far transfer." *PPS* 11(4). https://doi.org/10.1177/1745691616635612 — `MEASURED-META` (N4)**
41. Melby-Lervåg & Hulme (2013). Is working memory training effective? *Developmental Psychology* 49(2). https://doi.org/10.1037/a0028228 — `MEASURED-META`
42. Westwood et al. (2023). Computerized cognitive training in ADHD: meta-analysis of RCTs with blinded and objective outcomes. *Molecular Psychiatry* 28. https://doi.org/10.1038/s41380-023-02000-7 — `MEASURED-META`

**AAC / assistive technology**
43. Millar, Light & Schlosser (2006). The impact of AAC intervention on the speech production of individuals with developmental disabilities. *JSLHR* 49(2). **0% decreased; 89% gained.** https://doi.org/10.1044/1092-4388(2006/021) — `MEASURED-META`
44. Schlosser & Lee (2000). Promoting generalization and maintenance in AAC: meta-analysis of 20 years. *AAC* 16(4). https://doi.org/10.1080/07434610012331279074 — `MEASURED-META`
45. Schlosser & Raghavendra (2004). Evidence-based practice in AAC. *AAC* 20(1). https://doi.org/10.1080/07434610310001621083 — `OBSERVED`
46. Wood, Moxley, Tighe & Wagner (2018). Does use of text-to-speech and related read-aloud tools improve reading comprehension for students with reading disabilities? *JLD* 51(1). **d = 0.35 [0.14, 0.56]**. https://doi.org/10.1177/0022219416688170 — `MEASURED-META`

**UDL**
47. Capp (2017). The effectiveness of Universal Design for Learning: a meta-analysis 2013–2016. *IJIE* 21(8). https://doi.org/10.1080/13603116.2017.1325074 — `MEASURED-META` **(N7)**
48. Murphy (2020). Belief without evidence? A policy research note on Universal Design for Learning. *Policy Futures in Education* 19(1). https://doi.org/10.1177/1478210320940206 — `OBSERVED` **(N8)**
49. Boysen (2021). Lessons (not) learned: the troubling similarities between learning styles and Universal Design for Learning. *SoTL in Psychology*. https://doi.org/10.1037/stl0000280 — `OBSERVED`
50. Al-Meqdad, Alodat, Alquraan, Mohaidat & Al-Makhzoomy (2023). The effectiveness of UDL: systematic review and meta-analysis. *Cogent Education* 10(1). https://doi.org/10.1080/2331186x.2023.2218191 — `MEASURED-META` *(cite as methodological counter-example only)*
51. Zhang, Carter, Greene & Bernacki (2024). Unraveling challenges with the implementation of UDL. *Educ Psych Rev* 36. https://doi.org/10.1007/s10648-024-09860-7 — `OBSERVED`
52. Bray, Devitt & Banks (2023). What next for UDL? Systematic review of technology in UDL implementations at second level. *BJET* 54. https://doi.org/10.1111/bjet.13328 — `OBSERVED`

**AI, tutoring, and the gap**
53. **Paglialunga & Melogno (2025). The effectiveness of AI-based interventions for students with learning disabilities: a systematic review. *Brain Sciences* 15(8):806. 11 studies / 3,033 participants; **no study at low risk of bias**; all 11 positive. https://doi.org/10.3390/brainsci15080806 · https://pmc.ncbi.nlm.nih.gov/articles/PMC12385150/ — `MEASURED-META` (F2)**
54. Kestin, Miller, Klales, Milbourne & Ponti (2024/2025). AI tutoring outperforms in-class active learning. *Scientific Reports* 15. **d ≈ 0.63–1.3**, N = 194, Harvard physics. **Zero disability/accessibility reporting (own full-text audit).** https://doi.org/10.21203/rs.3.rs-4243877/v1 · https://doi.org/10.1038/s41598-025-97652-6 — `MEASURED-RCT`
55. Wang, Ribeiro, Robinson et al. (2024). Tutor CoPilot: a human–AI approach for scaling real-time expertise. **+4 p.p. mastery; +9 p.p. for lowest-rated tutors.** Special-education status appears only as a covariate. https://arxiv.org/abs/2410.03017 — `MEASURED-RCT`
56. De Simone, Tiberti, Barron Rodriguez, Manolio, Mosuro & Dikoru (2025). From chalkboards to chatbots: evaluating the impact of generative AI on learning outcomes in Nigeria. World Bank PRWP 11125. **+0.31 SD overall; largest effects for higher initial performers.** https://doi.org/10.1596/1813-9450-11125 — `MEASURED-RCT`
57. **Bastani, Bastani, Sungu, Ge, Kabakcı & Mariman (2025). Generative AI without guardrails can harm learning: evidence from high school mathematics. *PNAS* 122. **−17% after withdrawal.** https://doi.org/10.1073/pnas.2422633122 — `MEASURED-RCT` (N10)**
58. **Lehmann, Cornelius & Sting (2024). AI meets the classroom: when do large language models harm learning? arXiv 2409.09047. **No overall effect; substitution harms; LLMs widen the low/high prior-knowledge gap.** https://arxiv.org/abs/2409.09047 · https://doi.org/10.2139/ssrn.4941259 — `MEASURED-RCT` (N9, F7)**
59. Anonymous (2026). Reinforcement learning for special education: aligning LLM tutors to diverse learners through disability-adaptive training. arXiv 2605.30670. States that research aligning LLM tutors for special education "remains absent." https://arxiv.org/abs/2605.30670 — `OBSERVED` (preprint, no student outcomes)
60. Liang, Yuksekgonul, Mao, Wu & Zou (2023). GPT detectors are biased against non-native English writers. *Patterns* 4(7). https://doi.org/10.1016/j.patter.2023.100779 — `MEASURED-BENCH`
61. Al Ali, Helcl & Libovický (2026). Different time, different language: revisiting the bias against non-native speakers in GPT detectors. EACL SRW. https://doi.org/10.18653/v1/2026.eacl-srw.20 — `MEASURED-BENCH`
62. Zhang & Zhang (2025). A systematic review of AI-driven intelligent tutoring systems in K-12 education. *npj Science of Learning* 10. https://doi.org/10.1038/s41539-025-00320-7 — `OBSERVED`
63. OECD (2024). The potential impact of artificial intelligence on equity and inclusion in education. OECD AI Papers. https://doi.org/10.1787/15df715b-en — `OBSERVED`

**Legal / accessibility**
64. IDEA, 34 CFR §300.320 (definition of IEP). https://sites.ed.gov/idea/regs/b/d/300.320 — `OBSERVED`
65. IDEA, 34 CFR §300.321 (IEP Team). https://sites.ed.gov/idea/regs/b/d/300.321 — `OBSERVED`
66. Section 504, Rehabilitation Act of 1973 (29 U.S.C. §794; 34 CFR Part 104). https://www.ed.gov/laws-and-policy/individuals-disabilities/section-504 — `OBSERVED`
67. W3C (2024). Web Content Accessibility Guidelines (WCAG) 2.2. W3C Recommendation, 12 December 2024. https://www.w3.org/TR/WCAG22/ — `OBSERVED`

**Own measurements (this report)**
68. Gap census, Europe PMC REST API and ERIC API, run 2026-07-27. Query strings and counts in §3.1. — `MEASURED-BENCH`
69. Full-text disability-mention audit of Kestin et al. and Wang et al. (Tutor CoPilot), run 2026-07-27. Method and results in §3.4. — `OBSERVED`

---

## 10. Research notes, limitations, and unresolved items

**Sources that could not be retrieved.** Flagged rather than guessed:

- MDPI HTML/PDF endpoints returned **403** to direct `curl`; the Paglialunga & Melogno
  content above was obtained from the **PMC mirror (PMC12385150)** and the Crossref
  abstract, both authoritative.
- **NCII's numeric decision rules** could not be retrieved from `intensiveintervention.org`
  (the DBI landing page carries only the five-step process; three candidate training-module
  PDFs and two taxonomy pages returned **404**). The four-point / trend-line rule
  specifications in §1.4 therefore come from the peer-reviewed CBM decision-rule
  literature (Ardoin et al. 2013; Van Norman & Christ 2016; Van Norman et al. 2023). The
  survey should cite those, not NCII.
- **IRIS Center** module pages returned content that did not match the requested section.
- **Semantic Scholar** API returned HTTP 429 throughout; OpenAlex began 429-ing after ~20
  requests. Crossref, ERIC, Europe PMC, and arXiv (intermittently) carried the load.
- **arXiv API** became intermittently unresponsive; the two arXiv items were confirmed via
  WebFetch on the abstract pages.

**Limits on the census (§3.1).** It searches title/abstract/keyword indexing in two
databases. A trial that enrolled students with disabilities but reported the subgroup only
in a results table would be missed. It does not cover dissertations, conference
proceedings outside these indexes, vendor-run studies, or non-English literature. The
correct claim is therefore *"no such RCT is indexed in ERIC or Europe PMC as of
2026-07-27,"* not *"no such RCT exists."* The claim is falsifiable by a single
counter-example, which is the point.

**Items not resolved and worth a follow-up pass:**

- The **exact Grade-1 effect size** in Balu et al. (2015) — the executive summary states
  direction and significance; the full report (ED560820) has the magnitude.
- **King-Sears et al.** UDL meta-analysis appears only as an AERA poster
  (https://doi.org/10.3102/ip.22.1886863) in the indexes searched; a journal version may
  exist and would strengthen §2.
- **WWC practice guides** (Assisting Students Struggling with Reading / with Mathematics)
  returned 0 hits under the queries tried; they are the canonical practitioner translation
  of §1.1–1.5 and should be added by direct fetch from ies.ed.gov.
- **Autism-specific instructional research** (e.g. NPDC/NCAEP evidence-based practice
  reviews) is under-covered here relative to reading, mathematics, and ADHD.
- **Section 4.8's accommodation-conflict problem** has no literature answer that this
  research located. It is a genuine open problem and belongs in G4.
