%define	oname	rdiscount

Summary:	Discount (For Ruby) Implementation of John Gruber's Markdown
Name:		ruby-%{oname}
# (proyvind): stick with 1.3.1.1 for now as it's explicitly required by gitorious...
Version:	1.3.1.1
Release:	%mkrel 1
License:	BSD
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems ruby-devel
Requires:	ruby

%description
Discount (For Ruby) Implementation of John Gruber's Markdown.

%prep

%build

%install
rm -rf %{buildroot}
gem install --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

mv %{buildroot}%{ruby_gemdir}/bin %{buildroot}%{_prefix}

rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{_bindir}/*
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

