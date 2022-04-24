%define installation_basepath /opt/devops-common

Name:           tregonai-devops-common
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps Common

Group:          DevOps
License:        Tregonai
Vendor:         DevOps
URL:            https://<to-be-published>.com

%description
Common package by DevOps.

%install
mkdir -p %{buildroot}/%{installation_basepath}
cp -pr ~/rpmbuild/SOURCES/devops/tregonai-devops-common/* %{buildroot}/%{installation_basepath}
# Backup script is restricted to root only
chmod -R o-rx %{buildroot}/%{installation_basepath}/bin/backup

%files
%defattr(-,root,root,-)
%{installation_basepath}
