Summary:	OpenFabrics Alliance InfiniBand MAD library
Summary(pl.UTF-8):	Biblioteka OpenFabrics Alliance InfiniBand MAD
Name:		opensm
Version:	3.3.9
Release:	1
License:	BSD or GPL v2
Group:		Daemons
Source0:	http://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
# Source0-md5:	5e9b461073f7cfbafe0207e014796f9f
Patch0:		%{name}-link.patch
URL:		http://www.openfabrics.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libibumad-devel
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libibmad provides low layer InfiniBand functions for use by the IB
diagnostic and management programs. These include MAD, SA, SMP, and
other basic IB functions.

%description -l pl.UTF-8
libibmad to biblioteka udostępniająca niskopoziomowe funkcje
InfiniBand przeznaczone dla programów diagnostycznych i zarządzających
IB. Obejmuje MAD, SA, SMP i inne podstawowe funkcje IB.

%package libs
Summary:	OpenSM (InfiniBand Subnet Manager) libraries
Summary(pl.UTF-8):	Biblioteki OpenSM (InfiniBand Subnet Manager)
Group:		Libraries

%description libs
OpenSM (InfiniBand Subnet Manager) libraries.

%description libs -l pl.UTF-8
Biblioteki OpenSM (InfiniBand Subnet Manager).

%package devel
Summary:	Header files for OpenSM libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek OpenSM
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libibumad-devel

%description devel
Header files for OpenSM libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek OpenSM.

%package static
Summary:	Static OpenSM libraries
Summary(pl.UTF-8):	Statyczne biblioteki OpenSM
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static OpenSM libraries.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne biblioteki OpenSM.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/opensm,/etc/rc.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT/etc/init.d $RPM_BUILD_ROOT/etc/rc.d

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/opensmd
%attr(755,root,root) %{_sbindir}/opensm
%attr(755,root,root) %{_sbindir}/osmtest
%{_mandir}/man8/opensm.8*
%{_mandir}/man8/osmtest.8*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README doc/*.txt
%attr(755,root,root) %{_libdir}/libopensm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopensm.so.4
%attr(755,root,root) %{_libdir}/libosmcomp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosmcomp.so.3
%attr(755,root,root) %{_libdir}/libosmvendor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosmvendor.so.3
%dir %{_sysconfdir}/opensm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopensm.so
%attr(755,root,root) %{_libdir}/libosmcomp.so
%attr(755,root,root) %{_libdir}/libosmvendor.so
%{_libdir}/libopensm.la
%{_libdir}/libosmcomp.la
%{_libdir}/libosmvendor.la
%{_includedir}/infiniband/complib
%{_includedir}/infiniband/iba
%{_includedir}/infiniband/opensm
%{_includedir}/infiniband/vendor

%files static
%defattr(644,root,root,755)
%{_libdir}/libopensm.a
%{_libdir}/libosmcomp.a
%{_libdir}/libosmvendor.a
