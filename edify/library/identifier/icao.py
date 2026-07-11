"""``icao`` — ICAO airline (3 letters) or airport (4 letters) code."""

from __future__ import annotations

from edify import Pattern

icao = Pattern().start_of_input().between(3, 4).any_of().range("A", "Z").end().end_of_input()
"""Callable :class:`Pattern` for the ICAO code shape: 3 uppercase letters
(airline) or 4 uppercase letters (airport).
"""
