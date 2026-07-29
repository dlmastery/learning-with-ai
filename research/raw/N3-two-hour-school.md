---
title: "The Two-Hour School, Graded: Alpha School, 2 Hour Learning, and what a percentile claim is actually worth"
wave: N
section: N3
date_researched: 2026-07-29
sources_count: 118
status: raw-research
---

# N3 — The Two-Hour School

> **Why this section exists.** §30 of this survey argues that most of a learning week is
> overhead, that acquisition compresses by 10–40× on elapsed calendar and 3–5× on engaged
> effort, and that learning is counted in *opportunities, not days*. Alpha School and its
> operating programme **2 Hour Learning** claim to have built exactly that: academics
> finished in two hours a day, students in the top 1–2% nationally, no academic teachers.
> **This is the closest thing in existence to a live test of our own argument — which is
> precisely why it is the section most likely to make us credulous.**
>
> **The finding, stated first.** Two hours of academics is almost certainly real and is
> *less impressive than it sounds*: measured in **academic learning time** rather than
> clock time, two hours of high-engagement, high-success-rate software work is
> approximately **parity** with what a median conventional classroom already delivers in
> six hours. The compression is of overhead, exactly as §30 predicts, and it is a
> ~1× result on the quantity that matters, not a 3× one.
>
> The **percentile and multiplier claims are a different matter and do not survive contact
> with the primary norms document they cite.** Working only from 2 Hour Learning's own
> white paper and NWEA's published *2020 MAP Growth Achievement Status and Growth Norms*,
> two arithmetic facts are checkable and were checked:
>
> 1. The white paper's worked example of how "2x" is measured uses, as its denominator,
>    **the RIT gap between adjacent grade levels at a fixed achievement percentile** — not
>    the observed growth of a student at that percentile. Under that denominator a
>    **nationally average grade-5 mathematics student is scored as learning 2.4×**, and an
>    average grade-8 mathematics student is scored as learning **infinitely** fast, because
>    the denominator is zero.
> 2. The white paper states that "a 50th percentile 5th grader typically goes up 4 points in
>    math over a year." NWEA's published growth norm for that exact cell is **9.61 RIT**
>    (fall→spring), 8.32 (spring→spring), or 5.47 (fall→fall). The "8 points" the paper
>    attributes to an Alpha student at that cell corresponds to roughly the **40th
>    conditional growth percentile** — *below* the national median growth — while being
>    presented as double it.
>
> And a third, on attainment rather than growth: the claim is stated at **class** level
> ("our classes score in the top 1–2%"). NWEA norms the *school/grade* mean separately from
> the student. Computed from the published tables, the **99th school percentile equals
> approximately the 90th student percentile in mathematics and the 84th–87th in reading**,
> uniformly across every grade K–12. A "top 1% class" and a class of "top 1% students" are
> not the same object, and the published claim does not say which is meant.
>
> **And there is one number the operator produced under conditions that reward candour.**
> When the same programme applied for a Pennsylvania cyber charter, its application projected
> that in year two the school would rank **in the top half of all Pennsylvania schools**. The
> same programme is sold to fee-paying parents as producing classes **"in the top 1–2%
> nationally"**. Five states received applications; **four refused**, and the Pennsylvania
> Department of Education found *"deficiencies in all five of the required criteria"* and
> called the model **"untested"**. In the version written for a regulator, the "guides"
> become **certificated teachers at a 1:20 ratio — more adults per student than a typical
> school**.
>
> Since then: **IXL Learning deactivated Alpha's account in July 2025** for "violating our
> terms of service" — so the platform stack that produced the published results is not the
> one now running; **New York State declined to recognise the $65,000 Manhattan campus as a
> school at all**; and the group's entire corporate structure files nothing — no Form 990, no
> Form D, no SEC filing of any kind.
>
> **None of this shows the school does not work.** It shows that *nobody, including the
> operator, has produced a measurement capable of showing whether it works.* There is no
> peer-reviewed evaluation, no state accountability data, no external administration of the
> assessment, no control group, and no delayed unassisted outcome. The school is private,
> selective, tuition-gated at **$10,000–$75,000**, and requires a MAP exam and prior school
> records before enrolment. **Selection alone would produce most of the observed attainment
> under almost any instructional model, and this is unresolvable without a control group.**

**Retrieval note.** WebSearch was exhausted before this section began (CLAUDE.md §5).
Everything below came from `curl` and `WebFetch` against the operators' own domains
(`alpha.school`, `2hourlearning.com`, `gt.school`, `timeback.com`, `unbound.school`), the
2 Hour Learning white paper PDF retrieved from its flipbook CDN, **NWEA's 2020 norms
technical report retrieved in full and parsed programmatically**, Crossref, OpenAlex,
Semantic Scholar, ERIC, NBER, RAND, Cognia's own WordPress REST API, and the GDELT news
API. Unreachable sources are listed in §11 with status codes and are never guessed around.

**Evidence labels.** Project standard — `MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH`
· `OBSERVED` · `VENDOR` · `DEMO` · `INFERENCE` — plus, newly available for this wave:

- **`DESIGN`** — a proposed study or mechanism, stated together with **what result would
  show it wrong**. A `DESIGN` with no falsifier is not a `DESIGN`.
- **`OPEN`** — a question nobody has asked, stated together with **why** nobody asked it.
- **`UNVERIFIABLE`** — a claim that cannot be checked from outside, with the reason given.
- **`RECOMPUTED`** — a quantity *this section* calculated from a published primary table,
  with the table, the rows, and the arithmetic given so the calculation can be redone or
  refuted. `RECOMPUTED` is the only label under which a number here outranks the vendor's.

**The rule this section is most at risk of breaking.** A `VENDOR` claim may never be
restated as a finding. Every outcome number the operator reports about its own students,
on tests it administers, is `VENDOR` — including the ones that are probably true. Where
this section states a finding about Alpha's results, the finding is about the *structure
of the claim*, never the number.

---

## 0. The findings

| # | Finding | Label |
|---|---|---|
| **0** | **The operator's own forecast to a regulator is "top half", not "top 1%".** The Pennsylvania cyber-charter application projected that in year two the school would rank **in the top half of all Pennsylvania schools** (Chalkbeat, reading the application). The same programme is marketed to fee-paying parents as producing classes "in the top 1–2% nationally". **The gap between those two numbers is the operator's own estimate of how much of its claim survives an unselected intake.** | `OBSERVED` |
| **0b** | **Six states received cyber-charter applications; one approval is on record.** Utah, Arkansas and North Carolina rejected; Pennsylvania denied; Arizona approved. The Pennsylvania Department of Education found **"deficiencies in all five of the required criteria"** and described the instructional model as **"untested"**. | `OBSERVED` (regulator) |
| **0c** | **In the regulated version, the teachers come back.** The Arizona application specifies certificated teachers as the minimum qualification for "guides" and a **guide-to-student ratio of 1:20 against 1:30 in typical schools** — i.e. *more* certificated adults per student than a conventional school, in a programme marketed as having replaced teachers with AI. | `OBSERVED` |
| **0d** | **A supplier terminated the account.** IXL Learning told WIRED that **Alpha School's account was deactivated in July 2025** and that Alpha is *"no longer an IXL customer due to violating our terms of service"*, adding that IXL "is not intended… as a replacement" for "trained, caring teachers." IXL is one of the three named third-party platforms in the charter applications. **The system that produced the published results is not the system now in operation.** | `OBSERVED` (vendor statement) |
| **0e** | **A second regulator refused the model.** NYSED declined Alpha's application to incorporate as an independent school, writing that instruction is *"primarily online… with little to no supervision or competent teacher delivering such instruction."* The $65,000 New York campus operates as a homeschool co-op; families file as homeschoolers. | `OBSERVED` (regulator) |
| **0f** | **Where an outsider got a denominator, it was five.** A sympathetic insider review found the affiliated GT School's "5× faster" claim rested on **five children** who sat both the fall and winter tests. No published multiplier from this group carries an N. | `OBSERVED` |
| 1 | **"Two hours" means two hours of *academics*, not a two-hour school day.** The day runs 8:15 am–4:00 pm. The remaining ~4 hours are "life skills workshops". The operator states this plainly in its own FAQ; the ambiguity is created by third-party retelling, not by the school. | `VENDOR` (verbatim) |
| 2 | **Two hours of academic learning time is roughly parity with a conventional day, not a 3× compression.** BTES's cascade puts academic learning time at ~35% of allocated time in the median classroom; a 3.5–5 hour academic allocation therefore yields ~1.2–1.75 h. Alpha's two hours are engineered for high engagement and a 70–95% success band. The *clock* compresses ~3×; the *learning time* does not. | `INFERENCE` on `OBSERVED` (Fisher et al. 1980) |
| 3 | **The "2x" multiplier's denominator is the adjacent-grade RIT gap at fixed percentile, not observed growth.** Verified against the white paper's own two worked examples, both of which reproduce exactly from NWEA's Spring achievement tables. | `RECOMPUTED` |
| 4 | **Under that denominator, a nationally average student scores 1.2×–2.4× in mathematics and 1.0×–1.7× in reading, and is undefined at grade 8.** Table in §2.3. | `RECOMPUTED` |
| 5 | **The white paper's stated national norm (4 RIT/year, grade-5 math, p50) is wrong under every definition NWEA publishes** (9.61 fall→spring; 8.32 spring→spring; 5.47 fall→fall). | `RECOMPUTED` |
| 6 | **The 99th *school* percentile ≈ the 90th *student* percentile in maths, 84th–87th in reading, at every grade.** The class-level "top 1%" claim is compatible with an average student around the 85th–90th percentile. | `RECOMPUTED` |
| 7 | **There is no independent measurement of any kind.** No peer-reviewed evaluation; the only two academic items naming Alpha School are non-peer-reviewed preprints. No state accountability data, because the schools are private. No external test administration. No control group. | `OBSERVED` |
| 7b | **One exception is arriving.** **Unbound Academy** — listed by 2 Hour Learning as one of its schools — is an Arizona **tuition-free public virtual charter** for grades 4–8, opening 3 Aug. Public charters report state assessment results and A–F grades. It is also the variant that advertises *"certified teachers live on screen"*, which the flagship explicitly does not have. | `OBSERVED` |
| 8 | **Selection is documented by the operator itself**: $100 application fee, information session, shadow day, prior school records, a MAP exam reviewed at enrolment, a $1,000 non-refundable deposit, tuition $10k–$75k, and an explicit statement that "parental alignment" is a precondition and that the model "works for 80–90% of children". | `VENDOR` (verbatim) |
| 9 | **The operator's own numbers are internally inconsistent.** The same site reports the top-20% cohort as **6.5×** (home page) and **3.9×** (results page); the white paper says "nearly 4x". `timeback.com` metadata advertises "10x faster learning gains". | `OBSERVED` |
| 10 | **Mechanically, this is the Personalized System of Instruction with software.** Mastery criterion, self-pacing, unit-by-unit gating, proctors reassigned to motivation. PSI has real evidence — and a real ceiling. That is the correct prior, and it predicts a genuine but modest effect, not a top-1% one. | `INFERENCE` on `MEASURED-META` |

---

## 1. What is claimed, precisely, and by whom

### 1.1 The entities

| Entity | What it is | Source |
|---|---|---|
| **Alpha School** | Private PreK–12 school network. Flagship campus Austin, TX, opened 2014 ("now in year 11", "more than 150 students"). The site's own location menu lists **44 campus entries across 16 states, DC and Puerto Rico**; many are marked "launching soon" and enrolment is not stated for most. | `alpha.school` (HTTP 200) |
| **2 Hour Learning** | The instructional programme/company. Site lists schools: Alpha School, Alpha High, Alpha Anywhere, Texas Sports Academy, GT School, NextGen Academy, Nova Academy, Prequel, **Unbound Academy**, The Novatio School, learn+earn. | `2hourlearning.com` (HTTP 200) |
| **Timeback** | The platform brand. `timeback.com` metadata: *"Revolutionary AI-powered EducationOS helping children master academics in just 2 hours per day. Personalized learning with 10x faster gains. Join the waitlist for 2026 launch."* `timeback.app` renders only "Launching Soon". | `timeback.com` (HTTP 200), `timeback.app` (HTTP 200) |
| **Unbound Academy** | **Arizona tuition-free public virtual charter, grades 4–8**, school year starting 3 Aug. *"Certified teachers live on screen"*; *"2.8× faster learning, measured by NWEA MAP Growth"*. The only public-sector, publicly-reporting entity in the group. | `unbound.school` (HTTP 200) |
| **GT School** | Sibling K–8 school for gifted students, same model. *"1400+ SAT. AP 5s. 3X learning velocity."*; *"Our students outperform 91% of students nationally"*; *"Median MAP growth at 3X velocity"*. | `gt.school` (HTTP 200) |
| **Founders** | MacKenzie Price (co-founder, "innovated by"); Joe Liemandt (Trilogy/ESW Capital). Alpha's own podcast page titles Liemandt "Alpha School Principal". | `alpha.school`, `2hourlearning.com` |

### 1.2 The claims, verbatim

**On the day (this one is stated accurately by the operator and mis-stated by everyone else):**

> **"Are kids only in school for 2 hours?** No. Students attend a full school day, similar
> to a traditional school schedule. The difference is that core academics are completed in
> about two hours using personalized, mastery-based learning software."
> — Alpha School FAQ `VENDOR`

> "The daily schedule at Alpha runs from 8:15 AM to 4:00 PM." — Alpha Austin FAQ `VENDOR`

> "**Afternoon: Life Skills to Pursue Passions and Interests.** These four hours are packed
> with sports, arts, entrepreneurship — you name it!" — 2hourlearning.com `VENDOR`

**On results:**

> "Our classes score in the top 1-2% nationally across the board."
> — 2hourlearning.com, results page `VENDOR`

> "**2x faster** — Students learn at least 2x faster than their peers in traditional school.
> **6.5x growth** — The top 20% of students show 6.5x growth. **Top 1-2% nationally** — Our
> classes score in the the top 1-2% nationally across the board.
> *Based on data collected from our flagship campus, Alpha School.*"
> — 2hourlearning.com home page `VENDOR`

> "Spring '23 and Fall '24: Top 20% of students — **3.9x**. Spring '23 and Fall '24: Top
> 2/3rd — **2.6x**. Spring '23 and Fall '24: All students — **2.2x**. *Based on the MAP
> Spring '23 and Fall '24 results at Alpha School*"
> — 2hourlearning.com results page, counter widget values read from the DOM `VENDOR`

> "Results have consistently shown that Alpha students perform in the top 1–2% nationally
> and frequently progress academically twice as fast as the national average."
> — Alpha School FAQ `VENDOR`

