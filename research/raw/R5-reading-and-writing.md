---
title: "Reading and writing as skills for the ordinary learner — decoding, fluency, knowledge, and the essay a machine can grade but cannot teach"
wave: R
section: R5
date_researched: 2026-07-30
sources_count: 58
status: raw-research
---

# R5 — Reading and Writing

> **Why this report exists.** `Z1-coverage-audit.md` rows 9 and 10. Reading is covered
> only inside a special-education report: 14 of 17 corpus hits for `phonics` are in `H1`,
> and no report owns reading acquisition for the typical learner. Writing is absent
> outright — `writing instruction` 0 hits, `essay feedback` 0, `Kluger` 0, `AWE` 0. `F1`
> treats the essay as a sampling instrument to be replaced and never as a skill to be
> taught. These are the two subjects a general-purpose tutor cannot route around.
>
> **Retrieval note.** WebSearch was exhausted at the start of this session per
> `process/CLAUDE.md` §5 (200/200). Everything below was retrieved through the ERIC
> API (`api.ies.ed.gov`, the workhorse), Crossref REST, OpenAlex (working;
> `abstract_inverted_index` gave verbatim abstracts for Kluger & DeNisi and Recht &
> Leslie, both of which are paywalled everywhere else), Semantic Scholar (rate-limited
> to uselessness after four calls), and direct `curl` + `pdftotext` of four open PDFs: the
> National Reading Panel report, *Writing Next*, *Writing to Read*, and Perelman's WAC
> Clearinghouse chapter. APA PsycNet and eScholarship both returned challenge pages and
> are marked unreachable where they matter.

---

## 0. The findings, stated first

| # | Finding | Label |
|---|---|---|
| F1 | The National Reading Panel's two famous numbers are meta-analytic; its comprehension conclusion is not. On text comprehension the panel wrote that "a formal meta-analysis was not possible" and sorted 203 studies into 16 categories by narrative judgement. The field's most-cited authority for teaching comprehension never pooled an effect. | `MEASURED-META` + own extraction of the NRP report |
| F2 | Comprehension-strategy instruction moves strategy use far more than it moves comprehension. Okkinga et al.: d = 0.786 on strategic ability, d = 0.431 on researcher-built comprehension tests, d = 0.186 on standardised ones (52 studies, k = 125). | `MEASURED-META` |
| F3 | The knowledge case rests on a genuinely strong correlational demonstration (Recht & Leslie, n = 64, no interaction between prior knowledge and reading ability on any measure) and on intervention evidence that is much more modest than its popular restatement. Content-rich literacy instruction: ES = 0.25 on standardised comprehension; a 30-school, 2,952-student RCT of a sustained knowledge-building curriculum: ES = 0.18. | `OBSERVED` + `MEASURED-META` + `MEASURED-RCT` |
| F4 | Therefore the widely repeated claim that knowledge beats strategies is not supported at the magnitude at which it is stated. On standardised comprehension outcomes the two families sit in the same 0.18–0.32 band. What separates them is that knowledge-building also produces content knowledge at ES = 0.89, and strategy instruction has no second outcome at all. §1.6 states the falsifier. | `INFERENCE` |
| F5 | Writing instruction has better-behaved effect sizes than reading comprehension, and a much worse estimand. Strategy instruction 0.82 (adolescents) and 1.02 (elementary), summarisation 0.82, peer assistance 0.75, product goals 0.70, sentence combining 0.50, process writing 0.32. Nearly every one is rubric-scored quality of a composition produced during the instruction. Almost none is a delayed, unassisted post-test. | `MEASURED-META` |
| F6 | Traditional grammar instruction is a documented negative: ES = −0.32 in *Writing Next*, from the one intervention family with more than ten effect sizes and a negative sign. | `MEASURED-META` |
| F7 | Kluger & DeNisi is the load-bearing fact this corpus has never cited. 607 effect sizes, 23,663 observations, mean d = .41, and over one third of feedback interventions decreased performance. Their mechanism is that feedback which moves attention toward the self and away from the task gets worse as it moves. A returned essay with a grade on it is the canonical self-directed feedback intervention. | `MEASURED-META` |
| F8 | Automated writing evaluation improves the draft in front of the learner and has repeatedly failed to improve the next unassisted one. Three independent studies by the same group, including a randomised one, report no transfer: Wilson, Olinghouse & Andrada (statewide, grades 4–8), Wilson (n = 1,196, transfer subsample n = 655), Wilson & Roscoe (RCT, n = 114, no effect on holistic writing quality). | `MEASURED-RCT` + `OBSERVED` ×2 |
| F9 | The construct critique of AES survives into the current generation and is now made by AWE-friendly researchers. Myers & Wilson randomised 100 persuasive essays at the sentence level, 30 times each (n = 3,000), and the system's "idea development" and "organization" trait scores did not consistently fall. More than a third of essays scored significantly higher on one or both traits after being scrambled. | `MEASURED-BENCH` |
| F10 | Nobody has run the trial that matters for this project. `OBSERVED — absence`: across ERIC, Crossref title search, and OpenAlex, I could not locate a single randomised trial of generative-AI writing assistance with a delayed, unassisted post-test on a new composition. The nearest artifact is an unrefereed EEG preprint with 18 participants in its crossover session. §2.8 specifies the trial. | `OBSERVED — absence` |

---

## 1. Reading

### 1.1 What H1 already owns, and what it does not

`H1-selpa-accessibility.md` §1.1 owns structured literacy for children with word-level
reading disability: Ehri's National Reading Panel phonics syntheses, the Galuschka
randomised-only synthesis in which phonics was the only significant family, the
Orton-Gillingham null (g = 0.22, p = .40), Bowers' dissent, and the Al Otaiba non-responder
prediction. None of it is repeated here. What H1 does not have, because it was not its job,
is the architecture a tutor needs for a child who is *not* referred: a decomposition that
says which of four different failures is happening, and what each one costs to fix.

### 1.2 The simple view, and why a router needs it

Gough and Tunmer's proposal, formalised by Hoover and Gough (1990, *Reading and Writing*
2:127–160, `10.1007/bf00401799`), is that reading comprehension is the product of decoding
and linguistic comprehension, R = D × LC. The product form is the substantive claim: if
either term is zero the product is zero, and no amount of the other compensates.
`OBSERVED` (longitudinal, English–Spanish bilingual sample, grades 1–4).

The model has held up better than most things in education and it is still only a first
cut. Kendeou, Savage and van den Broek (2009, *BJEP*, `10.1348/978185408x369020`) found by
factor analysis in three independent samples (116 four-year-olds and 116 six-year-olds in
the US, 103 six-year-olds in Canada) that decoding and listening comprehension load as
distinct factors in children this young. `MEASURED-BENCH`. A one-stage meta-analytic SEM in
Chinese — 210 studies, 267 independent samples, **49,416 individuals** — found decoding and
language comprehension together explained **52.7%** of the variance in reading
comprehension, with decoding's contribution dropping significantly after Grade 2 and
language comprehension's contribution staying flat (Zhang et al. 2020, *RER*,
`10.3102/0034654320964198`). `MEASURED-META`.

Two consequences a tutor can act on. Roughly half the variance is somewhere else, so a
two-way branch is a floor and not a ceiling; Snow's commentary in the 2018 *RSE* special
issue makes the point that all three studies she was reviewing used simple comprehension
outcomes, and that academic language, perspective-taking and argumentation predict
comprehension on the tasks that actually matter. And Gustafson et al. (2013, *SJER*,
`10.1080/00313831.2012.656279`) found the two components explained **less** of the variance
for children with reading difficulties than for typical children, which is the population
where a mis-route is most expensive.

**Design consequence.** `J1`'s selection policy has no branch that distinguishes *this
child cannot lift the words off the page* from *this child lifted the words and does not
know what they refer to*. These have different interventions with different effect sizes,
different latencies, and different failure modes, and a tutor that cannot tell them apart
will run a vocabulary routine at a decoding problem. `INFERENCE`

### 1.3 Decoding, and the part of the phonics finding that decays

H1 records the headline: systematic phonics d = 0.41 on reading, larger when begun early
(0.55) than after first grade (0.27). The follow-up literature is what H1 did not reach.

**Suggate (2016), *Journal of Learning Disabilities*, ERIC EJ1083414.** 71
intervention–control groups, N = 8,161 at post-test, all reporting both post-test and
follow-up (mean follow-up 11.17 months). Post-test d_w = 0.37 fell to **d_w = 0.22** at
follow-up. The differential is the finding: *"comprehension and phonemic awareness
interventions showed good maintenance of effect that transferred to nontargeted skills,
whereas phonics and fluency interventions, and those for preschool and kindergarten
children, tended not to."* `MEASURED-META`.

