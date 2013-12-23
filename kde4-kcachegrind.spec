#
# TODO:
# - add man files
#
%define		orgname		kcachegrind
%define		_state		stable
%define		qtver		4.8.1

Summary:	KCachegrind - visualization of traces generated by profiling
Summary(pl.UTF-8):	KCachegrind - wizualizacja ścieżek tworzonych przez profilowanie
Name:		kde4-kcachegrind
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	aebb82c77d99838675b18d7a490d5d77
#Patch100: %{name}-branch.diff
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdesdk-kcachegrind
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KCachegrind visualizes traces generated by profiling.

%description -l pl.UTF-8
KCachegrind wizualizuje ścieżki tworzone przez profilowanie.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang	kcachegrind	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kcachegrind.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcachegrind
%attr(755,root,root) %{_bindir}/hotshot2calltree
%attr(755,root,root) %{_bindir}/op2calltree
%attr(755,root,root) %{_bindir}/pprof2calltree
%attr(755,root,root) %{_bindir}/dprof2calltree
%attr(755,root,root) %{_bindir}/memprof2calltree
%{_datadir}/apps/kcachegrind
%{_desktopdir}/kde4/kcachegrind.desktop
%{_iconsdir}/hicolor/*/apps/kcachegrind.png
