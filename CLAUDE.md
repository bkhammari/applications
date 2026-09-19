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
B1 (DELF), Italian A2. Parents are from Tunisia.

**Citizenship, stated by him on 18 September: he holds both EU and Tunisian
citizenship.** Previously this file only inferred the EU half from the EPSO
registration. The Tunisian half matters because some programmes restrict
eligibility by country of origin. **Do not assume it qualifies him for those.**
Tunisia is a lower-middle income country, but he was schooled at the
Cecilien-Gymnasium in Düsseldorf and studied in Cologne, so a programme aimed at
applicants *from* such countries may read him as a German-educated EU citizen.
Zurich's Global Talent pre-doc is the live case. **Ask `predoc@econ.uzh.ch` rather
than assuming either way.**

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

**Load that skill before writing academic prose.** He asked for it on 18 September
and it earned its place immediately. Run against the two statements drafted that
day it caught three real things a dash-grep does not. **Negative parallelism**, in
both documents: "not merely imprecise, it had the wrong sign" and "the headline is
not the coefficient, it is that the estimator reversed the sign". **Vague
attribution** without a citable source, "my reading is that the literature is
thinner on X", which had to become a design question rather than a claim about a
literature that cannot be cited in a statement of intent. And **bolded
key-term-plus-colon list items**, which became numbered prose. The skill also asks
that **magnitude be stated separately from statistical significance**, so the
ProUni result now reads "a wage gain of 3.04 per cent, statistically
distinguishable from zero at the 10 per cent level" rather than blurring the two.

**A statement of intent says why he wants the position and what he brings. Nothing
else.** Instructed 18 September, after two drafts that did other things. His words:
*"Just tell why I am interested in this PhD position. Why? Nothing about, you know,
I tried to do this in my thesis and it was wrong and I corrected this."*

Three concrete consequences, all of which cost a rewrite to learn.

**No error narratives.** A draft had built the whole UCLouvain statement around the
two-way fixed effects sign reversal in his thesis, told as a mistake he found and
fixed. It is a genuinely good story and it is wrong for this document, because a
reader who meets a mistake in paragraph one thinks about the mistake for the rest of
the page. State the estimator and the result as a capability. The reversal is an
excellent answer to an interview question, which is a different job.

**Do not volunteer a weakness.** The same statement had named the master's
Microeconomics 3,0 before the reader could find it, on the reasoning that the
transcript travels in the same PDF. That reasoning holds in a document that is
arguing with a sceptic. A statement of intent is not. State the theory training
positively instead, Ockenfels 1,3 on strategic thinking and competition alongside
econometrics 1,3, which answers the same requirement and concedes nothing. Prepare
the honest answer for interview, in `SEND.md`, and do not lead with it.

**A checklist of persuasive arguments is not a document.** An earlier draft followed
a four-paragraph persuasive layout he supplied and produced four disconnected blocks
with no roter Faden, opening on a sentence no cold reader could parse. His reaction
was that it was incoherent. Whatever the structure, the paragraphs have to join.

**Research the document type before writing it.** Instructed 18 September: look up
guides from academic chairs or professionals for whatever is being written, rather
than composing from instinct. Doing this for the statement of intent produced three
rules that changed the draft and are worth keeping. **Open with field and direction
in the vocabulary of the field**, not with an origin story or a declaration of
passion, which no committee is persuaded by. **Keep mathematical preparation near
the centre of the document**, because it carries real weight in economics admissions
and does not belong in a closing list. And **send the clearest signal of research
ability and cut everything that is noise around it.** Sources were Chris Blattman's
2022 post on writing the statement of purpose and the economics-SOP advice
collected alongside it.

**Never assume what he wants. Ask.** Instructed 18 September, after the UCLouvain
statement said he would take up research directions 3 and 4 from the call when he
wants **1 and 2**. Nothing in the posting or the repository said which, and I chose
two and wrote them into a document going out under his name as his own research
interest. That is the worst class of error available here, because it is invisible
to him unless he reads every line. Where a document has to state a preference he
has not expressed, ask him or leave the choice out.

### The statement of purpose, consolidated from three guides

He supplied the MIT EECS Communication Lab's *Graduate School Statement of Purpose*
on 18 September and asked that the lessons be kept. Read with his own
four-paragraph brief and the Blattman advice above, the three agree more than they
disagree, and where they conflict his brief wins. What follows is the working rule
set, ordered by how much it changed the drafts.

**Wrap meaning around every experience, and use it as the transition.** This is the
MIT guide's central structural teaching and the one the drafts kept missing. An
experience is the *what*, and on its own it is a CV in prose. Meaning is the *why*
and the *so what*: why the experience mattered to his growth as a researcher, what
it says about his ability. The guide's line is worth keeping verbatim: *"A statement
of purpose is a way to make a narrative out of your CV. It is not a diary entry."*
Meaning is also what carries the reader from one paragraph to the next, so a
document with no meaning statements has no joins, which is exactly the incoherence
he objected to.