> "every Alpha middle school student ranks in the top 5%" · "By year-end, almost all
> kindergartners were in the top 1% of MAP scores" · "an overall average SAT score of
> 1470+" · "Alpha Honors (with morning sessions yielding SAT scores of 1550+ and multiple
> AP 5's)" — 2hourlearning.com results page `VENDOR`

**On the mastery criterion:**

> "Students achieve 90% mastery in each concept before they move on." — Alpha FAQ `VENDOR`

> "To finish a grade level, students must score 90% on these tests, a mastery standard far
> higher than state or standard school requirements." — white paper, on state tests (STAAR
> in Texas, FAST in Florida) used *internally* as grade-completion exams `VENDOR`

**On suitability — the operator's own limiting conditions, which are more candid than the
marketing and deserve to be quoted at length:**

> "**Not Just EdTech:** This model isn't a mere magic software solution. It is a
> comprehensive system in which student motivation is the key to 90% of success.
> **Suitability:** While 2 Hour Learning works for 80-90% of children, it may not be
> suitable for everyone." — white paper, "Key Disclaimers" `VENDOR`

> "**Parental Alignment:** The most challenging aspect to overcome is when parents are not
> philosophically aligned with the 2 Hour Learning model." — white paper `VENDOR`

> "while it is presented as a polished model, it remains an evolving system … parents
> should expect excellent outcomes, not perfection." — white paper `VENDOR`

### 1.3 The claim-escalation ladder

The same organisation's own properties carry, simultaneously:

| Claim | Where | Cohort |
|---|---|---|
| "at least 2x" | 2hourlearning.com, white paper | all students |
| **2.2x** | results page counter | all students, Spring '23 + Fall '24 |
| 2.6x | results page counter | top 2/3 |
| **3.9x** | results page counter | top 20% |
| "nearly 4x" | white paper | top 20% |
| **6.5x** | 2hourlearning.com **home page** | top 20% |
| "3X learning velocity" | gt.school | GT School students |
| **"10x faster gains"** | timeback.com `<meta>` description | unspecified |
| "4.6x" | white paper | 7 named boys, 6 months |

And the same organisation's claim culture beyond the school itself. **Prequel**
(`joinprequel.com`, HTTP 200), listed by 2 Hour Learning among its schools:

> "**Go from a 4% to a 75% chance of acceptance to the Ivy League.** How? By putting
> yourself in the top 1% of real-world achievement." · "If you have an outstanding academic
> record and a world-class extracurricular, **your chances jump to 90%**." · "Reaching the
> top 1% in your field—and a **75% chance at Ivy League acceptance**—takes long-term
> commitment." `VENDOR`, `UNVERIFIABLE`

These are quantified causal claims about admissions probability, published without a
population, a denominator, a comparison, or a source. They cannot be checked and are not
checked here. They are recorded because **the standard of evidence an organisation applies
to its least checkable claim is information about the standard it applies to its most
checkable one.**

`OBSERVED`. The 3.9× and 6.5× figures describe the same cohort on the same website. No
methodology note reconciles them. **A number that moves by 67% between two pages of the
same site is not a measurement; it is a marketing parameter.** This is the cleanest
available evidence that these figures are not being produced by a stable analytic pipeline.

---

## 2. The instrument: what a MAP percentile is, and what these ones are

This is the load-bearing section. Everything the operator publishes about outcomes rests on
**NWEA MAP Growth**, administered by the school, three times a year. So: what is it, and
what do the specific claims mean against the primary norming document?

The primary document is **Thum, Y. M., & Kuhfeld, M. (2020), *NWEA 2020 MAP Growth
Achievement Status and Growth Norms for Students and Schools*, NWEA Research Report** —
retrieved in full (HTTP 200, 4.45 MB) and parsed programmatically for this section. Its
norming sample is test records from **Fall 2015 through Spring 2018**, over **11 million
unique students** in reading and mathematics.

### 2.1 First, a point in Alpha's favour

The reference population is **pre-pandemic**. Any school benchmarking 2023–24 performance
against 2020 norms is being scored against a *stronger* comparison population than the one
actually sitting in American classrooms in 2024. That is the conservative choice, and it
cuts in the school's favour. It should be said before anything else, because the rest of
this section does not.

### 2.2 The "2x" arithmetic, reconstructed

The white paper gives the only worked example of the method anywhere in the corpus of
operator materials:

> "As mentioned, MAP is the third-party grader, measuring how much students learn each
> year. At Alpha, these scores are always doubled. For example, looking at the NWEA MAP
> Math Student Achievement Percentiles for 2020 below, **a 50th percentile 5th grader
> typically goes up 4 points in math over a year. At Alpha, that student will go up 8
> points.** Similarly, **a 99th percentile 7th grader goes up 7 points in traditional
> settings but 14 points at Alpha.**" `VENDOR`

Both "traditional" figures reproduce exactly — from the **Spring Mathematics Student
Achievement Percentiles** table (Table C.1.3), reading *across grades at a fixed
percentile*:

| Cell | Spring RIT, grade *g* | Spring RIT, grade *g+1* | Difference |
|---|---|---|---|
| Math, p50, grade 5 → 6 | 219 | 223 | **4** |
| Math, p99, grade 7 → 8 | 270 | 277 | **7** |

`RECOMPUTED`. The denominator is therefore identified beyond reasonable doubt: it is **the
RIT gap between adjacent grade levels at a fixed achievement percentile** — a
*cross-sectional* quantity, describing how much more a same-ranked student one grade up
knows. It is not, and is not equal to, **the growth a real student at that percentile makes
over a school year**, which NWEA publishes separately and prominently.

Here is that quantity, from the same document, Appendix E (Conditional Growth
Distributions), Table E.1.37, Mathematics Grade 5, Fall→Spring, start status = 50th
achievement percentile (start RIT 209.13):

| Growth interval | NWEA mean growth, grade-5 math, p50 start |
|---|---|
| **Fall → Spring** | **9.61 RIT** (SD 6.53) |
| Spring → Spring | 8.32 RIT |
| Fall → next Fall | 5.47 RIT |

`RECOMPUTED`. **Under every definition of "a year" that NWEA publishes, the norm is not
4 points.** The closest is fall-to-fall at 5.47, and that interval includes summer loss
(NWEA's spring→fall norm for this cell is **−1.29** RIT).

And the consequence for the numerator. The white paper says the Alpha student at that cell
"will go up 8 points". From the same table, the conditional growth percentiles for a
grade-5 mathematics student starting at p50 are:

| CGP 20 | CGP 30 | CGP 40 | CGP 45 | **CGP 50** | CGP 55 | CGP 60 | CGP 70 | CGP 80 |
|---|---|---|---|---|---|---|---|---|
| 4.12 | 6.19 | 7.96 | 8.79 | **9.61** | 10.43 | 11.27 | 13.04 | 15.11 |

**8.0 RIT sits at roughly the 40th conditional growth percentile.** `RECOMPUTED`. Taken
entirely at face value, the white paper's own headline example describes a student growing
**below the national median rate** and labels it "2x".

Two honest caveats, because this finding is severe enough to deserve them:

1. The "grade levels per year" framing is not nonsense. If one "grade level" of content at
   a given rank is 4 RIT, then 8 RIT is two grade levels of content, and the school is
   entitled to say a student covered two grades of curriculum. What it is *not* entitled to
   say is that this is twice the rate at which other students learn — that is a different
   sentence about a different denominator, and it is the sentence the marketing makes.
2. The size of the distortion **varies by cell and is not always large**. At grade 7, p99,
   the adjacent-grade gap (7) happens to nearly equal NWEA's growth norm for a
   high-starting grade-7 student (6.68 RIT at start-status p90). At that cell the
   white paper's arithmetic is approximately fair, and its claimed 14 RIT would be a
   genuinely exceptional result — beyond CGP 80. **The method is not uniformly inflationary;
   it is uniformly *uninterpretable*, because the multiplier it produces depends on where in
   the grid you stand.**

### 2.3 How fast does a perfectly average student "learn", scored this way?

The test of a metric is what it reports for a known input. Feeding the **national average**
into the white paper's method — NWEA's own mean fall→spring growth at p50 start, divided by
NWEA's own adjacent-grade spring RIT gap at p50:

| Grade | **Mathematics**: growth / gap = "x" | **Reading**: growth / gap = "x" |
|---|---|---|
| K | 17.54 / 19 = **0.92×** | 16.45 / 18 = **0.91×** |
| 1 | 16.35 / 13 = **1.26×** | 15.47 / 15 = **1.03×** |
| 2 | 14.38 / 12 = **1.20×** | 13.22 / 11 = **1.20×** |
| 3 | 12.60 / 10 = **1.26×** | 10.50 / 8 = **1.31×** |
| 4 | 10.96 / 8 = **1.37×** | 8.16 / 6 = **1.36×** |
| 5 | 9.61 / 4 = **2.40×** | 6.50 / 4 = **1.62×** |
| 6 | 8.13 / 4 = **2.03×** | 5.19 / 3 = **1.73×** |
| 7 | 6.52 / 3 = **2.17×** | 4.16 / 4 = **1.04×** |
| 8 | 5.38 / **0** = **∞** | 3.65 / **−1** = **undefined** |

`RECOMPUTED` from Thum & Kuhfeld (2020), Tables C.1.3, C.1.6 and Appendix E.1/E.2.

**A nationally average American child, run through this metric, "learns 2.4× faster than a
nationally average American child" in fifth-grade mathematics, and infinitely fast in
eighth.** The reason is structural: the RIT scale compresses with grade — adjacent grade
means converge to nothing by grade 8 — while within-year growth does not compress at the
same rate. Any ratio with the first quantity in the denominator explodes.

This is not a claim that Alpha's students didn't grow. It is a claim that **the published
multiplier cannot distinguish a school that doubles learning from one that is exactly
average**, and that a "2.2× for all students" figure is within the range this metric
assigns to the national mean.

### 2.4 Attainment: whose percentile is "top 1%"?

The attainment claim is stated at class level — *"our classes score in the top 1-2%"*,
*"most of our classes are in the top 1% for every subject"*. NWEA norms **school/grade
means** in a separate set of tables (Appendix C.2) precisely because the distribution of
school means is far narrower than the distribution of students.

From Table C.2.3 (Spring Mathematics **School** Achievement Percentiles) against Table
C.1.3 (Spring Mathematics **Student** Achievement Percentiles):

| Grade | School p99 mean RIT | Equivalent **student** percentile |
|---|---|---|
| K–12, mathematics | 169.1 → 261.1 | **≈ 90th**, at every grade |
| K–12, reading | 165.4 → 247.8 | **≈ 84th–87th**, at every grade |

`RECOMPUTED`. Worked example, grade 5 mathematics: the 99th-percentile *school* has a mean
spring RIT of **238.2**. On the student table, 238.2 falls between the 90th student
percentile (240) and the 75th (230).

So: **a class in the top 1% of American classes has an average student around the 88th
percentile of American students.** Both sentences are true of the same school. The first is
the one that gets said. Which of the two Alpha's figures are is **`UNVERIFIABLE` from
outside** — the published claim does not specify, and the underlying reports are not public.

`OPEN`: **Nobody has asked Alpha to state whether its percentile claims are student-level
or school/grade-level.** Nobody asked because the distinction is invisible to a general
audience and costs nothing to leave ambiguous. It is a one-sentence disclosure and it would
change the reader's estimate by roughly ten percentile points.

### 2.4a "Nationally" means "of American public-school students"

One more property of the reference population, stated in the norms document's own opening
sentence of Chapter 3:

> "The primary goal of this study is to estimate achievement and growth norms that support
> inferences about the relative performance and changes in performance of K-12 students
> attending **U.S. public schools** who take the English versions of MAP Growth …"
> — Thum & Kuhfeld (2020), §3

The sampling frame is explicitly U.S. **public** schools; NWEA partners were "more than a
quarter of … some 92,000 U.S. public schools in 2016-17". `RECOMPUTED`/`OBSERVED`.

A $40,000–$75,000 private school reporting that its students are "in the top 1% nationally"
is therefore reporting a rank **against a population that excludes private-school students
altogether** — roughly a tenth of American enrolment, skewed towards exactly the
socioeconomic profile Alpha recruits from. This is not deceptive; it is how MAP works and
every MAP user is in the same position. It does mean the phrase "top 1% nationally" is doing
more rhetorical work than the underlying statistic supports, and it compounds with §2.4: the
claim is a **class-level rank against public-school students**, which is a considerably
weaker statement than "our students are the top 1% of American children."

### 2.5 Who administers the test, and does it matter

MAP Growth is administered **by the school**, on the school's own devices, on a schedule the
school sets, three times a year. There is no external proctor, no state monitor, and no
published chain of custody. This is entirely normal for an interim assessment — it is *not*
an accusation — but it means the outcome measure and the intervention are under the same
roof, which is the condition under which every education-research standard requires an
independent administration before a claim is treated as evidence.

Two specific, non-accusatory mechanisms are worth naming because they are documented in
NWEA's own research and are *predictable* consequences of Alpha's design rather than of any
misconduct:

1. **Test engagement.** NWEA: *"Researchers at NWEA have found that a meaningful amount of
   disengagement occurs with MAP Growth assessments … scores from disengaged students will be
   distorted and should not be considered trustworthy indicators of achievement."* The 2020
   norming sample **excluded** records with >10% rapid guessing, so the norm reference is
   engagement-cleaned. But a school whose entire operating model is a motivation engine —
   school currency, "WASTE meter", daily rings, "Test2Pass events" — will have systematically
   higher test engagement than the operational population its parents imagine it is being
   compared to. `INFERENCE` on `OBSERVED` (Thum & Kuhfeld 2020, §1.1.1).
2. **Test familiarity.** Students take MAP three times a year in an environment whose daily
   practice is adaptive item response with immediate feedback and an explicit accuracy
   target — structurally the same task as MAP. The white paper also lists "test-taking
   techniques" as an explicit use of the daily 20-minute block. Practice effects on a
   computer-adaptive test are a known and unquantified confound here. `OPEN` — no one has
   measured it, because it would require an external instrument to detect.

---

## 3. Is there any independent measurement at all?

**No.** Stated plainly, because that is the finding.

### 3.1 Peer-reviewed literature

Systematic retrieval across **OpenAlex**, **Crossref**, **ERIC** and **arXiv** returns
exactly two works naming Alpha School, both **preprints, neither peer-reviewed, neither
containing an independent measurement**:

| Work | Venue | Status |
|---|---|---|
| Choi, W. C. & Chang, C. I. (2026-02-27), *Can AI Replace Teachers? Using AI to Unleash Students and Transform Teaching: A Case Study of Alpha School*, `doi:10.36227/techrxiv.177220375.51273405/v1` | **TechRxiv preprint** | not peer-reviewed; 0 citations; full text HTTP **403** |
| Waford, L. D. (2025-05-08), *Skinner's Vision Realized: AI and the Future of Education*, `doi:10.5281/zenodo.17707250` (and a duplicate deposit `…17707251`) | **Zenodo preprint** | not peer-reviewed; 0 citations |

`OBSERVED`. Searches for **"Timeback"** and **"2 Hour Learning"** in an education sense
return nothing at all — the OpenAlex hits are false positives (a continuing-education credit
listing; an urban-design paper). arXiv returns zero results for `"Alpha School" AND "AI
tutor"`.

**There is no evaluation of this model in the peer-reviewed literature. Not a weak one. None.**

### 3.2 State accountability data

The schools are **private**. Private schools in Texas are not subject to state
accountability reporting; they do not receive TEA accountability ratings and do not appear
in the state's assessment results. The white paper confirms that STAAR (Texas) and FAST
(Florida) are used **internally**, as grade-completion mastery exams at a 90% cut score —
i.e. the state instrument is used, but the results are not in the state system.

Consequence: **the single easiest verification route — comparing a cohort's state test
results against demographically matched public-school cohorts — is closed by the operator's
choice of legal form.** That choice is legitimate and common; it is also the reason no
outside party can check the claims. `OBSERVED`.

The exception that would matter is any **public** entity in the group, because a public
school must report. 2 Hour Learning's own site lists **Unbound Academy** among its schools;
`unbound.academy` returns an "under construction" WordPress placeholder (HTTP 200) and
`unbound.school` a marketing site. Regulatory status is covered in §3.4.

### 3.3 Accreditation is not outcome verification

Alpha Austin's own page carries **both** strings in its footer markup: *"Alpha Austin is a
candidate for accreditation with Cognia"* and *"Alpha Austin is accredited by Cognia"* —
a toggled element with no visible date. `OBSERVED`.

Cognia's own account (retrieved from cognia.org, HTTP 200) is more informative than Alpha's:

> "Students in the Alpha School system … consistently score in the top 1% nationally on MAP
> tests. Still, Alpha leaders believed that no accrediting agency could accept the system's
> unusual approach … **if Alpha students had to transfer to a public school for any reason,
> their unaccredited transcripts were a hindrance.** System leaders decided to **pilot** the
> Cognia Accreditation process at Alpha High in Austin, Texas … As a result, Alpha School
> leaders approved systemwide accreditation."

Three things follow. (i) Alpha operated **unaccredited** for most of its first decade —
Cognia says so. (ii) Accreditation began as a **pilot at one campus** (Alpha High Austin)
and was then extended system-wide; it is recent. (iii) **Cognia's page repeats Alpha's
percentile claim as fact.** An accreditor restating an operator's self-reported outcome
does not convert it into an independent measurement; Cognia accreditation is a
process-and-improvement standard, not an audit of test results. `OBSERVED`.

`UNVERIFIABLE`: which specific Alpha campuses hold full accreditation versus candidacy, and
on what dates. Cognia's institution search endpoints returned HTTP **404**
(`/find-a-school/`) or **DNS failure** (`api.cognia.org`, `certification.cognia.org`);
`tepsac.org` timed out (curl exit 28, HTTP **000**); the TEA private-schools page returned
HTTP **404**.

### 3.4 Regulatory and journalistic record

*(This subsection is completed in §8.3 with the material returned by the regulatory
retrieval pass; the items below are what was retrieved directly.)*

- **404 Media**, Emanuel Maiberg, **17 Feb 2026**, *"Students Are Being Treated Like Guinea
  Pigs Inside an AI-Powered Private School"*. Free lede, retrieved verbatim (HTTP 200; body
  paywalled): *"Alpha School … is AI-generating faulty lesson plans that internal company
  documentation find sometimes do 'more harm than good,' and scraping data from a variety of
  other online courses without permission to train its own AI, **according to former Alpha
  School employees and internal company documents**."* `OBSERVED` — third-party
  investigation, primary documents claimed but not visible to this retrieval. The remainder
  of the article is behind a paywall and **was not read**; nothing beyond the lede is
  asserted here.
