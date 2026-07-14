"""``epoch`` — Unix epoch seconds (10-digit timestamp)."""

from __future__ import annotations

from edify import Pattern

epoch = Pattern().exactly(10).digit()
"""Composable :class:`Pattern` fragment for a 10-digit Unix epoch timestamp."""
