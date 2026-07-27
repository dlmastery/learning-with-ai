# In-Browser (No-Server) Code Execution Substrates — Original Measurements

**Measurement date:** 2026-07-27 (UTC). All `gh api` calls authenticated as `dlmastery`.
**Measurement host:** Linux x86_64, 20 vCPU, Node v24.18.0, Python 3.12.3, curl 8.x, datacenter-grade network.
**Label key:**
- `MEASURED-BENCH` — I ran the command/benchmark on this host.
- `OBSERVED` — read directly off an API, registry, lockfile, or CDN header.
- `VENDOR` — a project's own written claim about itself (quoted).
- `UNVERIFIED` — could not be measured with available tools.

**Byte convention:** "wire" = bytes a browser actually transfers, measured with `-H 'Accept-Encoding: br, gzip'`. "identity" = uncompressed. MB = 1024².

---

## 1. Repo facts (all OBSERVED)

Command template:
```bash
gh api repos/<owner>/<name> --jq '[.full_name,(.license.spdx_id//"NONE"),(.stargazers_count|tostring),(.forks_count|tostring),.created_at,.pushed_at,(.open_issues_count|tostring)]|@tsv'
gh api repos/<owner>/<name>/releases/latest --jq '[.tag_name,.published_at]|@tsv'
```

| Repo | License | Stars | Forks | Created | Last push | Open issues | Latest release | Released |
|---|---|---:|---:|---|---|---:|---|---|
| pyodide/pyodide | MPL-2.0 | 14,756 | 1,038 | 2018-02-23 | 2026-07-27 | 402 | `314.0.3` | 2026-07-24 |
| jupyterlite/jupyterlite | BSD-3-Clause | 4,856 | 441 | 2021-03-27 | 2026-07-23 | 242 | `v0.8.1` | 2026-07-08 |
| jupyterlite/pyodide-kernel | BSD-3-Clause | 88 | 45 | 2022-12-01 | 2026-07-25 | 63 | `v0.8.2` | 2026-07-15 |
| jupyterlite/xeus | BSD-3-Clause | 46 | 21 | 2021-10-11 | 2026-06-25 | 38 | `v5.0.0` | 2026-06-25 |
| marimo-team/marimo | Apache-2.0 | 22,073 | 1,198 | 2023-08-14 | 2026-07-27 | 604 | `0.23.15` | 2026-07-23 |
| r-wasm/quarto-live | MIT | 259 | 38 | 2024-06-18 | 2026-06-08 | 74 | `v0.2.0` | 2026-05-22 |
| r-wasm/webr | NOASSERTION (`gh api repos/r-wasm/webr/license` → "Other") | 1,085 | 96 | 2022-01-19 | 2026-06-23 | 90 | `v0.6.0` | 2026-05-19 |
| observablehq/framework | ISC | 3,558 | 199 | 2023-09-27 | 2026-05-15 | 181 | `v1.13.4` | 2026-03-02 |
| observablehq/runtime | ISC | 1,080 | 85 | 2017-05-02 | 2026-07-04 | 6 | `v6.0.0` | **2024-11-06** |
| whitphx/stlite | Apache-2.0 | 1,652 | 87 | 2022-05-14 | 2026-07-25 | 97 | `@stlite/browser@1.8.1` | 2026-06-19 |
| pyscript/pyscript | Apache-2.0 | 18,690 | 1,476 | 2022-02-21 | 2026-07-13 | 20 | `2026.7.2` | 2026-07-09 |
| jupyter-book/thebe | BSD-3-Clause | 442 | 68 | 2017-03-14 | 2026-06-23 | 116 | `thebe-lite@0.4.10` | **2024-09-06** |
| jupyterhub/binderhub | BSD-3-Clause | 2,670 | 409 | 2017-04-26 | 2026-07-25 | 266 | *(no GitHub release; 404)* | — |
| r-wasm/quarto-drop | MIT | 190 | — | — | **2025-09-26** | — | — | — |

Staleness signals worth noting: `observablehq/runtime` last released 2024-11-06 (~20 months); `thebe` last release 2024-09-06 (~23 months); `quarto-drop` last pushed 2025-09-26 (~10 months); `observablehq/framework` last release 2026-03-02.

PyPI (OBSERVED, `curl -s https://pypi.org/pypi/<pkg>/json`):

| PyPI package | Version | Wheel size |
|---|---|---:|
| jupyterlite-core | 0.8.1 | 15.15 MB |
| jupyterlite-pyodide-kernel | 0.8.2 | 0.31 MB |
| jupyterlite-xeus | 5.0.0 | 5.91 MB |
| marimo | 0.23.15 | 37.38 MB |
| thebe (py) | 0.0.4.6 | 9.91 MB |

npm (OBSERVED, `curl -s https://registry.npmjs.org/<pkg>` → `dist.unpackedSize`):

| npm package | Latest | Unpacked | License |
|---|---|---:|---|
| pyodide | 314.0.3 | 13.87 MB (jsDelivr flat listing) | MPL-2.0 |
| webr | 0.6.0 | 46.4 MB | — |
| @stlite/browser | 1.8.1 | 87.3 MB | Apache-2.0 |
| @marimo-team/islands | 0.23.15 | 37.6 MB | Apache-2.0 |
| thebe | 0.9.3 | 14.05 MB | BSD-3-Clause |
| thebe-lite | 0.5.0 | 3.99 MB | MIT |
| @pyscript/core | 0.7.31 | 5.16 MB | Apache-2.0 |
| @observablehq/framework | 1.13.4 | 0.43 MB | ISC |
| **@observablehq/runtime** | **6.0.0** | **0.039 MB (39 KB)** | ISC |

---

## 2. Real download weight — the cold-start byte budget

### 2.1 Pyodide 314.0.3 core (MEASURED-BENCH)

```bash
for f in pyodide.mjs pyodide.asm.wasm python_stdlib.zip pyodide-lock.json; do
  curl -s -o /dev/null -H 'Accept-Encoding: br, gzip' \
    -w "$f %{http_code} %{size_download}\n" \
    "https://cdn.jsdelivr.net/pyodide/v314.0.3/full/$f"
done
# and again with -H 'Accept-Encoding: identity'
```

| File | Wire (br) | Identity | Ratio |
|---|---:|---:|---:|
| `pyodide.mjs` | 7,285 B | 17,880 B | 0.41 |
| `pyodide.asm.wasm` | **3,435,323 B (3.28 MB)** | 9,596,462 B (9.15 MB) | 0.36 |
| `python_stdlib.zip` | 2,504,844 B (2.39 MB) | 2,545,106 B | 0.98 |
| `pyodide-lock.json` | 24,468 B | 113,804 B | 0.22 |
| **CORE TOTAL** | **5,971,920 B = 5.70 MB** | 12,273,252 B = 11.70 MB | |

`curl -sI -H 'Accept-Encoding: br, gzip' .../pyodide.asm.wasm` → `content-encoding: br`, `content-length: 3435323`, `vary: Accept-Encoding`. Brotli is real, not an artifact.

**`pyodide.js` (UMD) exists (7,607 B wire); `pyodide.asm.js` returns 404 in 314.0.3 — it is now `pyodide.asm.mjs` (1,249,447 B identity, OBSERVED from jsDelivr npm listing).**

