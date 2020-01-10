Name: libndp
Version: 1.2
Release: 7%{?dist}
Summary: Library for Neighbor Discovery Protocol
Group: System Environment/Libraries
License: LGPLv2+
URL: http://www.libndp.org/
Source: http://www.libndp.org/files/libndp-%{version}.tar.gz

Patch0: 0001-libndp-fix-cppcheck-Undefined-behavior-Variable-buf-.patch
Patch1: 0001-libndp-validate-the-IPv6-hop-limit.patch
Patch2: 0002-libndb-reject-redirect-and-router-advertisements-fro.patch
Patch3: 0003-libndp-add-option-flags-to-send-messages.patch
Patch4: 0004-ndptool-add-option-to-send-messages-types.patch
Patch5: 0005-libndp-fix-type-of-field-na-in-struct-ndp_msgna.patch
Patch6: 0006-libndp-revert-API-change-for-ndp_msg_send-and-add-nd.patch

%description
This package contains a library which provides a wrapper
for IPv6 Neighbor Discovery Protocol.  It also provides a tool
named ndptool for sending and receiving NDP messages.

%package devel
Group: Development/Libraries
Summary: Libraries and header files for libndp development
Requires: libndp = %{version}-%{release}

%description devel
The libndp-devel package contains the header files and libraries
necessary for developing programs using libndp.

%prep
%setup -q
%patch0 -p1 -b .fix_cppcheck_var_buf
%patch1 -p1 -b .hop-limit
%patch2 -p1 -b .link-local
%patch3 -p1 -b .flags-to-send-msgs
%patch4 -p1 -b .opts-to-send-msgs-types
%patch5 -p1 -b .fix-type-of-na
%patch6 -p1 -b .revert-api-change-for-ndp_msg_send

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name \*.la -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING
%{_libdir}/*so.*
%{_bindir}/ndptool
%{_mandir}/man8/ndptool.8*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue May 17 2016 Eric Garver <egarver@redhat.com> - 1.2-7
- libndp: add option flags to send messages
- ndptool: add option to send messages types
- libndp: fix type of field "na" in "struct ndp_msgna"
- libndp: revert API change for ndp_msg_send() and add

* Sat May 14 2016 Lubomir Rintel <lrintel@redhat.com> - 1.2-6
- libndp: fix hop limit validation [CVE-2016-3698]

* Fri May 06 2016 Lubomir Rintel <lrintel@redhat.com> - 1.2-5
- libndp: validate the IPv6 hop limit [CVE-2016-3698]
- libndb: reject redirect and router advertisements from non-link-local [CVE-2016-3698]

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.2-4
- Mass rebuild 2014-01-24

* Tue Jan 21 2014 Jiri Pirko <jpirko@redhat.com> - 1.2-3
- libndp: fix [cppcheck] Undefined behavior: Variable 'buf' is used as parameter and destination in s[n]printf() [1044084]

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2-2
- Mass rebuild 2013-12-27

* Tue Oct 15 2013 Jiri Pirko <jpirko@redhat.com> - 1.2-1
- Update to 1.2
- libndp: silently ignore packets with optlen 0 [1016064]
- libndp: fix processing for larger options [1016064]
- libndp: do not fail on receiving non-ndp packets [1016078]

* Fri Sep 13 2013 Dan Williams <dcbw@redhat.com> - 1.0-2
- Fix .pc file includes path
- Fix ndptool -v argument

* Thu Aug 08 2013 Jiri Pirko <jpirko@redhat.com> - 1.0-1
- Update to 1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4.20130723git873037a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Dan Williams <dcbw@redhat.com> - 0.1-3.20130723git873037a
- Update to git 873037a

* Fri Jun 07 2013 Jiri Pirko <jpirko@redhat.com> - 0.1-2.20130607git39e1f53
- Update to git 39e1f53

* Sat May 04 2013 Jiri Pirko <jpirko@redhat.com> - 0.1-1.20130504gitca3c399
- Initial build.
