Name:           glib2
Version:        2.68.1
Release:        10
Summary:        The core library that forms the basis for projects such as GTK+ and GNOME
License:        LGPLv2+
URL:            http://www.gtk.org
Source0:        http://download.gnome.org/sources/glib/2.68/glib-%{version}.tar.xz

Patch6000:      backport-correctly-use-3-parameters-for-clise-range.patch
Patch6001:      backport-fix-a-memory-leak.patch
Patch6002:      backport-gfileenumerator-fix-leak-in-error-path.patch
Patch6003:      backport-gdbusobjectmanagerservice-fix-leak-in-error-path.patch
Patch6004:      backport-gdbusauth-fix-error-leak.patch
Patch6005:      backport-gapplication-fix-arguments-leak-in-error-path.patch
Patch6006:      backport-gsocks5proxy-Handle-EOF-when-reading-from-a-stream.patch
Patch6007:      backport-application-Unset-the-registered-state-after-shutting-down.patch
Patch6008:      backport-gdtlsconnection-Fix-a-check-for-a-vfunc-being-implemented.patch
Patch6009:      backport-gthread-posix-Free-a-memory-leak-on-error-path.patch
Patch6010:      backport-gutils-Avoid-segfault-in-g_get_user_database_entry.patch
Patch6011:      backport-glocalfileinfo-Fix-atime-mtime-mix.patch
Patch6012:      backport-gopenuriportal-Fix-GVariantBuilder-and-string-leakage.patch
Patch6013:      backport-gproxyaddressenumerator-Fix-string-leakage-on-an-invalid-input.patch
Patch6014:      backport-gsocks5proxy-Fix-buffer-overflow-on-a-really-long-domain-name.patch
Patch6015:      backport-gvariant-Fix-memory-leak-on-a-TYPE-CHECK-failure.patch
Patch6016:      backport-gvariant-Fix-pointers-being-dereferenced-despite-NULL-checks.patch
Patch6017:      backport-gtype-Fix-pointer-being-dereferenced-despite-NULL-check.patch
Patch6018:      backport-add-OOM-handling-in-mimemagic.patch
Patch6019:      backport-garray-buffer-overflow-fix.patch
Patch6020:      backport-gdbusconnection-Move-ExportedSubtree-definition.patch
Patch6021:      backport-gdbusconnection-Add-some-ownership-annotations.patch
Patch6022:      backport-gdbusconnection-Make-ExportedInterface-ExportedSubtree-refcounted.patch
Patch6023:      backport-gdbusconnection-Fix-race-between-method-calls-and-object-unregistration.patch
Patch6024:      backport-gdbusconnection-Fix-race-between-subtree-method-call-and-unregistration.patch
Patch6025:      backport-Add-D-Bus-object-subtree-unregistration-tests.patch
Patch6026:      backport-gutf8-add-string-length-check.patch
Patch6027:      backport-garray-Fix-integer-overflows-in-element-capacity-calculations.patch
Patch6028:      backport-gdbusmessage-Disallow-zero-length-elements-in-arrays.patch
Patch6029:      backport-gvariant-serialiser-Prevent-unbounded-recursion.patch
Patch6030:      backport-gutils-Fix-g_find_program_in_path-to-return-an-absolute-path.patch
Patch6031:      backport-Fix-memory-leak-in-gdbusauthmechanismsha1.patch
Patch6032:      backport-gprintf-Fix-a-memory-leak-with-an-invalid-format.patch
Patch6033:      backport-tests-Add-some-tests-for-g_vasprintf-invalid-format-strings.patch
Patch6034:      backport-tests-Add-some-tests-for-g_string_append_vprintf.patch
Patch6035:      backport-gdbusmethodinvocation-Fix-a-leak-on-an-early-return-path.patch
Patch6036:      backport-gdbusmethodinvocation-Fix-dead-code-for-type-checking-GetAll.patch
Patch6037:      backport-gdbusmethodinvocation-Drop-redundant-quote-from-warning.patch
Patch6038:      backport-tests-Add-unit-tests-for-GDBusMethodInvocation.patch
Patch6039:      backport-gtestdbus-Print-the-dbus-address-on-a-specific-FD-intead-of-stdout.patch
Patch6040:      backport-gopenuriportal-Fix-a-use-after-free-on-an-error-path.patch
Patch6041:      backport-gio-tool-Fix-a-minor-memory-leak.patch
Patch6042:      backport-gsocketclient-Fix-still-reachable-references-to-cancellables.patch
Patch6043:      backport-gunixmounts-Add-cache-to-g_unix_mount_points_get.patch
Patch6044:      backport-Add-lock-in-_g_get_unix_mount_points-around-fsent-functions.patch
Patch6045:      backport-g_get_unix_mount_points-reduce-syscalls-inside-loop.patch
Patch6046:      backport-xdgmime-fix-double-free.patch
Patch6047:      backport-Implement-GFileIface.set_display_name-for-resource-files.patch
Patch6048:      backport-tests-dbus-appinfo-Add-test-case-for-flatpak-opening-an-invalid-file.patch
Patch6049:      backport-documentportal-Fix-small-leak-in-add_documents-with-empty-URI-list.patch
Patch6050:      backport-gio-tests-gdbus-proxy-threads-Unref-GVariant-s-that-we-own.patch
Patch6051:      backport-gio-tests-gdbus-peer-Unref-cached-property-GVariant-value.patch
Patch6052:      backport-gdesktopappinfo-Unref-the-GDBus-call-results.patch
Patch6053:      backport-Handling-collision-between-standard-i-o-file-descriptors-and-newly-created-ones.patch
Patch6054:      backport-glocalfileoutputstream-Do-not-double-close-an-fd-on-unlink-error.patch
Patch6055:      backport-tests-Make-the-642026-test-take-100x-less-time.patch
Patch6056:      backport-gmessages-Add-missing-trailing-newline-in-fallback-log-hander.patch
Patch6057:      backport-Revert-Handling-collision-between-standard-i-o-filedescriptors-and-newly-created-ones.patch
patch6058:	    backport-gdbusinterfaceskeleton-Fix-a-use-after-free-of-a-GDBusMethodInvocation.patch
patch6059:	    backport-CVE-2023-24593_CVE-2023-25180-1.patch
patch6060:	    backport-CVE-2023-24593_CVE-2023-25180-2.patch
patch9000:      backport-lib-openharmony-glib.patch

