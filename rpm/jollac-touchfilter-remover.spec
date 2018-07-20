Name:       jollac-touchfilter-remover

%define debug_package %{nil}

%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Jolla C Karman Filter Remover
Version:    0.2
Release:    1
Group:      Qt/Qt
License:    GPLv2
URL:        https://github.com/beidl/jollac-touchfilter-remover
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
Requires:   bash

%description
Jolla C Karman Filter Remover

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_libdir}/oneshot.d
cp jollac-touchfilter-remover %{buildroot}%{_libdir}/oneshot.d/

%files
%defattr(755,root,root,-)
%{_libdir}/oneshot.d/jollac-touchfilter-remover

%postun
%{_libdir}/oneshot.d/jollac-touchfilter-remover restore >/dev/null 2>&1 || :
