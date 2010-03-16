%define	major _1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	LPC-10 2400 bps Voice Coder
Name:		lpc10
Version:	1.5
Release:	%mkrel 10
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
rm -rf %{buildroot}

make -C lpc55-C \
    DESTDIR=%{buildroot} \
    LIBDIR="%{_libdir}" \
    install

cp -f lpc55-C/README README.tools
cp -f lpc55-C/lpc10/README README.lpc10

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

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
%attr(0644,root,root) %{_libdir}/*.la
%attr(0755,root,root) %{_libdir}/*.a
