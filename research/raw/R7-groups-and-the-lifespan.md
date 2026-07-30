---
title: "Groups and the Lifespan — what a group does that a tutor cannot, and the two ages this corpus does not serve"
wave: R
section: R7
date_researched: 2026-07-30
sources_count: 61
status: raw-research
---

# R7 — Groups and the Lifespan

> **What this document is.** Three rows from `Z1-coverage-audit.md` that share a single defect.
> Row 12 (groups), row 13 (very young children) and row 14 (adults returning to study) are all
> absent or weak because the corpus specified a one-to-one tutor for a school-age learner and
> then treated that arrangement as coextensive with learning. Rows 13 and 14 are the two ends of
> an age range. Row 12 is the axis the corpus never had at all.
>
> The commission asked one question above the others: **is the group a delivery constraint that
> AI removes, or a mechanism that AI destroys?** §5 answers it with numbers. The short version is
> that the corpus has been asking a question with a false disjunction in it, and the measured
> literature separates the two things cleanly enough that both halves can be priced.

---

## Retrieval note (2026-07-30)

WebSearch was budget-exhausted session-wide before this report began (`200/200`, per
`process/CLAUDE.md` §5). Every source below was retrieved by `curl` against **Crossref**,
**ERIC** (`api.ies.ed.gov`), **PubMed E-utilities**, **Europe PMC**, **Semantic Scholar**,
**OpenAlex**, **Unpaywall**, **OpenAIRE**, and the **arXiv API**, plus `WebFetch` on known URLs
and `pdftotext` on open PDFs.

Four retrievals failed and are reported as failures, never as absence: Elsevier
(`sciencedirect.com`) returns 403 to every request; the AAP (`publications.aap.org`,
`pediatrics.aappublications.org`) returns 403 including to its own Unpaywall-listed free PDF;
the EEF toolkit is behind Cloudflare; and `telearn.hal.science` returns an Anubis challenge.
Each is named at the point where it bites.

**Evidence labels** are the project standard, plus `OBSERVED — absence` for a gap established by
a stated query, which is never treated as proof of non-existence, and `[X]` for a census run
this session.

---

## 0. The findings, stated first

**1. Cooperative learning's achievement effect is conditional, the condition is individual
accountability, and the condition is almost never met.** Slavin's review of 99 studies of at
least four weeks in real classrooms splits cleanly: of the 64 studies whose group reward was
computed from the sum of members' individual learning, 50 (78%) found significant positive
achievement effects and **none found negative effects**, median effect size **+0.32**. Studies
that instead rewarded a single group product, or gave no group reward, had a median effect size
of **+0.07**. Twenty years later, an observational study of 49 German classrooms found that
group goals and individual accountability were present in **17% of observed lessons**, and that
**7% of teachers** implemented the five canonical elements. The headline number is the ceiling of
a condition satisfied about one lesson in six.

**2. The group's distinctive cognitive contribution is not throughput. It is disagreement.** The
cleanest result in the literature is Smith et al. (2009) in *Science*: peer discussion of a
concept question raises performance on a second, isomorphic question answered individually,
*"even when none of the students in a discussion group originally knows the correct answer."*
Against that, Marion & Thorley's meta-analysis of 64 studies establishes collaborative
inhibition as robust: a group recalls **less** than the pooled recall of its members working
alone, and yet **later individual retrieval is improved** by having collaborated. Groups are bad
at producing an answer and good at leaving something behind.

**3. The contingency exception to the video deficit is much weaker than this project would like
it to be, and chasing it down properly reverses the design conclusion.** Roseberry et al.'s
famous Skype result is `n = 36` across three conditions. Troseth's own lab then ran `n = 132`
with four conditions and found **no learning from video in either the responsive or the
unresponsive condition**. Strouse et al. (`n = 88`) found contingency raised engagement and only
*parental co-viewing* raised learning. Tsuji et al. concluded verbatim that *"contingency is not
sufficient."* Strouse & Samson's meta-analysis of 122 effect sizes found **no moderation by live
versus prerecorded video**. The better-evidenced moderator is the adult in the room.

**4. Andragogy has been tested and it did not survive.** Rachal's review of the experimental
literature found 18 studies comparing andragogical with pedagogical instruction; of the 16
measuring achievement, **10 found no significant difference and 2 favoured the traditional
group**. What survived was not learning: application of material, and attendance.

**5. The corporate training industry measures learning 234 times for every 26 times it measures
a result.** Those are the `k`s in Arthur et al.'s meta-analysis, and they are the finding. The
adult segment has the most money, the least time, and the only unambiguous transfer criterion in
this entire corpus — a job — and it does not use it.

---

# PART 1 — GROUPS

## 1.1 Two founding literatures, and who owns them

The cooperative-learning evidence base descends from two American research programmes that both
sell training in the method they meta-analyse. This is stated first because the corpus's own
standard forbids manufactured independence, and these two lines are not independent of their
own conclusions.

**The Johnson and Johnson tradition.** Johnson, Johnson, Nelson & Skon (1981), *Psychological
Bulletin*, meta-analysed 122 studies of cooperative, competitive and individualistic goal
structures and reported that cooperation outperformed both alternatives on achievement and
productivity (`MEASURED-META`, ERIC EJ254134). The tradition's best-scoped modern instalment is
Roseth, Johnson & Johnson (2008), also *Psychological Bulletin*: **148 independent studies, over
eight decades, more than 17,000 early adolescents, 11 countries and 4 multinational samples**,
finding higher achievement and more positive peer relationships under cooperative goal
structures (`MEASURED-META`, `10.1037/0033-2909.134.2.223`, abstract verbatim via Europe PMC).
The Roseth paper is a serious piece of work and its peer-relationship finding is the part of
this literature least contested by anyone.

The most-cited number in the tradition, however, is not in either paper. Johnson, Johnson &
Stanne (2000), *Cooperative Learning Methods: A Meta-Analysis*, is the source usually given for
per-method effect sizes. `[X]` **An ERIC title search returns zero records for it**, and it
circulates as a University of Minnesota Cooperative Learning Center document. The authors
operate the Cooperative Learning Institute and publish through Interaction Book Company. This is
not an accusation of bad faith; it is a statement that the field's most quoted per-method table
has never been through peer review and could not be retrieved this session. `OBSERVED — absence`.

**The Slavin tradition.** Slavin's reviews evaluate Student Teams-Achievement Divisions, Team
Accelerated Instruction and Cooperative Integrated Reading and Composition, which are methods he
designed and which were disseminated through the Success for All Foundation. His conclusions are
sharper than the Johnsons' and, as §1.2 shows, more useful. The adjacency should be held in mind
in both directions: an author who developed a method has an interest in its success, and also
knows better than anyone which version of it was actually delivered.

**The independent checks are thinner than the field's confidence.** Two exist and both are
deflationary:

- **Colliver, Feltovich & Verhulst (2003)**, *Teaching and Learning in Medicine*, re-examined the
  primary studies underlying Springer, Stanne & Donovan's (1999) *RER* meta-analysis and
  concluded that *"the meta-analysis' call for more widespread implementation of small group
  learning is not supported"* (ERIC EJ664775; the paper itself is closed and Unpaywall reports
  no OA copy, so the critique's internal argument could not be read this session).
- **Kyndt, Raes, Lismont, Timmers, Cascallar & Dochy (2013)**, *Educational Research Review*, is
  the one deliberately independent replication attempt, and its inclusion rule is the strictest
  in the literature: **65 articles, published 1995 onwards, in primary, secondary or tertiary
  education, conducted in real-life classrooms** (abstract retrieved verbatim from the University
  of Antwerp institutional repository record `irua:107136`, since Crossref, OpenAlex, Semantic
  Scholar and ERIC all carry the title without an abstract). It reports positive effects on
  achievement and attitudes and finds study domain, age level and culture to be significant
  moderators. **Its pooled magnitudes could not be retrieved.** The article is closed access,
  Unpaywall reports `is_oa: false` with zero OA locations, ScienceDirect returns 403, and the
  repository's own full text is intranet-only. `MEASURED-META`, magnitude **untraceable this
  session**.

## 1.2 The condition that carries the effect

Slavin (2014), *Anales de Psicología* 30(3), 785–791 — open access, PDF retrieved and text-extracted
this session — restates the numbers from his 1995 review with the inclusion criterion that
matters:

> *"A review of 99 studies of cooperative learning in elementary and secondary schools that
> involved durations of at least four weeks compared achievement gains in cooperative learning
> and control groups. Of sixty-four studies of cooperative learning methods that provided group
> rewards based on the sum of group members' individual learning, fifty (78%) found significantly
> positive effects on achievement, and none found negative effects (Slavin, 1995). The median
> effect size for the studies from which effect sizes could be computed was +.32… In contrast,
> studies of methods that used group goals based on a single group product or provided no group
> rewards found few positive effects, with a median effect size of only +.07."*

`MEASURED-META` (a vote-count and median-ES review, not a random-effects pooling; no CI is
reported and none can be). The estimand is achievement gain over a control class taught the same
content conventionally, in real elementary and secondary classrooms, over at least four weeks.

Slavin's mechanism claim in the same paper is the operative sentence for anyone building a
system: *"if group rewards are given based on a single group product (for example, the team
completes one worksheet or solves one problem), there is little incentive for group members to
explain concepts to one another, and one or two group members may do all the work."* The
free-rider problem and the achievement effect are the same variable observed from two sides.

`INFERENCE`: **+0.32 versus +0.07 is not a fact about groups. It is a fact about incentive
design, measured on groups.** Which is a considerably more transferable finding, because
incentive design is a thing software can do and seating is not.

## 1.3 What actually happens in classrooms

**Adl-Amini, Völlinger & Eckart (2024)**, *European Journal of Psychology of Education*, ran a
mixed-methods study across **49 German classrooms** with survey, structured teacher interviews
and rated classroom observation:

> *"Results show that the implementation quality of CL lessons was rather low. Only 7% of the
> observed teachers implemented the basic elements. Even group goals and individual
> accountability, the two most important elements of CL, were implemented in only 17% of the
> lessons observed."*

`OBSERVED` (ERIC EJ1439225). One country, one sample, no claim to representativeness. But it is
the only measurement of implementation fidelity at classroom scale I could locate, and it points
the same way as Slavin's own warning about the single group product.

`INFERENCE`: the corpus should stop treating "the classroom" as delivering the +0.32. In the
modal classroom the delivered condition is the one worth +0.07. That materially changes the
counterfactual against which a one-to-one AI tutor is being judged.

## 1.4 Active learning is not the same construct, and the corpus should stop conflating them

