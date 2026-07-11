"""``uri`` — generic URI shape (scheme + path)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

uri = RegexBackedPattern(
    r"^[a-zA-Z][a-zA-Z0-9+.\-]*:[^\s]+$"
)
"""Callable :class:`Pattern` for the generic URI shape:
``scheme:opaque-or-path`` where scheme starts with a letter.
"""
