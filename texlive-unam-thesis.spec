Name:		texlive-unam-thesis
Version:	51207
Release:	1
Summary:	Create documents according to the UNAM guidelines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unam-thesis
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unam-thesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unam-thesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a class for creating dissertation documents according
to the National Autonomous University of Mexico (UNAM)
guidelines.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/unam-thesis
%doc %{_texmfdistdir}/doc/latex/unam-thesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
