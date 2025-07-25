# 
# revad spec file containing two RPMs
#

Name: cernbox-revad
Summary: Reva for CERNBox
Version: 1.0.46_rc7
Release: 1%{?dist}
License: AGPLv3
BuildRoot: %{_tmppath}/%{name}-buildroot
Group: CERN-IT/ST
ExclusiveArch: x86_64
Source: %{name}-%{version}.tar.gz
Conflicts: cernbox-revad-ceph

%description -n cernbox-revad
This RPM provides Reva for the CERNBox backend

%package -n cernbox-revad-ceph
Summary: Reva for CERNBox with Ceph support
Conflicts: cernbox-revad
BuildRequires: libcephfs-devel
BuildRequires: libcephfs2
RemovePathPostfixes: .ceph

%description -n cernbox-revad-ceph
This RPM provides Reva for the CERNBox backend with Ceph support

%package -n cernbox-cli
Summary: Reva CLI for CERNBox

%description -n cernbox-cli
This RPM provides reva, the command-line interface for CERNBox

# Don't do any post-install weirdness, especially compiling .py files
%define __os_install_post %{nil}

%prep
%setup -n %{name}-%{version}

%install
rm -rf %buildroot/
mkdir -p %buildroot/usr/bin
mkdir -p %buildroot/etc/revad
mkdir -p %buildroot/var/log/revad
mkdir -p %buildroot/var/run/revad
install -m 755 revad %buildroot/usr/bin/revad
install -m 755 revad-ceph %buildroot/usr/bin/revad.ceph
install -m 755 reva %buildroot/usr/bin/reva

%preun

%post

%files -n cernbox-revad
%defattr(-,root,root,-)
/etc/revad
/var/log/revad
/var/run/revad
/usr/bin/revad

%files -n cernbox-revad-ceph
%defattr(-,root,root,-)
/etc/revad
/var/log/revad
/var/run/revad
/usr/bin/revad.ceph

%files -n cernbox-cli
%defattr(-,root,root,-)
/usr/bin/reva

%clean
rm -rf %buildroot/

