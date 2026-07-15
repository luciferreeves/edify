"""``zip_code`` — US postal-code shape (5 digits, optionally + 4)."""

from __future__ import annotations

from edify import Pattern

zip_code = (
    Pattern()
    .start_of_input()
    .exactly(5)
    .digit()
    .optional()
    .group()
    .char("-")
    .exactly(4)
    .digit()
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the US ZIP or ZIP+4 postal-code shape.

Guarantees:
    * Five decimal digits, optionally followed by ``-`` and four more decimal digits.
    * Anchored at both ends.

Does not guarantee:
    * Postal-service validity — accepts every 5- and 5+4-digit string, including
      unassigned or reserved ranges.
    * Non-US postal codes — those live under a country-specific validator.
"""
