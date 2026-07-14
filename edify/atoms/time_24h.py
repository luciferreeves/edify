"""``time_24h`` — 24-hour ``HH:MM[:SS]`` clock time."""

from __future__ import annotations

from edify import Pattern

time_24h = (
    Pattern()
    .any_of()
    .subexpression(Pattern().char("2").range("0", "3"))
    .subexpression(Pattern().range("0", "1").digit())
    .end()
    .char(":")
    .range("0", "5")
    .digit()
    .optional()
    .group()
    .char(":")
    .range("0", "5")
    .digit()
    .end()
)
"""Composable :class:`Pattern` fragment for a 24-hour clock time."""
