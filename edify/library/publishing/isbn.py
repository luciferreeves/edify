"""``isbn`` — ISBN-10 or ISBN-13 shape (with or without dashes)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

isbn = RegexBackedPattern(r"^(?:\d[- ]?){9}[\dXx]$|^(?:\d[- ]?){12}\d$")
"""Callable :class:`Pattern` for ISBN-10 or ISBN-13 shape."""
