Name:           %{name}
Version:        %{auto_version}
Release:        %{auto_release}.%{?dist}
Summary:        MK files for Cinnamon Gmenu

License:        MIT
BuildArch:      noarch
Source0:        %{name}-%{auto_version}.tar.gz

Requires: cinnamon-session
Requires: gmenu-applet

%description
MK files for Cinnamon Gmenu

%prep
# Nothing to prepare
%setup -q -n %{name}

%install
mkdir -p %{buildroot}/usr/share/cinnamon/applets/gmenu@noirlab.edu/
cp -r * %{buildroot}/usr/share/cinnamon/applets/gmenu@noirlab.edu/
rm -f %{buildroot}/usr/share/cinnamon/applets/gmenu@noirlab.edu/README.md
rm -f %{buildroot}/usr/share/cinnamon/applets/gmenu@noirlab.edu/gmenu-mk.spec

%post

%files
%attr(0755, software, software) /usr/share/cinnamon/applets/gmenu@noirlab.edu/applications/*
%attr(0755, software, software) /usr/share/cinnamon/applets/gmenu@noirlab.edu/desktop-directories/*
%attr(0755, software, software) /usr/share/cinnamon/applets/gmenu@noirlab.edu/icons/*
%attr(0755, software, software) /usr/share/cinnamon/applets/gmenu@noirlab.edu/gmenu.menu

%changelog
* Mon Apr 21 2025 Oscar Fuentes <oscar.fuentes@noirlab.edu> - 1.0-1
- Initial package
