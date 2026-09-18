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

**The thirty-second test for an academic vacancy.** Three postings in September
survived a surface read and died on the requirement list, so read these three lines
first and skip the salary until they pass.

1. **Which faculty is it?** Economics, econometrics or a business school. A Utrecht
   land-use post that looked like a fit sat in the Faculty of Geosciences.
2. **Is an economics MSc on their list of accepted degrees?** If the list runs
   Geoinformatics, Computer Science, Quantitative Geography and Environmental
   Science, the answer is no and "or a related discipline" does not stretch that far.
3. **Do they name a method he has not used?** Hands-on RCT implementation, spatial
   optimisation, structural estimation and lab experiments all take years to
   acquire. A project position inherits its requirements from its grant, so these
   are not negotiable.

It passes when the named methods are difference-in-differences, panel data, event
studies, instrumental variables, policy evaluation or administrative register data,
and the subject is labour, education, inequality or public policy.

**Two false signals, both of which have cost time.** A **shared country** is not a
fit signal: the thesis is on Brazilian labour market returns and the Utrecht post is
on Brazilian land use, and they have nothing else in common. And **558
microregions** reads as spatial work but is a regional panel, where geography is an
index rather than an object of analysis. There is no GIS, no raster data and no
spatial econometrics anywhere in the thesis.

If a role fails, mark it and move on:

```bash
python3 apply/track.py set frontier closed
```

### 3. Tune the CV

**On an English CV, two blocks at the top do the work.** A one-sentence `Profile`,
then a `Qualifications for this role` block: one line per requirement the posting
states, in their order and their words, five at most.

```latex
\section*{Qualifications for this role}
\begin{cvquals}
\cvqual{Economics degree, Germany 2.0 or better.}{M.Sc.\ 1.6 and B.Sc.\ 1.6, Cologne.}
\cvqual{Advanced Excel, and R or Stata.}{R for the thesis across five million records.}
\end{cvquals}
```

The test is whether a recruiter who is not an economist can tick every requirement
in ten seconds without reading further down the page. See the Frontier application
for a worked example against a posting that states five.

The block also earns its space twice, because once it carries the headline the
sections below can stop repeating themselves. On the Frontier CV it replaced the
whole Languages section and a thesis bullet.

**On a German CV, do neither.** The classic Lebenslauf has no Kurzprofil and no
qualifications block, and the Anschreiben is mandatory there, so the letter already
does this job. An American-style block on a German public-sector application reads
as foreign. Move whatever the profile was carrying, availability for instance, into
the entry it belongs to.

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

**It then renames the PDFs to what they are sent as**, so the GIZ folder holds
`cv_giz_khammari.pdf` and `anschreiben_giz_khammari.pdf` rather than `cv.pdf` and
`letter.pdf`. See the naming section below.

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

## The CV class

All CVs use `cv/shared/OpenCV.cls`. Four options, and the first two replace blocks
that used to be pasted into every tuned copy by hand.

| Option | What it does |
|---|---|
| `compact` | Tighter margins and single line spacing, for a one-page CV |
| `serif` | Latin Modern roman instead of the sans default |
| `noicons` | Plain-text contact line with no FontAwesome glyphs |
| `mono` | Headings, rules and links in black instead of blue |

```latex
\documentclass[serif,compact,mono]{../../../cv/shared/OpenCV}
\usepackage[english]{babel}

\cvname{Baha Khammari}
\cvlocation{D\"usseldorf, Germany}
\cvemail{b.e.khammari@gmail.com}
\cvphone{+49\,1520\,9016956}
\cvlinkedin{linkedin.com/in/baha-khammari}

\begin{document}
\cvheader
```

`\cvheader` skips whatever you leave unset, so the same block works for a CV with
GitHub and one without. **Keep it to four items.** A fifth wraps the contact block
onto a second line at any sensible size. The separator is a discretionary, so a
block that does wrap breaks between items and never leaves a dangling dot, but one
line still reads better than two.

The GitHub field is currently unset everywhere. `github.com/bkhammari` is public
and the repository it shows is this one, the job search itself. Set it again when
there is something worth sending a reader to.

**Use `noicons` whenever a machine reads the file first.** The class loads
`glyphtounicode` so text extracts cleanly, but the FontAwesome glyphs defeat it.
Extract the contact line from an icon build and it comes back as

```
Düsseldorf · Q b.e.khammari@gmail.com · +49 1520 9016956 · ¯
```

The envelope becomes `Q`, LinkedIn becomes a macron, the phone disappears. A
parser sees a stray letter glued to the email address. With `noicons` the same
line extracts as plain text. Icons stay the default because they look better to a
human, so the choice is: who reads this first, a person or a system.

**Use `mono` for anything commercial or public-sector.** Recruiters screening at
volume report that colour and extra columns slow them down, because the eye has to
decide where to go next instead of running straight down the page. The class has
never had a sidebar or a two-column split, and `mono` takes the last colour out.
Keep the blue on an academic CV, which one person reads slowly.

## Typography, and why the CV stopped being justified

Changed on 16 September after reading a build rather than the source. The German
CV was setting flush left and right on a narrow measure, and paying for the flush
right edge with stretched word spaces and a broken word at the end of most lines.
One page carried Mikroregio-nen, verfüg-bar, Jahresabschlussprü-fungen, Scha-bert
and Informationsveranstaltun-gen. German compounds are long and the measure is
about 95 characters, so there is nothing for TeX to do but hyphenate or stretch.