BuildRequires:  chrpath gcc gcc-c++ gettext perl-interpreter
BUildRequires:  glibc-devel libattr-devel libselinux-devel meson
BuildRequires:  systemtap-sdt-devel pkgconfig(libelf) pkgconfig(libffi)
BuildRequires:  pkgconfig(libpcre) pkgconfig(mount) pkgconfig(zlib)
BuildRequires:  python3-devel
%ifnarch i686
BuildRequires:  desktop-file-utils shared-mime-info gtk-doc 
%if %{?openEuler:1}0
BuildRequires:  pkgconfig(sysprof-capture-4)
%endif
%endif

Provides:       %{name}-fam = %{version}-%{release}
Obsoletes:      %{name}-fam < %{version}-%{release}

Recommends:     shared-mime-info

Conflicts:      gcr < 3.28.1

%description
GLib is a bundle of three (formerly five) low-level system libraries
written in C and developed mainly by GNOME. GLib's code was separated
from GTK, so it can be used by software other than GNOME and has been
developed in parallel ever since.

%package        devel
Summary:        Development and test files for the GLib library
Requires:       %{name} = %{version}-%{release}
Requires:       gdb-headless

Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-tests = %{version}-%{release}
Obsoletes:      %{name}-static < %{version}-%{release}
Obsoletes:      %{name}-tests < %{version}-%{release}

%description    devel
Development and test files for the GLib library.

%ifnarch i686
%package        help
Summary:        help document for the glib2 package
Buildarch:      noarch
Provides:       %{name}-doc = %{version}-%{release}
Obsoletes:      %{name}-doc < %{version}-%{release}

%description    help
help document for the glib2 package.
%endif

