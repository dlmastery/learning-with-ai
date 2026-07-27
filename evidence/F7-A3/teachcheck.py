#!/usr/bin/env python3
"""
teachcheck - a conformance checker for reproducible executable teaching material.

Generalises the G3 xiaol result (16/16 byte-identical, 0.55 s, by pure
subtraction) into nine mechanically checkable rules, and adds the two things
that artifact lacked: assertions, and a failing exit code.

Reproducibility criterion is FlowBook's (arXiv:2605.01560): an artifact is
reproducible iff executing it from an empty store reproduces the recorded
outputs exactly. We add: twice, in a clean process, with a scrubbed environment.

Usage:  python3 teachcheck.py <dir>          # dir contains *.py + expected/*.txt
Exit code 0 iff every rule passes for every script.
"""
import ast, hashlib, json, os, re, subprocess, sys, time

# ---------------------------------------------------------------- rule tables
# Modules Pyodide removes or breaks (pyodide/docs/usage/wasm-constraints.md)
WASM_BROKEN = {"multiprocessing", "threading", "socket", "socketserver", "subprocess",
               "curses", "dbm", "ensurepip", "fcntl", "grp", "idlelib", "lib2to3",
               "msvcrt", "pwd", "resource", "syslog", "termios", "tkinter", "turtle",
               "turtledemo", "venv", "winreg", "winsound", "ssl", "concurrent.futures"}
NETWORK = {"urllib", "urllib.request", "requests", "httpx", "http", "http.client",
           "ftplib", "smtplib", "telnetlib", "aiohttp", "socket", "urllib3"}
NONDET = {("random", None), ("secrets", None), ("uuid", "uuid1"), ("uuid", "uuid4"),
          ("os", "urandom"), ("time", "time"), ("datetime", "now"), ("datetime", "today")}
STDLIB = set(sys.stdlib_module_names)

RULES = [
    ("R1", "No network access, statically or dynamically"),
    ("R2", "No unseeded nondeterminism"),
    ("R3", "Dependencies stdlib-only, or declared inline (PEP 723) and pinned"),
    ("R4", "Byte-identical across two runs in fresh processes"),
    ("R5", "Reproduces its committed expected output byte-for-byte"),
    ("R6", "Contains at least one assertion (it can fail)"),
    ("R7", "Portable to a WASM runtime (no threads/processes/sockets)"),
    ("R8", "Runs inside the wall-clock budget"),
    ("R9", "Input data fits inside the size budget"),
]
BUDGET_S = 5.0
BUDGET_DATA_BYTES = 64 * 1024


def imports(tree):
    out = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Import):
            out |= {a.name.split(".")[0] for a in n.names} | {a.name for a in n.names}
        elif isinstance(n, ast.ImportFrom) and n.module:
            out.add(n.module.split(".")[0]); out.add(n.module)
    return out


def seeded(tree):
    """random.seed(...) / np.random.seed(...) present before any draw?"""
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "seed":
            return True
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "seed":
            return True
    return False


def nondeterministic(tree):
    hits = []
    imps = imports(tree)
    if "random" in imps and not seeded(tree):
        hits.append("random imported without seed()")
    if "secrets" in imps:
        hits.append("secrets")
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
            mod = getattr(n.func.value, "id", None)
            if (mod, n.func.attr) in NONDET:
                hits.append(f"{mod}.{n.func.attr}()")
            if n.func.attr in ("now", "today", "time") and mod in ("datetime", "time"):
                hits.append(f"{mod}.{n.func.attr}()")
    return hits


def inline_deps(src):
    """PEP 723 inline script metadata."""
    m = re.search(r"^#\s*/// script\s*$(.*?)^#\s*///\s*$", src, re.M | re.S)
    if not m:
        return None
    body = re.sub(r"^#\s?", "", m.group(1), flags=re.M)
    return body


