%define	name	lpc10
%define	version	1.5

%define	major	_1
%define libname	%mklibname %{name} %{major}

Summary:	LPC-10 2400 bps Voice Coder
Name:		%{name}
Version:	%{version}
Release:	%mkrel 7
Group:		Sound
License:	distributable
URL:		http://www.arl.wustl.edu/~jaf/lpc/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-shared.patch
BuildRequires:	libtool

%description
LPC-10 2400 bps Voice Coder library and tools.

%package -n	%{libname}
Summary:	The shared LPC-10 2400 bps Voice Coder Library
Group:          System/Libraries

%description -n	%{libname}
LPC-10 2400 bps Voice Coder library and tools.

%package -n	%{libname}-devel
Summary:	LPC-10 2400 bps Voice Coder headers files
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
LPC-10 2400 bps Voice Coder headers and static library.

%prep

%setup -q
%patch -p1

%build

make -C \
    lpc55-C \
    CC="%{__cc}" \
    LIBDIR="%{_libdir}" \
    OPT="%{optflags} -fPIC"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

make -C lpc55-C \
    DESTDIR=%{buildroot} \
    LIBDIR="%{_libdir}" \
    install

cp -f lpc55-C/README README.tools
cp -f lpc55-C/lpc10/README README.lpc10

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc FAQ README README-1.0 README.lpc10 README.tools
%attr(0755,root,root) %{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%attr(0755,root,root) %{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*.h
%attr(0755,root,root) %{_libdir}/*.so
%attr(0644,root,root) %{_libdir}/*.la
%attr(0755,root,root) %{_libdir}/*.a


