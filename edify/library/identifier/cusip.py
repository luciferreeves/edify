"""``cusip`` — 9-character CUSIP securities identifier."""

from __future__ import annotations

from edify import Pattern

cusip = (
    Pattern()
    .start_of_input()
    .exactly(9).any_of().range("A", "Z").range("0", "9").end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the 9-character alphanumeric CUSIP shape."""
