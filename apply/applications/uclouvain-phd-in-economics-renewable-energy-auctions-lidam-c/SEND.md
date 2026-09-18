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

**The certificates are not a problem.** The posting asks for bachelor's and
master's transcripts and degree certificates *"(if available)"*, and this file
previously quoted that line without the last two words. Your master's certificate
does not exist yet and the posting already allows for that. Send what exists.
The statement and the CV both carry the September 2026 completion date, which the
posting asks for by name on the CV.
If the Prüfungsamt has since reissued the transcript at 120 ECTS, use that version
instead, because it records the 1,0 thesis grade as a result rather than a claim.

## 3. Submit

The form: **https://forms.cloud.microsoft/e/Nbx4HmviLp**

Contact if anything about the form fails: **bert.willems@uclouvain.be**

```bash
python3 apply/track.py sent uclouvain
```

## 4. What the statement says

Rebuilt against the MIT EECS Communication Lab guide you sent, then revised on
18 September when you asked for a story, for the future-colleague argument, and for
concision. **651 words, one page, filling it.** Above the 400 to 500 general guides
quote, kept because the constraint the posting states is one page.

| Paragraph | Job |
|---|---|
| 1 | Why this doctorate. The question that recurs across your work, stated first |
| 2 | The Cologne energy modules, and what they let you see in an auction rule |
| 3 | Quantitative preparation, tutoring, the thesis, and what the thesis settled |
| 4 | The two directions you would take up, and the evidence behind each |
| 5 | Why a colleague here specifically, the impact, the ten-year goal |

**The story is an intellectual one, not a biographical one.** One question runs
through all of it: the support an instrument appears to offer and the incentive it
creates are different quantities, and the rules decide the distance between them.
ProUni is an instance, because dose rather than treatment status carries the
effect. The EU ETS paper is an instance, because free allocation attenuates the
allowance price. Renewable auctions are the next one. Paragraph one states it and
paragraphs three and four are the evidence, which is the roter Faden you said an
earlier draft lacked. It is not an error narrative and must not become one.

**The future-colleague question is answered in paragraph five, by addition.** The
group argues these questions formally. You are not a theorist and the statement
does not pretend otherwise. What it offers is the empirical counterpart, on the
ground that European support-scheme reform is staggered adoption and you know how
to read it. That answers the theory requirement without conceding anything, and it
is also the honest description of what you would add to that corridor.

### What the MIT guide changed

**Meaning is now wrapped around every experience.** That is the guide's central
teaching and every earlier draft missed it. An experience on its own is a CV in
prose. Its line is worth keeping: *"A statement of purpose is a way to make a
narrative out of your CV. It is not a diary entry."* Each block still ends on the
sentence that says what it proves.

| After | The sentence that says what it proves |
|---|---|
| The two energy modules | Why an auction rule reads to you as a physical and regulatory constraint as much as an economic one |
| Maths, econometrics, tutoring | Tutoring is the test of whether you know a method or only recognise it |
| The thesis | Dose, rather than treatment status, is where the answer sits, and you can get there from raw records on your own |

The last of those changed on 18 September. It used to say only that you can take a
staggered rollout from raw records to a defensible estimate, which is a claim about
craft. It now also names what the thesis found out about policy, which is the claim
that links the thesis to the auction question and carries the reader into paragraph
four.

**Your tutoring is in, quantified.** Two school students, Abitur-level mathematics.
The guide asks for exactly that kind of number and it sits next to the mathematics
marks it supports.

**The European institution route is out of the close**, on your answer. The
ten-year sentence is now research only. You were shown the trade-off and chose it,
so a future session should not put it back.

**No section headings**, on your answer. The guide recommends them and assumes two
pages. You have one.

### Two numbers the guide asks for and I do not have

The guide is explicit that collaboration should be quantified, not just data. Team
size, report counts, how selective an award was. **Only you can supply these.**

1. **PwC.** How large was the engagement team, how many reports did you work on,
   and did anything you built save measurable time?
