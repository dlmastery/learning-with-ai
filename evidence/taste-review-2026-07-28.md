# Taste review — 2026-07-28

A presentation-only pass over `docs/` and `README.md`. No survey content was edited: `survey/`,
`research/raw/`, `PAPER.md` and `CORRECTIONS.md` are untouched, and `PAPER.md` is byte-identical to
what the generator produced before this pass. Content problems found along the way are listed at the
bottom rather than fixed here.

---

## The single worst thing

**Every one of the survey's contents links was dead.** All 29 at the time of the audit (102 internal
links now, after the rail was added). `build()` slugged its anchors from the bare section title while
python-markdown slugged the rendered heading text, which carries the section number — so
`#the-floor-what-learning-science-actually-established` pointed at nothing, and the heading was
`id="1-the-floor-what-learning-science-actually-established"`. Two hand-matched slugging rules, no
test.

The docstring on `build_html` said "a single readable web page with a sticky contents rail." There
was no rail. There was a floating button labelled `↑ Contents` that scrolled to the top of a 236,000-
pixel page. 75,000 words, one column, 860px wide, no navigation, no position indication, and a
contents list where none of the links worked.

That is the whole diagnosis in one artifact: the work is serious and the presentation was never
looked at.

---

## Confirming or replacing the brief's diagnosis

| The brief said | Verdict |
|---|---|
| Front door leads with backstage material | **Confirmed, and worse than stated.** The dashboard had no link to the survey at all until ~10,000px down. |
| Dashboard is a data dump | **Confirmed**, plus a "Where the work stands" progress table reporting *to ourselves*, with "24 of 32 · 10 remaining" (24 of 32 leaves 8). |
| `paper.html` unreadable | **Confirmed**, see above. |
| No coherent identity | **Confirmed.** Three copies of the palette had already drifted: `.wrap` 980 vs 960, `h2` 31px vs 27px, `code` 12.5px vs 13px, `.pill` and `.chip` doing the same job under two names. |

Two things the brief did not name, both worse than a layout problem:

- **The dashboard's headline numbers were stale by a wide margin** — "24 survey sections · 60,300
  words · 23 published corrections" against a paper that was at 30 sections, 75,352 words, 25
  corrections. On a page whose entire pitch is *we publish our own errors*, that is the most damaging
  possible defect. C-23 is a correction *about exactly this failure mode* and the fix had not been
  generalised.
- **`README.md` opened with "A 740,000-word survey"** — an order of magnitude out.

---

## What changed

### A. Information architecture

**`docs/index.html`.** First screen is now: title, one-sentence question, two actions
(`Read the survey` / `Run the demos`), and four facts. Nothing about process is above the fold.
The page's argument now runs findings → evidence → span → consequences → open questions → where to
go next, and *ends* with `How to check this` — credibility as a closing argument rather than a
headline. Backstage material (`AUDIT.md`, `research/raw/`, the checker commands, the review reports)
is behind one `<details>` in that final section: reachable in one click, invisible otherwise.

**`README.md`** reordered: what it is and where to read it → three findings → why it exists → the
central claim and how to falsify it → how to check it → repository map last. The map was previously
in the middle of the argument.

### B. `docs/paper.html` — the reading experience

All via `evidence/build-paper.py`; the output is never hand-edited.

- `build()` now returns a **declarative outline** (parts, sections, anchors, word counts). The
  contents rail, the contents page and the section headings are all rendered from that one record,
  so an anchor cannot exist in one and be missing in another. This is the same discipline the project
  already applies to charts, applied to navigation.
- **Persistent contents rail** at ≥1080px — sticky, own scroll, parts as groups, current section
  marked and auto-scrolled into view. Below 1080px it is a drawer with a scrim, closing on link
  click, Escape, or scrim tap.
- **Position indication**: a sticky top bar showing `Part III · The Ladder of Explanation`, plus a
  2px progress line. One `IntersectionObserver` feeds the rail, the bar and the progress line, so
  they cannot disagree.
- **Part-level structure**: part openers get their own full-width divider, numeral, title and blurb.
  Sections carry `Section 12 of 32` and a `Next →` link, so 32 sections read as a sequence rather
  than a scroll.
- **Heading levels fixed.** Section bodies use `##` for their own subheads, which collided with the
  section heading once stitched into one document — the outline was flat, with 224 subsection
  headings styled identically to the 32 section headings. Bodies are now demoted one level at render
  time (`h2 > h3 > h4`). `PAPER.md` is unchanged.
