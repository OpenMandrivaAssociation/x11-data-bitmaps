Name: x11-data-bitmaps
Version: 1.1.1
Release: %mkrel 2
Summary: Bitmaps that are shared between X applications
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/data/xbitmaps-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5

%description
Bitmaps that are shared between X applications

%prep
%setup -q -n xbitmaps-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%pre 
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files
%defattr(-,root,root)
%doc COPYING
%dir %{_includedir}/X11/bitmaps
%{_includedir}/X11/bitmaps/*
%{_datadir}/pkgconfig/xbitmaps.pc
