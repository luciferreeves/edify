"""``brackets`` — a square-bracket group with no nested brackets."""

from __future__ import annotations

from edify import Pattern

brackets = Pattern().char("[").zero_or_more().anything_but_chars("]").char("]")
"""Composable :class:`Pattern` fragment for a ``[...]`` group."""
