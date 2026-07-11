"""``iata`` — IATA airline (2 letters) or airport (3 letters) code."""

from __future__ import annotations

from edify import Pattern

iata = Pattern().start_of_input().between(2, 3).any_of().range("A", "Z").end().end_of_input()
"""Callable :class:`Pattern` for the IATA code shape: 2 uppercase letters
(airline) or 3 uppercase letters (airport).
"""
