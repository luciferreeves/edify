"""``scientific`` — number in scientific notation (``N[.N]e[±]N``)."""

from __future__ import annotations

from edify import Pattern

scientific = (
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
    .any_of_chars("eE")
    .optional()
    .any_of_chars("+-")
    .one_or_more()
    .digit()
)
"""Composable :class:`Pattern` fragment for a number in scientific notation."""
