"""``scheme`` — URI scheme shape (letter + letter/digit/+/./-)."""

from __future__ import annotations

from edify import Pattern

scheme = (
    Pattern()
    .letter()
    .zero_or_more()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("+")
    .char(".")
    .char("-")
    .end()
)
"""Composable :class:`Pattern` fragment for a URI scheme."""