This cuts against the story a builder is likely to arrive with. The decoding channel has
the cleanest randomised support and the *weakest* eleven-month persistence in this
synthesis; the comprehension channel has the muddiest short-run evidence and the better
maintenance. Any design that treats phonics as the durable investment and comprehension as
the soft one has the sign backwards on the one dimension that has been measured.

**Torgerson, Brooks, Gascoine & Higgins (2019), *Research Papers in Education*, ERIC
EJ1205323**, a systematic tertiary review of the phonics reviews themselves, note that the
definitive trial comparing approaches, recommended in 2006, **was never conducted**.
`MEASURED-META` (review of reviews). Thirteen years of national policy sat on syntheses of
studies that were not designed to answer the policy question. That is the same shape as
this corpus's own `TutorGym` problem in `Z1` §2.4: a bounded measurement generalised into a
standing law because nobody re-ran the search.

### 1.4 Fluency

The NRP's fluency chapter *is* a meta-analysis, and its numbers are more useful decomposed
than aggregated. Extracted verbatim from the report (`nichd.nih.gov`, Chapter 3):

> "Overall, the study found a weighted effect size average of 0.41 … The highest impact was
> on reading accuracy, with a mean effect size of 0.55; the next was on reading fluency,
> with a mean effect size of 0.44, and the least, but still impressive impact was on
> reading comprehension, where the effect size was 0.35."

`MEASURED-META`. The estimand is guided repeated oral reading with feedback, against
untreated or alternative-activity controls, across grades. Lee & Yoon (2017, *JLD*, ERIC
EJ1129722) pooled 34 repeated-reading studies from 1990–2014 for students with reading
disabilities, 39 independent effect sizes, outcome coded as **correct words per minute**,
and found positive effects concentrated at elementary level, largest when repeated reading
was combined with a listening passage preview. `MEASURED-META`.

And the NRP's own null, which almost nobody quotes. On encouraging independent silent
reading:

> "It would be difficult to interpret this collection of studies as representing clear
> evidence that encouraging students to read more actually improves reading achievement …
> Most of the studies, including the best designed and largest ones … reported no
> appreciable benefit to reading from such procedures."

The panel adds that Carver and Liebert (1995) found no clear benefit from **60 hours of
additional reading**. `MEASURED-META` (narrative synthesis within the fluency chapter).
Reading volume is the single most common recommendation a parent receives and it does not
have the evidence people think it has.

### 1.5 Comprehension: what strategy instruction buys

Start with what the NRP itself said, because the field cites the phonics number and the
comprehension *conclusion* as though they had the same warrant. From the executive summary:

> "For comprehension instruction, there were simply too many studies involving too many
> variables to allow for a simple meta-analysis. … A formal meta-analysis was not possible
> because even the studies identified in the same instructional category used widely
> varying sets of methodologies and implementations."

203 studies were sorted into 16 categories, of which 7 were judged to have a solid
scientific basis. That is a vote count with expert judgement over it. It may well be right.
It is not a pooled effect and should never be cited as one. `MEASURED-META` label withheld;
this is `OBSERVED` (expert panel synthesis).

The pooled estimates came later, and they are small in the place that counts.

**Okkinga, van Steensel, van Gelderen, van Schooten, Sleegers & Arends (2018),
*Educational Psychology Review*, ERIC EJ1198360.** 52 studies, k = 125, restricted to
whole-classroom settings where the teacher is the sole instructor. Three outcomes, three
answers:

| Outcome | Cohen's d |
|---|---|
| Strategic ability (do they use the strategy?) | 0.786 |
| Reading comprehension, researcher-developed test | 0.431 |
| Reading comprehension, standardised test | 0.186 |

Effects were larger when the *researcher* was the trainer than when the teacher was, and
larger in grades 6–8. `MEASURED-META`. The gradient across the three rows is the whole
story: strategy instruction reliably teaches the strategy, teaches it into the researcher's
test at half strength, and reaches the standardised measure at a quarter.

**Elleman (2017), *JEP*, ERIC EJ1149970** narrows to inference instruction, 25 studies,
K–12: general comprehension d = 0.58, inferential d = 0.68, literal d = 0.28. The moderator
matters more than the mean. Less-skilled readers gained **d = 0.97** on literal outcomes
against **d = 0.06** for skilled readers. `MEASURED-META`. Inference instruction is a
targeted repair for a specific population and close to inert for readers who are already
fine.

**Scammacca, Roberts, Vaughn & Stuebing (2015), *JLD*, ERIC EJ1064370** supplies the
calibration everybody needs. 82 study-wise effect sizes, interventions for struggling
readers in grades 4–12, 1980–2011. Mean effect **0.49**; on standardised measures **0.21**.
Both are far below the same team's 2007 estimates of 0.95 and 0.42 on the 1980–2004
subset, and the difference between the two periods is statistically significant. The
authors attribute the decline to increased use of standardised measures, more rigorous
designs, and **improvement in the business-as-usual comparison condition**. `MEASURED-META`.

That last clause is the one to carry forward. An effect size is a contrast with whatever
the control group got, and the control group got better over thirty years. Any AI tutoring
claim benchmarked against "no intervention" is quoting a number from a world in which the
alternative was worse than it is now.

And the counterweight, reported because it exists. Suggate's follow-up analysis (§1.3)
found comprehension interventions among the *best*-maintained at eleven months. So the
clean story — strategies are a short-lived trick — is not what the maintenance data show.
What the data show is that strategy instruction produces a small, durable, transferable
gain that is largest for weak readers and close to zero for strong ones, and that its
apparent size in the literature is mostly an artifact of who built the outcome test.

### 1.6 Knowledge: the strong claim, the weaker evidence, and the falsifier

The classic demonstration, retrieved verbatim. Recht & Leslie (1988), *Journal of
Educational Psychology* 80(1):16–20, `10.1037/0022-0663.80.1.16`, abstract via OpenAlex:

> "Sixty-four junior high students were divided into four equal-sized groups on the basis
> of preassessed reading ability (high and low) and preassessed amount of existing prior
> knowledge about baseball (high and low). Each subject silently read an account of a half
> inning of a baseball game. … **There was a significant main effect for prior knowledge on
> all measures. No interactions between prior knowledge and ability were found.**"

`OBSERVED` (2×2 quasi-experiment; knowledge and ability are measured, not assigned). n = 64,
sixteen per cell. The design cannot license a causal claim about *building* knowledge, and
it is the cleanest existing demonstration that knowledge of the topic dominates measured
reading skill on a comprehension task. Poor readers who knew baseball out-recalled good
readers who did not.

The popular synthesis, and its traceability. Willingham's *How Knowledge Helps* is the
version most readers have met. It is a column in **American Educator**, the AFT's
professional magazine, not a peer-reviewed synthesis; ERIC indexes seventeen Willingham
items in that outlet, all in the *Ask the Cognitive Scientist* series. I could not retrieve
the 2006 piece itself through ERIC, Crossref or OpenAlex this session. It should be cited
as an accurate and influential trade restatement of the primary work, never as independent
evidence. `OBSERVED` (trade synthesis; the specific 2006 article was **not retrievable** by
the queries listed in §4).

The critical review. Smith, Snow, Serry & Hammond (2021), *Reading Psychology*,
`10.1080/02702711.2021.1888348`, ERIC EJ1291657. 23 studies of background knowledge and
comprehension in mid-to-late primary children. Their conclusion is conditional rather than
sweeping: effects are moderated by text type, by the quality of the situation model
required, **and by the presence of reader misconceptions**; readers with lower background
knowledge benefit more from high-cohesion text; weaker readers can partly compensate for
weak reading skill when background knowledge is high. `MEASURED-META` (systematic critical
review, no pooled estimate).

The misconception moderator deserves a line to itself. Background knowledge is not a
monotonic good — a confident wrong model can degrade comprehension of a correct text. A
tutor that "activates prior knowledge" without checking whether the prior knowledge is true
has a plausible mechanism for making things worse.

Now the intervention evidence, which is where the popular claim overreaches.

*Hwang, Cabell & Joyner (2022), Scientific Studies of Reading, ERIC EJ1360566.* 35
(quasi)experimental studies of integrated literacy and content-area instruction, K–5,
random-effects:

| Outcome | ES |
|---|---|
| Vocabulary (all measures) | 0.91 |
| Content knowledge | 0.89 |
| Comprehension (all measures) | 0.40 |
| Comprehension, standardised | 0.25 |
| Vocabulary, standardised | not significant |

