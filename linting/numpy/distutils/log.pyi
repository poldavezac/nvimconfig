# Stubs for numpy.distutils.log (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from distutils.log import *
from distutils.log import Log as old_Log
from .misc_util import red_text as red_text, default_text as default_text, cyan_text as cyan_text, green_text as green_text, is_sequence as is_sequence, is_string as is_string

class Log(old_Log):
    def good(self, msg, *args): ...

good = ...  # type: Any

def set_threshold(level, force: bool = ...): ...
def set_verbosity(v, force: bool = ...): ...
