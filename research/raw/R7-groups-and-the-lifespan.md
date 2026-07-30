---
title: "Groups and the Lifespan — what a group does that a tutor cannot, and the two ages this corpus does not serve"
wave: R
section: R7
date_researched: 2026-07-30
sources_count: 83
status: raw-research
---

# R7 — Groups and the Lifespan

> **What this document is.** Three rows from `Z1-coverage-audit.md` that share one defect. Row 12
> (groups), row 13 (very young children) and row 14 (adults returning to study) are absent or weak
> because the corpus specified a one-to-one tutor for a school-age learner and then treated that
> arrangement as coextensive with learning. Rows 13 and 14 are the two ends of an age range. Row 12
> is an axis the corpus never had.
>
> The commission asked one question above the others: is the group a delivery constraint that AI
> removes, or a mechanism that AI destroys? §5 answers it with numbers. The short version is that
> the question contains a false disjunction, and the measured literature separates the halves
> cleanly enough to price both.

## Retrieval note (2026-07-30)

WebSearch was budget-exhausted session-wide before this report began (`200/200`, per
`process/CLAUDE.md` §5). Every source was retrieved by `curl` against Crossref, ERIC
(`api.ies.ed.gov`), PubMed E-utilities, Europe PMC, Semantic Scholar, OpenAlex, Unpaywall and
OpenAIRE, plus `WebFetch` on known URLs and `pdftotext` on open PDFs.

Four retrievals failed and are reported as failures, never as absence: Elsevier
(`sciencedirect.com`) returns 403 to everything; the AAP returns 403 even to its own
Unpaywall-listed free PDF; the EEF toolkit sits behind Cloudflare; and `telearn.hal.science`
returns an anti-bot challenge. Each is named where it bites.

Labels are the project standard, plus `OBSERVED — absence` for a gap established by a stated query,
never treated as proof of non-existence, and `[X]` for a census run this session.

---

## 0. The findings, stated first

**1. Cooperative learning's achievement effect is conditional, the condition is individual
accountability, and the condition is almost never met.** Slavin's review of 99 studies of at least
four weeks in real classrooms splits cleanly. Of the 64 whose group reward was computed from the
sum of members' individual learning, 50 (78%) found significant positive effects and none found
negative effects; median effect size **+0.32**. Studies rewarding a single group product, or giving
no group reward, had a median of **+0.07**. An observational study of 49 German classrooms found
group goals and individual accountability present in 17% of lessons, and 7% of teachers
implementing the five canonical elements. The headline number is the ceiling of a condition
satisfied about one lesson in six.

**2. The group's distinctive cognitive contribution is disagreement, not throughput.** Smith et al.
(2009) in *Science*: peer discussion of a concept question raises performance on a second,
isomorphic question answered individually, *"even when none of the students in a discussion group
originally knows the correct answer."* Against that, Marion & Thorley's meta-analysis of 64 studies
establishes collaborative inhibition as robust — a group recalls less than the pooled recall of its
members alone — while later individual retrieval improves. Groups are bad at producing an answer
and good at leaving something behind.

**3. The contingency exception to the video deficit is much weaker than this project would like.**
Roseberry et al.'s Skype result is `n = 36` across three conditions. Troseth's own lab then ran
`n = 132` with four conditions and found no learning from video in either the responsive or the
unresponsive condition. Strouse et al. (`n = 88`) found contingency raised engagement and only
parental co-viewing raised learning. Tsuji et al. concluded verbatim that *"contingency is not
sufficient."* Strouse & Samson's meta-analysis of 122 effect sizes found no moderation by live
versus prerecorded video. The moderator that survives is the adult in the room.

**4. Andragogy was tested and did not survive.** Rachal found 18 experimental comparisons of
andragogical with pedagogical instruction; of the 16 measuring achievement, 10 found no significant
difference and 2 favoured the traditional group. What survived was not learning: application of
material, and attendance.

**5. Corporate training measures learning 234 times for every 26 times it measures a result.**
Those are the `k`s in Arthur et al.'s meta-analysis, and they are the finding. The adult segment
has the most money, the least time, and the only unambiguous transfer criterion in this corpus —
a job — and does not use it.

---

# PART 1 — GROUPS

## 1.1 Two founding literatures, and who owns them

The cooperative-learning base descends from two American programmes that both sell training in the
method they meta-analyse. Stated first, because the corpus forbids manufactured independence.

**Johnson and Johnson.** Johnson, Johnson, Nelson & Skon (1981), *Psychological Bulletin*,
meta-analysed 122 studies of cooperative, competitive and individualistic goal structures, finding
cooperation superior on achievement and productivity (`MEASURED-META`, ERIC EJ254134). The
tradition's best modern instalment is Roseth, Johnson & Johnson (2008), also *Psychological
Bulletin*: 148 independent studies, eight decades, over 17,000 early adolescents, 11 countries
(`MEASURED-META`, `10.1037/0033-2909.134.2.223`, verbatim via Europe PMC). Its peer-relationship
finding is the part of this literature nobody contests.

The tradition's most-cited number is in neither paper. Johnson, Johnson & Stanne (2000),
*Cooperative Learning Methods: A Meta-Analysis*, is the usual source for per-method effect sizes.
`[X]` An ERIC title search returns zero records; it circulates as a University of Minnesota
Cooperative Learning Center document, and the authors run the Cooperative Learning Institute and
publish through Interaction Book Company. This is not an accusation. It is a statement that the
field's most quoted per-method table never went through peer review and could not be retrieved.
`OBSERVED — absence`.

**Slavin.** His reviews evaluate Student Teams-Achievement Divisions, Team Accelerated Instruction
and Cooperative Integrated Reading and Composition, which he designed and which were disseminated
through the Success for All Foundation. The adjacency cuts both ways: an author who built a method
has an interest in its success, and also knows which version was delivered.

**Independent checks are thinner than the field's confidence, and both are deflationary.**
Colliver, Feltovich & Verhulst (2003), *Teaching and Learning in Medicine*, re-examined the primary
studies under Springer, Stanne & Donovan's (1999) *RER* meta-analysis and concluded that *"the
meta-analysis' call for more widespread implementation of small group learning is not supported"*
(ERIC EJ664775; the paper is closed, Unpaywall reports no OA copy, so its internal argument could
not be read). And Kyndt, Raes, Lismont, Timmers, Cascallar & Dochy (2013), *Educational Research
Review*, is the one deliberate replication attempt, with the strictest inclusion rule in the field:
65 articles, 1995 onwards, primary through tertiary, conducted in real-life classrooms (abstract
retrieved from the University of Antwerp repository record `irua:107136`, since Crossref, OpenAlex,
Semantic Scholar and ERIC all carry the title without an abstract). It reports positive effects on
achievement and attitudes, with study domain, age level and culture as significant moderators.
**Its pooled magnitudes could not be retrieved** — closed access, `is_oa: false` with zero OA
locations, ScienceDirect 403, repository full text intranet-only. `MEASURED-META`, magnitude
untraceable this session.

## 1.2 The condition that carries the effect

Slavin (2014), *Anales de Psicología* 30(3), 785–791 — open access, PDF extracted this session —
restates the 1995 numbers with the inclusion criterion that matters:

> *"A review of 99 studies of cooperative learning in elementary and secondary schools that
> involved durations of at least four weeks compared achievement gains in cooperative learning and
> control groups. Of sixty-four studies of cooperative learning methods that provided group rewards
> based on the sum of group members' individual learning, fifty (78%) found significantly positive
> effects on achievement, and none found negative effects (Slavin, 1995). The median effect size
> for the studies from which effect sizes could be computed was +.32… In contrast, studies of
> methods that used group goals based on a single group product or provided no group rewards found
> few positive effects, with a median effect size of only +.07."*

`MEASURED-META` — a vote-count and median-ES review, not a random-effects pooling, so no confidence
interval exists or can. The estimand is achievement gain over a control class taught the same
content conventionally, in real classrooms, over at least four weeks.

Slavin's mechanism claim in the same paper is operative for anyone building a system: *"if group
rewards are given based on a single group product… there is little incentive for group members to
explain concepts to one another, and one or two group members may do all the work."* The free-rider
problem and the achievement effect are one variable seen from two sides.

`INFERENCE`: +0.32 against +0.07 is not a fact about groups. It is a fact about incentive design,
measured on groups — a far more transferable finding, because incentive design is something
software does and seating is not.

## 1.3 What actually happens in classrooms

Adl-Amini, Völlinger & Eckart (2024), *European Journal of Psychology of Education*, ran survey,
structured interviews and rated observation across 49 German classrooms:

> *"Results show that the implementation quality of CL lessons was rather low. Only 7% of the
> observed teachers implemented the basic elements. Even group goals and individual accountability,
> the two most important elements of CL, were implemented in only 17% of the lessons observed."*

`OBSERVED` (ERIC EJ1439225). One country, one sample, no representativeness claim, and the only
classroom-scale fidelity measurement I could locate. It points the same way as Slavin's own warning
about the single group product.

`INFERENCE`: the corpus should stop treating "the classroom" as delivering the +0.32. In the modal
classroom the delivered condition is the +0.07 one. That changes the counterfactual against which
a one-to-one AI tutor is judged.

## 1.4 Active learning is a different construct

Freeman et al. (2014), *PNAS* `10.1073/pnas.1319030111`: 225 studies; examination and
concept-inventory performance **+0.47 SD** under active learning (`n = 158` studies); **odds ratio
1.95** for failing under traditional lecturing (`n = 67` studies); effective across all class sizes
with greatest effects at `n ≤ 50`; *"Trim and fill analyses and fail-safe n calculations suggest
that the results are not due to publication bias"* (`MEASURED-META`, verbatim via Europe PMC).
Hake (1998), *AJP* `10.1119/1.18809`, is the ancestor: 62 introductory physics courses, `N = 6542`,
average normalised gain **0.23 ± 0.04** across 14 traditional courses versus **0.48 ± 0.14** across
48 interactive-engagement courses (`OBSERVED` — a survey of courses, not randomised).

Neither measures groups. The contrast is "anything other than continuous lecture" against
"continuous lecture," and it includes clicker questions answered alone and worked-example study.
Freeman's own conclusion is about the control: the results *"raise questions about the continued
use of traditional lecturing as a control in research studies."* A system that replaces lecture
with anything responsive inherits most of this literature and learns nothing from it about whether
the other students matter.

## 1.5 Peer instruction — the mechanism result the AI question turns on

Crouch & Mazur (2001), *AJP* `10.1119/1.1374249`, report ten years of Peer Instruction with
*"increased student mastery of both conceptual reasoning and quantitative problem solving"*
(`OBSERVED` — single-institution decade data, with pre-class reading responses, a research-based
textbook and cooperative discussion sections all added over the period, as the paper itself
describes).

The mechanism was isolated eight years later. Smith, Wood, Adams, Wieman, Knight, Guild & Su
(2009), *Science* `10.1126/science.1165919`, in undergraduate genetics:

> *"This outcome could result from gains in understanding during discussion, or simply from peer
> influence of knowledgeable students on their neighbors. To distinguish between these
> alternatives… we followed the above exercise with a second, similar (isomorphic) question on the
> same concept that students answered individually. Our results indicate that peer discussion
> enhances understanding, even when none of the students in a discussion group originally knows the
> correct answer."*

`MEASURED-RCT` in design logic — the isomorphic-question test is the identification — delivered in
a single course. This is the sentence the corpus needs, because it rules out transmission. Whatever
the group contributes, it is not a better-informed member's answer.

## 1.6 CSCL and the scripting literature

Computer-supported collaborative learning is where the group question has already been asked in
software. `[X]` The corpus contains none of it.

| Meta-analysis | Base | Contrast | Result |
|---|---|---|---|
| Vogel, Wecker, Kollar & Fischer (2017), `10.1007/s10648-016-9361-7` | CSCL scripts | vs unstructured CSCL | domain knowledge **d = 0.20**; collaboration skills **d = 0.95** |
| Radkowitsch, Vogel & Fischer (2020), `10.1007/s11412-020-09316-4` | 53 studies, 5,616 learners, K-12 / HE / professional | vs unguided collaboration | motivation **g = 0.13, n.s.**; domain **g = 0.24**; collaboration skills **g = 0.72** |
| Jeong, Hmelo-Silver & Jo (2019), `10.1016/j.edurev.2019.100284` | 316 outcomes / 143 studies, STEM, 2005–2014 | vs non-CSCL | overall **0.51**, largest on process outcomes |
| Chen, Wang, Kirschner & Tsai (2018), `10.3102/0034654318791584` | 425 studies, 2000–2016 | collaboration *per se*, within computer-based conditions | knowledge gain **0.42**; skill acquisition **0.64** |
| Lou, Abrami & d'Apollonia (2001), `10.3102/00346543071003449` | 486 findings / 122 studies, 11,317 learners | small group vs **individual**, technology held constant | individual achievement **+0.15**; *"significantly heterogeneous"* |

