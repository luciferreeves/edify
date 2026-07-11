"""``gtin`` — GTIN barcode number (8/12/13/14 digits, includes UPC and EAN)."""

from __future__ import annotations

from edify import Pattern, any_of

gtin = (
    Pattern()
    .start_of_input()
    .subexpression(
        any_of(
            Pattern().exactly(8).digit(),
            Pattern().exactly(12).digit(),
            Pattern().exactly(13).digit(),
            Pattern().exactly(14).digit(),
        )
    )
    .end_of_input()
)
"""Callable :class:`Pattern` for the GTIN family: 8-, 12-, 13-, or 14-digit barcode number."""
