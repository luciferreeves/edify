"""``ipv4_octet`` — one IPv4 octet in the range ``0``-``255``."""

from __future__ import annotations

from edify import Pattern, any_of

ipv4_octet = any_of(
    Pattern().string("25").range("0", "5"),
    Pattern().char("2").range("0", "4").digit(),
    Pattern().char("1").digit().digit(),
    Pattern().range("1", "9").digit(),
    Pattern().digit(),
)
"""Composable :class:`Pattern` fragment for a single IPv4 octet (``0``-``255``)."""
