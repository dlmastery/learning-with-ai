# Learning with AI

This project asks a practical question:

**What would it take to give any learner sustained access to excellent, personal
instruction across subjects, ages and abilities?**

The intended reach is broad: a child learning to read, a student struggling with
algebra, an adult changing careers, or a graduate student trying to understand a
difficult proof. The system should be especially useful when ordinary instruction
creates unnecessary barriers—for example, when a learner understands a concept but
cannot show it through a worksheet, long passage or timed response.

This is personal. The work began with an eleven-year-old served under a SELPA plan.
Accessibility is therefore a design requirement from the beginning.

## The opportunity

Current AI systems can converse in real time, inspect images and documents, execute
code, generate interactive software, create diagrams and video, maintain state across
sessions, and coordinate specialized agents.

Education products use only a small part of this capability. Most remain chat
interfaces attached to course material.

The larger opportunity is a learning environment that can:

- establish what the learner knows before choosing where to begin;
- notice the reasoning behind an answer, including partial understanding;
- explain the same idea through language, diagrams, examples, simulation and
  formal notation;
- watch the learner work and respond to the step where understanding breaks;
- change approach when the current one fails;
- let the learner demonstrate knowledge through an appropriate response mode;
- remember earlier work and revisit it when useful;
- help with initiation, planning, attention and recovery from interruptions;
- require independent performance before recording mastery;
- connect books, courses, teachers, authors and other trusted sources;
- remain affordable and usable on ordinary devices.

No published system in this research collection combines all of those properties.
Building and evaluating that system is the project.

## What the research says

The early evidence for generative-AI tutoring is promising and incomplete.

- Purpose-built AI tutoring has improved immediate learning in controlled studies.
- Supervised deployments show that AI can help human tutors provide more consistent
  support at low inference cost.
- Unrestricted answer-giving can improve assisted work while weakening later
  independent performance.
- Delayed, unassisted transfer is rarely measured.
- Learners with disabilities are almost absent from the randomized evidence.

These findings do not establish a ceiling for AI tutoring. They identify the next
systems and experiments worth building.

The research also supports several durable design choices:

- diagnose prior knowledge rather than infer ability from age or course placement;
- use active attempts and produced work as evidence;
- separate practice completed with help from independent mastery;
- match the representation to the concept and the learner's obstacle;
- use retrieval and spacing for durable memory;
- give progress data a specific instructional response;
- evaluate effects by subgroup as well as by average;
- preserve source provenance and expose uncertainty.

The detailed evidence, qualifications and primary sources are in
[`research/raw/`](research/raw/).

## Repository

| Path | Purpose |
|---|---|
| [`research/raw/`](research/raw/) | Research reports based primarily on papers, technical documentation and product inspection |
| [`survey/`](survey/) | Thematic drafts assembled from the research |
| [`PAPER.md`](PAPER.md) | Current long-form manuscript |
| [`docs/demos/`](docs/demos/) | Browser prototypes of individual mechanisms |
| [`CORRECTIONS.md`](CORRECTIONS.md) | Public record of factual and editorial corrections |
| [`evidence/`](evidence/) | Reviews, validation scripts and reproducible experiments |
| [`process/`](process/) | Scope, assumptions and editorial process |
| [`TASK.md`](TASK.md) | The owner's requests and unresolved decisions |

## Current status

The research collection and mechanism prototypes are substantial. The public
presentation is being rebuilt.

- The pitch deck is undergoing a complete rewrite.
- The paper is being reduced and reorganized into a publishable argument.
- The dashboard is being redesigned around the product thesis and research program.
- The previous “University in a Box” walkthrough was a scripted interface prototype,
  not a credible product demonstration. It is being removed from the primary
  presentation.

The existing paper, deck and dashboard should be treated as working drafts until that
editorial rebuild is complete.

## Research standards

Published claims should be traceable to primary sources where available. Product
claims are identified as such. Demonstrations show implementation behavior; they do
not count as learning evidence.

Corrections are recorded in [`CORRECTIONS.md`](CORRECTIONS.md). The repository includes
checks for internal links, repeated prose, superseded values and demo rendering.

To rebuild the manuscript and web edition:

```bash
python3 evidence/build-paper.py --html
```

## Contributing

Useful contributions include:

- a primary source that changes a published claim;
- a missing capability, population or field of learning;
- a reproducible failure in a demonstration;
- an experimental design that distinguishes the proposed system from a strong
  frontier-model baseline;
- a concrete accessibility requirement the current design misses.

Please open an issue with enough detail to reproduce the claim or problem.
