"""Shared tracker state for the application workflow.

The tracker is a CSV so that git diffs it line by line, a spreadsheet can open it,
and grep still works. Everything that reads or writes it goes through here.
"""

import csv
import datetime as _dt
import os
import re

APPLY_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(APPLY_DIR)
TRACKER = os.path.join(APPLY_DIR, "tracker.csv")
APPLICATIONS = os.path.join(APPLY_DIR, "applications")
TEMPLATES = os.path.join(APPLY_DIR, "templates")

FIELDS = [
    "id",
    "added",
    "employer",
    "role",
    "track",
    "location",
    "pay",
    "deadline",
    "url",
    "cv",
    "lang",
    "firm",
    "status",
    "sent",
    "followup",
    "notes",
]

STATUSES = [
    "draft",
    "sent",
    "replied",
    "interview",
    "offer",
    "rejected",
    "closed",
]

# Open means still worth spending time on.
OPEN_STATUSES = {"draft", "sent", "replied", "interview"}

# Which CV goes with which track. Economic consulting is its own track on purpose:
# the firms hire economists to run econometrics, their process runs in English, and
# the academic CV carries the methods detail that is the actual qualification. It
# also lists advanced Excel, so nothing commercial is given up. Override
# with --cv when a posting argues for the other one.
TRACKS = {
    "academic": "cv/academic/cv_academic_khammari.tex",
    "research": "cv/academic/cv_academic_khammari.tex",
    "policy": "cv/academic/cv_academic_khammari.tex",
    "consulting": "cv/academic/cv_academic_khammari.tex",
    "industry": "cv/professional/cv_professional_khammari.tex",
}

# Days of silence after sending before a nudge is due.
FOLLOWUP_DAYS = 12

# Days before a deadline at which an unsent application becomes urgent.
DEADLINE_WARNING_DAYS = 14


def today():
    return _dt.date.today()


def iso(date):
    return date.isoformat()


def parse_date(value):
    """Parse an ISO date, returning None for blanks and anything unparseable."""
    if not value:
        return None
    try:
        return _dt.date.fromisoformat(value.strip())
    except ValueError:
        return None


def slugify(*parts):
    raw = "-".join(p for p in parts if p)
    slug = re.sub(r"[^a-z0-9]+", "-", raw.lower()).strip("-")
    return slug[:60].strip("-") or "application"


# === What the sent files are called ===
# A recruiter downloads the attachments into a folder next to forty other people's
# attachments. "cv.pdf" is invisible there and "Lebenslauf_final_v3.pdf" is worse.
# The format is cv_<firm>_<surname>.pdf, and the letter takes the word the reader
# expects in their own language.
SURNAME = "khammari"


def firm_token(row):
    """The short employer word used in filenames.

    Taken from the tracker's `firm` column when it is set, otherwise from the
    first word of the employer name. The column exists because the first word is
    wrong often enough to matter: Deutsche Bundesbank would give "deutsche" and
    European Central Bank would give "european". Set `firm` to bundesbank or ecb
    and the filename is right.
    """
    explicit = (row.get("firm") or "").strip()
    if explicit:
        return slugify(explicit)
    return slugify(row.get("employer", "")).split("-")[0] or "application"


def send_name(kind, row):
    """The filename an application's PDF is sent under. `kind` is cv or letter."""
    if kind == "cv":
        stem = "cv"
    elif (row.get("lang") or "en").strip().lower().startswith("de"):
        stem = "anschreiben"
    else:
        stem = "letter"
    return f"{stem}_{firm_token(row)}_{SURNAME}.pdf"


def unique_slug(base, existing):
    if base not in existing:
        return base
    n = 2
    while f"{base}-{n}" in existing:
        n += 1
    return f"{base}-{n}"


def read_rows():
    if not os.path.exists(TRACKER):
        return []
    with open(TRACKER, newline="", encoding="utf-8") as fh:
        return [dict(r) for r in csv.DictReader(fh)]


def write_rows(rows):
    tmp = TRACKER + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in FIELDS})
    os.replace(tmp, TRACKER)


def append_row(row):
    rows = read_rows()
    rows.append(row)
    write_rows(rows)


def find(rows, ident):
    """Find one row by exact id, then by unique prefix, then by employer substring."""
    for row in rows:
        if row["id"] == ident:
            return row
    needle = ident.lower()
    matches = [r for r in rows if r["id"].startswith(needle)]
    if len(matches) == 1:
        return matches[0]
    matches = [r for r in rows if needle in r["employer"].lower()]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        names = ", ".join(r["id"] for r in matches[:6])
        raise SystemExit(f"'{ident}' matches several applications: {names}")
    raise SystemExit(f"No application matches '{ident}'. Run: python3 apply/track.py list")


def render(template_path, values):
    with open(template_path, encoding="utf-8") as fh:
        text = fh.read()
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text