**Quantify the collaboration, not only the data.** Drafts here have been good at
quantifying datasets, five million observations, 558 microregions, 2005 to 2019, and
blind to everything the guide actually asks for. How many people were on the team.
How many reports. How many competitors for an award. Those numbers are the ones
missing from the PwC block and from the Dean's List claim, and **only he can supply
them**, which is a reason to ask rather than a reason to omit.

**Describe actions, not internal states.** The guide's own table is the test. *"My
mind was opened to the possibility of..."* against *"I collaborated with other group
members to develop a user-friendly Python wrapper for a 10,000-line Fortran
library."* Anything in the register of realising, becoming interested, growing
curious or being inspired is a diary entry and comes out.

**Open with a portrait of what drives him as a researcher, and name the research
direction.** Both guides agree and both forbid the childhood opening. The MIT
version adds a useful prompt: what would he work on if he had to start tomorrow,
and what does he picture himself doing in ten years.

**Close with two or three sentences on career interests, and say what the programme
supplies.** The current close names the ten-year goal and asserts the position is
the first step. The guide asks for the mechanism, so state what this group gives
him that he cannot get elsewhere.

**Demonstrate the match in the programme's own words.** Echo the call's vocabulary,
name the professors he would work with, and say which research directions or
projects he would pursue with each. Naming other groups at the university worth
collaborating with also counts, which is why ENERPOL is in the UCLouvain statement.

**Section headings are recommended but not free.** The MIT guide suggests explicit
titles such as Research Interests and Prior Experience, and assumes two pages.
UCLouvain caps the statement at one. On one page headings cost four lines, so this
is a per-application judgement and **his call, not an automatic yes**.

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
or European Central Bank. There are now **four base CVs**, listed under "The four base CVs" below.

### The four base CVs, settled 18 September

He asked for general, untuned copies he can keep and cut from. The split is by who
reads it, because that is what changes the order of the page.

| File | Language | Reader | Class options |
|---|---|---|---|
| `cv/academic/cv_academic_khammari.tex` | English | PhD programmes, chairs, research posts | `[serif]`, colour, icons |
| `cv/institutional/cv_institutional_khammari.tex` | English | ECB, Bundesbank, EU institutions, GIZ, DEval, OECD | `[compact,mono,noicons]` |
| `cv/private/cv_private_khammari.tex` | English | Economic consulting, banks, industry, Big Four | `[compact,mono,noicons]` |
| `cv/professional/cv_professional_khammari.tex` | German | Every German employer, public and private | `[compact,mono,noicons]` |

**One German CV covers both German readers, and that is deliberate.** The
conservative Lebenslauf is the same document for a Bundesunternehmen and for
industry, because the Anschreiben is mandatory in Germany and it is the Anschreiben
that differentiates. Splitting the German CV would duplicate a file to change
nothing.

**What separates the two English ones.** The institutional CV puts Languages on the
front page, because a multilingual profile is a selection criterion at an EU
institution rather than a decoration, and it runs the thesis and the EU ETS design
above PwC. The private CV puts PwC above the research, folds languages into the
skills block, cuts the thesis to the scale of the data and the tools, and holds one
page. Both carry a one-sentence Profile and a commented `cvquals` scaffold at the
foot, because the qualifications block only works when it maps a posting's own
words and cannot be written in advance.

**`noicons` is on all three non-academic base CVs.** They go through ATS portals,
and with FontAwesome on, `pdftotext` returns the contact line as
`Q b.e.khammari@gmail.com ... ¯` **and drops the phone number entirely**. Verified
18 September on the academic CV, which still does this and should, because one
person reads it slowly. Anywhere a system reads the file first, use `noicons`.

`apply/build.py` only walks application folders, so the base CVs are compiled by
hand: `cd cv/<folder> && pdflatex -interaction=nonstopmode <file>.tex`.

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

**He asked on 18 September about RA posts that would give RCT experience.** The
answer is in [`bridge/rct-and-ra-routes.md`](bridge/rct-and-ra-routes.md) and it
needs a decision from him rather than more research. The route that supplies
"hands-on RCT experience in a low- or middle-income country" is a J-PAL or IPA
Research Associate post, which is one to two years in the field and therefore a
change of direction, not a bridge. **Do not treat this as settled either way.** If he
says development economics is the direction, the whole plan rebuilds around it and
the doctorate moves to 2028. If not, the gap worth closing is the absence of any
research-assistant experience, which an ordinary economics pre-doc fixes inside the
existing geography. DEval in Bonn is the best single test of the middle option.

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
- **No GRE, but the GMAT is now open.** The GRE decision of 10 September stands for
  economics programmes and still closes the Bonn BGSE, UPF and the Barcelona School
  of Economics, so do not propose the GRE again for those. **On 18 September he said
  he would sit the GMAT for Erasmus Rotterdam and that a change of field is fine,
  because he is flexible about the doctorate.** Treat field as open from now on.
  **He probably does not need the GMAT anyway:** ERIM accepts applications without a
  test score given other evidence of excellence, and names **top 15 percent grades**
  as an example. He is top 5 percent with a Dean's List and a 1,0 thesis.
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

