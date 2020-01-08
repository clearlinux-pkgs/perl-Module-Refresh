#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-Refresh
Version  : 0.17
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/Module-Refresh-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/Module-Refresh-0.17.tar.gz
Summary  : 'Refresh %INC files when updated on disk'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Module-Refresh-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)
BuildRequires : perl(Path::Class)

%description
No detailed description available

%package dev
Summary: dev components for the perl-Module-Refresh package.
Group: Development
Provides: perl-Module-Refresh-devel = %{version}-%{release}
Requires: perl-Module-Refresh = %{version}-%{release}

%description dev
dev components for the perl-Module-Refresh package.


%package perl
Summary: perl components for the perl-Module-Refresh package.
Group: Default
Requires: perl-Module-Refresh = %{version}-%{release}

%description perl
perl components for the perl-Module-Refresh package.


%prep
%setup -q -n Module-Refresh-0.17
cd %{_builddir}/Module-Refresh-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::Refresh.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/Module/Refresh.pm