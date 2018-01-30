# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re

INSTALL_REQUIRES = ['requests']

okW = {}
# Get version and metadata of the package
with open("orakwlum_client/__init__.py") as ver_file:
    meta_file=ver_file.read()
    okW = dict(re.findall("__([a-z]+)__ = '([^']+)'", meta_file))

setup(
    name='orakwlum_client',
    description='Python interface desired to interact with the okW system',
    version=okW['version'],
    url='https://www.gisce.net',
    author='GISCE Enginyeria, SL',
    author_email='devel@gisce.net',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    license='General Public Licence 3',
    provides=['orakwlum_client'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ]
)