**Freeman et al. (2014)**, *PNAS* `10.1073/pnas.1319030111`, is the number everyone cites:
**225 studies**; examination and concept-inventory performance **+0.47 SD** under active learning
(`n = 158` studies); **odds ratio 1.95** for failing under traditional lecturing (`n = 67`
studies); *"active learning appears effective across all class sizes — although the greatest
effects are in small (n ≤ 50) classes"*; *"Trim and fill analyses and fail-safe n calculations
suggest that the results are not due to publication bias"* (`MEASURED-META`, abstract verbatim
via Europe PMC). **Hake (1998)**, *AJP* `10.1119/1.18809`, is the ancestor: 62 introductory
physics courses, `N = 6542`, average normalised gain **0.23 ± 0.04** for 14 traditional courses
versus **0.48 ± 0.14** for 48 interactive-engagement courses (`OBSERVED` — a survey of courses,
not randomised).

Neither is a measurement of *groups*. The active-learning contrast is "anything other than
continuous lecture" against "continuous lecture," and it includes clicker questions answered
alone, worked-example study, and in-class problem sets. Freeman's own conclusion is about the
control condition: the results *"raise questions about the continued use of traditional lecturing
as a control in research studies."* A system that replaces lecture with anything responsive
inherits most of this literature. It tells you nothing about whether the other students matter.

## 1.5 Peer instruction — the mechanism result the AI question turns on

**Crouch & Mazur (2001)**, *AJP* `10.1119/1.1374249`, report ten years of Peer Instruction in
introductory physics with *"increased student mastery of both conceptual reasoning and
quantitative problem solving"* (`OBSERVED` — a decade of single-institution course data with
sequential improvements confounded with the intervention, as the paper itself describes:
pre-class reading responses, a research-based textbook and cooperative discussion sections were
all added over the period).

The mechanism was isolated eight years later. **Smith, Wood, Adams, Wieman, Knight, Guild & Su
(2009)**, *Science* `10.1126/science.1165919`, in an undergraduate genetics course:

> *"When students answer an in-class conceptual question individually using clickers, discuss it
> with their neighbors, and then revote on the same question, the percentage of correct answers
> typically increases. This outcome could result from gains in understanding during discussion,
> or simply from peer influence of knowledgeable students on their neighbors. To distinguish
> between these alternatives… we followed the above exercise with a second, similar (isomorphic)
> question on the same concept that students answered individually. Our results indicate that
> peer discussion enhances understanding, even when none of the students in a discussion group
> originally knows the correct answer."*

`MEASURED-RCT` in design logic (the isomorphic-question test is the randomisation-free
identification), though the delivery was a single course. This is the sentence the corpus needs.
It rules out transmission. Whatever the group is contributing, it is not a better-informed
member's answer.

## 1.6 CSCL, scripting, and the over-scripting claim

Computer-supported collaborative learning is where the group question has already been asked in
software, and the corpus contains none of it. `[X]`

| Meta-analysis | Base | Contrast | Result |
|---|---|---|---|
| Vogel, Wecker, Kollar & Fischer (2017), *Educ. Psych. Rev.* `10.1007/s10648-016-9361-7` | CSCL scripts | vs **unstructured CSCL** | domain knowledge **d = 0.20**; collaboration skills **d = 0.95** |
| Radkowitsch, Vogel & Fischer (2020), *ijCSCL* `10.1007/s11412-020-09316-4` | 53 studies, **5,616 learners**, K-12 / HE / professional | vs **unguided collaborative learning** | motivation **g = 0.13, n.s.**; domain learning **g = 0.24**; collaboration skills **g = 0.72** |
| Jeong, Hmelo-Silver & Jo (2019), *Educ. Res. Rev.* `10.1016/j.edurev.2019.100284` | 316 outcomes from 143 studies, STEM, 2005–2014 | vs non-CSCL | overall **0.51**, largest on process outcomes |
| Chen, Wang, Kirschner & Tsai (2018), *RER* `10.3102/0034654318791584` | 425 studies, 2000–2016 | collaboration *per se*, within computer-based conditions | knowledge gain **ES = 0.42**; skill acquisition **0.64**; perceptions **0.38** |
| Lou, Abrami & d'Apollonia (2001), *RER* `10.3102/00346543071003449` | 486 findings, 122 studies, **11,317 learners** | small group vs **individual** learning with technology | **individual achievement +0.15**; group task performance +0.31; *"significantly heterogeneous"* |

All `MEASURED-META`; all abstracts retrieved verbatim this session via Crossref or Semantic
Scholar.

Read the last row against the fourth. Chen et al.'s +0.42 for "collaboration per se" and Lou et
al.'s **+0.15** for small-group versus individual are measuring the closest thing the literature
has to the question this project needs answered — *does putting the learner with others beat
putting them alone, holding the technology constant* — and the older, tighter estimate is small
and heterogeneous. `INFERENCE`: the honest summary is that with technology held constant, group
membership buys something around a sixth of a standard deviation on individual achievement, with
a large amount of it explained by moderators the meta-analysis itself could identify.

**Over-scripting.** Dillenbourg (2002) is the canonical statement that scripting collaboration
too tightly destroys the free interaction it was meant to produce. `[X]` I could not retrieve it:
`telearn.hal.science` returns an Anubis anti-bot challenge and no other full text resolved. So
the claim is reported here as widely held and **unverified at source**. What can be reported is
that it was tested. Radkowitsch et al. (2020) frame their meta-analysis around it and conclude:
*"This meta-analysis offers the first counterevidence against the widespread criticism that CSCL
scripts have negative motivational effects."* The motivational cost of scripting is `g = 0.13`
and non-significant. The over-scripting worry, in the form that was measured, did not replicate.

**The asymmetry across all five rows is the real finding.** Scripting collaboration reliably
teaches people **to collaborate** (0.72–0.95) and barely moves **domain knowledge** (0.20–0.24).
If the goal is that a child understands photosynthesis, the CSCL scripting literature is offering
a fifth of a standard deviation. If the goal is that a child can work with another person, it is
offering close to a full one, and there is nothing else in this corpus that offers that at all.

## 1.7 Composition, and the free rider

**Lou, Abrami, Spence, Poulsen, Chambers & d'Apollonia (1996)**, *RER*
`10.3102/00346543066004423`: 145 effect sizes for grouping versus no grouping,
**average achievement ES +0.17**; a second set of 20 effect sizes directly comparing homogeneous
with heterogeneous ability grouping, **+0.12 favouring homogeneous**. Both sets significantly
heterogeneous. `MEASURED-META`.

That +0.12 is inconvenient for the tradition. Heterogeneous grouping is a foundational commitment
of both the Johnson and Slavin programmes, and the meta-analysis that tested it directly found
the opposite sign, weakly.

**The free rider.** Karau & Williams (1993), *JPSP* `10.1037/0022-3514.65.4.681`, "Social loafing:
A meta-analytic review and theoretical integration," is the standard citation. `[X]` **Its pooled
effect size is untraceable this session**: Crossref and Semantic Scholar carry the record without
an abstract, Unpaywall reports no OA copy, PsycNet is inaccessible, and a PubMed search for the
title returns nothing. I searched `"social loafing" meta-analytic review theoretical integration`
on PubMed, Crossref, Semantic Scholar and Europe PMC. The paper exists and is heavily cited; the
number commonly attached to it is not verified here and is therefore not cited.

What *is* verified is the education-side answer. Slavin's +0.07 cell is the free-rider effect
measured as an achievement loss, and his stated remedy — reward computed from the sum of
individual scores — is the same construct as individual accountability. `INFERENCE`: the free
rider is not a social-psychological curiosity to be designed around. It is the default state of
a group, and the entire measured benefit of cooperative learning is the margin by which a
specific incentive structure suppresses it.

## 1.8 The documented null: groups can make content learning worse

**Bacon, D. R. (2005). "The Effect of Group Projects on Content-Related Learning."** *Journal of
Management Education* 29(2). `10.1177/1052562904263729`. Abstract verbatim via Crossref:

> *"Business schools often assign student group projects to enhance student learning of course
> content and to build teamwork skills. However, the characteristics of effective collaborative
> learning tasks, including group goals and individual accountability, are often not found in
> student group projects assigned in business classes. The current research found that content
> learning was actually inhibited by the use of a group project. The results indicate that the
> students who completed a project in groups learned less of the project-related content than did
> students who completed a shortened version of the project individually."*

`MEASURED-RCT` in the paper's own design terms (a controlled comparison within a course);
undergraduate business students; the comparison condition is a *shortened* individual version of
the same project, which is the fair comparison because the group version distributes the work.
Direction: **negative**. Magnitude is not in the abstract and the article is closed
(`sciencedirect`-hosted SAGE content, 403).

This is the null the commission required, and it is a good one because it is not a failure to
find an effect. It found an effect with the wrong sign, in the condition Slavin predicted would
produce it, in the setting where group projects are most heavily used.

**A second, near-null, with a much larger base.** Murphy, Wilkinson, Soter, Hennessey & Alexander
(2009), *Journal of Educational Psychology* `10.1037/a0015576`, meta-analysed classroom
discussion approaches (ERIC EJ861185, abstract verbatim):

> *"Results revealed that several discussion approaches produced strong increases in the amount
> of student talk and concomitant reductions in teacher talk, as well as substantial improvements
> in text comprehension. Few approaches to discussion were effective at increasing students'
> literal or inferential comprehension and critical thinking and reasoning. Effects were moderated
> by study design, the nature of the outcome measure, and student academic ability."*

`MEASURED-META`. Read those two sentences together. Discussion reliably changes **who is
talking**. Whether it changes what anyone understands depends on the approach, and for most
approaches it did not.

## 1.9 Collaborative inhibition — the sharpest fact about groups in the memory literature

**Marion & Thorley (2016)**, *Psychological Bulletin* `10.1037/bul0000071`, PMID 27618544,
abstract verbatim via PubMed. **75 effect sizes from 64 studies.**

> *"Collaborative inhibition was found to be a robust effect. Moreover, it was enhanced when
> remembering took place in larger groups, when uncategorized content items were retrieved, when
> group members followed free-flowing and free-order procedures, and when group members did not
> know one another… In a separate analysis (27 effect sizes), moderating factors of
> postcollaborative memory performance were examined. Generally, collaborative remembering tends
> to benefit later individual retrieval. Moderator analyses suggest that reexposure to study
> material may be partly responsible for this postcollaborative memory enhancement."*

`MEASURED-META`. The estimand is group recall against the **pooled non-redundant recall of the
same number of individuals working alone** (the nominal-group control). The pooled magnitude is
not in the abstract and the article is closed with no OA copy per Unpaywall; the qualitative
result ("robust") and the moderator directions are what is verified.

The two halves of this finding point opposite ways and both matter here. **At the moment of
collaboration the group underperforms its own members.** Retrieval strategies collide. But
**afterwards, the individuals are better than they were**, and the mechanism the authors can
support is re-exposure — hearing the material again, in someone else's order.

