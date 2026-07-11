"""``fraction`` — fraction shape (``A/B`` or mixed ``N A/B``)."""

from __future__ import annotations

from edify import Pattern

fraction = (
    Pattern()
    .start_of_input()
    .optional()
    .char("-")
    .optional()
    .group()
    .one_or_more()
    .digit()
    .one_or_more()
    .whitespace_char()
    .end()
    .one_or_more()
    .digit()
    .char("/")
    .one_or_more()
    .digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for a fraction shape:
``numerator/denominator`` with optional whole-number prefix.
"""
