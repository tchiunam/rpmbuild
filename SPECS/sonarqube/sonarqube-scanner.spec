%define installation_file sonar-scanner-cli-%{_build_version}.zip
%define installation_basepath /opt
%define installation_path %{installation_basepath}/sonar-scanner
%define source_file https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/%{installation_file}

Name:           tregonai-sonarqube-scanner
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps - SonarQube Scanner

Group:          DevOps
License:        Tregonai
Vendor:         DevOps
URL:            https://docs.sonarqube.org/latest/analysis/scan/sonarscanner
SOURCE0:        %{source_file}

%description
SonarQube Scanner setup released by DevOps.

%install
mkdir -p %{buildroot}/%{installation_basepath}
if [ ! -f /tmp/%{installation_file} ]; then
    wget %{source_file} --directory-prefix /tmp
fi
unzip /tmp/%{installation_file} -d %{buildroot}/%{installation_basepath}
mv %{buildroot}/%{installation_basepath}/sonar-scanner-%{_build_version} %{buildroot}/%{installation_path}

%files
%defattr(-,root,root,-)
%{installation_path}
