%define srcname ktp-accounts-kcm

Summary:	KControl Module which handles Telepathy Accounts
Name:		telepathy-kde-accounts-kcm
Version:	0.5.1
Release:	1	
Url:		https://projects.kde.org/projects/extragear/network/telepathy/ktp-accounts-kcm
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%srcname-%version.tar.bz2
License:	GPLv2+
Group:		Networking/Instant messaging 
BuildRequires:	ktp-common-internals-devel

Requires:	telepathy-kde-auth-handler
Obsoletes:	telepathy-kde-accounts-kcm-plugins < 0.2.0-0
Obsoletes:	telepathy-accounts-kcm < 0.2.0-0

%description
This is a KControl Module which handles adding/editing/removing Telepathy
Accounts. It interacts with any Telepathy Spec compliant AccountManager,
such as telepathy-accountmanager-kwallet to manipulate the accounts.

%files -f kcm_ktp_accounts.lang
%{_kde_libdir}/kde4/kcm_ktp_accounts.so
%{_kde_libdir}/kde4/ktpaccountskcm_plugin_butterfly.so
%{_kde_libdir}/kde4/ktpaccountskcm_plugin_gabble.so
%{_kde_libdir}/kde4/ktpaccountskcm_plugin_haze.so
%{_kde_libdir}/kde4/ktpaccountskcm_plugin_idle.so
%{_kde_libdir}/kde4/ktpaccountskcm_plugin_rakia.so
%{_kde_libdir}/kde4/ktpaccountskcm_plugin_salut.so
%{_kde_libdir}/kde4/ktpaccountskcm_plugin_sunshine.so
%{_kde_datadir}/telepathy/profiles/
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop

#------------------------------------------------------------------------------

%define major 4
%define libname    %mklibname ktpaccountskcminternal %{major}
#Added on 2011/11/27 for the switch to 0.2 to match upstream name
%define oldlibname %mklibname telepathy-accounts-kcm 4


%package -n %{libname}
Summary:    Library package for %{name}
Group:      System/Libraries
%rename %{oldlibname}

%description -n %{libname}
Library package for %{name}.

%files -n %{libname}
%{_kde_libdir}/libktpaccountskcminternal.so.%{major}*

#------------------------------------------------------------------------------

%define develname  %mklibname -d %{name}
# Added on 2011/11/27 for the switch to 0.2 to match upstream name
%define olddevelname %mklibname -d telepathy-accounts-kcm

%package -n %{develname}
Summary:    Development headers for %{name}
Group:      Development/KDE and Qt
Provides:   %{name}-devel = %{version}-%{release}
Requires:   %{libname} = %{version}-%{release}
%rename %{olddevelname}

%description -n %{develname}
This package contains the development headers required to compile software
against %{name}.

%files -n %{develname}
%{_kde_libdir}/libktpaccountskcminternal.so

#------------------------------------------------------------------------------

%prep
%setup -q -n %srcname-%version

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang kcm_ktp_accounts --all-name
