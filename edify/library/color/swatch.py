"""``swatch`` — single hex or named colour shape."""

from __future__ import annotations

from edify import Pattern

swatch = (
    Pattern()
    .start_of_input()
    .any_of()
    .group()
    .char("#")
    .between(3, 8)
    .any_of()
    .range("0", "9")
    .range("A", "F")
    .range("a", "f")
    .end()
    .end()
    .between(3, 20)
    .letter()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a single hex colour or CSS named colour."""
