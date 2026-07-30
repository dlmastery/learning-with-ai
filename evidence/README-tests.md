# Page test harnesses

Playwright checks for the dashboard, gallery, and every demo page: JS errors,
console errors, horizontal overflow at 390px, stylesheet presence, chart node
counts, label clipping, and tooltip behaviour.

```bash
mkdir -p /tmp/pw && cd /tmp/pw
npm i playwright@1.62.0 --no-save
npx playwright install chromium-headless-shell
cp ~/learning-with-ai/evidence/test-*.mjs .
node test-pages.mjs   # dashboard + gallery, 3 viewports x 2 colour schemes
node test-demos.mjs   # every docs/demos/*.html at 390px and 1400px
```

Both exit non-zero intent on failure and print one line per configuration.
Paths inside the scripts are absolute to `/home/eranti/learning-with-ai/docs/`.

## Corrections propagation check

```bash
python3 evidence/check-corrections.py            # report
python3 evidence/check-corrections.py --strict   # exit 1 on violation
```

Twelve rules, each derived from a row in `CORRECTIONS.md`. A rule fires when a
superseded value appears on a published surface without its correction within a
600-character window — because a correction that does not reach the sentence it
corrects is not a correction (C-17). `research/raw/` is excluded deliberately:
those reports are an immutable record of what an agent found at a point in time.

On its first run this caught four live violations, including the two the external
reviewer had flagged in `CLAUDE.md`.

## Repetition check

```bash
python3 evidence/check-repetition.py --strict
```

Eight load-bearing findings recur across the survey — Bastani's −17% appeared in ten
of thirty-three sections, Sierra Leone in seven. Reuse is correct; each is doing
different work in a different argument. **Unacknowledged** reuse is not: it inflates
apparent breadth and makes a paper read as a binder of essays.

The rule: outside its home section, a recurring claim must carry a section
cross-reference within a paragraph, so a reader can tell they are meeting an old
finding rather than a new one. First run flagged 21 bare restatements.

## Stance check

```bash
python3 evidence/check-stance.py --strict
```

The mission is that everyone becomes a polymath. The research discipline is
adversarial. Those are compatible only if the discipline is the *warrant* and the
mission is the *message* — and repeatedly that inverted. The dashboard opened on three
disqualifying findings; the deck's identity became "we build the examiner"; section
titles read *"what it cannot buy"* and *"what that is worth"*.

Each was fixed when pointed at and reappeared elsewhere, because nothing measured the
pattern. This does: defensive heading shapes, first-screen stance (claims that
something fails vs claims that something is possible), and volume used as an opening
argument. `research/raw/` is exempt — those are audits by design.
