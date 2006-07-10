#
# Conditional build:
%bcond_without	kde		# disable KDE support
#
Summary:	twinkle - SIP Soft Phone
Summary(pl):	twinkle - telefon programowy SIP
Name:		twinkle
Version:	0.8.1
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.xs4all.nl/~mfnboer/twinkle/download/%{name}-%{version}.tar.gz
# Source0-md5:	245ffd3b4a6f968d8f80d42f6aad079c
Source1:	%{name}.desktop
Patch0:		%{name}-gcc4.patch
Patch1:		%{name}-gsm.patch
Patch2:		%{name}-from-mainwindow.patch
URL:		http://www.twinklephone.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	alsa-lib-devel
BuildRequires:	boost-regex-devel
BuildRequires:	commoncpp2-devel >= 1.3.0
BuildRequires:	ccrtp-devel >= 1.3.4
%{?with_kde:BuildRequires:	kdelibs-devel}
BuildRequires:	libtool
BuildRequires:	libgsm-devel >= 1.0.11
BuildRequires:	libilbc-devel
BuildRequires:	libsndfile-devel
BuildRequires:	pkgconfig
BuildRequires:	qmake
BuildRequires:	qt-devel >= 6:3.3.0
BuildRequires:	speex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twinkle is a SIP based soft phone for making telephone calls over IP
networks.

%description -l pl
Twinkle to oparty na SIP programowy telefon do wykonywania po³±czeñ
telefonicznych po sieciach IP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1 # seems obsolete (arekm?)

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
