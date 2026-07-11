"""``mpn`` — Manufacturer Part Number (permissive alphanumeric)."""

from __future__ import annotations

from edify import Pattern

mpn = (
    Pattern()
    .start_of_input()
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
    .between(1, 63)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .char("-")
    .char("_")
    .char(".")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a permissive Manufacturer Part Number."""
