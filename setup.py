#!/usr/bin/env python
from setuptools import setup, find_packages
import versioneer

setup(
    name='intake-questhdf5',
    version=versioneer.get_version(),
    description='Quest Hdf5 plugins for Intake',
    url='',
    maintainer='',
    maintainer_email='',
    license='BSD',
    py_modules=['intake_questhdf5'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['intake', 'pandas'],
    long_description="",
    zip_safe=False,
)
