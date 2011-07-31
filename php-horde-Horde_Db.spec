%define		status		stable
%define		pearname	Horde_Db
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Database Libraries
Name:		php-horde-Horde_Db
Version:	1.0.3
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	5a36e0e50ac33ff26c15628d52fe923c
URL:		https://github.com/horde/horde/tree/master/framework/Db/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Date <= 2.0.0
Requires:	php-horde-Horde_Exception <= 2.0.0
Requires:	php-horde-Horde_Support <= 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-horde-Horde_Autoloader
Suggests:	php-horde-Horde_Cache
Suggests:	php-horde-Horde_Log
Suggests:	php-mysql
Suggests:	php-mysqli
Suggests:	php-pdo
Conflicts:	php-horde-Horde_Date = 2.0.0
Conflicts:	php-horde-Horde_Exception = 2.0.0
Conflicts:	php-horde-Horde_Support = 2.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Autoloader.*) pear(Horde/Cache.*) pear(Horde/Log.*)

%description
Horde database/SQL abstraction layer

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%doc docs/Horde_Db/*
%attr(755,root,root) %{_bindir}/horde-db-migrate-component
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Db.php
%{php_pear_dir}/Horde/Db
