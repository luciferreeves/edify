"""``creditcard`` — 13-to-19 digit credit-card number (no Luhn check)."""

from __future__ import annotations

from edify import Pattern

creditcard = Pattern().between(13, 19).digit()
"""Composable :class:`Pattern` fragment for a credit-card number shape."""
