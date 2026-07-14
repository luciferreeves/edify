"""``clock12`` — 12-hour clock time with AM/PM."""

from __future__ import annotations

from edify import Pattern

clock12 = (
    Pattern()
    .any_of()
    .subexpression(Pattern().char("1").range("0", "2"))
    .subexpression(Pattern().optional().char("0").range("1", "9"))
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
    .optional()
    .whitespace_char()
    .any_of_chars("AaPp")
    .any_of_chars("Mm")
)
"""Composable :class:`Pattern` fragment for a 12-hour clock time with AM/PM."""
