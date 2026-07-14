"""``ratio`` — colon-separated ratio (``N:M``)."""

from __future__ import annotations

from edify import Pattern

ratio = Pattern().one_or_more().digit().char(":").one_or_more().digit()
"""Composable :class:`Pattern` fragment for a ratio value."""
