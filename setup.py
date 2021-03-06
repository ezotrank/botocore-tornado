#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

import botocore_tornado

from setuptools import setup, find_packages


def read(filename):
    try:
        return open(filename).read()
    except (OSError, IOError):
        return ""


setup(
    name='botocore-tornado',
    version=botocore_tornado.__version__,
    description='botocore subclasses that uses AsyncHTTPClient',
    long_description=read('README.rst'),
    author='Simon Hewitt',
    author_email='simon@qudos.com.com',
    url='https://github.com/qudos-com/botocore-tornado',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    package_dir={'botocore_tornado': 'botocore_tornado'},
    include_package_data=True,
    install_requires=['botocore>=0.93.0',
                      'tornado>=4.0.0'],
    license=read("LICENSE.txt"),
    classifiers=(
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # not tested on python3 yet!
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
    ),
)
