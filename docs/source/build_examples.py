"""Convert docs/examples/*.py (percent format) to executed notebooks.

Files whose names start with an underscore are helper modules that the
examples import. They are not converted, but changing one rebuilds all examples.
"""
from pathlib import Path

import jupytext
from nbclient import NotebookClient

HERE = Path(__file__).parent          # docs/source
SRC = HERE.parent / "examples"        # docs/examples  (the .py scripts)
OUT = HERE / "examples"               # docs/source/examples  (the notebooks)
KERNEL = "python3"  # the kernel of the active venv, provided ipykernel is installed there


def build(force=False):
    OUT.mkdir(parents=True, exist_ok=True)

    # Helper modules are not examples, but the examples depend on them
    helpers = list(SRC.glob("_*.py"))
    newest_helper = max((h.stat().st_mtime for h in helpers), default=0)

    for script in sorted(SRC.glob("*.py")):
        if script.name.startswith("_"):
            continue
        nb_path = OUT / (script.stem + ".ipynb")
        source_mtime = max(script.stat().st_mtime, newest_helper)
        up_to_date = nb_path.exists() and nb_path.stat().st_mtime >= source_mtime
        if up_to_date and not force:
            continue
        print(f"Executing {script.name} -> {nb_path.name}")
        nb = jupytext.read(script)
        nb.metadata["kernelspec"] = {
            "name": KERNEL, "display_name": KERNEL, "language": "python",
        }
        # timeout=None: model runs can take a long time on CPU
        NotebookClient(nb, timeout=None, kernel_name=KERNEL,
                       resources={"metadata": {"path": str(SRC)}}).execute()
        jupytext.write(nb, nb_path)


if __name__ == "__main__":
    import sys
    build(force="--force" in sys.argv)