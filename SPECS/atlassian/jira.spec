%define installation_file atlassian-jira-software-%{_build_version}.tar.gz
%define installation_basepath /opt/atlassian
%define installation_path %{installation_basepath}/jira
%define source_file https://www.atlassian.com/software/jira/downloads/binary/%{installation_file}

Name:           tregonai-atlassian-jira
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps - Atlassian Jira

Group:          DevOps
License:        Tregonai
Vendor:         DevOps
URL:            https://www.atlassian.com/software/jira
SOURCE0:        %{source_file}

%description
Atlassian Jira setup released by DevOps.

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
mv %{buildroot}/%{installation_basepath}/atlassian-jira-software-%{_build_version}-standalone %{buildroot}/%{installation_path}
cp %{_sourcedir}/atlassian/jira/jira.service %{buildroot}/%{_unitdir}

%files
%defattr(-,doadmin,doadmin,-)
%{installation_path}
%{_unitdir}/jira.service
