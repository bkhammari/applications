# Context for Claude

This file loads automatically in any future Claude Code session in this repo. For a
Claude.ai chat, paste or upload it at the start.

It exists so that a new session does not re-derive what is already settled, repeat
research already done, or re-litigate decisions already made.

_Written 9 September 2026, updated the same evening after the first replies came in._

## Who this is

**Baha Khammari**, b.e.khammari@gmail.com, +49 1520 9016956, based in Düsseldorf.

M.Sc. Economics, University of Cologne, **graduating September 2026**, thesis
submitted. Available from October 2026. **Do not write that credits are
outstanding.** It was on the CV until 16 September and he asked for it removed. The
EU ETS seminar paper is a subject he can cite, not a gap to flag. M.Sc.
grade 1.6, B.Sc. 1.6, top 5 percent of cohort and Dean's List. German scale, 1.0 is
best.

**Master's thesis, graded 1.0.** *How Equal is Equal Opportunity? Gender, Ethnic and
Regional Disparities in Labor Market Outcomes of Higher Education Policies in
Brazil.* Callaway and Sant'Anna (2021) heterogeneity-robust staggered DiD with
doubly-robust inference, on roughly 5 million RAIS linked employer-employee
observations across 558 microregions, 2005 to 2019, built in R through BigQuery.
Headline result: a non-monotonic dose-response, +3.04 percent in low-exposure
regions, where naive TWFE returns -0.65 percent and reverses the sign. Supervised
by Prof. Pia Pinger with Anna Person, M.Sc. doing the day-to-day supervision.

Before the master's, two years at **PwC Germany, Assurance Solutions**, audit and
advanced Excel work. Erasmus semester at **RSM Rotterdam**, autumn 2024.

**Do not write VBA anywhere.** It was on the CV until 16 September 2026 and it was
wrong. He is very good in Excel and did not build VBA tools. Corrected across every
file. Claim advanced Excel, nothing more.

Languages: German native, Tunisian Arabic native, English C1 (IELTS 8.0), French
B1 (DELF), Italian A2. Parents are from Tunisia. He holds EU citizenship, inferred
reliably from having registered for the EPSO AD5 competition.

**No reference letters confirmed. No research-assistant experience.** Both are real
gaps and shape everything below.

## Writing rules, non-negotiable

He has asked for these repeatedly. Violating them is the fastest way to produce
work he will reject.

- **No em dashes. No narrative semicolons.** Use full stops or restructure.
- No inflated significance framing, no "broader implications" inflation
- No editorialising participial clauses, no formulaic conjunctive openers
- No negative parallelism ("not X, but Y" as a tic), no vague attribution
- No throat-clearing openers
- No bolded key-term-plus-colon bullets, except in genuine reference tables
- Vary sentence length

These come from the `econometric-scholar-style` skill, anti-AI-tells section. A
`grep -n "—\|–\|;"` over changed files before committing catches most of it.

Spelling: **British** in general documents, **American** in the Bonn-specific
documents (labor, subsidizing). This was a deliberate instruction, not drift.

**Academic emails are very short.** Four or five lines. Instructed on 10 September
after a draft to Anna Person ran long. Where there is a conversation history, use
it: no re-introducing himself, no restating the thesis, no attaching documents the
reader already knows. Cold emails carry the thesis paragraph because the reader has
never heard of him. Replies to people who know him do not.

**No Profil block on a German CV.** Decided 16 September. The classic Lebenslauf
runs Ausbildung, Berufserfahrung, Kenntnisse and nothing else, and for a
Bundesunternehmen the conservative form is the safe one. A Kurzprofil is not
unknown in German CVs, it is just a consulting and industry habit rather than a
convention, so leave it out. Anything the profile was carrying, such as
availability, moves into the relevant entry. English CVs keep their Profile block,
which is standard there.

**English CVs carry a role-aligned qualifications block.** Added 16 September. One
sentence of profile, then at most five lines mapping the posting's stated
requirements onto evidence, in the posting's own order and words. The test is a
ten-second scan by a recruiter who is not an economist. `\begin{cvquals}` and
`\cvqual` are in the class. **German CVs get neither this nor a Profil**, for the
same reason: the Anschreiben is mandatory in Germany and already does the job.

