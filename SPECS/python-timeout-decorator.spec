%bcond_without tests
%global srcname timeout-decorator

Name:           python-%{srcname}
Version:        0.4.1
Release:        1%{?dist}
Summary:        Timeout decorator for Python

License:        MIT
URL:            https://github.com/pnpnpn/timeout-decorator
Source0:        %{pypi_source}

BuildArch:      noarch

%description
A python module which provides a timeout decorator.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A python module which provides a timeout decorator.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%{__python3} setup.py test
%endif

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/timeout_decorator
%{python3_sitelib}/timeout_decorator-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Aug 26 2019 Joel Capitao <jcapitao@redhat.com> - 0.4.1-1
- Initial packaging
