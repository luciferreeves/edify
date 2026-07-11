"""``integer`` — integer number shape (signed, decimal)."""

from __future__ import annotations

from edify import Pattern

integer = (
    Pattern().start_of_input().optional().any_of_chars("+-").one_or_more().digit().end_of_input()
)
"""Callable :class:`Pattern` for a signed decimal integer."""
