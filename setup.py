# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='PasswordManagerApp',
    version='0.1.0',
    description='',
    long_description=readme,
    author='Fergus Haak',
    url='https://github.com/Quickmotions/Password-Manager-App',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

