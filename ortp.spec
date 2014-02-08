%define major 9
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} -d

Summary:	Real-time Transport Protocol Stack
Name:		ortp
Version:	0.22.0
Release:	2
License:	LGPLv2+
Group:		Communications
URL:		http://linphone.org/ortp/
Source0:	http://download.savannah.gnu.org/releases-noredirect/linphone/ortp/sources/%{name}-%{version}.tar.gz
Source1:	http://download.savannah.gnu.org/releases-noredirect/linphone/ortp/sources/%{name}-%{version}.tar.gz.sig
BuildRequires:	pkgconfig(openssl)
BuildRequires:	doxygen

%description
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

%package -n	%{libname}
Summary:	Real-time Transport Protocol Stack
Group:		System/Libraries

%description -n	%{libname}
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

%package -n	%{libnamedev}
Summary:	Headers, libraries and docs for the oRTP library
Group:		Development/Other
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{libname}5-devel < 0.18.0

%description -n %{libnamedev}
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

This package contains header files and development libraries needed to
develop programs using the oRTP library.

%prep
%setup -q

%build
%configure2_5x \
    --disable-strict \
    --enable-shared \
    --disable-static \
    --enable-ipv6

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{libnamedev}
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
%{_docdir}/%{name}-%{version}

%changelog
* Wed Feb 01 2012 Andrey Bondrov <abondrov@mandriva.org> 0.18.0-1mdv2012.0
+ Revision: 770437
- New version 0.18.0

* Thu May 05 2011 Funda Wang <fwang@mandriva.org> 0.16.3-2
+ Revision: 669312
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Fri Aug 06 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.16.3-1mdv2011.0
+ Revision: 566539
- update to 0.16.3
- drop patch0, hasn't been applied for some time (and Fedora already dropped it)
- update source url

* Wed Apr 07 2010 Funda Wang <fwang@mandriva.org> 0.16.1-4mdv2010.1
+ Revision: 532520
- rebuild

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 0.16.1-3mdv2010.1
+ Revision: 511607
- rebuilt against openssl-0.9.8m

* Sun Sep 27 2009 Olivier Blin <blino@mandriva.org> 0.16.1-2mdv2010.0
+ Revision: 450190
- fix build by adding missing read() check on non-x86, because it
  fallbacks to reading /dev/random to get random data and never checks
  read() return value; as we're building with Werror, it fails to
  build (from Arnaud Patard)

* Sun Sep 20 2009 Funda Wang <fwang@mandriva.org> 0.16.1-1mdv2010.0
+ Revision: 444862
- New version 0.16.1

* Tue May 05 2009 Funda Wang <fwang@mandriva.org> 0.16.0-1mdv2010.0
+ Revision: 372136
- New version 0.16.0

* Wed Feb 18 2009 Emmanuel Andry <eandry@mandriva.org> 0.15.0-1mdv2009.1
+ Revision: 342649
- BR doxygen
- New version 0.15.0
- New major 8
- apply devel library policy
- fix license
- disable P0 (doesn't apply, and can't check if still needed because of ppc arch
- BR openssl-devel
- enable ipv6
- package doc

* Sat Oct 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.13.1-1mdv2009.1
+ Revision: 297027
- Fix File list
- Fix File list
- New version (needed by kdenetwork 4.1.71)

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-5mdv2009.0
+ Revision: 229672
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-3mdv2008.1
+ Revision: 179114
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 03 2007 Emmanuel Blindauer <blindauer@mandriva.org> 0.10.0-2mdv2007.0
+ Revision: 103558
- fix ppc build (patch 0)
- Import ortp

* Fri Jun 16 2006 Austin Acton <austin@mandriva.org> 0.10.0-2mdv2007.0
- major 5

* Fri Jun 16 2006 Austin Acton <austin@mandriva.org> 0.10.0-1mdv2007.0
- New release 0.10.0

* Thu Mar 09 2006 Austin Acton <austin@mandriva.org> 0.9.0-1mdk
- New release 0.9.0
- major 4
- move docs to devel package
- buildrequires gtk-doc

* Mon Feb 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1mdk
- 0.8.1

* Tue Dec 20 2005 Lenny Cartier <lenny@mandriva.com> 0.8.0-1mdk
- 0.8.0

* Wed Oct 26 2005 Francois-Xavier Kowalski <fix@hp.com>
- Add to oRTP distribution with "make rpm" target

