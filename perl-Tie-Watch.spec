%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	Watch
Summary:	Tie::Watch - place watchpoints on Perl variables.
Name:		perl-Tie-Watch
Version:	1.0
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class module binds one or more subroutines of your devising to a
Perl variable.  All variables can have B<FETCH>, B<STORE> and B<DESTROY>
callbacks.  Additionally, arrays can define B<CLEAR>, B<EXTEND>,
B<FETCHSIZE>, B<POP>, B<PUSH>, B<SHIFT>, B<SPLICE>, B<STORESIZE>
and B<UNSHIFT> callbacks, and hashes can define B<CLEAR>, B<DELETE>,
B<EXISTS>, B<FIRSTKEY> and B<NEXTKEY> callbacks.  If these term are
unfamiliar to you, I I<really> suggest you read L<perltie>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%patch -p0
%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tie/Watch.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
