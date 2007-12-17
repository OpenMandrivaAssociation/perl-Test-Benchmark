
%define realname   Test-Benchmark
%define version    0.004
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Make sure something really is faster
Source:     http://www.cpan.org/modules/by-module/Test/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRequires: perl-devel
BuildRequires: perl(Benchmark)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Test::Tester)

BuildArch: noarch

%description
Sometimes you want to make sure that your "faster" algorithm really is
faster than the old way. This lets you check. It might also be useful to
check that your super whizzo XS or Inline::C version is actually faster.

This module is based on the standard L<Benchmark> module. If you have lots
of timings to compare and you don't want to keep running the same benchmarks
all the time, you can pass in a result object from C<Benchmark::timethis()>
instead of sub routine reference.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc META.yml CHANGES README
%{_mandir}/man3/*
%perl_vendorlib/*



