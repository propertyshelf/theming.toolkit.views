# -*- coding: utf-8 -*-
"""
This module contains the tool of theming.toolkit.views
"""
import os
from setuptools import setup, find_packages

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='theming.toolkit.views',
      version=version,
      description="",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Framework :: Zope2",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='Plone Views Propertyshelf',
      author='Jens Krause',
      author_email='jens@propertyshelf.com',
      url='https://github.com/propertyshelf/theming.toolkit.views',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['theming', 'theming.toolkit'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.mls.listing',
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*- 
      [z3c.autoinclude.plugin]
      target = plone
      """
      )
