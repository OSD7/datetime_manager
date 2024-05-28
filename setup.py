# setup.py
from glob import glob
from os.path import basename, splitext
from setuptools import setup, find_packages

setup(
    name='datetime_manager',
    version='0.1.0',
    description='A package for managing dates and times.',
    author='OSD7',
    url="https://github.com/OSD7/datetime_manager",
    packages=find_packages(),
    install_requires= ["pytz"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

