%define	major _1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	LPC-10 2400 bps Voice Coder
Name:		lpc10
Version:	1.5
Release:	%mkrel 14
Group:		Sound
License:	distributable
URL:		http://www.arl.wustl.edu/~jaf/lpc/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-shared.patch
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
LPC-10 2400 bps Voice Coder library and tools.

%package -n	%{libname}
Summary:	The shared LPC-10 2400 bps Voice Coder Library
Group:          System/Libraries

%description -n	%{libname}
LPC-10 2400 bps Voice Coder library and tools.

%package -n	%{develname}
Summary:	LPC-10 2400 bps Voice Coder development files
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname lpc10 -d _1}

%description -n	%{develname}
LPC-10 2400 bps Voice Coder headers and static library.

%prep
%setup -q
%patch0 -p1

%build

make -C \
    lpc55-C \
    CC="gcc %{?ldflags}" \
    LIBDIR="%{_libdir}" \
    OPT="%{optflags} -fPIC"

%install
make -C lpc55-C \
    DESTDIR=%{buildroot} \
    LIBDIR="%{_libdir}" \
    install

cp -f lpc55-C/README README.tools
cp -f lpc55-C/lpc10/README README.lpc10

%files
%defattr(-,root,root)
%doc FAQ README README-1.0 README.lpc10 README.tools
%attr(0755,root,root) %{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*.h
%attr(0755,root,root) %{_libdir}/*.so


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5-12mdv2011.0
+ Revision: 666095
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-11mdv2011.0
+ Revision: 606419
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-10mdv2010.1
+ Revision: 520975
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.5-9mdv2010.0
+ Revision: 426004
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 1.5-8mdv2009.1
+ Revision: 364612
- use ldflags

* Wed Jun 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5-8mdv2009.0
+ Revision: 225116
- fix devel package naming

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.5-7mdv2008.1
+ Revision: 140933
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.5-7mdv2007.0
+ Revision: 71214
- Import lpc10

* Thu Aug 03 2006 Oden Eriksson <oeriksson@mandriva.com> 1.5-7mdv2007.0
- rebuild

* Sun May 14 2006 Stefan van der Eijk <stefan@eijk.nu> 1.5-6mdk
- BuildRequires:	libtool

* Sun Feb 19 2006 Oden Eriksson <oeriksson@mandriva.com> 1.5-5mdk
- fix the summary and deps

* Sun Mar 13 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.5-4mdk
- use the %%mkrel macro

* Tue Dec 28 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.5-3mdk
- lib64 fixes

* Sun Dec 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.5-2mdk
- lib64 fix

* Sun Sep 12 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.5-1mdk
- initial mandrake package, pld import

