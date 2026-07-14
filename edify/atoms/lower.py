"""``lower`` — a single lowercase ASCII letter."""

from __future__ import annotations

from edify import Pattern

lower = Pattern().lowercase()
"""Composable :class:`Pattern` fragment for one lowercase letter ``[a-z]``."""
