"""``vat`` — VAT identification number shape (country prefix + digits)."""

from __future__ import annotations

from edify import Pattern

vat = Pattern().start_of_input().exactly(2).uppercase().between(6, 12).digit().end_of_input()
"""Callable :class:`Pattern` for a VAT identification number."""
