%global packname  mvtnorm
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9_9992
Release:          1
Summary:          Multivariate Normal and t Distributions
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-9992.tar.gz
Requires:         R-stats 
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex 
BuildRequires:    R-stats 
BuildRequires:    pkgconfig(lapack)
%rename R-cran-mvtnorm

%description
Computes multivariate normal and t probabilities, quantiles, random
deviates and densities.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9_9992-1
+ Revision: 775052
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9_9991-1
+ Revision: 774867
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Tue Dec 29 2009 Jérôme Brenier <incubusss@mandriva.org> 0.9.8-1mdv2010.1
+ Revision: 483319
- import R-cran-mvtnorm

