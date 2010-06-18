%define version 2.90.3
%define release %mkrel 1

%define glibmm_version 2.24.0
%define pangomm_version 2.26
%define gtk_version 2.90.2

%define pkgname	gtkmm
%define api_version 3.0
%define major 1
%define libname_orig %mklibname %{pkgname} %{api_version}
%define libname %mklibname %{pkgname} %{api_version} %{major}
%define libnamedev %mklibname -d %{pkgname} %{api_version}
%define libnamestaticdev %mklibname -d -s %{pkgname} %{api_version}

Name:		%{pkgname}%{api_version}
Summary:	C++ interface for popular GUI library gtk+
Version:	%{version}
Release:	%{release}
#gw lib is LGPL, tool is GPL
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
URL:		http://gtkmm.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildRequires:	gtk+3-devel >= %{gtk_version}
BuildRequires:	glibmm2.4-devel >= %{glibmm_version}
BuildRequires:	atk-devel >= 1.9.0
BuildRequires:	cairomm-devel  >= 1.2.2
BuildRequires:	pangomm2.4-devel >= %pangomm_version

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package	-n %{libname}
Summary:	C++ interface for popular GUI library gtk+
Group:		System/Libraries
Provides:	%{libname_orig} = %{version}-%{release}
Provides:	%{pkgname}%{api_version} = %{version}-%{release}

%description	-n %{libname}
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains the library needed to run programs dynamically
linked with %{pkgname}.


%package	-n %{libnamedev}
Summary:	Headers and development files of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Requires:	glibmm2.4-devel >= %{glibmm_version}
Obsoletes: %mklibname -d %{pkgname} %{api_version} %{major}

%description	-n %{libnamedev}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{pkgname}.


%package	-n %{libnamestaticdev}
Summary:	Static libraries of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libnamedev} = %{version}
Provides:	%{libname_orig}-static-devel = %{version}-%{release}
Obsoletes: %mklibname -d -s %{pkgname} %{api_version} %{major}

%description	-n %{libnamestaticdev}
This package contains the static libraries of %{pkgname}.


%package	doc
Summary:	GTKmm documentation
Group:		Books/Other

%description	doc
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains all API documentation for gtkmm. You can readily read
this documentation with devhelp, a documentation reader.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x --enable-static --enable-shared
%make

# make check does nothing

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/libatkmm-1.6.so.%{major}*
%{_libdir}/libgdkmm-%{api_version}.so.%{major}*
%{_libdir}/libgtkmm-%{api_version}.so.%{major}*


%files -n %{libnamedev}
%defattr(-, root, root)
%doc PORTING ChangeLog
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/gtkmm-%{api_version}
%{_libdir}/gdkmm-%{api_version}
%{_libdir}/pkgconfig/*.pc

%files -n %{libnamestaticdev}
%defattr(-, root, root)
%doc COPYING
%{_libdir}/*.a

%files doc
%defattr(-, root, root)
%doc %{_datadir}/doc/gtkmm-%{api_version}
%doc %{_datadir}/devhelp/books/*
