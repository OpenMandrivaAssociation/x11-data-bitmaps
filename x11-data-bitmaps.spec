Name:		x11-data-bitmaps
Version:	1.1.2
Release:	1
Summary:	Bitmaps that are shared between X applications
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/data/xbitmaps-%{version}.tar.bz2
Source1:	x11-data-bitmaps.rpmlintrc
License:	MIT
BuildRequires:	x11-util-macros	>= 1.1.5
Requires(pretrans):	bash
BuildArch:	noarch

%description
Bitmaps that are shared between X applications

%prep
%setup -q -n xbitmaps-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%pretrans 
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files
%doc COPYING
%dir %{_includedir}/X11/bitmaps
%{_includedir}/X11/bitmaps/*
%{_datadir}/pkgconfig/xbitmaps.pc