- **Measure**: 41rem column, 17px/1.72, prose capped at 38rem (~66ch). Was 74ch of 16px in an
  860px box with the right half of a 1400px screen empty.
- Front matter metadata was a run-together paragraph ending in a bare printed URL. It is now a
  four-item fact row (length, structure, sources, reading time).

### C. Coherence

- **New `docs/site.css`** is the single design system: tokens, a named spacing scale (`--s1`–`--s9`),
  type scale, links, tables, callouts, chips, pills, details, footer, theme toggle. Linked by the
  dashboard, the gallery, all 13 demos, and inlined by the paper generator. `docs/demos/demo.css`
  now contains only demo widgets (chat, controls, orientation block, readouts).
- **New `docs/theme.js`** persists the light/dark choice across pages and applies it before first
  paint. Each page keeps its own toggle; this only remembers. No preference stored means
  `prefers-color-scheme` still wins.
- One link-as-action style (`.go`), one page-open (crumb + header), one page-close (footer)
  everywhere.

### D. Bugs found while looking

- **`.q b { display:block }`** — the question-card title rule also caught every inline `<b>` inside
  the body text, so `44.3% of tutor edits were slowing the AI's questioning down` was punched onto
  its own line mid-sentence, in ten of eighteen cards. Pre-existing. Now scoped to `.q > b`.
- **The ladder chart was not ordered**, under a heading that says "Pooled effect sizes, ordered."
  When C-12 corrected Nickow from 0.37 to 0.288 the row stayed where it was, so 0.288 sat above 0.36
  and 0.327. The chart contradicted its own caption. Rows are now sorted in the renderer, from the
  spec, so the chart and the generated table can never disagree with the claim.
- **Raw markdown leaked into HTML.** The corrections table on the dashboard rendered
  `Nickow pooled tutoring **0.37**` and `` `survey/09` `` as literal asterisks and backticks.
- **A class-name collision** introduced during this pass: the top bar's `Contents` button had
  `class="toc"`, which picked up the contents *grid* rules and rendered as an empty box on mobile.
  Caught by screenshotting at 390px. Named `tocbtn`.
- **`summary::before { content:"▸ " }`** — HTML collapses the trailing space, so every disclosure
  read `▸Table view`. Now `\00a0`.

### E. The root cause of the stale numbers

`sync_dashboard()` in `evidence/build-paper.py` now writes the live counts into `docs/index.html`
(`<span data-gen="key">`) and `README.md` (`<!--gen:key-->…<!--/gen-->`) on every build: sections,
words, parts, demos, corrections, and the count of corrections found by an external reviewer. It
counted the drift the first time it ran. C-23 says "the count is generated from the filesystem" —
that was true of the ledger and false of every surface quoting it.

---

## What I removed

Deletion, in rough order of value:

1. **The "Where the work stands" table.** Five rows of progress reporting — sections written,
   reports complete, "10 remaining" — addressed to the authors, on the front page, and internally
   inconsistent. A reader does not need our burndown.
2. **Thirteen identical `Computed` badges** in the demo gallery, one per card. A label that is the
   same on every item conveys nothing; the lede now says it once and the `.ev` line carries the
   number that actually differs.
3. **Three of the gallery's four evidence chips** — `Scripted illustration`, `Shows a null result`,
   `Building — not yet written` — none of which any card used, plus the lede sentence explaining the
   `Building` state and the two-column legend explaining the Computed/Scripted distinction the page
   no longer makes. Advertising states you do not have is the purest form of this problem.
4. **Five of the eight rows** in the dashboard's corrections table. The three kept are the two most
   damaging and the one about the ledger itself. The full ledger is one click away; a reader
   evaluating the project needs the shape of the failures, not all of them.
5. **The dashboard's four stat tiles** (`g=0.50`, `d=0.54`, `d≈0.63`, `−17%`). Every number in them
   appears again in the ladder chart forty pixels below. Replaced with the three findings, which are
   an argument rather than a scoreboard.
6. **The "Editorial standard" callout**, which restated in a box what the header lede and the footer
   already say twice.
7. **The `↑ Contents` button** on the paper — a label that lied about what the control did.
8. **A small-caps opening line** I added to the abstract and then cut on sight. It was decoration,
   and it fought the run-in bold in the same paragraph.
