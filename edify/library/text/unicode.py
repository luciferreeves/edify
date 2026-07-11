"""``unicode`` — any Unicode-letter-or-digit string shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

unicode = RegexBackedPattern(r"^[^\x00-\x1F\x7F]+$")
"""Callable :class:`Pattern` for any Unicode string containing no control codes."""
