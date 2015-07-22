#global posttag .final.0

%global scl lsst-stack1

%{?scl:%global _scl_prefix /opt/lsst}
%{?scl:%scl_package scons}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}scons
Version:	2.3.4
Release:	4%{?posttag}%{?dist}
Summary:	An Open Source software construction tool
Group:		Development/Tools
License:	MIT
URL:		http://www.scons.org
Source:		http://downloads.sourceforge.net/scons/scons-%{version}%{?posttag}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:	%{?scl:python27-}python-devel >= 2.7
BuildRequires: %{?scl_prefix}build


%description
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software.  SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax.  SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines.  SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched.  SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.


%prep
%setup -q -n %{pkg_name}-%{version}
sed -i 's|/usr/bin/env python|/opt/rh/python27/root/usr/bin/python|' script/*


%build
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py build
%{?scl:EOF}


%install
rm -rf %{buildroot}
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py install -O1 --skip-build \
    --root=%{buildroot} \
    --no-version-script \
    --standalone-lib \
    --install-purelib=%{_exec_prefix}/lib \
    --install-scripts=%{_bindir} \
    --install-data=%{_datadir}
%{?scl:EOF}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES.txt LICENSE.txt README.txt RELEASE.txt
%{_bindir}/*
%{_exec_prefix}/lib/scons
%{_mandir}/man?/*


%changelog
* Wed Jul 22 2015 Joshua Hoblitt <josh@hoblitt.com> 2.3.4-4
- fix BuildRoot (josh@hoblitt.com)

* Wed Jul 22 2015 Joshua Hoblitt <josh@hoblitt.com> 2.3.4-3
- new package built with tito

* Wed Jul 22 2015 Joshua Hoblitt <josh@hoblitt.com> 2.3.4-3
- scl fixes (josh@hoblitt.com)
- backport %%build/%%install/%%clean from f22 (josh@hoblitt.com)

* Wed Jul 22 2015 Joshua Hoblitt <josh@hoblitt.com>
- scl fixes (josh@hoblitt.com)
- backport %%build/%%install/%%clean from f22 (josh@hoblitt.com)

* Tue Jul 21 2015 Joshua Hoblitt <josh@hoblitt.com>
- backport %%build/%%install/%%clean from f22 (josh@hoblitt.com)

* Tue Jul 21 2015 Joshua Hoblitt <josh@hoblitt.com> 2.3.4-1
- new package built with tito

* Mon Aug 23 2010 Chen Lei <supercyper@163.com> - 2.0.1-1
- New release 2.0.1 (#595107)

* Sun May 23 2010 Jochen Schmitt <Jochen herr-schmitt de> - 1.3.0-1
- New upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 25 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.0-1
- Update to 1.2.0 to fix problems with Python 2.6 (#475903)
  (currently causing broken deps with other packages)

* Thu Dec 18 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.1.0-1
- new release 1.1.0

* Fri Sep  5 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.0.0-1.d20080826
- new release 1.0.0

* Sun Aug  3 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.5-1
- new release 0.98.5

* Sun Jun  1 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.4-2
- added buildreq sed

* Sat May 31 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.4-1
- new release 0.98.4

* Sun May  4 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.3-2
- changed shebang line of scripts

* Sun May  4 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.3-1
- new release 0.98.3

* Sat Apr 19 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.1-1
- new release 0.98.1

* Sat Apr  5 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98-1
- new release 0.98

* Mon May 21 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.97-1
- new version 0.97

* Thu May 10 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.96.96-1
- new version 0.96.96

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.96.1-3
- Rebuild for FE6

* Sat Jun 18 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.96.1-1
- New Version 0.96.1

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Jan 25 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> 0.96-4
- Place libs in {_prefix}/lib/ and not in {libdir}; fixes x86_64 problems
- Adjust minor bits to be in sync with python-spec-template

* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 0.96-3
- Bump release to provide Extras upgrade path.

* Thu Aug 19 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.96-0.fdr.1
- New Version 0.96

* Thu Apr 15 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.95-0.fdr.1
- New Version 0.95

* Fri Nov  7 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:0.93-0.fdr.1
- First Fedora release
