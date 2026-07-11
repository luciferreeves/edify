"""``filter`` — CSS filter function shape."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
filter = RegexBackedPattern(
    r"^(?:blur|brightness|contrast|grayscale|hue-rotate|invert|opacity"
    r"|saturate|sepia|drop-shadow)"
    r"\([^)]+\)$"
)
"""Callable :class:`Pattern` for a CSS filter function call."""
