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
%   mono      everything in black. Headings, rules and links. Recruiters
%             screening at volume say colour slows them down, and a German
%             public-sector application is conservative anyway. Use it for
%             industry, consulting and public-sector. Colour is fine on an
%             academic CV, which is read slowly by one person.
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
% === Layout is deliberately one column ===
% No sidebar, no two-column split, no boxes. Recruiters reading twenty to fifty
% CVs in half an hour report that extra columns slow them down, because the eye
% has to decide where to go next instead of running straight down the page. The
% \hfill pairs in \resumeSubheading put a place or a date on the right of a line,
% which is not the same thing and reads fine.
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
\newif\if@cvmono\@cvmonofalse

\DeclareOption{compact}{\@cvcompacttrue}
\DeclareOption{serif}{\@cvseriftrue}
\DeclareOption{noicons}{\@cviconsfalse}
\DeclareOption{mono}{\@cvmonotrue}
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
\RequirePackage{ragged2e}
\RequirePackage{microtype}         % protrusion and expansion, fewer bad lines

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

\if@cvmono
  \definecolor{myblue}{RGB}{0,0,0}
  \definecolor{lightgray}{RGB}{120,120,120}
\else
  \definecolor{myblue}{RGB}{0,51,102}
  \definecolor{lightgray}{RGB}{180,180,180}
\fi

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
  \linespread{1.06}
\else
  \geometry{a4paper, portrait, left=0.75in, right=0.75in, top=0.6in, bottom=0.6in}
  \linespread{1.12}
\fi
\setlength{\tabcolsep}{0in}
\setlength{\parskip}{0pt}

% === Ragged right, and hyphenate only as a last resort ===
% Justified setting is wrong for a CV, and badly wrong for a German one. The
% measure is narrow, the words are long compounds, and TeX pays for a flush
% right edge with stretched inter-word spaces and a broken word at the end of
% most lines. An earlier build of the German CV hyphenated Mikroregionen,
% verfuegbar, Jahresabschlusspruefungen, Schabert and Informationsveranstaltungen
% on one page. Ragged right spends the same space as ragged margin instead, which
% the eye does not notice, and keeps every word whole.
\AtBeginDocument{\RaggedRight}
\hyphenpenalty=2000
\tolerance=2000
\emergencystretch=2em

% === Section headings ===
\titleformat{\section}
  {\vspace{6pt}\raggedright\large\bfseries\color{myblue}}
  {\thesection}{0em}{}
  [\vspace{-3pt}{\color{lightgray}\hrule height 0.6pt}\vspace{5pt}]
% Space above a heading is what separates one section from the next, so it is
% worth more than the same space spent inside a section.
\titlespacing*{\section}{0pt}{11pt}{5pt}

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

% Each contact item is an \mbox, so a line break in the contact block falls
% between items and never between an icon and the text it belongs to. The old
% version let the LinkedIn glyph end one line while its URL started the next.
%
% The separator is a \discretionary whose no-break text is the dot and its
% spacing, and whose pre-break and post-break texts are empty. A contact block
% that has to wrap therefore ends the line after the last item rather than after
% a dangling separator, and starts the next one on an item rather than a dot.
\newcommand{\cv@sep}{\discretionary{}{}{\mbox{\hspace{0.6em}$\cdot$\hspace{0.6em}}}}

\newcommand{\cvheader}{%
  \vspace*{-1.5cm}
  \begin{center}
    \textbf{\huge\@cvname} \\
    \vspace{6pt}
    \small
    \mbox{\@cvlocation}%
    \ifx\@cvemail\empty\else
      \cv@sep\mbox{\if@cvicons\faEnvelopeO\enskip\fi\href{mailto:\@cvemail}{\@cvemail}}%
    \fi
    \ifx\@cvphone\empty\else
      \cv@sep\mbox{\if@cvicons\faMobile\enskip\fi\@cvphone}%
    \fi
    \ifx\@cvlinkedin\empty\else
      \cv@sep\mbox{\if@cvicons\faLinkedin\enskip\fi\href{https://www.\@cvlinkedin}{\@cvlinkedin}}%
    \fi
    \ifx\@cvgithub\empty\else
      \cv@sep\mbox{\if@cvicons\faGithub\enskip\fi\href{https://\@cvgithub}{\@cvgithub}}%
    \fi
  \end{center}
  \vspace{2pt}
}

% === Role-aligned qualifications ===
% A short block that maps the posting's stated requirements onto evidence, one
% line each, readable in well under ten seconds. Put it directly under a
% one-sentence profile on an English CV.
%
% Do not use this on a German Lebenslauf. The tabellarischer CV is conservative
% and the Anschreiben is mandatory there, so the letter already does this job.
% Adding an American-style qualifications block to a German public-sector
% application reads as foreign, the same reason the Profil block came out.
%
%   \section*{Qualifications for this role}
%   \begin{cvquals}
%     \cvqual{What they asked for}{What answers it.}
%   \end{cvquals}
\newenvironment{cvquals}
  {\begin{itemize}[leftmargin=0.2in, itemsep=2pt, topsep=3pt]}
  {\end{itemize}\vspace{2pt}}
\newcommand{\cvqual}[2]{\item\small{\textbf{#1} #2}}

% === Bullet points ===
\newcommand{\resumeItem}[1]{
    \item\small{#1}
}

% === Subheading: title and place on one line, role and dates on the next ===
% The two \hfill pairs are the only thing on the page that puts content at the
% right margin. That is alignment, not a second column, and it reads fine: the
% eye still runs straight down the left edge through the employers and degrees.
\newcommand{\resumeSubheading}[4]{
    \item
    \vspace{3pt}
    \textbf{#1} \hfill \small{#2} \\[2pt]
    \textit{\small #3} \hfill \textit{\small #4}
    \vspace{-1pt}
}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

% Entries are separated by more space than the bullets inside them, so a reader
% skimming for employers sees blocks rather than one continuous list.
\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0in, label={}, itemsep=5pt]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.3in, itemsep=3pt, topsep=4pt, parsep=0pt]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{1pt}}
