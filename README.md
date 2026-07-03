# Bewerbungen — Application Documents

Personal repository of CVs, cover letters, and supporting application materials.

---

## Applicant

**Baha Khammari**  
M.Sc. Economics — University of Cologne (expected September 2026)  
Dusseldorf, Germany  
[LinkedIn](https://linkedin.com/in/baha-khammari) · [GitHub](https://github.com/bkhammari)

---

## Background

Master's student in Economics with a quantitative focus on causal inference and empirical policy evaluation. Currently completing a seminar paper on the EU Emissions Trading System (6 ECTS remaining).

**Master's thesis (Grade: 1.0):** *How Equal is Equal Opportunity? Gender, Ethnic and Regional Disparities in Labor Market Outcomes of Higher Education Policies in Brazil.* Applied the Callaway & Sant'Anna (2021) heterogeneity-robust staggered DiD estimator with doubly-robust inference to ~5 million observations of Brazilian administrative microdata (RAIS + ProUni) across 558 microregions (2005-2019). Key findings: non-monotonic dose-response (+3.04% wage effect in low-dose regions), TWFE bias demonstration, and heterogeneity by gender, ethnicity, and region. Supervised by Prof. Dr. Pia Pinger & Anna Person, M.Sc.

Previous experience includes audit and financial analysis at **PwC Germany**.

---

## Skills

| Domain | Tools & Methods |
|---|---|
| Econometrics & Causal Inference | R (`did`, `fixest`, `HonestDiD`, `tidyverse`, `ggplot2`), DiD (staggered, doubly-robust), IV, Panel Data, Event Studies, Bacon Decomposition |
| Data Engineering | `basedosdados` (BigQuery), SQL, administrative microdata (RAIS, ProUni, Census) |
| Financial Analysis | Excel (advanced, VBA), Power BI, audit methodology (PwC) |
| Languages | German (native), Tunisian Arabic (native), English (C2), French (B1), Italian (B1), Spanish (A2) |

---

## Repository Structure

```
bewerbungen/
├── README.md
├── cv/
│   ├── shared/
│   │   └── OpenCV.cls          # Custom LaTeX CV class
│   ├── academic/
│   │   └── academic_cv.tex     # Academic CV (English) — PhD applications
│   └── professional/
│       ├── cv.tex              # Professional CV (German) — industry roles
│       ├── education.tex       # Education section
│       ├── project.tex         # Professional experience section
│       ├── engagement.tex      # Extracurricular section
│       └── misc.tex            # Skills & languages section
├── anschreiben/                # Cover letters by company
│   ├── BNP/
│   ├── Colliers/
│   ├── Dior_LVMH/
│   ├── Douglas/
│   ├── GIZ/
│   ├── HAL/
│   ├── Henkel/
│   ├── LVMH/
│   ├── Loreal/
│   └── Vodafone/
└── templates/                  # Reusable LaTeX templates (scrlttr2)
```

### CV Files

Two CV variants, both using the shared `OpenCV.cls` class:

- **`cv/academic/academic_cv.tex`** — English, single-file academic CV for PhD supervision applications. Emphasises research experience (thesis results, methodology), econometric skills, and academic record.
- **`cv/professional/cv.tex`** — German, modular professional CV for industry roles. Pulls in section files (`education.tex`, `project.tex`, `misc.tex`).

Compile either file on Overleaf or locally with `pdflatex`.

### Cover Letters (`anschreiben/`)

Each subfolder contains the LaTeX source and compiled PDF for a specific application. Letters are written in German or English depending on the target company, and typeset using KOMA-Script (`scrlttr2`).

---

## Target Roles

- PhD positions in applied microeconomics / causal inference
- Research assistant / policy analyst positions
- Strategy & Corporate Development
- Data & Analytics
- FP&A / Business Intelligence

---

*Last updated: July 2026*
