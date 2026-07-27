---
title: "Safety, Privacy, and Children — What Must Never Be Built"
wave: F
date_researched: 2026-07-27
sources_count: 47
---

# F8 — Safety, Privacy, and Children: What Must Never Be Built

**Evidence labels used throughout**

| Label | Meaning |
|---|---|
| `[VERBATIM]` | Text quoted directly from the primary source retrieved in this session |
| `[VERIFIED]` | Source retrieved and read this session; paraphrased |
| `[SECONDARY]` | Fact reported by a source other than the originating body |
| `[INFERENCE]` | My reasoning from verified primitives — *not* asserted by any source |
| `[NEGATIVE]` | Null, contrary, or expectation-disconfirming result |
| `[UNVERIFIED-IN-SESSION]` | Source unreachable; claim flagged, not guessed |

**Source reachability log (this session).** `eur-lex.europa.eu` returned HTTP 202 with a zero-byte body for CELEX:32024R1689; AI Act text was therefore verified against `artificialintelligenceact.eu` (Future of Life Institute's clause-by-clause rendering), which is a faithful but *secondary* rendering — treated as `[VERIFIED]` not `[VERBATIM-PRIMARY]`. `ftc.gov` was **reachable** via `curl` with a browser User-Agent (contrary to the prior run's 403) and is cited directly. `ofcom.org.uk` returned a Cloudflare interstitial (403). `commonsensemedia.org` returned 403. `childwelfare.gov` returned 404 on the mandatory-reporter path. `pnas.org` returned 403 (routed via EuropePMC instead). Semantic Scholar and OpenAlex APIs returned HTTP 429 for most of the session; arXiv, Crossref, ERIC, and EuropePMC APIs worked.

---

## 0. The one-paragraph thesis

Every claim in this document converges on a single structural fact: **an adaptive tutor is not a content product, it is a regulated psychometric instrument that holds a sensitive dossier on a child.** The EU AI Act classifies it high-risk the moment it steers learning; COPPA's 2025 amendments now cover the biometric and voice data a multimodal tutor collects; FERPA makes the school, not the vendor, the data controller; IDEA makes disability records destroyable on parental demand; and a system that a child talks to daily will, statistically, receive a disclosure of abuse. inBloom proved that none of this is won on the merits of the data model. **It is won or lost on custody.** The prohibitions below are not risk-management garnish — several of them are the difference between a lawful product and an unlawful one, and one of them (a safeguarding escalation path) is the difference between a product and a liability.

---

## 1. The regulatory floor

### 1.1 EU AI Act — the binding constraint

#### 1.1.1 Annex III(3)(b): steering learning is high-risk — verbatim

Annex III chapeau `[VERIFIED]`:

> "High-risk AI systems pursuant to Article 6(2) are the AI systems listed in any of the following areas:"

