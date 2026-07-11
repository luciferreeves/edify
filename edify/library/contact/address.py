"""``address`` — permissive street-address shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

address = RegexBackedPattern(
    r"^\d+\s+[A-Za-z0-9\s.,'\-#/]+$"
)
"""Callable :class:`Pattern` for a permissive street-address shape:
one or more digits followed by whitespace and address body characters.
"""
