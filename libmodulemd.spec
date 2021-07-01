#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmodulemd
Version  : 2.9.2
Release  : 28
URL      : https://github.com/fedora-modularity/libmodulemd/releases/download/libmodulemd-2.9.2/modulemd-2.9.2.tar.xz
Source0  : https://github.com/fedora-modularity/libmodulemd/releases/download/libmodulemd-2.9.2/modulemd-2.9.2.tar.xz
Summary  : No detailed summary available
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
BuildRequires : pkgconfig(rpm)
BuildRequires : pkgconfig(yaml-0.1)
BuildRequires : pygobject
BuildRequires : yaml-dev
Patch1: 0001-Fix-install-location-of-gi-overrides-file.patch

%description
[![Travis](https://img.shields.io/travis/fedora-modularity/libmodulemd.svg?style=plastic)](https://travis-ci.org/fedora-modularity/libmodulemd)
[![Travis](https://img.shields.io/coverity/scan/13739.svg?style=plastic)](https://scan.coverity.com/projects/sgallagher-libmodulemd)

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
%setup -q -n modulemd-2.9.2
cd %{_builddir}/modulemd-2.9.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586065944
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddeveloper_build=false \
-Dskip_formatters=true \
-Dwith_docs=false \
-Dwith_manpages=enabled  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libmodulemd
cp %{_builddir}/modulemd-2.9.2/COPYING %{buildroot}/usr/share/package-licenses/libmodulemd/df8b6951986b90ed530a771fd3419725f7eaa4fb
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/modulemd-validator

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Modulemd-2.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
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
/usr/lib64/libmodulemd.so.2
/usr/lib64/libmodulemd.so.2.9.2

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
