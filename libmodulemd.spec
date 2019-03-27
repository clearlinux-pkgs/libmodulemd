#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmodulemd
Version  : 2.2.1
Release  : 12
URL      : https://github.com/fedora-modularity/libmodulemd/releases/download/libmodulemd-2.2.1/modulemd-2.2.1.tar.xz
Source0  : https://github.com/fedora-modularity/libmodulemd/releases/download/libmodulemd-2.2.1/modulemd-2.2.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: libmodulemd-bin = %{version}-%{release}
Requires: libmodulemd-data = %{version}-%{release}
Requires: libmodulemd-lib = %{version}-%{release}
Requires: libmodulemd-license = %{version}-%{release}
Requires: libmodulemd-python = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : glib-dev
BuildRequires : gobject-introspection
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt
BuildRequires : pygobject
BuildRequires : valgrind
BuildRequires : yaml-dev

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

%description dev
dev components for the libmodulemd package.


%package doc
Summary: doc components for the libmodulemd package.
Group: Documentation

%description doc
doc components for the libmodulemd package.


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


%package python
Summary: python components for the libmodulemd package.
Group: Default

%description python
python components for the libmodulemd package.


%prep
%setup -q -n modulemd-2.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553670172
export LDFLAGS="${LDFLAGS} -fno-lto"
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Ddeveloper_build=false \
-Dbuild_api_v1=true \
-Dbuild_api_v2=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libmodulemd
cp COPYING %{buildroot}/usr/share/package-licenses/libmodulemd/COPYING
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/modulemd-validator-v1

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Modulemd-1.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/modulemd/modulemd-buildopts.h
/usr/include/modulemd/modulemd-component-module.h
/usr/include/modulemd/modulemd-component-rpm.h
/usr/include/modulemd/modulemd-component.h
/usr/include/modulemd/modulemd-defaults.h
/usr/include/modulemd/modulemd-dependencies.h
/usr/include/modulemd/modulemd-deprecated.h
/usr/include/modulemd/modulemd-improvedmodule.h
/usr/include/modulemd/modulemd-intent.h
/usr/include/modulemd/modulemd-module.h
/usr/include/modulemd/modulemd-modulestream.h
/usr/include/modulemd/modulemd-prioritizer.h
/usr/include/modulemd/modulemd-profile.h
/usr/include/modulemd/modulemd-servicelevel.h
/usr/include/modulemd/modulemd-simpleset.h
/usr/include/modulemd/modulemd-subdocument.h
/usr/include/modulemd/modulemd-translation-entry.h
/usr/include/modulemd/modulemd-translation.h
/usr/include/modulemd/modulemd.h
/usr/lib64/libmodulemd.so
/usr/lib64/pkgconfig/modulemd.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/modulemd-1.0/ch01.html
/usr/share/gtk-doc/html/modulemd-1.0/home.png
/usr/share/gtk-doc/html/modulemd-1.0/index.html
/usr/share/gtk-doc/html/modulemd-1.0/left-insensitive.png
/usr/share/gtk-doc/html/modulemd-1.0/left.png
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.Buildopts.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.ComponentModule.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.ComponentRpm.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.Defaults.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.Dependencies.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.ImprovedModule.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.Intent.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.Module.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.ModuleStream.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.Prioritizer.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.Profile.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.ServiceLevel.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.SimpleSet.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.Subdocument.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.Translation.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.TranslationEntry.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-Modulemd.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0-ModulemdComponent.html
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0.devhelp2
/usr/share/gtk-doc/html/modulemd-1.0/modulemd-1.0.html
/usr/share/gtk-doc/html/modulemd-1.0/right-insensitive.png
/usr/share/gtk-doc/html/modulemd-1.0/right.png
/usr/share/gtk-doc/html/modulemd-1.0/style.css
/usr/share/gtk-doc/html/modulemd-1.0/up-insensitive.png
/usr/share/gtk-doc/html/modulemd-1.0/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmodulemd.so.1
/usr/lib64/libmodulemd.so.1.8.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmodulemd/COPYING

%files python
%defattr(-,root,root,-)
/usr/lib64/python*/*
