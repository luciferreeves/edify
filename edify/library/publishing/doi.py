"""``doi`` — DOI shape."""

from __future__ import annotations

from edify import Pattern

doi = (
    Pattern()
    .start_of_input()
    .string("10.")
    .between(4, 9)
    .digit()
    .char("/")
    .one_or_more()
    .any_of()
    .char("-")
    .char(".")
    .char("_")
    .char(";")
    .char("(")
    .char(")")
    .char("/")
    .char(":")
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the DOI shape."""
