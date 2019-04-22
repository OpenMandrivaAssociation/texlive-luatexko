# revision 34018
# category Package
# catalog-ctan /macros/luatex/generic/luatexko
# catalog-date 2014-05-11 12:36:43 +0200
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-luatexko
Version:	1.24
Release:	1
Summary:	Typeset Korean with Lua(La)TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/luatexko
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexko.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexko.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a Lua(La)TeX macro package that supports typesetting
Korean documents. LuaTeX version 0.76+ and luaotfload package
version 2.2+ are required. This package also requires both cjk-
ko and xetexko packages for its full functionality.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/luatex/luatexko/luatexko-core.sty
%{_texmfdistdir}/tex/luatex/luatexko/luatexko-normalize.lua
%{_texmfdistdir}/tex/luatex/luatexko/luatexko-uhc2utf8.lua
%{_texmfdistdir}/tex/luatex/luatexko/luatexko.lua
%{_texmfdistdir}/tex/luatex/luatexko/luatexko.sty
%doc %{_texmfdistdir}/doc/luatex/luatexko/ChangeLog
%doc %{_texmfdistdir}/doc/luatex/luatexko/README
%doc %{_texmfdistdir}/doc/luatex/luatexko/luatexko-doc.pdf
%doc %{_texmfdistdir}/doc/luatex/luatexko/luatexko-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
