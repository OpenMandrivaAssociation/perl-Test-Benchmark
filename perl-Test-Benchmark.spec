%define realname   Test-Benchmark

Name:		perl-%{realname}
Version:	0.004
Release:    10
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Make sure something really is faster
Source:		http://www.cpan.org/modules/by-module/Test/%{realname}-%{version}.tar.gz
Url:		https://search.cpan.org/dist/%{realname}

BuildRequires:	perl-devel
BuildRequires:	perl(Benchmark)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::Tester)

BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

# Disable test - they are not so predictable inside ABF LXC containers
# %check
# %make test

%install
%makeinstall_std

%files
%doc META.yml CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/*