All `MEASURED-META`, all abstracts verbatim via Crossref or Semantic Scholar.

Read the last row against the fourth. Those two are the closest the literature comes to the
question this project needs — does putting a learner with others beat putting them alone, holding
the technology constant — and the older, tighter estimate is small and heterogeneous.
`INFERENCE`: with technology fixed, group membership buys something near a sixth of a standard
deviation on individual achievement.

**Over-scripting.** Dillenbourg (2002) is the canonical claim that scripting collaboration too
tightly destroys the interaction it was meant to produce. `[X]` I could not retrieve it —
`telearn.hal.science` returns an anti-bot challenge and no other full text resolved — so it is
reported as widely held and unverified at source. What can be reported is that it was tested.
Radkowitsch et al. frame their meta-analysis around it: *"This meta-analysis offers the first
counterevidence against the widespread criticism that CSCL scripts have negative motivational
effects."* The motivational cost is `g = 0.13`, non-significant. In the form that was measured, the
over-scripting worry did not replicate.

**The asymmetry across all five rows is the real finding.** Scripting collaboration reliably
teaches people to collaborate (0.72–0.95) and barely moves domain knowledge (0.20–0.24). If the
goal is that a child understands photosynthesis, this literature offers a fifth of a standard
deviation. If the goal is that a child can work with another person, it offers close to a full one,
and nothing else in this corpus produces that outcome at all.

## 1.7 Composition, and the free rider

Lou, Abrami, Spence, Poulsen, Chambers & d'Apollonia (1996), *RER* `10.3102/00346543066004423`:
145 effect sizes for grouping versus no grouping, average achievement **+0.17**; a second set of
20 effect sizes comparing homogeneous with heterogeneous ability grouping directly, **+0.12
favouring homogeneous**. Both sets significantly heterogeneous. `MEASURED-META`. That +0.12 is
inconvenient: heterogeneous grouping is a foundational commitment of both traditions, and the
meta-analysis that tested it found the opposite sign.

**The free rider.** Karau & Williams (1993), *JPSP* `10.1037/0022-3514.65.4.681`, is the standard
citation. `[X]` Its pooled effect size is untraceable this session: Crossref and Semantic Scholar
carry the record without an abstract, Unpaywall reports no OA copy, PsycNet is inaccessible, and a
PubMed title search returns nothing. I searched `"social loafing" meta-analytic review theoretical
integration` on PubMed, Crossref, Semantic Scholar and Europe PMC. The paper exists and is heavily
cited; the number usually attached to it is not verified here and is therefore not cited.

The education-side answer is verified. Slavin's +0.07 cell is the free-rider effect measured as
achievement loss, and his remedy — reward computed from the sum of individual scores — is
individual accountability under another name. `INFERENCE`: the free rider is the default state of a
group, and the entire measured benefit of cooperative learning is the margin by which one specific
incentive structure suppresses it.

## 1.8 The documented null: groups can make content learning worse

**Bacon, D. R. (2005). "The Effect of Group Projects on Content-Related Learning."** *Journal of
Management Education* 29(2), `10.1177/1052562904263729`. Verbatim via Crossref:

> *"The characteristics of effective collaborative learning tasks, including group goals and
> individual accountability, are often not found in student group projects assigned in business
> classes. The current research found that content learning was actually inhibited by the use of a
> group project. The results indicate that the students who completed a project in groups learned
> less of the project-related content than did students who completed a shortened version of the
> project individually."*

`MEASURED-RCT` in the paper's own design terms; undergraduate business students; the comparison is
a *shortened* individual version, which is the fair contrast because the group version distributes
the work. Direction: negative. Magnitude is not in the abstract and the article is closed (SAGE via
ScienceDirect, 403).

This is the null the commission required, and a good one, because it is not a failure to find an
effect. It found an effect with the wrong sign, in the condition Slavin predicted would produce it,
in the setting where group projects are most heavily used.

A second, near-null, with a much larger base. Murphy, Wilkinson, Soter, Hennessey & Alexander
(2009), *Journal of Educational Psychology* `10.1037/a0015576`, meta-analysed classroom discussion
approaches (ERIC EJ861185, verbatim):

> *"Results revealed that several discussion approaches produced strong increases in the amount of
> student talk and concomitant reductions in teacher talk, as well as substantial improvements in
> text comprehension. Few approaches to discussion were effective at increasing students' literal or
> inferential comprehension and critical thinking and reasoning. Effects were moderated by study
> design, the nature of the outcome measure, and student academic ability."*

`MEASURED-META`. Discussion reliably changes who is talking. Whether it changes what anyone
understands depends on the approach, and for most approaches it did not.

## 1.9 Collaborative inhibition

Marion & Thorley (2016), *Psychological Bulletin* `10.1037/bul0000071`, PMID 27618544, verbatim via
PubMed. 75 effect sizes from 64 studies.

> *"Collaborative inhibition was found to be a robust effect. Moreover, it was enhanced when
> remembering took place in larger groups, when uncategorized content items were retrieved, when
> group members followed free-flowing and free-order procedures, and when group members did not know
> one another… In a separate analysis (27 effect sizes)… collaborative remembering tends to benefit
> later individual retrieval. Moderator analyses suggest that reexposure to study material may be
> partly responsible for this postcollaborative memory enhancement."*

`MEASURED-META`. The estimand is group recall against the pooled non-redundant recall of the same
number of individuals working alone. The pooled magnitude is not in the abstract and the article is
closed with no OA copy; the qualitative result and the moderator directions are what is verified.

The two halves point opposite ways and both matter. At the moment of collaboration the group
underperforms its own members, because retrieval strategies collide. Afterwards the individuals are
better than they were, and the mechanism the authors can support is re-exposure — hearing the
material again, in someone else's order.

`INFERENCE`: a group is not a better thinking machine; it is a worse one at time T, whose value is
what each member takes away at T+1, and a substantial part of that value is a re-encoding effect
that does not require the other people to be people.

## 1.10 Classroom discourse and accountable talk

`[X]` The corpus census found `accountable talk` at 0 hits. The construct is real, widely taught,
and its outcome evidence is thin. Michaels, O'Connor & Resnick (2008), *Studies in Philosophy and
Education* (ERIC EJ797081), state that the practices *"have been shown to result in academic
achievement for diverse populations of students."* The measurement layer underneath is instruments
more than trials: Wolf, Crosson & Resnick (2006), CRESST TR 670 (ERIC ED492865), rated 21 reading
lessons on Accountable Talk and Academic Rigor rubrics and found *"strong, positive relationships"*
between students' providing knowledge and rated rigour — `OBSERVED`, correlational, `n = 21`
lessons, both variables rated by the same instrument. `CRAFT`. The achievement warrant runs through
Murphy et al. (2009), which is the near-null above.

One methodological warning. ERIC's argumentation meta-analyses include Li, Wang & Li (2022),
*IJSE* (EJ1358804), reporting `g = 10.49, 95% CI [7.27, 13.71]`. A ten-standard-deviation effect is
an arithmetic or variance-estimation failure. Adjacent entries report `g = 0.927` (Koçoğlu &
Kanadlı 2024, 72 studies) and `g ≈ 0.60` (Zhou 2024, 46 studies, 5,415 students). The corpus should
not import pooled effect sizes from this sub-literature without opening the paper.

## 1.11 Socially shared regulation of learning

`[X]` 0 hits in the corpus. Panadero & Järvelä (2015), *European Psychologist*
`10.1027/1016-9040/a000226`, verbatim via Crossref:

> *"A total of 17 articles addressing SSRL were identified, 13 of which presented empirical
> evidence… most of the SSRL research has focused on characterizing phenomena through the use of
> mixed methods through qualitative data, mostly video-recorded observation data."*

A narrative review of 13 mostly-qualitative papers. Since then a small controlled literature has
appeared: Zheng, Li & Huang (2017), *ET&S* (EJ1157976), 66 undergraduates randomly assigned to an
SSRL-embedded tool or control, with significant gains in achievement and group performance
(`MEASURED-RCT`); Li, Liu, Yuan & Shadiev (2022) (EJ1336001), 94 students, experimental group
outperforming on mid- and post-test in computational thinking; Zheng et al. (2023) (EJ1372756),
63 groups / 189 students on knowledge-graph scaffolds.

`OBSERVED — absence`: there is no meta-analysis of socially shared regulation, and the largest
controlled study I could locate has fewer than 200 participants. The construct that describes a
group holding a plan together — the group analogue of everything `V5` specifies for an individual —
has an evidence base roughly the size of one well-run trial.

---

# PART 2 — VERY YOUNG CHILDREN

`[X]` `early childhood` 0 hits, `emergent literacy` 0, `toddler` 0.

## 2.1 The video deficit

Strouse & Samson (2021), *Child Development* `10.1111/cdev.13429`, verbatim via Crossref:

> *"An average deficit of about half of a standard deviation was reported across 122 independent
> effect sizes from 59 reports, involving children ages 0–6 years. Moderator analyses suggested (a)
> the deficit decreased with age, (b) object retrieval studies showed larger deficits than other
> domains, and (c) there was no difference between studies using live versus prerecorded video…
> However, the analyses highlighted potential quality and publication bias issues that may have
> resulted in overestimation of the effect."*

`MEASURED-META`, with both authorial caveats retained: the deficit shrinks with age, and the
authors think it is overestimated.

The founding experiment is Kuhl, Tsao & Liu (2003), *PNAS* `10.1073/pnas.1532872100`, PMID
12861072. Nine-month-old American infants received 12 laboratory sessions of Mandarin exposure;
live exposure *"reversed the decline seen in the English control group,"* while *"exposure to
recorded Mandarin, without interpersonal interaction, had no effect."* `MEASURED-RCT`, `n = 32` per
experiment with 21 and 28 completing. The commercial test is DeLoache et al. (2010), *Psychological
Science* `10.1177/0956797610384145`: a month of at-home baby-media DVD in 12–18-month-olds.
*"Children who viewed the DVD did not learn any more words… The highest level of learning occurred
in a no-video condition in which parents tried to teach their children the same target words during
everyday activities."* `MEASURED-RCT`.

## 2.2 The contingency exception, chased down

The commission asked for this to be chased properly, on the ground that a responsive AI is
contingent where a DVD is not. It does not survive the chase.

**The positive originals.** Roseberry, Hirsh-Pasek & Golinkoff (2014), *Child Development*
`10.1111/cdev.12166`, PMID 24112079: toddlers 24–30 months, `N = 36`, three conditions — live
interaction, socially contingent video chat, yoked non-contingent video. *"Results suggest that
children only learned novel verbs in socially contingent interactions."* `MEASURED-RCT`, twelve
children per cell. Myers, LeWitt, Gallo & Maselli (2017), *Developmental Science*
`10.1111/desc.12430`, PMID 27417537: ages 12–25 months, real-time FaceTime against pre-recorded
video across six calls in two weeks. *"Children in the FaceTime condition (but not the Video
condition) preferred and recognized their Partner, learned more novel patterns, and the oldest
children learned more novel words."* The word-learning result is restricted to the oldest band.

**The negatives, which are larger.**

- Troseth, Strouse, Verdine & Saylor (2018), *Frontiers in Psychology* `10.3389/fpsyg.2018.02195`,
  PMID 30483198, verbatim via PubMed: *"One hundred and thirty two toddlers (24 and 30 months old)"*
  in four conditions crossing responsiveness with medium. *"Children of both ages reliably learned
  the word in the responsive live condition, and older children (30 months) learned in the
  unresponsive live condition. Neither group learned in the responsive or unresponsive video
  conditions. The results show that the addition of communicative social cues to the video
  presentation via video chat was not sufficient to support learning in this case."* `MEASURED-RCT`.
  This is Troseth's own lab, which produced the 2006 contingent-video result the exception rests on.
- Strouse, Troseth, O'Doherty & Saylor (2018), *JECP* `10.1016/j.jecp.2017.09.005`, `n = 88`
  30-month-olds: *"Both on-screen contingency and parent modeling increased children's engagement…
  However, only parent modeling increased children's subsequent word learning."* `MEASURED-RCT`.
