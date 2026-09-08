# Application workflow

Posting in, tailored application out, tracked until it closes. Built so that the
only two blocks you write per application are the CV profile and the letter's fit
paragraph. Everything else already exists.

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

That creates `apply/applications/<slug>/` holding `posting.md`, `letter.tex` and a
`cv.tex` copied in for this application, and adds a row to `tracker.csv` with
status `draft`. Nothing is sent.

The CV is copied rather than referenced, because it is worth tuning per
application. The relative `\documentclass` path is rewritten so the copy still
finds `cv/shared/OpenCV`, and the German CV's `\input` sections are copied
alongside it. Pass `--shared-cv` to skip the copy and just record the canonical
path.

`--lang` picks the letter language and `--contact` sets the salutation, including
the gendered German form when you pass a name starting with Herr or Frau.

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

### 3. Tune the CV

One block does most of the work: the `Profile` at the top, three or four lines
aimed at this employer. It is to the CV what the fit paragraph is to the letter.

Beyond that, the tuning worth doing is reordering rather than rewriting. Put the
skill they named first, label the grades with the scale when the posting states a
threshold, and cut whatever is noise for this reader. The Frontier application in
`apply/applications/` carries a comment block at the top of `cv.tex` recording
exactly what changed and why, which is worth copying as a habit. Being able to see
the reasoning six weeks later is what stops the tuning becoming superstition.

### 4. Write the one paragraph

List what they actually asked for in `posting.md`, three or four concrete things:
a method, a dataset, a tool, a policy area. Then write two or three sentences that
could not have been written about any other employer, and move them into the FIT
block in `letter.tex`.

If you cannot write that paragraph from the posting, the role is probably not a
fit. That is useful information rather than a failure.

The rest of `letter.tex` is already true and stays as it is.

Then build the PDFs:

```bash
python3 apply/build.py frontier        # one application
python3 apply/build.py --all --clean   # everything open, aux files removed
```

It runs pdflatex twice on `cv.tex` and `letter.tex`, reports the page count, and
prints the first real error rather than the whole log when something fails. The
install line for a machine without LaTeX is in the file's docstring. `tex-gyre`
and `lmodern` are the two easy ones to miss, and the CV class needs both.

### 5. Send, then record it

```bash
python3 apply/track.py sent frontier
```

That stamps the send date and schedules a nudge twelve days out. Ids can be
shortened to any unique prefix, and a unique employer name works too.

### 6. Check what is owed

```bash
python3 apply/track.py due
```

Two things come back: applications that have been silent long enough to deserve a
follow-up, and deadlines closing within a fortnight that are still unsent. Run it
at the start of a working session. It is the part of the process that people drop,
and it is the part that produces replies.

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
| `python3 apply/build.py <id>` | Compile that application's CV and letter |
| `python3 apply/build.py --all --clean` | Compile everything open, tidy up after |

Statuses run `draft`, `sent`, `replied`, `interview`, `offer`, `rejected`,
`closed`. The first four count as open.

## Where things live

```
apply/
├── new.py              scaffold an application
├── track.py            read and update the tracker
├── build.py            compile the LaTeX to PDF
├── _tracker.py         shared state, the only thing that touches the CSV
├── tracker.csv         one row per application, the single source of truth
├── templates/
│   ├── posting.md      qualification checklist and posting record
│   ├── letter-en.tex   English motivation letter
│   └── letter-de.tex   German Anschreiben
└── applications/
    └── <employer-role>/
        ├── posting.md   the posting, the qualification check, the research
        ├── cv.tex       copied in and tuned for this application
        ├── letter.tex   boilerplate plus the one fit paragraph
        └── *.pdf        what you actually send
```

The tracker is a CSV rather than a markdown table so that git diffs it row by row,
a spreadsheet can open it, and nothing has to be reformatted by hand. It is the
single source of truth. Every script reaches it through `_tracker.py`.

## Where Claude fits

Steps 1 to 4 are the ones worth handing over. Paste a posting and ask for the
scaffold, the qualification check, the CV tuning and a draft fit paragraph. Ask
for the Gmail draft too, and it lands in the mailbox labelled **Applications**,
ready to review.

Sending stays manual on purpose. Nothing should go out that you have not read.

## Tuning

Both numbers sit at the top of `_tracker.py`. `FOLLOWUP_DAYS` is twelve, and
`DEADLINE_WARNING_DAYS` is fourteen. Change them there and both scripts follow.
