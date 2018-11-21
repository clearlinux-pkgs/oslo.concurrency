#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : oslo.concurrency
Version  : 3.29.0
Release  : 54
URL      : http://tarballs.openstack.org/oslo.concurrency/oslo.concurrency-3.29.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.concurrency/oslo.concurrency-3.29.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.concurrency/oslo.concurrency-3.29.0.tar.gz.asc
Summary  : Oslo Concurrency library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.concurrency-bin = %{version}-%{release}
Requires: oslo.concurrency-license = %{version}-%{release}
Requires: oslo.concurrency-python = %{version}-%{release}
Requires: oslo.concurrency-python3 = %{version}-%{release}
Requires: enum34
Requires: fasteners
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.utils
Requires: pbr
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the oslo.concurrency package.
Group: Binaries
Requires: oslo.concurrency-license = %{version}-%{release}

%description bin
bin components for the oslo.concurrency package.


%package license
Summary: license components for the oslo.concurrency package.
Group: Default

%description license
license components for the oslo.concurrency package.


%package python
Summary: python components for the oslo.concurrency package.
Group: Default
Requires: oslo.concurrency-python3 = %{version}-%{release}

%description python
python components for the oslo.concurrency package.


%package python3
Summary: python3 components for the oslo.concurrency package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.concurrency package.


%prep
%setup -q -n oslo.concurrency-3.29.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542839462
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.concurrency
cp LICENSE %{buildroot}/usr/share/package-licenses/oslo.concurrency/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lockutils-wrapper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.concurrency/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
