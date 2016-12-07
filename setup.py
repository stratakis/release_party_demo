#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='release_party_demo',
      version='0.0',
      description="Simple demo app",
      author='Michal Cyprian',
      author_email='mcyprian@redhat.com',
      url='https://github.com/mcyprian/release_party_demo',
      license='MIT',
      packages=['release_party_demo'],
      setup_requires=['setuptools',
                      'flexmock >= 0.9.3',
                      ],
      tests_require=['pytest'],
      )
