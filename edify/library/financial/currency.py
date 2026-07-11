"""``currency`` — ISO 4217 currency-code shape (3 uppercase letters)."""

from __future__ import annotations

from edify import Pattern

currency = Pattern().start_of_input().exactly(3).any_of().range("A", "Z").end().end_of_input()
"""Callable :class:`Pattern` for the ISO 4217 currency-code shape:
3 uppercase letters (``USD``, ``EUR``, ``JPY``, …).
"""
