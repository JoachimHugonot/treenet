import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "treenet",
    version = "0.0.1",
    author = "Romain Edelmann",
    author_email = "romain.edelmann@epfl.ch",
    description = "Recursive Neural Networks for PyTorch",
    license = "GPLv3",
    keywords = "recursive neural network tree lstm tree-lstm",
    url = "https://github.com/epfl-lara/treenet",
    packages=['treenet', 'tests'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python 2",
        "Programming Language :: Python 3",
    ],
    project_urls={
        "Source": 'https://github.com/epfl-lara/treenet',
        "Tracker": 'https://github.com/epfl-lara/treenet/issues',
    },
    install_requires=[
        "torch>=0.3"
    ]
)