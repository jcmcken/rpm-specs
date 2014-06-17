%global debug_package %{nil} 

Name:           grok
Version:        0.9.2
Release:        1%{?dist}
Summary:        A powerful pattern matching system for parsing and processing text data such as logs.

Group:          Development/Libraries
License:        BSD     
URL:            https://github.com/jordansissel/grok
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gperf
BuildRequires:  make
BuildRequires:  pcre-devel
BuildRequires:  libevent-devel
BuildRequires:  tokyocabinet-devel
BuildRequires:  gcc
Requires:       tokyocabinet
Requires:       libevent
Requires:       pcre 

# Set an absolute path to default patterns
Patch:          grok-patterns-base.patch

%description
A powerful pattern matching system for parsing and processing text data such 
as logs.

%prep
%setup -q
%patch -p0

%build
make grok

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# remove debug junk
rm -rf /usr/lib/debug

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 0644 grok.1 $RPM_BUILD_ROOT%{_mandir}/man1/grok.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%package devel
Summary: Headers for developing programs that will use grok
Group: Development/Libraries

%description devel
This package contains the necessary header files needed for
developing with grok.

%files devel
%defattr(-,root,root,-)
%{_includedir}/*

%files
%defattr(-,root,root,-)
%attr(0755,root,root) %{_bindir}/grok
%attr(0755,root,root) %{_bindir}/discogrok
/usr/lib/*
%{_datadir}/*
%doc LICENSE
%doc CHANGELIST
%doc %{_mandir}/man1/grok.1.gz

%changelog
