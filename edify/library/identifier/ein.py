"""``ein`` — US Employer Identification Number ``XX-XXXXXXX`` shape."""

from __future__ import annotations

from edify import Pattern

ein = (
    Pattern()
    .start_of_input()
    .exactly(2).digit()
    .char("-")
    .exactly(7).digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for the US EIN ``XX-XXXXXXX`` shape."""