2. **The Dean's List.** What does the letter actually say the criterion is? The
   Zeugnis Einstufungstabelle reports 5.5 per cent for a 1,6 across a pooled
   comparison group, and fourteen files in this repo say top 5 per cent.

Neither blocks this application. Both would strengthen every future one.

### The correction that mattered most

**You want directions 1 and 2. Earlier drafts said 3 and 4.** I chose those without
asking and wrote them into a document going out under your name as your own research
interest. Nothing in the posting or this repository said which you wanted. That is
the worst kind of error available here, because it is invisible unless you read
every line, and the rule is now in `CLAUDE.md`.

Directions 1 and 2 turn out to be the better home for your own work anyway.

**Direction 1, de-risking green investment.** The call asks whether public
intervention *"crowd[s] out private insurance or weaken[s] cost incentives"*. Your
seminar paper is already an instance of the second half of that question. Free
allocation is a public intervention that weakens a cost incentive while the headline
allowance price is unchanged, and the attenuation is not lump-sum because activity
thresholds and closure provisions tie allocation to production. The statement says
the same logic reaches guarantees, contracts for difference and public insurance.

**Direction 2, multi-technology auction design.** This one has the cleaner empirical
footing and the statement says so. Since the 2016 state aid framework, member states
have landed on technology-neutral, technology-specific and mixed designs at
different dates, and **Germany's joint wind and solar auction of April 2018 gave the
entire 200 MW to solar at bids above the technology-specific benchmark**. Portfolio
composition and rents are observable, which is what makes the direction measurable
rather than only modellable. That fact was verified before it went in.

### Two more corrections

**Your training is economics at the University of Cologne, not at EWI.** A previous
draft said *"My training is Cologne through the Institute of Energy Economics"*,
which overclaims. Ruhnau and Lindenberger are at EWI. You took their modules inside
an economics degree. Naming their affiliation on a CV line is accurate, implying you
were trained there is not.

**The energy modules are now written out by content rather than by grade**, on the
statement and on the CV, because two grade lines prove nothing about what you know
and this post is judged on energy substance.

| Module | Grade | What the CV and statement now say |
|---|---|---|
| Growth, Energy, Climate Change | 2,3 | Physical foundations of energy systems, economic foundations, European regulation and market intervention |
| Energy Markets and Regulation | **1,3** | The same ground, then grids and interconnectors and the European electricity market |

### What the guides changed

You asked me to research the document type first. Three rules came back that altered
the draft. **Open with field and direction in the vocabulary of the field**, not with
motivation, so paragraph one now opens on the doctorate you want to write rather
than on wanting to work on European instruments. **Keep mathematical preparation
near the centre**, because it carries real weight in economics admissions, so the
1.0 in mathematics, 1.3 in econometrics and the bachelor marks are in paragraph two
rather than in a closing list. **Cut everything that is noise around the research
signal.**

### Three people at CORE, all verified

- **Willems and Yu** on discriminatory versus uniform-price auctions and how
  short-run bidding maps into long-run investment, which is the rent question inside
  direction 2.
- **Quentin Lété**, assistant professor at CORE, on market design, capacity
  investment and risk management, which is direction 1.
- **ENERPOL**, the Horizon Europe doctoral network at CORE on energy inequality with
  **Jean Hindriks and François Maniquet**, which connects to the distributional side
  of your thesis.

Papavasiliou has moved to NTUA, so he stays a citation and is not offered as a
colleague.

### Still deliberately absent

The two-way fixed effects sign reversal, the master's Microeconomics 3,0, and the
Tunisia clause. All three were in earlier drafts and all three came out on your
instruction. Keep the sign reversal ready as an interview answer.


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
introduced auctions at different dates and then revised the rules on their own
national timetables, including whether technologies bid against each other in one
pot. That is variation of exactly the kind your thesis was built to handle, and the
statement offers it as the contribution a theory-trained candidate could not make.
The concrete case it names is Germany in April 2018.

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
