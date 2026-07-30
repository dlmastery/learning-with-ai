---
title: "Three Trials, and Each One Scores the Words It Taught — where the randomised generative-AI evidence in language learning lives"
section: language
status: draft
date: 2026-07-30
source_report: research/raw/R4-second-language-learning.md
---

# Second-Language Learning

Second-language learning holds the largest concentration of randomised
generative-AI evidence in any school subject. Of the seven randomised controlled
trials ERIC returns against roughly 1,565 ChatGPT-and-education records, three
are language trials: pronunciation, writing feedback, speaking. The modal
randomised trial of generative AI in education is an EFL study with fewer than a
hundred participants.

This survey said four. The corrected count is three, published as **C-58**, and
how the error happened matters more than the arithmetic.

---

## 1. The query reproduced; the classification was never checked

The ERIC API call ran on 2026-07-28 and returned seven records; re-run on
2026-07-30 it returns the same seven. `OBSERVED` — reproducible against a public
API, which is the property the census was trusted for.

Reading the records one at a time gives a different answer from reading the
count. **EJ1415077**, filed in this survey's summary table under "Blended
Learning," describes itself as a randomised trial in *"a foundational chemistry
course in a blended learning setting"* with 61 Taiwanese undergraduates, verified
against the ERIC record. **EJ1484052** is virtual reality with *"embedded IoT
tasks."* Neither is language learning. `OBSERVED` — own coding of the result set.

A reproducible retrieval step wrapped around an unchecked labelling step produces
confident wrong counts, in whichever direction the labeller was already leaning.
Re-running the query would never have caught it, and the reproducibility was the
reason nobody looked. §23 now carries the corrected figure, which does not weaken
the point the census was recruited for.

---

## 2. What the three surviving trials measured

### 2.1 Writing: the clean contrast is a null, and the paper never names it

Soori, Khojasteh & Javed (2025), *Technology in Language Teaching & Learning*
7(3). `MEASURED-RCT` (cluster-assigned). Eighty-eight adult learners in IELTS
writing courses, three feedback conditions over a semester: teacher screencast
video feedback, AI feedback (ChatGPT-4 plus Grammarly Premium), and hybrid. Pre-
and post-test Task 2 essays, anonymised, order-scrambled, double-marked blind to
condition and time point, weighted κ = 0.85 — better measurement than most of
this literature.

No arm goes without feedback, so the study cannot estimate whether any of the
three beats writing the same essays unaided. Three intact classes were randomly
assigned to the three conditions, one class each, then analysed by ANCOVA at
df = 84: condition is confounded with class, and the standard errors are those of
88 independent units when the contrast has three. The winning arm is the one that
received the other arm's feedback on top of its own.

The one contrast that isolates AI against a human is a null:

| Contrast | Mean difference (IELTS bands) | p |
|---|---|---|
| AI vs teacher e-feedback, overall writing | 0.079 | 0.921 |
| AI vs teacher, task achievement | 0.001 | 1.000 |
| AI vs teacher, grammatical range & accuracy | −0.223 | 0.463 |
| AI vs teacher, lexical resource | 0.436 | 0.029 |
| Hybrid vs teacher, overall | 0.392 | <0.001 |

IELTS writing is reported in half-band steps, so even the hybrid advantage of
0.392 bands is smaller than the smallest score the test can report. The title and
abstract carry the hybrid result and never mention the 0.079.

Read for what a builder needs, that null is the most encouraging number in the
section. ChatGPT-4 with Grammarly, over a full semester, produced writing
indistinguishable from an experienced instructor's personalised annotated video
feedback on every IELTS criterion except vocabulary, where the machine won by
0.436 of a band. Individual feedback on every draft is the scarcest thing in
instruction and the first thing rationed away from the learners with the least.
An underpowered null on three clusters is weak evidence for equivalence; it names
the claim worth establishing properly.

### 2.2 Pronunciation: the outcome is the training set

