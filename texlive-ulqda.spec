# revision 26313
# category Package
# catalog-ctan /macros/latex/contrib/ulqda
# catalog-date 2009-11-10 09:00:49 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-ulqda
Version:	1.1
Release:	11
Summary:	Support of Qualitative Data Analysis
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ulqda
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulqda.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulqda.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ulqda.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/ulqda/ulqda.pl ulqda
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-3
+ Revision: 813137
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 757248
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719838
- texlive-ulqda
- texlive-ulqda
- texlive-ulqda