- **Broadcast coverage exists and is descriptive.** Alpha's own "In the News" list names FOX 7
  Austin (*"Education Sec. McMahon visits Austin school…"*), KXAN, **CBS News** (*"Inside the
  $40,000 a year school where AI shapes every lesson, without teachers"*), ABC News and
  NewsNation. `OBSERVED`. **No retrieved item in this class contains an independent
  verification of a test result**; the pattern is site visit, interview, restatement of the
  operator's figures. That is not a criticism of the journalists — verifying a MAP percentile
  requires student-level data no news organisation can obtain — but it means the volume of
  coverage carries no evidentiary weight at all.

### 3.4a The regulatory record: five states, one approval

This turned out to be the richest verification channel available, because **a charter
application is a public document written under penalty, for readers who are paid to be
sceptical.** What the group says in an application can be compared with what it says in
marketing. The comparison is the finding.

**Unbound Academic Institute** — affiliated with the same founders — filed cyber-charter
applications in **Arizona, Utah, Arkansas, North Carolina, South Carolina and Pennsylvania**.
**Utah, Arkansas and North Carolina rejected them; Pennsylvania denied its application in
2025; Arizona is the only approval on record.** (The South Carolina outcome was not
established in this session — `UNVERIFIED`.) `OBSERVED` (Meyer 2025; Chalkbeat 2025; Bucks
County Beacon 2025).

**Pennsylvania denied it.** From the denial, quoted in Meyer's 26 March 2025 update:

> "While a single deficiency would be grounds for denial, **the Department has identified
> deficiencies in all five of the required criteria.**"
> — Pennsylvania Department of Education `OBSERVED` (regulator)

Separately reported: PDE described the instructional model as **"untested"** and not
demonstrating alignment with state academic standards. `OBSERVED`.

**And the single most revealing number in this entire section.** Chalkbeat, reading the
Pennsylvania application (Sitrin, 24 Jan 2025):

> "According to the school's Pennsylvania application, Unbound Academy would launch in the
> fall of 2025 with **500 students in grades 4-8 and only four teachers**. By its fifth year,
> Unbound plans to enroll 2,500 students and 76 teachers. And the application projects a
> **90% student retention rate** each year — much higher than other cyber charters have
> projected. **In year two, Unbound Academy projects it'll be ranked in the top half of all
> Pennsylvania schools**, according to the application."

`OBSERVED`. **Marketed to parents: "top 1–2% nationally". Projected to a state regulator:
top half of Pennsylvania.** Those are not the same forecast, and the gap between them is the
best available estimate of how much of the public claim the operator itself believes is
transferable to an unselected population.

Three further items from the same regulatory record, each corroborated by at least two of
the retrieved reports:

1. **The "AI" is largely commodity courseware.** Chalkbeat: the platform "relies on a mix of
   proprietary AI tutoring software and third-party apps like **Khan Academy, IXL, and
   Amplify**." Bucks County Beacon: *"Price has been clear that 'AI' in this case does not
   mean a ChatGPT type Large Language Model, but apps more along the lines of IXL Math or
   Khan Academy's Khanmigo."* The Arizona application, quoted by Meyer: *"We employ adaptive
   technology to tailor educational experiences through widely recognized platforms like IXL
   and Khan Academy, supplemented by custom content to address specific gaps."* `OBSERVED`.
   **The instructional engine is adaptive courseware of a kind that has existed for fifteen
   years, and neither IXL nor Khan Academy claims anything resembling these outcomes.**
2. **The same application specifies webcam-based affect inference.** Arizona application,
   quoted by Meyer: *"The AI rigorously analyzes comprehensive student data—response accuracy,
   engagement duration, and **emotional feedback via webcam**—to ensure lessons are
   appropriately challenging."* `OBSERVED`. This corpus's H1/F8 sections would treat
   webcam-based emotion inference on minors as a first-order safety and validity question;
   emotion recognition from facial expression has a weak scientific base and, in the EU AI
   Act, is prohibited outright in education. It is asserted here in a filing to a state
   board with no accompanying validity evidence.
3. **Vendor pricing to the public purse differs by state by a factor of ~3.** Meyer, from the
   applications: 2 Hour Learning, Inc. charges **$2,000 per student** in Arizona and
   **$6,500 per student** in Pennsylvania for "curriculum and resource materials". Meyer also
   documents that **100% of Unbound Academy's named board members are affiliated with the
   vendors the board approves contracts with** (2hr Learning, Crossover, Trilogy) — quoting
   the application's own disclosure. `OBSERVED`. This section takes no view on the legality
   of that structure; it records that **the entity setting the price and the entity approving
   the price are the same people**, which is a fact about how much weight a regulator's
   approval can bear.

Also documented: **Valenta Academy**, a 2 Hour Learning brick-and-mortar charter proposal, was
recommended for rejection by the Lancaster (PA) district administration in January 2025, and
the affiliated Texas charter application was reported as vetoed by the Texas Education Agency
in June 2025. `OBSERVED`, second item `UNVERIFIED` to a primary source in this session.

**And both state subsidy programmes it approached have excluded it, at least temporarily.**

- **Texas.** The Austin American-Statesman (Heath, 16 Jan 2026, HTTP 200) reports that of
  roughly **40 Austin private schools accredited solely by Cognia, one was approved** for the
  state's new Education Freedom Accounts (SB2) programme — Alpha School Austin was shut out —
  while ~90 Austin schools in total were approved. The comptroller had sought an attorney-
  general opinion over alleged foreign ties among *some* Cognia-accredited schools; Alpha was
  collateral. The account is worth ~**$10,500 per pupil** (~$30,000 for special education),
  and eligibility requires accreditation, two years of operation, **and a nationally
  norm-referenced test from grade 3**. The Houston Chronicle (4 Feb 2026) reports the block
  was later resolved for most affected schools. `OBSERVED`.
- **Oklahoma.** Oklahoma Watch (Henry, 21 Jul 2026, HTTP 200): **Alpha was listed on the
  Oklahoma Tax Commission's Parental Choice Tax Credit approved-schools list and was removed
  after Oklahoma Watch inquired**; Alpha then stated it had not applied to the programme. A
  follow-up two days later was headlined *"New AI-Powered Private School Won't Qualify for Tax
  Credit Program This Year"* (headline confirmed via a news index; **body HTTP 429, not
  read**). `OBSERVED`.

**The pattern is worth naming without over-reading it.** Four charter refusals, one
independent-school incorporation refused, and exclusion (temporary or otherwise) from two
state subsidy programmes. None of these is a judgement about learning. All of them are
judgements by bodies whose job is to check, and **every one of them went against the
operator.** The one approval is the one that will now have to report.

### 3.4b The one substantive independent technical analysis

**Meyer, D. (8 Jan 2025), "The Truth About 2 Hour Learning, Unbound Academy, and Alpha
School", *Mathworlds*.** Retrieved in full (HTTP 200). Dan Meyer is a mathematics educator
and a named critic, not a neutral party; his analysis is nonetheless the only piece of
retrieved third-party work that **reads the primary application documents and checks the
claims against them**, and its checkable assertions hold up against the other sources
retrieved here.

Its central factual finding, from the Arizona application:

> "In its charter application, Unbound Academy describes the minimum qualifications for its
> 'guides,' which, again, they claim are *not* teachers … their guides are just teachers.
> Certificated teachers. … '**The guide-to-student ratio is 1:20 compared to 1:30 in typical
> schools.**' Unbound Academy is employing **more** certificated teachers per student than
> 'typical schools.'"

`OBSERVED`. Chalkbeat independently reports the same reversal: *"She's already had to clarify
perhaps her most startling claim about whether her schools really employ traditional
teachers; in Pennsylvania at least, they would."*

Its central argument is the selection argument this section reaches independently in §4, and
it deserves quoting because it is the sharpest available statement of it:

> "each of those 'schools using 2hr Learning' are private schools in MacKenzie Price's Alpha
> School network, each of which charges tuition … each of which **can admit, expel, and
> counsel out students for reasons that are not legal in public schooling** … Applying a
> tuition filter in the admissions process—indeed, having an admissions process *at
> all*—does a great deal to ensure engagement from both students and parents."
>
> "This is the case with the Alpha private school network, which gets great results, as far
> as I can tell, **not by replacing teachers with AI, but by replacing poor kids with rich
> kids, by replacing unengaged families with engaged families.**"

Two further checkable details from the applications, via Meyer: **$1,000 per student per year
budgeted for marketing** (≈10% of Arizona's ~$10,000 per-pupil spending, per a reader's
comment Meyer endorses); and the Arizona application's description of the Brownsville campus
as serving *"students from underprivileged backgrounds"* while, per Meyer, charging
**$15,000** tuition — the campus page today states **$10,000**. `OBSERVED`.

### 3.4c The courseware vendor terminated the account

The most consequential single fact retrieved in this session, and it comes from a supplier's
own statement rather than from a critic. Reporting the Brownsville campus, **WIRED (Todd
Feathers, 27 Oct 2025)** — retrieved via `curl`, HTTP **200**; `wired.com` refuses WebFetch:

> **IXL Learning told WIRED that Alpha School's account was deactivated in July [2025] and
> that Alpha is "no longer an IXL customer due to violating our terms of service,"** adding
> that IXL "is not intended—and we do not recommend its use—as a replacement" for "trained,
> caring teachers."

`OBSERVED` — a named vendor statement to a named publication. IXL is one of the three
third-party platforms the charter applications name as the instructional engine (§3.4a). Two
things follow. First, **the supplier of a core component publicly disclaims the use it is
being put to.** Second, whatever the platform stack was when the 2023/24 MAP results were
generated, it is **not** the stack in operation afterwards — which means the published
outcome figures and the current product are not describing the same system.

The same report documents the mechanism failing in the direction the design predicts: a
nine-year-old locked in an IXL remediation loop on three-digit multiplication for 20-plus
repetitions with a guide refusing an exception; the child skipping lunch to catch up and
losing weight; children barred from rooms, field trips and off-campus lunches for missing
learning goals. **And the Brownsville head of school is quoted saying the adult guides "don't
do any teaching."** `OBSERVED`.

This section does not treat one investigation as proof of a systemic condition. It records
that the only two long-form investigations that obtained internal documents and named
sources — WIRED (Oct 2025, Jun 2026) and 404 Media (Feb 2026) — **both** report the software
producing bad instructional decisions, and that a supplier independently ended the
relationship.

### 3.4d The New York campus is not a school

**WIRED (Feathers, 4 Jun 2026)**, HTTP **200**, quoting the New York State Education
Department's counsel refusing Alpha's application to incorporate as an independent school
(late summer 2025):

> "Instruction as proposed is primarily online, with an AI-based platform called 2 Hour
> Learning™ that delivers instruction in core academic subjects **with little to no
> supervision or competent teacher delivering such instruction**… Generally, [NYSED] does not
> recognize online schools as proposed."

`OBSERVED` (regulator, via a document obtained by the publication). Alpha then operated the
**$65,000** Maiden Lane site as an *"Alpha Anywhere Center"* homeschool co-op — parents file
as homeschoolers — and re-applied in April 2026; **still pending**. Reported scale: *"more
than a dozen families."*

