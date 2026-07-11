"""``printable`` — printable-character string shape (excludes control codes)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

printable = RegexBackedPattern(r"^[^\x00-\x1F\x7F]+$")
"""Callable :class:`Pattern` for a printable-character string
(excludes ASCII control codes).
"""
