Summary:	C++ interface for working with XML files
Summary(pl):	Interfejs C++ do pracy z plikami XML
Name:		libxml++
Version:	0.22.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libxmlplusplus/%{name}-%{version}.tar.gz
# Source0-md5:	096c53bb75a146f7c5b2478eb51db2b8
URL:		http://libxmlplusplus.sourceforge.net/
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxml++ is a C++ interface for the libxml XML parser library.

%description -l pl
libxml++ jest interfejsem C++ do biblioteki libxml.

%package devel
Summary:	Header files for libxml++
Summary(pl):	Pliki nag³ówkowe do libxml++
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libxml2-devel

%description devel
Header files for libxml++.

%description devel -l pl
Pliki nag³ówkowe do libxml++.

%package static
Summary:	Static libxml++ libraries
Summary(pl):	Biblioteka statyczna libxml++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libxml++ libraries.

%description static -l pl
Biblioteka statyczna libxml++.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
