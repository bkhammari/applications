#!/usr/bin/env python3
"""Read and update the application tracker.

    python3 apply/track.py list              open applications
    python3 apply/track.py list --all        including closed and rejected
    python3 apply/track.py due               follow-ups owed and deadlines closing in
    python3 apply/track.py sent frontier     mark as sent, schedule the nudge
    python3 apply/track.py set frontier interview
    python3 apply/track.py note frontier "asked about the R pipeline"
    python3 apply/track.py summary

Ids can be shortened. Any unique prefix works, and so does a unique employer name.
"""

import argparse
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import _tracker as t


def table(rows, columns):
    """Print rows as an aligned table. columns is a list of (header, key) pairs."""
    if not rows:
        return
    widths = []
    for header, key in columns:
        longest = max([len(str(r.get(key, "") or "")) for r in rows] + [len(header)])
        widths.append(min(longest, 42))

    def line(cells):
        out = []
        for cell, width in zip(cells, widths):
            cell = str(cell or "")
            if len(cell) > width:
                cell = cell[: width - 1] + "…"
            out.append(cell.ljust(width))
        return "  ".join(out).rstrip()

    print(line([h for h, _ in columns]))
    print(line(["-" * w for w in widths]))
    for row in rows:
        print(line([row.get(k, "") for _, k in columns]))


def cmd_list(args):
    rows = t.read_rows()
    if not args.all:
        rows = [r for r in rows if r["status"] in t.OPEN_STATUSES]
    if not rows:
        print("Nothing tracked yet. Add one with apply/new.py")
        return 0
    rows.sort(key=lambda r: (r["status"], r["added"]))
    table(
        rows,
        [
            ("ID", "id"),
            ("EMPLOYER", "employer"),
            ("ROLE", "role"),
            ("TRACK", "track"),
            ("PAY", "pay"),
            ("DEADLINE", "deadline"),
            ("STATUS", "status"),
        ],
    )
    print(f"\n{len(rows)} shown.")
    return 0


def cmd_due(args):
    rows = t.read_rows()
    now = t.today()

    nudges = []
    for row in rows:
        if row["status"] != "sent":
            continue
        due = t.parse_date(row["followup"])
        if due and due <= now:
            row = dict(row, waiting=f"{(now - t.parse_date(row['sent'])).days}d")
            nudges.append(row)

    closing = []
    for row in rows:
        if row["status"] not in ("draft",):
            continue
        deadline = t.parse_date(row["deadline"])
        if deadline is None:
            continue
        left = (deadline - now).days
        if left <= t.DEADLINE_WARNING_DAYS:
            label = f"{left}d" if left >= 0 else f"{-left}d ago"
            closing.append(dict(row, left=label))

    if nudges:
        print("Follow-ups owed\n")
        nudges.sort(key=lambda r: r["followup"])
        table(
            nudges,
            [("ID", "id"), ("EMPLOYER", "employer"), ("SENT", "sent"), ("SILENT", "waiting")],
        )
        print()

    if closing:
        print("Deadlines closing, still unsent\n")
        closing.sort(key=lambda r: r["deadline"])
        table(
            closing,
            [("ID", "id"), ("EMPLOYER", "employer"), ("DEADLINE", "deadline"), ("LEFT", "left")],
        )
        print()

    if not nudges and not closing:
        print("Nothing owed today.")
    return 0


def _save(rows):
    t.write_rows(rows)


def cmd_sent(args):
    rows = t.read_rows()
    row = t.find(rows, args.id)
    date = args.date or t.iso(t.today())
    if t.parse_date(date) is None:
        raise SystemExit(f"--date must be an ISO date, got '{date}'")
    row["status"] = "sent"
    row["sent"] = date
    row["followup"] = t.iso(t.parse_date(date) + datetime.timedelta(days=t.FOLLOWUP_DAYS))
    _save(rows)
    print(f"{row['id']}: sent {date}, nudge due {row['followup']}")
    return 0


def cmd_set(args):
    rows = t.read_rows()
    row = t.find(rows, args.id)
    if args.status not in t.STATUSES:
        raise SystemExit(f"status must be one of: {', '.join(t.STATUSES)}")
    was = row["status"]
    row["status"] = args.status
    if args.status not in ("sent",):
        row["followup"] = ""
    _save(rows)
    print(f"{row['id']}: {was} -> {args.status}")
    return 0


def cmd_note(args):
    rows = t.read_rows()
    row = t.find(rows, args.id)
    stamp = t.iso(t.today())
    existing = row.get("notes", "")
    row["notes"] = f"{existing} | {stamp}: {args.text}".strip(" |")
    _save(rows)
    print(f"{row['id']}: noted")
    return 0


def cmd_summary(args):
    rows = t.read_rows()
    if not rows:
        print("Nothing tracked yet.")
        return 0
    counts = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    width = max(len(s) for s in counts)
    for status in t.STATUSES:
        if status in counts:
            print(f"{status.ljust(width)}  {counts[status]}")
    print(f"{'total'.ljust(width)}  {len(rows)}")

    sent = [r for r in rows if r["status"] not in ("draft",)]
    replied = [r for r in rows if r["status"] in ("replied", "interview", "offer")]
    if sent:
        rate = 100.0 * len(replied) / len(sent)
        print(f"\nreply rate  {len(replied)}/{len(sent)}  ({rate:.0f}%)")
    return 0


def build_parser():
    p = argparse.ArgumentParser(prog="apply/track.py", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command", required=True)

    lst = sub.add_parser("list", help="show applications")
    lst.add_argument("--all", action="store_true", help="include closed and rejected")
    lst.set_defaults(func=cmd_list)

    due = sub.add_parser("due", help="follow-ups owed and deadlines closing in")
    due.set_defaults(func=cmd_due)

    snt = sub.add_parser("sent", help="mark as sent and schedule the nudge")
    snt.add_argument("id")
    snt.add_argument("--date", default="", help="ISO date, defaults to today")
    snt.set_defaults(func=cmd_sent)

    st = sub.add_parser("set", help="set the status")
    st.add_argument("id")
    st.add_argument("status", choices=t.STATUSES)
    st.set_defaults(func=cmd_set)

    nt = sub.add_parser("note", help="append a dated note")
    nt.add_argument("id")
    nt.add_argument("text")
    nt.set_defaults(func=cmd_note)

    sm = sub.add_parser("summary", help="counts and reply rate")
    sm.set_defaults(func=cmd_summary)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
