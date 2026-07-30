# Evidence

Everything here exists so a reader can check us rather than trust us.

## The adversarial reviews

A hostile reviewer — brief: *fail this work* — read the repository in five rounds.
The reviews are preserved because several findings changed the build and editorial
rules rather than merely changing prose.

| | Verdict | What it found |
|---|---|---|
| [First pass](review-2026-07-28.md) | not yet | A superseded effect size published five times, in the document that states the rule against doing exactly that |
| [Second pass](review-2-2026-07-28.md) | not yet | Corrections were being applied by *silently rewriting the ledger rows* — inside a table headed "published rather than silently edited" |
| [Third pass](review-3-2026-07-28.md) | not yet | The propagation checker built to prevent all this **did not work**; the reviewer planted the original errors back in and it reported zero violations |
| [Fourth pass](review-4-2026-07-28.md) | not yet | Broken document structure, inconsistent counts and uncaught reader-facing surfaces |
| [Fifth pass](review-5-2026-07-28.md) | not yet | Cross-references that resolved to real but wrong sections and unsupported synthesis claims |

The [`CORRECTIONS.md`](../CORRECTIONS.md) ledger records who found each issue.

## The checks, and how to run them

```bash
# no superseded value survives anywhere on a published surface
python3 evidence/check-corrections.py --self-test --strict

# public pages and every demo render without JS errors or viewport overflow
PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=/snap/bin/chromium node evidence/test-pages.mjs
PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=/snap/bin/chromium node evidence/test-demos.mjs
```

`--self-test` plants each known violation into a scratch copy and **fails if the rule
does not fire**. It exists because the first version of this checker was theatre.

## Original measurements

| File | What it measures |
|---|---|
| [`F3-grounding-ladder-harness.py`](F3-grounding-ladder-harness.py) | Dimensional / numeric / symbolic checking against seeded derivation errors |
| [`F7-A3/`](F7-A3/) | Reactive-notebook hazard classes; the `teachcheck` conformance checker |
| [`bastani-2025-correction-check.md`](bastani-2025-correction-check.md) | Verifying a claim made *to* us — and rejecting it |
| [`build-manuscript.py`](build-manuscript.py) | Renders the edited `PAPER.md` manuscript to `docs/paper.html` |
| [`build-paper.py`](build-paper.py) | Assembles `survey/` into `ATLAS.md` and `docs/atlas.html` |
