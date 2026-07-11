"""``geohash`` — geohash string shape (1-12 base32-encoded chars)."""

from __future__ import annotations

from edify import Pattern

geohash = (
    Pattern()
    .start_of_input()
    .between(1, 12)
    .any_of()
    .range("0", "9")
    .any_of_chars("bcdefghjkmnpqrstuvwxyz")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the geohash string shape."""
