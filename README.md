Heretic
======

[![Build Status](https://travis-ci.org/jkloo/Heretic.png?branch=master)](https://travis-ci.org/jkloo/Heretic)
[![Coverage Status](https://coveralls.io/repos/jkloo/Heretic/badge.png?branch=master)](https://coveralls.io/r/jkloo/Heretic?branch=master)
[![PyPI Version](https://badge.fury.io/py/Heretic.png)](http://badge.fury.io/py/Heretic)


Validation engine for verifying conditions are met.


Getting Started
===============

Requirements
------------

* Python 3.3: http://www.python.org/download/releases/3.3.4/#download


Installation
------------

Heretic can be installed with 'pip':

    pip install Heretic

Or directly from the source code:

    git clone https://github.com/jkloo/Heretic.git
    cd Heretic
    python setup.py install



Basic Usage
===========

After installation, abstract base classes can be imported from the package:

    python
    >>> import heretic
    heretic.__version__



For Contributors
================

Requirements
------------

* GNU Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* virtualenv: https://pypi.python.org/pypi/virtualenv#installation
* Pandoc: http://johnmacfarlane.net/pandoc/installing.html


Installation
------------

Create a virtualenv:

    make env

Run the tests:

    make test
    make tests  # includes integration tests

Build the documentation:

    make doc

Run static analysis:

    make pep8
    make pylint
    make check  # pep8 and pylint

Prepare a release:

    make dist  # dry run
    make upload