The class now sets ragged right, raises `\hyphenpenalty`, and loads `microtype`
for protrusion and font expansion. Same space spent, on a ragged margin instead of
on visible holes in the lines. Two hyphenations survive on the German CV and both
are correct. Leading and the gaps between entries went up at the same time, which
is what actually makes a dense page readable.

**Academic documents are a separate class of thing.** Statements of intent,
research statements, the proposal and the academic CV are set in **Latin Modern
roman on the default `article` class**, justified, with wider margins. That is the
LaTeX look an economist expects on a working paper, and it is what the reader of a
doctoral application is used to. English justifies far better than German, so
Blocksatz costs almost nothing there. Everything in `research/` and
`letters/academic/` already worked this way. **The sans face is for German letters
and the German CV**, which are read by an HR portal rather than by a department.

**A German letter keeps Blocksatz**, because that is the convention there, so the
GIZ letter is justified and loads `microtype` to pay for it. It also carries a
`\hyphenation` list. Babel hyphenates by German rules, which is wrong for English
terms in the text, and it had produced Direk-tinvestitionen, where the compound
seam is behind *Direkt*. Anything wrong on the page is worth an exception entry.

**The letter uses the same typeface as the CV.** They arrive together and a serif
letter next to a sans CV is the first thing a reader notices.

## What the files are called

A recruiter downloads your attachments into a folder next to forty other people's.
`cv.pdf` is invisible there, `Lebenslauf_final_v3.pdf` is worse, and neither says
whose it is once it leaves the email it arrived in.

```
cv_<firm>_khammari.pdf
anschreiben_<firm>_khammari.pdf      German applications
letter_<firm>_khammari.pdf           English applications
```

`build.py` applies this after every compile, because pdflatex always writes
`<source>.pdf` and the rename has to happen each time. The sources keep their plain
names, so `cv.tex` and `letter.tex` are in the same place in every folder and
`new.py` has nothing to special-case.

`<firm>` comes from the tracker's **`firm`** column when it is set, otherwise from
the first word of the employer. The column exists because the first word is wrong
often enough to matter. Deutsche Bundesbank would give `deutsche` and European
Central Bank would give `european`, so set `firm` to `bundesbank` or `ecb` and the
filename comes out right.

```bash
python3 apply/track.py firm <id> bundesbank
```

The two base CVs follow the same shape, `cv_academic_khammari.tex` and
`cv_professional_khammari.tex`, so that compiling one by hand also produces a file
that is ready to attach.

## A hiring manager's checklist, and what it changed

From a COO who screens CVs, passed on 16 September. Most of it was already
satisfied. These are the things that were not.

**Order.** The checklist says the most recent job goes on top. PwC ended in July
2025 and Nespresso is current, but PwC is the entry worth reading first, and he
asked for it there. Both hold if the retail job gets its own **Nebentätigkeit**
heading below Berufserfahrung: PwC leads, each section is in order within itself,
and nothing looks rearranged. That is the shape in both German CVs now.

**No inflation.** "Eigenständige Durchführung von Jahresabschlussprüfungen" came
out. An intern and working student does not run an audit independently, and a
reader who knows the sector discounts the whole page when they hit one of those.
This is the same lesson as the VBA claim. What is left is checkable.

**The experience section should not be crowded out.** Ausbildung was about 60\,\%
of the German page, with the Abitur carrying its own bullet list. RSM and the
Gymnasium are now one line each with no bullets, which freed five lines. Education
still leads, because the degree is fresh and the role is research, which is the
exception the checklist itself allows.

**Put the posting's own words in both documents.** The letter already named World
Development Indicators, International Debt Statistics and the BMZ. The CV did not,
so the Kenntnisse block now says Paneldatensätze, BigQuery and verhandlungssicher,
and the letter picks up Weltbankgruppe, IWF, regionale Entwicklungsbanken and
internationale Finanzarchitektur.

**Measurable results are the gap.** Only one number in the PwC block is his own,
the 500 million balance sheet. Numbers cannot be invented here, that is the
inflation problem again, so the ones worth having have to come from him: how many
engagements, how large a team, how many reports, how much time a model saved.

**What does not transfer: the two-line summary at the top.** The checklist asks for
one and calls it a matter of taste. English CVs here have it. German CVs do not,
because the Anschreiben is mandatory in Germany and its first paragraph is that
summary. See the Profil decision in `CLAUDE.md`.

## Which CV goes with which track

| Track | CV |
|---|---|
| `academic`, `research`, `policy` | `cv/academic/cv_academic_khammari.tex`, English |
| `consulting` | `cv/academic/cv_academic_khammari.tex`, English |
| `industry` | `cv/professional/cv_professional_khammari.tex`, German |

Economic consulting has its own track rather than sitting under `industry`,
because the obvious mapping is the wrong one. Frontier, CRA, Compass Lexecon and
the rest hire economists to run econometrics, and their process runs in English.
The academic CV carries the thesis in the detail that is the actual
qualification, naming the estimator, the packages and the result, where the German
CV compresses it to a single line. It also lists advanced Excel, so nothing
commercial is given up, and it leaves out the Abitur, the Gymnasium and the retail
job, which are noise to a consultancy.

Override per application with `--cv cv/professional/cv_professional_khammari.tex` when a posting argues
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
| `python3 apply/track.py firm <id> <word>` | Fix the employer word in the filenames |
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
        ├── posting.md                 the posting, the qualification check, the research
        ├── cv.tex                     copied in and tuned for this application
        ├── letter.tex                 boilerplate plus the one fit paragraph
        ├── cv_<firm>_khammari.pdf     what you actually send
        └── anschreiben_<firm>_khammari.pdf
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