Pyodide distribution `info` block (OBSERVED, from `pyodide-lock.json`):
```json
{"abi_version":"2026_0","arch":"wasm32","platform":"emscripten_5_0_3","python":"3.14.0"}
```

### 2.2 Pyodide package sizes (MEASURED-BENCH)

All 354 lock entries HEAD-measured:
```bash
curl -s -o pyodide-lock.json https://cdn.jsdelivr.net/pyodide/v314.0.3/full/pyodide-lock.json
python3 -c "import json;[print(p['file_name']) for p in json.load(open('pyodide-lock.json'))['packages'].values()]" | sort -u > files.txt
cat > getsize.sh <<'EOF'
#!/bin/bash
n=$(curl -s -o /dev/null -H 'Accept-Encoding: identity' -w '%{size_download}' "https://cdn.jsdelivr.net/pyodide/v314.0.3/full/$1")
printf '%s\t%s\n' "$1" "$n"
EOF
chmod +x getsize.sh; xargs -P 20 -n1 ./getsize.sh < files.txt > sizes.tsv
```

**Distribution inventory (OBSERVED, parsed from lock):**

| Metric | Value |
|---|---:|
| Lock entries total | 354 |
| Real packages (non-`*-tests`) | **293** |
| Test-only entries (`*-tests`) | 61 |
| `package_type: shared_library` | 9 (`libcrc32c, libgdal, libgeos, libhdf5, libheif, libopenblas, libproj, libsuitesparse, libtaglib`) |
| Packages flagged `unvendored_tests: true` | 60 |
| **All 354 files, identity bytes** | **468,070,864 B = 446.4 MB** |
| …of which `*-tests.tar` | 94,963,251 B = 90.6 MB |
| …real package payload | 373,107,613 B = 355.8 MB |

**Per-package: wheel size vs. full dependency closure (MEASURED-BENCH, identity bytes):**

| Package | Version | Wheel MB | Closure pkgs | Closure MB |
|---|---|---:|---:|---:|
| numpy | 2.4.3 | 2.78 | 1 | 2.78 |
| pandas | 3.0.2 | 3.99 | 5 | 7.49 |
| matplotlib | 3.10.8 | 6.65 | 12 | 12.60 |
| sympy | 1.14.0 | 3.99 | 2 | 4.40 |
| scipy | 1.18.0 | **13.36** | 2 | 16.14 |
| scikit-learn | 1.8.0 | 4.22 | 5 | **20.56** |
| statsmodels | 0.14.6 | 7.74 | 9 | **28.80** |
| networkx | 3.6.1 | 1.03 | 15 | 14.36 |
| pillow | 12.2.0 | 0.99 | 1 | 0.99 |
| requests | 2.33.1 | 0.06 | 5 | 0.44 |
| altair | 6.0.0 | 0.76 | 12 | 1.77 † |
| micropip | 0.11.1 | 0.11 | 1 | 0.11 |
| bokeh | 3.9.0 | 6.10 | 13 | 15.06 |
| polars | 1.33.1 | 17.47 | 1 | 17.47 |
| duckdb | 1.5.1 | 8.31 | 1 | 8.31 |
| pyarrow | 22.0.0 | 9.55 | 7 | 17.04 |
| xarray | 2026.2.0 | 0.80 | 7 | 8.38 |
| sqlalchemy | 2.0.48 | 1.89 | 2 | 1.93 |
| opencv-python | 4.11.0.86 | 10.18 | 2 | 12.96 |
| geopandas | 1.1.3 | 0.17 | 16 | **23.89** |

† altair's closure resolution logged one unresolvable dep name (`jsonschema_specifications` vs. lock key `jsonschema-specifications`); the altair closure MB is therefore a slight undercount.

**15 largest files in the distribution (identity MB):** python-flint 69.49, polars 17.47, phispy 17.14, pymupdf 16.66, pandas-tests 14.52, rasterio 13.63, scipy 13.36, scipy-tests 10.79, cartopy-tests 10.65, fiona 10.59, sympy-tests 10.50, opencv-python 10.18, pyarrow 9.55, scikit-image 8.98, duckdb 8.31.

### 2.3 Teaching-stack cold-start budgets (MEASURED-BENCH)

Dependency closures resolved from `pyodide-lock.json` `depends` graph; per-file byte counts measured over HTTP.

| Stack | Packages | Identity MB | **Wire (br/gzip) MB** | **+ core = total wire MB** |
|---|---:|---:|---:|---:|
| Core only (no packages) | — | 11.70 | 5.70 | **5.70** |
| **Teaching: numpy+matplotlib+pandas** | 13 | 16.59 | **16.19** | **21.89** |
| **Math: numpy+sympy+matplotlib** | 14 | 17.00 | ~16.6 (est. from ratio) | ~22.3 |
| ML: numpy+pandas+matplotlib+sklearn | 17 | 34.36 | — | ~40 |
| Kitchen sink (adds scipy, sympy, networkx, statsmodels) | 24 | 48.39 | — | ~54 |

Teaching-stack per-file wire bytes (`Accept-Encoding: br, gzip`), summing to **16,972,700 B = 16.19 MB**:

| Wheel | Wire B |
|---|---:|
| matplotlib-3.10.8 | 6,866,830 |
| pandas-3.0.2 | 4,155,168 |
| numpy-2.4.3 | 2,884,968 |
| fonttools-4.62.1 | 1,121,104 |
| pillow-12.2.0 | 1,029,417 |
| pytz-2026.1.post1 | 302,109 |
| python_dateutil-2.9.0.post0 | 228,004 |
| pyparsing-3.3.2 | 121,001 |
| contourpy-1.3.3 | 115,821 |
| packaging-26.1 | 93,972 |
| kiwisolver-1.5.0 | 35,857 |
| six-1.17.0 | 10,641 |
| cycler-0.12.1 | 7,808 |

Wheels are already ZIP-compressed; brotli buys only ~1% on them. **The 5.70 MB core is the only part that compresses.**

**Derived transfer times (DERIVED from MEASURED bytes, not measured on a throttled link):** at 21.89 MB the teaching stack is ~2.9 s on 60 Mbps, ~17.5 s on 10 Mbps, ~70 s on 2.5 Mbps. On repeat visits the browser HTTP cache serves all of it.

### 2.4 WebR 0.6.0 (MEASURED-BENCH)

Two different builds ship under the same version. `webr.r-wasm.org` serves a smaller build than the npm tarball:

```bash
for f in R.wasm R.js webr.mjs webr-worker.js libRlapack.so libRblas.so; do
  curl -s -o /dev/null -H 'Accept-Encoding: identity' -w "$f %{http_code} %{size_download}\n" \
    "https://webr.r-wasm.org/v0.6.0/$f"; done
```

| File | webr.r-wasm.org/v0.6.0 identity | wire (br/gzip) | npm `webr@0.6.0` identity |
|---|---:|---:|---:|
| `R.wasm` | **12,328,048 B (11.76 MB)** | 12,328,048 (no further compression) | 18,062,845 B (17.23 MB) |
| `R.js` | 785,875 B | 131,542 B | 785,875 B |
| `webr.mjs` | 66,672 B | 18,455 B | 66,586 B |
| `webr-worker.js` | 134,029 B | — | 134,029 B |
| `libRlapack.so` | 1,769,888 B | — | 1,769,888 B |
| `libRblas.so` | 198,205 B | — | 198,205 B |
| **Base engine total (r-wasm host, identity)** | **≈15.28 MB** | | |