`INFERENCE`: this dissolves a confusion the corpus is carrying. A group is not a better thinking
machine. It is a **worse** one at time T. Its value is what each member takes away at T+1, and a
substantial part of that value is a re-encoding effect that has nothing to do with the other
people being people.

## 1.10 Classroom discourse and accountable talk

`[X]` The corpus census found `accountable talk` at 0 hits. The construct is real, it is widely
taught, and its outcome evidence is thin.

Michaels, O'Connor & Resnick (2008), *Studies in Philosophy and Education* (ERIC EJ797081),
state that Accountable Talk practices *"have been shown to result in academic achievement for
diverse populations of students"* and describe fifteen years of research. The measurement layer
underneath that sentence, as far as I can retrieve it, is instruments rather than trials: Wolf,
Crosson & Resnick (2006), CRESST Technical Report 670 (ERIC ED492865), rated **21 reading
comprehension lessons** on Accountable Talk and Academic Rigor rubrics and found *"strong,
positive relationships"* between students' providing knowledge and providing thinking, and rated
academic rigour. `OBSERVED` — correlational, `n = 21` lessons, both variables rated by the same
instrument.

`CRAFT`. Accountable Talk is elite practice with a rubric, and the achievement warrant for it
runs through Murphy et al. (2009), which is the near-null in §1.8.

**A methodological warning about this corner of the literature.** ERIC's argumentation
meta-analyses include Li, Wang & Li (2022), *International Journal of Science Education*
(EJ1358804), reporting **Hedges' g = 10.49, 95% CI [7.27, 13.71]** for scientific-argumentation
instruction on conceptual change. A ten-standard-deviation effect is not a finding; it is an
arithmetic error or a variance-estimation failure. Adjacent entries report `g = 0.927` (Koçoğlu &
Kanadlı 2024, 72 quantitative studies) and `g ≈ 0.60` (Zhou 2024, 46 studies, 5,415 students),
which are plausible. The corpus should not import pooled effect sizes from this sub-literature
without opening the paper.

## 1.11 Socially shared regulation of learning

`[X]` 0 hits in the corpus. **Panadero & Järvelä (2015)**, *European Psychologist*
`10.1027/1016-9040/a000226`, abstract verbatim via Crossref:

> *"A total of 17 articles addressing SSRL were identified, 13 of which presented empirical
> evidence… most of the SSRL research has focused on characterizing phenomena through the use of
> mixed methods through qualitative data, mostly video-recorded observation data. Also, SSRL seems
> to contribute to students' performance. Finally, the article discusses the need for the field to
> move forward, exploring the best conditions to promote SSRL, clarifying whether SSRL is always
> the optimal form of collaboration."*

`MEASURED-META` in name only — a narrative review of 13 empirical papers, mostly qualitative.

Since 2015 a small number of controlled studies exist. Zheng, Li & Huang (2017), *Educational
Technology & Society* (EJ1157976): **66 undergraduates randomly assigned** to an SSRL-embedded
collaborative tool or a non-SSRL control, with significant gains in achievement, group
performance and SSRL frequency (`MEASURED-RCT`, small). Li, Liu, Yuan & Shadiev (2022) (EJ1336001):
94 students, 46/48, experimental group outperformed on mid- and post-test in computational
thinking (`MEASURED-RCT`, non-randomised assignment not stated in the abstract). Zheng et al.
(2023) ran knowledge-graph scaffolds across 63 groups / 189 students (EJ1372756).

`OBSERVED — absence`: **there is no meta-analysis of socially shared regulation, and the largest
controlled study I could locate has fewer than 200 participants.** The construct that most
directly describes "a group holding a plan together" — the group analogue of everything `V5`
specifies for an individual — has an evidence base roughly the size of a single well-run trial.
This is the clearest place in row 12 where the answer is *nobody has measured it*.

---

# PART 2 — VERY YOUNG CHILDREN

`[X]` `early childhood` 0 hits, `emergent literacy` 0, `toddler` 0 across 45 reports and 40
sections.

## 2.1 The video deficit

**Strouse & Samson (2021)**, *Child Development* `10.1111/cdev.13429`, abstract verbatim via
Crossref and Semantic Scholar:

> *"An average deficit of about half of a standard deviation was reported across 122 independent
> effect sizes from 59 reports, involving children ages 0–6 years. Moderator analyses suggested
> (a) the deficit decreased with age, (b) object retrieval studies showed larger deficits than
> other domains, and (c) there was no difference between studies using live versus prerecorded
> video. Results are consistent with a multiple-mechanism explanation for the deficit. However,
> the analyses highlighted potential quality and publication bias issues that may have resulted
> in overestimation of the effect."*

`MEASURED-META`. Note both caveats the authors state: the deficit shrinks with age, and their own
analysis suggests it is overestimated.

The founding experiment is **Kuhl, Tsao & Liu (2003)**, *PNAS* `10.1073/pnas.1532872100`,
PMID 12861072, abstract verbatim via PubMed. Nine-month-old American infants received 12
laboratory sessions of Mandarin exposure. Live exposure *"reversed the decline seen in the
English control group."* In Experiment 2, *"exposure to recorded Mandarin, without interpersonal
interaction, had no effect."* `MEASURED-RCT`, `n = 32` per experiment with 21 and 28 completing.
Small, and replicated in spirit many times since.

**DeLoache et al. (2010)**, *Psychological Science* `10.1177/0956797610384145`, is the commercial
test: a month of at-home baby-media DVD exposure in 12–18-month-olds. *"Children who viewed the
DVD did not learn any more words from their monthlong exposure to it than did a control group.
The highest level of learning occurred in a no-video condition in which parents tried to teach
their children the same target words during everyday activities."* `MEASURED-RCT`.

## 2.2 The contingency exception, chased down

The commission asked for this to be chased down properly, on the ground that a responsive AI is
contingent in the way a DVD is not. It does not survive the chase.

**The positive originals.**
- **Roseberry, Hirsh-Pasek & Golinkoff (2014)**, *Child Development* `10.1111/cdev.12166`,
  PMID 24112079. Toddlers **24–30 months, N = 36**, three conditions: live interaction, socially
  contingent video chat, and yoked non-contingent video. *"Results suggest that children only
  learned novel verbs in socially contingent interactions (live interactions and video chat)."*
  `MEASURED-RCT`. **Twelve children per cell.**
- **Myers, LeWitt, Gallo & Maselli (2017)**, *Developmental Science* `10.1111/desc.12430`,
  PMID 27417537. Ages **12–25 months**, real-time FaceTime versus pre-recorded video, six calls
  over two weeks. *"After one week, children in the FaceTime condition (but not the Video
  condition) preferred and recognized their Partner, learned more novel patterns, and **the oldest
  children** learned more novel words."* `MEASURED-RCT`. The word-learning result is restricted to
  the oldest band.

**The negatives, which are larger.**
- **Troseth, Strouse, Verdine & Saylor (2018)**, *Frontiers in Psychology* `10.3389/fpsyg.2018.02195`,
  PMID 30483198, abstract verbatim via PubMed. **One hundred and thirty-two toddlers** at 24 and
  30 months, four conditions crossing responsiveness with medium. *"Children of both ages reliably
  learned the word in the responsive live condition, and older children (30 months) learned in the
  unresponsive live condition. **Neither group learned in the responsive or unresponsive video
  conditions.** The results show that the addition of communicative social cues to the video
  presentation via video chat was not sufficient to support learning in this case."* `MEASURED-RCT`.
  This is Troseth's own lab, which produced the 2006 contingent-video result the exception rests on.
- **Strouse, Troseth, O'Doherty & Saylor (2018)**, *JECP* `10.1016/j.jecp.2017.09.005`, `n = 88`
  30-month-olds, crossing on-screen contingency with parent modelling. *"Both on-screen contingency
  and parent modeling increased children's engagement with the actress during training. However,
  only parent modeling increased children's subsequent word learning."* `MEASURED-RCT`.
- **Tsuji, Fiévét & Cristia (2021)**, *Infant Behavior and Development* `10.1016/j.infbeh.2021.101553`.
  16-month-olds; in-person, video chat, virtual agent. *"Toddlers showed above-chance word learning
  in the in-person group only… These results confirm that in-person interaction leads to best
  learning outcomes even in the absence of rich social cues. They also elucidate that **contingency
  is not sufficient** either."* `MEASURED-RCT`.
- And the meta-analytic moderator: Strouse & Samson found *"no difference between studies using
  live versus prerecorded video."*

**The verdict.** The contingency exception is a small original positive (`n = 36`) with three
larger follow-ups that failed to reproduce it, one of them from the originating lab, plus a
meta-analytic moderator test that found nothing. The moderator that *does* survive is a person in
the room. **Mallawaarachchi et al. (2024)**, *JAMA Pediatrics* `10.1001/jamapediatrics.2024.2620`,
pooled 100 studies and 176,742 participants; among all screen-use contexts examined, **co-use was
the only one positively associated with cognitive outcomes, `r = 0.14, 95% CI [0.03, 0.25]`**,
while programme viewing (`r = −0.16`) and background television (`r = −0.10`) were negative.
`MEASURED-META`, observational.

`INFERENCE`, and it is the design conclusion for row 13: **a responsive AI does not inherit the
contingency exception, because the contingency exception is not well supported. What is supported
is co-viewing.** A product for under-threes that works is a product aimed at the adult holding the
child.

## 2.3 What preschool interventions achieve, and what fades

**Early numeracy.** Clements & Sarama's Building Blocks is the best-evidenced preschool
mathematics curriculum in existence and its own trajectory is the argument.

| Study | Design | Result |
|---|---|---|
| Clements & Sarama (2008), *AERJ* `10.3102/0002831207312908` | 36 classrooms, cluster RCT, 26 weeks | **ES = 0.47** vs an active comparison curriculum; **ES = 1.07** vs no-maths control |
| Clements, Sarama, Spitler, Lange & Wolfe (2011), *JRME* (ERIC EJ918252) | 42 schools, 106 classrooms, **1,375 preschoolers**, cluster RCT | **g = 0.72** at end of pre-K |
| Sarama, Clements, Wolfe & Spitler (2012), *JREE* `10.1080/19345747.2011.627980` | same cohort, one year later | ITT **g = 0.33** (follow-through), **g = 0.22** (non-follow-through) |
| Clements, Sarama, Wolfe & Spitler (2013), *AERJ* `10.3102/0002831212469270` | third year | **g = 0.51** follow-through, **g = 0.28** non-follow-through |

All `MEASURED-RCT` / cluster-randomised. Note the 0.47-versus-1.07 split in the first row: against
an *active* comparison curriculum the effect is less than half what it is against no curriculum.
The corpus's habit of quoting the larger number from a two-armed comparison is exactly the
`Z1` §2.1 failure mode.