- Tsuji, Fiévét & Cristia (2021), *Infant Behavior and Development* `10.1016/j.infbeh.2021.101553`,
  16-month-olds across in-person, video chat and virtual agent: *"Toddlers showed above-chance word
  learning in the in-person group only… These results… elucidate that contingency is not sufficient
  either."* `MEASURED-RCT`.
- And the meta-analytic moderator test above found no difference between live and prerecorded video.

**The verdict.** A small original positive (`n = 36`) with three larger follow-ups that failed to
reproduce it, one from the originating lab, plus a meta-analytic moderator test that found nothing.
The moderator that does survive is a person in the room. Mallawaarachchi et al. (2024), *JAMA
Pediatrics* `10.1001/jamapediatrics.2024.2620`, pooled 100 studies and 176,742 participants: among
all screen-use contexts examined, **co-use was the only one positively associated with cognitive
outcomes, `r = 0.14, 95% CI [0.03, 0.25]`**, while programme viewing (`r = −0.16`) and background
television (`r = −0.10`) were negative. `MEASURED-META`, observational.

`INFERENCE`, and this is the design conclusion for row 13: a responsive AI does not inherit the
contingency exception, because the contingency exception is not well supported. What is supported
is co-viewing. A product for under-threes that works is a product aimed at the adult holding the
child.

## 2.3 What preschool interventions achieve, and what fades

Clements & Sarama's Building Blocks is the best-evidenced preschool mathematics curriculum in
existence, and its own trajectory is the argument.

| Study | Design | Result |
|---|---|---|
| Clements & Sarama (2008), *AERJ* `10.3102/0002831207312908` | 36 classrooms, cluster RCT, 26 weeks | **0.47** vs an active comparison curriculum; **1.07** vs no-maths control |
| Clements, Sarama, Spitler, Lange & Wolfe (2011), *JRME*, ERIC EJ918252 | 42 schools, 106 classrooms, 1,375 preschoolers | **g = 0.72** at end of pre-K |
| Sarama, Clements, Wolfe & Spitler (2012), `10.1080/19345747.2011.627980` | same cohort, one year on | ITT **g = 0.33** / **0.22** |
| Clements, Sarama, Wolfe & Spitler (2013), `10.3102/0002831212469270` | third year | **g = 0.51** / **0.28** |

All cluster-randomised. Note the split in the first row: against an active comparison curriculum
the effect is less than half what it is against no curriculum. Quoting the larger arm of a
two-armed comparison is the `Z1` §2.1 failure mode.

The same programme's scale-up team reported the opposite. Clements, Sarama, Farran, Lipsey, Hofer &
Bilbrey (2011), SREE (ERIC ED518182): *"with the scale-up project, the authors saw evidence of
curricular effects across outcomes at the end of prekindergarten, but very few differences at the
end of kindergarten, and virtually none at the end of first grade."* Then Bailey, Duncan, Watts,
Clements & Sarama (2018), *American Psychologist* `10.1037/amp0000146`, with Clements and Sarama as
co-authors: *"experimental manipulation of early math skills generates much smaller effects on
later math achievement than the nonexperimental literature has suggested."* This dispute is
unresolved inside the programme that generated the data, and the corpus should carry it that way.

**The strongest negative in the field.** Tennessee's Voluntary Pre-K was oversubscribed, permitting
a lottery. Lipsey, Farran & Durkin (2018), *ECRQ* `10.1016/j.ecresq.2018.03.005`: `N = 2,990`
low-income children randomly assigned to admission offers or a waiting list; positive at end of
pre-K, then *"During the kindergarten year and thereafter, the control children caught up with the
pre-k participants on those tests and generally surpassed them."* Durkin, Lipsey, Farran & Wiesen
(2022), *Developmental Psychology* `10.1037/dev0001301`, followed the same randomised sample to
sixth grade: *"the children randomly assigned to attend pre-K had lower state achievement test
scores in third through sixth grades than control children, with the strongest negative effects in
sixth grade."* `MEASURED-RCT`, six-year follow-up, negative. The Head Start Impact Study
(Puma et al. 2012, `n = 4,667` randomised) is milder and points the same way: initial gains, *"very
few impacts found for either cohort in any of the four domains"* by third grade.

## 2.4 Emergent literacy, and the finding that the intervention teaches the adult

The National Early Literacy Panel (2008) (ERIC ED504224, PDF extracted this session) reports that
shared-reading interventions had their largest impact on oral language, **average ES 0.73**, falling
to **0.57** once one quasi-experimental outlier is removed; and that *"Shared-reading interventions
appear to have no impact on young children's PA skills or their AK"* — alphabet knowledge
**ES −0.06, 95% CI [−0.47, 0.35], k = 2**. Code-focused interventions averaged **0.82** on
phonological awareness across 51 studies. `MEASURED-META`.

Mol, Bus, de Jong & Smeets (2008), `10.1080/10409280701838603`: dialogic against typical shared
reading, expressive vocabulary **k = 9, n = 322, d = 0.59, SE 0.08, 95% CI [0.44, 0.75]**; *"the
effect size reduced substantially when children were older (4 to 5 years old) or when they were at
risk for language and literacy impairments."* Dowdall et al. (2020), *Child Development*
`10.1111/cdev.13225`: 19 RCTs, `N = 2,594`, expressive language **d = 0.41**, receptive **0.26**,
and caregiver book-sharing competence **d = 1.01**. Both `MEASURED-META`.

That last row is the shape of the literature. The intervention moves the adult by a full standard
deviation and the child by a third of one.

**The null.** Noble, Sala, Peter, Lingwood, Rowland, Gobet & Pine (2019), *Educational Research
Review*, preprint `10.31234/osf.io/cu7bk`:

> *"Our results show that, while there is an effect of shared reading on language development, this
> effect is smaller than reported in previous meta-analyses (ḡ = 0.215, p < .001). They also show
> that this effect is moderated by the type of control group used and is negligible in studies with
> active control groups (ḡ = 0.021, p = .783)."*

And the confirmatory trial: Noble et al. (2020), *JSLHR* `10.1044/2020_JSLHR-19-00288`, `n = 150`
children aged 2;6–3;0 randomised to pause reading, dialogic reading, or an active shared-reading
control. *"The findings indicated that the interventions were effective at changing caregiver
reading behaviors. However, the interventions did not boost children's language skills over and
above the effect of an active reading control condition."* `MEASURED-RCT`, null.

`INFERENCE`: what shared-reading interventions reliably buy is that the book gets opened and the
adult asks questions. Against a condition where the book gets opened anyway, they buy `g = 0.02`.

## 2.5 The two constraints

**Screen guidance.** WHO (2019), *Guidelines on physical activity, sedentary behaviour and sleep for
children under 5 years of age*, quoted from the WHO release accompanying the guideline: for infants
under 1, *"Screen time is not recommended"*; for 1-year-olds, *"sedentary screen time (such as
watching TV or videos, playing computer games) is not recommended"*; for ages 2 and 3–4,
*"sedentary screen time should be no more than 1 hour; less is better."*

The AAP's 2016 statement *Media and Young Minds* (`10.1542/peds.2016-2591`) is the source of the
widely-cited video-chat carve-out for under-18-months. `[X]` I could not retrieve its recommendation
text: `publications.aap.org`, `pediatrics.aappublications.org` including the free full PDF that
Europe PMC's Unpaywall record lists, the `doi.org` redirect and `healthychildren.org` all returned
403 or 404. The carve-out is confirmed only second-hand, in a peer-reviewed review — Glick et al.
(2022), *WIREs Cognitive Science* `10.1002/wcs.1599`: *"expert recommendations… suggest that video
chat, unlike other screen media, is acceptable for use by children under 18 months."* Reported as
second-hand and unverified at source. AAP issued a successor technical report in 2026
(`10.1542/peds.2025-075321`) reframing screen time as *"just the tip of the iceberg"*; whether it
supersedes the 2016 recommendations was not established.

`INFERENCE` for anyone reading the carve-out as a licence: the exception is for video chat with a
family member, and §2.2 shows the learning evidence for contingent video does not hold up. The
carve-out is a judgment about relationships, not a finding about learning.

**The learner cannot read the interface.** This is the constraint that most obviously favours a
frontier model, and there is one good trial. Xu, Aubele, Vigil, Bustamante, Kim & Warschauer (2022),
*Child Development* `10.1111/cdev.13708`, PMC9299009 (open access, full text extracted this
session): **117 children aged 3–6** (mean 57.6 months), 2×2 factorial crossing dialogic against
non-dialogic reading with conversational agent against human partner, random assignment. Dialogic
reading raised story comprehension, with subscale effects `β = 0.53, p < .001` for event
memorisation, `β = 0.38, p < .05` for inference making, `β = 0.34, p < .05` for sequence
understanding. And the comparison the corpus needs: *"the interaction model suggested that dialogic
reading with an agent induced a comparable level of positive effect on children's story
comprehension as an adult reader (β = 0.22, p = .35)."* `MEASURED-RCT`.

Two cautions the paper states itself. The equivalence claim rests on a non-significant interaction
in `n = 117`, which is not demonstrated equivalence; and the sample had *"homogeneous high language
proficiency,"* which the authors say *"may have obscured our ability to uncover the heterogenous
effects."*

Set that against Tsuji et al. (2021), where at 16 months the virtual-agent condition performed
significantly worse than in-person. Together the two results locate a boundary: somewhere between
two and four years, a responsive agent goes from worse-than-nothing to
indistinguishable-from-an-adult on a bounded conversational task.

## 2.6 Should a frontier AI tutor touch this age group?

**Under three: no, and not as a matter of caution.** The video deficit is `≈0.5 SD` across 122
effect sizes; contingency does not remove it in the three largest tests; a month of commercial baby
media taught zero words in a randomised trial; WHO recommends zero screen time to age two; and the
one intervention family that works moves the adult by `d = 1.01` and the child by `g = 0.02`
against an active control. There is no gap in that picture for a child-facing tutor to fill.

**Three to five: yes, in one shape.** An agent that talks, that the child answers aloud, on content
an adult chose, with the adult present and reading along, on a bounded task. That is Xu et al.'s
design and the only positive randomised result in this section involving a machine. It is a
dialogic reading partner, not a tutor.

`SPEC`: for this age the system's user is the caregiver and the child is the beneficiary. The
product surface is whatever gets the adult to open the book and ask the third question. The measured
target is caregiver book-sharing competence, where effect sizes are large and reliable, and child
language is accepted as the small downstream consequence it is.

---

# PART 3 — ADULTS RETURNING TO STUDY, AND RESKILLING

`[X]` `andragogy` 0 hits, `adult education` 0, `reskilling` 0.

## 3.1 Andragogy has been tested

Knowles's andragogy is the field's organising framework, resting on assumptions about
self-direction, the role of experience, readiness to learn, orientation to learning and internal
motivation. It was subjected to experimental test.

**Rachal, J. R. (1994). "Andragogical and Pedagogical Methods Compared: A Review of the Experimental
Literature."** ERIC ED380566, verbatim:

> *"Eighteen studies that attempted to do so included 15 dissertations and 3 journal articles… Of
> the 16 studies that examined achievement in terms of either cognitive gain or skill performance,
> 10 found no significant differences between control and experimental groups; 2 found the control
> or 'traditional' group performed better… Two other variables showed statistically significant
> differences favoring andragogy: application of the learned material and attendance. Despite some
> issues of design and questions of andragogical 'purity,' the trend of the available empirical
> literature runs counter to many of the anecdotal claims for andragogy superiority."*

`MEASURED-META` — a vote-count review, no pooling, no effect sizes. Fifteen of eighteen studies are
unpublished dissertations, which cuts both ways: weaker quality control, less publication filtering.

The most recent randomised test I could locate points the same way. Bradley (2010), ERIC ED517783,
randomly assigned 52 non-profit staff to andragogical or pedagogical online grant-writing modules,
analysing 33: *"one-way ANOVAs revealed there were no statistically significant differences as a
function of learning group between each of three dependant variables: reaction to learning…,
achievement growth…, and grant writing performance scores,"* and completion rates likewise did not
differ. `MEASURED-RCT`, small, null on every outcome.

Rachal (2002), *Adult Education Quarterly* (ERIC EJ644442): *"Evidence of the efficacy of andragogy
is inconclusive and affected by definitional confusion."* Davenport (1987), ERIC ED283989, reached
the same place. And the theory's own proponents concede the underlying problem — Holton, Wilson &
Bates (2009), *HRDQ* (ERIC EJ848487): *"A major and glaring gap in andragogy research is the lack of
a measurement instrument that adequately measures both andragogical principles and process design
elements. As a result, no definitive empirical test of the theory has been possible."* That is
forty years after publication.

