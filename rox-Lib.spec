%include  /usr/lib/rpm/macros.python
%define _name ROX-Lib
Summary:	A library for ROX applications
Summary(pl):	Biblioteka dla aplikacji ROXa
Name:		rox-Lib
Version:	0.1.4
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/rox/%{_name}-%{version}.tgz
URL:		http://rox.sourceforge.net/rox_lib.php3
BuildRequires:	rpm-pythonprov
Requires:	python-pygtk
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ROX-Lib contains shared code which can be used by other ROX
applications.

%description -l pl
ROX-Lib zawiera dzielone biblioteki, kt�re mog� by� u�ywane przez
inne aplikacje ROXa.

%prep
%setup -q -n %{_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{_name}/{bin,Help,python/rox}

install App* $RPM_BUILD_ROOT%{_libdir}/%{_name}
install bin/* $RPM_BUILD_ROOT%{_libdir}/%{_name}/bin
install python/rox/* $RPM_BUILD_ROOT%{_libdir}/%{_name}/python/rox
install Help/README $RPM_BUILD_ROOT%{_libdir}/%{_name}/Help

%py_comp $RPM_BUILD_ROOT%{_libdir}/%{_name}/python/rox
%py_ocomp $RPM_BUILD_ROOT%{_libdir}/%{_name}/python/rox

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/{Changes,Options,findrox.py,python}
%attr(755,root,root) %{_libdir}/%{_name}/AppRun
%attr(755,root,root) %{_libdir}/%{_name}/bin
%{_libdir}/%{_name}/AppI*
%{_libdir}/%{_name}/Help
%{_libdir}/%{_name}/python/rox/*.py[co]
%dir %{_libdir}/%{_name}
%dir %{_libdir}/%{_name}/python
%dir %{_libdir}/%{_name}/python/rox