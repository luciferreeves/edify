"""``sortcode`` — UK sort-code shape (``NN-NN-NN`` or 6 digits)."""

from __future__ import annotations

from edify import Pattern, any_of

_dashed = (
    Pattern()
    .start_of_input()
    .exactly(2)
    .digit()
    .char("-")
    .exactly(2)
    .digit()
    .char("-")
    .exactly(2)
    .digit()
    .end_of_input()
)
_solid = Pattern().start_of_input().exactly(6).digit().end_of_input()

sortcode = any_of(_dashed, _solid)
"""Callable :class:`Pattern` for a UK sort code."""
