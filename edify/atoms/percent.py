"""``percent`` — percentage value (``N[.N]%``)."""

from __future__ import annotations

from edify import Pattern

percent = (
    Pattern()
    .one_or_more()
    .digit()
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
    .char("%")
)
"""Composable :class:`Pattern` fragment for a percentage value."""
