%define rel 1

Summary:        KControl Module which handles Telepathy Accounts
Name:           telepathy-kde-accounts-kcm
Version:        0.2.0
Release:        %mkrel %{rel}
Url:            https://projects.kde.org/projects/playground/network/telepathy/telepathy-accounts-kcm
Source0:        ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%name-%version.tar.bz2
License:        GPLv2+
Group:          Graphical desktop/KDE
BuildRequires:  kdelibs4-devel
BuildRequires:  telepathy-qt4-devel >= 0.1.8
Obsoletes:      telepathy-kde-accounts-kcm-plugins < 0.2.0-0
Provides:       telepathy-accounts-kcm = %version-%release
Obsoletes:      telepathy-accounts-kcm < 0.2.0-0

%description
This is a KControl Module which handles adding/editing/removing Telepathy
Accounts. It interacts with any Telepathy Spec compliant AccountManager,
such as telepathy-accountmanager-kwallet to manipulate the accounts. It is
modular in design, with each ConnectionManager-Protocol combination having a
plugin that provides customised forms for adding or editing their accounts,
and also with a generic plugin which can be used as a fallback for
ConnectionManager-Protocol combinations where no plugin exists.

%files -f telepathy-accounts-kcm.lang
%{_kde_libdir}/kde4/kcm_telepathy_accounts.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_butterfly.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_gabble.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_haze.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_idle.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_rakia.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_salut.so
%{_kde_libdir}/kde4/kcmtelepathyaccounts_plugin_sunshine.so
%{_kde_datadir}/telepathy/profiles/
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop


#--------------------------------------------------------------------
%define major 4
%define libname    %mklibname %{name} %{major}
#Added on 2011/11/27 for the switch to 0.2 to match upstream name
%define oldlibname %mklibname telepathy-accounts-kcm 4


%package -n %{libname}
Summary:    Library package for %{name}
Group:      System/Libraries
%rename %{oldlibname}

%description -n %{libname}
Library package for %{name}.

%files -n %{libname}
%{_kde_libdir}/libkcmtelepathyaccounts.so.%{major}*

#--------------------------------------------------------------------
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
%{_kde_libdir}/libkcmtelepathyaccounts.so

#--------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang telepathy-accounts-kcm

for i in "kcmtelepathyaccounts_plugin_sunshine" "kcmtelepathyaccounts_plugin_salut" "kcmtelepathyaccounts_plugin_rakia" "kcmtelepathyaccounts_plugin_idle" "kcmtelepathyaccounts_plugin_haze" "kcmtelepathyaccounts_plugin_gabble" "kcmtelepathyaccounts_plugin_butterfly"; do
%find_lang $i
cat $i.lang >> telepathy-accounts-kcm.lang
done



