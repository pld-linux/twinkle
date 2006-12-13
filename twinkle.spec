#
# Conditional build:
%bcond_without	kde		# disable KDE support
#
Summary:	twinkle - SIP Soft Phone
Summary(pl):	twinkle - telefon programowy SIP
Name:		twinkle
Version:	0.9
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.xs4all.nl/~mfnboer/twinkle/download/%{name}-%{version}.tar.gz
# Source0-md5:	74ef85e9f4570cec10bd23d301f5549e
Source1:	%{name}.desktop
URL:		http://www.twinklephone.com/
BuildRequires:	alsa-lib-devel
BuildRequires:	boost-regex-devel
BuildRequires:	commoncpp2-devel >= 1.4.0
BuildRequires:	ccrtp-devel >= 1.5.0
%{?with_kde:BuildRequires:	kdelibs-devel}
BuildRequires:	libsndfile-devel
BuildRequires:	libilbc-devel
BuildRequires:	speex-devel
BuildRequires:	pkgconfig
BuildRequires:	qmake
BuildRequires:	qt-devel >= 6:3.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twinkle is a SIP based soft phone for making telephone calls over IP
networks.

%description -l pl
Twinkle to oparty na SIP programowy telefon do wykonywania po³±czeñ
telefonicznych po sieciach IP.

%prep
%setup -q

%build
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
