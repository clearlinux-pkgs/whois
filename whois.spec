#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : whois
Version  : 5.5.2
Release  : 7
URL      : https://github.com/rfc1036/whois/archive/v5.5.2/whois-5.5.2.tar.gz
Source0  : https://github.com/rfc1036/whois/archive/v5.5.2/whois-5.5.2.tar.gz
Summary  : Intelligent WHOIS client
Group    : Development/Tools
License  : GPL-2.0
Requires: whois-bin = %{version}-%{release}
Requires: whois-license = %{version}-%{release}
Requires: whois-locales = %{version}-%{release}
Requires: whois-man = %{version}-%{release}
BuildRequires : pkgconfig(libidn2)

%description
In 1999 I wrote this Whois client from scratch because the alternatives
were obsolete or bloated.

%package bin
Summary: bin components for the whois package.
Group: Binaries
Requires: whois-license = %{version}-%{release}

%description bin
bin components for the whois package.


%package extras
Summary: extras components for the whois package.
Group: Default

%description extras
extras components for the whois package.


%package license
Summary: license components for the whois package.
Group: Default

%description license
license components for the whois package.


%package locales
Summary: locales components for the whois package.
Group: Default

%description locales
locales components for the whois package.


%package man
Summary: man components for the whois package.
Group: Default

%description man
man components for the whois package.


%prep
%setup -q -n whois-5.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570068109
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  HAVE_LIBIDN2=1 \
HAVE_ICONV=1 \
CONFIG_FILE=/etc/whois.conf


%install
export SOURCE_DATE_EPOCH=1570068109
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/whois
cp COPYING %{buildroot}/usr/share/package-licenses/whois/COPYING
%make_install BASEDIR=%{buildroot} prefix=/usr
%find_lang whois

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/whois

%files extras
%defattr(-,root,root,-)
/usr/bin/mkpasswd
/usr/share/man/man1/mkpasswd.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/whois/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/whois.1
/usr/share/man/man5/whois.conf.5

%files locales -f whois.lang
%defattr(-,root,root,-)

