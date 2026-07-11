"""``percentage`` — percentage value shape (number followed by ``%``)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

percentage = RegexBackedPattern(r"^-?\d+(?:\.\d+)?\s?%$")
"""Callable :class:`Pattern` for a percentage value: signed number optionally
with a decimal part and a trailing ``%``.
"""
