# Stubs for numpy.distutils.extension (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from distutils.extension import Extension as old_Extension

basestring = ...  # type: Any
cxx_ext_re = ...  # type: Any
fortran_pyf_ext_re = ...  # type: Any

class Extension(old_Extension):
    sources = ...  # type: Any
    swig_opts = ...  # type: Any
    depends = ...  # type: Any
    language = ...  # type: Any
    f2py_options = ...  # type: Any
    module_dirs = ...  # type: Any
    extra_f77_compile_args = ...  # type: Any
    extra_f90_compile_args = ...  # type: Any
    def __init__(self, name, sources, include_dirs: Optional[Any] = ..., define_macros: Optional[Any] = ..., undef_macros: Optional[Any] = ..., library_dirs: Optional[Any] = ..., libraries: Optional[Any] = ..., runtime_library_dirs: Optional[Any] = ..., extra_objects: Optional[Any] = ..., extra_compile_args: Optional[Any] = ..., extra_link_args: Optional[Any] = ..., export_symbols: Optional[Any] = ..., swig_opts: Optional[Any] = ..., depends: Optional[Any] = ..., language: Optional[Any] = ..., f2py_options: Optional[Any] = ..., module_dirs: Optional[Any] = ..., extra_f77_compile_args: Optional[Any] = ..., extra_f90_compile_args: Optional[Any] = ...) -> None: ...
    def has_cxx_sources(self): ...
    def has_f2py_sources(self): ...