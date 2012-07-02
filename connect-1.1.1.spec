Summary: Connect - make socket connections through a Socks 4/5 proxy.
Name: connect
Version: 1.1.1
Release: 1
License: Unknown
Group: Applications/Internet
Source: http://www.taiyo.co.jp/~gotoh/ssh/connect.c 
Patch0: connect-1.1.1-alic-20120105.patch
#BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Make socket connections through a Socks 4/5 proxy.
http://www.taiyo.co.jp/~gotoh/ssh/connect.c

%prep
%setup -T -c connect-1.1.1
cp $RPM_SOURCE_DIR/connect.c .
chmod -R a+rX,g-w,o-w connect.c

%patch -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/connect

%changelog
* Sun Sep 14 2010 Ali Craigmile <ali@craigmile.com>
- First iteration of SPEC file for connect.c
