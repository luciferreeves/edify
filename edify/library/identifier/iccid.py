"""``iccid`` — 19-22 digit Integrated Circuit Card Identifier."""

from __future__ import annotations

from edify import Pattern

iccid = Pattern().start_of_input().between(19, 22).digit().end_of_input()
"""Callable :class:`Pattern` for the ICCID shape: 19 to 22 decimal digits."""
