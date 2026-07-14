"""``port_number`` — one TCP/UDP port in the range ``0``-``65535``."""

from __future__ import annotations

from edify import Pattern, any_of

port_number = any_of(
    Pattern().string("6553").range("0", "5"),
    Pattern().string("655").range("0", "2").digit(),
    Pattern().string("65").range("0", "4").digit().digit(),
    Pattern().char("6").range("0", "4").digit().digit().digit(),
    Pattern().range("1", "5").exactly(4).digit(),
    Pattern().range("1", "9").between(0, 3).digit(),
    Pattern().char("0"),
)
"""Composable :class:`Pattern` fragment for a TCP/UDP port number."""