**Sent files are named `cv_<firm>_khammari.pdf`.** His format, given on 16
September. German letters are `anschreiben_<firm>_khammari.pdf`, English ones
`letter_<firm>_khammari.pdf`. `build.py` renames after every compile, since
pdflatex always writes `<source>.pdf`. The sources stay `cv.tex` and `letter.tex`
in every folder. `<firm>` comes from the tracker's `firm` column, or the first word
of the employer when that column is blank, and `python3 apply/track.py firm <id>
<word>` fixes the cases where the first word is wrong, such as Deutsche Bundesbank
or European Central Bank. The base CVs are `cv/academic/cv_academic_khammari.tex`
and `cv/professional/cv_professional_khammari.tex`.

**PwC leads Berufserfahrung, and the retail job sits under its own heading.** He
asked for PwC first on 16 September, after I had put the current job on top for
strict antichronology. A separate **Nebentätigkeit** section does both: PwC is the
first thing read, and nothing looks out of order, because each section is in order
within itself.

**Claims stay checkable.** From a hiring manager's checklist he passed on 16
September. "Eigenständige Durchführung von Jahresabschlussprüfungen" came out,
because an intern does not run an audit alone and a reader who knows the sector
discounts the whole page over one such line. Same lesson as the VBA claim. Education may lead
while the degree is fresh, but it must not crowd the page: RSM and the Abitur are
one line each with no bullets. Whatever skills a posting names go in **both** the
CV and the letter, in the posting's words. Full list in
[`apply/README.md`](apply/README.md).

**What he actually did at PwC.** Told on 17 September. He worked the **same large
audit mandate in two consecutive years**, and supported several smaller
engagements for documentation. The repeat is the point, because the team put him
back on that mandate the following year.

**Audit clients are never named.** Not on a CV, not in a letter, not in an email.
He said so, and it is a confidentiality question rather than a style one. **He told
me which client it was and that name is deliberately not written down here, because
this repository is public.** If a future session needs it, ask him. The wording
that carries the fact without it is *zwei aufeinanderfolgende
Jahresabschlussprüfungen desselben Mandanten, dazu Zuarbeit und
Prüfungsdokumentation bei mehreren kleineren Mandaten.*

**Still missing, and only he can supply it:** how large the engagement team was,
how many reports he worked on, whether anything he built saved measurable time.
Numbers must not be invented.

**Destructive actions in Gmail need his say-so first.** Three drafts were deleted on
10 September without asking. They were verified duplicates and recoverable from
Trash, but the point stands: show the list, then wait.

## How he works

Direct, fast-moving, time-pressed. He says so plainly: "time is running out and
I'm really desperate." He wants finished artefacts, not options. He corrects
things bluntly and expects the correction absorbed without ceremony.

Verify before asserting. He has twice supplied information that turned out to be
wrong (a deadline he thought had passed, a reply he thought he had received), and
in both cases checking was the right move and he accepted the correction.

## Current state, 9 September 2026

### Decided, do not reopen

- **Düsseldorf HHU is dropped.** Not a missed deadline, a choice. Drafts kept in
  `phd/duesseldorf/` in case it is revisited.
- **Geography for jobs:** commuting range of Cologne, Düsseldorf and Frankfurt.
  Frankfurt counts because Köln Hbf to Frankfurt Flughafen is about an hour on the
  high-speed line. Luxembourg and Brussels are out.
- **Geography for PhD:** Germany's neighbours, plus Spain and Italy, pay as a
  tiebreaker.
- **Priority order:** salaried E13 research posts and graduate schemes first,
  internships only as a fallback.
- **No GRE.** Decided 10 September 2026. This closes the Bonn BGSE programme, UPF
  and the Barcelona School of Economics. Do not propose the GRE again.
