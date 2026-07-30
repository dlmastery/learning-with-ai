---
title: "Second-language learning: the one subject where the randomised evidence on generative AI actually lives, and what it turns out to have measured"
wave: R
section: R4
date_researched: 2026-07-30
sources_count: 0
status: raw-research
---

# R4 — Second-language learning

> **The finding, stated first.**
>
> 1. **The census this survey has been quoting is off by one, in the direction that
>    flatters language learning.** ERIC's `ChatGPT AND "randomized controlled trial"`
>    returns seven records. Re-run and read line by line (§1), **three** are
>    second-language learning. The fourth that E3 counted is a foundational chemistry
>    course in Taiwan. The correct sentence is *three of seven*, and it is still the
>    largest single concentration of randomised generative-AI evidence in any school
>    subject.
> 2. **All three measure the trained items.** The pronunciation trial (n = 60) scores
>    the same 30 words the learners practised. The writing trial (n = 88) has no
>    no-feedback arm at all, so it cannot estimate whether AI feedback helps; its one
>    clean contrast, AI feedback versus a human teacher's video feedback, is a **null**
>    (mean difference 0.079 IELTS bands, p = 0.921). The speaking trial (N = 436) is
>    the biggest and its full text is behind Sage; its abstract reports post-test means
>    with no control-group change, no SD, no effect size.
> 3. **The delay does most of the work.** In the pronunciation trial the between-group
>    gap is **d ≈ 1.57** at post-test and **d ≈ 0.65** two weeks later, because the
>    control group kept improving after the treatment group plateaued. Nobody reports
>    the second number.
> 4. **Vocabulary has the cleanest transfer test in education, and it is discouraging
>    for anything deck-shaped.** Vocabulary instruction moves comprehension of passages
>    containing the taught words at **d = 0.50** and standardised reading comprehension
>    at **d = 0.10** (Elleman et al. 2009, k = 37). Meanwhile the target is
>    **8,000–9,000 word families** for unassisted reading (Nation 2006), and the
>    98% coverage figure everyone quotes **failed a preregistered replication** in 2023.
> 5. **A frontier audio model cannot yet hear a mispronunciation.** On L2-ARCTIC,
>    GPT-4o-Audio detects L2 mispronunciations at **F1 = 46.3** (precision 52.7, recall
>    41.3). Cascaded Whisper + LLM does worse, and *worse the better the ASR gets*,
>    because a robust recogniser's job is to recover the word the learner meant. This is
>    the measured version of a thing the pronunciation trial assumed.
> 6. **Language is where a frontier model's native capability most nearly is the
>    product, and that is an argument against building the machinery, not for it** —
>    for high-resource languages. For low-resource ones the same models score at chance
>    (F4 §3.5) and the pedagogical system is the least of the problem.

---

## Source reachability log (2026-07-30)

WebSearch budget was exhausted at 200 calls partway through §4. Retrieval thereafter ran
on the **ERIC API** (`api.ies.ed.gov/eric`), **Crossref**, **OpenAlex**, **arXiv**, and
direct `curl` + `pdftotext` of open-access PDFs.

| Target | Status |
|---|---|
| ERIC API | Fully reachable and fast. All census counts in §1 are reproducible; query strings given. |
| Springer *Discover Education* (Xodabande et al.) | Open access. **Full text read**, `link.springer.com/content/pdf/…` (the HTML landing page 303s to `idp.springer.com`; the PDF path does not). |
| *Technology in Language Teaching & Learning* (Soori et al.) | Open access via `files.eric.ed.gov`. **Full text read.** |
| *Journal of Educational Computing Research* (Zhang et al., N = 436) | **HTTP 403** to WebFetch and to `curl` with a browser UA. OpenAlex confirms `oa_status: closed`, no repository copy anywhere. **Methods and results unread.** Everything said about it here comes from the Crossref-deposited abstract. |
| *Review of Educational Research* (Wang et al. chatbot meta-analysis) | Sage **403**. Abstract obtained from Crossref and ERIC; **confidence interval for g = 0.484 not retrieved**. |
| *Journal of Computer Assisted Learning* (Li et al. GenAI-SLA meta-analysis) | Wiley **403**. Full structured abstract obtained from Crossref, which carries the point estimate and CI. Moderator subgroup estimates not retrieved. |
| *Language Learning & Technology* (Lee & Lee 2024) | Open access. **Full text read** including both forest plots. |
| *Language Learning* (Kremmel et al. 2023 replication) | Green OA at Universität Innsbruck. **Full text read.** |
| Semantic Scholar API | **HTTP 429** throughout. Not used. |
| arXiv API | Reachable. Used for the pronunciation-benchmark literature. |