`[X]` `OBSERVED — absence`: **no meta-analysis or systematic quantitative synthesis of andragogy
exists.** ERIC returns `numFound: 0` for `"andragog*" AND "meta-analysis"`, and the one item calling
itself a meta-analysis (Taylor & Kroth 2009, ERIC EJ891073) is a narrative review with no `k`, no
pooled estimate and no effect sizes. It should not be cited as quantitative evidence.

The best quantitative evidence bearing on andragogy's central assumption comes from outside the
tradition. Sitzmann & Ely (2011), *Psychological Bulletin* `10.1037/a0022777`, meta-analysed
self-regulated learning in work-related training and educational attainment, **k = 430,
N = 90,380**: *"Goal level, persistence, effort, and self-efficacy were the self-regulation
constructs with the strongest effects on learning… However, 4 self-regulatory processes — planning,
monitoring, help seeking, and emotion control — did not exhibit significant relationships with
learning."* `MEASURED-META`. Self-direction, decomposed, is partly real and partly not.

`INFERENCE`: what survives is not a learning mechanism. It is two behavioural facts — adults who
chose to be there apply the material and attend — and one design constraint, that participation is
voluntary and therefore attrition is the binding risk. `F6` is already built for that constraint.
The rest of andragogy should not enter a specification.

## 3.2 The two-sided age effect

The corpus owns half of this. `J1`'s expertise-reversal law predicts that the adult learner's
prior-knowledge advantage makes guidance less useful, and that the asymmetry grows with domain
experience — a strong prediction for this population, stated in the corpus without ever being aimed
at adults.

**The cost side is well measured and it is not small.** Salthouse (2009), *Neurobiology of Aging*
`10.1016/j.neurobiolaging.2008.09.023`, PMC2683339, `N = 2,350` aged 18–60: *"The performance
difference from age 18 to age 60 was about 1 SD for the speed and spatial visualization variables,
and was between .6 and .7 SD for the reasoning and memory variables,"* with slopes of *"-.02 to -.03
SD units per year"* under 60. `OBSERVED` (cross-sectional; Schaie's published reply in the same
issue, PMID 19231029, disputes the design). Verhaeghen & Salthouse (1997), *Psychological Bulletin*,
`k = 91`, found speed and working memory mediate age effects on reasoning and episodic memory.
`MEASURED-META`. And directly on the outcome that matters here, Kubeck, Delp, Haslett & McDaniel
(1996), *Psychology and Aging*, PMID 8726375, **83 effect sizes from 6,610 individuals**:
*"older adults, relative to younger adults, showed less mastery of training material (r = −.26),
completed the final training task more slowly (r = .28), and took longer to complete the training
program (r = .42). Field samples generally showed smaller age effects than laboratory samples."*
`MEASURED-META`.

**The benefit side is measured too.** Verhaeghen (2003), *Psychology and Aging*, PMID 12825780,
pooled 324 independent young–old comparisons across 210 articles: *"The average effect size,
favoring the old, was 0.80 SD"* on vocabulary. `MEASURED-META`.

**And the one study that puts them in the same regression is optimistic.** Beier & Ackerman (2005),
*Psychology and Aging*, PMID 16029097, `n = 199` aged 19–68, predicting acquisition of new
cardiovascular-disease and xerography knowledge from prior knowledge, fluid ability and crystallised
ability: *"Gc was directly related to learning from the video for both domains. Because the
trajectory of Gc stays relatively stable throughout the life span, these findings provide a more
optimistic perspective on the relationship between aging and learning than that offered by theories
that focus on the role of fluid abilities in learning."* `OBSERVED`, correlational with ability
controls.

`INFERENCE`: an adult learns new material more slowly (`r ≈ .28–.42` on time) and masters less of it
per unit of instruction (`r ≈ −.26`), and arrives with an 0.80 SD verbal-knowledge advantage that
predicts acquisition in domains adjacent to what they already know. The design consequence is that
adult tutoring should be routed through the learner's existing knowledge as a matter of arithmetic,
not sentiment, and should never be paced by a clock calibrated on undergraduates.

## 3.3 The industry that does not measure the thing it sells

Arthur, Bennett, Edens & Bell (2003), *Journal of Applied Psychology* `10.1037/0021-9010.88.2.234`,
PMID 12731707, verbatim via PubMed:

> *"Results of the meta-analysis revealed training effectiveness sample-weighted mean ds of 0.60
> (k = 15, N = 936) for reaction criteria, 0.63 (k = 234, N = 15,014) for learning criteria, 0.62
> (k = 122, N = 15,627) for behavioral criteria, and 0.62 (k = 26, N = 1,748) for results criteria."*

`MEASURED-META`. Every effect size sits between 0.60 and 0.63, which looks suspicious until you read
the `k`s, and the `k`s are the finding. Learning is measured 234 times. Results are measured 26
times, on 1,748 people in total — the whole industry's evidence for whether training changes
anything an employer would pay for, spread across two decades of studies.

The practice survey behind that asymmetry is traceable. Twitchell (1997), LSU dissertation
`10.31390/gradschool_disstheses.6552`, published as Twitchell, Holton & Trott (2000), *Performance
Improvement Quarterly* `10.1111/j.1937-8327.2000.tb00177.x`, `n = 146` returned surveys, 42%
response: *"technical training managers reported using each of Kirkpatrick's four Levels of
evaluation in the following percentage of their courses: Level 1—72.74%, Level 2—47.05%,
Level 3—33.73%, and Level 4—20.82%."* `OBSERVED`. The more widely circulated ATD/ASTD percentages
could not be verified: `td.org` returned HTTP 429 on repeated attempts, the Wayback Machine has no
snapshot of the relevant pages, and ERIC indexes no ASTD report containing level-by-level figures.
Use the number that has a DOI.

Blume, Ford, Baldwin & Huang (2010), *Journal of Management* `10.1177/0149206309352880`, 89 studies,
gives the reason to distrust even the 122: *"situations in which transfer outcomes were obtained by
the same source in the same measurement context — which consistently inflated transfer
relationships."* Most behaviour-change measurement is the trainee reporting their own behaviour
change to the trainer.

Taylor, Russ-Eft & Chan (2005), *JAP* `10.1037/0021-9010.90.4.692`, PMID 16060787, 117 studies of
behaviour-modelling training, is the best-behaved result in the area: *"BMT effects were largest for
learning outcomes, smaller for job behavior, and smaller still for results outcomes. Although BMT
effects on declarative knowledge decayed over time, training effects on skills and job behavior
remained stable or even increased… Transfer was greatest when mixed (negative and positive) models
were presented, when practice included trainee-generated scenarios, when trainees were instructed to
set goals, when trainees' superiors were also trained, and when rewards and sanctions were
instituted in trainees' work environments."* `MEASURED-META`. Note the decay pattern runs opposite
to the folk claim: knowledge decays, skills and job behaviour do not.

Four of those five transfer conditions sit outside the training — goals, the manager, the incentive
structure, and the scenario coming from the trainee's own work. That is the adult analogue of
Slavin's individual accountability: the effect lives in the surrounding structure. Lacerenza, Reyes,
Marlow, Joseph & Salas (2017), *JAP* `10.1037/apl0000241`, `k = 335`, points the same way and adds
one finding a software vendor should read twice: leadership training produced *"reactions (δ = .63),
learning (δ = .73), transfer (δ = .82), and results (δ = .72),"* with moderator support for
*"spaced training sessions, a location that is on-site, and face-to-face delivery that is not
self-administered."* `MEASURED-META`.

**The 10% claim is untraceable, and the debunking is real.** The assertion that only about 10% of
training transfers to the job is universally attributed to Georgenson (1982), *Training and
Development Journal* 36(10), 75–78. `[X]` It is absent from Crossref, absent from OpenAlex, and
absent from ERIC — which indexes a *different* Georgenson article from the same journal and era
(EJ306199, 1984), so the gap is not a coverage artefact. The venue is a trade magazine and the piece
is three to four pages. There is no sample and no method behind the number. Fitzpatrick's debunking
does exist — *"The strange case of the transfer of training estimate,"* *TIP* 39(2), 2001,
`10.1037/e576912011-002` (APA PsycEXTRA), confirmed in both Crossref and OpenAlex — though its full
text was not retrieved and no verbatim quote from it is available. The 10% figure is folklore with a
citation attached and is not cited here as evidence.

## 3.4 Adult literacy and numeracy

**Scale, and it is getting worse.** PIAAC Cycle 1 (NCES 2019-179, PDF extracted this session):
*"one in five U.S. adults (21 percent) has difficulty completing these tasks… This translates into
43.0 million U.S. adults who possess low literacy skills."* Cycle 2 (NCES, *Highlights of the 2023
U.S. PIAAC Results*): *"Between 2017 and 2023, there were increases in the percentages of adults
performing at the lowest proficiency level (Level 1 or below) in both literacy and numeracy: in
literacy this percentage increased from 19 to 28 percent and in numeracy from 29 to 34 percent,"*
with the report's own caveat that *"Response rates for this data collection were relatively low."*
Internationally, OECD (2024), *Survey of Adult Skills 2023* `10.1787/b263dc5d-en`, assessed
*"about 160 000 adults aged 16-65 from 31 countries and economies"* and found *"26% in literacy, 25%
in numeracy"* at Level 1 or below, with *"average literacy proficiency… stable or declined in most
participating countries"* over the decade. `FILING`.

**Evidence.** Torgerson, Porthouse & Brooks ran two syntheses. The 2003 one
(`10.1111/1467-9817.00200`) restricted to RCTs and found **nine, worldwide, 1980–2002**, with
*"evidence of publication bias"* and the conclusion that *"There is a dearth of rigorous RCTs in the
field of adult literacy and numeracy."* The 2005 one (ERIC EJ718454) widened to controlled trials:
*"We included 27 controlled trials (CTs)… 18 CTs with no effect sizes (incomplete data) and 9 CTs
with full data… Three of the nine trials showed a positive effect for the interventions, five trials
showed no difference and one trial showed a positive effect for the control treatment… it is
difficult to make any recommendations as to the type of adult education that should be supported."*
`MEASURED-META`.

For scale against outcome: the US National Reporting System recorded **1,120,769** Title II adult
education participants in PY2022–23, of whom **43% made a measurable skill gain** and **15,320
attained a postsecondary credential** while enrolled or within a year of exit — 1.4%. `FILING`,
administrative, no control group.

## 3.5 The documented adult nulls

**Brooks, Burton, Cole, Miles, Torgerson & Torgerson (2008). "Randomised Controlled Trial of
Incentives to Improve Attendance at Adult Literacy Classes."** *Oxford Review of Education*, ERIC
EJ810523, verbatim:

> *"We used a cluster-randomised design. Twenty-nine adult literacy classes were randomised in two
> groups using minimisation. Intervention group learners received 5 British Pounds (US$10) for each
> class attended… In the 28 remaining classes there was a statistically significant reduction of
> about 1.5 sessions (95% confidence interval (CI) 0.28, 2.79; p = 0.019) attended by the
> intervention group compared with control, after adjusting for cluster size and baseline scores.
> The difference in reading scores… was −2.38 (with controls scoring higher than the intervention
> group), but this difference was not statistically significant (95% CI −7.40 to 2.57, p = 0.33)."*

`MEASURED-RCT`, the only UK RCT of financial incentives in adult literacy. The intervention reduced
attendance, and the reading-score point estimate also ran against it.

The second is the one most directly about a product. Ainsworth, Gilchrist, Grant, Hewitt, Ford,
Petrie, Torgerson & Torgerson (2012), *Educational Studies*, ERIC EJ959747: two RCTs of an online
medication-dosage simulation for student nurses' general numeracy. *"The Intention to Treat (ITT)
analysis in both trials revealed a small negative effect… statistically significant in one trial.
However, compliance with the intervention was very low in both trials, with only 24 and 12% of
students allocated to the intervention groups spending more than 15 minutes using the programme."*
`MEASURED-RCT`.

`INFERENCE`: for adults, dosage is the whole trial. Some 88% of a motivated, professionally
obligated population did not spend fifteen minutes with free software aimed at a skill they were
assessed on. An adult-tutoring specification whose efficacy argument does not open with an
engagement number is not making an argument.