`https://webr.r-wasm.org/latest/` also still serves a stale `R.bin.wasm` (5,900,311 B, `last-modified: Fri, 25 Oct 2024`) alongside the current `R.wasm` (12,325,655 B, `last-modified: Tue, 23 Jun 2026`). Do not cite `R.bin.wasm` as current.

npm dist split (OBSERVED, `https://data.jsdelivr.com/v1/packages/npm/webr@0.6.0?structure=flat`):

| Category | Files | MB |
|---|---:|---:|
| Core (non-`/dist/vfs`, non-`.map`) | 59 | 20.29 |
| **VFS images (`/dist/vfs/**`, lazily mounted)** | **109** | **25.47** |
| Total package | 170 | 46.37 |

Largest VFS images: `usr/lib/R/doc.data.gz` 4.00 MB, `library/translations.data.gz` 3.06 MB, `library/base/help.data.gz` 2.63 MB, `library/stats/help.data.gz` 1.84 MB, `usr/share/proj.data.gz` 1.71 MB, `grDevices/libs.data.gz` 1.64 MB, 6 Noto TTF fonts ≈ 0.4–0.5 MB each. Help/doc/translations dominate — ~13 MB of the VFS is documentation.

**WebR CRAN-for-WASM repository (MEASURED-BENCH):**
```bash
curl -s https://repo.r-wasm.org/bin/emscripten/contrib/4.4/PACKAGES -H 'Accept-Encoding: identity' -o webrPACKAGES
grep -c '^Package:' webrPACKAGES
```

| R version index | PACKAGES file size | Packages |
|---|---:|---:|
| 4.3 | 4,441,491 B | — |
| **4.4** | 4,789,119 B | **21,623** |
| 4.5 | 5,336,284 B | — |
| 4.6 | 6,977,627 B | — |

**21,623 R packages** are pre-built for wasm32/emscripten at R 4.4 — an order of magnitude more than Pyodide's 293. ggplot2 3.5.2, dplyr 1.1.4, tidyverse 2.0.0, data.table 1.17.0, shiny 1.9.1.8002, knitr 1.50, tidyr, readr, plotly 4.10.4, stringr, lme4, caret, Matrix, rmarkdown, sf, torch 0.14.2, keras 2.15.0 are all PRESENT.

Sample R package tarball sizes (MEASURED-BENCH, identity, `repo.r-wasm.org/bin/emscripten/contrib/4.4/<pkg>.tgz`):

| Package | Bytes | MB |
|---|---:|---:|
| ggplot2_3.5.2 | 4,188,673 | 3.99 |
| Matrix_1.7-3 | 2,858,416 | 2.73 |
| plotly_4.10.4 | 2,868,133 | 2.74 |
| data.table_1.17.0 | 2,168,239 | 2.07 |
| rlang_1.1.6 | 1,087,378 | 1.04 |
| dplyr_1.1.4 | 1,063,948 | 1.01 |
| tidyr_1.3.1 | 1,024,239 | 0.98 |
| knitr_1.50 | 801,011 | 0.76 |

### 2.5 Every substrate side by side — cold-start byte budget

| Substrate | Engine bytes to first "hello world" | Notes |
|---|---:|---|
| **Observable runtime 6.0.0** | **~27 KB JS** (whole npm package 39 KB) | JS dataflow only; no Python/R VM |
| **PyScript + MicroPython** | `core.js` 214 B (br) → `core-*.js` 48,133 B (br) + micropython.mjs 108,321 B + micropython.wasm 446,411 B ≈ **0.57 MB** | MicroPython 1.28.0-6, no numpy |
| **PyScript + Pyodide** | ≈48 KB core + Pyodide core 5.70 MB = **5.75 MB** | pins Pyodide `314.0.2` |
| **Pyodide raw** | **5.70 MB** wire | |
| **quarto-live 0.2.0 runtime shim** | `live-runtime.js` 647,245 B + `live-runtime.css` 18,391 B + `pyodide-worker.js` 23,344 B = **0.66 MB** | plus webR 15.3 MB and/or Pyodide 5.70 MB |
| **stlite 1.8.1** | `stlite.js` 3,067 B (br) + `stlite.css` 10,880 B (br) + `index-*.js` 4.16 MB + streamlit wheel 1.64 MB + stlite_lib 0.02 MB + Pyodide 5.70 MB ≈ **11.5 MB** minimum | 30.42 MB of non-map assets total, lazily chunked (PlotlyChart chunk alone 6.60 MB) |
| **marimo 0.23.15 WASM export** | **5.48 MB raw / 2.27 MB gzip** of preloaded JS/CSS + Pyodide core 5.70 MB = **≈8.0 MB** | MEASURED-BENCH, see §5 |
| **JupyterLite 0.8.1** | full static app 18.43 MB non-map (5.60 MB gzip upper bound) + Pyodide 5.70 MB | MEASURED-BENCH, see §7 |
| **WebR 0.6.0** | **≈15.28 MB** engine (R.wasm 11.76 MB) + lazily-mounted VFS | |
| **Thebe 0.9.3 (server-backed)** | `lib/index.js` 1,495,556 B (1.43 MB identity) + chunks | plus a live Jupyter server |
| **thebe-lite 0.5.0** | `thebe-lite.min.js` 0.50 MB + chunks | side-loads JupyterLite + Pyodide |

---

## 3. Package availability — the absences are the finding

### 3.1 Pyodide 314.0.3 distribution (OBSERVED, parsed from `pyodide-lock.json`)

| Package | In Pyodide distribution? | Version | Pure-Python wheel on PyPI (micropip fallback)? |
|---|---|---|---|
| numpy | ✅ PRESENT | 2.4.3 | — |
| scipy | ✅ PRESENT | 1.18.0 | — |
| pandas | ✅ PRESENT | 3.0.2 | — |
| matplotlib | ✅ PRESENT | 3.10.8 | — |
| sympy | ✅ PRESENT | 1.14.0 | — |
| scikit-learn | ✅ PRESENT | 1.8.0 | — |
| networkx | ✅ PRESENT | 3.6.1 | — |
| statsmodels | ✅ PRESENT | 0.14.6 | — |
| requests | ✅ PRESENT | 2.33.1 | — |
| altair | ✅ PRESENT | 6.0.0 | — |
| pillow | ✅ PRESENT | 12.2.0 | — |
| micropip | ✅ PRESENT | 0.11.1 | — |
| polars / duckdb / pyarrow / xarray / bokeh / sqlalchemy / opencv-python / nltk / geopandas | ✅ PRESENT | — | — |
| **plotly** | ❌ **ABSENT** | — | ✅ YES — `plotly-6.9.0-py3-none-any.whl`, **9.45 MB** |
| **ipywidgets** | ❌ **ABSENT** | — | ✅ YES — `ipywidgets 8.1.8`, 0.13 MB |
| **anywidget** | ❌ **ABSENT** | — | ✅ YES — `anywidget 0.11.0`, 0.30 MB |
| **seaborn** | ❌ **ABSENT** | — | ✅ YES — `seaborn 0.13.2`, 0.28 MB |
| **torch** | ❌ **ABSENT** | — | ❌ NO pure-Python wheel (2.13.0) |
| **tensorflow** | ❌ **ABSENT** | — | ❌ NO pure-Python wheel (2.21.0) |
| **jax** | ❌ **ABSENT** | — | ⚠️ `jax 0.11.0` has a pure-py wheel (3.10 MB) but requires native `jaxlib` — **not usable** |
| **`sqlite3` as a distribution package** | ❌ ABSENT as a lock entry | — | `sqlite3` is in the CPython stdlib and ships inside `python_stdlib.zip`; the lock ships `apsw 3.51.3.0` and `sqlalchemy 2.0.48` instead |

