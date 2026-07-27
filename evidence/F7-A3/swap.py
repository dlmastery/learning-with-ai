"""H5b: is the mutation-case answer determined by the DAG or by source position?
Build the SAME three cells in two different source orders; if the answer changes,
the DAG did not order them and source position decided the result."""
import textwrap, tempfile, os, subprocess, sys, json
HDR="import marimo\napp = marimo.App()\n\n"
def cell(body,args="",ret=""):
    return f"@app.cell\ndef _({args}):\n{textwrap.indent(textwrap.dedent(body),'    ')}\n    return {ret}\n\n"
A=cell("xs = [1, 2, 3]",ret="xs"); B=cell("xs.append(100)",args="xs",ret=""); C=cell("total = sum(xs)",args="xs",ret="total")
for label,src in [("A,B,C (mutate before read)",HDR+A+B+C),("A,C,B (read before mutate)",HDR+A+C+B)]:
    d=tempfile.mkdtemp(); p=os.path.join(d,"nb.py"); open(p,"w").write(src)
    code=f"""
import importlib.util,json
spec=importlib.util.spec_from_file_location("nb",{p!r}); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
o,defs=m.app.run(); print("TOTAL::",defs.get("total"))
"""
    r=subprocess.run([sys.executable,"-c",code],capture_output=True,text=True,timeout=120)
    print(label,"->",[l for l in (r.stdout+r.stderr).splitlines() if "TOTAL::" in l] or (r.stdout+r.stderr)[-300:])
