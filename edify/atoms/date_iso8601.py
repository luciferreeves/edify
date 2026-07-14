"""``date_iso8601`` — ISO 8601 calendar date ``YYYY-MM-DD``."""

from __future__ import annotations

from edify import Pattern

date_iso8601 = (
    Pattern().exactly(4).digit().char("-").exactly(2).digit().char("-").exactly(2).digit()
)
"""Composable :class:`Pattern` fragment for an ISO 8601 ``YYYY-MM-DD`` date."""
