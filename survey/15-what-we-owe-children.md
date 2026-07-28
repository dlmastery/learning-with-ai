---
title: "What We Owe Children — the legal floor as a design specification"
section: safety
status: draft
date: 2026-07-28
source_report: research/raw/F8-safety-privacy-children.md
---

# What We Owe Children

**Corrected 2026-07-28, and the correction is time-sensitive.** An earlier draft of
this section said the EU AI Act's Annex III education obligations begin to apply on
2 August 2026. They do not. **Regulation (EU) 2026/1744** — the Digital Omnibus on
AI, done at Strasbourg 8 July 2026, published as OJ L 2026/1744 on 24 July, in force
**27 July 2026** — replaced Article 113's third paragraph point (c). Verified against
the EUR-Lex primary text:

> *"…it is appropriate that the date of application of Sections 1, 2 and 3 of Chapter
> III is set to **2 December 2027** for AI systems classified as high-risk pursuant to
> Article 6(2) and Annex III, and to **2 August 2028** for AI systems classified as
> high-risk"* pursuant to Article 6(1).

Note what did **not** move. Article 113's first paragraph is unamended and Chapter IV
is not carved out, so **Article 50 — transparency, chatbot disclosure, synthetic-content
marking — still applies from 2 August 2026.** For a conversational tutor that is the
live deadline, and it is days away, not eighteen months.

Two sources that a reasonable person would check both give the wrong answer today:
`artificialintelligenceact.eu` is still stamped "last updated 1 August 2024," and the
Commission's own Digital Omnibus page still describes only the proposal. This is
exactly the case our editorial standard exists for — we published an unverified date,
flagged it as unverified, and corrected it against the primary text within a day.

The deferral changes the *deadline*, not the *design*. Read the Act and you will find
that the regulator has already written most of the architecture document for an AI
tutor — with more precision, and more courage, than the field has managed for
itself.

The legal floor is not an obstacle course laid across a good product. It is a set
of load-bearing constraints that coincide, almost line for line, with what the
evidence in the rest of this survey independently says a tutor should do: keep
the learner's record local and deletable, refuse to infer what the child *is*,
put a named human at the end of every consequential path, and never ship a
classifier whose errors land on the children it claims to serve.

---

## 1. The clause that ends the compliance argument

Annex III, point 3(b) makes high-risk any AI system "intended to be used to
evaluate learning outcomes, including when those outcomes are used to steer the
learning process." The operative verb is *evaluate*; the "including when" clause
extends the trigger rather than narrowing it. On the face of the text there is
no formative-assessment exemption, no it's-only-a-suggestion exemption, and no
the-teacher-is-still-in-the-loop exemption.

Article 6(3) offers a derogation for systems that perform a narrow procedural
task, improve a completed human activity, detect deviations from prior
decision-making, or prepare an assessment. Every adaptive-tutoring roadmap that
plans to argue its way out of high-risk classification plans to argue one of
those four. Then comes the sentence that closes it. A system

> "shall always be considered to be high-risk where the AI system performs
> profiling of natural persons."

GDPR Art. 4(4) defines profiling as automated processing to evaluate personal
aspects, in particular to analyse or predict performance, interests, reliability
or behaviour. **A learner model — a persistent per-child representation of
mastery, misconception, pace, and next-best-action — is profiling under that
definition, so no product that keeps one can self-exempt via Article 6(3).** The
escape hatch is closed by the exact artefact that makes the product worth
building. And Article 6(4) means self-exemption is not silent: a provider
claiming the derogation must document the assessment before market and register
the system anyway.

Two secondary readings are open rather than settled. Annex III 3(b) lacks the
institutional limiter that 3(c) and 3(d) carry, which on plain text pulls
direct-to-consumer tutors into scope; no authoritative construction was found.
And the application date itself needs re-verification — the best available
timeline source is stamped 1 August 2024, EUR-Lex was unreachable during the
research pass that produced this paragraph — **it was reached on 2026-07-28 and the
delay is real; see the correction at the head of this section. The paragraph below is
retained as written, and superseded.** The stale reasoning ran:
research (HTTP 202, empty body), and a simplification package proposing deferral
has been publicly discussed. ~~Do not plan on a delay.~~ **Superseded — the delay
was enacted by Reg. (EU) 2026/1744 on 27 July 2026. Annex III now applies from
2 December 2027; Article 50 still applies from 2 August 2026.** Check Article 113 against
EUR-Lex before making a compliance decision.**

