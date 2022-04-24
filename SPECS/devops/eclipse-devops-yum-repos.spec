Name:           tregonai-devops-yum-repos
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps Yum Repositories

Group:          DevOps
License:        Tregonai
Vendor:         DevOps
URL:            https://<to-be-published>.com

%description
Configure DevOps Yum Repositories.

%install
mkdir -p %{buildroot}/etc/pki/rpm-gpg %{buildroot}/etc/yum.repos.d
cp ~/rpmbuild/SOURCES/devops/tregonai-devops-repo/RPM-GPG-KEY-CentOS-DevOps %{buildroot}/etc/pki/rpm-gpg
cp ~/rpmbuild/SOURCES/devops/tregonai-devops-repo/tregonai-devops.repo %{buildroot}/etc/yum.repos.d

%files
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-DevOps
/etc/yum.repos.d/tregonai-devops.repo

%post
os_version=`cat /etc/centos-release`
os_version=`echo ${os_version#*release }`
os_version=`echo ${os_version% *}`
sed -i "s/OS_VERSION/${os_version}/" /etc/yum.repos.d/tregonai-devops.repo
# At the moment there is no perfect way to determine the environment of a host.
# Enable dev repo only if it is obviously a dev host.
if [[ `hostname` =~ dev ]]; then
    yum-config-manager --enable tregonai-devops-development
fi
