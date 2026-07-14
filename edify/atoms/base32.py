"""``base32`` — base32-encoded string (RFC 4648, with optional padding)."""

from __future__ import annotations

from edify import Pattern

base32 = (
    Pattern().one_or_more().any_of().range("A", "Z").range("2", "7").end().zero_or_more().char("=")
)
"""Composable :class:`Pattern` fragment for a base32 string."""
