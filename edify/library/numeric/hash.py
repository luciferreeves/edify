"""``hash`` — hex-hash digest shape (any common length)."""

from __future__ import annotations

from edify import Pattern

hash = (
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
"""Callable :class:`Pattern` for a hex-hash digest (8-128 hex characters,
covering CRC-32 through SHA-512).
"""