Xodabande, Shiri & Zohrabi (2025), *Discover Education* 4:307. `MEASURED-RCT`.
Sixty intermediate Iranian EFL learners, randomised 30/30, three weeks, ten
target words a week, ChatGPT-4's voice feature against electronic dictionaries.
Outcome: 30 sentences read aloud, one target word each, scored binary by three
blinded raters, α = 0.91.

Both groups practised those 30 words for three weeks, and those 30 words are the
test — different carrier sentences, same items, no untrained-item probe. The list
runs *colonel, aisle, debris, rendezvous, quay, choir, entrepreneur, bouquet* and
more of the same: English orthographic irregularities and French loanwords.
Knowing that *colonel* is /ˈkɜːnəl/ is a word-specific fact of the same order as
knowing what *colonel* means. Nothing here separates "pronounces English better"
from "memorised thirty pronunciations."

The retention claim inverts on arithmetic. The paper's own post-hoc table has the
treatment group flat from post-test to delayed test (+0.867, p = 1.000) and the
control still climbing (+3.700, p = .008). Computed from the reported means and
SDs, between-group Hedges' g is **1.57 at post-test and 0.65 two weeks later** —
58% of the gap gone in a fortnight, with the control still rising when
measurement stopped. `INFERENCE` (arithmetic on the paper's Table 2). The paper
describes this as ChatGPT retaining gains better.

One ambiguity outweighs all of that. The paper says learners used *"the voice
feature"* without saying which. If it was the speech-to-text pipeline, the model
received a transcript and never the audio, and could not have perceived a
mispronunciation. §5 shows why that is not a quibble.

### 2.3 Speaking: the largest trial, unreadable

Zhang, Liao, Li & Luo (2026), *Journal of Educational Computing Research*
64(1):59–91. N = 436, four arms, twelve weeks, ChatGPT role-play against machine
translation, automatic summarisation and traditional instruction. Behind Sage,
403 to every retrieval route, with no repository copy in OpenAlex. The abstract
reports *"adaptability (M = 85.50, Δ + 40.25), accuracy (M = 84.24, Δ + 43.93),
and fluency (M = 85.04, Δ + 42.54; all p < 0.001)"* — the treatment arm's
post-test means and its own pre-post change, with no control-group value, no SD,
no effect size and no delayed post-test. A four-arm design built to produce a
between-group comparison, and the public record carries a within-group one.

---

## 3. The within-group number and the between-group number are different quantities

This is the finding here that travels furthest outside the domain.

Lee & Lee (2024), *Language Learning & Technology* 28(2):134–162, meta-analysed
17 projects, N = 8,282, computing both estimates on overlapping samples and
printing both forest plots. Overall, **d = 1.18 within-group and d = 0.39 against
business as usual**, with seven studies in both pools. `MEASURED-META`
(Figures 4 and 5, read directly).

| Study | Within-group d (pre→post) | Between-group d (vs BAU) |
|---|---|---|
| Chambers et al. (2008a), Alphie's Alley | 2.35 [2.10, 2.60] | 0.05 [−0.15, 0.25] |
| Wijekumar et al. (2012), ITSS | 1.55 [1.10, 2.00] | 0.31 [−0.08, 0.70] |
| Al Otaiba et al. (2011), A2i | 1.09 [0.91, 1.27] | 0.26 [0.08, 0.44] |
| Connor et al. (2007), A2i | 1.09 [0.91, 1.27] | 0.14 [−0.02, 0.30] |
| Connor et al. (2011a), A2i | 1.03 [0.81, 1.25] | 0.11 [−0.09, 0.31] |
| Connor et al. (2011b), A2i | 0.45 [0.25, 0.64] | 0.09 [−0.09, 0.27] |
| Jia et al. (2012), Moodle | 0.23 [−0.16, 0.62] | 0.16 [−0.23, 0.55] |

Same trial, same learners, two ways of taking the difference. The first column
measures learning, maturation, testing effects, regression to the mean and the
treatment summed together; the second measures the treatment. In the Alphie's
Alley trial the two are **2.30 standard deviations apart**, and the pattern
repeats down the table.

Every effect size in this survey now has a question to answer before it is read:
*which difference is this?* An unlabelled `d = 1.2` in a product claim is almost
always the first column, which is why §24's benchmark specifies an active control
and a delayed post-test. It also explains how the three trials above line up: all
three report large within-group gains, two report a control contrast, one of
those two is a null, and the third reports none.

---

## 4. Transfer fails at the same seam here as everywhere else

Bibauw, Van den Noortgate, François & Desmet (2022), *LL&T* 26(1), meta-analysed
dialogue systems for language learning: 17 publications, 100 effect sizes, 803
participants, **d = 0.58 [0.35, 0.82]** on measured language outcomes with
motivation studies excluded. Their cross-modality breakdown is the field's only
quantitative transfer test:

| Practice → outcome | d | 95% CI |
|---|---|---|
| Speaking → speaking | 0.84 | [0.42, 1.26] |
| Writing → writing | 0.65 | [0.27, 1.04] |
| Written practice → speaking | 0.29 | [−0.21, 0.79] |
| Oral practice → writing | 0.19 | [−0.31, 0.70] |

`MEASURED-META`. Both cross-modality intervals cross zero and the authors call
the transfer *"quite limited."* Effects also decline with proficiency, from
d = 0.68 at A1 to d = −0.33 at B2. The search closed in January 2018, so this is
not about generative models; it is the best available prior for them.

Vocabulary carries the cleanest version, because the field routinely measures the
taught words and a standardised test in the same study. Elleman, Lindo, Morphy &
Compton (2009), 37 interventions pre-K to grade 12: effect on custom
comprehension measures built from passages containing the taught words
**d = 0.50**; on standardised comprehension **d = 0.10**; among the custom
measures, 1.23 for students with reading difficulties against 0.39 for students
without. `MEASURED-META`. That is first-language instruction, so the boundary
crossed is not identical to the L2 case, and the attenuation is five-fold from
"comprehends text built around the taught words" to "comprehends text."

The target these decks aim at has no edge to it either. Nation (2006) puts 98%
lexical coverage at 8,000–9,000 word families for written text and 6,000–7,000
for spoken; Kremmel, Indrarathne, Kormos & Suzuki (2023), *Language Learning*
73(4), preregistered with open data and materials, replicated the source study
with 104 Sri Lankan adult learners and *"failed to replicate an inferred 98%
coverage threshold as sufficient for adequate comprehension,"* confirming the
underlying linear relationship. `MEASURED-RCT`. No cliff to get a learner over; a
slope from roughly 4,000 to 9,000 families, every thousand of which buys a little
more comprehension. Deliberate study does build real lexical entries (Elgort
2011), and lexical entries are not comprehension. §08 owns scheduling; a tutor
that ships a scheduler and calls vocabulary solved has built the d = 0.10 half.

---

## 5. What a machine can hear, and why better recognition makes it worse

Pearson's copy for Versant says its scores are *"virtually indistinguishable from
expert human scoring,"* on a machine–human correlation of **r = 0.97**. `VENDOR`:
a vendor technical report, whole-test Overall against a purpose-built human
criterion, n = 143, where the pronunciation subscore is 0.88 and the correlation
with an ILR speaking interview 0.75 on n = 51.

The peer-reviewed comparison is ETS's SpeechRater (Zechner, Higgins & Xi, SLaTE
2007): machine–human **r = 0.61** on a single item and **0.68** on a six-item
form, against human–human agreement of 0.77–0.94, with the authors' verdict that
*"a large gap still remains."* On the open speechocean762 benchmark the
granularity gradient is explicit: utterance total 0.811, phone accuracy 0.693,
**word stress 0.361**. Wang & Min (2026), *Language Testing* 43(2), across 67
studies and 392 effect sizes, put the field-wide human–machine correlation at
r = .654 and pronunciation at .606, with ASR accuracy *not* a significant
moderator. `MEASURED-BENCH`. These engines rank whole speakers well and localise
individual errors poorly. Localisation is the product; the ranking is where the
validation number comes from.

