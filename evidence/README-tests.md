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
