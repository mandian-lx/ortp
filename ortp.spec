%define major 8
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} -d

Summary:	Real-time Transport Protocol Stack
Name:		ortp
Version:	0.18.0
Release:	%mkrel 1
License:	LGPLv2+
Group:		Communications
URL:		http://linphone.org/ortp/
Source0:	http://download.savannah.gnu.org/releases-noredirect/linphone/ortp/sources/%{name}-%{version}.tar.gz
Source1:	http://download.savannah.gnu.org/releases-noredirect/linphone/ortp/sources/%{name}-%{version}.tar.gz.sig
BuildRequires:	openssl-devel
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
Obsoletes:	%{libname}5-devel

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
%defattr(-,root,root,-)
%{_libdir}/*.so.%{major}*

%files -n %{libnamedev}
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
%{_docdir}/%{name}/%{name}-%{version}
