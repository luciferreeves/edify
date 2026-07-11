"""``charset`` — character set name shape."""

from __future__ import annotations

from edify import Pattern

charset = (
    Pattern()
    .start_of_input()
    .letter()
    .between(1, 39)
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("_")
    .char("+")
    .char(".")
    .char("-")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for an IANA character-set name."""