`MEASURED-META`. No moderators reached significance, which the authors attribute to the
small study count.

*Kim, Burkhauser, Relyea, Gilbert, Scherer & Fitzgerald (2023), JEP, ERIC EJ1373030.* The
Model of Reading Engagement, a sustained content literacy intervention running from Grade 1
into Grade 2. **30 schools, 2,952 students, 144 teachers, randomised at school level.**
Treatment students lost less over the summer on a domain-general reading measure and
outperformed controls on science content reading comprehension at **ES = 0.18**, with the
effect varying by how many directly taught words appeared in the passage (near-, mid-, and
far-transfer). `MEASURED-RCT`.

*Cabell, Kim, White, Gale, Edwards & Hwang (2025), JEP, ERIC EJ1507087.* Two RCTs, the
second a replication, 47 schools, 1,194 kindergarteners, Core Knowledge Language Arts
Knowledge Strand versus waitlist. Significant impacts on **proximal vocabulary and science
and social studies knowledge**. Listening comprehension is named in the title and does not
appear in the list of significant impacts. And the interaction runs the wrong way for
equity: *"children who began the year with relatively higher receptive vocabulary scores
derived a greater benefit."* `MEASURED-RCT` ×2.

**The awkward consequence, stated plainly.** The commission asked whether the
knowledge-over-strategies finding, if it holds, means a tutor that teaches comprehension
strategies is doing the small thing and a tutor that builds knowledge is doing the large
one. On the retrieved evidence, **the finding does not hold at that magnitude**. Line the
standardised-outcome estimates up:

| Intervention family | Standardised comprehension outcome |
|---|---|
| Whole-class strategy instruction (Okkinga, k = 125) | 0.186 |
| Struggling-reader interventions 1980–2011 (Scammacca, k = 82) | 0.21 |
| Content-rich integrated instruction (Hwang, k = 35) | 0.25 |
| Sustained knowledge-building RCT (Kim, N = 2,952) | 0.18 |
| Reciprocal teaching (Rosenshine & Meister 1994, as reported in Graham & Hebert 2011) | 0.32 |

Every one of these sits between 0.18 and 0.32. Nothing in this table licenses "knowledge
has a large effect and strategies a small one." What the table does license is a different
and more defensible claim: **the two families deliver about the same on the comprehension
outcome, and only one of them also produces content knowledge at ES ≈ 0.89.** Knowledge-building
wins on the second outcome, not the first. For a tutor whose learner has to pass a science
test as well as read a passage, that is decisive, and it is decisive for a reason nobody
argues about. `INFERENCE`

**What would falsify it.** The claim above is that knowledge-building and strategy
instruction are indistinguishable on standardised comprehension and separable on content
knowledge. It is falsified by any adequately powered trial that randomises comparable
learners, over equated instructional hours, to (a) explicit comprehension-strategy
instruction on domain-general texts and (b) content-rich instruction in one domain, and
finds a between-arm difference on a standardised comprehension measure with a confidence
interval excluding zero in either direction. Time-on-task must be equated, because every
knowledge-building study above adds content time. If such a trial exists I did not find it;
see §5. `SPEC`

### 1.7 The reading nulls

**Reading First (Gamse, Jacob, Horst, Boulay & Unlu 2008, NCEE 2009-4038, ERIC ED503344).**
248 schools, 13 states, 18 sites, three school years, regression-discontinuity around the
funding eligibility cutoff. The programme **did** increase instructional time on the five
essential components in grades 1 and 2, **did** increase professional development, reading
coaches and support for struggling readers, and **did** improve first-grade decoding in one
year of testing. It produced **no statistically significant impact on reading comprehension
in grades one, two or three.** `MEASURED-RCT` (RD design).

This is the largest test in existence of the proposition that delivering the NRP components
with fidelity and dosage produces readers, and it came back null on the outcome anyone
cares about. It belongs beside `H1`'s Balu 2015 RTI result as evidence that **a framework
can be implemented correctly and still not work**, and beside `H1` F5 (Fuchs) as evidence
that the missing ingredient is usually the decision rule and not the delivery.

**READ 180 (Kim, Samson, Fitzgerald & Hartry 2010, *Reading and Writing*, ERIC EJ898468).**
294 children in grades 4–6 randomly assigned to READ 180 or a district after-school
programme, four days per week for 23 weeks. *"There was no significant difference between
children in READ 180 and the district after-school program on norm-referenced measures of
word reading efficiency, reading comprehension, and vocabulary."* Positive effects on oral
reading fluency and attendance, restricted to Grade 4. `MEASURED-RCT`. The most widely sold
computer-assisted reading intervention in American schools, randomised, null on the
standardised measures.

---

## 2. Writing

### 2.1 The estimand problem, before any number

Nearly every effect size below is the same thing: **the rubric-scored holistic quality of a
composition, written during or immediately after the instruction, scored by human raters
blind to condition, compared with a control group that wrote under ordinary conditions.**
It is a good outcome. It is also, in almost every case, produced while the treatment is
still switched on. Very few writing studies administer a delayed post-test, and essentially
none of the AI studies administer an *unassisted* one. Read every number below with that
attached.

### 2.2 Writing Next, and the elementary replication

**Graham & Perin (2007), *Journal of Educational Psychology* 99(3):445–476,
`10.1037/0022-0663.99.3.445`.** Grades 4–12, experimental and quasi-experimental studies.
**123 documents yielding 154 effect sizes for quality of writing.** Average weighted effect
sizes, verbatim from the abstract:

| Element | ES |
|---|---|
| Strategy instruction | 0.82 |
| Summarisation | 0.82 |
| Peer assistance | 0.75 |
| Setting product goals | 0.70 |
| Word processing | 0.55 |
| Sentence combining | 0.50 |
| Inquiry | 0.32 |
| Prewriting activities | 0.32 |
| Process writing approach | 0.32 |
| Study of models | 0.25 |
| Grammar instruction | −0.32 |

`MEASURED-META`. The Carnegie report of the same work (*Writing Next*, ERIC ED517367) uses
a wider net — 582 documents screened, 142 studies included, 176 effect sizes — because it
folds in the separate writing-to-learn analysis and reports writing for content learning at
0.23. **Cite the JEP paper for the effect sizes and the Carnegie report for the prose.**
Two different study counts for the same project circulate and neither is wrong.

The report body carries four qualifications that get dropped whenever this table is
reproduced:

- Strategy instruction is **larger for weak writers**: 1.02 for low-achieving writers versus
  0.70 across the full ability range. Self-Regulated Strategy Development specifically ran
  **1.14 against 0.62 for non-SRSD** strategy approaches.
- The process writing approach's 0.32 is a mixture. *"When teachers had such training, the
  effect was moderate (0.46), but in the absence of training the effect was negligible."*
  Five of the six trained-teacher studies were conducted **by the National Writing Project
  to support its own work**, with no random assignment in any of them, and NWP as a research
  partner. The report says so itself.
- Word processing is also a mixture: 0.51 general, 0.70 for low-achieving writers.
- Only four elements had ten or more effect sizes: strategy instruction, word processing,
  process writing, and grammar instruction. The last of those is the negative one.

**Graham, McKeown, Kiuhara & Harris (2012), *JEP*, `10.1037/a0029185`** repeats the exercise
for elementary grades: 115 documents, 13 interventions each requiring at least four
studies. Strategy instruction 1.02, adding self-regulation 0.50, text structure 0.59,
creativity/imagery 0.70, transcription skills 0.55, prewriting 0.54, peer assistance 0.89,
product goals 0.76, assessing writing 0.42, word processing 0.47, extra writing 0.30,
comprehensive programmes 0.42; SRSD 1.17, process approach 0.40. Grammar instruction was
the only one of the six
explicit-teaching interventions that failed to reach significance. `MEASURED-META`. Note
the 2012 correction notice, `10.1037/a0029939`, which is on the record.

**The grammar result is the null this section owes.** Traditional grammar instruction, with
more than ten effect sizes behind it, produced a statistically significant negative effect
on writing quality in the adolescent meta-analysis and a non-significant one in the
elementary meta-analysis. The report's own gloss is that sentence combining is the
functioning replacement. Any AI writing tutor whose default move is to explain a grammar
rule is implementing the one element in the table with a minus sign.

### 2.3 The process-writing null, given its own space

**Graham & Sandmel (2011), *Journal of Educational Research*, ERIC EJ947129.** 29
experimental and quasi-experimental studies, grades 1–12, of the process approach — the
single most widely adopted method of teaching writing in English-speaking schools.

- General-education classes: average weighted **ES = 0.34** on overall writing quality,
  statistically significant, described by the authors as relatively modest.
