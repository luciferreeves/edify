"""``word`` — one or more word characters (``\\w+``)."""

from __future__ import annotations

from edify import Pattern

word = Pattern().one_or_more().word()
"""Composable :class:`Pattern` fragment for a run of word characters."""
