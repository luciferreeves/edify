"""``medical`` — medical-coding-system code shape (SNOMED, ICD, NPI, RxNorm, LOINC)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

medical = RegexBackedPattern(
    r"^(?:"
    r"\d{6,18}"
    r"|[A-TV-Z][0-9][A-Z0-9](?:\.[A-Z0-9]{1,4})?"
    r"|\d{10}"
    r"|\d{1,7}-\d"
    r")$"
)
"""Callable :class:`Pattern` for medical-coding-system codes."""
