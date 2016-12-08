%define oname oRTP
%define lname %(echo %oname | tr [:upper:] [:lower:])

%define major 12
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Real-time Transport Protocol Stack
Name:		%{lname}
Version:	0.27.0
Release:	1
License:	LGPLv2+
Group:		Communications
Url:		https://www.linphone.org/technical-corner/%{name}.html
#Source0:	https://github.com/BelledonneCommunications/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	http://download.savannah.gnu.org/releases-noredirect/linphone/%{name}/sources/%{name}-%{version}.tar.gz
Source1:	http://download.savannah.gnu.org/releases-noredirect/linphone/%{name}/sources/%{name}-%{version}.tar.gz.sig
Patch0:		%{name}-0.27.0-pkgconfig.patch

BuildRequires:	cmake
BuildRequires:	doxygen
#BuildRequires:	pkgconfig(openssl)

%description
%{oname} is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

#--------------------------------------------------------------------

%package -n	%{libname}
Summary:	Real-time Transport Protocol Stack
Group:		System/Libraries

%description -n	%{libname}
%{oname} is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

%files -n %{libname}
%{_libdir}/lib%{name}.so.*

#--------------------------------------------------------------------

%package -n	%{devname}
Summary:	Headers, libraries and docs for the %{oname} library
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains header files and development libraries needed to
develop programs using the %{oname} library.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/%{oname}/cmake/
%{_docdir}/%{oname}-%{version}
%doc README
%doc NEWS
%doc AUTHORS
%doc TODO
%doc ChangeLog
#doc INSTALL
%doc COPYING

#--------------------------------------------------------------------

%prep
%setup -q

# Apply all patches
%patch0 -p1 -b .orig

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Debug \
	-DENABLE_SHARED:BOOL=ON \
	-DENABLE_STATIC:BOOL=OFF \
	-DENABLE_DOC:BOOL=ON \
	-DENABLE_TESTS:BOOL=OFF
%make

%install
%makeinstall_std -C build

