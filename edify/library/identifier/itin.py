"""``itin`` — US Individual Taxpayer Identification Number ``9XX-YY-ZZZZ`` shape."""

from __future__ import annotations

from edify import Pattern, any_of

_group_range = any_of(
    Pattern().char("5").digit(),
    Pattern().char("6").range("0", "5"),
    Pattern().char("7").digit(),
    Pattern().char("8").range("0", "8"),
    Pattern().char("9").range("0", "2"),
    Pattern().char("9").range("4", "9"),
)

itin = (
    Pattern()
    .start_of_input()
    .char("9")
    .exactly(2)
    .digit()
    .char("-")
    .subexpression(_group_range)
    .char("-")
    .exactly(4)
    .digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for the US ITIN ``9NN-YY-ZZZZ`` shape (area starts
with 9; group in ``50``-``65``, ``70``-``88``, ``90``-``92``, or ``94``-``99``).
"""

del _group_range