---

## 1. The census, corrected

E3 §7.1 ran ERIC's API on 2026-07-28 and reported seven randomised controlled trials
against 1,565 ChatGPT-and-education records. That result reproduces. Re-run on
2026-07-30:

```
GET https://api.ies.ed.gov/eric/
    ?search=ChatGPT AND "randomized controlled trial"
    &format=json&rows=50
→ numFound: 7
```

`OBSERVED` — reproducible against a public API. The seven, with what each actually
randomised:

| ERIC ID | Year | Venue | Domain | n |
|---|---|---|---|---|
| EJ1409494 | 2023 | *Phys. Rev. PER* | Physics **task authoring by trainee teachers** | 26 |
| EJ1415077 | 2024 | *IJETHE* | **Foundational chemistry**, Taiwan, blended | 61 |
| EJ1481973 | 2025 | *Discover Education* | **EFL pronunciation**, Iran | 60 |
| EJ1484052 | 2025 | *Educ. & Info. Tech.* | **Embedded-IoT tasks in VR**, undergraduates | 81 |
| EJ1484562 | 2025 | *TLTL* | **EFL writing feedback**, Iran | 88 |
| EJ1490746 | 2026 | *J. Educ. Computing Res.* | **EFL speaking**, NLP tools | 436 |
| EJ1510259 | 2026 | *Educ. Psych. Rev.* | **SRL scaffolds**, Grades 7–9 physics/English | 371 |

E3 counted four second-language trials. Reading the abstracts, **three** are: the
pronunciation trial, the writing-feedback trial, and the speaking trial. EJ1415077, the
one E3's summary table labelled "Blended Learning," describes itself as *"a foundational
chemistry course in a blended learning setting"* with 61 Taiwanese undergraduates.
EJ1484052 is VR with *"embedded IoT tasks."* Neither is language learning. The survey's
claim should read **three of seven**. `OBSERVED` — own coding of the ERIC result set.

The correction does not weaken the point. Three of seven is still a subject
concentration that nothing else in K-12 comes near, and it still means the modal
randomised trial of generative AI in education is an Iranian or Chinese EFL study with
fewer than a hundred participants.

---

## 2. What the three trials actually measured

### 2.1 Pronunciation: 60 learners, 30 words, and the words are the test

