#!/usr/bin/env python
#
#  Copyright (c) 2013, Corey Goldberg (cgoldberg@gmail.com)
#
#  license: GNU LGPL
#
#  This file is part of: ystockquote
#  https://github.com/cgoldberg/ystockquote
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#


"""setup/install script for ystockquote"""


import os
from distutils.core import setup

from ystockquote import __version__

this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.rst')) as f:
    LONG_DESCRIPTION = '\n' + f.read()

setup(
    name='ystockquote',
    version=__version__,
    py_modules=['ystockquote'],
    author='Corey Goldberg',
    author_email='cgoldberg _at_ gmail.com',
    description='retrieve stock quote data from Yahoo Finance',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/cgoldberg/ystockquote',
    download_url='http://pypi.python.org/pypi/ystockquote',
    keywords='stocks stockmarket market finance yahoo quotes'.split(),
    license='GNU LGPLv2+',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: GNU Lesser General Public License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Investment',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ]
)
