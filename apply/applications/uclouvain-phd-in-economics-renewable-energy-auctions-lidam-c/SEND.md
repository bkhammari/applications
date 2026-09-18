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

## 4. How the statement is built

Rebuilt on the four-paragraph persuasive layout rather than a compressed
biography. **461 words of argument, 503 on the page including the closing line, one
page with room at the bottom.**

| Paragraph | Job | Words |
|---|---|---|
| 1 | The hook, the idea, the gap | 100 |
| 2 | Proven research: context, action, result, and a setback you fixed | 110 |
| 3 | What you would do, and why here | 142 |
| 4 | Where this goes in five to ten years | 109 |

**It opens on a concrete moment rather than a credential.** A week spent building the
EU ETS allowance price series before realising it was the wrong variable, because a
plant holding free allocation faces almost none of the headline price. Then the
objection, that allowances are tradable so a lump-sum grant should not move output,
and the answer, that activity thresholds and closure provisions tie EU allocation to
production. The previous draft opened with Ruhnau's 1.3, which is on the CV. This
one does not repeat the CV anywhere.

**Paragraph two now tells the sign reversal as something that went wrong and you
fixed.** First specification two-way fixed effects, minus 0.65 per cent, Goodman-Bacon
decomposition, already-treated regions serving as controls, re-estimate at plus 3.04
per cent. It closes on what you took from it rather than on the grade. That is the
paragraph the layout asks for and the earlier drafts did not have.

**Paragraph three names two people and says what you add to each.** Both were
verified rather than assumed.

- **Willems and Yu** compare discriminatory and uniform-price auctions on short-run
  bidding and long-run investment. Your point is that a penalty regime changing the
  map from bid to delivered capacity changes that comparison.
- **Lété, Smeers and Papavasiliou (2026)** on what zonal pricing with market-based
  re-dispatch costs in efficiency. Quentin Lété is an assistant professor at CORE
  and teaches Quantitative Energy Economics. Your point is that Europe has been
  generating the empirical counterpart for a decade through staggered national
  adoption, which is the setting your thesis was built for.

**Hindriks and Maniquet were considered and left out.** They appear on a Horizon
Europe project about energy inequality, which would connect to the distributional
side of your thesis, but that page would not load and a name in a statement of
intent has to be verified. Two named beats three with one guessed.

**One deliberate deviation from the layout.** It has no slot for logistics, so
availability from October, French, citizenship and the two referees sit in a single
small-type line under paragraph four. On an advertised post with an autumn 2026
start and a two-referee requirement, availability is load-bearing rather than
padding.

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