- **Bonn is out**, decided 10 September 2026, and now confirmed from the inside.
  Schiprowski replied to the direct chair enquiry on 10 September: *"In Bonn, all
  PhD admissions have to go through our graduate school, the BGSE... The next
  deadline is going to be beginning 2027."* Boneva said the same a day earlier. So
  Bonn genuinely routes chair positions through the BGSE too, which makes it an
  exception to the two-channel rule below, and the GRE requirement closes it. He
  was right to drop it. The one thread still open is **Qaim and Parlasca, who sit
  in agricultural economics rather than the economics department**, and they
  answered on 10 September: no new PhDs on the project. So every Bonn door tested
  is shut. Only Dohmen has not replied.

### The single most important insight of the session

**German academic hiring has two separate channels, and he had only been asking
about one.** Structured graduate programmes (BGSE, CGS, RGS, CDSE) run central
intake on fixed deadlines, which is why every professor pointed him there. Chair
positions are a different thing entirely: a professor holds a budget line, fills it
alone as *wissenschaftliche/r Mitarbeiter/in* at TV-L E13, and the doctorate runs
alongside as an Individualpromotion. No committee, no annual cycle, can start in
weeks, pays 2,700 to 3,000 gross at 65 percent.

The email has to ask a different question. Not "would you supervise me" (answer:
the graduate school) but **"do you have, or do you expect, a funded position"**,
which is answerable in one line. Full write-up in
[`phd/e13-direct.md`](phd/e13-direct.md), template in
[`phd/templates/email-e13-inquiry.md`](phd/templates/email-e13-inquiry.md).

### Sent 8 September 2026, nine emails

| To | What | Outcome |
|---|---|---|
| Anna Person + Prof. Pinger | Reference reply, asks for a general letter or referee status | **Pinger replied "Sounds good!" on 9 Sep. The arrangement is agreed** |
| Prof. Boneva, Bonn | Follow-up after eight weeks | **Replied 9 Sep.** Apply to BGSE, several Bonn professors work in these areas, meetings follow admission |
| Prof. Klagge, Bonn | TRR 228 phase three | **Declined 9 Sep**, no capacity for another PhD student |
| ROA Maastricht | Who to approach | **Tim Huijts, PhD coordinator, replied 9 Sep.** No funded openings now, but he is forwarding the message to Cörvers, Haelermans and Fouarge |
| Prof. Dohmen, Bonn | E13 enquiry, Bonn and Maastricht | No reply yet |
| Prof. Schiprowski, Bonn | E13 enquiry | **Declined 10 Sep.** All Bonn PhD admissions go through the BGSE, next deadline early 2027 |
| Qaim + Parlasca, Bonn | C08 Job Futures | **Declined 10 Sep.** Parlasca: "we will not hire any new PhDs in this project" |
| Prof. Siegloch, Cologne | Cold email | No reply yet |
| Frontier Economics | 2027 graduate intake | No reply yet |

**Six replies on nine emails inside 48 hours.** Every one was a clear answer rather
than silence, which is the direct question working exactly as intended. The earlier
diffuse emails got eight weeks of nothing.

The answers are mostly no, and that is worth reading correctly. He now knows where
Bonn stands in two days rather than in January, and the effort can move. Four of
five Bonn contacts have answered and all four were no, so **Bonn is fully closed**
except for Dohmen, who has not replied. The pipeline is now thin, and volume is the
only thing that fixes that.

### Drafted in Gmail, not sent

All labelled **PhD** except Frontier, labelled **Applications**.

| To | Address | Note |
|---|---|---|
| Prof. Sonja Settele | settele@wiso.uni-koeln.de | Asks for a CEBI introduction and about the second reference letter. **Send this one** |
| Prof. Johannes Wohlfart | wohlfart@wiso.uni-koeln.de | Address unverified. Neisser recommended him in July, never contacted |
| Anna Person + Pinger | anna.person127@gmail.com | **Still unsent as of 10 Sep.** Anna has never received the CV or transcript. The August attachments went to Pinger alone, and Anna was only copied on Pinger's reply, which carries no attachments. She cannot write the letter until this goes |