### Mailbox checked 18 September 2026

Three changes since the 10 September snapshot above, all verified in Gmail.

**GIZ was submitted on 16 September.** Portal confirmation at 14:37, RE-ID
`oeiqlwzjwwfzjjdmemfusupfotdgyhen`. Selection starts after the 21 September
deadline and GIZ say they will come back proactively. Tracker marked sent, nudge
due 28 September.

**Frontier replied on 14 September** with the 2027 timeline. See the Frontier entry
below. Cologne and Berlin are open now and close end of January 2027.

**No academic reply since 10 September.** Siegloch and Dohmen both silent for ten
days. Siegloch's follow-up falls due 29 September, three weeks after sending.

**The four PhD drafts are still unsent**, confirmed in the draft list: Settele,
Wohlfart, van Maarseveen, and the Anna Person reply dated 10 September that carries
the CV, transcript and proposal. A separate draft to Pinger from 10 September is
also unsent. There is also an unsent draft to `nmohame1@uni-koeln.de` about the
seminar paper grading timeline, which belongs to the EU ETS work and not here.

He opened an **AcademicTransfer account** on the morning of 18 September, which is
the Maastricht vacancy channel.

### Open questions he has not answered

1. **Did the Blue Book application go in before 4 September 2026?**
2. Whether to run the LinkedIn and Indeed search. He raised it himself on 10
   September, so the earlier refusal is superseded, but confirm before running it.

The GRE question is now answered. He does not want to sit it, which is recorded
above as a decision.

## The transcript, read 18 September 2026

He uploaded `Khammari_ToR_Aug2026.pdf`, dated 13 August 2026. Master only, 114 of
120 ECTS at that date, preliminary overall **1,6**, thesis **1,0** with **Anna
Person as Erstgutachterin**. Recorded here because several claims elsewhere in this
repo were built on memory and two of them were wrong.

**Examiners and grades, master's programme.**

| Module | Topic | Examiner | Grade |
|---|---|---|---|
| Core Mathematics | Mathematics for Economists | Dyckerhoff R | **1,0** |
| Core Econometrics | Econometrics | **Liesenfeld R** | **1,3** |
| Energy and Climate Change I | **Energy Markets and Regulation** | **Ruhnau O** | **1,3** |
| Seminar Markets and Economic Policy | Housing and the Macroeconomy | **Kang D** | **1,3** |
| Core Macroeconomics | Macroeconomics | **Krause M** | 1,7 |
| Selected Methods in Economics | Experimental Methods | **Roth C** | 1,7 |
| Markets and Economic Policy IV | Macroeconomics of the Labor Market | **van Maarseveen R** | 2,0 |
| Energy and Climate Change II | Growth, Energy, Climate Change | Lindenberger D | 2,3 |
| Markets and Economic Policy V | Determinants of Growth in Economic History | Hornung J | 2,3 |
| Core Microeconomics | Microeconomics | Schottmüller C | **3,0** |
| Markets and Economic Policy II | Money and Financial Markets | **Schabert A** | **3,0** |
| Markets and Economic Policy III | **Development Economics** | Hornung J | **3,3** |

### Read again on 18 September, in full, with the seminar paper beside it

The first reading of this transcript took the module table and stopped. The rest of
the document carries four things that were nowhere in this repository.

**The master's thesis is 30 ECTS**, a quarter of the degree, submitted 17 April 2026
against a deadline of 17 April 2026. That number is the strongest single piece of
evidence that this is a research master rather than a taught one, which is exactly
what UCLouvain asks for ("a two-year research master's degree (120 ECTS)"). It was on
none of the CVs and is now on all four.

**Section grades, which are not the same as the overall 1,6.**

| Section | ECTS | Grade |
|---|---|---|
| Basisbereich / Core | 24 | 1,7 |
| Schwerpunktbereich / Specialisation, *Markets and Economic Policy* | 30 | 2,0 |
| Ergänzungsbereich Economics / Supplementary | 18 | **2,3** |
| Ergänzungsbereich Management and Social Sciences (Rotterdam) | 12 | pass |
| **Masterarbeit** | **30** | **1,0** |

The Ergänzungsbereich at 2,3 is where Development Economics (3,3) sits, alongside
both energy modules. Worth knowing before quoting a section grade at anyone.

**The official grading scale, verbatim from page 5, for any document that has to
gloss a German grade:** 1,0–1,5 *sehr gut* / very good; 1,6–2,5 *gut* / good;
2,6–3,5 *befriedigend* / satisfactory; 3,6–4,0 *ausreichend* / sufficient;
4,1–5,0 *mangelhaft* / fail. So **1,6 is the first grade in the "gut" band**, which
is worth knowing before arguing an "obtained with distinction" clause.