And the same programme's own scale-up team reported the opposite: Clements, Sarama, Farran,
Lipsey, Hofer & Bilbrey (2011), SREE (ERIC ED518182): *"with the scale-up project, the authors
saw evidence of curricular effects across outcomes at the end of prekindergarten, but very few
differences at the end of kindergarten, and virtually none at the end of first grade."* Then
**Bailey, Duncan, Watts, Clements & Sarama (2018)**, *American Psychologist* `10.1037/amp0000146`,
with Clements and Sarama as co-authors: *"experimental manipulation of early math skills generates
much smaller effects on later math achievement than the nonexperimental literature has
suggested."* `MEASURED-META` / reanalysis. **This dispute is unresolved inside the programme that
generated the data, and the corpus should carry it that way.**

**And the strongest negative result in the field.** Tennessee's Voluntary Pre-K programme was
oversubscribed, which permitted a lottery. **Lipsey, Farran & Durkin (2018)**, *ECRQ*
`10.1016/j.ecresq.2018.03.005`: **N = 2,990** low-income children randomly assigned to admission
offers or a waiting list. Positive at the end of pre-K; *"During the kindergarten year and
thereafter, the control children caught up with the pre-k participants on those tests and
generally surpassed them."* **Durkin, Lipsey, Farran & Wiesen (2022)**, *Developmental Psychology*
`10.1037/dev0001301`, followed the same randomised sample to sixth grade:

> *"Data through sixth grade from state education records showed that the children randomly
> assigned to attend pre-K had lower state achievement test scores in third through sixth grades
> than control children, with the strongest negative effects in sixth grade. A negative effect was
> also found for disciplinary infractions, attendance, and receipt of special education services."*

`MEASURED-RCT`, `n = 2,990`, six-year follow-up, **negative**. The Head Start Impact Study
(Puma et al. 2012, `n = 4,667` randomly assigned) is milder and points the same way: initial
gains, *"very few impacts found for either cohort in any of the four domains"* by third grade.

## 2.4 Emergent literacy, and the finding that the intervention teaches the adult

**National Early Literacy Panel (2008)** (ERIC ED504224; PDF text-extracted this session).
Shared-reading interventions: largest impact on oral language, **average ES 0.73**, falling to
**0.57** with one quasi-experimental outlier removed; and *"Shared-reading interventions appear to
have no impact on young children's PA skills or their AK"* — alphabet knowledge **ES −0.06,
95% CI [−0.47, 0.35], k = 2**. Code-focused interventions: **average ES 0.82** on phonological
awareness across 51 studies. `MEASURED-META`.

**Mol, Bus, de Jong & Smeets (2008)**, *Early Education and Development* `10.1080/10409280701838603`:
dialogic reading versus typical shared reading, expressive vocabulary **k = 9, n = 322, d = 0.59,
SE 0.08, 95% CI [0.44, 0.75]**; *"the effect size reduced substantially when children were older
(4 to 5 years old) or when they were at risk for language and literacy impairments."*
`MEASURED-META`.

**Dowdall et al. (2020)**, *Child Development* `10.1111/cdev.13225`: 19 RCTs, **N = 2,594**,
expressive language **d = 0.41**, receptive **d = 0.26**, and **caregiver book-sharing competence
d = 1.01**. `MEASURED-META`.

That last row is the shape of the whole literature. The intervention moves the adult by a full
standard deviation and the child by a third of one.

**The null.** **Noble, Sala, Peter, Lingwood, Rowland, Gobet & Pine (2019)**, *Educational
Research Review*, preprint `10.31234/osf.io/cu7bk`:

> *"Our results show that, while there is an effect of shared reading on language development,
> this effect is smaller than reported in previous meta-analyses (ḡ = 0.215, p < .001). They also
> show that this effect is moderated by the type of control group used and is **negligible in
> studies with active control groups (ḡ = 0.021, p = .783)**."*

`MEASURED-META`. And the confirmatory trial: **Noble et al. (2020)**, *JSLHR*
`10.1044/2020_JSLHR-19-00288`, **n = 150** children aged 2;6–3;0 randomised to pause reading,
dialogic reading, or an **active** shared-reading control. *"The findings indicated that the
interventions were effective at changing caregiver reading behaviors. However, the interventions
did not boost children's language skills over and above the effect of an active reading control
condition."* `MEASURED-RCT`, **null**.

`INFERENCE`: what shared-reading interventions reliably buy is that the book gets opened and the
adult asks questions. Against a condition where the book gets opened anyway, they buy `g = 0.02`.

## 2.5 The two constraints

**Screen guidance.** WHO (2019), *Guidelines on physical activity, sedentary behaviour and sleep
for children under 5 years of age*, quoted verbatim from the WHO release accompanying the
guideline: for infants under 1, *"Screen time is not recommended"*; for 1-year-olds, *"sedentary
screen time (such as watching TV or videos, playing computer games) is not recommended"*; for
ages 2 and 3–4, *"sedentary screen time should be no more than 1 hour; less is better."*
`STATUTE`-adjacent (guidance, not law).

The AAP's 2016 policy statement *Media and Young Minds* (`10.1542/peds.2016-2591`) is the source
of the widely-cited **video-chat carve-out** for under-18-months. `[X]` **I could not retrieve its
recommendation text.** `publications.aap.org`, `pediatrics.aappublications.org` (including the
free full PDF that Europe PMC's Unpaywall record lists), `doi.org` redirect and
`healthychildren.org` all returned 403 or 404. The carve-out is confirmed only second-hand, in a
peer-reviewed review — Glick et al. (2022), *WIREs Cognitive Science* `10.1002/wcs.1599`:
*"expert recommendations (e.g., American Academy of Pediatrics Council on Communications and
Media, 2016)… suggest that video chat, unlike other screen media, is acceptable for use by
children under 18 months."* Reported here as second-hand and **not verified at source**. Note
also that AAP issued a successor technical report in 2026 (`10.1542/peds.2025-075321`) which
reframes "screen time" as *"just the tip of the iceberg"*; whether it supersedes the 2016
recommendations was not established.

`INFERENCE` that matters for anyone reading the carve-out as a licence: the AAP's exception is
for **video chat with a family member**, and §2.2 shows the learning evidence for contingent video
does not hold up. The carve-out is a judgment about relationships, not a finding about learning.

**The learner cannot read the interface.** This is the constraint that most obviously favours a
frontier model, and there is one good trial.

**Xu, Aubele, Vigil, Bustamante, Kim & Warschauer (2022)**, *Child Development* `10.1111/cdev.13708`,
PMC9299009 (open access; full text extracted this session). **117 children aged 3–6**
(mean 57.6 months), 2×2 factorial: dialogic versus non-dialogic reading, crossed with
conversational agent versus human partner, random assignment. Dialogic reading raised story
comprehension, with subscale effects **β = 0.53, p < .001** for event memorisation, **β = 0.38,
p < .05** for inference making, **β = 0.34, p < .05** for sequence understanding. And the
comparison the corpus needs: *"the interaction model suggested that dialogic reading with an agent
induced a comparable level of positive effect on children's story comprehension as an adult reader
(β = 0.22, p = .35)."* `MEASURED-RCT`.

Two cautions the paper states itself. The equivalence claim rests on a **non-significant
interaction in `n = 117`**, which is not the same as demonstrated equivalence; and the sample was
*"homogeneous high language proficiency,"* which the authors say *"may have obscured our ability
to uncover the heterogenous effects."*

Set that against Tsuji et al. (2021), where at **16 months** the virtual-agent condition performed
*significantly worse* than in-person. The two results together locate a boundary: somewhere
between two and four years, a responsive agent goes from worse-than-nothing to
indistinguishable-from-an-adult on a bounded conversational task.

## 2.6 Should a frontier AI tutor touch this age group?

**Under three: no, and not as a matter of caution.** The video deficit is `≈0.5 SD` across 122
effect sizes; contingency does not remove it in the three largest tests; a month of commercial
baby media taught zero words in a randomised trial; WHO recommends zero screen time to age two;
and the one intervention family that works — shared book reading — works by `d = 1.01` on the
adult and `g = 0.02` on the child against an active control. There is no gap in that picture for a
child-facing tutor to fill.

**Three to five: yes, in one specific shape.** The shape is: an agent that talks, that the child
answers aloud, on content an adult chose, with the adult present and reading along, on a bounded
task. That is Xu et al.'s design and it is the only positive randomised result in this section
involving a machine. It is not a tutor. It is a dialogic reading partner.

`SPEC`: for this age the system's user is the caregiver and the child is the beneficiary. The
product surface is the thing that gets the adult to open the book and ask the third question. The
measured target is caregiver book-sharing competence, where the effect sizes are large and
reliable, and the child-language effect is accepted as the small downstream consequence it is.

---

# PART 3 — ADULTS RETURNING TO STUDY, AND RESKILLING

`[X]` `andragogy` 0 hits, `adult education` 0, `reskilling` 0.

## 3.1 Andragogy has been tested

Knowles's andragogy is the field's organising framework and rests on assumptions about
self-direction, the role of experience, readiness to learn, orientation to learning and internal
motivation. It was subjected to experimental test, and the tests are not encouraging.

**Rachal, J. R. (1994). "Andragogical and Pedagogical Methods Compared: A Review of the
Experimental Literature."** ERIC ED380566, description verbatim:

> *"Eighteen studies that attempted to do so included 15 dissertations and 3 journal articles…
> Of the 16 studies that examined achievement in terms of either cognitive gain or skill
> performance, **10 found no significant differences between control and experimental groups; 2
> found the control or 'traditional' group performed better.** On the important variable of
> satisfaction with the learning experience, one study found significant differences favoring the
> andragogical group; three found no significant differences… Two other variables showed
> statistically significant differences favoring andragogy: application of the learned material
> and attendance."*

`MEASURED-META` (a vote-count review; no pooling, no effect sizes). Fifteen of eighteen studies
are unpublished dissertations, which cuts both ways: weaker quality control, and less publication
filtering.

**Rachal, J. R. (2002). "Andragogy's Detectives: A Critique of the Present and a Proposal for the
Future."** *Adult Education Quarterly*, ERIC EJ644442: *"Evidence of the efficacy of andragogy is
inconclusive and affected by definitional confusion."* His proposed remedy is a set of seven
operational criteria, beginning with **voluntary participation**. Davenport (1987), ERIC ED283989,
had reached the same place: *"Emerging research results do not appear to support Knowles'
conceptualization of andragogy as a theory or proven method."*

`INFERENCE`: what survives contact with the experimental literature is not a learning mechanism.
It is two behavioural facts — adults who chose to be there apply the material and attend — and
one design constraint, that participation is voluntary and therefore attrition is the binding
risk. That constraint is the one the corpus's `F6` material is already built for. The rest of
andragogy should not be carried into a specification.

## 3.2 The two-sided age effect

