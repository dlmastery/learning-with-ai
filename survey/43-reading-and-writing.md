---
title: "Reading and Writing — the tool improves the draft in front of the learner and never the next blank page"
section: literacy
status: draft
date: 2026-07-30
source_report: research/raw/R5-reading-and-writing.md
---

# Reading and Writing

Three studies by one research group, spanning six years and including one
randomised trial, converge on a single result: automated writing evaluation
improves the draft in front of the learner and does not improve the next one.

That is the shape of the unguarded-assistance finding this survey turns on
(§01), reached independently, in a different subject, against a different
comparison condition, with a tool generation that predates anything anyone would
now call AI.

---

## 1. The transfer result, three times

**Wilson, Olinghouse & Andrada (2014).** A statewide computer-based benchmark
writing assessment with automated scoring and feedback, grades 4–8, three-level
HLM. Writing quality improved across revisions and growth decelerated over time.
On the follow-up prompt: *"No significant transfer effects were observed"* —
neither an improved first draft nor accelerated growth. `OBSERVED` (statewide
observational).

**Wilson (2017).** PEG Writing, **n = 1,196**, students with disabilities and
typically developing students matched on prior writing achievement, transfer
subsample **n = 655**. Students with disabilities produced weaker first drafts,
grew faster, and closed the quality gap after five revisions. And: *"There was no
evidence of transfer for either group of students."* `OBSERVED`.

**Wilson & Roscoe (2020).** The randomised one. Sixth graders assigned by
classroom to PEG Writing (n = 56) or Google Docs word processing (n = 58), four
outcomes, path analysis controlling for pretest. **Composing condition had no
effect on holistic writing quality.** The AWE condition did produce higher
writing self-efficacy and better state ELA test performance, with self-efficacy
partially mediating the test effect. `MEASURED-RCT`.

Read the three together. Revision quality rises, self-efficacy rises, a distal
test score rises, and what the learner can do on a blank page tomorrow does not
move.

Two guards against overstating this. Nunes, Cordeiro, Limpo & Castro (2022)
systematically reviewed AWE in school settings 2000–2020 under PRISMA and found
**eight studies, six systems, 1,659 students aged 11–17**, of which all but one
showed a positive effect on at least one writing-related measure.
`MEASURED-META` (no pooled estimate). Twenty years of K–12 research on this
technology is eight studies. And the larger pooled numbers come from a different
population: Zhai & Ma (2023) report g = 0.861 on writing quality across 26
studies and 2,468 participants, larger for post-secondary and for EFL/ESL
learners than for secondary native speakers; Ngo, Chen & Lai (2024), in a
three-level model, separate **between-group g = 0.59** (24 studies) from
**within-group g = 0.98** (34 studies). `MEASURED-META` ×2. The gap between those
last two is the size of the maturation-plus-practice effect a within-subject
design cannot remove.

So the transfer null is not a verdict on the technology. It is a verdict on
fifteen years of measuring the assisted draft and calling the result learning.

---

## 2. What the writing effect sizes are effect sizes *of*

Nearly every number below is the same object: **the rubric-scored holistic
quality of a composition, written during or immediately after the instruction,
scored by human raters blind to condition, against a control group writing under
ordinary conditions.** It is a good outcome, produced while the treatment is
still switched on. Very few writing studies administer a delayed post-test, and
essentially none of the AI studies administer an unassisted one.

Graham & Perin (2007), *JEP* 99(3):445–476 — grades 4–12, 123 documents yielding
**154 effect sizes for quality of writing**. Average weighted effect sizes:

| Element | ES |
|---|---|
| Strategy instruction | 0.82 |
| Summarisation | 0.82 |
| Peer assistance | 0.75 |
| Setting product goals | 0.70 |
| Word processing | 0.55 |
| Sentence combining | 0.50 |
| Inquiry / prewriting / process writing | 0.32 each |
| Study of models | 0.25 |
| Grammar instruction | **−0.32** |

