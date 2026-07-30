---
title: "Second-language learning: the one subject where the randomised evidence on generative AI actually lives, and what it turns out to have measured"
wave: R
section: R4
date_researched: 2026-07-30
sources_count: 88
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
>    gap is d ≈ 1.57 at post-test and d ≈ 0.65 two weeks later, because the
>    control group kept improving after the treatment group plateaued. Nobody reports
>    the second number.
> 4. **Vocabulary carries a clean transfer test, and it is discouraging for anything
>    deck-shaped.** Vocabulary instruction moves comprehension of passages containing the
>    taught words at d = 0.50 and standardised reading comprehension at d = 0.10
>    (Elleman et al. 2009, k = 37). The target is 8,000–9,000 word families for
>    unassisted reading (Nation 2006), and the 98% coverage figure everyone quotes
>    **failed a preregistered replication** in 2023.
> 5. **A frontier audio model cannot yet hear a mispronunciation.** On L2-ARCTIC,
>    GPT-4o-Audio detects L2 mispronunciations at F1 = 46.3 (precision 52.7, recall
>    41.3), and cascaded Whisper + LLM does worse *the better the ASR gets*, because a
>    robust recogniser's job is to recover the word the learner meant.
> 6. **Language is the subject where a frontier model's native capability most nearly is
>    the product**, which argues against building the machinery rather than for it — in
>    high-resource languages. In low-resource ones the same models score at chance
>    (F4 §3.5) and the pedagogical system is the least of the problem.

---

**Retrieval note.** WebSearch budget was exhausted at 200 calls partway through §4.
Retrieval thereafter ran on the ERIC API (`api.ies.ed.gov/eric`), Crossref,
OpenAlex, arXiv, SEC EDGAR, and direct `curl` + `pdftotext` of open-access
PDFs. Full texts read: Xodabande et al., Soori et al., Lee & Lee 2024 (including both
forest plots), Kremmel et al. 2023, Liu et al. arXiv:2601.14744, Duolingo's Q1 2026 10-Q.
Blocks are itemised in §9.3.

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
| EJ1409494 | 2023 | *Phys. Rev. PER* | Physics task authoring by trainee teachers | 26 |
| EJ1415077 | 2024 | *IJETHE* | Foundational chemistry, Taiwan, blended | 61 |
| EJ1481973 | 2025 | *Discover Education* | EFL pronunciation, Iran | 60 |
| EJ1484052 | 2025 | *Educ. & Info. Tech.* | Embedded-IoT tasks in VR, undergraduates | 81 |
| EJ1484562 | 2025 | *TLTL* | EFL writing feedback, Iran | 88 |
| EJ1490746 | 2026 | *J. Educ. Computing Res.* | EFL speaking, NLP tools | 436 |
| EJ1510259 | 2026 | *Educ. Psych. Rev.* | SRL scaffolds, Grades 7–9 physics/English | 371 |

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
vowel length)."* The list is *albeit, choir, colonel, niche, aisle, debt, island, plumber,
genre, entrepreneur, chaos, mischievous, gauge, queue, rendezvous, subtle, bouquet,
debris, buffet, epitome, plough, suite, squirrel, quay* and six more of the same kind:
English orthographic irregularities and French loanwords. Knowing that *colonel* is
/ˈkɜːnəl/ is a word-specific fact of the same order as knowing what *colonel* means. It is
not a motor-phonetic skill, and success on it implies nothing about producing an
unfamiliar consonant cluster.

