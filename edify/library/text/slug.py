"""``slug`` — URL-safe slug shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

slug = RegexBackedPattern(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
"""Callable :class:`Pattern` for a URL-safe slug: lowercase alphanumerics
separated by single hyphens.
"""
