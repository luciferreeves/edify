"""``checksum`` — hex checksum shape (any common hash width)."""

from __future__ import annotations

from edify import Pattern

checksum = (
    Pattern()
    .start_of_input()
    .between(8, 128)
    .any_of()
    .range("a", "f")
    .range("A", "F")
    .range("0", "9")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a hex checksum (any common hash width)."""
