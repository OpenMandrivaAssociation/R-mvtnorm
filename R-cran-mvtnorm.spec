%define modulename mvtnorm
%define realver 0.9-8
%define r_library %{_libdir}/R/library
%define _requires_exceptions libR.so

Summary:	Multivariate Normal and t Distributions for R
Name:		R-cran-%{modulename}
Version:	%(echo %{realver} | tr '-' '.')
Release:	%mkrel 1
License:	GPLv2
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
BuildRequires:	gcc-gfortran
BuildRequires:	texinfo
BuildRequires:	tetex-latex
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This R package computes multivariate normal and t probabilities, 
quantiles, random deviates and densities.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
