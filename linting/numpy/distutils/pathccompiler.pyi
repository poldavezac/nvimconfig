# Stubs for numpy.distutils.pathccompiler (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from distutils.unixccompiler import UnixCCompiler

class PathScaleCCompiler(UnixCCompiler):
    compiler_type = ...  # type: str
    cc_exe = ...  # type: str
    cxx_exe = ...  # type: str
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...