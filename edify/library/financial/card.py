"""``card`` — credit-card number shape (13-19 digits, optional dash/space separators)."""

from __future__ import annotations

from edify import Pattern

card = (
    Pattern()
    .start_of_input()
    .exactly(4)
    .digit()
    .optional()
    .any_of_chars("- ")
    .exactly(4)
    .digit()
    .optional()
    .any_of_chars("- ")
    .exactly(4)
    .digit()
    .optional()
    .any_of_chars("- ")
    .between(1, 7)
    .digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for credit-card number shape:
groups of 4 digits with optional dash/space separators, 13-19 digits total.
"""