%changelog
* Fri Jul 25 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.46_rc7
- v1.0.46_rc7, based on commit 39d211b at cs3org/reva/fix/mountpoints and commit 19fdcb9 at cernbox/reva-plugins/master
* Fri Jul 25 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.46_rc6
- v1.0.46_rc6, based on commit 14269db at cs3org/reva/fix/mountpoints and commit 19fdcb9 at cernbox/reva-plugins/master
* Fri Jul 25 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.46_rc5
- v1.0.46_rc5, based on commit 4adf715 at cs3org/reva/fix/mountpoints and commit 19fdcb9 at cernbox/reva-plugins/master
* Fri Jul 25 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.46_rc4
- v1.0.46_rc4, based on commit 320c0d2 at cs3org/reva/fix/put-request-broken and commit 19fdcb9 at cernbox/reva-plugins/master
* Fri Jul 25 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.46_rc3
- v1.0.46_rc3, based on commit e416400 at cs3org/reva/fix/multiple-user-share and commit 19fdcb9 at cernbox/reva-plugins/master
* Wed Jul 02 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.46_rc2
- v1.0.46_rc2, based on commit dfaf124 at cs3org/reva/master and commit b10ba9f at cernbox/reva-plugins/feat/share-expiration
* Tue Jul 01 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.46_rc1
- v1.0.46_rc1, based on commit badf0ed at cs3org/reva/fix/eos-grpc-cleanup and commit 07df4ef at cernbox/reva-plugins/master
* Fri Jun 27 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.45
- v1.0.45, based on commit e554685 at cs3org/reva/master and commit 4faa32a at cernbox/reva-plugins/master
* Fri Jun 27 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.45_rc4
- v1.0.45_rc4, based on commit 1613c15 at cs3org/reva/fix/home-creation and commit 4faa32a at cernbox/reva-plugins/master
* Fri Jun 27 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.45_rc3
- v1.0.45_rc3, based on commit 0db7497 at cs3org/reva/fix/enablehome-double-wrap and commit 4faa32a at cernbox/reva-plugins/master
* Thu Jun 26 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.45_rc2
- v1.0.45_rc2, based on commit ab3c530 at cs3org/reva/fix/enablehome-double-wrap and commit 4faa32a at cernbox/reva-plugins/master
* Thu Jun 26 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.45_rc1
- v1.0.45_rc1, based on commit d62a20e at cs3org/reva/fix/enablehome-double-wrap and commit 4faa32a at cernbox/reva-plugins/master
* Thu Jun 19 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.44
- v1.0.44, based on commit 65db3d5 at cs3org/reva/master and commit 13bf423 at cernbox/reva-plugins/master
* Thu Jun 19 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.43
- v1.0.43, based on commit e581079 at cs3org/reva/master and commit 13bf423 at cernbox/reva-plugins/master
* Thu Jun 12 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.42
- v1.0.42, based on commit 6f5353c at cs3org/reva/master and commit 13bf423 at cernbox/reva-plugins/master
* Thu Jun 12 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.42_rc1
- v1.0.42_rc1, based on commit f76b226 at cs3org/reva/cbox-patch-1.0.40 and commit 13bf423 at cernbox/reva-plugins/master
* Tue Jun 03 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.41
- v1.0.41, based on commit 8cd6e1a at cs3org/reva/master and commit 13bf423 at cernbox/reva-plugins/master
* Tue May 20 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.41_rc1
- v1.0.41_rc1, based on commit 18b5f4b at cs3org/reva/cbox-patch-1.0.40 and commit 13bf423 at cernbox/reva-plugins/master
* Mon May 05 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.40
- v1.0.40, based on commit 8e826d2 at cs3org/reva/master and commit 13bf423 at cernbox/reva-plugins/master
* Mon May 05 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39
- v1.0.39, based on commit 7d393f1 at cs3org/reva/master and commit 13bf423 at cernbox/reva-plugins/master
* Mon May 05 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc16
- v1.0.39_rc16, based on commit 1ad059a at cs3org/reva/ fix/failed-handlenew and commit 13bf423 at cernbox/reva-plugins/master
* Mon May 05 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc15
- v1.0.39_rc15, based on commit 93efc78 at cs3org/reva/fix/failed-handlenew and commit 13bf423 at cernbox/reva-plugins/master
* Mon May 05 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc14
- v1.0.39_rc14, based on commit 457caea at cs3org/reva/fix/my-office-files-fix-2 and commit 7ba667d at cernbox/reva-plugins/fix/remove-public-link-expiry
* Mon May 05 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc13
- v1.0.39_rc13, based on commit 457caea at cs3org/reva/fix/my-office-files-fix-2 and commit 0facb44 at cernbox/reva-plugins/fix/storage-id
* Mon May 05 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc12
- v1.0.39_rc12, based on commit 457caea at cs3org/reva/fix/my-office-files-fix-2 and commit b29300f at cernbox/reva-plugins/master
* Wed Apr 30 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc11
- v1.0.39_rc11, based on commit 457caea at cs3org/reva/fix/my-office-files-fix-2 and commit 1cbdbae at cernbox/reva-plugins/master
* Wed Apr 30 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc10
- v1.0.39_rc10, based on commit 2d3e306 at cs3org/reva/fix/my-office-files-fix-2 and commit 1cbdbae at cernbox/reva-plugins/master
* Tue Apr 29 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc9
- v1.0.39_rc9, based on commit 2d3e306 at cs3org/reva/ fix/my-office-files-fix-2 and commit 4855ce7 at cernbox/reva-plugins/master
* Tue Apr 29 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc8
- v1.0.39_rc8, based on commit f152493 at cs3org/reva/fix/my-office-files-fix-2 and commit 4855ce7 at cernbox/reva-plugins/master
* Tue Apr 29 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc7
- v1.0.39_rc7, based on commit f799533 at cs3org/reva/fix/my-office-files-fix-2 and commit 4855ce7 at cernbox/reva-plugins/master
* Mon Apr 28 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc6
- v1.0.39_rc6, based on commit f799533 at cs3org/reva/fix/my-office-files-fix-2 and commit f487892 at cernbox/reva-plugins/master
* Mon Apr 28 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc5
- v1.0.39_rc5, based on commit a0b631a at cs3org/reva/fix/my-office-files-fix-2 and commit f487892 at cernbox/reva-plugins/master
* Mon Apr 28 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc4
- v1.0.39_rc4, based on commit dc849ae at cs3org/reva/fix/my-office-files-fix-2 and commit f487892 at cernbox/reva-plugins/master
* Mon Apr 28 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc3
- v1.0.39_rc3, based on commit 0659c09 at cs3org/reva/fix/my-office-files-fix-2 and commit f487892 at cernbox/reva-plugins/master
* Fri Apr 25 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc2
- v1.0.39_rc2, based on commit d24a469 at cs3org/reva/fix/my-office-files-fix-2 and commit f487892 at cernbox/reva-plugins/master
* Tue Apr 22 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.39_rc1
- v1.0.39_rc1, based on commit ff38b0c at cs3org/reva/fix/my-office-files-bugfix and commit f487892 at cernbox/reva-plugins/master
* Tue Apr 15 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.38
- v1.0.38, based on commit eb3722d at cs3org/reva/master and commit f487892 at cernbox/reva-plugins/master
* Fri Mar 14 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.38_rc1
- v1.0.38_rc1, based on commit eb8805d at cs3org/reva/ocm1.2 and commit 0b2f4f1 at cernbox/reva-plugins/master
* Fri Mar 14 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.37
- v1.0.37, based on commit 1943e78 at cs3org/reva/master and commit 0b2f4f1 at cernbox/reva-plugins/master
* Fri Mar 14 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.37_rc1
- v1.0.37_rc1, based on commit eb8805d at cs3org/reva/ocm1.2 and commit 0b2f4f1 at cernbox/reva-plugins/master
* Thu Mar 13 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.36
- v1.0.36, based on commit 29a7113 at cs3org/reva/master and commit 0b2f4f1 at cernbox/reva-plugins/master
* Thu Mar 13 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.36_rc3
- v1.0.36_rc3, based on commit 9993bcb at cs3org/reva/fix/unset-attr-as-root and commit 0b2f4f1 at cernbox/reva-plugins/master
* Thu Mar 13 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.36_rc2
- v1.0.36_rc2, based on commit ea066cf at cs3org/reva/fix/unset-attr-as-root and commit 0b2f4f1 at cernbox/reva-plugins/master
* Thu Mar 13 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.36_rc1
- v1.0.36_rc1, based on commit 82fb7cb at cs3org/reva/master and commit 930c823 at cernbox/reva-plugins/fix/shared-with-me
* Wed Mar 12 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.35
- v1.0.35, based on commit 82fb7cb at cs3org/reva/master and commit ebcc603 at cernbox/reva-plugins/master
* Mon Mar 10 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.35_rc8
- v1.0.35_rc8, based on commit 0b13cf8 at cs3org/reva/fix/better-eosfs-logging and commit ebcc603 at cernbox/reva-plugins/master
* Mon Mar 10 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.35_rc7
- v1.0.35_rc7, based on commit 8a152e5 at cs3org/reva/fix/better-eosfs-logging and commit ebcc603 at cernbox/reva-plugins/master
* Fri Mar 07 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.35_rc6
- v1.0.35_rc6, based on commit 0b22b49 at cs3org/reva/fix/better-eosfs-logging and commit 6fed204 at cernbox/reva-plugins/fix/duplicate-pk-with-deleted
* Fri Mar 07 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.35_rc5
- v1.0.35_rc5, based on commit 2112df0 at cs3org/reva/fix/better-eosfs-logging and commit 6fed204 at cernbox/reva-plugins/fix/duplicate-pk-with-deleted
* Fri Mar 07 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.35_rc4
- v1.0.35_rc4, based on commit 2112df0 at cs3org/reva/fix/better-eosfs-logging and commit 5a2749e at cernbox/reva-plugins/fix/duplicate-pk-with-deleted
* Fri Mar 07 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.35_rc3
- v1.0.35_rc3, based on commit 7bbdcd5 at cs3org/reva/master and commit 5a2749e at cernbox/reva-plugins/fix/duplicate-pk-with-deleted
* Fri Mar 07 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.35_rc2
- v1.0.35_rc2, based on commit 7bbdcd5 at cs3org/reva/master and commit 76dd6b6 at cernbox/reva-plugins/fix/shared-ids-sharing
* Thu Mar 06 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.35_rc1
- v1.0.35_rc1, based on commit 7bbdcd5 at cs3org/reva/master and commit e9f14e0 at cernbox/reva-plugins/fix/shared-ids-sharing
* Tue Mar 04 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.34
- v1.0.34, based on commit ba01f0e at cs3org/reva/master and commit d4c5866 at cernbox/reva-plugins/master
* Mon Mar 03 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.34_rc5
- v1.0.34_rc5, based on commit 2177f11 at cs3org/reva/feat/publicshares-logging and commit d4c5866 at cernbox/reva-plugins/master
* Mon Mar 03 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.34_rc4
- v1.0.34_rc4, based on commit e511623 at cs3org/reva/feat/publicshares-logging and commit d4c5866 at cernbox/reva-plugins/master
* Mon Mar 03 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.34_rc3
- v1.0.34_rc3, based on commit d36f5cf at cs3org/reva/feat/publishare-sqldriver-in-plugins and commit d4c5866 at cernbox/reva-plugins/master
* Thu Feb 27 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.34_rc2
- v1.0.34_rc2, based on commit 9d2533e at cs3org/reva/master and commit 641d885 at cernbox/reva-plugins/feat/public-links-ormified
* Tue Feb 25 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.34_rc1
- v1.0.34_rc1, based on commit 9d2533e at cs3org/reva/master and commit 412e47f at cernbox/reva-plugins/feat/public-links-ormified
* Thu Feb 20 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.33
- v1.0.33, based on commit 7c299e3 at cs3org/reva/master and commit 6fa38f1 at cernbox/reva-plugins/master
* Tue Feb 18 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.32
- v1.0.32, based on commit bb9b46f at cs3org/reva/master and commit bb9833a at cernbox/reva-plugins/master
* Fri Feb 07 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.32_rc3
- v1.0.32_rc3, based on commit 048f548 at cs3org/reva/master and commit 3f27993 at cernbox/reva-plugins/fix/tx-sharing
* Thu Feb 06 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.32_rc2
- v1.0.32_rc2, based on commit 9de042a at cs3org/reva/fix/eos-versions-grpc-proj and commit 38c8c5a at cernbox/reva-plugins/fix/eos-revisions-grpc
* Wed Feb 05 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.32_rc1
- v1.0.32_rc1, based on commit 19a7a86 at cs3org/reva/master and commit 0c91845 at cernbox/reva-plugins/fix/tx-sharing
* Wed Feb 05 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.31
- v1.0.31, based on commit 19a7a86 at cs3org/reva/master and commit 226dde5 at cernbox/reva-plugins/master
* Tue Feb 03 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.30
- v1.0.30, based on commit 9f14cb9 at cs3org/reva/master and commit aa40edc at cernbox/reva-plugins/master
* Thu Jan 30 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.29
- v1.0.29, based on commit 9f14cb9 at cs3org/reva/master and commit 226dde5 at cernbox/reva-plugins/master
* Wed Jan 29 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.28
- v1.0.28, based on commit f697e1c at cs3org/reva/master and commit 4f311f5 at cernbox/reva-plugins/master
* Fri Jan 17 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.27
- v1.0.27, based on commit 51e12b4 at cs3org/reva/master and commit 4f311f5 at cernbox/reva-plugins/master
* Wed Jan 08 2025 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.26
- v1.0.26, based on commit bb7dcda at cs3org/reva/master and commit 4f311f5 at cernbox/reva-plugins/master
* Tue Dec 10 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.25
- v1.0.25, based on commit 1973726 at cs3org/reva/master and commit 4f311f5 at cernbox/reva-plugins/master
* Thu Nov 28 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.24
- v1.0.24, based on commit 4820f8c at cs3org/reva/master and commit 4f311f5 at cernbox/reva-plugins/master
* Mon Nov 25 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.23
- v1.0.23, based on commit 683954c at cs3org/reva/master and commit 9969421 at cernbox/reva-plugins/master
* Fri Nov 15 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.22
- v1.0.22, based on commit c71d70c at cs3org/reva/master and commit 9969421 at cernbox/reva-plugins/master
* Mon Nov 04 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.21
- v1.0.21, based on commit 1a51ab7 at cs3org/reva/master and commit 9969421 at cernbox/reva-plugins/master
* Wed Oct 30 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.20
- v1.0.20 experimental, based on Reva commit 6b0f9b3 at cs3org/ceph2cbox
* Thu Oct 24 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.19
- v1.0.19, based on Reva commit 10664f4 at cs3org/master
* Tue Sep 17 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.18
- v1.0.18, based on Reva commit 122da0b at cs3org/master
* Mon Sep 02 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.17
- v1.0.17, based on Reva commit 8d1b4ab at cs3org/master
* Mon Sep 02 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.16
- v1.0.16, based on Reva commit 8d1b4ab at cs3org/master
* Tue Jun 04 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.15
- v1.0.15, based on Reva commit d0695a4 at cs3org/master
* Mon Jun 03 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.14
- v1.0.14, based on reva Reva commit d0695a4 at cs3org/master
* Wed Apr 17 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.13
- v1.0.13
* Wed Mar 27 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.12
- v1.0.12
* Wed Mar 27 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.11
- v1.0.11
* Wed Mar 13 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.10
- v1.0.10
* Wed Feb 14 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.9
- v1.0.9
* Wed Feb 07 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.8
- v1.0.8
* Tue Jan 30 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.7
- v1.0.7
* Tue Jan 30 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.6
- v1.0.6
* Tue Jan 30 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.5
- v1.0.5
* Fri Jan 12 2024 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.4
- v1.0.4
* Mon Dec 18 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.3
- v1.0.3
* Mon Dec 04 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.2
- v1.0.2
* Thu Nov 16 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 1.0.1
- v1.0.1
* Mon Nov 13 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.52
- v0.0.52
* Wed Oct 25 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.51
- v0.0.51
* Tue Oct 24 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.50
- v0.0.50
* Thu Oct 12 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.49
- v0.0.49
* Tue Oct 10 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.48
- v0.0.48
* Wed Aug 23 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.47
- v0.0.47
* Fri Aug 18 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.46
- v0.0.46
* Wed Aug 16 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.45
- v0.0.45
* Mon Aug 14 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.44
- v0.0.44
* Fri Jul 21 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.43
- v0.0.43
* Tue Jun 06 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.42.experimental
- v0.0.42.experimental
* Mon Jun 05 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.41
- v0.0.41
* Fri May 12 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.40
- v0.0.40
* Wed May 10 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.39
- v0.0.39
* Fri May 05 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.38
- v0.0.38
* Thu Apr 20 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.37
- v0.0.37
* Mon Apr 17 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.36
- v0.0.36
* Wed Apr 12 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.35
- v0.0.35
* Tue Apr 11 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.34
- v0.0.34
* Tue Apr 11 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.33
- v0.0.33
* Tue Apr 04 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.32
- v0.0.32
* Wed Mar 22 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.31
- v0.0.31
* Wed Mar 15 2023 Giuseppe Lo Presti <lopresti@cern.ch> 0.0.30
- v0.0.30
* Tue Mar 14 2023 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.29
- v0.0.29
* Mon Feb 06 2023 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.28
- v0.0.28
* Tue Jan 24 2023 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.27
- v0.0.27
* Sat Dec 03 2022 Giuseppe Lo Presti <giuseppe.lopresti@cern.ch> 0.0.26
- Temporary patch
* Fri Dec 02 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.25
- v0.0.25
* Fri Dec 02 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.24
- v0.0.24
* Tue Nov 29 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.23
- v0.0.23
* Mon Nov 07 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.22
- v0.0.22
* Thu Nov 03 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.21
- v0.0.21
* Wed Oct 19 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.20
- v0.0.20
* Wed Oct 19 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.19
- v0.0.19
* Mon Oct 17 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.18
- v0.0.18
* Thu Oct 13 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.17
- v0.0.17
* Tue Oct 11 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.16
- v0.0.16
* Fri Oct 07 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.15
- v0.0.15
* Tue Oct 04 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.14
- v0.0.14
* Thu Sep 29 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.13
- v0.0.13
* Wed Sep 21 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.12
- v0.0.12
* Wed Sep 21 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.11
- v0.0.11
* Wed Sep 14 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.10
- v0.0.10
* Tue Sep 13 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.9
- v0.0.9
* Wed Sep 07 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.8
- v0.0.8
* Wed Sep 07 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.7
- v0.0.7
* Thu Aug 25 2022 Diogo Castro <diogo.castro@cern.ch> 0.0.6
- Do not lowercase case sensitive hash (fix public links)
* Tue Aug 16 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.5
- v0.0.5
* Thu Aug 11 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.4
- v0.0.4
* Thu Jul 14 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.2
- v0.0.2
* Thu Jul 07 2022 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.1
- v0.0.1