**This is a second regulator, in a second state, refusing the same model on the same
ground.** Alpha's own New York City page lists a $65,000 tuition and carries the same
percentile claims as every other campus; it does not disclose that the state has declined to
recognise it as a school.

The same piece quotes internal Trilogy documents on the expansion's own stated priority
order — *"Opening date > safety > operability > cost efficiency > permanence"*; *"We will
commence the buildout at risk. We are willing to trade off the financial risk if permits are
not obtained"*; *"many permits exist by habit, not necessity"* — and reports that **Miami-Dade
Fire Rescue confirmed** the Miami campus holds no annual Life Safety Operating Permit and
operates on a temporary certificate of occupancy, with students relocated off-site for
several days. `OBSERVED`. This corpus's §15 (*what we owe children*) and F8 (safety) would
treat that as disqualifying independent of any outcome claim, and it is recorded here for
that reason rather than as evidence about learning.

### 3.4e Corporate form: nothing files anything

Searched directly: **IRS** (ProPublica Nonprofit Explorer, the IRS Business Master File) and
**SEC EDGAR** full-text search.

| Query | Result |
|---|---|
| "2 Hour Learning" (IRS) | **0 organisations** |
| "Trilogy Enterprises" / "Trilogy Foundation" / "Legacy of Education" (IRS) | **0 matching organisations** |
| "Alpha School" (IRS, national and TX) | 27 hits, **none** the Austin network |
| **"Unbound Academic Institute"** (IRS) | **EIN 33-3639402**, Goodyear AZ, 501(c)(3), NTEE B19, **IRS ruling date 1 Apr 2026**, **zero Form 990 filings on record** |
| "Alpha School", "2 Hour Learning", "Timeback", (SEC EDGAR full text) | **no filings**; all hits are unrelated companies. **No Form D.** |

`OBSERVED`. **The entire group files nothing that a regulator or the public can read.** There
is one recognised non-profit in it, it was recognised three months ago, and it has never
filed a 990. There is no Form D, consistent with self-funding rather than outside capital.

Reported ownership chain (**The Lever**, 24 Jun 2025, HTTP 200; corroborated by Bucks County
Beacon): **Legacy of Education, Inc.** — formerly a Trilogy subsidiary — owns **both** Alpha
School and 2 Hour Learning, Inc.; **Trilogy** owns the 2 Hour Learning patent and software;
**Andrew Price** is CFO of Trilogy and ESW Capital and president of **YYYYY, LLC**, a Delaware
entity that supplied *"general and administrative services"* to the schools and **~$2 million
in private grants to the charter applicants**; **Crossover Markets** recruits the virtual
educators. `OBSERVED`.

And the fee schedule, which differs by state by a factor of ~3 and was retrieved twice with
slightly different figures — recorded here **with the discrepancy intact**: 2 Hour Learning's
per-pupil charge to the public purse is **$2,000 in Arizona and Arkansas**, and **either
$5,500 (Bucks County Beacon) or $6,500 (Mathworlds)** in Pennsylvania; Trilogy's revenue
share is 2.5% capped at **$350,000/year in Pennsylvania** against **$150,000** elsewhere.
`OBSERVED`, `UNVERIFIED` as to which Pennsylvania figure is right.

**One widely repeated number is not supported.** The claim that Joe Liemandt "committed
$1 billion" to the project **could not be traced to any reachable source**. The nearest item
is a Forbes headline referring to his *net worth*; the Texas ESA programme is itself a
$1 billion programme, which is a plausible source of the conflation. `UNVERIFIABLE` — **the
figure is not restated in this report.**

### 3.5 The natural experiment that is about to happen — and it is the whole ballgame

**Approved by the Arizona State Board for Charter Schools on a 4–3 vote, 19 December 2024.**
`OBSERVED`. It is registered in Arizona's accountability system: querying the ADE School
Report Cards API directly returns `Unbound Academic Institute` as
`educationOrganizationId` **1002639** (Charter District) and `Unbound Academy` as
**1002640**, typed both **"Charter School"** and **"Online School"** (HTTP **200**).

**And the record is empty.** The report-card detail page for 1002640 renders with **no AASA
results and no A–F letter grade**, and Unbound appears in **neither** the NCES Common Core of
Data directory for SY2023-24 nor SY2024-25 (2,613 and 2,633 Arizona schools scanned via the
Urban Institute Education Data API; zero matches). `OBSERVED` — consistent with a school that
has not yet operated a testable year.

**So the state file exists and is blank.** That is the precise current position: the
verification mechanism is in place, registered, and has produced nothing yet.

`unbound.school` (HTTP 200, accessed 2026-07-29) describes it in its own words:

> "Arizona · Grades 4–8 · Tuition-Free Public Charter … Unbound Academy is Arizona's
> tuition-free virtual charter school for grades 4–8. **Real teachers on screen all day**, a
> curriculum personalized to each child, and a school day that runs 8 to 2 — with core
> academics mastered by 11 AM." · "✓ Tuition free — funded by Arizona · ✓ Laptop provided ·
> ✓ **Certified teachers live on screen**" · "**2.8× faster learning, measured by NWEA MAP
> Growth**" `VENDOR`

It is listed by 2 Hour Learning as one of its schools. **It is a public charter.** Public
charters in Arizona sit inside state accountability: statewide assessment (AASA), an A–F
letter grade, and published, disaggregated results.

**This is the single most important fact in this section.** Every verification route
described in §3.1–§3.4 is closed by the schools' private status. Unbound Academy closes none
of them voluntarily — it closes them by operation of law. Within one to two assessment
cycles there will exist, for the first time, an **externally administered, externally scored,
publicly reported** outcome for a 2 Hour Learning school, with a state-defined comparison
population and mandatory reporting of enrolment and mobility.

Two caveats before anyone treats it as the answer:

1. **It is the online variant**, and §8.3 documents that online delivery of schooling has a
   uniformly bad externally-measured record. A poor Unbound result would be confounded with
   virtuality; a *good* one would be extraordinary precisely because it would break that
   pattern.
2. **The model is not the same model.** The flagship sells *"There are no academic teachers"*
   (white paper) and *"the AI tutor"* as the instructional engine. Unbound sells *"Certified
   teachers are on screen all morning — our students go to them first, not the software"* and
   *"AI builds the plan. Teachers teach the kid."* `OBSERVED` — this is a direct comparison of
   two texts published by the same organisation. **When the same programme enters a regulated
   environment, the human teacher reappears in the marketing.** Whatever Unbound's results
   turn out to be, they will be results for a *teacher-led* variant, and a `2.8×` claim
   attached to it cannot be transferred back to the teacherless one.

Note also the schedule arithmetic: 8:00–8:30 launch, **8:30–11:00 core academics** (a
2.5-hour block described as "2 Focused Hours" with breaks inside it), 11:00–12:00 break,
12:00–2:00 workshops. `OBSERVED`. The two-hour figure is again a description of *content
time inside a longer block*, not of the block.

**And the school says the verification is coming, in writing** (`unbound.school/program`,
HTTP 200):

> "Unbound Academy students take **Arizona's state assessments (AASA and AzSCI) like every
> public school.** Progress is also measured through frequent internal benchmarks in 2 Hour
> Learning and the national NWEA MAP exam …" · "**Arizona state assessment results will be
> published as they become available.**" `VENDOR`

Its footer carries the statutory links — *ASBCS Performance Dashboards*, *ADE School Report
Cards*, *Title IX*, *AZ Parent Rights Handbook*, *Governing Board* — and the mandatory
salary disclosure: *"Average salary of teachers in budget year 2025-26 is $60,000 … Previous
Year: N/A"*, confirming a first year of operation. Registered address: Goodyear, Arizona.
`OBSERVED`.

**Three differences between the regulated and unregulated versions of the same programme,
all read directly off the operators' own pages:**

| | Alpha School (private) | Unbound Academy (public charter) |
|---|---|---|
| Adults | *"There are no academic teachers"*; "Guides"; reported $100k–$150k | *"Certified teachers are live on screen all morning. Students go to them first"*; statutory average teacher salary **$60,000** |
| Students with disabilities | Oklahoma Watch reports the schools do not serve students requiring intensive support or IEPs | *"We accept students of all abilities. 1:1 academic coaching is available for students who need extra support."* (a public charter is legally obliged to) |
| External measurement | none | **AASA + AzSCI, published** |

`OBSERVED`. This table is the section's most compact statement of the problem. **The claims
that are hardest to check are attached to the entity that no one can check, and the entity
that must report has quietly acquired certified teachers, an obligation to enrol everyone,
and a lower salary line.** Whether the results follow the model or the regulation is,
finally, an empirical question with a date on it.

The headline attached to the public entity is nonetheless the same metric §2 takes apart:
*"**2.8×** faster learning vs. national average (NWEA MAP Growth) … Measured by NWEA MAP
Growth assessments across the 2-Hour Learning model."* `VENDOR`. Read against §2.3, a
grade 4–8 cohort growing at exactly the national average would be scored between **1.37×
and ∞** by this method.

- **Oklahoma Watch / KGOU**, **20 July 2026** (retrieved via GDELT, HTTP 200): Alpha opening
  Edmond and Tulsa campuses 12 Aug 2026 with **26 and 32 students** respectively; Oklahoma
  tuition **$40,000** (reduced to $30,000 for a founding cohort); "guides" are **not
  certified teachers** and earn **$100,000–$150,000**; the schools were **initially included
  on and then removed from the Oklahoma Tax Commission's approved-schools list**; the report
  states the schools do not serve students requiring intensive support or IEPs.
  `OBSERVED`.

---

## 4. Selection — the variable that decides everything

### 4.1 What can be quantified

Tuition, read directly from each campus page (all HTTP 200, 2026-07-29):

| Campus | Tuition |
|---|---|
| San Francisco · Palo Alto | **$75,000** |
| New York City · Chantilly (DC) | **$65,000** |
| Miami · Plano · Denver | **$50,000** |
| **Austin (flagship)** · Scottsdale · Houston | **$40,000** |
| **Brownsville, TX** | **$10,000** |

Plus: **$100** non-refundable application fee; **$1,000** non-refundable deposit; 5% sibling
discount; "Alpha tuition remains on par with the nation's best private schools." `VENDOR`.

Enrolment, where the operator states it: **Alpha Austin, "more than 150 students", year 11.**
Oklahoma launch campuses, **26 and 32** students. `VENDOR` / `OBSERVED`.

**And the scale, honestly.** The marketing menu lists **44 campus entries**; the campus table
maintained from the operator's own locations page as of April 2026 lists **13 operating
campuses**. Reported enrolments: Austin flagship **~90 students** (K–8) as of 2020 and
Alpha High Austin **152**; the four campuses opened in 2024 each opened with **fewer than ten
students**; NYC *"more than a dozen families"*; Oklahoma **26 and 32**. `OBSERVED`, with the
per-campus figures resting on one insider account (Astral Codex Ten, 27 Jun 2025) and two
news reports.

**Two consequences.** First, **the denominators behind "our classes score in the top 1–2%"
are small** — plausibly tens of students per grade-subject cell, and in the one case where an
outside reader checked, five. Second, this is a network reported in the press as a national
phenomenon whose total enrolment has never been stated by anyone, including the operator.

**The sample-size finding, from a sympathetic source.** The most detailed independent account
of the programme is a book-length review by a parent who *moved to Austin in October 2024* to
try it (**Astral Codex Ten, 27 Jun 2025**, HTTP 200) — a source predisposed to believe it.
Two of its findings are load-bearing:

> "there is nowhere on the internet that provides a detailed, non-partisan description of what
> the '2 hour learning' program actually is."

and, on the affiliated gifted school's headline multiplier: **GT School's "5× faster" figure
rested on only five children who took both the fall and the winter test.** `OBSERVED`.

**n = 5.** That is the only occasion on which anyone outside the organisation has been able to
put a denominator under one of these multipliers, and it collapsed. It does not follow that
Alpha's own figures rest on five students. It does follow that **the published figures carry
no N, that at least one of them was tiny, and that the burden of showing otherwise has never
been met.**

### 4.2 The admissions funnel, in the operator's words

1. Attend an information session.
2. Submit application + **$100** fee.
3. **Shadow Day** — the child spends a day on site using the apps; **prior school records
   (grades 2–8) required before the visit**.
4. *"During your meeting, we will review the **MAP exam results**, feedback from your child's
   Shadow Day or Observation, and discuss your academic goals."*
5. Enrolment offer, tuition agreement, **$1,000** deposit.

`VENDOR`, verbatim from `alpha.school/admission/`.

And the point a private school's own materials will never make, made by an outside reader of
the charter applications (Meyer 2025): these are *"private schools … each of which **can
admit, expel, and counsel out students for reasons that are not legal in public
schooling**."* `OBSERVED`. Selection is not only at the gate. It operates continuously, and
it operates on exactly the two variables the operator names as decisive — student engagement
and parental alignment.

**A MAP exam is taken before enrolment and reviewed at the enrolment meeting.** The operator
does not describe it as a selection instrument, and it plausibly functions as placement. But
the distinction is invisible from outside, and a school that (a) tests applicants on the same
instrument it later reports outcomes on, (b) requires prior school records, and (c) states
that the model "works for 80–90% of children" and requires parental philosophical alignment,
has by its own description a **non-random intake on prior attainment, family engagement, and
fit.** `OBSERVED`.

### 4.3 How much could selection explain?

The honest answer is: **most of the attainment claim, and none of the growth claim, and we
cannot separate them.**

- **Attainment.** §2.4 established that "top 1% of classes" corresponds to an average
  student near the ~88th percentile. A $40,000–$75,000 tuition, application-fee,
  shadow-day, records-required private school in Austin, Palo Alto, Greenwich and the
  Upper East Side would be expected to enrol students near that percentile *on day one*.
  The correlation of family income and parental education with MAP achievement is large and
  well documented. **A defensible statement is that selection is sufficient, on its own, to
  produce the entire published attainment claim.** `INFERENCE`.
- **Growth.** Selection does not straightforwardly explain *growth*, and this is where the
  interesting question lives. Two things cut in opposite directions: (i) NWEA's own
  conditional growth norms already condition on starting status, so a high-starting cohort
  is not automatically credited with high growth; (ii) but the *metric Alpha uses* (§2.2) is
  not a conditional growth metric, and its inflation is largest precisely in the mid-grades.
- **Brownsville is the case that matters.** A $10,000-tuition campus in one of the poorest
  districts in the country, where the white paper claims low-SES students "learned 2.1x
  faster" and reports 2nd-grade cohort percentile moves of 31%→71% (reading) and 31%→84%
  (maths) between Winter 2023 and Winter 2024. **If any part of this programme is real, this
  is where it would show.** It is also where the sample is smallest, the selection into a
  new school in a poor district is strongest (families who seek out and can reach a novel
  private school), and the reported quantity is a *cohort mean percentile move* with no N,
  no cohort definition, and no statement of who left. `VENDOR`, `UNVERIFIABLE`.

