"""``place`` — permissive place-name / locality shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

place = RegexBackedPattern(r"^[A-Za-z][A-Za-z .,'\-]{1,99}$")
"""Callable :class:`Pattern` for a permissive place-name shape."""
