#!/usr/bin/env python
#coding:utf-8
# Author:  smeggingsmegger
# Purpose: setup
# Created: 2016-04-01
#
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return "File '%s' not found.\n" % fname

long_description = read('README.md')

if os.path.exists('README.rst'):
    long_description = open('README.rst').read()

setup(
    name='PyScanii',
    version='1.1.4',
    url='http://github.com/smeggingsmegger/PyScanii',
    license='MIT',
    author='Scott Blevins',
    author_email='sblevins@gmail.com',
    description='A Python wrapper for Scanii.com',
    long_description= long_description+'\n'+read('CHANGES'),
    platforms='OS Independent',
    packages=['PyScanii'],
    include_package_data=True,
    install_requires=['requests'],
    keywords=['Scan', 'Virus', 'Scanii', 'API'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
