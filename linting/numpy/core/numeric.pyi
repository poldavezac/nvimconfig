# Stubs for numpy.core.numeric (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .umath import invert as invert, sin as sin, UFUNC_BUFSIZE_DEFAULT as UFUNC_BUFSIZE_DEFAULT, ERR_IGNORE as ERR_IGNORE, ERR_WARN as ERR_WARN, ERR_RAISE as ERR_RAISE, ERR_CALL as ERR_CALL, ERR_PRINT as ERR_PRINT, ERR_LOG as ERR_LOG, ERR_DEFAULT as ERR_DEFAULT, PINF as PINF, NAN as NAN
from .numerictypes import longlong as longlong, intc as intc, int_ as int_, float_ as float_, complex_ as complex_, bool_ as bool_
from ._internal import TooHardError as TooHardError
from .arrayprint import array2string as array2string, get_printoptions as get_printoptions, set_printoptions as set_printoptions
from .umath import *
from .numerictypes import *
from .fromnumeric import *

loads = ...  # type: Any

class ComplexWarning(RuntimeWarning): ...

bitwise_not = ...  # type: Any
CLIP = ...  # type: Any
WRAP = ...  # type: Any
RAISE = ...  # type: Any
MAXDIMS = ...  # type: Any
ALLOW_THREADS = ...  # type: Any
BUFSIZE = ...  # type: Any
MAY_SHARE_BOUNDS = ...  # type: Any
MAY_SHARE_EXACT = ...  # type: Any
ndarray = ...  # type: Any
flatiter = ...  # type: Any
nditer = ...  # type: Any
nested_iters = ...  # type: Any
broadcast = ...  # type: Any
dtype = ...  # type: Any
copyto = ...  # type: Any
ufunc = ...  # type: Any

def zeros_like(a, dtype: Optional[Any] = ..., order: str = ..., subok: bool = ...): ...
def ones(shape, dtype: Optional[Any] = ..., order: str = ...): ...
def ones_like(a, dtype: Optional[Any] = ..., order: str = ..., subok: bool = ...): ...
def full(shape, fill_value, dtype: Optional[Any] = ..., order: str = ...): ...
def full_like(a, fill_value, dtype: Optional[Any] = ..., order: str = ..., subok: bool = ...): ...

newaxis = ...  # type: Any
arange = ...  # type: Any
array = ...  # type: Any
zeros = ...  # type: Any
count_nonzero = ...  # type: Any
empty = ...  # type: Any
empty_like = ...  # type: Any
fromstring = ...  # type: Any
fromiter = ...  # type: Any
fromfile = ...  # type: Any
frombuffer = ...  # type: Any
shares_memory = ...  # type: Any
may_share_memory = ...  # type: Any
int_asbuffer = ...  # type: Any
where = ...  # type: Any
concatenate = ...  # type: Any
fastCopyAndTranspose = ...  # type: Any
set_numeric_ops = ...  # type: Any
can_cast = ...  # type: Any
promote_types = ...  # type: Any
min_scalar_type = ...  # type: Any
result_type = ...  # type: Any
lexsort = ...  # type: Any
compare_chararrays = ...  # type: Any
putmask = ...  # type: Any
einsum = ...  # type: Any
dot = ...  # type: Any
inner = ...  # type: Any
vdot = ...  # type: Any
matmul = ...  # type: Any

def asarray(a, dtype: Optional[Any] = ..., order: Optional[Any] = ...): ...
def asanyarray(a, dtype: Optional[Any] = ..., order: Optional[Any] = ...): ...
def ascontiguousarray(a, dtype: Optional[Any] = ...): ...
def asfortranarray(a, dtype: Optional[Any] = ...): ...
def require(a, dtype: Optional[Any] = ..., requirements: Optional[Any] = ...): ...
def isfortran(a): ...
def argwhere(a): ...
def flatnonzero(a): ...
def correlate(a, v, mode: str = ...): ...
def convolve(a, v, mode: str = ...): ...
def outer(a, b, out: Optional[Any] = ...): ...
def alterdot(): ...
def restoredot(): ...
def tensordot(a, b, axes: int = ...): ...
def roll(a, shift, axis: Optional[Any] = ...): ...
def rollaxis(a, axis, start: int = ...): ...
def moveaxis(a, source, destination): ...
def cross(a, b, axisa: int = ..., axisb: int = ..., axisc: int = ..., axis: Optional[Any] = ...): ...
def array_repr(arr, max_line_width: Optional[Any] = ..., precision: Optional[Any] = ..., suppress_small: Optional[Any] = ...): ...
def array_str(a, max_line_width: Optional[Any] = ..., precision: Optional[Any] = ..., suppress_small: Optional[Any] = ...): ...
def set_string_function(f, repr: bool = ...): ...

little_endian = ...  # type: Any

