"""``palette`` — comma-separated list of colours (2-16 entries)."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
palette = RegexBackedPattern(
    r"^(?:#[0-9A-Fa-f]{3,8}|[a-zA-Z]{3,20})"
    r"(?:\s*,\s*(?:#[0-9A-Fa-f]{3,8}|[a-zA-Z]{3,20})){1,15}$"
)
"""Callable :class:`Pattern` for a comma-separated list of 2-16 colours."""
