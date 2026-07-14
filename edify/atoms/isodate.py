"""``isodate`` — ISO 8601 calendar date ``YYYY-MM-DD``."""

from __future__ import annotations

from edify import Pattern

isodate = Pattern().exactly(4).digit().char("-").exactly(2).digit().char("-").exactly(2).digit()
"""Composable :class:`Pattern` fragment for an ISO 8601 ``YYYY-MM-DD`` date."""
