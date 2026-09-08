# Application workflow

Posting in, tailored application out, tracked until it closes. Built so that the
only thing you write per application is the one paragraph that proves you read the
posting. Everything else already exists.

Python 3, no dependencies. Run from the repo root.

## The loop

### 1. Scaffold

```bash
python3 apply/new.py \
  --employer "Frontier Economics" \
  --role "Economic Analyst" \
  --track industry \
  --location Cologne \
  --pay "55k" \
  --deadline 2026-10-15 \
  --url "https://..." \
  --lang en \
  --posting-file posting.txt
```

That creates `apply/applications/<slug>/` holding `posting.md` and `letter.tex`,
picks the right CV for the track, and adds a row to `tracker.csv` with status
`draft`. Nothing is sent.

`--lang` picks the letter language and `--contact` sets the salutation, including
the gendered German form when you pass a name starting with Herr or Frau.

## Which CV goes with which track

| Track | CV |
|---|---|
| `academic`, `research`, `policy` | `cv/academic/academic_cv.tex`, English |
| `consulting` | `cv/academic/academic_cv.tex`, English |
| `industry` | `cv/professional/cv.tex`, German |

Economic consulting has its own track rather than sitting under `industry`,
because the obvious mapping is the wrong one. Frontier, CRA, Compass Lexecon and
the rest hire economists to run econometrics, and their process runs in English.
The academic CV carries the thesis in the detail that is the actual
qualification, naming the estimator, the packages and the result, where the German
CV compresses it to a single line. It also lists advanced Excel and VBA, so nothing
commercial is given up, and it leaves out the Abitur, the Gymnasium and the retail
job, which are noise to a consultancy.

Override per application with `--cv cv/professional/cv.tex` when a posting argues
the other way, such as a German-language application to a German office. The path
is checked, so a typo fails immediately rather than silently recording a CV that
does not exist.

`--posting-file` is optional. Without it, paste the posting into `posting.md`
afterwards. Keep the text either way, because postings vanish once the role is
filled and you will want it again before the interview.

### 2. Qualify

Work through the checklist at the top of `posting.md`. Rejecting fast is what buys
the time to write a good fit paragraph for the ones that survive. The filters are
in [`../bridge/README.md`](../bridge/README.md) for research roles and
[`../bridge/private-sector.md`](../bridge/private-sector.md) for finance,
consulting and industry.

If a role fails, mark it and move on:

```bash
python3 apply/track.py set frontier closed
```

### 3. Write the one paragraph

List what they actually asked for in `posting.md`, three or four concrete things:
a method, a dataset, a tool, a policy area. Then write two or three sentences that
could not have been written about any other employer, and move them into the FIT
block in `letter.tex`.

If you cannot write that paragraph from the posting, the role is probably not a
fit. That is useful information rather than a failure.

The rest of `letter.tex` is already true and stays as it is. Compile with
`pdflatex` locally or on Overleaf. There is no LaTeX in this repo's tooling, so
the workflow produces sources rather than PDFs.

### 4. Send, then record it

```bash
python3 apply/track.py sent frontier
```

That stamps the send date and schedules a nudge twelve days out. Ids can be
shortened to any unique prefix, and a unique employer name works too.

### 5. Check what is owed

```bash
python3 apply/track.py due
```

Two things come back: applications that have been silent long enough to deserve a
follow-up, and deadlines closing within a fortnight that are still unsent. Run it
at the start of a working session. It is the part of the process that people drop,
and it is the part that produces replies.

## Commands

| Command | What it does |
|---|---|
| `python3 apply/new.py ...` | Scaffold an application and add the tracker row |
| `python3 apply/new.py --cv <path>` | Same, overriding the CV the track would pick |
| `python3 apply/track.py list` | Open applications |
| `python3 apply/track.py list --all` | Including closed and rejected |
| `python3 apply/track.py due` | Follow-ups owed, deadlines closing |
| `python3 apply/track.py sent <id>` | Mark sent, schedule the nudge |
| `python3 apply/track.py set <id> <status>` | Move it along |
| `python3 apply/track.py note <id> "text"` | Append a dated note |
| `python3 apply/track.py summary` | Counts and reply rate |

Statuses run `draft`, `sent`, `replied`, `interview`, `offer`, `rejected`,
`closed`. The first four count as open.

## Where things live

```
apply/
├── new.py              scaffold an application
├── track.py            read and update the tracker
├── _tracker.py         shared state, the only thing that touches the CSV
├── tracker.csv         one row per application, the single source of truth
├── templates/
│   ├── posting.md      qualification checklist and posting record
│   ├── letter-en.tex   English motivation letter
│   └── letter-de.tex   German Anschreiben
└── applications/
    └── <employer-role>/
        ├── posting.md
        └── letter.tex
```

The tracker is a CSV rather than a markdown table so that git diffs it row by row,
a spreadsheet can open it, and nothing has to be reformatted by hand. It is the
single source of truth. Both scripts read and write it through `_tracker.py`.

## Where Claude fits

Steps 1 to 3 are the ones worth handing over. Paste a posting and ask for the
scaffold plus a draft fit paragraph, and the qualification check comes back with
it. Ask for the Gmail draft too, and it lands in the mailbox labelled
**Applications**, ready to review.

Sending stays manual on purpose. Nothing should go out that you have not read.

## Tuning

Both numbers sit at the top of `_tracker.py`. `FOLLOWUP_DAYS` is twelve, and
`DEADLINE_WARNING_DAYS` is fourteen. Change them there and both scripts follow.
