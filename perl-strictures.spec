#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	strictures
%include	/usr/lib/rpm/macros.perl
Summary:	Turn on strict and make all warnings fatal
#Summary(pl.UTF-8):	
Name:		perl-strictures
Version:	1.005002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/H/HA/HAARG/strictures-1.005002.tar.gz
# Source0-md5:	3003ab606c221b0f125496ee186c9f1c
URL:		http://search.cpan.org/dist/strictures/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Turn on strict and make all warnings fatal.

# %description -l pl.UTF-8
# TODO

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
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
