%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	Watch
Summary:	Tie::Watch - place watchpoints on Perl variables
Summary(pl):	Tie::Watch - umieszczanie punktów ¶ledzenia na zmiennych
Name:		perl-Tie-Watch
Version:	1.0
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5: b55a9b34ff0125a9e059145c1719f326
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Ten modu³ dowi±zuje jedn± lub wiêcej ¿±danych funkcji do perlowej
zmiennej. Wszystkie zmienne mog± mieæ callbacki FETCH, STORE i
DESTROY. Dodatkowo, tablice mog± mieæ zdefiniowane callbacki CLEAR,
EXTEND, FETCHSIZE, POP, PUSH, SHIFT, SPLICE, STORESIZE i UNSHIFT, a
hasze mog± mieæ zdefiniowane callbacki CLEAR, DELETE, EXISTS, FIRSTKEY
i NEXTKEY. Je¿eli te nazwy nie wygl±daj± znajomo, dobrze jest
przeczytaæ manual perltie(1).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%patch -p0
%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Tie/Watch.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
