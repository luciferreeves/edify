"""``percentage`` — percentage value shape (number followed by ``%``)."""

from __future__ import annotations

from edify import Pattern

percentage = (
    Pattern()
    .start_of_input()
    .optional()
    .char("-")
    .one_or_more()
    .digit()
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
    .optional()
    .whitespace_char()
    .char("%")
    .end_of_input()
)
"""Callable :class:`Pattern` for a percentage value: signed number optionally
with a decimal part and a trailing ``%``.
"""
