#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from django_paystack/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("django_paystack", "__init__.py")


if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.md').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
# requirements = open('requirements.txt').readlines()

setup(
    name='django_paystack',
    version=version,
    description="""Django Paystack Payments package""",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    author='Chinonso Ani',
    author_email='achinonso@gmail.com',
    url='https://github.com/kingnonso/django_paystack',
    packages=[
        'django_paystack',
    ],
    include_package_data=True,
    python_requires = '>=3.9',
    install_requires=[
        "Django>=3.2",
        "pypaystack2==2.0.3"
    ],
    license="MIT",
    zip_safe=False,
    keywords='django_paystack',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
