"""``pin`` — numeric PIN shape (4–12 digits)."""

from __future__ import annotations

from edify import Pattern

pin = (
    Pattern()
    .start_of_input()
    .between(4, 12).digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for the numeric PIN shape: 4–12 digits."""
