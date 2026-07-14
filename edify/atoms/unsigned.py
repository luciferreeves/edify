"""``unsigned`` — unsigned decimal integer (one or more digits)."""

from __future__ import annotations

from edify import Pattern

unsigned = Pattern().one_or_more().digit()
"""Composable :class:`Pattern` fragment for an unsigned integer."""