The corpus already owns half of this. `J1`'s expertise-reversal law predicts that the adult
learner's prior-knowledge advantage makes guidance *less* useful, not more, and predicts the
asymmetry grows with domain experience. That prediction is a strong one for this population and it
is stated in the corpus without ever having been aimed at adults.

The other half — processing-speed decline, and whether it eats the prior-knowledge advantage — I
did not establish to this corpus's standard within this session, and I will not assert it. See
§6.3.

## 3.3 Corporate training: the industry that does not measure the thing it sells

**Arthur, Bennett, Edens & Bell (2003)**, *Journal of Applied Psychology*
`10.1037/0021-9010.88.2.234`, PMID 12731707, abstract verbatim via PubMed:

> *"Results of the meta-analysis revealed training effectiveness sample-weighted mean ds of 0.60
> (k = 15, N = 936) for reaction criteria, 0.63 (k = 234, N = 15,014) for learning criteria, 0.62
> (k = 122, N = 15,627) for behavioral criteria, and 0.62 (k = 26, N = 1,748) for results
> criteria."*

`MEASURED-META`. Every effect size is between 0.60 and 0.63, which is suspicious-looking until you
read the `k`s, and the `k`s are the finding. **Learning is measured 234 times. Results are measured
26 times, on 1,748 people total.** That is the whole industry's evidence for whether training
changes anything an employer would pay for, and it is one small trial's worth of participants
spread over twenty years of studies.

**Blume, Ford, Baldwin & Huang (2010)**, *Journal of Management* `10.1177/0149206309352880`, 89
studies of transfer predictors, gives the reason to distrust even the 122: *"Other moderators
related to the measurement of transfer also influenced transfer relationships, including
situations in which transfer outcomes were obtained by the same source in the same measurement
context — which **consistently inflated** transfer relationships."* `MEASURED-META`. Most
"behaviour change" measurement is the trainee reporting their own behaviour change to the trainer.

**Taylor, Russ-Eft & Chan (2005)**, *JAP* `10.1037/0021-9010.90.4.692`, PMID 16060787, is the
best-behaved result in the area. 117 studies of behaviour-modelling training: *"BMT effects were
largest for learning outcomes, smaller for job behavior, and smaller still for results outcomes.
Although BMT effects on declarative knowledge decayed over time, training effects on skills and
job behavior remained stable or even increased. …Transfer was greatest when mixed (negative and
positive) models were presented, when practice included trainee-generated scenarios, when trainees
were instructed to set goals, when trainees' superiors were also trained, and when rewards and
sanctions were instituted in trainees' work environments."* `MEASURED-META`.

Read that moderator list. **Four of the five conditions under which training transfers are
conditions outside the training.** Goals, the manager, the incentive structure, and the scenario
coming from the trainee's own work. That is the adult analogue of Slavin's individual
accountability: the effect lives in the surrounding structure, not in the instruction.

**The 10% claim is untraceable.** The assertion that only about 10% of training transfers to the
job is attributed universally to Georgenson (1982) in *Training and Development Journal*. `[X]`
Searched: ERIC by author (`Georgenson` returns one 1984 needs-analysis article, not this one),
ERIC full-text search on the phrase, Crossref bibliographic search on the title *"The problem of
transfer calls for partnership"*, and a Crossref/ERIC search for Fitzpatrick's often-cited
debunking. **None resolved.** The number is reported here as **untraceable** and is not cited as
evidence of anything.

## 3.4 Adult literacy and numeracy: the sobering part

**Scale.** NCES 2019-179, *Adult Literacy in the United States*, from PIAAC (PDF retrieved and
text-extracted this session): *"one in five U.S. adults (21 percent) has difficulty completing
these tasks… This translates into 43.0 million U.S. adults who possess low literacy skills: 26.5
million at level 1 and 8.4 million below level 1, while 8.2 million could not participate."*
`FILING`.

**Evidence.** **Torgerson, Porthouse & Brooks (2005)**, *Journal of Research in Reading*, ERIC
EJ718454, description verbatim:

> *"We included 27 controlled trials (CTs) that evaluated strategies and pedagogies designed to
> increase adult literacy and numeracy: 18 CTs with no effect sizes (incomplete data) and 9 CTs
> with full data… **Three of the nine trials showed a positive effect for the interventions, five
> trials showed no difference and one trial showed a positive effect for the control treatment.**
> …There have been few attempts to expose common adult literacy or numeracy programmes to rigorous
> evaluation and therefore in terms of policy and practice it is difficult to make any
> recommendations as to the type of adult education that should be supported."*

`MEASURED-META`. Twenty-two years of literature, nine usable trials, a third of them positive.

## 3.5 The documented adult null, and a second one

**Brooks, Burton, Cole, Miles, Torgerson & Torgerson (2008). "Randomised Controlled Trial of
Incentives to Improve Attendance at Adult Literacy Classes."** *Oxford Review of Education*, ERIC
EJ810523. Description verbatim:

> *"We used a cluster-randomised design. Twenty-nine adult literacy classes were randomised in two
> groups using minimisation. Intervention group learners received 5 British Pounds (US$10) for
> each class attended. The main outcome was class attendance… In the 28 remaining classes there
> was a **statistically significant reduction of about 1.5 sessions (95% confidence interval (CI)
> 0.28, 2.79; p = 0.019) attended by the intervention group compared with control**, after
> adjusting for cluster size and baseline scores. The difference in reading scores between the
> intervention and control group, conditioned on baseline scores, was **−2.38 (with controls
> scoring higher than the intervention group), but this difference was not statistically
> significant (95% CI −7.40 to 2.57, p = 0.33)."*

`MEASURED-RCT`. Cluster-randomised, 28 classes analysed, the only UK RCT of financial incentives
in adult literacy. The intervention **reduced** attendance. This is the null the commission
required for row 14 and it is better than a null: paying adults to show up made fewer of them show
up, and the reading-score point estimate also ran against the intervention.

**A second, and it is the one most directly about a product.** **Ainsworth, Gilchrist, Grant,
Hewitt, Ford, Petrie, Torgerson & Torgerson (2012)**, *Educational Studies*, ERIC EJ959747: two
RCTs of an online medication-dosage simulation for student nurses' general numeracy. *"The
Intention to Treat (ITT) analysis in both trials revealed a **small negative effect** of Authentic
World on general numeracy, which was statistically significant in one trial. However, compliance
with the intervention was very low in both trials, with **only 24 and 12% of students allocated to
the intervention groups spending more than 15 minutes using the programme.**"* `MEASURED-RCT`.

`INFERENCE`: for adults, dosage is the whole trial. Eighty-eight percent of a motivated,
professionally-obligated adult population did not spend fifteen minutes with software provided free
and aimed at a skill they were assessed on. Any adult-tutoring specification whose efficacy
argument does not begin with an engagement number is not making an argument.

## 3.6 Reskilling: the only unambiguous transfer criterion in this corpus

**Card, Kluve & Weber (2018)**, *Journal of the European Economic Association* `10.1093/jeea/jvx028`
(NBER w21431), summarising *"over 200 recent studies"* of active labour market programmes: average
impacts are small in the short run and larger two to three years after completion, with
*"larger average gains for programs that emphasize human capital accumulation."* `MEASURED-META`.
The exact estimate counts and significance distribution are not in the retrievable abstract; the
IZA working-paper PDF did not extract cleanly. Reported at the level the abstract supports.

**The RCT.** The WIA Gold Standard Evaluation (Fortson, Rotz, Burkander, Mastri, Schochet,
Rosenberg & McConnell, 2017; Mathematica for the U.S. Department of Labor), a national random-
assignment evaluation across 28 randomly selected local workforce investment areas. Thirty-month
findings: intensive staff-assisted services raised earnings by *"$3,300 to $7,100 (7 to 20 percent)
per customer depending on the data source"*; and *"the evidence suggests that **training funded by
the Adult and Dislocated Worker programs does not have positive impacts in the 30 months after
study enrollment**,"* with the report's own caveat that the finding *"is not conclusive"* because
training uptake within the programme was limited. `MEASURED-RCT`.

The two results together are the shape of the adult market. **Help from a person who knows the
system pays. Training, as delivered, did not.** And the reason offered is dosage again — people
did not take the training.

**Reich & Ruipérez-Valiente (2019)**, *Science* `10.1126/science.aav7958`, "The MOOC pivot,"
is the same story in the online segment; the corpus's `F6` already carries MOOC attrition and it
is not re-derived here.

`INFERENCE`: this is the segment where an outcome could genuinely be measured, and the reason is
structural. The transfer criterion is administrative — employment, wages, a credential an employer
accepts — and it is recorded by somebody else, in state unemployment-insurance wage records, which
is how the WIA evaluation measured it. Every other population in this corpus requires the
evaluator to build the outcome measure. This one does not.

---

## 4. Null and negative register

| # | Result | Source | Label |
|---|---|---|---|
| N1 | Group project **reduced** content learning versus a shortened individual version | Bacon (2005), *JME* `10.1177/1052562904263729` | `MEASURED-RCT` |
| N2 | Cooperative learning without individual accountability: median **ES +0.07** | Slavin (2014) summarising Slavin (1995), 99 studies | `MEASURED-META` |
| N3 | *"Few approaches to discussion were effective at increasing students' literal or inferential comprehension and critical thinking"* | Murphy et al. (2009), *JEP* `10.1037/a0015576` | `MEASURED-META` |
| N4 | CSCL scripts on **motivation g = 0.13, n.s.** — the over-scripting worry did not replicate | Radkowitsch et al. (2020), 53 studies, 5,616 learners | `MEASURED-META` |
| N5 | Small-group vs individual learning with technology: **+0.15** on individual achievement, heterogeneous | Lou, Abrami & d'Apollonia (2001), 122 studies | `MEASURED-META` |
| N6 | Homogeneous ability grouping beat heterogeneous, **+0.12** | Lou et al. (1996), 20 direct comparisons | `MEASURED-META` |
| N7 | Collaborating groups recall **less** than the pooled recall of the same individuals alone | Marion & Thorley (2016), 64 studies | `MEASURED-META` |
| N8 | No word learning from responsive **or** unresponsive video, `n = 132` | Troseth et al. (2018) `10.3389/fpsyg.2018.02195` | `MEASURED-RCT` |
| N9 | Contingency raised engagement, only **parent modelling** raised learning, `n = 88` | Strouse et al. (2018) `10.1016/j.jecp.2017.09.005` | `MEASURED-RCT` |
| N10 | A month of commercial baby-media DVD taught **zero** additional words | DeLoache et al. (2010) `10.1177/0956797610384145` | `MEASURED-RCT` |
| N11 | Shared reading vs **active** controls: **ḡ = 0.021, p = .783** | Noble et al. (2019) `10.31234/osf.io/cu7bk`; confirmed by RCT `n = 150` (2020) | `MEASURED-META` + `MEASURED-RCT` |
| N12 | Shared-reading interventions on alphabet knowledge: **ES −0.06 [−0.47, 0.35]** | NELP (2008), k = 2 | `MEASURED-META` |
| N13 | Tennessee pre-K randomised sample scored **lower** through sixth grade | Durkin et al. (2022) `10.1037/dev0001301`, `n = 2,990` | `MEASURED-RCT` |
| N14 | Andragogical vs pedagogical instruction: **10 of 16 no difference, 2 favouring traditional** | Rachal (1994), ERIC ED380566 | `MEASURED-META` |
| N15 | **£5 per class attended reduced attendance** by ~1.5 sessions, p = .019 | Brooks et al. (2008), 28 clusters | `MEASURED-RCT` |
| N16 | Numeracy software: small negative ITT effect; **12–24% used it for >15 minutes** | Ainsworth et al. (2012), two RCTs | `MEASURED-RCT` |
| N17 | WIA-funded training: **no positive earnings impact at 30 months** | WIA Gold Standard Evaluation (2017) | `MEASURED-RCT` |

