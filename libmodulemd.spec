#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v2
# autospec commit: f032afc
#
# Source0 file verified with key 0x4FD1AEC3365AF7BF (ppisar@redhat.com)
#
Name     : libmodulemd
Version  : 2.14.0
Release  : 43
URL      : https://github.com/fedora-modularity/libmodulemd/releases/download/2.14.0/modulemd-2.14.0.tar.xz
Source0  : https://github.com/fedora-modularity/libmodulemd/releases/download/2.14.0/modulemd-2.14.0.tar.xz
Source1  : https://github.com/fedora-modularity/libmodulemd/releases/download/2.14.0/modulemd-2.14.0.tar.xz.asc
Summary  : Module metadata manipulation library
Group    : Development/Tools
License  : MIT
Requires: libmodulemd-bin = %{version}-%{release}
Requires: libmodulemd-data = %{version}-%{release}
Requires: libmodulemd-lib = %{version}-%{release}
Requires: libmodulemd-license = %{version}-%{release}
Requires: libmodulemd-man = %{version}-%{release}
Requires: libmodulemd-python = %{version}-%{release}
Requires: libmodulemd-python3 = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : file-dev
BuildRequires : glib-dev
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : help2man
BuildRequires : libxslt
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(popt)
BuildRequires : pkgconfig(rpm)
BuildRequires : pkgconfig(yaml-0.1)
BuildRequires : pygobject
BuildRequires : yaml-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
C Library for manipulating module metadata files.
See https://github.com/fedora-modularity/libmodulemd/blob/master/README.md for
more details.

%package bin
Summary: bin components for the libmodulemd package.
Group: Binaries
Requires: libmodulemd-data = %{version}-%{release}
Requires: libmodulemd-license = %{version}-%{release}

%description bin
bin components for the libmodulemd package.


%package data
Summary: data components for the libmodulemd package.
Group: Data

%description data
data components for the libmodulemd package.


%package dev
Summary: dev components for the libmodulemd package.
Group: Development
Requires: libmodulemd-lib = %{version}-%{release}
Requires: libmodulemd-bin = %{version}-%{release}
Requires: libmodulemd-data = %{version}-%{release}
Provides: libmodulemd-devel = %{version}-%{release}
Requires: libmodulemd = %{version}-%{release}

%description dev
dev components for the libmodulemd package.


%package lib
Summary: lib components for the libmodulemd package.
Group: Libraries
Requires: libmodulemd-data = %{version}-%{release}
Requires: libmodulemd-license = %{version}-%{release}

%description lib
lib components for the libmodulemd package.


%package license
Summary: license components for the libmodulemd package.
Group: Default

%description license
license components for the libmodulemd package.


%package man
Summary: man components for the libmodulemd package.
Group: Default

%description man
man components for the libmodulemd package.


%package python
Summary: python components for the libmodulemd package.
Group: Default
Requires: libmodulemd-python3 = %{version}-%{release}

%description python
python components for the libmodulemd package.


%package python3
Summary: python3 components for the libmodulemd package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libmodulemd package.


%prep
%setup -q -n modulemd-2.14.0
cd %{_builddir}/modulemd-2.14.0
pushd ..
cp -a modulemd-2.14.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697560775
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dwith_docs=false \
-Dwith_manpages=enabled  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dwith_docs=false \
-Dwith_manpages=enabled  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
mkdir -p %{buildroot}/usr/share/package-licenses/libmodulemd
cp %{_builddir}/modulemd-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libmodulemd/df8b6951986b90ed530a771fd3419725f7eaa4fb || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/modulemd-validator
/usr/bin/modulemd-validator

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Modulemd-2.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/modulemd-2.0/modulemd-build-config.h
/usr/include/modulemd-2.0/modulemd-buildopts.h
/usr/include/modulemd-2.0/modulemd-component-module.h
/usr/include/modulemd-2.0/modulemd-component-rpm.h
/usr/include/modulemd-2.0/modulemd-component.h
/usr/include/modulemd-2.0/modulemd-compression.h
/usr/include/modulemd-2.0/modulemd-defaults-v1.h
/usr/include/modulemd-2.0/modulemd-defaults.h
/usr/include/modulemd-2.0/modulemd-dependencies.h
/usr/include/modulemd-2.0/modulemd-deprecated.h
/usr/include/modulemd-2.0/modulemd-errors.h
/usr/include/modulemd-2.0/modulemd-module-index-merger.h
/usr/include/modulemd-2.0/modulemd-module-index.h
/usr/include/modulemd-2.0/modulemd-module-stream-v1.h
/usr/include/modulemd-2.0/modulemd-module-stream-v2.h
/usr/include/modulemd-2.0/modulemd-module-stream.h
/usr/include/modulemd-2.0/modulemd-module.h
/usr/include/modulemd-2.0/modulemd-obsoletes.h
/usr/include/modulemd-2.0/modulemd-packager-v3.h
/usr/include/modulemd-2.0/modulemd-profile.h
/usr/include/modulemd-2.0/modulemd-rpm-map-entry.h
/usr/include/modulemd-2.0/modulemd-service-level.h
/usr/include/modulemd-2.0/modulemd-subdocument-info.h
/usr/include/modulemd-2.0/modulemd-translation-entry.h
/usr/include/modulemd-2.0/modulemd-translation.h
/usr/include/modulemd-2.0/modulemd.h
/usr/lib64/libmodulemd.so
/usr/lib64/pkgconfig/modulemd-2.0.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libmodulemd.so.2.14.0
/usr/lib64/libmodulemd.so.2
/usr/lib64/libmodulemd.so.2.14.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmodulemd/df8b6951986b90ed530a771fd3419725f7eaa4fb

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/modulemd-validator.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
