# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

INSTALL_REQUIRES = ['requests']

setup(
    name='orakwlum_client',
    description='Python interface desired to interact with the okW system',
    version='0.2.1',
    url='https://www.gisce.net',
    author='GISCE Enginyeria, SL',
    author_email='devel@gisce.net',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    license='General Public Licence 3',
    provides=['orakwlum_client'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ]
)