- Variation in effect size was **not** related to grade, reliability of the quality measure,
  professional development, genre, or study quality.
- *"The process writing approach neither resulted in a statistically significant improvement
  in students' motivation nor enhanced the quality of struggling writers' compositions."*

`MEASURED-META`. Two nulls inside one meta-analysis: motivation, which the method is
principally marketed on, and struggling writers, who are the population it is most often
prescribed for.

### 2.4 Writing as a tool for learning, and for reading

This is the part of the writing literature the commission was right to call
better-evidenced, and it is the part with the clearest implication for an AI tutor.

**Graham, Kiuhara & MacKay (2020), *RER*, ERIC EJ1249514.** k = 56 experiments, grades 1–12,
writing about content in science, social studies and mathematics, with a control condition
that did not use writing to support learning and with instructional time and content
coverage equated. **ES = 0.30** on content learning. Equally effective across the three
subjects and across elementary, middle and high school; **not moderated by any feature of
the writing activity, the instruction, or the assessment**, and not related to study
quality. `MEASURED-META`.

The absence of moderators is the useful part. Whatever writing-to-learn is doing, it is not
sensitive to the format of the writing task, which means a tutor does not need to get the
prompt design clever to get the effect.

**Graham & Hebert (2011), *Harvard Educational Review*, `10.17763/haer.81.4.t2k0m13756113566`.**
Writing about text read: **ES = 0.40** on published standardised norm-referenced tests (11
studies) and **0.51** on researcher-designed tests (50 studies); 57 of 61 outcomes positive.
Increasing how much students write: **0.30** on standardised measures. The report's own
calibration is worth reproducing, because it sets the scale for every comprehension claim
in §1: writing about text at 0.40 exceeded Slavin et al.'s 0.17 for secondary reading
programmes and Elleman et al.'s 0.10 for vocabulary instruction, and matched Rosenshine &
Meister's 0.32 for reciprocal teaching. `MEASURED-META` (the three comparison figures are
`MEASURED-META` **as reported in** Graham & Hebert; I did not retrieve those three sources
independently).

And its null. In twelve studies with lower-achieving students, writing about text ran
0.63 — *"However, the average weighted effect size for writing about text activities was not
greater than zero when lower-achieving students were not explicitly taught how to use
them."* Assigning the writing does nothing for a weak writer. Teaching the writing does.

**Graham, Liu, Bartlett, Ng, Harris et al. (2018), *RER*,
`10.3102/0034654317746927`** closes the loop in the other direction: reading interventions
improve writing, overall ES **0.57** (k = 54, 5,018 students), writing quality **0.63**,
**maintained over time at 0.37**. `MEASURED-META`. That maintenance figure is one of the few
delayed estimates in this whole report.

### 2.5 Feedback, and the finding this corpus has never connected

The writing-specific meta-analysis. Graham, Hebert & Harris (2015), *Elementary School
Journal*, ERIC EJ1068976. True and quasi-experiments, grades 1–8, outcome is writing
quality. Average weighted effect sizes by feedback source:

| Source | ES |
|---|---|
| Adults | 0.87 |
| Self | 0.62 |
| Peers | 0.58 |
| Computers | 0.38 |

And the two nulls in the same paper: *"We did not find, however, that teachers' monitoring
of students' writing progress or implementation of the 6 + 1 Trait Writing model
meaningfully enhanced students' writing."* `MEASURED-META`.

Teacher progress-monitoring producing nothing is the same result as `H1` F5 (Fuchs, Hamlett
& Stecker 1991): measurement without a prescribed change of instruction is inert. Two
independent literatures, reading measurement and writing assessment, reached it separately.

The estimand trap in the feedback literature. Huisman, Saab, van den Broek & van Driel
(2019, *AEHE*, ERIC EJ1209907) synthesised 24 studies of peer feedback on higher-education
academic writing and reported three different answers depending on the comparison:

| Peer feedback versus | Hedges' g | 95% CI |
|---|---|---|
| No-feedback control | 0.91 | [0.41, 1.42] |
| Self-assessment | 0.33 | [0.01, 0.64] |
| Teacher feedback | 0.46 | [−0.44, 1.36] |

`MEASURED-META`. Same intervention, same outcome, three effect sizes spanning an order of
magnitude, and the comparison against teacher feedback has a confidence interval nearly two
units wide. Vuogan & Li (2023, *TESOL Quarterly*, ERIC EJ1399091) get d = 0.73 [0.54, 0.92]
across 26 L2 studies with a further wrinkle: peer feedback had **greater effects on
revisions than on new compositions**. Feedback improves the thing it was given about more
than it improves the next thing.

**Kluger & DeNisi (1996), *Psychological Bulletin* 119(2):254–284,
`10.1037/0033-2909.119.2.254`.** Abstract retrieved verbatim via OpenAlex (PsycNet returned
a loading shell and is unreachable):

> "Since the beginning of the century, feedback interventions (FIs) produced negative — but
> largely ignored — effects on performance. A meta-analysis (607 effect sizes; 23,663
> observations) suggests that FIs improved performance on average (d = .41) but that **over
> 1/3 of the FIs decreased performance.** This finding cannot be explained by sampling
> error, feedback sign, or existing theories. … The central assumption of FIT is that FIs
> change the locus of attention among 3 general and hierarchically organized levels of
> control: task learning, task motivation, and meta-tasks (including self-related)
> processes. The results suggest that **FI effectiveness decreases as attention moves up the
> hierarchy closer to the self and away from the task.**"

`MEASURED-META`. Zero hits for `Kluger` across every report and survey section in the
corpus before this one (censused 2026-07-30).

A traceability note, because two numbers circulate. Wisniewski, Zierer & Hattie (2020,
*Frontiers in Psychology*, `10.3389/fpsyg.2019.03087`) describe Kluger & DeNisi as *"based
on 131 studies, over 12,000 participants, with an average effect of 0.38, noting that about
a third of the effects were negative."* The primary abstract says 607 effect sizes, 23,663
observations, d = .41. The 131 figure is the paper's study count and the 12,000 is not the
observation count. **Use the primary numbers.** Wisniewski et al.'s own synthesis — 435
studies, 994 effect sizes, over 61,000 subjects — reports **d = 0.48 [0.44, 0.51]** overall,
with the composition that matters: reinforcement and punishment **0.24 [0.06, 0.43]**,
corrective feedback **0.46 [0.39, 0.55]**, high-information feedback **0.99 [0.82, 1.15]**;
cognitive outcomes 0.51, motivational outcomes 0.33; and **17% of all effects negative**,
rising to 21% for motivational outcomes. `MEASURED-META`.

**Why this is load-bearing for anything that generates essay feedback at scale.** A returned
essay carrying a grade, a rubric score, or a global judgement of quality is the textbook
self-level feedback intervention in Kluger and DeNisi's hierarchy: it tells the writer
something about the writer. Their result says that the more feedback points at the person
and the less it points at the next revision move, the worse it does, and that a third of the
time it does harm. Generative systems make this failure cheap and unlimited. Every essay,
every draft, instantly, with a score and a paragraph of encouragement.

Three testable design rules come out of this. `INFERENCE` from Kluger & DeNisi 1996 +
Wisniewski et al. 2020 + Graham, Hebert & Harris 2015:

1. **No global quality judgement returned to the learner.** Scores may drive routing
   internally; they should not be surfaced. The 0.99 cell is high-information feedback, the
   0.24 cell is reinforcement and punishment, and a holistic score is the latter wearing the
   former's clothes.
2. **Feedback names the next move on this text.** "Your second paragraph asserts X and the
   evidence you gave supports Y — add the missing step or change the claim" is task-level.
   "Your development is a 3" is self-level.
3. **Cap the number of comments.** Nothing in the retrieved literature sets the cap; the
   attention-hierarchy mechanism predicts that past some volume the learner stops processing
   moves and starts processing the verdict. This is `SPEC` and it is worth measuring.

### 2.6 What automated writing evaluation actually measures

`C2-assessment-psychometrics.md` §8.2 owns the psychometric half of this — human–machine
agreement, quadratic weighted kappa, e-rater's operational evaluations, Perelman's 2014
re-analysis of the ASAP competition, and Jiao, Song & Lee's Many-Facet Rasch treatment of
LLM raters. That material is not repeated. What follows is the instructional half.

**The length result, from the primary.** Perelman, "Construct Validity, Length, Score, and
Time in Holistically Graded Writing Assessments," WAC Clearinghouse,
`10.37514/per-b.2012.0452.2.07`, extracted from the open PDF:

