%bcond_without tests
%global srcname more-itertools

Name:           python-%{srcname}
Version:        8.5.0
Release:        2%{?dist}
Summary:        More routines for operating on Python iterables, beyond itertools
License:        MIT
URL:            https://github.com/erikrose/more-itertools
Source0:        %{pypi_source}
BuildArch:      noarch
# Exclude i686 arch. Due to a modularity issue it's being added to the
# x86_64 compose of CRB, but we don't want to ship it at all.
# See: https://projects.engineering.redhat.com/browse/RCM-72605
ExcludeArch:    i686

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-six

%global _description %{expand:
Python's itertools library is a gem - you can compose elegant solutions for
a variety of problems with the functions it provides. In more-itertools we
collect additional building blocks, recipes, and routines for working with
Python iterables.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%{python3} setup.py test
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst PKG-INFO
%{python3_sitelib}/more_itertools/
%exclude %{python3_sitelib}/more_itertools/tests
%{python3_sitelib}/more_itertools-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Jan 12 2021 Tomas Orsava <torsava@redhat.com> - 8.5.0-2
- Convert from Fedora to the python39 module in RHEL8
- Resolves: rhbz#1877430

* Wed Sep 09 2020 Lumír Balhar <lbalhar@redhat.com> - 8.5.0-1
- Update to 8.5.0 (#1873653)

* Wed Jul 29 2020 Miro Hrončok <mhroncok@redhat.com> - 8.4.0-1
- Update to 8.4.0
- Fixes rhbz#1778332

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 7.2.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 7.2.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 7.2.0-2
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Thomas Moschny <thomas.moschny@gmx.de> - 7.2.0-1
- Update to 7.2.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 aarem AT fedoraproject DOT org - 7.0.0-1
- Update to 7.0.0
- Drop python-2

* Sun Apr 01 2018 aarem AT fedoraproject DOT org - 4.1.0-1
- rebuit for 4.1.0 using Thomas Moschny modification to spec file

* Sat Mar 24 2018 Thomas Moschny <thomas.moschny@gmx.de> - 4.1.0-1
- Update to 4.1.0.
- Do not do  package tests.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.3-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 aarem AT fedoraproject DOT org - 2.3-1
- update to 2.3
* Fri Oct 14 2016 aarem AT fedoraproject DOT org - 2.2-4
- fixed missing sum in line 9 of spec file, per BZ #138195
* Sat Oct 8 2016 aarem AT fedoraproject DOT org - 2.2-3
- renamed spec file to match package as per BZ #1381029
-fixed bug (incorrect python3_provides) as per BZ #1381029
- use common macro for description as per suggestion in BZ #1381029

* Wed Oct 05 2016 aarem AT fedoraproject DOT org - 2.2-2
- separated python and python3 cases as per BZ #1381029

* Sun Oct 02 2016 aarem AT fedoraproject DOT org - 2.2-1
- initial packaging of 2.2 version
