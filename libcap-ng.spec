#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcap-ng
Version  : 0.7.8
Release  : 25
URL      : https://people.redhat.com/sgrubb/libcap-ng/libcap-ng-0.7.8.tar.gz
Source0  : https://people.redhat.com/sgrubb/libcap-ng/libcap-ng-0.7.8.tar.gz
Summary  : An alternate posix capabilities library
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.0+ LGPL-2.1 LGPL-2.1+
Requires: libcap-ng-bin
Requires: libcap-ng-lib
Requires: libcap-ng-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : python3-dev

%description
Libcap-ng is a library that makes using posix capabilities easier

%package bin
Summary: bin components for the libcap-ng package.
Group: Binaries

%description bin
bin components for the libcap-ng package.


%package dev
Summary: dev components for the libcap-ng package.
Group: Development
Requires: libcap-ng-lib
Requires: libcap-ng-bin
Provides: libcap-ng-devel

%description dev
dev components for the libcap-ng package.


%package dev32
Summary: dev32 components for the libcap-ng package.
Group: Default
Requires: libcap-ng-lib32
Requires: libcap-ng-bin

%description dev32
dev32 components for the libcap-ng package.


%package doc
Summary: doc components for the libcap-ng package.
Group: Documentation

%description doc
doc components for the libcap-ng package.


%package lib
Summary: lib components for the libcap-ng package.
Group: Libraries

%description lib
lib components for the libcap-ng package.


%package lib32
Summary: lib32 components for the libcap-ng package.
Group: Default

%description lib32
lib32 components for the libcap-ng package.


%prep
%setup -q -n libcap-ng-0.7.8
pushd ..
cp -a libcap-ng-0.7.8 build32
popd

%build
export LANG=C
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/captest
/usr/bin/filecap
/usr/bin/netcap
/usr/bin/pscap

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libcap-ng.so
/usr/lib64/pkgconfig/libcap-ng.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcap-ng.so
/usr/lib32/pkgconfig/32libcap-ng.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcap-ng.so.0
/usr/lib64/libcap-ng.so.0.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcap-ng.so.0
/usr/lib32/libcap-ng.so.0.0.0
