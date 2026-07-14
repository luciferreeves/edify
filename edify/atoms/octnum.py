"""``octnum`` — octal integer literal (``0o`` or ``0O`` prefix)."""

from __future__ import annotations

from edify import Pattern

octnum = Pattern().char("0").any_of_chars("oO").one_or_more().range("0", "7")
"""Composable :class:`Pattern` fragment for a ``0oNN``-shaped octal literal."""
