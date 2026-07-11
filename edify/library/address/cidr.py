"""``cidr`` — CIDR-notation subnet ``address/prefix`` shape."""

from __future__ import annotations

from edify import Pattern, any_of

_ipv4_octet = any_of(
    Pattern().string("25").any_of().range("0", "5").end(),
    Pattern().char("2").any_of().range("0", "4").end().digit(),
    Pattern().char("1").digit().digit(),
    Pattern().any_of().range("1", "9").end().digit(),
    Pattern().digit(),
)

_ipv4_prefix = any_of(
    Pattern().char("3").any_of().range("0", "2").end(),
    Pattern().optional().any_of_chars("12").digit(),
)

_hextet = (
    Pattern()
    .between(1, 4)
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .range("A", "F")
    .end()
)

_ipv6_prefix = any_of(
    Pattern().string("12").any_of().range("0", "8").end(),
    Pattern().char("1").any_of_chars("01").digit(),
    Pattern().optional().any_of().range("1", "9").end().digit(),
)

_ipv4_cidr = (
    Pattern()
    .subexpression(_ipv4_octet)
    .exactly(3)
    .group()
    .char(".")
    .subexpression(_ipv4_octet)
    .end()
    .char("/")
    .subexpression(_ipv4_prefix)
)

_ipv6_cidr = (
    Pattern()
    .between(0, 7)
    .group()
    .subexpression(_hextet)
    .char(":")
    .end()
    .subexpression(_hextet)
    .char("/")
    .subexpression(_ipv6_prefix)
)

cidr = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_ipv4_cidr, _ipv6_cidr))
    .end_of_input()
)
"""Callable :class:`Pattern` for CIDR notation: IPv4 address + ``/0``-``/32``
or IPv6 address + ``/0``-``/128``.
"""
