%define installation_file atlassian-confluence-%{_build_version}.tar.gz
%define installation_basepath /opt/atlassian
%define installation_path %{installation_basepath}/confluence
%define source_file https://www.atlassian.com/software/confluence/downloads/binary/%{installation_file}

Name:           tregonai-atlassian-confluence
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps - Atlassian Confluence

Group:          DevOps
License:        Tregonai
Vendor:         DevOps
URL:            https://www.atlassian.com/software/confluence
SOURCE0:        %{source_file}

%description
Atlassian Confluence setup released by DevOps.

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
mv %{buildroot}/%{installation_basepath}/atlassian-confluence-%{_build_version} %{buildroot}/%{installation_path}
# A 'run' plugin that connects to mysql requires an extra library
if [ ! -f /tmp/mysql-connector-java-5.1.31-bin.jar ]; then
    wget http://nexus/service/local/repositories/release/content/com/tregonai/devops/mysql-connector-java/5.1.31/mysql-connector-java-5.1.31-bin.jar --directory-prefix /tmp
fi
cp /tmp/mysql-connector-java-5.1.31-bin.jar %{buildroot}/%{installation_path}/confluence/WEB-INF/lib
cp %{_sourcedir}/atlassian/confluence/confluence.service %{buildroot}/%{_unitdir}

%files
%defattr(-,doadmin,doadmin,-)
%{installation_path}
%{_unitdir}/confluence.service
