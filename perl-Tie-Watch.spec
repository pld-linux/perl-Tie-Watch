%include	/usr/lib/rpm/macros.perl
Summary:	Tie-Watch perl module
Summary(pl):	Modu� perla Tie-Watch
Name:		perl-Tie-Watch
Version:	1.0
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/Tie-Watch-%{version}.tar.gz
Patch0:		perl-Tie-Watch-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-Watch perl module.

%description -l pl
Modu� perla Tie-Watch.

%prep
%setup -q -n Tie-Watch-%{version}

%patch -p0
%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tie/Watch
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Tie/Watch.pm
%{perl_sitearch}/auto/Tie/Watch

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}-%{version}