> "Although length appears to predict 40-60% of the shared variance for essays written in 25
> minutes, as the time allotted increases, the correlation between length and score
> decreases significantly. When students have one hour to write, the shared variance
> predicted by length decreases to approximately 20%, and when students are given 72 hours,
> length predicts 10% or less of the shared variance of the holistic score."

He adds an untimed case: a first-year psychology assignment with a 1,250-word limit showed
**1.7%** shared variance between grade and length (Norton 1990). `OBSERVED` (synthesis of
College Board research reports plus the author's own MIT assessments).

The mechanism is documented rather than inferred. In e-rater the organisation feature is
the count of discourse elements, and the development feature is *"average length of each
discourse element in words"*; Perelman reports that Attali and Powers found the correlation
between both features and total word count so strong that **word count could be substituted
for both**. And e-rater will not credit more than three supporting points, which is the
five-paragraph essay hard-coded as a scoring construct.

**The critical qualification, so this section is not itself skewed.** The length effect is
largely a property of the *timed impromptu*, not of machine scoring. Perelman's own data
show it collapsing as time increases and nearly vanishing when students write about
something they know. A tutoring system does not administer 25-minute impromptus, so the
sharpest version of the critique does not transfer to it unmodified. What does transfer is
the construct question: if the machine's "development" is a word count, then a learner who
optimises against it learns to produce words.

**The gaming result, updated to the current generation.** Perelman (2020, *Journal of
Writing Assessment*) reports that ETS built an advisory to flag BABEL-generated text, and
that the newer e-rater *"still appears to reward lexically complex, but nonsensical
essays."* `OBSERVED` (the JWA article was reachable only through its OpenAlex abstract;
eScholarship returned a challenge page).

The stronger and more recent result comes from inside the AWE research community. **Myers &
Wilson (2023), *International Journal of Artificial Intelligence in Education*, ERIC
EJ1388568.** 100 persuasive essays by grade 7–8 students, each randomised at the sentence
level 30 times with an NLTK script, n = 3,000 randomisations, scored by the MI Write AWE
system on six traits. Sentence-order randomisation destroys idea development and
organisation by construction, so those trait scores should collapse. They did not:

> "Overall, complete randomizations did not consistently significantly impact trait scoring
> for these high-level writing traits. In fact, **more than a third of the essays saw
> significant increases in one or both high-level traits despite randomization**, indicating
> a disconnect between MI Write's formative feedback and its underlying constructs."

`MEASURED-BENCH`. This is the BABEL demonstration rebuilt as a controlled ablation, on a
system marketed for classroom formative feedback, published in an AI-in-education venue, by
authors whose other work is broadly positive about AWE. It is the single most citable piece
of evidence that AWE trait feedback on high-level writing constructs is not measuring those
constructs.

Corroborating from the NLP side: Kabra et al. (2023, *Dialogue & Discourse*,
`10.5210/dad.2023.101`) find that deep AES models with contextual embeddings
*"behave like bag-of-words models. A few words determine the essay score without the
requirement of any context,"* producing simultaneous overstability and oversensitivity.
`MEASURED-BENCH`.

### 2.7 Does anything survive the tool being removed?

This is the question the commission put at the centre, and the writing literature has an
answer for the pre-generative tools. It has been answered three times, by the same research
group, in the same direction, including once under randomisation.

**Wilson, Olinghouse & Andrada (2014), *Learning Disabilities: A Contemporary Journal*, ERIC
EJ1039856.** Statewide computer-based benchmark writing assessment with automated scoring
and feedback, grades 4–8, three-level HLM. Writing quality improved across revisions, and
*"growth decelerated over time."* On transfer: **"No significant transfer effects were
observed"** — neither improved first-draft performance nor accelerated growth on a follow-up
prompt. `OBSERVED` (statewide observational, not randomised).

**Wilson (2017), *Reading and Writing*, ERIC EJ1133697.** PEG Writing; **n = 1,196**,
students with disabilities and typically developing students matched on prior writing
achievement, with a transfer subsample of **n = 655** given a follow-up prompt. Students with
disabilities produced weaker first drafts, grew faster, and closed the quality gap **after
five revisions**. And: **"There was no evidence of transfer for either group of students."**
`OBSERVED`.

**Wilson & Roscoe (2020), *Journal of Educational Computing Research*, ERIC EJ1241689.** The
randomised one. Sixth graders randomly assigned **by classroom** to PEG Writing (n = 56) or
Google Docs word processing (n = 58); four outcomes; path analysis controlling for pretest.
**Composing condition had no effect on holistic writing quality.** Students in the AWE
condition had higher writing self-efficacy and better state ELA test performance, with
self-efficacy partially mediating the test effect. `MEASURED-RCT`.

Read those three together. Revision quality goes up, self-efficacy goes up, a distal test
score goes up, and the thing the learner can do on a blank page tomorrow does not move. That
is the exact shape of the Bastani result this corpus already carries, arrived at
independently, in a different subject, with a different tool generation, and against a
different comparison condition. `Z1` §2.3 records that Bastani has not been replicated with
a withdrawal design in fourteen months. The AWE transfer literature is not a replication —
it is a different intervention and a weaker design — and it is the closest converging
evidence in the corpus, and it points the same way.

**The base rate, so this is not overstated.** Nunes, Cordeiro, Limpo & Castro (2022,
*JCAL*, ERIC EJ1327602) systematically reviewed AWE in school settings, 2000–2020, PRISMA:
**eight studies, six systems, 1,659 students aged 11–17.** *"Except for one, all studies
showed a positive effect of automated feedback in at least one writing-related measure."*
`MEASURED-META` (systematic review, no pooled estimate). Twenty years of K–12 AWE research
is eight studies. Any strong claim in either direction is running ahead of the evidence.

The larger AWE meta-analyses are dominated by adult second-language learners and by
within-subject designs, and their numbers should not be transported to a K–12 first-language
tutor. Zhai & Ma (2023, *JECR*, ERIC EJ1380424): 26 studies, 2,468 participants, **g = 0.861**
on writing quality, larger for post-secondary than secondary and larger for EFL/ESL than
native speakers. Ngo, Chen & Lai (2024, *ILE*, ERIC EJ1419671), three-level: **between-group
g = 0.59** from 24 studies versus **within-group g = 0.98** from 34 studies. `MEASURED-META`
×2. The between/within gap is the size of the maturation-plus-practice effect that a
within-subject design cannot separate from the tool.

### 2.8 Generative-AI feedback, and the trial nobody has run

**Steiss, Tate, Graham, Cruz & Hebert (2024), *Learning and Instruction*,
`10.1016/j.learninstruc.2024.101894`.** 200 secondary student essays; human and ChatGPT
feedback scored on five quality dimensions — criteria-based, clear directions for
improvement, accurate, prioritises essential features, supportive tone. *"Human raters were
better at providing high-quality feedback to students in all categories other than
criteria-based. Considering the ease of generating feedback through ChatGPT and its overall
quality, practical differences between humans and ChatGPT were not substantial."*
`MEASURED-BENCH`. This measures the **quality of the feedback artifact**, judged by trained
raters. It does not measure whether any student wrote better afterwards.

**Yan (2024), *Language Learning & Technology*, `10.64152/10125/73597`.** 117 EFL sophomores,
six teachers, seven weeks, four conditions differing in how ChatGPT feedback was processed:
individually, with a teacher, with peers, or both. Two outcomes were separated — task
improvement (draft-to-final gain on the three intervention tasks) and learning (performance
on a **new post-intervention writing task**). *"The learners who individually processed
feedback registered the most significant task improvements, whereas learners processing
feedback with teacher collaboration progressed the most for subsequent learning."*
`MEASURED-RCT` (assignment procedure not fully specified in the abstract; treat as
quasi-experimental until the method section is read).

This is the closest published thing to the design the commission asked for, and it splits
the way the theory predicts: the arm that got the most out of the AI on the assisted task
got the least on the unassisted one. The new task was still administered immediately, in
the same course, and not with the tool withheld as a manipulation.

**The EEG preprint, discounted and labelled.** Kosmyna et al., *Your Brain on ChatGPT:
Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task*,
arXiv:2506.08872. Three conditions — LLM, search engine, brain-only — over three sessions,
with a fourth crossover session in which LLM users were reassigned to brain-only. **54
participants in sessions 1–3; 18 completed session 4.** LLM users showed the weakest EEG
connectivity, the lowest self-reported ownership of their essays, and struggled to quote
their own work; the LLM-to-Brain group showed reduced alpha and beta connectivity in session
4. `OBSERVED` (preprint, not peer-reviewed). A published comment (arXiv:2601.00856) raises
sample size, reproducibility, EEG methodology, inconsistent reporting and transparency. The
crossover is the right instinct and n = 18 with EEG connectivity as the primary outcome
cannot carry the claim. Report it as the nearest attempt and not as evidence.