**The retention claim inverts on inspection.** The authors' own post-hoc table shows the
treatment group flat between post-test and delayed (+0.867, p = 1.000) and the control
group **still improving** (+3.700, p = .008). Computed from the reported means and SDs,
Hedges' g for the between-group difference is 1.57 at post-test and **0.65 at the
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
| AI feedback vs teacher e-feedback, overall writing | 0.079 | 0.921 |
| AI vs teacher, task achievement | 0.001 | 1.000 |
| AI vs teacher, coherence & cohesion | 0.173 | 0.661 |
| AI vs teacher, grammatical range & accuracy | −0.223 | 0.463 |
| AI vs teacher, lexical resource | 0.436 | 0.029 |
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
with the intervention name filled into a placeholder `x` left blank for that purpose.
Eleven of 28 responded. The authors call this *"a deliberate design feature, not an
oversight."* The 73% who "reported reduced writing anxiety" are eleven volunteers from the
arm that won.

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
| Wang, Cheung, Neitzel & Chai (2024), *Rev. Educ. Res.*, [10.3102/00346543241255621](https://doi.org/10.3102/00346543241255621) | 28 studies, 70 ES, robust variance estimation | vs non-chatbot conditions | g = 0.484 (CI not retrieved) |
| Li, Wang & Yang (2025), *J. Comp. Assist. Learn.* 41(4), [10.1111/jcal.70060](https://doi.org/10.1111/jcal.70060) | 41 experimental/quasi studies, 48 ES, N = 3,515 | mixed | ES = 0.576, 95% CI [0.385, 0.768] |
| Zhang, Shan, Lee, Che & Kim (2023), *Educ. Inf. Technol.* | 18 studies, 61 samples | mixed | g = 0.527 |
| Lee & Lee (2024), *Lang. Learn. Technol.* 28(2):134–162 | 17 projects, N = 8,282 | both designs, separately | d = 1.18 within-group; d = 0.39 vs business-as-usual |

`MEASURED-META` for all four. Lee & Lee is the one to read, because it is the only one
that computes both estimates on overlapping samples and prints both forest plots. Seven
studies appear in both pools:

| Study | Within-group d (pre→post) | Between-group d (vs BAU) |
|---|---|---|
| Chambers et al. (2008a), Alphie's Alley | 2.35 [2.10, 2.60] | 0.05 [−0.15, 0.25] |
| Wijekumar et al. (2012), ITSS | 1.55 [1.10, 2.00] | 0.31 [−0.08, 0.70] |
| Al Otaiba et al. (2011), A2i | 1.09 [0.91, 1.27] | 0.26 [0.08, 0.44] |
| Connor et al. (2007), A2i | 1.09 [0.91, 1.27] | 0.14 [−0.02, 0.30] |
| Connor et al. (2011a), A2i | 1.03 [0.81, 1.25] | 0.11 [−0.09, 0.31] |
| Connor et al. (2011b), A2i | 0.45 [0.25, 0.64] | 0.09 [−0.09, 0.27] |
| Jia et al. (2012), Moodle | 0.23 [−0.16, 0.62] | 0.16 [−0.23, 0.55] |

Same intervention, same learners, two ways of taking the difference. The first column
measures learning, maturation, testing effects, regression to the mean and the treatment
added together; the second measures the treatment. In the Alphie's Alley trial they differ
by 2.30 standard deviations. `MEASURED-META` (Lee & Lee's Figures 4 and 5, read directly).
Carry that into §2: all three ERIC trials report large within-group gains, two report a
control contrast, one of those contrasts is a null, and the third reports none.

Two cautions on the GenAI syntheses. Li et al. find their largest moderator effects for
*"the first language (L1) represented by Indonesian"* and for *"intervention time of 1–7
days,"* and Lee & Lee's Duolingo and Memrise samples are almost entirely Indonesian
undergraduate quasi-experiments (Ali 2021; Aulia et al. 2020; Purwanto et al. 2022; Rohim
et al. 2022; Taebenu & Katemba 2021). Two syntheses reporting their strongest effects in
the same small national quasi-experimental literature is not two pieces of evidence. A
moderator showing effects concentrated in interventions lasting **under a week** is the
signature of novelty and unblinded measurement.

Lee & Lee's moderator table carries one more result, stated with its caveat. Coding by AI
role, the adjusted between-group estimate for **"individual learning tool"** (the
Duolingo/Babbel/Memrise/Busuu category) is −0.02 (SE 0.50) against 0.44 for
intelligent tutoring systems. That estimate comes from a meta-regression with nine
predictors over 35 samples in which tool type, adult learners and foreign-language context
are nearly collinear, and the standard error says so; the raw between-group estimates for
those same consumer-app studies are positive (0.49 to 0.71). The reading is that the model
cannot separate these factors, and that the 0.39 headline should not be attributed to the
consumer apps.

---

## 3. The acquisition literature that predates all of this

A tutor architecture makes commitments about mechanism whether or not it states them, and
the SLA field has been arguing about those commitments since 1982. Before any of the
numbers, the fact that governs how to read them:

> Plonsky & Brown (2015), *Second Language Research* 31(2):267–278,
> `10.1177/0267658314536436`, counted **18 unique meta-analyses of corrective feedback**
> whose overall effect sizes range from **d = −0.155 to d = 1.16**. Their diagnosis is that
> the 1.3-SD spread is driven by **inclusion decisions rather than sampling error**, and
> that L2 meta-analysts use "a stable but very limited set of search strategies, none of
> which is likely to yield unpublished studies." `MEASURED-META`.

So the question "does correcting a learner help, and by how much" does not have a stable
meta-analytic answer. It has a family of answers that track their authors' criteria.

**Comprehensible input.** Krashen's Input Hypothesis holds that acquisition happens when
the learner understands input slightly beyond current competence, that conscious rule
learning cannot become acquisition, and that an affective filter can block input from
reaching the acquisition device. *Principles and Practice* (1982) is unambiguous about
correction: "Error correction has little or no effect on subconscious acquisition" (p. 10);
"a sure method of raising the filter is attempting to correct errors… in my view it has
been a serious mistake" (pp. 74–75). The unfalsifiability is visible in Krashen's own
statement of the filter (p. 31): an acquirer who receives a great deal of comprehensible
input and still fossilises has done so "due to the affective filter." Any disconfirming
case is absorbed by the construct meant to explain it. Gregg's 1984 critique in *Applied
Linguistics* is the canonical objection; **it is paywalled with no published abstract and
was not read in this session**, so its detail is second-hand and is not quoted here.
`CRAFT` for the pedagogy; the theory is contested.

Note where Krashen's anti-correction position comes from. It is a consequence of the
non-interface claim, stipulated rather than measured: there is no mechanism by which
feedback could reach the acquired system, so feedback cannot help.

**Interaction, output, and noticing** supply the mechanism Krashen closed off. Long (1996)
routes negative feedback through selective attention, with a scope limitation that
citations usually drop: feedback is facilitative "at least for vocabulary, morphology, and
language-specific syntax, and essential for learning certain specifiable L1–L2 contrasts"
(p. 414). Swain's pushed output is production under pressure to convey a message
"precisely, coherently, and appropriately," a concept she explicitly parallels to i+1, on
the grounds that using a language "may force the learner to move from semantic processing
to syntactic processing" (1985, pp. 248–249). Schmidt (1990) adds the condition that makes
this testable, defining noticing operationally as availability for verbal report and
refusing the escape hatch: "subconscious noticing… is oxymoronic."

**And White (1987)**, *Applied Linguistics* 8(2):95–110, supplies the in-principle argument
for correction that the rest of this section is about. Positive evidence can show a learner
that a form is possible; it can never show that one is impossible. Input "will not be able
to show the learner how to retreat from certain non-target forms: the input hypothesis is
geared to handling additions to intermediate grammars, rather than losses." Retreat from
over-generation requires negative evidence. That is why a tutor corrects at all.

### 3.1 What corrective feedback is actually worth

**Lyster, Roy & Saito, Kazuya (2010),** *Studies in Second Language Acquisition*
32(2):265–302, [10.1017/S0272263109990520](https://doi.org/10.1017/S0272263109990520).
`MEASURED-META`. Fifteen **classroom** studies, N = 827; they deliberately excluded the 19
laboratory studies on the ground that lab results "cannot predict the pedagogical
effectiveness of CF." Their Table 3, transcribed:

| Contrast | n | k | d | 95% CI |
|---|---|---|---|---|
| CF vs control, all | 15 | 43 | 0.74 | 0.58–0.86 |
| Recasts | 7 | 13 | 0.53 | 0.32–0.74 |
| Prompts | 7 | 15 | 0.83 | 0.56–1.10 |
| Explicit correction | 6 | 10 | 0.84 | 0.57–1.11 |
| Immediate post-test | 15 | 25 | 0.63 | 0.45–0.81 |
| Delayed post-test | 10 | 18 | 0.84 | 0.63–1.05 |
| Free constructed response | 5 | 13 | 0.97 | 0.68–1.33 |
| Constrained constructed response | 9 | 38 | 0.70 | 0.55–0.85 |
| Metalinguistic judgement | 5 | 27 | 0.45 | 0.26–0.64 |
| *Within-group* CF gain | 10 | 33 | 0.91 | 0.76–1.06 |
| *Within-group* control gain | 10 | 17 | 0.39 | 0.30–0.48 |

The estimand for the first block is the standardised post-test difference between a CF
group and a control group, pooled SD. The last two rows are pre-to-post gains, and the
authors' own net figure is **0.91 − 0.39 = 0.52**.

**Li, Shaofeng (2010),** *Language Learning* 60(2):309–365. `MEASURED-META`. Thirty-three
studies (22 published, 11 dissertations), 17 coded features. **The paper is closed access
with no repository copy and was not read.** Its abstract reports a medium overall effect
maintained over time, that "the effect of implicit feedback was better maintained than that
of explicit feedback," that lab studies exceeded classroom studies, and that **shorter
treatments produced larger effects than longer ones**. Second-hand sources give d = 0.61
fixed / 0.64 random, and Truscott's restatement gives a sequence of 0.70/0.88 initially,
0.61/0.64 after outlier removal, and **0.56/0.53 after adjustment for likely missing
findings**. Those numbers are `[2nd]` and are not treated as established here.

Four things follow that a build should act on.

**The implicit-at-long-delay reversal is not safe to design around.** Li's contrast is
between-study, his own moderator table puts implicit feedback disproportionately in the
laboratory and in longer treatments, and with 33 studies split across feedback type by
three post-test timings the long-delayed implicit cell must be small. The k for that cell
is the number that decides the question and it is not publicly available. Against it,
Ellis, Loewen & Erlam (2006), *SSLA* 28(2):339–368, tested recasts against metalinguistic
explanation at one day and two weeks and found "a clear advantage for explicit feedback
over implicit feedback for both the delayed imitation and grammaticality judgement
post-tests."

**Prompts beat recasts less than everyone says.** In Lyster and Saito the difference is
significant **only in the within-group contrasts**. In the between-group analysis, which is
the one that controls for maturation and testing, recasts (0.53) and prompts (0.83) have
overlapping intervals, and explicit correction (0.84) is numerically largest and
distinguishable from neither. The design instruction survives in weaker form: a prompt
withholds the form and pushes the learner to produce it, which is the generation effect,
and it is the harder thing for a language model to do than smoothly reformulating.

There is a second-order irony here. Brown (2016), *Language Teaching Research*
20(4):436–458, `10.1177/1362168814563200`, meta-analysed **proportions** from observational
classroom studies rather than effects, and found that **recasts make up 57% of all
corrective feedback teachers actually give, prompts 30%**. The most-used type is the
least-supported one. `MEASURED-META`.

**Li's explicit/implicit and Lyster–Saito's prompts/recasts are the same studies in
different bins.** Lyster and Saito state that Ellis's and Ellis et al.'s "explicit CF" was
"operationalized as metalinguistic information in the form of a prompt. Therefore, we
categorized Ellis's explicit feedback as prompts." Treating "explicit beats implicit" and
"prompts beat recasts" as converging evidence double-counts.

**The measurement critique cuts both ways, which is not how it is usually reported.**
Norris & Ortega (2000), *Language Learning* 50(3), established that explicit instruction
beats implicit (**d = 1.13 vs 0.54**, non-overlapping intervals) and in the same paper
established why to distrust it: roughly **90% of outcome measures required discrete,
focused L2 use and only 10% extended communicative use** (p. 486), with selected and
constrained responses returning d = 1.20 against **d = 0.55 for free constructed
response**. But Lyster and Saito's classroom set inverts that: free constructed response is
their **largest** effect (0.97) and metalinguistic judgement their smallest (0.45).
Corrective feedback effects do show up on free production. Anyone asserting flatly that
these effects are artefacts of explicit-knowledge measures is overstating it for oral CF.

### 3.2 What "durable" means here, and the power problem

**Two to seven weeks.** Lyster and Saito define delayed as two to six weeks, and the
longest delay anywhere in their fifteen studies is seven. Norris and Ortega's average
immediate post-test came 1.57 days after treatment and their delayed post-tests 4.34 weeks
after. Ten of Lyster and Saito's fifteen studies ran any delayed post-test; 22 of Norris
and Ortega's 49 did. In Jeon and Kaya's pragmatics synthesis, one of thirteen did.

The delayed estimate in Lyster and Saito is *higher* than the immediate one (0.84 against
0.63), which reads better than it is: the ten studies contributing delayed effect sizes are
not the fifteen contributing immediate ones. Norris and Ortega's honest version is that
effects fell by about **one-fifth of a standard deviation** from immediate to delayed, with
their own hedge (p. 500) that the finding "should not be interpreted as indicative" given
how few studies had delayed post-tests.

**And the median study in this literature had 35 participants across all groups.** To
detect Lyster and Saito's own pooled effect of 0.74 at 80% power needs about 29 per group;
their median study has roughly twelve per cell, giving about **43% power** for d = 0.74 and
**25%** for the recast effect of 0.53. Lyster and Saito report no heterogeneity statistics,
no publication-bias assessment, no random-effects model and no inverse-variance weighting,
so a study of 179 counts the same as one of 25. Underpowered studies that reach
significance necessarily overestimate; with no bias assessment, these pooled values should
be read as upper bounds.

One more recalibration applies to every number above. Plonsky & Oswald (2014), *Language
Learning* 64(4):878–912, derived field-specific benchmarks from 346 studies and 91
meta-analyses (N > 604,000): for between-group d, **0.40 is small, 0.70 medium, 1.00
large**. Read against those, Lyster and Saito's 0.74 is medium and not "medium-to-large,"
their within-group 0.91 falls below medium, and recasts at 0.53 are barely above small.
The meta-analysts used Cohen's benchmarks, so every headline in this area drops a category
when read against its own field.

### 3.3 Written correction, where the null case is strongest

Truscott (1996) argued that grammar correction "has no place in writing courses and should
be abandoned," and his 2007 meta-analysis in *JSLW* 16(4) puts the point estimate at
**d = −0.1555** on new writing: "we can be 95% confident that if it has any actual
benefits, they are very small." Ferris's reply concedes more than it disputes ("Truscott is
right in asserting that the evidence supporting the effectiveness of error correction is
scant"), and by 2004 she reported that only **six studies in the entire literature make a
correction/no-correction comparison at all**, two of them over time. Later syntheses are
more favourable: Kang & Han (2015), *MLJ* 99(1), report g ≈ 0.54 across 21 studies, and
Lim & Renandya (2020), *TESL-EJ* 24(3), report **g = 0.59, 95% CI [0.423, 0.755],
Q = 83.11, τ² = 0.144, I² = 59.09%** across 35 studies. The two disagree in sign on two
headline moderators, which is Plonsky and Brown's dispersion finding in miniature.

Three results from this literature belong in any tutor's design file.

**Revision success is not learning.** Truscott & Hsu (2008), *JSLW* 17(4):292–305,
underlined errors for half a group and had both halves revise. The underlined group revised
significantly better. A week later everyone wrote a **new** narrative and "the two groups
were virtually identical" (**g = −0.068**). A tutor measuring whether the learner fixed the
flagged error is measuring the thing that does not transfer.

**The flagship positive result is narrower than its citation.** Bitchener and Knoch's
studies, including the 10-month one (n = 52, g = 0.642, the **smallest** in the set), target
two functions of the English article. Ekiert & di Gennaro's conceptual replication
(*Language Teaching* 54(1)) kept the design and widened the outcome to all article
functions, finding that "the same WCF may negatively impact the remaining non-targeted
article functions, especially for the group that received the most explicit WCF."

**Correction can cost something an accuracy measure cannot see.** Scherer, Graham & Busse
(2024), *Learning and Instruction* 93:101961, across 200 comparisons, report surface
feedback improving surface outcomes at g = 0.58 while moving **foreign-language learners'
deep-level outcomes at g = −0.23**. Grammar feedback measurably degrades content and
organisation for FL writers, and any study measuring only accuracy is blind to it.

**The cleanest oral-CF null is a failed self-replication.** Loewen & Erlam (2006),
*Computer Assisted Language Learning* 19(1):1–14, repeated Ellis, Loewen & Erlam (2006) in
a synchronous chat environment with N = 31 and found "no statistically significant gains in
response to either type of feedback." Two of the same authors, the same contrast, the
opposite result — from a study with about ten per cell, i.e. roughly 20% power for
d = 0.74. The positives and the nulls in this literature are equally underpowered.

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
vocabulary size, coverage and comprehension in the same learners and proposed two
thresholds: an **optimal** one at 8,000 families / 98% coverage and a **minimal** one at
4,000–5,000 families / 95% coverage. Their incidental observation is the useful one:
*"small increments of vocabulary knowledge contribute to reading comprehension even though
they hardly improve text coverage."* Schmitt, Jiang & Grabe (2011), *Modern Language
Journal* 95(1), found the same directly with 661 participants from eight countries — a
**relatively linear** relationship between percentage of vocabulary known and
comprehension, with **no threshold**.

Then the number itself failed to replicate. Kremmel, Indrarathne, Kormos & Suzuki (2023),
*Language Learning* 73(4):1127–1163,
[10.1111/lang.12622](https://doi.org/10.1111/lang.12622), preregistered with Open Data and
Open Materials badges, replicated Hu & Nation (2000) with 104 Sri Lankan adult learners at
five coverage densities. The study *"confirmed the original finding of a mostly linear
relationship between vocabulary coverage and reading comprehension but **failed to
replicate an inferred 98% coverage threshold as sufficient for adequate
comprehension**."* `MEASURED-RCT`. The original figure rests on a regression over 66 New
Zealand university students, and the replication found the relationship varies by genre
and response format, so the threshold is not a single quantity.

The load-bearing version: there is no cliff to get a learner over. There is a slope, its
useful range runs from roughly 4,000 to 9,000 word families, and every thousand families
buys a little more comprehension. That is a different design target from "unlock B1."

### 4.2 Incidental versus intentional, with real numbers on both

Webb, Uchihara & Yanagisawa (2023), *Language Teaching* 56(2), meta-analysed
**incidental** vocabulary learning from meaning-focused input: 24 studies, 29 effect
sizes, N = 2,771 (1,517 experimental, 1,254 control). Mean proportions of target words
learned: 9–18% on immediate post-tests, 6–17% on delayed. By mode: reading 17%/15%,
listening 15%/13%, reading-while-listening 13%/17%, viewing 7%/5%. `MEASURED-META`.

Webb, Yanagisawa & Uchihara (2020), *Modern Language Journal* 104(4), meta-analysed
**intentional** word-focused activities — flashcards, word lists, writing,
fill-in-the-blanks: 100 effect sizes from 22 studies. Average percentage gains
60.1% (meaning recall) and 58.5% (form recall) on immediate post-tests, falling to
39.4% and 25.1% on delayed post-tests. Between activities the range was 18.4% to
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
learning: r = .34. Repetition matters and explains about a ninth of the variance.
Encounters are not the mechanism people assume.

### 4.3 The transfer question, in its cleanest available form

The question this survey turns on is whether a scheduler that reliably produces
recognition of the items in its deck produces anything else. Vocabulary has an unusually
clean version because the field routinely measures both the taught words and a
standardised comprehension test in the same study.

Elleman, Lindo, Morphy & Compton (2009), *Journal of Research on Educational
Effectiveness* 2(1):1–44, meta-analysed 37 vocabulary interventions, pre-K to grade 12:

- effect on **custom** comprehension measures (passages containing the taught words):
  d = 0.50
- effect on **standardised** comprehension measures: d = 0.10
- among custom measures, controlling for method variables: students with reading
  difficulties d = 1.23 versus d = 0.39 for students without
- correlation between a study's vocabulary effect and its comprehension effect, among
  studies reporting both: r = 0.43

`MEASURED-META`. This is first-language vocabulary instruction, so the boundary being
crossed is not identical to the L2 case; it remains the clean version of the question, and
the answer is a five-fold attenuation from "comprehends text built around the taught
words" to "comprehends text."

The counterweight matters, because the naive reading of Elleman is that deliberate
vocabulary learning is shallow, and the psycholinguistics says otherwise. Elgort (2011),
*Language Learning* 61(2), taught 48 pseudowords by deliberate study and probed them with
masked repetition priming, form priming and automatic semantic priming in lexical
decision. All three effects appeared, and response-latency variability showed the items
were processed with higher automaticity than genuine low-frequency L2 words.
`MEASURED-RCT` (within-subject). Deliberate learning produces integrated, automatised
lexical entries.

Both results hold. Deck study builds genuine word knowledge; word knowledge is not
comprehension; the gap between them is where reading, listening and speaking practice has
to go. A tutor that ships a scheduler and calls vocabulary solved has built the d = 0.10
half.

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

This is the one skill where an AI tutor has an advantage that is not merely economic.
A learner will say a sentence badly to a machine that they would not say at all to a
person, and will say it eighty times. No human tutor supplies that, at any price. The
question is whether the machine on the other end can tell the difference between the
eighty attempts.

### 5.1 What is measured on automated pronunciation feedback

The CALL literature's answer is positive and its own authors say it should not be
believed yet.

Mahdi & Al Khateeb (2019), *Review of Education* 7(3), meta-analysed 20 studies,
1,014 participants, computer-assisted pronunciation training versus traditional
instruction: d = 0.68, equally effective for young and adult learners, larger for
beginners and intermediates than for advanced learners. `MEASURED-META`. Their own
closing caution is the part to carry forward:

> *"The small number of studies, all of very low quality (most with fewer than 100
> participants, conducted within the same institution using intervention-related
> assessments) means that the evidence of effectiveness can only be indicative and not
> conclusive."*

"Intervention-related assessments" is the same defect as §2.1: the test is made of the
material that was trained. A meta-analysis that warns its own readers this way is doing
its job, and the d = 0.68 should not be quoted without the sentence attached.

Almusharraf, Mahdi, Al-Nofaie & Aljasser (2024), *J. Computer Assisted Learning* 40(6),
updated the synthesis to 31 studies and 42 effect sizes from experimental-versus-control
designs. Its abstract reports every result as a verbal magnitude, "medium" or "large,"
with no numeric effect size, confidence interval or heterogeneity statistic, and the
full text was not retrievable here. It is recorded so that it is not silently treated as
a second, converging estimate of Mahdi & Al Khateeb.

The distinction the whole area rests on is Munro and Derwing's separation of
**accentedness** (how different a speaker sounds from a reference variety),
**comprehensibility** (how much effort a listener spends) and **intelligibility** (how much
the listener actually recovers). The three dissociate: heavily accented speech is routinely
fully intelligible, and only the last two are legitimate instructional targets. Their
primary papers were **not retrieved in this session**, so the framework is described here
and no effect size is attributed to it. The design consequence stands regardless: most CAPT
tools score similarity to a native reference, which is an accentedness measure, and an AI
pronunciation tutor built that way optimises the one construct the field says is not the
goal.

### 5.2 The benchmark that bounds the product

The relevant question for a build is not whether pronunciation training works. It is
whether the machine can detect the error. That is a benchmark question, and it has an
answer.

Liu, Cui, Gu & Wang (2026), *Unlocking Large Audio-Language Models for Interactive
Language Learning*, [arXiv:2601.14744](https://arxiv.org/abs/2601.14744), evaluated
cascaded ASR-plus-LLM pipelines and end-to-end audio-language models on mispronunciation
detection over L2-ARCTIC (read L2 English with phoneme-level annotation of actual learner
errors), one-shot prompted. `MEASURED-BENCH`. Detection precision / recall / F1:

| System | P | R | F1 |
|---|---|---|---|
| Whisper Large + Mistral-7B | 48.9 | 3.4 | 6.4 |
| Whisper Small + Llama-3.1-8B | 53.3 | 12.1 | 19.7 |
| Wav2vec2 Base + Llama-3.1-8B (best cascade) | 53.8 | 17.8 | 26.8 |
| Qwen2-Audio (end-to-end) | 41.7 | 22.0 | 28.8 |
| GPT-4o-Audio (end-to-end) | 52.7 | 41.3 | 46.3 |
| Their instruction-tuned Whisper-Large + Llama-3 | 48.9 | 87.7 | 62.8 |

Three readings, in ascending order of consequence.

**A frontier audio model misses most mispronunciations.** GPT-4o-Audio, the strongest
off-the-shelf system tested, recovers 41.3% of annotated errors and is right about
52.7% of the errors it claims. On a GPT-4o-judged 1–5 rating of the *feedback text*, it
scored 2.145; the best cascade scored 1.426; the authors' tuned model 2.328. Nothing in
the table is near usable-without-review.

**Better ASR makes it worse.** Whisper Small beats Whisper Medium beats Whisper Large,
with the same LLM; Wav2vec2 Base beats Wav2vec2 Large. The authors' explanation:
*"stronger ASR models tend to correct pronunciation errors during transcription due to
their robustness to accent variations, preventing them from accurately reflecting
learners' speech errors."* A speech recogniser's entire objective is to recover the word
the speaker intended. Every improvement in that objective destroys the signal a
pronunciation tutor needs. This is the measured form of the ambiguity in §2.1: if the
Tehran learners were talking to a speech-to-text pipeline, the model was reading a
transcript that had already fixed their errors.

**The best purpose-built systems reach F1 ≈ 0.60–0.72 on read speech.** The 2026
mispronunciation-detection literature on the same benchmark reports F1 = 59.52%
(arXiv:2606.05569) and 71.77% (arXiv:2604.22133) for dedicated architectures.
`MEASURED-BENCH`. Read speech is the easy case: known target text, no spontaneity, no
disfluency.

Against that, a useful equivalence result. Neri, Mich, Gerosa & Giuliani (2008),
*Computer Assisted Language Learning* 21(5), gave eleven-year-olds either teacher-fronted
pronunciation instruction or a CAPT system with a **simple** ASR component, and both
groups improved significantly on word-level pronunciation quality, including on words
judged particularly difficult, with the two modes comparable. `MEASURED-RCT` (small,
word-level, short-term). A crude recogniser used to structure repeated practice matched a
teacher, which suggests the work is being done by the structured repetition and not by
diagnostic accuracy.

### 5.3 Willingness to communicate, and the transfer nobody has measured

Anxiety in L2 learning is real and measured. Teimouri, Goetze & Plonsky (2019), *Studies in
Second Language Acquisition* 41(2), meta-analysed 97 reports, 105 independent samples,
N = 19,933, 23 countries, 216 correlations: mean r = −0.36 between L2 anxiety and
language achievement. `MEASURED-META`. It is the best estimate in the area and it is
correlational, so it establishes no direction.

The chatbot-and-WTC literature is where marketing and measurement diverge. Waluyo &
Pratiwi (2025), *JALT CALL Journal* 21(2), synthesised the Asian EFL evidence across eight
countries and reported that chatbot interaction enhances willingness to communicate,
communicative confidence and motivation by reducing speaking anxiety. It also reported, in
the same abstract:

> *"[E]vidence on long-term transfer to real-world communication remains scarce."*

`MEASURED-META` (narrative meta-synthesis, so no pooled estimate). The pattern is
consistent and it is entirely made of self-report. Willingness to communicate is a
questionnaire. Communicative confidence is a questionnaire. Speaking anxiety is the
FLCAS, a questionnaire. Every one of those can move without a single additional word
being spoken to a human being.

**What is absent, stated as specifically as I can make it.** No study located in this
session measured whether practice with an AI conversational partner changes behaviour
with a human interlocutor: minutes of unscripted L2 speech produced with a person,
turns initiated, conversations not avoided, or a blind rating of comprehensibility in a
human-to-human exchange. The trial would need an AI-practice arm and a human-practice arm
matched on speaking minutes, with the primary outcome collected in a **human** interaction
by a rater blind to condition, at least four weeks after the last AI session. Currently
that trial does not exist in ERIC.

---

## 6. The critical-period question, stated accurately

The folk version says adults cannot learn languages. The literature says something much
narrower, and the most-cited recent attempt to say it quantitatively has a published
reanalysis that dissolves its headline.

**Hartshorne, Tenenbaum & Pinker (2018),** *Cognition* 177:263–277,
[10.1016/j.cognition.2018.04.007](https://doi.org/10.1016/j.cognition.2018.04.007).
Two-thirds of a million English speakers took a viral online grammar quiz. Fitting an
exponential-learning-with-sigmoidal-decay model, the authors concluded that the *rate* of
grammar learning stays high until about 17.4 years of age and then drops sharply. The
claim is about learning rate, not about ceiling: a learner who starts at 17 can still
improve, but does so more slowly, and because near-native grammar takes roughly thirty
years of exposure, starting much after about 10 makes native-like attainment unlikely on
a normal lifespan. `OBSERVED` — a cross-sectional web survey, not an experiment.

**van der Slik, Schepens, Bongaerts & van Hout (2021),** *Language Learning* 71(1),
[10.1111/lang.12470](https://doi.org/10.1111/lang.12470), reanalysed the same data and
concluded that *"their overall conclusion of one sharply defined critical age at 17.4 for
all language learners is based on artificial results."* Fitted separately by learner type,
a **continuous** decay model fits better for monolinguals, bilinguals and early-immersion
learners; only non-immersion and later-immersion learners fit a discontinuous model, with
break points at 18.6 and 19.0 years. Their reading: those break points look like
**schooling effects**, produced by changes in living circumstances and socialisation
around the end of secondary education, not by a cognitive developmental window.
`MEASURED-META` (reanalysis of the original dataset, so not independent evidence — the
same data, better partitioned).

**Vanhove (2013),** *PLOS ONE* 8(7):e69172,
[10.1371/journal.pone.0069172](https://doi.org/10.1371/journal.pone.0069172), makes the
prior methodological point: a critical period requires a **discontinuity**, and the
analyses this literature usually runs cannot distinguish one from a smooth decline.
Reanalysing two datasets with piecewise regression, he finds the predicted age patterns
are not cross-linguistically robust.

A further inferential problem sits in the sampling, where no reanalysis can reach it. The
respondents chose to take a viral quiz billed as a grammar test, in English, on a social
network. Age of acquisition, current age, immigration history, education and willingness
to take an English grammar quiz for fun are all correlated in that population, with no
sampling frame to reweight against.

**What survives.** Age effects are real, they are largest for phonology and smallest for
vocabulary, and they are gradual. Adults are *faster* than children in the early stages of
naturalistic acquisition, and children overtake later. For a product the operative fact is
that nothing here identifies an age past which instruction stops working, and the one
number everyone quotes has a published reanalysis attributing it to leaving school.

---

## 7. The commercial reality

Duolingo appears 93 times in this corpus and never once as evidence about acquisition.
That is defensible, and the reason is worth setting out, because the largest body of
efficacy research in language learning is a vendor's. Applying the rule that a `VENDOR`
claim is never restated as a finding means reading the studies anyway, describing their
designs, and saying which claim rests on which.

### 7.1 The 34 hours

**Vesselinov & Grego (2012), "Duolingo Effectiveness Study."** `VENDOR`
(Duolingo-funded, external authors; self-published PDF, no DOI, never peer-reviewed).

The design has no control group. It is a pre/post within-subject study, and the "one
university semester" comparison is against the WebCAPE placement cut-off of 270 points,
a scoring threshold, not against students. The 34 hours is arithmetic: 270 ÷ 8.1
points-per-hour, extrapolated linearly from zero. The recruitment funnel, from the report's
Figure A1: 727 viewed a banner ad shown to logged-in Duolingo Spanish learners → 556
completed the entry survey → 386 eligible → 211 took a baseline WebCAPE → 196 sampled →
88 analysed. Mean actual study time was 22 hours, the range 2 to 133, and **16%
(n = 14) scored the same or lower at post-test**. WebCAPE tests vocabulary, reading and
grammar; the authors themselves recommend adding *"some test of spoken proficiency."*

Krashen (2014), *International Journal of Foreign Language Teaching*, made the decisive
statistical point: the **median** gain rate was 3.9 points per hour against a mean of 8.1,
because the distribution is heavily right-skewed. The same arithmetic on the median gives
about 69 hours.

The same two authors ran the same design for a series of vendors: Rosetta Stone (2009) 55
hours; Duolingo (2012) 34; an **anonymised "Language App"** (2015) 25, published under a
generic name because *"the report was not officially made public"*; Babbel (2016) 21;
italki (2018) 19. Each successive sponsor gets a better number, and the 2015 report is a
file drawer with the door open.

### 7.2 The company's own later measurement contradicts its famous one

**Jiang, Rollinson, Plonsky, Gustafson & Pajak (2021),** *Foreign Language Annals*
54(4):974–1002, [10.1111/flan.12600](https://doi.org/10.1111/flan.12600). `VENDOR`
(four of five authors are Duolingo employees; peer-reviewed).

Cross-sectional, post-test only. No control group and no pre-test. Learners reaching
Checkpoint 5 were tested once and compared by ANOVA against published means and SDs from
other researchers' university cohorts (Tschirner 2016; Rubio & Hacking 2019). n = 225,
paid $100 each, over 80% holding at least a bachelor's degree. ACTFL Reading and Listening
administered externally by Language Testing International; the paper states plainly that
**"No other skills were assessed."** Outcome: Reading at Intermediate Low, Listening at
Novice High, with Spanish listening scoring significantly lower than the university
comparison cohort.

The number that matters is in the methods. Median time to finish the beginning content was
112 hours (125 Spanish, 99 French); the 2012 study priced roughly the same milestone at
34, and the follow-up through Unit 7 (DRR-21-03, n = 340) reports a median of **203
hours**. Same company, same product, its own instrumentation, and the hours figure has
grown six-fold while the marketing number stayed put.

`OBSERVED`: **no Duolingo Research Report before DRR-25-06 (June 2025) used a control
group.** Every reading, listening and speaking report is single-cohort and post-test-only,
benchmarked against published university averages or against Duolingo's own CEFR
expectations, with heavy selection (DRR-24-04: 3,153 invitations → 165 tested, 5.2%).
Where fairness is owed: the instruments are mostly external and reputable (ACTFL via LTI,
Pearson Versant, Avant STAMP 4S), and DRR-25-06 appears to be a genuine randomised trial,
n = 567 with Versant pre/post — which is not listed on the company's `/efficacy/studies`
page and whose live link returns 403.

### 7.3 The independent record, which is thin and mostly null

| Study | Independence | Design | Result |
|---|---|---|---|
| Rachels & Rockinson-Szapkiw (2018), *CALL* 31(1–2), [10.1080/09588221.2017.1382536](https://doi.org/10.1080/09588221.2017.1382536) | Independent | Quasi-exp., grades 3–4, 12 weeks, Duolingo vs regular Spanish class | Null on achievement and on self-efficacy (§8.2) |
| Loewen et al. (2019), *ReCALL* 31(3), [10.1017/S0958344019000065](https://doi.org/10.1017/S0958344019000065) | Independent | n = 9, Turkish, one semester, self-study | Gains; time-on-app correlated with gains; not an efficacy estimate |
| Kim, Payant, Skalicky & Namkung (2026), *SSLA*, [10.1017/S0272263126101521](https://doi.org/10.1017/S0272263126101521) | Duolingo Efficacy Research Program funding | Classroom-only (58) vs Duolingo-only (65) vs both (60), 16 weeks, beginner French | All three improved by similar magnitudes on proficiency, grammar, vocabulary and communicative competence; the only difference was *tu/vous* pragmatics favouring Classroom+Duolingo |
| Meltzer et al. (2023), *Aging Neuropsychol. Cogn.*, [10.1080/13825585.2021.1991262](https://doi.org/10.1080/13825585.2021.1991262), NCT03638882 | Independent | True RCT, n = 76, ages 65–75, Duolingo vs BrainHQ vs waitlist, 4 months | A cognitive-ageing trial. Duolingo matched BrainHQ on two measures; BrainHQ was superior on reaction time |
| James & Mayer (2019), *Appl. Cogn. Psychol.* | Independent | RCT, n = 64, Duolingo vs matched-content slideshow | Null on achievement, large effects on affect (§8.1) |

The Kim et al. result deserves its own sentence because it cuts both ways and gets
reported one way. Sixteen weeks of Duolingo alone produced beginner French gains
statistically similar to a semester of university classroom instruction. That is a real
achievement for a free app. It is also a null for the app's incremental value, and a null
for the classroom's, and the study was funded by the vendor whose product came out level
with a university course.

**The strongest single sentence in the independent literature is still Loewen et al.'s
framing** that one *commissioned* study found favourable outcomes while limited
independent research *"reported issues related to learner persistence, motivation, and
program efficacy."*

### 7.4 The English Test, where the vendor research is strongest and one result went missing

The Duolingo English Test carries far more psychometric apparatus than the learning app.
Its Technical Manual is self-published and not peer-reviewed, and carries a DOI under
Duolingo's own self-assigned prefix `10.46999`, which makes it look peer-reviewed in a
reference list. Concurrent validity, from the manual: DET Overall against official TOEFL
iBT reports (n = 328) r = .71 overall, .82 center-based, **.61 for the Home
Edition** — and the Home Edition is the product actually used in admissions. Against
IELTS (n = 1,943), Overall r = .73, but subscores **Writing .54, Reading .53,
Listening .57**, and subscore concordance tables are published from those.

**Isaacs, Hu, Trenkic & Varga (2023),** *Language Testing* 40(3):748–770,
[10.1177/02655322231158550](https://doi.org/10.1177/02655322231158550), is
**Duolingo-commissioned** by its own funding statement, which matters because its result is
unfavourable: across 1,881 DET-admitted students at a large London university, DET
correlated with first-year credit-weighted grades at adj. r = 0.195 for postgraduates
and adj. r = −0.112 for undergraduates, and DET-admitted students had lower academic
success than IELTS and TOEFL entrants. That paper is **cited zero times in either the 2025
or the 2026 Technical Manual**, whose predictive-validity section rests instead on a blog
post with no paper and no methodology document. Wagner (2020), *Language Assessment
Quarterly* 17(3), independent: *"the use of DET scores cannot be recommended."*

### 7.5 What the audited filings say, and one sentence in them that is not supported

`FILING` — Duolingo, Inc., CIK 0001562088. Q1 2026 Form 10-Q (filed 2026-05-05):
DAU 56.5 million (up 21% year over year from 46.6 M), MAU 137.8 million, **paid
subscribers 12.5 million**, subscription bookings $268.065 M for the quarter. FY2025
10-K: DAU 52.7 M against MAU 133.1 M (DAU/MAU ≈ 39.6%), paid subscribers 12.2 M
(~9% of MAU), and roughly 43 M users with a seven-day streak against roughly 15 M with a
365-day streak. The FY2022 10-K disclosed over 800 million cumulative downloads
against 60.7 M MAU; the FY2025 filing no longer reports cumulative downloads.

**No filing discloses course completion.** Searches of the FY2025 10-K for "complete a
course," "churn," and "learning objectives" return nothing.

And this, from the FY2025 10-K:

> *"According to an internal study, learners who completed five sections of Duolingo
> achieved proficiency comparable to five university semesters of language education.
> **Independent studies corroborate this finding**: Duolingo learners' speaking skills
> were found to match those of university students…"*

The company labels its own work "internal," correctly. The studies that fit the
description of the corroborating work are Duolingo-funded (Smith, Jiang & Peters 2024 in
*Language Learning & Technology* states *"This study was supported financially by
Duolingo"*; the Colombia comparison is a Duolingo whitepaper whose link is dead). The
word "independent" is doing work in an audited document that the underlying papers do not
support. Note also that FY2022 said "four university semesters" and FY2025 says "five."

`INFERENCE`. The rule that a vendor claim is never restated as a finding is not an
inconvenience here. It is the only thing that separates "Duolingo is the most successful
habit-formation product in the history of education" — which is true, audited, and
remarkable — from "Duolingo teaches a language better than the alternative," for which no
randomised evidence exists in either direction.

---

## 8. Nulls, given their own space

The brief asks for one. There are four worth the space, and they line up.

### 8.1 The primary null: same content, gamified wrapper, no achievement difference

**James, Kelsey K. & Mayer, Richard E. (2019), "Learning a second language by playing a
game," *Applied Cognitive Psychology* 33(4).** `MEASURED-RCT`.

Sixty-four college students learned Italian at home over seven sessions, either by
playing Duolingo or by working through **an online slideshow covering the same material**.
Matched content, matched sessions, randomised assignment. Result:

> *"Although the groups did not differ significantly on achievement posttests, the
> Duolingo group rated their learning experience as significantly more enjoyable
> (d = 0.77), more appealing (d = 1.17), and less difficult (d = 0.51), and was
> significantly more willing to continue with similar learning experiences (d = 1.39)."*

This is the cleanest experiment in the consumer-language-app literature and it is a null
on the outcome and a set of large effects on affect. The affective effects are not
nothing — d = 1.39 on willingness to continue is exactly the variable F6 argues is the
binding constraint, and a learner who continues learns more than one who quits. But the
result forecloses the claim that gamification *teaches*. Over seven sessions of identical
content it did not.

### 8.2 A null reported as a success, in the same sentence

**Rachels, Jason R. & Rockinson-Szapkiw, Amanda J. (2018), "The effects of a mobile
gamification app on elementary students' Spanish achievement and self-efficacy,"
*Computer Assisted Language Learning* 31(1–2):72–89.** `OBSERVED`
(quasi-experimental, non-equivalent control group).

Third and fourth graders, twelve weeks. The treatment group's Spanish instruction *was*
Duolingo; the control group had its regular Spanish class. A 50-item vocabulary and
grammar test both directions, plus the PALS academic-efficacy subscale, as pre- and
post-tests, analysed by ANCOVA. From the abstract:

> *"An analysis of covariance showed no significant difference in students' Spanish
> achievement or in academic self-efficacy between students who used Duolingo® and
> students who were taught with traditional face-to-face instruction. **This demonstrates
> that Duolingo® is a useful tool for teaching Spanish to elementary students.**"*

Those two sentences are adjacent in the published abstract. A non-significant difference in
an underpowered quasi-experiment is being reported as a demonstration of usefulness.
Equivalence is a defensible thing to want to claim, but the study was not designed or
powered as an equivalence trial and specifies no equivalence margin. The move from "we did
not detect a difference" to "it works" is the most common error in this literature, and it
is recorded here because a survey that only counts effect sizes will read this paper as
supportive.

### 8.3 Two more, briefly

Soori, Khojasteh & Javed (2025), §2.2: AI feedback versus experienced-teacher video
feedback on overall IELTS writing, mean difference 0.079 bands, p = 0.921, with task
achievement at p = 1.000 and grammatical accuracy numerically favouring the teacher. The
title and abstract report the hybrid advantage and never mention this contrast.
`MEASURED-RCT` (cluster-assigned).

Fütterer et al. (2026), *Educational Psychology Review*, n = 371, Grades 7–9, six 45-minute
sessions **in regular physics or English lessons**, two scaffolded GenAI conditions against
a control using **standard ChatGPT**: *"no statistically significant advantages of either
intervention over the control condition… for effort, domain-specific knowledge, or
elaboration-based strategy use"* (doi:10.1007/s10648-026-10133-8; E3 §7.3, survey §23).
`MEASURED-RCT`. E3 read this as the K-12 core-subject result. Half its sessions ran in
English lessons, which also makes it the only randomised test in the ERIC set of whether
designed pedagogy beats plain ChatGPT in a language classroom. It did not.

See also §3.3 for Loewen & Erlam (2006), a failed self-replication of the flagship
explicit-feedback study, and Truscott & Hsu (2008), where revision gains did not survive to
a new piece of writing (g = −0.068).

---

## 9. What is now buildable, the experiment worth running, and what I could not find out

### 9.1 Buildable now

**Hold items out, and report the two numbers separately.** Every trial in §2 and every
study behind the d = 0.68 CAPT estimate scores the material that was trained. In language
this is avoidable for free: for any target set, a model can generate a matched held-out
probe set controlled for frequency band, phonological structure and part of speech, and
the tutor reports trained-item and untrained-item performance as two numbers. `SPEC`.
Nothing in this literature would have survived that reporting convention unchanged, which
is the reason to adopt it.

**Generate input at a measured coverage, and validate the lexical profile rather than
trusting the prompt.** Comprehension is close to linear in the proportion of words known
(Schmitt et al. 2011), the 98% threshold failed replication (Kremmel et al. 2023), and
the useful range runs from roughly 4,000 to 9,000 word families. So the design target is
not a level to unlock; it is a coverage to hold, against the learner's own measured
vocabulary, on material they want to read. A model can write to a lexical profile, but
only with constraints: the CEFR-controlled generation work reports that unconstrained
prompting gives *"weak control"* while prompting plus explicit lexical constraints reaches
0.91 cosine similarity to reference profiles (arXiv:2606.21981, Arabic). `MEASURED-BENCH`.
Build the validator, not just the prompt.

**Build the speaking loop; do not ship phoneme-level correction as though it worked.**
The unique advantage is unlimited low-stakes practice with a partner who cannot be
embarrassed. The diagnostic layer is not ready: GPT-4o-Audio at F1 = 46.3 on read
speech. Ship practice volume and comprehensibility-level feedback, and hold segmental
correction back.

**And one design inversion the benchmark hands over.** Because stronger ASR *repairs*
learner errors before any model sees them (§5.2), a deliberately non-robust recogniser is
a better proxy for a real listener's difficulty than a robust one. Run the learner's
speech through a small, accent-brittle recogniser and treat its failures as an
intelligibility signal. `SPEC`, untested, and cheap to test.

**Withhold the form.** A language model's reflex when a learner produces a wrong sentence
is to restate it correctly, which is a recast, the least effective of the three feedback
types in the only classroom meta-analysis that separates them (§3.1), and the one teachers
already over-supply at 57% of all corrections. Prompting the learner to self-repair is
harder to generate and better supported. This is the cheapest pedagogical edit available in
the whole domain: it is a change to a system prompt.

**Say the vendor sentence out loud.** No randomised trial has shown that any consumer
language app teaches a language better than an alternative, in either direction. A product
that wants to claim otherwise has to run the trial.

### 9.2 The experiment

**Does AI speaking practice transfer to speaking with a person?** Three arms, individually
randomised: (A) 12 weeks of AI conversational practice, (B) 12 weeks of human conversation
partners matched on **speaking minutes**, (C) matched-time non-speaking study. Primary
outcome collected **four weeks after the last session**, in an unscripted conversation
with a human interlocutor the participant has not met, scored for **comprehensibility** on
a nine-point scale by two raters blind to condition, with intelligibility (orthographic
transcription accuracy by naive listeners) as the co-primary. Secondary: minutes of L2
speech produced, turns initiated, and self-reported willingness to communicate, so the
self-report and behavioural measures can be compared in the same sample.

**Power.** The prior to plan against is not the CAPT d = 0.68 or the d ≈ 1.6 of §2.1, both
of which come from trained-item outcomes. It is Lee & Lee's control-adjusted d = 0.39
against business-as-usual, together with the AI-versus-human null of §2.2. So plan for
d = 0.35 on the A-versus-C contrast and be prepared for A ≈ B. At α = .05 two-sided
and 80% power, a two-arm comparison at d = 0.35 needs 129 per arm; three arms with a
hierarchical testing order (A vs C, then A vs B) and 20% attrition gives n ≈ 465. If
only two arms are affordable, drop C and run A against B, the question a builder actually
faces, at 310 participants. For contrast, §2.1's trial had 30 per arm, detecting only
d ≥ 0.72, and §2.2's had about 29 per arm before any correction for its three clusters.

**Why this one.** It is the only place where AI holds a capability advantage that is not
economic, it is the outcome the marketed value proposition rests on, and ERIC contains
zero trials measuring it. A null here would be worth more than another significant result
on trained items.

A cheaper second experiment if the first is unaffordable: randomise learners to a spaced
deck of 300 word families versus matched-time reading of text containing those families,
and measure recall of the 300, comprehension of **novel** text at controlled coverage, and
lexical-decision priming, at eight weeks. That is Elleman's d = 0.50 against d = 0.10 run
inside a single L2 sample, and no one has run it.

### 9.3 What I could not find out

- **The largest trial is unread.** Zhang et al. (2026), N = 436, is behind Sage with no
  repository copy. Its abstract reports pre-post change for the treatment arm only.
  Everything in §2.3 is a description of an abstract.
- **Whether the Tehran learners' ChatGPT could hear them.** The paper says "the voice
  feature." If it was speech-to-text, the model never received audio, and §5.2 shows that
  matters a great deal. Unresolvable from the published text.
- **The confidence interval on g = 0.484**, the best chatbot-language meta-analytic
  estimate (Wang et al. 2024, *RER*). Sage 403.
- **Almusharraf et al. (2024)'s numbers.** A 2024 CAPT meta-analysis of 31 studies whose
  public abstract reports only "medium" and "large." Not usable, and not counted here as a
  second estimate.
- **Li (2010) in full.** The most-cited corrective-feedback meta-analysis is closed access
  with no repository copy anywhere. Its explicit/implicit contrast, its post-test-timing
  pattern and every k it reports are unread. The pooled d values circulating for it are
  second-hand and are not asserted in §3.
- **Gregg (1984)**, the canonical falsifiability critique of Krashen: paywalled, no
  published abstract, not read. Its argument is described, not quoted.
- **Brown, Liu & Norouzian (2023)**, *Language Teaching Research*,
  `10.1177/13621688221147374`, the state of the art on written corrective feedback and the
  only meta-analysis modelling short-, medium- and long-term effects separately. Abstract
  only; every point estimate and credible interval unretrieved.
- **Egger's-test values in Lee & Lee (2024).** Reported as a figure only; the numbers are
  not in the text.
- **Rachels & Rockinson-Szapkiw's F, p and effect sizes.** Paywalled, and no repository
  copy. The null is documented from the abstract; its precision is not.
- **Duolingo course completion.** Not disclosed in any SEC filing, and the FY2025 10-K
  drops the cumulative-downloads figure the FY2022 10-K carried.
- **Whether any of this holds outside high-resource languages.** Every trial here is
  English as a foreign language, except Kim et al.'s French and James & Mayer's Italian.
  F4 §3.5 records frontier models scoring at or near chance on around thirty of 122
  language variants. For those languages the pedagogical architecture is not the
  binding constraint and this report has nothing to say about them.