`MEASURED-META`. Four qualifications travel with that table and are usually
dropped when it is reproduced. Strategy instruction runs **1.02 for
low-achieving writers against 0.70 across the full ability range**, and
Self-Regulated Strategy Development specifically runs **1.14 against 0.62** for
non-SRSD strategy approaches. The process approach's 0.32 is a mixture: *"When
teachers had such training, the effect was moderate (0.46), but in the absence of
training the effect was negligible"* — and five of the six trained-teacher
studies were conducted by the National Writing Project to support its own work,
with no random assignment in any of them. Word processing is likewise 0.51
general and 0.70 for low-achieving writers. Only four elements had ten or more
effect sizes behind them, and one of those four is the negative one.

The elementary replication (Graham et al. 2012, 115 documents) holds the ranking:
strategy instruction 1.02, SRSD 1.17, peer assistance 0.89. `MEASURED-META`.

**The part that pays twice.** Writing about content the learner is studying has
the best-behaved evidence in this literature. Graham, Kiuhara & MacKay (2020),
k = 56 experiments, grades 1–12, science, social studies and mathematics,
against a control that did not use writing to support learning and with
instructional time and content coverage equated: **ES = 0.30 on content
learning**, equally effective across the three subjects and across elementary,
middle and high school, and **not moderated by any feature of the writing
activity, the instruction, or the assessment**. `MEASURED-META`. The absent
moderators are the useful part: a tutor does not have to design a clever prompt
to get the effect. Graham & Hebert (2011) close the loop toward reading:
writing about text read scores **0.40 on published standardised norm-referenced
tests** (11 studies) and 0.51 on researcher-designed ones (50 studies), with 57
of 61 outcomes positive. `MEASURED-META`.

That 0.40 calibrates the reading half below: it exceeds Slavin et al.'s 0.17 for
secondary reading programmes and Elleman et al.'s 0.10 for vocabulary
instruction, and matches Rosenshine & Meister's 0.32 for reciprocal teaching (all
three as reported in Graham & Hebert, not retrieved independently).

And its own null, which constrains the build. In twelve studies with
lower-achieving students, writing about text ran 0.63 — *"However, the average
weighted effect size for writing about text activities was not greater than zero
when lower-achieving students were not explicitly taught how to use them."*
Assigning the writing does nothing for a weak writer. Teaching the writing does.

---

## 3. Grammar instruction carries a minus sign

Traditional grammar instruction, the standalone teaching of syntactic rules and
usage, produced **ES = −0.32 on writing quality** in the adolescent
meta-analysis, and it is one of only four elements with more than ten effect
sizes behind it. In the elementary meta-analysis it was the single
explicit-teaching intervention that failed to reach significance.
`MEASURED-META`.

This is the null this section owes, and it is the one with the sharpest
consequence for a conversational tutor. Explaining a rule about language is the
cheapest, most fluent, most on-brand move a language model has. It is also the
one element in the table with a negative sign, and the meta-analysis names its
functioning replacement: sentence combining, at 0.50. A system that answers *my
writing is bad* with a lesson on subordinate clauses is implementing the
documented negative and skipping the documented positive.

The same shape recurs in the feedback literature. Graham, Hebert & Harris (2015),
grades 1–8, outcome writing quality: adults 0.87, self 0.62, peers 0.58,
computers 0.38 — and two nulls in the same paper, *"we did not find, however,
that teachers' monitoring of students' writing progress or implementation of the
6 + 1 Trait Writing model meaningfully enhanced students' writing."*
`MEASURED-META`. Progress monitoring that changes nothing about instruction is
inert, which is the reading-measurement result of §04 reached separately in a
second literature.

---

## 4. Over a third of feedback interventions make performance worse

Kluger & DeNisi (1996), *Psychological Bulletin* 119(2):254–284, abstract
retrieved verbatim:

> "A meta-analysis (607 effect sizes; 23,663 observations) suggests that FIs
> improved performance on average (d = .41) but that over 1/3 of the FIs
> decreased performance. This finding cannot be explained by sampling error,
> feedback sign, or existing theories. … The results suggest that FI
> effectiveness decreases as attention moves up the hierarchy closer to the self
> and away from the task."

`MEASURED-META`. Before this section, the string *Kluger* appeared zero times
across every report and survey section in this corpus.