They also score the wrong construct. Similarity to a native reference is an
accentedness measure, which Levis (2020) calls *"largely irrelevant"* under the
intelligibility principle, and in Saito & Plonsky's 77-study synthesis of
pronunciation instruction every interval covering a *global* construct or a
*spontaneous* task crosses zero. `MEASURED-META`.

### 5.1 Robust ASR repairs the error before the model sees it

Liu, Cui, Gu & Wang (2026), arXiv:2601.14744, evaluated cascaded ASR-plus-LLM
pipelines and end-to-end audio models on mispronunciation detection over
L2-ARCTIC, read L2 English with phoneme-level annotation of real learner errors,
one-shot prompted. `MEASURED-BENCH`.

| System | P | R | F1 |
|---|---|---|---|
| Whisper Large + Mistral-7B | 48.9 | 3.4 | 6.4 |
| Wav2vec2 Base + Llama-3.1-8B (best cascade) | 53.8 | 17.8 | 26.8 |
| Qwen2-Audio (end-to-end) | 41.7 | 22.0 | 28.8 |
| GPT-4o-Audio (end-to-end) | 52.7 | 41.3 | 46.3 |
| Their instruction-tuned Whisper-Large + Llama-3 | 48.9 | 87.7 | 62.8 |

A frontier audio model recovers 41.3% of annotated errors and is right about
52.7% of the errors it claims. Dedicated architectures on the same benchmark
reach F1 ≈ 60–72, on read speech, which is the easy case.

