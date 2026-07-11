"""``aircraft`` — aircraft-registration shape (e.g. ``N123AB``, ``G-ABCD``)."""

from __future__ import annotations

from edify import Pattern

aircraft = (
    Pattern()
    .start_of_input()
    .between(1, 2)
    .uppercase()
    .optional()
    .char("-")
    .between(1, 5)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for an aircraft-registration mark."""
