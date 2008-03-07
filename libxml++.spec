Summary:	C++ interface for working with XML files
Summary(pl.UTF-8):	Interfejs C++ do pracy z plikami XML
Name:		libxml++
Version:	2.22.0
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libxml++/2.22/%{name}-%{version}.tar.bz2
# Source0-md5:	9a9b3ba876fe212df3a73c5a97e9235a
Patch0:		%{name}-examples.patch
URL:		http://libxmlplusplus.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibmm-devel >= 2.12.7
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	pkgconfig
Requires:	glibmm >= 2.12.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxml++ is a C++ interface for the libxml XML parser library.

%description -l pl.UTF-8
libxml++ jest interfejsem C++ do biblioteki libxml.

%package devel
Summary:	Header files for libxml++
Summary(pl.UTF-8):	Pliki nagłówkowe do libxml++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.12.7
Requires:	libxml2-devel >= 1:2.6.28

%description devel
Header files for libxml++.

%description devel -l pl.UTF-8
Pliki nagłówkowe do libxml++.

%package static
Summary:	Static libxml++ libraries
Summary(pl.UTF-8):	Biblioteka statyczna libxml++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxml++ libraries.

%description static -l pl.UTF-8
Biblioteka statyczna libxml++.

%package apidocs
Summary:	libxml++ API documentation
Summary(pl.UTF-8):	Dokumentacja API libxml++
Group:		Documentation

%description apidocs
libxml++ API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libxml++.

%package examples
Summary:	libxml++ - example programs
Summary(pl.UTF-8):	libxml++ - przykładowe programy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
libxml++ - example programs.

%description examples -l pl.UTF-8
libxml++ - przykładowe programy.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-api-exceptions
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d docs_install/{manual,reference}
cp -R docs/manual/html/* docs_install/manual
cp -R docs/reference/2.*/html/* docs_install/reference

rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}-2.6/docs/{manual,reference/2.*}/html

# clean examples dir
%{__make} -C examples clean
find examples -type d -name .deps | xargs rm -rf

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libxml++-2.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxml++-2.6.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxml++-2.6.so
%{_libdir}/libxml++-2.6.la
%{_libdir}/libxml++-2.6
%{_includedir}/libxml++-2.6
%{_pkgconfigdir}/libxml++-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxml++-2.6.a

%files apidocs
%defattr(644,root,root,755)
%doc docs_install/{manual,reference}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