`OPEN`: **No attrition figure exists anywhere in the operator's materials.** Not
year-on-year retention, not mid-year withdrawal, not the fraction of the "10–20% of children"
the model admittedly does not suit who leave. Nobody asked because nobody has standing to
ask a private school for it — and because a cohort-mean percentile computed on survivors is
exactly the statistic attrition inflates. **This is the single highest-value missing number
in the entire case.**

---

## 5. What the model actually is, mechanically

Stripping the marketing, from the white paper and FAQ (`VENDOR` throughout — this is a
description of the design, not an endorsement of its effects):

| Component | What it actually is |
|---|---|
| **Session structure** | 4 × 25-minute focused blocks (Maths, Science/Social Science, Language/Writing, Reading) + 20 minutes mostly maths and "learning strategies, test-taking techniques, Depth of Knowledge exercises" + breaks = 120 minutes. Explicitly Pomodoro. |
| **Content** | Adaptive apps, a mix of in-house (**AlphaRead, AlphaFlash, AlphaWrite**) and third-party. AlphaFlash is a flashcard/fact-fluency app — retrieval practice by another name. **The third-party component is named in the charter applications and by the founder: IXL, Khan Academy (Khanmigo), Amplify.** Price is on record that "AI" here does **not** mean a large language model but adaptive courseware of the IXL/Khanmigo class. `OBSERVED` |
| **Placement** | Diagnostic on entry; students placed at knowledge level, not age grade. "A 2nd grader ready for 5th-grade math will engage with that level." |
| **Mastery criterion** | **90%** on a concept before progression; **90%** on a grade-completion exam (STAAR/FAST used internally) to close a grade level. |
| **What happens on failure** | The **"Struggle Detector"** identifies difficulty and injects "additional targeted or easier lessons"; the paper explicitly states that this is why a 25-hour grade takes 40 hours in practice. For maths specifically: mandatory return to fact fluency ("Fast Math skills … memorizing basic addition, subtraction, multiplication and division tables"). |
| **Pacing rule** | ~40 hours per grade per subject → ~80 school days at 30-minute sessions → two grade levels in 180 days, with 90-day windows. |
| **Accuracy control** | Explicit band: **above 95% ⇒ material too easy; below 70% ⇒ too hard or guessing.** |
| **Effort control** | The **"WASTE meter"** — percentage of session time not spent on genuine work ("being present at the computer, entering meaningful answers, reading explanations, and avoiding random guessing"). >50% WASTE is flagged as the reason a student exceeds two hours. |
| **Student-facing loop** | "Dash" dashboard: Jenga-tower progress visual, goal setting, "Daily Rings" completion check. |
| **Adults** | "Guides", explicitly **not academic teachers**; role is motivation, emotional support, life-skills workshops, goal-setting. FAQ: "Guides earn six-figure salaries." Selection criteria are motivational and workshop-design ability, not subject expertise. |
| **Extrinsic motivation** | School currency ("Alphas") exchangeable for prizes; earned time; "ThinkTank" room access; collective rewards. |
| **Assessment loop** | MAP 3×/year (percentile achievement, percentile growth, "times growth"); in-app mastery gates; internal STAAR/FAST grade-completion exams at 90%; "Test2Pass" events; ISEE/SSAT "being added for benchmarking". |
| **Parent loop** | Daily-updated learning plan; minutes per subject vs target; accuracy; WASTE. |

**One design detail deserves singling out.** The accuracy band — *keep the learner between
70% and 95% correct* — is centred at ~82.5%, which is within a couple of points of the
theoretically optimal training accuracy derived in **Wilson, Shenhav, Straccia & Cohen
(2019), "The Eighty Five Percent Rule for optimal learning", *Nature Communications*
10:4646, `doi:10.1038/s41467-019-12552-4`**. Whether arrived at empirically or by
derivation, **this is a correct piece of engineering**, and it is the same quantity BTES
called "high success rate". A survey that dismissed this school wholesale would be missing
that its core control loop is right.

### 5.1 Is two hours actually a compression? Audited in academic learning time

This is the question §30 of this survey exists to answer, and the answer is not the one the
marketing implies.

The clock arithmetic is trivial: a 6-hour academic day becomes a 2-hour one, so **3×**. But
§30's whole argument is that clock time is the wrong unit. The right unit is **academic
learning time** — allocated time × engagement × time at a high success rate — and the BTES
cascade (Fisher et al. 1980) puts it at **≈35% of allocated time in the median classroom**,
with extremes of ~4 minutes and ~52 minutes of productive learning inside identically sized
school days.

Apply that honestly to both sides:

| | Conventional elementary day | 2 Hour Learning day |
|---|---|---|
| Allocated to core academics | ~3.5–5 h (a ~6.5 h day less lunch, recess, transitions and specials) | **2.0 h** |
| Engagement | BTES class averages ~50–90% | engineered: WASTE meter, currency, daily rings |
| High-success fraction | ~50% of engaged time at high success | engineered: explicit 70–95% accuracy band |
| **Implied academic learning time** | **≈1.2–1.75 h** (at the 35% median cascade) | **≈1.5–1.9 h** (if the engineering works as described) |

`INFERENCE`, and the arithmetic is stated so it can be attacked. The conclusion:

> **Two hours of high-engagement, correctly-pitched, individually-placed practice is
> approximately *equal* to the academic learning time a median conventional classroom
> already delivers across a full day. The compression is ~3× on the clock and ~1× on the
> thing that produces learning.**

Three consequences follow, and they are the intellectual core of this section:

1. **The two-hour figure is not extraordinary; it is exactly what §30 predicts, and it is
   at the *low* end of what §30 predicts.** This survey's own bound is 10–40× on elapsed
   calendar and 3–5× on engaged effort. A school that finds 3× on the clock has recovered
   the overhead a school day contains. It has not demonstrated anything about the learner.
   **If Alpha's claim were only "two hours", we would say: yes, obviously, and you could
   probably go further.**
2. **Therefore the two-hour figure cannot explain the attainment claim.** If ALT is roughly
   at parity, then "twice as fast in a third of the time" is not being produced by time
   efficiency. It would have to be produced by **targeting** — Koedinger's 3.6× prior-knowledge
   parameter, which the placement diagnostic directly attacks — or by **selection**. Those
   are the only two candidates left, and the second is uncontrolled.
3. **A large part of "two hours" is definitional.** The day is still 7 hours 45 minutes long.
   Four of those hours are "life skills workshops" — leadership, public speaking,
   entrepreneurship, financial literacy, Socratic discussion, writing-adjacent projects. A
   conventional school would count a substantial slice of that as instruction. **Whether the
   two-hour claim is a compression result or a reclassification result depends entirely on
   how much of the afternoon is academic learning under another name, and no outside party
   has ever observed an Alpha afternoon and coded it.** `OPEN` — nobody asked because it
   requires classroom observation access that a private school need not grant.

**The honest verdict on the headline number: "two hours of academics" is very likely true as
stated, is a real and well-engineered removal of overhead, and is *not* evidence of
accelerated learning.** It is evidence that a school day contains a great deal of
non-learning, which this survey already argued from independent data.

---

## 6. Mapping it against this survey's findings

| This corpus's finding | Does 2 Hour Learning implement it? | Verdict |
|---|---|---|
| **Mastery learning** (Bloom; Keller PSI) | Yes, explicitly and as the load-bearing mechanism. 90% gates, self-pacing, no progression without mastery. | **Yes** — and this is PSI. See §7.1. |
| **A decision rule, not just measurement** (Fuchs & Fuchs 1986/1991: formative measurement without a *prescription* attached is inert) | **Yes.** The Struggle Detector does not merely flag; it injects specific remedial lessons, and the maths path has an explicit fallback rule (return to fact fluency). The WASTE meter is a rule about effort, not a report. | **Yes — and this is the strongest single point in the model's favour.** Most edtech fails precisely here. |
| **Prior knowledge is the 3.6× parameter** (Koedinger et al. 2023, PNAS: learning *rate* varies 1.14×, prior knowledge 3.6×) | Yes. Entry diagnostic, placement by knowledge grade not age grade, "no knowledge gaps" as the stated design goal. | **Yes.** Theoretically, this is the highest-leverage thing a school can do, and it is exactly what they do. |
| **Opportunities, not time** | Partially. Lesson counts and "opportunities" are tracked; but the headline metric sold to parents is *minutes per subject* and *hours per day* — a time-based frame the PNAS result specifically shows is a poor predictor (*"A time-based model, time-AFM, systematically provides poor predictive fit"*). | **Mixed** — the mechanism is opportunity-based; the marketing is time-based. |
| **Retrieval practice** | Partially. AlphaFlash is retrieval by construction; mastery checks are retrieval. But retrieval practice is never named as a principle in any operator document retrieved. | **Incidental, not designed.** |
| **Spacing / distributed practice** | **No evidence.** The white paper's pacing model is *massed*: ~80 consecutive days per grade level, then move on. Nothing in any retrieved document schedules a return to previously mastered material after a delay. The one place spacing appears at all is the 3×/year MAP cycle, which is measurement, not practice. | **Absent — and this is the model's clearest omission against this corpus's own findings.** |
| **Delayed, unassisted, novel-item outcome** (this survey's standing bar) | **No.** Every reported outcome is either (a) in-platform, (b) MAP, taken during the year, or (c) SAT/AP, which are unassisted and novel-item but are *terminal high-school* measures reported without a denominator (how many students, how many sat, who withdrew). No delayed retention measure exists anywhere. | **No.** |
| **Durability does not compress** (§30) | Not addressed. The model's entire time argument is about *acquisition*. Nothing in it addresses whether a grade level mastered in 80 days at 90% survives to the following year, and the assessment loop (MAP each term) would partly detect but never isolate this. | **Not addressed.** |

**The composite judgement.** On the two mechanisms this corpus rates highest — *diagnose and
place on prior knowledge*, and *attach a prescription to every measurement* — the design is
good, arguably better than most of what is in schools. On the two mechanisms this corpus
rates highest for **durability** — *spacing* and *delayed unassisted testing* — it is silent.
That is exactly the profile §30 predicts for a system optimised on acquisition speed:
**the compressible part is compressed, and the incompressible part is not measured.**

---

## 7. The honest comparison

Our standard: **the control must be a real alternative, not nothing.** "Better than a
six-hour day of nothing in particular" is not a finding.

### 7.1 If this is PSI with software, what does PSI predict?

**Kulik, J. A., Kulik, C.-L. C., & Cohen, P. A. (1979), "A meta-analysis of outcome studies
of Keller's personalized system of instruction", *American Psychologist* 34(4), 307–318,
`doi:10.1037/0003-066X.34.4.307`.** `MEASURED-META`. PSI's defining features are exactly
Alpha's: written units in hierarchical order, **a mastery criterion**, **self-pacing**,
**repeatable unit tests**, learning largely **without lectures**, and **proctors** whose job
is administration and encouragement rather than instruction — the ERIC record for PSI
describes precisely this feature list. The meta-analysis found superior final-examination
achievement and **reduced variance in outcomes**, and PSI subsequently disappeared from
higher education for **administrative** reasons — self-pacing collides with semesters,
proctor labour, and procrastination — not evidential ones.

**If this is PSI with the administrative burden automated away, that is a strong prior, and
it should be said plainly: the model should work.** It is the single most credible thing
about the enterprise. What PSI's evidence does *not* predict is a top-1% attainment result
or a 2–6× learning-rate multiplier; it predicts a solid, positive, moderate effect with
lower variance.

### 7.2 What mastery learning's own evidence says — including the part that hurts

- **Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990), "Effectiveness of Mastery
  Learning Programs: A Meta-Analysis", *Review of Educational Research* 60(2), 265–299,
  `doi:10.3102/00346543060002265`.** `MEASURED-META`. 108 controlled evaluations; positive
  effects on examination performance in colleges, high schools and upper-elementary grades.
- **Guskey, T. R., & Gates, S. (1985), *A Synthesis of Research on Group-Based Mastery
  Learning Programs*, ERIC ED262088.** `MEASURED-META`. 38 studies. ERIC abstract, verbatim:
  *"Results show that such applications yield consistently positive effects on both cognitive
  and affective student learning outcomes … However, **variation in the size of the effect
  across studies is quite large.**"* The heterogeneity is the point: mastery learning is a
  family of implementations, not a treatment, and its effect is dominated by which one you
  built.
- **Slavin, R. E. (1987), "Mastery Learning Reconsidered", *Review of Educational Research*
  57(2), 175–213, `doi:10.3102/00346543057002175`.** `MEASURED-META` — **NEGATIVE.** The
  ERIC abstract, verbatim: *"The review found **no evidence to support the claim that mastery
  learning improves student performance on standardized achievement measures**."*

That disagreement is the whole ballgame, and it has a known resolution: **mastery learning's
large effects concentrate on locally-developed tests aligned to the mastered units, and
shrink or vanish on external standardized measures.** Alpha's design sits squarely inside
that pattern — its internal gates (90% on unit and grade tests) are the locally-aligned
measure; MAP is the external one; and MAP is administered by the same organisation. **The
one comparison that would discriminate — the same cohort on an externally administered
standardized test — is the one that does not exist.**

### 7.3 What high-dosage tutoring predicts

**Nickow, A., Oreopoulos, P., & Quan, V. (2020), NBER WP 27476.** `MEASURED-META`, retrieved
in full: *"tutoring programs yield consistent and substantial positive impacts on learning
outcomes, with an **overall pooled effect size estimate of 0.37 SD**. Effects are stronger,
on average, for **teacher and paraprofessional** tutoring programs than for nonprofessional
and parent tutoring."*

0.37 SD is roughly 14 percentile points for a median student. It is a large, real,
expensive effect — and it is delivered by *humans*, with the meta-analysis specifically
finding **weaker** effects for less-professional tutors. Alpha's guides are explicitly not
academic instructors. **The best-evidenced version of "1:1 attention" predicts about 14
percentile points, from people, at high cost. It does not predict the 99th percentile.**

### 7.4 What "personalized learning at scale" actually delivered on this exact instrument

**Pane, J. F., Steiner, E. D., Baird, M. D., Hamilton, L. S., & Pane, J. D. (2017),
*Informing Progress: Insights on Personalized Learning Implementation and Effects*, RAND
RR-2042, `doi:10.7249/RR2042`.** `MEASURED-BENCH` — retrieved in full. Personalized-learning
schools, outcomes **measured on MAP**, against matched virtual comparison groups:

> "We estimated positive treatment effects of approximately **0.09 in mathematics and 0.07
> in reading** … Only the mathematics estimate is statistically significant. These effect
> sizes translate to gains of about **3 percentile points**."

