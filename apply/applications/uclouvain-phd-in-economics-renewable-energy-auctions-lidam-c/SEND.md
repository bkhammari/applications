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

## 4. What the one-page cut kept, and what it dropped

The statement was two pages and is now one, which the posting requires as well as
you. Four things survived, in this order of priority.

**The free-allocation argument from your own seminar paper.** The effective carbon
cost is the allowance price attenuated by the sector-year free-allocation share, a
fully allocated sector faces zero effective cost whatever the headline price does,
and EU allocation is not lump-sum because activity thresholds and closure provisions
tie it to production. Then the parallel: an auction award price is not the effective
support either, once pre-qualification, penalties, bonds and local content are priced
into the bid. That paragraph is the application. Everything else is support.

**Ruhnau's 1.3 in energy market design**, which also tells the reader who your second
referee is before they reach the reference list.

**The staggered-adoption problem and the sign reversal**, compressed to two sentences
because the CV carries the detail.

**The theory position, stated before the transcript states it.** Master's
microeconomics 3.0, bachelor microeconomics 1.0, advanced microeconomics with
Ockenfels 1.3 on strategic thinking and competition. The admitted gap is graduate
industrial organization and nothing wider.

**Dropped:** the specification detail of the triple difference, the identification
threats catalogue, the full thesis description, and the section headings. All of it
is either on the CV or in the paper itself, which you offer to send.

## 5. French is on the front page now

**UCLouvain is in Louvain-la-Neuve, in francophone Wallonia.** B1 French is not a
decorative line for this application, it is a fact about whether you can live and
work there, so Languages moved from the foot of the CV to page one with French
first. The statement says the same thing in one clause.

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

**The honesty is deliberate, and it is now narrower than it was.** The statement
names the master's Microeconomics 3,0 before the reader finds it, because both
transcripts travel in the same PDF. What it no longer concedes is general weakness
in theory, because the BSc transcript does not support that: microeconomics 1,0, and
advanced microeconomics on strategic thinking and competition with Ockenfels 1,3.
The admitted gap is graduate industrial organization alone, which is coursework.

## Why this one is worth three days

It is the only position found so far that **starts inside the gap**. Autumn 2026, no
later than January 2027, against every other target starting in late 2027. About
€2.400 net and tax-exempt under the Belgian doctoral regime, which is worth more
than the number suggests. Belgium is inside the PhD geography. No GRE.

It is still a long shot on the theory requirement. A long shot that pays from
November beats a strong fit that pays from October 2027.
