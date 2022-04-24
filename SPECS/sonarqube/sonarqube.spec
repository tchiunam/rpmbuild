%define installation_file sonarqube-%{_build_version}.zip
%define installation_basepath /opt
%define installation_path %{installation_basepath}/sonarqube
%define source_file https://sonarsource.bintray.com/Distribution/sonarqube/%{installation_file}

Name:           tregonai-sonarqube
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps - SonarQube

Group:          DevOps
License:        Tregonai
Vendor:         DevOps
URL:            https://www.sonarqube.org
SOURCE0:        %{source_file}

%description
SonarQube setup released by DevOps.

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
unzip /tmp/%{installation_file} -d %{buildroot}/%{installation_basepath}
mv %{buildroot}/%{installation_basepath}/sonarqube-%{_build_version} %{buildroot}/%{installation_path}
cp %{_sourcedir}/sonarqube/sonarqube.service %{buildroot}/%{_unitdir}

%files
%defattr(-,doadmin,doadmin,-)
%{installation_path}
%{_unitdir}/sonarqube.service