**Administrative facts.** Legal name **Baha Eddine Khammari**, born 12 February 2001
in Düsseldorf, Matrikelnummer **7364599**, Ein-Fach-Master, Prüfungsordnung 20212,
six Fachsemester against a Regelstudienzeit of four. The CVs use **Baha Khammari**,
which is fine, but official forms and the UCLouvain file name should use what the
transcript says. Status on 13 August was *"im laufenden Prüfungsverfahren"*.

**Two things this corrects.**

**The housing seminar was examined by Kang D, not Krause, and the mailbox settles
it.** The CV, the research statement and the general motivation letter all name
*Prof. Dr. Michael Krause* as the instructor of the Housing and the Macroeconomy
seminar, and the transcript names **Kang D** as Prüfer with 1,3. This no longer
needs asking. His own email to Krause of 13 August 2026 reads: *"I was a student in
your macroeconomics and labour courses across Bachelor and Master of Economics as
well as the housing seminar with Dong-Ho Kang in 2024."* He wrote that before any of
this analysis existed, to the man himself.

**That paragraph was half right, and the seminar paper itself settles the other
half.** He uploaded the paper on 18 September and its title page reads:
*"Supervisor: Univ.-Prof. Dr. Krause. Co-Supervisor: Dong-Ho Kang, PhD."* So Krause
supervised it, Kang co-supervised it and is the Prüfer of record on the transcript,
and **naming either one alone is incomplete**. Every CV now reads *"Supervisors:
Prof. Dr. Michael Krause and Dong-Ho Kang, PhD"*. A correction was made in the other
direction earlier the same day, on this file's authority, and the primary document
overruled it. Read the paper before renaming its supervisor again.

**Krause therefore has three teaching relationships, not two**, which is what this
file originally claimed before the transcript appeared to contradict it: Core
Macroeconomics 1,7 in the master, Economic Policy 2,0 in the bachelor, and
supervision of the housing seminar paper graded 1,3. He is still the weakest of the
three referees proposed on 18 September, on grades and on a five-day silence in
September, but not for the reason previously given here.

**Schabert is not a referee.** He graded *Money and Financial Markets* at **3,0**.
He supervised the bachelor's thesis and is worth an E13 enquiry, but do not name him
as a referee anywhere.

**Two grades worth knowing before writing.** **Microeconomics is 3,0**, which is the
visible weakness on any post asking for microeconomic theory, and UCLouvain asks for
exactly that. **Development Economics is 3,3**, and the GIZ letter leads with
Development Economics. The letter claims no grade, so nothing there is false, but if
GIZ asks for the transcript it is visible.

### The housing seminar paper, read 18 September

**Title: *From Boom to Bust: The Role of Subprime Mortgage Credit in the 2007 U.S.
Housing Crisis*.** Nineteen pages, dated 18 June 2024, Faculty of Management,
Economics and Social Sciences, University of Cologne. Seminar *Markets and Economic
Policy*, topic *Housing and the Macroeconomy*, **6 ECTS, grade 1,3**, and the
transcript records it as a **Kombinierte Prüfung**, so a paper plus a presentation.

**He named it as one of his strengths on 18 September** and asked for it on the CVs.
It had been cut from the UCLouvain CV on 18 September because the repo named Krause
while the transcript named Kang and that looked like an open question. It is not an
open question, and the paper is back on all four CVs.

**What it actually does, and the distinction matters as much as it does for the EU
ETS paper.** It is an appraisal of competing identification strategies, not original
estimation. **Never describe it as producing estimates.** It weighs the three
explanations of the 2002 to 2005 subprime mortgage expansion against one another:
the income-based hypothesis, the credit-supply hypothesis, and the house-price
expectations hypothesis. The spine is **Mian and Sufi (2009)** and their
within-county comparisons across ZIP codes, which is what lets income growth and
credit growth be separated. Around it: **Saiz (2010)** for the housing supply
elasticity instrument built from GIS data at MSA level, **Keys et al. (2010)** on
slacker screening under securitisation, **Adelino, Schoar and Severino (2016)** on
the extensive against the intensive margin and the role of middle-class borrowers,
and **Demyanyk and Van Hemert (2011)**, **Dell'Ariccia, Igan and Laeven (2012)** and
**Fuster et al. (2019)**. He handles the reverse-causality problem between house
prices and credit growth explicitly, which is the part worth citing in an interview.

**Why this is useful beyond the housing topic.** It is a second worked example of him
appraising identification strategies rather than describing results, on a completely
different literature from the thesis and the ETS paper. Three pieces of written work,
three appraisals of how a causal claim is made. That is the thing a doctoral reader
is looking for, and it is now visible on the CVs rather than buried in a grade line.

**One note for macro-financial applications.** Bundesbank, ECB financial stability,
BaFin and bank risk functions all care about this subject directly, and the paper is
the only thing in his file that speaks to it. It leads the research block on the
institutional CV for that reason.

## His energy background, in his own words

Given on 18 September, and it corrects an overclaim I had put in a document.

