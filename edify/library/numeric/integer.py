"""``integer`` — integer number shape (signed, decimal)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

integer = RegexBackedPattern(r"^[+-]?\d+$")
"""Callable :class:`Pattern` for a signed decimal integer."""
