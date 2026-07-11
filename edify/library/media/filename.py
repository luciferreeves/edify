"""``filename`` — file name shape (basename with extension)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

filename = RegexBackedPattern(r"^[^\x00-\x1f/\\:*?\"<>|]+\.[a-zA-Z0-9]{1,10}$")
"""Callable :class:`Pattern` for a valid file name with extension."""