A third, at national scale. Ricciuti, St.Pierre, Lee, Parsad & Rimdzius (2004), *Third National Even
Start Evaluation* (ERIC ED484058; IES), randomly assigned **463 families** across 18 grantees in 14
states — 309 to Even Start, 154 to control — and measured adult literacy directly with the
Woodcock-Johnson: *"Even Start children and parents made gains on a variety of literacy assessments
and other measures at follow-up, but they did not gain more than children and parents in the control
group… The underlying premise of Even Start as described by the statute and implemented in the field
was not supported by this study."* `MEASURED-RCT`. The report notes this was the third consecutive
null for the programme: *"A previous randomized controlled trial in the early 1990s did not show
this program to have positive impacts."*

## 3.6 Reskilling: the only unambiguous transfer criterion in this corpus

Card, Kluve & Weber (2018), *JEEA* `10.1093/jeea/jvx028` (IZA DP 9236, PDF extracted this session)
assemble *"a sample of 207 studies that provide 857 separate estimates."* Their conclusions:
*"(1) average impacts are close to zero in the short run, but become more positive 2-3 years after
completion of the program; (2) the time profile of impacts varies by type of program, with larger
gains for programs that emphasize human capital accumulation."* And the training-specific pattern:
*"Work first programs tend to have larger short term effects, whereas human capital programs have
small (or in some cases even negative) short term impacts, coupled with larger impacts in the medium
or longer run… the pattern of rising impacts is driven almost entirely by training-based programs."*
One caveat from the same paper matters for how much of this corpus can lean on it: *"the fractions
of training programs evaluated by RCT's is relatively low."* `MEASURED-META`, predominantly
non-experimental.

**The RCT.** The WIA Gold Standard Evaluation (Fortson, Rotz, Burkander, Mastri, Schochet, Rosenberg
& McConnell, 2017; Mathematica for the U.S. Department of Labor) randomly assigned over 34,000
customers across 28 randomly selected local workforce investment areas to three research groups. At
thirty months, intensive staff-assisted services raised earnings by *"$3,300 to $7,100 (7 to 20
percent) per customer depending on the data source."* But: *"Though not conclusive, the evidence
suggests that training funded by the Adult and Dislocated Worker programs does not have positive
impacts in the 30 months after study enrollment… the evidence suggests that it is not likely that
the impacts will increase because the difference across groups in enrollment in training disappeared
by the beginning of the second year after random assignment."* `MEASURED-RCT`.

`OBSERVED`, and worth a sentence on its own: **the arm that worked was published in a journal and
the arm that produced the null was not.** The counselling result appears as McConnell, Schochet,
Rotz, Fortson, Burkander & Mastri (2021), *JPAM* `10.1002/pam.22305`. The training null appears only
in the grey-literature report. That is the corpus's own publication-bias concern operating inside a
single federal evaluation.

**The rest of the record.** Trade Adjustment Assistance (Schochet, D'Amico, Berk, Dolfin & Wozny,
2012) is the most negative large-scale US retraining result: *"even four years after job loss, they
had not yet closed the gap,"* and *"Over the entire 16-quarter follow-up period, the average
participant earned about $37,100 less than the average comparison."* `OBSERVED` — a matched
comparison design, not an RCT, as the report states. Job Corps (Schochet, Burghardt & McConnell,
2008, *AER* `10.1257/aer.98.5.1864`, `n = 15,400` randomised) is an RCT and reports its own fade:
*"Based on tax data, however, the earnings gains were not sustained except for the oldest
participants."* `MEASURED-RCT`.

Two positives, with their caveats attached. Year Up (Fein & Hamadyk, 2018, OPRE 2018-65,
`n = 2,544` randomised) *"increased average quarterly earnings by $1,895 (53 percent)"* — *"the
largest reported to date for workforce programs tested using a randomized controlled trial"* —
against a per-participant cost of $28,290, more than half funded by employers, and a control group
of whom *"57 percent… pursued training"* anyway. `MEASURED-RCT`. And WorkAdvance (MDRC,
`n = 2,564`) is the reason to distrust any single-timepoint claim: at two years Per Scholas had
*"large and consistent impacts"* while St. Nicks Alliance *"did not produce positive impacts"*; at
seven years Per Scholas raised earnings 14% and no other site moved; at ten years *"the WorkAdvance
program at St. Nicks Alliance increased average earnings by 32 percent"* and *"the other three
WorkAdvance programs did not have an impact."* `MEASURED-RCT`. The sign flipped between sites over
a decade.

## 3.7 Adult online learning, and why the headline numbers mislead

Two meta-analyses settle the shape of this and both are routinely misquoted.

Means, Toyama, Murphy, Bakia & Jones (2009), the US Department of Education review (ERIC ED505824),
is cited everywhere for *"an average effect size of +0.20 favoring online conditions."* Its own text
supplies the correction: *"The mean effect size in studies comparing blended with face-to-face
instruction was +0.35, p < .001… larger than that for studies comparing purely online and purely
face-to-face conditions, which had an average effect size of +0.05, p = .46. In fact, the learning
outcomes for students in purely online conditions and those for students in purely face-to-face
conditions were statistically equivalent."* And on the population: *"The meta-analysis of 50 study
effects, 43 of which were drawn from research with older learners,"* with the authors warning
against generalising to K-12. `MEASURED-META`. This is an adult-learning meta-analysis that the
field cites as a schools one.

Cook, Levinson, Garside, Dupras, Erwin & Montori (2008), *JAMA* `10.1001/jama.300.10.1181`,
`k = 201` studies of internet-based learning in the health professions, makes the same point in one
comparison: against no intervention, knowledge **1.00, 95% CI [0.90, 1.10]**; against non-internet
formats, knowledge **0.12, 95% CI [0.003, 0.24]**, satisfaction **0.10, n.s.**, skills **0.09,
n.s.** *"Internet-based learning is associated with large positive effects compared with no
intervention. In contrast, effects compared with non-Internet instructional methods are
heterogeneous and generally small."* `MEASURED-META`.

The best-powered field estimate runs mildly negative. Xu & Jaggars (2013), CCRC WP 54 /
*Journal of Higher Education* `10.1080/00221546.2014.11777343`, used individual fixed effects across
*"nearly 500,000 courses taken by over 40,000 community and technical college students"*: online
course grade **−0.215 (OLS)** to **−0.282 (with working hours)**, persistence **−0.031** to
**−0.046**, all `p < .001`, and *"males, younger students, Black students, and students with lower
grade point averages"* suffered most. `OBSERVED`, quasi-experimental. The randomised versions agree:
Figlio, Rush & Yin (2013), *JOLE* `10.1086/669930`, found *"modest evidence that live-only
instruction dominates internet instruction… particularly strong for Hispanic students, male
students, and lower-achieving students"* (Hispanic `11.276***`); Joyce et al. (2015), `n = 725`,
found traditional format ahead by 2.3 points and noted *"the non-experimental [estimates] were 2.5
times larger, suggesting that the large effects of attending lectures found in the previous
literature are likely due to selection bias."* Bowen, Chingos, Lack & Nygren (2014), *JPAM*
`10.1002/pam.21728`, `n = 605` across six campuses, found hybrid and face-to-face statistically
equivalent.

MOOC completion supplies the dosage number. Reich & Ruipérez-Valiente (2019), *Science*
`10.1126/science.aav7958`, over *"12.67 million course registrations from 5.63 million learners"*:
*"Of those who register for a course, 52% never enter the courseware,"* certification 4.96% in
2013–14 falling to **3.13%** in 2017–18, 46.02% among paying verified learners, and *"Six years of
investment in course development and learning research has not produced meaningful improvements in
these figures."* `OBSERVED`.

**A vendor claim, traced.** Grow with Google's certificates page states *"70%+ of certificate
graduates report a positive career outcome… within six months"* and, on the same page, *"75 percent
of program graduates report an improvement in their career."* The entire source footnote reads:
*"Based on program graduate survey, United States 2025."* `VENDOR`. No control group, so it is not
an impact estimate; no sample size or response rate; graduates only, excluding every dropout;
self-reported rather than administrative earnings; and two different headline percentages sharing
one footnote. `[X]` No independent or peer-reviewed evaluation of Google Career Certificates was
located in Crossref, ERIC or NBER; since WebSearch was unavailable, that is *not located*, not
*does not exist*.

`INFERENCE`: this is the segment where an outcome could genuinely be measured, and the reason is
structural. The transfer criterion is administrative — employment, wages, a credential an employer
accepts — and somebody else records it, in state unemployment-insurance wage records, which is how
the WIA evaluation and the Job Corps tax-data follow-up measured it. Every other population in this
corpus requires the evaluator to build the outcome measure. This one does not, and the WorkAdvance
sequence shows that whoever does build it must plan to read it at seven and ten years, because the
two-year answer was wrong at three of four sites.

---

## 4. Null and negative register

| # | Result | Source | Label |
|---|---|---|---|
| N1 | Group project reduced content learning vs a shortened individual version | Bacon (2005) `10.1177/1052562904263729` | `MEASURED-RCT` |
| N2 | Cooperative learning without individual accountability: median **+0.07** | Slavin (2014) summarising Slavin (1995), 99 studies | `MEASURED-META` |
| N3 | *"Few approaches to discussion were effective at increasing students' literal or inferential comprehension and critical thinking"* | Murphy et al. (2009) `10.1037/a0015576` | `MEASURED-META` |
| N4 | CSCL scripts on motivation **g = 0.13, n.s.** — the over-scripting worry did not replicate | Radkowitsch et al. (2020), 53 studies, 5,616 learners | `MEASURED-META` |
| N5 | Small-group vs individual with technology held constant: **+0.15**, heterogeneous | Lou, Abrami & d'Apollonia (2001), 122 studies | `MEASURED-META` |
| N6 | Homogeneous ability grouping beat heterogeneous, **+0.12** | Lou et al. (1996), 20 direct comparisons | `MEASURED-META` |
| N7 | Groups recall less than the pooled recall of the same individuals alone | Marion & Thorley (2016), 64 studies | `MEASURED-META` |
| N8 | No word learning from responsive **or** unresponsive video, `n = 132` | Troseth et al. (2018) `10.3389/fpsyg.2018.02195` | `MEASURED-RCT` |
| N9 | Contingency raised engagement; only parent modelling raised learning, `n = 88` | Strouse et al. (2018) `10.1016/j.jecp.2017.09.005` | `MEASURED-RCT` |
| N10 | A month of commercial baby-media DVD taught zero additional words | DeLoache et al. (2010) `10.1177/0956797610384145` | `MEASURED-RCT` |
| N11 | Shared reading vs active controls: **ḡ = 0.021, p = .783** | Noble et al. (2019); confirmed by RCT `n = 150` (2020) | `MEASURED-META` + `MEASURED-RCT` |
| N12 | Shared reading on alphabet knowledge: **−0.06 [−0.47, 0.35]** | NELP (2008), k = 2 | `MEASURED-META` |
| N13 | Tennessee pre-K randomised sample scored lower through sixth grade | Durkin et al. (2022), `n = 2,990` | `MEASURED-RCT` |
| N14 | Andragogical vs pedagogical: 10 of 16 no difference, 2 favouring traditional | Rachal (1994), ERIC ED380566 | `MEASURED-META` |
| N15 | Andragogical vs pedagogical online modules: null on reaction, achievement, performance and completion | Bradley (2010), ERIC ED517783, `n = 52` randomised | `MEASURED-RCT` |
| N16 | Planning, monitoring, help seeking and emotion control showed **no significant relationship with learning** | Sitzmann & Ely (2011), `k = 430`, `N = 90,380` | `MEASURED-META` |
| N17 | **£5 per class attended reduced attendance** by ~1.5 sessions, p = .019 | Brooks et al. (2008), 28 clusters | `MEASURED-RCT` |
| N18 | Numeracy software: small negative ITT effect; 12–24% used it for >15 minutes | Ainsworth et al. (2012), two RCTs | `MEASURED-RCT` |
| N19 | Even Start: parents gained, but no more than controls — the programme's third consecutive null | Ricciuti et al. (2004), 463 families randomised | `MEASURED-RCT` |
| N20 | WIA-funded training: no positive earnings impact at 30 months | WIA Gold Standard Evaluation (2017), `n > 34,000` | `MEASURED-RCT` |
| N21 | Purely online vs purely face-to-face: **+0.05, p = .46** — statistically equivalent | Means et al. (2009), `k = 50` | `MEASURED-META` |
| N22 | Internet-based learning vs **non-internet formats**: knowledge **0.12**, skills 0.09 n.s., satisfaction 0.10 n.s. | Cook et al. (2008), *JAMA*, `k = 201` | `MEASURED-META` |
| N23 | Online community-college courses: grade **−0.28**, persistence **−0.046**, `p < .001` | Xu & Jaggars (2013), ~500,000 courses | `OBSERVED` |