def indices(dimensions, dtype: Any = ...): ...
def fromfunction(function, shape, **kwargs): ...
def isscalar(num): ...
def binary_repr(num, width: Optional[Any] = ...): ...
def base_repr(number, base: int = ..., padding: int = ...): ...
def load(file): ...
def identity(n, dtype: Optional[Any] = ...): ...
def allclose(a, b, rtol: float = ..., atol: float = ..., equal_nan: bool = ...): ...
def isclose(a, b, rtol: float = ..., atol: float = ..., equal_nan: bool = ...): ...
def array_equal(a1, a2): ...
def array_equiv(a1, a2): ...
def seterr(all: Optional[Any] = ..., divide: Optional[Any] = ..., over: Optional[Any] = ..., under: Optional[Any] = ..., invalid: Optional[Any] = ...): ...
def geterr(): ...
def setbufsize(size): ...
def getbufsize(): ...
def seterrcall(func): ...
def geterrcall(): ...

class _unspecified: ...

class errstate:
    call = ...  # type: Any
    kwargs = ...  # type: Any
    def __init__(self, **kwargs) -> None: ...
    oldstate = ...  # type: Any
    oldcall = ...  # type: Any
    def __enter__(self): ...
    def __exit__(self, *exc_info): ...

Inf = ...  # type: Any

inf = ...  # type: Any

infty = ...  # type: Any

Infinity = ...  # type: Any
nan = ...  # type: Any
NaN = ...  # type: Any
False_ = ...  # type: Any
True_ = ...  # type: Any

# Names in __all__ with no definition:
#   FLOATING_POINT_SUPPORT
#   FPE_DIVIDEBYZERO
#   FPE_INVALID
#   FPE_OVERFLOW
#   FPE_UNDERFLOW
#   NINF
#   NZERO
#   PZERO
#   SHIFT_DIVIDEBYZERO
#   SHIFT_INVALID
#   SHIFT_OVERFLOW
#   SHIFT_UNDERFLOW
#   ScalarType
#   UFUNC_PYVALS_NAME
#   absolute
#   add
#   alen
#   all
#   alltrue
#   amax
#   amin
#   any
#   arccos
#   arccosh
#   arcsin
#   arcsinh
#   arctan
#   arctan2
#   arctanh
#   argmax
#   argmin
#   argpartition
#   argsort
#   around
#   bitwise_and
#   bitwise_or
#   bitwise_xor
#   bool8
#   busday_count
#   busday_offset
#   busdaycalendar
#   byte
#   bytes0
#   bytes_
#   cast
#   cbrt
#   cdouble
#   ceil
#   cfloat
#   character
#   choose
#   clip
#   clongdouble
#   clongfloat
#   complex128
#   complex256
#   complex64
#   complexfloating
#   compress
#   conj
#   conjugate
#   copysign
#   cos
#   cosh
#   csingle
#   cumprod
#   cumproduct
#   cumsum
#   datetime64
#   datetime_as_string
#   datetime_data
#   deg2rad
#   degrees
#   diagonal
#   divide
#   double
#   e
#   equal
#   euler_gamma
#   exp
#   exp2
#   expm1
#   fabs
#   find_common_type
#   flexible
#   float128
#   float16
#   float32
#   float64
#   floating
#   floor
#   floor_divide
#   fmax
#   fmin
#   fmod
#   frexp
#   frompyfunc
#   generic
#   geterrobj
#   greater
#   greater_equal
#   half
#   hypot
#   inexact
#   int0
#   int16
#   int32
#   int64
#   int8
#   integer
#   intp
#   is_busday
#   isfinite
#   isinf
#   isnan
#   issctype
#   issubdtype
#   ldexp
#   left_shift
#   less
#   less_equal
#   log
#   log10
#   log1p
#   log2
#   logaddexp
#   logaddexp2
#   logical_and
#   logical_not
#   logical_or
#   logical_xor
#   long
#   longcomplex
#   longdouble
#   longfloat
#   maximum
#   maximum_sctype
#   mean
#   minimum
#   mod
#   modf
#   multiply
#   nbytes
#   ndim
#   negative
#   nextafter
#   nonzero
#   not_equal
#   number
#   obj2sctype
#   object0
#   object_
#   partition
#   pi
#   power
#   prod
#   product
#   ptp
#   put
#   rad2deg
#   radians
#   rank
#   ravel
#   reciprocal
#   remainder
#   repeat
#   reshape
#   resize
#   right_shift
#   rint
#   round_
#   sctype2char
#   sctypeDict
#   sctypeNA
#   sctypes
#   searchsorted
#   seterrobj
#   shape
#   short
#   sign
#   signbit
#   signedinteger
#   single
#   singlecomplex
#   sinh
#   size
#   sometrue
#   sort
#   spacing
#   sqrt
#   square
#   squeeze
#   std
#   str0
#   str_
#   string_
#   subtract
#   sum
#   swapaxes
#   take
#   tan
#   tanh
#   timedelta64
#   trace
#   transpose
#   true_divide
#   trunc
#   typeDict
#   typeNA
#   typecodes
#   ubyte
#   uint
#   uint0
#   uint16
#   uint32
#   uint64
#   uint8
#   uintc
#   uintp
#   ulonglong
#   unicode
#   unicode_
#   unsignedinteger
#   ushort
#   var
#   void
#   void0