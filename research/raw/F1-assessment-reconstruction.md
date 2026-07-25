---
title: "The Collapse and Reconstruction of Assessment"
wave: F
date_researched: 2026-07-25
sources_count: 85
---

# The Collapse and Reconstruction of Assessment

## 0. The question, stated precisely

The panic formula is "AI can write the essay." The useful formulation is harder: **when a machine can produce any artifact a student could produce, at negligible cost, what inference can an educator still license from an observation?**

Assessment has never been about artifacts. It is an inference: from something observed, to a claim about a person, licensed by an argument (Messick 1990, ETS RR-90-11, doi:10.1002/j.2333-8504.1990.tb01343.x; Kane's argument-based framing as applied to education in Schuwirth & van der Vleuten 2012, *Medical Education*, doi:10.1111/j.1365-2923.2011.04098.x). The essay was never the evidence. It was a *sampling instrument* — and a spectacularly cheap one, which is why it colonised education.

Four distinct claims were bundled into that one instrument, and generative AI has pulled them apart:

| Claim | Form | Who needs it |
|---|---|---|
| **Product claim** | "This artifact is good." | The discipline; the reader |
| **Process claim** | "This person made this artifact." | The integrity office; the credential |
| **Capability claim** | "This person can produce artifacts like this, unaided, again." | Employers, licensing boards, downstream courses |
| **Learning claim** | "This person's capability changed between t₁ and t₂." | The teacher, and the student |

Before 2022, one observation licensed all four, because human production cost welded them together. It no longer does. **Almost every confused argument in the current literature is a failure to say which of the four claims is at stake.** "AI-proof assessment" usually means securing the process claim. "Authentic assessment" usually means strengthening the capability claim. "Assessment for learning" abandons both in favour of the learning claim. These are not competing schools. They are different jobs, and they now need different instruments.

---

## 1. The forgery margin: the actual thing that broke

Here is the load-bearing idea of this section, and it is not in the literature in this form.

**Every assessment in history has been secured not by its construct but by a cost asymmetry: the cost of producing a credible fake exceeded the cost of actually learning.** Call the ratio the *forgery margin*.

- Supervised written exams: forging requires impersonation or smuggled material — high cost, high risk.
- Coursework essays: forging requires a ghostwriter. Contract cheating survived precisely at the price point where it was affordable to a minority — reported prevalence of 6–15.7% (Ison 2020, *Online Learning*, doi:10.24059/olj.v24i2.2096). That is not a moral fact about students. It is a price.
- Lab reports, problem sets, reading responses: forging required a competent friend, so the margin was set by social capital.

Generative AI did not invent cheating and did not, on the available evidence, produce an explosion of it. A pre/post survey of US high school students spanning ChatGPT's release found self-reported cheating rates essentially flat (Lee et al. 2024, *Computers and Education: Artificial Intelligence*, doi:10.1016/j.caeai.2024.100253). What AI did was drive the *forgery cost* of one enormous class of artifacts to approximately zero while leaving the *learning cost* untouched. The margin collapsed. The proportion of people willing to exploit it barely moved; the population who *could* exploit it became everyone.

This reframing is immediately generative, because it says the design problem is not "invent tasks AI cannot do" — a losing race, and a race whose finish line recedes annually. The design problem is: **restore a forgery margin.** There are exactly four ways to do that, and every serious proposal in the literature is one of them:

1. **Bind the response to real time.** Orals, interactive vivas, live problem-solving. Forgery requires an undetectable real-time channel plus the ability to use it under conversational pressure.
2. **Bind the claim to a verifiable object.** Proof assistants, test suites, executable notebooks, replication on withheld data. There is nothing to forge, because the claim is *checked*, not judged.
3. **Bind the artifact to a process trace.** Keystroke logs, version control, revision history. Forgery requires simulating a plausible human trajectory.
4. **Abandon per-task security; secure the aggregate.** Programmatic assessment: many low-stakes observations, decisions made at programme level, no single data point load-bearing (van der Vleuten 2016, *Medical Science Educator*, doi:10.1007/s40670-016-0343-7; Baartman et al. 2022, *Frontiers in Education*, doi:10.3389/feduc.2022.931980; Govaerts et al. 2022, *Education Sciences*, doi:10.3390/educsci12100717).

**Detection is not on this list.** That is not an oversight — it is the diagnosis. Detection attempts to recover the margin *post hoc, from the artifact itself*, after the margin has already gone to zero. It is the only strategy that tries to extract information that is no longer there.

---

## 2. The homework apocalypse and the detector catastrophe

### 2.1 Detection is impossible in principle and harmful in practice

The theoretical result is clean. Sadasivan et al. (arXiv:2303.11156) bound the AUROC of the *best possible* detector by the total variation distance between the human and machine text distributions: as models improve, the distributions converge, and the achievable AUROC of any detector — present or future, however clever — falls toward chance. A 2026 preprint pushes this to a formal impossibility result absent generator cooperation such as watermarking (Silva 2026, SSRN 6272998; preprint, unreviewed). Empirically, the attack is trivial: paraphrasing defeats detectors, with retrieval over generator outputs the only effective defence — which requires the generator's cooperation and its logs (Krishna et al., NeurIPS 2023, doi:10.52202/075280-1195).

The empirical evaluations concur. The largest comparative test — 14 systems, including Turnitin and PlagiarismCheck — concluded the tools are "neither accurate nor reliable," with a systematic bias toward classifying text as human-written, and performance degrading sharply under obfuscation (Weber-Wulff et al. 2023, *International Journal for Educational Integrity*, doi:10.1007/s40979-023-00146-z). Independent evaluations found inconsistency across tools and markedly worse detection of GPT-4 output than GPT-3.5 (Elkhatat et al. 2023, doi:10.1007/s40979-023-00140-5; Dalalah & Dalalah 2023, *International Journal of Management Education*, doi:10.1016/j.ijme.2023.100822).

### 2.2 The bias finding is worse than usually reported — and it is not a bug

Liang et al. (2023, *Patterns*, doi:10.1016/j.patter.2023.100779) is the single most damning study in this literature, and it is usually cited too weakly. Seven widely deployed detectors were run on TOEFL essays by non-native English writers and on US 8th-graders' essays:

- **61.22% average false-positive rate** on non-native writers' essays, versus **~5.19%** on native writers' essays.
- **19.78% (18 of 91) of TOEFL essays were unanimously flagged as AI-authored by all seven detectors.**
- **97.80% were flagged by at least one.**
- Prompting an LLM to rewrite the same essays with more "literary" language dropped the false-positive rate from 61.22% to 11.77% — and dropped detection of genuinely AI-generated text from up to 100% to as low as 13%.
- The mechanism is explicit: unanimously flagged essays had significantly *lower perplexity*.

Replication work confirms the bias persists across newer detector generations (Al Ali et al. 2026, EACL Student Research Workshop, doi:10.18653/v1/2026.eacl-srw.20). Reviews extend the affected populations to neurodivergent writers and to formal-genre writing whose conventions produce low-perplexity prose — medical abstracts, legal briefs, methods sections (Angelier 2026, SSRN 6356858; Sorochkin 2026, SocArXiv, doi:10.31235/osf.io/qnkrw_v1 — both preprints, treat as indicative).

**The strong claim I want to make: the false positive is not a malfunction. It is the classifier working correctly.** These detectors measure distance from the distributional centre of unconstrained fluent English. Writing that is fluent-but-conventional — restricted vocabulary, high-frequency collocations, textbook structure — *is the signal*. A detector is therefore, quite precisely, a **conventionality meter**. And conventionality is what a writing course explicitly teaches to a second-language writer. The construct the detector measures is negatively correlated with the construct the course develops. That is a validity failure, not merely a fairness complaint, and no threshold adjustment repairs it.

### 2.3 The base-rate arithmetic no institution ran

Take a 500-student cohort. Assume 5% undisclosed AI use, and give the detector *better* properties than any documented — 90% sensitivity, 5% false-positive rate.

- True positives: 25 × 0.90 = **22.5**
- False positives: 475 × 0.05 = **23.75**
- Total flags: 46.25. **False discovery rate: 51.4%.**

More than half of accusations are wrong, with a detector far better than reality. Now apply Liang's measured L2 false-positive rate: among 100 honest non-native speakers, **61 false accusations**. Institutions deployed a screening instrument with a majority-false discovery rate against a population defined by immigration status, and did so without publishing the error rate to the students it judged. Detection is deployed across a reported 20,000+ institutions and 250M+ submissions (Sorochkin 2026, preprint). The scale of harm is not a rhetorical flourish; it is arithmetic.

**Position 1: AI-text detection should be abolished as an evidentiary instrument, not merely used "with caution."** "Use it as a signal, not proof" is not a mitigation — a signal with a >50% false discovery rate, concentrated on a protected class, contaminates the human judgement that follows it. There is no procedurally just way to tell a student "an algorithm we cannot explain, with an error rate we will not state, has raised a question about you; defend yourself." Dawson's framing of assessment *security* — designing so that cheating is hard, rather than policing after the fact — is the correct posture (Dawson 2020, *Defending Assessment Security in a Digital World*, doi:10.4324/9780429324178).

### 2.4 What institutions actually did

The literature records the whole predictable arc: detector procurement, panic reversion to invigilated handwritten exams, and then — where thinking occurred — assessment redesign (Xia et al. 2024, *IJETHE*, doi:10.1186/s41239-024-00468-z, a PRISMA-ScR scoping review; Winstone 2026, *AAEHE*, doi:10.1080/02602938.2026.2661365). The most-adopted framework is the "two-lane" design: secured assessments for assurance, open AI-permitted assessments for learning. It has been sharply and correctly criticised as an all-or-none binary that maps badly onto real practice (Curtis et al. 2025, *Higher Education Research & Development*, doi:10.1080/07294360.2025.2476516).

I think the critique lands but the remedy is easy: **assurance is continuous, not binary, and grade weight should be a monotone function of assurance.** Not two lanes — a dial. An unsupervised essay is not banned; it simply cannot carry 40% of a grade, because its forgery margin is zero and it therefore contributes noise plus a systematic advantage to students with better AI access. I return to this in §7.

---

## 3. Process over product: what the trajectory can and cannot license

### 3.1 The evidence base is real but proves a different thing than people think

Writing-process research is mature. Keystroke logging via Inputlog and similar instruments yields pause distributions, revision patterns, burst lengths, and source-integration behaviour (Leijten & Van Waes 2013, *Written Communication*; Almond et al. 2012, ETS RR-12-23). Process features predict essay scores — using boosting and random forests as well as regression (Sinharay et al. 2019, *Applied Measurement in Education*), in L2 assessment contexts (Choi & Deane 2021, *Language Assessment Quarterly*; Chan et al. 2017, *Language Testing in Asia*), and combined with eye tracking (de Smet et al. 2018, *Written Communication*; Chukharev-Hudilainen et al. 2019, *SSLA*).

**But note exactly what is established: process features *predict product quality*.** That is a correlation, useful for research and for feedback (Vandermeulen et al. 2020, *Journal of Writing Research*). It is *not* a validity argument for scoring the process. And the features are unstable across task types — the same writer produces different keystroke signatures on different tasks (Conijn et al. 2019, *Reading and Writing*), which is fatal for any scheme that sets forensic thresholds on process metrics.

### 3.2 Process forensics is detection wearing a lab coat

The newest work does exactly what the arms race demands: deep models over keystroke logs that separate copy-typing from natural composition (Zhang et al. 2026, *Assessing Writing*, doi:10.1016/j.asw.2026.101070; see also Pan et al. 2025, LAK, doi:10.1145/3706468.3706536, on writing analytics plus authorship attribution).

**This is a binary classifier over student behaviour used to make accusations. It inherits the entire pathology of §2.3.** Same base-rate arithmetic. Same likely fairness profile — this time concentrated on students who compose offline and transcribe, who use assistive technology, who share devices, who draft on a phone, whose L1 writing process involves heavy pre-planning. Plus a new cost: pervasive keystroke-level surveillance of every student, which the learning analytics ethics literature has been warning about for a decade with limited effect (Ferguson et al. 2016, *Journal of Learning Analytics*, doi:10.18608/jla.2016.31.2; Prinsloo & Slade 2018, doi:10.4324/9780203731864-6; Francis 2023, doi:10.18608/jla.2023.7975).

And the margin is the most fragile of the four. Simulating a plausible typing trajectory is a *solved engineering problem* — it requires no intelligence at all, only a stochastic replay of an empirical pause distribution. Of the four margin-restoring strategies, **process forensics is the one that will close first.**

**Position 2: process data has real assessment value, but only in a dialogic register, never a forensic one.** The defensible use is to make the trajectory an object the student *curates and defends*, not a trace collected covertly and used against them. This is the move signalled by the shift "from authentic products to authenticated processes" (Tsiligkiris et al. 2026, *AAEHE*, doi:10.1080/02602938.2026.2695376) and operationalised in authorship quizzing, where students answer questions about their own submitted writing — with promising validity and usability evidence (Quesnel et al. 2025, *AJET*, doi:10.14742/ajet.9529).

### 3.3 Version control is strictly better than keystroke logging, and nobody has studied it

Git history has properties keystroke logs lack: it is **authored** (commit messages are claims the student makes about their own reasoning), **discrete and inspectable** (a commit is a defensible unit, not a statistical artifact), **already professional practice** (construct-relevant, not construct-irrelevant surveillance), and **usable as an oral prompt** ("explain the decision in commit 4a3f").

*Flagging clearly: I could locate no controlled validity study of version-control history as assessment evidence — not for reliability, not for fairness, not for its susceptibility to fabricated commit sequences. This is a real and cheap research gap, and given how much institutional weight is about to be placed on process evidence, it is a surprising one.*

### 3.4 The think-aloud caution

Verbal-report methods (Ericsson & Simon's protocol analysis) are the original process assessment, and their limits are well established: reports are reactive (verbalising changes the process) and unreliable for processes that are not verbally mediated. This is a direct caution against the popular "just make them explain their AI use" reflex — an AI-use reflection statement is a self-report about a partly non-verbalisable process, collected under incentive to misreport. It has value as a pedagogical prompt (Falconer 2025, *MSOR Connections*, doi:10.21100/msor.v23i2.1540). It has close to none as evidence.

---

## 4. Oral examination at scale — and why the standard argument for it is wrong

### 4.1 The standard argument

"The viva was the un-cheatable assessment. We abandoned it because examiner time doesn't scale. Live multimodal AI makes examiner time free. Therefore: bring back the viva."

**The premise is wrong, and getting it wrong will produce a generation of bad oral assessments.**

### 4.2 What actually killed the viva was reliability, and its cause was sampling

The traditional viva has poor psychometric properties, and the literature has said so for decades: unreliability, subjectivity, inconsistent question difficulty across candidates, halo effects, and limited content validity (Memon et al. 2010, *Advances in Health Sciences Education*; Somasekhar et al. 2024, *Advances in Physiology Education*; Pearce & Lee 2009, *Journal of Marketing Education*, doi:10.1177/0273475309334050). A PRISMA systematic review screening 2,657 articles and including 17 concluded that validity, reliability and integrity benefits are all *conditional* on the assessment being designed, scaffolded and implemented well (Nallaya et al. 2024, *Issues in Educational Research*).

But the dominant source of unreliability in performance assessment is not examiner subjectivity — it is **content/case specificity**: performance on one task is a weak predictor of performance on another, so generalisable scores require sampling broadly across tasks. This is the central finding of the clinical competence measurement literature (Wass et al. 2001, *The Lancet*, doi:10.1016/S0140-6736(00)04221-5; Wass et al. 2001, *Medical Education*, doi:10.1046/j.1365-2923.2001.00928.x, which estimates the number of long cases required for defensible decisions). The OSCE's advantage over the long case was never that stations are more objective — it is that there are *more of them*.

**Therefore: AI's contribution to oral assessment is not cheap examiners. It is cheap sampling.** This flips the design. The naive implementation — one AI-conducted 30-minute high-stakes viva replacing the final exam — reproduces exactly the psychometric weakness that killed orals, now at scale and with an unappealable machine judge. The correct implementation is **many short, structured, low-stakes orals distributed across a term**, aggregated programmatically (Schuwirth & van der Vleuten 2012, doi:10.1111/j.1365-2923.2011.04098.x). Frequency is the entire point.

Structure is the second lever. Objective structured viva formats measurably outperform traditional ones (Shaikh et al. 2015; Chhaiya et al. 2022, doi:10.5455/njppp.2022.12.01049202227012022; Somasekhar et al. 2024). An LLM examiner is *natively* structurable — the rubric, probe bank, and follow-up policy are all inspectable artifacts. This is an underrated advantage over human examiners, whose criteria are private.

### 4.3 The fairness objection is serious, and the best available evidence is more encouraging than expected

The prior worry: orals advantage the socially confident, the native-accented, the non-anxious, the neurotypical. There is direct evidence of differential experience for English-as-additional-language doctoral candidates (Carter 2012, *AAEHE*) and near-total absence of autistic student voices in viva accessibility research (Sandland & Brown 2023, *JFHE*).

Against that, the strongest empirical datapoint currently available on interactive oral assessment at scale: 722 students across a bioscience course from 2009–2023, comparing cohorts before and after introducing one-on-one interactive oral assessments as the major final assessment. Performance and course grades improved, **and there were no significant differences by gender, international status, or language background.** Anxiety was initially reported but declined with familiarity and did not depress performance. The format was resilient to AI misuse (Davey et al. 2025, *AAEHE*, doi:10.1080/02602938.2025.2502577).

*Caveats I want on the record: single institution, single discipline, cohort comparison across 14 years rather than randomisation, confounded with everything else that changed in that period, and no reported reliability coefficients.* Corroborating evidence is more qualitative: fidelity and authenticity across three programmes with 158 students (Tan et al. 2022, *AAEHE*, doi:10.1080/02602938.2021.2020722), four case studies across computing, education, French literature and aviation (Ward et al. 2024, *IETI*, doi:10.1080/14703297.2023.2251967), and the foundational integrity-plus-employability argument for interactive orals (Sotiriadou et al. 2019, *Studies in Higher Education*, doi:10.1080/03075079.2019.1582015). A 2025 systematic review of 24 studies identifies what makes oral performance improve: structured practice opportunities, timely feedback, and self-reflective strategies (*AAEHE*, "Interventions and Facilitators of Oral Assessment Performance in Higher Education").

**Position 3: the equity case for AI-conducted orals rests on frequency and practice, not on the technology.** Every documented fairness risk of orals — anxiety, unfamiliarity, differential coaching — is a *first-exposure* effect that decays with repetition. What made orals inequitable was that students met one, once, under maximum stakes. An assessment modality students encounter forty times per degree is a modality they are fluent in. This is the strongest argument for AI-conducted orals and it is almost never the argument that is made.

### 4.4 What it would take to do this well

1. **Structured probe policies, published.** The examiner's question-selection policy is a rubric and must be inspectable and auditable — including for demographic invariance in probe difficulty.
2. **Many short events, not one long one.** Content specificity is the binding constraint.
3. **Human appeal path with human re-examination.** No consequential decision on a machine transcript alone.
4. **Explicit accommodation architecture.** Extended response windows, text-input mode, non-real-time variants — and evidence that these preserve the construct rather than altering it.
5. **Accent and dialect robustness testing before deployment**, benchmarked as automated speech scoring systems already are (Evanini et al. 2017, ETS RR-17-18).
6. **Reliability reported.** Generalisability-style decomposition across probes, occasions, and examiner policies. If a programme cannot report this, it is not assessing, it is performing assessment.

Conversation-based assessment has a real research base to build on — ETS's animated-agent conversational assessments for English learners are a decade-old validated line (Lopez et al. 2021, ETS RR-21-03) — but it does not yet contain a validated LLM examiner. *This is currently the largest empirical gap in the entire field.*

---

## 5. Verification-first assessment: where it wins, where it lies

### 5.1 The move

If a student's claim is machine-checkable, cheating becomes *irrelevant* rather than *detected*. A Lean proof either compiles or does not; the checker does not care who wrote it, and neither, in a strong sense, should we — the artifact carries its own warrant. Proof assistants are now in undergraduate mathematics classrooms (Hanna et al. 2024, *ZDM – Mathematics Education*, doi:10.1007/s11858-024-01577-9). Test-based autograders are ubiquitous in programming education (Messer et al. 2024, *ACM TOCE*, systematic review of 121 papers), and some are built on explicit measurement theory rather than heuristics (Conejo et al. 2019, *IEEE TLT*, using CTT and IRT over evidence items).

### 5.2 The generalisation principle

Verification-first works wherever the domain has a **checkable core**: a formal object whose correctness is decidable independent of the checker's beliefs. Ranked by how much of the discipline's value the core captures:

- **Mathematics** — proof assistants. The core is nearly the whole discipline for the proof-production skill (though not for problem-posing, exposition, or taste).
- **Software** — test suites and type systems. The core captures correctness, not design, maintainability, or the choice of what to build.
- **Empirical data analysis** — executable notebooks plus *withheld* data plus preregistered analysis. Strong: the verification target is out-of-sample performance, which cannot be reverse-engineered from the oracle.
- **Engineering design** — simulation against tolerance envelopes. Strong for satisfaction of constraints; silent on whether the constraints were the right ones.
- **Experimental science** — replication of a claimed result. Very strong, very expensive.
- **Language production** — weak. Communicative success is judged, not checked.
- **Interpretation, historiography, ethics, policy, clinical reasoning under ambiguity** — no core. Quality here *is* judgement under underdetermination. Verification is not merely hard; it is category-inappropriate, and attempts to force it produce rubrics that measure conformity.

**The generalisation rule I propose: verification-first is available exactly where the discipline has already agreed to submit to an oracle.** Mathematics agreed centuries ago; software agreed by construction; empirical science agreed via replication. Where the discipline itself has no oracle, assessment cannot manufacture one, and the attempt reduces the construct to whatever the pseudo-oracle happens to measure.

### 5.3 Where verification fails: the oracle becomes the specification

Autograders are known to induce adverse behaviours — trial-and-error submission against hidden oracles rather than reasoning about the program (Chin et al. 2026, *ACM TOCE*; see also Hao et al. 2022, *Computer Science Education*, and Haldeman et al. 2021, *ACM TOCE*, on formative feedback design as mitigation). This is the classical Campbell/Goodhart dynamic, well documented in high-stakes testing as score inflation without corresponding gains in the underlying construct (Koretz 2005, *Teachers College Record*, doi:10.1177/016146810510701405; Koretz 2010, doi:10.1016/B978-0-08-044894-7.00273-6).

**And here AI makes it categorically worse in a way I have not seen stated.** Oracle-gaming is a *search* problem: find a point in the preimage of "pass." Humans search slowly, so an attempt budget of ten was an effective constraint. An LLM agent searches that space orders of magnitude faster. **Under generation, an unbounded-attempt verification task measures available compute and API budget, not competence.** The construct silently becomes wealth.

**Design rule (mine, not from the literature): verification-first assessment must specify an attempt budget, or it is not an assessment.** Corollaries: hidden oracles with disclosed *cardinality* of hidden tests; scoring that does not reward oracle-probing (no partial credit proportional to tests passed unless attempts are capped); and — the strongest form — verification paired with an oral on the verified artifact, so the compiling proof becomes the *ticket* to the assessment rather than the assessment.

*This is reasoning beyond the evidence: I know of no study manipulating attempt budgets under AI assistance and measuring the effect on the validity of autograded scores. It is a clean, cheap, high-value experiment and someone should run it.*

### 5.4 The honest limit

A compiling Lean proof proves the theorem. It does not prove the student understands the theorem. Verification delivers an **absolute product claim and no capability claim whatsoever** — which is precisely the decoupling described in §0. Verification-first is therefore not a replacement for assessment; it is a way of making the product claim free so that assessment resources can be spent entirely on the capability and learning claims. Institutions adopting autograders as a *cost saving* have inverted this: they bank the savings and never spend them on the claims that now go unevidenced.

---

## 6. Adversarial and Socratic grilling: the item was always a frozen interrogation

### 6.1 The concept-inventory insight, restated

The Force Concept Inventory works, and it is worth being precise about *why*. Its power is not in the stems. It is in the **distractors**, which were derived empirically from documented student misconceptions (Hestenes, Wells & Swackhamer 1992, *The Physics Teacher*). The wrong answers carry the diagnostic information — a point made explicitly in analyses of "central distractors" in FCI response data (Scott & Schumayer 2018, *PRPER*) and exploited by the dominant-incorrect-answer method for diagnosing misconceptions (Bani-Salameh 2017, *Physics Education*; Martin-Blas et al. 2010, *EJEE*). Concept-inventory validity claims nevertheless often lack a structured argument that inferences about student thinking are warranted (Jorion et al. 2015, *Journal of Engineering Education*) — the field's own most rigorous self-criticism.

**So: a multiple-choice item is a frozen interrogation.** It is one scripted branch of a diagnostic conversation, with the follow-up questions precomputed into four options. It was frozen because conversation was expensive. That constraint is gone.

### 6.2 What unfreezing changes, measurement-theoretically

Sampling recall estimates θ on a latent continuum. Probing for misconceptions **searches for the boundary of a student's model.** These are different estimation problems, and the second has a better-suited existing apparatus:

- **Cognitive diagnostic models** estimate attribute-mastery profiles rather than a scalar, and were built for exactly this inference (Tatsuoka 1996, *Applied Measurement in Education*, on person-fit indices for misconception-driven response patterns; Sinharay & Almond 2007, *EPM*; Lee & Sawaki 2012, *Asia Pacific Education Review*). CDMs have a known weakness — most applications *retrofit* the model to tests designed for other purposes (Lee & Sawaki 2012; Ma & de la Torre 2020), and it is not always clear they add information over unidimensional IRT.
- **Nested-logit IRT** models misconception choice as a second-stage process, using distractor selection as signal (Yildiz 2017).
- **Diagnostic tree models** combine multidimensional response options with sequential adaptive administration (Davison et al. 2023, *JEBS*).
- **Dynamic assessment** measures *responsiveness to mediation* rather than static accuracy, which is the natural construct for a Socratic exchange, and has a computerised implementation with published validity work (Poehner & Lantolf 2015, *Language Testing*; Shrestha & Coffin 2012, *Assessing Writing*). Its major critique — that consequential validity remains unestablished — is important and unresolved (Tiekstra et al. 2016, *Educational Psychology*).

**The retrofitting problem is exactly the one that disappears.** CDMs underperformed largely because nobody could afford to build assessments *designed* for diagnosis. An adaptive prober selecting each question conditioned on the full response history — not merely on a running θ — can build one on the fly.

### 6.3 Grilling is an intervention, not just a measurement

Eliciting explanations improves understanding (Chi et al. 1994, *Cognitive Science*, doi:10.1207/s15516709cog1803_3), with known boundary conditions (Rittle-Johnson & Loehr 2017, *Psychonomic Bulletin & Review*, doi:10.3758/s13423-016-1079-5). Retrieval practice enhances retention beyond restudy (Roediger & Karpicke 2006, *Psychological Science*, doi:10.1111/j.1467-9280.2006.01693.x). Socratic questioning targets misconceptions directly (Chian & Bridges 2020, doi:10.20533/ijcdse.2042.6364.2020.0515).

Early causal evidence for the machine version exists: a randomised controlled trial of an LLM-driven Socratic questioning system versus instructor-led case-based learning in endodontic education (n = 79, 97.5% completion) found significant within-group improvement in both arms with substantially reduced synchronous faculty time (Liu et al. 2026, *International Endodontic Journal*, doi:10.1111/iej.70222). *Caveats: single site, one clinical specialty, short-term outcomes, no delayed retention measure.*

**Position 4: the formative/summative distinction dissolves at the point where both are conversation.** A well-run adversarial probe simultaneously (a) measures the boundary of the student's model, (b) teaches at that boundary via retrieval and self-explanation, and (c) leaves an inspectable transcript. This is not a compromise between assessment and instruction; it is the recognition that the separation was an artifact of assessment being expensive.

### 6.4 The psychometric bill that comes due

An adaptive LLM interrogation has **no fixed item set**, so internal-consistency reliability (Cronbach's α, KR-20) is undefined for it. Nor is classical parallel-forms equating available. The warrant has to come from somewhere else, and the candidates are:

- **Test–retest with independently sampled probe policies** — administer two independently seeded interrogations and correlate. This directly estimates the generalisability of the *policy*, which is the object we actually deploy.
- **Generalisability-style decomposition** across probes, occasions, examiner-policy seeds, and domains.
- **Convergent validity** against a secured, conventional criterion during a transition period.

*I am not aware of an established psychometrics for adaptive LLM interrogation. Naming this as the field's central open measurement problem is, I believe, the most useful thing this section can do.* Until it is solved, adversarial grilling should be used formatively and as a component of a programmatic decision, not as a standalone high-stakes instrument.

---

## 7. Psychometrics under generation: infinite items, finite calibration

### 7.1 The one unambiguous win

Item exposure and pool compromise are the chronic security failure of computerised adaptive testing (see the item-exposure control literature, e.g. doi:10.12738/estp.2015.1.2593; Gianopulos 2025, *Journal of Computerized Adaptive Testing*, doi:10.7333/2502-1201054). Automatic item generation was proposed as an exposure remedy long before LLMs (Terteryan 2014, *Computer Technology and Application*). Generation genuinely solves item theft: a stolen item is worthless if no one else will ever see it. Bank this win; it is real.

### 7.2 The item bank was never valuable because items were scarce

**It was valuable because *calibration* was scarce.** An item's parameters are estimated from examinee responses. Generation makes item *text* free; it does nothing to make examinee responses free. So the binding constraint moves from item authoring to item exposure to a calibration sample.

**An infinite bank of uncalibrated items has no measurement properties at all.** This is the sentence institutions rolling out LLM quiz generators need on the wall.

### 7.3 What the AIG literature actually established, and its unresolved assumption

Pre-LLM AIG is a serious 15-year programme, mostly in medical education. Items generated from cognitive models were rated by blinded expert panels as comparable in quality to traditionally authored items, including for application-of-knowledge (Pugh et al. 2020, *RPTEL*, doi:10.1186/s41039-020-00134-8; Gierl & Lai 2012, *Medical Education*, doi:10.1111/j.1365-2923.2012.04289.x; Gierl et al. 2013, *Medical Education*, doi:10.1111/medu.12202; Leslie & Gierl 2023, *AJPE*, doi:10.1016/j.ajpe.2023.100081). Integration with IRT and CAT has been demonstrated end-to-end (Harrison et al. 2017, *Scientific Reports*, doi:10.1038/s41598-017-03586-z).

But the load-bearing assumption is **isomorphicity**: that sibling items generated from one item model share parameters. It is an assumption, not a finding, and sibling difficulty does vary. The mitigations in the literature are (a) calibrate at the *model* level and absorb the extra variance, or (b) predict parameters from item features — the "linguistic signal in item text" programme (Yaneva et al. 2023, doi:10.4324/9781003278658-14; Siller 2020; Aryadoust 2019). LLM-era work is early and mostly quality-screening rather than calibration (Hoffman 2025, doi:10.35542/osf.io/ts5vg_v1, preprint; Zhang et al. 2026, *Proceedings of the Psychometric Society*; Dizon & Tang 2026, *Language Education & Assessment*, doi:10.29140/lea.2026.104152, comparing ChatGPT-generated and expert-developed L2 reading items; Firoozi & Gierl 2025 on banking strategies for generated items).

### 7.4 Three claims about psychometrics under generation

**(a) Stop calibrating items. Calibrate generators.** If item text comes from a stochastic policy conditioned on a specification, then the psychometric object is the *distribution* of items that policy induces, not any individual item. The right model treats item parameters as draws from a family distribution — random-item / crossed random-effects IRT is the existing apparatus. The claim to test is that generator-level parameters are stable enough to support inference even though item-level ones are not.

**(b) Every operational system currently understates measurement error.** Conventional CAT scoring treats calibrated item parameters as *known*. With generated items they are not known — they are draws. The standard error of θ must include item-sampling variance, and no shipping system I am aware of does this. **Prediction: reported reliabilities for LLM-generated adaptive quizzes are systematically optimistic, and the gap widens as item novelty increases.** *This is a derivation, not an empirical finding, and it is directly testable: administer two independently generated forms from the same generator and compare observed score correlation against the reliability the system claims.*

**(c) Fairness must move to the generator, and there is a new failure mode.** Differential item functioning analysis assumes a fixed item administered to multiple groups. If every student receives distinct items, item-level DIF is undefined; what must be demonstrated is **generator invariance** — that the generation policy produces equivalent difficulty distributions across subgroups. Worse, personalised generation, the flagship selling point, conditions item content on student context. A generator that draws contexts from a student's interests or locale can produce **personalisation-induced DIF**: construct-irrelevant difficulty variation correlated with demographics, arising *by design*, invisible to every existing fairness procedure, and defended as a feature. Automated essay scoring has already shown that generative scoring carries measurable accuracy-and-fairness trade-offs (Huang et al. 2026, *Assessing Writing*, doi:10.1016/j.asw.2026.101047); the generation side has had no comparable scrutiny. *Flagging: personalisation-induced DIF is my construction. I found no study of it. I think it is the most serious unexamined fairness risk in AI-driven assessment.*

### 7.5 Equating

With per-student items, equating in the classical sense is gone. Its replacement is model-based linking: a common generator plus anchor items plus hierarchical parameter structure. Practically this means **the anchor set becomes the entire basis of comparability across students and years** — and anchor items are exposed by construction. Generation therefore does not eliminate item security; it *concentrates* it into a small, extremely valuable anchor pool. That pool is now the single point of failure for the whole measurement system, and it will be attacked.

---

## 8. Does assessment still serve learning, or only credentialing?

### 8.1 The two functions were always in tension, and AI has separated them cleanly

Assessment does two incompatible jobs. **Formative:** generate information that changes what the learner does next (Black & Wiliam, *Phi Delta Kappan*, doi:10.1177/003172171009200119; Boud 2000, *Studies in Continuing Education*, doi:10.1080/713695728, on sustainable assessment; Tai et al. 2018, *Higher Education*, doi:10.1007/s10734-017-0220-3, on evaluative judgement; Boud & Molloy 2013, doi:10.1080/02602938.2012.691462, on feedback design). **Credentialing:** emit a costly signal to third parties who cannot observe the learner (the signalling tradition after Spence; see Page 2010, doi:10.1016/B978-0-08-044894-7.01214-8).

Note that a signal works *only* if it is costly to fake. **That is the forgery margin, restated in economics.** The two literatures have been describing the same quantity from opposite ends for fifty years without noticing.

### 8.2 The asymmetric verdict

**The formative function is in the best shape it has ever been.** Retrieval practice, self-explanation, and Socratic probing all now cost approximately nothing and can be delivered continuously (§6). Assessment-as-learning becomes the default rather than the aspiration. This is a genuine, large win and it is being drowned out by integrity panic.

**The credentialing function is in serious trouble**, and the trouble is not fixable by better task design. Its currency was the costly signal; the cost went to zero for every unsupervised artifact. There are only two honest responses: migrate credentialing to the expensive modalities (supervised, live, verified, aggregated), which makes credentialing *scarcer and more concentrated*; or accept that the credential now certifies something weaker and say so out loud.

### 8.3 Position 5: stop grading unsupervised artifacts

Not "redesign homework so AI can't do it." **Remove its grade weight.**

The argument is decision-theoretic, not moral. A grade is a composite. An unsupervised component with a forgery margin near zero contributes (i) noise, and (ii) systematic bias toward students with better AI access, prompting skill, and time. Including it *lowers* both the reliability and the fairness of the composite. Its inclusion is therefore not a compromise between rigour and workload; it is a measurement error that also happens to be regressive.

Two objections deserve real answers.

**Objection A: "The grade is the only thing making students do the work."** True, and it is the strongest objection. Grades on homework are doing hidden work as compliance enforcement. Remove them and unsupervised practice collapses — unless practice is *instrumentally rational*, i.e. unless the secured checkpoints are frequent enough that arriving unprepared is immediately and repeatedly costly. **Hence the design consequence: secured checkpoints must be frequent, not merely high-stakes.** This is the real reason cheap AI-conducted orals matter. Not because they replace the viva — because they make the checkpoint *weekly*.

**Objection B: "This is the two-lane binary you criticised in §2.4."** No. Curtis et al. (2025) are right that an all-or-none split is insupportable. My claim is continuous: **grade weight should be a monotone function of assurance.** An unsupervised AI-permitted essay can be required, can be rich, can be the centre of the course's intellectual life, and can carry 0–5% of the grade while functioning as the *substrate* for a secured oral that carries 30%. The essay is not policed. It is the thing you are examined on.

### 8.4 Why this matters more than integrity: the Bastani result

In a field experiment with nearly a thousand high-school mathematics students, access to a standard ChatGPT-style tutor improved performance on practice problems by 48% (127% for a pedagogically guardrailed variant). When access was removed, students who had used the unguarded tool performed **17% worse than students who never had access at all**. The guardrailed variant eliminated the harm. Students used the unguarded model as a "crutch" (Bastani et al. 2025, *PNAS*, doi:10.1073/pnas.2422633122; correction doi:10.1073/pnas.2518204122).

This is the finding that should reorganise the field's priorities. **The threat generative AI poses to education is not that students will submit work they did not do. It is that they will do work from which they learn nothing, and the grading system will be unable to tell the difference — and will in fact reward it.** Cheating is a distribution-of-credit problem. This is a human-capital-destruction problem, and it operates on students who are not cheating at all.

It also reassigns assessment's job. **If learning happens in practice, and practice is now AI-saturated, then assessment's primary function is to create the incentive to practise in the guardrailed mode.** Assessment becomes an instrument of practice design. That is a more interesting and more consequential job than sorting, and it is one that only a *frequent, secured, diagnostic* assessment system can perform — which is precisely the system §4 and §6 describe.

### 8.5 Choosing which unfairness to accept

Every margin-restoring strategy has a distributional cost, and pretending otherwise is the field's characteristic dishonesty.

| Strategy | Who it disadvantages |
|---|---|
| Live orals | The socially anxious, the newly-arrived, some autistic and speech-disabled students, those in poor-connectivity settings |
| Process telemetry | Shared-device users, offline drafters, assistive-technology users, the privacy-vulnerable |
| Verification-first | Students without compute, API budget, or reliable machines |
| Frequent secured checkpoints | Caregivers, part-time workers, chronically ill and disabled students who need temporal flexibility |
| Detection | Non-native English writers, neurodivergent writers, formal-genre writers — **with no appeal, no stated error rate, and an accusation attached** |

The first four are *legible and accommodatable*: you can see who is disadvantaged, and the accommodation is a design problem with known solutions. Detection's unfairness is invisible, accusatory, concentrated on a protected characteristic, and epistemically unappealable. **That is the ranking that should drive institutional policy, and it is the argument for abolition rather than caution.**

---

## 9. What I think is actually true

1. **The artifact was never the evidence.** It was a cheap proxy for an inference, secured by a cost asymmetry that has now vanished. The four bundled claims — product, process, capability, learning — need four instruments.
2. **Detection is dead, and it died correctly.** It is bounded in theory, broken in practice, and its errors are a conventionality meter pointed at second-language writers. The base-rate arithmetic makes a majority of accusations false at plausible parameters. Abolish it.
3. **Process forensics is detection with better branding.** The dialogic use of process evidence — as something students curate and defend — is sound. The surveillance use inherits every pathology of §2 and adds new ones. Version control is the best available process substrate and has never been validated.
4. **AI does not make examiners cheap; it makes sampling cheap.** That is why one AI-run viva is a mistake and forty short structured orals are a transformation. Oral assessment's historical unreliability was a sampling problem, and sampling is exactly what got cheap.
5. **Verification-first is real where the discipline has already accepted an oracle, and it silently measures compute unless attempts are bounded.** Pair verification with an oral and the compiling proof becomes the ticket, not the grade.
6. **The multiple-choice item was a frozen interrogation.** Unfreezing it moves the target construct from θ to a mastery/misconception profile, revives cognitive diagnostic modelling by removing the retrofitting problem, and leaves us with no reliability theory for the resulting instrument. That gap is the field's central open measurement problem.
7. **Under generation, calibrate generators, not items; expect reported reliabilities to be optimistic; and watch for personalisation-induced DIF**, which is invisible to every existing fairness procedure and is being shipped as a feature.
8. **Assessment still serves learning — better than ever. It serves credentialing much worse, and cannot be repaired into serving it well at scale.** The right response is to shrink the credentialing footprint to a small number of well-secured, frequent, diagnostic events, and to stop attaching grades to artifacts whose provenance is unknowable.
9. **The real emergency is not cheating.** It is that unguarded AI in practice degrades unassisted capability by measurable amounts (Bastani et al. 2025) while producing artifacts that look like learning. An assessment system that cannot distinguish these is not merely insecure. It is actively selecting for the students who learned least.

---

## Appendix: flagged reasoning beyond the evidence

Marked so a reader can separate synthesis from claim:

- **The forgery-margin framework** (§1) — my construction. Individual components (assessment security, signalling costliness, contract-cheating price points) are documented; the unification is not.
- **"The detector is a conventionality meter"** (§2.2) — my interpretation of Liang et al.'s perplexity finding. The numbers are theirs; the construct-validity argument is mine.
- **Base-rate arithmetic** (§2.3) — my calculation from published operating characteristics.
- **"Process forensics is detection wearing a lab coat"** (§3.2) — an argument by structural analogy. No study has yet measured the false-positive profile of keystroke-based AI-use classifiers by student subgroup. **That study is the single most urgent piece of empirical work implied by this section.**
- **Version control as assessment evidence** (§3.3) — no validity studies located. Genuine gap.
- **"AI makes sampling cheap, not examiners cheap"** (§4.2) — my inference from the content-specificity literature; not stated this way in the oral assessment literature.
- **Attempt budgets in verification** (§5.3) — my design rule. Untested; directly testable.
- **Test–retest with independently seeded probe policies** as the reliability warrant for adaptive interrogation (§6.4) — proposed, not established.
- **Generator calibration, understated standard errors, and personalisation-induced DIF** (§7.4) — derivations from random-item IRT plus the structure of LLM generation. The first is a known technical apparatus applied to a new object; the second and third are predictions I have not seen tested.
- **The Davey et al. (2025) fairness result** is the strongest evidence I found for oral assessment equity and is a single-institution, non-randomised cohort comparison across 14 years. I have leaned on it and want that weakness visible.
