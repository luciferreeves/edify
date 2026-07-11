"""``natural`` — natural-number shape (positive integers, no leading zero)."""

from __future__ import annotations

from edify import Pattern

natural = Pattern().start_of_input().range("1", "9").zero_or_more().digit().end_of_input()
"""Callable :class:`Pattern` for a positive integer with no leading zero."""
