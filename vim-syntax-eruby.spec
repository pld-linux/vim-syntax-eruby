
%define		_vimdatadir	%{_datadir}/vim/vimfiles

Summary:	Vim syntax: Highlight eruby code blocks within HTML
Summary(pl):	Opis sk³adni dla Vima: pod¶wietlanie bloków kodu eruby wewn±trz HTML-a
Name:		vim-syntax-eruby
Version:	2.0
Release:	0.2
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

%description
This script properly highlights <%...%>, <%=...%>, and <%#...%> as
ruby code within HTML.

%description -l pl
Ten skrypt w³a¶ciwie pod¶wietla <%...%>, <%=...%> i <%#...%> jako kod
w jêzyku ruby wewn±trz HTML-a.

%prep
%setup -q -c -T
install %{SOURCE0} eruby.vim
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
install eruby.vim $RPM_BUILD_ROOT%{_vimdatadir}/syntax

cat > $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{name}.vim <<-EOF
au BufNewFile,BufRead *.rhtml	setfiletype eruby
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*
%{_vimdatadir}/ftdetect/*