**Net:** for a teaching stack, the deal-breakers are **plotly, seaborn, ipywidgets, anywidget** — all four are `micropip`-installable pure-Python wheels, but plotly alone adds 9.45 MB and ipywidgets additionally needs a front-end widget manager the host page must supply. **torch / tensorflow / jax are hard NOs.**

### 3.2 What Pyodide says about C extensions and micropip (VENDOR, verbatim)

`docs/usage/loading-packages.md` @ tag `314.0.3`:
> "Only the Python standard library is available after importing Pyodide."
> "`micropip.install` (Python) for pure Python packages with wheels as well as Pyodide packages (including Emscripten/wasm32 binary wheels). It can install packages from PyPI, the JsDelivr CDN or from other URLs."
> "At present, `loadPackagesFromImports` will not download packages from PyPI, it will only download packages included in the Pyodide distribution."

`docs/usage/faq.md` @ tag `314.0.3`, § "Why can't Micropip find a 'pure Python wheel' for a package?":
> "either the package is pure Python … and its maintainers didn't upload a wheel."
> "or the package has binary extensions (e.g. C, Fortran or Rust), in which case it needs to be cross-compiled for Pyodide. Please make a request to the package maintainers to add Pyodide support."

### 3.3 xeus-python / emscripten-forge alternative (OBSERVED)

```bash
python3 -c "import urllib.request;open('ef.json','wb').write(urllib.request.urlopen(urllib.request.Request('https://repo.prefix.dev/emscripten-forge-dev/emscripten-wasm32/repodata.json',headers={'Accept-Encoding':'identity','User-Agent':'curl/8'})).read())"
```

| Channel/subdir | Distinct packages |
|---|---:|
| `emscripten-forge-dev/emscripten-wasm32` | 340 |
| `emscripten-forge-dev/noarch` | 17 |
| **Combined distinct** | **351** |

PRESENT: numpy, scipy, pandas, matplotlib, sympy, scikit-learn, statsmodels, pyarrow, sqlite, ipython, xeus-python.
**ABSENT: networkx, ipywidgets, anywidget, plotly, altair, seaborn, requests, bqplot, ipyleaflet, ipycanvas, polars, pytorch.**
So xeus-python is *not* a superset of Pyodide — it trades `networkx`/`requests`/`altair` away. (Caveat: only the `-dev` channel was enumerated; a stable channel may differ — treat non-`-dev` coverage as UNVERIFIED.)

---

## 4. Documented limits (Pyodide)

### 4.1 Performance multiplier — the verbatim number

**Source:** `gh api "repos/pyodide/pyodide/contents/docs/project/roadmap.md?ref=314.0.3" --jq .content | base64 -d`
Rendered at <https://pyodide.org/en/stable/project/roadmap.html>

> **"Across [benchmarks](https://github.com/pyodide/pyodide/tree/main/benchmark) Pyodide is currently around 3x to 5x slower than native Python."**
>
> "At the same time, C code compiled to WebAssembly typically runs between near native speed and 2x to 2.5x times slower (Jangda et al. 2019)."

(VENDOR. Note `pyodide.org` returns **HTTP 403 to WebFetch and HTTP 429 to plain curl** — the docs source had to be read from the git tag. The FAQ page no longer contains a slowdown figure; the roadmap does.)

### 4.2 WASM memory ceiling (OBSERVED, from build flags)

`gh api "repos/pyodide/pyodide/contents/Makefile.envs?ref=314.0.3"` — lines 167–172 and 297–300:
```
-s INITIAL_MEMORY=31457280      # 30 MB
-s ALLOW_MEMORY_GROWTH=1
-s MAXIMUM_MEMORY=4GB
-s STACK_SIZE=10MB
```
Hard ceiling is **4 GB** (the wasm32 address-space limit); heap starts at 30 MB and grows. Real browsers cap lower than 4 GB in practice — that per-browser cap is **UNVERIFIED** here.

### 4.3 Threading / processes / sockets (VENDOR, verbatim)

`docs/usage/wasm-constraints.md` @ `314.0.3`:
> "The following modules can be imported, but are not functional due to the limitations of the WebAssembly VM:
> - multiprocessing
> - threading
> - sockets
> as well as any functionality that requires these."

> "Because Pyodide does not support threading or multiprocessing, packages that use threading or multiprocessing will not work without a patch to disable it."

`docs/usage/faq.md` @ `314.0.3`, § "Can I use threading/multiprocessing/subprocess?":
> "No, fork and pthreads do not work in Pyodide. Attempts to use `threading`, `multiprocessing`, or `subprocess` will raise a `RuntimeError`."

### 4.4 Removed stdlib modules (VENDOR, verbatim list)

> "The following modules are removed from the standard library to reduce download size and since they currently wouldn't work in the WebAssembly VM,
> curses, dbm, ensurepip, fcntl, grp, idlelib, lib2to3, msvcrt, pwd, resource, syslog, termios, tkinter, turtle.py, turtledemo, venv, winreg, winsound"

Plus: `pty` and `tty` are "present but cannot be imported due to a dependency on the termios package which has been removed."

### 4.5 Limited-functionality modules (VENDOR, verbatim)

> "decimal: The decimal module has C (_decimal) and Python (_pydecimal) implementations with the same functionality. The Python implementation is not available."
> "pydoc: Help messages for Python builtins are not available by default in order to reduce the initial download size. You need to call `pyodide.loadPackage('pydoc_data')`…"
> "webbrowser: The original webbrowser module is not available. Instead, Pyodide includes some method stubs based on browser APIs."
> "zoneinfo: The zoneinfo package will only work if you install the timezone data using the tzdata package."
> "hashlib: Hash algorithms that are depending on OpenSSL are not available."
> "**ssl: SSL module is replaced with a stub implementation that does not use OpenSSL. All the methods that depend on OpenSSL will not work as expected or will raise `NotImplementedError`.**"

### 4.6 Networking (VENDOR, verbatim)

> "Packages for `urllib3` and `requests` are included in pyodide. In browser, these function _roughly_ the same as on other operating systems with some limitations."
> "The first limitation is that streaming download of files only works in very specific circumstances, which are that pyodide has to be running in a web-worker, and it has to be on a cross-origin isolated website."
> "**Secondly, all network calls are done via the browser.** This means you are subject to the same limitations as any JavaScript network call. This means you have very little or no control over certificates, timeouts, proxies and other network related settings. You also are constrained by browser policies relating to cross-origin requests, sometimes things will be blocked by CORS policies if the server doesn't serve them with the correct headers."