The row ordering carries the general insight. Whisper Small beats Whisper Medium
beats Whisper Large with the same LLM attached, and Wav2vec2 Base beats Wav2vec2
Large. The authors' explanation: *"stronger ASR models tend to correct
pronunciation errors during transcription due to their robustness to accent
variations, preventing them from accurately reflecting learners' speech
errors."* A recogniser's whole objective is to recover the word the speaker
intended, and every improvement against it destroys the signal a pronunciation
tutor needs. Any diagnostic layered on a perception model inherits that model's
objective, and where the two point in opposite directions the upgrade path runs
backwards. This is the measured form of the ambiguity in §2.2: a learner talking
to a speech-to-text pipeline is assessed on a transcript that already fixed the
thing being assessed.

The inversion is free to try. Run the learner's speech through a small,
deliberately accent-brittle recogniser and treat its failures as an
intelligibility signal, closer to what a real listener supplies than any
similarity-to-native score. `SPEC`, untested, and cheap to test.

---

## 6. Corrective feedback has no stable answer, and the reason is procedural

Plonsky & Brown (2015), *Second Language Research* 31(2), counted **18 unique
meta-analyses of corrective feedback with overall effects from d = −0.155 to
d = 1.16**, and diagnosed the 1.3-SD spread as driven by inclusion decisions and
not by sampling error. `MEASURED-META`. So the question has a family of answers
that track their authors' criteria.

Inside that spread, the estimate with the best claim on a classroom builder is
Lyster & Saito (2010), 15 classroom studies, N = 827, laboratory studies
deliberately excluded: CF versus control **d = 0.74 [0.58, 0.86]**, recasts 0.53
[0.32, 0.74], prompts 0.83 [0.56, 1.10], explicit correction 0.84 [0.57, 1.11].
`MEASURED-META`. The famous result that prompts beat recasts is significant only
within groups; between groups the intervals overlap, and explicit correction is
numerically largest and distinguishable from neither.

