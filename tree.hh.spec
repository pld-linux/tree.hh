Summary:	Tree.hh - a STL-like generic container class for n-ary trees
Summary(pl.UTF-8):	Tree.hh - uniwersalna klasa kontenerowa do obsługi drzew n-klasowych
Name:		tree.hh
Version:	2.51
Release:	1
License:	GPL v2
Group:		Development/Libraries
Source0:	http://www.aei.mpg.de/~peekas/tree/tree-%{version}.tar.gz
# Source0-md5:	46981914c41b00fb34631582e3f91c3c
URL:		http://www.aei.mpg.de/~peekas/tree/
Requires:	libstdc++-devel
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

install tree{,_util}.hh $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc tree.pdf
%{_includedir}/*.hh