The practical consequence for a builder is not defensive. The conformity
artefacts — risk management, data governance, logging, human oversight, and a
Fundamental Rights Impact Assessment under Article 27 for public deployers — are
procurement assets. A state school buying an adaptive tutor has a legal duty to
produce a FRIA. Ship an honest pre-populated template, including a candid list of
the groups your system underserves, and you have handed the customer the hardest
part of their own compliance. Don't, and the school will find those groups
without your help.

---

## 2. The prohibition that clears the field

Article 5(1)(f) prohibits — outright, not as high-risk, applicable since
2 February 2025 — "AI systems to infer emotions of a natural person in the areas
of workplace and education institutions." Read with Art. 3(39) (emotion
inference *on the basis of biometric data*) and Art. 3(34) (biometric data
includes behavioural characteristics, "such as facial images"), this means:

| Technique | Status |
|---|---|
| Webcam frustration / boredom / engagement detection | **Prohibited** |
| Voice-affect scoring in a spoken session | **Prohibited** (voice is biometric; COPPA agrees, §3) |
| "Sensor-free" affect detection from clickstream and latency | **Grey zone** — turns on whether interaction traces are "behavioural characteristics" under 3(34) |

That third row is the sharpest open legal question in the field — it determines
the legality of a substantial body of published AIED work in the EU, and no
authoritative construction was found. Treat it as prohibited until there is one.

Here is why this is a gift rather than a loss. The design move it forces is
**affect response without affect inference.** A tutor may respond to what the
learner says ("I'm stuck", "this is boring") and to behavioural facts (three
wrong answers, forty seconds idle, a session abandoned mid-problem). What it may
not do is maintain a durable variable named `frustration_level`. Generalised:

> **A learner model may hold what the child has demonstrated. It must not hold
> what the child is.**

Mastery of subtraction with regrouping is demonstrated. Dyscalculia is an
identity claim. Article 5(1)(b) independently prohibits exploiting
"vulnerabilities of a natural person... due to their age, disability," which
attaches directly to any engagement mechanic tuned using an inferred condition.

The architecture that satisfies all of this is **derive-and-discard**. Computing
within a single turn that a learner is probably struggling with phonological
decoding, in order to choose the next scaffold, and then throwing it away, is
teaching. Writing `suspected_dyslexia: 0.72` to a durable record creates health
data under GDPR Art. 9(1), a retained record under 16 CFR 312.10, and an
IDEA-destroyable record under 34 CFR 300.624 simultaneously — with none of the
clinical process, appeal rights, or accuracy guarantees of a diagnosis. Data
minimisation is conventionally a collection rule. For a learner model it is a
*persistence* rule.

---

## 3. Deletion is an architecture, not a policy page

COPPA's 2025 amendments (16 CFR Part 312, full compliance required since 22 April
2026) do two things that matter here. § 312.10 states categorically: **"Personal
information collected online from a child may not be retained indefinitely,"**
with a written retention policy required and published. And § 312.2 now expressly
counts as children's personal information "voiceprints... facial templates... or
faceprints," plus "a photograph, video, or audio file where such file contains a
child's image or voice." **A multimodal tutor collects COPPA-regulated biometrics
by default, on turn one** — not a corner case of the live-video architecture in
the next section but its baseline condition.

IDEA is stricter still. 34 CFR § 300.624: when personally identifiable
information is no longer needed to provide educational services, the agency must
inform parents, and **"The information must be destroyed at the request of the
parents."**

This survey stated the consequence once already, in the section on designing for
the margin, and it is worth restating because it is the most under-appreciated
engineering fact in children's edtech. If a child's interaction history has been
folded into model weights, a shared embedding index, or a cross-learner prior,
**you can delete the row and you cannot delete the influence.** Undeletable
learner state is a compliance failure for precisely the population an adaptive
tutor claims to serve best. The positive form: per-learner state genuinely
deletable, and no cross-learner training without irreversible, pre-storage
de-identification.

A correction to a widely-held belief. The FTC's 2025 final rule **did not**
codify a school-authorisation exception for edtech. After roughly 300 comments
the Commission recorded that it "decided against adopting some proposed changes,
including... changes relating to the requirements applicable to educational
technology companies operating in a school environment." Edtech continues to rely
on non-binding enforcement guidance. Any architecture premised on a codified
school exception is premised on something the Commission explicitly declined to
enact.

---

## 4. inBloom, and the null result inside it

