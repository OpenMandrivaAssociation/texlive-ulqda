Name:		texlive-ulqda
Version:	26313
Release:	1
Summary:	Support of Qualitative Data Analysis
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ulqda
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulqda.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulqda.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulqda.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-ulqda.bin = %{EVRD}

%description
The package is for use in Qualitative Data Analysis research.
It supports the integration of Qualitative Data Analysis (QDA)
research tasks, specifically for Grounded Theory, into the
LaTeX work flow. It assists in the analysis of textual data
such as interview transcripts and field notes by providing the
LaTeX user with macros which are used to markup textual
information -- for example, in-depth interviews.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/ulqda
%{_texmfdistdir}/scripts/ulqda/ulqda.pl
%{_texmfdistdir}/tex/latex/ulqda/ulqda.sty
%doc %{_texmfdistdir}/doc/latex/ulqda/README
%doc %{_texmfdistdir}/doc/latex/ulqda/ulqda.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ulqda/Makefile
%doc %{_texmfdistdir}/source/latex/ulqda/ulqda.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/ulqda/ulqda.pl ulqda
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
