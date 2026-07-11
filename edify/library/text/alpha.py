"""``alpha`` — letters-only string shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

alpha = RegexBackedPattern(r"^[A-Za-z]+$")
"""Callable :class:`Pattern` for a letters-only string."""
