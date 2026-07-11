"""``routing`` — US ABA routing-number shape (9 digits)."""

from __future__ import annotations

from edify import Pattern

routing = Pattern().start_of_input().exactly(9).digit().end_of_input()
"""Callable :class:`Pattern` for a US ABA routing number (9 digits)."""
