#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup(
    author="dem4ply",
    author_email='dem4ply@gmail.com',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="send the metada of chibi_dl to elasticseach",
    entry_points={
        'console_scripts': [
            'chibi_dl_elasticsearch=chibi_dl_elasticsearch.cli:main',
        ],
    },
    install_requires=requirements,
    license="WTFPL",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='chibi_dl_elasticsearch',
    name='chibi_dl_elasticsearch',
    packages=find_packages(include=['chibi_dl_elasticsearch', 'chibi_dl_elasticsearch.*']),
    url='https://github.com/dem4ply/chibi_dl_elasticsearch',
    version='0.0.1',
    zip_safe=False,
)
