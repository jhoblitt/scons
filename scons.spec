Name:           scons
Version:        0.96
Release:        0.fdr.1.1
Epoch:          0
Summary:        An Open Source software construction tool

Group:          Development/Tools
License:        MIT
URL:            http://www.scons.org/
Source:         http://download.sourceforge.net/scons/scons-0.96.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArchitectures: noarch
BuildRequires:  python-devel

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
%setup -q


%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES --install-lib=%{_libdir}/scons --install-scripts=%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -f scons.1 sconsign.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGES.txt LICENSE.txt README.txt RELEASE.txt
%{_bindir}/*
%{_libdir}/scons
%{_mandir}/man*/*

%changelog
* Thu Aug 19 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.96-0.fdr.1
- New Version 0.96

* Thu Apr 15 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:0.95-0.fdr.1
- New Version 0.95

* Fri Nov  7 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:0.93-0.fdr.1
- First Fedora release
