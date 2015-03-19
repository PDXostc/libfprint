Name:     libfprint
Summary:  An open source library to provide access to fingerprint scanning devices
Version:  0.6.0
Release:  1
Group:    Applications/Native Applications
License:  LGPL-2.1
URL:      http://www.freedesktop.org/wiki/Software/fprint/libfprint/
Source0:  http://people.freedesktop.org/~hadess/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(pixman-1)

%define debug_package %{nil}

%description
libfprint is an open source software library designed to make it easy for
application developers to add support for consumer fingerprint readers to
their software.

%prep
%autosetup

%build
%autogen
%configure --enable-x11-examples-build=no
make %{?_smp_mflags}

%install
%make_install

%check
make %{?_smp_mflags} check

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%license COPYING
%doc README
%{_includedir}/fprint.h
