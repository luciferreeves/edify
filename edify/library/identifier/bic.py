"""``bic`` — ISO 9362 BIC / SWIFT code shape (8 or 11 chars)."""

from __future__ import annotations

from edify import Pattern

bic = (
    Pattern()
    .start_of_input()
    .exactly(4)
    .any_of()
    .range("A", "Z")
    .end()
    .exactly(2)
    .any_of()
    .range("A", "Z")
    .end()
    .exactly(2)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
    .optional()
    .subexpression(Pattern().exactly(3).any_of().range("A", "Z").range("0", "9").end())
    .end_of_input()
)
"""Callable :class:`Pattern` for the ISO 9362 BIC/SWIFT shape:
4-letter bank code + 2-letter country + 2-alphanumeric location + optional
3-alphanumeric branch (8 or 11 characters total).
"""
