%define installation_file atlassian-bitbucket-%{_build_version}.tar.gz
%define installation_basepath /opt/atlassian
%define installation_path %{installation_basepath}/bitbucket
%define source_file https://www.atlassian.com/software/stash/downloads/binary/%{installation_file}

Name:           tregonai-atlassian-bitbucket
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps - Atlassian Bitbucket

Group:          DevOps
License:        Tregonai
Vendor:         DevOps
URL:            https://www.atlassian.com/software/bitbucket
SOURCE0:        %{source_file}

%description
Atlassian Bitbucket setup released by DevOps.

%pre
if [ "`grep -c '^doadmin:' /etc/passwd`" -ne 1 ]; then
    echo "User 'doadmin' does not exist." >&2
    exit 1
fi

%install
mkdir -p %{buildroot}/%{installation_basepath} %{buildroot}/%{_unitdir}
if [ ! -f /tmp/%{installation_file} ]; then
    wget %{source_file} --directory-prefix /tmp
fi
tar xzf /tmp/%{installation_file} --directory %{buildroot}/%{installation_basepath}
mv %{buildroot}/%{installation_basepath}/atlassian-bitbucket-%{_build_version} %{buildroot}/%{installation_path}
cp %{_sourcedir}/atlassian/bitbucket/bitbucket.service %{buildroot}/%{_unitdir}

%files
%defattr(-,doadmin,doadmin,-)
%{installation_path}
%{_unitdir}/bitbucket.service