**His training is economics at the University of Cologne. It is not EWI.** A
UCLouvain draft said *"My training is Cologne through the Institute of Energy
Economics"*, which is wrong. He took modules taught by EWI-affiliated staff inside
an economics degree. Ruhnau and Lindenberger are at EWI, he is not, and naming their
affiliation on a CV line is fine while implying he was trained there is not.

**The energy specialisation is two master's modules, and their content matters more
than their grades.**

| Module | Examiner | Grade | What it covered |
|---|---|---|---|
| Growth, Energy, Climate Change | Lindenberger D | 2,3 | Three parts: the **physical foundations** of energy, the **economic foundations**, and **European regulation and market intervention** |
| Energy Markets and Regulation | **Ruhnau O** | **1,3** | The same ground, then specialised further into **grids and interconnectors** and the **European electricity market** |

Behind those sits the bachelor module **Current Topics in Economics** with Gürtler
at **1,3**, covering energy and environmental policy, and in front of them the EU
ETS seminar paper. So the honest description is a two-module master's specialisation
inside an economics degree, with a bachelor module before it and a research design
after it. **Write the content, not the grade.** Two grade lines are not evidence of
what he knows, and an energy post is judged on substance.

## Which referee to name

Asked on 10 September, reopened on 18 September when he said Anna Person is willing
and asked about Krause, Liesenfeld, or an energy professor. **The transcript answers
it.**

**For anything energy: Oliver Ruhnau**, `ruhnau@wiso.uni-koeln.de`. Jun.-Prof. for
**energy market design** at Cologne and senior scientist at EWI. He taught *Energy
Markets and Regulation* and graded it **1,3**. For the UCLouvain renewable-auctions
post he is a better name than any general econometrician, because the chair, the
course and the application subject are the same thing.

**For anything general: Roman Liesenfeld**, 1,3 in Econometrics, and he is already
getting an E13 enquiry so the ask can ride along.

**Krause is the weaker of the three he proposed.** One course on the transcript,
Macroeconomics at 1,7, and the seminar that justified him belongs to Kang on paper.
He is also recorded as unresponsive for five days in September.

**Anna Person is willing**, stated 18 September. That does not change the rule below.
She is an M.Sc. and a PhD candidate, so she goes where a professorial title is not
required.

The older answer, which still holds for the professor-versus-Anna split:

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

**Email address patterns, corrected 18 September against the sent folder.** The
earlier claim here was that **Cologne is consistent at `lastname@wiso.uni-koeln.de`
and that is wrong**. Most are: `settele@`, `neisser@`, `kang@`, `boelmann@`,
`rubio@`, `siegloch@`, `vanmaarseveen@`, `wohlfart@`, `schabert@`, `liesenfeld@`,
`roth@`, `ruhnau@`, and Anna Person at `person@`. But **Krause is
`michael.krause@wiso.uni-koeln.de` and Braun is `helge.braun@wiso.uni-koeln.de`**,
and **Pinger is `pia.pinger@uni-koeln.de` with no `wiso`**, all three verified from
replies they sent. So Cologne has three patterns, not one, and the rule is the same
as for Bonn: check the faculty page before writing to someone new.

**Bonn**: `t.dohmen@`, `tboneva@`, `amelie.schiprowski@`, `klagge@`, `mqaim@`,
`parlasca@`. Department fallback: `econpr@uni-bonn.de`. **RWI Essen** capitalises:
`Ronald.Bachmann@`, `Matthias.Westphal@`, `Marcus.Tamm@rwi-essen.de`.

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

**Frontier Economics, and this one has a live window.** Their recruitment team
**replied on 14 September** with the 2027 timeline. Applications for interns and
analysts in **Amsterdam, Berlin, Cologne, Dublin and London opened mid-September
2026**. Brussels, Paris and Junior Data Scientist roles open early October.
Closing: **London November 2026, Dublin end of December 2026, every other office
end of January 2027.** So Cologne and Berlin close end of January.

Checked the Workday board on 18 September and the Cologne and Berlin postings are
not up yet, so this is a weekly watch at
`frontiereconomics.wd3.myworkdayjobs.com`. The tuned CV and letter already exist in
`apply/applications/frontier-economics-graduate-...`.

Their Graduate Economic Analyst programme accepts "Germany 2.0 or better" plus a
master's, wants R or Stata and advanced Excel, and requires fluency in the language
of the office, which is what makes **Cologne and Berlin** work and Amsterdam not.

**Maastricht GSBE expects a supervisor and funded position to be identified before
applying.** So the portal is paperwork that follows the approach. Rolling review
through May 2027, Studielink opens 1 October 2026. Central address
`gsbe-phd-application@maastrichtuniversity.nl`.

