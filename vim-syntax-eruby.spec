
%define		_vimdatadir	%{_datadir}/vim/vimfiles

Summary:	Vim syntax: Highlight eruby code blocks within HTML
Summary(pl.UTF-8):   Opis składni dla Vima: podświetlanie bloków kodu eruby wewnątrz HTML-a
Name:		vim-syntax-eruby
Version:	2.0
Release:	1
# dunno, can't find license information.
License:	as-is
Group:		Applications/Editors/Vim
Source0:	http://vim.sourceforge.net/scripts/download_script.php?src_id=1505
# Source0-md5:	33843de6fab620e476e76b88f4a8e511
Patch0:		%{name}-delimiter.patch
URL:		http://vim.sourceforge.net/scripts/script.php?script_id=403
# for _vimdatadir existence
Requires:	vim >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_syntax eruby

%description
This script properly highlights <%...%>, <%=...%>, and <%#...%> as
ruby code within HTML.

%description -l pl.UTF-8
Ten skrypt właściwie podświetla <%...%>, <%=...%> i <%#...%> jako kod
w języku ruby wewnątrz HTML-a.

%prep
%setup -q -c -T
install %{SOURCE0} %{_syntax}.vim
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
install %{_syntax}.vim $RPM_BUILD_ROOT%{_vimdatadir}/syntax

cat > $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{_syntax}.vim <<-EOF
au BufNewFile,BufRead *.rhtml	set filetype=%{_syntax}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*
%{_vimdatadir}/ftdetect/*
