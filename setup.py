#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Barmaan - is a very simple, easy to use yet powerful monitoring tool.
# Copyright (C) 2013-2014 Yellowen
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# -----------------------------------------------------------------------------

from setuptools import setup, find_packages


setup(name='Barmaan',
      version='2.67.0',
      description='Barmaan is a very simple, easy to use yet powerful monitoring tool.',
      author='Sameer Rahmani, Shervin Ara,',
      author_email='lxsameer@gnu.org, shervin.ara@gmail.com',
      url='http://barmaan.yellowen.com/',
      download_url="http://barmaan.yellowen.com/downloads/",
      keywords="Monitoring",
      license='GPL v2',
      packages=find_packages(),
      install_requires=['Twisted',],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
          ]
)

