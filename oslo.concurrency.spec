#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9069B1335700CDC (infra-root@openstack.org)
#
Name     : oslo.concurrency
Version  : 3.20.0
Release  : 49
URL      : http://tarballs.openstack.org/oslo.concurrency/oslo.concurrency-3.20.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.concurrency/oslo.concurrency-3.20.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.concurrency/oslo.concurrency-3.20.0.tar.gz.asc
Summary  : Oslo Concurrency library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.concurrency-bin
Requires: oslo.concurrency-python
Requires: enum34
Requires: fasteners
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/oslo.concurrency.svg
:target: http://governance.openstack.org/reference/tags/index.html

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
%setup -q -n oslo.concurrency-3.20.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490883524
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1490883524
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lockutils-wrapper

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
