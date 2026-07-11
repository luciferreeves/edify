"""``alphanumeric`` — letters-and-digits-only string shape."""

from __future__ import annotations

from edify import Pattern

alphanumeric = Pattern().start_of_input().one_or_more().alphanumeric().end_of_input()
"""Callable :class:`Pattern` for a letters-and-digits-only string."""
