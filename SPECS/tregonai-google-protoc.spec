%define installation_file google-protoc-%{_build_version}.tar.gz
%define installation_basepath /opt
%define installation_path %{installation_basepath}/google-protoc-%{_build_version}

Name:           tregonai-google-protoc%{_build_version}
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps - Google Protocol Buffers %{_build_version}

Group:          DevOps
License:        Tregoani
Vendor:         DevOps
URL:            https://<to-be-published>.com
SOURCE0:        https://github.com/google/protobuf

%description
Google protocol buffers setup released by DevOps.

%install
mkdir -p %{buildroot}/%{installation_basepath}
tar xzf /tmp/%{installation_file} --directory %{buildroot}/%{installation_basepath}
rm /tmp/%{installation_file}

%files
%defattr(-,root,root,-)
%{installation_path}
