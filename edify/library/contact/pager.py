"""``pager`` — numeric pager-number shape (4-10 digits)."""

from __future__ import annotations

from edify import Pattern

pager = Pattern().start_of_input().between(4, 10).digit().end_of_input()
"""Callable :class:`Pattern` for the numeric pager-number shape: 4-10 digits."""
