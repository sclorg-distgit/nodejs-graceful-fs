%{?scl:%scl_package nodejs-graceful-fs}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-graceful-fs
Version:    4.1.6
Release:    2%{?dist}
Summary:    'fs' module with incremental back-off on EMFILE
License:    ISC
URL:        https://github.com/isaacs/node-graceful-fs
Source0:    http://registry.npmjs.org/graceful-fs/-/graceful-fs-%{version}.tgz
# The LICENSE file has been updated upstream to reflect the actual license.
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Just like node.js' fs module, but it does an incremental back-off when EMFILE is
encountered.  Useful in asynchronous situations where one needs to try to open
lots and lots of files.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/graceful-fs
cp -p fs.js graceful-fs.js package.json polyfills.js legacy-streams.js \
    %{buildroot}%{nodejs_sitelib}/graceful-fs

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/graceful-fs
%doc README.md LICENSE

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.1.6-2
- rh-nodejs8 rebuild

* Thu Sep 22 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.1.6-1
- Updated with script

* Wed Sep 21 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.1.4-1
- Updated with script

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.1.2-4
- rebuilt

* Wed Dec 09 2015 Tomas Hrcka <thrcka@redhat.com> - 4.1.2-3
- Reflect Upstream License

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 4.1.2-2
- New upstream release

* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 3.0.5-2
- Add missing source file fs.js

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 3.0.5-1
- New upstream release 3.0.5

* Fri Jul 12 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-2
- include missing polyfills.js file

* Fri Jul 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.0-1
- new upstream release 2.0.0
- license file now updated upstream

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.2-1
- new upstream release 1.2.2

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.1-3
- restrict to compatible arches

* Tue May 28 2013 Tomas Hrcka <thrcka@redhat.com> - 1.2.1-2.1
- merged latest upstream release and fix BZ#967550

* Mon May 27 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-2
- the LICENSE file previously contained the wrong license (MIT), but now
  upstream have fixed it to contain the correct license (BSD) (#967442)

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-1
- update to upstream release 1.2.1

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-2
- add macro for EPEL6 dependency generation

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.0-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-1
- new upstream release 1.2.0

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.14-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.14-1
- new upstream release 1.1.14
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.8-2
- guard Requires for F17 automatic depedency generation

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.8-1
- new upstream release 1.1.8

* Sun Jan 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.5-1
- new upstream release 1.1.5

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-2
- missing Group field for EL5

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-1
- new upstream release 1.1.4

* Thu Nov 10 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-0.1.20111109git33dee97
- new upstream release
- Node v0.6.0 compatibility fixes

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-1
- new upstream release

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-1
- initial package
