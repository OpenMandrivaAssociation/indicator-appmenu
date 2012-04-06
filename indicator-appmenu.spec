Summary:	This indicator displays application menus on the panel
Name:		indicator-appmenu
Version:	0.3.2
Release:	1
License:	GPLv3
Group:		Graphical desktop/GNOME
Url:		http://launchpad.net/indicator-appmenu
Source0:	%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - 001_openSUSE_current-menu-dump_fix.patch - nmarques@opensuse.org 
#- Fixes current-menu-dump so that it picks up dbusmenu-dumper from _libexecdir and not from _libexecdir/dbusmenu.
# Sent upstream (lp#721491).
Patch0:	001_openSUSE_current-menu-dump_fix.patch

BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:	pkgconfig(dbusmenu-jsonloader-0.4)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(indicator3-0.4)
BuildRequires:	pkgconfig(libbamf3)
BuildRequires:	pkgconfig(libxslt)

%description
This package provides an indicator that hosts the menus from applications on
the panel. This application is a part of the Ayatana's Project.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files
%doc AUTHORS COPYING
%{_libexecdir}/current-menu
%{_libexecdir}/current-menu-dump
%{_libexecdir}/menu-pusher
%{_libexecdir}/mock-json-app
%{_libdir}/indicators3/

