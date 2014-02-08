%define upstream_name    XML-SAX-Writer
%define upstream_version 0.53

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	9

Summary:	SAX2 Writer
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Text::Iconv)
BuildRequires:	perl(XML::Filter::BufferText)
BuildRequires:	perl(XML::SAX)
BuildArch:	noarch

%description
A new XML Writer was needed to match the SAX2 effort because quite naturally no
existing writer understood SAX2. My first intention had been to start patching
XML::Handler::YAWriter as it had previously been my favourite writer in the
SAX1 world.

However the more I patched it the more I realised that what I thought was going
to be a simple patch (mostly adding a few event handlers and changing the
attribute syntax) was turning out to be a rewrite due to various ideas I'd been
collecting along the way. Besides, I couldn't find a way to elegantly make it
work with SAX2 without breaking the SAX1 compatibility which people are
probably still using. There are of course ways to do that, but most require
user interaction which is something I wanted to avoid.

So in the end there was a new writer. I think it's in fact better this way as
it helps keep SAX1 and SAX2 separated.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 README Changes lib/XML/SAX/Writer/XML.pm

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/XML
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.530.0-6mdv2012.0
+ Revision: 765852
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.530.0-4
+ Revision: 763379
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.530.0-3
+ Revision: 667457
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.530.0-2mdv2011.0
+ Revision: 564825
- rebuild for perl 5.12.1

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.530.0-1mdv2011.0
+ Revision: 552695
- update to 0.53

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.520.0-1mdv2010.1
+ Revision: 401853
- rebuild using %%perl_convert_version

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.52-1mdv2009.1
+ Revision: 305770
- new version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.50-3mdv2009.0
+ Revision: 224663
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.50-2mdv2008.1
+ Revision: 133734
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Sep 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.50-1mdv2007.0
- New version 0.50
- drop patch

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.44-5mdv2007.0
- Rebuild

* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.44-4mdk
- Fix According to perl Policy

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.44-3mdk
- Fix BuildRequires

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.44-2mdk 
- spec cleanup
- don't ship useless empty directories
- make test in %%check

* Sun Jan 23 2005 Guillaume Rousse <guillomovitch@mandrake.org> 0.44-1mdk 
- first mdk release

