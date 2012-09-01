%define pkgname	gtkmm
%define api_version 3.0
%define major 1
%define libname_orig %mklibname %{pkgname} %{api_version}
%define libname %mklibname %{pkgname} %{api_version} %{major}
%define develname %mklibname -d %{pkgname} %{api_version}

Name:		%{pkgname}%{api_version}
Summary:	C++ interface for popular GUI library gtk+
Version:	3.4.1
Release:	1
#gw lib is LGPL, tool is GPL
License:	LGPLv2+ and GPLv2+
Group:		System/Libraries
URL:		http://gtkmm.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz

BuildRequires:	xsltproc
BuildRequires:	pkgconfig(atkmm-1.6)
BuildRequires:	pkgconfig(cairomm-1.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(giomm-2.4)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(pangomm-1.4)
BuildRequires:	doxygen

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

%package	-n %{develname}
Summary:	Headers and development files of %{pkgname}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Obsoletes:	%{_lib}gtkmm3.0_1-static-devel
Obsoletes:	%{_lib}gtkmm3.0-static-devel

%description	-n %{develname}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{pkgname}.

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
%setup -qn %{pkgname}-%{version}

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING NEWS README
%{_libdir}/libgdkmm-%{api_version}.so.%{major}*
%{_libdir}/libgtkmm-%{api_version}.so.%{major}*

%files -n %{develname}
%doc PORTING ChangeLog
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/gtkmm-%{api_version}
%{_libdir}/gdkmm-%{api_version}
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_datadir}/doc/gtkmm-%{api_version}
%doc %{_datadir}/devhelp/books/*
