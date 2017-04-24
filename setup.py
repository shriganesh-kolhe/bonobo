# This file is autogenerated by edgy.project code generator.
# All changes will be overwritten.

import os
from setuptools import setup, find_packages

root_dir = os.path.dirname(os.path.abspath(__file__))

tolines = lambda c: list(filter(None, map(lambda s: s.strip(), c.split('\n'))))


def read(filename, flt=None):
    try:
        with open(filename) as f:
            content = f.read().strip()
            return flt(content) if callable(flt) else content
    except EnvironmentError:
        return ''


# Py3 compatibility hacks, borrowed from IPython.
try:
    execfile
except NameError:

    def execfile(fname, globs, locs=None):
        locs = locs or globs
        exec(compile(open(fname).read(), fname, "exec"), globs, locs)


version_ns = {}
try:
    execfile(os.path.join(root_dir, 'bonobo/_version.py'), version_ns)
except EnvironmentError:
    version = 'dev'
else:
    version = version_ns.get('__version__', 'dev')

setup(
    name='bonobo',
    description='Bonobo',
    license='Apache License, Version 2.0',
    install_requires=[
        'blessings >=1.6,<1.7', 'colorama >=0.3,<0.4', 'psutil >=5.0,<5.1',
        'requests >=2.12,<2.13', 'stevedore >=1.19,<1.20', 'toolz >=0.8,<0.9'
    ],
    version=version,
    long_description=read('README.rst'),
    classifiers=read('classifiers.txt', tolines),
    packages=find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data=True,
    data_files=[('share/jupyter/nbextensions/bonobo-jupyter', [
        'bonobo/ext/jupyter/static/extension.js',
        'bonobo/ext/jupyter/static/index.js',
        'bonobo/ext/jupyter/static/index.js.map'
    ])],
    extras_require={
        'dev': [
            'coverage >=4.3,<4.4', 'mock >=2.0,<2.1', 'nose >=1.3,<1.4',
            'pylint >=1.6,<1.7', 'pytest >=3,<4', 'pytest-cov >=2.4,<2.5',
            'pytest-timeout >=1.2,<1.3', 'sphinx', 'sphinx_rtd_theme', 'yapf'
        ],
        'jupyter': ['jupyter >=1.0,<1.1', 'ipywidgets >=6.0.0.beta5']
    },
    entry_points={
        'bonobo.commands': [
            'init = bonobo.commands.init:register',
            'run = bonobo.commands.run:register',
            'version = bonobo.commands.version:register'
        ],
        'console_scripts': ['bonobo = bonobo.commands:entrypoint'],
        'edgy.project.features':
        ['bonobo = '
         'bonobo.ext.edgy.project.feature:BonoboFeature']
    },
    url='https://bonobo-project.org/',
    download_url=
    'https://github.com/python-bonobo/bonobo/tarball/{version}'.format(
        version=version), )