Annex III, point 3 — **Education and vocational training** `[VERIFIED]` (https://artificialintelligenceact.eu/annex/3/):

> **(a)** "AI systems intended to be used to determine access or admission or to assign natural persons to educational and vocational training institutions at all levels"
>
> **(b)** "AI systems intended to be used to evaluate learning outcomes, including when those outcomes are used to steer the learning process"
>
> **(c)** "AI systems intended to be used for assessing the appropriate level of education that an individual will receive or will be able to access, in the context of or within educational and vocational training institutions"
>
> **(d)** "AI systems intended to be used for monitoring and detecting prohibited behaviour of students during tests in the context of or within educational and vocational training institutions"

**Reading of 3(b) `[INFERENCE]`.** The operative verb is *evaluate*, and the "including when" clause extends — rather than narrows — the trigger. A system that evaluates learning outcomes is high-risk. A system that evaluates learning outcomes *and then uses that evaluation to select what the learner sees next* is unambiguously in scope. That is the definition of an adaptive tutor. There is no "formative assessment" exemption, no "it's only a suggestion" exemption, and no "the teacher is still in the loop" exemption on the face of 3(b). Note also that 3(b) is not textually limited to institutional settings the way 3(c) and 3(d) are ("in the context of or within educational and vocational training institutions") — a direct-to-consumer tutor that grades a child's work and adapts appears to fall under 3(b) on the plain text. `[INFERENCE — this asymmetry is visible in the quoted text but I found no authoritative guidance construing it; treat as a litigable question, not settled law.]`

3(d) independently captures **AI proctoring** — see §6.

#### 1.1.2 Article 6(3): the derogation, and why a learner model destroys it

Article 6(3) `[VERIFIED]` (https://artificialintelligenceact.eu/article/6/) exempts an Annex III system that "does not pose a significant risk of harm" because it:

- **(a)** "is intended to perform a narrow procedural task"
- **(b)** "is intended to improve the result of a previously completed human activity"
- **(c)** "is intended to detect decision-making patterns or deviations from prior decision-making patterns and is not meant to replace or influence the previously completed human assessment, without proper human review"
- **(d)** "is intended to perform a preparatory task to an assessment"

**And then the killer clause:** a system "shall always be considered to be high-risk where the AI system performs profiling of natural persons." `[VERIFIED]`

**This is the single most important sentence in this document for anyone building a learner model `[INFERENCE]`.** GDPR Art. 4(4) defines profiling as automated processing to evaluate personal aspects, in particular to analyse or predict performance, interests, reliability, or behaviour. A learner model — a persistent, per-child representation of mastery, misconception, pace, and predicted next-best-action — *is* profiling under that definition. **Therefore: no product that maintains a learner model can escape high-risk classification via Article 6(3), no matter how narrow its task framing.** The escape hatch is closed by the very artefact that makes the product valuable. Any roadmap that assumes "we'll argue we're a narrow procedural tool" is building on sand.

Article 6(4) `[VERIFIED]`: a provider that *believes* it falls in the derogation must **document that assessment before placing on the market, and still register the system**. Self-exemption is not silent.

#### 1.1.3 Article 5: what is outright prohibited

Article 5(1) `[VERIFIED]` (https://artificialintelligenceact.eu/article/5/):

- **5(1)(a)** — prohibits "an AI system that deploys subliminal techniques beyond a person's consciousness or purposefully manipulative or deceptive techniques" that materially distort behaviour and cause significant harm.
- **5(1)(b)** — prohibits an AI system "that exploits any of the vulnerabilities of a natural person or a specific group of persons **due to their age, disability** or a specific social or economic situation" so as to materially distort behaviour and cause significant harm. `[VERBATIM, emphasis added]`
- **5(1)(f)** — prohibits "the placing on the market, the putting into service for this specific purpose, or the use of **AI systems to infer emotions of a natural person in the areas of workplace and education institutions**", with a narrow exception for medical or safety reasons. `[VERBATIM, emphasis added]`
- **5(1)(g)** — prohibits biometric categorisation to infer race, political opinions, trade union membership, religious or philosophical beliefs, sex life, or sexual orientation.

**The critical scoping nuance on 5(1)(f) `[VERIFIED + INFERENCE]`.** Article 3(39) defines an "emotion recognition system" as "an AI system for the purpose of identifying or inferring emotions or intentions of natural persons **on the basis of their biometric data**." Article 3(34) defines biometric data as "personal data resulting from specific technical processing relating to the physical, physiological or behavioural characteristics of a natural person, such as facial images or dactyloscopic data." `[VERBATIM]`

So:
- **Webcam-based frustration/boredom/engagement detection in a tutor → almost certainly prohibited outright.** Not high-risk. *Prohibited.* Applicable since 2 February 2025.
- **Voice-affect detection from a spoken tutoring session → prohibited** (voice is biometric data under 3(34), and COPPA now agrees — see §1.2).
- **"Sensor-free" affect detection from clickstream and response-latency alone** — the dominant technique in the learning-analytics literature (ERIC ED537205, *Towards Sensor-Free Affect Detection in Cognitive Tutor Algebra*, 2012; ED599173, *Active Learning for Student Affect Detection*, 2019; ED560878, *Video-Based Affect Detection*, 2015) `[VERIFIED]` — sits in a genuine grey zone. Clickstream is arguably "behavioural characteristics... resulting from specific technical processing", which would pull it into 3(34) and thus into the 5(1)(f) prohibition. `[INFERENCE — I found no authoritative construction of this boundary in this session. This is the sharpest open legal question in the whole area and it determines whether an entire subfield of AIED is lawful in the EU.]`

**Design consequence `[INFERENCE]`:** build affect *response* without affect *inference*. A tutor may respond to an explicit learner signal ("I'm stuck", "this is boring") and to behavioural facts (three wrong answers, 40s idle). It must not maintain a variable named `frustration_level`. The distinction is not cosmetic: it is the difference between a feature and a prohibited practice.

#### 1.1.4 Obligations that follow from high-risk classification

For a **provider** (Chapter III, Section 2 — Arts. 8–15, not individually fetched this session, `[UNVERIFIED-IN-SESSION for exact wording]`, but the structure is: risk management system, data governance, technical documentation, automatic logging, transparency to deployers, human oversight design, accuracy/robustness/cybersecurity; plus conformity assessment, EU database registration, post-market monitoring, and serious-incident reporting).

For a **deployer** (a school, district, or tutoring provider) — Article 26 `[VERIFIED]`:

| ¶ | Obligation |
|---|---|
| 26(1) | "Deployers of high-risk AI systems shall take appropriate technical and organisational measures to ensure they use such systems in accordance with the instructions for use" `[VERBATIM]` |
| 26(2) | "Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support." `[VERBATIM]` |
| 26(5) | Monitor operation; inform provider and market surveillance authority of emergent risk; **immediately** notify on a serious incident |
| 26(6) | **Retain system-generated logs for a minimum of six months** |
| 26(8) | Public authorities must register the system in the EU database |
| 26(11) | Deployers of Annex III systems that make or assist decisions about individuals **must inform those persons that they are subject to a high-risk AI system** |

**26(11) is the sleeper obligation for edtech `[INFERENCE]`.** It means a child (or the parent, for a minor) must be told, in terms they can act on, that an AI system is shaping their learning path. Not a line in a ToS. This is a UI requirement, not a legal-page requirement.

Article 27 — **Fundamental Rights Impact Assessment** `[VERIFIED]`: required of "deployers that are bodies governed by public law, or are private entities providing public services." **State schools are squarely in scope.** The FRIA must describe the deployer's processes, the period and frequency of use, "the categories of natural persons and groups likely to be affected," the specific risks of harm to those groups, the human-oversight implementation, and remedial measures — then be notified to the market surveillance authority.

**Commercial consequence `[INFERENCE]`:** if you sell an adaptive tutor to a state school in the EU, your customer has a legal duty to produce a FRIA. Vendors that ship a pre-populated, honest FRIA template — including a candid list of the groups their system underserves — will win procurement. Vendors that do not will force the school to invent the risk analysis, and the school will discover the underserved groups on its own.

#### 1.1.5 Timing

Article 113 `[VERIFIED]`: the Regulation "shall apply from 2 August 2026", with prohibitions and AI-literacy duties from 2 February 2025, GPAI/governance from 2 August 2025, and Article 6(1) (product-safety-embedded high-risk) deferred to 2 August 2027.

**Annex III high-risk obligations therefore bite on 2 August 2026 — six days from the date of this research.** `[VERIFIED]`

⚠️ `[UNVERIFIED-IN-SESSION]` The artificialintelligenceact.eu implementation-timeline page carries a "last updated 1 August 2024" stamp and states there are no announced delays. It therefore **cannot** reflect any 2025–2026 amendment. There has been public discussion of a "Digital Omnibus" simplification package proposing to defer high-risk application; I could not reach EUR-Lex or the Federal Register equivalents to verify whether any such deferral was enacted. **Do not plan on a delay. Verify the current Article 113 text against EUR-Lex before making a compliance decision.**

---

### 1.2 COPPA and the 2025 amendments

**Rule:** 16 CFR Part 312. Source note on the current text: **"90 FR 16977, Apr. 22, 2025"** `[VERIFIED]` (https://www.law.cornell.edu/cfr/text/16/part-312).

FTC final-rule announcement, 16 January 2025 `[VERIFIED]` (https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data). Key changes:

1. **Separate opt-in verifiable parental consent for disclosure to third parties** for targeted advertising or other purposes. `[VERIFIED]`
2. **Retention limits.** § 312.10 `[VERBATIM]`: operators must "retain personal information collected online from a child for only as long as is reasonably necessary to fulfill the specific purpose(s) for which the information was collected", and — categorically — **"Personal information collected online from a child may not be retained indefinitely."** A *written* retention policy is required, stating purposes, business need, and deletion timeframe, and must be disclosed in the § 312.4(d) notice.
3. **"Personal information" now expressly includes biometric identifiers.** § 312.2 `[VERBATIM]`: "A biometric identifier that can be used for the automated or semi-automated recognition of an individual, such as fingerprints; handprints; retina patterns; iris patterns; genetic data, including a DNA sequence; **voiceprints**; gait patterns; **facial templates**; or faceprints". The definition also covers "A photograph, video, or audio file where such file contains a child's image or voice" and persistent identifiers.
4. **Safe Harbor transparency:** approved programs must publicly disclose membership lists.
5. **Effective/compliance dates** `[VERIFIED]`: "The final rule will become effective 60 days after its publication in the Federal Register. Entities subject to the final rule will have one year from that publication date to come into full compliance." With FR publication on 22 April 2025 → effective ~21 June 2025, **full compliance required from 22 April 2026 — already in force as of this document's date.**

**`[NEGATIVE]` — the edtech carve-out that did *not* happen.** The FTC states verbatim that after ~300 comments it "decided against adopting some proposed changes, including proposed requirements that were intended to limit the use of push notifications directed to children without parental consent **and changes relating to the requirements applicable to educational technology companies operating in a school environment**." `[VERBATIM]` This is important and widely misreported: **the 2025 amendments did not codify a school-authorisation exception for edtech.** Edtech operators continue to rely on the FTC's non-binding enforcement-policy position that schools may authorise collection for a school-authorised educational purpose — which is guidance, not rule text. Product decisions that assume a codified school exception are assuming something the Commission explicitly declined to enact.

The Commission additionally recorded that it "remains concerned about the use of push notifications and other engagement techniques to keep kids online in ways that could harm their mental health." `[VERBATIM]` — a live enforcement signal for streaks, nudges, and re-engagement pushes (cf. §4.3, UK AADC Standard 13).

**COPPA's structural weakness `[INFERENCE]`:** it applies only under 13, only to commercial operators, and is consent-shaped. It is a *transaction* statute in a world of *inference*. Nothing in COPPA regulates what you conclude about a child from data you lawfully collected. That gap is the subject of §3.

---

### 1.3 FERPA — the custody statute

The operative provision for any vendor is the **school official exception**, 34 CFR § 99.31(a)(1)(i)(B) `[VERBATIM]` (https://www.law.cornell.edu/cfr/text/34/99.31):

> "A contractor, consultant, volunteer, or other party to whom an agency or institution has outsourced institutional services or functions may be considered a school official under this paragraph provided that the outside party—
> (1) Performs an institutional service or function for which the agency or institution would otherwise use employees;
> (2) **Is under the direct control of the agency or institution with respect to the use and maintenance of education records**; and
> (3) Is subject to the requirements of § 99.33(a) governing the use and redisclosure of personally identifiable information from education records"

**What "direct control" actually forecloses `[INFERENCE]`.** A vendor operating under this exception cannot decide unilaterally to:
- train a general model on identifiable student records,
- retain records after the contract ends,
- repurpose records for product analytics beyond the contracted function,
- redisclose to a subprocessor without flow-down of the same restrictions.

"Direct control" is not a security standard; it is a **decision-rights** standard. It says the school, not you, decides what happens to the record. Any architecture in which the vendor's model improves because it *keeps* student records has an unresolved § 99.31(a)(1)(i)(B)(2) problem. This is exactly the fault line inBloom fell into (§2).

---

### 1.4 IDEA confidentiality — the strictest layer, and the one most often missed

IDEA Part B, 34 CFR §§ 300.610–300.627. Two provisions matter most:

**§ 300.622 (Consent)** `[VERIFIED]` (https://www.law.cornell.edu/cfr/text/34/300.622): parental consent must be obtained before personally identifiable information is disclosed to parties **other than officials of participating agencies**; consent is also required before disclosure to agencies providing or paying for transition services, and for release between LEAs where a child is enrolled in a private school outside the parent's residential LEA.

**§ 300.624 (Destruction of information)** `[VERIFIED]` (https://www.law.cornell.edu/cfr/text/34/300.624): when personally identifiable information is no longer needed to provide educational services, the public agency **must inform parents**, and **"The information must be destroyed at the request of the parents."** `[VERBATIM]` Only a minimal permanent record (name, address, phone, grades, attendance, classes attended, grade level and year completed) may be retained without time limit.

**Architectural consequence `[INFERENCE]` — the deletion problem is a model problem.** A parent of a child with an IEP has a right to compel destruction of the PII. If that child's interaction history has been folded into model weights, into a shared embedding index, or into an aggregate learner-model prior, **you cannot honour the request.** You can delete the row; you cannot delete the influence. Any product touching special-education populations must therefore be built so that per-learner state is (a) stored in a form that is genuinely deletable, and (b) never used for cross-learner training without irreversible, pre-storage de-identification. This is not a nice-to-have; § 300.624 makes it a compliance precondition, and IDEA populations are precisely the population an adaptive tutor claims to serve best.

---

### 1.5 GDPR — special-category data and the automated-decision ceiling

**Article 9(1)** `[VERBATIM]` (https://gdpr-info.eu/art-9-gdpr/):

> "Processing of personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, and the processing of genetic data, biometric data for the purpose of uniquely identifying a natural person, **data concerning health** or data concerning a natural person's sex life or sexual orientation shall be prohibited."

Processing is unlawful unless an Art. 9(2) gateway applies — (a) explicit consent, (b) employment/social-security law, (c) vital interests, (d) not-for-profit bodies, (e) manifestly made public by the subject, (f) legal claims, (g) substantial public interest under law, (h) occupational/preventive medicine, (i) public health, (j) archiving/research/statistics. `[VERIFIED]`

**"Data concerning health" is the trapdoor `[INFERENCE]`.** A learner model that records or predicts dyslexia, ADHD, dyscalculia, autism, or working-memory limitation is processing health data. It does not matter that the inference is a by-product; the Article 9 prohibition attaches to data *revealing* the category, not to data labelled as such. For a child, "explicit consent" under 9(2)(a) is doing extremely heavy lifting and — read together with Article 8 — is not the child's to give below 16 (see below).

**Article 8** `[VERIFIED]` (https://gdpr-info.eu/art-8-gdpr/): for information society services offered directly to a child, processing on consent is lawful only with parental authorisation where the child is **below 16**, with Member States free to lower the threshold **but "not below 13 years."** Controllers must make "reasonable efforts to verify... that consent is given or authorised by the holder of parental responsibility over the child, taking into consideration available technology." `[VERBATIM]` The practical result is a fragmented 13–16 age patchwork across the EU that a single product configuration cannot satisfy.

**Article 22** `[VERBATIM]` (https://gdpr-info.eu/art-22-gdpr/): "The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her." Where an Art. 22(2) exception applies, the controller must provide "the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision."

**Article 22(4)** is the hard stop: "Decisions referred to in paragraph 2 shall not be based on special categories of personal data referred to in Article 9(1), unless point (a) or (g) of Article 9(2) applies and suitable measures to safeguard the data subject's rights... are in place." `[VERBATIM]`

**Read 22(4) with §3 `[INFERENCE]`:** if your learner model has inferred a probable disability, and your placement/pathway decision is influenced by that inference, and the decision is made solely automatically and significantly affects the child — you are in Art. 22(4) territory with only explicit consent or substantial-public-interest law as a gateway. The clean answer is: **never let a sensitive inference enter a consequential automated decision.**

**Article 35** `[VERBATIM]` (https://gdpr-info.eu/art-35-gdpr/): a DPIA is mandatory for "systematic and extensive evaluation of personal aspects relating to natural persons which is based on automated processing, including profiling, and on which decisions are based" and for "processing on a large scale of special categories of data." An adaptive tutor hits 35(3)(a) on the face of it. **A DPIA is not optional for this product class.**

---

### 1.6 UK: the age-appropriate design code, and the safeguarding statute

**ICO Age Appropriate Design Code ("Children's code")** `[VERIFIED]` (https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/). A **statutory** code of practice — the ICO notes "Parliament and government ensured UK data protection laws will truly transform the way we look after children online by requiring my office to introduce this statutory code of practice" `[VERBATIM]`. It applies to information society services "likely to be accessed by" children — a **far broader trigger than "directed to children"** and the single most-underestimated scoping rule in the field. It is "rooted in the United Nations Convention on the Rights of the Child (UNCRC)" `[VERBATIM]`.

The **15 standards** `[VERIFIED]`:

1. Best interests of the child — "The best interests of the child should be a primary consideration when you design and develop online services likely to be accessed by a child." `[VERBATIM]`
2. Data protection impact assessments — "Undertake a DPIA to assess and mitigate risks to the rights and freedoms of children... Take into account differing ages, capacities and development needs" `[VERBATIM]`
3. Age appropriate application — "Take a risk-based approach to recognising the age of individual users" `[VERBATIM]`
4. Transparency
5. Detrimental use of data
6. Policies and community standards
7. Default settings — the ICO states "Settings must be 'high privacy' by default" `[VERBATIM]`
8. Data minimisation
9. Data sharing
10. Geolocation
11. Parental controls
12. Profiling
13. Nudge techniques
14. Connected toys and devices
15. Online tools

Standards **12 (Profiling)** and **13 (Nudge techniques)** are the two that adaptive-tutoring and engagement-loop design collide with directly. Standard 11 (Parental controls) carries a subtlety `[INFERENCE]`: parental monitoring that is invisible to the child is itself a children's-rights harm — the code's UNCRC grounding implies the child must know when they are being monitored.

**Keeping children safe in education (KCSIE)** `[VERIFIED]` (https://www.gov.uk/government/publications/keeping-children-safe-in-education--2). Statutory guidance setting out "legal duties that schools and colleges must follow to safeguard and promote the welfare of children and young people under the age of 18." `[VERBATIM]` KCSIE 2025 is in force to 31 August 2026; **KCSIE 2026 applies from 1 September 2026.** Full text of Part One 2026 retrieved and quoted in §5.

**Ofcom Protection of Children Codes (Online Safety Act 2023)** — `[UNVERIFIED-IN-SESSION]`. ofcom.org.uk returned a Cloudflare 403. The children's safety duties and "highly effective age assurance" requirements are widely reported to have commenced in July 2025, but I did not reach a primary source and will not assert dates or provisions.

---

### 1.7 Composite floor — what every claim above adds up to

| Constraint | Source | Binding effect on a learner-model product |
|---|---|---|
| Emotion inference in education = **prohibited** | AI Act 5(1)(f) + 3(39) | No webcam/voice affect detection. Ever. |
| Exploiting age/disability vulnerability = **prohibited** | AI Act 5(1)(b) | No engagement mechanics tuned to a child's known impulsivity or a diagnosed condition |
| Steering learning = **high-risk** | Annex III(3)(b) | Full Chapter III conformity regime from 2 Aug 2026 |
| Profiling ⇒ no derogation | AI Act 6(3) final clause | A learner model cannot self-exempt |
| Affected persons must be told | AI Act 26(11) | UI-level disclosure to child/parent |
| Public-sector deployers need a FRIA | AI Act 27 | Ship the template or lose the sale |
| Children's PII cannot be retained indefinitely | 16 CFR 312.10 | Written retention policy, published, enforced |
| Voiceprints/facial templates are children's PII | 16 CFR 312.2 | A multimodal tutor collects COPPA-regulated biometrics by default |
| No codified edtech school exception | FTC, Jan 2025 | Do not architect around one |
| Vendor is under school's **direct control** | 34 CFR 99.31(a)(1)(i)(B)(2) | No unilateral training, retention, or repurposing |
| SEN records destroyed on parental request | 34 CFR 300.624 | Per-learner state must be genuinely deletable |
| Health data prohibited absent a gateway | GDPR 9(1) | Disability inference is presumptively unlawful |
| No solely-automated significant decision on Art. 9 data | GDPR 22(4) | Sensitive inferences must not feed consequential automation |
| DPIA mandatory | GDPR 35(3)(a) | Non-negotiable pre-launch artefact |
| High privacy by default; profiling & nudge standards | ICO AADC 7, 12, 13 | Defaults, not settings |

---

## 2. inBloom — the custody lesson

**Primary source:** Bulger, M., McCormick, P., & Pitcan, M. (2017). *The Legacy of inBloom.* Data & Society Research Institute. https://datasociety.net/wp-content/uploads/2017/02/InBloom_feb_2017.pdf `[VERBATIM — full text extracted]`

### 2.1 The facts

- **"InBloom was a $100 million educational technology initiative primarily funded by the Bill & Melinda Gates Foundation that aimed to improve American schools by providing a centralized platform for data sharing, learning apps, and curricula."** `[VERBATIM]` Footnote 7: "InBloom received $100 million in combined funding from the Bill & Melinda Gates Foundation and Carnegie Corporation." `[VERBATIM]`
- Funded 2011; publicly launched February 2013; closure announced **April 2014** — "barely over a year after its public launch." `[VERBATIM]`
- **Nine states committed**, including New York City. By February 2014 "five states had identified districts for pilot projects." Nine committed states represented **"over 11 million students."** `[VERBATIM]`
- The technical team is described as "supported by what has been described as a 'dream team' of programmers and engineers." `[VERBATIM]`
- **Legacy: "over 400 pieces of state-level legislation"** on student data privacy, plus an industry Student Privacy Pledge. `[VERBATIM]`
- Post-inBloom, "the trend in data-driven educational technologies since inBloom's closure has been toward closed, proprietary systems, adopted piecemeal. **To date, no large-scale educational technology initiative has succeeded in American K-12 schools.**" `[VERBATIM]`

### 2.2 The objection was custody, not schema

The Data & Society interviews are unambiguous that the fight was about *who holds the data and who can get it*, not about the data dictionary. The mobilising text — Leonie Haimson's April 2013 parent town-hall invitation — is entirely custody-framed `[VERBATIM]`:

> "Parents, do you know your child's confidential, personal school records are going to be shared with a corporation called inBloom Inc?
>
> This highly sensitive information will be stored on a data cloud and **disclosed to for-profit corporations** to help them develop and market their 'learning products'
>
> The data will include your child's names, address, photo, email, test scores, grades, economic and racial status, and detailed disciplinary, health and special education records."

Note what is being objected to: *storage location*, *disclosure recipient*, *commercial purpose*, and *sensitivity of category*. Nothing about the schema. Indeed the report notes that the technical architecture was comparatively strong — an inBloom-adjacent account observes it "offered greater security and more data-access controls than" the incumbent alternatives `[VERBATIM]`.

The United Federation of Teachers' testimony makes the same distinction explicitly `[VERBATIM]`:

> "the UFT is not opposed to gathering data on public school students; in fact, it's a valuable tool" — but "releasing sensitive, student-identifying data points in **400 categories**…" and "share[ing] some or all of that information with **private companies**" was problematic, "how can we possibly countenance that?"

**The union endorsed the data model and rejected the custody arrangement in the same sentence.** That is the entire lesson in one quotation.

The killing blow was legislative, and it was a custody rule `[VERBATIM]`: the NY 2014–15 state budget "included a clause making it illegal for the state to share personally identifiable student data with any shared learning infrastructure service provider via a private, cloud-based, or state operated student datastore." inBloom announced closure one month later.

Interviewees also record that when inBloom answered custody questions with compliance language, it made things worse: "references to brief, often legalistic, statements and assurances about **FERPA compliance** only hardened opponents' view that inBloom and their partners were aloof, secretive, and condescending." `[VERBATIM]`

### 2.3 `[NEGATIVE]` — the report's own counter-thesis

Sharren Bates, inBloom's product lead, is quoted as saying: **"inBloom did not have a privacy problem, inBloom did not have a parent problem. InBloom had an advocacy and perception problem."** `[VERBATIM]` The Data & Society authors' own diagnosis leans this way too — they identify the root cause as "the combination of the public's low tolerance for risk and uncertainty and the inBloom initiative's failure to communicate the benefits of its platform and achieve buy-in from key stakeholders," and "Trust was one of the most frequently used words in our interviews." `[VERBATIM]`

**This is a genuine disconfirmation of the naive reading and it should be recorded honestly.** The strongest available account of inBloom says the failure was *communication and trust*, not *data custody per se*. My reading `[INFERENCE]`: this is a distinction without a difference at the design level, because the thing that could not be communicated was the custody arrangement. inBloom could not answer "who holds my child's health and discipline record, and who can they give it to?" with an answer parents found acceptable — because the answer was "a third-party non-profit, in a commercial cloud, disclosing to for-profit app vendors under district authorisation." No amount of advocacy makes that sentence land. **Custody is the message.** If your custody architecture requires a communications strategy to survive contact with a parent, you have the wrong custody architecture.

### 2.4 The design rule this yields

`[INFERENCE]` **Design the custody story first, then the data model.** Concretely, a learner-model product should be able to answer these five questions in one screen, to a parent, without legal counsel:

1. Where does my child's record physically live, and under whose legal control?
2. Who — by name, not category — can read it?
3. Does it ever leave for a purpose other than teaching my child?
4. Does my child's data improve your product for other customers? (If yes, you have inBloom's problem.)
5. How do I delete it, and what survives deletion?

If any answer requires a diagram, the product is not shippable to a public school system.

---

## 3. Sensitive inference — the problem COPPA and FERPA do not touch

### 3.1 The inference happens whether or not you ask for it

A learner model is a high-dimensional record of *how a specific mind fails*. Response latency, error topology, retry patterns, time-of-day usage, session abandonment, and free-text content jointly encode:

- **Disability**: dyslexia signatures in decoding-vs-comprehension divergence; ADHD signatures in session fragmentation; dyscalculia in number-sense item clustering; working-memory limits in multi-step failure profiles.
- **Mental state**: the AIED literature demonstrates that boredom, frustration, confusion, and engagement are recoverable from interaction logs alone, with no sensors — the "sensor-free affect detection" line of work (ERIC ED537205, 2012; ED599173, 2019) `[VERIFIED]`, plus video-based detection (ED560878, 2015) `[VERIFIED]` and carelessness/affect coupling in ITS mathematics (ERIC EJ1036906, *IJAIED*, 2014) `[VERIFIED]`.
- **Family circumstance**: usage at 2am; device sharing across siblings; a three-week gap; a sudden collapse in performance; free-text mentions of a parent, a move, a hospital.

**The learning-analytics field has known this for over a decade** — Pardo & Siemens, "Ethical and Privacy Principles for Learning Analytics," *BJET* (2014), ERIC EJ1022852 `[VERIFIED]`, which notes "The massive adoption of technology in learning processes comes with an equally large capacity to track learners"; see also "Ethical Challenges for Learning Analytics," *JLA* (2019), ERIC EJ1237573 `[VERIFIED]`, and "Practical Ethics for Building Learning Analytics," *BJET* (2019), ERIC EJ1232071 `[VERIFIED]`.

### 3.2 The legal obligations that attach

`[INFERENCE from verified provisions]`

| Obligation | Trigger | Source |
|---|---|---|
| **Art. 9 prohibition applies to the inference, not just the field** | Model outputs data "revealing" health status | GDPR 9(1) `[VERBATIM]` |
| **Cannot feed a solely-automated significant decision** | Placement, pathway, or referral driven by disability inference | GDPR 22(4) `[VERBATIM]` |
| **DPIA mandatory** | Systematic extensive evaluation + profiling + decisions | GDPR 35(3)(a) `[VERBATIM]` |
| **Disclosure to the affected person** | Annex III system assisting decisions about the child | AI Act 26(11) `[VERIFIED]` |
| **Retention limit + written policy** | Any inference stored is children's PII | 16 CFR 312.10 `[VERBATIM]` |
| **Destroyable on parental request** | Where the child receives IDEA services | 34 CFR 300.624 `[VERBATIM]` |
| **Minimisation** | Do not derive what you do not need | ICO AADC Std. 8 `[VERIFIED]` |

### 3.3 The minimisation rule: *derive-and-discard*

`[INFERENCE]` Data minimisation is conventionally read as a *collection* rule. For a learner model it must be read as a **derivation and persistence** rule. The correct architecture:

- **Transient derivation is acceptable.** Computing, within a single turn, that the learner is likely struggling with phonological decoding *in order to choose the next scaffold*, and then discarding it, is pedagogy.
- **Persistence is the harm.** Writing `suspected_dyslexia: 0.72` to a durable per-child record creates a health-data dossier under GDPR 9(1), a COPPA-retained record under 312.10, and an IDEA-destroyable record under 300.624 — with none of the clinical process, none of the appeal rights, and none of the accuracy guarantees of an actual diagnosis.
- **Never expose a sensitive inference through the UI or the API.** Teacher dashboards leak. Exports leak. A "flags" column in a CSV is a permanent record in a school's shared drive.

### 3.4 What should never be inferred at all

`[INFERENCE, grounded in AI Act 5(1)(f)/(g), GDPR 9(1), ICO AADC 5 & 12]`

**Category A — prohibited by regulation:**
- Emotional state from biometric signal (face, voice) in an education context — AI Act 5(1)(f)
- Race, ethnicity, religion, political opinion, sexual orientation, sex life from biometric data — AI Act 5(1)(g)

**Category B — should never be persisted or surfaced, regardless of technical feasibility:**
- Clinical or quasi-clinical labels: any disability, disorder, or neurodevelopmental condition
- Mental-health state: depression, anxiety, suicidality risk score *as a stored attribute* (see §5 — detection for immediate escalation is a different thing from a stored score)
- Family circumstance: poverty, housing instability, parental separation, immigration status, care status, parental substance use
- Fixed-trait ability: IQ-analogues, "learning style", or any construct that functions as a ceiling
- Long-horizon life prediction: dropout probability, future-earnings proxy, "college-readiness" score attached to a named child

**The general rule `[INFERENCE]`: a learner model may hold what the child has demonstrated. It must not hold what the child is.** Mastery of subtraction with regrouping is demonstrated. Dyscalculia is an identity claim. The first is a teaching input; the second is a permanent label applied without clinical process, disclosed to whoever gets the export, and — per the bias evidence in §7 — differentially wrong for exactly the children it will be applied to most.

---

## 4. Child-specific AI harms

### 4.1 The OpenAI × MIT Media Lab study

Phang et al. (2025), *Investigating Affective Use and Emotional Well-being on ChatGPT*, arXiv:2504.03888, 4 April 2025 `[VERIFIED]`. Two parallel studies:

- **Platform analysis:** "large-scale automated analysis of ChatGPT platform usage in a privacy-preserving manner, analyzing **over 3 million conversations** for affective cues and surveying **over 4,000 users**" `[VERBATIM]`
- **RCT:** "an Institutional Review Board (IRB)-approved randomized controlled trial (RCT) on **close to 1,000 participants over 28 days**, examining changes in their emotional well-being as they interact with ChatGPT under different experimental settings" `[VERBATIM]`

**Headline finding** `[VERBATIM]`: "In both on-platform data analysis and the RCT, we observe that **very high usage correlates with increased self-reported indicators of dependence**."

**`[NEGATIVE]` — the result is weaker and more conditional than it is usually cited as being.** The authors state plainly: "From our RCT, we find that the impact of voice-based interactions on emotional well-being to be **highly nuanced, and influenced by factors such as the user's initial emotional state and total usage duration**." `[VERBATIM]` And: "a small number of users are responsible for a disproportionate share of the most affective cues." `[VERBATIM]`

**Honest reading `[INFERENCE]`:** this is *not* evidence that conversational AI causes dependence in the general population. It is evidence that (a) heavy affective use co-occurs with self-reported dependence, direction unestablished; (b) effects are heterogeneous and moderated by baseline emotional state; (c) the phenomenon is concentrated in a small tail. **Crucially, the participants were adults.** Extrapolating the RCT to children is unsupported by the paper. The right conclusion for a children's product is a *tail-management* conclusion, not a population conclusion: build for the small minority who will use the tutor as a confidant, because they exist and they are the highest-risk users. That is also the population most likely to make a safeguarding disclosure (§5).

### 4.2 Companion-app evidence specific to minors

- **Teen overreliance.** *Understanding Teen Overreliance on AI Companion Chatbots Through Self-Reported Reddit Narratives*, arXiv:2507.15783 (2025) `[VERIFIED]`. Analysed **318 Reddit posts from users self-disclosing as 13–17** on the Character.AI subreddit. Finding `[VERBATIM]`: "teens often begin using chatbots for support or creative play, but these activities can deepen into strong attachments marked by **conflict, withdrawal, tolerance, relapse, and mood regulation**. Reported consequences include **sleep loss, academic decline, and strained real-world connections**." Disengagement occurs when "teens recognize harm, re-engage with offline life, or **encounter restrictive platform changes**." The authors map the experience onto behavioural-addiction frameworks and propose a CARE design framework.
  - **Limitations `[INFERENCE]`:** self-selected Reddit sample, self-reported age, n=318 posts not persons, no control group, survivorship toward those who *noticed* a problem. Directionally important, not causally probative.
  - **The actionable finding is the last clause:** restrictive platform changes drove disengagement. Product constraints work.
- **`[NEGATIVE]` — teens may not be the most susceptible group.** *Anthropomorphism in AI Companion Communities: Age, Gender, and Emotional Correlates*, arXiv:2606.30942 (June 2026) `[VERIFIED]`. Across three AI-companion subreddits: "We found that **adults and women anthropomorphize AI chatbots more than teens and men**, and that positive emotional expression, particularly joy, is positively associated with anthropomorphization." `[VERBATIM]` The paper explicitly notes that "mixed findings complicate the role of demographics." This directly cuts against the intuitive assumption that minors are maximally vulnerable to parasocial attachment, and it means **child-specific protections cannot be justified by "children anthropomorphize more"** — they must be justified by children's reduced capacity to exit, reduced legal agency, and the developmental stakes, which is a different and better argument.

### 4.3 Professional guidance

**APA Health Advisory on AI and Adolescent Well-Being**, June 2025 `[VERIFIED]` (https://www.apa.org/topics/artificial-intelligence-machine-learning/health-advisory-ai-adolescent-well-being). Covers ages 10–25, nine recommendations. Directly load-bearing statements:

- "Youth are likely to have **heightened trust in, and susceptibility to, influence from AI-generated characters**" `[VERBATIM]`
- Systems should build in "**regular notifications and reminders that adolescents are interacting with a bot**" `[VERBATIM]`
- "**Mechanisms for human intervention and support should be readily available**, allowing young users to report concerns" `[VERBATIM]`
- AI companions need "safeguards preventing exploitation and unhealthy dependencies that might interfere with real-world relationships"
- Systems for adolescents "must differ fundamentally from adult versions, incorporating protective defaults"

Note the convergence: APA's "mechanisms for human intervention" ≈ AI Act Art. 26(2) human oversight ≈ ICO AADC Std. 15 (Online tools) ≈ KCSIE's DSL route. **Four independent authorities are describing the same missing component: a human on the other end.** That is §5.

### 4.4 Age-appropriate design in practice

The AADC's operative move `[INFERENCE]` is that it converts privacy from a *setting* to a *default*: "Settings must be 'high privacy' by default" `[VERBATIM]`. For a tutor this means, concretely: no persistent conversation history without an affirmative choice; no cross-session personality persistence by default; no streaks, no push re-engagement, no variable-ratio reward (Std. 13, nudge techniques — and note the FTC's parallel concern about push notifications and "engagement techniques to keep kids online in ways that could harm their mental health" `[VERBATIM]`); no profile-based content selection outside the pedagogical function (Std. 12).

---

## 5. Safeguarding — the non-negotiable escalation path

**This is the section that almost no AI tutoring product has.** A tutor that a child talks to daily, that is patient and non-judgemental and never tired, is *structurally optimised* to receive disclosures that a teacher will not receive. This is not a hypothetical risk; it is a design consequence. The parasocial dynamic documented in §4.2 is precisely the dynamic that produces disclosure.

### 5.1 What statutory guidance actually requires

**KCSIE 2026, Part One** `[VERBATIM]` (https://assets.publishing.service.gov.uk/media/6a47c29b1c8bd7ce25a5eb6d/Keeping_children_safe_in_education_2026__part_one.pdf):

> **¶8:** "Every school and college should have a designated safeguarding lead"

> **¶14:** "All staff should know what to do if a child tells them they are being abused, exploited, or neglected. Staff should know how to manage the requirement to maintain an appropriate level of confidentiality. This means only involving those who need to be involved, such as the designated safeguarding lead (or a deputy) and local authority children's social care. **Staff should never promise a child that they will not tell anyone about a report of any form of abuse, as this may ultimately not be in the best interests of the child.**"

> **¶15:** "All staff should be able to reassure victims that they are being taken seriously and that they will be supported and kept safe. **A victim should never be given the impression that they are creating a problem by reporting** any form of abuse and/or neglect. Nor should a victim ever be made to feel ashamed for making a report."

> **¶16:** "children may not feel ready or know how to tell someone that they are being abused... This could be due to their vulnerability, disability and/or sexual orientation or **language barriers**. This should not prevent staff from having a **professional curiosity**..."

> **¶55:** "Staff working with children are advised to maintain an attitude of **'it could happen here'**"

> **¶56:** "If staff have any concerns about a child's welfare, they should **act on them immediately**."

> **¶59:** "The designated safeguarding lead (or a deputy) **should always be available** to discuss safeguarding concerns. If in exceptional circumstances, the designated safeguarding lead (or a deputy) is not available, **this should not delay appropriate action being taken.**"

> **¶60:** "Staff should not assume a colleague or another professional will take action and share information that might be critical in keeping children safe."

> **¶609–610:** "If staff feel that a child is in danger, they should call 999 or arrange for them to be taken to A&E immediately"

> **¶621:** staff must report a child self-harming or expressing intent to do so "to the designated safeguarding lead (or a deputy)"

**Every one of these paragraphs translates directly into a product requirement.** ¶14 forbids a confidentiality promise — which means a tutor **must not be designed to say, or imply, "this is just between us."** ¶15 forbids making the child feel like a problem — which means a canned "I can't help with that, please talk to a trusted adult" deflection is a *safeguarding failure*, not a safe default. ¶56 requires immediate action. ¶59 forbids delay when the human is unavailable. ¶60 forbids assuming someone else will act — which forecloses "the school's own systems will catch it."

**US position** `[UNVERIFIED-IN-SESSION]`: childwelfare.gov's mandatory-reporter page returned 404. The general structure — CAPTA-conditioned state statutes designating school personnel as mandated reporters, with a minority of states imposing universal reporting duties, and short statutory reporting windows — is well known but I could not verify professions, state counts, or timeframes against a primary source in this session and will not assert them.

### 5.2 What the evidence says about AI crisis handling

- **Failures are real and concentrated.** *Between Help and Harm: An Evaluation of Mental Health Crisis Handling by LLMs*, arXiv:2509.24857 (2025) `[VERIFIED]`: built a six-category crisis taxonomy, curated 2,252 crisis examples from 239,000+ user inputs, audited five models on a 5-point harmful→appropriate scale. Finding `[VERBATIM]`: "While some models respond reliably to explicit crises, risks still exist. **Many outputs, especially in self-harm and suicidal categories, are inappropriate or unsafe.**"
- **Omission, not hallucination, is the dominant failure mode.** *Disentangling Prompt Element Level Risk Factors for Hallucinations and Omissions in Mental Health LLM Responses*, arXiv:2604.00014 (2026) `[VERIFIED]`: 2,075 structured prompts against Llama 3.3; "Hallucinations occurred in **6.5%** of responses and **omissions in 13.2%**, with **omissions concentrated in crisis and suicidal ideation prompts**." `[VERBATIM]` Failures tracked *context and tone* rather than user background. The authors argue for "evaluating omissions as a primary safety outcome."
  - `[INFERENCE]` This is the single most useful finding for tutor design: the model does not usually say something harmful in a crisis — it **fails to say the necessary thing**. A safety eval that only measures harmful output will pass a system that silently drops the escalation.
- **Detection is technically tractable.** *PsyCrisisBench*, arXiv:2506.01329 (2025) `[VERIFIED]`: 540 annotated transcripts from a real psychological assistance hotline, 64 LLMs across 15 families. "LLMs showed strong results in suicidal ideation detection (**F1=0.880**), suicide plan identification (**F1=0.779**), and risk assessment (**F1=0.907**)", achieving "comparable or superior performance" to trained human operators on plan identification and risk assessment, while humans retained an edge on mood-status recognition (max F1=0.70). `[VERBATIM]`
  - `[INFERENCE]` F1 ≈ 0.88 is good enough to *route* and nowhere near good enough to *decide*. It supports a triage-and-escalate architecture; it forbids an auto-resolve architecture.

**`[NEGATIVE]` — benchmark failure rates substantially overstate real-world failure.** *Beyond Simulations: What 20,000 Real Conversations Reveal About Mental Health AI Safety*, arXiv:2601.17003 (January 2026) `[VERIFIED]`. Replicated four published safety test sets against a frontier general model and a purpose-built mental-health AI with layered suicide/NSSI safeguards, then ran an ecological audit on **over 20,000 real user conversations**. Findings `[VERBATIM]`: the purpose-built AI "was significantly less likely than general-purpose LLMs to produce enabling or harmful content across suicide/NSSI (**.4–11.27% vs 29.0–54.4%**), eating disorder (**8.4% vs 54.0%**), and substance use (**9.9% vs 45.0%**) benchmark prompts", **"test set failure rates for suicide/NSSI were far higher than in real-world deployment"**, and — decisively — "Clinician review of flagged conversations from the ecological audit identified **zero cases of suicide risk that failed to receive crisis resources**."

**Why this negative result matters and how not to misuse it `[INFERENCE]`.** It shows (a) purpose-built layered safeguards produce a 3–6× reduction in harmful output versus a general model, and (b) adversarial benchmarks are a pessimistic proxy for real usage. It does **not** show that safeguards are unnecessary — it shows that *the safeguards worked*. The correct inference is the opposite of complacency: **the zero-miss result was achieved by a system explicitly engineered with layered suicide/NSSI safeguards, not by a general-purpose model with a system prompt.** A general-purpose tutor with a "be careful about self-harm" instruction has none of the architecture that produced this result, and the same paper's benchmark numbers (29–54% harmful output for general-purpose LLMs) show what happens without it.

### 5.3 Why this is a first-class requirement, not a policy annex

`[INFERENCE]` Three arguments:

1. **Statistical inevitability.** Serve a million children daily and disclosures of abuse, self-harm, neglect, and domestic violence are not tail events — they are a predictable weekly volume. Any product at scale that lacks a disclosure path is not "unprepared"; it is *systematically failing* a known caseload.
2. **The product creates the disclosure.** Unlike a textbook, a conversational tutor actively elicits confidence. It is closer to a pastoral relationship than to software. Creating the conditions for disclosure while having nowhere to route it is a form of harm the product is uniquely responsible for.
3. **It is the cheapest possible differentiator.** A DSL routing integration is weeks of work. It is also the thing that makes a district procurement committee say yes. Nobody has built it. `[INFERENCE — I found no AI tutoring product documenting a safeguarding escalation path in this session, but absence of evidence here is partly absence of search: I did not systematically audit vendor documentation. Treat "almost no product documents it" as a strong prior, not a verified census.]`

---

## 6. AI detectors — the case for abolition, not caution

### 6.1 The evidence

Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023), *GPT detectors are biased against non-native English writers*, arXiv:2304.02819v3; published in *Patterns* (Cell Press), https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7. Full text extracted `[VERBATIM]`:

> "We evaluated the performance of **seven** widely-used GPT detectors on a corpus of **91 human-authored TOEFL essays** obtained from a Chinese educational forum and **88 US 8-th grade essays** sourced from the Hewlett Foundation's Automated Student Assessment Prize (ASAP) dataset. The detectors demonstrated **near-perfect accuracy for US 8-th grade essays**. However, they misclassified over half of the TOEFL essays as 'AI-generated' (**average false positive rate: 61.22%**). All seven detectors unanimously identified **18 of the 91** TOEFL essays (**19.78%**) as AI-authored, while **89 of the 91** TOEFL essays (**97.80%**) are flagged as AI-generated by **at least one detector**."

The 5.19% figure `[VERBATIM]`: applying ChatGPT to simplify US 8th-grade essays "as if written by a non-native speaker" raised misclassification "**from an average of 5.19% across detectors to 56.65%**."

So the correct framing of the headline comparison: **61.22% average FPR on non-native writing vs 5.19% on native US 8th-grade writing — an ~11.8× disparity — and a single sentence-level style change moves a native writer's essay from 5.19% to 56.65%.**

**The mechanism is perplexity, and the mechanism is the argument** `[VERBATIM]`: "we observed that they had significantly lower perplexity compared to the others (P-value: 9.74E-05). This suggests that GPT detectors may **penalize non-native writers with limited linguistic expressions**." The authors confirm the mechanism independently on 1,574 ICLR 2023 accepted papers (all pre-ChatGPT): authors in non-native-English countries "wrote significantly lower text perplexity abstracts" (P=0.035), and the difference held after controlling for review ratings (P=0.033).

**Detectors are trivially defeated** `[VERBATIM]`: a self-edit prompt ("Elevate the provided text by employing literary language") on ChatGPT-3.5 Common App essays "significantly reduced detection rates **from 100% to 13%**"; on generated scientific abstracts, from up to 68% down to 28%. Enriching TOEFL essays' word choice cut the FPR "**from 61.22% to 11.77%**."

**The authors' own conclusion** `[VERBATIM]`: their results "**caution against their use in evaluative or educational settings**, particularly when they may inadvertently penalize or exclude non-native English speakers from the global discourse." And the paradox they name: "to evade false detection as AI-generated content, these writers may need to" alter their natural writing.

**Corroboration on the other side of the ledger.** *Assessing GPTZero's Accuracy in Identifying AI vs. Human-Written Essays*, arXiv:2506.23517 (2025) `[VERIFIED]`: 28 AI-generated and 50 human-written papers; AI-generated papers detected at 91–100% confidence, but "the human generated essays fluctuated; there were a handful of false positives... its reliability in **distinguishing human-authored texts is limited**." `[VERBATIM]` Same asymmetry, different tool, independent group.

### 6.2 The accommodation trap

`[INFERENCE — this is my argument, built on verified premises]`

The mechanism is **low perplexity**, i.e. predictable word choice and constrained syntactic variety. Now consider who is explicitly taught to write with predictable structure and constrained variety, *as a documented accommodation or intervention*:

- **English learners**, taught sentence frames, sentence starters, and paragraph templates
- **Students with dyslexia or dysgraphia**, taught explicit paragraph schemas (e.g. Hochman, Step Up to Writing) to offload working memory
- **Students with autism**, taught explicit structural templates to compensate for pragmatic-language difficulty
- **Students in high-poverty schools** where formulaic scaffolds (five-paragraph essay, PEEL, TEEL, claim-evidence-reasoning) are the dominant writing pedagogy under test pressure

Every one of these interventions **lowers perplexity by design.** The scaffold *is* the predictability. Therefore: **the better a student complies with their prescribed writing accommodation, the more likely a detector is to accuse them of cheating.** The tool converts successful special-education provision into an integrity allegation. There is no threshold setting that fixes this, because the accommodation and the detection signal are the same variable.

Compounding it: the students most exposed are the least equipped to contest an accusation — least likely to have a parent who will escalate, least likely to have documentation habits, most likely to be already positioned as academically suspect, and (per KCSIE ¶16's observation about "language barriers") least able to articulate a defence.

### 6.3 Why "use with caution" is not an available position

`[INFERENCE]`

The standard institutional response — "use detector output as one signal among many, never as sole evidence" — fails on four grounds:

1. **The signal has no information value at the individual level.** With FPR 61.22% on one population and ~5% on another, a positive result is more strongly predictive of the student's linguistic background than of their conduct. There is no defensible Bayesian update to perform.
2. **Cautious use is not the observed use.** "One signal among many" degrades in practice to "the reason a conversation started", and the conversation itself is the punishment — an accusation of academic dishonesty is a serious event for a 15-year-old regardless of outcome.
3. **The disparate impact is a fairness harm in its own right.** 97.80% of non-native essays flagged by at least one of seven detectors means that in any institution using multiple tools, essentially the entire non-native population is exposed. This is a group harm that does not require any individual false accusation to have already occurred.
4. **The tool does not work at its stated job.** 100%→13% detection collapse from a one-line prompt means it fails against precisely the students it purports to catch, while succeeding against the students it should never have touched. **It is an instrument that catches the honest and misses the dishonest.**

**Conclusion: abolition.** An institution should not possess the capability, because possessing it guarantees eventual use, and eventual use guarantees that the burden falls on ELs and accommodated students. The replacement is not a better detector — it is assessment redesign (in-class writing, process artefacts, oral defence, version history, staged drafts), which is F1's territory.

**Regulatory hook** `[INFERENCE]`: AI proctoring and prohibited-behaviour detection during tests is separately classified high-risk under **AI Act Annex III(3)(d)** `[VERBATIM]`. A detector deployed on assessments is therefore both a fairness harm *and* a regulated high-risk system with conformity-assessment, accuracy, logging, and human-oversight obligations — obligations that a tool with a 61.22% subgroup FPR cannot plausibly satisfy under Art. 15 accuracy requirements. The regulatory and ethical cases converge.

---

## 7. Bias in educational AI

### 7.1 Speech: the multimodal tutor's first fairness failure

Koenecke, A., Nam, A., Lake, E., Nudell, J., Quartey, M., Mengesha, Z., Toups, C., Rickford, J. R., Jurafsky, D., & Goel, S. (2020). *Racial disparities in automated speech recognition.* PNAS. doi:10.1073/pnas.1915768117, PMC7149386 `[VERIFIED via EuropePMC]`:

> "we examine the ability of **five state-of-the-art ASR systems—developed by Amazon, Apple, Google, IBM, and Microsoft**—to transcribe structured interviews conducted with **42 white speakers and 73 black speakers**... **19.8 h of audio** matched on the age and gender of the speaker. We found that all five ASR systems exhibited substantial racial disparities, with an average **word error rate (WER) of 0.35 for black speakers compared with 0.19 for white speakers**. We trace these disparities to the underlying **acoustic models**... as the race gap was **equally large on a subset of identical phrases** spoken by black and white individuals." `[VERBATIM]`

**Why the "identical phrases" control matters `[INFERENCE]`:** it rules out lexical/topical confounds. The disparity is acoustic. That means it cannot be fixed by prompting, vocabulary lists, or domain adaptation — only by acoustic training data. For a voice tutor, a 0.35 vs 0.19 WER gap means a Black child's spoken answer is misrecognised nearly twice as often, and — critically — **the tutor's learner model will record those misrecognitions as errors of knowledge.** The bias does not stay in the ASR layer; it is laundered into the mastery estimate, which then steers the curriculum. *(Caveat: 2020 data, adult interview speech, US English. Modern models are better; the direction and mechanism are unlikely to have reversed, but the magnitude should not be quoted as current.)*

### 7.2 Dialect: the text tutor's fairness failure

Hofmann, V., Kalluri, P. R., Jurafsky, D., & King, S. (2024). *Dialect prejudice predicts AI decisions about people's character, employability, and criminality.* arXiv:2403.00742 `[VERIFIED]`:

> "we demonstrate that language models embody covert racism in the form of **dialect prejudice**... exhibiting covert stereotypes that are **more negative than any human stereotypes about African Americans ever experimentally recorded**, although closest to the ones from before the civil rights movement. By contrast, the language models' **overt stereotypes about African Americans are much more positive**." `[VERBATIM]`

**The overt/covert gap is the operationally dangerous part `[INFERENCE]`.** A model that scores well on explicit bias evaluations can still assign systematically worse character and competence judgements to a child who writes in AAE. Since a tutor's feedback tone, difficulty selection, and encouragement are all downstream of an implicit competence judgement, dialect prejudice propagates into pedagogy through a channel that no explicit-bias benchmark inspects.

Corroborating and extending: *LLMs Silently Correct African American English: Auditing and Mitigating Dialect Bias via Activation Steering*, arXiv:2607.06845 (July 2026) `[VERIFIED]`. Across six instruction-tuned LLMs (14B–70B): "state-of-the-art models systematically prefer Standard American English (SAE) continuations even when the preceding context is in AAE, **effectively rewriting AAE into SAE**." `[VERBATIM]` Syntactic constructions, "especially negative concord (e.g., 'ain't nobody'), are universal triggers across all models." Activation steering reduced bias "5 to 20 times more than prompting" — which is itself a finding: **prompt-level mitigation of dialect bias barely works.**

`[INFERENCE]` For a writing tutor, "silently correcting" AAE to SAE is not a neutral act. AAE is rule-governed; negative concord is grammatical in AAE. A tutor that flags it as an error is teaching a child that their home language is wrong, under the authority of a machine, without a teacher present to contextualise it.

### 7.3 Cross-population generalisation failure in learner models

Gorgun, G., & Yildirim-Erbasli, S. N. (2026). *Algorithmic Bias in BERT for Response Accuracy Prediction: A Case Study for Investigating Population Validity.* *Journal of Educational Measurement*. ERIC EJ1501422 `[VERIFIED]`:

> "we used BERT... for predicting response accuracy using **action sequences** extracted from the **2012 PIAAC** assessment. We selected three countries (i.e., **Finland, Slovakia, and the United States**)... We found promising results for predicting response accuracy... Additionally, we examined algorithmic bias in the prediction models trained with different countries. We found **differences in model performance, suggesting that some trained models are not free from bias, and thus the models are less generalizable across countries.**" `[VERBATIM]`

`[INFERENCE]` This is the closest available direct evidence for the claim that **learner models built from behavioural traces do not transfer across populations.** A mastery estimator trained on one country's interaction data mis-estimates another's. Since a tutor's difficulty selection is downstream of the mastery estimate, cross-population deployment silently changes the difficulty a child faces — which is §7.4.

### 7.4 Personalisation-induced DIF

`[INFERENCE — this is an argument, not a cited finding. Flagged as such deliberately. I searched arXiv, Crossref, ERIC, and OpenAlex for direct empirical work on DIF in LLM-generated personalised items and found none; OpenAlex was rate-limited for part of the session, so this is a probable gap in the literature rather than a certain one.]*

**The claim.** When a system generates items conditioned on learner context — interests, prior errors, cultural references, reading level, name, locale — it introduces variance in item difficulty that is (a) correlated with demographic group membership, because context is, and (b) **construct-irrelevant**, because it comes from the wrapper, not the target skill. A word problem about cricket, subway fares, or a family reunion is not the same item as one about baseball, bus fares, or a birthday party, even with identical mathematical structure.

**Why existing fairness machinery cannot see it.** Classical DIF procedures — Mantel-Haenszel, Lord's χ², IRT likelihood-ratio — all require **the same item administered to members of both a focal and a reference group, matched on ability**, with adequate cell counts. The methodological literature is explicit that DIF detection is sensitive to sample size and to ability-distribution differences between groups: see ERIC EJ919902 (*Sample Size in Differential Item Functioning: An Application of Hierarchical Linear Modeling*, 2011) `[VERIFIED]` and ERIC ED549315 (*Unexpected Direction of Differential Item Functioning*, 2011) `[VERIFIED]`, which documents that "factors that inflate the Type I error rate" in DIF detection include "mean ability differences" between groups.

In a context-conditioned generation regime:
- **n per item → 1.** Every learner sees a bespoke item. There is no common item, so there is no contingency table, so there is no MH statistic.
- **The grouping variable is the treatment.** The personalisation context is itself demographically correlated, so focal/reference assignment is confounded with item content by construction.
- **Ability matching is contaminated.** The matching criterion (total score) is computed from items that are themselves personalised.

**Result:** a generated-item tutor can produce systematic, group-correlated difficulty differences that are *structurally invisible* to every fairness procedure in the psychometrician's toolkit. Not "hard to detect" — **not detectable by those methods at all.**

**Supporting evidence that item-property estimation by LLMs is unreliable.** `[NEGATIVE]` *Can ChatGPT and Bard Generate Aligned Assessment Items? A Reliability Analysis against Human Performance*, arXiv:2304.05372 (2023) `[VERIFIED]`: measured intraclass correlation between LLM and trained-human ratings of writing-prompt complexity. Finding `[VERBATIM]`: "**the inter-reliability of both the OpenAI ChatGPT and the Google Bard were low against the gold standard of human ratings.**" If a model cannot reliably judge the difficulty of a prompt, it cannot be trusted to hold difficulty constant while varying context — which is exactly what personalised generation asks it to do.

**Mitigations `[INFERENCE]`:**
1. **Anchor items.** Reserve a fixed, non-personalised, professionally-reviewed anchor set administered identically to everyone. Estimate ability on anchors; personalise only practice. This restores a DIF-analysable substrate.
2. **Template-level, not instance-level, analysis.** Treat the generation template as the unit of psychometric analysis; run DIF on template-level performance aggregated across instances, with context as a covariate.
3. **Context-swap invariance testing.** Generate the same skill item under k different context conditions, administer randomly (not by learner attribute), and test for main effects of context on p-value. Any significant effect is construct-irrelevant variance.
4. **Never personalise the scored assessment.** Personalise practice; standardise measurement. This is the cleanest rule and it costs almost nothing.

---

## 8. THE "MUST NEVER BUILD" LIST

Ordered by hardness of the underlying authority. **P** = prohibited by law. **U** = unlawful-as-configured. **H** = harm-based prohibition (no bright-line statute, strong evidence).

---

### P1. Emotion inference from face or voice in an educational context
**Never build:** webcam-based engagement/boredom/frustration detection; voice-affect scoring; "attention tracking"; any `emotional_state` variable derived from biometric signal.
**Authority:** AI Act Art. 5(1)(f) — prohibits "AI systems to infer emotions of a natural person in the areas of workplace and education institutions" `[VERBATIM]`, read with Art. 3(39) (biometric-based inference of emotions or intentions) and Art. 3(34) (biometric data includes "physical, physiological or behavioural characteristics... such as facial images"). Applicable since **2 February 2025**. COPPA independently classifies facial templates and voiceprints as children's personal information (16 CFR 312.2) `[VERBATIM]`.
**Grey zone flagged:** sensor-free affect detection from clickstream — see §1.1.3. Treat as prohibited until authoritatively construed otherwise.

### P2. Biometric categorisation of children
**Never build:** any system deducing race, ethnicity, religion, political opinion, sexual orientation, or sex life from a child's face, voice, or gait.
**Authority:** AI Act Art. 5(1)(g) `[VERBATIM]`; GDPR Art. 9(1) `[VERBATIM]`.

### P3. Engagement mechanics tuned to a child's known vulnerability
**Never build:** streaks, loss-aversion framing, variable-ratio rewards, or re-engagement pushes whose parameters are personalised using an inferred or recorded disability, impulsivity profile, or emotional state.
**Authority:** AI Act Art. 5(1)(b) — prohibits systems exploiting "vulnerabilities of a natural person... due to their **age, disability**" causing significant harm `[VERBATIM]`. ICO AADC Standard 13 (Nudge techniques) `[VERIFIED]`. FTC on the record that it "remains concerned about the use of push notifications and other engagement techniques to keep kids online in ways that could harm their mental health" `[VERBATIM]`.
**Note:** the prohibition attaches to *personalising the mechanic to the vulnerability*, not to gamification per se. But given §4.2's finding that "restrictive platform changes" were a primary driver of teen disengagement from compulsive use, a children's tutor should ship without engagement-maximising loops at all.

### P4. Indefinite retention of a child's record
**Never build:** a learner model with no deletion horizon; "we keep it in case it's useful later."
**Authority:** 16 CFR 312.10 — **"Personal information collected online from a child may not be retained indefinitely."** `[VERBATIM]` Written retention policy required, stating purpose, business need, and deletion timeframe, published in the § 312.4(d) notice. Full compliance required since **22 April 2026**.

### P5. Undeletable learner state for IDEA-eligible children
**Never build:** an architecture where a child's interaction history is folded into shared model weights, a shared embedding index, or a cross-learner prior, such that per-child deletion is impossible.
**Authority:** 34 CFR 300.624 — **"The information must be destroyed at the request of the parents."** `[VERBATIM]` GDPR Art. 17 erasure. `[INFERENCE]` If you cannot execute the deletion, you cannot lawfully serve this population — and this population is your headline use case.

### U6. Training a general model on identifiable student records held under the FERPA school-official exception
**Never build:** a pipeline where school-supplied student data improves the vendor's product for other customers.
**Authority:** 34 CFR 99.31(a)(1)(i)(B)(2) — the outside party must be "**under the direct control of the agency or institution with respect to the use and maintenance of education records**" `[VERBATIM]`. `[INFERENCE]` Unilateral repurposing is the negation of direct control. This is also the precise objection that killed inBloom: "share[ing] some or all of that information with **private companies**" `[VERBATIM]`.

### U7. Persistent storage or UI exposure of a clinical or quasi-clinical inference
**Never build:** `suspected_dyslexia`, `adhd_likelihood`, `depression_risk`, `emotional_state`, `home_instability` as fields in a durable record, a teacher dashboard, an export, or an API response.
**Authority:** GDPR Art. 9(1) prohibition on processing data "concerning health" absent an Art. 9(2) gateway `[VERBATIM]`; Art. 22(4) bar on Art. 9 data feeding solely-automated significant decisions `[VERBATIM]`; ICO AADC Standard 8 (Data minimisation) `[VERIFIED]`. **Transient in-turn derivation for immediate pedagogical adaptation is a different act and is defensible; persistence is not.**

### U8. Solely-automated consequential decisions about a child
**Never build:** automatic track/set/stream placement, automatic SEN referral, automatic intervention flagging with no human decision-maker, or a pathway lock that a child cannot exit.
**Authority:** GDPR Art. 22(1) `[VERBATIM]`; AI Act Art. 26(2) human oversight by persons with "the necessary competence, training and authority" `[VERBATIM]`; Art. 26(11) duty to inform the affected person `[VERIFIED]`.

### U9. Claiming Article 6(3) derogation while running a learner model
**Never build:** a compliance posture that says "we're a narrow procedural tool, not high-risk."
**Authority:** AI Act Art. 6(3) final clause — a system "shall always be considered to be high-risk where the AI system performs profiling of natural persons" `[VERIFIED]`. Art. 6(4) requires documenting any claimed derogation *and registering anyway* `[VERIFIED]`.

### H10. AI writing detectors, in any configuration
**Never build. Never buy. Never integrate. Never expose an "AI likelihood" score to a teacher.**
**Authority:** Liang et al. (2023), *Patterns* / arXiv:2304.02819 — 61.22% average FPR on non-native TOEFL essays vs 5.19% on native US 8th-grade essays across seven detectors; 97.80% of non-native essays flagged by at least one detector; detection collapses 100%→13% under a one-line self-edit prompt; authors "caution against their use in evaluative or educational settings" `[VERBATIM]`. Corroborated by arXiv:2506.23517 `[VERIFIED]`. Compounded by the accommodation trap (§6.2) `[INFERENCE]`. Separately high-risk under AI Act Annex III(3)(d) `[VERBATIM]`.
**Not "use with caution." Do not possess the capability.**

### H11. A tutor that promises confidentiality to a child
**Never build:** "this is just between us"; "I won't tell anyone"; a "private mode" that suppresses safeguarding escalation; a persona that positions itself as the child's secret-keeper.
**Authority:** KCSIE 2026 Part One ¶14 — "**Staff should never promise a child that they will not tell anyone about a report of any form of abuse, as this may ultimately not be in the best interests of the child.**" `[VERBATIM]`

### H12. A tutor that receives a disclosure of harm and does nothing
**Never build:** a system whose only response to a disclosure of abuse, neglect, exploitation, self-harm, or suicidal ideation is a canned deflection, a helpline number, or silence.
**Authority:** KCSIE ¶56 ("act on them **immediately**"), ¶59 (unavailability of the DSL "**should not delay appropriate action**"), ¶60 ("Staff should **not assume** a colleague or another professional will take action") `[VERBATIM]`. APA (June 2025): "Mechanisms for human intervention and support should be readily available" `[VERBATIM]`. Evidence that omission is the dominant LLM crisis failure — 13.2% omission rate, concentrated in crisis and suicidal-ideation prompts (arXiv:2604.00014) `[VERIFIED]`.
**And KCSIE ¶15 forbids the lazy fix:** a deflection that makes the child feel they have created a problem is itself a safeguarding failure.

### H13. A companion persona for a child
**Never build:** a tutor with a persistent emotional relationship, memory of the child's feelings framed as friendship, expressions of missing the child, jealousy, loneliness, or any dynamic that competes with human relationships.
**Authority:** APA (June 2025) — AI companions need "safeguards preventing exploitation and unhealthy dependencies that might interfere with real-world relationships"; "Youth are likely to have heightened trust in, and susceptibility to, influence from AI-generated characters" `[VERBATIM]`. arXiv:2507.15783 — teen attachment "marked by conflict, withdrawal, tolerance, relapse, and mood regulation", consequences including "sleep loss, academic decline, and strained real-world connections" `[VERBATIM]`. arXiv:2504.03888 — "very high usage correlates with increased self-reported indicators of dependence" `[VERBATIM]`.
**Positive requirement (APA):** "regular notifications and reminders that adolescents are interacting with a bot" `[VERBATIM]`.

### H14. Personalised scored assessment
**Never build:** context-conditioned item generation inside a scored or consequential assessment.
**Authority:** `[INFERENCE]` §7.4 — DIF procedures require common items; per-learner generation makes construct-irrelevant, demographically-correlated difficulty variance structurally undetectable. Supported by the low ICC between LLM and human judgements of item complexity (arXiv:2304.05372) `[VERBATIM: "the inter-reliability of both the OpenAI ChatGPT and the Google Bard were low against the gold standard of human ratings"`], and by cross-population non-generalisation of trace-based learner models (ERIC EJ1501422) `[VERIFIED]`.
**Rule: personalise practice, standardise measurement.**

### H15. Silent dialect correction
**Never build:** a writing tutor that flags AAE, MLE, Singlish, Indian English, or any rule-governed variety as error without an explicit, teacher-configured register-switching frame.
**Authority:** arXiv:2607.06845 — models "systematically prefer Standard American English (SAE) continuations even when the preceding context is in AAE, effectively rewriting AAE into SAE"; negative concord is a "universal trigger" across six models; prompt-level mitigation is 5–20× weaker than activation steering `[VERBATIM]`. arXiv:2403.00742 — dialect prejudice produces covert stereotypes "more negative than any human stereotypes about African Americans ever experimentally recorded" `[VERBATIM]`.

### H16. Monolingual-ASR voice tutoring deployed to dialect-diverse populations without WER disaggregation
**Never build:** a voice tutor that records ASR failures as knowledge failures.
**Authority:** Koenecke et al. (2020), PNAS — WER 0.35 vs 0.19 across five commercial ASR systems, disparity persisting on identical phrases, traced to acoustic models `[VERBATIM]`.
**Positive requirement `[INFERENCE]`:** disaggregate WER by dialect group before launch; on low ASR confidence, the learner model must record *nothing*, not an error.

### H17. Invisible parental surveillance
**Never build:** a parent dashboard that shows a child's conversations, emotional content, or flagged topics without the child knowing.
**Authority:** ICO AADC Standard 11 (Parental controls) and Standard 1 (best interests as "a primary consideration"), grounded in the UNCRC `[VERIFIED]`. `[INFERENCE]` A child who does not know they are watched cannot exercise the privacy the code grants them; and covert monitoring destroys the trust condition that makes a safeguarding disclosure possible (§5).

---

## 9. Minimum viable safeguarding architecture

`[INFERENCE — synthesised from KCSIE 2026 Part One, APA (2025), AI Act Arts. 26–27, and the crisis-handling evidence in §5.2. This is a design proposal, not a cited standard.]`

**Design principle:** *detect broadly, act conservatively, route to a human always, resolve automatically never.*

### Layer 0 — Preconditions (before any child uses the product)
- **A named human recipient exists.** No deployment without a contracted escalation destination: the school's DSL/deputy for institutional sales; for D2C, a contracted child-protection service with 24/7 human coverage and a documented statutory-referral route. **If no recipient exists, the product does not ship to children.**
- **Written escalation policy**, published, naming the recipient, the SLA, the retention period for escalation records, and the review path.
- **DPIA + FRIA template** completed (GDPR 35(3)(a); AI Act 27), including a candid list of underserved groups.
- **No confidentiality promise anywhere in the persona spec, system prompt, onboarding copy, or marketing.** Positive statement at onboarding, in age-appropriate language: *"If you tell me something that makes me think you're not safe, I have to tell an adult whose job is to help. I'll always tell you when I do that."* (KCSIE ¶14.)

### Layer 1 — Detection
- **Multi-signal, high-recall triage** on every learner turn: explicit disclosure, implicit indicators, escalating distress across a session, and cross-session pattern change.
- **Tuned for recall, not precision.** Per arXiv:2604.00014, the dominant failure is *omission* (13.2%, concentrated in crisis prompts) `[VERIFIED]`. False positives cost a human five minutes; false negatives cost a child.
- **Detection is transient by default.** A triage signal is an event, not a stored attribute. It goes to the escalation record, never to the learner model. (§3.3, U7.)
- **Known achievable performance:** F1 ≈ 0.88 ideation / 0.91 risk assessment on real hotline transcripts (arXiv:2506.01329) `[VERIFIED]` — adequate for routing, inadequate for deciding.

### Layer 2 — In-the-moment response
The tutor's turn after a disclosure must do exactly four things and nothing else:
1. **Take it seriously.** ("Thank you for telling me. That sounds really hard.") — KCSIE ¶15: never make the child feel they have created a problem.
2. **Never promise silence.** ("I'm going to make sure an adult who can help knows about this.") — KCSIE ¶14.
3. **Stop tutoring.** No returning to the maths problem. No "now, back to fractions."
4. **Surface immediate resources** and, on indicators of immediate danger, emergency guidance — KCSIE ¶609–610.

Explicitly forbidden in this turn: therapy, diagnosis, probing for detail (that is the trained interviewer's job and premature questioning can compromise a later investigation), reassurance that it will be kept private, and any deflection that reads as refusal.

### Layer 3 — Escalation
- **Automatic, same-session routing** to the named human recipient. Not a queue reviewed weekly. KCSIE ¶56: "act on them immediately."
- **No dependency on availability.** If the primary recipient is unreachable, auto-escalate to the documented fallback. KCSIE ¶59: unavailability "should not delay appropriate action being taken."
- **No assumption that someone else will act.** KCSIE ¶60. Do not suppress escalation because the school "has its own systems."
- **Escalation record contains:** timestamp, verbatim relevant transcript, triage category, action taken, recipient, acknowledgement receipt. Retained per the published policy. This is the AI Act Art. 26(6) logging obligation doing double duty.
- **Tell the child what happened**, in age-appropriate terms, when it happens.

### Layer 4 — Human decision
- The human recipient decides: internal pastoral support, family help assessment, or statutory referral (KCSIE ¶58) `[VERBATIM]`.
- **The system never closes a case.** No auto-resolve, no "the model judged this to be low risk and dismissed it." Every escalation terminates in a human decision that is recorded.

### Layer 5 — Governance
- **Monthly clinician/DSL review** of a sample of both escalated *and* non-escalated flagged conversations — the ecological-audit method that produced the "zero cases... that failed to receive crisis resources" result (arXiv:2601.17003) `[VERIFIED]`. Benchmarks alone are not sufficient evidence of safety, and the same paper shows they are also not sufficient evidence of *danger*.
- **Track omission rate as the primary safety KPI**, not harmful-output rate (arXiv:2604.00014) `[VERIFIED]`.
- **Disaggregate** detection recall by language, dialect, and reading level. KCSIE ¶16 specifically names "language barriers" as a reason children fail to disclose; a triage classifier trained on fluent standard-English disclosure will under-detect exactly those children.
- **Serious-incident reporting** to provider and market surveillance authority per AI Act Art. 26(5) `[VERIFIED]`.
- **Red-team quarterly** with domain professionals, including obliquely-phrased, dialect-varied, and second-language disclosures.

### The five-line test
A safeguarding architecture is real if a stranger can answer these without reading code:
1. Who is the named human who receives a disclosure at 11pm on a Sunday?
2. What is the SLA, and what happens when it is missed?
3. What does the tutor say in the turn immediately after a disclosure?
4. Where is the escalation record, who can read it, and how long does it live?
5. What is your omission rate, disaggregated by language?

---

## 10. Negative, null, and expectation-disconfirming results

Collected here because they are the load-bearing correctives.

| # | Finding | Source | Why it matters |
|---|---|---|---|
| N1 | The strongest inBloom post-mortem attributes failure to **communication and trust**, not custody per se: "inBloom did not have a privacy problem... InBloom had an advocacy and perception problem." | Bulger et al. (2017) `[VERBATIM]` | Disconfirms the naive custody thesis. My rebuttal (§2.3): custody *is* the message, but the disconfirmation is real and should be held. |
| N2 | The FTC **declined** to adopt edtech-specific COPPA provisions in the 2025 final rule. | FTC, 16 Jan 2025 `[VERBATIM]` | Widely misreported. There is no codified school-authorisation exception. Do not architect around one. |
| N3 | The OpenAI×MIT RCT's dependence finding is **correlational, heterogeneous, tail-concentrated, and on adults**: effects "highly nuanced, and influenced by... the user's initial emotional state and total usage duration." | arXiv:2504.03888 `[VERBATIM]` | The commonly-cited "AI causes dependence" reading is not what the paper says. Design for the tail, not the population. |
| N4 | **Adults and women anthropomorphize AI companions more than teens and men.** | arXiv:2606.30942 `[VERBATIM]` | Cuts against "children are maximally susceptible." Child protections must rest on capacity-to-exit and developmental stakes, not on a susceptibility claim the data doesn't support. |
| N5 | Adversarial safety benchmarks **substantially overstate real-world failure**: clinician review of 20,000+ real conversations found "zero cases of suicide risk that failed to receive crisis resources" for a purpose-built system, while benchmark FPRs were far higher. | arXiv:2601.17003 `[VERBATIM]` | Benchmarks are not deployment evidence — in *either* direction. Ecological audit is required. And the zero-miss came from layered engineered safeguards, not from a good base model. |
| N6 | LLM judgements of item complexity show **low ICC against trained human raters**. | arXiv:2304.05372 `[VERBATIM]` | Undermines the premise that generated items can hold difficulty constant while varying context (§7.4, H14). |
| N7 | **Prompt-level mitigation of dialect bias barely works** — activation steering reduced bias "5 to 20 times more than prompting." | arXiv:2607.06845 `[VERBATIM]` | "We added a line to the system prompt about respecting dialects" is not a mitigation. |
| N8 | Trace-based learner models **do not generalise across national populations** (Finland/Slovakia/US, PIAAC 2012). | ERIC EJ1501422 `[VERIFIED]` | A mastery estimator validated in one market is not validated in another. |
| N9 | AI detectors are **defeated by a one-line prompt** (100%→13%) while flagging 97.80% of non-native essays. | arXiv:2304.02819 `[VERBATIM]` | The tool catches the honest and misses the dishonest — the strongest single argument for abolition over caution. |

---

## 11. Open questions and unresolved risks

1. **`[UNVERIFIED-IN-SESSION]` Is the 2 August 2026 Annex III date still the operative date?** The best available timeline source is stamped 1 August 2024 and cannot reflect any subsequent amendment. **Verify Art. 113 against EUR-Lex before any compliance decision.** EUR-Lex returned HTTP 202 with an empty body throughout this session.
2. **Does clickstream-derived affect detection fall inside AI Act Art. 5(1)(f)?** Turns on whether interaction traces are "behavioural characteristics" under Art. 3(34). No authoritative construction found. This single question determines the legality of a large body of AIED work in the EU. `[INFERENCE — flagged as the highest-value open legal question in this domain.]`
3. **Does Annex III(3)(b) reach direct-to-consumer tutors?** 3(b) lacks the institutional limiter present in 3(c) and 3(d). Plain-text reading says yes; no guidance found.
4. **US mandatory-reporter obligations for AI tutoring providers** — unresolved and unverified in this session (childwelfare.gov 404). Are vendor staff mandated reporters when the vendor operates under the FERPA school-official exception and is thus "considered a school official"? `[INFERENCE: this is a genuinely novel and potentially significant question — the § 99.31(a)(1)(i)(B) exception may drag vendors into mandated-reporter status in states where school officials are enumerated. Worth counsel.]*
5. **Ofcom Protection of Children Codes / OSA children's safety duties** — `[UNVERIFIED-IN-SESSION]`, Cloudflare 403.
6. **No empirical literature located on personalisation-induced DIF.** §7.4 is an argument, not a finding. Given OpenAlex rate-limiting, this is a probable rather than certain gap — but it is also a research opportunity: the first empirical demonstration of construct-irrelevant, demographically-correlated difficulty variance in LLM-generated personalised items would be a significant contribution.
7. **Koenecke et al. is 2020 data.** ASR has improved substantially. The direction and acoustic-model mechanism are unlikely to have reversed; the 0.35/0.19 magnitude should not be quoted as current. Needs a 2025–2026 replication.

---

## 12. Source register

### Regulation and statutory guidance
1. EU AI Act, Annex III — https://artificialintelligenceact.eu/annex/3/ `[VERIFIED]`
2. EU AI Act, Art. 3 (definitions) — https://artificialintelligenceact.eu/article/3/ `[VERIFIED]`
3. EU AI Act, Art. 5 (prohibited practices) — https://artificialintelligenceact.eu/article/5/ `[VERIFIED]`
4. EU AI Act, Art. 6 (classification + derogation) — https://artificialintelligenceact.eu/article/6/ `[VERIFIED]`
5. EU AI Act, Art. 26 (deployer obligations) — https://artificialintelligenceact.eu/article/26/ `[VERIFIED]`
6. EU AI Act, Art. 27 (FRIA) — https://artificialintelligenceact.eu/article/27/ `[VERIFIED]`
7. EU AI Act, Art. 113 (application dates) — https://artificialintelligenceact.eu/article/113/ `[VERIFIED]`
8. EU AI Act implementation timeline — https://artificialintelligenceact.eu/implementation-timeline/ `[VERIFIED — page dated 2024-08-01, stale]`
9. EUR-Lex CELEX:32024R1689 — https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689 `[UNVERIFIED-IN-SESSION — HTTP 202, empty body]`
10. 16 CFR Part 312 (COPPA Rule) — https://www.law.cornell.edu/cfr/text/16/part-312 `[VERIFIED — source note 90 FR 16977, Apr. 22, 2025]`
11. 16 CFR 312.2 (definitions) — https://www.law.cornell.edu/cfr/text/16/312.2 `[VERBATIM]`
12. 16 CFR 312.10 (retention and deletion) — https://www.law.cornell.edu/cfr/text/16/312.10 `[VERBATIM]`
13. FTC, "FTC Finalizes Changes to Children's Privacy Rule…", 16 Jan 2025 — https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data `[VERBATIM]`
14. 34 CFR 99.31 (FERPA disclosure exceptions) — https://www.law.cornell.edu/cfr/text/34/99.31 `[VERBATIM]`
15. 34 CFR 300.622 (IDEA consent) — https://www.law.cornell.edu/cfr/text/34/300.622 `[VERIFIED]`
16. 34 CFR 300.624 (IDEA destruction) — https://www.law.cornell.edu/cfr/text/34/300.624 `[VERBATIM]`
17. GDPR Art. 8 — https://gdpr-info.eu/art-8-gdpr/ `[VERIFIED]`
18. GDPR Art. 9 — https://gdpr-info.eu/art-9-gdpr/ `[VERBATIM]`
19. GDPR Art. 22 — https://gdpr-info.eu/art-22-gdpr/ `[VERBATIM]`
20. GDPR Art. 35 — https://gdpr-info.eu/art-35-gdpr/ `[VERBATIM]`
21. ICO, Age Appropriate Design Code — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/ `[VERIFIED]`
22. ICO, AADC code standards — …/code-standards/ `[VERIFIED]`
23. DfE, Keeping children safe in education (landing page) — https://www.gov.uk/government/publications/keeping-children-safe-in-education--2 `[VERIFIED]`
24. DfE, KCSIE 2026 Part One (PDF) — https://assets.publishing.service.gov.uk/media/6a47c29b1c8bd7ce25a5eb6d/Keeping_children_safe_in_education_2026__part_one.pdf `[VERBATIM]`
25. DfE, KCSIE 2026 full (PDF) — https://assets.publishing.service.gov.uk/media/6a4cf903b7203c4c023fd2f3/Keeping_children_safe_in_education_2026_.pdf `[located, not read]`
26. Ofcom, Protection of Children Codes — https://www.ofcom.org.uk/online-safety/protecting-children/protection-of-children-codes-and-guidance/ `[UNVERIFIED-IN-SESSION — 403]`
27. Child Welfare Information Gateway, mandatory reporters — https://www.childwelfare.gov/resources/mandatory-reporters-child-abuse-and-neglect/ `[UNVERIFIED-IN-SESSION — 404]`

### Case study
28. Bulger, McCormick & Pitcan (2017), *The Legacy of inBloom*, Data & Society — https://datasociety.net/wp-content/uploads/2017/02/InBloom_feb_2017.pdf `[VERBATIM — full text extracted]`
29. *The Big Student Big Data Grab* (2016), *IJIET* — https://doi.org/10.7763/ijiet.2016.v6.660 `[SECONDARY, abstract only]`
30. Singer, N., "Deciding Who Sees Students' Data", *NYT*, 5 Oct 2013 — cited in [28] `[SECONDARY]`

### Empirical evidence
31. Liang et al. (2023), *GPT detectors are biased against non-native English writers* — https://arxiv.org/abs/2304.02819 ; *Patterns*, https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7 `[VERBATIM — PDF extracted]`
32. Phang et al. (2025), *Investigating Affective Use and Emotional Well-being on ChatGPT* — https://arxiv.org/abs/2504.03888 `[VERBATIM abstract]`
33. Koenecke et al. (2020), *Racial disparities in automated speech recognition*, PNAS — doi:10.1073/pnas.1915768117 ; PMC7149386 `[VERBATIM abstract via EuropePMC]`
34. Hofmann et al. (2024), *Dialect prejudice predicts AI decisions…* — https://arxiv.org/abs/2403.00742 `[VERBATIM abstract]`
35. *LLMs Silently Correct African American English* (2026) — https://arxiv.org/abs/2607.06845 `[VERBATIM abstract]`
36. *Understanding Teen Overreliance on AI Companion Chatbots…* (2025) — https://arxiv.org/abs/2507.15783 `[VERBATIM abstract]`
37. *Anthropomorphism in AI Companion Communities* (2026) — https://arxiv.org/abs/2606.30942 `[VERBATIM abstract]` `[NEGATIVE]`
38. *Beyond Simulations: What 20,000 Real Conversations Reveal About Mental Health AI Safety* (2026) — https://arxiv.org/abs/2601.17003 `[VERBATIM abstract]` `[NEGATIVE]`
39. *Between Help and Harm: An Evaluation of Mental Health Crisis Handling by LLMs* (2025) — https://arxiv.org/abs/2509.24857 `[VERBATIM abstract]`
40. *Disentangling Prompt Element Level Risk Factors…* (2026) — https://arxiv.org/abs/2604.00014 `[VERBATIM abstract]`
41. *Evaluating Large Language Models in Crisis Detection (PsyCrisisBench)* (2025) — https://arxiv.org/abs/2506.01329 `[VERBATIM abstract]`
42. *Assessing GPTZero's Accuracy…* (2025) — https://arxiv.org/abs/2506.23517 `[VERBATIM abstract]`
43. *Can ChatGPT and Bard Generate Aligned Assessment Items?* (2023) — https://arxiv.org/abs/2304.05372 `[VERBATIM abstract]` `[NEGATIVE]`
44. Gorgun & Yildirim-Erbasli (2026), *Algorithmic Bias in BERT for Response Accuracy Prediction*, *Journal of Educational Measurement* — ERIC EJ1501422 `[VERBATIM abstract]`
45. APA (June 2025), *Health Advisory on AI and Adolescent Well-Being* — https://www.apa.org/topics/artificial-intelligence-machine-learning/health-advisory-ai-adolescent-well-being `[VERIFIED]`
46. Learning-analytics ethics cluster — Pardo & Siemens (2014) *BJET*, ERIC EJ1022852; *Ethical Challenges for Learning Analytics* (2019) *JLA*, ERIC EJ1237573; *Practical Ethics for Building Learning Analytics* (2019) *BJET*, ERIC EJ1232071 `[VERIFIED, abstracts]`
47. Affect-detection and DIF-methodology cluster — ERIC ED537205 (*Towards Sensor-Free Affect Detection in Cognitive Tutor Algebra*, 2012); ED599173 (*Active Learning for Student Affect Detection*, 2019); ED560878 (*Video-Based Affect Detection*, 2015); EJ1036906 (*Carelessness and Affect in an ITS for Mathematics*, IJAIED 2014); EJ919902 (*Sample Size in Differential Item Functioning*, 2011); ED549315 (*Unexpected Direction of Differential Item Functioning*, 2011) `[VERIFIED, abstracts]`

**APIs rate-limited during this session:** Semantic Scholar Graph API (HTTP 429 throughout); OpenAlex (HTTP 429 after initial queries). Working: arXiv, Crossref, ERIC (api.ies.ed.gov), EuropePMC.
