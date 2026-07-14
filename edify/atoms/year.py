"""``year`` — four-digit calendar year."""

from __future__ import annotations

from edify import Pattern

year = Pattern().exactly(4).digit()
"""Composable :class:`Pattern` fragment for a four-digit calendar year."""
