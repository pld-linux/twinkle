#
# Conditional build:
%bcond_with	kde		# enable KDE support
#
Summary:	twinkle - SIP Soft Phone
Name:		twinkle
Version:	0.4.2
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.xs4all.nl/~mfnboer/twinkle/download/%{name}-%{version}.tar.gz
# Source0-md5:	cffa1f6a477d1342561ce6be8ea58302
URL:		http://www.twinklephone.com/
BuildRequires:	alsa-lib-devel
BuildRequires:	commoncpp2-devel >= 1.3.0
BuildRequires:	ccrtp-devel >= 1.3.4
%{?with_kde:BuildRequires:	kdelibs-devel}
BuildRequires:	pkgconfig
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twinkle is a SIP based soft phone for making telephone calls over IP
networks.

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
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/gui/images/twinkle48.png $RPM_BUILD_ROOT%{_pixmapsdir}/twinkle.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/twinkle
%{_pixmapsdir}/twinkle.png
