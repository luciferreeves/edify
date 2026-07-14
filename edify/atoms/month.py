"""``month`` — two-digit calendar month (``01``-``12``)."""

from __future__ import annotations

from edify import Pattern, any_of

month = any_of(
    Pattern().char("0").range("1", "9"),
    Pattern().char("1").range("0", "2"),
)
"""Composable :class:`Pattern` fragment for a two-digit calendar month."""
