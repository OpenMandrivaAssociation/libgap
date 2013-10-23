Name:		libgap
Version:	4.6.5
Release:	3%{?dist}
License:	GPLv2+

Summary:	C library version of the GAP kernel
URL:		https://bitbucket.org/vbraun/libgap
Source0:	https://bitbucket.org/vbraun/libgap/downloads/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
BuildRequires:	libtool
BuildRequires:	gap-devel
BuildRequires:	gap-libs
Patch0:		%{name}-arch.patch
Patch1:		%{name}-nogmp.patch

%description
LibGAP -- a C library version of the GAP kernel (http://www.gap-system.org)

LibGAP is essentially a fork of the upstream GAP kernel. It is developed
in its own repository at https://bitbucket.org/vbraun/libgap. This is
also where the spkg metadata is tracked.

%package	devel
Summary:	Development files for %{name}

Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This package contains the header files and development documentation
for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
# due to patching configure.ac in patch1
autoreconf -ifs

%build
export CFLAGS='%{optflags} -DSYS_DEFAULT_PATHS=\"%{_gap_dir}\"'
%configure --enable-shared --disable-static --without-gmp
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/*.la

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS
%doc COPYING
%doc README
%{_libdir}/%{name}.so.0*

%files		devel
%{_includedir}/gap
%{_libdir}/%{name}.so
