from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("collecting_nos_II.pyx")
)