| Jun.-Prof. van Maarseveen | vanmaarseveen@wiso.uni-koeln.de | **On hold.** It asserts he never replied, which the mailbox confirms. Rewrite if a reply surfaces elsewhere |

### Open questions he has not answered

1. **Did the Blue Book application go in before 4 September 2026?**
2. Whether to run the LinkedIn and Indeed search. He raised it himself on 10
   September, so the earlier refusal is superseded, but confirm before running it.

The GRE question is now answered. He does not want to sit it, which is recorded
above as a decision.

## Which referee to name

Asked on 10 September. The answer splits by context and the split matters.

**PhD programme applications: name Pinger.** Most programmes require a professor,
and Anna Person is an M.Sc. and a PhD candidate. The agreed arrangement covers this,
since Anna writes the substance and Pinger sends it under her name.

**Jobs, internships, consulting: name Anna.** No employer requires a professorial
title, and she is the stronger reference on the merits. She supervised him day to
day for six months and graded the thesis 1.0.

The reason this is not symmetric: **Pinger has never met him.** She said as much
when she suggested Anna write the letter, because Anna "knows you from personal
interaction". A written letter signed by Pinger is fine, since Anna supplies the
content. A phone call to Pinger from an employer would go badly.

So: Pinger for anything that needs a professor's signature, Anna for anything where
someone might actually pick up the phone. Never list Anna where the form says
professor. The CV currently says "References available upon request", which is the
right default until something is confirmed.

## Facts verified this session

Recorded so they are not re-researched, and because two were corrections of my own
errors.

**People.** Sonja Settele is an Associate Professor at **Cologne**, ECONtribute
faculty, senior research fellow at the MPI Bonn, and an **external member** of CEBI
Copenhagen where she was previously Assistant Professor. She is not at Copenhagen.
She replied to a cold email in July and **met Baha in person on 21 July 2026**,
which makes her the answer to Pinger's question about a second letter writer.

**Thomas Dohmen holds chairs at both Bonn and Maastricht.** Applied Microeconomics
at Bonn, **Professor of Education and the Labour Market** at Maastricht SBE, and
**Chairman of ROA's Scientific Advisory Board**, plus ECONtribute spokesperson. One
email reaches Bonn, Maastricht and ROA.

**Carina Neisser's recommendation, 17 July 2026:** Siegloch, Pinger, Settele,
Wohlfart. Three are now in motion. Wohlfart sat unused for eight weeks.

**Email address patterns.** Cologne is consistent: `lastname@wiso.uni-koeln.de`.
**Bonn is not**: `t.dohmen@`, `tboneva@`, `amelie.schiprowski@`, `klagge@`,
`mqaim@`, `parlasca@`. Always verify a Bonn address on the faculty page. Department
fallback: `econpr@uni-bonn.de`.

**Two CRCs just refunded, both staffing now.**

- **CRC TR 224 EPoS**, Bonn and Mannheim. Research Area A is *equality of
  opportunity*. Extended four years from 1 January 2026, about €12 million.
- **CRC TRR 228 Future Rural Africa**, Bonn and Cologne. Third phase 2026 to 2029,
  about €13.1 million. Britta Klagge takes over as spokesperson from Michael Bollig.
  Field sites are **Kenya, Tanzania, Namibia, Zambia**, not North Africa. Its
  economics sub-project is **C08 Job Futures** (Qaim, Parlasca), which uses
  household, individual and employer data on jobs, income and inequality. That is
  the fit, not the spokespersons.

**Pay figures.** ECB Graduate Programme about €4,982 a month, two-year contract,
annual September cohorts, the 2026 one advertised around February. ECB traineeship
€1,170. Bundesbank Forschungszentrum research assistant, E13, recently advertised
at roughly €32,900 to €47,500, often a two-year 50 percent contract. PhD stipends
by country are tabulated in [`phd/geography-and-pay.md`](phd/geography-and-pay.md).

