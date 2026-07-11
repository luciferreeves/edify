"""``version`` — permissive version-string shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

version = RegexBackedPattern(r"^v?\d+(?:\.\d+){0,3}(?:[-.+][a-zA-Z0-9.\-]+)?$")
"""Callable :class:`Pattern` for a permissive dotted version string."""