And on the raw percentile trajectory, which is the number most comparable to Alpha's claim:

> "students started the year significantly below national norms in both mathematics and
> reading … In mathematics, students gained about **two percentile points** but remained
> significantly below national norms; in reading, students also gained about **two percentile
> points**."

This is the fairest available comparator: **same instrument, same broad model, independent
evaluator, matched controls.** It produced **2–3 percentile points**. It also has a specific
cautionary history — RAND's own earlier report on an overlapping sample (*Continued Progress:
Promising Evidence on Personalized Learning*, RR-1365, 2015) was markedly more optimistic;
the estimate shrank when the comparison group improved. **That is the single most instructive
precedent in this section: the effect size of "personalized learning" fell as the control got
better.**

### 7.5 What a fair control for Alpha would actually be

Ranked by how much of the claim each would absorb:

1. **A matched-tuition, matched-metro private school** using the same MAP administration and
   the same reporting cadence. This is the control the claim demands and the one that would
   absorb the most.
2. **A high-performing charter with a comparable selected-by-application intake** — nearest
   available public-sector analogue, with the enormous advantage that its results are already
   externally reported.
3. **Homeschooling with an engaged parent and a commercial adaptive curriculum** — matches
   the parental-alignment variable, which the operator itself names as decisive. Alpha
   Anywhere makes this a *within-programme* comparison the operator could run tomorrow.
4. **The same students' own pre-enrolment trajectory** — a within-child interrupted time
   series on prior school records, which the school already collects for every applicant.
   **This is the cheapest credible study in this entire section and it has not been done.**

---

## 8. Precedents and the graveyard

This is not the first claim to have reinvented school. The base rate matters, and it is bad.
Below are **six named negative results** (§8.1–§8.6) against the project's requirement of
three, plus **nine documented precedents** (§8.7) — every one of them retrieved this session,
with the source and HTTP status recorded in §11.

### 8.1 NEGATIVE 1 — Mastery learning itself, on external tests

**Slavin (1987), *Review of Educational Research* 57(2):175–213,
`doi:10.3102/00346543057002175`.** Best-evidence synthesis of group-based mastery learning
in elementary and secondary schools. ERIC abstract, verbatim: *"The review found **no
evidence to support the claim that mastery learning improves student performance on
standardized achievement measures**."* `MEASURED-META`.

Slavin was contested at the time — a companion piece, *"Rethinking Mastery Learning
Reconsidered"*, argued his method was misapplied — and Kulik et al. (1990) reached the
opposite conclusion on 108 evaluations. The reconciliation is the one that matters here:
**the effect is large on locally-aligned tests and small-to-absent on external standardized
ones.** Alpha's internal gates are the first kind. MAP, in Alpha's hands, is somewhere in
between.

### 8.2 NEGATIVE 2 — "Personalized learning" shrank as its control improved

**Pane et al. (2017), RAND RR-2042.** Effects of **0.09 SD** (maths, significant) and
**0.07 SD** (reading, not significant) on **MAP**, ≈ **3 percentile points**, in schools
explicitly built around personalized learning. The predecessor report on an overlapping
sample (RR-1365, 2015) had been read as far more promising. `MEASURED-BENCH`.

**The lesson is methodological, not substantive: the headline effect of personalized
learning is a function of what you compare it to.** Alpha currently compares itself to a
norm table.

### 8.3 NEGATIVE 3 — Virtual charter schools: large, persistent, negative

**CREDO / Mathematica / CRPE (2015), *Online Charter School Study*, Center for Research on
Education Outcomes, Stanford.** Virtual-control-record matched design, 17 states + DC.
Retrieved in full via the Internet Archive (live CREDO URLs all **404**; Wayback capture
**200**, 1.34 MB). Verbatim:

> "Across all tested students in online charters, the typical academic gains for math are
> **−0.25 standard deviations (equivalent to 180 fewer days of learning)** and **−0.10
> (equivalent to 72 fewer days) for reading** … the sizes of the coefficients leave little
> doubt attending an online charter school leads to lessened academic growth for the average
> student."

> "Only **two percent** of the online charter schools outperform their comparison schools,
> **32 percent** perform no differently, and **67 percent** have weaker growth … In math, a
> full **88 percent** of online charter schools had significantly weaker growth than their
> comparison."

> "In math, **none** of the online charter schools had average achievement scores higher than
> their state average."

`MEASURED-BENCH`. **This is the largest and most directly analogous negative result in
education technology, and it is the number the 2 Hour Learning group's online expansion is
betting against.** A −0.25 SD baseline is not a headwind; it is roughly the size of the
largest positive effects anyone in this literature has ever produced, pointing the other way.

**Fitzpatrick, B. R., Berends, M., Ferrare, J. J., & Waddington, R. J. (2020), "Virtual
Illusion", *Educational Researcher* 49(3):161–175, `doi:10.3102/0013189X20909814`.**
Abstract, verbatim: *"We found that students who switched to virtual charter schools
experienced **large, negative effects on mathematics and English/language arts achievement
that persisted over time** and that these effects could not be explained by observed teacher
or classroom characteristics."* `MEASURED-BENCH`. **The numeric effect sizes could not be
retrieved** (SAGE full text **403**; two mirrors gave abstract only) and are therefore not
stated; the paper is used for direction and persistence only.

**Ahn, J., & McEachin, A. (2017), "Student Enrollment Patterns and Achievement in Ohio's
Online Charter Schools", *Educational Researcher*, `doi:10.3102/0013189X17692999`.** ERIC
abstract, verbatim: *"We utilize state data of nearly **1.7 million students in Ohio** … Our
results also show that **students in e-schools are performing worse on standardized
assessments than their peers in traditional charter and traditional public schools**."*
The RAND brief on the same work (RB-9964, 2017) adds: *"Across all subjects and grade spans,
students in e-schools score significantly lower … even when controlling for prior
achievement, previous school attended, and student demographics"*, and — the sentence that
matters most for a model claiming to close gaps — ***"The lowest-performing students fare the
worst in e-schools."*** `MEASURED-BENCH`.

**Cordes, S. (2023), "Cyber versus Brick and Mortar", *Education Finance and Policy*
19(2):361–384, `doi:10.1162/edfp_a_00399`.** Pennsylvania. Abstract, verbatim: *"attending a
cyber charter is associated with almost universally worse outcomes … Students who enroll in
a cyber charter at the beginning of ninth grade are **9.5 percentage points less likely to
graduate, 16.8 pp less likely to enroll in college, and 15.2 pp less likely to persist in a
postsecondary institution beyond one semester**."* `MEASURED-BENCH`.

**Why this is the most relevant precedent of all.** It is the *only* body of evidence in
which "school is replaced by software plus a non-instructional adult" has been measured
externally at scale, because cyber charters are public and therefore *must* report. The
answer, twice, independently, is that it goes badly. The 2 Hour Learning group's expansion
into online delivery — **Alpha Anywhere** and **Unbound Academy** — walks directly into this
literature. **If any part of the group ends up publicly funded and publicly reported, this is
the comparison it will face, and it is the comparison that would finally settle the
question.**

### 8.4 NEGATIVE 4 — One Laptop Per Child, Peru

**Cristia, J., Ibarrarán, P., Cueto, S., Santiago, A., & Severín, E. (2017), "Technology and
Child Development: Evidence from the One Laptop per Child Program", *AEJ: Applied Economics*
9(3), `doi:10.1257/app.20150385`; working paper IZA DP 6401 (2012), retrieved in full.**
Randomised, **319 primary schools** in rural Peru, 15 months. Abstract, verbatim: *"The
program increased the ratio of computers per student from 0.12 to 1.18 in treatment schools.
This expansion in access translated into substantial increases in use of computers both at
school and at home. **No evidence is found of effects on test scores in math and language.**"*

The point estimate, verbatim from the working paper: *"The estimated effect on the average
Math and Language score is **0.003 standard deviations**, and the associated standard error
is **0.055**."* Precision: *"we can rule out effects larger than 0.11 standard deviations."*
Mechanism checks were null on attendance, homework time, motivation and reading habits.
`MEASURED-RCT`.

The canonical demonstration that **device access and software time are not the mechanism**.
2 Hour Learning agrees, in writing — *"Edtech constitutes only 10% of the solution, while 90%
depends on having a motivated student"* — which is both correct and a reason to doubt that
the AI is doing the work the name implies.

### 8.5 NEGATIVE 5 — The self-paced tradition's own cause of death

PSI (the Keller Plan) did **not** die of poor results. Kulik, Kulik & Cohen (1979) found
superior final-exam achievement and reduced outcome variance. It died of self-pacing's
administrative consequences: procrastination, incompletes, and the collision between
unbounded pacing and bounded terms. `MEASURED-META` + `OBSERVED`.

**This is a negative result about *institutions*, not about learning, and it is the one 2
Hour Learning has most plausibly solved** — by automating the proctor, instrumenting
procrastination directly (the WASTE meter *is* a procrastination detector), and running a
motivation apparatus around it. It is the strongest structural argument that this time could
be different, and it should be conceded.

### 8.6 NEGATIVE 6 — The operator's own numbers

Documented in §1.3: the same cohort reported as **3.9×** and **6.5×** on two pages of the
same website; "10x faster gains" in a third property's metadata; a national norm figure
(§2.2) that is wrong by a factor of 2.4 against the document it cites. `OBSERVED` /
`RECOMPUTED`.

**A vendor that cannot keep its own headline number stable across two web pages has not
built a measurement system.** This is a negative result about the *evidence*, and in a
section where every outcome number is `VENDOR`, it is the decisive one.

### 8.7 The wider graveyard

Five more, each with the closest thing to evidence that exists for it.

**AltSchool → Altitude Learning.** Max Ventilla, founded 2013; **~$174 M raised** (Zuckerberg,
Thiel, Powell Jobs, Omidyar, Andreessen among investors); peak **~8 campuses**; tuition
**~$27–28 k**. Reported burn **$30–40 M/year against ~$7 M/year revenue**. Palo Alto and SF
Dogpatch campuses closed at the end of 2017–18 and the Chicago expansion was cancelled; on
**1 July 2019** the company handed its four remaining schools (**240 students**) to Higher
Ground Education, Ventilla stepped down as CEO, and it renamed itself Altitude Learning. In
**January 2021** it sold the learning platform itself and pivoted again to consulting.
Ventilla, in Forbes at the exit: **"We might not be around in five years."**
`OBSERVED` — journalism (Palo Alto Online 2017, Forbes 2019, EdSurge 2021), all retrieved.
**Independent evaluation: none exists.** In six years and $174 M, AltSchool never published a
third-party achievement result. **That is the structural precedent — not the closure, the
absence.**

**Summit Learning (Chan Zuckerberg Initiative).** Five Facebook engineers assigned in 2014;
**$99.1 M** in CZI grants since 2016; a 2016 grant plan projecting **~50,000 schools by 2025**.
Actual peak **~380 schools / 74,000 students** (NYT, April 2019). The decisive facts:

- **Summit paid the Harvard Center for Education Policy Research to design an evaluation in
  2016 and then chose not to participate in it** (NYT, 21 Apr 2019). `OBSERVED`. **An operator
  that commissions an independent study and then declines to run it has told you its own
  estimate of the result.**
- Attrition: Summit stated 10% of schools quit annually; **Chalkbeat recomputed the
  enrolment-weighted figure at 18%, with 25% of schools quitting in their first year**
  (23 May 2019). `OBSERVED`.
- Withdrawals and revolts, all documented: **~100 students walked out** of Brooklyn's
  Secondary School for Journalism (Nov 2018), after which NYC DOE dropped Summit for grades
  11–12; a walkout in **McPherson, Kansas** (Jan 2019) followed by a district survey in which
  **77% of middle-school parents preferred their child not be in a Summit classroom**; a
  sit-in and withdrawals in **Wellington, Kansas**; termination by vote in **Indiana,
  Pennsylvania** after a survey found **70% of students wanted it dropped or made optional**;
  suspension and non-return in **Cheshire, Connecticut**. `OBSERVED` (NYT; New York Post).
- **NEPC (Boninger, Molnar & Saldaña, 2020), *Big Claims, Little Evidence, Lots of Money***:
  expansion proceeded *"despite a lack of transparency and the absence of convincing evidence
  that it can deliver on its promises."* `OBSERVED`.

**Teach to One / New Classrooms — and a correction to this section's own brief.** There is
**no MarGrady 2020 evaluation of Teach to One on New Jersey state tests**; that report does
not exist. The two real studies point in opposite directions and the contrast is the finding:

- **Independent, federally funded, and null.** Ready, Conn, Bretas & Daruwala, *Final Impact
  Results from the i3 Implementation of Teach to One: Math*, CPRE at Teachers College (Jan
  2019). Comparative interrupted time series, **36,158 student-level measurements, 209
  school-by-year cohorts, 5 treatment vs 16 comparison schools in Elizabeth NJ**, seven
  pre-years. Verbatim: *"the TtO estimates for each of the three implementation years were
  **statistically non-significant**"*; year-two estimate slightly **negative**. The authors'
  own honest caveat: *"This heterogeneity … leaves us unable to draw generalizable
  conclusions, positive or negative."* `MEASURED-BENCH`.
- **Vendor-favourable, weaker, and positive.** MarGrady Research (Feb 2019), Gates-funded,
  non-experimental, **NWEA MAP growth** against a national reference group, 14 schools:
  *"scores on the math MAP test for consistently-enrolled TtO students improved sufficiently
  to raise the average school-level percentile by **20 points**"*. `OBSERVED`.

**Read those two together and the whole methodological argument of this section is
reproduced in miniature: on MAP growth, self-selected schools, "consistently-enrolled"
students — a large positive. On the state test states actually hold schools to, with a
comparison group and seven years of pre-trend — nothing.** Alpha reports only the first kind
of number.

**Rocketship and Carpe Diem — the "learning lab" generation.** Rocketship's original model
replaced one credentialed teacher per grade with software and an hourly aide, saving a
reported **$500,000 per school per year**. Education Week commissioned the **California
Department of Education** to compute network-wide proficiency across five years: *"As the
Rocketship charter network has added schools and students, the percentage of its students
scoring proficient on California state tests has **steadily declined**."* The 2012–13
flexible-classroom redesign — also a cost play, at **$200,000/school/year** — produced *"sharp
networkwide test-score drops"* and was rolled back. Rocketship's own leaders conceded the
model scaled *"to nine schools and 5,200 students, before its impact could be rigorously
studied."* `OBSERVED`.

