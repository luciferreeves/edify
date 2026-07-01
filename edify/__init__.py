import importlib.metadata

from edify.builder.builder import RegexBuilder
from edify.errors.base import EdifyError
from edify.errors.syntax import EdifySyntaxError
from edify.pattern.composition import Pattern


def _resolve_installed_version() -> str:
    """Return the installed package version or ``"0.0.0"`` when metadata is missing."""
    try:
        return importlib.metadata.version("edify")
    except importlib.metadata.PackageNotFoundError:
        return "0.0.0"


__version__ = _resolve_installed_version()

__all__ = [
    "EdifyError",
    "EdifySyntaxError",
    "Pattern",
    "RegexBuilder",
    "__version__",
]