**Filesystem:** Emscripten MEMFS/IDBFS in-memory; the `docs/usage/file-system.md` and `accessing-files.md` pages exist but were not quoted here — **filesystem specifics: UNVERIFIED**.

---

## 5. marimo WASM

**`marimo export html-wasm` exists in current docs and current CLI.** MEASURED-BENCH:
```bash
python3 -m venv mv && ./mv/bin/pip install marimo==0.23.15
./mv/bin/marimo export html-wasm nb.py -o wasmout --mode run
./mv/bin/marimo export html-wasm nb.py -o wasmedit --mode edit
```

| Metric | `--mode run` | `--mode edit` |
|---|---:|---:|
| Output dir size | 27 MB | 27 MB |
| Files emitted | 705 | 705 |
| Non-`.map` bytes | 25.08 MB | 25.08 MB |
| `index.html` | 21.7 KB | 21.7 KB |
| `<link rel="modulepreload">` tags | 179 | 179 |
| **Assets referenced by `index.html` (upfront fetch)** | **192 files, 5.48 MB raw / 2.27 MB gzip** | same |
| Byte-level diff run vs. edit | *(empty — identical file inventory)* | |

Both modes ship the identical asset tree; `--mode` only sets a runtime flag. Largest assets: `Plot-*.js` 4.60 MB, `loro_wasm_bg-*.wasm` 3.11 MB (CRDT), `node-sql-parser-*.js` 2.48 MB.

**Pyodide is NOT bundled.** `find wasmout -name '*.wasm'` returns only `loro_wasm_bg-*.wasm`. The worker chunk contains (MEASURED-BENCH, grep of `wasmout/assets/worker-BQo2bijx.js`):
```js
var Ho=`314.0.0`; … e.cdnUrl=X(e.packageBaseUrl??`https://cdn.jsdelivr.net/pyodide/v${Uo}/full/`)
```
So marimo 0.23.15 fetches **Pyodide 314.0.0** from jsDelivr at runtime. Its core weight (MEASURED-BENCH): `pyodide.asm.wasm` 3,445,966 B br / 9,610,179 B identity; `python_stdlib.zip` 2,511,627 B br; `pyodide-lock.json` 24,870 B br.

**Total marimo WASM cold start ≈ 2.27 MB (gzip app shell) + 5.71 MB (Pyodide core) ≈ 8.0 MB**, before any package wheels.

CLI options (VENDOR, `docs/guides/exporting/webassembly_html.md` @ `0.23.15`): `--mode {run|edit}`, `--output`, `--show-code/--no-show-code`, `--watch/--no-watch`, `--include-cloudflare`.

> "The exported file **must be served over HTTP** to function correctly - it cannot be opened directly from the filesystem (`file://`). Your server must also serve the assets in the `assets` directory, next to the HTML file."

**marimo's own stated limitations (VENDOR, verbatim, `docs/guides/wasm.md` @ `0.23.15`):**

> "**Packages.** Many but not all packages are supported. All packages with pure Python wheels on PyPI are supported, as well as additional packages like NumPy, SciPy, scikit-learn, duckdb, polars, and more."

> "**PDB.** PDB is not currently supported."

> "**Concurrency.** WASM notebooks support cooperative adapters for `threading.Thread`, `threading.Event`, `threading.local`, `concurrent.futures.ThreadPoolExecutor`, `wait`, `as_completed`, and process-shaped `multiprocessing.Process`, `Queue`, `SimpleQueue`, `Pool`, and `ProcessPoolExecutor`. … **They do not create OS threads, shared-memory processes, or true CPU parallelism.** Blocking waits are bridged through Pyodide's JSPI-backed asyncio loop."
> "Native synchronization and process APIs such as `threading.Lock`, `Condition`, `Semaphore`, `Barrier`, `Timer`, `multiprocessing.Pipe`, managers, shared memory, and non-`spawn` start methods are unsupported. For CPU-bound parallelism or process isolation, use a regular marimo notebook."

> "**Memory.** WASM notebooks have a memory limit of 2GB; this may be increased in the future."

> "WASM notebooks are supported in the latest versions of Chrome, Firefox, Edge, and Safari. **Chrome is the recommended browser** for WASM notebooks as it seems to have the best performance and compatibility."

Also documented: PEP 508 environment markers with `sys_platform != 'emscripten'` to exclude native-only deps from WASM installs; `sys.platform == "emscripten"` for runtime detection; `mo.notebook_location()` + a `public/` folder for bundling data; local modules auto-wheeled into `public/wheels` (requires `uv`).

`@marimo-team/islands@0.23.15` (embed-in-any-HTML path): 37.6 MB unpacked npm, `dist/main.js` 1.32 MB, `dist/Plot-*.js` 8.00 MB. Docs mark islands as **"an early feature"** / **"Preview"**.

---

## 6. Quarto Live (r-wasm/quarto-live)

**What it is (VENDOR, README @ `v0.2.0`):**
> "This extension embeds WebAssembly powered code blocks and exercises for both the R and Python languages into Quarto documents using HTML-based output formats. The webR and Pyodide WebAssembly engines are used to dynamically execute code in the user's web browser, so **only a static web service … is required**."

Feature list (VENDOR): interactive R and Python code blocks; exercises with hints, solutions, custom grading; client-side plots/images/HTML widgets; CodeMirror editor with theming, autocomplete, code persistence, autorun; integration with Quarto's OJS engine so `{webr}`/`{pyodide}` cells update reactively with `{ojs}` cells.

| Fact | Value | Label |
|---|---|---|
| License | MIT | OBSERVED |
| Stars / forks / open issues | 259 / 38 / 74 | OBSERVED |
| Latest release | `v0.2.0`, 2026-05-22 | OBSERVED |
| Last push | 2026-06-08 | OBSERVED |
| Install | `quarto add r-wasm/quarto-live` | VENDOR |
| Formats | `format: live-html`, `format: live-revealjs` | VENDOR |
| Cell types | `{webr}` (R), `{pyodide}` (Python) | VENDOR |
| Pinned engines | **webR `^0.6.0`, Pyodide `^0.28.1`** (`live-runtime/package.json` devDeps) | OBSERVED |
| `live-runtime/package.json` version | `0.1.4-dev` (lags the `v0.2.0` tag) | OBSERVED |

**Shipped runtime bytes (OBSERVED, `gh api .../contents/_extensions/live/resources`; MEASURED-BENCH via jsDelivr gh CDN):**

| File | Bytes |
|---|---:|
| `live-runtime.js` | 647,245 (verified 647,245 over `cdn.jsdelivr.net/gh/r-wasm/quarto-live@v0.2.0/...`) |
| `live-runtime.css` | 18,391 |
| `pyodide-worker.js` | 23,344 |
| `live.lua` (Pandoc filter) | 19,612 |
| `tinyyaml.lua` | 22,978 |

