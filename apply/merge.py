#!/usr/bin/env python3
"""Merge an application's PDFs into the single file a portal asks for.

Several programmes want one PDF containing statement, CV, transcripts,
certificates and a writing sample, in that order, under a name they specify.
UCLouvain is the first, and it will not be the last, so this is a tool rather
than a one-off command.

Each application folder that needs it carries a `merge.txt` manifest:

    # lines starting with a hash are ignored, blank lines too
    out: Khammari_Baha.pdf
    statement.pdf
    cv_uclouvain_khammari.pdf
    ~/documents/Khammari_ToR_Aug2026.pdf
    ../../../research/thesis/Master_Thesis_Final.pdf

Order in the file is order in the output. Relative paths resolve against the
application folder. `~` expands, so personal documents can live outside the
repository, which they should: this repository is public and transcripts are
not.

Usage:

    python3 apply/merge.py uclouvain          # substring match on the folder
    python3 apply/merge.py                    # every folder that has a manifest

Missing sources are reported by name and stop the merge. A half-assembled
application PDF is worse than none, because it looks finished.

Needs either pypdf (`pip install pypdf`) or pdfunite from poppler-utils
(`apt install poppler-utils`). It uses whichever it finds.
"""

import logging
import os
import subprocess
import sys

# pypdf logs "Annotation sizes differ" once per annotation when it appends a
# document with internal links, which the thesis has by the dozen. The warning
# is about nothing and it buries the page table under sixty lines.
logging.getLogger("pypdf").setLevel(logging.ERROR)

HERE = os.path.dirname(os.path.abspath(__file__))
APPS = os.path.join(HERE, "applications")
MANIFEST = "merge.txt"


def parse(path):
    """Return (out_name, [absolute source paths]) from a manifest."""
    folder = os.path.dirname(path)
    out = None
    sources = []
    for raw in open(path, encoding="utf-8"):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if line.lower().startswith("out:"):
            out = line.split(":", 1)[1].strip()
            continue
        expanded = os.path.expanduser(line)
        if not os.path.isabs(expanded):
            expanded = os.path.join(folder, expanded)
        sources.append(os.path.normpath(expanded))
    if out is None:
        out = "merged.pdf"
    return out, sources


def pages(path):
    try:
        from pypdf import PdfReader

        return len(PdfReader(path).pages)
    except Exception:
        return None


def merge(sources, target):
    try:
        from pypdf import PdfWriter
    except ImportError:
        subprocess.run(["pdfunite"] + sources + [target], check=True)
        return
    writer = PdfWriter()
    for src in sources:
        writer.append(src)
    with open(target, "wb") as fh:
        writer.write(fh)


def run(folder):
    path = os.path.join(folder, MANIFEST)
    out_name, sources = parse(path)
    target = os.path.join(folder, out_name)

    missing = [s for s in sources if not os.path.exists(s)]
    if missing:
        print(f"{os.path.basename(folder)}: cannot merge, {len(missing)} missing")
        for m in missing:
            print(f"    {m}")
        print("\n  Put the file where the manifest expects it, or edit the path in")
        print(f"  {path}")
        return False

    merge(sources, target)
    print(f"{out_name}")
    total = 0
    for src in sources:
        n = pages(src)
        total += n or 0
        label = f"{n}p" if n else "?"
        print(f"    {label:>4}  {os.path.relpath(src, folder)}")
    if total:
        print(f"    {total:>4}  total")
    return True


def main():
    pattern = sys.argv[1].lower() if len(sys.argv) > 1 else None
    folders = []
    for name in sorted(os.listdir(APPS)):
        folder = os.path.join(APPS, name)
        if not os.path.isfile(os.path.join(folder, MANIFEST)):
            continue
        if pattern and pattern not in name.lower():
            continue
        folders.append(folder)

    if not folders:
        where = f"matching '{pattern}'" if pattern else "at all"
        print(f"No application folder {where} has a {MANIFEST}.")
        return 1

    ok = True
    for folder in folders:
        ok = run(folder) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
