%----------------------------------%
% ATS-Optimised CV Class
% Clean, airy layout with Helvetica
%----------------------------------%

\ProvidesPackage{smoothThemeCV}
\LoadClass[a4paper,11pt]{article}

% === ATS-CRITICAL: Unicode glyph mapping ===
\input{glyphtounicode}
\pdfgentounicode=1

% Required packages
\RequirePackage{enumitem}
\RequirePackage[utf8]{inputenc}
\RequirePackage[empty]{fullpage}
% babel is deliberately NOT loaded here. Loading it with a fixed language made the
% English CV fail with an option clash, because it asks for english and the class
% demanded ngerman. Each CV now loads babel itself with the language it needs.
\RequirePackage{latexsym}
\RequirePackage{amsmath}   % \text in maths, used in the thesis bullets
\RequirePackage{tabularx}
\RequirePackage{fontawesome}
\RequirePackage[T1]{fontenc}
\RequirePackage{tgheros}           % ATS-safe Helvetica/Arial clone
\renewcommand{\familydefault}{\sfdefault}
\RequirePackage{titlesec}
\RequirePackage{xcolor}

\definecolor{myblue}{RGB}{0,51,102}
\definecolor{lightgray}{RGB}{180,180,180}

\RequirePackage[colorlinks=true,
    linkcolor=myblue,
    urlcolor=myblue,
    citecolor=myblue,
    anchorcolor=myblue]{hyperref}

\RequirePackage{geometry}
\RequirePackage{lastpage}
\RequirePackage{fancyhdr}
\RequirePackage{parskip}

\renewcommand\headrulewidth{0pt}
\fancyhf{}
\pagestyle{fancy}

% === Page geometry: generous but one-page-friendly ===
\geometry{a4paper, portrait, left=0.75in, right=0.75in, top=0.6in, bottom=0.6in}
\setlength{\tabcolsep}{0in}
\setlength{\parskip}{0pt}

% === Comfortable line spacing ===
\linespread{1.08}

% === Section headings: blue, thin light-gray rule ===
\titleformat{\section}
  {\vspace{6pt}\raggedright\large\bfseries\color{myblue}}
  {\thesection}{0em}{}
  [\vspace{-4pt}{\color{lightgray}\hrule height 0.5pt}\vspace{4pt}]
\titlespacing*{\section}{0pt}{8pt}{4pt}

% === Bullet points: comfortable reading size ===
\newcommand{\resumeItem}[1]{
    \item\small{#1}
}

% === Subheading: clean hfill layout with breathing room ===
\newcommand{\resumeSubheading}[4]{
    \item
    \vspace{3pt}
    \textbf{#1} \hfill \small{#2} \\[1pt]
    \textit{\small #3} \hfill \textit{\small #4}
    \vspace{-2pt}
}

% Item symbols
\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

% List environments with breathing room
\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0in, label={}, itemsep=2pt]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.35in, itemsep=1pt, topsep=2pt]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{2pt}}