inBloom was a $100 million initiative funded by the Gates Foundation and
Carnegie Corporation, launched publicly in February 2013, closed in April 2014.
Nine states committed, representing over 11 million students. The engineering was
strong; contemporaneous accounts describe better security and more access
controls than the incumbents. Its legacy is over 400 pieces of state-level
student-data-privacy legislation and this sentence from the definitive
post-mortem: "To date, no large-scale educational technology initiative has
succeeded in American K-12 schools."

The objection was never the schema. The mobilising parent letter names storage
location, disclosure recipient, commercial purpose, and category sensitivity.
The teachers' union endorsed the data model and rejected the custody arrangement
in a single sentence: gathering data on students is "a valuable tool," but
sharing 400 categories of student-identifying data with private companies — "how
can we possibly countenance that?" The killing blow was a custody rule in the New
York state budget forbidding the state to share identifiable student data with
any shared-learning-infrastructure provider. Closure came a month later.

**And here is the documented disconfirmation, which deserves its own space
because it is the strongest counter-argument available.** inBloom's own product
lead, quoted in that same post-mortem: *"inBloom did not have a privacy problem,
inBloom did not have a parent problem. InBloom had an advocacy and perception
problem."* The Data & Society authors lean the same way, identifying the root
cause as low public tolerance for risk plus a failure to communicate benefit.
"Trust was one of the most frequently used words in our interviews."

That is a real disconfirmation of the naive custody thesis and it should be held,
not waved away. The rebuttal is narrow: what could not be communicated *was* the
custody arrangement. The answer to "who holds my child's health and discipline
record, and who can they give it to?" was "a third-party non-profit, in a
commercial cloud, disclosing to for-profit app vendors under district
authorisation," and no communications strategy makes that sentence land. The same
report records that answering custody questions with FERPA-compliance language
actively hardened opposition.

The design rule that survives both readings: **if your custody architecture
requires a communications strategy to survive contact with a parent, you have
the wrong custody architecture.** The test is five questions answerable on one
screen, without counsel — where does my child's record live and under whose legal
control; who by name can read it; does it leave for any purpose other than
teaching my child; does my child's data improve your product for other customers;
how do I delete it and what survives deletion. If any answer needs a diagram, it
is not shippable to a public school system.

---

## 5. Abolish the detector

Seven widely-used GPT detectors, evaluated on 91 human-authored TOEFL essays and
88 US 8th-grade essays:

| Corpus | Average false-positive rate |
|---|---|
| US 8th-grade essays (native writers) | **5.19%** |
| TOEFL essays (non-native writers) | **61.22%** |

All seven detectors unanimously flagged 18 of the 91 TOEFL essays; **89 of 91
(97.80%) were flagged by at least one detector.** An ~11.8× disparity, and in
any institution running more than one tool, essentially the entire non-native
population is exposed.

The mechanism is perplexity, and the mechanism is the whole argument. Non-native
essays had significantly lower text perplexity (P = 9.74E-05), confirmed
independently on 1,574 pre-ChatGPT ICLR abstracts where authors in
non-native-English countries wrote lower-perplexity text (P = 0.035). Enriching
the TOEFL essays' word choice dropped the FPR from 61.22% to 11.77%; simplifying
native 8th-grade essays "as if written by a non-native speaker" moved them from
5.19% to 56.65%.

Now name who is *taught* to write with low perplexity, as a documented
accommodation: English learners given sentence frames and paragraph templates;
students with dyslexia or dysgraphia given explicit paragraph schemas to offload
working memory; autistic students given structural templates; and every student
in a high-pressure school where the five-paragraph essay is the writing pedagogy.
**The scaffold is the predictability. Therefore the better a student complies
with their prescribed writing accommodation, the more likely a detector is to
accuse them of cheating.** No threshold setting fixes this, because the
accommodation and the detection signal are the same variable — and the students
most exposed are the least equipped to contest an allegation.

"Use with caution, as one signal among many" is not an available position. With
a 61.22%/5.19% split there is no defensible Bayesian update to perform; "one
signal among many" degrades in practice into "the reason a conversation
started," and for a fifteen-year-old the conversation *is* the punishment. And
the tool fails at its stated job: a one-line self-edit prompt collapsed
detection on generated Common App essays **from 100% to 13%.** It catches the
honest and misses the dishonest.

The regulatory and ethical cases converge. Annex III 3(d) separately classifies
detection of prohibited behaviour during tests as high-risk, with Article 15
accuracy obligations a tool carrying a 61.22% subgroup FPR cannot plausibly
meet. **Conclusion: abolition, not caution. Do not possess the capability,**
because possession guarantees eventual use. The replacement is assessment
redesign — in-class writing, process artefacts, oral defence, version history,
staged drafts.

