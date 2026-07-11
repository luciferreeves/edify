"""``uri`` — generic URI shape (scheme + path)."""

from __future__ import annotations

from edify import Pattern

uri = (
    Pattern()
    .start_of_input()
    .letter()
    .zero_or_more()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("+")
    .char(".")
    .char("-")
    .end()
    .char(":")
    .one_or_more()
    .non_whitespace_char()
    .end_of_input()
)
"""Callable :class:`Pattern` for the generic URI shape:
``scheme:opaque-or-path`` where scheme starts with a letter.
"""
