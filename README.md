# Applications

Personal repository of CVs, cover letters, research documents, and supporting application materials.

---

## Applicant

**Baha Khammari**
M.Sc. Economics -- University of Cologne (expected September 2026)
Dusseldorf, Germany
[LinkedIn](https://linkedin.com/in/baha-khammari) · [GitHub](https://github.com/bkhammari)

---

## Background

Master's student in Economics with a quantitative focus on causal inference and empirical policy evaluation. 6 ECTS remaining (one seminar paper); available from October 2026.

**Master's thesis (Grade: 1.0):** *How Equal is Equal Opportunity? Gender, Ethnic and Regional Disparities in Labor Market Outcomes of Higher Education Policies in Brazil.* Applied the Callaway & Sant'Anna (2021) heterogeneity-robust staggered DiD estimator with doubly-robust inference to ~5 million observations of Brazilian administrative microdata (RAIS + ProUni) across 558 microregions (2005-2019). Supervised by Anna Person, M.Sc. & Prof. Dr. Pia Pinger.

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

## Repository Structure

```
applications/
├── README.md
├── .gitignore
│
├── cv/
│   ├── shared/
│   │   └── OpenCV.cls              # Custom LaTeX CV class (ATS-optimised, Helvetica)
│   ├── academic/
│   │   └── academic_cv.tex         # English academic CV -- PhD & scholarship applications
│   └── professional/
│       ├── cv.tex                   # German professional CV -- industry roles
│       ├── education.tex
│       ├── project.tex
│       ├── engagement.tex
│       └── misc.tex
│
├── cover-letters/
│   ├── academic/                    # PhD / postdoc / scholarship motivation letters
│   │   ├── motivation-letter.tex    # General academic motivation-letter template
│   │   ├── bonn/                    # BGSE: tailored letter + research proposal
│   │   ├── duesseldorf/             # HHU / DICE: tailored letter
│   │   └── rwi-essen/               # RWI: tailored letter
│   └── industry/                    # Company cover letters (German, scrlttr2)
│       └── colliers/
│
├── outreach/                        # PhD & research outreach hub (email drafts + tracker)
│   ├── README.md                    # Master tracker: every target, status, next action
│   ├── _templates/                  # Reusable email templates (supervisor, institute, internships)
│   ├── cologne/                     # Siegloch, Pinger, van Maarseveen, CGS note
│   ├── bonn/                        # Boneva (initial + follow-up)
│   ├── duesseldorf/                 # Schildberg-Hörisch, Südekum
│   ├── rwi-essen/                   # Bachmann (initial + reply)
│   ├── institutes/                  # ifo, ZEW, DIW
│   └── international/               # Netherlands, France, Belgium
│
├── administrative-applications/     # EU & public-sector tracks
│   ├── README.md                    # Tracker: EPSO AD5, Blue Book
│   ├── blue-book-traineeship.md     # Commission traineeship (deadline 4 Sep 2026)
│   └── epso-ad5.md                  # EU administrator competition
│
├── research/
│   ├── thesis/
│   │   └── Master_Thesis_Final.pdf  # Full master's thesis
│   ├── proposal/
│   │   └── research-proposal.tex    # PhD research proposal (3-paper design)
│   └── abstracts/
│       └── masters-thesis-abstract.tex  # Standalone thesis abstract for applications
│
├── scholarships/                    # Scholarship & grant application materials
│
└── templates/
    ├── cover-letter-de.tex          # German cover letter template (scrlttr2)
    ├── cover-letter-en.tex          # English cover letter template
    └── research-statement.tex       # Research statement / proposal template
```

### How to use

**CVs:** Two variants, both using the shared `OpenCV.cls` class. Compile with `pdflatex` locally or on Overleaf.

- `cv/academic/academic_cv.tex` -- single-file English CV for PhD supervision, scholarships, and research positions. Includes referees.
- `cv/professional/cv.tex` -- modular German CV for industry roles. Pulls in section files.

**Cover letters:** Copy a template from `templates/` into the appropriate `cover-letters/` subdirectory, rename, and fill in.

**Research statement:** Use `templates/research-statement.tex` for PhD proposals, fellowship applications, or scholarship essays. Adapt the section headings to the specific call.

**Thesis abstract:** `research/abstracts/masters-thesis-abstract.tex` is a ready-to-compile standalone abstract. Attach to applications that ask for a writing sample or thesis summary.

**Research proposal:** `research/proposal/research-proposal.tex` is a full PhD research proposal (3-paper design) extending the master's thesis to a comparative analysis of ProUni, FIES, and the Quota Law. Adapt the title page, timeline, and supervisor-fit sections per application.

**Outreach:** `outreach/README.md` is the master tracker for every PhD, doctoral-programme, and interim-position contact — who, status, and next action. Ready-to-send email drafts live in the per-target subfolders; reusable templates are in `outreach/_templates/`. Formal LaTeX letters stay under `cover-letters/academic/`.

---

## Target Roles

- PhD positions in applied microeconomics / causal inference / labour economics
- Research assistant / policy analyst positions
- Scholarship & fellowship applications (DAAD, Studienstiftung, etc.)
- Strategy & Corporate Development
- Data & Analytics / FP&A

---

## Referees

| Name | Role | Context |
|---|---|---|
| Anna Person, M.Sc. | PhD candidate, University of Cologne | Primary supervisor and grader of master's thesis |
| Univ.-Prof. Dr. Andreas Schabert | CMR, University of Cologne | Bachelor's thesis supervisor |
| Prof. Dr. Michael Krause | CMR, University of Cologne | Seminar instructor (Housing and the Macroeconomy) |

*Contact details in the academic CV and available on request.*

---

*Last updated: July 2026*
