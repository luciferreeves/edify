"""``isbn`` — ISBN-10 or ISBN-13 shape (with or without dashes)."""

from __future__ import annotations

from edify import Pattern, any_of

_isbn10 = (
    Pattern()
    .start_of_input()
    .exactly(9)
    .group()
    .digit()
    .optional()
    .any_of_chars("- ")
    .end()
    .any_of()
    .digit()
    .char("X")
    .char("x")
    .end()
    .end_of_input()
)
_isbn13 = (
    Pattern()
    .start_of_input()
    .exactly(12)
    .group()
    .digit()
    .optional()
    .any_of_chars("- ")
    .end()
    .digit()
    .end_of_input()
)

isbn = any_of(_isbn10, _isbn13)
"""Callable :class:`Pattern` for ISBN-10 or ISBN-13 shape."""
