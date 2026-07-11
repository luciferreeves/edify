"""``numeric`` — digits-only string shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

numeric = RegexBackedPattern(r"^\d+$")
"""Callable :class:`Pattern` for a digits-only string."""
