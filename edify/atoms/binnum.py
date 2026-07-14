"""``binnum`` — binary integer literal (``0b`` or ``0B`` prefix)."""

from __future__ import annotations

from edify import Pattern

binnum = Pattern().char("0").any_of_chars("bB").one_or_more().any_of_chars("01")
"""Composable :class:`Pattern` fragment for a ``0bNN``-shaped binary literal."""
