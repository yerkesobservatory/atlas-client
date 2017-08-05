#!/usr/bin/env python

from setuptools import setup

setup(name='atlas_client',
      version='0.1',
      description='Client package for Atlas telescopes',
      long_description=open('README.md').read(),
      license='LICENSE', 
      author='Remy Prechelt',
      author_email='rprechelt@uchicago.edu',
      url='https://github.com/yerkesobservatory/atlas-client',
      packages=['telescope'],
      install_requires=[
          'colorlog>=3.0.1',
          'gevent>=1.2.2',
          'greenlet>=0.4.12',
          'websocket>=0.2.1']
)