**UCLouvain, read off the posting page on 18 September rather than inferred.**
Submission is a **Microsoft Forms page**, `https://forms.cloud.microsoft/e/Nbx4HmviLp`,
and the contact is `bert.willems@uclouvain.be`. One PDF, **named
`Lastname_Firstname.pdf`**, so `Khammari_Baha.pdf` and not the house
`cv_<firm>_khammari.pdf`. The **statement of intent is capped at one page by the
posting**, which happens to match his own instruction. The deadline is softer than
it reads: *"Applications received by 21 September 2026 will receive full
consideration. Review continues until the position is filled."* So Monday is the
date for full consideration and Tuesday with two referees beats Monday with one.
Referees are **names and contact details only**, since *"letters of recommendation
may be requested at a later stage"*, which is why the Ruhnau ask is one line and not
a request for a letter. They also want **bachelor's and master's degree
certificates**, and the master's one does not exist yet, so the transcript at 114 of
120 ECTS goes in and the statement carries the September completion date.

**The board was empty in his field on 18 September.** Checked AcademicTransfer,
filtered to scientific vacancies in economics and labour economics. The only
economics vacancy was the Maastricht Assistant Professor in Macroeconomics, out of
reach. So the board is a **weekly** check, not a daily one, and the effort belongs
in direct enquiries and the Frontier window.

**Two postings he sent on 18 September were both rejects, and both failed on the
requirement list rather than on fit.** Tilburg wanted hands-on RCT implementation,
Utrecht sat in the Faculty of Geosciences and asked for Geoinformatics or spatial
data science. A thirty-second test now lives at the top of step 2 in
[`apply/README.md`](apply/README.md): check the faculty, check whether an economics
MSc is on their accepted list, check whether they name a method he has never used.
**Two false signals have cost time.** A shared country is not a fit signal, Brazil
appearing in both his thesis and a land-use project means nothing. And **558
microregions reads as spatial work but is a regional panel**, so geography is an
index rather than an object of analysis. No GIS, no raster data, no spatial
econometrics anywhere in the thesis.

**The Dutch job board carries two different things, and the filter matters.**
Learned 18 September from a Tilburg posting he sent. **Project positions** are
attached to a specific grant, so their requirements come from the grant rather than
the graduate school and are not negotiable. The Tilburg one required *"demonstrated
hands-on experience implementing randomized controlled trials in low- or
middle-income countries"* and substantial periods in Kenya, which is a reject on the
first screen however well the subject fits. **General graduate-school intakes** run
to the school's own admission rules. Read the requirement list before the salary.
Rejected and written up in
`apply/applications/tilburg-university-phd-candidate-in-economics-center-digital/posting.md`.

**Tilburg CentER takes an academic Master's and does not need the GRE.** Verified on
their admission pages, 18 September. They ask for *"an academic Master's or Research
Master's degree"*, with Research Master holders *"preferred"* rather than required,
and the GRE is only the fallback for applicants who cannot show **24 ECTS of
quantitative and research methods** across the BSc and MSc. His econometrics
coursework clears that alone. So the no-GRE decision does not close the
Netherlands. **Check which Tilburg route a posting is**: the direct PhD is salaried
from day one at about €2,750 gross rising to €3,500 by year 4, while the Research
Master plus PhD route is five years and starts with two years of coursework, which
is a second master's after this one.

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