The design instruction survives in weaker form, and Brown (2016) is why it is
worth acting on: across observational classroom studies, **recasts are 57% of all
corrective feedback teachers actually give and prompts 30%**. `MEASURED-META`.
The most-supplied type is the least-supported one, and a language model's reflex
when a learner produces a wrong sentence is to restate it correctly, which is a
recast. Prompting the learner to self-repair withholds the form and recruits the
generation effect — a change to a system prompt, and the cheapest pedagogical
edit available in this domain.

---

## 7. Duolingo, handled by the rule

Duolingo runs all the way through this corpus and appears nowhere in it as
evidence about language acquisition. The rule that a `VENDOR` claim is never
restated as a finding is doing that, and here the rule is the point and not a
cost.

The 34-hour claim — Duolingo teaching in 34 hours what a university semester
teaches — comes from Vesselinov & Grego (2012), a self-published, never
peer-reviewed, uncontrolled within-subject pre/post study. `VENDOR`. The "one
university semester" comparison is against the WebCAPE placement cut-off of 270
points, a scoring threshold and not a cohort of students, and 34 is arithmetic:
270 ÷ 8.1 points-per-hour, extrapolated linearly from zero. Of 196 participants
sampled, **88 were analysed**, mean actual study time 22 hours, 16% (n = 14)
scoring the same or lower at post-test. Krashen (2014) added that the median gain
rate was 3.9 points per hour against that mean of 8.1, so the same arithmetic on
the median gives about 69 hours.

The company's own later measurement disagrees with its famous one. Jiang,
Rollinson, Plonsky, Gustafson & Pajak (2021), *Foreign Language Annals* 54(4),
peer-reviewed with four of five authors employed by Duolingo, puts median time to
finish the beginning content at **112 hours**, and the follow-up report through
Unit 7 at **203 hours**. `VENDOR`. Same product, its own instrumentation, and the
hours figure has grown six-fold while the marketing number has not moved.

The FY2025 Form 10-K says learners completing five sections *"achieved
proficiency comparable to five university semesters"* and that
*"**Independent studies corroborate this finding**."* `FILING`. The company
labels its own study internal, correctly; the work fitting the description of the
corroboration is Duolingo-funded, Smith, Jiang & Peters (2024) stating *"This
study was supported financially by Duolingo."* The word *independent* is carrying
weight in an audited document that the underlying papers do not support.

What is true, audited and remarkable is that this is the most successful
habit-formation product education has produced, which §14 owns. What does not
follow is that it teaches a language better than the alternative. The one
randomised comparison holding content constant — James & Mayer (2019), 64
students learning Italian from Duolingo or from a slideshow of the same material
— was a null on achievement with willingness to continue at d = 1.39.
`MEASURED-RCT`. Nothing establishes an app's teaching advantage in either
direction.

---

## 8. Revision gains that did not survive the next piece of writing

Truscott & Hsu (2008), *JSLW* 17(4):292–305, underlined the errors in half a
group's drafts and had both halves revise. The underlined group revised
significantly better. A week later everyone wrote a **new** narrative and the two
groups were *"virtually identical"* — **g = −0.068**. `MEASURED-RCT`. A tutor
measuring whether the learner fixed the flagged error is measuring the one thing
that does not carry to the next task, and it is the easiest measurement in the
domain to instrument, which is why it is the one that gets built.

Correction can also cost something an accuracy measure cannot see. Scherer,
Graham & Busse (2024), *Learning and Instruction* 93:101961, across 200
comparisons, report surface-level feedback improving surface outcomes at
g = 0.58 while moving **foreign-language learners' deep-level outcomes to
g = −0.23**. `MEASURED-META`. Grammar feedback measurably degrades content and
organisation for FL writers, and a study measuring only accuracy cannot see that
trade.

And one a survey counting effect sizes will read as supportive. Rachels &
Rockinson-Szapkiw (2018), *CALL* 31(1–2), third and fourth graders,
twelve weeks, Duolingo as the Spanish instruction against the regular Spanish
class. `OBSERVED` (non-equivalent control group). From the published abstract:

