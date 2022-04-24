# Nexus archive released by Sonatype contains their build no.
%define sonatype_build_version %{_build_version}-%{_nexus_release_no}
%define installation_file nexus-%{sonatype_build_version}-unix.tar.gz
%define installation_basepath /opt
%define installation_path %{installation_basepath}/nexus
# Sonatype hides the URL for downloading latest package. We have to download it from browser.
%define source_file /tmp/%{installation_file}

Name:           tregonai-sonatype-nexus
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps - Sonatype Nexus

Group:          DevOps
License:        Tregonai
Vendor:         DevOps
URL:            https://www.sonatype.com/products/nexus-repository
SOURCE0:        %{source_file}

%description
Sonatype Nexus setup released by DevOps.

%pre
if [ "`grep -c '^doadmin:' /etc/passwd`" -ne 1 ]; then
    echo "User 'doadmin' does not exist." >&2
    exit 1
fi

%install
mkdir -p %{buildroot}/%{installation_basepath} %{buildroot}/%{_unitdir} %{buildroot}/data/nexus
tar xzf /tmp/%{installation_file} --directory %{buildroot}/%{installation_basepath}
mv %{buildroot}/%{installation_basepath}/nexus-%{sonatype_build_version} %{buildroot}/%{installation_path}
cp %{buildroot}/%{installation_basepath}/sonatype-work/* %{buildroot}/data/nexus
cp %{_sourcedir}/sonatype/nexus.service %{buildroot}/%{_unitdir}

%files
%defattr(-,doadmin,doadmin,-)
%{installation_path}

%{_unitdir}/nexus.service