---

## 6. The component four authorities independently asked for

A tutor that is patient, never tired, non-judgemental and available at 11pm on a
Sunday is *structurally optimised* to receive disclosures a teacher will never
receive. That is not a risk bolted onto the product; it is a consequence of the
product working.

Statutory guidance is unusually specific about what follows. KCSIE 2026 Part One
¶14: staff "should never promise a child that they will not tell anyone about a
report of any form of abuse." ¶15: a victim "should never be given the
impression that they are creating a problem by reporting." ¶56: act "immediately."
¶59: unavailability of the safeguarding lead "should not delay appropriate action
being taken." ¶60: "Staff should not assume a colleague or another professional
will take action."

Each is a product requirement. ¶14 forbids a persona that says or implies *this
is just between us*. ¶15 means a canned "I can't help with that, please talk to a
trusted adult" deflection is a safeguarding failure, not a safe default. ¶59
forbids a weekly review queue. ¶60 forecloses "the school's own systems will
catch it." The APA's June 2025 advisory, AI Act Art. 26(2) human oversight, and
ICO AADC Standard 15 converge on the same missing piece: a named human on the
other end.

The evidence says this is tractable and says exactly where the failure mode is.
Detection is good enough to route: on 540 annotated real hotline transcripts
across 64 models, **F1 = 0.880 for suicidal-ideation detection and 0.907 for risk
assessment** — comparable to trained human operators on plan identification.
Good enough to route, nowhere near good enough to decide. And the dominant
failure is not what people expect: against 2,075 structured mental-health
prompts, hallucinations occurred in 6.5% of responses but **omissions in 13.2%,
concentrated in crisis and suicidal-ideation prompts.** The model rarely says
something harmful in a crisis; it fails to say the necessary thing. **A safety
eval that measures only harmful output will pass a system that silently drops the
escalation.** Omission rate, disaggregated by language and dialect, is the
primary safety KPI.

**Second documented null, and it cuts toward optimism.** An ecological audit of
over 20,000 real conversations found that adversarial benchmarks substantially
overstate real-world failure. A purpose-built mental-health AI with layered
suicide/NSSI safeguards produced enabling or harmful content on 0.4–11.27% of
benchmark prompts against 29.0–54.4% for general-purpose LLMs, and clinician
review of flagged real conversations "identified zero cases of suicide risk that
failed to receive crisis resources."

The wrong inference is that safeguards are unnecessary. The right one is that
**the safeguards worked** — the zero-miss came from layered engineering, not from
a good base model with a careful system prompt, and the same paper's 29–54%
figure shows the alternative. Benchmarks are not deployment evidence in either
direction; ecological audit is the method.

Two further nulls belong on the record. Across three AI-companion communities,
**adults and women anthropomorphised chatbots more than teens and men** — so
child-specific protections cannot rest on "children anthropomorphise more." They
rest on reduced capacity to exit, reduced legal agency, and developmental stakes,
which is a different and sturdier argument. And the widely-cited OpenAI × MIT
dependence result is correlational, heterogeneous, tail-concentrated, and
measured on **adults**. Design for the tail; do not claim the population.

---

## 7. What this section commits us to

- **No emotion inference, ever.** Art. 5(1)(f) is a prohibition, not a risk
  tier. Build affect *response* from stated signals and behavioural facts.
- **Assume high-risk and ship the paperwork as a feature.** A learner model
  forecloses the Art. 6(3) derogation. The FRIA template is a sales asset.
- **Deletable by construction.** No cross-learner training on identifiable
  records; no indefinite retention; per-child state genuinely destroyable. The
  row *and* the influence.
- **Hold what the child demonstrated, never what the child is.** Transient
  derivation is pedagogy; persistence is a dossier.
- **Custody first, data model second.** Five questions, one screen, no diagram.
- **No AI writing detector, in any configuration.** 61.22% vs 5.19%; 100% → 13%
  under one prompt. Abolition, not caution.
- **No product for children without a named human escalation recipient**, a
  published SLA, and omission rate as the primary safety KPI.

What the law forbids here is almost exactly what the evidence says does not work
anyway: inferring fixed traits, retaining what you cannot justify, tuning
engagement to a vulnerability, and shipping a classifier whose errors land on the
children who can least afford them. The floor turns out to be a good place to
build from.
