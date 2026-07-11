"""``codec`` — media codec name shape."""

from __future__ import annotations

from edify import Pattern

codec = (
    Pattern()
    .start_of_input()
    .letter()
    .between(1, 29)
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("_")
    .char(".")
    .char("-")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a media codec name (``h264``, ``vp9``, ``aac``, etc.)."""
