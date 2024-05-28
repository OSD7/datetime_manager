# setup.py
from setuptools import setup, find_packages

setup(
    name='datetime_manager',
    version='0.1.0',
    description='A package for managing dates and times.',
    author='OSD7',
    packages=find_packages(),
    install_requires=[
        'pytz'
    ],
    tests_require=['unittest'],
)

