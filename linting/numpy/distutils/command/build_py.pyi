# Stubs for numpy.distutils.command.build_py (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from distutils.command.build_py import build_py as old_build_py

class build_py(old_build_py):
    packages = ...  # type: Any
    def run(self): ...
    def find_package_modules(self, package, package_dir): ...
    def find_modules(self): ...