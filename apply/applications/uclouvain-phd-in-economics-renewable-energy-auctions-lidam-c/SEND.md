# UCLouvain, what to do and in what order

**Deadline: Monday 21 September 2026.** Today is Friday 18 September. Both written
documents are finished. What is left is one email, four of your own files, and a
form.

## 1. Today, before anything else: the referee

**A draft to Jun.-Prof. Dr. Oliver Ruhnau is in Gmail, labelled PhD.** Send it now.
It asks only for permission to name him, not for a letter, because the posting says
outright that *"letters of recommendation may be requested at a later stage"*. A
one-word answer is enough and the email says so.

**Nothing else can be submitted until he answers**, because the CV names him and the
application requires two academic referees inside the PDF. If he says no by Sunday,
the fallback is **Prof. Dr. Roman Liesenfeld** (Econometrics 1,3), whose E13 draft
is already in Gmail and can carry the same ask. Do not fall back to Schabert, who
graded his own module 3,0.

**If he has not answered by Sunday evening, do not submit without him.** The posting
says *"Applications received by 21 September 2026 will receive full consideration.
Review continues until the position is filled."* Monday is the date for full
consideration rather than a cut-off. Tuesday with two referees beats Monday with
one. This is not licence to drift, because rolling review means someone who applied
on time can take the position.

## 2. Collect four files of your own

They want **one PDF** and they name it for you: `Lastname_Firstname.pdf`, so
`Khammari_Baha.pdf`. Everything goes inside it, in the posting's order.

| Item | Where it is |
|---|---|
| Statement of intent | Ready, `statement.pdf`, **one page**, which is their cap |
| CV | Ready, `cv_uclouvain_khammari.pdf`, two pages |
| Master's transcript | Yours. `Khammari_ToR_Aug2026.pdf` |
| BSc transcript | Yours |
| Bachelorzeugnis | Yours, the certificate with the Einstufungstabelle |
| IELTS certificate | Yours |
| Writing sample | The thesis, already in the repository |
| Two academic referees | Named in the CV. **Pinger agreed, Ruhnau pending** |
| Test scores | None, and none required |

Put the four personal files in a folder called `personal/` at the top of the
repository. It is in `.gitignore` and will never be committed, which matters because
this repository is public. Name them as `merge.txt` expects, or edit the paths in
that file, whichever is quicker.

Then:

```bash
python3 apply/merge.py uclouvain
```

That writes `Khammari_Baha.pdf` and prints the page count of every part, so you can
see at a glance whether anything went in twice or not at all. Expect about ninety
pages, most of it the thesis.

**One wrinkle on the certificates.** They ask for bachelor's and master's degree
certificates. The master's one does not exist yet, and the transcript in hand is
dated 13 August at 114 of 120 ECTS. Send what exists. The statement already says you
complete the M.Sc. this month and are available from October, so nothing is hidden.
If the Prüfungsamt has since reissued the transcript at 120 ECTS, use that version
instead, because it records the 1,0 thesis grade as a result rather than a claim.

## 3. Submit

The form: **https://forms.cloud.microsoft/e/Nbx4HmviLp**

Contact if anything about the form fails: **bert.willems@uclouvain.be**

```bash
python3 apply/track.py sent uclouvain
```

## 4. What the statement says, and what it deliberately leaves out

Rewritten on 18 September to the brief: say why you want the position and what you
bring. **463 words of argument, 493 on the page, one page.**

| Paragraph | Job | Words |
|---|---|---|
| 1 | Why this position, stated as a claim about auction design | 95 |
| 2 | What you bring on energy. Ruhnau 1.3, and the ETS paper | 130 |
| 3 | What you bring on method. The thesis, and why it transfers | 113 |
| 4 | Which directions, whose work, your theory training, the close | 125 |

**Three things came out that earlier drafts carried, and it is worth knowing they
were removed on purpose rather than lost.**

The **two-way fixed effects sign reversal** is gone. An earlier draft made it the
spine of the whole document. It reads as a confession, and a reader who meets a
mistake in paragraph one is thinking about the mistake for the rest of the page. The
thesis now states its estimator and its result as a capability. If it comes up in an
interview it is a good answer to a question, which is a different thing from an
opening line.

The **microeconomics 3.0** is gone. It was in on the argument that the transcript
travels in the same PDF, so naming it first beats being caught by it. That holds in a
document that is arguing with the reader. This one is not. Paragraph four states the
theory training positively instead, game theory and competition with Ockenfels at
1.3 alongside econometrics at 1.3, which is true and answers the same requirement
without volunteering anything against you.

The **Tunisia clause** is gone with the narrative structure that carried it. There is
no slot for it in a document about why you want the post and what you bring.

### Paragraph four names two people, both verified

- **Willems and Yu** compare discriminatory and uniform-price auctions on short-run
  bidding and long-run investment. Your point is that a penalty regime changing the
  map from bid to delivered capacity changes that comparison.
- **Lété, Smeers and Papavasiliou (2026)** on what zonal pricing with market-based
  re-dispatch costs in efficiency. Quentin Lété is an assistant professor at CORE
  and teaches Quantitative Energy Economics.

**Hindriks and Maniquet were considered for a third and left out.** They appear on a
Horizon Europe project about energy inequality, which would connect to the
distributional side of your thesis, but that page would not load and a name in a
statement of intent has to be verified. Two named beats three with one guessed.

**One thing the layout has no slot for.** Availability from October, French,
citizenship and the two referees sit in a single small-type line under paragraph
four. On an advertised post with an autumn 2026 start and a two-referee requirement,
availability is load-bearing rather than padding.

## 5. French is on the front page now

**UCLouvain is in Louvain-la-Neuve, in francophone Wallonia.** B1 French is not a
decorative line for this application, it is a fact about whether you can live and
work there, so Languages moved from the foot of the CV to page one with French
first. On the statement it sits in the closing line with availability and the
referees.

The application itself stays in English, because the posting requires it: *"Applications
must be submitted in English."*

## 6. What the application argues

Worth knowing before an interview, since the position is theory-led and you are not.

**The claim is that European auction design is staggered adoption.** Member states
introduced auctions at different dates and then revised penalty levels, bid bonds,
realisation deadlines, technology lots and local content rules on different national
timetables. That is variation of exactly the kind your thesis was built to handle,
and the statement proposes it as the contribution a theory-trained candidate could
not make.

**Prepare one answer before any interview.** The statement does not raise the
master's Microeconomics 3,0 and it should not, but both transcripts are in the
submitted PDF and a theory-led group may ask. The answer is on the record and it is
a good one: bachelor microeconomics 1,0, advanced microeconomics on strategic
thinking and competition with Ockenfels 1,3, econometrics 1,3, mathematics 1,0. What
is genuinely ahead of you is graduate industrial organization, and that is
coursework. Say it that way if asked, and do not say it first.

## Why this one is worth three days

It is the only position found so far that **starts inside the gap**. Autumn 2026, no
later than January 2027, against every other target starting in late 2027. About
€2.400 net and tax-exempt under the Belgian doctoral regime, which is worth more
than the number suggests. Belgium is inside the PhD geography. No GRE.

It is still a long shot on the theory requirement. A long shot that pays from
November beats a strong fit that pays from October 2027.
