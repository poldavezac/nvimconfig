# Stubs for numpy.distutils.cpuinfo (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class CPUInfoBase:
    def __getattr__(self, name): ...

class LinuxCPUInfo(CPUInfoBase):
    info = ...  # type: Any
    def __init__(self) -> None: ...

class IRIXCPUInfo(CPUInfoBase):
    info = ...  # type: Any
    def __init__(self) -> None: ...
    def get_ip(self): ...

class DarwinCPUInfo(CPUInfoBase):
    info = ...  # type: Any
    def __init__(self) -> None: ...

class SunOSCPUInfo(CPUInfoBase):
    info = ...  # type: Any
    def __init__(self) -> None: ...

class Win32CPUInfo(CPUInfoBase):
    info = ...  # type: Any
    pkey = ...  # type: str
    def __init__(self) -> None: ...

cpu = ...  # type: Any
