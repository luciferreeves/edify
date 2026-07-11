"""``swatch`` — single hex or named colour shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
swatch = RegexBackedPattern(r"^(?:#[0-9A-Fa-f]{3,8}|[a-zA-Z]{3,20})$")
"""Callable :class:`Pattern` for a single hex colour or CSS named colour."""
