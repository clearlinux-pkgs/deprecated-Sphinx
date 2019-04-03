#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : deprecated-Sphinx
Version  : 1.8.5
Release  : 107
URL      : https://files.pythonhosted.org/packages/2a/86/8e1e8400bb6eca5ed960917952600fce90599e1cb0d20ddedd81ba163370/Sphinx-1.8.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/2a/86/8e1e8400bb6eca5ed960917952600fce90599e1cb0d20ddedd81ba163370/Sphinx-1.8.5.tar.gz
Source99 : https://files.pythonhosted.org/packages/2a/86/8e1e8400bb6eca5ed960917952600fce90599e1cb0d20ddedd81ba163370/Sphinx-1.8.5.tar.gz.asc
Summary  : Python documentation generator
Group    : Development/Tools
License  : BSD-3-Clause
Requires: deprecated-Sphinx-bin = %{version}-%{release}
Requires: deprecated-Sphinx-license = %{version}-%{release}
Requires: deprecated-Sphinx-python = %{version}-%{release}
Requires: Babel
Requires: Jinja2
Requires: Pygments
Requires: Whoosh
Requires: alabaster
Requires: colorama
Requires: docutils
Requires: imagesize
Requires: packaging
Requires: python-future
Requires: recommonmark
Requires: requests
Requires: setuptools
Requires: six
Requires: snowballstemmer
Requires: sphinxcontrib-websupport
Requires: typing
BuildRequires : Babel
BuildRequires : Jinja2
BuildRequires : MarkupSafe
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : Whoosh
BuildRequires : alabaster
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : docutils-python
BuildRequires : imagesize
BuildRequires : nose
BuildRequires : packaging
BuildRequires : pluggy
BuildRequires : py
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : recommonmark
BuildRequires : requests
BuildRequires : setuptools
BuildRequires : setuptools-python
BuildRequires : six
BuildRequires : snowballstemmer
BuildRequires : sphinxcontrib-websupport
BuildRequires : tox
BuildRequires : typing
BuildRequires : virtualenv

%description
========
Sphinx
========
.. image:: https://img.shields.io/pypi/v/sphinx.svg
:target: https://pypi.org/project/Sphinx/
:alt: Package on PyPI

%package bin
Summary: bin components for the deprecated-Sphinx package.
Group: Binaries
Requires: deprecated-Sphinx-license = %{version}-%{release}

%description bin
bin components for the deprecated-Sphinx package.


%package legacypython
Summary: legacypython components for the deprecated-Sphinx package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-Sphinx package.


%package license
Summary: license components for the deprecated-Sphinx package.
Group: Default

%description license
license components for the deprecated-Sphinx package.


%package python
Summary: python components for the deprecated-Sphinx package.
Group: Default
Provides: deprecated-sphinx-python

%description python
python components for the deprecated-Sphinx package.


%prep
%setup -q -n Sphinx-1.8.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554300416
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-Sphinx
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-Sphinx/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/sphinx-apidoc
%exclude /usr/bin/sphinx-autogen
%exclude /usr/bin/sphinx-build
%exclude /usr/bin/sphinx-quickstart

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-Sphinx/LICENSE

%files python
%defattr(-,root,root,-)
