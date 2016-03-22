Name:			puppet-openstacklib
Version:		XXX
Release:		XXX
Summary:		Puppet OpenStack Libraries
License:		Apache-2.0

URL:			https://launchpad.net/puppet-openstacklib

Source0:		https://github.com/openstack/puppet-openstacklib/archive/%{version}.tar.gz

BuildArch:		noarch

Requires:		puppet-apache
Requires:		puppet-inifile
Requires:		puppet-mysql
Requires:		puppet-stdlib
Requires:		puppet-rabbitmq
Requires:		puppet-postgresql
Requires:		puppet >= 2.7.0

%description
Puppet OpenStack Libraries

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/openstacklib/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/openstacklib/



%files
%{_datadir}/openstack-puppet/modules/openstacklib/


%changelog

