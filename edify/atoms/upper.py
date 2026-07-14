"""``upper`` — a single uppercase ASCII letter."""

from __future__ import annotations

from edify import Pattern

upper = Pattern().uppercase()
"""Composable :class:`Pattern` fragment for one uppercase letter ``[A-Z]``."""
