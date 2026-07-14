"""``natural`` — natural number (positive integer, no leading zero)."""

from __future__ import annotations

from edify import Pattern

natural = Pattern().range("1", "9").zero_or_more().digit()
"""Composable :class:`Pattern` fragment for a positive integer without a leading zero."""
