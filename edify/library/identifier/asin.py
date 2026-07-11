"""``asin`` — Amazon Standard Identification Number (10-character)."""

from __future__ import annotations

from edify import Pattern

asin = (
    Pattern()
    .start_of_input()
    .exactly(10)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the 10-character alphanumeric ASIN shape."""
