"""``ascii`` — printable-ASCII-only string shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

ascii = RegexBackedPattern(r"^[\x20-\x7E]+$")
"""Callable :class:`Pattern` for a printable-ASCII-only string
(characters ``0x20``–``0x7E``).
"""
