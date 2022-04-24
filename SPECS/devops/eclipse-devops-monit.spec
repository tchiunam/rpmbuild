%define installation_file monit-%{_build_version}-linux-x86.tar.gz
%define source_file https://mmonit.com/monit/dist/binary/%{_build_version}/%{installation_file}
%define etc_logrotate_dir %{_sysconfdir}/logrotate.d
%define doc_dir %{_defaultdocdir}/monit-%{_build_version}

Name:           tregonai-devops-monit
Version:        %{_build_version}
Release:        %{_release_no}%{?dist}
Summary:        DevOps Monit

Group:          DevOps
License:        Tregonai
Vendor:         DevOps
URL:            https://<to-be-published>.com
SOURCE0:        %{source_file}

%description
Monit package by DevOps to keep with latest features.

%install
mkdir -p %{buildroot}/{%{_bindir},%{_unitdir},%{etc_logrotate_dir},%{doc_dir},%{_mandir}} %{buildroot}/%{_sysconfdir}/monit.d %{buildroot}/%{_var}/log
if [ ! -f /tmp/%{installation_file} ]; then
    wget %{source_file} --directory-prefix /tmp
fi
tar xzf /tmp/%{installation_file} --directory /tmp
cp -p %{_sourcedir}/devops/tregonai-devops-monit/monit-logrotate %{buildroot}/%{etc_logrotate_dir}/monit
cp -p %{_sourcedir}/devops/tregonai-devops-monit/monit.service %{buildroot}/%{_unitdir}
cp -p %{_sourcedir}/devops/tregonai-devops-monit/logging %{buildroot}/%{_sysconfdir}/monit.d
cp -p %{_sourcedir}/devops/tregonai-devops-monit/README %{buildroot}/%{doc_dir}
mv /tmp/monit-%{_build_version}/bin/monit %{buildroot}/%{_bindir}
mv /tmp/monit-%{_build_version}/conf/monitrc %{buildroot}/%{_sysconfdir}
mv /tmp/monit-%{_build_version}/COPYING %{buildroot}/%{doc_dir}
mv /tmp/monit-%{_build_version}/man/man1 %{buildroot}/%{_mandir}
gzip %{buildroot}/%{_mandir}/man1/monit.1
touch %{buildroot}/%{_var}/log/monit.log
rm -rf /tmp/monit-%{_build_version}

%files
%defattr(-,root,root,-)
%{etc_logrotate_dir}/monit
%{_sysconfdir}/monit.d
%{_sysconfdir}/monitrc
%{_bindir}/monit
%{_unitdir}/monit.service
%{doc_dir}
%{_mandir}/man1/monit.1.gz
%{_var}/log/monit.log
