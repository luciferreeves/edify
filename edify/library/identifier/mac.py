"""``mac`` — IEEE 802 MAC-address 6-octet hex shape (callable :class:`Pattern`)."""

from __future__ import annotations

from edify import Pattern

mac = (
    Pattern()
    .start_of_input()
    .exactly(5)
    .group()
    .exactly(2)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .range("A", "F")
    .end()
    .any_of_chars(":-")
    .end()
    .exactly(2)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .range("A", "F")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the IEEE 802 MAC-address shape.

Guarantees:
    * Six 2-hex-digit octets separated by ``:`` or ``-``.
    * Either case is accepted.
    * Separator is uniform: mixed ``:`` and ``-`` in the same address is rejected.
    * Anchored at both ends.

Does not guarantee:
    * OUI or IANA-assignment validity — every syntactically-valid octet passes.
    * Dot-separated Cisco-style ``0000.5e00.53af``, bare 12-hex-digit ``00005e0053af``,
      or EUI-64 8-octet ``00:00:5e:ff:fe:00:53:af`` — those forms require dedicated
      validators.
"""
