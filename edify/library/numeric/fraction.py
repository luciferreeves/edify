"""``fraction`` — fraction shape (``A/B`` or mixed ``N A/B``)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

fraction = RegexBackedPattern(r"^-?(?:\d+\s+)?\d+/\d+$")
"""Callable :class:`Pattern` for a fraction shape:
``numerator/denominator`` with optional whole-number prefix.
"""
