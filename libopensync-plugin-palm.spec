Summary:	OpenSync Plugin for palm
Summary(pl.UTF-8):	Wtyczka palm do OpenSync
Name:		libopensync-plugin-palm
Version:	0.22
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	0c85fe8439856d7b38b3d10e183acf8f
URL:		http://www.opensync.org/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pilot-link-devel >= 0.11.8
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the palm-sync plugin based on the pilot-link library
libpisock.

%description -l pl.UTF-8
Ten pakiet zawiera wtyczkę palm-sync do OpenSync opartą na bibliotece
pilot-link libpisock.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync/{plugins,formats}/*.la
# no -devel yet
rm -rf $RPM_BUILD_ROOT/usr/include/opensync-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/opensync/plugins/palm_sync.so
%attr(755,root,root) %{_libdir}/opensync/formats/palm.so
%{_datadir}/opensync/defaults/palm-sync

# devel
#%{_includedir}/opensync-1.0/opensync/palm_*.h
