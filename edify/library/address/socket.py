"""``socket`` — ``host:port`` socket address shape."""

from __future__ import annotations

from edify import Pattern, any_of
from edify.library._support.atoms import octet

_ipv4 = Pattern().subexpression(octet).exactly(3).group().char(".").subexpression(octet).end()
_ipv6_bracket = (
    Pattern()
    .char("[")
    .one_or_more()
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .range("A", "F")
    .char(":")
    .end()
    .char("]")
)
_hostname_label = (
    Pattern()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .end()
    .optional()
    .group()
    .between(0, 61)
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .char("-")
    .end()
    .any_of()
    .range("a", "z")
    .range("A", "Z")
    .range("0", "9")
    .end()
    .end()
)
_hostname = (
    Pattern()
    .subexpression(_hostname_label)
    .zero_or_more()
    .group()
    .char(".")
    .subexpression(_hostname_label)
    .end()
)

socket = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_ipv4, _ipv6_bracket, _hostname))
    .char(":")
    .between(1, 5)
    .digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for the ``host:port`` socket-address shape."""
