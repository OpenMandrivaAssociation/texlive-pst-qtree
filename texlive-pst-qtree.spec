# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-qtree
# catalog-date 2009-09-20 13:03:55 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-pst-qtree
Version:	20190228
Release:	1
Summary:	Simple syntax for trees
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-qtree
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-qtree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-qtree.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a qtree-like front end for PSTricks.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-qtree/pst-qtree.tex
%{_texmfdistdir}/tex/latex/pst-qtree/pst-qtree.sty
%doc %{_texmfdistdir}/doc/generic/pst-qtree/CHANGES
%doc %{_texmfdistdir}/doc/generic/pst-qtree/LICENSE
%doc %{_texmfdistdir}/doc/generic/pst-qtree/pst-qtree-manual.pdf
%doc %{_texmfdistdir}/doc/generic/pst-qtree/pst-qtree-manual.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090920-2
+ Revision: 755402
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090920-1
+ Revision: 719383
- texlive-pst-qtree
- texlive-pst-qtree
- texlive-pst-qtree
- texlive-pst-qtree