**`OBSERVED — absence`: the trial does not exist.** Across ERIC (`title:"AI" AND
title:"writing" AND title:"transfer"` → 0; `title:"generative AI" AND title:"writing" AND
title:"randomized"` → 0; `title:"automated feedback" AND title:"writing" AND
title:"experiment"` → 0; `title:"artificial intelligence" AND title:"writing" AND
title:"dependence"` → 0), Crossref `query.title` on *"randomized controlled trial students
write essays with and without AI assistance independent posttest"* and *"AI assistance essay
writing subsequent unassisted performance"*, and OpenAlex free-text search on
*"ChatGPT essay writing randomized controlled trial delayed posttest without AI assistance
transfer"* and *"AI writing assistance dependence students perform worse when tool
removed"*, **I could not locate a single randomised trial of generative-AI writing support
with a delayed, unassisted post-test on a new composition.** The result set is dominated by
EFL quasi-experiments with pre/post designs, no control group or a non-equivalent one, and
sample sizes between 30 and 120. Term censuses miss synonyms; this means *not found by
these queries*, never *does not exist*.

**The trial that should be run** is specified in §3.3.

---

## 3. What is now buildable

### 3.1 A four-way reading router, which `J1` does not have

The simple view plus the effect sizes above give a tutor a decision procedure it can execute
from ordinary interaction data. `SPEC`, assembled from `MEASURED-META` components:

| Observed | Likely locus | Move | Evidenced at |
|---|---|---|---|
| Slow or inaccurate word reading; errors are phonologically plausible | Decoding | Explicit systematic decoding (see `H1` §1.1) | d = 0.41 overall, 0.55 if early |
| Accurate but effortful reading; comprehension recovers when the text is read aloud to the child | Fluency | Repeated reading with listening passage preview | 0.41 aggregate; 0.35 on comprehension |
| Fluent reading; comprehension fails only on unfamiliar topics | Knowledge | Content-rich instruction in the domain, then re-read | 0.25 standardised comp., 0.89 content knowledge |
| Fluent reading, familiar topic, literal recall intact, inference fails | Inference | Explicit inference instruction, small group | 0.58 general; 0.97 literal for weak readers |

The listening-comprehension probe in row two is the operationally important one and it is
free for a system that can already read aloud: administer the same passage by text and by
audio and compare. A gap says decoding; no gap says the problem is downstream. This is the
simple view used as an instrument rather than as a slogan.

Two guards. Route on **at least four data points before changing method**, per `H1` F6 (Van
Norman et al. 2023: trend-based non-response judgements are not viable for 7–10 weeks on
weekly probes). And check whether the "background knowledge" the system is about to activate
is *correct*, per Smith et al. 2021 — a confident misconception is a documented moderator in
the wrong direction.

### 3.2 The writing system, and what it should refuse to do

Buildable from the above, with the evidence attached:

- **Default writing task is writing about content the learner is studying.** ES = 0.30 on
  content learning, unmoderated by task features; ES = 0.40 on standardised reading
  comprehension. It is the only writing intervention in this report that pays twice.
- **Teach the writing activity before assigning it.** Graham & Hebert's null: writing about
  text has an effect **not greater than zero** for lower-achieving students who were not
  taught how to do it.
- **Strategy instruction with self-regulation is the highest-yield teaching move** (SRSD
  1.14 adolescent / 1.17 elementary), and it is larger for weak writers than strong ones.
  It is also the element with the most studies behind it.
- **Do not teach grammar as a standalone unit.** ES = −0.32. Use sentence combining (0.50).
- **Never return a holistic quality score to the learner.** Kluger & DeNisi's hierarchy plus
  Wisniewski's 0.24 reinforcement cell against 0.99 high-information cell.
- **Do not claim the tool teaches writing until an unassisted probe says so.** Three studies
  and one RCT say revision quality and self-efficacy rise while transfer does not.

The last one is an architectural requirement and not a policy preference: the system must
periodically administer a **cold prompt** — new topic, no assistance, no feedback, scored
against the same rubric — and must report *that* number, not the assisted one, as its
learning claim. This is cheap. It is also the measurement that would have caught the AWE
transfer failure fifteen years earlier than it was reported.

### 3.3 The single highest-value experiment, with power

**Design.** Three arms, randomised at the learner level within class, over one term.
(A) unguarded AI writing assistance — the learner may ask for drafting, rewriting and
feedback without restriction; (B) guarded assistance — task-level feedback only, no
generated prose, no holistic score, structured after `H1` F5's expert-system pattern of
prescribing the next move; (C) no AI, ordinary instruction with teacher feedback. All three
write the same number of compositions on the same prompts. **Primary outcome: a delayed,
unassisted, cold-prompt composition written four weeks after the last session, on a new
topic, scored by blinded human raters on the standard rubric.** Secondary outcomes: the
assisted compositions during the term (to establish that the assistance worked at all, which
is what every existing study measures), and a content-knowledge test on the topics written
about, since writing-to-learn predicts a second effect.

**Power.** The reference effect is Bastani's unguarded arm, a 17% grade reduction relative
to never-had-access. Translating a 17% grade shift into an SD requires the grade SD, which
the PNAS abstract does not give, so I do not do the translation. Instead, power to the
smallest difference that would change a build decision. Writing-quality rubric scores in the
Graham meta-analyses carry pooled SDs consistent with a detectable minimum around d = 0.30,
which is also the size of the writing-to-learn effect and of the AWE between-group estimate
minus its within-group inflation. For a two-sided α = .05 and 80% power on a pairwise
contrast at **d = 0.30**, each arm needs **n = 175** (the standard 2(z_{α/2}+z_β)²/d² =
15.7/d² approximation, ⌈15.7/0.09⌉ = 175), so 525 learners for three arms. Correcting for
two pairwise comparisons at Bonferroni α = .025 raises it to **212 per arm, 636 total**. If randomisation is by class rather
than learner, a design effect of 1 + (m − 1)ρ with clusters of m = 25 and an ICC of
ρ = 0.15 for writing achievement multiplies this by 1 + 24(0.15) = 4.6, giving **≈ 2,930
learners across 117 classes** — which is why learner-level randomisation within class is the design, and why the
assistance condition has to be enforced technically rather than by instruction. A trial half
this size can still rule out the *large* harm; it cannot rule out the harm that matters,
which is a quarter of a standard deviation on what the child can do alone.

**What it would settle.** Whether the −17% withdrawal effect is a property of unguarded AI
assistance in general or of mathematics practice specifically; whether the guardrail result
("harm removed, not benefit added") reproduces in a domain where the AI can do the whole
task rather than just the answer; and whether AWE's fifteen-year transfer null was a
property of weak automated feedback or of automated feedback as such.

---

## 4. Null and negative results ledger

| # | Null / negative | Source |
|---|---|---|
| N1 | Reading First: no significant impact on reading comprehension in grades 1–3 across 248 schools, despite significant impacts on instructional time, professional development, coaching, and grade-1 decoding | Gamse et al. 2008, NCEE 2009-4038 |
| N2 | READ 180: no significant difference from a district after-school programme on norm-referenced word reading, comprehension or vocabulary, n = 294 randomised | Kim et al. 2010 |
| N3 | Encouraging independent silent reading: no clear evidence of benefit; 60 additional hours of reading produced no clear gain | NRP 2000, Chapter 3 |
| N4 | Comprehension-strategy instruction in whole classrooms: d = 0.186 on standardised comprehension against d = 0.786 on strategy use | Okkinga et al. 2018 |
| N5 | Inference instruction is near-inert for skilled readers: d = 0.06 on literal comprehension | Elleman 2017 |
| N6 | Content-rich literacy curriculum: significant on proximal vocabulary and content knowledge, and the benefit was larger for children who started with higher vocabulary | Cabell et al. 2025 |
| N7 | Traditional grammar instruction: ES = −0.32 on writing quality, from the intervention family with the most effect sizes | Graham & Perin 2007 |
| N8 | Process writing approach: no significant improvement in motivation and none in struggling writers' composition quality | Graham & Sandmel 2011 |
| N9 | Teacher progress-monitoring of writing, and the 6+1 Trait model: no meaningful enhancement of student writing | Graham, Hebert & Harris 2015 |
| N10 | Writing about text: effect not greater than zero for lower-achieving students not taught how to do it | Graham & Hebert 2011 |
| N11 | AWE: no effect on holistic writing quality in a randomised classroom trial (n = 114) | Wilson & Roscoe 2020 |
| N12 | AWE: no evidence of transfer to unassisted first drafts, twice, including at n = 1,196 | Wilson et al. 2014; Wilson 2017 |
| N13 | AWE construct validity: sentence-level randomisation did not consistently reduce idea-development or organisation trait scores; >1/3 of essays scored significantly higher after scrambling | Myers & Wilson 2023 |
| N14 | Peer feedback versus teacher feedback on academic writing: g = 0.46, 95% CI [−0.44, 1.36] — no distinguishable difference | Huisman et al. 2019 |
| N15 | Over one third of all feedback interventions reduced performance | Kluger & DeNisi 1996 |
| N16 | Reading intervention effects declined from 0.95 to 0.49 (and 0.42 to 0.21 on standardised measures) between the 1980–2004 and 2005–2011 study cohorts, partly because business-as-usual instruction improved | Scammacca et al. 2015 |