**Documented limits / requirements (VENDOR):**
- Knitr engine requires an explicit include: `{{< include ./_extensions/r-wasm/live/_knitr.qmd >}}` — "a temporary requirement for the `knitr` engine and will be removed in a future release."
- Package loading: "outside of its dependencies, quarto-live avoids automatically downloading additional packages." Packages must be declared under `webr: packages:` / `pyodide: packages:` in YAML or installed interactively.
- Custom R packages: must be compiled with `{rwasm}` and hosted in a CRAN-like repo (R-universe suggested), listed under `webr: repos:`.
- Custom Python packages: "If a package is not found in the Pyodide repository it will be loaded from PyPI. The `micropip` package can load PyPI packages for Pyodide **if they are built as pure Python wheels**. Python packages containing compiled code should be built as a `wasm32/emscripten` WebAssembly wheel."
- Filesystem: "there is a Virtual Filesystem (VFS) made available that contains **only the minimum required** to run R or Python code." Local files must be listed under `resources:` and are downloaded into the VFS at startup, landing in `/home/web_user`.
- Version history (NEWS.md): 0.2.0 = webR → v0.6.0; 0.1.3 = webR → v0.5.8, Pyodide → v0.28.1.

**quarto-drop** (`r-wasm/quarto-drop`): MIT, 190 stars, **last pushed 2025-09-26** — ~10 months stale. **`quarto-wasm` as a distinct repo: not found (UNVERIFIED / likely does not exist).** The `coatless-quarto/pyodide` extension exists (108 stars, no license file, last push 2025-01-31 — stale); `coatless-quarto/webr` returns 404.

---

## 7. JupyterLite

| Fact | Value |
|---|---|
| jupyterlite/jupyterlite | BSD-3-Clause, 4,856★, `v0.8.1` (2026-07-08) |
| jupyterlite/pyodide-kernel | BSD-3-Clause, 88★, `v0.8.2` (2026-07-15) |
| jupyterlite/xeus | BSD-3-Clause, 46★, `v5.0.0` (2026-06-25) |

**Kernels (VENDOR, README @ `v0.8.1`):**
> "Python kernels running in a Web Worker:
> - Pyodide: jupyterlite-pyodide-kernel
> - Xeus Python: jupyterlite-xeus"

Other kernels in the org (OBSERVED, `gh api orgs/jupyterlite/repos`): `xeus-lua-kernel` (14★), `xeus-wren-kernel` (3★), `xeus-sqlite-kernel` (35★), `xeus-nelson-kernel` (2★), `xeus-lfortran-kernel` (1★), `javascript-kernel` (14★), `p5-kernel` (23★), `echo-kernel` (13★), plus `cockle` (in-browser bash-like shell, 21★) and `terminal` (29★).

**Static app weight (MEASURED-BENCH):**
```bash
pip download jupyterlite-core==0.8.1 --no-deps -d .
python3 -c "import zipfile;z=zipfile.ZipFile('jupyterlite_core-0.8.1-py3-none-any.whl');open('app.tgz','wb').write(z.read('jupyterlite_core/jupyterlite-app-0.8.1.tgz'))"
tar xzf app.tgz -C app
find app/package/build -type f ! -name '*.map' -printf '%s\n' | awk '{s+=$1}END{print s}'
```

| Metric | Value |
|---|---:|
| Wheel size on PyPI | 15,884,058 B (15.15 MB) |
| Wheel content that is the app | `jupyterlite-app-0.8.1.tgz`, 15.09 MB of the 15.26 MB wheel |
| Extracted app tree | 69 MB |
| `build/` non-`.map` files | **428 files, 18.43 MB uncompressed** |
| `build/` source maps | 275 files, 47.64 MB |
| gzip -9 of all non-map build assets (concatenated → upper bound on wire) | **5.60 MB** |
| Largest single asset | `jlab_core.*.js` 2.86 MB (its map is 9.25 MB) |
| `lab/index.html` entry | one script: `../build/lab/bundle.js` |

A JupyterLite Pyodide notebook therefore costs **~5.6 MB (app shell, gzip upper bound) + 5.70 MB (Pyodide core) ≈ 11.3 MB before any package**, plus the JupyterLab app's lazy chunks.

**Version compatibility table (VENDOR, README):** jupyterlite-core 0.7.0 ↔ jupyterlab 4.5.0 / notebook 7.5.0; 0.6.0 ↔ 4.4.3 / 7.4.3; earlier ❌. "**Only the last two releases are actively supported.**"

**Documented limits (VENDOR, `docs/troubleshooting.md` @ `v0.8.1`):**
> "JupyterLite runs Python kernels in the browser using WebAssembly, which is different from a regular JupyterLab setup that runs on the server. **This means that not all Python packages that work in a standard Python environment will work in JupyterLite.**"

> "When using WebAssembly-based kernels, you may encounter limitations with packages that:
> - Require native C extensions that are not compiled for WebAssembly
> - Depend on system libraries not available in the browser environment
> - Use threading or multiprocessing features not supported in WebAssembly
> - Access the file system in ways not compatible with the browser sandbox"

> "JupyterLite uses a **Service Worker** to allow accessing files from a kernel. But in some cases the Service Worker may fail to register… Use a different browser. Currently we support the latest Chrome and Firefox versions. However **it is known that Service Workers are not supported in Firefox private windows.**"

> "By default JupyterLite stores the contents of the file browser and user settings in the browser's **local storage**." (README says "browser's `IndexDB` (or `localStorage`)".) `Help > Clear Browser Data` "will permanently remove data stored in your browser. This operation cannot be undone."

Known race: `FileNotFoundError: [Errno 44] No such file or directory` "seems to happen when code is executed before a kernel is fully ready. See issue #1371."

Package installation is via `%pip install` (piplite/micropip) for Pyodide and `%mamba install` / `%pip install` for xeus-python.

README (VENDOR) claims support for "interactive visualization libraries such as `altair`, `bqplot`, `ipywidgets`, `matplotlib`, and `plotly`" — note that `ipywidgets`, `plotly`, and `bqplot` are **not** in the Pyodide distribution (§3.1) and must be micropip-installed at runtime.

---

## 8. Observable

| Repo | License | Stars | Latest release | Released | Unpacked npm |
|---|---|---:|---|---|---:|
| observablehq/framework | ISC | 3,558 | `v1.13.4` | 2026-03-02 | 0.43 MB |
| observablehq/runtime | ISC | 1,080 | `v6.0.0` | **2024-11-06** | **0.039 MB** |

`@observablehq/runtime@6.0.0` file inventory (OBSERVED, jsDelivr data API): total 39 KB, of which `src/runtime.js` 11,822 B, `src/variable.js` 8,657 B, `src/module.js` 6,049 B, `README.md` 12,743 B. There is no `dist/` (404 on `dist/runtime.js`); the package is ESM source. **This is three orders of magnitude smaller than any Python substrate — because it executes no Python.**

**What the reactive runtime actually guarantees (VENDOR, verbatim):**

`observablehq/runtime` README @ `v6.0.0`:
> "The **Observable Runtime** implements reactivity in both Observable Framework and Observable notebooks."
> "**A variable without an associated *observer* is only computed if any transitive output of the variable has an *observer*; variables are computed on an as-needed basis for display.** This is particularly useful when the runtime has multiple modules (as with imports): only the needed variables from imported modules are computed."
> "Unlike variables, builtins cannot depend on the value of other variables or builtins; they are defined with no inputs."
> "*runtime*.dispose() … Disposes this runtime, invalidating all active variables and disabling future computation."