A traceability note, because two versions circulate. Wisniewski, Zierer & Hattie
(2020) describe Kluger & DeNisi as based on 131 studies and over 12,000
participants with an average effect of 0.38. The primary abstract says 607
effect sizes, 23,663 observations, d = .41. Both the n and the d are misstated in
the restatement; use the primary. Wisniewski et al.'s own synthesis, across 435
studies, 994 effect sizes and over 61,000 subjects, reports d = 0.48 [0.44, 0.51]
overall, decomposing into reinforcement and punishment **0.24 [0.06, 0.43]**,
corrective feedback 0.46 [0.39, 0.55], and high-information feedback **0.99
[0.82, 1.15]**, with 17% of all effects negative. `MEASURED-META`.

A returned essay carrying a grade, a rubric score or a global verdict on quality
is the textbook self-level feedback intervention: it tells the writer something
about the writer. Generative systems make that free and unlimited — every draft,
instantly, with a score and a paragraph of encouragement. Three design rules
follow, `INFERENCE` from the three feedback meta-analyses above:

1. **No global quality judgement is returned to the learner.** Scores may route
   internally; they do not surface. A holistic score is the 0.24 cell wearing the
   0.99 cell's clothes.
2. **Feedback names the next move on this text.** *"Your second paragraph asserts
   X and the evidence supports Y — add the missing step or change the claim"* is
   task-level. *"Your development is a 3"* is self-level.
3. **Cap the comment count.** Nothing in the retrieved literature sets the cap;
   the attention-hierarchy mechanism predicts that past some volume the learner
   stops processing moves and starts processing the verdict. `SPEC`, and
   measurable.

---

## 5. Scrambled essays score higher

Myers & Wilson (2023), *IJAIED*: 100 persuasive essays by grade 7–8 students,
each randomised at the sentence level 30 times, **n = 3,000 randomisations**,
scored by the MI Write AWE system on six traits. Sentence-order randomisation
destroys idea development and organisation by construction, so those trait scores
should collapse.

> "Overall, complete randomizations did not consistently significantly impact
> trait scoring for these high-level writing traits. In fact, more than a third
> of the essays saw significant increases in one or both high-level traits
> despite randomization."

`MEASURED-BENCH`. This is the BABEL demonstration rebuilt as a controlled
ablation, on a system marketed for classroom formative feedback, published in an
AI-in-education venue, by authors whose other work is broadly favourable to AWE.
Kabra et al. (2023) corroborate it from the NLP side: deep AES models with
contextual embeddings *"behave like bag-of-words models."* `MEASURED-BENCH`.

§12 owns the question of what an essay score licenses as a claim about a person.
What the construct result adds here is instructional: a learner who optimises
against a development score that is a word count learns to produce words.

---

## 6. The hypothesis this project asked for, and what came back

The brief that commissioned the underlying report asked the researcher to
establish that comprehension strategies have a much weaker effect than background
knowledge, so that a tutor building knowledge could be said to be doing the large
thing. Traced to primaries, the claim does not hold at that magnitude. On
standardised comprehension outcomes:

| Intervention family | Standardised comprehension |
|---|---|
| Whole-class strategy instruction (Okkinga, k = 125) | 0.186 |
| Struggling-reader interventions 1980–2011 (Scammacca, k = 82) | 0.21 |
| Content-rich integrated instruction (Hwang, k = 35) | 0.25 |
| Sustained knowledge-building RCT (Kim 2023, N = 2,952) | 0.18 |
| Reciprocal teaching (Rosenshine & Meister, as reported) | 0.32 |

Every one sits between 0.18 and 0.32. `MEASURED-META` ×4 plus one
`MEASURED-RCT` — the Kim et al. figure comes from 30 schools, 2,952 students and
144 teachers randomised at school level, on science content reading
comprehension.

The classic demonstration behind the popular claim is genuinely strong and
genuinely correlational. Recht & Leslie (1988), n = 64, sixteen per cell:
students split by preassessed reading ability and preassessed baseball
knowledge, each reading an account of a half inning. *"There was a significant
main effect for prior knowledge on all measures. No interactions between prior
knowledge and ability were found."* `OBSERVED` — knowledge and ability are
measured, never assigned, so the design cannot license a claim about *building*
knowledge. Poor readers who knew baseball out-recalled good readers who did not,
and that is all it says.

