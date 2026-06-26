from importlib.metadata import PackageNotFoundError, version

from edify.builder.builder import RegexBuilder
from edify.errors.base import EdifyError
from edify.errors.syntax import EdifySyntaxError

try:
    __version__ = version("edify")
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = [
    "EdifyError",
    "EdifySyntaxError",
    "RegexBuilder",
    "__version__",
]
