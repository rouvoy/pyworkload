# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyworkload',
    version='0.1.0',
    description='Workload generator',
    long_description=readme,
    author='Romain Rouvoy',
    author_email='romain@rouvoy.fr',
    url='https://github.com/rouvoy/pyworkload',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

