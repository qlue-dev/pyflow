# Author: Deepak Pathak (c) 2016

from __future__ import absolute_import, division, print_function

import multiprocessing as mp
from glob import glob

import numpy
from setuptools import Extension, setup
from Cython.Build import cythonize

# from __future__ import unicode_literals

sourcefiles = ['pyflow.pyx', ]
sourcefiles.extend(glob("src/*.cpp"))
extensions = [
    Extension("pyflow", sourcefiles, include_dirs=[numpy.get_include()])]
setup(
    name="pyflow",
    version="1.0.1",
    description="Python wrapper for the Coarse2Fine Optical Flow code.",
    author="Deepak Pathak",
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            'language_level': 3},
        nthreads=mp.cpu_count()),
    include_dirs=[numpy.get_include()]
)
