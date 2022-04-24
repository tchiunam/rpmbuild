%define installation_file apache-maven-%{_build_version}-bin.tar.gz
%define installation_basepath /opt
%define installation_path %{installation_basepath}/apache-maven-%{_build_version}
%define source_file https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/%{_build_version}/%{installation_file}

Name:           tregonai-apache-maven%{_build_version}
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps - Apache Maven %{_build_version}

Group:          DevOps
License:        Tregoani
Vendor:         DevOps
URL:            https://<to-be-published>.com
SOURCE0:        %{source_file}

%description
Apache maven setup released by DevOps.

%install
mkdir -p %{buildroot}/%{installation_basepath}
wget %{source_file} --directory-prefix /tmp
tar xzf /tmp/%{installation_file} --directory %{buildroot}/%{installation_basepath}
rm /tmp/%{installation_file}

%files
%defattr(-,root,root,-)
%{installation_path}
