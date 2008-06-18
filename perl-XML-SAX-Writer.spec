%define module  XML-SAX-Writer
%define name    perl-%{module}
%define version 0.50
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        SAX2 Writer
License:        Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildRequires:  perl(Text::Iconv)
BuildRequires:  perl(XML::Filter::BufferText)
BuildRequires:  perl(XML::SAX)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}
chmod 644 Writer.pm README Changes lib/XML/SAX/Writer/XML.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/XML
%{_mandir}/*/*

