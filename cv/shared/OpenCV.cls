%----------------------------------------------------------------------%
% OpenCV.cls
%
% CV class for this repository. Article-based, one shared look, with the
% per-document tuning that used to be copy-pasted moved into class options.
%
% Options
%   compact   tighter margins and single line spacing, for a one-page CV.
%             Replaces the \geometry{...} plus \linespread{1.0} block that was
%             being pasted into every tuned copy by hand.
%   serif     Latin Modern roman instead of the sans default. The English
%             academic CV used this via \renewcommand{\familydefault} after the
%             fact, which is now an option.
%   noicons   plain-text contact line with no FontAwesome glyphs. Use it
%             whenever a machine will parse the CV. See the note below.
%
% Usage
%   \documentclass[compact]{../shared/OpenCV}
%   \cvname{...}\cvlocation{...}\cvemail{...}\cvphone{...}
%   \cvlinkedin{...}\cvgithub{...}
%   \begin{document}\cvheader
%
% Passing no options reproduces the previous behaviour exactly, so existing
% documents keep compiling and keep their page counts.
%
% === A note on the old "ATS-Optimised" claim ===
% The class loads glyphtounicode so that text extracts cleanly, which is right.
% But the FontAwesome icons in the contact line defeat it. Run pdftotext over a
% CV built with icons and the most important line on the page comes back as
%   Duesseldorf  Q b.e.khammari@gmail.com   +49 1520 9016956   ¯
% The envelope becomes Q, the LinkedIn mark becomes a macron, the phone becomes
% nothing. A parser reading that sees a stray letter glued to the email address.
% So: icons are the default because they look better to a human, and [noicons]
% exists for anywhere a system reads the file first.
%----------------------------------------------------------------------%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{OpenCV}[2026/09/16 CV class for the applications repository]

\newif\if@cvcompact\@cvcompactfalse
\newif\if@cvserif\@cvseriffalse
\newif\if@cvicons\@cviconstrue

\DeclareOption{compact}{\@cvcompacttrue}
\DeclareOption{serif}{\@cvseriftrue}
\DeclareOption{noicons}{\@cviconsfalse}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\LoadClass[a4paper,11pt]{article}

% === Text extraction: map glyphs back to Unicode ===
\input{glyphtounicode}
\pdfgentounicode=1

% babel is deliberately NOT loaded here. Loading it with a fixed language made
% the English CV fail with an option clash, because it asks for english and the
% class demanded ngerman. Each CV loads babel itself with the language it needs.
\RequirePackage{enumitem}
\RequirePackage[utf8]{inputenc}
\RequirePackage[empty]{fullpage}
\RequirePackage{amsmath}           % \text inside maths, used in thesis bullets
\RequirePackage[T1]{fontenc}
\RequirePackage{titlesec}
\RequirePackage{xcolor}
\RequirePackage{geometry}
\RequirePackage{parskip}

\if@cvicons
  \RequirePackage{fontawesome}
\fi

% === Typeface ===
\if@cvserif
  \RequirePackage{lmodern}
  \renewcommand{\familydefault}{\rmdefault}
\else
  \RequirePackage{tgheros}         % Helvetica/Arial clone, widely readable
  \renewcommand{\familydefault}{\sfdefault}
\fi

\definecolor{myblue}{RGB}{0,51,102}
\definecolor{lightgray}{RGB}{180,180,180}

\RequirePackage[colorlinks=true,
    linkcolor=myblue,
    urlcolor=myblue,
    citecolor=myblue,
    anchorcolor=myblue]{hyperref}

% No running head or foot. fancyhdr and lastpage used to be loaded to produce an
% empty one, which is what \pagestyle{empty} does on its own.
\pagestyle{empty}

% === Page geometry ===
\if@cvcompact
  \geometry{a4paper, portrait, left=0.65in, right=0.65in, top=0.5in, bottom=0.45in}
  \linespread{1.0}
\else
  \geometry{a4paper, portrait, left=0.75in, right=0.75in, top=0.6in, bottom=0.6in}
  \linespread{1.08}
\fi
\setlength{\tabcolsep}{0in}
\setlength{\parskip}{0pt}

% === Section headings: blue, thin light-gray rule ===
\titleformat{\section}
  {\vspace{6pt}\raggedright\large\bfseries\color{myblue}}
  {\thesection}{0em}{}
  [\vspace{-4pt}{\color{lightgray}\hrule height 0.5pt}\vspace{4pt}]
\titlespacing*{\section}{0pt}{8pt}{4pt}

% === Header fields ===
% Set what applies, leave the rest unset. \cvheader skips empty fields, so the
% same block works for a CV with GitHub and one without.
\def\@cvname{}\def\@cvlocation{}\def\@cvemail{}
\def\@cvphone{}\def\@cvlinkedin{}\def\@cvgithub{}

\newcommand{\cvname}[1]{\def\@cvname{#1}}
\newcommand{\cvlocation}[1]{\def\@cvlocation{#1}}
\newcommand{\cvemail}[1]{\def\@cvemail{#1}}
\newcommand{\cvphone}[1]{\def\@cvphone{#1}}
\newcommand{\cvlinkedin}[1]{\def\@cvlinkedin{#1}}
\newcommand{\cvgithub}[1]{\def\@cvgithub{#1}}

\newcommand{\cv@sep}{\quad$\cdot$\quad}

\newcommand{\cvheader}{%
  \vspace*{-1.5cm}
  \begin{center}
    \textbf{\Huge\@cvname} \\
    \vspace{5pt}
    \small
    \@cvlocation
    \ifx\@cvemail\empty\else
      \cv@sep\if@cvicons\faEnvelopeO\enskip\fi\href{mailto:\@cvemail}{\@cvemail}%
    \fi
    \ifx\@cvphone\empty\else
      \cv@sep\if@cvicons\faMobile\enskip\fi\@cvphone
    \fi
    \ifx\@cvlinkedin\empty\else
      \cv@sep\if@cvicons\faLinkedin\enskip\fi\href{https://www.\@cvlinkedin}{\@cvlinkedin}%
    \fi
    \ifx\@cvgithub\empty\else
      \cv@sep\if@cvicons\faGithub\enskip\fi\href{https://\@cvgithub}{\@cvgithub}%
    \fi
  \end{center}
  \vspace{-2pt}
}

% === Bullet points ===
\newcommand{\resumeItem}[1]{
    \item\small{#1}
}

% === Subheading: title and place on one line, role and dates on the next ===
\newcommand{\resumeSubheading}[4]{
    \item
    \vspace{3pt}
    \textbf{#1} \hfill \small{#2} \\[1pt]
    \textit{\small #3} \hfill \textit{\small #4}
    \vspace{-2pt}
}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0in, label={}, itemsep=2pt]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.35in, itemsep=1pt, topsep=2pt]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{2pt}}
