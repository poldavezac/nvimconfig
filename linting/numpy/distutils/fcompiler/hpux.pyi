# Stubs for numpy.distutils.fcompiler.hpux (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from numpy.distutils.fcompiler import FCompiler

compilers = ...  # type: Any

class HPUXFCompiler(FCompiler):
    compiler_type = ...  # type: str
    description = ...  # type: str
    version_pattern = ...  # type: str
    executables = ...  # type: Any
    module_dir_switch = ...  # type: Any
    module_include_switch = ...  # type: Any
    pic_flags = ...  # type: Any
    def get_flags(self): ...
    def get_flags_opt(self): ...
    def get_libraries(self): ...
    def get_library_dirs(self): ...
    def get_version(self, force: int = ..., ok_status: Any = ...): ...