**Frontier Economics.** Four open roles worldwide on 8 September 2026, none
reachable. The Amsterdam Consultant role needs C2 Dutch and several years of
experience. Their Graduate Economic Analyst programme accepts "Germany 2.0 or
better" plus a master's, wants R or Stata and advanced Excel, and requires fluency
in the language of the office, which is what makes **Cologne and Berlin** work and
Amsterdam not.

**Maastricht GSBE expects a supervisor and funded position to be identified before
applying.** So the portal is paperwork that follows the approach. Rolling review
through May 2027, Studielink opens 1 October 2026. Central address
`gsbe-phd-application@maastrichtuniversity.nl`.

**A Dutch PhD is an advertised job, not a programme intake.** Verified 17
September. Every funded Maastricht PhD is published on **AcademicTransfer** and the
UM job site and filled by applying to it, with no committee cycle. Same shape as
the German E13 channel, and it pays more than either alternative: the last
economics vacancy advertised **€3,059 to €3,881 gross** over four years. Maastricht
had been treated here as a programme problem when half of it is a job problem.
**MILE runs an annual department-wide round called Inequality Dynamics**, which
closed 30 April 2025 and 1 February 2026, so expect February to April 2027. The
theme is the master's thesis restated. Nothing was open in economics on 17
September. Full detail in
[`phd/international/maastricht.md`](phd/international/maastricht.md).

**UNU-MERIT dates, confirmed rather than inferred.** Call **opens 1 November 2026,
closes 15 February 2027**, selection March and April, starts September 2027.
Fellowship **€1,650 net a month** for four years, not the roughly €1,700 recorded
earlier, and net rather than gross. No GRE. **The number of reference letters is
not stated on their pages**, so the earlier "one letter" claim is unverified. Ask
`phdprogramme@merit.unu.edu`, because one versus two changes whether Settele has to
be asked in time.

**Maastricht uses two email patterns, not one.** `t.huijts@` and `b.golsteyn@` are
initial.lastname, `julian.ashwin@` and `lex.borghans@` are firstname.lastname, all
at `maastrichtuniversity.nl`. The earlier rule in this repo inferred one pattern
from one address and would have sent Borghans's mail to a dead box. UM staff pages
render in JavaScript, so a plain fetch returns nothing and verification needs a
browser.

## Bugs fixed, do not reintroduce

`cv/shared/OpenCV.cls` used to load `\RequirePackage[ngerman]{babel}`, which clashed
with `\usepackage[english]{babel}` in the academic CV and made it **fail to compile
entirely**. It also never loaded `amsmath`, so the `\text{TWFE}` in the thesis
bullet was an undefined control sequence. Both fixed: babel is now declared per CV,
and amsmath is loaded in the class. The English CV had never compiled before this.

LaTeX needs `tex-gyre` and `lmodern` on top of the usual texlive packages. The
install line is in the docstring of `apply/build.py`.

`apply/build.py` decoded pdflatex output strictly as UTF-8 and crashed on the
first German document, since pdflatex emits Latin-1 for umlauts. Fixed with
`errors="replace"`.

The German letter template used **scrlttr2**, which reserves a third of the page
for fold marks, a deep reference line and a footer it never prints, and would not
come down to one page. The GIZ letter sets its geometry directly on `article`
instead. Do that for the next German letter rather than fighting the class again.

`OpenCV.cls` now takes options: `compact` for a one-page CV, `serif` for Latin
Modern roman, `noicons` for a machine-readable contact line, `mono` for black
instead of blue. Header fields are set with `\cvname` and friends and printed by
`\cvheader`, so the header block is no longer copy-pasted per document. **The old
"ATS-Optimised" claim was false where it mattered**: FontAwesome glyphs made the
contact line extract as `Q b.e.khammari@gmail.com ... ¯`. Use `noicons` wherever a
system parses the CV.

**Single column, black and white, for anything commercial or public-sector.** A
recruiter rule he sent on 16 September, and it matches everything else recruiters
say about screening at volume. The class has never had a sidebar or a two-column
split, so only the colour needed taking out, which is what `mono` does. Use
`[compact,mono]` on German and industry CVs, `[serif,compact,mono]` on consulting
ones. Colour stays on the academic CV, which one person reads slowly.