Xodabande, Shiri & Zohrabi (2025), *Discover Education* 4:307,
[10.1007/s44217-025-00782-2](https://doi.org/10.1007/s44217-025-00782-2). `MEASURED-RCT`.

Sixty intermediate Iranian EFL learners at a private institute in Tehran, aged 19–25,
randomised 30/30. The treatment group used ChatGPT-4's voice feature to practise
pronunciation with a fixed prompt (*"listen carefully to my pronunciation of the word
'[target]' and give me feedback on how to improve it"*). The control group used
electronic dictionaries. Three weeks, ten target words per week, two self-directed
sessions a week at home. Treatment learners submitted weekly screenshots; control
learners logged dictionary entries.

Outcome: read aloud 30 sentences, one target word each, scored binary correct/incorrect
by three blinded teachers, Cronbach's α = 0.91 across raters. Pre-test, post-test at
week 4, delayed post-test two weeks later with a third set of carrier sentences.

Results as reported: Time × Group interaction F(2, 116) = 11.8, p < .001, η²p = .169;
between-subjects Group F(1, 58) = 22.9, p < .001, η²p = .283. Means out of 30 —
treatment 7.67 → 19.07 → 18.20, control 8.20 → 13.43 → 15.37.

Three things the paper does not say.

**The outcome is the training set.** The authors are careful that the five words used in
the one-hour ChatGPT tutorial were excluded from the 30 targets. They are not careful
about the fact that the 30 targets *are* what both groups practised for three weeks.
Different carrier sentences, same words. There is no untrained-item measure and no
generalisation probe, so nothing in this trial distinguishes "learned to pronounce
English better" from "memorised 30 pronunciations."

**The 30 items are lexical facts wearing a phonological costume.** The paper says the
words were chosen for *"segmental and suprasegmental features (e.g., consonant clusters,
vowel length)."* The list is *albeit, choir, colonel, niche, enzyme, aisle, debt, island,
plumber, aesthetic, genre, entrepreneur, chaos, mischievous, recipe, gauge, queue,
rendezvous, anonymous, subtle, bouquet, debris, buffet, epitome, plough, suite, squirrel,
quay, zebra*. That is a list of English orthographic irregularities and French loanwords.
Knowing that *colonel* is /ˈkɜːnəl/ is a word-specific fact of the same kind as knowing
what *colonel* means. It is not a motor-phonetic skill, and success on it does not imply
anything about producing an unfamiliar consonant cluster.

**The retention claim inverts on inspection.** The authors' own post-hoc table shows the
treatment group flat between post-test and delayed (+0.867, p = 1.000) and the control
group **still improving** (+3.700, p = .008). Computed from the reported means and SDs,
Hedges' g for the between-group difference is **1.57 at post-test** and **0.65 at the
two-week delay** — the gap closed by 58% in a fortnight, and the control's trajectory was
still rising when measurement stopped. `INFERENCE` (arithmetic on the paper's Table 2).
The paper reports this pattern as ChatGPT "retaining gains better." Read the other way,
electronic dictionaries with an extra fortnight caught most of the way up.

One unresolvable ambiguity, and it matters more than anything above. The paper says
learners used *"the voice feature"* of ChatGPT-4. It does not say which one. If it was
the speech-to-text pipeline, the model received a **transcript**, never the audio, and
could not have perceived a mispronunciation at all — its "feedback" would have been a
generic description of the correct pronunciation, keyed to whatever word the recogniser
decided the learner meant. §5 shows this is not a hypothetical: robust ASR actively
repairs learner errors before any model sees them. The trial cannot be interpreted
without knowing which pipeline was used, and it does not say.

### 2.2 Writing: three feedback arms, no control, and a null nobody named

Soori, Khojasteh & Javed (2025), *Technology in Language Teaching & Learning* 7(3),
[EJ1484562](https://files.eric.ed.gov/fulltext/EJ1484562.pdf). `MEASURED-RCT`
(cluster-assigned; see below).

Eighty-eight adult intermediate learners in IELTS writing courses at two branches of one
language centre in Shiraz. Three conditions over a two-and-a-half-month semester:
teacher e-feedback (Snagit screencast video with Wacom annotation, delivered by
Telegram); AI feedback (ChatGPT-4 plus Grammarly Premium, five scripted prompts mapped to
the IELTS criteria); hybrid (AI first, then the same teacher screencasts). One instructor
taught all three. Pre- and post-test 200-word IELTS Task 2 essays, anonymised and
order-scrambled, double-marked on the IELTS band descriptors by two trained raters blind
to condition and to time point, weighted κ = 0.85.

That is a more careful measurement apparatus than most of this literature. Four things
about the design bound what can be concluded from it.

**There is no control group.** Every arm receives feedback. The design can compare
feedback modalities and cannot estimate whether any of them beats writing the same essays
without feedback, or beats a semester of ordinary instruction. The abstract's framing —
*"the pedagogical potential of integrating human and AI feedback"* — is not supported by
a contrast the study ran.

**Assignment was by class, analysis was by student.** *"[T]he three selected classes were
randomly assigned to one of the three feedback groups."* Three clusters, one per
condition, analysed with ANCOVA at df = 84. Condition is fully confounded with class, and
the standard errors are those of 88 independent units when the between-condition contrast
has three. Any p-value here is optimistic by an unknown and large factor.

**The winning arm got more feedback.** Hybrid is AI feedback *plus* the teacher feedback
the teacher-only arm received. The headline result reduces to two sources of feedback
beating one, which is not a finding about AI.

**The one clean AI-versus-human contrast is a null, and the paper does not label it as
one.** From the pairwise table:

| Contrast | Mean difference (IELTS bands) | p |
|---|---|---|
| AI feedback vs teacher e-feedback, **overall writing** | 0.079 | **0.921** |
| AI vs teacher, task achievement | 0.001 | 1.000 |
| AI vs teacher, coherence & cohesion | 0.173 | 0.661 |
| AI vs teacher, grammatical range & accuracy | **−0.223** | 0.463 |
| AI vs teacher, lexical resource | 0.436 | **0.029** |
| Hybrid vs teacher, overall | 0.392 | <0.001 |
| Hybrid vs AI, overall | 0.313 | <0.001 |

ChatGPT-4 plus Grammarly Premium, over a full semester, produced writing indistinguishable
from an experienced instructor's personalised video feedback on every IELTS criterion
except vocabulary, where it won by 0.436 of a band. Depending on the reader's priors that
is either a striking result for AI or a striking result for teachers. It is not in the
abstract.

Scale check on the "substantial improvements": IELTS writing is reported in half-band
steps. The hybrid advantage over teacher feedback, 0.392 bands, is **smaller than the
smallest score the test can report**. There is no delayed post-test, and the paper does
not state whether learners had tool access during the post-test essay.

The qualitative half deserves a sentence because the paper is unusually open about it.
Reflection prompts went only to the winning arm, after the quantitative result was known,
with the intervention name filled into a placeholder `x` that had been left blank for
that purpose. Eleven of 28 responded. The authors describe this as *"a deliberate design
feature, not an oversight."* It is a confirmation instrument, and the 73% who "reported
reduced writing anxiety" is a number about eleven volunteers from the arm that won.

### 2.3 Speaking: the largest trial, and I could not read it

Zhang, Liao, Li & Luo (2026), *Journal of Educational Computing Research* 64(1):59–91,
[10.1177/07356331251377414](https://doi.org/10.1177/07356331251377414). `MEASURED-RCT`
(design as described in the abstract only).

N = 436, four arms over twelve weeks: 20 ChatGPT role-play sessions; machine translation
(Google Translate/DeepL); automatic summarisation (SMMRY/QuillBot); traditional
instruction as control. Outcomes named as adaptability, accuracy, fluency.

Sage returns 403 to every retrieval route available in this session, and OpenAlex
confirms no repository copy exists. So this is what the abstract reports, in full:
*"adaptability (M = 85.50, Δ + 40.25), accuracy (M = 84.24, Δ + 43.93), and fluency
(M = 85.04, Δ + 42.54; all p < 0.001)."*

Those are the treatment group's post-test means and its own pre-post gains. The abstract
contains **no control-group value, no standard deviation, no standardised effect size, no
confidence interval, and no delayed post-test.** Gains of roughly 40 points on what
appears to be a 100-point scale in twelve weeks would be, if real and control-adjusted, by
some distance the largest speaking-proficiency effect in the CALL literature. On the
available evidence it is a within-group change reported without the between-group
comparison that the four-arm design was built to produce. **The single largest randomised
trial of generative AI in second-language learning is, for this survey's purposes,
unreadable.** That is a finding about the field's access norms as much as about the study.

### 2.4 The meta-analytic backdrop, and the number that explains it

Four syntheses bear on this, and they do not descend from independent literatures — the
GenAI ones overlap heavily and one of them ingests a vendor study.

| Synthesis | Scope | Comparison | Result |
|---|---|---|---|
| Wang, Cheung, Neitzel & Chai (2024), *Rev. Educ. Res.*, [10.3102/00346543241255621](https://doi.org/10.3102/00346543241255621) | 28 studies, 70 ES, robust variance estimation | vs **non-chatbot** conditions | **g = 0.484** (CI not retrieved) |
| Li, Wang & Yang (2025), *J. Comp. Assist. Learn.* 41(4), [10.1111/jcal.70060](https://doi.org/10.1111/jcal.70060) | 41 experimental/quasi studies, 48 ES, N = 3,515 | mixed | **ES = 0.576, 95% CI [0.385, 0.768]** |
| Zhang, Shan, Lee, Che & Kim (2023), *Educ. Inf. Technol.* | 18 studies, 61 samples | mixed | **g = 0.527** |
| Lee & Lee (2024), *Lang. Learn. Technol.* 28(2):134–162 | 17 projects, N = 8,282 | **both** designs, separately | **d = 1.18** within-group; **d = 0.39** vs business-as-usual |

`MEASURED-META` for all four. Lee & Lee is the one to read, because it is the only one
that computes both estimates on overlapping samples and prints both forest plots. Seven
studies appear in both pools:

| Study | Within-group d (pre→post) | Between-group d (vs BAU) |
|---|---|---|
| Chambers et al. (2008a), Alphie's Alley | **2.35** [2.10, 2.60] | **0.05** [−0.15, 0.25] |
| Wijekumar et al. (2012), ITSS | 1.55 [1.10, 2.00] | 0.31 [−0.08, 0.70] |
| Al Otaiba et al. (2011), A2i | 1.09 [0.91, 1.27] | 0.26 [0.08, 0.44] |
| Connor et al. (2007), A2i | 1.09 [0.91, 1.27] | 0.14 [−0.02, 0.30] |
| Connor et al. (2011a), A2i | 1.03 [0.81, 1.25] | 0.11 [−0.09, 0.31] |
| Connor et al. (2011b), A2i | 0.45 [0.25, 0.64] | 0.09 [−0.09, 0.27] |
| Jia et al. (2012), Moodle | 0.23 [−0.16, 0.62] | 0.16 [−0.23, 0.55] |

Same intervention, same learners, two ways of taking the difference. The first column is
what a pre-post design measures: learning, maturation, testing effects, regression to the
mean, and the treatment, added together. The second is the treatment. In the Alphie's
Alley trial the two differ by **2.30 standard deviations**. `MEASURED-META` (Lee & Lee's
Figures 4 and 5, read directly).

This is the number to carry into every claim in §2. All three of the ERIC trials report
large within-group gains. Two of them also report a control contrast; one of those
contrasts (§2.2) is a null. The third reports no control contrast at all.

Two further cautions on the GenAI meta-analyses specifically. Li et al. find their largest
moderator effects for *"the first language (L1) represented by Indonesian"* and for
*"intervention time of 1–7 days."* Lee & Lee's Duolingo and Memrise samples are almost
entirely Indonesian undergraduate quasi-experiments (Ali 2021; Aulia et al. 2020;
Purwanto et al. 2022; Rohim et al. 2022; Taebenu & Katemba 2021; Nuralisah & Kareviati
2020; Maesaroh 2021). Two syntheses reporting their strongest effects in the same small
national quasi-experimental literature is not two pieces of evidence. And a moderator
showing effects concentrate in interventions lasting **under a week** is the standard
signature of novelty and unblinded outcome measurement, not of durable acquisition.

Lee & Lee's own moderator table carries one more result worth stating with its caveat.
Coding intervention type by AI role, the adjusted between-group estimate for
**"individual learning tool"** — the Duolingo/Babbel/Memrise/Busuu category — is
**−0.02 (SE 0.50)**, against 0.44 for intelligent tutoring systems and 0.50 for learning
management. The caveat is that this estimate comes from a meta-regression with nine
predictors over 35 samples in which tool type, adult learners, and foreign-language
context are nearly collinear; the standard error of 0.50 says so. The raw between-group
estimates for those same consumer-app studies are positive (0.49 to 0.71). The correct
reading is that the design cannot separate these factors, and that the confident-looking
0.39 headline should not be attributed to the consumer apps.

---

## 3. The acquisition literature that predates all of this

<!--SEC3-->

---

## 4. Vocabulary: how many words, gained how, and whether the deck transfers

F11 owns spacing and scheduling and this section does not re-derive them; its
conclusion that expanding intervals have no aggregate advantage over uniform ones
(g = 0.032 [−0.10, 0.17], k = 54) applies unchanged to a vocabulary deck. What F11 does
not cover, and what a language tutor cannot be designed without, is the size of the
target, the two ways of hitting it, and whether hitting it produces anything outside the
deck.

### 4.1 The size of the target

Nation (2006), *Canadian Modern Language Review* 63(1):59–82, trialled fourteen
1,000-word-family lists built from the British National Corpus and asked what vocabulary
size yields 98% lexical coverage. The answer: **8,000–9,000 word families for written
text, 6,000–7,000 for spoken text.** `OBSERVED` (corpus study, not an experiment).

Laufer & Ravenhorst-Kalovski (2010), *Reading in a Foreign Language* 22(1), measured
vocabulary size (Levels Test), coverage (Vocabulary Profile) and comprehension (a
standardised national test) in the same learners and proposed two thresholds: an
**optimal** one at 8,000 families / 98% coverage and a **minimal** one at
**4,000–5,000 families / 95% coverage**. Their incidental observation is the useful one
for a tutor: *"small increments of vocabulary knowledge contribute to reading
comprehension even though they hardly improve text coverage"* — the returns are smooth,
not stepped.

Which is what Schmitt, Jiang & Grabe (2011), *Modern Language Journal* 95(1), found
directly with 661 participants from eight countries: a **relatively linear** relationship
between percentage of vocabulary known and comprehension, with **no threshold** at which
comprehension jumps.

And then the number itself failed to replicate. Kremmel, Indrarathne, Kormos & Suzuki
(2023), *Language Learning* 73(4):1127–1163,
[10.1111/lang.12622](https://doi.org/10.1111/lang.12622), preregistered, Open Data and
Open Materials badges, replicated Hu & Nation (2000) with 104 Sri Lankan adult learners
at five coverage densities (80/90/95/98/100%). Their conclusion: the study *"confirmed the
original finding of a mostly linear relationship between vocabulary coverage and reading
comprehension but **failed to replicate an inferred 98% coverage threshold as sufficient
for adequate comprehension**."* `MEASURED-RCT` (randomised assignment to coverage
condition). The original figure rests on a regression over 66 New Zealand university
students; the replication also found that unknown-word density affects comprehension
differently by genre and by response format, so the threshold is not even a single
quantity.

The pedagogically load-bearing version, therefore: there is no cliff to get the learner
over. There is a slope, its useful range runs from roughly 4,000 to roughly 9,000 word
families, and every thousand families buys a bit more comprehension. That is a very
different design target from "unlock B1."

### 4.2 Incidental versus intentional, with real numbers on both

Webb, Uchihara & Yanagisawa (2023), *Language Teaching* 56(2), meta-analysed
**incidental** vocabulary learning from meaning-focused input: 24 studies, 29 effect
sizes, N = 2,771 (1,517 experimental, 1,254 control). Mean proportions of target words
learned: **9–18% on immediate post-tests, 6–17% on delayed.** By mode: reading 17%/15%,
listening 15%/13%, reading-while-listening 13%/17%, **viewing 7%/5%**. `MEASURED-META`.

Webb, Yanagisawa & Uchihara (2020), *Modern Language Journal* 104(4), meta-analysed
**intentional** word-focused activities — flashcards, word lists, writing,
fill-in-the-blanks: 100 effect sizes from 22 studies. Average percentage gains
**60.1% (meaning recall) and 58.5% (form recall)** on immediate post-tests, falling to
**39.4% and 25.1%** on delayed post-tests. Between activities the range was 18.4% to
77.0% immediate and 23.9% to 73.4% delayed. The authors' own summary: *"learning through
word-focused tasks is far from guaranteed."* `MEASURED-META`.

Two things follow that a product decision depends on.

Intentional study is roughly **four times** as efficient per target word as incidental
exposure at immediate test, and the advantage narrows at delay because intentional gains
decay faster — most sharply for **form recall**, the productive direction, which loses
more than half its gain (58.5% → 25.1%). A deck teaches recognition durably and
production poorly. That is the shape of the thing, measured.

And Uchihara, Webb & Yanagisawa (2019), *Language Learning* 69(3):559–599, meta-analysed
45 correlations from 26 studies (N = 1,918) between number of encounters and incidental
learning: **r = .34**. Repetition matters and explains about a ninth of the variance.
Encounters are not the mechanism people assume.

### 4.3 The transfer question, in its cleanest available form

The question this survey turns on is whether a scheduler that reliably produces
recognition of the items in its deck produces anything else. Vocabulary has an unusually
clean version because the field routinely measures both the taught words and a
standardised comprehension test in the same study.

Elleman, Lindo, Morphy & Compton (2009), *Journal of Research on Educational
Effectiveness* 2(1):1–44, meta-analysed 37 vocabulary interventions, pre-K to grade 12:

- effect on **custom** comprehension measures (passages containing the taught words):
  **d = 0.50**
- effect on **standardised** comprehension measures: **d = 0.10**
- among custom measures, controlling for method variables: students with reading
  difficulties **d = 1.23** versus **d = 0.39** for students without
- correlation between a study's vocabulary effect and its comprehension effect, among
  studies reporting both: **r = 0.43**

`MEASURED-META`. This is first-language vocabulary instruction, so the transfer is
across a different boundary than L2 acquisition; it is nonetheless the clean version of
the question, and the answer is a five-fold attenuation from "comprehends text built
around the taught words" to "comprehends text."

The counterweight is worth stating fully, because the naive reading of Elleman is that
deliberate vocabulary learning is shallow, and that is not what the psycholinguistics
shows. Elgort (2011), *Language Learning* 61(2), taught 48 pseudowords by deliberate
study and then probed them with masked repetition priming, form priming, and automatic
semantic priming in lexical decision. All three effects appeared for the deliberately
learned items, and response-latency variability showed they were processed with **higher
automaticity than genuine low-frequency L2 words**. `MEASURED-RCT` (within-subject
experimental). Deliberate learning produces real, integrated, automatised lexical
entries.

Both results hold. Deck study builds genuine word knowledge; word knowledge is not
comprehension; and the gap between them is where the reading, listening and speaking
practice has to go. A tutor that ships a scheduler and calls the vocabulary problem
solved has built the d = 0.10 half.

**The arithmetic nobody in the consumer category publishes.** Take the intentional-study
delayed-recall figure at face value: about 39% of studied items retained in meaning
recall, 25% in form recall, per pass. Take the target as 8,000 word families and a
starting point of roughly 2,000 for a false beginner in a cognate language. Six thousand
families at a 39% durable yield per pass is on the order of 15,000 item-passes even
before spacing overhead, and that is for the receptive direction only. Duolingo's own
published outcome for **finishing** a beginner course is approximately CEFR A2
(F6 §4.3b), which is conventionally on the order of 1,500–2,000 words. `INFERENCE`. The
gap between what a deck-shaped product delivers and what unassisted reading requires is
not a matter of a few more months of streak.

---

## 5. Speaking and pronunciation: what a machine can actually hear

<!--SEC5-->

---

## 6. The critical-period question, stated accurately

<!--SEC6-->

---

## 7. The commercial reality

<!--SEC7-->

---

## 8. Nulls, given their own space

<!--SEC8-->

---

## 9. What is now buildable, the experiment worth running, and what I could not find out

<!--SEC9-->
