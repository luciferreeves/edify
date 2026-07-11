"""``address`` — permissive street-address shape."""

from __future__ import annotations

from edify import Pattern

address = (
    Pattern()
    .start_of_input()
    .one_or_more()
    .digit()
    .one_or_more()
    .whitespace_char()
    .one_or_more()
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .whitespace_char()
    .any_of_chars(".,'-#/")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a permissive street-address shape:
one or more digits followed by whitespace and address body characters.
"""
