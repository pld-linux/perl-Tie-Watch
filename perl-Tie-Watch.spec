#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Tie
%define		pnam	Watch
Summary:	Tie::Watch - place watchpoints on Perl variables
Summary(pl.UTF-8):	Tie::Watch - umieszczanie punktów śledzenia na zmiennych Perla
Name:		perl-Tie-Watch
Version:	1.301
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tie/SREZIC/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7ca00e8a3aeef60f6356fac46fec219c
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Tie-Watch/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class module binds one or more subroutines of your devising to a
Perl variable. All variables can have FETCH, STORE and DESTROY
callbacks. Additionally, arrays can define CLEAR, EXTEND, FETCHSIZE,
POP, PUSH, SHIFT, SPLICE, STORESIZE and UNSHIFT callbacks, and hashes
can define CLEAR, DELETE, EXISTS, FIRSTKEY and NEXTKEY callbacks. If
these term are unfamiliar to you, I really suggest you read
perltie(1).

%description -l pl.UTF-8
Ten moduł dowiązuje jedną lub więcej żądanych funkcji do perlowej
zmiennej. Wszystkie zmienne mogą mieć callbacki FETCH, STORE i
DESTROY. Dodatkowo, tablice mogą mieć zdefiniowane callbacki CLEAR,
EXTEND, FETCHSIZE, POP, PUSH, SHIFT, SPLICE, STORESIZE i UNSHIFT, a
hasze mogą mieć zdefiniowane callbacki CLEAR, DELETE, EXISTS, FIRSTKEY
i NEXTKEY. Jeżeli te nazwy nie wyglądają znajomo, dobrze jest
przeczytać manual perltie(1).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%patch0 -p0
%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Tie/Watch.pm
%{_mandir}/man3/Tie::Watch.3pm*
%{_examplesdir}/%{name}-%{version}
