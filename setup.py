# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='maze',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Zachary D. Rowitsch',
    author_email='rowitsch@yahoo.com',
    url='https://github.com/twistdroach/maze-python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

