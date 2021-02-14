# TODO:
# - g729 support: https://github.com/LubosD/twinkle/issues/104
#
Summary:	twinkle - SIP Soft Phone
Summary(pl.UTF-8):	twinkle - telefon programowy SIP
Name:		twinkle
Version:	1.10.2
Release:	2
License:	GPL v2
Group:		Applications/Communications
Source0:	https://github.com/LubosD/twinkle/archive/v%{version}.tar.gz
# Source0-md5:	ca6884f9834a25e89fc945b48a91c7a2
Patch0:		ilbc.patch
Patch1:		webrtc-libilbc3.patch
URL:		http://twinkle.dolezel.info/
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	alsa-lib-devel
#BuildRequires:	bcg729-devel
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	ccrtp-devel >= 2.0.0
BuildRequires:	cmake
BuildRequires:	flex
BuildRequires:	libgsm-devel >= 1.0.11
BuildRequires:	libmagic-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libzrtpcpp-devel >= 1.4.3
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	speex-devel
BuildRequires:	ucommon-devel
BuildRequires:	webrtc-libilbc-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twinkle is a SIP based soft phone for making telephone calls over IP
networks.

%description -l pl.UTF-8
Twinkle to oparty na SIP programowy telefon do wykonywania połączeń
telefonicznych po sieciach IP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake \
	-DWITH_ALSA=ON \
	-DWITH_SPEEX=ON \
	-DWITH_ILBC=ON \
	-DWITH_ZRTP=ON \
	-DWITH_G729=OFF \
	-DWITH_QT5=ON \
	-DWITH_DIAMONDCARD=OFF \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md THANKS
%attr(755,root,root) %{_bindir}/twinkle
%attr(755,root,root) %{_bindir}/twinkle-console
%{_datadir}/twinkle
%{_pixmapsdir}/twinkle.png
%{_desktopdir}/twinkle.desktop
%{_iconsdir}/*/*/apps/twinkle.png
%{_iconsdir}/*/*/apps/twinkle.svg
%{_mandir}/man1/twinkle.1*
