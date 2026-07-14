"""``day`` — two-digit day-of-month (``01``-``31``)."""

from __future__ import annotations

from edify import Pattern, any_of

day = any_of(
    Pattern().char("0").range("1", "9"),
    Pattern().range("1", "2").digit(),
    Pattern().char("3").range("0", "1"),
)
"""Composable :class:`Pattern` fragment for a two-digit day-of-month."""