---

## 5. Delivery constraint, or mechanism? Taking the position

The corpus has treated one-to-one as the ideal and the classroom as a rationing artifact. That
framing contains a false disjunction, and the literature above separates the parts.

**Most of what a classroom does is a rationing artifact, and the numbers say so.** Group size,
seating, simultaneous pacing, the lecture, the shared worksheet, the single group product — these
are consequences of one adult and thirty children, and every one of them costs measured
achievement. The single group product is the +0.07 condition. Ability-heterogeneous grouping,
imposed because a classroom cannot sort continuously, loses 0.12 against homogeneous grouping.
Traditional lecture, which exists because talking to thirty people at once is the only way to talk
to thirty people at once, loses 0.47 SD and carries an odds ratio of 1.95 for failing. **AI removes
all of this and the corpus is right about it.**

**Three things are mechanisms, and they behave differently under substitution.**

**(a) Individual accountability is a mechanism, and AI supplies it better than a classroom does.**
The entire measured achievement effect of cooperative learning is the margin by which reward
computed from every member's individual learning suppresses the free rider: +0.32 against +0.07.
A classroom achieves that condition in 17% of lessons because computing it is administratively
expensive. A system that measures every learner continuously can compute it for free. This is the
one place where the group's mechanism is not destroyed by AI but **strengthened** by it, and it is
the finding this section exists to deliver.

**(b) Explaining and being explained to is a mechanism, and it is partly recoverable.** The corpus
already records the numbers: `g = 0.56` for human learning-by-teaching, `g = 0.43` for peer
tutoring's tutor gain. Marion & Thorley add the mechanism for one part of it: post-collaborative
individual retrieval improves, and the moderator analysis supports **re-exposure** as a partial
cause. Re-exposure in another person's order does not require the other person to be a person. A
system that makes a learner articulate a position, then presents the material back reorganised by
a different logic, is reproducing the part of the effect whose mechanism is understood.

**(c) Being disagreed with by someone who is genuinely uncertain is a mechanism, and AI cannot
supply it.** Smith et al. (2009) is the load-bearing sentence: discussion improved performance
*"even when none of the students in a discussion group originally knows the correct answer."*
Whatever produces that gain requires two agents who have committed to positions, neither of whom
knows, and whose commitment is real. A model that knows the answer and performs uncertainty is not
in that state, and the corpus has already reached this conclusion twice from other directions —
`I1` scores "genuine peers with real stakes" as one of three costs AI does not collapse, and `I2`
finds chavruta's symmetry does not survive substitution. `INFERENCE`, and it is the same inference
arrived at a third time from the measured side.

**How much is (c) worth?** This is where the argument has to be quantitative or it is just a
worry. The upper bound is Slavin's +0.32, and that is the *whole* cooperative-learning effect,
of which (a) individual accountability is by construction the largest part, since removing it
takes the effect to +0.07. Lou et al.'s +0.15 for small-group versus individual learning with
technology held constant is a better estimate of the residual, and it is heterogeneous. Peer
instruction's clean isolation is a within-course gain on isomorphic items, not a semester
outcome.

`INFERENCE`, stated as the position the commission asked for: **the irreducible peer mechanism is
worth on the order of 0.1 to 0.2 SD, it is the only part of the group AI cannot fake, and it is
smaller than the corpus's anxiety about it.** Against that, the delivery constraints AI removes
are worth 0.47 SD on the lecture alone and roughly 0.25 SD on the accountability structure that
classrooms cannot afford to implement.

**But the loss is not zero, and it is concentrated somewhere specific.** Look again at the CSCL
table. Scripted collaboration moves domain knowledge by 0.20–0.24 and **collaboration skills by
0.72–0.95**. Perfect personalisation does not lose much subject matter. It loses the outcome the
group was uniquely good at teaching, which is working with another person, and this corpus has no
other instrument that produces it. That is the real cost of the single-tutor thesis, and the
corpus's existing worry — that a personalised explanation can be discussed with nobody — is
pointing at it from the wrong side. The problem is not that the explanation is unshareable. The
problem is that the learner never practises sharing.

---

## 6. What is now buildable, the experiment, and what I could not find out

### 6.1 Buildable, given the findings above

1. **An individual-accountability layer, which is the highest-value group mechanism and the one AI
   makes cheaper.** `SPEC`. Slavin's condition, implemented literally: any multi-learner activity
   the system runs computes its group outcome from every member's *separately measured*
   individual post-performance, never from a shared artifact. The falsifier is stated in the
   literature already — if a system rewards a single group product, the predicted effect is +0.07.
   This is a fifteen-line scoring rule with a meta-analytic prior attached, and it is the only
   place in this report where the measured group effect and cheap software point the same way.

2. **AI-brokered human pairing, with the AI outside the dyad.** `SPEC`. Since (c) requires two
   genuinely uncertain agents, the system's role is to *find* the second one: match two learners
   whose current model states disagree on the same item, put the item to both, require each to
   commit before seeing the other, and let them talk. `I2` §9.4 already specifies the pairing idea;
   what this report adds is the measured selection rule — Smith et al. show the gain survives when
   *neither* knows, so the matching criterion is disagreement, not complementary expertise.

3. **A caregiver-facing product for ages 3–5, and nothing child-facing under 3.** `SPEC`. §2.6.
   The measured target is caregiver book-sharing competence (`d = 1.01`), and the delivery form
   with the only positive randomised result is a talking dialogic-reading partner used with an
   adult present (Xu et al. 2022, `n = 117`).

4. **An adult product whose first metric is minutes-on-task, published before any efficacy claim.**
   `SPEC`. Ainsworth et al. is the standing warning: 12–24% compliance destroyed two RCTs of a
   product aimed at a professionally-obligated population. `F4`'s reach economics and `F6`'s
   attrition material are the right machinery; what this report adds is that for adults, dosage is
   not a threat to validity, it *is* the finding.

5. **Structural transfer supports for adult workplace learning, taken from Taylor et al.'s
   moderator list.** `SPEC`. Trainee-generated scenarios, explicit goal setting, and the learner's
   manager brought into the loop. Four of the five conditions under which behaviour-modelling
   training transferred are outside the instruction, which means they are the product.

### 6.2 The single highest-value experiment, with power

**Question.** Does the irreducible peer mechanism — commitment plus genuine mutual uncertainty —
carry measured achievement over an AI tutor that supplies everything else?

