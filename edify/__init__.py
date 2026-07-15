import importlib.metadata

from edify.builder.fluent import RegexBuilder
from edify.errors.base import EdifyError
from edify.errors.syntax import EdifySyntaxError
from edify.pattern.anchors import END, START
from edify.pattern.boundaries import NON_WORD_BOUNDARY, WORD_BOUNDARY
from edify.pattern.classes import (
    ALPHANUMERIC,
    ANY_CHAR,
    CARRIAGE_RETURN,
    DIGIT,
    LETTER,
    LOWERCASE,
    NEW_LINE,
    NON_DIGIT,
    NON_WHITESPACE,
    NON_WORD,
    NULL_BYTE,
    TAB,
    UPPERCASE,
    WHITESPACE,
    WORD,
)
from edify.pattern.composition import Pattern
from edify.pattern.factories import (
    any_of,
    assert_ahead,
    assert_behind,
    assert_not_ahead,
    assert_not_behind,
    at_least,
    at_most,
    back_reference,
    between,
    between_lazy,
    capture,
    char,
    chars,
    exactly,
    group,
    named_back_reference,
    named_capture,
    nonchars,
    nonrange,
    nonstring,
    one_or_more,
    one_or_more_lazy,
    optional,
    range_of,
    string,
    zero_or_more,
    zero_or_more_lazy,
)
from edify.result import Regex


def _resolve_installed_version() -> str:
    """Return the installed package version or ``"0.0.0"`` when metadata is missing."""
    try:
        return importlib.metadata.version("edify")
    except importlib.metadata.PackageNotFoundError:
        return "0.0.0"


__version__ = _resolve_installed_version()

__all__ = [
    "ALPHANUMERIC",
    "ANY_CHAR",
    "CARRIAGE_RETURN",
    "DIGIT",
    "END",
    "LETTER",
    "LOWERCASE",
    "NEW_LINE",
    "NON_DIGIT",
    "NON_WHITESPACE",
    "NON_WORD",
    "NON_WORD_BOUNDARY",
    "NULL_BYTE",
    "START",
    "TAB",
    "UPPERCASE",
    "WHITESPACE",
    "WORD",
    "WORD_BOUNDARY",
    "EdifyError",
    "EdifySyntaxError",
    "Pattern",
    "Regex",
    "RegexBuilder",
    "__version__",
    "any_of",
    "assert_ahead",
    "assert_behind",
    "assert_not_ahead",
    "assert_not_behind",
    "at_least",
    "at_most",
    "back_reference",
    "between",
    "between_lazy",
    "capture",
    "char",
    "chars",
    "exactly",
    "group",
    "named_back_reference",
    "named_capture",
    "nonchars",
    "nonrange",
    "nonstring",
    "one_or_more",
    "one_or_more_lazy",
    "optional",
    "range_of",
    "string",
    "zero_or_more",
    "zero_or_more_lazy",
]
