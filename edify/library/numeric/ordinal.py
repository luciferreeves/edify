"""``ordinal`` — English ordinal-number shape (``1st``, ``2nd``, ``3rd``, ``4th``, ...)."""

from __future__ import annotations

from edify import Pattern

ordinal = (
    Pattern()
    .start_of_input()
    .one_or_more()
    .digit()
    .group()
    .any_of()
    .string("st")
    .string("nd")
    .string("rd")
    .string("th")
    .end()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for an English ordinal number."""