---

## 5. Delivery constraint, or mechanism? The position

The corpus has treated one-to-one as the ideal and the classroom as a rationing artifact. That
framing contains a false disjunction, and the literature separates the parts.

**Most of what a classroom does is a rationing artifact, and the numbers say so.** Group size,
seating, simultaneous pacing, the lecture, the shared worksheet, the single group product — each is
a consequence of one adult and thirty children, and each costs measured achievement. The single
group product is the +0.07 condition. Ability-heterogeneous grouping, imposed because a classroom
cannot sort continuously, loses 0.12 against homogeneous grouping. Traditional lecture, which
exists because talking to thirty people at once is the only way to talk to thirty people at once,
loses 0.47 SD and carries an odds ratio of 1.95 for failing. AI removes all of this and the corpus
is right about it.

**Three things are mechanisms, and they behave differently under substitution.**

*(a) Individual accountability is a mechanism, and AI supplies it better than a classroom does.*
The entire measured achievement effect of cooperative learning is the margin by which reward
computed from every member's individual learning suppresses the free rider: +0.32 against +0.07. A
classroom achieves that condition in 17% of lessons because computing it is administratively
expensive. A system that measures every learner continuously computes it for free. This is the one
place where the group's mechanism is strengthened by AI, and it is the finding this section exists
to deliver.

*(b) Explaining and being explained to is a mechanism, partly recoverable.* The corpus already
records `g = 0.56` for human learning-by-teaching and `g = 0.43` for peer tutoring's tutor gain.
Marion & Thorley supply the mechanism for one part: post-collaborative individual retrieval
improves, and the moderator analysis supports re-exposure as a partial cause. Re-exposure in another
person's order does not require the other person to be a person. A system that makes a learner
articulate a position, then presents the material back reorganised by a different logic, reproduces
the part of the effect whose mechanism is understood.

*(c) Being disagreed with by someone genuinely uncertain is a mechanism, and AI cannot supply it.*
Smith et al. (2009) is load-bearing: discussion improved performance *"even when none of the
students in a discussion group originally knows the correct answer."* Whatever produces that gain
requires two agents who have committed to positions, neither of whom knows, and whose commitment is
real. A model that knows the answer and performs uncertainty is not in that state. The corpus has
reached this conclusion twice from other directions — `I1` scores "genuine peers with real stakes"
as one of three costs AI does not collapse, and `I2` finds chavruta's symmetry does not survive
substitution — and this is the same inference arriving a third time from the measured side.

**How much is (c) worth?** Here the argument has to be quantitative or it is a worry. The upper
bound is Slavin's +0.32, and that is the whole cooperative-learning effect, of which (a) is by
construction the largest part, since removing it takes the effect to +0.07. Lou et al.'s +0.15 for
small-group against individual learning with technology held constant is a better estimate of the
residual, and it is heterogeneous. Peer instruction's clean isolation is a within-course gain on
isomorphic items, not a semester outcome.

`INFERENCE`, as the position the commission asked for: **the irreducible peer mechanism is worth on
the order of 0.1 to 0.2 SD, it is the only part of the group AI cannot fake, and it is smaller than
the corpus's anxiety about it.** Against it, the delivery constraints AI removes are worth 0.47 SD
on the lecture alone and roughly a quarter of a standard deviation on the accountability structure
classrooms cannot afford to implement.

**The loss is not zero, and it is concentrated somewhere specific.** Look again at the CSCL table.
Scripted collaboration moves domain knowledge by 0.20–0.24 and collaboration skills by 0.72–0.95.
Perfect personalisation loses little subject matter. It loses the outcome the group was uniquely
good at teaching — working with another person — and this corpus has no other instrument that
produces it. That is the real cost of the single-tutor thesis. The corpus's existing worry, that a
personalised explanation can be discussed with nobody, points at it from the wrong side: the
problem is not that the explanation is unshareable, but that the learner never practises sharing.

---

## 6. What is now buildable, the experiment, and what I could not find out

### 6.1 Buildable

1. **An individual-accountability layer** — the highest-value group mechanism and the one AI makes
   cheaper. `SPEC`. Slavin's condition implemented literally: any multi-learner activity computes
   its group outcome from every member's separately measured individual post-performance, never from
   a shared artifact. The falsifier is already in the literature — a system rewarding a single group
   product has a predicted effect of +0.07. This is a short scoring rule with a meta-analytic prior
   attached.

2. **AI-brokered human pairing, with the AI outside the dyad.** `SPEC`. Since (c) requires two
   genuinely uncertain agents, the system's job is to find the second one: match two learners whose
   current model states disagree on the same item, put it to both, require each to commit before
   seeing the other, then let them talk. `I2` §9.4 already specifies the pairing idea; what this
   report adds is the selection rule, because Smith et al. show the gain survives when neither knows.
   The matching criterion is disagreement, not complementary expertise.

3. **A caregiver-facing product for ages 3–5, and nothing child-facing under 3.** `SPEC`, per §2.6.
   The measured target is caregiver book-sharing competence (`d = 1.01`); the delivery form with the
   only positive randomised result is a talking dialogic-reading partner used with an adult present.

4. **An adult product whose first published metric is minutes-on-task, before any efficacy claim.**
   `SPEC`. Ainsworth et al. is the standing warning: 12–24% compliance destroyed two RCTs aimed at a
   professionally obligated population. `F4` and `F6` supply the machinery; what this report adds is
   that for adults, dosage is not a threat to validity, it is the finding.

5. **Structural transfer supports for workplace learning**, taken from Taylor et al.'s moderator
   list: trainee-generated scenarios, explicit goal setting, and the learner's manager brought into
   the loop. `SPEC`. Four of the five conditions under which behaviour-modelling training
   transferred sit outside the instruction, which makes them the product.

### 6.2 The single highest-value experiment, with power

**Question.** Does the irreducible peer mechanism — commitment plus genuine mutual uncertainty —
carry measured achievement over an AI tutor supplying everything else?

**Design.** Three arms, randomised at learner level within classrooms, one term, one subject with a
validated concept inventory. Introductory mechanics is the obvious choice: the FCI exists, and
Hake's data give a baseline.

- **A** — AI tutor alone: full personalisation, individual-accountability scoring, no peers.
- **B** — AI tutor plus an AI peer that commits to a possibly-wrong position and defends it. This is
  `F2`'s specification, tested.
- **C** — AI tutor plus brokered human pairing on disagreement items (§6.1.2).

**Primary outcome.** Delayed concept-inventory score at eight weeks, scored blind. **Secondary.** A
collaboration-skill measure, because the CSCL table says that is where the group's distinctive
effect lives and no arm-A system can produce it.

**Power.** The contrast that matters is C − B: whether human uncertainty beats simulated
uncertainty. §5 puts the residual peer mechanism at 0.1–0.2 SD, so the trial must be powered for the
low end. Detecting `d = 0.15` at 80% power, α = 0.05 two-sided, needs `n ≈ 699` per arm
(2 × (1.96 + 0.84)² / 0.15²), so about 2,100 learners across three arms. With individual
randomisation inside classrooms, an ICC of 0.05 and average cluster size 25 give a design effect of
1 + (25 − 1)(0.05) = 2.2 against classroom-level contamination, raising the requirement to roughly
4,600. At the more optimistic `d = 0.25` it is `n ≈ 252` per arm before the design effect and about
1,700 after it.

`INFERENCE`: that arithmetic says the peer-mechanism question cannot be answered by anything smaller
than a multi-school trial, which is why nobody has answered it. A 60-learner pilot has 80% power
only for `d ≈ 0.51`, larger than the entire cooperative-learning effect. Any study in this space
with `n < 500` per arm reporting a null on peers has not tested the hypothesis.

**The cheap experiment worth running first is a different one.** The collaboration-skill secondary
outcome is where the CSCL metas predict `g ≈ 0.7`, and at that magnitude `n ≈ 33` per arm suffices
before the design effect. The highest-value cheap experiment is not the achievement question at all.
It is measuring whether an AI-mediated group teaches a learner to work with a person.

### 6.3 What I could not find out

1. **Kyndt et al.'s pooled effect sizes.** The one deliberately independent replication of the
   cooperative-learning literature, with the strictest inclusion rule, and its magnitudes are behind
   Elsevier. Unpaywall: `is_oa: false`, zero OA locations; ScienceDirect 403; the Antwerp repository
   copy intranet-only. The largest single gap in Part 1.
2. **Karau & Williams's pooled social-loafing effect.** Untraceable across PubMed, Crossref,
   Semantic Scholar, Europe PMC and Unpaywall. Not cited.
3. **The 10%-of-training-transfers figure.** Untraceable; searches listed in §3.3. Not cited.
4. **Dillenbourg's over-scripting paper at source.** HAL returns an anti-bot challenge. Reported as
   widely held and unverified; the one meta-analysis that tested it found against it.
5. **The AAP 2016 recommendation text**, including the video-chat carve-out, confirmed only
   second-hand through a peer-reviewed review. Every AAP host returned 403.
6. **Marion & Thorley's pooled magnitude**, and **Colliver's internal argument against Springer et
   al.** Both closed, no OA copies. The same applies to the numeric values inside Blume et al.
   (2010) and Taylor et al. (2005), and to Sitzmann, Kraiger, Stewart & Wisher (2006) on web-based
   instruction, whose abstract the publisher has elided everywhere and which has no OA location.
7. **The ATD/ASTD level-3 and level-4 measurement percentages** that circulate in every corporate
   L&D deck. `td.org` returned HTTP 429 repeatedly, Wayback has no snapshot of the relevant pages,
   and ERIC indexes no ASTD report with level-by-level figures. Twitchell (1997/2000) is used
   instead because it has a DOI and a stated method.
8. **Age moderation of the testing and spacing effects.** Neither Rowland (2014) nor Cepeda et al.
   (2006) reports it. `OBSERVED — absence`. Since this corpus's `F11` architecture is built on
   spacing and retrieval and §3.2 shows adults differ measurably on speed and prior knowledge, the
   moderator that would tell us whether `F11`'s schedules transfer to a forty-year-old has not been
   estimated.
9. **Whether anyone has measured socially shared regulation at scale.** `OBSERVED — absence`: one
   narrative review of 13 mostly-qualitative papers, and controlled studies at `n = 66` and `n = 94`.
   No meta-analysis. The group analogue of `V5`'s entire premise has an evidence base smaller than
   one adequately powered trial.
10. **Any RCT of a coding bootcamp, or of online vocational training in a low-income country.**
    Not located; with WebSearch unavailable this is *not found*, not *does not exist*.

---

## 7. References

**Cooperative and collaborative learning**

1. Johnson, D. W., Johnson, R., Nelson, D., & Skon, L. (1981). *Psychological Bulletin*, 89(1), 47–62. `10.1037/0033-2909.89.1.47`. ERIC EJ254134. `MEASURED-META`
2. Roseth, C. J., Johnson, D. W., & Johnson, R. T. (2008). *Psychological Bulletin*, 134(2), 223–246. `10.1037/0033-2909.134.2.223`. 148 studies, 17,000+ adolescents. `MEASURED-META`
3. Johnson, D. W., Johnson, R. T., & Stanne, M. E. (2000). *Cooperative Learning Methods: A Meta-Analysis.* University of Minnesota. **Not indexed in ERIC; not retrieved.** `OBSERVED — absence`
4. Slavin, R. E. (1983). *Psychological Bulletin*, 94(3), 429–445. `10.1037/0033-2909.94.3.429`. `MEASURED-META`
5. Slavin, R. E. (1996). *Contemporary Educational Psychology*, 21(1). `10.1006/ceps.1996.0004`. ERIC EJ526831, with critical commentary by Abrami & Chambers. `MEASURED-META`
6. † Slavin, R. E. (2014). Cooperative learning and academic achievement: Why does groupwork work? *Anales de Psicología*, 30(3), 785–791. `10.6018/analesps.30.3.201201`. Open access; PDF extracted this session. `MEASURED-META`
7. † Kyndt, E., Raes, E., Lismont, B., Timmers, F., Cascallar, E., & Dochy, F. (2013). *Educational Research Review*, 10, 133–149. `10.1016/j.edurev.2013.02.002`. Abstract via UAntwerp `irua:107136`; **magnitudes untraceable**. `MEASURED-META`
8. Springer, L., Stanne, M. E., & Donovan, S. S. (1999). *RER*, 69(1), 21–51. `10.3102/00346543069001021`. 39 studies. `MEASURED-META`
9. Colliver, J. A., Feltovich, P. J., & Verhulst, S. J. (2003). *Teaching and Learning in Medicine*, 15(1). `10.1207/s15328015tlm1501_01`. ERIC EJ664775. `MEASURED-META` (critique)
10. † Adl-Amini, K., Völlinger, V. A., & Eckart, A. (2024). *European Journal of Psychology of Education*. ERIC EJ1439225. 49 classrooms. `OBSERVED`
11. † Bacon, D. R. (2005). *Journal of Management Education*, 29(2). `10.1177/1052562904263729`. `MEASURED-RCT` (null / negative)
12. Lou, Y., Abrami, P. C., Spence, J. C., Poulsen, C., Chambers, B., & d'Apollonia, S. (1996). *RER*, 66(4), 423–458. `10.3102/00346543066004423`. `MEASURED-META`
13. Öztürk, B. (2023). Second-order meta-analysis of cooperative learning models. *EPASR*. ERIC EJ1408689. 23 first-order meta-analyses. `MEASURED-META`
14. Nokes-Malach, T. J., Richey, J. E., & Gadgil, S. (2015). When is it better to learn together? *Educational Psychology Review*, 27. `10.1007/s10648-015-9312-8`. `MEASURED-META` (review)

