"""``imei`` — 15-digit International Mobile Equipment Identity."""

from __future__ import annotations

from edify import Pattern

imei = (
    Pattern()
    .start_of_input()
    .exactly(15).digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for the 15-digit IMEI shape."""
