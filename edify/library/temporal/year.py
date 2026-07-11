"""``year`` — 4-digit calendar year shape."""

from __future__ import annotations

from edify import Pattern

year = Pattern().start_of_input().exactly(4).digit().end_of_input()
"""Callable :class:`Pattern` for the 4-digit calendar-year shape."""