**Active learning and peer instruction**

15. † Freeman, S., et al. (2014). *PNAS*, 111(23). `10.1073/pnas.1319030111`, PMID 24821756. 225 studies. `MEASURED-META`
16. Hake, R. R. (1998). *American Journal of Physics*, 66(1). `10.1119/1.18809`. `N = 6542`. `OBSERVED`
17. Crouch, C. H., & Mazur, E. (2001). *AJP*, 69(9). `10.1119/1.1374249`. `OBSERVED`
18. † Smith, M. K., Wood, W. B., Adams, W. K., Wieman, C., Knight, J. K., Guild, N., & Su, T. T. (2009). *Science*, 323(5910). `10.1126/science.1165919`. `MEASURED-RCT`
19. Chi, M. T. H., & Wylie, R. (2014). The ICAP framework. *Educational Psychologist*, 49(4). `10.1080/00461520.2014.965823`. `INFERENCE` (framework)

**CSCL**

20. † Vogel, F., Wecker, C., Kollar, I., & Fischer, F. (2017). *Educational Psychology Review*, 29. `10.1007/s10648-016-9361-7`. `MEASURED-META`
21. † Radkowitsch, A., Vogel, F., & Fischer, F. (2020). *ijCSCL*, 15. `10.1007/s11412-020-09316-4`. 53 studies, 5,616 learners. `MEASURED-META`
22. Jeong, H., Hmelo-Silver, C. E., & Jo, K. (2019). *Educational Research Review*, 28. `10.1016/j.edurev.2019.100284`. 316 outcomes / 143 studies. `MEASURED-META`
23. Chen, J., Wang, M., Kirschner, P. A., & Tsai, C.-C. (2018). *RER*, 88(6). `10.3102/0034654318791584`. 425 studies. `MEASURED-META`
24. Lou, Y., Abrami, P. C., & d'Apollonia, S. (2001). *RER*, 71(3). `10.3102/00346543071003449`. 122 studies, 11,317 learners. `MEASURED-META`
25. Janssen, J., & Kirschner, P. A. (2020). Collaborative cognitive load theory. *ETR&D*, 68. `10.1007/s11423-019-09729-5`. `INFERENCE` (framework)
26. Dillenbourg, P. (2002). Over-scripting CSCL. **Not retrieved** (HAL anti-bot challenge). Reported as unverified.

**Discourse, argumentation, shared regulation**

27. † Murphy, P. K., Wilkinson, I. A. G., Soter, A. O., Hennessey, M. N., & Alexander, J. F. (2009). *JEP*, 101(3). `10.1037/a0015576`. ERIC EJ861185. `MEASURED-META` (near-null)
28. Michaels, S., O'Connor, C., & Resnick, L. B. (2008). *Studies in Philosophy and Education*. ERIC EJ797081. `CRAFT`
29. Wolf, M. K., Crosson, A. C., & Resnick, L. B. (2006). CRESST TR 670. ERIC ED492865. 21 lessons. `OBSERVED`
30. Li, X., Wang, W., & Li, Y. (2022). *IJSE*. ERIC EJ1358804. Reports `g = 10.49 [7.27, 13.71]`; cited only as a methodological warning.
31. Koçoğlu, A., & Kanadlı, S. (2024). *Asia Pacific Education Review*. ERIC EJ1440274. `g = 0.927 [0.789, 1.064]`. `MEASURED-META`
32. Zhou, D. (2024). *Interactive Learning Environments*. ERIC EJ1449153. 46 studies, 5,415 students. `MEASURED-META`
33. † Panadero, E., & Järvelä, S. (2015). *European Psychologist*, 20(3). `10.1027/1016-9040/a000226`. 17 articles, 13 empirical. `MEASURED-META` (narrative)
34. Zheng, L., Li, X., & Huang, R. (2017). *ET&S*. ERIC EJ1157976. `n = 66`, randomised. `MEASURED-RCT`
35. Li, J., Liu, J., Yuan, R., & Shadiev, R. (2022). *ET&S*. ERIC EJ1336001. `n = 94`. `MEASURED-RCT`
36. Zheng, L., Niu, J., Long, M., & Fan, Y. (2023). *BJET*. ERIC EJ1372756. 63 groups / 189 students. `MEASURED-RCT`
37. Järvelä, S., Järvenoja, H., & Malmberg, J. (2019). *ijCSCL*. ERIC EJ1236539. `INFERENCE` (methods review)

**Collaborative memory**

38. † Marion, S. B., & Thorley, C. (2016). *Psychological Bulletin*, 142(11). `10.1037/bul0000071`, PMID 27618544. 75 ES / 64 studies. `MEASURED-META`
39. Weldon, M. S., & Bellinger, K. D. (1997). *JEP:LMC*, 23(5). `10.1037/0278-7393.23.5.1160`. `MEASURED-RCT`
40. Karau, S. J., & Williams, K. D. (1993). *JPSP*, 65(4). `10.1037/0022-3514.65.4.681`. **Pooled effect untraceable this session; not cited as evidence.**

**Video deficit and contingency**

41. † Strouse, G. A., & Samson, J. E. (2021). *Child Development*, 92(1). `10.1111/cdev.13429`. 122 ES / 59 reports. `MEASURED-META`
42. † Kuhl, P. K., Tsao, F.-M., & Liu, H.-M. (2003). *PNAS*, 100(15). `10.1073/pnas.1532872100`, PMID 12861072, PMC166444. `MEASURED-RCT`
43. DeLoache, J. S., et al. (2010). *Psychological Science*, 21(11). `10.1177/0956797610384145`. `MEASURED-RCT` (null)
44. † Roseberry, S., Hirsh-Pasek, K., & Golinkoff, R. M. (2014). *Child Development*, 85(3). `10.1111/cdev.12166`, PMID 24112079. `N = 36`. `MEASURED-RCT`
45. † Myers, L. J., LeWitt, R. B., Gallo, R. E., & Maselli, N. M. (2017). *Developmental Science*, 20(4). `10.1111/desc.12430`, PMID 27417537. `MEASURED-RCT`
46. Troseth, G. L., Saylor, M. M., & Archer, A. H. (2006). *Child Development*, 77(3). `10.1111/j.1467-8624.2006.00903.x`. `MEASURED-RCT`
47. † Troseth, G. L., Strouse, G. A., Verdine, B. N., & Saylor, M. M. (2018). *Frontiers in Psychology*, 9, 2195. `10.3389/fpsyg.2018.02195`, PMID 30483198. `n = 132`. `MEASURED-RCT` (non-replication)
48. † Strouse, G. A., Troseth, G. L., O'Doherty, K. D., & Saylor, M. M. (2018). *JECP*, 166. `10.1016/j.jecp.2017.09.005`. `n = 88`. `MEASURED-RCT`
49. Tsuji, S., Fiévét, A. C., & Cristia, A. (2021). *Infant Behavior and Development*, 63. `10.1016/j.infbeh.2021.101553`. `MEASURED-RCT`
50. † Mallawaarachchi, S., et al. (2024). *JAMA Pediatrics*, 178(10). `10.1001/jamapediatrics.2024.2620`. 100 studies, 176,742 participants. `MEASURED-META`
51. Glick, A. R., et al. (2022). *WIREs Cognitive Science*, 13(4). `10.1002/wcs.1599`. Cited only as second-hand confirmation of the AAP carve-out.
52. Moser, A., Zimmermann, L., Dickerson, K., Grenell, A., Barr, R., & Gerhardstein, P. (2015). *JECP*, 137. `10.1016/j.jecp.2015.04.002`. Touchscreen transfer deficit. `MEASURED-RCT`
53. Barr, R. (2010). *Developmental Review*, 30(2). `10.1016/j.dr.2010.03.001`. `INFERENCE` (review)

**Early numeracy, emergent literacy, preschool**

54. Clements, D. H., & Sarama, J. (2008). *AERJ*, 45(2). `10.3102/0002831207312908`. `MEASURED-RCT`
55. Clements, D. H., Sarama, J., Spitler, M. E., Lange, A. A., & Wolfe, C. B. (2011). *JRME*, 42(2). ERIC EJ918252. 1,375 preschoolers. `MEASURED-RCT`
56. Sarama, J., Clements, D. H., Wolfe, C. B., & Spitler, M. E. (2012). *JREE*, 5(2). `10.1080/19345747.2011.627980`. `MEASURED-RCT`
57. Clements, D. H., Sarama, J., Wolfe, C. B., & Spitler, M. E. (2013). *AERJ*, 50(4). `10.3102/0002831212469270`. `MEASURED-RCT`
58. Clements, D. H., Sarama, J., Farran, D., Lipsey, M., Hofer, K. G., & Bilbrey, C. (2011). SREE. ERIC ED518182. **Contradicts 56–57 on persistence.** `MEASURED-RCT`
59. Bailey, D. H., Duncan, G. J., Watts, T., Clements, D. H., & Sarama, J. (2018). *American Psychologist*, 73(1). `10.1037/amp0000146`. `MEASURED-META` / reanalysis
60. † Lipsey, M. W., Farran, D. C., & Durkin, K. (2018). *ECRQ*, 45. `10.1016/j.ecresq.2018.03.005`. `N = 2,990`. `MEASURED-RCT`
61. † Durkin, K., Lipsey, M. W., Farran, D. C., & Wiesen, S. E. (2022). *Developmental Psychology*, 58(3). `10.1037/dev0001301`. Negative through grade 6. `MEASURED-RCT`
62. Pion, G. M., & Lipsey, M. W. (2021). TN-VPK regression discontinuity, 155 classrooms / 5,189 children. *AERA Open*. ERIC EJ1323710. `OBSERVED`
63. Puma, M., et al. (2012). Third grade follow-up to the Head Start Impact Study. OPRE 2012-45. ERIC ED539263/ED539264. `n = 4,667`. `MEASURED-RCT`
64. † National Early Literacy Panel (2008). *Developing Early Literacy.* ERIC ED504224. `MEASURED-META`
65. Mol, S. E., Bus, A. G., de Jong, M. T., & Smeets, D. J. H. (2008). *Early Education and Development*, 19(1). `10.1080/10409280701838603`. `k = 9, n = 322, d = 0.59 [0.44, 0.75]`. `MEASURED-META`
66. Dowdall, N., et al. (2020). *Child Development*, 91(2). `10.1111/cdev.13225`. 19 RCTs, `N = 2,594`. `MEASURED-META`
67. † Noble, C., Sala, G., Peter, M., Lingwood, J., Rowland, C. F., Gobet, F., & Pine, J. (2019). *Educational Research Review*, 28. Preprint `10.31234/osf.io/cu7bk`. **`ḡ = 0.021, p = .783` with active controls.** `MEASURED-META` (null)
68. † Noble, C., et al. (2020). *JSLHR*, 63(6). `10.1044/2020_JSLHR-19-00288`. `n = 150`. `MEASURED-RCT` (null)
69. Dowdall, N., Murray, L., Skeen, S., et al. (2021). Book-sharing RCT, South Africa. *Child Development*, 92(6). `10.1111/cdev.13619`. `n = 140`, wait-list control. `MEASURED-RCT`
70. Griffith, S. F., Hagan, M. B., Heymann, P., Heflin, B. H., & Bagner, D. M. (2020). Apps as learning tools: A systematic review. *Pediatrics*, 145(1). `10.1542/peds.2019-1579`. 35 studies. `MEASURED-META` (narrative)
71. Kearney, M. S., & Levine, P. B. (2019). *AEJ: Applied*, 11(1). `10.1257/app.20170300`. `OBSERVED`; point estimates not verified.
72. † Xu, Y., Aubele, J., Vigil, V., Bustamante, A. S., Kim, Y.-S., & Warschauer, M. (2022). *Child Development*, 93(2). `10.1111/cdev.13708`, PMC9299009. `n = 117`. `MEASURED-RCT`
73. WHO (2019). *Guidelines on physical activity, sedentary behaviour and sleep for children under 5 years of age.* ISBN 978-92-4-155053-6. Quoted from the WHO release; guideline PDF not retrieved.
74. AAP Council on Communications and Media (2016). Media and young minds. *Pediatrics*, 138(5). `10.1542/peds.2016-2591`. **Recommendation text not retrieved (403 from every AAP host).**

