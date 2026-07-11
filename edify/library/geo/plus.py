"""``plus`` — Google Plus Code (Open Location Code) shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

plus = RegexBackedPattern(
    r"^[23456789CFGHJMPQRVWX]{2,8}\+[23456789CFGHJMPQRVWX]{2,3}(?:\s+.+)?$"
)
"""Callable :class:`Pattern` for a Google Plus Code (Open Location Code)."""
