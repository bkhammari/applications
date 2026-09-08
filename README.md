# Applications

Personal repository of CVs, letters, research documents, and application
materials, organized by track: PhD, EU institutions, bridge internships,
industry, and scholarships.

---

## Applicant

**Baha Khammari**
M.Sc. Economics, University of Cologne (expected September 2026)
Düsseldorf, Germany
[LinkedIn](https://linkedin.com/in/baha-khammari) · [GitHub](https://github.com/bkhammari)

---

## Background

Master's student in Economics with a quantitative focus on causal inference and empirical policy evaluation. 6 ECTS remaining (one seminar paper), available from October 2026.

**Master's thesis (Grade: 1.0):** *How Equal is Equal Opportunity? Gender, Ethnic and Regional Disparities in Labor Market Outcomes of Higher Education Policies in Brazil.* Applied the Callaway & Sant'Anna (2021) heterogeneity-robust staggered DiD estimator with doubly-robust inference to ~5 million observations of Brazilian administrative microdata (RAIS and ProUni) across 558 microregions (2005 to 2019). Supervised by Prof. Dr. Pia Pinger and Anna Person, M.Sc.

Previous experience includes audit and financial analysis at **PwC Germany** (Assurance Solutions).

---

## Skills

| Domain | Tools & Methods |
|---|---|
| Econometrics & Causal Inference | R (`did`, `fixest`, `HonestDiD`, `tidyverse`, `ggplot2`), DiD (staggered, doubly-robust), IV, Panel Data, Event Studies, Bacon Decomposition |
| Data Engineering | `basedosdados` (BigQuery), SQL, administrative microdata (RAIS, ProUni, Census) |
| Financial Analysis | Excel (advanced, VBA), Power BI, audit methodology (PwC) |
| Languages | German (native), Tunisian Arabic (native), English (C1, IELTS Academic 8.0), French (B1, DELF) |

---

## Repository structure

```
applications/
├── README.md
├── .gitignore
│
├── cv/                     # CVs
│   ├── shared/OpenCV.cls   # Custom LaTeX CV class (ATS-optimised)
│   ├── academic/           # academic_cv.tex (English, PhD and scholarships)
│   └── professional/       # German industry CV (modular)
│
├── letters/                # Motivation and cover letters
│   ├── academic/           # PhD motivation letters (general + bonn, duesseldorf, rwi-essen)
│   ├── industry/           # Company cover letters (colliers = past interview)
│   └── templates/          # Reusable letter templates (EN, DE)
│
├── research/               # Thesis, proposal, abstract, statement
│   ├── thesis/             # Master_Thesis_Final.pdf
│   ├── proposal/           # research-proposal.tex (3-paper PhD design)
│   ├── abstracts/          # Standalone thesis abstract
│   └── statement.tex       # Research statement
│
├── phd/                    # PhD outreach hub (email drafts + tracker)
│   ├── README.md           # Master tracker: target, status, next action
│   ├── templates/          # Cold-email and reference-request templates
│   └── cologne/ bonn/ duesseldorf/ rwi-essen/ institutes/ international/
│
├── eu/                     # EU competitions and traineeships
│   ├── README.md           # Tracker: EPSO AD5, Blue Book
│   ├── epso-ad5.md         # AD5 competition (registered)
│   ├── blue-book.md        # Commission traineeship (deadline 4 Sep 2026)
│   └── ad5-prep/           # AD5 mock exams and abstract-reasoning trainer
│
├── apply/                  # The application workflow (posting -> letter -> tracker)
│   ├── new.py              # Scaffold an application, pick the CV, add the row
│   ├── track.py            # list / due / sent / set / note / summary
│   ├── tracker.csv         # One row per application, single source of truth
│   ├── templates/          # posting.md, letter-en.tex, letter-de.tex
│   └── applications/       # One folder per application
│
├── bridge/                 # Paid interim positions, Rhine-Ruhr and Frankfurt
│   ├── README.md           # Targets by city, and the case for E13 over internships
│   ├── private-sector.md   # Finance, consulting and industry
│   ├── pipeline.md         # The daily loop
│   └── email-*.md          # Research and policy internship templates
│
├── scholarships/           # Scholarship and grant materials
│
└── dashboards/             # Interactive HTML dashboards
    ├── deadlines.html      # Every deadline, requirement, and fit
    └── status.html         # Overall status across all tracks
```

### How to use

**Applying to a job.** Start here. `apply/new.py` takes a posting and produces the
folder, the letter to tailor, and the tracker row. `apply/track.py due` tells you
what is owed today. Full loop in [`apply/README.md`](apply/README.md).

```bash
python3 apply/new.py --employer "Frontier Economics" --role "Economic Analyst" \
    --track industry --location Cologne --deadline 2026-10-15 --lang en
python3 apply/track.py due
```

**CVs.** Two variants, both using the shared `OpenCV.cls` class. Compile with `pdflatex` locally or on Overleaf. `cv/academic/academic_cv.tex` is the single-file English CV for PhD, scholarships, and research. `cv/professional/cv.tex` is the modular German CV for industry roles.

**Letters.** Copy a template from `letters/templates/` into the right `letters/` subfolder, rename, and fill in. Tailored PhD motivation letters are in `letters/academic/`.

**Research.** `research/proposal/research-proposal.tex` is the full 3-paper PhD proposal. `research/statement.tex` is the research statement. `research/abstracts/` holds the standalone thesis abstract.

**PhD outreach.** `phd/README.md` is the master tracker for every PhD and doctoral-program contact, with status and next action. Ready-to-send email drafts live in the per-target subfolders, and reusable templates are in `phd/templates/`.

**EU track.** `eu/README.md` tracks the EPSO AD5 competition and the Blue Book traineeship. `eu/ad5-prep/` holds mock exams and an interactive abstract-reasoning trainer.

**Bridge internships.** `bridge/README.md` is the curated tracker of paid interim positions, sorted by whether the pay clears the target. Email templates sit alongside it.

**Dashboards.** `dashboards/` holds the interactive HTML views: `deadlines.html` for all deadlines and `status.html` for the overall picture across tracks. Open them in a browser.

---

## Target roles

- PhD positions in applied microeconomics, causal inference, and labour economics
- EU institutions (EPSO AD5, Blue Book traineeship)
- Paid research or policy internships (GIZ, KfW, Bundesbank, ECB, EIB)
- Scholarships and fellowships (DAAD, Studienstiftung, and similar)
- Research assistant and policy analyst positions

---

## References

Most programs require professors as referees, so the two formal referees are the
thesis-supervising professors. None are formally confirmed yet, and the CV states
"References available on request."

| Name | Affiliation | Role |
|---|---|---|
| Prof. Dr. Pia Pinger | University of Cologne | Master's thesis supervisor (professorial) |
| Univ.-Prof. Dr. Andreas Schabert | University of Cologne (CMR) | Bachelor's thesis supervisor |
| Anna Person, M.Sc. | University of Cologne | Direct thesis supervisor and grader; briefs Pinger's letter |
| Prof. Dr. Michael Krause | University of Cologne (CMR) | Seminar instructor; backup reference |

---

*Last updated: August 2026*
