"""``iban`` — International Bank Account Number shape."""

from __future__ import annotations

from edify import Pattern

iban = (
    Pattern()
    .exactly(2)
    .uppercase()
    .exactly(2)
    .digit()
    .between(11, 30)
    .any_of()
    .range("A", "Z")
    .range("0", "9")
    .end()
)
"""Composable :class:`Pattern` fragment for an IBAN."""
