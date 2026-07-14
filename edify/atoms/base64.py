"""``base64`` — base64-encoded string (with optional padding)."""

from __future__ import annotations

from edify import Pattern

base64 = (
    Pattern()
    .one_or_more()
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .char("+")
    .char("/")
    .end()
    .zero_or_more()
    .char("=")
)
"""Composable :class:`Pattern` fragment for a standard base64 string."""