**Adults**

75. † Rachal, J. R. (1994). Andragogical and pedagogical methods compared. ERIC ED380566. 18 studies. `MEASURED-META` (null)
76. Rachal, J. R. (2002). Andragogy's detectives. *Adult Education Quarterly*, 52(3). `10.1177/0741713602052003004`. ERIC EJ644442. `MEASURED-META` (review)
77. † Bradley, J. B., Jr. (2010). Andragogical vs pedagogical online modules for non-profit professionals. ERIC ED517783. `n = 52` randomised, 33 analysed. `MEASURED-RCT` (null)
78. Holton, E. F., III, Wilson, L. S., & Bates, R. A. (2009). Toward development of a generalized instrument to measure andragogy. *HRDQ*, 20(2). ERIC EJ848487. `OBSERVED`
79. Taylor, B., & Kroth, M. (2009). *Journal of Adult Education*, 38(1). ERIC EJ891073. **Titled a meta-analysis; is a narrative review. Not quantitative evidence.**
80. Davenport, J., III (1987). A way out of the andragogy morass. ERIC ED283989. `INFERENCE` (critique)
81. † Sitzmann, T., & Ely, K. (2011). A meta-analysis of self-regulated learning in work-related training and educational attainment. *Psychological Bulletin*, 137(3). `10.1037/a0022777`, PMID 21401218. `k = 430`, `N = 90,380`. `MEASURED-META`
82. † Salthouse, T. A. (2009). When does age-related cognitive decline begin? *Neurobiology of Aging*, 30(4). `10.1016/j.neurobiolaging.2008.09.023`, PMC2683339. `N = 2,350`. `OBSERVED` — with Schaie's published reply, PMID 19231029
83. Verhaeghen, P., & Salthouse, T. A. (1997). *Psychological Bulletin*, 122(3). PMID 9354147. `k = 91`. `MEASURED-META`
84. † Verhaeghen, P. (2003). Aging and vocabulary scores: A meta-analysis. *Psychology and Aging*, 18(2). PMID 12825780. 324 comparisons across 210 articles; **+0.80 SD favouring older adults**. `MEASURED-META`
85. † Kubeck, J. E., Delp, N. D., Haslett, T. K., & McDaniel, M. A. (1996). Does job-related training performance decline with age? *Psychology and Aging*, 11(1). PMID 8726375. `k = 83`, `N = 6,610`. `MEASURED-META`
86. † Beier, M. E., & Ackerman, P. L. (2005). Age, ability, and the role of prior knowledge on the acquisition of new domain knowledge. *Psychology and Aging*, 20(2). PMID 16029097. `n = 199`, ages 19–68. `OBSERVED`
87. Hartshorne, J. K., & Germine, L. T. (2015). *Psychological Science*, 26(4). `10.1177/0956797614567339`. `n = 48,537`. `OBSERVED`
88. † Arthur, W., Jr., Bennett, W., Jr., Edens, P. S., & Bell, S. T. (2003). *JAP*, 88(2). `10.1037/0021-9010.88.2.234`, PMID 12731707. `MEASURED-META`
89. † Taylor, P. J., Russ-Eft, D. F., & Chan, D. W. (2005). *JAP*, 90(4). `10.1037/0021-9010.90.4.692`, PMID 16060787. 117 studies. `MEASURED-META`; numeric `d` values not retrievable
90. Blume, B. D., Ford, J. K., Baldwin, T. T., & Huang, J. L. (2010). *Journal of Management*, 36(4). `10.1177/0149206309352880`. 89 studies. `MEASURED-META`; correlations not retrievable
91. Lacerenza, C. N., Reyes, D. L., Marlow, S. L., Joseph, D. L., & Salas, E. (2017). Leadership training design, delivery, and implementation. *JAP*, 102(12). `10.1037/apl0000241`, PMID 28749153. `k = 335`. `MEASURED-META`
92. † Twitchell, S. (1997). *Technical Training Program Evaluation: Present Practices in United States' Business and Industry.* LSU dissertation, `10.31390/gradschool_disstheses.6552`; published as Twitchell, Holton & Trott (2000), *PIQ*, 13(3), `10.1111/j.1937-8327.2000.tb00177.x`. `n = 146`. `OBSERVED`
93. Georgenson, D. (1982). The problem of transfer calls for partnership. *Training and Development Journal*, 36(10). **Absent from Crossref, OpenAlex and ERIC; the "10% transfers" figure is not cited.**
94. Fitzpatrick, R. (2001). The strange case of the transfer of training estimate. *TIP*, 39(2). `10.1037/e576912011-002`. **Existence verified in Crossref and OpenAlex; full text not retrieved.**
95. † Torgerson, C. J., Porthouse, J., & Brooks, G. (2003). *Journal of Research in Reading*, 26(3). `10.1111/1467-9817.00200`. Nine RCTs worldwide, 1980–2002; publication bias present. `MEASURED-META`
96. † Torgerson, C., Porthouse, J., & Brooks, G. (2005). *Journal of Research in Reading*, 28(2). `10.1111/j.1467-9817.2005.00256.x`. ERIC EJ718454. 27 CTs, 9 usable. `MEASURED-META`
97. † Brooks, G., Burton, M., Cole, P., Miles, J., Torgerson, C., & Torgerson, D. (2008). *Oxford Review of Education*, 34(4). `10.1080/03054980701768741`. ERIC EJ810523. 28 clusters. `MEASURED-RCT` (null / backfire)
98. † Ainsworth, H., et al. (2012). *Educational Studies*. ERIC EJ959747. Two RCTs. `MEASURED-RCT` (null / negative)
99. † Ricciuti, A. E., St.Pierre, R. G., Lee, W., Parsad, A., & Rimdzius, T. (2004). *Third National Even Start Evaluation.* NCEE/IES. ERIC ED484058. 463 families randomised. `MEASURED-RCT` (null)
100. What Works Clearinghouse (2020). *Integrated Basic Education and Skills Training (I-BEST).* WWC 2020-012. 12 studies, 3 meeting standards. `MEASURED-META`
101. NCES (2019). *Adult Literacy in the United States.* NCES 2019-179. ERIC ED596118. PIAAC Cycle 1. `FILING`
102. † NCES (2024). *Highlights of the 2023 U.S. PIAAC Results.* Cycle 2. Level 1 or below rose 19→28% literacy, 29→34% numeracy, 2017–2023. `FILING`
103. † OECD (2024). *Do Adults Have the Skills They Need to Thrive in a Changing World? Survey of Adult Skills 2023.* `10.1787/b263dc5d-en`. ~160,000 adults, 31 countries. `FILING`
104. OCTAE, *National Reporting System for Adult Education*, PY2022–23 Data Highlights. 1,120,769 participants; 43% measurable skill gain; 15,320 postsecondary credentials. `FILING`
105. † Card, D., Kluve, J., & Weber, A. (2018). *JEEA*, 16(3). `10.1093/jeea/jvx028`; IZA DP 9236. **207 studies, 857 estimates.** `MEASURED-META`
106. † Fortson, K., Rotz, D., Burkander, P., Mastri, A., Schochet, P., Rosenberg, L., & McConnell, S. (2017). *Providing Public Workforce Services to Job Seekers: 30-Month Impact Findings on the WIA Adult and Dislocated Worker Programs.* Mathematica for U.S. DOL. 28 local areas, `n > 34,000`. `MEASURED-RCT` (null on training)
107. McConnell, S., Schochet, P. Z., Rotz, D., Fortson, K., Burkander, P., & Mastri, A. (2021). *JPAM*, 40(4). `10.1002/pam.22305`. The counselling arm of the same trial, published. `MEASURED-RCT`
108. † Schochet, P. Z., D'Amico, R., Berk, J., Dolfin, S., & Wozny, N. (2012). *Estimated Impacts for Participants in the Trade Adjustment Assistance Program.* SPR & Mathematica for U.S. DOL. `OBSERVED` — matched comparison, not an RCT
109. Schochet, P. Z., Burghardt, J., & McConnell, S. (2008). Does Job Corps work? *AER*, 98(5). `10.1257/aer.98.5.1864`. `n = 15,400`. `MEASURED-RCT`
110. † Fein, D., & Hamadyk, J. (2018). *Bridging the Opportunity Divide for Low-Income Youth: Year Up.* OPRE 2018-65. ERIC ED615553. `n = 2,544`. `MEASURED-RCT`
111. † MDRC WorkAdvance sequence: Hendra et al. (2016), two years; Kanengiser & Schaberg (2022), seven years; Yusim, Schaberg, Tessler & Ubalijoro (2025), ten years. `n = 2,564`. `MEASURED-RCT`
112. † Means, B., Toyama, Y., Murphy, R., Bakia, M., & Jones, K. (2009). *Evaluation of Evidence-Based Practices in Online Learning.* U.S. Dept of Education. ERIC ED505824. `k = 50`, 43 with older learners. `MEASURED-META`
113. † Cook, D. A., Levinson, A. J., Garside, S., Dupras, D. M., Erwin, P. J., & Montori, V. M. (2008). Internet-based learning in the health professions. *JAMA*, 300(10). PMID 18780847. `k = 201`. `MEASURED-META`
114. † Xu, D., & Jaggars, S. S. (2013/2014). Adaptability to online learning. CCRC WP 54 / *Journal of Higher Education*, 85(5). `10.1080/00221546.2014.11777343`. ~500,000 courses, ~40,000 students. `OBSERVED`
115. Figlio, D. N., Rush, M., & Yin, L. (2013). *Journal of Labor Economics*, 31(4). `10.1086/669930`. `MEASURED-RCT`
116. Joyce, T. J., Crockett, S., Jaeger, D. A., Altindag, O., & O'Connell, S. D. (2015). Does classroom time matter? *Economics of Education Review*, 46. `n = 725`. `MEASURED-RCT`
117. Bowen, W. G., Chingos, M. M., Lack, K. A., & Nygren, T. I. (2014). *JPAM*, 33(1). `10.1002/pam.21728`. `n = 605`, six campuses. `MEASURED-RCT`
118. † Reich, J., & Ruipérez-Valiente, J. A. (2019). The MOOC pivot. *Science*, 363(6423). `10.1126/science.aav7958`. `OBSERVED`
119. Grow with Google, certificates page (retrieved 30 July 2026). *"Based on program graduate survey, United States 2025."* `VENDOR` — never restated as a finding.
120. Kyndt, E., & Beinicke, A. (2020). Evidence-based actions for maximising training effectiveness in corporate e-learning and classroom training. *Studies in Continuing Education*. ERIC EJ1262820. `OBSERVED` (survey)

**Carried from the corpus, not re-derived:** `I1`'s mechanism-survival test and its scoring of
"genuine peers with real stakes"; `I2` §2.6 on chavruta's symmetry under substitution and §9.4 on
AI-brokered human pairing; `F2` §4.1–4.3 on peer instruction and jigsaw as AI roles; the standing
corrections `g = 0.56` (human learning-by-teaching) and `g = 0.43` (peer tutoring's tutor gain);
`J1`'s expertise-reversal law; `F6` on attrition; `F4` on reach economics; `V5` on supplying the
executive; `V3` on the EEF toolkit's collaborative-learning entry, which the toolkit's Cloudflare
block prevented me from re-verifying this session.

† = primary source retrieved verbatim this session.
