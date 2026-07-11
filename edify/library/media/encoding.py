"""``encoding`` — text encoding name shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

encoding = RegexBackedPattern(r"^[a-zA-Z][a-zA-Z0-9_+.\-]{1,39}$")
"""Callable :class:`Pattern` for a text-encoding name (utf-8, latin-1, etc.)."""
