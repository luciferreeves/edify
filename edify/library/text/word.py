"""``word`` — Python word-character string shape (``\\w+``)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

word = RegexBackedPattern(r"^\w+$")
"""Callable :class:`Pattern` for a word-character string:
letters, digits, and underscores.
"""
