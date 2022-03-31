%global real_name cuda_gdb
%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 11-6

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        11.6.124
Release:        1%{?dist}
Summary:        CUDA GDB
License:        GPLv3+ and GPLv3+ with exceptions and GPLv2+ and GPLv2+ with exceptions and GPL+ and LGPLv2+ and LGPLv3+ and BSD and Public Domain and GFDL
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 ppc64le aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-ppc64le/%{real_name}-linux-ppc64le-%{version}-archive.tar.xz
Source2:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz

Requires(post): ldconfig
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
CUDA-GDB is the NVIDIA tool for debugging CUDA applications. It's an extension
to GDB, the GNU Project debugger. The tool provides developers with a mechanism
for debugging CUDA applications running on actual hardware. This enables
developers to debug applications without the potential variations introduced by
simulation and emulation environments.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch ppc64le
%setup -q -T -b 1 -n %{real_name}-linux-ppc64le-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 2 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}

cp -f bin/* %{buildroot}%{_bindir}/
cp -fr share/gdb/* %{buildroot}%{_datadir}/%{name}/
cp -f extras/Debugger/lib64/* %{buildroot}%{_libdir}/
cp -f extras/Debugger/include/* %{buildroot}%{_includedir}/

%{?ldconfig_scriptlets}

%files
%license LICENSE
%{_bindir}/cuda-gdb
%{_bindir}/cuda-gdbserver
%{_datadir}/%{name}
%{_includedir}/cudacoredump.h
%{_includedir}/cudadebugger.h
%{_includedir}/cuda_stdint.h
%{_includedir}/libcudacore.h
%{_libdir}/libcudacore.a

%changelog
* Thu Mar 31 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.124-1
- Update to 11.6.124 (CUDA 11.6.2).

* Tue Mar 08 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.112-1
- Update to 11.6.112 (CUDA 11.6.1).

* Mon Jan 31 2022 Simone Caronni <negativo17@gmail.com> - 1:11.6.55-1
- First build with the new tarball components.
