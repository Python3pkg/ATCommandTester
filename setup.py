#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

from setuptools import setup, find_packages


setup(
    name='ATCommandTester',

    version='0.1.dev1',

    description='A AT Command Tester Tool',

    url='https://github.com/jat001/ATCommandTester',

    author='Jat',
    author_email='chat@jat.email',

    license='GPLv3+',

    classifiers=[
        'Development Status :: 1 - Planning',

        'Environment :: X11 Applications :: Qt',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
    ],

    packages=find_packages(),

    install_requires=['libATCommand', 'PyQt5'],
)
