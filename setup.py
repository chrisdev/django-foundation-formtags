#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
    "Django>=1.6,<1.10",
]

test_requirements = [
    # TODO: put package test requirements here
    "Django>=1.6,<1.10",
]

setup(
    name='django-foundation-formtags',
    version='0.0.6',
    description="Templatetags to add Zurb Foundation support to Django Forms",
    long_description=readme + '\n\n' + history,
    author="Christopher Clarke",
    author_email='cclarke@chrisdev.com',
    url='https://github.com/chrisdev/django-foundation-formtags',
    packages=[
        'foundation_formtags',
    ],
    package_dir={'foundation_formtags':
                 'foundation_formtags'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='foundation_formtags',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='runtests.runtests',
    tests_require=test_requirements
)
