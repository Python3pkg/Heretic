#!/usr/bin/env python

"""
Setup script for Heretic.
"""

import setuptools

from heretic import __project__, __version__

import os
if os.path.exists('README.rst'):
    README = open('README.rst').read()
else:
    README = ""  # a placeholder, readme is generated on release
CHANGES = open('CHANGES.md').read()


setuptools.setup(
    name=__project__,
    version=__version__,

    description="Heretic is a validation engine for written in python.",
    url='http://pypi.python.org/pypi/Heretic',
    author='Jeff Kloosterman',
    author_email='kloosterman.jeff@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    long_description=(README + '\n' + CHANGES),
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
    ],

    install_requires=[],
)
