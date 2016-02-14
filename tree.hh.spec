Summary:	Tree.hh - a STL-like generic container class for n-ary trees
Summary(pl.UTF-8):	Tree.hh - uniwersalna klasa kontenerowa do obsługi drzew n-klasowych
Name:		tree.hh
Version:	3.1
Release:	1
License:	GPL v3
Group:		Development/Libraries
#Source0Download: http://tree.phi-sci.com/download.html
Source0:	http://tree.phi-sci.com/tree-%{version}.tar.gz
# Source0-md5:	559c033dcc60cb9ebaa0bb1b7ecaa678
URL:		http://tree.phi-sci.com/
Requires:	libstdc++-devel >= 6:4.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tree.hh library for C++ provides an STL-like container class for
n-ary trees, templated over the data stored at the nodes. Various
types of iterators are provided (post-order, pre-order, and others).
Where possible the access methods are compatible with the STL or
alternative algorithms are available.

%description -l pl.UTF-8
Biblioteka Tree.hh dla C++ udostępnia uniwersalną klasę kontenerową
dla drzew n-klasowych zbliżoną w obsłudze do standardowych kontenerów
biblioteki STL. Dostępne są różne rodzaje iteratorów (post-order,
pre-order i inne).

%prep
%setup -q -n tree-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

cp -p src/tree{,_util}.hh $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/*.html doc/*.css doc/*.png
%{_includedir}/tree.hh
%{_includedir}/tree_util.hh
