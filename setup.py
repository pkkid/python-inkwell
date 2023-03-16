#!/usr/bin/python3
# -*- coding: utf-8 -*-
from inkwell import VERSION
from pkg_resources import parse_requirements
from setuptools import setup

readme = open('README.md', 'r').read()
with open('requirements.txt') as handle:
    requirements = [str(req) for req in parse_requirements(handle)]

setup(
    name='inkwell',
    version=VERSION,
    description='A minimalistic dark theme for QT',
    author='Michael Shepanski',
    author_email='michael.shepanski@gmail.com',
    url='https://github.com/pkkid/python-inkwell',
    packages=['inkwell'],
    install_requires=requirements,
    python_requires='>=3.7',
    long_description=readme,
    keywords=['qt', 'pyside6', 'theme', 'dark', 'inkwell'],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
    ]
)
