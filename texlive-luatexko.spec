%global tl_name luatexko
%global tl_revision 78005

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.7
Release:	%{tl_revision}.1
Summary:	Typeset Korean with Lua(La)TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/luatexko
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexko.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luatexko.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a Lua(La)TeX macro package that supports typesetting Korean
documents including Old Hangul texts. As LuaTeX has opened up access to
almost all the hidden routines of TeX engine, users can obtain more
beautiful outcome using this package rather than other Hangul macros
operating on other engines. LuaTeX version 1.10+ and luaotfload version
2.96+ are required for this package to run. This package also requires
the cjk-ko package for its full functionality.