Carpe Diem put students in individual computer cubicles at roughly **50:1** student-to-teacher
ratios (226 students, 5 teachers, 4 aides in Yuma in 2012). Its 2010 marketing results carried
**wrong-to-right answer erasure rates seven times the state average**; passing rates then fell
**10–30%** below that baseline in 2011–12. Indiana's charter board voted **5–1 not to renew**
Carpe Diem Meridian in 2017. The executive who ran the national expansion, on the cause of
death: **"kids just didn't want to enroll, and when they did, they didn't want to stay."**
Surviving campuses removed the cubicles. `OBSERVED`.

**Khan Lab School.** Independent private school, Mountain View CA, founded by Sal Khan;
mastery-based progression, mixed-age grouping, extended day. Tuition for 2026–27, from the
school's own page: **$34,750** (TK–5) and **$38,850** (6–12), plus a $750 registration fee and
a deposit of 10% of tuition. **Published outcome data: none.** No independent evaluation, no
achievement study, no peer-reviewed work. `OBSERVED`. **After a decade, the most
learning-science-literate school-reinvention project in America has published nothing an
outsider can check.** That is the base rate Alpha sits inside, and it is worth noticing that
Alpha publishes *more* than Khan Lab School does — it just publishes it about itself.

**LAUSD's iPad programme (2013–15).** A **$1.3 bn** plan to put a Pearson-loaded iPad in the
hands of ~650,000 students. The number that survives: the district's own first formal
internal evaluation found that **in 245 classrooms, one teacher was using the curriculum.**
The superintendent resigned; the FBI seized documents; the successor cancelled the programme
as unaffordable. **No independent evaluation of learning outcomes was ever produced.**
`OBSERVED`.

**The pattern across the graveyard, stated once.** Every entrant publishes spectacular
internal numbers and no external ones. Every external evaluation ever performed on the
category — RAND on personalized learning (+0.09/+0.07 SD), CPRE on Teach to One (null),
CREDO on virtual charters (−0.25/−0.10 SD), Ahn & McEachin on Ohio e-schools (negative,
worst for the weakest students), Cristia et al. on devices (0.003 SD, SE 0.055) — has
returned a number **between zero and substantially negative**. **The prior on "school
reinvented around software" is not neutral. It is bad. Alpha does not merely have to differ
from it; it has to beat it, and it has not yet produced a number capable of doing so.**

---

## 9. What it would take to believe it

This is the section that has to be specific, because "more research is needed" is not a
standard. Each item below is a `DESIGN`, and each names **what result would show it wrong**.

### 9.1 The minimum credible study — and it is cheap

**`DESIGN` — Within-child interrupted time series on pre-enrolment records.**
Alpha already collects prior school records for every applicant in grades 2–8 and a MAP
score at admission. Take every student enrolled for ≥2 years; fit each child's growth
trajectory on pre-enrolment data; test for a level and slope change at enrolment; model
selection on observables. Pre-register the analysis; have an external statistician hold the
code.
**Falsifier:** no discontinuity in slope at enrolment, or a discontinuity that disappears
once regression-to-the-mean at the admission test is modelled (applicants are tested once,
and a single test score is inflated by measurement error at the moment of selection).
**Why it is the first study:** it costs one analyst and no new data collection, it uses data
the school already holds, and it is the only design that partly controls for selection
*without* a control group. **That it has not been run after eleven years is itself
information.**

### 9.2 The study that would settle attainment

**`DESIGN` — Externally administered, externally scored, matched-comparison assessment.**
An instrument the school does not administer (state assessment under state proctoring; or
NAEP-linked; or an externally proctored ISEE/SSAT sitting with 100% of the cohort, not
volunteers), on **every enrolled student**, with published N, published attrition, and a
comparison group of matched-tuition private-school students in the same metro.
**Falsifier:** cohort mean lands at or below the matched private-school comparison. Note
that "below the national norm" is *not* the falsifier — the relevant counterfactual is a
$40,000 private school, not the nation.
**Report both:** the class/school percentile *and* the student percentile (§2.4). Reporting
only one is the current failure mode.
**And note that a weak version of this study is now running by accident**: Arizona will
publish AASA results and an A–F grade for **Unbound Academy** (§3.5). It is the online,
teacher-led variant, so it does not test the flagship model — but it is the first
externally-scored number this group will ever have, and the way its results are received will
tell us how much of the claim was ever meant to be checkable.

### 9.3 The study that would settle growth

**`DESIGN` — NWEA conditional growth percentiles, reported directly, at cohort level.**
NWEA already computes exactly the statistic in question: the **Conditional Growth Percentile
/ Conditional Growth Index**, which asks "did this student grow more than similar students
with the same starting status, in the same grade, over the same interval?" It is in every
MAP report the school already receives.
**Falsifier:** cohort mean CGP at or near 50.
**Why this is decisive:** it requires no new testing, no new consent, no control group, and
no methodology invention. It replaces a home-made multiplier with the vendor's own published,
peer-reviewed-adjacent statistic. **The fact that the operator publishes a bespoke "times
growth" number instead of the CGP its own reports contain is the most consequential
methodological choice in this entire case.**

### 9.4 This survey's standing bar

**`DESIGN` — A delayed, unassisted, novel-item outcome.**
Cohort tested **≥8 weeks after** the relevant material was mastered, **without** the
platform, on items **not** drawn from the training distribution, scored blind.
**Falsifier:** retention below a matched conventional cohort at the same delay — which §30
of this survey predicts is a live possibility, because the model's pacing is *massed*
(≈80 consecutive days per grade level) and contains no scheduled return to mastered material.
**This is the bar every vendor in this corpus is held to, and it is the bar under which the
two-hour claim is most at risk**, because acquisition speed and retention are the two
quantities §30 says behave completely differently.

### 9.5 The disclosures that cost nothing

| Disclosure | Why it settles something |
|---|---|
| Student-level vs school-level percentile | ±10 percentile points (§2.4) |
| Denominator of "x faster", stated arithmetically | The whole of §2.2–2.3 |
| N per reported figure | "7 boys" and "all students" currently carry equal typographic weight |
| Year-on-year retention, and mid-year withdrawal | Cohort-mean percentiles are inflated by attrition; no figure exists |
| Fraction of enrolled students included in each reported statistic | Distinguishes a cohort result from a highlight reel |
| Test administration conditions and rapid-guessing rates | NWEA flags disengagement as a validity threat in its own norms |

### 9.6 The positional caveat, which no study can remove

**Percentile rank is zero-sum by construction.** "Top 1% nationally" is a claim about
*other people's children*. It cannot generalise: if 2 Hour Learning were adopted by every
school in the United States, the fraction of students in the top 1% would be **1%**. The
scalable version of the claim has to be stated in criterion terms — *this fraction of
students can do this specific thing by this age* — and no such claim has been published.
`INFERENCE`.

This matters more than it sounds. A school selling positional advantage to families paying
$75,000 has a business model that **works better the less the method spreads.** The
incentive to publish a replicable protocol runs backwards.

---

## 10. Open questions

| # | `OPEN` | Why nobody asked |
|---|---|---|
| 1 | **Attrition.** No retention or withdrawal figure exists in any operator material. | No one has standing to compel a private school, and cohort-mean percentiles on survivors are exactly the statistic attrition flatters. |
| 2 | **Are the percentiles student-level or school-level?** | The distinction is invisible to a lay reader and costs nothing to leave open. |
| 3 | **What is the practice-effect size of taking MAP 3×/year inside a platform structurally similar to MAP?** | Detecting it requires an external instrument, which is the thing that does not exist. |
| 4 | **Does mastery at 90% survive to the next year?** | The assessment loop measures current status three times a year; nothing isolates decay of previously mastered material. |
| 5 | **What do the "guides" actually do, minute by minute?** | Never observed by an outside party in any retrieved source; every description is the operator's. |
| 6 | **What happens to a student for whom the model is in the 10–20% it "may not be suitable" for?** | The operator states the fraction and never states the disposition. |
| 7 | **What is the actual content coverage?** ~40 hours per grade per subject is asserted; against what scope-and-sequence, aligned to what standard, verified by whom? | No external curriculum audit has been published; accreditation reviews process, not content mastery. |
| 8 | **Is there any measurement of writing, or of any construct MAP cannot score?** | MAP is multiple-choice adaptive; the model's assessment loop is built around what MAP measures. Extended writing, argument, and open-ended problem solving are absent from every reported outcome. |

---

## 11. Source reachability log

**Retrieved successfully (HTTP 200):** `alpha.school` (home, FAQ, admission, Austin,
Brownsville, NYC, guides, overview, parent-survey, 2-hour-learning, founders, sitemaps, and
10 campus tuition pages); `2hourlearning.com` (home, results, challenge, schools, sitemaps);
the **2 Hour Learning white paper PDF** (2.34 MB) via `cdnc.heyzine.com` from the flipbook at
`heyzine.com/flip-book/2hourlearning.html`; `gt.school`; `timeback.com`; `timeback.app`;
`unbound.school`; `unbound.academy` (placeholder); `joinprequel.com`; `cognia.org` WordPress
REST API and the Alpha School community story; **NWEA `teach.mapnwea.org/impl/normsResearchStudy.pdf`
(4.45 MB, the 2020 norms technical report)** and `MAPGrowthNormativeDataOverview.pdf`; NBER
`w27476.pdf`; RAND `RAND_RR2042.pdf`; `404media.co` (lede + podcast page); `kgou.org`
(Oklahoma Watch syndication); Crossref, OpenAlex, Semantic Scholar, ERIC APIs.

**Blocked, failed, or paywalled:**

| Source | Status | Note |
|---|---|---|
| `techrxiv.org` full text of the Alpha School case study | **403** | preprint metadata only, via OpenAlex |
| `404media.co` article body | **200 + paywall** | only the free lede is quoted; nothing else asserted |
| `asbcs.az.gov` (Arizona State Board for Charter Schools) | **403** (curl and WebFetch) | Unbound Academy regulatory status not verified directly here |
| `online.asbcs.az.gov` | **000** (TLS chain failure) | |
| `azed.gov` | **403** | |
| `tepsac.org` (Texas Private School Accreditation Commission) | **000** (timeout, 45 s) | accreditation registry not reached |
| `tea.texas.gov` private-schools page | **404** | |
| `cognia.org/find-a-school/` | **404** | institution search not reachable |
| `api.cognia.org`, `certification.cognia.org` | **DNS failure** | |
| CREDO *Online Charter School Study* (2015) PDF, five live URLs | **404** | **recovered in full from the Internet Archive (HTTP 200, 1.34 MB)** and quoted verbatim in §8.3 |
| Fitzpatrick et al. (2020) full text, `journals.sagepub.com` | **403** | two mirrors gave abstract only; **numeric effect sizes not obtained and not stated** |
| MarGrady "2020 Teach to One state-test evaluation" | **404 — does not exist** | the brief's premise was wrong; the real i3/CPRE evaluation (null) and the real MarGrady report (Feb 2019, MAP growth, positive) are both used, and the discrepancy is the finding |
| `nytimes.com`, `latimes.com`, `npr.org`, `nypost.com`, `edweek.org` direct | **403 / refused / timeout** | all recovered via the Internet Archive, HTTP 200 |
| `washingtonpost.com`, `fastcompany.com`, `the74million.org` (Summit walkout coverage) | **403** | not used; the same events are carried by NYT and NY Post |
| SRI *Rocketship middle-school outcomes* interim brief | **200** | design read; **achievement point estimates not extracted, and no direction is claimed from it** |
| Alpha `/tuition/` | **404** | tuition is on campus pages only |
| `alpha.school` pages under a short user-agent | **403** | full browser UA required; noted so the retrieval is reproducible |
| GDELT DOC API | **429** on ~60% of calls | one request per 6 s enforced; coverage window short |
| `nwea.org` 2025 norms tables (four candidate URLs) | **404** | the **2020** norms are used throughout, which is also the edition the white paper cites |
| `penncapital-star.com` (PDE denial report) | **403** | content corroborated through Mathworlds and Chalkbeat, both retrieved in full |
| `azreportcards.azed.gov` search UI | **200, no data** | search interface only |
| `azreportcards.azed.gov/api/Search/GetByName?name=Unbound` and `/Schools/Detail/1002640` | **200 / 200** | entity registered (IDs 1002639 / 1002640, "Charter School" + "Online School"); **no AASA results, no A–F grade published** |
| NCES Common Core of Data, AZ directory SY2023-24 and SY2024-25 (Urban Institute API) | **200** | **zero matches** for Unbound / Novatio / Alpha — consistent with no operating year yet |
| `asbcs.az.gov`, `online.asbcs.az.gov`, `www.azed.gov` | **403 / 000 / 403** | Cloudflare; charter contract, enrolment cap and opening date **not obtained**; Wayback CDX returned zero matching rows |
| ProPublica Nonprofit Explorer / IRS BMF (7 queries) | **200** | only `Unbound Academic Institute` EIN 33-3639402 exists; **zero Form 990s**; nothing for 2 Hour Learning, Trilogy, Legacy of Education |
| SEC EDGAR full-text (`efts.sec.gov`) | **200** (500 on one query) | **no filings, no Form D** for any group entity |
| `wired.com` | **WebFetch refused; curl 200** | both investigations retrieved in full via curl |
| `oktaxcredit.ok.gov`, Texas Comptroller ESA school database | **000 / 404** | approved-school lists not obtained directly |
| Oklahoma Watch follow-up (23 Jul 2026) body | **429** | headline only |
| Hechinger Report site search | **200 — "Nothing Found"** | **confirmed zero coverage**, recorded because absence is informative |
| The 74 article body | **403** | not used |
| "Liemandt committed $1 billion" | **not traceable** | nearest item is a Forbes headline about net worth; **figure not restated** |
| Summit Learning, Khan Lab School, Teach to One, Rocketship, Carpe Diem evaluations | **not retrieved** | GDELT 429; no primary evaluation reached. **No figure for any of them appears in this report.** |
| NYT, Austin American-Statesman, Houston Chronicle article bodies | **not read** (subscription) | referenced only for the existence and date of the event; no content restated |

**Retrieved late and used**: `danmeyer.substack.com` (**200**, full text), `chalkbeat.org`
(**200**, full text), `buckscountybeacon.com` (**200**, full text), `unbound.school/program`
(**200**), `en.wikipedia.org` action API (**200**, used as a citation index only).

**Not attempted / out of scope:** any attempt to obtain non-public student data, enrolment
records, or internal documents.

---

## 12. Bibliography

**Primary operator documents (all `VENDOR`)**

1. 2 Hour Learning, *Welcome to the Future of Education: Transforming Classrooms & Unlocking Potential with AI-Powered Mastery Learning* (white paper, 27 pp., undated; content references the 2023/24 school year). Retrieved as PDF from the `heyzine` flipbook linked at `2hourlearning.com`. **[FT]**
2. `alpha.school` — FAQ, Admission, Austin, Brownsville, New York City, Guides, Overview, End of 2025 Parent Survey Results, campus tuition pages (10 retrieved). Accessed 2026-07-29.
3. `2hourlearning.com` — Home, Results, Challenge, Schools. Accessed 2026-07-29.
4. `gt.school`; `timeback.com`; `timeback.app`; `unbound.school`; `unbound.academy`; `joinprequel.com`. Accessed 2026-07-29.

