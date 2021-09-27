Name:		bossa
Version:	1.9.2
Release:	0.20210927.1
Summary:	Flash utility for Atmel's SAM ARM microcontrollers (e.g. Arduino)
Source0:	https://github.com/arduino/BOSSA/archive/refs/heads/nrf.tar.gz
License:	BSD 3-clause
Group:		System
BuildRequires:	wxqt3.1-devel
BuildRequires:	pkgconfig(readline)
Provides:	bossac = %{EVRD}

%description
BOSSA is a flash programming utility for Atmel's SAM family of flash-based ARM
microcontrollers (such as various Arduino boards).

The motivation behind BOSSA is to create a simple, easy-to-use, open source
utility to replace Atmel's SAM-BA software. BOSSA is an acronym for Basic Open
Source SAM-BA Application to reflect that goal.

%package ui
Summary:	Graphical frontend for the BOSSA Atmel SAM (e.g. Arduino) flash tool
Group:		System
Requires:	%{name} = %{EVRD}

%description ui
Graphical frontend for the BOSSA Atmel SAM (e.g. Arduino) flash tool

%prep
%autosetup -p1 -n BOSSA-nrf

%build
%make_build WXVERSION=3.1

%install
mkdir -p %{buildroot}%{_bindir}
install -c -m 755 bin/bossa* %{buildroot}%{_bindir}/

%files
%{_bindir}/bossa
%{_bindir}/bossash

%files ui
%{_bindir}/bossac