> *"An analysis of covariance showed no significant difference in students'
> Spanish achievement or in academic self-efficacy… **This demonstrates that
> Duolingo® is a useful tool for teaching Spanish to elementary students.**"*

Those two sentences are adjacent. A non-significant difference in an underpowered
quasi-experiment is reported as a demonstration of usefulness, with no
equivalence margin and no design able to support one.

Two citations circulate here that do not exist in OpenAlex or Crossref: a Mollica
& Piantadosi commentary on Hartshorne et al., and a "Zhang & Zou" pronunciation
meta-analysis. A reference list carrying either is a reference list nobody
checked.

---

## 9. Whether language is the easy win

A frontier model converses in a dozen languages, corrects a wrong sentence,
adapts register on request and never tires of the eightieth attempt at one vowel,
with none of the machinery this survey specifies (§16). So: is language the
easiest domain to build for, or the one where a pedagogical system has least to
add over plain ChatGPT?

The evidence says the second, and the survey already had the result. Fütterer et
al. (2026), n = 371, Grades 7–9, ran two scaffolded generative-AI conditions
against a control using **standard ChatGPT** and found no significant advantage
for either on effort, domain-specific knowledge or elaboration-based strategy use
(§23). `MEASURED-RCT`. Half its sessions ran in English lessons, which makes it
the only randomised test in the ERIC set of whether designed pedagogy beats plain
ChatGPT in a language classroom. It did not.

That bounds the machinery and also specifies where it earns its place, because
three of the model's native reflexes are wrong in ways this section measured. It
recasts when it should withhold the form. It will happily score the items it just
taught. And any pronunciation feedback it gives sits on a recogniser optimised to
erase the error. Each is a cheap correction to default behaviour, and none needs
a better model.

All of which holds for English as a foreign language, which is what every trial
here measures. Frontier models score at or near chance on around thirty of 122
language variants, and for those languages the pedagogical architecture is not
the binding constraint on anything.

---

## 10. The two numbers a language tutor has to publish

- **Report trained-item and untrained-item performance separately, always.** For
  any target set a model can generate a matched held-out probe controlled for
  frequency band, phonological structure and part of speech, so this is free.
  `SPEC`. Nothing in this literature would have survived the convention
  unchanged, which is the argument for it.
- **Name which difference an effect size is.** Within-group and between-group
  differed by 2.30 SD in the same trial. A product number with no comparison
  attached is the first column.
- **Withhold the form.** The recast is the model's reflex, 57% of what teachers
  already over-supply, and the least-supported of the three types.
- **Ship speaking volume; hold segmental correction back.** Unlimited low-stakes
  practice with a partner who cannot be embarrassed is an advantage no human
  tutor supplies at any price. Phoneme-level correction at F1 = 46.3 on read
  speech is not ready to show a learner as though it were right.
- **Generate input to a measured lexical coverage, and validate the profile**
  rather than trusting the prompt: unconstrained prompting gives *"weak control"*
  over CEFR level, explicit lexical constraints 0.91 cosine similarity to
  reference profiles (arXiv:2606.21981). `MEASURED-BENCH`.
- **Run the transfer trial.** Three arms, individually randomised; primary
  outcome four weeks after the last session, in an unscripted conversation with a
  human the participant has not met, scored for comprehensibility by two blinded
  raters. Plan against Lee & Lee's control-adjusted 0.39 and §2.1's null, so
  d = 0.35: 129 per arm, n ≈ 465 with attrition, or 310 for the two-arm version a
  builder actually faces.

The organising constraint of this project is a child who can hold a conversation
about photosynthesis and cannot pass the worksheet about it. She is not a
second-language learner, and the language literature still describes her
situation better than any other here: every trial in it scores the taught item,
which is the worksheet, and none scores the conversation. The field measured what
was easy to instrument and reported it as proficiency. The instrument for the
other thing is buildable now, and nobody has built it.
