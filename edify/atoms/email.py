"""``email`` — permissive email address shape."""

from __future__ import annotations

from edify import Pattern

email = (
    Pattern()
    .one_or_more()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char(".")
    .char("_")
    .char("+")
    .char("-")
    .end()
    .char("@")
    .one_or_more()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char(".")
    .char("-")
    .end()
)
"""Composable :class:`Pattern` fragment for a permissive email address."""
