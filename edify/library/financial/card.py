"""``card`` — credit-card number shape (13–19 digits, optional dash/space separators)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

card = RegexBackedPattern(r"^\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{1,7}$")
"""Callable :class:`Pattern` for credit-card number shape:
groups of 4 digits with optional dash/space separators, 13–19 digits total.
"""