---

## 5. What I could not find out

**The head-to-head knowledge-versus-strategies trial.** §1.6 states a falsifiable claim and
the trial that would settle it does not appear in ERIC or Crossref under any phrasing I
tried. Every knowledge-building study adds instructional time in a content area, and every
strategy study adds instructional time on strategies, so the two literatures have never been
run against each other with hours equated. Until they are, the ranking everyone asserts is
an inference from two separately-run programmes.

**Willingham 2006 itself.** The most-circulated statement of the knowledge case is a trade
magazine column I could not retrieve through any of the three bibliographic APIs available
this session. The primary work it summarises is retrievable and is cited above. The column
should not be cited as evidence.

**Kluger & DeNisi's full text.** Only the abstract was reachable — verbatim, which is enough
for the headline numbers, and not enough to report the moderator table or the study-level
inclusion criteria. PsycNet returned a loading shell to WebFetch. The 131-study figure that
circulates comes from the body and I could not verify it directly; I report the abstract's
607 effect sizes and 23,663 observations instead, and flag that Wisniewski et al. restate
both the n and the d incorrectly.

**Perelman's 2020 BABEL follow-up.** Reachable only as an OpenAlex abstract; eScholarship,
which hosts the *Journal of Writing Assessment*, returned a challenge page to both `curl`
and WebFetch. The 2012 chapter with the length data was open and is quoted directly.

**Any generative-AI writing trial with an unassisted delayed post-test.** §2.8 gives the
queries. This is the gap that matters, and it is the gap this project is best placed to
close, because it can enforce the assistance condition in software and can administer a cold
prompt at zero marginal cost. Fifteen years of automated writing evaluation research
converged on a transfer null that its own field did not treat as disqualifying. The
generative generation is repeating the design that produced it: measure the draft in front
of you, report the rubric score, and never ask what the learner can do on a blank page four
weeks later.

---

## References

**Reading — models and syntheses**

1. Hoover, W. A., & Gough, P. B. (1990). The simple view of reading. *Reading and Writing*, 2, 127–160. `10.1007/bf00401799`. `OBSERVED`
2. Kendeou, P., Savage, R., & van den Broek, P. (2009). Revisiting the simple view of reading. *BJEP*. `10.1348/978185408x369020`. `MEASURED-BENCH`
3. Zhang, et al. (2020). Simple View of Reading in Chinese: A one-stage meta-analytic SEM. *RER*. `10.3102/0034654320964198`. `MEASURED-META`
4. Gustafson, S., Samuelsson, C., Johansson, E., & Wallmann, J. (2013). How simple is the Simple View of Reading? *SJER*. `10.1080/00313831.2012.656279`. `OBSERVED`
5. Snow, C. E. (2018). Simple and not-so-simple views of reading. *RSE*, ERIC EJ1191980. `OBSERVED`
6. National Reading Panel (2000). *Teaching Children to Read*, NICHD. Chapter 3 (fluency, meta-analytic) and Chapter 4 (comprehension, explicitly not meta-analysed). Full report retrieved and text-extracted this session. `MEASURED-META` / `OBSERVED`
7. Suggate, S. P. (2016). A meta-analysis of the long-term effects of phonemic awareness, phonics, fluency, and reading comprehension interventions. *JLD*, ERIC EJ1083414. `MEASURED-META`
8. Torgerson, C., Brooks, G., Gascoine, L., & Higgins, S. (2019). Phonics: reading policy and the evidence of effectiveness from a systematic 'tertiary' review. *Research Papers in Education*, ERIC EJ1205323. `MEASURED-META`
9. Lee, J., & Yoon, S. Y. (2017). The effects of repeated reading on reading fluency for students with reading disabilities: a meta-analysis. *JLD*, ERIC EJ1129722. `MEASURED-META`
10. Okkinga, M., van Steensel, R., van Gelderen, A. J. S., van Schooten, E., Sleegers, P. J. C., & Arends, L. R. (2018). Effectiveness of reading-strategy interventions in whole classrooms: a meta-analysis. *EPR*, ERIC EJ1198360. `MEASURED-META`
11. Elleman, A. M. (2017). Examining the impact of inference instruction on the literal and inferential comprehension of skilled and less skilled readers. *JEP*, ERIC EJ1149970. `MEASURED-META`
12. Scammacca, N. K., Roberts, G., Vaughn, S., & Stuebing, K. K. (2015). A meta-analysis of interventions for struggling readers in grades 4–12: 1980–2011. *JLD*, ERIC EJ1064370. `MEASURED-META`

**Reading — knowledge**

13. Recht, D. R., & Leslie, L. (1988). Effect of prior knowledge on good and poor readers' memory of text. *JEP*, 80(1), 16–20. `10.1037/0022-0663.80.1.16`. Abstract retrieved verbatim via OpenAlex. `OBSERVED`
14. Smith, R., Snow, P., Serry, T., & Hammond, L. (2021). The role of background knowledge in reading comprehension: a critical review. *Reading Psychology*. `10.1080/02702711.2021.1888348`. `MEASURED-META`
15. Hwang, H., Cabell, S. Q., & Joyner, R. E. (2022). Effects of integrated literacy and content-area instruction on vocabulary and comprehension in the elementary years. *SSR*, ERIC EJ1360566. `MEASURED-META`
16. Kim, J. S., Burkhauser, M. A., Relyea, J. E., Gilbert, J. B., Scherer, E., & Fitzgerald, J. (2023). A longitudinal randomized trial of a sustained content literacy intervention from first to second grade. *JEP*, ERIC EJ1373030. `MEASURED-RCT`
17. Cabell, S. Q., Kim, J. S., White, T. G., Gale, C. J., Edwards, A. A., & Hwang, H. (2025). Impact of a content-rich literacy curriculum on kindergarteners' vocabulary, listening comprehension, and content knowledge. *JEP*, ERIC EJ1507087. `MEASURED-RCT` ×2
18. Mosher, D. M., & Kim, J. S. (2023). Structured read-aloud supplements and reading comprehension transfer. EdWorkingPaper 23-847, ERIC ED639223. `MEASURED-RCT`
19. Willingham, D. T. *How Knowledge Helps*, *American Educator* (2006). **Not retrievable** via ERIC, Crossref or OpenAlex this session. Cite as trade synthesis, never as evidence.

**Reading — nulls**

20. Gamse, B. C., Jacob, R. T., Horst, M., Boulay, B., & Unlu, F. (2008). *Reading First Impact Study: Final Report*, NCEE 2009-4038, ERIC ED503344. `MEASURED-RCT` (RD)
21. Kim, J. S., Samson, J. F., Fitzgerald, R., & Hartry, A. (2010). A randomized experiment of a mixed-methods literacy intervention for struggling readers in grades 4–6. *Reading and Writing*, ERIC EJ898468. `MEASURED-RCT` (null)

**Writing — instruction**

22. Graham, S., & Perin, D. (2007). A meta-analysis of writing instruction for adolescent students. *JEP*, 99(3), 445–476. `10.1037/0022-0663.99.3.445`. `MEASURED-META`
23. Graham, S., & Perin, D. (2007). *Writing Next*. Carnegie Corporation / Alliance for Excellent Education, ERIC ED517367. PDF retrieved and text-extracted this session. `MEASURED-META`
24. Graham, S., McKeown, D., Kiuhara, S., & Harris, K. R. (2012). A meta-analysis of writing instruction for students in the elementary grades. *JEP*. `10.1037/a0029185`; correction `10.1037/a0029939`. `MEASURED-META`
25. Graham, S., & Sandmel, K. (2011). The process writing approach: a meta-analysis. *Journal of Educational Research*, ERIC EJ947129. `MEASURED-META` (two nulls)
26. Graham, S. (2019). Changing how writing is taught. *Review of Research in Education*, ERIC EJ1217170. `OBSERVED`
27. Asaro-Saddler, K., Moeyaert, M., Xu, X., & Yerden, X. (2021). Multilevel meta-analysis of SRSD in writing for children with ASD. *Exceptionality*, ERIC EJ1296263. `MEASURED-META`

