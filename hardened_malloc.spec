Name:           hardened_malloc
Version:        12
Release:        1%{?dist}
Summary:        Hardened allocator designed for modern systems

License:        MIT
URL:            https://github.com/GrapheneOS/%{name}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: make
BuildRequires: clang >= 11.0.1
BuildRequires: glibc >= 2.31
BuildRequires: python3 >= 3.8.0
Requires: kernel >= 5.10.0

%undefine _auto_set_build_flags

%global debug_package %{nil}

%description
Hardened allocator designed for modern systems. It has integration into Android's Bionic libc and can be used externally with musl and glibc as a dynamic library for use on other Linux-based platforms. It will gain more portability / integration over time.


%prep
%setup -q


%build
make
echo %{_usr}/lib/libhardened_malloc.so > out/ld.so.preload


%install
%{__install} -Dm 0755 out/libhardened_malloc.so %{buildroot}/%{_usr}/lib/libhardened_malloc.so
%{__install} -Dm 0644 out/ld.so.preload %{buildroot}/%{_sysconfdir}/ld.so.preload


%check
make test


%files
%license LICENSE
%{_usr}/lib/libhardened_malloc.so
%{_sysconfdir}/ld.so.preload


%changelog
* Mon Nov 20 2023 Lukas Hajn <lhajn@redhat.com> - 12-1
- update to v12

* Wed May 4 2022 Lukas Hajn <lhajn@redhat.com> - 11-1
- initial release
