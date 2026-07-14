"""``username`` — permissive social-handle shape (3-30 chars)."""

from __future__ import annotations

from edify import Pattern

username = (
    Pattern()
    .between(3, 30)
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char(".")
    .char("_")
    .char("-")
    .end()
)
"""Composable :class:`Pattern` fragment for a social-handle username."""
