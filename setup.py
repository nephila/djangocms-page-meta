#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    print('You probably want to also tag the version now:')
    print('  git tag -a %s -m "version %s"' % (version, version))
    print('  git push --tags')
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
    install_requires=(
        'django-cms>=3.0',
        'django-meta>=0.1.0',
        'django-filer>=0.9.5',
        'django-meta-mixin',
    ),
    license='BSD',
    zip_safe=False,
    keywords='django cms, meta tags, OpenGraph, Twitter Cards, Google+',
    test_suite='cms_helper.run',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Framework :: Django',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
