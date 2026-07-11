"""``datetime`` — combined date-time shape (ISO 8601 / RFC 3339 / common variants)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

datetime = RegexBackedPattern(
    r"^(?:"
    r"\d{4}-\d{2}-\d{2}[Tt ]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?"
    r"(?:[Zz]|[+-]\d{2}:?\d{2})?"
    r"|\d{4}\d{2}\d{2}[Tt]\d{2}\d{2}\d{2}(?:[Zz]|[+-]\d{4})?"
    r")$"
)
"""Callable :class:`Pattern` for combined date-time shapes: ISO 8601 /
RFC 3339 forms with ``T`` or space separator, optional fractional seconds,
optional timezone suffix.
"""
