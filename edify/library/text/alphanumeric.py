"""``alphanumeric`` — letters-and-digits-only string shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

alphanumeric = RegexBackedPattern(r"^[A-Za-z0-9]+$")
"""Callable :class:`Pattern` for a letters-and-digits-only string."""
