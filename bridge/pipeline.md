# Application pipeline

A repeatable way to send 5 to 10 tailored applications a day for bridge roles,
without the quality collapsing into mass mail.

## First, split the two tracks

They need opposite strategies, and treating them as one job is what makes the
whole thing feel impossible.

**PhD positions are not a volume game.** There are not 5 to 10 to apply to in a
day. The German winter cycle is about six programmes on fixed dates between 15
January and 31 March, plus a few institutes and the international options. The
entire PhD effort is roughly 8 to 12 applications spread across three months.
What decides that outcome is references, the GRE decision for Bonn, and a
proposal tailored per programme. Volume does nothing here, and chasing it costs
you the tailoring that does matter.

**Bridge roles are a volume game.** RA posts, pre-doc posts, and paid internships
turn over constantly, many get few serious applicants, and reply rates are low
enough that throughput is what produces offers. This is where 5 to 10 a day is
the right target, and where the pipeline below applies.

## Why volume is possible without losing quality

Almost every part of an application is already written and sits in this repo: the
CV, the research proposal, the thesis abstract, and the boilerplate in
`email-research-internship.md` and `email-policy-internship.md`. The only
genuinely new writing per application is one paragraph, the one that proves you
read the posting.

That paragraph is also the only thing that decides whether the application reads
as tailored or as spam. So the pipeline automates everything else and spends the
saved time there.

## The five steps

1. **Source.** Collect open postings. Institute career pages (RWI, ZEW, DIW, ifo,
   IZA), employer pages (ECB, Bundesbank, KfW, BaFin, Destatis, GIZ), and boards (INOMICS and
   EconJobMarket for economics RA and pre-doc roles, Indeed and LinkedIn for the
   wider set). For the private-sector track, add the firm career pages listed in
   [`private-sector.md`](private-sector.md), since consulting and insurance rarely
   post to the economics boards.
2. **Qualify.** Reject fast on the hard criteria before reading any further.
3. **Draft.** For each survivor, take the matching template and write only the fit
   paragraph, quoting something concrete from the posting.
4. **Stage.** Put each draft where it can be reviewed and sent in seconds. Never
   auto-send.
5. **Track and follow up.** One row per application below, and one nudge after 10
   to 14 days of silence.

## Qualification filter

Reject immediately if any of these is true. Being ruthless here is what buys the
time for the drafting.

- Unpaid, or below 1,200 euros a month
- Requires current enrolment (Werkstudent, Pflichtpraktikum), since the M.Sc.
  finishes in September 2026
- Requires a completed PhD
- Requires a working language you do not have

## The fit paragraph, the only genuinely new part

Two or three sentences that could not have been written about any other employer.
A pattern that works:

> Your [team or project] works on [specific thing named in the posting]. My
> master's thesis [one clause connecting the method or the topic], and [one clause
> on the concrete skill they asked for]. I would like to bring that to [the thing
> they named].

If you cannot write that paragraph from the posting, the role is probably not a
real fit, which is useful information rather than a failure.

## Daily routine, about 90 minutes

- 30 minutes sourcing, collecting 15 to 20 postings into the tracker
- 20 minutes qualifying, which usually leaves 6 to 10
- 30 minutes drafting the fit paragraphs
- 10 minutes reviewing and sending

## Tracker

| Date | Employer | Role | Link | Pay | Status | Follow-up | Notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Status values: drafted, sent, replied, interview, rejected, closed.

## What Claude can run

Steps 1 to 4 can be done in a batch: search for openings, apply the qualification
filter, draft the fit paragraph and the full email per opening, and either write
them into this folder or create them directly as Gmail drafts ready to review.
Sending stays manual on purpose, so nothing goes out that you have not read.

To start a batch, either paste a set of postings, or say which sources and roles
to search and the filter above will be applied to whatever comes back.
