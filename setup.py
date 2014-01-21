# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys

import djangocms_page_meta

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_page_meta.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='djangocms-page-meta',
    version=version,
    description='OpenGraph, Twitter Card and Google+ snippet tags for django CMS 3 pages',
    long_description=readme + '\n\n' + history,
    author='Iacopo Spalletti',
    author_email='i.spalletti@nephila.it',
    url='https://github.com/nephila/djangocms-page-meta',
    packages=[
        'djangocms_page_meta',
    ],
    include_package_data=True,
    install_requires=open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).readlines(),
    license="BSD",
    zip_safe=False,
    keywords='django cms, meta tags, OpenGraph, Twitter Cards, Google+',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
