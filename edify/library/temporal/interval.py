"""``interval`` — ISO 8601 time-interval shape (``start/end`` or ``start/duration``)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

interval = RegexBackedPattern(
    r"^\d{4}-\d{2}-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?"
    r"(?:[Zz]|[+-]\d{2}:?\d{2})?"
    r"/"
    r"(?:\d{4}-\d{2}-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?"
    r"(?:[Zz]|[+-]\d{2}:?\d{2})?"
    r"|P(?!$)(?:\d+(?:\.\d+)?Y)?(?:\d+(?:\.\d+)?M)?"
    r"(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?"
    r"(?:T(?=\d)(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?"
    r"(?:\d+(?:\.\d+)?S)?)?"
    r")$"
)
"""Callable :class:`Pattern` for the ISO 8601 time-interval shape:
``start-datetime/end-datetime`` or ``start-datetime/duration``.
"""
