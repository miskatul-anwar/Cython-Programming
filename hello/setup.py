from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("hello.pyx")
    # Let's print hello world!
)
