#!/usr/bin/env python3
"""Compile the LaTeX in an application folder to PDF.

    python3 apply/build.py frontier          one application
    python3 apply/build.py --all             every open application
    python3 apply/build.py --all --clean     and remove the aux files after

Needs pdflatex on PATH. On Ubuntu:

    sudo apt-get install -y texlive-latex-base texlive-latex-recommended \\
        texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra \\
        texlive-lang-german tex-gyre lmodern

tex-gyre and lmodern are easy to miss and both are required by the CV class.
"""

import argparse
import glob
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import _tracker as t

AUX = (".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".synctex.gz")


def compile_one(tex_path, runs=2):
    """Run pdflatex, twice by default so cross-references settle."""
    folder = os.path.dirname(tex_path)
    name = os.path.basename(tex_path)
    for _ in range(runs):
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", name],
            cwd=folder,
            capture_output=True,
            text=True,
        )
    pdf = os.path.splitext(tex_path)[0] + ".pdf"
    if os.path.exists(pdf):
        return True, pdf, ""
    log = os.path.splitext(tex_path)[0] + ".log"
    detail = ""
    if os.path.exists(log):
        lines = open(log, encoding="utf-8", errors="replace").read().splitlines()
        for i, line in enumerate(lines):
            if line.startswith("!"):
                detail = "\n      ".join(lines[i : i + 4])
                break
    return False, pdf, detail or result.stdout[-400:]


def pages(pdf):
    try:
        out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
        for line in out.splitlines():
            if line.startswith("Pages:"):
                return line.split()[1]
    except FileNotFoundError:
        pass
    return "?"


def clean(folder):
    for ext in AUX:
        for path in glob.glob(os.path.join(folder, "*" + ext)):
            os.remove(path)


def main(argv=None):
    p = argparse.ArgumentParser(prog="apply/build.py", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("id", nargs="?", help="Application id, or a unique prefix")
    p.add_argument("--all", action="store_true", help="Build every open application")
    p.add_argument("--clean", action="store_true", help="Remove aux files afterwards")
    args = p.parse_args(argv)

    if shutil.which("pdflatex") is None:
        raise SystemExit("pdflatex not found. See the install line in this file's docstring.")

    rows = t.read_rows()
    if args.all:
        targets = [r for r in rows if r["status"] in t.OPEN_STATUSES]
    elif args.id:
        targets = [t.find(rows, args.id)]
    else:
        raise SystemExit("Give an application id, or --all.")

    failures = 0
    for row in targets:
        folder = os.path.join(t.APPLICATIONS, row["id"])
        if not os.path.isdir(folder):
            print(f"{row['id']}: no folder, skipped")
            continue
        print(f"\n{row['employer']}, {row['role']}")
        for name in ("cv.tex", "letter.tex"):
            tex = os.path.join(folder, name)
            if not os.path.exists(tex):
                continue
            ok, pdf, detail = compile_one(tex)
            if ok:
                print(f"  ok    {os.path.relpath(pdf, t.REPO)}  ({pages(pdf)}p)")
            else:
                failures += 1
                print(f"  FAIL  {os.path.relpath(tex, t.REPO)}\n      {detail}")
        if args.clean:
            clean(folder)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
