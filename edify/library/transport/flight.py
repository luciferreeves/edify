"""``flight`` — flight-number shape (2-letter airline + 1-4 digits, optional suffix)."""

from __future__ import annotations

from edify import Pattern

flight = (
    Pattern()
    .start_of_input()
    .exactly(2)
    .uppercase()
    .between(1, 4)
    .digit()
    .optional()
    .uppercase()
    .end_of_input()
)
"""Callable :class:`Pattern` for an IATA/ICAO flight-number shape."""
