Summary:	C++ interface for working with XML files
Summary(pl.UTF-8):   Interfejs C++ do pracy z plikami XML
Name:		libxml++
Version:	2.14.0
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libxml++/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	4f5644788dfd6ba87ce7c9b6cc28890d
URL:		http://libxmlplusplus.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibmm-devel >= 2.11.3
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
Requires:	glibmm >= 2.11.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxml++ is a C++ interface for the libxml XML parser library.

%description -l pl.UTF-8
libxml++ jest interfejsem C++ do biblioteki libxml.

%package devel
Summary:	Header files for libxml++
Summary(pl.UTF-8):   Pliki nagłówkowe do libxml++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel >= 2.11.3
Requires:	libxml2-devel >= 1:2.6.26

%description devel
Header files for libxml++.

%description devel -l pl.UTF-8
Pliki nagłówkowe do libxml++.

%package static
Summary:	Static libxml++ libraries
Summary(pl.UTF-8):   Biblioteka statyczna libxml++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxml++ libraries.

%description static -l pl.UTF-8
Biblioteka statyczna libxml++.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d docs_install/{manual,reference}
cp -R docs/manual/html/* docs_install/manual
cp -R docs/reference/2.14/html/* docs_install/reference

rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}-2.6/docs/{manual,reference/2.14}/html

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs_install/{manual,reference}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