**The CV is ragged right, not justified.** He said on 16 September that it was
hard to read and he was right. Justified setting on a 95-character measure full of
German compounds gave stretched word spaces and a hyphenated word at the end of
most lines: Mikroregio-nen, verfüg-bar, Jahresabschlussprü-fungen, Scha-bert,
Informationsveranstaltun-gen. The class now sets `\RaggedRight`, raises
`\hyphenpenalty` and loads `microtype`, and the leading and the gaps between
entries went up. **A German letter keeps Blocksatz**, which is the convention
there, and pays for it with `microtype` plus a `\hyphenation` exception list.
Check a rebuild by rendering it, not by reading the source. Full reasoning in
[`apply/README.md`](apply/README.md).

Two habits that came out of the same pass. **Bold has to be scarce to mean
anything**: on the German CV it is now the name, the section headings, the
employers, the thesis grade and the start date, and nothing else. **The letter
uses the CV's typeface**, because they arrive together.

**`github.com/bkhammari` is off the CVs.** Verified public on 16 September, and
the repository it shows is this one: the tracker, the replies including every
rejection, and the reasoning about referees. The `\cvgithub` line is commented out
in `cv/academic/cv_academic_khammari.tex` and in the Frontier copy rather than deleted. Put
it back when there is a repository worth sending a reader to, such as thesis
replication code. **Whether to make this repo private is his call and he has not
been asked yet.**

## The tooling

```
apply/new.py     scaffold an application: posting record, tuned CV, letter, tracker row
apply/track.py   list / due / sent / set / note / summary
apply/build.py   compile the LaTeX to PDF
apply/tracker.csv  one row per application, the single source of truth
```

Full loop in [`apply/README.md`](apply/README.md). Two blocks get written per
application: the **Profile** at the top of the CV, and the **fit paragraph** in the
letter. Everything else is already true and reusable.

`track.py due` is the part that matters, because it surfaces follow-ups owed and
deadlines closing. Following up is the step people drop and the step that produces
replies.

**Economic consulting has its own track** mapping to the academic CV, not the German
professional one. Those firms hire economists to run econometrics and their process
runs in English.

**Sending always stays manual.** Draft into Gmail, never send.

## Which Claude to use for what

Asked twice, so recorded. The split is about what each surface can touch, not
about capability.

**This one, Claude Code on the repo.** It holds the tracker, the LaTeX and PDF
build, git, and Gmail. Use it for anything that produces or changes an artefact:
batches of applications, tuned CVs, drafted emails, research that has to persist.
It is the system of record.

**A chat session, Cowork or claude.ai or the desktop app.** Upload `CLAUDE.md` at
the start and it has the full picture. Use it for the things that happen away from
the keyboard: triaging a reply on a phone, judging whether a posting is worth
applying to, preparing for an interview, thinking out loud about a decision. It
cannot touch the repo, so nothing decided there is real until it comes back here.

**The bridge is this file plus GitHub.** That is the whole integration and it is
already built. Do not build a dashboard, a website or an app for this. The
bottleneck has never been tooling.

**One thing that belongs in a separate session entirely:** the seminar paper on
the EU ETS. It has nothing to do with the job search and it is not in this repo, so
give it its own chat. In applications it is a subject he can cite, never a gap.

## Where things are

- `apply/` the workflow and per-application folders
- `phd/` outreach hub. `README.md` is the master tracker with per-target status
- `phd/e13-direct.md` the two-channel explanation and where positions actually are
- `phd/geography-and-pay.md` PhD destinations ranked by pay
- `bridge/` paid interim positions. `private-sector.md` covers finance and consulting
- `eu/` EPSO AD5 and Blue Book, with mock exams and an abstract-reasoning trainer
- `cv/`, `letters/`, `research/`, `scholarships/`, `dashboards/`

Work happens on the branch `claude/sleepy-keller-gissaq`. Commit and push as you go.
