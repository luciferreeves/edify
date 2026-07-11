"""``offset`` — UTC offset shape (``±HH:MM`` or ``Z``)."""

from __future__ import annotations

from edify import Pattern, any_of

_hh = any_of(
    Pattern().char("0").digit(),
    Pattern().char("1").range("0", "4"),
)

offset = (
    Pattern()
    .start_of_input()
    .any_of()
    .char("Z")
    .subexpression(
        Pattern()
        .any_of_chars("+-")
        .subexpression(_hh)
        .optional().char(":")
        .range("0", "5").digit()
    )
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the UTC-offset shape: ``Z`` for UTC or
``±HH:MM`` / ``±HHMM`` with range ``-14:00`` to ``+14:00``.
"""
