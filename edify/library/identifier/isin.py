"""``isin`` — International Securities Identification Number (12-char)."""

from __future__ import annotations

from edify import Pattern

isin = (
    Pattern()
    .start_of_input()
    .exactly(2).any_of().range("A", "Z").end()
    .exactly(9).any_of().range("A", "Z").range("0", "9").end()
    .digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for the ISO 6166 ISIN shape: 2-letter country
code + 9 alphanumeric identifier characters + 1 check digit.
"""
