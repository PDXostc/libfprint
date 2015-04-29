%define includedir %{_includedir}/libfprint/
%define pcdir %{_libdir}/pkgconfig/
%define libdir %{_libdir}/
%define udevdir %{_libdir}/udev/rules.d/
%define debug_package %{nil}

Name:           libfprint
Summary:        A library to provide access to fingerprint scanning devices
Version:        0.6.0
Release:        1
Group:          System/Libraries
License:        LGPL-2.1
URL:            http://www.freedesktop.org/wiki/Software/fprint/libfprint/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(udev)

%package devel
Summary:        Development files for libfprint
Group:          System/Development
Requires:       libfprint

%description
libfprint is an open source software library designed to make it easy for
application developers to add support for consumer fingerprint readers to
their software.

%description devel
This package contains all development files required for compiling with
libfprint.

%prep
%autosetup

%build
%autogen --disable-x11-examples-build
make %{?_smp_mflags}

%install
%make_install

%check
make %{?_smp_mflags} check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README NEWS AUTHORS
%{libdir}%{name}.so*
%{udevdir}60-fprint-autosuspend.rules

%files devel
%{includedir}fprint.h
%{pcdir}%{name}.pc
