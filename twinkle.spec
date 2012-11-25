#
# Conditional build:
%bcond_with	kde		# disable KDE support
#
Summary:	twinkle - SIP Soft Phone
Summary(pl.UTF-8):	twinkle - telefon programowy SIP
Name:		twinkle
Version:	1.4.2
Release:	16.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.xs4all.nl/~mfnboer/twinkle/download/%{name}-%{version}.tar.gz
# Source0-md5:	d70c8972f296ffd998c7fb698774705b
Source1:	%{name}.desktop
Patch0:		%{name}-nobind.patch
Patch1:		%{name}-build.patch
Patch2:		%{name}-ucommon.patch
Patch3:		%{name}-ilbc.patch
URL:		http://www.twinklephone.com/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	ccrtp-devel >= 2.0.0
BuildRequires:	commoncpp2-devel >= 1.7.1
%{?with_kde:BuildRequires:	kdelibs-devel}
BuildRequires:	libgsm-devel >= 1.0.11
BuildRequires:	webrtc-libilbc-devel
BuildRequires:	libmagic-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libzrtpcpp-devel >= 1.4.3
BuildRequires:	pkgconfig
BuildRequires:	qmake
BuildRequires:	qt-devel >= 6:3.3.0
BuildRequires:	qt-linguist
BuildRequires:	readline-devel
BuildRequires:	speex-devel
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
%patch1 -p0
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
export QTDIR=%{_prefix}
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?with_kde:--without-kde} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/gui/images/twinkle48.png $RPM_BUILD_ROOT%{_pixmapsdir}/twinkle.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/twinkle
%{_pixmapsdir}/twinkle.png
%{_desktopdir}/twinkle.desktop
