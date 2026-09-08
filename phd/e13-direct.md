# Going direct for an E13 position

Short answer to the question: **yes, this is possible, and it is how a large share
of German economics PhDs actually get hired.** The professors telling you it runs
through the graduate school are not wrong, but they are answering a different
question from the one worth asking.

_Last updated: September 2026._

## There are two hiring channels, not one

**Channel one, the structured programme.** BGSE in Bonn, CGS in Cologne, DGSE in
Düsseldorf, RGS in the Ruhr, MGSE in Munich, CDSE in Mannheim, the DIW Graduate
Center. Central admissions, one deadline a year, a cohort, a coursework year. No
individual professor decides this, which is exactly why they point you at it. It
is the honest answer to "will you take me as a doctoral student."

**Channel two, the chair position.** A professor holds a budget line, either core
university funding (Haushaltsstelle) or a third-party grant (Drittmittelstelle)
from the DFG, the ERC, a ministry, or a cluster. That line is a **job**, advertised
as *wissenschaftliche/r Mitarbeiter/in*, usually TV-L E13 at 65 or 75 percent. The
professor hires. There is no committee and no annual cycle. The doctorate is done
alongside, as an Individualpromotion, and the position and the PhD are the same
thing.

Both statements are true at once. A professor can say "we recruit through the
graduate school" and still have a project position opening in November. You have
only been asking about channel one.

## Why this matters more for you than for most people

The winter cycle deadlines run January to March for an **October 2027** start. That
is thirteen months of waiting, and it depends on reference letters you do not have
confirmed yet.

A chair position can start within weeks, is decided by one person who can simply
say yes, pays 2,700 to 3,000 euros gross at 65 percent E13, and is the PhD. It
solves the bridge problem and the PhD problem in one move. It is the single
highest-value thing you can do tomorrow.

## Ask a different question

This is the part that changes your reply rate, and it is why the answers so far
have been unhelpful.

Your emails have asked some version of "would you be available to discuss this
research field, or do you have any tips on who to contact." That is diffuse. A
busy professor reads it as a request for a meeting about someone else's career,
and the cheapest honest reply is "apply through the graduate school."

The E13 email asks something a professor can answer in one line without a meeting:
**do you have, or do you expect, a funded position.** Yes or no. Name the project
if you know it, state that you are available from October 2026, attach the CV, and
stop. Template in
[`templates/email-e13-inquiry.md`](templates/email-e13-inquiry.md).

## Where the positions actually are

### The trick almost nobody uses: find the grant, then write to the PI

A newly funded project has positions that **must** be filled, often before anything
is advertised. [GEPRIS](https://gepris.dfg.de), the DFG's public project database,
lists every funded project with its principal investigator, institution, and start
date. Search your terms in German (Bildungsungleichheit, Bildungsrenditen,
Arbeitsmarktungleichheit, Chancengleichheit), filter to universities in the region,
sort by recent, and write to the PIs of anything that started in the last year.

It is a JavaScript site, so open it in a browser rather than expecting a link to
work headlessly.

### One target that is close to a bullseye

**CRC TR 224 EPoS**, Bonn and Mannheim. A Collaborative Research Centre whose
Research Area A is literally *equality of opportunity*, which is your thesis
subject. It was **extended for another four years from 1 January 2026 with about
12 million euros**. A CRC that has just been refunded is staffing up, and Bonn is
thirty minutes from Cologne. Site: [crctr224.de](https://www.crctr224.de/).

### Boards worth checking, all reachable

| Where | What |
|---|---|
| [uni-bonn.de vacancies for researchers](https://www.uni-bonn.de/en/university/working-at-the-university/job-opportunities/vacancies-for-researchers) | Bonn, all faculties |
| [econ.uni-bonn.de jobs](https://www.econ.uni-bonn.de/en/department/jobs-1) | Bonn economics specifically |
| [econtribute.de/career](https://econtribute.de/career/) | The Bonn and Cologne excellence cluster |
| [jobportal.uni-koeln.de](https://jobportal.uni-koeln.de/) | Cologne |
| [academics.de](https://www.academics.de/) | The main German academic board |
| jobs.zeit.de | ZEIT Chancen, overlaps with academics.de |
| EURAXESS Germany | EU-wide, catches things the German boards miss |
| EconJobMarket, INOMICS | Economics-specific, more international |

Also check the vacancy pages of HHU Düsseldorf, Duisburg-Essen, Bochum, Dortmund,
Wuppertal, Münster, Aachen, Paderborn and Siegen directly. Regional universities
advertise on their own pages and often nowhere else, which is exactly why those
posts get fewer applicants.

### People in the region already in your network

You have more standing here than you are using.

- **Sonja Settele**, Cologne. Met you in person. Draft already written.
- **Johannes Wohlfart**, Cologne. Recommended by Neisser, draft already written.
- **Sebastian Siegloch**, Cologne. Emailed 8 September.
- **Pia Pinger**, Cologne. In the reference thread.
- **Christopher Roth**, Cologne and ECONtribute. Taught you, MSc Methods 1.7.
- **Roman Liesenfeld**, Cologne. Econometrics, 1.3.
- **Andreas Schabert**, Cologne. Supervised your bachelor's thesis.
- **IZA Bonn**, **briq**, **MPI for Research on Collective Goods**, Bonn.
- **RWI Essen**. Bachmann has no slot, but Westphal and Tamm are closer field fits
  and were never contacted directly.
- **DICE Düsseldorf**. The PhD programme was dropped, the E13 posts are separate.

Everyone in that list already knows your name or taught you. That is a different
email from a cold one.

## The honest caveat

Chair positions are competitive too, and a real share go to people the professor
already knows, often their own research assistants or thesis students. You have no
RA experience, which is a genuine gap here.

What works in your favour is volume and turnover. Positions open constantly rather
than once a year, regional universities get far fewer applicants than Bonn and
Cologne do, and a 1.0 thesis using Callaway and Sant'Anna on five million
administrative records is a real signal for anyone running an empirical project.

So expect a low hit rate per email and send a lot of them. That is what the
[`../apply/`](../apply/) workflow is for.

## What to do tomorrow

1. Open GEPRIS, search the German terms, list every recent project in the region.
2. Check the six boards above and note every E13 economics post.
3. Send the two drafts already sitting in Gmail, Settele and Wohlfart.
4. Email Roth, Liesenfeld and Schabert. They taught you, so these are warm.
5. Write to CRC TR 224 and to Westphal and Tamm at RWI.
6. Scaffold each one with `python3 apply/new.py --track research`.

Ten emails asking a yes-or-no question beats one asking for a meeting.
