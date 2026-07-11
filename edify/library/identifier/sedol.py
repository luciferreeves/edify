"""``sedol`` — 7-character SEDOL securities identifier."""

from __future__ import annotations

from edify import Pattern

sedol = (
    Pattern()
    .start_of_input()
    .exactly(6).any_of().range("B", "D").range("F", "H").range("J", "N")
    .range("P", "T").range("V", "X").range("Y", "Z").range("0", "9").end()
    .digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for the 7-character SEDOL shape:
6 body characters (consonants + digits, excluding vowels) + 1 check digit.
"""
