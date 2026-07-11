"""``mgrs`` — Military Grid Reference System coordinate shape."""

from __future__ import annotations

from edify import Pattern

mgrs = (
    Pattern()
    .start_of_input()
    .between(1, 2)
    .digit()
    .any_of()
    .range("C", "H")
    .range("J", "N")
    .range("P", "X")
    .end()
    .exactly(2)
    .uppercase()
    .any_of()
    .exactly(2)
    .digit()
    .exactly(4)
    .digit()
    .exactly(6)
    .digit()
    .exactly(8)
    .digit()
    .exactly(10)
    .digit()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for an MGRS coordinate."""
