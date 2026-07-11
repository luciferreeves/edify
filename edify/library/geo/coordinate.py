"""``coordinate`` — latitude/longitude coordinate shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

coordinate = RegexBackedPattern(
    r"^-?(?:90(?:\.0+)?|[0-8]?\d(?:\.\d+)?)\s*,\s*"
    r"-?(?:180(?:\.0+)?|(?:1[0-7]\d|[0-9]?\d)(?:\.\d+)?)$"
)
"""Callable :class:`Pattern` for the ``latitude,longitude`` coordinate shape."""