**Primary measurement documents**

5. **Thum, Y. M., & Kuhfeld, M. (2020).** *NWEA 2020 MAP Growth Achievement Status and Growth Norms for Students and Schools.* NWEA Research Report, Portland OR. Norming sample Fall 2015–Spring 2018; >11 M unique students in reading and mathematics. Tables used: **C.1.1/C.1.3** (Fall/Spring Mathematics Student Achievement Percentiles), **C.1.4/C.1.6** (Reading), **C.2.3/C.2.6** (School Achievement Percentiles), **Appendix E.1/E.2** (Conditional Growth Distributions, all intervals). **[FT — parsed programmatically]**
6. Cognia, *"Alpha School: Accreditation Boosts Excellence in a New Pedagogical Approach"* (community story). `cognia.org/insights/alpha-school-community-story/`. **[FT]**

**Peer-reviewed and evaluation literature**

7. Bloom, B. S. (1984). *The 2 Sigma Problem.* **Educational Researcher** 13(6):4–16. `doi:10.3102/0013189X013006004`.
8. Kulik, J. A., Kulik, C.-L. C., & Cohen, P. A. (1979). *A meta-analysis of outcome studies of Keller's personalized system of instruction.* **American Psychologist** 34(4):307–318. `doi:10.1037/0003-066X.34.4.307`. `MEASURED-META`.
9. **Slavin, R. E. (1987).** *Mastery Learning Reconsidered.* **Review of Educational Research** 57(2):175–213. `doi:10.3102/00346543057002175`. **NEGATIVE.** `MEASURED-META`. **[AB — ERIC EJ record, verbatim]**
9b. Guskey, T. R., & Gates, S. (1985). *A Synthesis of Research on Group-Based Mastery Learning Programs.* ERIC **ED262088**. 38 studies; consistently positive but highly heterogeneous effects. `MEASURED-META`. **[AB — ERIC record, verbatim]**
10. Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). *Effectiveness of Mastery Learning Programs: A Meta-Analysis.* **Review of Educational Research** 60(2):265–299. `doi:10.3102/00346543060002265`. 108 controlled evaluations. `MEASURED-META`. **[AB]**
11. **Nickow, A., Oreopoulos, P., & Quan, V. (2020).** *The Impressive Effects of Tutoring on PreK-12 Learning.* NBER WP 27476. `doi:10.3386/w27476`. Pooled **0.37 SD**. `MEASURED-META`. **[FT]**
12. **Pane, J. F., Steiner, E. D., Baird, M. D., Hamilton, L. S., & Pane, J. D. (2017).** *Informing Progress: Insights on Personalized Learning Implementation and Effects.* RAND RR-2042. `doi:10.7249/RR2042`. **0.09 / 0.07 SD on MAP ≈ 3 percentile points.** `MEASURED-BENCH`. **[FT]**
13. Pane, J. F., Griffin, B. A., McCaffrey, D. F., & Karam, R. (2014). *Effectiveness of Cognitive Tutor Algebra I at Scale.* **EEPA** 36(2):127–144. `doi:10.3102/0162373713507480`.
14. **Fitzpatrick, B. R., Berends, M., Ferrare, J. J., & Waddington, R. J. (2020).** *Virtual Illusion.* **Educational Researcher** 49(3):161–175. `doi:10.3102/0013189X20909814`. **NEGATIVE.** `MEASURED-BENCH`. **[AB — verbatim]**
15. **Cordes, S. (2023).** *Cyber versus Brick and Mortar.* **Education Finance and Policy** 19(2):361–384. `doi:10.1162/edfp_a_00399`. **NEGATIVE.** `MEASURED-BENCH`. **[AB — verbatim]**
16. **Cristia, J., Ibarrarán, P., Cueto, S., Santiago, A., & Severín, E. (2017).** *Technology and Child Development: Evidence from the One Laptop per Child Program.* **AEJ: Applied Economics** 9(3):295–320. `doi:10.1257/app.20150385`. **NEGATIVE, randomised, 318 schools.** `MEASURED-RCT`. **[AB — verbatim]**
16b. **CREDO / Mathematica / CRPE (2015).** *Online Charter School Study 2015.* Center for Research on Education Outcomes, Stanford. Recovered via the Internet Archive. **−0.25 SD math (≈180 fewer days), −0.10 SD reading (≈72 fewer days); 67% of online charters weaker, 88% weaker in math; 2% outperform.** `MEASURED-BENCH`. **[FT]**
16c. Gill, B., Walsh, L., Smither Wulsin, C., et al. (2015). *Inside Online Charter Schools.* Mathematica Policy Research. ERIC **ED560967**. **[FT]**
16d. **Ahn, J., & McEachin, A. (2017).** *Student Enrollment Patterns and Achievement in Ohio's Online Charter Schools.* **Educational Researcher.** `doi:10.3102/0013189X17692999`. ~1.7 M Ohio students. **NEGATIVE.** Companion: RAND RB-9964. `MEASURED-BENCH`. **[AB + brief FT]**
16e. **Ready, D., Conn, K., Bretas, S., & Daruwala, I. (2019).** *Final Impact Results from the i3 Implementation of Teach to One: Math.* CPRE, Teachers College, Columbia University. CITS, 36,158 measurements, 5 vs 16 schools, 7 pre-years. **NULL.** `MEASURED-BENCH`. **[FT]**
16f. MarGrady Research (Feb 2019). *Three-Year MAP Growth at Teach to One Schools.* Non-experimental, MAP growth, 14 schools; **+20 school-level percentile points**. `OBSERVED` — included as the *contrast* to 16e, not as a finding.
16g. Boninger, F., Molnar, A., & Saldaña, C. (2020). *Big Claims, Little Evidence, Lots of Money: The Reality Behind the Summit Learning Program…* National Education Policy Center. `OBSERVED`.
17. Wilson, R. C., Shenhav, A., Straccia, M., & Cohen, J. D. (2019). *The Eighty Five Percent Rule for optimal learning.* **Nature Communications** 10:4646. `doi:10.1038/s41467-019-12552-4`.
18. Fisher, C. W., Berliner, D. C., Filby, N. N., Marliave, R., Cahen, L. S., & Dishaw, M. M. (1980). *Teaching Behaviors, Academic Learning Time, and Student Achievement* (BTES). ERIC **ED192454**. — carried from this project's K1 report.
19. Koedinger, K. R., Carvalho, P. F., Liu, R., & McLaughlin, E. A. (2023). *An astonishing regularity in student learning rate.* **PNAS**. PMC10068755. — carried from K1.

**Non-peer-reviewed items naming the subject (listed for completeness; used for nothing)**

20. Choi, W. C., & Chang, C. I. (2026). *Can AI Replace Teachers? … A Case Study of Alpha School.* TechRxiv preprint. `doi:10.36227/techrxiv.177220375.51273405/v1`. Full text **403**.
21. Waford, L. D. (2025). *Skinner's Vision Realized: AI and the Future of Education.* Zenodo preprint. `doi:10.5281/zenodo.17707250`.

**Journalism**

22. Maiberg, E. (17 Feb 2026). *"Students Are Being Treated Like Guinea Pigs" Inside an AI-Powered Private School.* **404 Media**. Free lede only; body paywalled. `OBSERVED`.
23. Oklahoma Watch / KGOU (20 July 2026). *A $40,000-per-year AI school with no teachers is opening in Oklahoma this August.* `OBSERVED`.
24. **Meyer, D. (8 Jan 2025, updated 26 Mar 2025).** *The Truth About 2 Hour Learning, Unbound Academy, and Alpha School a/k/a The School "Replacing Teachers with AI".* **Mathworlds** (`danmeyer.substack.com`). **Retrieved in full, HTTP 200.** The only retrieved third-party analysis that reads the primary charter applications. Quotes the Pennsylvania denial: *"deficiencies in all five of the required criteria."* `OBSERVED`. **[FT]**
25. **Sitrin, C. (24 Jan 2025).** *Two AI-powered charter schools could soon open in Pennsylvania.* **Chalkbeat Philadelphia.** **Retrieved in full, HTTP 200.** Source for the Pennsylvania application's staffing, 90% projected retention, and the **"top half of all Pennsylvania schools"** year-two projection. `OBSERVED`. **[FT]**
26. **Greene, P. (17 Jan 2025).** *Texas Businesswoman Wants to Open AI-Driven, Teacherless Cyber Charter School in Pennsylvania.* **Bucks County Beacon.** **Retrieved in full, HTTP 200.** Source for governance structure (2 Hour Learning / Trilogy / Crossover / ESW Capital) and for Price's own statement that "AI" here means IXL/Khanmigo-class adaptive apps, not an LLM. `OBSERVED`. **[FT]**
27. Karbal, I. (29 Jan 2025). *State rejects application for cyber charter school with AI teacher and two hours of daily class.* **Pennsylvania Capital-Star.** Direct retrieval **403**; content corroborated via (24) and (25). `OBSERVED`.
28. Salhotra, P. (27 Jul 2025). *Alpha School, AI-Driven Education Founded in Austin, Is Coming to More Cities.* **New York Times.** Cited via citation index; **body not read**; nothing restated from it.
29. Heath, K. (16 Jan 2026), *Austin American-Statesman*; Yu, I. & Sander, E. (4 Feb 2026), *Houston Chronicle* — Texas voucher programme and Cognia-only accreditation. Cited via citation index; **bodies not read**; nothing beyond the headline fact restated.
30. Cobler, N. (28 May 2024), *Axios Austin*; Farrell, J. (31 Jul 2025), *WFAE*; Suri, Z. (25 Aug 2025), *KUT/Texas Standard*; NBC Bay Area (25 Jul 2025) — campus-expansion coverage, used only for the existence and grade span of campuses.
31. *Alpha School*, English Wikipedia (accessed 2026-07-29) — used **only as a citation index** to locate items 24–30 and the AltSchool record. **No claim in this section rests on it.**

**Investigations and regulator-quoting reports on the subject**

31a. **Feathers, T. (27 Oct 2025).** *Parents Fell in Love With Alpha School's Promise. Then They Wanted Out.* **WIRED.** Retrieved in full via curl, HTTP 200. **Source for IXL's termination statement**, the Brownsville remediation-loop account, and the head of school's "don't do any teaching". `OBSERVED`. **[FT]**
31b. **Feathers, T. (4 Jun 2026).** *Alpha School's Ritzy New York City Campus Costs $65,000 a Year—but Isn't Actually a School.* **WIRED.** HTTP 200. **Source for the NYSED refusal quote**, the internal Trilogy priority-order documents, and the Miami-Dade Fire Rescue confirmation. `OBSERVED`. **[FT]**
31c. **Astral Codex Ten (27 Jun 2025).** *Your Review: Alpha School.* HTTP 200. Insider parent account. **Source for the GT School n=5 finding** and per-campus enrolments. `OBSERVED`. **[FT]**
31d. **The Lever (24 Jun 2025).** *The Headmaster Of The AI Apocalypse.* HTTP 200. Ownership chain: Legacy of Education → Alpha School + 2 Hour Learning; Trilogy holds the patent; YYYYY, LLC and ~$2 M in grants to charter applicants. `OBSERVED`. **[FT]**
31e. **Henry, M. (21 Jul 2026).** *A $40,000-per-year AI school with no teachers is opening in Oklahoma this August.* **Oklahoma Watch.** HTTP 200. Oklahoma Tax Commission list removal; Edmond/Tulsa enrolments. `OBSERVED`. **[FT]**
31f. **Heath, K. (16 Jan 2026).** *Dozens of Austin private schools shut out of Texas voucher program. Here's why.* **Austin American-Statesman.** HTTP 200. `OBSERVED`. **[FT]**
31g. ProPublica Nonprofit Explorer API (IRS Business Master File) and SEC EDGAR full-text search, 9 queries, 2026-07-29. **Primary databases.**
31h. Arizona Department of Education, **AZ School Report Cards API** (`azreportcards.azed.gov/api/Search/GetByName`) and NCES Common Core of Data via the Urban Institute Education Data API. **Primary / regulator.**
31i. Texas Observer (18 Jul 2023). *$1M Donation to Glenn Youngkin Linked to Associates of Austin Area Billionaire Investor.* `OBSERVED`.

**Graveyard journalism (all retrieved; Internet Archive where marked)**

32. Kadvany, E. (10 Nov 2017). *AltSchool Palo Alto to close at end of year.* **Palo Alto Online.** HTTP 200.
33. Adams, S. (1 Jul 2019). *Zuckerberg-Backed AltSchool Gives Up On Schools And Focuses On Tech.* **Forbes.** HTTP 200. Source for $174 M, campus count, 240 students, "We might not be around in five years."
34. Wan, T. (15 Jan 2021). *The Edtech Company Formerly Known as AltSchool Sold Its Tech. So What's Left?* **EdSurge.** HTTP 200.
35. Bowles, N. (21 Apr 2019). *Silicon Valley Came to Kansas Schools. That Started a Rebellion.* **New York Times** (via Internet Archive, HTTP 200). Source for the Harvard CEPR study Summit declined, and the Kansas/Connecticut/Pennsylvania withdrawals.
36. Barnum, M. (23 May 2019). *Summit Learning … says 10% of schools quit each year. The real figure…* **Chalkbeat.** HTTP 200. Enrolment-weighted 18%; 25% first-year quit.
37. Edelman, S. (10 Nov 2018). *Brooklyn students hold walkout in protest of Facebook-designed online program.* **New York Post** (via Internet Archive, HTTP 200).
38. Herold, B. (21 Jan 2014). *Growing Pains for Rocketship's Blended-Learning Juggernaut.* **Education Week** (via Internet Archive, HTTP 200). Includes the California Department of Education proficiency series.
39. Herold, B. (21 Feb 2019). *Teach to One … Has No Effect on Students' Math Scores, Federal Evaluation Finds.* **Education Week.** HTTP 200.
40. Safier, D. (19 Jun 2017). *Carpe Diem Charters Are Failing to Seize the Day.* **Tucson Weekly.** HTTP 200. Erasure rates 7× state average; Indiana non-renewal 5–1.
41. Hechinger Report. *Students sat in cubicles using computers. It wasn't popular.* HTTP 200.
42. Khan Lab School, *Tuition & Affordability* (2026–27). HTTP 200. $34,750 / $38,850 + fees.
43. Blume, H. (21 Feb 2017). *No charges in LAUSD iPad probe.* **Los Angeles Times** (via Internet Archive, HTTP 200); Gilbertson, A. (27 Aug 2014). *The L.A. School iPad Scandal: What You Need To Know.* **NPR** (via Internet Archive, HTTP 200).