**Design.** Three arms, randomised at the learner level within classrooms, one term, a single
subject with a validated concept inventory (introductory mechanics is the obvious choice, since
the FCI and its norms already exist and Hake's data give a baseline).

- **A — AI tutor alone.** Full personalisation, individual accountability scoring, no peers.
- **B — AI tutor plus AI "peer" that commits to a possibly-wrong position and defends it.** This
  is `F2`'s specification, tested.
- **C — AI tutor plus brokered human pairing on disagreement items** (§6.1.2).

**Primary outcome.** Delayed concept-inventory score at eight weeks post-instruction, scored
blind. **Secondary.** A collaboration-skill measure, because the CSCL table says that is where the
group's distinctive effect lives and no arm-A system can produce it.

**Power.** The contrast that matters is C − B: whether human uncertainty beats simulated
uncertainty. §5 puts the residual peer mechanism at 0.1–0.2 SD, so the trial must be powered for
the low end. Detecting **d = 0.15** at 80% power, α = 0.05 two-sided, requires **n ≈ 699 per arm**
(2 × (1.96 + 0.84)² / 0.15²), so **≈ 2,100 learners** across three arms. With individual
randomisation inside classrooms, a modest ICC of 0.05 and average cluster size 25 gives a design
effect of 1 + (25 − 1)(0.05) = 2.2 for any classroom-level contamination, pushing the requirement
to **≈ 4,600**. Detecting the more optimistic d = 0.25 needs `n ≈ 252` per arm before the design
effect and **≈ 1,700** after it.

`INFERENCE`: **the honest reading of that arithmetic is that the peer-mechanism question cannot be
answered by anything smaller than a multi-school trial**, and that this is precisely why nobody has
answered it. A 60-learner pilot has 80% power only for `d ≈ 0.51`, which is larger than the entire
cooperative-learning effect. Any study in this space with `n < 500` per arm reporting a null on
peers has not tested the hypothesis.

**Cheaper variant worth running first.** The B-versus-A contrast alone tests whether a simulated
committed peer does anything, and if `F2` is right that authenticity is the binding constraint,
the expected effect is zero — which is a useful, cheap, publishable null and needs the same power.
The genuinely cheap experiment is the **collaboration-skill secondary outcome**, where the CSCL
metas predict `g ≈ 0.7`. At `d = 0.7`, `n ≈ 33` per arm before the design effect. **The
highest-value cheap experiment is not the achievement question at all; it is measuring whether an
AI-mediated group teaches a learner to work with a person.**

### 6.3 What I could not find out

1. **Kyndt et al.'s pooled effect sizes.** The one deliberately independent replication of the
   cooperative-learning literature, with the strictest inclusion rule (65 studies, real classrooms,
   1995 onward), and its magnitudes are behind Elsevier. Unpaywall: `is_oa: false`, zero OA
   locations. ScienceDirect 403. The Antwerp repository copy is intranet-only. **This is the single
   most consequential gap in Part 1.**
2. **Karau & Williams's pooled social-loafing effect.** Untraceable this session across PubMed,
   Crossref, Semantic Scholar, Europe PMC and Unpaywall. Not cited.
3. **The 10%-of-training-transfers figure.** Untraceable. Searches listed in §3.3. Not cited.
4. **Dillenbourg's over-scripting paper at source.** HAL returns an anti-bot challenge. The claim
   is reported as widely held and unverified; the one meta-analysis that tested it found against it.
5. **The AAP 2016 recommendation text**, including the video-chat carve-out, which is confirmed
   only second-hand through a peer-reviewed review. Every AAP host returned 403.
6. **Marion & Thorley's pooled magnitude for collaborative inhibition**, and **Colliver's internal
   argument against Springer et al.** Both closed, no OA copies.
7. **The processing-speed side of §3.2.** I did not establish adult age-related processing-speed
   decline, or its interaction with prior knowledge, to this corpus's citation standard within this
   session, and I have therefore asserted nothing about it. The specific missing object is a study
   that measures whether older adults acquire *new* domain material more slowly than younger adults
   **once prior knowledge is held constant** — which is the only version of the question that
   matters for a tutoring specification, and the version the ageing literature least often runs.
8. **Whether anyone has measured socially shared regulation at scale.** `OBSERVED — absence`: one
   narrative review of 13 mostly-qualitative papers, and controlled studies with `n = 66` and
   `n = 94`. No meta-analysis. The group analogue of `V5`'s entire premise has an evidence base
   smaller than a single adequately powered trial.

---

## 7. References

**Cooperative and collaborative learning**

1. Johnson, D. W., Johnson, R., Nelson, D., & Skon, L. (1981). Effects of cooperative, competitive, and individualistic goal structures on achievement: A meta-analysis. *Psychological Bulletin*, 89(1), 47–62. `10.1037/0033-2909.89.1.47`. ERIC EJ254134. `MEASURED-META`
2. Roseth, C. J., Johnson, D. W., & Johnson, R. T. (2008). Promoting early adolescents' achievement and peer relationships. *Psychological Bulletin*, 134(2), 223–246. `10.1037/0033-2909.134.2.223`. `MEASURED-META`
3. Johnson, D. W., Johnson, R. T., & Stanne, M. E. (2000). *Cooperative Learning Methods: A Meta-Analysis.* University of Minnesota. **Not indexed in ERIC; not retrieved.** `OBSERVED — absence`
4. Slavin, R. E. (1983). When does cooperative learning increase student achievement? *Psychological Bulletin*, 94(3), 429–445. `10.1037/0033-2909.94.3.429`. `MEASURED-META`
5. Slavin, R. E. (1996). Research on cooperative learning and achievement: What we know, what we need to know. *Contemporary Educational Psychology*, 21(1). `10.1006/ceps.1996.0004`. ERIC EJ526831 (with critical commentary by Abrami & Chambers). `MEASURED-META`
6. † Slavin, R. E. (2014). Cooperative learning and academic achievement: Why does groupwork work? *Anales de Psicología*, 30(3), 785–791. `10.6018/analesps.30.3.201201`. Open access; PDF retrieved and extracted this session. `MEASURED-META`
7. † Kyndt, E., Raes, E., Lismont, B., Timmers, F., Cascallar, E., & Dochy, F. (2013). A meta-analysis of the effects of face-to-face cooperative learning. *Educational Research Review*, 10, 133–149. `10.1016/j.edurev.2013.02.002`. Abstract via UAntwerp `irua:107136`; **magnitudes untraceable**. `MEASURED-META`
8. Springer, L., Stanne, M. E., & Donovan, S. S. (1999). Effects of small-group learning on undergraduates in SMET: A meta-analysis. *Review of Educational Research*, 69(1), 21–51. `10.3102/00346543069001021`. 39 studies. `MEASURED-META`
9. Colliver, J. A., Feltovich, P. J., & Verhulst, S. J. (2003). Small group learning in medical education: A second look at the Springer, Stanne, and Donovan meta-analysis. *Teaching and Learning in Medicine*, 15(1). `10.1207/s15328015tlm1501_01`. ERIC EJ664775. `MEASURED-META` (critique)
10. † Adl-Amini, K., Völlinger, V. A., & Eckart, A. (2024). Implementation quality of cooperative learning and teacher beliefs. *European Journal of Psychology of Education*. ERIC EJ1439225. 49 classrooms. `OBSERVED`
11. † Bacon, D. R. (2005). The effect of group projects on content-related learning. *Journal of Management Education*, 29(2). `10.1177/1052562904263729`. `MEASURED-RCT` **(null / negative)**
12. Lou, Y., Abrami, P. C., Spence, J. C., Poulsen, C., Chambers, B., & d'Apollonia, S. (1996). Within-class grouping: A meta-analysis. *RER*, 66(4), 423–458. `10.3102/00346543066004423`. `MEASURED-META`
13. Öztürk, B. (2023). The effect of cooperative learning models on learning outcomes: A second-order meta-analysis. *Educational Policy Analysis and Strategic Research*. ERIC EJ1408689. 23 first-order meta-analyses. `MEASURED-META`
14. Nokes-Malach, T. J., Richey, J. E., & Gadgil, S. (2015). When is it better to learn together? *Educational Psychology Review*, 27. `10.1007/s10648-015-9312-8`. `MEASURED-META` (review)

**Active learning and peer instruction**

15. † Freeman, S., et al. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS*, 111(23). `10.1073/pnas.1319030111`, PMID 24821756. 225 studies. `MEASURED-META`
16. Hake, R. R. (1998). Interactive-engagement versus traditional methods. *American Journal of Physics*, 66(1). `10.1119/1.18809`. `N = 6542`. `OBSERVED`
17. Crouch, C. H., & Mazur, E. (2001). Peer Instruction: Ten years of experience and results. *AJP*, 69(9). `10.1119/1.1374249`. `OBSERVED`
18. † Smith, M. K., Wood, W. B., Adams, W. K., Wieman, C., Knight, J. K., Guild, N., & Su, T. T. (2009). Why peer discussion improves student performance on in-class concept questions. *Science*, 323(5910). `10.1126/science.1165919`. `MEASURED-RCT`
19. Chi, M. T. H., & Wylie, R. (2014). The ICAP framework. *Educational Psychologist*, 49(4). `10.1080/00461520.2014.965823`. `INFERENCE` (framework)

**CSCL**

20. † Vogel, F., Wecker, C., Kollar, I., & Fischer, F. (2017). Socio-cognitive scaffolding with computer-supported collaboration scripts: A meta-analysis. *Educational Psychology Review*, 29. `10.1007/s10648-016-9361-7`. `MEASURED-META`
21. † Radkowitsch, A., Vogel, F., & Fischer, F. (2020). Good for learning, bad for motivation? *ijCSCL*, 15. `10.1007/s11412-020-09316-4`. 53 studies, 5,616 learners. `MEASURED-META`
22. Jeong, H., Hmelo-Silver, C. E., & Jo, K. (2019). Ten years of CSCL: A meta-analysis of CSCL in STEM education 2005–2014. *Educational Research Review*, 28. `10.1016/j.edurev.2019.100284`. `MEASURED-META`
23. Chen, J., Wang, M., Kirschner, P. A., & Tsai, C.-C. (2018). The role of collaboration, computer use, learning environments, and supporting strategies in CSCL: A meta-analysis. *RER*, 88(6). `10.3102/0034654318791584`. 425 studies. `MEASURED-META`
24. Lou, Y., Abrami, P. C., & d'Apollonia, S. (2001). Small group and individual learning with technology: A meta-analysis. *RER*, 71(3). `10.3102/00346543071003449`. 122 studies, 11,317 learners. `MEASURED-META`
25. Janssen, J., & Kirschner, P. A. (2020). Applying collaborative cognitive load theory to CSCL. *ETR&D*, 68. `10.1007/s11423-019-09729-5`. `INFERENCE` (framework)
26. Dillenbourg, P. (2002). Over-scripting CSCL. **Not retrieved** (HAL anti-bot challenge). Reported as unverified.

**Discourse, argumentation, shared regulation**

27. † Murphy, P. K., Wilkinson, I. A. G., Soter, A. O., Hennessey, M. N., & Alexander, J. F. (2009). Examining the effects of classroom discussion on students' comprehension of text: A meta-analysis. *JEP*, 101(3). `10.1037/a0015576`. ERIC EJ861185. `MEASURED-META` **(near-null)**
28. Michaels, S., O'Connor, C., & Resnick, L. B. (2008). Deliberative discourse idealized and realized: Accountable Talk. *Studies in Philosophy and Education*. ERIC EJ797081. `CRAFT`
29. Wolf, M. K., Crosson, A. C., & Resnick, L. B. (2006). Accountable Talk in reading comprehension instruction. CRESST TR 670. ERIC ED492865. 21 lessons. `OBSERVED`
30. Li, X., Wang, W., & Li, Y. (2022). Systematically reviewing the potential of scientific argumentation. *IJSE*. ERIC EJ1358804. **Reports `g = 10.49 [7.27, 13.71]`; cited only as a methodological warning.**
31. Koçoğlu, A., & Kanadlı, S. (2024). Effect of argumentation-based instruction on student achievement. *Asia Pacific Education Review*. ERIC EJ1440274. `g = 0.927 [0.789, 1.064]`. `MEASURED-META`
32. Zhou, D. (2024). "Learn to argue" and "argue to learn." *Interactive Learning Environments*. ERIC EJ1449153. 46 studies, 5,415 students. `MEASURED-META`
33. † Panadero, E., & Järvelä, S. (2015). Socially shared regulation of learning: A review. *European Psychologist*, 20(3). `10.1027/1016-9040/a000226`. 17 articles, 13 empirical. `MEASURED-META` (narrative)
34. Zheng, L., Li, X., & Huang, R. (2017). The effect of socially shared regulation approach on learning performance in CSCL. *ET&S*. ERIC EJ1157976. `n = 66`, randomised. `MEASURED-RCT`
35. Li, J., Liu, J., Yuan, R., & Shadiev, R. (2022). The influence of socially shared regulation on computational thinking performance. *ET&S*. ERIC EJ1336001. `n = 94`. `MEASURED-RCT`
36. Järvelä, S., Järvenoja, H., & Malmberg, J. (2019). Capturing the dynamic and cyclical nature of regulation. *ijCSCL*. ERIC EJ1236539. `INFERENCE` (methods review)

**Collaborative memory**

37. † Marion, S. B., & Thorley, C. (2016). A meta-analytic review of collaborative inhibition and postcollaborative memory. *Psychological Bulletin*, 142(11). `10.1037/bul0000071`, PMID 27618544. 75 ES / 64 studies. `MEASURED-META`
38. Weldon, M. S., & Bellinger, K. D. (1997). Collective memory: Collaborative and individual processes in remembering. *JEP:LMC*, 23(5). `10.1037/0278-7393.23.5.1160`. `MEASURED-RCT`
39. Karau, S. J., & Williams, K. D. (1993). Social loafing: A meta-analytic review and theoretical integration. *JPSP*, 65(4). `10.1037/0022-3514.65.4.681`. **Pooled effect untraceable this session; not cited as evidence.**

**Video deficit and contingency**

40. † Strouse, G. A., & Samson, J. E. (2021). Learning from video: A meta-analysis of the video deficit in children ages 0 to 6 years. *Child Development*, 92(1). `10.1111/cdev.13429`. 122 ES / 59 reports. `MEASURED-META`
41. † Kuhl, P. K., Tsao, F.-M., & Liu, H.-M. (2003). Foreign-language experience in infancy. *PNAS*, 100(15). `10.1073/pnas.1532872100`, PMID 12861072, PMC166444. `MEASURED-RCT`
42. DeLoache, J. S., et al. (2010). Do babies learn from baby media? *Psychological Science*, 21(11). `10.1177/0956797610384145`. `MEASURED-RCT` (null)
43. † Roseberry, S., Hirsh-Pasek, K., & Golinkoff, R. M. (2014). Skype me! *Child Development*, 85(3). `10.1111/cdev.12166`, PMID 24112079. `N = 36`. `MEASURED-RCT`
44. Myers, L. J., LeWitt, R. B., Gallo, R. E., & Maselli, N. M. (2017). Baby FaceTime. *Developmental Science*, 20(4). `10.1111/desc.12430`, PMID 27417537. `MEASURED-RCT`
45. Troseth, G. L., Saylor, M. M., & Archer, A. H. (2006). Young children's use of video as a source of socially relevant information. *Child Development*, 77(3). `10.1111/j.1467-8624.2006.00903.x`. `MEASURED-RCT`
46. † Troseth, G. L., Strouse, G. A., Verdine, B. N., & Saylor, M. M. (2018). Let's chat: On-screen social responsiveness is not sufficient. *Frontiers in Psychology*, 9, 2195. `10.3389/fpsyg.2018.02195`, PMID 30483198. `n = 132`. `MEASURED-RCT` **(non-replication)**
47. † Strouse, G. A., Troseth, G. L., O'Doherty, K. D., & Saylor, M. M. (2018). Co-viewing supports toddlers' word learning. *JECP*, 166. `10.1016/j.jecp.2017.09.005`. `n = 88`. `MEASURED-RCT`
48. Tsuji, S., Fiévét, A. C., & Cristia, A. (2021). Toddler word learning from contingent screens. *Infant Behavior and Development*, 63. `10.1016/j.infbeh.2021.101553`. `MEASURED-RCT`
49. † Mallawaarachchi, S., et al. (2024). Early childhood screen use contexts and cognitive and psychosocial outcomes. *JAMA Pediatrics*, 178(10). `10.1001/jamapediatrics.2024.2620`. 100 studies, 176,742 participants. `MEASURED-META`
50. Glick, A. R., et al. (2022). Implications of video chat use for young children. *WIREs Cognitive Science*, 13(4). `10.1002/wcs.1599`. Cited only as second-hand confirmation of the AAP carve-out.

**Early numeracy, emergent literacy, preschool**

51. Clements, D. H., & Sarama, J. (2008). Experimental evaluation of a research-based preschool mathematics curriculum. *AERJ*, 45(2). `10.3102/0002831207312908`. `MEASURED-RCT`
52. Clements, D. H., Sarama, J., Spitler, M. E., Lange, A. A., & Wolfe, C. B. (2011). *JRME*, 42(2). ERIC EJ918252. 1,375 preschoolers. `MEASURED-RCT`
53. Sarama, J., Clements, D. H., Wolfe, C. B., & Spitler, M. E. (2012). *JREE*, 5(2). `10.1080/19345747.2011.627980`. `MEASURED-RCT`
54. Clements, D. H., Sarama, J., Wolfe, C. B., & Spitler, M. E. (2013). *AERJ*, 50(4). `10.3102/0002831212469270`. `MEASURED-RCT`
55. Clements, D. H., Sarama, J., Farran, D., Lipsey, M., Hofer, K. G., & Bilbrey, C. (2011). SREE. ERIC ED518182. **Contradicts 53–54 on persistence.** `MEASURED-RCT`
56. Bailey, D. H., Duncan, G. J., Watts, T., Clements, D. H., & Sarama, J. (2018). Risky business. *American Psychologist*, 73(1). `10.1037/amp0000146`. `MEASURED-META` / reanalysis
57. † Lipsey, M. W., Farran, D. C., & Durkin, K. (2018). *ECRQ*, 45. `10.1016/j.ecresq.2018.03.005`. `N = 2,990`. `MEASURED-RCT`
58. † Durkin, K., Lipsey, M. W., Farran, D. C., & Wiesen, S. E. (2022). *Developmental Psychology*, 58(3). `10.1037/dev0001301`. **Negative through grade 6.** `MEASURED-RCT`
59. Puma, M., et al. (2012). Third grade follow-up to the Head Start Impact Study. OPRE 2012-45. ERIC ED539263/ED539264. `n = 4,667`. `MEASURED-RCT`
60. † National Early Literacy Panel (2008). *Developing Early Literacy.* ERIC ED504224. `MEASURED-META`
61. Mol, S. E., Bus, A. G., de Jong, M. T., & Smeets, D. J. H. (2008). Added value of dialogic parent–child book readings. *Early Education and Development*, 19(1). `10.1080/10409280701838603`. `k = 9, n = 322, d = 0.59 [0.44, 0.75]`. `MEASURED-META`
62. Dowdall, N., et al. (2020). Shared picture book reading interventions for child language development. *Child Development*, 91(2). `10.1111/cdev.13225`. 19 RCTs, `N = 2,594`. `MEASURED-META`
63. † Noble, C., Sala, G., Peter, M., Lingwood, J., Rowland, C. F., Gobet, F., & Pine, J. (2019). The impact of shared book reading on children's language skills: A meta-analysis. *Educational Research Review*, 28. Preprint `10.31234/osf.io/cu7bk`. **`ḡ = 0.021, p = .783` with active controls.** `MEASURED-META` (null)
64. † Noble, C., et al. (2020). The impact of interactive shared book reading on children's language skills: An RCT. *JSLHR*, 63(6). `10.1044/2020_JSLHR-19-00288`. `n = 150`. `MEASURED-RCT` (null)
65. Griffith, S. F., Hagan, M. B., Heymann, P., Heflin, B. H., & Bagner, D. M. (2020). Apps as learning tools: A systematic review. *Pediatrics*, 145(1). `10.1542/peds.2019-1579`. 35 studies. `MEASURED-META` (narrative)
66. Kearney, M. S., & Levine, P. B. (2019). Early childhood education by television. *AEJ: Applied*, 11(1). `10.1257/app.20170300`. `OBSERVED` (quasi-experiment); point estimates not verified.
67. † Xu, Y., Aubele, J., Vigil, V., Bustamante, A. S., Kim, Y.-S., & Warschauer, M. (2022). Dialogue with a conversational agent promotes children's story comprehension. *Child Development*, 93(2). `10.1111/cdev.13708`, PMC9299009. `n = 117`. `MEASURED-RCT`
68. WHO (2019). *Guidelines on physical activity, sedentary behaviour and sleep for children under 5 years of age.* ISBN 978-92-4-155053-6. Quoted from the WHO release; guideline PDF not retrieved. `STATUTE`-adjacent
69. AAP Council on Communications and Media (2016). Media and young minds. *Pediatrics*, 138(5). `10.1542/peds.2016-2591`. **Recommendation text not retrieved (403 from every AAP host).**

**Adults**

70. † Rachal, J. R. (1994). Andragogical and pedagogical methods compared: A review of the experimental literature. ERIC ED380566. 18 studies. `MEASURED-META` **(null)**
71. Rachal, J. R. (2002). Andragogy's detectives. *Adult Education Quarterly*. ERIC EJ644442. `MEASURED-META` (review)
72. Davenport, J., III (1987). A way out of the andragogy morass. ERIC ED283989. `INFERENCE` (critique)
73. † Arthur, W., Jr., Bennett, W., Jr., Edens, P. S., & Bell, S. T. (2003). Effectiveness of training in organizations. *JAP*, 88(2). `10.1037/0021-9010.88.2.234`, PMID 12731707. `MEASURED-META`
74. † Taylor, P. J., Russ-Eft, D. F., & Chan, D. W. (2005). A meta-analytic review of behavior modeling training. *JAP*, 90(4). `10.1037/0021-9010.90.4.692`, PMID 16060787. 117 studies. `MEASURED-META`
75. Blume, B. D., Ford, J. K., Baldwin, T. T., & Huang, J. L. (2010). Transfer of training: A meta-analytic review. *Journal of Management*, 36(4). `10.1177/0149206309352880`. 89 studies. `MEASURED-META`
76. Georgenson, D. (1982). The problem of transfer calls for partnership. *Training and Development Journal*, 36(10). **Untraceable in ERIC and Crossref; the "10% transfers" figure is not cited.**
77. † Torgerson, C., Porthouse, J., & Brooks, G. (2005). A systematic review of controlled trials evaluating interventions in adult literacy and numeracy. *Journal of Research in Reading*. ERIC EJ718454. 27 CTs, 9 usable. `MEASURED-META`
78. † Brooks, G., Burton, M., Cole, P., Miles, J., Torgerson, C., & Torgerson, D. (2008). RCT of incentives to improve attendance at adult literacy classes. *Oxford Review of Education*. ERIC EJ810523. 28 clusters. `MEASURED-RCT` **(null / backfire)**
79. † Ainsworth, H., et al. (2012). Computer-based instruction for improving student nurses' general numeracy. *Educational Studies*. ERIC EJ959747. Two RCTs. `MEASURED-RCT` **(null / negative)**
80. Card, D., Kluve, J., & Weber, A. (2018). What works? A meta analysis of recent active labor market program evaluations. *JEEA*, 16(3). `10.1093/jeea/jvx028`; NBER w21431. 200+ studies. `MEASURED-META`
81. † Fortson, K., Rotz, D., Burkander, P., Mastri, A., Schochet, P., Rosenberg, L., & McConnell, S. (2017). *Providing Public Workforce Services to Job Seekers: 30-Month Impact Findings on the WIA Adult and Dislocated Worker Programs.* Mathematica for U.S. DOL. 28 local areas. `MEASURED-RCT` **(null on training)**
82. NCES (2019). *Adult Literacy in the United States.* Data Point NCES 2019-179. ERIC ED596118. PIAAC. `FILING`
83. Reich, J., & Ruipérez-Valiente, J. A. (2019). The MOOC pivot. *Science*, 363(6423). `10.1126/science.aav7958`. `OBSERVED`

**Carried from the corpus, not re-derived:** `I1`'s mechanism-survival test and its scoring of
"genuine peers with real stakes"; `I2` §2.6 on chavruta's symmetry under substitution and §9.4 on
AI-brokered human pairing; `F2` §4.1–4.3 on peer instruction and jigsaw as AI roles; the corpus's
standing corrections `g = 0.56` (human learning-by-teaching) and `g = 0.43` (peer tutoring's tutor
gain); `J1`'s expertise-reversal law; `F6` on attrition; `F4` on reach economics; `V5` on supplying
the executive.

† = primary source retrieved verbatim this session.
