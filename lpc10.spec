%define	major 0
%define libname %mklibname %{name}_ %{major}
%define devname %mklibname %{name} -d
%define _disable_lto 1

Summary:	LPC-10 2400 bps Voice Coder
Name:		lpc10
Version:	1.5
Release:	30
Group:		Sound
License:	distributable
Url:		http://www.arl.wustl.edu/~jaf/lpc/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-shared.patch
BuildRequires:	libtool

%description
LPC-10 2400 bps Voice Coder library and tools.

%package -n	%{libname}
Summary:	The shared LPC-10 2400 bps Voice Coder Library
Group:		System/Libraries
Obsoletes:	%{_lib}lpc10_1 < 1.5-15

%description -n	%{libname}
LPC-10 2400 bps Voice Coder library and tools.

%package -n	%{devname}
Summary:	LPC-10 2400 bps Voice Coder development files
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
LPC-10 2400 bps Voice Coder headers and static library.

%prep
%setup -q
%autopatch -p1

%build
make -C \
    lpc55-C \
    CC="gcc %{?ldflags}" \
    LIBDIR="%{_libdir}" \
    OPT="%{optflags} -fPIC"

%install
%makeinstall_std -C lpc55-C \
	LIBDIR=%{_libdir}


cp -f lpc55-C/README README.tools
cp -f lpc55-C/lpc10/README README.lpc10

%files
%doc FAQ README README-1.0 README.lpc10 README.tools
%{_bindir}/*

%files -n %{libname}
%{_libdir}/liblpc10.so.%{major}*

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/*.so

