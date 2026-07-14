"""``decimal`` — decimal number with a fractional part (``N.M``)."""

from __future__ import annotations

from edify import Pattern

decimal = Pattern().one_or_more().digit().char(".").one_or_more().digit()
"""Composable :class:`Pattern` fragment for a decimal number ``digits.digits``."""
