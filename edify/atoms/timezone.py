"""``timezone`` — UTC offset (``Z`` or ``±HH[:]MM``)."""

from __future__ import annotations

from edify import Pattern, any_of

timezone = any_of(
    Pattern().char("Z"),
    Pattern().any_of_chars("+-").exactly(2).digit().optional().char(":").exactly(2).digit(),
)
"""Composable :class:`Pattern` fragment for a timezone offset."""
