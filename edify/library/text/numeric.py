"""``numeric`` — digits-only string shape."""

from __future__ import annotations

from edify import Pattern

numeric = Pattern().start_of_input().one_or_more().digit().end_of_input()
"""Callable :class:`Pattern` for a digits-only string."""
