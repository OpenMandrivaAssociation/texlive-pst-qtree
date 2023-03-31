Name:		texlive-pst-qtree
Version:	15878
Release:	2
Summary:	Simple syntax for trees
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-qtree
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-qtree.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-qtree.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
