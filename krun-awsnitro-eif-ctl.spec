Name:           krun-awsnitro-eif-ctl
Version:        0.1.0
Release:        %autorelease
Summary:        krun-awsnitro EIF configuration tool

License:        Apache-2.0
URL:            https://github.com/virtee/krun-awsnitro-eif-ctl
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
krun-awsnitro EIF configuration tool.}

%description %{_description}

%prep
%autosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -t

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%check
%cargo_test

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/krun-awsnitro-eif-ctl

%changelog
%autochangelog
