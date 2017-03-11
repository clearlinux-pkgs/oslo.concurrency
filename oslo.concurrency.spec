#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD9631FEAF0CC6227 (infra-root@openstack.org)
#
Name     : oslo.concurrency
Version  : 3.15.0
Release  : 47
URL      : http://tarballs.openstack.org/oslo.concurrency/oslo.concurrency-3.15.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.concurrency/oslo.concurrency-3.15.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.concurrency/oslo.concurrency-3.15.0.tar.gz.asc
Summary  : Oslo Concurrency library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.concurrency-bin
Requires: oslo.concurrency-python
Requires: enum34
Requires: fasteners
Requires: iso8601
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: retrying
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

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

%description python
python components for the oslo.concurrency package.


%prep
%setup -q -n oslo.concurrency-3.15.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489272734
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489272734
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lockutils-wrapper

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
