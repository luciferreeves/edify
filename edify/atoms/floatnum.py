"""``floatnum`` — general floating-point number (integer, decimal, or scientific)."""

from __future__ import annotations

from edify import Pattern

floatnum = (
    Pattern()
    .optional()
    .any_of_chars("+-")
    .one_or_more()
    .digit()
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
    .optional()
    .group()
    .any_of_chars("eE")
    .optional()
    .any_of_chars("+-")
    .one_or_more()
    .digit()
    .end()
)
"""Composable :class:`Pattern` fragment for a general floating-point number."""