%prep
%autosetup -n glib-%{version} -p1

%build
rm glib/pcre/*.[ch]
%meson --default-library=both  -Ddtrace=true  \
%ifnarch i686
%if %{?openEuler:1}0
    -Dsysprof=enabled \
%endif
    -Dman=true -Dgtk_doc=true \
%else
    -Dsysprof=disabled -Dman=false -Dgtk_doc=false \
%endif
    -Dsystemtap=true -Dinstalled_tests=true \
    -Dglib_debug=disabled

%meson_build

find . -name *.dtrace-temp.c -exec rm -f {} \;

%check
%meson_test

%install
%meson_install
touch -r gio/gdbus-2.0/codegen/config.py.in %{buildroot}%{_datadir}/glib-2.0/codegen/*.py
chrpath --delete %{buildroot}%{_libdir}/*.so

export PYTHONHASHSEED=0
%py_byte_compile %{__python3} %{buildroot}%{_datadir}

mv  %{buildroot}%{_bindir}/gio-querymodules %{buildroot}%{_bindir}/gio-querymodules-%{__isa_bits}
mkdir -p %{buildroot}%{_libdir}/gio/modules/
touch %{buildroot}%{_libdir}/gio/modules/giomodule.cache

# remove pycache
rm -rf %{buildroot}/%{_datadir}/gdb/auto-load/%{_libdir}/__pycache__
rm -rf %{buildroot}/%{_datadir}/glib-2.0/codegen/__pycache__
rm -rf %{buildroot}/%{_datadir}/glib-2.0/gdb/__pycache__

# remove rpath
chrpath -d %{buildroot}%{_libexecdir}/installed-tests/glib/gdbus-peer

%find_lang glib20

%transfiletriggerin -- %{_libdir}/gio/modules
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules &> /dev/null || :

%transfiletriggerpostun -- %{_libdir}/gio/modules
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules &> /dev/null || :

%transfiletriggerin -- %{_datadir}/glib-2.0/schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%transfiletriggerpostun -- %{_datadir}/glib-2.0/schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f glib20.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/*.so.*
%dir %{_libdir}/gio
%ghost %{_libdir}/gio/modules/giomodule.cache

%dir %{_datadir}/glib-2.0
%dir %{_datadir}/bash-completion
%{_datadir}/bash-completion/completions/gapplication
%{_datadir}/bash-completion/completions/gdbus
%{_datadir}/bash-completion/completions/gio
%{_datadir}/bash-completion/completions/gsettings

%{_bindir}/gio
%{_bindir}/gio-querymodules*
%{_bindir}/glib-compile-schemas
%{_bindir}/gsettings
%{_bindir}/gdbus
%{_bindir}/gapplication

%files devel
%{_libdir}/lib*.so
%{_libdir}/glib-2.0
%{_libdir}/pkgconfig/*
%{_libdir}/*.a
%{_includedir}/*
%{_libexecdir}/installed-tests
%exclude %{_libexecdir}/installed-tests/glib/cert-tests
%exclude %{_libexecdir}/installed-tests/glib/tls-certificate

%{_datadir}/aclocal/*
%{_datadir}/glib-2.0/*
%{_datadir}/bash-completion/completions/gresource
%{_datadir}/gdb/auto-load/%{_libdir}/*-gdb.py
%{_datadir}/gettext/
%{_datadir}/systemtap/
%{_datadir}/installed-tests
%exclude %{_datadir}/installed-tests/glib/tls-certificate.test

%{_bindir}/glib-genmarshal
%{_bindir}/glib-gettextize
%{_bindir}/glib-mkenums
%{_bindir}/gobject-query
%{_bindir}/gtester
%{_bindir}/gdbus-codegen
%{_bindir}/glib-compile-resources
%{_bindir}/gresource
%attr (0755, root, root) %{_bindir}/gtester-report

%ifnarch i686
%files help
%defattr(-,root,root)
%{_mandir}/man1/*
%doc %{_datadir}/gtk-doc/html/*
%endif

%changelog
* Fri Mar 11 2022 weijin deng <weijin.deng@turbolinux.com.cn> - 2.68.1-10
- Type:bugfix
- DESC:solve glib2 enable "glib2_debug" option causes gnome-calendar reopen
       coredumped in gtk3's _gtk_widget_get_toplevel()

* Wed Mar 9 2022 yangcheng<yangcheng87@h-partners.com> - 2.68.1-9
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:remove gdbus-peer rpath compile option

* Wed Mar 2 2022 hanhui<hanhui15@h-partners.com> - 2.68.1-8
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:custom installation depend on sysprof

* Sat Feb 19 2022 wangkerong<wangkerong@h-partners.com> - 2.68.1-7
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add i686 options，fix build failure on i686

* Sun Nov 14 2021 fengtao<fengtao40@huawei.com> - 2.68.1-6
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add require gdb-headless for devel


* Tue Sep 14 2021 yangcheng<yangcheng87@huawei.com> - 2.68.1-5
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:Drop dependebcy on gamin

* Tue Sep 7 2021 fengtao<fengtao40@huawei.com> - 2.68.1-4
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:enable all tests

* Sat Aug 14 2021 liuyumeng<liuyumeng5@huawei.com> - 2.68.1-3
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:fix a memory leak

* Tue Aug 10 2021 liuyumeng<liuyumeng5@huawei.com> - 2.68.1-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:fix the third parameter of clise-range

* Wed Jun 30 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 2.68.1-1
- Upgrade to 2.68.1 because gnome-builder and more new gnome applications
  need function g_memdup2 which needs glib2 ≥2.67.3 to instead of g_memdup

* Wed May 19 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 2.66.8-1
- Upgrade to 2.66.8
- Update Version, Release
- Delete patch files, delete gio-launch-desktop(not exist in 2.66.8)
- Correct date, make it match weekday

* Tue Apr 13 2021 hanhui<hanhui15@huawei.com> - 2.62.5-5
- Type:cve
- Id:CVE-2021-28153
- SUG:NA
- DESC:fix CVE-2021-28153

* Sat Mar 6 2021 hanhui<hanhui15@huawei.com> - 2.62.5-4
- Type:cve
- Id:CVE-2021-27219
- SUG:NA
- DESC:fix CVE-2021-27219

* Mon Mar 1 2021 jinzhimin<jinzhimin2@huawei.com> - 2.62.5-3
- Type:cve
- Id:CVE-2021-27218
- SUG:NA
- DESC:fix CVE-2021-27218

* Sat Feb 27 2021 zhujunhao<zhujunhao8@huawei.com> - 2.62.5-2
- Type:cve
- Id:CVE-2020-35457
- SUG:NA
- DESC:fix CVE-2020-35457

* Tue Jul 21 2020 hanhui<hanhui15@huawei.com> - 2.62.5-1
- Update to 2.62.5

* Mon Mar 2 2020 hexiujun<hexiujun1@huawei.com> - 2.62.1-4
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:fix accidentally delete temp file within dtrace

* Fri Feb 28 2020 zhangrui <zhangrui182@huawei.com> - 2.62.1-3
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:remove dist in spec

* Mon Feb 24 2020 openEuler Buildteam <buildteam@openeuler.org> - 2.62.1-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:exclude some unnecessary files

* Thu Jan 9 2020 openEuler Buildteam <buildteam@openeuler.org> - 2.62.1-1
- update to 2.62.1

* Tue Dec 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.58.1-6
- change the path of files

* Sat Dec 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.58.1-5
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:Fix a leaking GRemoteActionGroup member

* Sat Nov 23 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.58.1-4
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add the libxslt in buildrequires

* Wed Sep 25 2019 huzunhao<huzunhao2@huawei.com> - 2.58.1-3
- Type:cves
- ID:CVE-2019-12450 CVE-2019-13012
- SUG:restart
- DESC:fix CVE-2019-12450 CVE-2019-13012

* Thu Sep 19 2019 Lijin Yang <yanglijin@huawei.com> - 2.58.1-2
- Package init