9. **Dead CSS**: `.tag.soon`, `.card.soon`, `.legendbar`, `.card .ev.none`, and roughly 120 lines of
   duplicated tokens and base rules across `index.html` and `demo.css`.
10. **"built incrementally"** from the dashboard eyebrow. It is a fact about us, in the first six
    words a reader sees.

---

## What I deliberately left alone

- **The two charts and their renderers.** `renderBars` / `renderSlope` are the best-engineered thing
  on the site: declarative spec, deterministic renderer, generated accessible table, negative bars
  drawn left of a zero baseline and outlined so they cannot read as short positive ones, and a
  connector explicitly dotted because the columns share no scale. I added a sort and changed nothing
  else.
- **The palette.** No new hues; `--good/--warn/--bad` remain status-only. Neutrals and spacing were
  reorganised into a named scale but not re-valued.
- **The twelve "Findings that change what you build" cards** and both numbered question lists. The
  tag vocabulary is inconsistent in register (`Kills a product`, `Boundary`, `Empty chair`) but the
  writing is the strongest on the site and the tags aid scanning. Normalising them is an editorial
  decision, not a taste fix.
- **The thirteen demo pages' own content.** The shared stylesheet was split under them; nothing else
  changed. `evidence/test-demos.mjs` passes on all 14 pages at 390px and 1400px.
- **The orientation block** (`what this is / why it matters / how to use it`) on every demo. It is
  the single best convention in the project.

---

## Verification

Every page screenshotted and inspected at 390px and 1400px in both colour schemes: `index.html`,
`paper.html`, `demos/index.html`, plus `demos/patha.html` and `demos/refusal-engine.html` as
representatives of the shared-CSS split. Additionally:

```
paper.html   102 internal links, 0 dead   (was 29 links, 29 dead)
all pages    no horizontal page scroll at 390px, no console errors, no leaked markdown
demos        node evidence/test-demos.mjs — ALL DEMO PAGES PASS (14 pages × 2 widths)
ledger       python3 evidence/check-corrections.py --self-test --strict — 14 rules, 50 surfaces, 0 violations
PAPER.md     byte-identical across the refactor
```

The mobile contents drawer was driven through a real open → navigate → auto-close cycle, asserting
the position readout and the progress figure afterwards.

---

## Content problems found, not fixed

These need an author, not a designer:

1. **`CORRECTIONS.md`'s own scoreboard disagrees with itself.** The table says
   `Caught by an adversarial external reviewer | 7`; the prose immediately below says "Eight of
   twenty-five"; the ledger contains 8 `EXTERNAL-REVIEW` rows. This is the one file that must be
   right. The generated surfaces now count the rows, so they say 8, and they will diverge from the
   scoreboard table until it is corrected.
2. **"32 research reports" is stale.** `research/raw/` holds 35 files and is still growing. The
   string is hardcoded in `build-paper.py`'s header *and* written out in `ABSTRACT`, so fixing it
   means editing prose. I removed the count from the dashboard rather than publish a number that
   contradicts the paper.
3. **`check-corrections.py` is checking two files that do not exist.** `SURFACES` lists
   `process/CLAUDE.md` and `process/AUDIT.md`; both live at the repository root. They are silently
   skipped, so `AUDIT.md` and `CLAUDE.md` have never been checked for superseded values.
4. The dashboard's EU AI Act callout is dated `verified 28 Jul 2026`. It carries a live deadline of
   2 August 2026 and will need re-verifying or removing within the week.

---

## What I would do next

1. **Search across the survey.** 78,000 words with a contents rail and no way to find a number in
   it. A prebuilt JSON index over section titles and headings, ~40KB, no dependency, would be the
   next highest-value hour.
2. **Deep links into the paper from the dashboard.** Every card in "Findings that change what you
   build" states a result that lives in a specific section, and none of them link to it. The
   generator already knows every anchor; the dashboard should consume that map rather than have
   anchors typed into it.
3. **A print stylesheet worth the name.** There is a `@media print` block that hides the chrome and
   page-breaks on parts. A survey this size will be printed and annotated; it deserves running
   heads, a real title page and figure numbering.
4. **Fold `sync_dashboard` into a pre-commit hook.** It only runs on `--html` today, so the counts
   are correct only when someone remembers to rebuild. The autosave commits are already frequent
   enough that they will drift again between builds.
5. **A single `figure` component in `site.css`.** The dashboard defines it; the demos each redefine
   something close to it inline. That is the next drift.