**Writing — for learning and for reading**

28. Graham, S., Kiuhara, S. A., & MacKay, M. (2020). The effects of writing on learning in science, social studies, and mathematics. *RER*, ERIC EJ1249514. `MEASURED-META`
29. Graham, S., & Hebert, M. (2011). Writing to read. *Harvard Educational Review*. `10.17763/haer.81.4.t2k0m13756113566`; Carnegie report PDF retrieved and text-extracted this session. `MEASURED-META`
30. Graham, S., Liu, X., Bartlett, B., Ng, C., Harris, K. R., Aitken, A., Barkel, A., Kavanaugh, C., & Talukdar, J. (2018). Reading for writing: a meta-analysis of the impact of reading interventions on writing. *RER*. `10.3102/0034654317746927`. `MEASURED-META`

**Feedback**

31. Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance. *Psychological Bulletin*, 119(2), 254–284. `10.1037/0033-2909.119.2.254`. Abstract retrieved verbatim via OpenAlex; full text unreachable. `MEASURED-META`
32. Wisniewski, B., Zierer, K., & Hattie, J. (2020). The power of feedback revisited. *Frontiers in Psychology*. `10.3389/fpsyg.2019.03087`. `MEASURED-META` ‡ (misreports Kluger & DeNisi's n and d — see §2.5)
33. Graham, S., Hebert, M., & Harris, K. R. (2015). Formative assessment and writing: a meta-analysis. *Elementary School Journal*, ERIC EJ1068976. `MEASURED-META`
34. Huisman, B., Saab, N., van den Broek, P., & van Driel, J. (2019). The impact of formative peer feedback on higher education students' academic writing: a meta-analysis. *AEHE*, ERIC EJ1209907. `MEASURED-META`
35. Vuogan, A., & Li, S. (2023). Examining the effectiveness of peer feedback in second language writing: a meta-analysis. *TESOL Quarterly*, ERIC EJ1399091. `MEASURED-META`
36. Lim, S. C., & Renandya, W. A. (2020). Efficacy of written corrective feedback in writing instruction: a meta-analysis. *TESL-EJ*, ERIC EJ1275821. `MEASURED-META` — the L2 corrective-feedback literature belongs to `R4`; noted here for the hand-off.
37. Lv, X., Ren, W., & Xie, Y. (2021). The effects of online feedback on ESL/EFL writing: a meta-analysis. *APER*, ERIC EJ1316613. `MEASURED-META` (teacher g = 2.248 vs automated g = 0.696; the teacher cell is implausibly large and should be treated as a diagnostic of the primary studies)

**Automated writing evaluation**

38. Perelman, L. (2012). Construct validity, length, score, and time in holistically graded writing assessments: the case against automated essay scoring. WAC Clearinghouse, `10.37514/per-b.2012.0452.2.07`. PDF retrieved and text-extracted this session. `OBSERVED`
39. Perelman, L. (2014). When "the state of the art" is counting words. *Assessing Writing*. `10.1016/j.asw.2014.05.001`. `OBSERVED` — carried from `C2` §8.2, not re-derived.
40. Perelman, L. (2020). The BABEL Generator and e-rater. *Journal of Writing Assessment*. Abstract via OpenAlex; full text unreachable (eScholarship challenge page). `OBSERVED`
41. Myers, M. C., & Wilson, J. (2023). Evaluating the construct validity of an automated writing evaluation system with a randomization algorithm. *IJAIED*, ERIC EJ1388568. `MEASURED-BENCH`
42. Kabra, A., et al. (2023). Automatic essay scoring systems are both overstable and oversensitive. *Dialogue & Discourse*. `10.5210/dad.2023.101`; preprint arXiv:2109.11728. `MEASURED-BENCH`
43. Wilson, J., Olinghouse, N. G., & Andrada, G. N. (2014). Does automated feedback improve writing quality? *LDCJ*, ERIC EJ1039856. `OBSERVED` (null on transfer)
44. Wilson, J. (2017). Associated effects of automated essay evaluation software on growth in writing quality for students with and without disabilities. *Reading and Writing*, ERIC EJ1133697. `OBSERVED` (null on transfer)
45. Wilson, J., & Roscoe, R. D. (2020). Automated writing evaluation and feedback: multiple metrics of efficacy. *JECR*, ERIC EJ1241689. `MEASURED-RCT` (null on writing quality)
46. Potter, A., & Wilson, J. (2021). Statewide implementation of automated writing evaluation. *ETR&D*, ERIC EJ1302863. `OBSERVED` (n = 114,582; association only)
47. Wilson, J., & Rodrigues, J. (2020). Classification accuracy and efficiency of writing screening using automated essay scoring. *Journal of School Psychology*, ERIC ED611395. `MEASURED-BENCH` — AES as a *screener* is a different and better-supported use than AES as a *teacher*.
48. Nunes, A., Cordeiro, C., Limpo, T., & Castro, S. L. (2022). Effectiveness of automated writing evaluation systems in school settings: a systematic review of studies from 2000 to 2020. *JCAL*, ERIC EJ1327602. `MEASURED-META` (8 studies)
49. Zhai, N., & Ma, X. (2023). The effectiveness of automated writing evaluation on writing quality: a meta-analysis. *JECR*, ERIC EJ1380424. `MEASURED-META`
50. Ngo, T. T.-N., Chen, H. H.-J., & Lai, K. K.-W. (2024). The effectiveness of automated writing evaluation in EFL/ESL writing: a three-level meta-analysis. *ILE*, ERIC EJ1419671. `MEASURED-META`
51. Huawei, S., & Aryadoust, V. (2023). A systematic review of automated writing evaluation systems. *Education and Information Technologies*, ERIC EJ1363931. `MEASURED-META` — 105 papers coded against an argument-based validation framework; the domain-description inference (whether AWE tasks correspond to real writing tasks) is the least-researched.
52. Palermo, C., & Thomson, M. M. (2018). Teacher implementation of SRSD with an automated writing evaluation system. *Contemporary Educational Psychology*. `10.1016/j.cedpsych.2018.07.002`. Abstract not retrievable via OpenAlex; listed as located, not read.

**Generative AI and writing**

53. Steiss, J., Tate, T., Graham, S., Cruz, J., & Hebert, M. (2024). Comparing the quality of human and ChatGPT feedback of students' writing. *Learning and Instruction*. `10.1016/j.learninstruc.2024.101894`; preprint `10.35542/osf.io/ty3em`. `MEASURED-BENCH`
54. Yan, D. (2024). Comparing individual vs. collaborative processing of ChatGPT-generated feedback. *Language Learning & Technology*. `10.64152/10125/73597`. `MEASURED-RCT` (assignment procedure unverified)
55. Kosmyna, N., et al. (2025). Your brain on ChatGPT: accumulation of cognitive debt when using an AI assistant for essay writing task. arXiv:2506.08872. `OBSERVED` (preprint, n = 18 in the crossover session). Critical comment: arXiv:2601.00856.
56. Nam, Y., Lee, J. M., & Park, H. (2026). Improving L2 writing through artificial intelligence: comparing AIDT and ChatGPT feedback. *English Teaching*, ERIC EJ1504813. `OBSERVED` (n = 50, no no-AI control)
57. *How AI-generated feedback hinders or helps learning: a heterogeneous TNA study of learning dynamics.* (2026). *JCAL*. `10.1002/jcal.70285`. 13,000 first-grade pupils, GPT-4.1 feedback on numeracy tasks; clarification-oriented feedback preceded successful re-attempts, question-based prompts and direct orders preceded unsuccessful ones. `OBSERVED` (process analysis, single session, no learning outcome).

**Carried from the corpus, not re-derived**

58. `H1` §1.1 (Ehri/NRP phonics d = 0.41, Galuschka randomised-only synthesis, Stevens Orton-Gillingham g = 0.22 n.s., Bowers dissent, Al Otaiba non-responders) · `H1` F5 (Fuchs, Hamlett & Stecker 1991: measurement without a decision rule) · `H1` F6 (Van Norman et al. 2023: 7–10 weeks) · `C2` §8.2 (AES psychometrics, Shermis & Hamner, LLM rater effects) · `Z1` §2.3 (Bastani −17%, non-replication declared) · `F1` (the essay as a sampling instrument).
