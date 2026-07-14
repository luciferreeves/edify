"""``rgbcolor`` — CSS ``rgb()`` / ``rgba()`` colour value."""

from __future__ import annotations

from edify import Pattern

rgbcolor = (
    Pattern()
    .string("rgb")
    .optional()
    .char("a")
    .char("(")
    .zero_or_more()
    .whitespace_char()
    .one_or_more()
    .digit()
    .zero_or_more()
    .group()
    .char(",")
    .zero_or_more()
    .whitespace_char()
    .one_or_more()
    .digit()
    .end()
    .char(")")
)
"""Composable :class:`Pattern` fragment for a CSS ``rgb()``/``rgba()`` colour."""
