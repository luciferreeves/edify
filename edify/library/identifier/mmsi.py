"""``mmsi`` — 9-digit Maritime Mobile Service Identity."""

from __future__ import annotations

from edify import Pattern

mmsi = (
    Pattern()
    .start_of_input()
    .exactly(9).digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for the 9-digit MMSI shape."""
