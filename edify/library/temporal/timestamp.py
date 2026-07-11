"""``timestamp`` — Unix millisecond timestamp shape (13-digit integer)."""

from __future__ import annotations

from edify import Pattern

timestamp = (
    Pattern()
    .start_of_input()
    .optional()
    .char("-")
    .between(10, 13)
    .digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for a Unix epoch timestamp in seconds or
milliseconds: optional sign followed by 10-13 digits.
"""
