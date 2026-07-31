%define name gmenu-mk
# CI exports GIT_HASH; fall back to the local checkout so manual builds work too.
%define git_hash %(if [ -n "$GIT_HASH" ]; then echo "$GIT_HASH"; else git rev-parse --short HEAD 2>/dev/null || echo nogit; fi)

Name:           %{name}
Version:        1.1
Release:        2.git.%{git_hash}%{?dist}
Summary:        MK files for Cinnamon Gmenu

License:        MIT
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz

Requires: cinnamon-session
Requires: gmenu-applet

%description
MK files for Cinnamon Gmenu

# The dev container installs the -devel RPM to pull in the build/dev
# environment; the shared CI build hard-fails on a spec without this section.
# There is nothing to compile here (menu XML, .desktop files and icons), so
# it carries no files and only depends on the main package.
%package devel
Summary: %{name}-devel Package
Requires: %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
# Nothing to prepare
# The CI build tars the tree as <name>-<version>/, so the unpacked dir carries
# the version suffix -- %{name} alone would not match.
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}/usr/share/cinnamon/applets/gmenu@noirlab.edu/
cp -r * %{buildroot}/usr/share/cinnamon/applets/gmenu@noirlab.edu/
rm -f %{buildroot}/usr/share/cinnamon/applets/gmenu@noirlab.edu/README.md
rm -f %{buildroot}/usr/share/cinnamon/applets/gmenu@noirlab.edu/gmenu-mk.spec
# The CI submodule and workflow are build-time only; never ship them.
rm -rf %{buildroot}/usr/share/cinnamon/applets/gmenu@noirlab.edu/gemini-rtsw-ci
rm -rf %{buildroot}/usr/share/cinnamon/applets/gmenu@noirlab.edu/.github

%post

%files
%attr(0755, software, software) /usr/share/cinnamon/applets/gmenu@noirlab.edu/applications/*
%attr(0755, software, software) /usr/share/cinnamon/applets/gmenu@noirlab.edu/desktop-directories/*
%attr(0755, software, software) /usr/share/cinnamon/applets/gmenu@noirlab.edu/icons/*
%attr(0755, software, software) /usr/share/cinnamon/applets/gmenu@noirlab.edu/gmenu.menu

%files devel
# Intentionally empty: no headers or build artifacts to ship.

%changelog
* Fri Jul 31 2026 Hawi Stecher <hawi.stecher@noirlab.edu> - 1.1-2
- GNFR-75106: fix the StripTool menu entry, which never launched on EL9.
  It ran "python2 $HOME/sciops/das/bin-gn/showstrip.py"; EL9 ships no
  python2 at all. Point it at /gemsoft/opt/ssaTools/scripts/showstrip
  (owned by ssaTools-2021A) by absolute path -- a bare command would rely
  on the Cinnamon session inheriting the interactive PATH, and the
  "showstrip" that works in a terminal is only a shell alias.

* Fri Jul 31 2026 Hawi Stecher <hawi.stecher@noirlab.edu> - 1.1-1
- Migrate to the shared gemini-rtsw-ci GitHub pipeline (EL9)
- Replace unresolvable %%{auto_version}/%%{auto_release} macros with a real
  version and a git-hash release
- Add an empty -devel subpackage, required by the shared CI build

* Mon Apr 21 2025 Oscar Fuentes <oscar.fuentes@noirlab.edu> - 1.0-1
- Initial package
