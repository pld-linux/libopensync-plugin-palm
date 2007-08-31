Summary:	OpenSync Plugin for palm
Name:		libopensync-plugin-palm
Version:	0.22
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	0c85fe8439856d7b38b3d10e183acf8f
URL:		http://www.opensync.org/
BuildRequires:	libopensync-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the palm-sync plugin based on the pilot-link library libpisock.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no -devel yet
rm -rf $RPM_BUILD_ROOT/usr/include/opensync-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/opensync/plugins/*.so
%{_libdir}/opensync/plugins/*.la
%attr(755,root,root) %{_libdir}/opensync/formats/*.so
%{_libdir}/opensync/formats/*.la
%{_datadir}/opensync/defaults/*
