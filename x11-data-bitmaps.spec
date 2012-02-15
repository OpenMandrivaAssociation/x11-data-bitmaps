Summary: Bitmaps that are shared between X applications
Name: x11-data-bitmaps
Version: 1.1.1
Release: 3
Group: Development/X11
License: MIT
Url:	http://xorg.freedesktop.org/releases/individual/data/
Source0: http://xorg.freedesktop.org/releases/individual/data/xbitmaps-%{version}.tar.bz2

BuildRequires: x11-util-macros	>= 1.1.5

%description
Bitmaps that are shared between X applications

%package devel
Summary:    The pkgconfig for %{name}
Group:      Development/X11
Requires:   %{name} = %{version}

%description devel
The pkgconfig for %{name}.

%prep
%setup -qn xbitmaps-%{version}

%build
%configure2_5x \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%pre 
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files
%doc COPYING
%dir %{_includedir}/X11/bitmaps
%{_includedir}/X11/bitmaps/*

%files devel
%{_datadir}/pkgconfig/xbitmaps.pc
