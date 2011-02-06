%define		modname front
Summary:	Drupal Frontpage Module
Summary(pl.UTF-8):	Moduł Frontpage (strony tytułowej) dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.7
License:	GPL
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	83e2fc918b3cbd1ad43a1290220bd608
URL:		http://drupal.org/project/front
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules

%description
The Front Page module allows user to specify splash pages or front
pages to their site that are different in layout to the default
theme/style.

Useful if you want to do the following:
- Have a splash front page to your Drupal site that is different from
  your default layout,
- Automatically display a different front page for Anonymous and
  Authenticated Users,
- Easily update/change the contents or the redirects of your front
  page(s) from within the Drupal Administration area,
- Include PHP code in your Front Page(s).

%description -l pl.UTF-8
Moduł Front Page pozwala na określenie stron startowych lub tytułowych
na stronie różniących się w wyglądzie od domyślnego motywu/stylu.

Jest to przydatne jeśli chcemy zrobić takie rzeczy, jak:
- mieć tytułową stronę startową na witrynie Drupala różniącą się od
  domyślnego wyglądu,
- automatycznie wyświetlać różne strony tytułowe dla anonimowych i
  uwierzytelnionych użytkowników,
- łatwo uaktualniać/zmieniać zawartość lub przekierowania strony
  tytułowej z obszaru administracyjnego Drupala,
- włączać kod PHP na stronie tytułowej.

%prep
%setup -q -n %{modname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}

install *.module $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_moddir}/*.module
