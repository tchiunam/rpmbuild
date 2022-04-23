%define installation_file atlassian-bamboo-agent-installer-%{_build_version}.jar
%define installation_basepath /opt/atlassian
%define installation_path %{installation_basepath}/bamboo_agent
%define source_file /tmp/%{installation_file}

Name:           tregonai-atlassian-bamboo-agent
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps - Atlassian Bamboo Agent

Group:          DevOps
License:        Tregonai
Vendor:         DevOps
URL:            https://www.atlassian.com/software/bamboo
SOURCE0:        %{source_file}

%description
Atlassian Bamboo Agent setup released by DevOps.

%pre
if [ "`grep -c '^doadmin:' /etc/passwd`" -ne 1 ]; then
    echo "User 'doadmin' does not exist." >&2
    exit 1
fi

%install
mkdir -p %{buildroot}/%{installation_path} %{buildroot}/%{_unitdir}
cp %{source_file} %{buildroot}%{installation_path}
cp %{_sourcedir}/atlassian/bamboo/initialize-bamboo_agent_home.sh %{buildroot}/%{installation_path}
sed -i 's!JAR_FILE!%{installation_path}/%{installation_file}!' %{buildroot}/%{installation_path}/initialize-bamboo_agent_home.sh
cp %{_sourcedir}/atlassian/bamboo/bamboo_agent.service %{buildroot}/%{_unitdir}

%files
%defattr(-,doadmin,doadmin,-)
%{installation_path}
%{_unitdir}/bamboo_agent.service

%post
# Not set as part of installed files in order to support existence of multiple tregonai-atlassian applications
chown doadmin:doadmin %{installation_basepath}
