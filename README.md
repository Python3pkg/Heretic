Heretic
======

[![Build Status](https://travis-ci.org/jkloo/Heretic.png?branch=master)](https://travis-ci.org/jkloo/Heretic)
[![Coverage Status](https://coveralls.io/repos/jkloo/Heretic/badge.png?branch=master)](https://coveralls.io/r/jkloo/Heretic?branch=master)
[![PyPI Version](https://badge.fury.io/py/Heretic.png)](http://badge.fury.io/py/Heretic)


Heretic is a Generic Data model viewer and manipulator.

Why?
============
Traditionally any complex data that you might want to store gets dumped into a spreadsheet program with gobs of columns
and hosts of rows. Typically the first row in the spreadsheet contains descriptions of the fields below it. This is a
representation of some abstract object, a data model, and the rows below are instances of that object. This format
appeals to some due to the ability to hide and filter data you dont want out of the way, while still keeping multiple
entities visible on the screen at once. I think we can do better.

Spreadsheet programs fall short as your data grows. How well can you filter your data when you have 10 isntances, 100,
100000? What happens when your data model has 5 attributes, or 10, or 100. The answer is: you filter and hide information.

Ok, so I found the object that I wanted to look at after painstakingly filtering and hiding away information. But now I
want to see all similar objects. I want to see more information about this one instance that I worked so hard to find.
Insert more filtering, more hiding, more headaches.

We can do better, and we are just getting started.


> One data model should be able to reference other data models. 

In ceratin software sects, projects begin with a requirements specification. This specification is a hierarchy of sorts
with usage/system level (read: general) requirements at the top, and generic descriptions of how the code will operate
at the bottom.

Here are data model is a hierarchy of data models. One data model should be able to reference other data models. Your
implementation details need to link all the way up to the usage requirements. To do this in a spreadsheet is maddening.
Spreadsheets have no means for an entire row of data (an instance) to reference another instance.

...



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
