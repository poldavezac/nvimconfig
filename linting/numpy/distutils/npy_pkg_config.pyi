# Stubs for numpy.distutils.npy_pkg_config (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class FormatError(IOError):
    msg = ...  # type: Any
    def __init__(self, msg) -> None: ...

class PkgNotFound(IOError):
    msg = ...  # type: Any
    def __init__(self, msg) -> None: ...

def parse_flags(line): ...

class LibraryInfo:
    name = ...  # type: Any
    description = ...  # type: Any
    requires = ...  # type: Any
    version = ...  # type: Any
    vars = ...  # type: Any
    def __init__(self, name, description, version, sections, vars, requires: Optional[Any] = ...) -> None: ...
    def sections(self): ...
    def cflags(self, section: str = ...): ...
    def libs(self, section: str = ...): ...

class VariableSet:
    def __init__(self, d) -> None: ...
    def interpolate(self, value): ...
    def variables(self): ...
    def __getitem__(self, name): ...
    def __setitem__(self, name, value): ...

def read_config(pkgname, dirs: Optional[Any] = ...): ...
