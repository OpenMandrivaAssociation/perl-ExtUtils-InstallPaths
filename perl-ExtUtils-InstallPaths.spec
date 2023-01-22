%define upstream_name  	    ExtUtils-InstallPaths

Name:		perl-%{upstream_name}
Version:	0.012
Release:	1
Summary:	Build.PL install path logic made easy
License:	GPL or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/ExtUtils::InstallPaths
Source:		http://www.cpan.org/modules/by-module/ExtUtils/%{upstream_name}-%{version}.tar.gz
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	perl-devel
# For tests
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Build.PL install path logic made easy.

%prep
%autosetup -p1 -n %{upstream_name}-%{version} 
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install

%files 
%doc Changes
%{perl_vendorlib}/ExtUtils
%{_mandir}/man3/*
