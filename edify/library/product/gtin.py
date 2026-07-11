"""``gtin`` — GTIN barcode number (8/12/13/14 digits, includes UPC and EAN)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

gtin = RegexBackedPattern(r"^\d{8}$|^\d{12}$|^\d{13}$|^\d{14}$")
"""Callable :class:`Pattern` for the GTIN family: 8-, 12-, 13-, or 14-digit barcode number."""
