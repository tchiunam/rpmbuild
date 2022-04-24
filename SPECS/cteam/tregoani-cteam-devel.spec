%define installation_basepath /opt/cteam-devel

Name:           tregonai-cteam-devel
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        C Development Utilities

Group:          CTeam
License:        Tregonai
Vendor:         CTeam
URL:            https://<to-be-published>.com

%description
Utilities for C Development.

%install
mkdir -p %{buildroot}/%{installation_basepath}/bin
cp ~/rpmbuild/SOURCES/cteam/calculate-feature_version.sh %{buildroot}/%{installation_basepath}/bin
# This symlink is for backward compatibility. We should remove this after all plans are migrated to use it from /opt.
mkdir -p %{buildroot}/home/bamboo/bin
ln -s %{installation_basepath}/bin/calculate-feature_version.sh %{buildroot}/home/bamboo/bin/calculateFeatureVersion.sh

%files
%{installation_basepath}
# Make everything under /home/bamboo belong to CTeam as they are the only team which has script deployed here
/home/bamboo
