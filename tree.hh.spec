Summary:	Tree.hh - a STL-like generic container class for n-ary trees
Summary(pl):	Tree.hh - uniwersalna klasa kontenerowa do obs³ugi drzew n-klasowych
Name:		tree.hh
Version:	1.90
Release:	1
License:	GPL v2+
Group:		Development/Libraries
Source0:	http://www.damtp.cam.ac.uk/user/kp229/tree/tree.hh
# Source0-md5:	03039ae44f9738dfaf86422c21a1776d
Source1:	http://www.damtp.cam.ac.uk/user/kp229/tree/tree_util.hh
# Source1-md5:	abbe54395344b362023885e7cb37afbc
Source2:	http://www.damtp.cam.ac.uk/user/kp229/tree/tree.pdf
# Source2-md5:	3e98e874821814b02e666d5504dd01fb
URL:		http://directory.fsf.org/libs/cpp/tree.hh.html
Requires:	libstdc++-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tree.hh library for C++ provides an STL-like container class for
n-ary trees, templated over the data stored at the nodes. Various
types of iterators are provided (post-order, pre-order, and others).
Where possible the access methods are compatible with the STL or
alternative algorithms are available.

%description -l pl
Biblioteka Tree.hh dla C++ udostêpnia uniwersaln± klasê kontenerow±
dla drzew n-klasowych zbli¿on± w obs³udze do standardowych kontenerów
biblioteki STL. Dostêpne s± ró¿ne rodzaje iteratorów (post-order,
pre-order i inne).

%prep
%setup -qcDT

%build
cp -f %{SOURCE2} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_includedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc tree.pdf
%{_includedir}/*.hh
