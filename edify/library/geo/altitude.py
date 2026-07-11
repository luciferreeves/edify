"""``altitude`` — altitude value shape (signed number, optional decimal, optional unit)."""

from __future__ import annotations

from edify import Pattern

altitude = (
    Pattern()
    .start_of_input()
    .optional()
    .char("-")
    .one_or_more()
    .digit()
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
    .optional()
    .whitespace_char()
    .optional()
    .any_of("m", "ft", "km", "mi")
    .end_of_input()
)
"""Callable :class:`Pattern` for a signed altitude value with optional unit."""
