"""``issn`` — ISSN shape (``NNNN-NNNC``)."""

from __future__ import annotations

from edify import Pattern

issn = (
    Pattern()
    .start_of_input()
    .exactly(4)
    .digit()
    .char("-")
    .exactly(3)
    .digit()
    .any_of()
    .digit()
    .char("X")
    .char("x")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the ISSN shape."""
