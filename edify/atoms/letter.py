"""``letter`` — a single ASCII letter."""

from __future__ import annotations

from edify import Pattern

letter = Pattern().letter()
"""Composable :class:`Pattern` fragment for one ASCII letter ``[a-zA-Z]``."""
