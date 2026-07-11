"""``altitude`` — altitude value shape (signed number, optional decimal, optional unit)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

altitude = RegexBackedPattern(r"^-?\d+(?:\.\d+)?\s?(?:m|ft|km|mi)?$")
"""Callable :class:`Pattern` for a signed altitude value with optional unit."""
