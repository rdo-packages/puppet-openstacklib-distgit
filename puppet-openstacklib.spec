%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-openstacklib
Version:        XXX
Release:        XXX
Summary:        Puppet OpenStack Libraries
License:        ASL 2.0

URL:            https://launchpad.net/puppet-openstacklib

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

Requires:       puppet-apache
Requires:       puppet-inifile
Requires:       puppet-mysql
Requires:       puppet-stdlib
Requires:       puppet-rabbitmq
#Requires:       puppet-postgresql
Requires:       puppet >= 2.7.0

%description
Puppet OpenStack Libraries

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n openstack-openstacklib-%{upstream_version}

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


# REMOVEME: error caused by commit https://opendev.org/openstack/puppet-openstacklib/commit/e61fb1e4e25ba64bd3159c86ef51699995acf2f8
