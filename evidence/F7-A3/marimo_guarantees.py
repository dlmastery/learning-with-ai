#!/usr/bin/env python3
"""
A3 original measurement: what classes of "inconsistent learner state" does a
reactive-DAG notebook eliminate BY CONSTRUCTION, and which does it not?

Method: construct minimal marimo notebooks, one per hazard class, and attempt
to run each. Record (a) whether marimo refuses to build the DAG, (b) whether
it runs and produces the dependency-correct answer, (c) whether a naive
source-order executor (the Jupyter "run all top-to-bottom" model) agrees.

Reproduce:  uv venv .venv && uv pip install marimo && .venv/bin/python marimo_guarantees.py
"""
import io, os, sys, json, traceback, textwrap, contextlib, tempfile, subprocess, time

RESULTS = []


def write_nb(name, src):
    d = tempfile.mkdtemp(prefix="mo_")
    p = os.path.join(d, f"{name}.py")
    open(p, "w").write(textwrap.dedent(src))
    return p


def run_marimo(path):
    """Load the notebook module and call app.run(); return (status, detail)."""
    code = textwrap.dedent(f"""
        import sys, json, traceback
        sys.path.insert(0, {os.path.dirname(path)!r})
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location("nb", {path!r})
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            outs, defs = m.app.run()
            print("MARIMO_OK::" + json.dumps({{k: repr(v) for k, v in defs.items()
                                              if not k.startswith("_")}}, default=str))
        except Exception as e:
            print("MARIMO_ERR::" + type(e).__name__ + "::" + str(e).replace("\\n", " | ")[:400])
    """)
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=120)
    out = (r.stdout + r.stderr).strip().splitlines()
    line = next((l for l in out if l.startswith("MARIMO_")), "MARIMO_ERR::NoOutput::" + " ".join(out[-3:]))
    if line.startswith("MARIMO_OK::"):
        return "RAN", json.loads(line[len("MARIMO_OK::"):])
    _, kind, msg = line.split("::", 2)
    return "REFUSED/ERROR", f"{kind}: {msg}"


def run_source_order(cells, probe):
    """The Jupyter 'run all cells top to bottom' model, for contrast."""
    g = {}
    for c in cells:
        try:
            exec(textwrap.dedent(c), g)
        except Exception as e:
            return f"{type(e).__name__}: {e}"
    return repr(g.get(probe))


def run_arbitrary_order(cells, order, probe):
    """The Jupyter 'learner clicks cells in whatever order' model."""
    g = {}
    for i in order:
        try:
            exec(textwrap.dedent(cells[i]), g)
        except Exception as e:
            return f"{type(e).__name__}: {e}"
    return repr(g.get(probe))


def case(name, hazard, marimo_src, plain_cells, probe, orders):
    p = write_nb(name, marimo_src)
    status, detail = run_marimo(p)
    src_ord = run_source_order(plain_cells, probe)
    alts = {str(o): run_arbitrary_order(plain_cells, o, probe) for o in orders}
    RESULTS.append(dict(case=name, hazard=hazard, marimo=status,
                        marimo_detail=detail if isinstance(detail, str) else detail.get(probe, detail),
                        source_order=src_ord, arbitrary_orders=alts))


HDR = "import marimo\napp = marimo.App()\n\n"


def cell(body, args="", ret=""):
    return f"@app.cell\ndef _({args}):\n{textwrap.indent(textwrap.dedent(body), '    ')}\n    return {ret}\n\n"


# ---------------------------------------------------------------- H1: out-of-order definition
case(
    "H1_out_of_order",
    "Cell that USES a name appears ABOVE the cell that DEFINES it (the single "
    "commonest cause of NameError in published notebooks: 14.53% of Pimentel failures).",
    HDR + cell("y = x * 2", args="x", ret="y") + cell("x = 21", ret="x"),
    ["y = x * 2", "x = 21"],
    "y", [(1, 0)],
)

# ---------------------------------------------------------------- H2: multiple definition
case(
    "H2_multiple_definition",
    "Two cells define the same global. In Jupyter the answer depends on which "
    "cell you ran last; there is no notion of a wrong answer.",
    HDR + cell("x = 1", ret="x") + cell("x = 99", ret="x"),
    ["x = 1", "x = 99"],
    "x", [(1, 0)],
)

# ---------------------------------------------------------------- H3: cycle
case(
    "H3_cycle",
    "Mutual dependency between two cells.",
    HDR + cell("a = b + 1", args="b", ret="a") + cell("b = a + 1", args="a", ret="b"),
    ["a = b + 1", "b = a + 1"],
    "a", [(1, 0)],
)

# ---------------------------------------------------------------- H4: stale downstream after edit
case(
    "H4_stale_downstream",
    "Learner changes an upstream parameter but does not re-run the downstream "
    "cell. Tests whether the DAG forces recomputation.",
    HDR + cell("rate = 0.10", ret="rate") + cell("total = 1000 * (1 + rate)", args="rate", ret="total"),
    ["rate = 0.10", "total = 1000 * (1 + rate)", "rate = 0.50"],
    "total", [(0, 1, 2)],  # learner edits rate afterwards and does not re-run cell 1
)

# ---------------------------------------------------------------- H5: the mutation hole
case(
    "H5_mutation_hole",
    "Cell A binds a mutable object; cell B mutates it in place; cell C reads a "
    "derived value. marimo's static analysis sees only NAME reads/writes.",
    HDR + cell("xs = [1, 2, 3]", ret="xs") + cell("xs.append(100)", args="xs", ret="")
        + cell("total = sum(xs)", args="xs", ret="total"),
    ["xs = [1, 2, 3]", "xs.append(100)", "total = sum(xs)"],
    "total", [(0, 2, 1), (0, 1, 2)],
)

# ---------------------------------------------------------------- H6: attribute mutation
case(
    "H6_attribute_mutation",
    "Mutation through an attribute rather than a method - the marimo docs' own "
    "stated non-guarantee (`foo.bar = 10`).",
    HDR + "import types\n\n" + cell("cfg = __import__('types').SimpleNamespace(n=10)", ret="cfg")
        + cell("cfg.n = 999", args="cfg", ret="") + cell("area = cfg.n ** 2", args="cfg", ret="area"),
    ["import types", "cfg = types.SimpleNamespace(n=10)", "cfg.n = 999", "area = cfg.n ** 2"],
    "area", [(0, 1, 3, 2), (0, 1, 2, 3)],
)

# ---------------------------------------------------------------- H7: hidden state from a deleted cell
case(
    "H7_deleted_cell_residue",
    "A cell is deleted from the document but its variable is still referenced. "
    "In Jupyter the variable survives in kernel memory; the notebook appears to work.",
    HDR + cell("z = helper * 2", args="helper", ret="z"),   # `helper` is never defined
    ["helper = 5", "z = helper * 2"],   # source-order arm keeps the deleted cell to show the contrast
    "z", [(0, 1)],
)

# ---------------------------------------------------------------- H8: nondeterminism (not a hidden-state class)
case(
    "H8_nondeterminism",
    "Unseeded randomness. Present in neither model's guarantee. Included as the "
    "control: reactivity is orthogonal to determinism.",
    HDR + cell("import random\nr = random.random()", ret="r"),
    ["import random", "r = random.random()"],
    "r", [(0, 1)],
)

print(json.dumps(RESULTS, indent=2, default=str))