**Academic documents get the LaTeX look.** Instructed 18 September. Latin Modern
roman on the default `article` or `letter` class, justified, generous margins, the
working-paper aesthetic an economist expects. That covers statements of intent,
research statements, the research proposal, the thesis abstract and the academic
CV, which gets it through the class option `serif`. Everything already in
`research/` and `letters/academic/` was built that way. The two statements written
on 18 September were the outliers, because they had been set in `tgheros`, and both
are now converted. **German letters and the German CV stay sans**, since neither is
an academic document and the reader there is an HR portal.

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
apply/merge.py   assemble the single PDF a portal asks for, from a merge.txt manifest
apply/tracker.csv  one row per application, the single source of truth
```

**`personal/` at the repository root holds transcripts and certificates and is in
`.gitignore`.** Added 18 September, when UCLouvain turned out to want bachelor's and
master's transcripts and degree certificates inside one PDF. This repository is
public, so those files are referenced by path from a `merge.txt` manifest and never
committed. If they are not on disk, `merge.py` names each missing one and refuses to
build, rather than producing a bundle that looks complete.

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

### The Bachelorzeugnis, read 18 September

He uploaded it. **B.Sc. Volkswirtschaftslehre, conferred 1 February 2023, overall
gut (1,6).** Bachelorarbeit **Finanz-Akzelerator**, 12 ECTS, gut (1,7), Erstgutachter
Univ.-Prof. Dr. Andreas Schabert. Section grades: Basis- und Aufbaubereich 90 ECTS
at 1,7, **Ergänzungsbereich 36 ECTS at sehr gut (1,5)**, Schwerpunktbereich 30 ECTS
at 1,8, Studium Integrale 12 ECTS passed.

**The "top 5 percent" claim needs his decision, and it is on fourteen files.** The
Zeugnis carries the university's **Einstufungstabelle**. For an overall grade of 1,6
it reports that **5.5 per cent** of the 256 degrees awarded in the reference period,
1 February 2021 to 1 February 2023, were 1,6 or better. Every CV in this repo says
*top 5 %*.

Those may both be true. The comparison group in that table pools Betriebswirtschaft,
Sozialwissenschaften, Volkswirtschaft and Wirtschaftsinformatik, and **the Dean's
List is a separate award with its own criterion**, which may well be top 5 per cent
of the VWL cohort alone. **Ask him what his Dean's List letter says.** Until then:
the UCLouvain CV now reads *B.Sc. Economics, 1.6. Dean's List*, with no percentage,
because the Zeugnis travels in the same PDF and a reader can check. Nothing else was
mass-edited on an inference.

**The bachelor's thesis title is German on the certificate.** It reads
*Finanz-Akzelerator*, and the English certificate leaves it untranslated. The CVs
render it as *The Financial Accelerator Mechanism*, which adds a word the official
title does not have. Submitted 4 July 2022, graded 1,7.

**The BSc transcript, read 18 September, and it is stronger than the 1,6 average
suggests.** 180 of 180 ECTS, seven Fachsemester.

| Module | Topic | Examiner | Grade |
|---|---|---|---|
| Advanced Microeconomics | **Strategic thinking and competition** | **Ockenfels A** | **1,3** |
| Core Microeconomics | Grundzüge der Mikroökonomik | Gürtler O | **1,0** |
| Core Statistics | | Gribisch B | **1,0** |
| Core Mathematics | | Scheicher C | **1,0** |
| Advanced Macroeconomics | Growth and structural change | Funk P | **1,0** |
| Supply Chain Management | | Thonemann U | **1,0** |
| Finance I | Corporate finance | Hess D | **1,0** |
| Advanced Econometrics | **Applied econometrics** | **Breitung J** | **1,3** |
| Current Topics in Economics | **Energy and environmental policy**, media regulation | Gürtler O | **1,3** |
| Cost accounting | | Homburg C | 1,3 |
| Economic Policy | | **Krause M** | 2,0 |
| Bachelorseminar VWL | Macro topics from the CMR | **Schabert A** | **2,3** |
| Institutions | | Nayin T | 2,3 |
| Core Macroeconomics | | Barbie M | 2,7 |
| International Economics | | Prantl S | 2,7 |
| Finance II | Bank management | Spörk W | 3,3 |

**This changes the theory story.** The master's Microeconomics 3,0 had been treated
as the whole picture. At bachelor level microeconomics is **1,0** and advanced
microeconomics is **1,3**, and the topic of the latter is **strategic thinking and
competition, taught by Axel Ockenfels**, whose own field is market and auction
design and who heads *Market Design and Behavior* at ECONtribute. Any application
asking for game theory should say so. The UCLouvain statement now does.

**It also adds referee candidates who beat the ones previously listed.**
**Oliver Gürtler** taught him twice, 1,0 in microeconomics and 1,3 in a module
covering energy and environmental policy, which is the strongest teaching
relationship on either transcript. **Jörg Breitung** gave 1,3 in applied
econometrics. **Axel Ockenfels** gave 1,3. All at Cologne, so the
`lastname@wiso.uni-koeln.de` pattern applies, and all need verifying before use.

**Schabert is now definitively off the referee list.** He examined three things:
the bachelor seminar at **2,3**, the bachelor's thesis at 1,7, and a master's
module at **3,0**. He supervised the thesis and is worth an E13 enquiry. He is not
a reference.

**Krause is confirmed at two courses**, Economic Policy at 2,0 in the bachelor and
Macroeconomics at 1,7 in the master. The repo's "three courses" claim may still
hold if a third sits outside these transcripts.

### What the EU ETS seminar actually is, recovered 18 September

He asked for it from "other chats and memory". **Neither is reachable from Claude
Code**: chat history on claude.ai cannot be read from here and no memory store is
mounted. What worked was Gmail and **Google Drive**, and that is the route to use
next time.

**The seminar is Panel Data Methods, Summer 2026, Cologne.** Instructor **Nada Fadl
Mohamed**. His paper there is the final requirement of the degree. The group
presentation was with Márton and Yin, twenty minutes, three papers with one each:
Colmer et al. (2025), Dechezleprêtre et al. (2023) and D'Arcangelo et al. (2022).
Working document in Drive, titled *EU ETS and Firm Production*, file id
`1HiclTmRu9P-mA6NadIDZxbPmT1yD8Q4nR3vtwgbl0aY`.

**The subject is identification, not energy policy description.** The seminar
compared how the firm-level ETS literature identifies effects: coarsened exact
matching with DiD (Colmer, Martin, Muûls and Wagner, 2025, *ReStud*, emissions down
about 15 per cent in Phase I and 26 per cent in Phase II, no significant effect on
value added or employment, capital stock rising); propensity-score matching on
pre-treatment trends (Dechezleprêtre, Nachtigall and Venmans, 2023, *JEEM*, about
$-10$ per cent, null effects on revenue, employment and fixed assets); instrumental
variables on carbon-leakage criteria (Martin, Muûls, de Preux and Wagner, 2014,
*AER*); Poisson count models for patents (Calel and Dechezleprêtre, 2016, *REStat*,
roughly 10 per cent more low-carbon patenting); and **heterogeneity-robust staggered
DiD in Bremer and Sommer (2025, *Energy Economics*), who apply Callaway and
Sant'Anna to Dutch firms across Phases I to III**.

**That last one is the single most useful fact in this file for energy
applications.** The estimator he used on Brazilian labour data is the estimator the
frontier ETS literature uses on European carbon regulation. The bridge between his
econometrics and energy policy is already built, in his own coursework.

Threats to identification he worked through: anticipation, since the Directive was
adopted in 2003 and the scheme began in 2005; Great Recession confounding; SUTVA
violations through product markets; free allocation weakening effective treatment
intensity; survivorship bias from balanced panels. The gap he identified is that
credible firm-level evidence concentrates on Phases I and II and is scarce for
Phases III and IV.

**His individual paper is on GitHub, and it is much better than the group document
suggested.** Repo `bkhammari/EU-ETS-and-Production`, public. `main` holds only a
README. **The work is on the branch `claude/eu-ets-carbon-leakage-8etb0s`**, in
`paper/` as a LaTeX project with sections and a bib file, plus a `proposal/`.

The question: **did increases in the effective EU ETS carbon cost, net of free
allocation, raise EU imports of emission-intensive goods from Morocco, Algeria,
Egypt and Tunisia between 2005 and 2021**, relative to less emission-intensive goods
and to comparison partners? It argues against the aggregate null in Naegele and
Zaklan (2019), on the ground that an aggregate null can hide leakage concentrated in
corridors with large regulatory asymmetry, low transport costs and existing
emission-intensive capacity.

**It is a research design and produces no estimates.** He said so on 18 September:
it was the groundwork for a master's thesis on the topic that he decided not to
write. **Never describe it as empirical results.** That is not a weakness to hide
either. A worked specification with its treatment definition, data sources and
identifying assumptions paired against the threats each one answers is the shape of
a doctoral proposal, which is exactly what a doctoral application wants to see. The
UCLouvain statement says outright that it is a design rather than a set of
estimates, and says why it exists.

**Triple difference.** Exposure varies across products through sectoral CO$_2$
intensity, over time through the effective carbon cost, across partners through
corridor membership. Product-by-year fixed effects absorb global product shocks,
partner-by-year absorb macro and exchange-rate movements, product-by-partner absorb
bilateral relationships. Comparison groups considered: Turkey, the Western Balkans,
an intra-EU benchmark, with the limitation of each stated.

**The idea worth reusing in any energy application.** The treatment is
$C_{st} = P_t \times (1 - a_{st})$, the allowance price attenuated by the sector-year
free-allocation share, so a fully allocated sector faces an effective cost of zero
whatever the headline price does. He anticipates the lump-sum objection and answers
it: EU allocation is tied to continued production through activity thresholds,
closure provisions and partial-cessation rules. **The headline price of an
instrument and the incentive it creates are different objects, and the gap is a
property of the rules.** That is the sentence the UCLouvain statement now turns on,
because an auction award price is not the effective support either once
pre-qualification, penalties, bonds and local content are priced into a bid.

Endogeneity of the allocation share is handled by fixing it to 2005 to 2007 verified
emissions. The window stops in 2021 to give a pre-CBAM baseline.

Note without putting it in an application: **Tunisia is in his own treatment
corridor.** This was tested on 18 September and the note holds. A UCLouvain draft
carried the clause *"Morocco, Algeria, Egypt and Tunisia, the last of which is where
my family is from"*, written when he had asked for a personal touch. It came out
with the narrative structure that carried it, because a statement saying why he
wants the post and what he brings has no slot for it. Do not propose it again
unless he asks for it.

**One thing to tell him.** An unsent draft opening *"Dear Ms Fadl"* is addressed to
`ilias@uni-koeln.de`. ILIAS is the Cologne learning platform, so that is a system
address rather than hers. Her address is `nmohame1@uni-koeln.de`, which the second
draft uses correctly.

## Where things are

- `apply/` the workflow and per-application folders
- `phd/` outreach hub. `README.md` is the master tracker with per-target status
- `phd/e13-direct.md` the two-channel explanation and where positions actually are
- `phd/geography-and-pay.md` PhD destinations ranked by pay
- `bridge/` paid interim positions. `private-sector.md` covers finance and consulting
- `eu/` EPSO AD5 and Blue Book, with mock exams and an abstract-reasoning trainer
- `cv/academic/`, `cv/institutional/`, `cv/private/`, `cv/professional/` the four
  base CVs, plus `cv/shared/OpenCV.cls`
- `letters/`, `research/`, `scholarships/`, `dashboards/`

Work happens on the branch `claude/sleepy-keller-gissaq`. Commit and push as you go.
