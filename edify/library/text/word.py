"""``word`` — word-character string shape."""

from __future__ import annotations

from edify import Pattern

word = (
    Pattern()
    .start_of_input()
    .one_or_more()
    .word()
    .end_of_input()
)
"""Callable :class:`Pattern` for a word-character string:
letters, digits, and underscore.
"""
