"""``uri`` — generic URI shape (``scheme:opaque``)."""

from __future__ import annotations

from edify import Pattern

uri = (
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
    .char(":")
    .one_or_more()
    .anything_but_chars(" \t\r\n")
)
"""Composable :class:`Pattern` fragment for a generic URI."""
