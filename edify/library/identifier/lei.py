"""``lei`` — ISO 17442 Legal Entity Identifier (20 alphanumeric chars)."""

from __future__ import annotations

from edify import Pattern

lei = (
    Pattern()
    .start_of_input()
    .exactly(20).any_of().range("A", "Z").range("0", "9").end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the ISO 17442 LEI: 20 uppercase-alphanumeric characters."""
