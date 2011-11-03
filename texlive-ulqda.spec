# revision 18835
# category Package
# catalog-ctan /macros/latex/contrib/ulqda
# catalog-date 2009-11-10 09:00:49 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-ulqda
Version:	1.1
Release:	1
Summary:	Support of Qualitative Data Analysis
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ulqda
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulqda.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulqda.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulqda.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-ulqda.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package is for use in Qualitative Data Analysis research.
It supports the integration of Qualitative Data Analysis (QDA)
research tasks, specifically for Grounded Theory, into the
LaTeX work flow. It assists in the analysis of textual data
such as interview transcripts and field notes by providing the
LaTeX user with macros which are used to markup textual
information -- for example, in-depth interviews.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/ulqda/ulqda.pl ulqda
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
