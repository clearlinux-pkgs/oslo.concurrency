#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.concurrency
Version  : 2.6.0
Release  : 22
URL      : http://tarballs.openstack.org/oslo.concurrency/oslo.concurrency-2.6.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.concurrency/oslo.concurrency-2.6.0.tar.gz
Summary  : Oslo Concurrency library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.concurrency-bin
Requires: oslo.concurrency-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : coverage-python
BuildRequires : debtcollector-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : eventlet-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fasteners-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : futures-python
BuildRequires : greenlet-python
BuildRequires : hacking
BuildRequires : iso8601-python
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : monotonic-python
BuildRequires : mox3-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : oslo.config
BuildRequires : oslo.i18n-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : posix_ipc
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : retrying-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : wrapt-python

%description
==================
oslo.concurrency
==================
.. image:: https://img.shields.io/pypi/v/oslo.concurrency.svg
:target: https://pypi.python.org/pypi/oslo.concurrency/
:alt: Latest Version

%package bin
Summary: bin components for the oslo.concurrency package.
Group: Binaries

%description bin
bin components for the oslo.concurrency package.


%package python
Summary: python components for the oslo.concurrency package.
Group: Default
Requires: Babel-python
Requires: oslo.i18n-python
Requires: oslo.utils-python
Requires: retrying-python
Requires: iso8601-python
Requires: fasteners-python
Requires: six-python

%description python
python components for the oslo.concurrency package.


%prep
%setup -q -n oslo.concurrency-2.6.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lockutils-wrapper

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
