Name:		libgap
Version:	4.7.2
Release:	1.0%{?dist}
License:	GPLv2+

Summary:	C library version of the GAP kernel
URL:		https://bitbucket.org/vbraun/libgap
Source0:	https://bitbucket.org/vbraun/libgap/downloads/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
BuildRequires:	libtool
BuildRequires:	gap-devel
BuildRequires:	gap-libs
Patch0:		%{name}-nogmp.patch

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

%changelog
* Wed Jan 15 2014 Jerry James <loganjerry@gmail.com> - 4.7.2-1
- New upstream release
- Drop upstreamed -arch patch

* Tue Oct  8 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.6.5-3
- Only run x86 specific asm code on x86 (#919703#c17)
- Do not link to gmp as gmp interface is disabled (#919703#c17)

* Sat Oct  5 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.6.5-2
- Make CFLAGS an environment variable (#919703#c12)
- Add gap-libs to build requires (#919703#c12)
- Make package exclusive arch x86.

* Sat Oct  5 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.6.5-1
- Update to version matching rawhide gap (#919703#c8)

* Sat Sep 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.6.4.p0-1
- Update to latest version in bz (#919703#c4)

* Fri Feb 22 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.5.7-1
- Initial libgap spec.