`observablehq/framework` `docs/reactivity.md` @ `v1.13.4`:
> "Framework runs like a spreadsheet: code re-runs automatically when referenced variables change."
> "Framework's reactivity is implemented at the language layer as part of the JavaScript runtime: there's no new API or syntax to learn. It's vanilla JavaScript, but the code runs automatically. **Code blocks in Markdown run in topological order determined by top-level variable references (a.k.a. _dataflow_), rather than in top-down document order.**"
> "Reactivity also allows **incremental evaluation** of code when values change: **only the code blocks that are downstream of changed variables run.**"
> "To be precise, Framework's reactivity manifests as:
> - Promises are implicitly awaited across code blocks
> - Generators are implicitly iterated across code blocks
> - Editing code (or files) triggers reactive updates during preview
> - The `invalidation` promise allows clean-up"
> "**Only pages can declare top-level reactive variables. Components can't define their own reactive state**, but you can pass values to them."
> "If multiple blocks define top-level variables with the same name, these blocks will still run, but any references to duplicated variables in other blocks will **throw a duplicate definition error** because the definition is ambiguous."

Framework README (VENDOR): "a free, open-source, **static site generator** for data apps… Framework features **data loaders** that precompute static snapshots of data at build time." So Observable's answer to "run computation in the browser" is: don't — precompute at build time and ship JSON.

---

## 9. Stlite and PyScript

### Stlite 1.8.1 (whitphx/stlite, Apache-2.0, 1,652★)

