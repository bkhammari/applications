#!/usr/bin/env python3
"""Scaffold one application: a posting file, a letter to tailor, and a tracker row.

    python3 apply/new.py --employer "Frontier Economics" --role "Economic Analyst" \
        --track industry --location Cologne --pay "55k" --deadline 2026-10-15 \
        --url https://... --lang en

Paste the posting text with --posting-file, or leave it and fill in the file after.
Nothing is sent. This only prepares the folder and records the row.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import _tracker as t


def build_parser():
    p = argparse.ArgumentParser(
        prog="apply/new.py",
        description="Scaffold an application folder and add it to the tracker.",
    )
    p.add_argument("--employer", required=True, help="Company or institution name")
    p.add_argument("--role", required=True, help="Job title as the posting states it")
    p.add_argument(
        "--track",
        required=True,
        choices=sorted(t.TRACKS),
        help="Decides which CV goes with the application",
    )
    p.add_argument("--location", default="", help="City")
    p.add_argument("--pay", default="", help="Whatever the posting says, verbatim")
    p.add_argument("--deadline", default="", help="ISO date, or blank for rolling")
    p.add_argument("--url", default="", help="Link to the posting")
    p.add_argument("--lang", default="en", choices=["en", "de"], help="Letter language")
    p.add_argument("--contact", default="", help="Named person, if the posting gives one")
    p.add_argument("--posting-file", default="", help="File holding the posting text")
    p.add_argument("--notes", default="", help="Anything worth remembering")
    return p


def build_opening(lang, contact):
    """German needs the gendered form, so derive it from the Herr or Frau in --contact."""
    if lang == "de":
        if not contact:
            return "Sehr geehrte Damen und Herren"
        if contact.startswith("Herr"):
            return f"Sehr geehrter {contact}"
        if contact.startswith("Frau"):
            return f"Sehr geehrte {contact}"
        # No Herr or Frau given, so no basis to guess. Leave it to be filled in.
        return f"Sehr geehrte/r {contact}"
    if not contact:
        return "Dear Sir or Madam"
    return f"Dear {contact}"


def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.deadline and t.parse_date(args.deadline) is None:
        raise SystemExit(f"--deadline must be an ISO date like 2026-10-15, got '{args.deadline}'")

    posting_text = ""
    if args.posting_file:
        if not os.path.exists(args.posting_file):
            raise SystemExit(f"No such file: {args.posting_file}")
        with open(args.posting_file, encoding="utf-8") as fh:
            posting_text = fh.read().strip()

    rows = t.read_rows()
    slug = t.unique_slug(
        t.slugify(args.employer, args.role), {r["id"] for r in rows}
    )
    folder = os.path.join(t.APPLICATIONS, slug)
    os.makedirs(folder, exist_ok=True)

    date = t.iso(t.today())
    cv = t.TRACKS[args.track]
    opening = build_opening(args.lang, args.contact)

    values = {
        "EMPLOYER": args.employer,
        "ROLE": args.role,
        "TRACK": args.track,
        "LOCATION": args.location or "[city]",
        "PAY": args.pay or "not stated",
        "DEADLINE": args.deadline or "rolling",
        "URL": args.url or "[link]",
        "DATE": date,
        "CONTACT": args.contact or "[contact]",
        "OPENING": opening,
        "POSTING": posting_text or "[paste the posting text here]",
        "FIT": "[WRITE THIS. See the comment above.]",
    }

    posting_path = os.path.join(folder, "posting.md")
    letter_path = os.path.join(folder, "letter.tex")
    written = []

    if os.path.exists(posting_path):
        print(f"  kept   {os.path.relpath(posting_path, t.REPO)} (already exists)")
    else:
        with open(posting_path, "w", encoding="utf-8") as fh:
            fh.write(t.render(os.path.join(t.TEMPLATES, "posting.md"), values))
        written.append(posting_path)

    if os.path.exists(letter_path):
        print(f"  kept   {os.path.relpath(letter_path, t.REPO)} (already exists)")
    else:
        template = os.path.join(t.TEMPLATES, f"letter-{args.lang}.tex")
        with open(letter_path, "w", encoding="utf-8") as fh:
            fh.write(t.render(template, values))
        written.append(letter_path)

    t.append_row(
        {
            "id": slug,
            "added": date,
            "employer": args.employer,
            "role": args.role,
            "track": args.track,
            "location": args.location,
            "pay": args.pay,
            "deadline": args.deadline,
            "url": args.url,
            "cv": cv,
            "lang": args.lang,
            "status": "draft",
            "sent": "",
            "followup": "",
            "notes": args.notes,
        }
    )

    print(f"\n{args.employer}, {args.role}  [{slug}]")
    for path in written:
        print(f"  wrote  {os.path.relpath(path, t.REPO)}")
    print(f"  CV     {cv}")
    print("\nNext:")
    print(f"  1. Paste the posting into {os.path.relpath(posting_path, t.REPO)}")
    print("  2. Pull out what they actually asked for, then write the fit paragraph")
    print(f"  3. Move it into {os.path.relpath(letter_path, t.REPO)} and compile")
    print(f"  4. python3 apply/track.py sent {slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