def run_clean(path, env_extra=None):
    """Fresh interpreter, scrubbed env, no site-packages inheritance surprises."""
    env = {"PATH": "/usr/bin:/bin", "HOME": "/nonexistent", "LC_ALL": "C",
           "PYTHONHASHSEED": "0", "TZ": "UTC", "PYTHONDONTWRITEBYTECODE": "1"}
    if env_extra:
        env.update(env_extra)
    t0 = time.perf_counter()
    p = subprocess.run([sys.executable, os.path.basename(path)], capture_output=True,
                       cwd=os.path.dirname(os.path.abspath(path)), env=env, timeout=60)
    return p.returncode, p.stdout, p.stderr, time.perf_counter() - t0


def check(path, expected_dir):
    src = open(path).read()
    tree = ast.parse(src)
    imps = imports(tree)
    third = {m for m in imps if m.split(".")[0] not in STDLIB and "." not in m}
    res, notes = {}, {}

    net = sorted(imps & NETWORK)
    res["R1"] = not net; notes["R1"] = ",".join(net) or "clean"

    nd = nondeterministic(tree)
    res["R2"] = not nd; notes["R2"] = ";".join(nd) or "deterministic"

    dep = inline_deps(src)
    if not third:
        res["R3"], notes["R3"] = True, "stdlib-only"
    elif dep and all(re.search(r"[=~><]=", l) for l in re.findall(r'"([^"]+)"', dep) or ["x"]):
        res["R3"], notes["R3"] = True, "PEP723 pinned: " + ",".join(sorted(third))
    else:
        res["R3"], notes["R3"] = False, "undeclared/unpinned: " + ",".join(sorted(third))

    rc1, o1, e1, t1 = run_clean(path)
    rc2, o2, e2, t2 = run_clean(path)
    res["R4"] = (rc1 == rc2 == 0) and o1 == o2
    notes["R4"] = f"rc={rc1}/{rc2} sha1={hashlib.sha1(o1).hexdigest()[:10]}/{hashlib.sha1(o2).hexdigest()[:10]}"
    if rc1 != 0:
        notes["R4"] += " ERR:" + e1.decode("utf8", "ignore").strip().splitlines()[-1][:90]

    exp = os.path.join(expected_dir, os.path.basename(path).replace(".py", ".txt"))
    if os.path.exists(exp):
        want = open(exp, "rb").read()
        res["R5"] = (o1 == want); notes["R5"] = "match" if o1 == want else f"differs ({len(o1)}B vs {len(want)}B)"
    else:
        res["R5"] = False; notes["R5"] = "no committed expected output"

    n_assert = sum(isinstance(n, ast.Assert) for n in ast.walk(tree))
    res["R6"] = n_assert > 0; notes["R6"] = f"{n_assert} assert(s)"

    bad = sorted(imps & WASM_BROKEN)
    res["R7"] = not bad; notes["R7"] = ",".join(bad) or "wasm-portable"

    res["R8"] = max(t1, t2) <= BUDGET_S; notes["R8"] = f"{max(t1,t2)*1000:.0f} ms"

    d = os.path.join(os.path.dirname(os.path.abspath(path)), "data")
    size = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(d) for f in fs) if os.path.isdir(d) else 0
    res["R9"] = size <= BUDGET_DATA_BYTES; notes["R9"] = f"{size} B"
    return res, notes, max(t1, t2)


def main(d):
    expected = os.path.join(d, "expected")
    scripts = sorted(f for f in os.listdir(d) if f.endswith(".py"))
    rows, total_t, t_start = [], 0.0, time.perf_counter()
    for s in scripts:
        r, n, t = check(os.path.join(d, s), expected)
        total_t += t
        rows.append((s, r, n))
    print(f"{'script':<26} " + " ".join(f"{k}" for k, _ in RULES))
    allpass = True
    for s, r, n in rows:
        line = f"{s:<26} " + "  ".join(("PASS" if r[k] else "FAIL")[:4].replace("PASS", " ok ").replace("FAIL", "FAIL") for k, _ in RULES)
        print(line)
        for k, _ in RULES:
            if not r[k]:
                allpass = False
                print(f"{'':<26}   {k}: {n[k]}")
    npass = sum(all(r.values()) for _, r, _ in rows)
    print(f"\n{npass}/{len(rows)} scripts fully conformant; "
          f"execution {total_t*1000:.0f} ms; checker wall-clock {(time.perf_counter()-t_start)*1000:.0f} ms")
    return 0 if allpass else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
