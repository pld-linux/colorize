%include	/usr/lib/rpm/macros.perl
Summary:	Perl script to colorize logs
Summary(pl):	Skrypt w perlu do kolorowania logów
Name:		colorize
Version:	0.3.0
Release:	1
Group:		Applications/Text
License:	GPL
URL:		http://colorize.raszi.hu/
Source0:	http://colorize.raszi.hu/download/%{name}_%{version}.tar.gz
Requires:	perl
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a short perl script to colorize your logs. You can use your
own colors, you can simply modify your config file in your home
directory, or system-wide (/etc/colorize).

%description -l pl
Colorize jest krótkim skryptem w perlu który umo¿liwi Ci pokolorowanie
logów. Mo¿esz u¿ywaæ w³asnych schematów kolorów modyfikuj±c swój
w³asny plik konfiguracyjny lub ogólnosystemowy.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install colorize.pl $RPM_BUILD_ROOT%{_bindir}/colorize.pl
install colorize.pl.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/
install colorizerc $RPM_BUILD_ROOT%{_sysconfdir}/colorizerc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog.gz copyright examples/ README THANKS TIPS TODO
%attr(755,root,root) %{_bindir}/colorize.pl
%{_mandir}/man1/colorize.pl.1*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/colorizerc
