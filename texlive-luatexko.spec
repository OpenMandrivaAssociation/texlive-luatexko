Name:		texlive-luatexko
Version:	68243
Release:	1
Summary:	Typeset Korean with Lua(La)TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/luatexko
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexko.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexko.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/luatex/luatexko
%doc %{_texmfdistdir}/doc/luatex/luatexko

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