| Metric | Value | Label |
|---|---:|---|
| `@stlite/browser@1.8.1` unpacked npm | 91,517,039 B (87.3 MB) | OBSERVED |
| Non-`.map` assets | 191 files, **30.42 MB** | OBSERVED |
| `build/stlite.js` | 3,067 B wire / 7,847 B identity | MEASURED-BENCH |
| `build/stlite.css` | 10,880 B wire / 70,818 B identity | MEASURED-BENCH |
| `build/index-*.js` (main chunk) | 4.16 MB | OBSERVED |
| Bundled `streamlit-1.57.0-cp313-none-any.whl` | 1.64 MB | OBSERVED |
| Bundled `stlite_lib-0.1.0-py3-none-any.whl` | 0.02 MB | OBSERVED |
| `build/assets/*.wasm` | 5.24 MB (single wasm, not Pyodide's) | OBSERVED |
| Heaviest lazy chunks | `PlotlyChart-*.js` **6.60 MB**, `DeckGlJsonChart-*.js` 3.37 MB, `embed-*.js` 0.99 MB, `GraphVizChart-*.js` 0.82 MB | OBSERVED |
| Pyodide pin | **`pyodide: 0.29.3`** (devDep of `packages/kernel`, version 0.103.1) — an older major than 314.x | OBSERVED |
| Pyodide load path | configurable `pyodideUrl` option; not bundled in `@stlite/browser` | OBSERVED |
| Older `@stlite/mountable` | 0.75.0, 74.7 MB unpacked, last published 2025-01-05 | OBSERVED |

**Stated limitations (VENDOR, verbatim, README):**
> "As _Stlite_ runs on the web browser environment (Pyodide runtime), there are things not working well."
> "`st.spinner()` does not work with blocking methods like `pyodide.http.open_url()` because **_Stlite_ runs on a single-threaded environment**, so `st.spinner()` can't execute its code to start showing the spinner during the blocking method occupies the only event loop."
> "`st.bokeh_chart()` does not work since Pyodide uses Bokeh version 3.x while Streamlit only supports 2.x."
> "**`time.sleep()` is no-op. Use `asyncio.sleep()` instead. This is a restriction from Pyodide runtime.**"
> "`st.write_stream()` should be used with an async generator function rather than a normal generator function."
> "There are some small differences in how (less common) data types of DataFrame columns are handled in `st.dataframe()`, `st.data_editor()`, `st.table()`, and Altair-based charts. The reason is that _Stlite_ uses the **Parquet format instead of the Arrow IPC format** to serialize dataframes."
> "**Packages including binary extensions (e.g. C/Rust/Fortran/etc) that are not built for the Pyodide environment cannot be installed.**"

### PyScript 2026.7.2 (pyscript/pyscript, Apache-2.0, 18,690★)

| Asset | Wire (br) | Identity |
|---|---:|---:|
| `https://pyscript.net/releases/2026.7.2/core.js` (re-export shim) | 214 B | 260 B |
| `.../core-Ze80f4LS.js` (real bundle) | **48,133 B** | 136,035 B |
| `.../core.css` | 382 B | 879 B |
| `@pyscript/core@0.7.31` unpacked npm | — | 5.16 MB (158 files, mostly maps + CodeMirror + xterm) |

**Two interpreters, pinned in the bundle (MEASURED-BENCH, grep of `core-Ze80f4LS.js`):**
```js
{type:"pyodide", module:(e="314.0.2")=>`https://cdn.jsdelivr.net/pyodide/v${e}/full/pyodide.mjs`, …}
// and
`https://cdn.jsdelivr.net/npm/@micropython/micropython-webassembly-pyscript@${e}/micropython.mjs`
```
Version literals in the bundle: `"314.0.2"` (Pyodide), `"1.28.0-6"` (MicroPython), `"0.28.0"`.

**MicroPython path weight (MEASURED-BENCH, identity):**

| File | Bytes |
|---|---:|
| `micropython.mjs` | 108,321 |
| `micropython.wasm` | **446,411** |
| **Total** | **554,732 B = 0.53 MB** |

**This is the single most important number for lightweight teaching material: PyScript's MicroPython target is 0.53 MB vs. Pyodide's 5.70 MB — an ~11× reduction — at the cost of losing numpy/pandas/matplotlib entirely.**

`@pyscript/core` deps (OBSERVED): built on `polyscript ^0.20.16`. PyScript docs limitations page: **UNVERIFIED** (docs.pyscript.net not fetched).

---

## 10. Thebe / Binder — the server-backed contrast

**Thebe (jupyter-book/thebe, BSD-3-Clause, 442★).** Latest release `thebe-lite@0.4.10`, **2024-09-06 — ~23 months stale.** npm `thebe@0.9.3` last published 2025-01-28.

Packages (VENDOR, README): `thebe` (browser bundle), `thebe-core` (low-level TS), **`thebe-lite`** ("adds a `jupyterlite` server for WASM based kernels"), `thebe-react`.
> "**`thebe` 0.9.0 is still under development and documentation is work in progress (PRs welcome!)**"

| Asset | Bytes | Label |
|---|---:|---|
| `thebe@0.9.3/lib/index.js` | 1,495,556 (1.43 MB identity, identical on jsDelivr and unpkg) | MEASURED-BENCH |
| `thebe@0.9.3` npm unpacked | 14.05 MB (6.15 MB of which is `index.js.map`) | OBSERVED |
| `thebe-lite@0.5.0/dist/lib/thebe-lite.min.js` | 0.50 MB | OBSERVED |
| `thebe-lite@0.5.0` npm unpacked | 3.99 MB | OBSERVED |

**mybinder.org live facts (MEASURED-BENCH / OBSERVED):**
```bash
curl -s https://mybinder.org/versions
# {"builder_info":{"build_image":"quay.io/jupyterhub/repo2docker:2026.4.1.dev17-gc38409c7f"},
#  "binderhub":"0.2.0+2252.g1013493a", ...}
curl -s -o /dev/null -w '%{http_code} %{time_total}\n' https://mybinder.org/   # 200, 0.339 s
```

**Per-user resource limits (OBSERVED, `gh api repos/jupyterhub/mybinder.org-deploy/contents/mybinder/values.yaml`):**

| Setting | Value |
|---|---|
| `singleuser.memory.guarantee` | **450M** |
| `singleuser.memory.limit` | **2G** |
| `singleuser.cpu.guarantee` | **0.01** |
| `singleuser.cpu.limit` | **1** |
| `MappingKernelManager.cull_idle_timeout` | **600 s** |
| `MappingKernelManager.cull_interval` | 60 s |
| `MappingKernelManager.cull_connected` | true |
| `shutdown_no_activity_timeout` | 600 s |
| repo2docker build pod limits | ephemeral-storage 2G, memory 2G, cpu 1; `KubernetesCleaner.max_age` 3600 s |

So Binder gives you **exactly the same 2 GB memory ceiling marimo advertises for WASM, plus 1 CPU**, but costs a live container, an image build (up to ~10 min cold), and dies after 10 minutes idle. `jupyterhub/binderhub` publishes **no GitHub releases** (`releases/latest` → 404).

---

## 11. MEASURED-BENCH: Pyodide compute timings on Node

**Caveat first, stated explicitly: Node.js Pyodide load is NOT the same as a browser's.** `loadPyodide()` in Node reads `pyodide.asm.wasm` and `python_stdlib.zip` **from the local filesystem** (`node_modules/pyodide`), so **zero network bytes** are involved. The numbers below are a **floor on compute time only** — they exclude the 5.70 MB core + 16.19 MB package download measured in §2. On a real browser cold start, add the network time.

```bash
mkdir pybench && cd pybench && npm init -y && npm install pyodide@314.0.3   # node_modules/pyodide = 14M
node bench.mjs   # times loadPyodide, runPython, loadPackage, imports
```

| Phase | Run 1 (cold pkg cache) | Run 2 | Run 3 |
|---|---:|---:|---:|
| `loadPyodide()` | 1.057 s | 1.009 s | 1.029 s |
| `runPython("1+1")` | 0.0004 s | 0.0004 s | 0.0012 s |
| `loadPackage("numpy")` | 0.383 s † | 0.180 s | 0.216 s |
| `import numpy` + `np.arange(10).sum()` | 0.269 s | 0.255 s | 0.258 s |
| `loadPackage(["matplotlib","pandas"])` (12 pkgs) | 0.926 s † | 0.510 s | 0.548 s |
| `import matplotlib.pyplot` + `import pandas` | 2.350 s | 2.501 s | 2.480 s |
| **Total to a usable numpy+pandas+matplotlib session** | **4.986 s** | **4.455 s** | **4.532 s** |

† Run 1 fetched the 13 wheels from jsDelivr and cached them into `node_modules`; runs 2–3 are fully local.

**The dominant cost is not download — it's `import matplotlib.pyplot` + `import pandas`, at ~2.5 s of pure CPU.** That cost is paid on every page load in a browser (no way to cache a warm interpreter), on top of the network.

### Pyodide vs. native CPython on the same host (MEASURED-BENCH)

| Microbenchmark | Pyodide 314.0.3 (Python 3.14, wasm32) | Native CPython 3.12.3 | Ratio |
|---|---:|---:|---:|
| Pure-Python loop, `sum i for i in range(3_000_000)` | 0.316 / 0.349 / 0.353 s (median **0.349**) | **0.1444 s** | **2.4×** |
| `numpy` 300×300 matmul × 20, 1 thread | 0.302 / 0.302 / 0.303 s (median **0.302**) | 0.0179 s (`OMP_NUM_THREADS=1`) | **16.9×** |
| same, native BLAS unrestricted (20 cores) | 0.302 s | 0.0070 s | **43×** |

The pure-Python ratio (2.4×) is consistent with Pyodide's own "3x to 5x slower than native Python" claim (§4.1). **The numpy gap is far worse (17–43×)** because Pyodide's BLAS is single-threaded, unvectorized `libopenblas` compiled to wasm32 with no SIMD tuning. Caveat: native is CPython 3.12/numpy 2.5.1, Pyodide is CPython 3.14/numpy 2.4.3 — not a version-matched comparison. Label the numpy ratio as indicative, not exact.

---

## 12. Summary matrix

| Substrate | Language | Cold-start wire bytes (engine) | Package universe | Memory ceiling | Threads | Maintenance |
|---|---|---:|---:|---|---|---|
| PyScript + MicroPython | MicroPython 1.28.0-6 | **0.53 MB** | stdlib-ish only | UNVERIFIED | no | active (2026-07) |
| Observable runtime | JavaScript | **0.027 MB** | npm/ESM (no Python) | browser heap | Workers | runtime stale (2024-11) |
| Pyodide (raw) | CPython 3.14 | 5.70 MB | **293** wasm pkgs + pure-py PyPI | 4 GB build cap | **no** | very active |
| PyScript + Pyodide | CPython 3.14 | 5.75 MB | same | same | no | active |
| marimo WASM export | CPython 3.14 | ≈8.0 MB | same (Pyodide 314.0.0) | **2 GB (vendor)** | cooperative adapters only | very active |
| Quarto Live | R + Python | 0.66 MB shim + 5.70 (Py) and/or 15.28 (R) | 21,623 R + 293 Py | inherit | no | active (0.2.0, 2026-05) |
| stlite | CPython (Pyodide 0.29.3) | ≈11.5 MB | Pyodide 0.29.x set | inherit | **single event loop** | active |
| JupyterLite + Pyodide | CPython 3.14 | ≈11.3 MB | 293 + `%pip` | inherit | no | very active |
| WebR | R 4.4/4.5 | ≈15.28 MB | **21,623** | UNVERIFIED | no | active |
| Thebe + Binder | any (real container) | 1.43 MB JS + container | full PyPI/conda | **2 GB, 1 CPU** | yes | **thebe stale (2024-09)** |

**Three findings that dominate the rest:**
1. **The floor for real Python is ~5.7 MB, and a numpy+pandas+matplotlib teaching session is ~21.9 MB over the wire plus ~4.5 s of CPU** (MEASURED-BENCH), on every cold visit.
2. **R's browser package ecosystem is 74× larger than Python's** (21,623 vs. 293 pre-built wasm packages), at the cost of a 2.7× heavier engine.
3. **plotly, seaborn, ipywidgets, and anywidget are all absent from the Pyodide distribution.** They are micropip-installable pure-Python wheels, but plotly alone is 9.45 MB and ipywidgets needs host-page widget-manager plumbing. torch/tensorflow/jax are simply unavailable.

## 13. Explicitly UNVERIFIED
- Real browser cold-start wall clock (no headless browser available; only Node compute timings + measured byte counts).
- Per-browser wasm memory caps below Pyodide's 4 GB build ceiling.
- WebR's documented memory/threading limits (docs.r-wasm.org not fetched).
- PyScript's own limitations page (docs.pyscript.net not fetched).
- Pyodide's filesystem/persistence semantics beyond what §4.5 quotes.
- Non-`-dev` emscripten-forge channel contents.
- `quarto-wasm` — no such repo found on GitHub.
- stlite's default runtime Pyodide CDN URL (the option `pyodideUrl` exists; the default value was not resolved from the minified bundle).
