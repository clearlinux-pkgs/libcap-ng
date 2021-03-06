#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcap-ng
Version  : 0.8.2
Release  : 36
URL      : https://people.redhat.com/sgrubb/libcap-ng/libcap-ng-0.8.2.tar.gz
Source0  : https://people.redhat.com/sgrubb/libcap-ng/libcap-ng-0.8.2.tar.gz
Summary  : An alternate posix capabilities library
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.0+ LGPL-2.1 LGPL-2.1+
Requires: libcap-ng-bin = %{version}-%{release}
Requires: libcap-ng-lib = %{version}-%{release}
Requires: libcap-ng-license = %{version}-%{release}
Requires: libcap-ng-man = %{version}-%{release}
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
Requires: libcap-ng-license = %{version}-%{release}

%description bin
bin components for the libcap-ng package.


%package dev
Summary: dev components for the libcap-ng package.
Group: Development
Requires: libcap-ng-lib = %{version}-%{release}
Requires: libcap-ng-bin = %{version}-%{release}
Provides: libcap-ng-devel = %{version}-%{release}
Requires: libcap-ng = %{version}-%{release}

%description dev
dev components for the libcap-ng package.


%package dev32
Summary: dev32 components for the libcap-ng package.
Group: Default
Requires: libcap-ng-lib32 = %{version}-%{release}
Requires: libcap-ng-bin = %{version}-%{release}
Requires: libcap-ng-dev = %{version}-%{release}

%description dev32
dev32 components for the libcap-ng package.


%package lib
Summary: lib components for the libcap-ng package.
Group: Libraries
Requires: libcap-ng-license = %{version}-%{release}

%description lib
lib components for the libcap-ng package.


%package lib32
Summary: lib32 components for the libcap-ng package.
Group: Default
Requires: libcap-ng-license = %{version}-%{release}

%description lib32
lib32 components for the libcap-ng package.


%package license
Summary: license components for the libcap-ng package.
Group: Default

%description license
license components for the libcap-ng package.


%package man
Summary: man components for the libcap-ng package.
Group: Default

%description man
man components for the libcap-ng package.


%prep
%setup -q -n libcap-ng-0.8.2
cd %{_builddir}/libcap-ng-0.8.2
pushd ..
cp -a libcap-ng-0.8.2 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609963827
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1609963827
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libcap-ng
cp %{_builddir}/libcap-ng-0.8.2/COPYING %{buildroot}/usr/share/package-licenses/libcap-ng/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/libcap-ng-0.8.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/libcap-ng/3ac522f07da0f346b37b29cd73a60f79e992ffba
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
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
/usr/include/cap-ng.h
/usr/lib64/libcap-ng.so
/usr/lib64/libdrop_ambient.so
/usr/lib64/pkgconfig/libcap-ng.pc
/usr/share/aclocal/*.m4
/usr/share/man/man3/capng_apply.3
/usr/share/man/man3/capng_apply_caps_fd.3
/usr/share/man/man3/capng_capability_to_name.3
/usr/share/man/man3/capng_change_id.3
/usr/share/man/man3/capng_clear.3
/usr/share/man/man3/capng_fill.3
/usr/share/man/man3/capng_get_caps_fd.3
/usr/share/man/man3/capng_get_caps_process.3
/usr/share/man/man3/capng_get_rootid.3
/usr/share/man/man3/capng_have_capabilities.3
/usr/share/man/man3/capng_have_capability.3
/usr/share/man/man3/capng_lock.3
/usr/share/man/man3/capng_name_to_capability.3
/usr/share/man/man3/capng_print_caps_numeric.3
/usr/share/man/man3/capng_print_caps_text.3
/usr/share/man/man3/capng_restore_state.3
/usr/share/man/man3/capng_save_state.3
/usr/share/man/man3/capng_set_rootid.3
/usr/share/man/man3/capng_setpid.3
/usr/share/man/man3/capng_update.3
/usr/share/man/man3/capng_updatev.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcap-ng.so
/usr/lib32/libdrop_ambient.so
/usr/lib32/pkgconfig/32libcap-ng.pc
/usr/lib32/pkgconfig/libcap-ng.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcap-ng.so.0
/usr/lib64/libcap-ng.so.0.0.0
/usr/lib64/libdrop_ambient.so.0
/usr/lib64/libdrop_ambient.so.0.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcap-ng.so.0
/usr/lib32/libcap-ng.so.0.0.0
/usr/lib32/libdrop_ambient.so.0
/usr/lib32/libdrop_ambient.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libcap-ng/3ac522f07da0f346b37b29cd73a60f79e992ffba
/usr/share/package-licenses/libcap-ng/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man7/libdrop_ambient.7
/usr/share/man/man8/captest.8
/usr/share/man/man8/filecap.8
/usr/share/man/man8/netcap.8
/usr/share/man/man8/pscap.8
