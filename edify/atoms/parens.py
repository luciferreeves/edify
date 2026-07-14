"""``parens`` — a parenthesised group with no nested parentheses."""

from __future__ import annotations

from edify import Pattern

parens = Pattern().char("(").zero_or_more().anything_but_chars(")").char(")")
"""Composable :class:`Pattern` fragment for a ``(...)`` group."""
