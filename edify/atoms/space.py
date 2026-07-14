"""``space`` — a single whitespace character."""

from __future__ import annotations

from edify import Pattern

space = Pattern().whitespace_char()
"""Composable :class:`Pattern` fragment for one whitespace character."""
