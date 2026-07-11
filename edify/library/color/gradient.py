"""``gradient`` — CSS gradient shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

gradient = RegexBackedPattern(r"^(?:linear|radial|conic)-gradient\([^()]*(?:\([^()]*\)[^()]*)*\)$")
"""Callable :class:`Pattern` for a CSS gradient function call."""
