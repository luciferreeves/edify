"""``scientific`` — scientific-notation number shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

scientific = RegexBackedPattern(r"^[+-]?\d+(?:\.\d+)?[eE][+-]?\d+$")
"""Callable :class:`Pattern` for scientific-notation shape."""
