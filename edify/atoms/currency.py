"""``currency`` — three-letter ISO 4217 currency code."""

from __future__ import annotations

from edify import Pattern

currency = Pattern().exactly(3).uppercase()
"""Composable :class:`Pattern` fragment for an ISO 4217 currency code."""
