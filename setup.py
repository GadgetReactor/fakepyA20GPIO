#!/usr/bin/env python
# -*- coding: utf-8 -*

from distutils.core import setup
import os
from gpio import gpio


def get_packages(package):
    """
    Return root package & all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]

def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

setup(
    name='fakepyA20GPIO',
    version='0.1.0',
    description='fakeOPiGPIO is a package to simulate the pyA20 package',
    long_description=open('README.md').read(),
    url='https://github.com/gadgetreactor/fakepyA20GPIO',
    author='Sean Seah',
    license='MIT',
    keywords='OPi fake GPIO',
    packages=['pyA20'],
    install_requires=[],

)
