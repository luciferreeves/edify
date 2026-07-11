"""``color`` — CSS colour shape (hex/rgb/rgba/hsl/hsla/named)."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
color = RegexBackedPattern(
    r"^(?:#(?:[0-9A-Fa-f]{3,4}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})"
    r"|rgba?\(\s*\d{1,3}%?\s*,\s*\d{1,3}%?\s*,\s*\d{1,3}%?(?:\s*,\s*[\d.]+)?\s*\)"
    r"|hsla?\(\s*\d{1,3}(?:deg)?\s*,\s*\d{1,3}%\s*,\s*\d{1,3}%(?:\s*,\s*[\d.]+)?\s*\)"
    r"|[a-zA-Z]{3,20}"
    r")$"
)
"""Callable :class:`Pattern` for any common CSS colour shape."""
