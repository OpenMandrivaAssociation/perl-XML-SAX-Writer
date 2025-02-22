%define modname	XML-SAX-Writer
%define modver 0.57

Summary:	SAX2 Writer
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/XML::SAX::Writer
Source0:	http://www.cpan.org/modules/by-module/XML/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-Test-Simple
BuildRequires:	perl(Text::Iconv)
BuildRequires:	perl(XML::Filter::BufferText)
BuildRequires:	perl(XML::SAX)

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
%setup -qn %{modname}-%{modver}
chmod 644 README Changes lib/XML/SAX/Writer/XML.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/XML
%{_mandir}/man3/*
