%include	/usr/lib/rpm/macros.perl
Summary:	Perl script to colorize logs
Summary(pl):	Skrypt w Perlu do kolorowania log�w
Name:		colorize
Version:	0.3.4
Release:	1
Group:		Applications/Text
License:	GPL
URL:		http://colorize.raszi.hu/
Source0:	http://colorize.raszi.hu/download/%{name}_%{version}.tar.gz
# Source0-md5:	1fab421342cf02b4b6bc9ccb8234c232
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a short perl script to colorize your logs. You can use your
own colors, you can simply modify your config file in your home
directory, or system-wide (/etc/colorize).

%description -l pl
Colorize jest kr�tkim skryptem w Perlu umo�liwiaj�cym pokolorowanie
log�w. Mo�na u�ywa� w�asnych schemat�w kolor�w modyfikuj�c sw�j
w�asny plik konfiguracyjny lub og�lnosystemowy.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install colorize $RPM_BUILD_ROOT%{_bindir}/colorize
install colorize.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/
install colorizerc $RPM_BUILD_ROOT%{_sysconfdir}/colorizerc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog.gz copyright examples/ README THANKS TIPS TODO
%attr(755,root,root) %{_bindir}/colorize
%{_mandir}/man1/colorize.1*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/colorizerc
