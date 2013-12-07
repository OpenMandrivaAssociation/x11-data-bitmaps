Name:		x11-data-bitmaps
Version:	1.1.1
Release:	8
Summary:	Bitmaps that are shared between X applications
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/data/xbitmaps-%{version}.tar.bz2
License:	MIT
BuildRequires:	x11-util-macros	>= 1.1.5
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

%pre 
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files
%doc COPYING
%dir %{_includedir}/X11/bitmaps
%{_includedir}/X11/bitmaps/*
%{_datadir}/pkgconfig/xbitmaps.pc


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdv2011.0
+ Revision: 671112
- mass rebuild

* Thu Dec 09 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.1-1mdv2011.0
+ Revision: 617674
- Use configure2_5x
- Fix %%files definitions

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 464642
- New version: 1.1.0

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-8mdv2009.1
+ Revision: 351431
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-7mdv2009.0
+ Revision: 225939
- rebuild

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-6mdv2008.1
+ Revision: 153305
- Update BuildRequires and rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-5mdv2008.0
+ Revision: 75595
- rebuild


* Thu Jun 01 2006 Laurent Montel <lmontel@mandriva.com>
+ 2006-06-01 09:26:34 (31826)
- This package mustn't be "noarch'ed" otherwise it breaks
  compile on x86_64

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