What replaced the hypothesis is narrower and survives the evidence:
**knowledge-building and strategy instruction are indistinguishable on
standardised comprehension, and only one of them also produces content knowledge
at ES = 0.89** (Hwang et al., alongside vocabulary at 0.91). Strategy instruction
has no second outcome at all. For a learner who has to pass a science test as
well as read a passage, the second outcome decides it. `INFERENCE`. The
falsifier is a trial that randomises comparable learners over equated
instructional hours to strategy instruction on domain-general texts versus
content-rich instruction in one domain, and finds a between-arm difference on a
standardised comprehension measure. Nobody has run it; every knowledge study adds
content time and every strategy study adds strategy time, so the two literatures
have never met. This refutation is logged in `process/ASSUMPTIONS.md`.

Two further constraints on the knowledge story. Smith, Snow, Serry & Hammond
(2021), a critical review of 23 studies, find effects moderated by text type, by
the situation model required, **and by the presence of reader misconceptions** —
a confident wrong model degrades comprehension of a correct text.
`MEASURED-META` (no pooled estimate). A tutor that "activates prior knowledge"
without checking whether it is true has a mechanism for making things worse. And
Cabell et al. (2025), two RCTs across 47 schools and 1,194 kindergarteners, found
that *"children who began the year with relatively higher receptive vocabulary
scores derived a greater benefit"* — the interaction runs the wrong way for the
learners this project designs for. `MEASURED-RCT` ×2.

Finally, provenance. Willingham's *How Knowledge Helps* is the version of this
argument most readers have met. It is a column in *American Educator*, the AFT's
professional magazine, and it was not retrievable through ERIC, Crossref or
OpenAlex. Cite it as an accurate trade restatement of primary work; do not cite
it as evidence.

---

## 7. What decays is not what you expect, and one authority is a vote count

Suggate (2016) pooled 71 intervention–control groups, **N = 8,161** at
post-test, all reporting a follow-up at a mean of 11.17 months. The aggregate
post-test d_w = 0.37 fell to **d_w = 0.22** at follow-up, and the differential is
the finding: *"comprehension and phonemic awareness interventions showed good
maintenance of effect that transferred to nontargeted skills, whereas phonics and
fluency interventions, and those for preschool and kindergarten children, tended
not to."* `MEASURED-META`.

A builder arrives expecting the opposite: decoding as the durable investment,
comprehension as the soft one. On the single dimension that has been measured
across eleven months, the sign is the other way round. Strategy instruction
produces a small, durable, transferable gain, largest for weak readers, close to
zero for strong ones (Elleman 2017: d = 0.97 on literal outcomes for less-skilled
readers against **d = 0.06** for skilled ones), and its apparent size in the
literature is mostly an artifact of who wrote the outcome test — 0.786 on
strategy use, 0.431 on researcher-built comprehension tests, 0.186 on
standardised ones, in the same meta-analysis.

**A warrant note about the authority everyone cites.** The National Reading
Panel's phonics and fluency chapters are meta-analyses. Its comprehension chapter
is not. From the executive summary: *"For comprehension instruction, there were
simply too many studies involving too many variables to allow for a simple
meta-analysis. … A formal meta-analysis was not possible."* 203 studies were
sorted into 16 categories, of which 7 were judged to have a solid scientific
basis. That is a vote count with expert judgement over it, and it may well be
right; it is `OBSERVED`, never `MEASURED-META`, and the field quotes it beside
d = 0.41 for phonics as though the two carried the same warrant.

The panel's own null on reading volume is quoted even less: *"Most of the
studies, including the best designed and largest ones … reported no appreciable
benefit to reading from such procedures,"* with Carver and Liebert finding no
clear benefit from **60 hours of additional reading**. Reading more is the most
common advice a parent is given.

