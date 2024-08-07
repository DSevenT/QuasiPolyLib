# setup.py
from setuptools import setup, find_packages

setup(
    name='QuasiPolyLib',
    version='0.1.0',
    description='A library for analyzing quasi-polynomials',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Diego Torres-Garcia',
    author_email='diego.imt7@gmail.com',
    url='https://github.com/DSevenT/QuasiPolyLib',
    packages=find_packages(),
    install_requires=[
        # List dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',  
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
