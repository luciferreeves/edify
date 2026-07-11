"""``imo`` — International Maritime Organization vessel identifier ``IMO NNNNNNN``."""

from __future__ import annotations

from edify import Pattern

imo = Pattern().start_of_input().string("IMO").exactly(7).digit().end_of_input()
"""Callable :class:`Pattern` for the IMO ship-number shape: literal
``IMO`` followed by 7 digits.
"""
