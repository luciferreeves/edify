"""``base58`` — Bitcoin-style base58 string."""

from __future__ import annotations

from edify import Pattern

base58 = (
    Pattern()
    .one_or_more()
    .any_of()
    .range("1", "9")
    .range("A", "H")
    .range("J", "N")
    .range("P", "Z")
    .range("a", "k")
    .range("m", "z")
    .end()
)
"""Composable :class:`Pattern` fragment for a base58 string."""
