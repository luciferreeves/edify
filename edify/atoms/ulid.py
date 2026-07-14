"""``ulid`` — 26-character Crockford base32 ULID."""

from __future__ import annotations

from edify import Pattern

ulid = (
    Pattern()
    .exactly(26)
    .any_of()
    .range("0", "9")
    .range("A", "H")
    .range("J", "K")
    .char("M")
    .char("N")
    .range("P", "T")
    .range("V", "Z")
    .end()
)
"""Composable :class:`Pattern` fragment for a Crockford-base32 ULID."""
