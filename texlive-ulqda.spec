%global tl_name ulqda
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Support of Qualitative Data Analysis
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ulqda
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ulqda.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ulqda.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ulqda.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(ulqda.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is for use in Qualitative Data Analysis research. It
supports the integration of Qualitative Data Analysis (QDA) research
tasks, specifically for Grounded Theory, into the LaTeX work flow. It
assists in the analysis of textual data such as interview transcripts
and field notes by providing the LaTeX user with macros which are used
to markup textual information -- for example, in-depth interviews.

