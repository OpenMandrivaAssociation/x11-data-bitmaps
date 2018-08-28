Name:		x11-data-bitmaps
Version:	1.1.2
Release:	3
Summary:	Bitmaps that are shared between X applications
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/data/xbitmaps-%{version}.tar.bz2
Source1:	x11-data-bitmaps.rpmlintrc
License:	MIT
BuildRequires:	x11-util-macros	>= 1.1.5
BuildArch:	noarch

%description
Bitmaps that are shared between X applications

%prep
%autosetup -n xbitmaps-%{version}

%build
%configure --x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%make_install

%files
%doc COPYING
%dir %{_includedir}/X11/bitmaps
%{_includedir}/X11/bitmaps/*
%{_datadir}/pkgconfig/xbitmaps.pc