And the largest test of the whole framework came back null. Reading First (Gamse
et al. 2008), **248 schools, 13 states, three school years**, regression
discontinuity: significant increases in instructional time on the five essential
components, in professional development, in reading coaches, and in first-grade
decoding — and **no statistically significant impact on reading comprehension in
grades one, two or three.** `MEASURED-RCT` (RD). A framework can be delivered
with fidelity and dosage and still not move the outcome, which is §04's
measurement-without-a-decision-rule result at national scale.

---

## 8. What becomes buildable, and the trial that would settle it

The simple view of reading, R = D × LC, is a product: if either term is zero the
product is zero. A meta-analytic SEM across 210 studies and **49,416
individuals** puts the two components at **52.7%** of the variance in reading
comprehension, with decoding's share dropping after Grade 2. `MEASURED-META`.
Half the variance is elsewhere, so this is a floor for a routing decision and not
a ceiling.

What it buys is a probe that costs a tutor nothing. Administer the same passage
by text and by audio and compare comprehension. A gap says decoding; no gap says
the problem is downstream, and the four-way branch that follows (decoding,
fluency, knowledge, inference) has different effect sizes, latencies and failure
modes on each arm. For the eleven-year-old this survey is organised around,
decoding cost is the specific barrier and §04 owns the structured-literacy answer
to it; the point here is that nothing in her file distinguishes her from a child
whose comprehension fails for want of the topic, and a system without the probe
will run a vocabulary routine at a decoding problem.

**The trial nobody has run.** Across ERIC, Crossref title search and OpenAlex,
with the query strings logged in the source report, no randomised trial of
generative-AI writing support with a delayed, unassisted post-test on a new
composition could be located. `OBSERVED — absence`; term censuses miss synonyms,
so this means *not found by these queries*. The nearest artifact is an
unrefereed EEG preprint with 18 participants in its crossover session, which
should be read as the right instinct and not as evidence.

The design is three arms randomised at learner level within class over one term:
(A) unguarded AI writing assistance, (B) guarded assistance giving task-level
feedback only with no generated prose and no holistic score, (C) no AI. Primary
outcome is a delayed, unassisted, cold-prompt composition four weeks after the
last session, new topic, blinded human raters, standard rubric. Powered at
d = 0.30 with two-sided α = .05 and 80% power, each arm needs **n = 175**;
Bonferroni correction across two pairwise contrasts raises it to **212 per arm,
636 total**. Randomising by class instead multiplies that by a design effect of
4.6 at m = 25 and ρ = 0.15, giving **≈ 2,930 learners across 117 classes** —
which is why the assistance condition has to be enforced in software and not by
instruction. `SPEC`.

---

## 9. What a literacy tutor must measure about itself

Writing is how a learner discovers they do not understand something. The
sentence that will not finish is the diagnostic. A system that drafts, revises or
returns feedback at the point where that discovery would happen may be removing
the mechanism that makes writing worth assigning, and no one has measured
whether it does.

That gives this project a small number of obligations it can meet immediately.

- **Report the cold prompt, never the assisted draft.** The system administers a
  new-topic, no-assistance, no-feedback composition on a schedule and publishes
  *that* score as its learning claim. It is nearly free, and it would have caught
  the AWE transfer failure fifteen years before the field reported it.
- **Default the writing task to content the learner is studying.** 0.30 on
  content learning, unmoderated by task features, 0.40 on standardised reading
  comprehension. It is the only writing intervention here that pays twice.
- **Teach the activity before assigning it**, because for lower-achieving
  students who were not taught how, writing about text has an effect not greater
  than zero.
- **Surface no holistic quality score**, cap the comments, and name the next move
  on the text.
- **Do not teach grammar as a unit.** ES = −0.32. Sentence combining at 0.50 is
  the replacement the meta-analysis names.
- **Probe with audio before routing.** A listening-comprehension comparison
  separates the decoding failure from the knowledge failure, and every downstream
  effect size depends on getting that branch right.

The reading half of this literature has been arguing about strategies versus
knowledge for thirty years while both families delivered between 0.18 and 0.32 on
the measure that counts. The writing half has been reporting the assisted draft
for fifteen. A tutor that runs a cold prompt every month is producing, at zero
marginal cost, the evidence that two mature literatures declined to collect.
