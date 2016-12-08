%define major 10
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Real-time Transport Protocol Stack
Name:		ortp
Version:	0.25.0
Release:	1
License:	LGPLv2+
Group:		Communications
Url:		http://linphone.org/ortp/
#Source0:	https://github.com/BelledonneCommunications/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	http://download.savannah.gnu.org/releases-noredirect/linphone/ortp/sources/%{name}-%{version}.tar.gz
Source1:	http://download.savannah.gnu.org/releases-noredirect/linphone/ortp/sources/%{name}-%{version}.tar.gz.sig
BuildRequires:	doxygen
BuildRequires:	pkgconfig(openssl)

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

%package -n	%{devname}
Summary:	Headers, libraries and docs for the oRTP library
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
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
%{_libdir}/libortp.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
%{_docdir}/%{name}-%{version}

