%define ortp_glib 1

%define major 8
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} -d

Summary:	Real-time Transport Protocol Stack
Name:		ortp
Version:	0.16.1
Release:	%mkrel 2
License:	LGPLv2+
Group:		Communications
URL:		http://linphone.org/ortp/
Source0:	http://www.linphone.org/ortp/sources/%{name}-%{version}.tar.gz
Patch0:		ortp-ppcfix.patch
Patch1:		ortp_stun_rand.patch
%if %ortp_glib
BuildRequires:	glib2-devel
%endif
BuildRequires:	gtk-doc
BuildRequires:	openssl-devel
BuildRequires:	doxygen
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

%package -n	%{libname}
Summary:        Real-time Transport Protocol Stack
Group:		System/Libraries


%description -n	%{libname}
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

%package -n	%{libnamedev}
Summary:        Headers, libraries and docs for the oRTP library
Group:          Development/Other
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:       %{libname} = %{version}
Obsoletes:      %{libname}5-devel

%description -n %{libnamedev}
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

This package contains header files and development libraries needed to
develop programs using the oRTP library.

#define ortp_cflags %ortp_arch_cflags -Wall -g -pipe -pthread -O3 -fomit-frame-pointer -fno-schedule-insns -fschedule-insns2 -fstrict-aliasing

%prep
%setup -q
#%patch0 -p0
%patch1 -p1

%build
%configure2_5x \
    --enable-shared \
    --enable-static \
    --enable-glib \
    --enable-glibtest \
    --enable-gtk-doc \
    --enable-ipv6

%make  
#CXXFLAGS="%ortp_cflags"

%install
rm -rf %{buildroot}
%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/*.so.%{major}*

%files -n %{libnamedev}
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}
%if %ortp_glib
# `--enable-gtk-doc' does not work : cannot be disabled
%{_docdir}/%{name}/%{name}-%{version}/html
%endif



