"""``alpha`` — letters-only string shape."""

from __future__ import annotations

from edify import Pattern

alpha = Pattern().start_of_input().one_or_more().letter().end_of_input()
"""Callable :class:`Pattern` for a letters-only string."""
