"""``roman`` — Roman-numeral shape (1-3999)."""

from __future__ import annotations

from edify import Pattern

roman = (
    Pattern()
    .start_of_input()
    .between(0, 3)
    .char("M")
    .group()
    .any_of()
    .string("CM")
    .string("CD")
    .subexpression(Pattern().optional().char("D").between(0, 3).char("C"))
    .end()
    .end()
    .group()
    .any_of()
    .string("XC")
    .string("XL")
    .subexpression(Pattern().optional().char("L").between(0, 3).char("X"))
    .end()
    .end()
    .group()
    .any_of()
    .string("IX")
    .string("IV")
    .subexpression(Pattern().optional().char("V").between(0, 3).char("I"))
    .end()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a Roman-numeral value 1-3999."""
