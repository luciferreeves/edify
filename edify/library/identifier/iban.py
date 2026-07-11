"""``iban`` — International Bank Account Number shape (2 letter country + 2 check digits + up to 30 alphanumerics)."""

from __future__ import annotations

from edify import Pattern

iban = (
    Pattern()
    .start_of_input()
    .exactly(2).any_of().range("A", "Z").end()
    .exactly(2).digit()
    .between(1, 30).any_of().range("A", "Z").range("0", "9").end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the IBAN shape: 2-letter ISO country code +
2 check digits + 1–30 uppercase-alphanumeric BBAN characters.
"""
