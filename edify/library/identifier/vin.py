"""``vin`` — 17-character Vehicle Identification Number (no I, O, Q)."""

from __future__ import annotations

from edify import Pattern

vin = (
    Pattern()
    .start_of_input()
    .exactly(17)
    .any_of()
    .range("A", "H")
    .range("J", "N")
    .char("P")
    .range("R", "Z")
    .range("0", "9")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the ISO 3779 VIN shape: 17 uppercase-alphanumeric
characters excluding ``I``, ``O``, and ``Q``.
"""
