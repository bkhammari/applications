# Bewerbungen — Job Application Documents

Personal repository of cover letters, CVs, and supporting application materials for internships and graduate positions.

---

## Applicant

**Baha Khammari**  
M.Sc. Economics — Universität zu Köln (graduating March 2026)  
📍 Cologne, Germany  
🔗 [LinkedIn](https://linkedin.com/in/baha-khammari) · [GitHub](https://github.com/bkhammari)

---

## Background

Master's student in Economics with a quantitative focus on causal inference and empirical policy evaluation. Thesis: *Gender, Ethnic and Regional Disparities in Labor Market Outcomes of Higher Education Policies in Brazil* — using the Callaway & Sant'Anna difference-in-differences estimator applied to administrative data via the `basedosdados` package in R.

Previous experience includes audit and financial analysis at **PwC Germany**.

---

## Skills

| Domain | Tools & Methods |
|---|---|
| Econometrics & Causal Inference | R (`did`, `dplyr`, `fixest`, `ggplot2`), DiD, IV, Panel Data |
| Data Engineering | `basedosdados` (BigQuery), data wrangling, administrative datasets |
| Financial Analysis | Excel, PowerBI, audit methodology (PwC) |
| Languages | German (C1), English (C1), French (C1), Arabic (native) |

---

## Repository Structure

```
bewerbungen/
├── OpenCV.cls            # Custom LaTeX CV class
├── cv.tex                # Main CV file
├── education.tex         # Education section
├── engagement.tex        # Extracurricular / engagement section
├── project.tex           # Projects & thesis section
├── misc.tex              # Miscellaneous / skills section
├── anschreiben/          # Cover letters by company
│   ├── GIZ/
│   ├── Henkel/
│   ├── Vodafone/
│   ├── Dior_LVMH/
│   ├── LVMH/
│   ├── Loreal/
│   ├── Douglas/
│   ├── Colliers/
│   ├── HAL/
│   └── BNP/
└── templates/            # Reusable LaTeX templates (scrlttr2)
```

### CV Files

The CV is modularised into separate `.tex` files and compiled via `cv.tex` using the custom `OpenCV.cls` class. Edit individual section files (`education.tex`, `project.tex`, etc.) and recompile `cv.tex` on Overleaf or locally.

### Cover Letters (`anschreiben/`)

Each subfolder contains the LaTeX source and compiled PDF for a specific application. Letters are written in German or English depending on the target company, and typeset using KOMA-Script (`scrlttr2`).

---

## Target Roles

- Strategy & Corporate Development internships
- Data & Analytics internships
- FP&A / Business Intelligence roles
- Research assistant / policy analyst positions
- Graduate programmes in consulting, finance, or economics

---

*Last updated: March 2026*
