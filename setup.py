# setup.py
from setuptools import setup, find_packages

setup(
    name='datetime_manager',
    version='0.1.0',
    description='A package for managing dates and times.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'pytz'
    ],
    tests_require=['unittest'],
)

