#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	strictures
Summary:	Turn on strict and make all warnings fatal
Summary(pl.UTF-8):	Włączenie trybu ścisłego i uczynienie wszystkich ostrzeżeń krytycznymi
Name:		perl-strictures
Version:	2.000006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/H/HA/HAARG/%{pdir}-%{version}.tar.gz
# Source0-md5:	35c14fd25320f32ff40e977feae95d0d
URL:		https://metacpan.org/release/strictures
%{?with_tests:BuildRequires:	perl-Test-Simple}
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Turn on strict and make all warnings fatal.

%description -l pl.UTF-8
Włączenie trybu ścisłego i uczynienie wszystkich ostrzeżeń
krytycznymi.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/strictures.pm
%{perl_vendorlib}/strictures
%{_mandir}/man3/strictures.3pm*
%{_mandir}/man3/strictures::extra.3pm*
