Summary:	Download file manager (official core)
Summary(pl):	�ci�gacz plik�w (oficjalny)
Name:		edonkey2k-core
Version:	0.50
Release:	1
Epoch:		1
License:	unknown
Group:		Applications/Communications
Source0:	http://www.overnet.com/files/donkey%{version}.tar.gz
# Source0-md5:	1090c786b8575f3b59e8aea256fcfa1c
Source1:	%{name}.sh
URL:		http://ed2k-gtk-gui.sourceforge.net/core.shtml
Provides:	eDonkey-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Download file manager hosted by http://www.edonkey2000.com/

%description -l pl
�ci�gacz plik�w z http://www.edonkey2000.com/

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install donkey%{version} $RPM_BUILD_ROOT%{_bindir}/edonkey%{version}

ln -s %{_bindir}/edonkey%{version} $RPM_BUILD_ROOT%{_bindir}/edonkey

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/edonkey-conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
