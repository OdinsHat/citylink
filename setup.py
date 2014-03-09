#!/usr/bin/env python

"""Check if we're using setuptools or ditutils if not available"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = ('mechanize', 'lxml', 'Mailer')

setup(name='citylink-utils',
    version=citylink.__version__,
    description='Simple utility package to handle CityLink dispatches for commercial customers',
    long_description=open('README.md'),
    author='Doug Bromley',
    author_email='doug+clutils@tintophat.com',
    url='https://github.com/OdinsHat/citylink-utils',
    scripts=['citylink.py'],
    license='BSD',
    keywords='citylink courier web scraping',
    platforms = 'any',
    install_requirements=['mechanize', 'lxml', 'Mailer'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
