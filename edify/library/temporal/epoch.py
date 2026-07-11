"""``epoch`` — Unix epoch seconds shape (10-digit integer, allow negative)."""

from __future__ import annotations

from edify import Pattern

epoch = (
    Pattern()
    .start_of_input()
    .optional()
    .char("-")
    .between(1, 10)
    .digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for a Unix epoch-seconds value: optional sign
followed by 1-10 digits (fits in a 32-bit signed integer).
"""
